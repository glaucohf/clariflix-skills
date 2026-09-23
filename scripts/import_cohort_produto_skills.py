#!/usr/bin/env python3
"""Importa, com proveniência, as skills indicadas no Kit Cohort Produto."""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = ROOT / ".verification" / "cohort-sources"

TO_PRD = """---
name: to-prd
description: Turn the current conversation context into a PRD and submit it as a GitHub issue. Use when user wants to create a PRD from the current context.
---

This skill takes the current conversation context and codebase understanding and produces a PRD. Do NOT interview the user — just synthesize what you already know.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already.
2. Sketch the modules to build or modify, look for deep modules, and check expectations and tests with the user.
3. Write a PRD with problem statement, solution, user stories, implementation decisions, testing decisions, out of scope, and further notes. Submit it as a GitHub issue.
"""

SKILLS = [
    ("brainstorming", "obra--superpowers", "skills/brainstorming", "MIT", "Jesse Vincent", "gestao", "Brainstorm com propósito", "BRAINSTORMING", "Transforma uma ideia vaga em hipóteses, requisitos e um desenho que alguém possa revisar", "Ideia, requisitos, decisão", ["Objetivo", "Hipóteses", "Design"], ["Produto", "Descoberta", "Planejamento"]),
    ("customer-research", "coreyhaines31--marketingskills", "skills/customer-research", "MIT", "Corey Haines", "marketing", "Pesquisa que escuta", "CUSTOMER RESEARCH", "Extrai dores, linguagem e evidências de conversas, tickets e pesquisas", "Transcrições, tickets ou pesquisas", ["Evidências", "Dores", "Citações"], ["Pesquisa", "Marketing", "Produto"]),
    ("discovery-interview-prep", "deanpeters--product-manager-skills", "skills/discovery-interview-prep", "CC BY-NC-SA 4.0", "Dean Peters", "gestao", "Entrevistas que descobrem", "INTERVIEW PREP", "Prepara entrevistas de descoberta orientadas por evidências, sem perguntas hipotéticas", "Objetivo de pesquisa e acesso a clientes", ["Objetivo", "Perguntas", "Vieses"], ["Produto", "Discovery", "Entrevistas"]),
    ("discovery-process", "deanpeters--product-manager-skills", "skills/discovery-process", "CC BY-NC-SA 4.0", "Dean Peters", "gestao", "Discovery antes do build", "DISCOVERY PROCESS", "Conduz um ciclo de discovery de hipótese a experimento e decisão", "Hipótese, evidências e contexto", ["Hipótese", "Pesquisa", "Experimentos"], ["Produto", "Discovery", "Estratégia"]),
    ("lean-startup", "wondelai--skills", "lean-startup", "MIT", "Wondel.ai", "gestao", "Teste antes de escalar", "LEAN STARTUP", "Aplica construir, medir e aprender para testar uma hipótese de produto", "Hipótese, métrica e experimento", ["Hipótese", "Métrica", "Aprendizado"], ["Produto", "Experimentos", "MVP"]),
    ("to-prd", "mattpocock--skills", None, "MIT", "Matt Pocock", "gestao", "Conversa em PRD", "TO PRD", "Transforma o contexto da conversa em um PRD com escopo e decisões", "Contexto de produto e repositório", ["Problema", "Escopo", "Critérios"], ["Produto", "PRD", "Planejamento"]),
    ("mvp", "slavingia--skills", "skills/mvp", "Authorized redistribution", "Sahil Lavingia", "gestao", "O mínimo que entrega", "MVP", "Define o fluxo essencial e corta o que ainda não precisa existir", "Problema, cliente e restrições", ["Escopo", "Manual", "Primeira entrega"], ["Produto", "MVP", "Escopo"]),
    ("supabase", "supabase--agent-skills", "skills/supabase", "MIT", "Supabase", "operacoes", "Dados com segurança", "SUPABASE", "Orienta banco, autenticação, storage e funções Supabase com checagens de segurança", "Projeto Supabase e objetivo técnico", ["Banco", "Auth", "RLS"], ["Desenvolvimento", "Banco de dados", "Segurança"]),
    ("n8n-workflow-lifecycle-official", "n8n-io--skills", "skills/n8n-workflow-lifecycle-official", "Apache-2.0", "n8n", "operacoes", "Automação que fecha o ciclo", "N8N WORKFLOW", "Desenha, valida, testa e versiona workflows n8n", "Objetivo do fluxo e integrações", ["Desenho", "Validação", "Publicação"], ["Automação", "n8n", "Operações"]),
    ("web-design-guidelines", "vercel-labs--agent-skills", "skills/web-design-guidelines", "MIT", "Vercel", "operacoes", "Interface pronta para revisão", "WEB DESIGN", "Revisa interfaces usando as diretrizes atualizadas de web da Vercel", "Arquivos ou padrões de UI", ["Interface", "Acessibilidade", "Revisão"], ["Design", "UI", "Qualidade"]),
    ("cro", "coreyhaines31--marketingskills", "skills/cro", "MIT", "Corey Haines", "marketing", "Landing que converte", "CRO", "Audita a página de conversão por promessa, prova, fricção e ação", "URL, página ou cópia", ["Promessa", "Prova", "Ação"], ["Marketing", "Conversão", "Landing page"]),
    ("pricing-strategy", "coreyhaines31--marketingskills", "skills/pricing", "MIT", "Corey Haines", "vendas", "Preço ancorado em valor", "PRICING STRATEGY", "Estrutura precificação com cenários, valor e disposição a pagar", "Oferta, cliente e contexto de preço", ["Valor", "Cenários", "Preço"], ["Vendas", "Precificação", "Produto"]),
    ("copywriting", "coreyhaines31--marketingskills", "skills/copywriting", "MIT", "Corey Haines", "marketing", "Copy que fala como o cliente", "COPYWRITING", "Produz copy orientada por pesquisa para landing, proposta e mensagens", "Público, oferta e evidências", ["Público", "Mensagem", "CTA"], ["Marketing", "Copy", "Conversão"]),
]

LICENSE_REPOS = {"obra--superpowers", "coreyhaines31--marketingskills", "deanpeters--product-manager-skills", "wondelai--skills", "mattpocock--skills", "supabase--agent-skills", "n8n-io--skills"}

def slug_text(value: str) -> str:
    return value.replace("-", " ")

def inventory(path: Path) -> list[dict]:
    return [{"path": str(p.relative_to(path)).replace("\\", "/"), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(path.rglob("*")) if p.is_file()]

def wrapper(slug: str, license_name: str, author: str, title: str, subtitle: str) -> str:
    return f'''---
name: {slug}
description: {subtitle} Use quando o pedido corresponder a {slug_text(slug)}.
version: 0.3.0
license: {license_name}
author: {author}
---

# {title}

Esta é uma adaptação de catálogo. As instruções originais e seus arquivos de apoio estão preservados em [references/source/](references/source/).

## When to Use

Use quando a necessidade corresponder ao propósito descrito pela skill de origem. Leia primeiro [references/source/SKILL.md](references/source/SKILL.md) e qualquer referência que ela indicar.

## Quick Reference

Forneça o contexto necessário, siga o fluxo da fonte e mantenha revisões humanas antes de ações externas, configurações ou publicação.

## Procedure

1. Leia as instruções de origem e identifique entradas, entregáveis e limites.
2. Reúna apenas o contexto necessário e execute o fluxo com as ferramentas disponíveis.
3. Apresente o resultado para revisão antes de qualquer ação externa ou irreversível.

## Pitfalls

Não invente acesso a serviços, não exponha credenciais e não trate recomendações da fonte como resultados garantidos.

## Verification

Confirme que o resultado usa as entradas fornecidas, respeita os limites da fonte e deixa explícitos os próximos passos que dependem de revisão humana.
'''

def main() -> None:
    for slug, repo, relative, license_name, author, row, title, netflix, subtitle, requires, cast, genres in SKILLS:
        target = ROOT / "skills" / slug
        if target.exists():
            raise RuntimeError(f"Destino já existe: {target}")
        source = SOURCE_ROOT / repo
        target_source = target / "references" / "source"
        if relative:
            shutil.copytree(source / relative, target_source)
            commit = (source / ".git").exists() and __import__("subprocess").check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
            source_url = f"https://github.com/{repo.replace('--', '/')}/tree/{commit}/{relative}"
        else:
            target_source.mkdir(parents=True)
            (target_source / "SKILL.md").write_text(TO_PRD, encoding="utf-8")
            commit = "62f43a18177be6ec82da242e59ffbc490a4c22ea"
            source_url = f"https://github.com/mattpocock/skills/blob/{commit}/skills/engineering/to-prd/SKILL.md"
        if repo in LICENSE_REPOS:
            shutil.copy2(source / "LICENSE", target / "LICENSE.source")
        elif slug == "web-design-guidelines":
            (target / "LICENSE.source").write_text("MIT, conforme declarado no README da fonte Vercel Labs.\n", encoding="utf-8")
        else:
            (target / "LICENSE.source").write_text("A fonte não declara uma licença. O mantenedor do ClariFlix confirmou autorização para republicação em 2026-09-22.\n", encoding="utf-8")
        (target / "SKILL.md").write_text(wrapper(slug, license_name, author, title, subtitle), encoding="utf-8")
        (target / "manifest.yaml").write_text("\n".join([f"row: {row}", f"title: {title}", f"title_netflix: {netflix}", f"subtitle: {subtitle}", "genre: procedural", "badge: Nova", "runtime_only: false", "painel:", "  ano: 2026", f"  tamanho: {len(inventory(target_source))} arquivo(s) de origem", f"  requer: {requires}", f"  como_usar: 'Instale a skill e forneça o contexto solicitado pela fonte'", f"  elenco: [{', '.join(cast)}]", f"  generos: [{', '.join(genres)}]", "  esta_skill_e: [Rastreável, Estruturada, Revisável]", ""]), encoding="utf-8")
        metadata = {"source_url": source_url, "source_commit": commit, "source_repository": f"https://github.com/{repo.replace('--', '/')}", "license": license_name, "files": inventory(target_source)}
        (target / "references" / "cohort-source-inventory.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (target / "SOURCE.md").write_text(f"# Proveniência\n\n- Fonte: [{repo.replace('--', '/')}]({source_url})\n- Commit: `{commit}`\n- Licença: `{license_name}`\n- Arquivos de origem preservados em `references/source/`; inventário e hashes em `references/cohort-source-inventory.json`.\n", encoding="utf-8")
    print(f"Importadas {len(SKILLS)} skills do Kit Cohort Produto.")

if __name__ == "__main__":
    main()
