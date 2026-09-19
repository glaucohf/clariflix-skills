#!/usr/bin/env python3
"""Adapt the 64 Máquina de Receita generated squads to installable ClariFlix skills.

Requires PyYAML, as do the catalog scripts. Source files are copied byte for byte.
Usage: python scripts/import_generated_squads.py --source-root /path/to/maquina-de-receita
Pass --check to verify reproducibility without writing, or --skills-root for a staging area.
Only destinations carrying this importer's SOURCE.md marker can be updated.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from urllib.parse import quote

import yaml


ROOT = Path(__file__).resolve().parent.parent
VERSION = "0.2.0"
RESTRICTION = "Material da turma, para uso próprio e nos seus projetos, sem republicação em canais abertos"
CACHE_NAMES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
SECTIONS = ("When to Use", "Quick Reference", "Procedure", "Pitfalls", "Verification")

# Explicit capability descriptions replace the source's promotional performance claims.
CAPABILITIES = {
    "founder-agentic-analytics": "Analisar indicadores do negócio, investigar variações e preparar recomendações rastreáveis para o founder.",
    "founder-ai-chief-of-staff": "Organizar prioridades, decisões e acompanhamento executivo com um roteiro de Chief of Staff para o founder.",
    "founder-board-investor-relations": "Preparar materiais de conselho, atualizações a investidores e acompanhamento de decisões e compromissos.",
    "founder-clone-digital-twin": "Estruturar um perfil de critérios e estilo decisório do founder para simular decisões e revisar recomendações.",
    "founder-competitive-intelligence": "Pesquisar concorrentes, consolidar mudanças de mercado e preparar inteligência competitiva com fontes verificáveis.",
    "founder-decision-journal-postmortem": "Registrar decisões, hipóteses e resultados e conduzir postmortems com aprendizados e ações de acompanhamento.",
    "founder-deep-research-orchestrator": "Conduzir pesquisa estratégica em etapas, confrontar fontes e produzir uma síntese de evidências para decisões do founder.",
    "founder-due-diligence-ma-screening": "Organizar triagem de oportunidades de aquisição e due diligence, identificando evidências, riscos e lacunas para revisão.",
    "founder-fundraising-ops": "Organizar pipeline de captação, materiais para investidores e próximos passos de fundraising com revisão humana.",
    "founder-knowledge-base-institucional": "Estruturar conhecimento institucional, registrar decisões e organizar fontes para consulta e atualização pelo founder.",
    "founder-kpi-okr-pulse": "Consolidar KPIs e OKRs, identificar desvios e preparar acompanhamento executivo com responsáveis e próximos passos.",
    "founder-market-sizing-opportunity-scout": "Estimar mercados e avaliar oportunidades usando hipóteses explícitas, fontes e cenários comparáveis.",
    "founder-meeting-intelligence": "Transformar pautas, notas ou transcrições de reuniões em síntese, decisões e ações com responsáveis.",
    "founder-risk-scenario-sentinel": "Mapear riscos do negócio, acompanhar sinais de mudança e preparar cenários e propostas de mitigação.",
    "founder-strategic-foresight-wargaming": "Explorar cenários estratégicos, simular respostas de concorrentes e testar decisões sob diferentes hipóteses.",
    "founder-tech-radar-build-vs-buy": "Pesquisar tecnologias e comparar desenvolver ou contratar soluções, documentando custos, riscos e critérios de decisão.",
    "marketing-abm-signal-orchestrator": "Planejar campanhas ABM a partir de sinais de intenção, perfis de contas, mensagens e sequência de canais para aprovação.",
    "marketing-ai-sdr-outbound": "Preparar prospecção outbound com pesquisa de contas, qualificação, mensagens e sequência de contato para revisão.",
    "marketing-competitive-adspy": "Analisar campanhas e anúncios de concorrentes, reunir referências verificáveis e propor hipóteses de marketing.",
    "marketing-creative-ugc-factory": "Preparar conceitos, roteiros e variações de criativos UGC com revisão de marca e critérios de teste.",
    "marketing-cro-landing-agentico": "Diagnosticar páginas de conversão e preparar hipóteses, textos e planos de experimentos para landing pages.",
    "marketing-demand-sensing-radar": "Pesquisar sinais de demanda e intenção de compra, priorizar oportunidades e propor ações de marketing.",
    "marketing-dormant-lead-reactivation": "Segmentar leads inativos e preparar campanhas de reativação com mensagens, critérios de elegibilidade e revisão.",
    "marketing-funnel-analytics-attribution": "Analisar funil e atribuição de marketing, investigar anomalias e documentar limites dos dados e recomendações.",
    "marketing-influencer-creator-outreach": "Pesquisar criadores e influenciadores, avaliar aderência e preparar propostas e mensagens de parceria para revisão.",
    "marketing-intelligent-timing": "Planejar horários e cadências de contato a partir de sinais disponíveis, evitando conflitos entre canais.",
    "marketing-lead-scoring-router": "Definir pontuação e roteamento de leads com critérios explícitos, validar casos e preparar encaminhamentos.",
    "marketing-living-icp-profiler": "Construir e revisar o perfil de cliente ideal com dados de contas, evidências e critérios de segmentação.",
    "marketing-paid-media-autopilot": "Analisar mídia paga e preparar campanhas, ajustes de orçamento e criativos sujeitos à aprovação antes de publicação.",
    "marketing-pmf-deep-research": "Investigar adequação de produto ao mercado, analisar evidências de clientes e formular hipóteses de posicionamento.",
    "marketing-programmatic-seo-geo": "Planejar conteúdo e arquitetura para SEO programático e descoberta em mecanismos de busca e respostas de IA.",
    "marketing-whatsapp-qualifier": "Preparar fluxos de qualificação de leads no WhatsApp, respostas a objeções e encaminhamento comercial para revisão.",
    "ops-cs-agent-assist-copilot": "Preparar sugestões de resposta e consulta à base de conhecimento para apoiar atendentes humanos em casos de suporte.",
    "ops-cs-ai-sre-incident": "Investigar incidentes a partir de logs e evidências, propor diagnóstico e plano de resposta com gates de aprovação.",
    "ops-cs-back-office-financeiro-reconciliacao": "Conferir transações, conciliar registros e preparar exceções e propostas de lançamentos financeiros para revisão.",
    "ops-cs-churn-prediction": "Analisar sinais de risco de churn e preparar planos de retenção com evidências e responsáveis.",
    "ops-cs-dunning-recuperacao-pagamentos": "Analisar inadimplência e preparar cadências de cobrança e recuperação de pagamentos para revisão humana.",
    "ops-cs-handoff-orchestrator-hitl": "Definir quando escalar casos para humanos e preparar handoffs com contexto, evidências e critérios de retomada.",
    "ops-cs-kb-curator": "Revisar e organizar bases de conhecimento de suporte, identificar lacunas e preparar atualizações rastreáveis.",
    "ops-cs-onboarding-psa-agentica": "Planejar onboarding e implementação de clientes, acompanhando etapas, dependências, riscos e responsáveis.",
    "ops-cs-qa-conversas-verifier": "Auditar conversas de atendimento com critérios de qualidade, evidências por item e recomendações de melhoria.",
    "ops-cs-renovacao-expansao-qbr": "Preparar revisões de negócio com clientes, planos de renovação e oportunidades de expansão baseadas em evidências.",
    "ops-cs-self-healing-etl": "Investigar falhas e anomalias de ingestão de dados e preparar planos de recuperação de pipelines para revisão.",
    "ops-cs-sla-health-monitor": "Analisar prazos de SLA e saúde operacional, priorizar riscos e preparar escalonamentos com contexto.",
    "ops-cs-tier1-resolver-multicanal": "Triar solicitações de suporte em múltiplos canais, preparar respostas e escalar casos fora do escopo de primeiro nível.",
    "ops-cs-triagem-roteamento-priorizacao": "Classificar tickets, definir prioridade e destino e preparar roteamento com justificativa e critérios de SLA.",
    "ops-cs-voz-do-cliente-sentimento": "Consolidar feedback de clientes, analisar temas e sentimento e priorizar insights para produto e operações.",
    "ops-cs-voz-ia-telefonia": "Planejar atendimento por voz, analisar transcrições e preparar fluxos de resolução e escalonamento para revisão.",
    "vendas-agendamento-appointment-setting": "Preparar agendamento comercial com critérios de qualificação, disponibilidade, confirmação e tratamento de reagendamentos.",
    "vendas-ai-sdr-outbound-signal-based": "Preparar prospecção comercial baseada em sinais de intenção, com pesquisa, mensagens e encaminhamento de oportunidades.",
    "vendas-conversation-intelligence-coaching": "Analisar conversas comerciais e preparar feedback de coaching com evidências, pontos de melhoria e ações práticas.",
    "vendas-followup-nurture-reativacao": "Preparar follow-ups, cadências de nutrição e reativação de leads conforme estágio, contexto e histórico de contato.",
    "vendas-forecast-deal-risk": "Revisar pipeline, identificar riscos de oportunidades e preparar previsões de vendas com hipóteses explícitas.",
    "vendas-higiene-enriquecimento-crm-revops": "Diagnosticar qualidade dos dados do CRM e preparar correções, deduplicação e enriquecimento para revisão.",
    "vendas-inteligencia-conta-battlecards": "Pesquisar contas e concorrentes e preparar battlecards e inteligência de apoio a oportunidades comerciais.",
    "vendas-lead-scoring-preditivo": "Analisar sinais e histórico de leads e preparar critérios de pontuação e priorização comercial verificáveis.",
    "vendas-objection-handling-qa-tempo-real": "Preparar respostas a objeções e perguntas comerciais com base no contexto do prospect e em informações verificadas.",
    "vendas-qualificacao-conversacional-whatsapp": "Preparar conversas de qualificação comercial por WhatsApp com perguntas, critérios de avanço e handoff humano.",
    "vendas-recuperacao-oportunidades-estagnadas": "Diagnosticar oportunidades paradas e preparar planos de recuperação com próximos passos e mensagens para revisão.",
    "vendas-reengajamento-pos-evento": "Segmentar participantes de eventos e webinars e preparar ações e mensagens de reengajamento comercial.",
    "vendas-roteamento-inteligente-leads": "Definir regras de distribuição de leads, avaliar responsáveis e preparar roteamento comercial com justificativa.",
    "vendas-social-selling-linkedin": "Pesquisar contexto profissional e preparar conteúdo e abordagens de social selling no LinkedIn para revisão.",
    "vendas-speed-to-lead": "Planejar triagem e primeira resposta a novos leads, com priorização, qualificação e encaminhamento comercial.",
    "vendas-voz-cold-calling-discovery": "Preparar roteiros de cold calling e discovery, analisar transcrições e definir qualificação e próximos passos.",
}


def read_yaml(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError(f"Esperado mapa YAML: {path}")
    return value


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        raise ValueError(f"Frontmatter ausente: {path}")
    return yaml.safe_load(match.group(1))


def yaml_text(value: dict) -> str:
    return yaml.safe_dump(value, allow_unicode=True, sort_keys=False, width=120)


def link(label: str, relative: str) -> str:
    return f"[{label}]({quote(relative, safe='/.-_')})"


def ref(label: str, relative: str) -> str:
    return link(label, f"references/squad/{relative}")


def source_files(source: Path) -> dict[str, bytes]:
    files = {}
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        if any(part in CACHE_NAMES for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Link simbólico não importado: {path}")
        if path.is_file() and path.suffix not in {".pyc", ".pyo"}:
            files[relative.as_posix()] = path.read_bytes()
    return files


def marker(slug: str) -> str:
    return f"<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/{slug} -->"


def build_package(source: Path) -> dict[str, bytes]:
    slug = source.name
    original = source_files(source)
    squad = read_yaml(source / "squad.yaml")
    config = read_yaml(source / "config.yaml")
    if squad["name"] != slug or config["name"] != slug:
        raise ValueError(f"Nome divergente: {slug}")
    title = str(config["pack"]["short-title"])
    description = "Use para " + CAPABILITIES[slug][0].lower() + CAPABILITIES[slug][1:]
    if len(description) > 200:
        raise ValueError(f"Descrição longa: {slug}")
    entry = str(config["entry_agent"])
    entry_file = f"agents/{entry}.md"
    workflows = [f"workflows/{name}" for name in config["workflows"]]
    checklists = [f"checklists/{name}" for name in config["checklists"]]
    if len(workflows) != 1 or not checklists:
        raise ValueError(f"Revisar roteamento de workflows/checklists: {slug}")
    pipeline = read_yaml(source / workflows[0])
    if pipeline["entry_agent"] != entry:
        raise ValueError(f"Orquestradores divergentes: {slug}")
    phases = pipeline["phases"]
    agents = {agent: frontmatter(source / "agents" / f"{agent}.md")["agent"] for agent in config["agents"]}
    entry_name = agents[entry]["name"]
    entry_task = next(phase["task"] for phase in phases if phase.get("agent") == entry and phase.get("task"))
    required_refs = [entry_file, *workflows, *checklists, f"tasks/{entry_task}"]
    for phase in phases:
        if phase.get("task"):
            required_refs.append(f"tasks/{phase['task']}")
        required_refs.append(f"agents/{phase['agent']}.md")
    for required in required_refs:
        if required not in original:
            raise ValueError(f"Referência ausente em {slug}: {required}")
    row = next(value for prefix, value in (("vendas-", "vendas"), ("marketing-", "marketing"),
               ("ops-cs-", "operacoes"), ("founder-", "gestao")) if slug.startswith(prefix))
    origin = squad["origem"]
    area = origin["area"]
    fm = {
        "name": slug, "description": description, "version": VERSION,
        "author": squad["author"], "license": "Proprietary",
        "platforms": ["linux", "macos", "windows"], "required_environment_variables": [],
        "metadata": {"hermes": {"tags": [row, "squad", "maquina-de-receita"], "related_skills": []}},
    }
    phase_rows = []
    for phase in phases:
        agent = phase["agent"]
        task = phase.get("task")
        instruction = ref(task.removesuffix(".md"), f"tasks/{task}") if task else "Consolidar resultados e gates do workflow"
        phase_rows.append(f"| {phase['name']} | {ref(agents[agent]['name'], f'agents/{agent}.md')} | {instruction} |")
    gates = "\n".join(f"- **{gate['level']}** — {gate['condition']}" for gate in pipeline["hitl_gates"])
    checklist_links = ", ".join(ref(Path(name).stem, name) for name in checklists)
    pipeline_link = ref("workflow", workflows[0])
    skill = "---\n" + yaml_text(fm) + "---\n\n" + f"""# {title}

{CAPABILITIES[slug]}

Adaptação do squad de {area} da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- {description}
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | {ref('README original', 'README.md')} |
| Entrada: {entry_name} | {ref('papel do orquestrador', entry_file)} |
| Intake e decomposição | {ref('tarefa de entrada', f'tasks/{entry_task}')} |
| Ordem das fases, contratos, critérios e vetos | {pipeline_link} |
| Verificação das saídas | {checklist_links} |
| Dependências e configuração original | {ref('config.yaml', 'config.yaml')} |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **{entry_name}** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o {pipeline_link} para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
{chr(10).join(phase_rows)}

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/{slug}/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do {pipeline_link}.

### Gates humanos deste squad

{gates}

7. Aplique {checklist_links} e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
8. Consolide o entregável definido no workflow para o escopo solicitado, distinguindo resultado produzido, hipótese, pendência e ação externa confirmada. Preserve aprovações e fontes junto dos artefatos.

## Pitfalls

- Os percentuais, SLAs, benchmarks e projeções do material original são hipóteses ou metas da especificação; não são resultados comprovados nem garantias desta skill.
- Serviços e bases externas mencionados nas referências não são instalados por este pacote. Verifique disponibilidade e documentação vigente quando forem necessários.
- Não aceite uma saída só por estar bem formatada: aplique o critic e os vetos antes de qualquer entrega ou ação dependente.
- Os arquivos originais são um snapshot. Referências a outros squads ou ao workspace do autor não autorizam execução nem substituem um recurso realmente disponível.

## Verification

- As tarefas selecionadas têm entradas suficientes e saídas rastreáveis aos dados usados.
- O checklist do critic foi aplicado, com evidência e veredito por item.
- Gates aplicáveis possuem decisão humana registrada; etapas bloqueadas estão identificadas.
- O entregável contém fontes, hipóteses e pendências, sem apresentar simulação ou planejamento como execução externa.
- Métricas realizadas foram medidas; metas do material original permanecem identificadas como metas.
"""
    manifest = {
        "row": row, "title": title, "title_netflix": title.upper(),
        "subtitle": CAPABILITIES[slug].rstrip("."), "genre": "procedural", "badge": "Nova",
        "painel": {
            "ano": int(str(origin["gerado_em"])[:4]),
            "tamanho": f"{len(agents)} papéis, {len(config['tasks'])} tarefas, {len(workflows)} workflow, {len(checklists)} checklist",
            "requer": "Contexto e dados do negócio; integrações opcionais exigem configuração e autorização",
            "como_usar": f'Diga: "use {slug} para [objetivo]" e forneça o contexto e os dados disponíveis',
            "elenco": [str(agents[agent]["name"]) for agent in config["agents"]],
            "generos": [str(area), "Squads", "Máquina de Receita"],
            "esta_skill_e": ["Especializada", "Rastreável", "Com revisão humana"],
        },
    }
    inventory = "\n".join(f"| `{name}` | `{hashlib.sha256(content).hexdigest()}` |" for name, content in original.items())
    provenance = f"""{marker(slug)}
# Proveniência de {title}

- Origem local: `maquina-de-receita/squads-gerados/{slug}`.
- Repositório de origem: https://github.com/educacional-lendario/maquina-de-receita .
- Especificação: {origin['pagina']}.
- Autoria declarada: {squad['author']}.
- Versão original: {squad['version']}; geração original: {origin['gerado_em']}.
- Adaptação para ClariFlix: {VERSION}, em 2026-09-18.
- A inclusão no repositório ClariFlix foi autorizada pelo mantenedor em 2026-09-18, que confirmou possuir autorização dos autores para publicação. Essa declaração não altera os direitos de terceiros nem concede nova licença sobre o material original.

## Licença e restrição de origem

O manifesto original declara `Proprietary`. A restrição fornecida com o material é preservada:

> {RESTRICTION}

Consulte [LICENSE](LICENSE). A licença geral MIT do catálogo não substitui a licença deste pacote.

## Adaptação e limites

`SKILL.md` e `manifest.yaml` adicionam entrada instalável, descrição de capacidade, roteamento dos papéis e execução sequencial quando não houver runtime multiagente. Todos os arquivos originais estão copiados sem alteração de bytes em `references/squad/`. Somente caches Python/de ferramentas são ignorados, se existirem.

Os caminhos e links históricos internos do snapshot continuam como na fonte; referências a `../../squads-gratuitos/` ou ao workspace do autor não indicam dependências instaladas. O ponto de entrada da adaptação liga diretamente aos recursos presentes neste pacote. Integrações externas, ativação AIOX, observabilidade e resultados operacionais não são provisionados pelo importador.

## Reproduzir e conferir

No checkout do catálogo, use `python scripts/import_generated_squads.py --source-root /caminho/maquina-de-receita`. Acrescente `--check` para comparar os pacotes sem escrever arquivos. O importador recusa diretórios de destino não gerenciados por ele.

## Integridade dos arquivos originais

{len(original)} arquivos preservados. Hashes SHA-256 calculados sobre os bytes originais:

| Arquivo em references/squad | SHA-256 |
|---|---|
{inventory}
"""
    license_text = f"""Proprietary — Máquina de Receita

Autoria declarada no manifesto de origem:
{squad['author']}

Restrição de uso fornecida com o material, preservada literalmente:
{RESTRICTION}

O mantenedor confirmou em 2026-09-18 possuir autorização dos autores para
a inclusão deste material no repositório ClariFlix. A inclusão não altera
os direitos de terceiros nem concede nova licença ao conteúdo original.
A licença MIT geral do catálogo não substitui esta licença Proprietary.
Consulte SOURCE.md e references/squad/squad.yaml para proveniência.
"""
    files = {f"references/squad/{name}": content for name, content in original.items()}
    files.update({"SKILL.md": skill.encode("utf-8"), "manifest.yaml": yaml_text(manifest).encode("utf-8"),
                  "SOURCE.md": provenance.encode("utf-8"), "LICENSE": license_text.encode("utf-8")})
    verify_package(slug, files)
    return files


def verify_package(slug: str, files: dict[str, bytes]) -> None:
    """Check adapter links and catalog contracts, without rewriting historical source."""
    text = files["SKILL.md"].decode("utf-8")
    fm = yaml.safe_load(text.split("---\n", 2)[1])
    if fm["name"] != slug or len(fm["description"]) > 200:
        raise ValueError(f"Frontmatter inválido: {slug}")
    for section in SECTIONS:
        if f"## {section}\n" not in text:
            raise ValueError(f"Seção ausente em {slug}: {section}")
    from urllib.parse import unquote
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if unquote(target.split("#", 1)[0]) not in files:
            raise ValueError(f"Link local inválido em {slug}: {target}")
    manifest = yaml.safe_load(files["manifest.yaml"])
    for key in ("ano", "tamanho", "requer", "como_usar", "elenco", "generos", "esta_skill_e"):
        if not manifest["painel"].get(key):
            raise ValueError(f"Painel incompleto em {slug}: {key}")


def preflight(destination: Path, packages: dict[str, dict[str, bytes]], check: bool) -> None:
    """Refuse unmanaged destinations and symlinks before any writes occur."""
    if destination.is_symlink():
        raise ValueError(f"Destino não pode ser link simbólico: {destination}")
    for slug, files in packages.items():
        target = destination / slug
        if target.is_symlink():
            raise ValueError(f"Destino não pode ser link simbólico: {target}")
        if not target.exists():
            if check:
                raise ValueError(f"Pacote ausente: {slug}")
            continue
        ownership = target / "SOURCE.md"
        if not target.is_dir() or not ownership.is_file() or marker(slug) not in ownership.read_text(encoding="utf-8"):
            raise ValueError(f"Destino não gerenciado; não será sobrescrito: {target}")
        actual = set()
        for path in target.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"Destino contém link simbólico: {path}")
            if path.is_file():
                actual.add(path.relative_to(target).as_posix())
        extra = actual - files.keys()
        if extra:
            raise ValueError(f"Arquivos fora da geração em {slug}; revisar manualmente: {sorted(extra)}")
        if check:
            missing = files.keys() - actual
            changed = [name for name, content in files.items() if name in actual and (target / name).read_bytes() != content]
            if missing or changed:
                raise ValueError(f"Divergência em {slug}; ausentes={sorted(missing)}, alterados={changed}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True, help="Máquina de Receita root or its squads-gerados folder")
    parser.add_argument("--skills-root", type=Path, default=ROOT / "skills", help="Output skill directory (default: repository skills/)")
    parser.add_argument("--check", action="store_true", help="Verify generated packages without writing")
    args = parser.parse_args()
    try:
        source_root = args.source_root.resolve(strict=True)
        if (source_root / "squads-gerados").is_dir():
            source_root = source_root / "squads-gerados"
        actual = {path.name for path in source_root.iterdir() if path.is_dir() and path.name not in CACHE_NAMES}
        if actual != CAPABILITIES.keys():
            raise ValueError(f"Esperados 64 squads conhecidos; ausentes={sorted(CAPABILITIES.keys() - actual)}, extras={sorted(actual - CAPABILITIES.keys())}")
        destination = args.skills_root.absolute()
        # Existing parent symlinks could otherwise redirect writes outside the chosen root.
        if any(parent.is_symlink() for parent in (destination, *destination.parents)):
            raise ValueError(f"Destino contém ancestral simbólico: {destination}")
        packages = {slug: build_package(source_root / slug) for slug in sorted(CAPABILITIES)}
        preflight(destination, packages, args.check)
        if not args.check:
            for slug, files in packages.items():
                for name, content in files.items():
                    path = destination / slug / name
                    path.parent.mkdir(parents=True, exist_ok=True)
                    if not path.exists() or path.read_bytes() != content:
                        path.write_bytes(content)
            preflight(destination, packages, True)
        originals = sum(sum(name.startswith("references/squad/") for name in files) for files in packages.values())
        print(f"{'Verificados' if args.check else 'Importados e verificados'}: {len(packages)} squads; {originals} arquivos originais íntegros; 64 manifests e links locais válidos.")
        return 0
    except (OSError, ValueError, KeyError, yaml.YAMLError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
