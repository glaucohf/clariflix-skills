# proposta-comercial · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

Esta skill exige ferramentas de execução para parte do procedimento. Anexar este arquivo a um chat não habilita essas ferramentas; confira os requisitos da skill antes de prometer o resultado.

---

---
name: proposta-comercial
description: "Cria propostas comerciais em HTML e PDF: extrai o briefing, adapta a identidade visual, organiza escopo e investimento e valida o deck antes da entrega."
version: 0.2.0
author: "Máquina de Receita · Gabriel Marcondes / Academia Lendária; adaptação ClariFlix"
license: LicenseRef-MaquinaDeReceita
platforms: [linux, macos, windows]
---

# Proposta Comercial — deck premium HTML → PDF

## Visão geral

Esta skill produz uma **proposta comercial em formato de deck 2:1** (páginas de
1280×640, como slides widescreen estendidos): um único arquivo
`proposta-<cliente>.html` self-contained (CSS inline, fontes com fallback, zero
dependências obrigatórias), revisado com o usuário no navegador e depois exportado
para **PDF paginado com fidelidade exata** (1 section = 1 página).

O design segue um sistema visual validado — neo-suíço, flat, preto/branco/cinza com
acento pontual na cor da marca, espaço em branco radical, divisórias dramáticas de uma
palavra ("Entregáveis.", "Cronograma.", "Investimento."). O arco narrativo apresenta
valor antes do preço: abertura → oferta → execução → comercial → fechamento.

**Para quem**: qualquer empresa ou profissional que venda serviços/projetos e precise
enviar propostas com aparência de agência de design — sem ter uma. A skill descobre o
negócio, o cliente e a oferta, e a marca do usuário entra por re-branding de tokens.

Tudo em pt-BR, salvo pedido explícito do usuário.

## When to Use

Use quando o usuário pedir uma proposta comercial, orçamento de serviços ou deck de proposta em HTML/PDF. Extraia primeiro os dados dos materiais já fornecidos. Não invente preços, prazos, condições ou provas sociais.

## Quick Reference

| Etapa | Recurso |
|---|---|
| Briefing | `references/descoberta.md` |
| Marca e layouts | `references/design-system.md` |
| Sumário e copy | `references/estrutura-narrativa.md` |
| Base do deck | `assets/template.html` |
| Exportação | `scripts/html2pdf.py` |
| Validação | `references/qa-checklist.md` |

Resolva esses caminhos a partir da **pasta instalada desta skill**, não do diretório atual do projeto. Para HTML, use um ambiente que possa criar arquivos. Para PDF automático, verifique Python 3.8+ e Edge, Chrome ou Chromium; não instale dependências automaticamente. O script usa a biblioteca padrão, com `pypdf` opcional para contar páginas. Sem navegador automatizável, ofereça a impressão manual descrita abaixo.

## Procedure

### Fluxo em 5 fases

Execute as fases em ordem. Cada fase indica o arquivo de referência a ler **naquele
momento** — não carregue todos de uma vez (mapa de recursos ao final).

### FASE 1 — Descoberta

1. Leia `references/descoberta.md` e execute o protocolo dele integralmente.
2. Inventarie os materiais fornecidos (mensagens, arquivos, URLs, transcrições de
   call) e **extraia primeiro, pergunte depois** — perguntar o que o material já
   responde queima a confiança do usuário.
3. Preencha os blocos A–F (quem vende, cliente, oferta, execução, comercial, extras).
   Entreviste apenas o que faltar, em grupos de no máximo 3–4 perguntas por mensagem.
4. **Nunca invente dados.** Preço, prazo, feature, nome, depoimento ou garantia que
   não veio do usuário não existe. Faltou? Pergunte.
5. Consolide o brief no formato do protocolo (com a soma comercial já conferida) e
   obtenha o "sim" explícito do usuário antes de seguir.

### FASE 2 — Configuração de marca

1. Leia a seção **"Protocolo de Adaptação de Marca"** (seção 4) de
   `references/design-system.md`.
2. Extraia a marca dos materiais: site (ferramenta de navegação disponível), logo SVG/PNG, brand guide (o brand
   guide tem prioridade). Sem materiais: entrevista mínima ou default monocromático —
   um default limpo vale mais que um acento inventado.
3. Monte o **brand-config**: bloco de tokens CSS com a cor da marca aplicada **apenas
   aos papéis de acento** (`--verde-toggle`, `--badge-texto`, derivados
   `--verde-icone-bg` ~12–15% de luminosidade e `--badge-bg` ~90%, `--acento-quente`).
   Fundos permanecem preto/branco/cinza — o estilo suíço é o produto.
4. Valide contraste WCAG AA nos contextos onde o acento carrega informação; clareie
   sobre fundo escuro / escureça sobre fundo claro conforme a seção 4c.
5. Registre no brand-config: fonte escolhida (Google Fonts + fallback), logo (arquivo
   ou monograma tipográfico), modo claro/escuro (dark-first inverte o ritmo, não o
   sistema) e, se o usuário pediu fuga do estilo suíço, o aviso dado e a confirmação.

### FASE 3 — Arquitetura de conteúdo

1. Leia `references/estrutura-narrativa.md` (arco, variantes e regras de mapeamento).
2. Escolha a variante — compacto (8–10 p.), padrão (12–16 p.) ou extenso (16–20 p.) —
   pelo tamanho da oferta. Na dúvida, a menor.
3. Aplique as regras de mapeamento brief → páginas: 1 produto = 1 página (6–8
   features), sumário de toggles com 2+ produtos, 4 sprints por página de cronograma,
   opcional só se houver upsell (e aparecendo exatamente 2x), soma da tabela = total.
4. Monte o **sumário de páginas** (lista numerada: nº, tipo de layout, conteúdo) e
   **apresente ao usuário para aprovação ANTES de gerar qualquer HTML**. Só avance
   após o "sim"; se ele ajustar, reexiba e confirme de novo.
5. Escreva a copy seguindo as diretrizes da seção 4 (bold-em-muted com 1–2 bolds por
   parágrafo, números concretos, divisórias de uma palavra com ponto final, zero
   clichês, zero exclamações, zero emojis).

### FASE 4 — Geração

1. **Copie** `assets/template.html` para o diretório de trabalho como
   `proposta-<cliente>.html` (nome do cliente em minúsculas, sem espaços). **Nunca
   edite o template original da skill** — ele é a matriz de todos os decks futuros.
2. No arquivo copiado: substitua os tokens do `:root` pelo brand-config; troque o
   `<symbol>` do logo pelo SVG da marca (instruções no próprio symbol); reescreva as
   sections conforme o sumário aprovado — duplique/remova/reordene as
   `<section class="page" data-layout="...">` (10 variantes de layout disponíveis).
3. Elimine TODO o conteúdo de exemplo ("Studio Vetor", "Café Aurora"): a proposta
   entregue não pode conter um único texto do template.
4. Consulte as especificações de layout (seção 3 de `references/design-system.md`)
   ao ajustar qualquer página — cada layout tem blocos "NÃO MEXER".
5. Abra o preview no navegador disponível no ambiente e itere com o
   usuário até ele aprovar. Texto que estoura um card é problema de copy: encurte o
   texto ou crie outra página — nunca reduza a fonte.

### FASE 5 — Exportação e QA

1. Exporte com validação:
   `python "<raiz-da-skill>/scripts/html2pdf.py" "<caminho-do-projeto>/proposta-<cliente>.html" --check`
   (exit 0 = ok; 2 = aviso de divergência de páginas; 1 = erro — ver Resolução de
   problemas). Use `--dpi-scale 2` se o usuário pedir mais nitidez.
2. Leia `references/qa-checklist.md` e rode o checklist COMPLETO (Técnica, Visual,
   Comercial). Itens comerciais em dúvida **bloqueiam a entrega** até o usuário
   responder.
3. Quando possível, renderize 2–3 páginas do PDF (capa, uma página de produto, a de
   investimento) e confira visualmente contra o HTML antes de entregar.
4. Reporte o resultado do QA ao usuário no formato compacto do checklist e entregue
   os caminhos do HTML e do PDF finais.

## Regras inegociáveis

- **Tudo em pt-BR** — skill, perguntas, copy do deck e mensagens — salvo pedido
  explícito do usuário por outro idioma.
- **Nunca inventar preço, prazo, feature, nome, depoimento ou garantia.** Tudo que
  aparece na proposta é rastreável ao brief confirmado. Lacuna = pergunta.
- **Sumário de páginas aprovado pelo usuário ANTES de gerar o HTML.** Sem exceção.
- **QA completo antes de entregar** (os 3 blocos do checklist), com resultado
  reportado. Divergência comercial (soma, multiplicadores "3x", promessas) para tudo
  até o usuário confirmar.
- **O template original da skill permanece intacto.** Trabalhe sempre numa cópia no
  diretório de trabalho do usuário.
- Fundos não recebem a cor da marca; acento não vira cor de corpo de texto; se o
  usuário pedir fuga do estilo suíço, avise uma vez, obtenha confirmação e registre.

## Pitfalls

### Resolução de problemas

| Problema | O que fazer |
|---|---|
| **Navegador não encontrado** (`html2pdf.py` exit 1) | Tente `--browser "C:/caminho/para/msedge.exe"` (ou chrome.exe). Se não houver navegador automatizável, instrua o fallback manual: abrir o HTML, Ctrl+P → Salvar como PDF → Margens: **Nenhuma** → ativar **"Gráficos de fundo"**. Resultado idêntico ao do script. |
| **Fontes não carregam** (sem internet / Google Fonts bloqueado) | Comportamento esperado: o `@import` falha em silêncio e o stack cai para `'Helvetica Neue', Helvetica, Arial`. O layout não quebra. Se o usuário exigir a fonte exata offline, embuta-a como `@font-face` com fonte em base64. |
| **`--check` acusa divergência de páginas** (exit 2) | Uma section está vazando conteúdo e criando página extra (ou uma section a menos/a mais no HTML). Confira: cada `<section class="page">` com a altura exata do template, `overflow: hidden` presente, `@page { margin: 0 }` intacto. Ache a página que estourou comparando PDF × HTML página a página. |
| **Texto vazando de card, badge ou tabela** | Reduza o CONTEÚDO, nunca a fonte: encurte a copy (features em até 2 linhas, bullets de 1 linha, máx. 4 sprints por página) ou mova o excedente para outra página. Encolher fonte para "caber" é bug de design. |
| **Fundos pretos/cinzas saem brancos no PDF** | Confirme `print-color-adjust: exact` no CSS (o template já traz); na exportação manual, "Gráficos de fundo" precisa estar marcado. |
| **Soma da tabela não bate com o total** | Nunca ajuste um número por conta própria. Multiplicadores ("3x R$ 40.000") podem ser quantidade ou parcelamento — pergunte ao usuário e só então corrija. |

## Mapa de recursos (progressive disclosure)

Leia cada arquivo apenas na fase indicada — não carregue tudo de uma vez.

| Arquivo | Quando ler |
|---|---|
| `references/descoberta.md` | Início da FASE 1 — protocolo de entrevista/extração dos blocos A–F e confirmação do brief. |
| `references/design-system.md` | FASE 2 (seção 4, adaptação de marca) e FASE 4 (seções 1–3 e 5–6: tokens, gramática visual, especificações dos 10 layouts, tipografia, anti-padrões). |
| `references/estrutura-narrativa.md` | Início da FASE 3 — arco de páginas, variantes de deck, mapeamento brief→páginas e diretrizes de copy. |
| `assets/template.html` | FASE 4 — copiar como base do deck (nunca editar o original). Cabeçalho do arquivo traz instruções de uso, re-branding e troca de logo. |
| `scripts/html2pdf.py` | FASE 5 — conversão HTML→PDF via Edge/Chrome headless; `--check` valida nº de páginas; `--help` documenta opções e fallback. |
| `references/qa-checklist.md` | FASE 5 — checklist obrigatório (Técnica/Visual/Comercial) e formato do reporte ao usuário. |

## Verification

- O briefing, o sumário e as decisões comerciais foram confirmados conforme o procedimento.
- Não restam nomes ou ofertas de exemplo do template; valores, quantidades e condições são rastreáveis ao briefing.
- O HTML abre com a marca correta, sem cortes de conteúdo; o template instalado permanece intacto.
- Quando PDF foi solicitado, o arquivo existe e a quantidade de páginas corresponde às sections; execute `--check` e informe o resultado real.
- O checklist técnico, visual e comercial foi aplicado. Entregue links para os arquivos e identifique qualquer pendência; não declare exportação concluída se apenas gerou HTML.

Proveniência e condições de uso: [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE).


## Referência: LICENSE

```text
LicenseRef-MaquinaDeReceita

Material de Gabriel Marcondes; montagem e revisão pela Academia Lendária.

Condição de origem preservada:
Material da turma, para uso próprio e nos seus projetos, sem republicação em canais abertos.

O mantenedor confirmou em 2026-09-18 possuir autorização dos autores para
publicação no ClariFlix. Isso não altera os direitos dos titulares nem torna
o conteúdo MIT. O pacote não inclui uma licença de redistribuição irrestrita.
Veja SOURCE.md para origem e adaptações.
```


## Referência: SOURCE.md

# Origem da proposta-comercial

Origem: `skill-proposta-comercial/` do [Máquina de Receita](https://github.com/educacional-lendario/maquina-de-receita), material de Gabriel Marcondes montado e revisado pela Academia Lendária.

Adaptação ClariFlix 0.2.0 em 2026-09-18: metadados e seções de catálogo, instruções de instalação multiplataforma, resolução de caminhos a partir da skill e verificação explícita. Template, quatro referências e exportador Python preservados integralmente. O tutorial foi adaptado ao catálogo ClariFlix.

O pacote original não declara licença própria; o README do material informa:

> Material da turma, para uso próprio e nos seus projetos, sem republicação em canais abertos.

O mantenedor confirmou em 2026-09-18 possuir autorização dos autores para disponibilizar este material no repositório público ClariFlix. A inclusão não transfere autoria nem altera a licença original. A licença MIT da infraestrutura do catálogo não se aplica automaticamente a este conteúdo. Consulte [LICENSE](LICENSE).


## Referência: TUTORIAL.md

# Proposta Comercial no ClariFlix

Instale o pacote completo para obter o template, as referências e o exportador:

```sh
npx skills add https://github.com/glaucohf/clariflix-skills/tree/v0.2.0 --skill proposta-comercial -a codex -g
```

Troque `codex` por `claude-code` ou `hermes-agent` conforme seu agente. No Claude.ai, envie o ZIP individual da release do ClariFlix. Consulte `LICENSE` e `SOURCE.md` para as condições do material.

Peça: “Crie uma proposta comercial para [cliente]. Seguem o briefing e os materiais da minha marca.” A skill extrai os dados, confirma o briefing e o sumário, prepara o HTML e verifica a exportação. Envie escopo, valores e prazos reais; campos ausentes serão perguntados.

Para exportar, resolva a pasta instalada da skill e execute:

```sh
python "<raiz-da-skill>/scripts/html2pdf.py" "<projeto>/proposta-cliente.html" --check
```

Requisitos: Python 3.8+ e Edge, Chrome ou Chromium. O script usa biblioteca padrão; `pypdf` é opcional. Fontes de internet têm fallback local. Sem exportação automática, abra o HTML e use Imprimir → Salvar como PDF, sem margens e com gráficos de fundo ativados.

Trabalhe numa cópia de `assets/template.html`; preserve a matriz instalada. Siga [SKILL.md](SKILL.md) e os checklists das referências para revisar conteúdo, marca, valores e paginação.


## Referência: assets/template.html

```html
<!DOCTYPE html>
<!-- ============================================================================
  TEMPLATE DE PROPOSTA COMERCIAL — deck HTML self-contained, proporção 2:1
  ============================================================================
  Estilo: neo-suíço tipográfico (referência Proposta_XFlow) — flat, preto/branco/
  cinza, espaço em branco radical, divisórias de uma palavra com ponto final.

  COMO USAR ESTE ARQUIVO
  1. Cada página é uma <section class="page" data-layout="...">. Duplique,
     remova ou reordene sections conforme a proposta (o rodapé vai junto).
  2. Re-branding: edite APENAS os tokens no :root (bloco "TOKENS DE MARCA").
     A cor da marca do usuário substitui os ACENTOS (verde/azul/laranja);
     os fundos preto/branco/cinza são o design — evite trocá-los.
  3. Logo: substitua o conteúdo do <symbol id="marca-octogono"> pelo SVG da
     marca do usuário (instruções no próprio symbol, logo abaixo).
  4. Visualizar: abra direto no navegador (duplo clique). O deck se ajusta
     à largura da janela e rola verticalmente entre páginas.
  5. Exportar PDF: scripts/html2pdf.py, ou manualmente Ctrl+P -> Salvar como
     PDF -> margens: Nenhuma -> ativar "Gráficos de fundo". Cada section vira
     exatamente uma página (338.67mm x 169.33mm).
  Zero dependências obrigatórias: a fonte Inter vem do Google Fonts, mas se
  não houver internet o deck cai graciosamente para Helvetica/Arial.
============================================================================= -->
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Proposta Comercial — Café Aurora | Studio Vetor</title>
<style>
/* Fonte Inter (Google Fonts). Se offline, o @import falha silenciosamente e o
   stack cai para 'Helvetica Neue'/Helvetica/Arial — o layout não quebra. */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  /* ================= TOKENS DE MARCA (edite aqui o re-branding) =================
     FUNDOS DE PÁGINA — a base "suíça" do deck. O ritmo claro/escuro/cinza É o
     design system: em regra, não recebem a cor da marca. */
  --pagina-branca:    #ffffff;  /* capa, cronograma, investimento, fechamento */
  --pagina-cinza:     #f8f8f8;  /* página de contexto — variação sutil do branco */
  --pagina-preta:     #000000;  /* bloco escuro: entregáveis e produtos */
  --pagina-cinza-med: #b8b8b8;  /* divisória "soft" e página de opcional (título branco sobre ele) */

  /* CARDS SOBRE FUNDO ESCURO */
  --card-escuro: #161616;                 /* fundo dos cards de toggle do sumário */
  --card-borda:  rgba(255,255,255,0.08);  /* borda 1px sutil de todos os cards escuros */

  /* TEXTO */
  --texto-escuro:   #000000;  /* texto primário em páginas claras */
  --texto-claro:    #ffffff;  /* texto primário em páginas escuras */
  --texto-muted:    #a5a5a5;  /* parágrafos secundários e bullets — o cinza da casa.
                                 Padrão de ênfase: parágrafo muted + <strong> na cor primária. */
  --texto-fantasma: #ececec;  /* elementos decorativos gigantes (ano da capa, logo do fechamento) */

  /* ACENTOS — é AQUI que entra a cor da marca do usuário:
     - troque o par verde-toggle/verde-icone-bg pela cor primária da marca
       (tom vivo + tom bem escuro da mesma cor);
     - troque badge-bg/badge-texto por um par pastel/vivo da marca;
     - acento-quente é o acento secundário (rótulo "Opcional )" no investimento). */
  --verde-toggle:   #2fd157;  /* toggle iOS ligado + ícone de check = "está incluído" */
  --verde-icone-bg: #132315;  /* fundo do quadrado atrás do ícone de check */
  --badge-bg:       #e4e6ff;  /* fundo do pill "Sprint NN" no cronograma */
  --badge-texto:    #0079ff;  /* texto do pill "Sprint NN" */
  --acento-quente:  #ff8770;  /* rótulo "Opcional )" na página de investimento */

  /* ESTRUTURA */
  --linha-clara: #d9d9d9;     /* linha do cronograma, tracejados e divisores em páginas claras */
  --fonte: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --margem-x: 64px;           /* margem lateral (~5% de 1280px) */
  --zoom: 1;                  /* escala de visualização em tela (recalculada via JS) */
}

/* ============================== BASE ============================== */
* { margin: 0; padding: 0; box-sizing: border-box; }
html { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
body {
  font-family: var(--fonte);
  background: #e7e7e7;               /* moldura cinza atrás das páginas (só em tela) */
  -webkit-font-smoothing: antialiased;
}
.deck { display: flex; flex-direction: column; align-items: center; gap: 28px; padding: 28px 0; }

/* Página base: 1280x640 (2:1). Em tela, `zoom` ajusta ao viewport; na
   impressão, o zoom é resetado e a section ocupa exatamente uma folha. */
.page {
  width: 1280px;
  height: 640px;
  position: relative;
  overflow: hidden;
  flex: none;
  zoom: var(--zoom);
  box-shadow: 0 2px 22px rgba(0,0,0,0.14);
}

/* Fundos + variáveis contextuais (cor de texto, rodapé e logo por tema) */
.pg-branca    { background: var(--pagina-branca);    color: var(--texto-escuro); --rodape-cor: #b0b0b0; --logo-cor: #d4d4d4; }
.pg-cinza     { background: var(--pagina-cinza);     color: var(--texto-escuro); --rodape-cor: #b0b0b0; --logo-cor: #d4d4d4; }
.pg-preta     { background: var(--pagina-preta);     color: var(--texto-claro); --rodape-cor: #3a3a3a; --logo-cor: rgba(255,255,255,0.35); }
.pg-cinza-med { background: var(--pagina-cinza-med); color: var(--texto-claro); --rodape-cor: rgba(255,255,255,0.45); --logo-cor: rgba(255,255,255,0.6); }

/* ============================== RODAPÉ PADRÃO ==============================
   4 colunas fixas em TODAS as páginas exceto o fechamento:
   documento | quem assina | © | ano  — sempre low-contrast. */
.rodape {
  position: absolute;
  left: var(--margem-x); right: var(--margem-x); bottom: 26px;
  display: grid; grid-template-columns: repeat(4, 1fr);
  font-size: 13px; font-weight: 500; color: var(--rodape-cor);
}
.rodape span:nth-child(2) { text-align: center; }
.rodape span:nth-child(3) { text-align: center; }
.rodape span:nth-child(4) { text-align: right; }

/* ============================== LOGO (slot) ==============================
   .logo-marca fica no topo-direito das páginas de conteúdo.
   Ele referencia o <symbol id="marca-octogono"> definido no <body>. */
.logo-marca {
  position: absolute; top: 42px; right: var(--margem-x);
  width: 46px; height: 46px; color: var(--logo-cor);
}

/* ============================== TÍTULOS ============================== */
/* Título de divisória: gigante, uma palavra, SEMPRE com ponto final. */
.divisoria-titulo {
  position: absolute; left: var(--margem-x); top: 22px;
  font-size: 112px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.12;
}
/* Título de página de conteúdo */
.titulo-pagina {
  position: absolute; left: var(--margem-x); top: 34px;
  font-size: 62px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.08;
}

/* ============================== CAPA ============================== */
.capa-linha {
  position: absolute; left: var(--margem-x); right: var(--margem-x);
  top: 50%; transform: translateY(-50%);
  display: flex; align-items: center; justify-content: space-between;
}
.capa-nome { font-size: 86px; font-weight: 700; letter-spacing: -0.03em; }
.capa-nome sup { font-size: 0.3em; vertical-align: super; font-weight: 700; }
.capa-copy { font-size: 34px; font-weight: 600; color: var(--texto-fantasma); }
.capa-ano  { font-size: 86px; font-weight: 700; letter-spacing: -0.02em; color: var(--texto-fantasma); } /* mesmo tamanho do nome (regra do design-system) */

/* ============================== CONTEXTO ============================== */
/* Parágrafo isolado no quadrante inferior-direito — o resto da página fica
   intencionalmente vazio (espaço em branco radical). */
.contexto-texto {
  position: absolute; right: var(--margem-x); bottom: 128px; width: 424px;
  font-size: 19.5px; line-height: 1.55; color: var(--texto-muted);
}
.contexto-texto p + p { margin-top: 26px; }
.contexto-texto strong { color: var(--texto-escuro); font-weight: 700; }

/* ============================== SUMÁRIO (toggles) ============================== */
.sumario-texto {
  position: absolute; left: 640px; width: 420px; top: 40px;
  font-size: 17.5px; line-height: 1.6; color: var(--texto-muted);
}
.sumario-texto strong { color: var(--texto-claro); font-weight: 700; }
.cards-toggle {
  position: absolute; left: var(--margem-x); right: var(--margem-x); bottom: 132px;
  display: grid; grid-template-columns: 1fr 1fr; gap: 20px 24px;
}
.card-toggle {
  height: 62px; background: var(--card-escuro);
  border: 1px solid var(--card-borda); border-radius: 14px;
  display: flex; align-items: center; gap: 18px; padding: 0 26px;
  font-size: 19px; font-weight: 700; color: var(--texto-claro);
}
/* Toggle iOS: sempre LIGADO, sempre na cor de acento — significa "incluído
   na proposta". O upsell opcional NÃO entra no sumário (ele aparece apenas
   na página de opcional e na linha de opcional do investimento). */
.toggle { flex: none; width: 40px; height: 24px; border-radius: 999px; background: var(--verde-toggle); position: relative; }
.toggle::after {
  content: ""; position: absolute; top: 2.5px; right: 2.5px;
  width: 19px; height: 19px; border-radius: 50%; background: #ffffff;
}

/* ============================== PRODUTO (grid 4x2 de features) ============================== */
.grid-features {
  position: absolute; left: var(--margem-x); right: var(--margem-x); top: 176px;
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px 24px;
  grid-auto-rows: 156px;
}
.card-feature {
  border: 1px solid var(--card-borda); border-radius: 12px;
  background: rgba(255,255,255,0.015);
  padding: 18px; display: flex; flex-direction: column; justify-content: space-between;
}
.card-feature p { font-size: 16.5px; font-weight: 600; line-height: 1.42; color: #f2f2f2; }
.icone-check {
  width: 32px; height: 32px; border-radius: 8px; flex: none;
  background: var(--verde-icone-bg); color: var(--verde-toggle);
  display: flex; align-items: center; justify-content: center;
}
.icone-check svg { width: 18px; height: 18px; }

/* ============================== OPCIONAL (2 colunas + mini-cards) ============================== */
.opcional-grade {
  position: absolute; left: var(--margem-x); right: var(--margem-x); top: 52px; bottom: 72px;
  display: grid; grid-template-columns: 1fr 0.82fr 0.78fr; column-gap: 42px;
}
.opcional-titulo h2 { font-size: 56px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.12; }
.opcional-titulo .rotulo { display: block; margin-top: 18px; font-size: 21px; font-weight: 500; color: rgba(255,255,255,0.55); }
.opcional-col { border-left: 1px solid rgba(255,255,255,0.38); padding-left: 42px; padding-top: 62px; }
.opcional-col h3 { font-size: 22px; font-weight: 700; line-height: 1.3; margin-bottom: 16px; }
.opcional-col p  { font-size: 16px; line-height: 1.6; color: rgba(255,255,255,0.82); }
.opcional-col hr { border: 0; border-top: 1px solid rgba(255,255,255,0.38); margin: 34px 0; }
.mini-cards { display: flex; flex-direction: column; gap: 10px; margin-top: 22px; }
.mini-card {
  border: 1px solid rgba(255,255,255,0.5); border-radius: 12px;
  padding: 12px 16px; display: flex; align-items: center; gap: 14px;
}
.mini-card .icone {
  width: 30px; height: 30px; border-radius: 8px; flex: none;
  background: rgba(255,255,255,0.22); color: #ffffff;
  display: flex; align-items: center; justify-content: center;
}
.mini-card .icone svg { width: 17px; height: 17px; }
.mini-card p { font-size: 15.5px; font-weight: 600; line-height: 1.35; }

/* ============================== CRONOGRAMA (timeline) ============================== */
/* Linha horizontal no centro vertical, dots nas colunas, conteúdo alternando
   acima/abaixo. Para 4 sprints por página, mude repeat(3,1fr) para repeat(4,1fr)
   e acrescente um dot em left:75% (com colunas em 0/25/50/75%). */
.cronograma-area {
  position: absolute; left: var(--margem-x); right: var(--margem-x); top: 140px; bottom: 60px;
  display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: 1fr 1fr;
}
.cronograma-area--cheia { top: 60px; }  /* variante para a 2ª página, sem título */
.cronograma-area::before {              /* linha sólida */
  content: ""; position: absolute; left: 0; right: -40px; top: 50%;
  height: 2px; margin-top: -1px; background: var(--linha-clara);
}
.cronograma-area::after {               /* trecho tracejado que "entra" pela esquerda */
  content: ""; position: absolute; left: calc(-1 * var(--margem-x)); width: var(--margem-x);
  top: 50%; margin-top: -1px; border-top: 2px dashed var(--linha-clara);
}
.ponto {
  position: absolute; top: 50%; width: 11px; height: 11px; border-radius: 50%;
  background: #c9c9c9; transform: translate(-50%, -50%); z-index: 1;
}
.sprint { padding-right: 40px; }
.sprint--acima  { grid-row: 1; align-self: end;   padding-bottom: 26px; }
.sprint--abaixo { grid-row: 2; align-self: start; padding-top: 26px; }
.sprint h4 { font-size: 21px; font-weight: 700; letter-spacing: -0.01em; margin: 12px 0 10px; }
.lista-sprint { list-style: none; }
.lista-sprint li {
  position: relative; padding-left: 24px; margin-bottom: 7px;
  font-size: 15px; line-height: 1.4; color: #8d8d8d;
}
/* Bullet "asterisco circulado" desenhado em SVG embutido (independe de fonte) */
.lista-sprint li::before {
  content: ""; position: absolute; left: 0; top: 3px; width: 15px; height: 15px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='none' stroke='%23a5a5a5' stroke-width='1.2'%3E%3Ccircle cx='8' cy='8' r='6.4'/%3E%3Cpath d='M8 4.6v6.8M5.1 6.3l5.8 3.4M10.9 6.3l-5.8 3.4'/%3E%3C/svg%3E") no-repeat center / contain;
}
/* Badge pill do sprint */
.badge-sprint {
  display: inline-flex; align-items: center; gap: 9px;
  background: var(--badge-bg); color: var(--badge-texto);
  font-size: 16px; font-weight: 700; padding: 7px 16px; border-radius: 999px;
}
.badge-sep { width: 18px; height: 8px; stroke: currentColor; fill: none; stroke-width: 1.6; opacity: 0.55; flex: none; }
.badge-dias { opacity: 0.62; font-weight: 600; }

/* ============================== PRAZO (fundo dramático) ============================== */
/* Fundo escuro em CSS puro (gradientes) no lugar da foto, para o template não
   depender de arquivo externo.
   PARA USAR UMA FOTO REAL: substitua o background da regra abaixo por
     background: linear-gradient(rgba(0,0,0,0.84), rgba(0,0,0,0.84)),
                 url('data:image/jpeg;base64,SUA_IMAGEM_AQUI') center / cover no-repeat;
   Mantenha o overlay escuro em >= 80% de opacidade e prefira foto P&B
   (equipe trabalhando) — a foto é clima, não protagonista.
   Para gerar o base64 no Windows:
     python -c "import base64; print(base64.b64encode(open('foto.jpg','rb').read()).decode())" */
.page[data-layout="prazo-foto"] {
  background:
    radial-gradient(900px 500px at 78% 10%, rgba(255,255,255,0.055), transparent 60%),
    radial-gradient(700px 420px at 10% 88%, rgba(255,255,255,0.04), transparent 55%),
    repeating-linear-gradient(115deg, rgba(255,255,255,0.016) 0 2px, transparent 2px 96px),
    linear-gradient(150deg, #141414, #060606 55%, #101010);
}
.prazo-texto {
  position: absolute; left: 640px; width: 430px; bottom: 128px;
  font-size: 19.5px; line-height: 1.55; color: var(--texto-muted);
}
.prazo-texto p + p { margin-top: 26px; }
.prazo-texto strong { color: var(--texto-claro); font-weight: 700; }

/* ============================== INVESTIMENTO (tabela) ============================== */
.invest-texto { position: absolute; left: var(--margem-x); width: 490px; bottom: 128px; }
.invest-lead { font-size: 25px; line-height: 1.42; color: var(--texto-muted); font-weight: 500; }
.invest-lead strong { color: var(--texto-escuro); font-weight: 700; }
.invest-corpo { margin-top: 22px; font-size: 16.5px; line-height: 1.6; color: var(--texto-muted); }
.invest-corpo strong { color: #111111; font-weight: 600; }
.invest-opcional { margin-top: 30px; font-size: 16px; line-height: 1.6; color: var(--texto-muted); }
.rotulo-opcional { color: var(--acento-quente); font-weight: 600; }
/* Tabela: itens separados por linhas tracejadas; total com linha sólida acima. */
.tabela-investimento { position: absolute; left: 640px; right: var(--margem-x); bottom: 118px; }
.linha {
  display: flex; justify-content: space-between; align-items: baseline;
  padding: 21px 0; font-size: 21px; font-weight: 700; color: var(--texto-escuro);
}
.linha + .linha { border-top: 1px dashed #cccccc; }
.linha--total { border-top: 2px solid #161616 !important; font-size: 22px; }

/* ============================== FECHAMENTO ============================== */
.logo-fechamento {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  width: 96px; height: 96px; color: var(--texto-fantasma);
}

/* ============================== IMPRESSÃO ==============================
   Cada section = exatamente uma folha 2:1, sem margens nem vazamento. */
@page { size: 338.67mm 169.33mm; margin: 0; }
@media print {
  body { background: #ffffff; }
  .deck { display: block; padding: 0; gap: 0; }
  .page {
    zoom: 1 !important;
    width: 1280px;
    height: 169.33mm;        /* levemente < 640px: garante que nada vaze para a folha seguinte */
    margin: 0 !important;
    box-shadow: none;
    page-break-after: always; break-after: page;
    break-inside: avoid;
  }
  .page:last-of-type { page-break-after: auto; break-after: auto; }
}
</style>
</head>
<body>

<!-- ============================================================================
  BIBLIOTECA DE ÍCONES (SVG inline, reutilizados via <use>)
  LOGO: substitua o CONTEÚDO do <symbol id="marca-octogono"> pelo SVG do logo
  do usuário. Dicas:
   - mantenha o viewBox quadrado (ex.: 0 0 48 48) e traços com stroke="currentColor"
     (assim o logo herda a cor certa em páginas claras E escuras);
   - se o logo for um arquivo (PNG/JPG), troque os <svg class="logo-marca">...</svg>
     das páginas por <img class="logo-marca" src="data:image/png;base64,...">
     e prefira uma versão monocromática;
   - sem logo? Troque o symbol por um monograma: <text x="24" y="32"
     text-anchor="middle" font-size="28" font-weight="700" fill="currentColor">SV</text>
============================================================================= -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <!-- Placeholder: octógono line-art com cubo (estilo marca XFlow) -->
    <symbol id="marca-octogono" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">
      <path d="M14 4h20l10 10v20L34 44H14L4 34V14Z"/>
      <path d="M24 14.5l8.5 4.9v9.2L24 33.5l-8.5-4.9v-9.2Z"/>
      <path d="M15.5 19.4l8.5 4.9 8.5-4.9"/>
      <path d="M24 24.3v9.2"/>
    </symbol>
    <!-- Check circular usado nos cards de feature -->
    <symbol id="icone-check-circulo" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="9"/>
      <path d="M8.4 12.3l2.4 2.4 4.8-5.3"/>
    </symbol>
  </defs>
</svg>

<main class="deck">

<!-- ===== PÁGINA 1: CAPA (layout: capa) ===== -->
<!-- Nome do CLIENTE da proposta gigante à esquerda; © e ano em cinza-fantasma.
     No rodapé, quem assina é o usuário da skill (quem vende). -->
<section class="page pg-branca" data-layout="capa">
  <div class="capa-linha">
    <h1 class="capa-nome">Café Aurora<sup>&reg;</sup></h1>
    <span class="capa-copy">&copy;</span>
    <span class="capa-ano">2026</span>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 2: CONTEXTO (layout: contexto) ===== -->
<!-- Página quase vazia de propósito: um único parágrafo no quadrante
     inferior-direito. Ênfase seletiva: cinza muted + <strong> escuro. -->
<section class="page pg-cinza" data-layout="contexto">
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="contexto-texto">
    <p>O Studio Vetor &mdash; consultoria especializada em automa&ccedil;&atilde;o comercial &mdash; desenha sistemas que trabalham enquanto a sua equipe cuida do que importa: o cliente.</p>
    <p>Nesta proposta, <strong>apresentamos um plano completo de automa&ccedil;&atilde;o para a rede Caf&eacute; Aurora,</strong> conectando pedidos, fidelidade e gest&atilde;o das unidades em uma &uacute;nica opera&ccedil;&atilde;o digital.</p>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 3: DIVISÓRIA ENTREGÁVEIS (layout: divisoria, variante dark) ===== -->
<!-- Divisória dramática: só a palavra gigante com ponto final. -->
<section class="page pg-preta" data-layout="divisoria" data-variante="dark">
  <h2 class="divisoria-titulo">Entreg&aacute;veis.</h2>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 4: SUMÁRIO DE ENTREGÁVEIS (layout: sumario-toggles) ===== -->
<!-- Toggle sempre ligado = incluído na proposta. Upsells opcionais NÃO entram
     aqui (aparecem só na página de opcional e no investimento).
     Grade 2x2; com mais produtos, os cards quebram em novas linhas. -->
<section class="page pg-preta" data-layout="sumario-toggles">
  <h2 class="titulo-pagina">Entreg&aacute;veis</h2>
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="sumario-texto">
    <p>Automatize a opera&ccedil;&atilde;o da Caf&eacute; Aurora com um ecossistema que conecta atendimento, fideliza&ccedil;&atilde;o e gest&atilde;o. <strong>Tr&ecirc;s projetos integrados que reduzem filas, aumentam a recorr&ecirc;ncia e d&atilde;o visibilidade total</strong> sobre as 12 unidades da rede.</p>
  </div>
  <div class="cards-toggle">
    <div class="card-toggle"><span class="toggle" aria-hidden="true"></span>Agente de Pedidos</div>
    <div class="card-toggle"><span class="toggle" aria-hidden="true"></span>Fidelidade Digital</div>
    <div class="card-toggle"><span class="toggle" aria-hidden="true"></span>Central de Gest&atilde;o</div>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 5: PRODUTO — AGENTE DE PEDIDOS (layout: produto-features-grid) ===== -->
<!-- Uma página por produto: título + grid 4x2 com 8 features (frases curtas,
     ~2 linhas cada). Para mais produtos, duplique esta section inteira. -->
<section class="page pg-preta" data-layout="produto-features-grid">
  <h2 class="titulo-pagina">Agente de Pedidos</h2>
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="grid-features">
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Atendimento 24/7 no WhatsApp com card&aacute;pio interativo</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Pedidos registrados direto no caixa, integrados ao PDV</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Sugest&atilde;o de combos com base no hist&oacute;rico de consumo</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Confirma&ccedil;&atilde;o autom&aacute;tica de retirada e delivery</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Fila priorizada nos hor&aacute;rios de pico</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Status do pedido em tempo real para o cliente</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Transi&ccedil;&atilde;o suave para atendente humano quando necess&aacute;rio</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Relat&oacute;rio di&aacute;rio de pedidos por unidade</p></div>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 6: PRODUTO — FIDELIDADE DIGITAL (layout: produto-features-grid) ===== -->
<section class="page pg-preta" data-layout="produto-features-grid">
  <h2 class="titulo-pagina">Fidelidade Digital</h2>
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="grid-features">
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Cart&atilde;o fidelidade digital, sem app e sem senha</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Ac&uacute;mulo autom&aacute;tico de pontos a cada compra</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Resgate de recompensas em qualquer unidade</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Campanhas de reativa&ccedil;&atilde;o para clientes inativos</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Cupons personalizados por perfil de consumo</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Oferta autom&aacute;tica para aniversariantes do m&ecirc;s</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Painel de ades&atilde;o e resgates por unidade</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Integra&ccedil;&atilde;o com o caixa das 12 lojas</p></div>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 7: PRODUTO — CENTRAL DE GESTÃO (layout: produto-features-grid) ===== -->
<section class="page pg-preta" data-layout="produto-features-grid">
  <h2 class="titulo-pagina">Central de Gest&atilde;o</h2>
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="grid-features">
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Painel &uacute;nico com as vendas das 12 unidades em tempo real</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Alertas de ruptura de estoque por insumo</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Reposi&ccedil;&atilde;o autom&aacute;tica junto aos fornecedores</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Consolida&ccedil;&atilde;o di&aacute;ria de caixa por loja</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Ranking de produtos mais vendidos por unidade</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Controle padronizado de perdas e desperd&iacute;cio</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Exporta&ccedil;&atilde;o cont&aacute;bil em um clique</p></div>
    <div class="card-feature"><span class="icone-check"><svg><use href="#icone-check-circulo"/></svg></span><p>Acessos por perfil: matriz, gerente e franqueado</p></div>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 8: OPCIONAL — CONSULTORIA DE DADOS (layout: opcional-2col) ===== -->
<!-- Página de upsell em cinza médio: título + rótulo "(Opcional)", duas colunas
     de texto e coluna de mini-cards com ícones. -->
<section class="page pg-cinza-med" data-layout="opcional-2col">
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="opcional-grade">
    <div class="opcional-titulo">
      <h2>Consultoria<br>de Dados</h2>
      <span class="rotulo">(Opcional)</span>
    </div>
    <div class="opcional-col">
      <h3>Leitura Mensal<br>dos Indicadores</h3>
      <p>An&aacute;lise recorrente dos dados gerados pelos tr&ecirc;s sistemas, transformando n&uacute;meros de vendas, fidelidade e opera&ccedil;&atilde;o em decis&otilde;es pr&aacute;ticas para a rede.</p>
      <hr>
      <h3>Evolu&ccedil;&atilde;o Cont&iacute;nua<br>das Automa&ccedil;&otilde;es</h3>
      <p>Ajustes mensais nos fluxos de atendimento e nas regras do programa de pontos, considerando sazonalidade, campanhas e o comportamento real dos clientes.</p>
    </div>
    <div class="opcional-col">
      <h3>An&aacute;lise Avan&ccedil;ada<br>&amp; Relat&oacute;rios Mensais</h3>
      <div class="mini-cards">
        <div class="mini-card">
          <span class="icone"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><path d="M5 20v-8M12 20V5M19 20v-5"/></svg></span>
          <p>M&eacute;tricas de vendas por unidade e por canal</p>
        </div>
        <div class="mini-card">
          <span class="icone"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5V12l6 5.5"/></svg></span>
          <p>An&aacute;lise do comportamento de consumo</p>
        </div>
        <div class="mini-card">
          <span class="icone"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="5.5" cy="6" r="2.4"/><circle cx="18.5" cy="6" r="2.4"/><circle cx="12" cy="18" r="2.4"/><path d="M7.4 7.4l3.2 8M16.6 7.4l-3.2 8M7.9 6h8.2"/></svg></span>
          <p>Segmenta&ccedil;&atilde;o dos clientes do fidelidade</p>
        </div>
        <div class="mini-card">
          <span class="icone"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.6"/><path d="M5 20c1.2-3.8 3.6-5.6 7-5.6s5.8 1.8 7 5.6"/></svg></span>
          <p>Mapa de hor&aacute;rios de pico por loja</p>
        </div>
        <div class="mini-card">
          <span class="icone"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20 4v4h-4"/></svg></span>
          <p>Recomenda&ccedil;&otilde;es de card&aacute;pio e campanhas</p>
        </div>
      </div>
    </div>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 9: DIVISÓRIA CRONOGRAMA (layout: divisoria, variante light) ===== -->
<section class="page pg-branca" data-layout="divisoria" data-variante="light">
  <h2 class="divisoria-titulo">Cronograma.</h2>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 10: CRONOGRAMA PARTE 1 (layout: cronograma-timeline) ===== -->
<!-- Sprints 01-03. Ímpares abaixo da linha, pares acima (alternância contínua).
     LIMITES para caber na metade da página: máximo de 4 bullets por sprint e
     frases de UMA linha (até ~38 caracteres cada). -->
<section class="page pg-branca" data-layout="cronograma-timeline">
  <h2 class="titulo-pagina">Cronograma.</h2>
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="cronograma-area">
    <i class="ponto" style="left:0%"></i>
    <i class="ponto" style="left:33.333%"></i>
    <i class="ponto" style="left:66.667%"></i>
    <article class="sprint sprint--abaixo" style="grid-column:1">
      <span class="badge-sprint">Sprint 01
        <svg class="badge-sep" viewBox="0 0 18 8" aria-hidden="true"><line x1="1" y1="4" x2="11" y2="4"/><circle cx="14.5" cy="4" r="2.4"/></svg>
        <span class="badge-dias">1-10 Dias</span>
      </span>
      <h4>Imers&atilde;o e Mapeamento</h4>
      <ul class="lista-sprint">
        <li>Visita e mapeamento das unidades-piloto</li>
        <li>Levantamento de card&aacute;pio e combos</li>
        <li>Acessos a PDV, estoque e fornecedores</li>
        <li>Metas e indicadores por unidade</li>
      </ul>
    </article>
    <article class="sprint sprint--acima" style="grid-column:2">
      <span class="badge-sprint">Sprint 02
        <svg class="badge-sep" viewBox="0 0 18 8" aria-hidden="true"><line x1="1" y1="4" x2="11" y2="4"/><circle cx="14.5" cy="4" r="2.4"/></svg>
        <span class="badge-dias">11-20 Dias</span>
      </span>
      <h4>Agente de Pedidos</h4>
      <ul class="lista-sprint">
        <li>Fluxo de pedidos no WhatsApp</li>
        <li>Card&aacute;pio interativo e combos</li>
        <li>Integra&ccedil;&atilde;o com o PDV das lojas-piloto</li>
        <li>Regras de delivery e hor&aacute;rios de pico</li>
      </ul>
    </article>
    <article class="sprint sprint--abaixo" style="grid-column:3">
      <span class="badge-sprint">Sprint 03
        <svg class="badge-sep" viewBox="0 0 18 8" aria-hidden="true"><line x1="1" y1="4" x2="11" y2="4"/><circle cx="14.5" cy="4" r="2.4"/></svg>
        <span class="badge-dias">21-30 Dias</span>
      </span>
      <h4>Fidelidade Digital</h4>
      <ul class="lista-sprint">
        <li>Estrutura&ccedil;&atilde;o do programa de pontos</li>
        <li>Regras de ac&uacute;mulo, resgate e expira&ccedil;&atilde;o</li>
        <li>Campanhas de reativa&ccedil;&atilde;o e anivers&aacute;rio</li>
        <li>Integra&ccedil;&atilde;o com o caixa das lojas</li>
      </ul>
    </article>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 11: CRONOGRAMA PARTE 2 (layout: cronograma-timeline) ===== -->
<!-- Continuação sem título repetido (.cronograma-area--cheia ocupa a página). -->
<section class="page pg-branca" data-layout="cronograma-timeline">
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="cronograma-area cronograma-area--cheia">
    <i class="ponto" style="left:0%"></i>
    <i class="ponto" style="left:33.333%"></i>
    <i class="ponto" style="left:66.667%"></i>
    <article class="sprint sprint--acima" style="grid-column:1">
      <span class="badge-sprint">Sprint 04
        <svg class="badge-sep" viewBox="0 0 18 8" aria-hidden="true"><line x1="1" y1="4" x2="11" y2="4"/><circle cx="14.5" cy="4" r="2.4"/></svg>
        <span class="badge-dias">31-40 Dias</span>
      </span>
      <h4>Central de Gest&atilde;o</h4>
      <ul class="lista-sprint">
        <li>Painel de vendas em tempo real</li>
        <li>Alertas de estoque e reposi&ccedil;&atilde;o autom&aacute;tica</li>
        <li>Consolida&ccedil;&atilde;o de caixa e exporta&ccedil;&atilde;o cont&aacute;bil</li>
      </ul>
    </article>
    <article class="sprint sprint--abaixo" style="grid-column:2">
      <span class="badge-sprint">Sprint 05
        <svg class="badge-sep" viewBox="0 0 18 8" aria-hidden="true"><line x1="1" y1="4" x2="11" y2="4"/><circle cx="14.5" cy="4" r="2.4"/></svg>
        <span class="badge-dias">41-50 Dias</span>
      </span>
      <h4>Testes Assistidos</h4>
      <ul class="lista-sprint">
        <li>Piloto assistido em 3 unidades</li>
        <li>Ajustes finos com feedback das equipes</li>
        <li>Treinamento de gerentes e atendentes</li>
      </ul>
    </article>
    <article class="sprint sprint--acima" style="grid-column:3">
      <span class="badge-sprint">Sprint 06
        <svg class="badge-sep" viewBox="0 0 18 8" aria-hidden="true"><line x1="1" y1="4" x2="11" y2="4"/><circle cx="14.5" cy="4" r="2.4"/></svg>
        <span class="badge-dias">51-60 Dias</span>
      </span>
      <h4>Implanta&ccedil;&atilde;o na Rede</h4>
      <ul class="lista-sprint">
        <li>Ativa&ccedil;&atilde;o nas 12 unidades</li>
        <li>Acompanhamento em hor&aacute;rio de pico</li>
        <li>Documenta&ccedil;&atilde;o e passagem de bast&atilde;o</li>
      </ul>
    </article>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 12: O PRAZO (layout: prazo-foto) ===== -->
<!-- Fundo escuro dramático em CSS puro (veja o comentário na regra
     .page[data-layout="prazo-foto"] no CSS para trocar por foto em base64). -->
<section class="page" data-layout="prazo-foto" style="color:#ffffff; --rodape-cor:#3a3a3a; --logo-cor:rgba(255,255,255,0.35);">
  <h2 class="titulo-pagina">O Prazo</h2>
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="prazo-texto">
    <p>Para garantir a m&aacute;xima qualidade na implanta&ccedil;&atilde;o, solicitamos um <strong>prazo total de 60 dias.</strong> As etapas descritas no Cronograma ser&atilde;o organizadas internamente da forma mais eficiente poss&iacute;vel.</p>
    <p>Obs.: H&aacute; uma <strong>grande possibilidade</strong> de que a entrega final <strong>seja conclu&iacute;da antes do prazo</strong> estipulado.</p>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 13: DIVISÓRIA INVESTIMENTO (layout: divisoria, variante gray) ===== -->
<section class="page pg-cinza-med" data-layout="divisoria" data-variante="gray">
  <h2 class="divisoria-titulo">Investimento.</h2>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 14: INVESTIMENTO (layout: investimento-tabela) ===== -->
<!-- Esquerda: valor total por extenso + condição + opcional mensal (laranja).
     Direita: tabela com linhas tracejadas e total com linha sólida.
     REGRA DE OURO: preços e condições vêm SEMPRE do usuário — nunca invente. -->
<section class="page pg-branca" data-layout="investimento-tabela">
  <h2 class="titulo-pagina">Investimento</h2>
  <svg class="logo-marca" aria-hidden="true"><use href="#marca-octogono"/></svg>
  <div class="invest-texto">
    <p class="invest-lead">O Investimento ser&aacute; de <strong>R$ 96 mil &agrave; vista,</strong><br><strong>para constru&ccedil;&atilde;o dos 3 projetos.</strong></p>
    <p class="invest-corpo">Este <strong>investimento inclui todas as ferramentas, licen&ccedil;as e integra&ccedil;&otilde;es</strong> necess&aacute;rias para a execu&ccedil;&atilde;o do projeto &mdash; sem surpresas ou custos adicionais.</p>
    <p class="invest-opcional"><span class="rotulo-opcional">Opcional )</span> Caso opte pela nossa Consultoria de Dados &mdash; para receber an&aacute;lises e recomenda&ccedil;&otilde;es mensais &mdash; o valor ser&aacute; de R$ 4.500 por m&ecirc;s.</p>
  </div>
  <div class="tabela-investimento">
    <div class="linha"><span>Agente de Pedidos</span><span>R$ 38.000,00</span></div>
    <div class="linha"><span>Fidelidade Digital</span><span>R$ 26.000,00</span></div>
    <div class="linha"><span>Central de Gest&atilde;o</span><span>R$ 32.000,00</span></div>
    <div class="linha linha--total"><span>Investimento Total</span><span>R$ 96.000,00</span></div>
  </div>
  <footer class="rodape">
    <span>Proposta Comercial</span><span>Studio Vetor</span><span>&copy;</span><span>2026</span>
  </footer>
</section>

<!-- ===== PÁGINA 15: FECHAMENTO (layout: fechamento-logo) ===== -->
<!-- Só o logo centralizado em cinza-fantasma. Única página SEM rodapé. -->
<section class="page pg-branca" data-layout="fechamento-logo">
  <svg class="logo-fechamento" aria-hidden="true"><use href="#marca-octogono"/></svg>
</section>

</main>

<script>
/* Scale-to-fit em tela: ajusta a propriedade --zoom para o deck caber na
   largura da janela. Na impressão o CSS reseta zoom para 1 (tamanho real).
   Sem JavaScript, o deck abre em tamanho natural (1280px) — nada quebra. */
(function () {
  function ajustarEscala() {
    var largura = document.documentElement.clientWidth;
    var escala = Math.min((largura - 48) / 1280, 1.35);
    if (!(escala > 0)) { escala = 1; }
    document.documentElement.style.setProperty('--zoom', escala.toFixed(4));
  }
  window.addEventListener('resize', ajustarEscala);
  ajustarEscala();
})();
</script>

</body>
</html>
```


## Referência: references/descoberta.md

# Descoberta — protocolo pré-geração

Este protocolo roda **antes** de qualquer proposta ser gerada. O objetivo é preencher os
6 blocos de informação abaixo com o mínimo de fricção: primeiro **extrair** de materiais
que o usuário já forneceu, depois **perguntar** apenas o que faltar, e por fim
**confirmar** o brief consolidado antes de passar à geração.

---

## Regra de ouro

> **NUNCA invente preços, prazos, features, nomes de produtos, nomes de pessoas ou
> promessas.** Tudo que aparece na proposta vem do usuário ou dos materiais dele.
> Se uma informação necessária não existir, **pergunte** — não preencha com suposição,
> não use "valores típicos de mercado", não complete listas de features por conta própria.
> Placeholder só existe dentro do template; na proposta entregue, zero invenção.

---

## Ordem de operação

1. **Inventariar materiais fornecidos** (mensagens, arquivos anexados, URLs citadas).
2. **Extrair automaticamente** tudo que der (seção "Extração automática" abaixo).
3. **Marcar cada bloco A–F** como: `completo`, `parcial` ou `vazio`.
4. **Entrevistar** só sobre o que está `parcial`/`vazio` — máximo de 3–4 perguntas por
   mensagem. Comece pelo que bloqueia a geração (ver tabela "Mínimo viável").
5. **Consolidar e confirmar** o brief com o usuário antes de gerar qualquer HTML.

---

## Extração automática (SEMPRE antes de perguntar)

Perguntar algo que o material já responde queima a confiança do usuário. Por isso:

### Site do usuário (ou do cliente dele)
- Se o usuário citou uma URL, use **WebFetch** para ler o site.
- Extrair: nome/marca como escrita oficialmente, o que a empresa faz, tom de voz
  (formal? direto? técnico?), produtos/serviços listados, cores predominantes se
  descritas, claims e frases de posicionamento reutilizáveis.
- Preenche principalmente os **blocos A e B**.

### PDFs e arquivos (brief, brand guide, apresentação institucional)
- Use **Read** em cada arquivo fornecido (`.pdf`, `.md`, `.txt`, `.docx` convertido).
- De um **brand guide**: cores exatas (hex), fontes, regras de uso do logo, caminho do
  arquivo de logo — alimenta a fase de brand-config.
- De um **brief**: qualquer campo dos blocos A–F que estiver escrito. Copiar valores
  literalmente (preços, prazos, nomes) — nunca "arredondar" nem parafrasear números.

### Transcrições de calls de vendas
- Fonte mais valiosa de todas. Ler por inteiro e extrair:
  - **Dores literais do cliente**, nas palavras dele ("a gente perde lead no fim de
    semana", "meu time não dá conta do pós-venda"). Guardar as citações — elas viram
    o texto da página de contexto e dos parágrafos de entregáveis, porque proposta
    que ecoa as palavras do cliente fecha mais.
  - O que foi **efetivamente prometido/combinado** na call: escopo, prazos mencionados,
    valores discutidos, objeções e como foram respondidas.
  - Nomes das pessoas (decisor, contato) e como o cliente chama o próprio negócio.
- Atenção: transcrição contém especulação e negociação. Só entra na proposta o que foi
  **acordado ou confirmado pelo usuário** — na dúvida, listar e perguntar
  "isso ficou fechado ou ainda está em aberto?".

---

## Os 6 blocos de informação

Para cada bloco: as perguntas abaixo são o roteiro de entrevista. Faça apenas as que a
extração automática não respondeu, em grupos de **no máximo 3–4 perguntas por mensagem**.

### Bloco A — Quem vende (o usuário da skill)

| Campo | Obrigatório? |
|---|---|
| Nome/marca (grafia exata) | Sim |
| O que a empresa faz (1 frase) | Sim |
| Logo (arquivo SVG/PNG) ou aceitar monograma tipográfico | Não |
| Site, cores da marca, tom de voz | Não |

Perguntas:
1. Qual o nome da sua empresa/marca, exatamente como deve aparecer na proposta?
2. Em uma frase: o que vocês fazem e para quem?
3. Você tem logo em SVG ou PNG e um site que eu possa analisar? Se sim, me passe o
   caminho/URL.

### Bloco B — Para quem (o cliente da proposta)

| Campo | Obrigatório? |
|---|---|
| Nome da empresa cliente (grafia exata) | Sim |
| Setor/contexto do negócio | Recomendado |
| Nome do contato/decisor | Não |
| Dor ou motivação principal | Recomendado |

Perguntas:
1. Para qual empresa é esta proposta? Confirme a grafia exata do nome.
2. Qual o principal problema ou objetivo que levou esse cliente até você?
3. Tem alguma call, e-mail ou anotação dessa negociação que eu possa ler? (Se tiver,
   eu uso as palavras do próprio cliente no texto.)

### Bloco C — Oferta (produtos/serviços)

| Campo | Obrigatório? |
|---|---|
| Lista de produtos/serviços com nome de cada um | Sim (mínimo 1) |
| Features por produto (ideal 6–8; mínimo 3) | Sim |
| Opcionais/upsells (ex.: consultoria mensal) | Não |

Perguntas:
1. Quais produtos ou serviços entram nesta proposta? Liste os nomes.
2. Para cada um: quais são as entregas/features concretas? (O ideal são 6 a 8 por
   produto — se me der menos, eu pergunto, nunca completo sozinho.)
3. Existe algum item opcional/upsell que deva aparecer como "(Opcional)"?

### Bloco D — Execução (cronograma e prazo)

| Campo | Obrigatório? |
|---|---|
| Prazo total do projeto | Sim |
| Fases/sprints com nome, duração e atividades | Recomendado |
| Observações (ex.: possibilidade de entrega antecipada) | Não |

Perguntas:
1. Qual o prazo total do projeto?
2. Como você divide a execução em fases ou sprints? (Nome de cada fase, duração e
   2–4 atividades por fase.)
3. Alguma observação sobre prazo que valha registrar (ex.: "pode sair antes")?

### Bloco E — Comercial (preços e condições)

| Campo | Obrigatório? |
|---|---|
| Preço por item OU preço total fechado | Sim (total é obrigatório) |
| Condições de pagamento (à vista, parcelado, entrada) | Sim |
| Valor de opcionais/mensalidades | Se houver opcional |

Perguntas:
1. Qual o valor total do investimento?
2. Quanto custa cada item individualmente? (A tabela da proposta lista item a item —
   a soma precisa bater com o total.)
3. Quais as condições de pagamento (à vista, parcelas, entrada + parcelas)?
4. Se houver opcionais: qual o valor e a recorrência de cada um (ex.: R$ X/mês)?

Cuidado com multiplicadores: se o usuário disser "3x R$ 40.000", confirmar se é
**3 unidades** de R$ 40.000 (soma R$ 120.000) ou **3 parcelas** (soma R$ 40.000 ou
R$ 120.000 dependendo do combinado). Nunca decidir sozinho.

### Bloco F — Extras (opcional)

| Campo | Obrigatório? |
|---|---|
| Depoimentos/cases | Não |
| Garantias | Não |
| Outros anexos (equipe, metodologia) | Não |

Pergunta única (fazer só se os blocos A–E já estiverem resolvidos):
1. Quer incluir páginas extras — depoimentos, cases, garantias? Se sim, me passe o
   conteúdo exato (nunca vou redigir um depoimento ou uma garantia por conta própria).

---

## Mínimo viável vs. ideal

| Campo | Mínimo viável para gerar | Ideal |
|---|---|---|
| Quem vende | Nome/marca | + logo, site, cores, tom de voz |
| Cliente | Nome da empresa | + setor, contato, dor nas palavras do cliente |
| Oferta | 1 produto com **3+ features** | 2–4 produtos com 6–8 features cada + opcional |
| Execução | Prazo total | + 4–8 sprints nomeados com atividades |
| Comercial | **Preço total** | + preço por item, condições, opcionais mensais |
| Extras | — (nada) | Depoimentos, cases, garantias |

- **Abaixo do mínimo viável: não gerar.** Explique ao usuário exatamente o que falta e
  pergunte.
- **No mínimo viável (mas sem o ideal): pode gerar**, avisando quais páginas ficarão de
  fora (ex.: sem sprints detalhados, o deck sai sem as páginas de timeline — só a página
  de prazo).

---

## Confirmação do brief (obrigatória)

Antes de passar para a geração, mostrar ao usuário o **brief consolidado** em resumo
estruturado, neste formato:

```
BRIEF DA PROPOSTA — confirme antes de eu gerar

Quem vende:   <nome> — <o que faz> — logo: <arquivo/monograma>
Cliente:      <empresa> — <setor> — contato: <nome ou "não informado">
Dor/contexto: <resumo em 1–2 frases, com citações da call se houver>

Oferta:
  1. <Produto A> — <n> features: <lista curta>
  2. <Produto B> — ...
  Opcional: <item> — <valor/recorrência>

Execução:     <prazo total> — <n> sprints: <nomes>
Comercial:    Total <R$ X> — condições: <à vista/parcelado> 
              Itens: <item = valor, ...> (soma conferida: <R$ X>)
Extras:       <depoimentos/cases/garantias ou "nenhum">

Páginas previstas: <n> (<lista dos tipos de página>)
```

Perguntar explicitamente: **"Está tudo correto? Posso gerar a proposta com base nisso?"**

- Só avançar para a geração após o "sim" do usuário.
- Se o usuário corrigir algo, atualizar o brief, reexibir o resumo e confirmar de novo.
- Registrar no resumo a soma dos itens comerciais já conferida — se a soma dos itens não
  bater com o total informado, resolver **aqui**, nunca na página de investimento.


## Referência: references/design-system.md

# Design System — Proposta Comercial

> Especificação visual canônica da skill `proposta-comercial`. Baseada na análise
> página-a-página da proposta de referência (Proposta_XFlow, 16 páginas, proporção 2:1).
> Este arquivo garante que QUALQUER proposta gerada — com qualquer marca — mantenha a
> qualidade do design de referência: suíço, tipográfico, flat, com espaço em branco radical.

**Convenção de medidas**: todas as medidas são RELATIVAS à largura da página
(base de referência: 1280×640px, proporção 2:1). Ex.: "5% da largura" = 64px na base.
Use `clamp()`/unidades relativas no CSS para que o deck escale sem quebrar.
Nunca use medidas absolutas que não derivem da largura da página.

---

## 1. Design Tokens

Declare TODOS os tokens como CSS custom properties no `:root` do HTML gerado.
O re-branding acontece SOMENTE trocando valores de tokens — nunca editando CSS espalhado.

| CSS var | Valor default | Papel | O que muda no re-branding |
|---|---|---|---|
| `--pagina-branca` | `#ffffff` | Fundo das páginas claras (capa, cronograma, investimento, fechamento) | NADA. Fundos permanecem neutros. |
| `--pagina-cinza` | `#f8f8f8` | Variação sutil para páginas de contexto (quebra a monotonia do branco puro) | NADA. |
| `--pagina-preta` | `#000000` | Fundo do bloco escuro (entregáveis, páginas de produto, prazo) | NADA (exceção: modo dark-first pode trocar por um "quase-preto" da marca, ex. `#0a0a0c`, se o brand guide o definir). |
| `--pagina-cinza-med` | `#b8b8b8` | Fundo das divisórias cinza e da página de opcional/upsell — título branco sobre ele | NADA, ou um cinza neutro equivalente (luminância similar). Nunca uma cor saturada. |
| `--card-escuro` | `#161616` | Fundo dos cards sobre página preta (borda: `rgba(255,255,255,0.08)`) | NADA. Card escuro é sempre "um degrau acima" do fundo preto. |
| `--texto-primario` | `#000000` (claro) / `#ffffff` (escuro) | Títulos, trechos em bold, texto de ênfase | NADA. Texto primário é sempre preto-ou-branco. |
| `--texto-muted` | `#a5a5a5` | Bullets, parágrafos secundários, a "voz baixa" do deck | NADA (ajuste fino de contraste permitido, ver seção 4c). |
| `--texto-fantasma` | `#ececec` | Elementos gigantes decorativos (ano na capa, "©" central, logo do fechamento) | NADA. Deve ser quase invisível — é textura, não informação. |
| `--verde-toggle` | `#2fd157` | Toggle iOS "ligado" nos cards de entregáveis; ícones de check nas features | SIM — recebe a cor de acento da marca (validada, ver seção 4c). |
| `--verde-icone-bg` | `#132315` | Fundo do quadrado atrás do ícone de check (versão escurecida do acento) | SIM — recalcular: mesma matiz do acento, ~12-15% de luminosidade (mistura do acento com o preto a ~85%). |
| `--badge-bg` | `#e4e6ff` | Pill do sprint no cronograma (versão pastel do acento frio) | SIM — versão pastel/clareada da cor de acento (~90% de luminosidade, mesma matiz). |
| `--badge-texto` | `#0079ff` | Texto dentro do pill do sprint | SIM — a cor de acento da marca (ou versão escurecida dela que passe AA sobre `--badge-bg`). |
| `--acento-quente` | `#ff8770` | Rótulo "Opcional )" na página de investimento — o ÚNICO ponto quente do deck | SIM — segunda cor da marca se existir; senão, derivar um tom quente análogo, ou reutilizar o acento principal. |

Tokens derivados recomendados (declarar também, para consistência):

```css
--card-borda:  rgba(255,255,255,0.08);  /* borda 1px dos cards escuros */
--linha-clara: #d9d9d9;                 /* linha do cronograma e divisores em páginas claras
                                           (equivale a rgba(0,0,0,0.15) sobre branco) */
--margem-x:    64px;                    /* margem lateral padrão (~5% da largura base 1280px) */
--fonte: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
```

Raio dos cards: 12–14px conforme o card (cards de toggle 14px; cards de feature e
mini-cards 12px) — sempre sutil, nunca "pílula".

---

## 2. Gramática Visual — as 9 regras e o porquê de cada uma

Estas regras NÃO são sugestões estéticas. São o mecanismo pelo qual a proposta comunica
competência e valor antes mesmo de o cliente ler uma linha. Violar uma regra barateia o deck.

**Regra 1 — Ritmo de cores.**
Capa clara → contexto claro → bloco escuro (entregáveis/produtos) → respiro cinza (opcional) →
bloco claro (cronograma) → pontuação escura (prazo) → divisória cinza → fechamento claro.
*Por quê:* a alternância claro/escuro cria capítulos perceptíveis — o leitor SENTE quando muda
de assunto sem precisar de numeração. O bloco escuro concentra a oferta (o "produto" fica em
palco escuro, como vitrine); as páginas claras dão respiro e credibilidade documental.
Divisórias de uma palavra só funcionam como respiração dramática entre atos.

**Regra 2 — Espaço em branco radical.**
Páginas com 60-80% de vazio são INTENCIONAIS. A capa é ~90% vazia. O contexto tem um único
parágrafo num quadrante.
*Por quê:* espaço em branco é o sinal visual mais barato e mais forte de percepção premium —
diz "não precisamos gritar". Encher a página comunica insegurança e barateia o preço pedido.
Se o conteúdo não cabe, a resposta é criar outra página, nunca comprimir.

**Regra 3 — Grid e margens.**
Margens laterais de ~5% da largura em todas as páginas; conteúdo alinhado a um grid implícito
de 12 colunas.
*Por quê:* o alinhamento invisível é o que faz 16 páginas diferentes parecerem UM documento.
Quando títulos, parágrafos e cards de páginas distintas caem nas mesmas colunas, o leitor
percebe rigor de execução — exatamente a promessa comercial da proposta.

**Regra 4 — Cards uniformes.**
Bordas de 1px sutis (`rgba(255,255,255,0.08)` no escuro), cantos arredondados ~12-16px,
preenchimento interno generoso, MESMA altura dentro de cada grid.
*Por quê:* uniformidade transmite sistema, não improviso. A borda sutil delimita sem pesar;
sombras e bordas grossas criariam ruído e quebrariam o flat suíço.

**Regra 5 — Toggles verdes = incluído.**
Cada entregável do sumário aparece num card com um toggle estilo iOS LIGADO na cor de acento.
*Por quê:* é uma metáfora universal ("está ativado para você") que transforma uma lista
burocrática em sensação de produto configurado e pronto. O acento aparece pouco no deck —
por isso, quando aparece, significa "isto está incluso".

**Regra 6 — Timeline com dots e alternância.**
Cronograma como linha horizontal central com pontos; conteúdo dos sprints alternando acima e
abaixo da linha (pares acima, ímpares abaixo).
*Por quê:* a alternância dobra a densidade sem parecer cheio, e a linha única comunica que o
projeto tem começo, meio e fim — sequência sob controle. Tabelas de cronograma parecem
burocracia; timelines parecem plano.

**Regra 7 — Fotografia disciplinada.**
Foto SOMENTE quando dramatiza (página do prazo/equipe). Sempre P&B/dessaturada, escurecida por
overlay preto de ~85%, texto branco por cima.
*Por quê:* foto colorida em página de proposta compete com o texto e introduz paleta fora dos
tokens. Escurecida a ~85%, ela vira textura emocional (gente trabalhando) sem quebrar o
monocromático. Uma única página com foto tem impacto; três teriam nenhum.

**Regra 8 — Rodapé fixo low-contrast.**
Todas as páginas de conteúdo levam o rodapé de 4 colunas:
`Proposta Comercial | {Marca do usuário} | © | {Ano}` — cinza discreto
(~`#b0b0b0` sobre claro; ~`#3a3a3a` sobre escuro), nunca chamando atenção.
*Por quê:* o rodapé é assinatura silenciosa e âncora de consistência — confirma em cada página
que o documento é um sistema. Low-contrast porque é metadado, não mensagem. Única página sem
rodapé: o fechamento (só o logo).

**Regra 9 — Flat, tipográfico, suíço.**
Nada de gradientes, sombras fortes, ilustrações 3D ou clip-art. A hierarquia nasce de tamanho,
peso e cor de texto — não de efeitos.
*Por quê:* efeitos datam rápido e sinalizam template genérico. Tipografia gigante bem colocada
sinaliza confiança de design. O estilo suíço é o produto: é ele que faz uma proposta de
R$ 200 mil parecer que vale R$ 200 mil.

---

## 3. Especificações por Layout (10 variantes)

Medidas em % da LARGURA da página, salvo indicação "da altura". Base: 1280×640.
Os valores com "~" são alvos aproximados; `assets/template.html` é a implementação
de referência — em caso de conflito numérico, o template prevalece.
O rodapé padrão (ver Regra 8) fica com baseline a ~92-93% da altura, texto ~1.1% da largura,
nas colunas: esquerda em 5%, centro-esquerda centrada em ~54%, "©" em ~76%, ano alinhado à
direita na margem de 95%.

### 3.1 `capa`
- Fundo: `--pagina-branca`. Sem logo no topo.
- Nome do cliente: bold, ~6.5-7% da largura (86px na base), tracking -0.02em, posicionado à
  esquerda (margem 5%), verticalmente centrado (~48-52% da altura). Sufixo "®" opcional em
  sobrescrito.
- "©" decorativo: `--texto-fantasma`, ~3% da largura, centrado horizontalmente (~62%), na
  mesma linha visual do nome.
- Ano: `--texto-fantasma`, MESMO tamanho do nome do cliente, alinhado à direita
  na margem de 95%, mesma baseline.
- Rodapé padrão presente.
- NÃO MEXER: no vazio. A capa é ~90% vazia por design. Nada de subtítulo, foto, tagline ou
  logo grande. Um elemento a mais aqui destrói a primeira impressão.

### 3.2 `contexto`
- Fundo: `--pagina-cinza` (#f8f8f8 — sutilmente diferente do branco da capa).
- Logo do usuário: line-art/monocromático, topo-direito (~2.5-3% de largura), margem 5%.
- Parágrafo único no quadrante inferior-direito: começa em ~50-55% da largura e ~55-60% da
  altura; largura de coluna ~35-40%; corpo ~1.6% da largura, line-height 1.55.
- Padrão de ênfase: texto base em `--texto-muted`, frases-chave em bold `--texto-primario`.
- Rodapé padrão presente.
- NÃO MEXER: na posição do parágrafo (inferior-direito) e no vazio dos outros 3 quadrantes.
  Não adicionar títulos — a página É o parágrafo.

### 3.3 `divisoria` (variantes dark / light / gray)
- Fundo: `--pagina-preta`, `--pagina-branca` ou `--pagina-cinza-med` conforme o ritmo.
- Uma ÚNICA palavra (ou expressão curtíssima) + ponto final: "Entregáveis.", "Cronograma.",
  "Investimento.".
- Título: ~9% da largura (112px na base), bold, tracking -0.02em, topo-esquerdo
  (margem 5%, topo ~8-12% da altura). Cor: branco sobre preto/cinza-med; preto sobre branco.
- Sem logo. Rodapé padrão presente (low-contrast adequado ao fundo).
- NÃO MEXER: uma palavra só, ponto final obrigatório, canto superior-esquerdo. Não centralizar,
  não adicionar subtítulo, não diminuir para "caber melhor" — se a palavra for longa demais,
  escolher palavra mais curta.

### 3.4 `sumario-toggles`
- Fundo: `--pagina-preta`. Logo topo-direito.
- Título da página (~5% da largura, bold, branco) no topo-esquerdo, margem 5%, topo ~8%.
- Parágrafo de apoio à direita: coluna de ~50% a ~84% da largura, topo alinhado ao título;
  corpo ~1.6%, ênfase seletiva (muted + bold branco).
- Cards de entregáveis: grid 2×2 (até 4 itens; com 5-6 itens usar 2×3), começando a
  ~56% da altura. Cada card: largura ~46% (duas colunas com gap ~2.5%), altura ~9.5-10% da
  altura da página, fundo `--card-escuro`, borda `--card-borda`, raio 14px.
- Dentro do card: toggle iOS ligado (`--verde-toggle`, largura ~2.2% da página) à esquerda +
  nome do entregável bold branco ~1.6%, alinhados verticalmente ao centro.
- Rodapé padrão presente.
- NÃO MEXER: no toggle (sempre LIGADO, sempre a cor de acento), na altura única dos cards,
  no espaço vazio entre o título e os cards.

### 3.5 `produto-features-grid`
- Fundo: `--pagina-preta`. Logo topo-direito.
- Título = nome do produto: ~5% da largura, bold branco, topo-esquerdo (margem 5%, topo ~7%).
- Grid de features: 4 colunas × 2 linhas (8 features — o ideal; aceitável 6 em grid 3×2).
  Cards: largura ~21.5% cada com gap ~2%, altura ~23% da altura da página;
  linha 1 a ~26% da altura, linha 2 a ~56%. Fundo `--card-escuro` (ou transparente com borda),
  borda 1px sutil, raio 12px.
- Dentro do card: quadrado do ícone (~3% da largura, raio ~10px, fundo `--verde-icone-bg`,
  ícone check circular em `--verde-toggle` com ~55% do quadrado) no topo; texto branco de
  2 linhas (~1.4-1.5% da largura, line-height 1.4) na base do card.
- Rodapé padrão presente.
- NÃO MEXER: máximo 8 cards; textos de NO MÁXIMO 2 linhas (cortar copy, não fonte); o mesmo
  ícone check em todos (a variação fica no texto, não no ícone).

### 3.6 `opcional-2col`
- Fundo: `--pagina-cinza-med` (#b8b8b8). Logo topo-direito (branco/line-art).
- Título branco em até 2 linhas, ~4.5% da largura, topo-esquerdo; rótulo "(Opcional)" logo
  abaixo em branco translúcido (`rgba(255,255,255,0.55)`), ~1.9%.
- Coluna central de texto (de ~46% a ~72% da largura): 2 blocos, cada um com título bold
  branco ~1.9% + corpo ~1.5% em branco translúcido; blocos separados por linha horizontal
  sutil (`rgba(255,255,255,0.3)`). Divisor vertical sutil entre coluna central e direita.
- Coluna direita (de ~75% a ~97%): título bold branco ~1.9% + pilha de até 5 mini-cards
  (altura ~9% da altura da página, borda 1px `rgba(255,255,255,0.35)`, raio ~12px), cada um
  com quadrado de ícone line-art branco (~2.4%) + texto bold branco ~1.3% em até 2 linhas.
- Rodapé padrão presente.
- NÃO MEXER: fundo cinza-médio com texto TODO branco (é o "respiro" do deck — não escurecer,
  não colorir); máximo 5 mini-cards.

### 3.7 `cronograma-timeline`
- Fundo: `--pagina-branca`. Logo topo-direito.
- Título "Cronograma." (COM ponto final) ~5.5% da largura, bold preto, topo-esquerdo —
  apenas na PRIMEIRA página de cronograma; páginas de continuação omitem o título.
- Linha do tempo: horizontal, y = ~50% da altura, cor `--linha-clara` (#d9d9d9), atravessando de
  0 a 100% da largura (pode iniciar em dashed antes do primeiro dot); dots (~0.55% de
  diâmetro, cinza `#c9c9c9`) marcando cada sprint.
- 4 sprints por página, alternando: ímpares ABAIXO da linha, pares ACIMA. Cada bloco de
  sprint ocupa coluna de ~25-30% da largura, alinhado ao seu dot.
- Badge pill: fundo `--badge-bg`, raio pill, padding ~0.6%/1%; texto "Sprint NN" bold +
  separador + "X-Y Dias", em `--badge-texto`, ~1.3% da largura.
- Título do sprint: bold preto, ~1.9%, logo abaixo (ou acima, nos blocos superiores) do badge.
- Bullets: até 5 por sprint, ~1.35%, `--texto-muted`, com ícone prefixo discreto (⊛ / ✳
  line-art cinza), line-height ~1.9.
- Rodapé padrão presente.
- NÃO MEXER: na alternância acima/abaixo (é ela que evita a cara de tabela); máximo
  4 sprints por página — 5 a 8 sprints = segunda página de cronograma, mesmo layout sem título.

### 3.8 `prazo-foto`
- Fundo: foto P&B (pessoas trabalhando/contexto do projeto), dessaturada, coberta por
  overlay preto de ~85% de opacidade (a foto deve ser percebida, não lida).
- Título ("O Prazo") branco bold, ~4.5% da largura, topo-esquerdo. Logo topo-direito.
- Parágrafo no quadrante inferior-direito: coluna de ~50% a ~84% da largura, iniciando a
  ~55% da altura; corpo ~1.6%, texto base em cinza-claro (`rgba(255,255,255,0.72)`) com
  ênfase bold branca nos números e compromissos ("prazo total de 90 dias").
- Segundo parágrafo opcional ("Obs.: ...") separado por linha em branco.
- Rodapé padrão presente (versão low-contrast clara).
- NÃO MEXER: overlay nunca abaixo de ~80% (texto precisa passar contraste AA sobre qualquer
  área da foto); foto sempre monocromática; sem créditos de foto visíveis.

### 3.9 `investimento-tabela`
- Fundo: `--pagina-branca` (ou `--pagina-cinza`). Logo topo-direito.
- Título ("Investimento") ~5.5% da largura, bold preto, topo-esquerdo.
- Coluna esquerda (margem 5% até ~45%), iniciando a ~50% da altura: frase principal ~1.9%
  com padrão de ênfase (muted + bold preto nos valores e condições); subtexto ~1.4% muted
  ("sem surpresas ou custos adicionais"); depois a linha do opcional: rótulo
  "Opcional )" em `--acento-quente` + texto muted ~1.4% descrevendo o recorrente mensal.
- Coluna direita (de ~50% a ~96.5%): tabela de linhas — cada linha com item bold preto
  ~1.9% à esquerda e preço bold preto alinhado à DIREITA; separadores `1px dashed`
  em cinza claro (#cccccc); altura de linha ~11% da altura da página.
- Linha final "Investimento Total": separada por borda SÓLIDA mais forte acima, item e valor
  em bold, mesmo corpo ou levemente maior.
- Rodapé padrão presente.
- NÃO MEXER: alinhamento dos preços à direita (escaneabilidade); dashed nas linhas comuns e
  sólida apenas antes do total; o acento quente aparece SÓ no rótulo do opcional — nunca nos
  valores.

### 3.10 `fechamento-logo`
- Fundo: `--pagina-branca`.
- Apenas o logo do usuário, centralizado (horizontal e vertical), em `--texto-fantasma` ou
  cinza-claro equivalente, com ~6-8% da largura.
- SEM rodapé. SEM texto. SEM CTA.
- NÃO MEXER: é a única página sem rodapé; a ausência de "chamada final" é intencional —
  o silêncio fecha a proposta com a mesma confiança da capa.

---

## 4. Protocolo de Adaptação de Marca

Executar ANTES de gerar o HTML. O resultado é um "brand-config" (mapa de tokens + fonte +
logo + modo claro/escuro) que parametriza o template.

### (a) Extrair a marca dos materiais do usuário

1. **Site (via WebFetch)**: buscar no HTML/CSS retornado: cores de fundo e de acento
   (procurar custom properties, cores de botões/links), família tipográfica declarada
   (`font-family` de headings e corpo), URL do logo (`<img>` no header, `og:image`,
   favicon SVG). Anotar se o site é dark-first (fundo global escuro).
2. **Logo (SVG/PNG fornecido)**: extrair a(s) cor(es) dominante(s) — em SVG, ler os `fill`;
   em PNG, perguntar ao usuário o hex se não for óbvio. Verificar se existe versão
   monocromática/line-art (ideal para o topo-direito das páginas). Se só houver logo colorido
   e pesado, preferir usar o NOME da marca tipografado (bold, na fonte do deck) ou um
   monograma tipográfico gerado.
3. **Brand guide (PDF)**: ler e extrair: paleta oficial (primária, secundária, neutros),
   tipografia oficial e usos, regras de logo (margens de proteção, versões). O brand guide
   TEM PRIORIDADE sobre o que for inferido de site/logo.
4. **Fonte**: se a fonte da marca existir no Google Fonts, usar com fallback no stack padrão
   (`'FonteDaMarca', 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif`). Se for
   proprietária sem equivalente, escolher a grotesca do Google Fonts mais próxima
   (Inter, Manrope, Archivo, Space Grotesk...) e AVISAR o usuário da substituição.
5. Sem materiais nenhum: entrevista mínima (3-6 perguntas) ou herdar o default monocromático
   integral (que é elegante por si só — melhor default limpo do que acento inventado).

### (b) Mapear a cor da marca APENAS para papéis de acento

- A cor primária da marca substitui: `--verde-toggle`, `--badge-texto` e os ícones de check.
- Derivar: `--verde-icone-bg` = acento a ~12-15% de luminosidade (mistura com preto ~85%);
  `--badge-bg` = acento a ~90% de luminosidade (versão pastel).
- `--acento-quente` recebe a cor secundária da marca, se houver; senão um análogo quente,
  ou o próprio acento principal.
- **Fundos NÃO mudam.** `--pagina-branca`, `--pagina-preta`, `--pagina-cinza`,
  `--pagina-cinza-med` e `--card-escuro` permanecem neutros. O estilo suíço monocromático
  com acento pontual É o produto — pintar fundos com a cor da marca transforma a proposta
  em panfleto. A marca aparece no acento, no logo e no rodapé; isso basta.

### (c) Validar contraste (WCAG AA)

- Textos: mínimo 4.5:1 contra o fundo (3:1 para texto grande, >= ~24px/19px bold).
- Testar o acento nos contextos onde ele carrega informação:
  - `--badge-texto` sobre `--badge-bg`;
  - ícone check sobre `--verde-icone-bg`;
  - `--acento-quente` sobre fundo claro.
- Se a cor de acento falhar sobre fundo ESCURO (ex.: azul-marinho da marca sobre `#000000`):
  CLAREAR a cor (aumentar luminosidade mantendo a matiz) até passar. O toggle e os ícones
  precisam "acender" sobre o preto.
- Se falhar sobre fundo CLARO (ex.: amarelo): escurecer para os usos sobre branco
  (`--badge-texto`, `--acento-quente`) mantendo a versão viva para os usos sobre preto.
  É legítimo ter duas variantes do acento (sobre-claro / sobre-escuro) — documentar ambas
  no brand-config.
- **NUNCA usar o acento como cor de corpo de texto.** Acento é para toggle, badge, ícone e
  rótulo curto. Parágrafos são sempre preto/branco/muted.
- `--texto-muted` (#a5a5a5) está no limite de AA para corpo pequeno: usar apenas em textos
  >= 1.4% da largura e nunca para informação crítica (preços, prazos ficam em bold primário).

### (d) Modo dark-first

Se a marca do usuário for dark-first (site escuro, brand guide dark), inverter o ritmo de
páginas: capa preta (nome do cliente em branco, ano em cinza-escuro fantasma ~`#1c1c1c`),
contexto quase-preto (`#0f0f0f` no papel do `--pagina-cinza`), bloco de produtos pode ir a
claro OU permanecer escuro com divisórias claras fazendo a pontuação invertida, cronograma
segue legível (se mantido escuro, badge pastel vira badge translúcido
`rgba(acento, 0.15)` com texto no acento clareado), fechamento preto com logo em
cinza-escuro. As REGRAS não mudam: continua havendo alternância de capítulos, espaço radical,
rodapé low-contrast (agora ~`#3a3a3a`), cards com borda sutil. Dark-first é espelhamento do
ritmo, não um design novo.

### (e) Quando o usuário pede para fugir do estilo suíço

Se o usuário pedir explicitamente algo fora do design system (fundos coloridos, gradientes,
estilo "vibrante", ilustrações): **obedecer** — a proposta é dele. Mas antes de gerar,
avisar em uma frase objetiva, por exemplo:

> "Posso fazer. Só registrando: isso sai do design system validado (estilo suíço da proposta
> de referência), então a garantia de consistência visual passa a ser menor. Confirma?"

Confirmado, gerar o que foi pedido mantendo o que ainda se aplicar (grid, margens, rodapé,
hierarquia tipográfica, contraste AA). Registrar no brand-config que o deck está em modo
"fora do padrão" para que iterações futuras não tentem "corrigir" de volta sem o usuário pedir.

---

## 5. Tipografia

**Stack**: `'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif` (grotesca neo-suíça,
Helvetica Now-like). Carregar Inter via Google Fonts com fallback graceful — o deck deve
continuar correto se a fonte não carregar. Pesos usados: 400 (corpo), 500 (apoios), 700
(títulos e ênfases). Nada de itálico, nada de light/thin.

**Escala (em % da largura da página; base 1280px entre parênteses):**

| Papel | Tamanho | Peso | Tracking | Observações |
|---|---|---|---|---|
| Título de divisória | ~9% (≈112px; reduza só se a palavra não couber) | 700 | -0.02em | SEMPRE com ponto final. Uma palavra. |
| Nome do cliente na capa / ano fantasma | ~6.5-7% (≈86px) | 700 | -0.02em | Ano em `--texto-fantasma`, MESMO tamanho do nome. |
| Título de página de conteúdo | ~5% (≈64px; até ~6.5% em páginas de 1 título) | 700 | -0.02em | Topo-esquerdo, margem 5%. |
| Título de seção interna (colunas, sprints) | ~1.9% (≈24px) | 700 | normal | |
| Corpo | 1.5-1.7% (≈19-22px) | 400 | normal | line-height 1.5-1.6. |
| Bullets / mini-cards / badge | ~1.3-1.4% (≈17-18px) | 400-700 | normal | badge em 700. |
| Rodapé | ~1.1% (≈14px) | 400 | normal | low-contrast sempre. |

**Regra do ponto final**: títulos de DIVISÓRIA terminam com ponto final ("Entregáveis.",
"Cronograma.", "Investimento.") — o ponto transforma a palavra em afirmação. Títulos de
páginas de conteúdo NÃO levam ponto ("Agente CS", "O Prazo", "Investimento" na página da
tabela). Não aplicar ponto final em nomes de produto nem em itens de card.
Exceção única (herdada da referência): a PRIMEIRA página de cronograma-timeline repete o
título "Cronograma." COM ponto final (ver 3.7); as páginas de continuação não têm título.

**Padrão de ênfase (assinatura tipográfica do deck)**: parágrafos em `--texto-muted` com os
trechos-chave em bold na cor primária (preto no claro, branco no escuro). O leitor apressado
deve conseguir ler SÓ os bolds e entender a proposta: promessa, prazo, preço. Ao escrever
copy, escolher os bolds deliberadamente (valores, entregas, compromissos) — nunca bold em
frase inteira, nunca mais de ~30% do parágrafo em bold.

**Alinhamento**: tudo alinhado à esquerda (exceto preços da tabela de investimento, à direita,
e o ano da capa/rodapé, à direita). Nunca centralizar parágrafos. Nunca justificar.

---

## 6. Anti-padrões Visuais (proibições)

Se qualquer item abaixo aparecer no HTML gerado, é bug de design — corrigir antes de mostrar:

1. **Gradientes chamativos** (fundos degradê, texto com gradiente, glassmorphism). O deck é
   flat. Único "gradiente" tolerado: overlay escuro uniforme sobre a foto do prazo.
2. **Sombras pesadas** (`box-shadow` visível, drop-shadows em cards ou títulos). Cards se
   separam do fundo por borda de 1px e diferença de tom — nunca por sombra.
3. **Clip-art, ilustrações 3D, stock icons coloridos**. Ícones são line-art monocromáticos
   ou o check no quadrado de acento. Fotografia só na página de prazo, P&B com overlay.
4. **Emojis como ícones** (em cards, bullets, títulos ou rodapé). Além de quebrarem a
   estética suíça, quebram a renderização consistente entre navegador e PDF.
5. **Mais de 1 cor de acento por papel**: um acento para "incluído/positivo"
   (toggle, checks, badges) e no máximo um acento quente para "opcional". Três ou mais cores
   vivas = panfleto. Se a marca tem 5 cores, escolher 1 (máximo 2) e ignorar o resto.
6. **Texto justificado** (`text-align: justify`) ou parágrafos centralizados. Alinhamento à
   esquerda, bandeira à direita, sempre.
7. **Mais de 8 cards por página** (ou mais de 4 sprints por página de cronograma, ou mais de
   5 mini-cards na coluna do opcional). Estourou? Cria-se outra página — nunca encolher
   cards ou fonte para caber.
8. Derivados diretos das regras (igualmente proibidos): encher o vazio das divisórias/capa
   com conteúdo; usar o acento em corpo de texto; colorir fundos com a cor da marca;
   rodapé em alto contraste; fotos coloridas ou sem overlay.


## Referência: references/estrutura-narrativa.md

# Estrutura Narrativa do Deck de Proposta

> Referência para a FASE 3 (arquitetura de conteúdo). Leia este arquivo ANTES de mapear
> o brief em páginas e ANTES de escrever qualquer texto do deck. O arco descrito aqui
> vem da proposta de referência (Proposta_XFlow, 16 páginas) e é o padrão da skill.
> Design e tokens visuais ficam em `design-system.md` — aqui o assunto é NARRATIVA e COPY.

---

## 1. O arco de 16 páginas da referência (papel persuasivo de cada página)

A proposta não é um documento: é uma apresentação de vendas silenciosa. Cada página tem
UM trabalho persuasivo. Se uma página tenta fazer dois trabalhos, divida em duas.
Se não tem trabalho nenhum, corte.

| # | Página | Papel persuasivo | Como cumpre esse papel |
|---|--------|------------------|------------------------|
| 1 | **Capa** (branca) | **Autoridade minimalista.** Primeira impressão: "quem manda isso é gente séria". | Só o nome do cliente em tipografia gigante, "©" e o ano em cinza-fantasma. Zero venda, zero enfeite. A confiança nasce da contenção. |
| 2 | **Contexto** (cinza claro) | **Conexão e promessa.** Diz quem é o proponente e o que vai acontecer na vida do cliente. | Um único parágrafo no quadrante inferior-direito, resto da página vazio. Frases-chave em bold preto dentro de texto cinza. É a única página "sobre nós" do deck inteiro. |
| 3 | **Divisória "Entregáveis."** (preta) | **Respiro e drama.** Muda o assunto com um corte de cena. Prepara o cérebro para a parte mais importante. | Uma palavra gigante branca com ponto final, página inteira preta. Nada mais. |
| 4 | **Sumário de entregáveis** (preta) | **Tangibilizar a oferta.** O cliente vê, num relance, TUDO que vai receber. | Cards com toggle verde "ligado" + nome de cada produto. A metáfora do toggle diz: "isso já está incluso, já está ativado para você". Parágrafo de apoio à direita com bolds seletivos. |
| 5-8 | **Uma página por produto** (pretas) | **Profundidade sem sobrecarregar.** Prova que cada item do sumário é substância, não bullet vazio. | Título = nome do produto. Grid de 8 cards de features (4×2), cada um com check verde + texto de 2 linhas. Uma página = um produto. Nunca dois produtos na mesma página. |
| 9 | **Opcional / upsell** (cinza médio) | **Upsell sem pressão.** Planta a semente do recorrente sem contaminar a oferta principal. | Rótulo "(Opcional)" explícito abaixo do título. Fundo cinza médio = deliberadamente fora do ritmo preto/branco, sinalizando "isto é um anexo, não uma condição". |
| 10 | **Divisória "Cronograma."** (branca) | **Respiro.** Fecha o bloco da oferta, abre o bloco da execução. | Uma palavra preta gigante com ponto final. |
| 11 | **Cronograma parte 1** (branca) | **Confiança na execução.** Mostra que existe método: quem detalha sprint por sprint já fez isso antes. | Timeline horizontal com dots; sprints alternando acima/abaixo da linha. Badge pill com "Sprint NN + faixa de dias", título bold, 3-5 bullets de atividades. Sprints 01-04. |
| 12 | **Cronograma parte 2** (branca) | Continuação do mesmo argumento. | Mesmo layout, sprints 05-08. Sem repetir o título "Cronograma". |
| 13 | **Prazo** (preta, foto de fundo escurecida) | **Expectativa administrada.** Um número de prazo claro + a observação de que pode chegar antes. Sob-promete, sobre-entrega. | Foto P&B de equipe trabalhando com overlay escuro (~85%). Parágrafo no quadrante inferior-direito com o prazo total em bold. Única página com fotografia do deck. |
| 14 | **Divisória "Investimento."** (cinza médio) | **Respiro antes do preço.** A pausa evita que o preço apareça "de supetão" e dá peso cerimonial ao momento. | Uma palavra branca gigante com ponto final sobre fundo cinza médio. |
| 15 | **Investimento** (branca) | **Ancoragem e clareza.** O total já foi ancorado item a item; a tabela prova que o número é a soma de coisas concretas. | Esquerda: frase do total em bold + "sem surpresas ou custos adicionais" + linha do opcional mensal em cor de acento quente. Direita: tabela item/preço com linhas tracejadas e "Investimento Total" em bold com borda sólida acima. Preço NUNCA aparece antes desta página. |
| 16 | **Fechamento** (branca) | **Elegância.** Termina como começou: com contenção. Sem CTA agressivo, sem "aproveite agora". | Só o logo centralizado em cinza-claro. Sem rodapé. O silêncio final é a assinatura. |

### Princípios do arco (por que essa ordem funciona)

1. **Valor antes do preço.** O cliente atravessa entregáveis → profundidade → método → prazo
   antes de ver um único número. Quando o preço chega, ele já sabe o que está pagando.
2. **Divisórias são pausas de respiração.** Três divisórias de uma palavra (Entregáveis. /
   Cronograma. / Investimento.) dividem o deck em três atos: OFERTA → EXECUÇÃO → COMERCIAL.
3. **Ritmo de cor conta a história junto.** Claro (abertura) → preto (oferta, o "palco
   principal") → cinza (anexo opcional) → claro (execução) → preto pontual (prazo) →
   cinza (pausa) → claro (preço e fechamento). Ver `design-system.md`.
4. **O deck fala sozinho.** Ele será lido sem o vendedor presente. Cada página precisa
   ser compreendida em menos de 10 segundos.

---

## 2. Variantes de deck (escolher pelo tamanho da oferta)

Escolha a variante ANTES de montar o sumário de páginas e apresente ao usuário para
aprovação. Na dúvida entre duas, escolha a menor: página a menos vende mais que página a mais.

| | **Deck compacto** | **Deck padrão** | **Deck extenso** |
|---|---|---|---|
| Total de páginas | 8-10 | 12-16 | 16-20 |
| Quando usar | 1-2 produtos, oferta simples, ticket menor, cliente que já conhece o proponente | 3-5 produtos, projeto multi-fase (referência XFlow) | 5+ produtos OU venda que exige prova social (cliente novo, ticket alto, concorrência) |
| Capa | 1 | 1 | 1 |
| Contexto | 1 | 1 | 1 (pode ganhar 1 página extra de "quem somos" com números da empresa) |
| Divisória Entregáveis. | opcional (cortar se o deck ficar < 9 p.) | 1 | 1 |
| Sumário de entregáveis (toggles) | 1 (se houver 2 produtos) ou 0 (se houver 1 só) | 1 | 1 |
| Páginas de produto | 1-2 | 3-5 | 5-7 |
| Opcional/upsell | 0-1 | 0-1 | 0-2 |
| Divisória Cronograma. | 0 (ir direto à timeline) | 1 | 1 |
| Cronograma (timeline) | 1 | 1-2 | 2-3 |
| Prazo | 1 (pode fundir com a última página de cronograma se apertar) | 1 | 1 |
| Divisória Investimento. | opcional | 1 | 1 |
| Investimento | 1 | 1 | 1 |
| Páginas extras (cases, depoimentos, garantia) | 0 | 0 | 1-3 (ver abaixo) |
| Fechamento | 1 | 1 | 1 |

### Páginas extras do deck extenso (Bloco F) e onde entram no arco

Só existem se o usuário fornecer o material (regra de ouro: nunca inventar case,
depoimento ou garantia).

| Página extra | Papel persuasivo | Posição no arco |
|---|---|---|
| **Cases / resultados** | Prova social por números ("reduzimos X% do tempo de resposta"). | Depois do Contexto e ANTES da divisória "Entregáveis." — prova quem fala antes de mostrar o que vende. |
| **Depoimentos** | Prova social por voz de terceiros. | Junto dos cases (mesma zona do arco), ou 1 página entre Prazo e a divisória "Investimento." como último empurrão antes do preço. |
| **Garantia** | Reversão de risco. | Imediatamente APÓS a página de Investimento — responde à objeção no momento em que ela nasce. Nunca antes do preço. |

Ritmo de cor das extras: cases/depoimentos em página clara ou preta conforme o bloco onde
caem; garantia clara, sóbria, sem parecer selo de infomercial.

---

## 3. Regras de mapeamento brief → páginas

Aplicar nesta ordem, depois de preencher os blocos A-F da descoberta:

1. **Produtos → páginas de produto.** 1 produto = 1 página, sempre. Cada página pede
   6-8 features (ideal 8, para o grid 4×2). Se um produto tem menos de 4 features
   relevantes, pergunte ao usuário se ele é mesmo um produto separado ou uma feature
   de outro — não gere página rala.
2. **Sumário de toggles.** Existe se houver 2+ produtos. Com 1 produto só, a página do
   produto assume o papel de sumário. Layout dos cards: 2 produtos = 1 linha; 3-4 = grade
   2×2; 5-6 = grade 2×3. Acima de 6 produtos, questione o escopo com o usuário.
3. **Sprints → páginas de cronograma.** 4 sprints por página (2 acima, 2 abaixo da linha).
   1-4 sprints = 1 página; 5-8 = 2 páginas; 9-12 = 3 páginas. Cada sprint: badge com
   número + faixa de dias, título de 2-5 palavras, 3-5 bullets de atividades. Se o brief
   trouxer fases sem duração, pergunte as faixas de dias — nunca invente.
4. **Página de opcional.** SÓ existe se o brief tiver upsell/oferta opcional (Bloco C).
   Sem upsell, a página não existe e a linha de opcional some também do Investimento.
   Com upsell, ele aparece exatamente 2 vezes no deck: na página de opcional (detalhe)
   e na página de investimento (preço, marcado com o acento quente).
5. **Página de prazo.** Existe se houver prazo total declarado (Bloco D). O prazo total
   deve bater com a soma das faixas dos sprints — se não bater, alerte o usuário antes
   de gerar.
6. **Investimento.** Sempre 1 página. A tabela lista cada item com preço + linha final
   "Investimento Total". A soma dos itens DEVE ser igual ao total — confira aritmética
   antes de gerar. Condições de pagamento (à vista, parcelas) entram na frase à esquerda,
   não na tabela.
7. **Divisórias.** Deck padrão/extenso: 3 divisórias (Entregáveis. / Cronograma. /
   Investimento.). Deck compacto: cortar primeiro a de Cronograma, depois a de
   Investimento; a de Entregáveis é a última a cair.
8. **Capa, contexto e fechamento existem sempre**, em qualquer variante.
9. **Ordem fixa dos atos:** abertura → oferta → execução → comercial → fechamento.
   Nunca mostrar preço antes do valor; nunca colocar cronograma antes dos entregáveis.

Depois de aplicar as regras, gere o SUMÁRIO DE PÁGINAS (lista numerada: nº, tipo, conteúdo
de cada página) e mostre ao usuário para aprovação ANTES de escrever o HTML.

---

## 4. Diretrizes de copywriting (pt-BR)

### Tom
- **Direto e confiante.** Quem escreve já resolveu esse problema antes e não precisa
  provar nada gritando. Afirmações, não promessas hiperbólicas.
- **Frases curtas.** Uma ideia por frase. Se a frase pede vírgula duas vezes, quebre em duas.
- **Parágrafos de 2-4 frases**, no máximo ~50 palavras. O deck tem muito espaço vazio
  de propósito — texto longo destrói o design e a persuasão ao mesmo tempo.
- Tratamento: "você/sua empresa" para o cliente; "nós" para o proponente, com parcimônia.

### Padrão de ênfase (assinatura tipográfica do deck)
Parágrafos em cinza muted com os trechos-chave em **bold na cor primária** (preto no claro,
branco no escuro). Regras:
- 1 a 2 trechos em bold por parágrafo, nunca mais.
- O bold marca o trecho que sobrevive se o leitor só passar o olho: a promessa, o número,
  o prazo, o preço.
- Teste: leia apenas os bolds da página — eles devem contar a história sozinhos.
- Nunca aplicar bold em parágrafo inteiro (vira grito) nem deixar página de texto sem
  nenhum bold (vira ruído).

### Títulos
- Divisórias: UMA palavra, primeira letra maiúscula, **sempre com ponto final**.
  "Entregáveis." / "Cronograma." / "Investimento." O ponto final é afirmação, não detalhe.
- Títulos de página de conteúdo: substantivo direto, 1-4 palavras, sem ponto final
  ("Agente CS", "O Prazo", "Investimento"). Exceção única, herdada da referência: a
  primeira página de cronograma repete o título "Cronograma." COM ponto final (as
  páginas de continuação não têm título). Nada de títulos-frase ("Conheça nossos
  incríveis entregáveis").
- Features (cards): fragmento nominal de até 2 linhas, começando por substantivo ou verbo
  no infinitivo. Sem ponto final nos cards.

### Números sempre concretos
Todo claim quantificável usa o número real do brief:
- Certo: "atendimento **24/7** com interações simultâneas ilimitadas".
- Errado: "atendimento incrível a qualquer hora".
- Certo: "prazo total de **90 dias**", "**R$ 200 mil** à vista, para construção dos 6 projetos".
- Errado: "entrega rápida", "investimento acessível".
Se não houver número no brief, pergunte ou escreva o benefício concreto sem número —
nunca invente estatística ("aumente suas vendas em 300%").

### Proibições (lista de bloqueio)
- **Clichês de IA / marketing inflado:** "revolucione", "desbloqueie", "impulsione sua
  jornada", "eleve seu negócio a outro patamar", "transforme sua realidade", "potencialize
  resultados exponenciais", "solução disruptiva", "sinergia", "mergulhe", "e muito mais".
- **Superlativos vazios:** "incrível", "extraordinário", "único no mercado", "o melhor do
  Brasil", "de última geração" — a menos que citando prêmio/fato verificável do brief.
- **Parágrafos longos** (mais de 4 frases ou ~50 palavras).
- **Exclamações.** Zero "!" no deck inteiro.
- **Emojis** em qualquer texto do deck.
- **Jargão sem tradução:** termo técnico só se o cliente da proposta o usa; senão,
  explique em palavras simples ("agente que responde no WhatsApp" em vez de
  "orquestração conversacional multicanal").
- **Promessa não autorizada:** nenhum resultado, prazo, preço ou feature que não esteja
  no brief ou tenha sido confirmado pelo usuário.

---

## 5. Checklist de completude de conteúdo (antes de gerar o HTML)

Percorra TODOS os itens. Qualquer item faltante = perguntar ao usuário antes de gerar.
Nunca preencher lacuna com invenção.

**Bloco A — Quem vende (usuário da skill)**
- [ ] Nome/marca do proponente (como aparece no rodapé e no contexto)
- [ ] Descrição de 1-2 frases do que a empresa faz (página de contexto)
- [ ] Logo (arquivo SVG/PNG) ou decisão registrada de usar monograma tipográfico
- [ ] Tom de voz / restrições de marca (se houver)

**Bloco B — Para quem (cliente da proposta)**
- [ ] Nome da empresa cliente exatamente como vai na capa
- [ ] Setor/contexto e dor principal (alimenta o parágrafo de contexto e o sumário de entregáveis)

**Bloco C — Oferta**
- [ ] Lista fechada de produtos/serviços (nomes finais)
- [ ] 6-8 features por produto, com números concretos onde existirem
- [ ] Upsell/opcional definido (existe ou não; se existe: nome, escopo, preço, recorrência)

**Bloco D — Execução**
- [ ] Sprints/fases com título, faixa de dias e 3-5 atividades cada
- [ ] Prazo total declarado e coerente com a soma dos sprints
- [ ] Observações de prazo (ex.: possibilidade de entrega antecipada), se houver

**Bloco E — Comercial**
- [ ] Preço de cada item da tabela
- [ ] Total conferido (soma dos itens = Investimento Total)
- [ ] Condição de pagamento (à vista / parcelado / "3x", etc.)
- [ ] Preço e recorrência do opcional (se o Bloco C tiver opcional)

**Bloco F — Extras (apenas deck extenso)**
- [ ] Cases com números reais fornecidos pelo usuário (ou item marcado como "não haverá")
- [ ] Depoimentos com autor identificado e autorização implícita (ou "não haverá")
- [ ] Texto de garantia exato fornecido pelo usuário (ou "não haverá")

**Estrutura**
- [ ] Variante escolhida (compacto / padrão / extenso) e justificada
- [ ] Sumário de páginas montado com as regras da seção 3
- [ ] Sumário aprovado pelo usuário ANTES de gerar o HTML

**Copy**
- [ ] Todos os textos passam nas proibições da seção 4 (sem clichês, sem superlativos vazios, sem "!")
- [ ] Bolds seletivos aplicados (1-2 por parágrafo) e "teste dos bolds" feito por página
- [ ] Títulos de divisória com ponto final; títulos de conteúdo sem
- [ ] Nenhum preço, prazo ou feature inventado — tudo rastreável ao brief


## Referência: references/qa-checklist.md

# QA Checklist — controle de qualidade pré-entrega

**Rode este checklist SEMPRE antes de entregar a proposta ao usuário** — tanto na primeira
versão quanto após qualquer rodada de ajustes. Nenhuma proposta é considerada pronta sem
os três blocos verificados (Técnica, Visual, Comercial).

Ao terminar, **reporte o resultado ao usuário** em formato compacto:

```
QA da proposta — resultado
Tecnica:   X/Y ok
Visual:    X/Y ok
Comercial: X/Y ok
Pendencias: <lista do que falhou e o que foi feito, ou "nenhuma">
```

Itens que falharem devem ser corrigidos e re-verificados antes da entrega. Itens do bloco
COMERCIAL que dependam de confirmação do usuário (valores, promessas) **bloqueiam a
entrega** até a resposta dele.

---

## 1. TÉCNICA

Verificações sobre o arquivo HTML e o PDF exportado.

- [ ] **HTML abre sem erros**: abrir o arquivo no navegador (`start <arquivo>.html`) e
      conferir que renderiza; sem erros no console (F12) que afetem o layout.
- [ ] **Proporção das sections**: todas as `<section class="page">` têm a proporção 2:1
      (1280×640 base) — nenhuma página esticada, cortada ou com altura diferente das demais.
- [ ] **Contagem de páginas na impressão**: o PDF gerado tem **exatamente N páginas**,
      onde N = número de `<section>` no HTML. Sem páginas em branco extras no meio ou no
      fim (causa comum: margem/overflow empurrando conteúdo — corrigir com
      `page-break-after` e `@page { margin: 0 }`). Usar `scripts/html2pdf.py --check`.
- [ ] **Cores de fundo na impressão**: fundos pretos/cinzas aparecem no PDF
      (`-webkit-print-color-adjust: exact` / `print-color-adjust: exact` presentes; se a
      exportação for manual, "Gráficos de fundo" marcado).
- [ ] **Fontes**: a fonte principal carrega; se a Google Font falhar (sem internet), o
      fallback do stack (`Helvetica Neue, Helvetica, Arial, sans-serif`) mantém o deck
      legível e sem quebra de layout.
- [ ] **Zero texto vazando**: nenhum texto escapa de card, tabela, badge ou section —
      conferir especialmente nomes longos de produto nos cards de feature, valores na
      tabela de investimento e títulos gigantes das divisórias.
- [ ] **PDF final conferido página a página**: abrir o PDF exportado e passar por TODAS as
      páginas, uma a uma, comparando com o HTML. Não entregar PDF que não foi aberto.

## 2. VISUAL

Fidelidade ao design system (ver `design-system.md`) e ao brand-config do usuário.

- [ ] **Tokens respeitados**: cores usadas são exatamente as do brand-config/tokens
      (fundos, muted, acentos) — nenhuma cor "aproximada" inventada durante a geração.
- [ ] **Rodapé em todas as páginas exceto o fechamento**: 4 colunas
      ("Proposta Comercial" | marca do usuário | "©" | ano), low-contrast, presente em
      todas as sections menos a última (fechamento com logo centralizado).
- [ ] **Ênfase bold com parcimônia**: parágrafos em cinza muted com apenas trechos-chave
      em bold — se mais da metade de um parágrafo está em bold, a ênfase morreu; reescrever.
- [ ] **Nenhum placeholder esquecido**: buscar no HTML por `{{`, `}}`, "LOREM", "TODO",
      "Studio Vetor", "Café Aurora" (conteúdo de exemplo do template) — zero ocorrências.
- [ ] **Logo correto**: logo do usuário (ou monograma acordado) nas páginas de conteúdo,
      no tamanho/posição do padrão (topo-direito); nunca o logo de exemplo do template.
- [ ] **Ano correto**: capa e rodapé exibem o ano atual (ou o ano informado pelo usuário)
      — não o ano do template.
- [ ] **Ritmo de fundos respeitado**: a alternância claro → escuro → respiro → claro →
      pontuação escura segue o arco definido em `estrutura-narrativa.md`; divisórias de
      uma palavra com ponto final ("Entregáveis.", "Cronograma.", "Investimento.");
      nenhuma sequência longa de páginas iguais que quebre o drama do deck.

## 3. COMERCIAL

O bloco mais crítico: erro aqui custa dinheiro ou credibilidade do usuário.

- [ ] **Valores conferidos com o usuário**: todos os preços exibidos foram informados ou
      confirmados por ele — nenhum valor estimado ou "completado".
- [ ] **Soma da tabela bate com o total**: somar linha a linha a tabela de investimento e
      conferir contra o "Investimento Total". Atenção a multiplicadores ("3x R$ 40.000"):
      confirmar com o usuário se é quantidade (entra 120.000 na soma) ou parcelamento —
      se a soma não bater, **parar e perguntar**, nunca ajustar um número por conta própria.
- [ ] **Nomes grafados corretamente em TODAS as ocorrências**: nome da empresa cliente e
      nome/marca do usuário — capa, contexto, rodapés, tabela, texto corrido. Buscar cada
      variação de grafia no HTML para garantir consistência (ex.: "XFlow" vs "Xflow").
- [ ] **Features correspondem ao que foi vendido**: cada card de feature veio do brief
      confirmado — nenhuma feature adicionada, renomeada ou "melhorada" na geração.
- [ ] **Prazo consistente**: a soma/duração dos sprints do cronograma é compatível com o
      prazo total da página de prazo (ex.: sprints somando 90 dias ↔ "prazo de 90 dias").
      Datas ou faixas de dias sem contradição entre páginas.
- [ ] **Condições de pagamento explícitas**: a página de investimento diz claramente como
      se paga (à vista, parcelas, entrada) e o que está incluído; opcionais marcados como
      opcionais, com valor e recorrência ("R$ X/mês") corretos.
- [ ] **Nenhuma promessa que o usuário não fez**: varrer o texto por garantias, prazos de
      resposta, SLAs, resultados prometidos ("aumento de X%", "sem custos adicionais") —
      cada afirmação dessas precisa existir no brief confirmado; o que não veio dele, sai.

---

## Regra final

Se qualquer item comercial estiver em dúvida, a resposta certa nunca é "provavelmente está
certo" — é perguntar ao usuário. Uma proposta atrasada em cinco minutos é melhor que uma
proposta entregue com o preço errado.


## Referência: scripts/html2pdf.py

```python
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
```
