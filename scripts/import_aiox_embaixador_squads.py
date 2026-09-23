#!/usr/bin/env python3
"""Importa squads AIOX Embaixador com proveniência e adaptadores ClariFlix."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = ROOT / ".verification" / "aiox-embaixador-pro-20260923"
REPOSITORY = "https://github.com/aiox-embaixadores/aiox-embaixador-pro"

SQUADS = [
    ("aiox-sop", "sop", "SOP de ponta a ponta", "AIOX SOP", "Estrutura SOPs com qualidade, evidências e melhoria contínua", "Processo, responsáveis e evidências", ["Processo", "Qualidade", "Melhoria"], ["SOP", "Operações", "Qualidade"]),
    ("brand", "marketing", "Marca com direção", "BRAND", "Organiza naming, identidade e go-to-market da marca", "Negócio, público e posicionamento", ["Nome", "Identidade", "Mensagem"], ["Marca", "Marketing", "Estratégia"]),
    ("claude-code-mastery", "especialistas", "Claude Code em domínio", "CLAUDE CODE MASTERY", "Orienta hooks, skills, MCP e subagentes no Claude Code", "Repositório e objetivo técnico", ["Hooks", "Skills", "MCP"], ["Desenvolvimento", "Agentes", "Claude Code"]),
    ("copy", "marketing", "Copy de alta conversão", "COPY", "Cria mensagens persuasivas para aquisição e conversão", "Oferta, público e prova", ["Oferta", "Mensagem", "Conversão"], ["Copy", "Marketing", "Vendas"]),
    ("data", "gestao", "Dados que decidem", "DATA", "Analisa métricas e encontra alavancas de crescimento", "Dados, métrica e pergunta de negócio", ["Métricas", "Diagnóstico", "Ações"], ["Dados", "Estratégia", "Crescimento"]),
    ("db-sage", "operacoes", "Banco sem mistério", "DB SAGE", "Orienta PostgreSQL e Supabase com foco em dados e consultas", "Schema, consulta ou problema de banco", ["Schema", "Consultas", "Segurança"], ["Banco de dados", "PostgreSQL", "Supabase"]),
    ("aiox-design", "operacoes", "Design que escala", "AIOX DESIGN", "Constrói e governa sistemas de design, tokens e componentes", "Produto, design system e objetivo", ["Tokens", "Componentes", "Acessibilidade"], ["Design", "UI", "Operações"]),
    ("design-ops", "operacoes", "Operação de design", "DESIGN OPS", "Organiza ferramentas, processos e governança para times de design", "Time, processo e contexto de design", ["Processos", "Ferramentas", "Governança"], ["DesignOps", "Design", "Operações"]),
    ("design-system", "operacoes", "Sistema visual coerente", "DESIGN SYSTEM", "Estrutura tokens, componentes e documentação de interface", "Interface, componentes e objetivos", ["Tokens", "Componentes", "Padrões"], ["Design", "UI", "Sistema"]),
    ("etl-ops", "operacoes", "Pipelines que fluem", "ETL OPS", "Opera pipelines de extração, transformação e carga de dados", "Fonte de dados, destino e transformação", ["Extração", "Transformação", "Carga"], ["ETL", "Dados", "Operações"]),
    ("hormozi", "marketing", "Oferta que vende", "HORMOZI", "Aplica frameworks de oferta, aquisição e escala comercial", "Oferta, cliente e meta de receita", ["Oferta", "Preço", "Aquisição"], ["Marketing", "Vendas", "Crescimento"]),
    ("hub-manager", "operacoes", "Hubs em movimento", "HUB MANAGER", "Organiza a operação de hubs locais e seus responsáveis", "Hub, equipe e objetivo operacional", ["Agenda", "Equipe", "Acompanhamento"], ["Operações", "Comunidade", "Gestão"]),
    ("n8n-white-ops", "operacoes", "n8n com controle", "N8N WHITE OPS", "Audita e organiza automações n8n com segurança operacional", "Workflow, integrações e objetivo", ["Auditoria", "Workflow", "Segurança"], ["Automação", "n8n", "Operações"]),
    ("research", "gestao", "Pesquisa com método", "RESEARCH", "Conduz pesquisa profunda, benchmark e inteligência competitiva", "Pergunta, escopo e evidências", ["Escopo", "Fontes", "Síntese"], ["Pesquisa", "Estratégia", "Inteligência"]),
    ("revenue-os", "vendas", "Receita em sistema", "REVENUE OS", "Coordena marketing, comercial e RevOps para receita previsível", "Funil, metas e dados comerciais", ["Funil", "Receita", "Operação"], ["Vendas", "RevOps", "Marketing"]),
    ("sales-fran", "vendas", "Vendas com método", "SALES FRAN", "Estrutura processo comercial, conversa e fechamento de vendas", "Oferta, lead e etapa comercial", ["Qualificação", "Conversa", "Fechamento"], ["Vendas", "Comercial", "Negociação"]),
    ("slides-creator", "marketing", "Slides que convencem", "SLIDES CREATOR", "Cria apresentações estruturadas com narrativa e design", "Briefing, público e objetivo", ["Narrativa", "Slides", "Design"], ["Apresentações", "Marketing", "Storytelling"]),
    ("spy", "marketing", "Mercado em foco", "SPY", "Pesquisa concorrentes, sinais e inteligência de mercado", "Mercado, concorrente ou pergunta", ["Concorrentes", "Sinais", "Insights"], ["Pesquisa", "Marketing", "Inteligência"]),
    ("squad-creator", "especialistas", "Squads sob medida", "SQUAD CREATOR", "Cria e estrutura squads para objetivos definidos", "Objetivo, domínio e entregáveis", ["Papéis", "Tarefas", "Workflow"], ["Agentes", "Squads", "Operações"]),
    ("squad-creator-pro", "especialistas", "Squads com profundidade", "SQUAD CREATOR PRO", "Cria squads avançadas com DNA, qualidade e validação", "Objetivo, especialistas e critérios", ["DNA", "Agentes", "Qualidade"], ["Agentes", "Squads", "Estratégia"]),
    ("storytelling", "marketing", "Histórias que movem", "STORYTELLING", "Constrói narrativas para marca, vendas e apresentações", "Público, mensagem e objetivo", ["Mensagem", "Estrutura", "Emoção"], ["Storytelling", "Marketing", "Marca"]),
    ("webapp-defender", "especialistas", "Aplicação mais segura", "WEBAPP DEFENDER", "Audita aplicações web de forma defensiva com referências OWASP", "Aplicação, escopo e evidências", ["Superfície", "Riscos", "Correções"], ["Segurança", "OWASP", "Desenvolvimento"]),
]


def inventory(path: Path):
    return [{"path": str(file.relative_to(path)).replace("\\", "/"), "sha256": hashlib.sha256(file.read_bytes()).hexdigest()} for file in sorted(path.rglob("*")) if file.is_file()]


def main():
    commit = subprocess.check_output(["git", "-C", str(SOURCE_ROOT), "rev-parse", "HEAD"], text=True).strip()
    for slug, row, title, netflix, subtitle, requires, cast, genres in SQUADS:
        target = ROOT / "skills" / slug
        if target.exists():
            continue
        snapshot = target / "references" / "squad"
        shutil.copytree(SOURCE_ROOT / "squads" / slug, snapshot)
        (target / "LICENSE.source").write_text("A fonte não declara licença pública. O mantenedor do ClariFlix solicitou a disponibilização pública das squads em 2026-09-23.\n", encoding="utf-8")
        adapter = """---
name: %s
description: %s Use quando o pedido corresponder a %s.
version: 0.6.0
license: Authorized redistribution
author: AIOX Embaixadores
---

# %s

Os arquivos originais da squad estão preservados em [references/squad/](references/squad/).

## When to Use

Use quando a necessidade corresponder ao propósito da squad. Leia primeiro [references/squad/README.md](references/squad/README.md) quando disponível e depois os workflows, tasks e agentes relevantes.

## Quick Reference

Forneça o objetivo, contexto e critérios de sucesso. A squad pode exigir AIOX Core, ferramentas locais, integrações ou credenciais declaradas nos seus próprios arquivos.

## Procedure

1. Leia a configuração e selecione o workflow que corresponde ao objetivo.
2. Reúna o contexto mínimo, execute as etapas com as ferramentas disponíveis e registre evidências.
3. Apresente entregáveis para revisão antes de publicar, alterar dados externos ou realizar ações irreversíveis.

## Pitfalls

Não presuma disponibilidade de AIOX Core, integrações, serviços ou credenciais. Não exponha dados confidenciais e não trate estimativas da squad como resultados garantidos.

## Verification

Confirme que o workflow usou as entradas fornecidas, que os artefatos atendem aos critérios declarados e que dependências ou ações externas pendentes ficaram explícitas.
""" % (slug, subtitle, slug.replace("-", " "), title)
        (target / "SKILL.md").write_text(adapter, encoding="utf-8")
        manifest = "\n".join(["row: " + row, "title: " + title, "title_netflix: " + netflix, "subtitle: " + subtitle, "genre: procedural", "badge: Nova", "runtime_only: true", "painel:", "  ano: 2026", "  tamanho: " + str(len(inventory(snapshot))) + " arquivo(s) de origem", "  requer: " + requires, "  como_usar: 'Instale a squad e siga os pré-requisitos declarados pela fonte'", "  elenco: [" + ", ".join(cast) + "]", "  generos: [" + ", ".join(genres) + "]", "  esta_skill_e: [Rastreável, Estruturada, Revisável]", ""])
        (target / "manifest.yaml").write_text(manifest, encoding="utf-8")
        metadata = {"source_url": REPOSITORY + "/tree/" + commit + "/squads/" + slug, "source_repository": REPOSITORY, "source_commit": commit, "license": "Authorized redistribution", "files": inventory(snapshot)}
        (target / "references" / "aiox-squad-source-inventory.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        source = "# Proveniência\n\n- Fonte: [AIOX Embaixador Pro](%s)\n- Commit: %s\n- Licença: não declarada publicamente; disponibilização solicitada pelo mantenedor do ClariFlix em 2026-09-23.\n- Arquivos de origem preservados em references/squad/; inventário e hashes em references/aiox-squad-source-inventory.json.\n" % (metadata["source_url"], commit)
        (target / "SOURCE.md").write_text(source, encoding="utf-8")
    print("Importadas %s squads do AIOX Embaixador." % len(SQUADS))


if __name__ == "__main__":
    main()
