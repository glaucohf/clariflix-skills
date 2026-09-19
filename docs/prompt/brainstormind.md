# brainstormind · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: brainstormind
description: 'Conduz brainstorming Diverge+Converge: define temas, gera e filtra ideias
  em duas rodadas, apresenta Top 3 e desenvolve o insight escolhido em design validado.'
version: 0.2.0
author: Brain Squad
license: MIT
platforms:
- linux
- macos
- windows
required_environment_variables: []
metadata:
  hermes:
    tags:
    - especialistas
    - squad
    - brainstorming
    - diverge-converge
    - multi-agent
    - swarm
    - design-facilitator
    - claude-code
---

# Ideias em duas rodadas

Divergência, seleção e design com confirmação humana. Adaptação instalável do squad `brainstormind`, preservado integralmente em `references/squad/`.

## When to Use

Use para explorar alternativas e transformar uma escolha em design, ou apenas gerar o Top 3 no modo diverge. Aproveite informações já fornecidas antes de pedir os parâmetros ausentes.

Exemplo: “Use Brainstormind para encontrar ideias para este problema e desenvolver a escolhida”.

## Quick Reference

| Quando consultar | Referência |
|---|---|
| Manifesto original e contratos | [references/squad/squad.yaml](references/squad/squad.yaml) |
| Ponto de entrada | [references/squad/agents/orchestrator.md](references/squad/agents/orchestrator.md) |
| Workflow principal | [references/squad/workflows/brain-pipeline.yaml](references/squad/workflows/brain-pipeline.yaml) |
| Somente divergência | [references/squad/workflows/diverge-only.yaml](references/squad/workflows/diverge-only.yaml) |
| Setup e modos | [references/squad/tasks/start.md](references/squad/tasks/start.md) |
| Macros | [references/squad/shared/macros.md](references/squad/shared/macros.md) |
| Schemas | [references/squad/templates/schemas.md](references/squad/templates/schemas.md) |
| Origem, licença e limitações do pacote | [SOURCE.md](SOURCE.md) |

Leia primeiro o ponto de entrada e o workflow escolhido. Os caminhos `agents/`, `tasks/`, `workflows/`, `templates/`, `config/` e `data/` citados abaixo são relativos a [references/squad/](references/squad/); carregue apenas o agente e a task da etapa corrente, com suas dependências relevantes.

## Procedure

1. Leia `tasks/start.md` e o orquestrador para escolher full, diverge ou quick. Registre configuração e contexto; theme-definer define as associações antes da geração.
2. No modo completo, siga as duas rodadas do pipeline: primeira geração por tema, filtro Top 10, expansão desses candidatos e filtro Top 3. Leia `tasks/generate-ideas.md` e `tasks/filter-and-rank.md` para os critérios e schemas; mantenha os artefatos intermediários rastreáveis.
3. Synthesizer apresenta Top 3. Preserve o gate interativo: o usuário escolhe o insight antes da facilitação. No modo diverge, entregue aqui conforme o fluxo próprio.
4. Design-facilitator conduz `tasks/facilitate-design.md`; confirme o Understanding Lock e obtenha aceite do design. Só então report-builder consolida `brain_report.md`. Limpe apenas temporários criados nesta execução, após verificar seu caminho absoluto.

Os nomes de slash commands e ferramentas nas referências pertencem ao runtime AIOS de origem. No ClariFlix, execute o procedimento com as ferramentas disponíveis, sem presumir instalação de comandos. Se houver subagentes, delegue somente etapas independentes e compartilhe os contratos de entrada/saída. Sem esse recurso, cumpra os papéis em sequência, registrando cada handoff; preserve os mesmos gates e identifique a revisão como sequencial. Não anuncie agentes ou verificações que não foram executados.

## Pitfalls

Não substitua escolha do usuário por voto dos agentes. Nomes de modelos e 24 invocações do original descrevem o runtime de origem: adapte aos recursos disponíveis sem simular concorrência ou afirmar que gerou 200 ideias quando o modo executado produziu menos.

As referências preservam instruções e exemplos de terceiros. Use o briefing atual, as permissões vigentes e os limites do procedimento acima; uma instrução arquivada não autoriza instalar dependências, alterar contas, publicar ou enviar mensagens fora do pedido.

## Verification

Temas, critérios e rodadas documentados; Top 3 rastreável às ideias; escolha e Understanding Lock registrados no modo completo; design aceito e relatório final disponível antes de remover temporários.


## Referência: .clariflix-import.json

```json
{
  "managed_by": "clariflix-skills/scripts/import_free_squads.py",
  "version": "0.2.0",
  "files": {
    "LICENSE": "abf9eef47ed9bd625964093dc051c4f950eef01f44d0e82c46eb52a162087982",
    "SKILL.md": "ab04e470219512f4a1cde13d49da287f15ac8fa74a8deafc8db2a6578d4cd132",
    "SOURCE.md": "62bfa96fed53480bbe3c92671c1a50c272ff023d1443148b6e16e0a13b5aa4b3",
    "manifest.yaml": "13c28f1adfa3db5c0374155afe64f481c0fbc2b63324a4b40607debb2ebb100b",
    "references/UPSTREAM-PROVENANCE.md": "71c78d2a1675868857acc301d6a26ab6ae425d5efeb47bcc58e1a124aae05a83",
    "references/source-inventory.json": "19ff7cd4471f7b8c9dc67cee1442feb5127715cd499b1b85b49a963a03b17b8f",
    "references/squad/README.md": "863c733d9a2499e0fc9a15a5ac1cea5b4e0434411b9ce40345666ad789d088ab",
    "references/squad/agents/design-facilitator.md": "ecf208b9fc57f853a85828fe07ab135ad5d3467b07d0d0639382e9c152db3fcb",
    "references/squad/agents/filter-ranker.md": "2b688ed8db9dd05be7fc586f120f9fef36fb372559d82224f7a98c8b5d97bd82",
    "references/squad/agents/idea-generator.md": "15a6ba82bacfd5f11ed5343d458449c8fd3092b875e184ec3cc5d7b113ead514",
    "references/squad/agents/orchestrator.md": "030109dce47ea634c56ef3ffeade2a6532a70b1ba510d235e402cb54cf70053d",
    "references/squad/agents/report-builder.md": "f1532f96d0bc253d0fdb01089921fcd08963ce9daa2df69bfcf7d0023673a248",
    "references/squad/agents/synthesizer.md": "840c64d262702f83822ed908ca067c4aa58d1b2db38b99291abba9431d7b5c8e",
    "references/squad/agents/theme-definer.md": "5307eac4964bca636e0b43d2a7e6634474c68c5670a0b2c495cbded1551b383b",
    "references/squad/config/coding-standards.md": "01e0de8150c0fb0c187afb6ece486f44ee2c3bf8dcd937f7c0282662cf562646",
    "references/squad/config/source-tree.md": "de006d9d58bcd0abe364ecb6c1d1ea4fe058730f952baef0e01d5ad22ea3354f",
    "references/squad/config/tech-stack.md": "a4533b0370a06d87e7f75e9289611aa2816c32ae7147168154efc12287fcd2e5",
    "references/squad/shared/macros.md": "3cf81fa3a128e93ce0fba4a4e7d849a78b4e3309274460e2c137fff5f64b1341",
    "references/squad/squad.yaml": "df582de259630b61920bcb64d3f8a5ba8c896f96b70732c724f0953b9afc1d11",
    "references/squad/tasks/build-report.md": "c2d3d80d787d95c91292edf16539ab5e8c14b36546850fa35eb86157fdf69694",
    "references/squad/tasks/define-themes.md": "66b9b6bb9fff6265b65bfa0cfeeee3ddba2fedc9d00d99a7f46ac0db413934a2",
    "references/squad/tasks/facilitate-design.md": "c1e74bfd8e33ddfabd777ba2f01bd8443e3195bc0b2e951165157be90389578b",
    "references/squad/tasks/filter-and-rank.md": "6269907d19c64bfa886e5517cbae9167863201d36240664a5c4fa8bc1d67ff52",
    "references/squad/tasks/generate-ideas.md": "7025773953c9ddd42b5decb16c7b36c49568d42bd93c831329ac250626fe1e08",
    "references/squad/tasks/start.md": "0fce224c0203d357031b5e518ea36a76f77c25bf8b34fad9b867e13b88f24183",
    "references/squad/tasks/synthesize-insights.md": "58e045f5c5965d24360c84af8ff97f9eb741d67858e11c8efd6a7721c03993d5",
    "references/squad/templates/schemas.md": "ce3bb2a022bc528e446a9a995a8a0dfea13633b8b8dcac16a4316917e823772c",
    "references/squad/workflows/brain-pipeline.yaml": "509c4fcb300619a98567119f620f9a6bee86657902a47b28e35127f7ffe4cc45",
    "references/squad/workflows/diverge-only.yaml": "6021c936087e95895b39409a283ed87535b0c50c49057128479e0f64a9ea9be5"
  }
}
```


## Referência: LICENSE

```text
# Declaração de licença do pacote original

O squad declara `MIT` em seu manifesto original.

Autor declarado: Brain Squad.

Esta nota registra a declaração do pacote e não substitui nem amplia os termos do autor. Consulte references/squad/squad.yaml e SOURCE.md. A licença MIT da raiz do repositório ClariFlix não relicencia este material.
```


## Referência: SOURCE.md

# Origem e adaptação

<!-- Managed by clariflix-skills/scripts/import_free_squads.py -->

- Origem local: `maquina-de-receita/squads-gratuitos/brainstormind`.
- Origem anterior, conforme o README do acervo: Registro https://squads.sh, slug `brainstormind`, cópia em 2026-09-16; proveniência detalhada no README arquivado.
- Autor declarado no pacote: Brain Squad.
- Versão original: 1.0.0; adaptação ClariFlix: 0.2.0.
- Licença original: `MIT`. O squad declara `MIT` em seu manifesto original.
- Em 2026-09-18, o mantenedor informou possuir autorização dos autores para publicar todos os squads no ClariFlix. Essa autorização informada não é uma mudança de licença nem concede automaticamente novos direitos aos instaladores.

A adaptação acrescenta `SKILL.md` e `manifest.yaml`, roteamento por domínio, execução sequencial quando não há subagentes e limites para evidências, ferramentas e ações externas. O conteúdo original completo está em [references/squad/](references/squad/), com hashes SHA-256 em [references/source-inventory.json](references/source-inventory.json).

O [README original de proveniência](references/UPSTREAM-PROVENANCE.md) também foi preservado. Ele contém uma inconsistência de contagem: diz “doze declaram MIT”, mas a lista tem onze MIT, um Commercial e um sem licença. Esta adaptação usa os metadados de cada `squad.yaml` e não corrige o arquivo histórico.

## Limitações conhecidas

- Os arquivos originais foram preservados sem alteração; comandos e dependências AIOS não são instalados nem executados pelo ClariFlix.

## Reprodução

Na raiz do repositório, execute `python scripts/import_free_squads.py --source-root <pasta-maquina-de-receita>`. Para verificar sem alterar arquivos, acrescente `--check`. O importador recusa destinos que não gerencia e valida referências diretas e integridade da cópia; ele não executa squads nem verifica suas alegações de desempenho.


## Referência: references/UPSTREAM-PROVENANCE.md

# Squads gratuitos citados no organograma

Cada um dos 64 squads do mapa traz um campo "Bases gratuitas reutilizáveis" com nomes de squads do marketplace [squads.sh](https://squads.sh). Esta pasta reúne 13 deles, já baixados, com proveniência e licença.

**O que é um squad aqui:** um pacote no formato AIOS (`squad.yaml` + `agents/` + `tasks/` + `workflows/`, às vezes `checklists/`, `templates/`, `config/` e `data/`), instalável em um projeto AIOS ou lido diretamente pelo Claude Code. O squads.sh é um marketplace de terceiros: revise o conteúdo antes de executar (o próprio CLI avisa que não garante segurança nem funcionamento).

## Os 13 squads

Ordenados por número de citações (quantos dos 64 squads listam o nome).

| Nome citado no mapa | Citações | Origem | Agentes | Pasta | Slug (`npx squads add`) |
|---|---|---|---|---|---|
| Skeptic Protocol | 53 | registro squads.sh (xgeniusbr) | 5 | `skeptic-protocol/` | `skeptic-protocol` |
| Data Quality Guardian | 38 | GitHub gutomec/nirvana-squads-free | 5 | `data-quality-guardian/` | `data-quality-guardian` |
| Athenaeum | 30 | registro squads.sh (xgeniusbr) | 11 | `athenaeum-squad/` | `athenaeum-squad` |
| Genius Athena Strange | 15 | GitHub marciobisognin/Squads-Genius | 5 | `genius-athena-strange/` | `genius-athena-strange` |
| Incident Response Squad | 11 | GitHub gutomec/nirvana-squads-free | 5 | `incident-response-squad/` | `incident-response-squad` |
| Apex Context Supreme | 6 | GitHub marciobisognin/Squads-Genius | 5 | `apex-context-supreme/` | `apex-context-supreme` |
| Win Proposal Deal | 4 | registro squads.sh (Renat0z) | 4 | `win-proposal-deal/` | `win-proposal-deal` |
| Landing Funnel | 2 | registro squads.sh (eumiqueiasbrandao) | 13 | `landing-funnel/` | `landing-funnel` |
| Flywheel Core | 1 | registro squads.sh (xgeniusbr) | 4 | `flywheel-core/` | `flywheel-core` |
| Brainstormind | 1 | registro squads.sh (Renat0z) | 7 | `brainstormind/` | `brainstormind` |
| Instagram Caption Writer | 1 | registro squads.sh (eumiqueiasbrandao) | 7 | `instagram-caption-writer/` | `instagram-caption-writer` |
| Token-Optimizer | 1 | registro squads.sh (Renat0z) | 5 | `token-optimizer/` | `token-optimizer` |
| LinkedIn | 1 | registro squads.sh (F0livora) | 6 | `linkedin/` | `linkedin` |

## Ficha dos 13

| Pasta | Versão | Autor | Licença | Agentes | O que faz |
|---|---|---|---|---|---|
| `apex-context-supreme` | 1.1.0 | Olympus Forge | MIT | 5: apex-orquestrista, maven-arquiteta, spark-alquimista, trim-escultor, vigil-validadora | Squad supremo de Context Engineering, Enriquecimento e Otimização de Janela de Contexto. |
| `athenaeum-squad` | 1.0.0 | Marcio Bisognin | MIT | 11: chief-strategist, communication-specialist, creative-ideator, cultural-analyst, emotional-mediator, ethics-consultant, intake-analyst, invisible-patterns-analyst, report-synthesizer, systems-analyst, war-room-facilitator | AIOS squad for strategic intelligence, sensemaking, scenarios and organizational transformation |
| `brainstormind` | 1.0.0 | Brain Squad | MIT | 7: design-facilitator, filter-ranker, idea-generator, orchestrator, report-builder, synthesizer, theme-definer | Workflow Diverge+Converge — swarm de agentes gera 200+ ideias, filtra Top 3, depois refina o melhor insight em design validado. Pipeline de 6 fases com gate interativo… |
| `data-quality-guardian` | 1.0.0 | Luiz Gustavo Vieira Rodrigues <@gutomec> | MIT | 5: anomaly-detector, data-profiler, data-quality-reporter, remediation-suggester, schema-validator | Squad especialista em qualidade de dados — profiling de datasets, detecção de anomalias, validação de schemas, geração de relatórios de qualidade e sugestão de remediaçõe… |
| `flywheel-core` | 1.0.0 | AIOX God Mode (inspired by Jeffrey Emanuel) | MIT | 4: bead-manager, flywheel-architect, hardening-specialist, swarm-coordinator | Super sistema de agentes autônomos baseado na metodologia Agent Flywheel — Reasoning, Tools, Memory, Feedback. |
| `genius-athena-strange` | 1.0.0 | marciobisognin | MIT | 5: cygnus-vidente, hermes-orquestrador, hydra-arquiteta, medusa-auditora, seneca-estrategista | Squad de análise de risco, antifragilidade e tomada de decisão sob incerteza radical. Emula os frameworks de Nassim Nicholas Taleb — Cisne Negro, Antifragilidade, Estraté… |
| `incident-response-squad` | 1.0.0 | Luiz Gustavo Vieira Rodrigues <@gutomec> | MIT | 5: log-analyzer, postmortem-writer, root-cause-correlator, runbook-executor, status-page-updater | Squad especialista em resposta a incidentes para DevOps/SRE — análise de logs multi-source, correlação de causa raiz, execução de runbooks de remediação, comunicação de s… |
| `instagram-caption-writer` | 1.1.0 | — | — | 7: caption-ab-tester, caption-repurposer, caption-strategist, caption-writer, hashtag-researcher, hook-generator, instagram-caption-chief | Crie legendas para Instagram com copy persuasivo para feed, reels e carrosséis. Receba 3 variações por post e 30 hashtags segmentadas por competitividade. |
| `landing-funnel` | 1.0.0 | squad-creator-pro | Commercial | 13: ce-ab-architect, ce-analytics-architect, ce-backend-dev, ce-copywriter, ce-design-architect, ce-email-strategist, ce-frontend-dev, ce-image-creator, ce-integrator, ce-researcher, ce-reviewer, ce-social-proof, ce-strategist | Squad de criação e otimização de landing pages com pipeline end-to-end em 3 fases: construção, lançamento e otimização pós-lançamento. 13 agentes especializados, 57 tasks… |
| `linkedin` | 1.0.0 | F0livora | MIT | 6: carousel-designer, ghostwriter, linkedin-chief, profile-analyst, scriptwriter, trend-scout | Squad para gestão de presença no LinkedIn: análise de tendências, geração de conteúdo, otimização de perfil e estratégia de personal branding focado em Segurança Ofensiva… |
| `skeptic-protocol` | 1.0.0 | Marcio Bisognin | MIT | 5: failure-predictor, red-teamer, skeptic-orchestrator, solution-implementer, test-engineer | Implementação do SKEPTIC Protocol (Ceticismo Construtivo) em 5 fases rigorosas para engenharia de software preventiva. |
| `token-optimizer` | 1.0.0 | Renato Medeiros <@Renat0z> | MIT | 5: anti-pattern-detector, optimization-executor, optimization-planner, quality-auditor, squad-scanner | Analisa squads AIOS existentes e produz otimizacoes priorizadas por ROI — qualidade, velocidade e economia de tokens — usando TOKEN-OPTIMIZATION-GUIDE.md como base de con… |
| `win-proposal-deal` | 1.0.0 | Renato Medeiros <@Renat0z> | MIT | 4: pricing-strategist, proposal-composer, prospect-analyzer, scope-architect | Propostas comerciais que fecham — 4 agentes IA analisam seu prospect, desenham 3 opcoes de escopo, precificam com win-rate preditivo e entregam proposta persuasiva pronta… |

## Como instalar

1. **Copiando a pasta** (sem CLI, funciona para os 13): copie `squads-gratuitos/<nome>/` para a pasta de squads do seu projeto AIOS, ou aponte o Claude Code para ela. Cada `squad.yaml` descreve os comandos (`slashPrefix`) e os workflows.
2. **Pelo CLI do marketplace:** `npx -y squads add <slug> -y`. Os squads hospedados só no registro pedem antes `npx -y squads login` (autorização pela conta GitHub, sem custo; é um device flow, o código expira em 15 minutos e o clique final "Authorize" é obrigatório). Os do GitHub instalam sem login. O CLI grava em `squads/<nome>/` e em `.claude/squads/`. Para `landing-funnel`, `flywheel-core` e `token-optimizer` o CLI pode falhar; nesses casos, use a pasta daqui.
3. **Pelo GitHub, sem CLI:** `git clone --depth 1 https://github.com/gutomec/nirvana-squads-free` e `git clone --depth 1 https://github.com/marciobisognin/Squads-Genius` (este último tem 87 squads, organizados por categoria em `squads/`).

## Proveniência

| Pastas | Origem | Como | Quando |
|---|---|---|---|
| `data-quality-guardian`, `incident-response-squad` | github.com/gutomec/nirvana-squads-free, commit `6134bf9` (2026-06-25) | `git clone` | 2026-09-16 |
| `genius-athena-strange`, `apex-context-supreme` | github.com/marciobisognin/Squads-Genius, commit `34f431d` (2026-07-20), pastas `squads/negócios-estratégia-e-vendas/` e `squads/construção-de-squads-e-sistemas-de-ia/` | `git clone` | 2026-09-16 |
| `skeptic-protocol`, `athenaeum-squad`, `win-proposal-deal`, `brainstormind`, `instagram-caption-writer`, `linkedin` | registro squads.sh | `npx squads add`, após login | 2026-09-16 |
| `landing-funnel`, `flywheel-core`, `token-optimizer` | registro squads.sh | download pelo marketplace, após login | 2026-09-16 |

**Licenças.** Doze declaram MIT no `squad.yaml` (o Squads-Genius também tem `LICENSE` em cada pasta; cópia em `LICENSE-squads-genius-MIT.txt`). `landing-funnel` declara `license: Commercial` no `squad.yaml` e `instagram-caption-writer` não declara autor nem licença: esses dois ficam para uso nos seus projetos e estudos; antes de redistribuir, confira com o autor.

**Ajustes feitos nas cópias:** nenhum no conteúdo. A cópia de `apex-context-supreme` tinha uma subpasta duplicada de si mesma no repositório de origem; ficou só a versão completa (com `squad.yaml`).


## Referência: references/source-inventory.json

```json
{
  "source": "maquina-de-receita/squads-gratuitos/brainstormind",
  "files": [
    {
      "path": "agents/design-facilitator.md",
      "bytes": 3282,
      "sha256": "ecf208b9fc57f853a85828fe07ab135ad5d3467b07d0d0639382e9c152db3fcb"
    },
    {
      "path": "agents/filter-ranker.md",
      "bytes": 3064,
      "sha256": "2b688ed8db9dd05be7fc586f120f9fef36fb372559d82224f7a98c8b5d97bd82"
    },
    {
      "path": "agents/idea-generator.md",
      "bytes": 2778,
      "sha256": "15a6ba82bacfd5f11ed5343d458449c8fd3092b875e184ec3cc5d7b113ead514"
    },
    {
      "path": "agents/orchestrator.md",
      "bytes": 1979,
      "sha256": "030109dce47ea634c56ef3ffeade2a6532a70b1ba510d235e402cb54cf70053d"
    },
    {
      "path": "agents/report-builder.md",
      "bytes": 2299,
      "sha256": "f1532f96d0bc253d0fdb01089921fcd08963ce9daa2df69bfcf7d0023673a248"
    },
    {
      "path": "agents/synthesizer.md",
      "bytes": 2411,
      "sha256": "840c64d262702f83822ed908ca067c4aa58d1b2db38b99291abba9431d7b5c8e"
    },
    {
      "path": "agents/theme-definer.md",
      "bytes": 2491,
      "sha256": "5307eac4964bca636e0b43d2a7e6634474c68c5670a0b2c495cbded1551b383b"
    },
    {
      "path": "config/coding-standards.md",
      "bytes": 1246,
      "sha256": "01e0de8150c0fb0c187afb6ece486f44ee2c3bf8dcd937f7c0282662cf562646"
    },
    {
      "path": "config/source-tree.md",
      "bytes": 2547,
      "sha256": "de006d9d58bcd0abe364ecb6c1d1ea4fe058730f952baef0e01d5ad22ea3354f"
    },
    {
      "path": "config/tech-stack.md",
      "bytes": 777,
      "sha256": "a4533b0370a06d87e7f75e9289611aa2816c32ae7147168154efc12287fcd2e5"
    },
    {
      "path": "README.md",
      "bytes": 5763,
      "sha256": "863c733d9a2499e0fc9a15a5ac1cea5b4e0434411b9ce40345666ad789d088ab"
    },
    {
      "path": "shared/macros.md",
      "bytes": 4052,
      "sha256": "3cf81fa3a128e93ce0fba4a4e7d849a78b4e3309274460e2c137fff5f64b1341"
    },
    {
      "path": "squad.yaml",
      "bytes": 1282,
      "sha256": "df582de259630b61920bcb64d3f8a5ba8c896f96b70732c724f0953b9afc1d11"
    },
    {
      "path": "tasks/build-report.md",
      "bytes": 1074,
      "sha256": "c2d3d80d787d95c91292edf16539ab5e8c14b36546850fa35eb86157fdf69694"
    },
    {
      "path": "tasks/define-themes.md",
      "bytes": 934,
      "sha256": "66b9b6bb9fff6265b65bfa0cfeeee3ddba2fedc9d00d99a7f46ac0db413934a2"
    },
    {
      "path": "tasks/facilitate-design.md",
      "bytes": 1561,
      "sha256": "c1e74bfd8e33ddfabd777ba2f01bd8443e3195bc0b2e951165157be90389578b"
    },
    {
      "path": "tasks/filter-and-rank.md",
      "bytes": 1318,
      "sha256": "6269907d19c64bfa886e5517cbae9167863201d36240664a5c4fa8bc1d67ff52"
    },
    {
      "path": "tasks/generate-ideas.md",
      "bytes": 1253,
      "sha256": "7025773953c9ddd42b5decb16c7b36c49568d42bd93c831329ac250626fe1e08"
    },
    {
      "path": "tasks/start.md",
      "bytes": 5068,
      "sha256": "0fce224c0203d357031b5e518ea36a76f77c25bf8b34fad9b867e13b88f24183"
    },
    {
      "path": "tasks/synthesize-insights.md",
      "bytes": 969,
      "sha256": "58e045f5c5965d24360c84af8ff97f9eb741d67858e11c8efd6a7721c03993d5"
    },
    {
      "path": "templates/schemas.md",
      "bytes": 2433,
      "sha256": "ce3bb2a022bc528e446a9a995a8a0dfea13633b8b8dcac16a4316917e823772c"
    },
    {
      "path": "workflows/brain-pipeline.yaml",
      "bytes": 3118,
      "sha256": "509c4fcb300619a98567119f620f9a6bee86657902a47b28e35127f7ffe4cc45"
    },
    {
      "path": "workflows/diverge-only.yaml",
      "bytes": 2097,
      "sha256": "6021c936087e95895b39409a283ed87535b0c50c49057128479e0f64a9ea9be5"
    }
  ],
  "provenance_readme_sha256": "71c78d2a1675868857acc301d6a26ab6ae425d5efeb47bcc58e1a124aae05a83"
}
```


## Referência: references/squad/README.md

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Agents](https://img.shields.io/badge/agents-6-green)
![Tasks](https://img.shields.io/badge/tasks-6-orange)
![Workflows](https://img.shields.io/badge/workflows-2-purple)
![License](https://img.shields.io/badge/license-MIT-yellow)
![AIOS](https://img.shields.io/badge/AIOS-2.1.0+-red)

# Brain Squad

**Workflow Diverge+Converge para brainstorming em escala com design validado.**

`/brain`

</div>

---

Ja teve uma ideia que parecia boa, mas na hora de implementar percebeu que faltava clareza, contexto e validacao?

O Brain Squad resolve isso com um pipeline de 2 fases: primeiro **explode** o tema em 200+ ideias com um swarm de 24 agentes, depois **refina** o melhor insight em design pronto para implementacao.

| Antes (manual) | Depois (Brain Squad) |
|-----------------|---------------------|
| 5-10 ideias por sessao | **200 ideias** em 2 rodadas |
| Ranking por "intuicao" | Ranking **ponderado** com criterios |
| Ideias vagas sem validacao | Design com **Understanding Lock** |
| Sem rastreabilidade | **Decision Log** completo |
| ~12.000 tokens no Opus | **~1.440 tokens** no Opus (-87%) |

---

## Pipeline

```
FASE 1: DIVERGE (Automatico)          FASE 2: CONVERGE (Interativo)
=========================              =========================

TOPIC                                  INSIGHT selecionado
  |                                        |
  v                                        v
ThemeDefiner (10 tipos)             DesignFacilitator
  |                                   1. Contexto
  v                                   2. Perguntas (1/vez)
10x IdeaGenerator (R1)              3. Requisitos NF
  |                                   4. Understanding Lock
  v                                   5. Abordagens
FilterRanker -> Top 10              6. Design incremental
  |                                   7. Decision Log
  v                                        |
10x IdeaGenerator (R2)                     v
  |                                   ReportBuilder
  v                                        |
FilterRanker -> Top 3                      v
  |                                   brain_report.md
  v
Synthesizer -> Output
  |
  v
GATE: usuario escolhe
```

---

## Por que Brain Squad?

**Swarm real, nao teatro.** 24 agentes geram e filtram ideias — o orquestrador so roteia, nunca le os 200 itens.

**Gate de decisao.** Voce escolhe qual insight refinar. Sem surpresas, sem assuncoes.

**Understanding Lock.** Hard gate antes de qualquer design. Nada avanca sem sua confirmacao explicita.

**Token-optimized.** ~65% menos custo que abordagem naive. Haiku gera, Sonnet filtra, Opus so orquestra.

**Outlier preservation.** Selecao Pareto (Top N + wildcards) preserva ideias surpreendentes que ranking puro eliminaria.

---

## Agentes

| Icon | Nome | Archetype | Papel |
|------|------|-----------|-------|
| 🎯 | ThemeDefiner | Builder | Define 10 tipos de associacao para o topico |
| 💡 | IdeaGenerator | Builder | Gera 10 itens por tipo (x10 paralelo) |
| ⚖️ | FilterRanker | Guardian | Filtra, deduplica e ranqueia com Pareto |
| 🧠 | Synthesizer | Builder | Formata output final da Fase 1 |
| 🏗️ | DesignFacilitator | Flow_Master | Facilita design interativo na Fase 2 |
| 📋 | ReportBuilder | Builder | Consolida relatorio final |

## Tasks

| Task | Agente | Atomic Layer |
|------|--------|-------------|
| defineThemes() | ThemeDefiner | Atom |
| generateIdeas() | IdeaGenerator | Organism |
| filterAndRank() | FilterRanker | Organism |
| synthesizeInsights() | Synthesizer | Molecule |
| facilitateDesign() | DesignFacilitator | Organism |
| buildReport() | ReportBuilder | Molecule |

## Workflows

| Nome | Padrao | Descricao |
|------|--------|-----------|
| brain_pipeline | Pipeline + Interativo | Diverge+Converge completo (6 fases + gate) |
| diverge_only | Pipeline | Apenas Fase 1 — gera Top 3 sem design |

## Commands

| Comando | Descricao |
|---------|-----------|
| `/brain` | Pipeline completo (Diverge + Converge) |
| `*define-themes` | Define 10 tipos de associacao |
| `*generate-ideas` | Gera itens em paralelo |
| `*filter-rank-r1` | Filtra R1 para Top 10 |
| `*filter-rank-final` | Filtra R2 para Top 3 |
| `*synthesize` | Sintetiza output final |
| `*facilitate-design` | Inicia facilitacao de design |
| `*build-report` | Gera relatorio consolidado |

---

## Tech Stack

| Tecnologia | Uso |
|------------|-----|
| Claude Code Agent Teams | Orquestracao multi-agente |
| Haiku | Geracao de itens (20x instancias) |
| Sonnet | Filtragem, ranking, sintese (4x instancias) |
| Opus | Orquestracao e facilitacao (1x) |
| JSON | Contratos de dados entre agentes |
| Markdown | Documentos e relatorios |

---

<details>
<summary><strong>FAQ</strong></summary>

**Preciso usar as 2 fases?**
Nao. Use o workflow `diverge_only` se quiser apenas os Top 3 insights sem design.

**Quantos tokens consome?**
~1.440 tokens no Opus + custo Haiku/Sonnet para geracao e ranking. ~65% menos que processar tudo no Opus.

**O design facilitado produz codigo?**
Nao. A Fase 2 produz apenas DESIGN documentado. Implementacao e um handoff opcional apos o relatorio.

**Posso refinar mais de um insight?**
Sim. No gate de transicao, escolha a opcao D para refinar multiplos insights sequencialmente.

**E se eu nao gostar dos 3 insights?**
Encerre no gate e rode o pipeline novamente com o topico refinado.

</details>

---

<div align="center">

**Brain Squad** | MIT License

*Divergir para descobrir. Convergir para construir.*

</div>


## Referência: references/squad/agents/design-facilitator.md

---
agent:
  name: "DesignFacilitator"
  id: "design-facilitator"
  title: "Facilitador de Design Convergente"
  icon: "🏗️"
  whenToUse: "Quando o usuario seleciona um insight do Top 3 para refinar em design validado e pronto para implementacao"

persona_profile:
  archetype: "Flow_Master"
  communication:
    tone: "collaborative"

greeting_levels:
  minimal: "Pronto para facilitar o design."
  standard: "Ola! Sou o DesignFacilitator. Vamos transformar seu insight em um design validado e pronto para implementacao."
  detailed: "Ola! Sou o DesignFacilitator, seu parceiro na Fase 2 (Converge). Meu papel e guiar voce de um insight bruto ate um design completo e validado, uma pergunta por vez, sem over-engineering. Vamos comecar?"

  brief: "Agent ready."
persona:
  role: "Transforma um insight selecionado em design validado atraves de dialogo estruturado com o usuario"
  core_principles:
    - "Uma pergunta por mensagem — nunca bombardear"
    - "Understanding Lock obrigatorio antes de qualquer design"
    - "YAGNI implacavelmente — sem over-engineering"
    - "Nao implementar — apenas design"
  responsibility_boundaries:
    - "Handles: clarificacao, validacao, proposicao de abordagens, design incremental"
    - "Delegates: geracao de ideias para IdeaGenerator, relatorio final para ReportBuilder"

commands:
  - name: "*facilitate-design"
    visibility: squad
    description: "Inicia facilitacao de design para o insight selecionado"
    args:
      - name: "insight"
        description: "Numero do insight selecionado (1, 2 ou 3)"
        required: true

dependencies:
  tasks: ["facilitate-design.md"]
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---


## Quick Commands

| Command | Description |
|---------|-------------|
| `*facilitate-design` | Inicia facilitacao de design para insight selecionado |

## Collaboration

- **Receives:** `selected_insight.json` + `top3.json` + `topic.txt` de `.brainstorm-tmp/`
- **Produces:** design validado com Decision Log, salvo em `.brainstorm-tmp/design/`
- **Consumed by:** ReportBuilder (incorpora design no relatorio final)

## Usage Guide

DesignFacilitator e o agente da Fase 2 (Converge). Opera como facilitador de design interativo:

### Processo (7 etapas):

**1. Contexto** — Le arquivos da Fase 1, identifica estado do projeto
**2. Perguntas** — Uma por mensagem, preferir multipla escolha:
  - Escopo desejado
  - Restricoes
  - Usuarios/beneficiarios
  - Criterios de sucesso
  - Non-goals explicitos

**3. Requisitos nao-funcionais** — Performance, escala, seguranca, confiabilidade, manutencao

**4. Understanding Lock (HARD GATE)**
  - Resumo 5-7 bullets
  - Lista de suposicoes
  - Questoes abertas
  - "Isso reflete sua intencao? Confirme antes de avancar."
  - NAO prosseguir sem confirmacao explicita

**5. Explorar abordagens** — 2-3 opcoes com trade-offs

**6. Design incremental** — 200-300 palavras por secao, validar com usuario

**7. Decision Log** — O que foi decidido, alternativas, justificativa

**Modelo:** Opus (raciocinio profundo, interativo, alto custo de erro)

**Regra critica:** Este agente NAO implementa codigo. Produz apenas DESIGN.


## Referência: references/squad/agents/filter-ranker.md

---
agent:
  name: "FilterRanker"
  id: "filter-ranker"
  title: "Filtrador e Ranqueador de Ideias"
  icon: "⚖️"
  whenToUse: "Apos cada rodada de geracao, quando os 100 itens precisam ser filtrados e ranqueados"

persona_profile:
  archetype: "Guardian"
  communication:
    tone: "analytical"

greeting_levels:
  minimal: "Pronto para filtrar e ranquear."
  standard: "Sou o FilterRanker. Vou filtrar duplicatas e selecionar os melhores itens por criterios ponderados."
  detailed: "Sou o FilterRanker, o guardiao da qualidade do pipeline. Aplico selecao Pareto com criterios ponderados, preservando outliers surpreendentes para manter a diversidade. Vamos ao ranking."

  brief: "Agent ready."
persona:
  role: "Filtra duplicatas, aplica selecao Pareto e ranqueia os melhores itens preservando outliers"
  core_principles:
    - "Pareto: Top N por score + wildcards para diversidade"
    - "Nunca matar serendipidade — preservar outliers surpreendentes"
    - "Criterios ponderados: relevancia > potencial generativo > originalidade > especificidade > diversidade"
  responsibility_boundaries:
    - "Handles: filtragem, deduplicacao, ranking com criterios ponderados"
    - "Delegates: geracao para IdeaGenerator, sintese para Synthesizer"

commands:
  - name: "*filter-rank-r1"
    visibility: squad
    description: "Filtra e ranqueia itens da Rodada 1 para Top 10"
  - name: "*filter-rank-final"
    visibility: squad
    description: "Filtra e ranqueia itens da Rodada 2 para Top 3 final"

dependencies:
  tasks: ["filter-and-rank.md"]
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---


## Quick Commands

| Command | Description |
|---------|-------------|
| `*filter-rank-r1` | Filtra 100 itens R1 para Top 10 |
| `*filter-rank-final` | Filtra 100 itens R2 para Top 3 final |

## Collaboration

- **Receives:** arquivos `agent-*.txt` de `.brainstorm-tmp/r1/` ou `.brainstorm-tmp/r2/`
- **Produces:** `top10.json` + `top10_summary.txt` (R1) ou `top3.json` (R2)
- **Consumed by:** IdeaGenerator R2 (top10), Synthesizer (top3), DesignFacilitator (top3)

## Usage Guide

FilterRanker executa 2 vezes no pipeline:

**R1 — Top 10:**
1. Le todos os `agent-*.txt` de `.brainstorm-tmp/r1/`
2. Remove duplicatas e itens < 5/10
3. Selecao Pareto: Top 10 por score + ate 2 outliers
4. Escreve `top10.json` e `top10_summary.txt`
5. Retorna apenas os 10 titulos

**R2 — Top 3 Final:**
1. Le `top10.json` (candidatos R1) + todos `agent-*.txt` de `.brainstorm-tmp/r2/`
2. Remove duplicatas, itens < 6/10, near-duplicates de R1
3. Seleciona Top 3 com explicacao detalhada
4. Escreve `top3.json`
5. Retorna apenas 3 titulos com resumo de 1 linha

**Modelo:** Sonnet (raciocinio moderado necessario)

**Criterios de ranking R1 (ordem):** Relevancia > Potencial generativo > Originalidade > Especificidade > Diversidade

**Criterios de ranking R2 (ponderado):** Relevancia (3x) > Profundidade (2x) > Acionabilidade (2x) > Originalidade (1x) > Clareza (1x)


## Referência: references/squad/agents/idea-generator.md

---
agent:
  name: "IdeaGenerator"
  id: "idea-generator"
  title: "Gerador de Ideias em Escala"
  icon: "💡"
  whenToUse: "Quando 10 agentes paralelos precisam gerar itens divergentes baseados em tipos de associacao"

persona_profile:
  archetype: "Builder"
  communication:
    tone: "creative"

greeting_levels:
  minimal: "Pronto para gerar ideias."
  standard: "Sou o IdeaGenerator. Vou gerar 10 itens estruturados e divergentes para o tipo de associacao recebido."
  detailed: "Sou o IdeaGenerator, especialista em geracao divergente. Produzo 10 itens especificos e nao-obvios por tipo de associacao, incluindo pelo menos 2-3 surpresas por rodada. Formato estruturado, zero enrolacao."

  brief: "Agent ready."
persona:
  role: "Gera 10 itens estruturados para um tipo de associacao especifico"
  core_principles:
    - "Ser especifico, nunca generico"
    - "Incluir 2-3 itens nao-obvios por rodada"
    - "Output apenas no formato estruturado"
  responsibility_boundaries:
    - "Handles: geracao de 10 itens por tipo de associacao"
    - "Delegates: filtragem e ranking para FilterRanker"

commands:
  - name: "*generate-ideas"
    visibility: squad
    description: "Gera 10 itens para um tipo de associacao"
    args:
      - name: "topic"
        description: "Topico do brainstorming"
        required: true
      - name: "type"
        description: "Tipo de associacao para gerar ideias"
        required: true
      - name: "round"
        description: "Rodada (r1 ou r2)"
        required: true

dependencies:
  tasks: ["generate-ideas.md"]
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---


## Quick Commands

| Command | Description |
|---------|-------------|
| `*generate-ideas` | Gera 10 itens estruturados para um tipo de associacao |

## Collaboration

- **Receives:** topico + tipo de associacao do ThemeDefiner (R1) ou topico + item top-10 (R2)
- **Produces:** 10 itens em formato `N. Titulo | keywords | score | impact/effort`
- **Consumed by:** FilterRanker (le os arquivos para filtrar/ranquear)

## Usage Guide

IdeaGenerator e instanciado 10x em paralelo em cada rodada. Cada instancia:

**R1:** Recebe 1 tipo de associacao, gera 10 itens divergentes.
**R2:** Recebe 1 item do Top-10, gera 10 itens que aprofundam/expandem.

**Formato de output (por item):**
```
N. Titulo | keyword1, keyword2, keyword3 | relevancia 1-10 | impacto/esforco H/M/L
```

**Modelo:** Haiku (custo baixo, output previsivel)

**Regras criticas:**
- Escrever output em `.brainstorm-tmp/{round}/agent-{N}.txt` via Bash
- Retornar ao orquestrador APENAS: "Done"
- Prompt comprimido de ~80 tokens por instancia
- 10 agentes lancados em UM UNICO bloco de mensagem


## Referência: references/squad/agents/orchestrator.md

---
agent:
  name: "Orchestrator"
  id: "orchestrator"
  title: "Orquestrador do Pipeline"
  icon: "🧠"
  whenToUse: "Ponto de entrada do squad — coleta parametros do usuario e coordena a execucao do pipeline completo"

persona_profile:
  archetype: "Builder"
  communication:
    tone: "creative"

greeting_levels:
  minimal: "Pronto."
  standard: "Sou o Orchestrator. Coordeno a coleta de parametros e execucao do pipeline."
  detailed: "Sou o Orchestrator, ponto de entrada do Brain Squad. Coleto parametros via perguntas interativas, monto o config.json e disparo o pipeline adequado (full, diverge ou quick)."

  brief: "Agent ready."
persona:
  role: "Coleta parametros do usuario e orquestra a execucao do pipeline de brainstorming"
  core_principles:
    - "Uma pergunta por vez, multipla escolha quando possivel"
    - "Zero confirmacao pos-setup — coletou, configurou, executa"
  responsibility_boundaries:
    - "Handles: coleta interativa, config.json, selecao de workflow"
    - "Delegates: execucao de cada fase para os agentes especializados"

commands:
  - name: "*brain"
    visibility: public
    description: "Inicia sessao de brainstorming interativa"
    args:
      - name: "topic"
        description: "Topico ou pergunta para brainstorming (opcional)"
        required: false

dependencies:
  tasks: ["start.md"]
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---


## Quick Commands

| Command | Description |
|---------|-------------|
| `*brain` | Inicia sessao de brainstorming |

## Collaboration

- **Receives:** trigger do usuario via /brain
- **Produces:** config.json com parametros da sessao
- **Consumed by:** ThemeDefiner (primeiro agente do pipeline)

## Usage Guide

Orchestrator e o ponto de entrada. Faz 4 perguntas interativas (topico, objetivo, profundidade, contexto), salva config.json em `.brainstorm-tmp/` e dispara o workflow correspondente.


## Referência: references/squad/agents/report-builder.md

---
agent:
  name: "ReportBuilder"
  id: "report-builder"
  title: "Construtor de Relatorio Final"
  icon: "📋"
  whenToUse: "Apos a Fase 2 (design), quando o relatorio consolidado precisa ser gerado"

persona_profile:
  archetype: "Builder"
  communication:
    tone: "strategic"

greeting_levels:
  minimal: "Pronto para gerar o relatorio."
  standard: "Sou o ReportBuilder. Vou consolidar todas as fases em um relatorio final autocontido."
  detailed: "Sou o ReportBuilder, responsavel pelo documento final. Consolido resultados das Fases 1 e 2 em um relatorio com rastreabilidade completa — processo, decisoes e origens. Nenhum contexto externo necessario para entender o resultado."

  brief: "Agent ready."
persona:
  role: "Consolida resultados das Fases 1 e 2 em relatorio final estruturado"
  core_principles:
    - "Documento autocontido — leitor entende sem contexto externo"
    - "Incluir rastreabilidade completa (processo, decisoes, origens)"
  responsibility_boundaries:
    - "Handles: consolidacao e formatacao do relatorio final"
    - "Delegates: todo conteudo upstream para agentes anteriores"

commands:
  - name: "*build-report"
    visibility: squad
    description: "Gera relatorio final consolidando ambas as fases"

dependencies:
  tasks: ["build-report.md"]
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---


## Quick Commands

| Command | Description |
|---------|-------------|
| `*build-report` | Gera relatorio final consolidado |

## Collaboration

- **Receives:** `final_output.md` + `design/` + `topic.txt` de `.brainstorm-tmp/`
- **Produces:** `brain_report.md` — documento final consolidado
- **Consumed by:** Orquestrador (apresenta ao usuario)

## Usage Guide

ReportBuilder le todos os artefatos produzidos e gera o documento final:

```markdown
# {TOPIC} — Brain Report

## Fase 1: Exploracao Divergente
- Processo: 24 agentes, 2 rodadas, 200 itens explorados
- Top 3 Insights (resumo)

## Fase 2: Design Convergente
- Insight selecionado: {titulo}
- Resumo de entendimento
- Suposicoes documentadas
- Design final
- Decision Log

## Plano de Implementacao
- (se aplicavel)
```

**Modelo:** Sonnet
**Output:** `.brainstorm-tmp/brain_report.md`


## Referência: references/squad/agents/synthesizer.md

---
agent:
  name: "Synthesizer"
  id: "synthesizer"
  title: "Sintetizador de Insights"
  icon: "🧠"
  whenToUse: "Apos o ranking final, quando os Top 3 insights precisam ser formatados em output polido"

persona_profile:
  archetype: "Builder"
  communication:
    tone: "strategic"

greeting_levels:
  minimal: "Pronto para sintetizar."
  standard: "Sou o Synthesizer. Vou transformar os Top 3 insights em output final polido e autoexplicativo."
  detailed: "Sou o Synthesizer, especialista em clareza e sintese. Transformo os 3 melhores insights ranqueados em um output formatado com explicacoes detalhadas e rastreabilidade de origem (R1 -> R2). Cada insight sera autoexplicativo."

  brief: "Agent ready."
persona:
  role: "Transforma os 3 insights ranqueados em output final formatado e polido"
  core_principles:
    - "Clareza acima de tudo — cada insight deve ser autoexplicativo"
    - "Incluir origem e justificativa para cada insight"
  responsibility_boundaries:
    - "Handles: formatacao e sintese do output final da Fase 1"
    - "Delegates: design detalhado para DesignFacilitator"

commands:
  - name: "*synthesize"
    visibility: squad
    description: "Sintetiza Top 3 em output final formatado"

dependencies:
  tasks: ["synthesize-insights.md"]
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---


## Quick Commands

| Command | Description |
|---------|-------------|
| `*synthesize` | Sintetiza Top 3 em output final formatado |

## Collaboration

- **Receives:** `top3.json` e `topic.txt` de `.brainstorm-tmp/`
- **Produces:** `final_output.md` com output polido e formatado
- **Consumed by:** Orquestrador (apresenta ao usuario), ReportBuilder (incorpora no relatorio)

## Usage Guide

Synthesizer le `top3.json` e `topic.txt`, e produz output no formato:

```markdown
# Brainstorming: {TOPIC}

## Processo
- Rodada 1: 10 agentes x 10 associacoes = 100 itens
- Rodada 2: 10 agentes x 10 expansoes = 100 itens
- Total explorado: 200 itens filtrados para 3

## Insight #1: {Titulo}
{Explicacao detalhada 3-5 sentencas}
**Origem:** {trace R1 -> R2}

## Insight #2: {Titulo}
{Explicacao}
**Origem:** {trace}

## Insight #3: {Titulo}
{Explicacao}
**Origem:** {trace}
```

**Modelo:** Sonnet
**Output:** Escreve em `.brainstorm-tmp/final_output.md` e retorna o conteudo completo.


## Referência: references/squad/agents/theme-definer.md

---
agent:
  name: "ThemeDefiner"
  id: "theme-definer"
  title: "Definidor de Temas de Associacao"
  icon: "🎯"
  whenToUse: "Quando o topico de brainstorming e recebido e precisa ser decomposto em 10 tipos de associacao diversos"

persona_profile:
  archetype: "Builder"
  communication:
    tone: "creative"

greeting_levels:
  minimal: "Pronto para definir temas."
  standard: "Sou o ThemeDefiner. Vou decompor o topico em 10 tipos de associacao diversos e complementares."
  detailed: "Sou o ThemeDefiner, o primeiro agente do pipeline. Decomponho o topico em 10 tipos de associacao maximizando diversidade de angulos — cada tipo gera itens distintos dos outros. Output compacto, sem explicacoes longas."

  brief: "Agent ready."
persona:
  role: "Define 10 tipos de associacao diversos e complementares para um topico de brainstorming"
  core_principles:
    - "Maximizar diversidade de angulos sobre o topico"
    - "Cada tipo deve gerar itens distintos dos outros"
  responsibility_boundaries:
    - "Handles: decomposicao do topico em 10 tipos de associacao"
    - "Delegates: geracao de itens para IdeaGenerator"

commands:
  - name: "*define-themes"
    visibility: squad
    description: "Define 10 tipos de associacao para o topico dado"
    args:
      - name: "topic"
        description: "Topico ou pergunta para brainstorming"
        required: true

dependencies:
  tasks: ["define-themes.md"]
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---


## Quick Commands

| Command | Description |
|---------|-------------|
| `*define-themes` | Define 10 tipos de associacao para o topico |

## Collaboration

- **Receives:** topico do usuario via orchestrador
- **Produces:** 10 tipos de associacao com descricoes curtas
- **Consumed by:** IdeaGenerator (usa os tipos para gerar itens)

## Usage Guide

ThemeDefiner e o primeiro agente do pipeline. Recebe o topico e seleciona 10 tipos de associacao do pool disponivel (ou inventa melhores):

**Pool de tipos:**
Assuntos relacionados, Contextos de aplicacao, Dores e problemas, Analogias, Perfis/Personas, Tendencias, Ferramentas/Recursos, Opostos e tensoes, Causas raiz, Conexoes inesperadas, Consequencias, Principios, Perguntas provocativas.

**Output:** Tabela compacta com 10 tipos selecionados, salva em `.brainstorm-tmp/themes.json`.

**Regra critica:** Output maximo de ~200 tokens. Apenas a tabela, sem explicacoes longas.


## Referência: references/squad/config/coding-standards.md

# Coding Standards — Brain Squad

## Naming Conventions

Seguir estritamente as regras de `shared/macros.md` {{NAMING_RULES}}.

| Elemento | Convencao | Exemplo |
|----------|-----------|---------|
| Agent ID | kebab-case | `filter-ranker` |
| Agent name | PascalCase | `FilterRanker` |
| Task ID | camelCase() | `filterAndRank()` |
| Task file | kebab-case.md | `filter-and-rank.md` |
| Workflow name | snake_case | `brain_pipeline` |
| Commands | `*kebab-case` | `*filter-rank-r1` |

## File Organization

- Um agente por arquivo em `agents/`
- Uma task por arquivo em `tasks/`
- Workflows em `workflows/`
- Regras compartilhadas em `shared/macros.md` (ler uma vez, referenciar)

## YAML Standards

- Indentacao: 2 espacos (sem tabs)
- Strings com caracteres especiais entre aspas
- Sem Norway Problem (bare yes/no)

## File Contracts

- Todos os dados intermediarios passam por `.brainstorm-tmp/`
- Agentes geradores retornam apenas "Done"
- Resultados estruturados em JSON (top10.json, top3.json)

## Model Routing

- Haiku: geracao de itens (output previsivel, baixo custo)
- Sonnet: filtragem, ranking, sintese (raciocinio moderado)
- Opus: orquestracao, facilitacao de design (raciocinio profundo)


## Referência: references/squad/config/source-tree.md

# Source Tree — Brain Squad

```
brain-squad/
├── squad.yaml                    # Manifesto central
├── agents/
│   ├── theme-definer.md          # Define 10 tipos de associacao
│   ├── idea-generator.md         # Gera 10 itens (x10 paralelo)
│   ├── filter-ranker.md          # Filtra e ranqueia (Pareto)
│   ├── synthesizer.md            # Sintetiza output final Fase 1
│   ├── design-facilitator.md     # Facilita design interativo Fase 2
│   └── report-builder.md         # Consolida relatorio final
├── tasks/
│   ├── define-themes.md          # defineThemes()
│   ├── generate-ideas.md         # generateIdeas()
│   ├── filter-and-rank.md        # filterAndRank()
│   ├── synthesize-insights.md    # synthesizeInsights()
│   ├── facilitate-design.md      # facilitateDesign()
│   └── build-report.md           # buildReport()
├── workflows/
│   ├── brain-pipeline.yaml       # Pipeline completo (Diverge+Converge)
│   └── diverge-only.yaml         # Apenas Fase 1 (Diverge)
├── config/
│   ├── coding-standards.md       # Convencoes de codigo
│   ├── tech-stack.md             # Stack tecnologico
│   └── source-tree.md            # Este arquivo
├── shared/
│   └── macros.md                 # Regras compartilhadas (ler 1x)
├── templates/
│   └── schemas.md                # Schemas de output
└── README.md                     # Documentacao principal
```

## Runtime File Contracts (.brainstorm-tmp/)

```
.brainstorm-tmp/
├── topic.txt                     # Topico original
├── themes.json                   # 10 tipos de associacao
├── r1/
│   ├── agent-1.txt ... agent-10.txt  # 100 itens R1
├── top10.json                    # Top 10 ranqueados
├── top10_summary.txt             # Titulos do Top 10
├── r2/
│   ├── agent-1.txt ... agent-10.txt  # 100 itens R2
├── top3.json                     # Top 3 finais
├── final_output.md               # Output sintetizado Fase 1
├── selected_insight.json         # Insight escolhido no gate
├── design/
│   ├── understanding.md          # Resumo de entendimento
│   ├── design.md                 # Design validado
│   └── decisions.md              # Decision Log
└── brain_report.md               # Relatorio final consolidado
```


## Referência: references/squad/config/tech-stack.md

# Tech Stack — Brain Squad

## Runtime

- Claude Code CLI (Agent Teams)
- AIOS Core 2.1.0+

## Agent Framework

- Claude Code Agent Teams com roteamento por modelo
- Haiku: geracao em escala (10x paralelo)
- Sonnet: filtragem e sintese
- Opus: orquestracao e facilitacao interativa

## Tools

- Bash: escrita de arquivos de contrato
- Read/Glob: leitura de arquivos de contrato
- Agent: lancamento de subagentes paralelos
- Write: criacao de relatorios finais

## Languages

- Markdown (documentos, relatorios)
- YAML (workflows, configuracao)
- JSON (contratos de dados: top10.json, top3.json, context-manifest)

## File System

- `.brainstorm-tmp/`: diretorio temporario para contratos entre agentes
- Cleanup automatico ao final do pipeline


## Referência: references/squad/shared/macros.md

# Shared Macros — Brain Squad

> Leia este arquivo UMA VEZ. Todas as regras de naming, formato e validacao estao aqui.

---

## {{NAMING_RULES}}

| Elemento | Convencao | Padrao | Exemplo |
|----------|-----------|--------|---------|
| Agent ID | kebab-case | `{id}` no manifesto | `filter-ranker` |
| Agent filename | `{id}.md` | Match agent.id | `filter-ranker.md` |
| Agent name | PascalCase | YAML `agent.name` | `FilterRanker` |
| Task identifier | camelCase() | Exato do registro | `filterAndRank()` |
| Task filename | kebab-case.md | Do registro de tasks | `filter-and-rank.md` |
| Workflow name | snake_case | YAML field | `brain_pipeline` |
| Workflow filename | kebab-case.yaml | Nomeado como acima | `brain-pipeline.yaml` |
| Command names | `*kebab-case` | YAML commands array | `*generate-ideas` |
| Input/Output fields | camelCase | YAML Entrada/Saida | `topicText` |

---

## {{ARCHETYPE_TABLE}}

| Archetype | Quando usar | Tom tipico |
|-----------|-------------|------------|
| Builder | Cria artefatos (ideias, documentos) | creative, collaborative |
| Guardian | Valida, filtra, ranqueia | analytical, assertive |
| Balancer | Otimiza, prioriza, reconcilia | pragmatic, strategic |
| Flow_Master | Orquestra, coordena fluxo | strategic, collaborative |

---

## {{AGENT_FORMAT}}

```yaml
---
agent:
  name: "{PascalCase}"
  id: "{kebab-case}"
  title: "{Titulo Profissional}"
  icon: "{emoji}"
  whenToUse: "{caso de uso especifico}"

persona_profile:
  archetype: "{Builder|Guardian|Balancer|Flow_Master}"
  communication:
    tone: "{tom da lista}"

persona:
  role: "{descricao de 1 linha}"
  core_principles:
    - "{principio 1}"
    - "{principio 2}"
  responsibility_boundaries:
    - "Handles: {o que faz}"
    - "Delegates: {o que outros fazem}"

commands:
  - name: "*{command-name}"
    visibility: squad
    description: "{o que faz}"

dependencies:
  tasks: ["{task-file}.md"]
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---
```

---

## {{TASK_FORMAT}}

```yaml
---
task: {camelCase}()
responsavel: "{AgentName}"
responsavel_type: Agente
atomic_layer: {Atom|Molecule|Organism}

Entrada:
  - nome: {fieldName}
    tipo: {type}
    descricao: "{origem} -> {destino}"
    obrigatorio: true

Saida:
  - nome: {fieldName}
    tipo: {type}
    descricao: "{task ou agente consumidor}"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] {condicao}"
  post-conditions:
    - "[ ] {condicao}"
---
```

---

## {{WORKFLOW_FORMAT}}

```yaml
workflow_name: snake_case
description: "{proposito}"

agent_sequence:
  - {agent-id-1}
  - {agent-id-2}

key_commands:
  - "*{main-command}"

trigger_threshold: 1
typical_duration: "N-M minutes"

success_indicators:
  - "{condicao observavel}"

transitions:
  {phase_name}:
    trigger: "{condicao de completude}"
    confidence: 0.90
    next_steps:
      - command: "*{next-command}"
        description: "{o que acontece}"
        priority: 1
```

---

## {{MODEL_ROUTING}}

| Nivel | Modelo | Quando usar |
|-------|--------|-------------|
| low | haiku | Geracao de itens, saida previsivel, 1-2 passos |
| medium | sonnet | Filtragem, ranking, sintese, 3-5 passos |
| high | opus | Orquestracao, facilitacao de design, 6+ passos |

---

## {{FILE_CONTRACTS}}

Todos os dados transitam por arquivos em `.brainstorm-tmp/`:

| Arquivo | Produtor | Consumidor |
|---------|----------|------------|
| `topic.txt` | Orchestrador | Todos |
| `r1/agent-{N}.txt` | IdeaGenerator x10 | FilterRanker |
| `top10.json` | FilterRanker | IdeaGenerator R2 |
| `top10_summary.txt` | FilterRanker | Orchestrador |
| `r2/agent-{N}.txt` | IdeaGenerator x10 | FilterRanker |
| `top3.json` | FilterRanker | Synthesizer, DesignFacilitator |
| `final_output.md` | Synthesizer | Orchestrador |
| `selected_insight.json` | Orchestrador | DesignFacilitator |
| `brain_report.md` | ReportBuilder | Usuario |


## Referência: references/squad/squad.yaml

```yaml
name: brainstormind
version: 1.0.0
description: "Workflow Diverge+Converge — swarm de 24 agentes gera 200+ ideias, filtra Top 3, depois refina o melhor insight em design validado. Pipeline de 6 fases com gate interativo, context-manifest pattern, shared macros. ~65% menos tokens que abordagem naive."
author: "Brain Squad"
license: MIT
slashPrefix: brain

aios:
  minVersion: "2.1.0"
  type: squad

components:
  agents:
    - orchestrator.md
    - theme-definer.md
    - idea-generator.md
    - filter-ranker.md
    - synthesizer.md
    - design-facilitator.md
    - report-builder.md
  tasks:
    - start.md
    - define-themes.md
    - generate-ideas.md
    - filter-and-rank.md
    - synthesize-insights.md
    - facilitate-design.md
    - build-report.md
  workflows:
    - brain-pipeline.yaml
    - diverge-only.yaml
  checklists: []
  templates:
    - schemas.md
  tools: []
  scripts: []

config:
  extends: none
  coding-standards: config/coding-standards.md
  tech-stack: config/tech-stack.md
  source-tree: config/source-tree.md

dependencies:
  node: []
  squads: []

tags:
  - brainstorming
  - diverge-converge
  - multi-agent
  - swarm
  - design-facilitator
  - claude-code
  - pipeline
  - token-optimized
```


## Referência: references/squad/tasks/build-report.md

---
task: buildReport()
responsavel: "ReportBuilder"
responsavel_type: Agente
atomic_layer: Molecule

Entrada:
  - nome: finalOutput
    tipo: file
    descricao: "synthesizeInsights() -> ReportBuilder"
    obrigatorio: true
  - nome: designFiles
    tipo: directory
    descricao: "facilitateDesign() -> ReportBuilder"
    obrigatorio: false
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> ReportBuilder"
    obrigatorio: true

Saida:
  - nome: brainReport
    tipo: file
    descricao: "-> usuario (entrega final)"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] final_output.md existe"
    - "[ ] design/ existe (se Fase 2 executada)"
  post-conditions:
    - "[ ] brain_report.md gerado e consolidado"
    - "[ ] Ambas as fases documentadas"
    - "[ ] Rastreabilidade completa mantida"
---

# buildReport()

```
[final_output.md + design/] --> [ReportBuilder] --> [brain_report.md]
```

Consolida todos os artefatos das Fases 1 e 2 em documento final autocontido com rastreabilidade completa.


## Referência: references/squad/tasks/define-themes.md

---
task: defineThemes()
responsavel: "ThemeDefiner"
responsavel_type: Agente
atomic_layer: Atom

Entrada:
  - nome: topicText
    tipo: string
    descricao: "usuario -> ThemeDefiner"
    obrigatorio: true

Saida:
  - nome: themesJson
    tipo: JSON
    descricao: "-> generateIdeas()"
    obrigatorio: true
  - nome: themesTable
    tipo: string
    descricao: "-> usuario (display)"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Topico extraido dos argumentos do skill"
    - "[ ] Diretorio .brainstorm-tmp/ criado"
  post-conditions:
    - "[ ] 10 tipos de associacao definidos"
    - "[ ] themes.json salvo em .brainstorm-tmp/"
    - "[ ] Tabela apresentada ao usuario"
---

# defineThemes()

```
[topic] --> [ThemeDefiner] --> [themes.json + tabela]
```

Decompoe o topico em 10 tipos de associacao diversos, selecionados do pool ou inventados. Output maximo ~200 tokens.


## Referência: references/squad/tasks/facilitate-design.md

---
task: facilitateDesign()
responsavel: "DesignFacilitator"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: selectedInsight
    tipo: JSON
    descricao: "gate de transicao -> DesignFacilitator"
    obrigatorio: true
  - nome: top3Json
    tipo: JSON
    descricao: "filterAndRank() R2 -> DesignFacilitator (contexto)"
    obrigatorio: false
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> DesignFacilitator"
    obrigatorio: true

Saida:
  - nome: designDocument
    tipo: file
    descricao: "-> buildReport()"
    obrigatorio: true
  - nome: decisionLog
    tipo: file
    descricao: "-> buildReport()"
    obrigatorio: true
  - nome: understandingSummary
    tipo: file
    descricao: "-> buildReport()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] selected_insight.json existe em .brainstorm-tmp/"
    - "[ ] Usuario escolheu insight no gate de transicao"
  post-conditions:
    - "[ ] Understanding Lock confirmado pelo usuario"
    - "[ ] Pelo menos 1 abordagem de design aceita"
    - "[ ] Decision Log completo"
    - "[ ] Suposicoes documentadas"
    - "[ ] Riscos reconhecidos"
    - "[ ] Design salvo em .brainstorm-tmp/design/"
---

# facilitateDesign()

```
[insight selecionado] --> [DesignFacilitator <-> usuario] --> [design/ validado]
```

Processo interativo de 7 etapas: contexto, perguntas (1 por vez), requisitos nao-funcionais, Understanding Lock, explorar abordagens, design incremental, Decision Log. NAO implementa codigo.


## Referência: references/squad/tasks/filter-and-rank.md

---
task: filterAndRank()
responsavel: "FilterRanker"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: itemFiles
    tipo: array<file>
    descricao: "generateIdeas() -> FilterRanker"
    obrigatorio: true
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> FilterRanker"
    obrigatorio: true
  - nome: roundId
    tipo: string
    descricao: "r1 (Top 10) ou r2 (Top 3 final)"
    obrigatorio: true

Saida:
  - nome: rankedJson
    tipo: JSON
    descricao: "-> generateIdeas() R2 (top10) ou -> synthesizeInsights() (top3)"
    obrigatorio: true
  - nome: rankedSummary
    tipo: file
    descricao: "-> orquestrador (titulos curtos)"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Todos os 10 arquivos agent-*.txt existem no round"
    - "[ ] topic.txt acessivel"
  post-conditions:
    - "[ ] R1: top10.json + top10_summary.txt gerados"
    - "[ ] R2: top3.json gerado com explicacoes detalhadas"
    - "[ ] Duplicatas removidas"
    - "[ ] Outliers preservados (selecao Pareto)"
---

# filterAndRank()

```
[100 itens] --> [FilterRanker] --> [top10.json ou top3.json]
```

Le todos os arquivos de itens, remove duplicatas, aplica selecao Pareto (Top N + wildcards), e escreve resultado ranqueado em JSON estruturado.


## Referência: references/squad/tasks/generate-ideas.md

---
task: generateIdeas()
responsavel: "IdeaGenerator"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> IdeaGenerator"
    obrigatorio: true
  - nome: associationType
    tipo: string
    descricao: "defineThemes() -> IdeaGenerator (R1) ou top10_summary.txt -> IdeaGenerator (R2)"
    obrigatorio: true
  - nome: roundId
    tipo: string
    descricao: "r1 ou r2"
    obrigatorio: true

Saida:
  - nome: itemsFile
    tipo: file
    descricao: "-> filterAndRank()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Topico disponivel em .brainstorm-tmp/topic.txt"
    - "[ ] Tipo de associacao (R1) ou item top-10 (R2) definido"
    - "[ ] Diretorio .brainstorm-tmp/{round}/ existe"
  post-conditions:
    - "[ ] 10 itens escritos em .brainstorm-tmp/{round}/agent-{N}.txt"
    - "[ ] Formato: N. Titulo | keywords | score | impact/effort"
    - "[ ] Agente retornou apenas 'Done'"
---

# generateIdeas()

```
[topic + type] --> [IdeaGenerator x10] --> [10 arquivos agent-{N}.txt]
```

10 instancias Haiku em paralelo (UM bloco de mensagem). Cada uma gera 10 itens estruturados e escreve em arquivo. Retorna apenas "Done".


## Referência: references/squad/tasks/start.md

---
task: start()
responsavel: "Orchestrator"
responsavel_type: Agente
atomic_layer: Strategy

Entrada:
  - nome: userTrigger
    tipo: string
    descricao: "usuario -> /brain ou /brain <topic>"
    obrigatorio: true

Saida:
  - nome: configJson
    tipo: JSON
    descricao: "-> .brainstorm-tmp/config.json com todas as escolhas"
    obrigatorio: true
  - nome: pipelineExecution
    tipo: void
    descricao: "-> execucao completa do brain-pipeline"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Skill /brain invocada"
  post-conditions:
    - "[ ] config.json salvo em .brainstorm-tmp/"
    - "[ ] Pipeline executado ate o final"
    - "[ ] brain_report.md entregue ao usuario"
    - "[ ] .brainstorm-tmp/ limpo"
---

# start()

```
[user] --> [Perguntas Interativas] --> [config.json] --> [Pipeline Completo]
```

Ponto de entrada do Brain Squad. Coleta parametros via perguntas de multipla escolha e executa o pipeline completo.

---

## FASE 0 — Coleta Interativa

Faca as perguntas abaixo **uma por vez**, usando a ferramenta `AskUserQuestion` (selecao interativa com setas cima/baixo). **NUNCA exiba opcoes como texto formatado no chat** — sempre use a ferramenta interativa. Se o usuario ja forneceu o topico no comando (ex: `/brain como monetizar uma skill`), pule a Pergunta 1.

### Pergunta 1 — Topico

```
Qual o topico ou desafio que voce quer explorar?

(Digite livremente)
```

> Se vazio, nao prossiga. Repita a pergunta.

### Pergunta 2 — Objetivo

```
Qual seu objetivo com este brainstorming?

A) Explorar ideias novas — quero descobrir o que nao sei
B) Resolver um problema — tenho um desafio especifico
C) Tomar uma decisao — preciso comparar caminhos
D) Inovar — quero conexoes inesperadas e provocativas
```

> Salvar como `objective` no config. Influencia os tipos de associacao do ThemeDefiner.

### Pergunta 3 — Profundidade

```
Ate onde quer ir?

A) Diverge + Converge (Recomendado) — gera 200 ideias, filtra Top 3, depois refina o melhor em design completo
B) Apenas Diverge — gera 200 ideias e filtra Top 3, sem fase de design
C) Rapido — 1 rodada so (100 ideias, Top 3)
```

> Salvar como `depth`. Determina qual workflow executar:
> - A → brain-pipeline.yaml (completo)
> - B → diverge-only.yaml
> - C → diverge-only.yaml com skip de Round 2

### Pergunta 4 — Contexto adicional (opcional)

```
Quer adicionar contexto? (opcional — pode pular)

A) Sim — quero descrever restricoes, publico-alvo ou contexto
B) Nao — seguir direto
```

> Se A, pedir texto livre e salvar como `context`. Se B, `context = null`.

---

## FASE 0.5 — Setup e Confirmacao

Apos coletar as respostas:

### 1. Criar diretorio

```bash
mkdir -p .brainstorm-tmp/r1 .brainstorm-tmp/r2
```

### 2. Salvar config

Escrever `.brainstorm-tmp/config.json`:

```json
{
  "topic": "...",
  "objective": "explore | solve | decide | innovate",
  "depth": "full | diverge | quick",
  "context": "..." | null,
  "timestamp": "ISO-8601"
}
```

### 3. Salvar topico

```bash
echo "{TOPIC}" > .brainstorm-tmp/topic.txt
```

### 4. Confirmar e iniciar

Apresentar resumo compacto ao usuario:

```
--- Brain Session ---
Topico:      {topic}
Objetivo:    {objective}
Profundidade: {depth}
Contexto:    {context ou "nenhum"}

Iniciando pipeline...
```

**NAO pedir confirmacao adicional. Iniciar imediatamente.**

---

## FASE 1+ — Execucao do Pipeline

Com base no `depth` escolhido, executar o workflow correspondente:

| depth | workflow | fases |
|-------|----------|-------|
| `full` | brain-pipeline.yaml | Todas (Diverge + Gate + Converge + Report) |
| `diverge` | diverge-only.yaml | Fase 1 apenas (Diverge + Synthesize + Cleanup) |
| `quick` | diverge-only.yaml | Round 1 apenas (skip Round 2) |

### Mapeamento objetivo → tipos de associacao

O `objective` influencia a selecao de tipos pelo ThemeDefiner:

| objective | tipos priorizados |
|-----------|-------------------|
| `explore` | Conexoes inesperadas, Analogias, Tendencias, Perguntas provocativas |
| `solve` | Dores e problemas, Causas raiz, Ferramentas/Recursos, Contextos de aplicacao |
| `decide` | Opostos e tensoes, Consequencias, Principios, Perfis/Personas |
| `innovate` | Conexoes inesperadas, Analogias, Opostos e tensoes, Perguntas provocativas |

> Passar este mapeamento como hint para o ThemeDefiner, nao como restricao rigida.

### Se `context` fornecido

Incluir no prompt de cada agente gerador:

```
Context: {context}
```

---

## Regras

1. **Uma pergunta por vez** — nunca enviar todas de uma vez
2. **Multipla escolha sempre que possivel** — reduz fricao
3. **Topico obrigatorio** — sem topico nao ha pipeline
4. **Zero confirmacao pos-setup** — coletou, configurou, executa
5. **Respeitar depth** — se o usuario escolheu "rapido", nao sugira "completo"
6. **Idioma do usuario** — perguntas no mesmo idioma do topico/interacao


## Referência: references/squad/tasks/synthesize-insights.md

---
task: synthesizeInsights()
responsavel: "Synthesizer"
responsavel_type: Agente
atomic_layer: Molecule

Entrada:
  - nome: top3Json
    tipo: JSON
    descricao: "filterAndRank() R2 -> Synthesizer"
    obrigatorio: true
  - nome: topicText
    tipo: string
    descricao: "topic.txt -> Synthesizer"
    obrigatorio: true

Saida:
  - nome: finalOutput
    tipo: file
    descricao: "-> orquestrador (apresentar ao usuario) + -> buildReport()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] top3.json existe em .brainstorm-tmp/"
    - "[ ] topic.txt acessivel"
  post-conditions:
    - "[ ] final_output.md gerado com formato polido"
    - "[ ] Cada insight tem explicacao + origem + justificativa"
---

# synthesizeInsights()

```
[top3.json + topic] --> [Synthesizer] --> [final_output.md]
```

Formata os 3 insights finais em documento polido com explicacoes detalhadas, trace de origem e metricas do processo.


## Referência: references/squad/templates/schemas.md

# Output Schemas — Brain Squad

## Schema: themes.json

```json
[
  {
    "id": 1,
    "type": "Analogias",
    "description": "Comparacoes com outros dominios"
  }
]
```

## Schema: Item de Geracao (agent-{N}.txt)

```
1. Titulo do Item | keyword1, keyword2, keyword3 | 8 | H/M
2. Outro Item | keyword1, keyword2 | 7 | M/L
```

Formato por linha: `N. Titulo | keywords CSV | relevancia 1-10 | impacto/esforco H/M/L`

## Schema: top10.json

```json
[
  {
    "rank": 1,
    "title": "Titulo do insight",
    "keywords": ["k1", "k2", "k3"],
    "score": 9,
    "source_type": "Analogias",
    "one_line": "Descricao curta de uma linha"
  }
]
```

## Schema: top3.json

```json
[
  {
    "rank": 1,
    "title": "Titulo do insight",
    "explanation": "3-5 sentencas conectando ao topico original",
    "origin": "R1 tipo Analogias -> R2 expansao sobre X",
    "why": "Justificativa: acionabilidade + profundidade + originalidade"
  }
]
```

## Schema: selected_insight.json

```json
{
  "topic": "topico original",
  "title": "titulo do insight selecionado",
  "explanation": "explicacao detalhada",
  "origin": "trace de origem R1 -> R2",
  "why_selected": "justificativa da selecao"
}
```

## Schema: final_output.md

```markdown
# Brainstorming: {TOPIC}

## Processo
- **Rodada 1:** 10 agentes x 10 associacoes = 100 itens gerados
- **Rodada 2:** 10 agentes x 10 expansoes = 100 itens gerados
- **Total explorado:** 200 itens -> filtrado para 3

---

## Insight #1: {Title}

{Explicacao detalhada 3-5 sentencas}

**Origem:** {Origin trace}

---

## Insight #2: {Title}

{Explicacao}

**Origem:** {Origin trace}

---

## Insight #3: {Title}

{Explicacao}

**Origem:** {Origin trace}

---

> Estes 3 insights foram selecionados entre 200 itens gerados por 24 agentes em 2 rodadas de brainstorming divergente.
```

## Schema: brain_report.md

```markdown
# {TOPIC} — Brain Report

## Fase 1: Exploracao Divergente
- Processo: 24 agentes, 2 rodadas, 200 itens explorados
- Top 3 Insights (resumo com titulos e 1 linha cada)

## Fase 2: Design Convergente
- Insight selecionado: {titulo}
- Resumo de entendimento (5-7 bullets)
- Suposicoes documentadas
- Design final (secoes incrementais)
- Decision Log (decisao, alternativas, justificativa)

## Plano de Implementacao
- (se o usuario solicitou handoff)
```


## Referência: references/squad/workflows/brain-pipeline.yaml

```yaml
workflow_name: brain_pipeline
description: "Pipeline completo Diverge+Converge — gera 200+ ideias com swarm, filtra Top 3, refina insight selecionado em design validado"

agent_sequence:
  - theme-definer
  - idea-generator
  - filter-ranker
  - idea-generator
  - filter-ranker
  - synthesizer
  - design-facilitator
  - report-builder

key_commands:
  - "*define-themes"
  - "*generate-ideas"
  - "*filter-rank-r1"
  - "*filter-rank-final"
  - "*synthesize"
  - "*facilitate-design"
  - "*build-report"

trigger_threshold: 1
typical_duration: "15-30 minutes"

success_indicators:
  - "Top 3 insights gerados e apresentados ao usuario"
  - "Insight selecionado refinado em design validado"
  - "brain_report.md consolidado"
  - ".brainstorm-tmp/ limpo"

transitions:
  phase_1_setup:
    trigger: "Topico recebido e .brainstorm-tmp/ criado com topic.txt"
    confidence: 0.95
    next_steps:
      - command: "*define-themes"
        description: "ThemeDefiner define 10 tipos de associacao"
        priority: 1

  phase_2_round1_generate:
    trigger: "themes.json gerado com 10 tipos de associacao"
    confidence: 0.95
    next_steps:
      - command: "*generate-ideas"
        description: "10x IdeaGenerator Haiku em paralelo (R1)"
        priority: 1

  phase_3_round1_rank:
    trigger: "Todos os 10 arquivos agent-*.txt existem em .brainstorm-tmp/r1/"
    confidence: 0.90
    next_steps:
      - command: "*filter-rank-r1"
        description: "FilterRanker Sonnet filtra 100 itens para Top 10"
        priority: 1

  phase_4_round2_generate:
    trigger: "top10.json e top10_summary.txt gerados"
    confidence: 0.95
    next_steps:
      - command: "*generate-ideas"
        description: "10x IdeaGenerator Haiku em paralelo (R2, expandindo Top 10)"
        priority: 1

  phase_5_round2_rank:
    trigger: "Todos os 10 arquivos agent-*.txt existem em .brainstorm-tmp/r2/"
    confidence: 0.90
    next_steps:
      - command: "*filter-rank-final"
        description: "FilterRanker Sonnet filtra para Top 3 final"
        priority: 1

  phase_6_synthesize:
    trigger: "top3.json gerado com 3 insights ranqueados"
    confidence: 0.95
    next_steps:
      - command: "*synthesize"
        description: "Synthesizer Sonnet formata output final"
        priority: 1

  gate_transition:
    trigger: "final_output.md apresentado ao usuario e insight selecionado"
    confidence: 0.90
    next_steps:
      - command: "*facilitate-design"
        description: "DesignFacilitator Opus inicia facilitacao interativa"
        priority: 1

  phase_7_design:
    trigger: "Understanding Lock confirmado e design aceito pelo usuario"
    confidence: 0.90
    next_steps:
      - command: "*build-report"
        description: "ReportBuilder Sonnet consolida relatorio final"
        priority: 1

  phase_8_cleanup:
    trigger: "brain_report.md gerado e apresentado ao usuario"
    confidence: 0.95
    next_steps:
      - command: "cleanup"
        description: "rm -rf .brainstorm-tmp/"
        priority: 1
```


## Referência: references/squad/workflows/diverge-only.yaml

```yaml
workflow_name: diverge_only
description: "Pipeline somente Fase 1 (Diverge) — gera 200+ ideias e filtra Top 3 sem fase de design"

agent_sequence:
  - theme-definer
  - idea-generator
  - filter-ranker
  - idea-generator
  - filter-ranker
  - synthesizer

key_commands:
  - "*define-themes"
  - "*generate-ideas"
  - "*filter-rank-r1"
  - "*filter-rank-final"
  - "*synthesize"

trigger_threshold: 1
typical_duration: "8-15 minutes"

success_indicators:
  - "Top 3 insights gerados e apresentados ao usuario"
  - "final_output.md gerado"
  - ".brainstorm-tmp/ limpo"

transitions:
  phase_1_setup:
    trigger: "Topico recebido e .brainstorm-tmp/ criado"
    confidence: 0.95
    next_steps:
      - command: "*define-themes"
        description: "ThemeDefiner define 10 tipos de associacao"
        priority: 1

  phase_2_round1:
    trigger: "themes.json gerado"
    confidence: 0.95
    next_steps:
      - command: "*generate-ideas"
        description: "10x IdeaGenerator R1 em paralelo"
        priority: 1

  phase_3_rank1:
    trigger: "10 arquivos R1 gerados"
    confidence: 0.90
    next_steps:
      - command: "*filter-rank-r1"
        description: "FilterRanker filtra para Top 10"
        priority: 1

  phase_4_round2:
    trigger: "top10.json gerado"
    confidence: 0.95
    next_steps:
      - command: "*generate-ideas"
        description: "10x IdeaGenerator R2 em paralelo"
        priority: 1

  phase_5_rank2:
    trigger: "10 arquivos R2 gerados"
    confidence: 0.90
    next_steps:
      - command: "*filter-rank-final"
        description: "FilterRanker filtra para Top 3"
        priority: 1

  phase_6_output:
    trigger: "top3.json gerado"
    confidence: 0.95
    next_steps:
      - command: "*synthesize"
        description: "Synthesizer formata output final"
        priority: 1

  cleanup:
    trigger: "final_output.md apresentado ao usuario"
    confidence: 0.95
    next_steps:
      - command: "cleanup"
        description: "rm -rf .brainstorm-tmp/"
        priority: 1
```
