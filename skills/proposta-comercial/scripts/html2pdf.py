#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
html2pdf.py — Conversor HTML -> PDF para a skill "proposta-comercial".

Converte o deck HTML da proposta (sections com proporcao 2:1) em PDF usando
o Microsoft Edge, o Google Chrome ou o Chromium em modo headless. Encontra o
navegador sozinho em Windows, macOS, Linux e WSL (no WSL, usa um navegador
Linux se houver; senao, o Chrome/Edge do Windows via /mnt/c, convertendo os
caminhos com wslpath). Se nada for encontrado, use --browser.

Ajuste Academia Lendaria (2026-09-16): deteccao multiplataforma; o original
so procurava caminhos do Windows.

USO:
    python html2pdf.py <entrada.html> [saida.pdf] [opcoes]

ARGUMENTOS:
    entrada.html     Arquivo HTML da proposta (obrigatorio).
    saida.pdf        Caminho do PDF de saida. Padrao: mesmo nome da entrada
                     com extensao .pdf, na mesma pasta.

OPCOES:
    --check          Apos converter, valida o PDF: existencia, tamanho > 10KB
                     e numero de paginas do PDF == numero de <section> com
                     class contendo "page" no HTML.
    --dpi-scale N    Fator de escala de renderizacao (ex.: 2 para maior
                     nitidez de texto/imagens). Padrao: o do navegador.
    --browser CAMINHO
                     Caminho explicito para msedge.exe ou chrome.exe.
                     Se omitido, o script procura automaticamente.

EXEMPLOS:
    python html2pdf.py proposta-acme.html
    python html2pdf.py proposta-acme.html proposta-acme.pdf --check
    python html2pdf.py proposta.html --check --dpi-scale 2
    python html2pdf.py proposta.html --browser "C:/Program Files/Google/Chrome/Application/chrome.exe"

CODIGOS DE SAIDA:
    0  sucesso
    1  erro fatal (navegador nao encontrado, conversao falhou, PDF ausente)
    2  sucesso com avisos (ex.: --check encontrou divergencia de paginas)

FALLBACK MANUAL (se nenhum navegador for encontrado ou a conversao falhar):
    Abra o HTML no navegador, pressione Ctrl+P, escolha "Salvar como PDF",
    defina Margens: Nenhuma e ative "Graficos de fundo".
"""

import argparse
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

TIMEOUT_SEGUNDOS = 120
TAMANHO_MINIMO_PDF = 10 * 1024  # 10 KB

MSG_FALLBACK_MANUAL = (
    "Fallback manual: abra o arquivo HTML no navegador, pressione Ctrl+P,\n"
    "        escolha 'Salvar como PDF', defina Margens: Nenhuma e ative a opcao\n"
    "        'Graficos de fundo'. O resultado e identico ao deste script."
)


def eh_wsl():
    """True quando rodando dentro do Windows Subsystem for Linux."""
    if platform.system() != "Linux":
        return False
    try:
        return "microsoft" in Path("/proc/version").read_text(errors="ignore").lower()
    except OSError:
        return False


def eh_exe_windows(caminho):
    """True quando o navegador e um executavel do Windows acessado pelo WSL (/mnt/...)."""
    return eh_wsl() and str(caminho).lower().endswith(".exe")


def caminhos_windows(raiz=None):
    """Caminhos padrao de Edge e Chrome no Windows.

    Com raiz (ex.: Path('/mnt/c')), monta os mesmos caminhos vistos pelo WSL.
    """
    if raiz is None:
        program_files = Path(os.environ.get("ProgramFiles", r"C:\Program Files"))
        program_files_x86 = Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"))
        local_app_data = os.environ.get("LOCALAPPDATA", "")
        local_app_data = Path(local_app_data) if local_app_data else None
    else:
        program_files = raiz / "Program Files"
        program_files_x86 = raiz / "Program Files (x86)"
        local_app_data = None
        usuarios = raiz / "Users"
        if usuarios.is_dir():
            # Chrome instalado por usuario: C:\Users\<nome>\AppData\Local\Google\Chrome
            for pasta in usuarios.iterdir():
                candidato = pasta / "AppData" / "Local"
                if candidato.is_dir():
                    local_app_data = candidato
                    break

    candidatos = [
        # Microsoft Edge (presente por padrao no Windows 10/11)
        program_files_x86 / "Microsoft" / "Edge" / "Application" / "msedge.exe",
        program_files / "Microsoft" / "Edge" / "Application" / "msedge.exe",
        # Google Chrome
        program_files / "Google" / "Chrome" / "Application" / "chrome.exe",
        program_files_x86 / "Google" / "Chrome" / "Application" / "chrome.exe",
    ]
    if local_app_data:
        candidatos.append(local_app_data / "Google" / "Chrome" / "Application" / "chrome.exe")
    return candidatos


def caminhos_candidatos():
    """Retorna a lista ordenada de caminhos padrao do navegador para este sistema."""
    sistema = platform.system()
    if sistema == "Windows":
        return caminhos_windows()
    if sistema == "Darwin":
        apps = Path("/Applications")
        return [
            apps / "Google Chrome.app" / "Contents" / "MacOS" / "Google Chrome",
            apps / "Microsoft Edge.app" / "Contents" / "MacOS" / "Microsoft Edge",
            apps / "Chromium.app" / "Contents" / "MacOS" / "Chromium",
            Path.home() / "Applications" / "Google Chrome.app" / "Contents" / "MacOS" / "Google Chrome",
        ]
    # Linux (inclui WSL): navegadores nativos primeiro
    candidatos = [
        Path("/usr/bin/google-chrome"),
        Path("/usr/bin/google-chrome-stable"),
        Path("/opt/google/chrome/chrome"),
        Path("/usr/bin/microsoft-edge"),
        Path("/usr/bin/microsoft-edge-stable"),
        Path("/usr/bin/chromium"),
        Path("/usr/bin/chromium-browser"),
        Path("/snap/bin/chromium"),
    ]
    if eh_wsl():
        # Navegadores do Windows vistos pelo WSL (unidade C: montada em /mnt/c)
        candidatos += caminhos_windows(Path("/mnt/c"))
    return candidatos


NOMES_NO_PATH = (
    "msedge", "msedge.exe",
    "google-chrome", "google-chrome-stable", "chrome", "chrome.exe",
    "chromium", "chromium-browser",
    "microsoft-edge", "microsoft-edge-stable",
)


def localizar_navegador(caminho_explicito=None):
    """Localiza o executavel do navegador.

    Ordem: --browser explicito -> caminhos padrao do sistema (Edge/Chrome/
    Chromium; no WSL, nativos primeiro e depois os do Windows) -> busca no PATH.
    Retorna o caminho como string ou None se nada for encontrado.
    """
    if caminho_explicito:
        caminho = Path(caminho_explicito)
        if caminho.is_file():
            return str(caminho)
        print(f"[ERRO] Navegador informado em --browser nao existe: {caminho}")
        return None

    for candidato in caminhos_candidatos():
        if candidato.is_file():
            return str(candidato)

    # Ultimo recurso: busca no PATH (equivalente ao comando 'where'/'which')
    for nome in NOMES_NO_PATH:
        encontrado = shutil.which(nome)
        if encontrado:
            return encontrado

    return None


def caminho_para_navegador(caminho, navegador):
    """Converte um caminho local para o formato que o navegador entende.

    Quando o navegador e um .exe do Windows chamado a partir do WSL, os
    arquivos precisam ser referenciados com caminho Windows (wslpath -w).
    """
    caminho = Path(caminho).resolve()
    if not eh_exe_windows(navegador):
        return str(caminho)
    try:
        return subprocess.run(
            ["wslpath", "-w", str(caminho)], capture_output=True, text=True, check=True
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return str(caminho)


def contar_sections_page(html_texto):
    """Conta as tags <section ...> cujo atributo class contem 'page'.

    Comentarios HTML sao ignorados: o template traz exemplos de <section>
    dentro de comentarios de instrucao, que nao viram paginas no PDF.
    """
    html_texto = re.sub(r"<!--.*?-->", "", html_texto, flags=re.DOTALL)
    total = 0
    for tag in re.finditer(r"<section\b[^>]*>", html_texto, re.IGNORECASE):
        m = re.search(
            r"class\s*=\s*(?:\"([^\"]*)\"|'([^']*)')", tag.group(0), re.IGNORECASE
        )
        if m:
            classes = (m.group(1) or m.group(2) or "").lower()
            if "page" in classes:
                total += 1
    return total


def contar_paginas_pdf(caminho_pdf):
    """Conta as paginas do PDF.

    Usa pypdf se estiver instalado; caso contrario, conta as ocorrencias de
    '/Type /Page' (excluindo '/Type /Pages') no binario do arquivo.
    Retorna (numero_de_paginas, metodo_usado).
    """
    try:
        from pypdf import PdfReader

        return len(PdfReader(str(caminho_pdf)).pages), "pypdf"
    except ImportError:
        pass
    except Exception as exc:  # PDF corrompido ou ilegivel pelo pypdf
        print(f"[AVISO] pypdf nao conseguiu ler o PDF ({exc}); usando contagem binaria.")

    dados = Path(caminho_pdf).read_bytes()
    # \b garante que '/Type /Pages' (o no raiz da arvore) nao seja contado.
    paginas = len(re.findall(rb"/Type\s*/Page\b", dados))
    return paginas, "contagem binaria"


def executar_conversao(navegador, html_path, pdf_path, dpi_scale=None):
    """Roda o navegador em modo headless para imprimir o HTML em PDF.

    Retorna True em sucesso, False em falha (mensagens ja impressas).
    """
    if eh_exe_windows(navegador):
        # Navegador do Windows chamado pelo WSL: caminhos no formato Windows
        html_win = caminho_para_navegador(html_path, navegador)
        url = "file:///" + html_win.replace("\\", "/")
        destino_pdf = caminho_para_navegador(pdf_path, navegador)
    else:
        url = html_path.resolve().as_uri()  # file:///C:/... correto no Windows
        destino_pdf = str(pdf_path.resolve())
    comando = [
        navegador,
        "--headless",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--no-pdf-header-footer",
        f"--print-to-pdf={destino_pdf}",
    ]
    if dpi_scale:
        comando.append(f"--force-device-scale-factor={dpi_scale}")
    comando.append(url)

    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SEGUNDOS,
        )
    except subprocess.TimeoutExpired:
        print(f"[ERRO] A conversao excedeu o tempo limite de {TIMEOUT_SEGUNDOS}s.")
        print("        Verifique se o HTML nao depende de recursos externos lentos.")
        print(f"        {MSG_FALLBACK_MANUAL}")
        return False
    except OSError as exc:
        print(f"[ERRO] Falha ao executar o navegador: {exc}")
        print(f"        {MSG_FALLBACK_MANUAL}")
        return False

    if resultado.returncode != 0:
        print(f"[ERRO] O navegador retornou codigo {resultado.returncode}.")
        stderr = (resultado.stderr or "").strip()
        if stderr:
            # Mostra so as ultimas linhas para nao poluir o console.
            ultimas = "\n        ".join(stderr.splitlines()[-5:])
            print(f"        Saida de erro:\n        {ultimas}")
        print(f"        {MSG_FALLBACK_MANUAL}")
        return False

    return True


def validar_pdf(html_texto, pdf_path):
    """Validacoes do modo --check. Retorna lista de avisos (vazia = tudo OK)."""
    avisos = []

    tamanho = pdf_path.stat().st_size
    if tamanho <= TAMANHO_MINIMO_PDF:
        avisos.append(
            f"PDF muito pequeno ({tamanho} bytes, minimo esperado {TAMANHO_MINIMO_PDF}). "
            "O conteudo pode nao ter sido renderizado (pagina em branco?)."
        )
    else:
        print(f"[OK] Tamanho do PDF: {tamanho / 1024:.1f} KB (> 10 KB).")

    esperadas = contar_sections_page(html_texto)
    obtidas, metodo = contar_paginas_pdf(pdf_path)
    print(f"[OK] Contagem de paginas via {metodo}: {obtidas} pagina(s) no PDF.")

    if esperadas == 0:
        avisos.append(
            "Nenhuma <section> com class contendo 'page' foi encontrada no HTML. "
            "Confirme se o deck segue o padrao <section class=\"page ...\">."
        )
    elif obtidas != esperadas:
        avisos.append(
            f"Divergencia de paginas: HTML tem {esperadas} section(s) '.page', "
            f"mas o PDF tem {obtidas} pagina(s). Causas provaveis: "
            "(1) CSS @page { size: 338.67mm 169.33mm; margin: 0 } ausente ou incorreto; "
            "(2) conteudo vazando alem da altura da pagina e criando paginas extras; "
            "(3) page-break-after ausente entre as sections."
        )
    else:
        print(
            f"[OK] Numero de paginas confere: {obtidas} pagina(s) no PDF == "
            f"{esperadas} section(s) '.page' no HTML."
        )

    return avisos


def main():
    parser = argparse.ArgumentParser(
        prog="html2pdf.py",
        description="Converte o HTML da proposta comercial em PDF via Edge/Chrome headless.",
        epilog="Codigos de saida: 0 = sucesso, 1 = erro fatal, 2 = sucesso com avisos.",
    )
    parser.add_argument("entrada", help="arquivo HTML de entrada")
    parser.add_argument(
        "saida",
        nargs="?",
        default=None,
        help="arquivo PDF de saida (padrao: mesmo nome da entrada, extensao .pdf)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="valida o PDF gerado (tamanho e numero de paginas vs sections do HTML)",
    )
    parser.add_argument(
        "--dpi-scale",
        type=float,
        default=None,
        metavar="N",
        help="fator de escala de renderizacao (ex.: 2)",
    )
    parser.add_argument(
        "--browser",
        default=None,
        metavar="CAMINHO",
        help="caminho explicito para msedge.exe ou chrome.exe",
    )
    args = parser.parse_args()

    html_path = Path(args.entrada)
    if not html_path.is_file():
        print(f"[ERRO] Arquivo HTML nao encontrado: {html_path}")
        return 1
    if html_path.suffix.lower() not in (".html", ".htm"):
        print(f"[AVISO] A entrada nao tem extensao .html/.htm: {html_path.name}")

    pdf_path = Path(args.saida) if args.saida else html_path.with_suffix(".pdf")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    navegador = localizar_navegador(args.browser)
    if not navegador:
        print("[ERRO] Nenhum navegador compativel encontrado (Microsoft Edge ou Google Chrome).")
        print("        Caminhos verificados:")
        for candidato in caminhos_candidatos():
            print(f"        - {candidato}")
        print(f"        Tambem foi feita busca no PATH por {', '.join(NOMES_NO_PATH)}, sem sucesso.")
        print("        Opcoes: (1) informe o caminho com --browser CAMINHO;")
        print(f"        (2) {MSG_FALLBACK_MANUAL}")
        return 1

    print(f"[OK] Navegador: {navegador}")
    print(f"[OK] Entrada:   {html_path.resolve()}")
    print(f"[OK] Saida:     {pdf_path.resolve()}")

    if not executar_conversao(navegador, html_path, pdf_path, args.dpi_scale):
        return 1

    if not pdf_path.is_file():
        print("[ERRO] O navegador terminou sem erro, mas o PDF nao foi criado.")
        print(f"        {MSG_FALLBACK_MANUAL}")
        return 1

    print(f"[OK] PDF gerado: {pdf_path.resolve()}")

    avisos = []
    if args.check:
        try:
            html_texto = html_path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"[ERRO] Nao foi possivel reler o HTML para validacao: {exc}")
            return 1
        avisos = validar_pdf(html_texto, pdf_path)
        for aviso in avisos:
            print(f"[AVISO] {aviso}")

    if avisos:
        print(f"[AVISO] Conversao concluida com {len(avisos)} aviso(s). Revise antes de enviar.")
        return 2

    print("[OK] Conversao concluida com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
