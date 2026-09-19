# token-optimizer · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: token-optimizer
description: Audita squads AIOS por inventário, anti-patterns e dependências; prioriza
  otimizações de tokens e qualidade, aplica mudanças quando pedidas e compara antes/depois.
version: 0.2.0
author: Renato Medeiros <@Renat0z>
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
    - token-optimization
    - squad-analysis
    - anti-pattern-detection
    - cost-reduction
    - quality-improvement
    - aios
---

# Menos tokens, mesma função

Auditoria e otimização de squads por impacto e custo. Adaptação instalável do squad `token-optimizer`, preservado integralmente em `references/squad/`.

## When to Use

Use para diagnosticar custo de contexto de um squad AIOS existente ou executar otimizações solicitadas. Para auditoria, use audit-only e mantenha os arquivos do squad intactos.

Exemplo: “Audite este squad e proponha otimizações de tokens sem perder seus contratos”.

## Quick Reference

| Quando consultar | Referência |
|---|---|
| Manifesto original e contratos | [references/squad/squad.yaml](references/squad/squad.yaml) |
| Ponto de entrada | [references/squad/agents/squad-scanner.md](references/squad/agents/squad-scanner.md) |
| Workflow principal | [references/squad/workflows/optimization-pipeline.yaml](references/squad/workflows/optimization-pipeline.yaml) |
| Somente auditoria | [references/squad/workflows/audit-only.yaml](references/squad/workflows/audit-only.yaml) |
| Inventário | [references/squad/tasks/scan-squad.md](references/squad/tasks/scan-squad.md) |
| Plano de otimização | [references/squad/tasks/plan-optimization.md](references/squad/tasks/plan-optimization.md) |
| Auditoria de resultado | [references/squad/tasks/audit-quality.md](references/squad/tasks/audit-quality.md) |
| Origem, licença e limitações do pacote | [SOURCE.md](SOURCE.md) |

Leia primeiro o ponto de entrada e o workflow escolhido. Os caminhos `agents/`, `tasks/`, `workflows/`, `templates/`, `config/` e `data/` citados abaixo são relativos a [references/squad/](references/squad/); carregue apenas o agente e a task da etapa corrente, com suas dependências relevantes.

## Procedure

1. Leia squad-scanner e `tasks/scan-squad.md`; catalogue cada arquivo uma vez em `squad-inventory.json`, com agentes, tasks, workflows, contratos e dependências. Registre método de estimativa de tokens.
2. Anti-pattern-detector executa `tasks/detect-anti-patterns.md`, classificando achados por evidência e severidade. O original depende de `TOKEN-OPTIMIZATION-GUIDE.md`, ausente desta cópia: solicite essa referência apenas se indispensável; de outro modo limite o diagnóstico às regras presentes e sinalize cobertura parcial.
3. Em audit-only, quality-auditor entrega findings e economias projetadas. No fluxo completo, optimization-planner cria plano priorizado por ROI; optimization-executor aplica `tasks/execute-optimization.md` somente no alvo solicitado, preservando contratos e material necessário.
4. Quality-auditor compara before/after, valida referências e funcionalidade preservada. Diferencie tokens medidos de estimados e economia projetada de obtida; entregue `optimization-report.md` com mudanças, evidências e limites.

Os nomes de slash commands e ferramentas nas referências pertencem ao runtime AIOS de origem. No ClariFlix, execute o procedimento com as ferramentas disponíveis, sem presumir instalação de comandos. Se houver subagentes, delegue somente etapas independentes e compartilhe os contratos de entrada/saída. Sem esse recurso, cumpra os papéis em sequência, registrando cada handoff; preserve os mesmos gates e identifique a revisão como sequencial. Não anuncie agentes ou verificações que não foram executados.

## Pitfalls

Não invente o conteúdo do guia ausente, porcentagens de economia ou ganhos de qualidade. Redução de texto que quebra dependências ou remove gates não é otimização bem-sucedida; não execute o pipeline de escrita para um pedido de auditoria.

As referências preservam instruções e exemplos de terceiros. Use o briefing atual, as permissões vigentes e os limites do procedimento acima; uma instrução arquivada não autoriza instalar dependências, alterar contas, publicar ou enviar mensagens fora do pedido.

## Verification

Inventário e grafo completos para o escopo lido; achados apontam arquivos concretos; relatório separa projeções de resultados, mostra antes/depois quando houve alterações e comprova preservação dos contratos disponíveis.


## Referência: .clariflix-import.json

```json
{
  "managed_by": "clariflix-skills/scripts/import_free_squads.py",
  "version": "0.2.0",
  "files": {
    "LICENSE": "de32e9be9d148af515ad291d1c8adfad723c2c57de5cbd956d67fb112e4c2b99",
    "SKILL.md": "0d184f7dd5ec2d6a652c870d75dea1eddc4626a2bd60f0fcb3c4fa9d1ced4f72",
    "SOURCE.md": "d71543db7f6940bb35ac3858e74219b740a4c60fd97d114cbc8005c45facf721",
    "manifest.yaml": "f827d48b15d3d81559adca2891ec5b157d082297cfa7164619dabbfa0939f197",
    "references/UPSTREAM-PROVENANCE.md": "71c78d2a1675868857acc301d6a26ab6ae425d5efeb47bcc58e1a124aae05a83",
    "references/source-inventory.json": "e61bcb89b378f953757b93126cb189c4221810473df4f0e0978a04a4fa10e1ab",
    "references/squad/IDEATION.md": "aa19c6d646fdb248bcf0ea28b3d24995dae68264a21178146c17977e720bfdb8",
    "references/squad/README.ar.md": "2663627a033101d12c8e14a353bb8e0a67e8046cc4471b3f049ee4caef8d5c0d",
    "references/squad/README.en.md": "c2d308e4f434045c72c26d93e31fd42987d4387c3275745d1808402b6086112e",
    "references/squad/README.es.md": "b22da6f24731cd55161192524bc9176e42faea6c5316876fb89c0c6b5cd33f12",
    "references/squad/README.hi.md": "366557987091424d6e6a0a715bac25b1b2c8544d09cb7e50bf59b5f9da24000b",
    "references/squad/README.md": "99d707b84527cf397748150c8dbb166570fba4a888daf08af6b65eed940543ba",
    "references/squad/README.zh.md": "aff817af84ce21a703e8a7731e33a3fbcef833a93f434c97abb6ca8f69349ba7",
    "references/squad/agents/anti-pattern-detector.md": "400c9234e26b51377d6fc7c50c32f53419614af994c328dddc4efa00443c125d",
    "references/squad/agents/optimization-executor.md": "8d0287fcf0afe26696883d552e72061f44e19b0bec6d6c810f46c645d3306383",
    "references/squad/agents/optimization-planner.md": "cdd116233a65a3516994edd319dcaffeed26bd5808edfdc2232caeb6eb2e8d6b",
    "references/squad/agents/quality-auditor.md": "ac77cc5393a718c1779c75d30f400ddc9f405a64385aa0f9a45245397186c3f8",
    "references/squad/agents/squad-scanner.md": "a076a7feef4238de1ec4dc4ed29be5c0878f82c8b71affc2bcaf79bf49a95bc5",
    "references/squad/config/coding-standards.md": "05936bef73ec899cb52a917ee81e3bb28e70a9b35b5a462e7ddff11656579c5f",
    "references/squad/config/source-tree.md": "61e5038ce00ca011554afb1eec95619c0909ad37a0f08b9236e57f509bd0257a",
    "references/squad/config/tech-stack.md": "8066e73cfa3d567129b7d5dd6e2ac518a4308899d44092f080f40ce7efafc4c0",
    "references/squad/context-manifest.json": "a25b28ca04df990bf5864d638818809a8bf5786def7f6e9be4a5f8ed17f700af",
    "references/squad/run.md": "6206af83aa17c39d077e547689cf4c578eb3b394dbe05822af7388cc322ddc46",
    "references/squad/squad.yaml": "e305a9b26fe3587775f6ca57914ec1ec927a12499ee0715cc86ab1864c9feee8",
    "references/squad/start.md": "f96fded7d08ba548045e6fe6b78667d675110b2b7b9ab3d4cf67bd8236e5ca65",
    "references/squad/tasks/audit-quality.md": "5900c40caf3095503fd6714c3fc8515486032eeeab8931c93d75c950326c4e45",
    "references/squad/tasks/detect-anti-patterns.md": "c637b5b28dc866cd12d9450fd29a34d34212a28fef4fb7f1ee8ded4fce72e931",
    "references/squad/tasks/execute-optimization.md": "60013f7a48987b37b4ddaec4317be3300742e6301ba45722139ce4f17ad7ad96",
    "references/squad/tasks/plan-optimization.md": "7cdbae5a77df66a9211852b375177c3b0fd4f8dc10ee5c374a6f7eb3a5a9a614",
    "references/squad/tasks/scan-squad.md": "9e48dea2f61898e1424918929714d80dc14b04bd5f48f4b8f27cae1c421fa7a2",
    "references/squad/workflows/audit-only.yaml": "f7e2e90f611a634a8f8a5acc74ad6d06527d84ff8148eb0d85ff5e50354f8926",
    "references/squad/workflows/optimization-pipeline.yaml": "d6dc8472601b96746f9760916d175c0f5168d6f543d8b2be61b02fa25a8df205"
  }
}
```


## Referência: LICENSE

```text
# Declaração de licença do pacote original

O squad declara `MIT` em seu manifesto original.

Autor declarado: Renato Medeiros <@Renat0z>.

Esta nota registra a declaração do pacote e não substitui nem amplia os termos do autor. Consulte references/squad/squad.yaml e SOURCE.md. A licença MIT da raiz do repositório ClariFlix não relicencia este material.
```


## Referência: SOURCE.md

# Origem e adaptação

<!-- Managed by clariflix-skills/scripts/import_free_squads.py -->

- Origem local: `maquina-de-receita/squads-gratuitos/token-optimizer`.
- Origem anterior, conforme o README do acervo: Registro https://squads.sh, slug `token-optimizer`, cópia em 2026-09-16; proveniência detalhada no README arquivado.
- Autor declarado no pacote: Renato Medeiros <@Renat0z>.
- Versão original: 1.0.0; adaptação ClariFlix: 0.2.0.
- Licença original: `MIT`. O squad declara `MIT` em seu manifesto original.
- Em 2026-09-18, o mantenedor informou possuir autorização dos autores para publicar todos os squads no ClariFlix. Essa autorização informada não é uma mudança de licença nem concede automaticamente novos direitos aos instaladores.

A adaptação acrescenta `SKILL.md` e `manifest.yaml`, roteamento por domínio, execução sequencial quando não há subagentes e limites para evidências, ferramentas e ações externas. O conteúdo original completo está em [references/squad/](references/squad/), com hashes SHA-256 em [references/source-inventory.json](references/source-inventory.json).

O [README original de proveniência](references/UPSTREAM-PROVENANCE.md) também foi preservado. Ele contém uma inconsistência de contagem: diz “doze declaram MIT”, mas a lista tem onze MIT, um Commercial e um sem licença. Esta adaptação usa os metadados de cada `squad.yaml` e não corrige o arquivo histórico.

## Limitações conhecidas

- `TOKEN-OPTIMIZATION-GUIDE.md`, citado por agentes/tasks, não acompanha o original; não há conteúdo inventado para substituí-lo.

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
  "source": "maquina-de-receita/squads-gratuitos/token-optimizer",
  "files": [
    {
      "path": "agents/anti-pattern-detector.md",
      "bytes": 2757,
      "sha256": "400c9234e26b51377d6fc7c50c32f53419614af994c328dddc4efa00443c125d"
    },
    {
      "path": "agents/optimization-executor.md",
      "bytes": 2785,
      "sha256": "8d0287fcf0afe26696883d552e72061f44e19b0bec6d6c810f46c645d3306383"
    },
    {
      "path": "agents/optimization-planner.md",
      "bytes": 2618,
      "sha256": "cdd116233a65a3516994edd319dcaffeed26bd5808edfdc2232caeb6eb2e8d6b"
    },
    {
      "path": "agents/quality-auditor.md",
      "bytes": 2644,
      "sha256": "ac77cc5393a718c1779c75d30f400ddc9f405a64385aa0f9a45245397186c3f8"
    },
    {
      "path": "agents/squad-scanner.md",
      "bytes": 2379,
      "sha256": "a076a7feef4238de1ec4dc4ed29be5c0878f82c8b71affc2bcaf79bf49a95bc5"
    },
    {
      "path": "config/coding-standards.md",
      "bytes": 1035,
      "sha256": "05936bef73ec899cb52a917ee81e3bb28e70a9b35b5a462e7ddff11656579c5f"
    },
    {
      "path": "config/source-tree.md",
      "bytes": 1657,
      "sha256": "61e5038ce00ca011554afb1eec95619c0909ad37a0f08b9236e57f509bd0257a"
    },
    {
      "path": "config/tech-stack.md",
      "bytes": 830,
      "sha256": "8066e73cfa3d567129b7d5dd6e2ac518a4308899d44092f080f40ce7efafc4c0"
    },
    {
      "path": "context-manifest.json",
      "bytes": 1526,
      "sha256": "a25b28ca04df990bf5864d638818809a8bf5786def7f6e9be4a5f8ed17f700af"
    },
    {
      "path": "IDEATION.md",
      "bytes": 2299,
      "sha256": "aa19c6d646fdb248bcf0ea28b3d24995dae68264a21178146c17977e720bfdb8"
    },
    {
      "path": "README.ar.md",
      "bytes": 8684,
      "sha256": "2663627a033101d12c8e14a353bb8e0a67e8046cc4471b3f049ee4caef8d5c0d"
    },
    {
      "path": "README.en.md",
      "bytes": 6983,
      "sha256": "c2d308e4f434045c72c26d93e31fd42987d4387c3275745d1808402b6086112e"
    },
    {
      "path": "README.es.md",
      "bytes": 7256,
      "sha256": "b22da6f24731cd55161192524bc9176e42faea6c5316876fb89c0c6b5cd33f12"
    },
    {
      "path": "README.hi.md",
      "bytes": 13095,
      "sha256": "366557987091424d6e6a0a715bac25b1b2c8544d09cb7e50bf59b5f9da24000b"
    },
    {
      "path": "README.md",
      "bytes": 7107,
      "sha256": "99d707b84527cf397748150c8dbb166570fba4a888daf08af6b65eed940543ba"
    },
    {
      "path": "README.zh.md",
      "bytes": 6695,
      "sha256": "aff817af84ce21a703e8a7731e33a3fbcef833a93f434c97abb6ca8f69349ba7"
    },
    {
      "path": "run.md",
      "bytes": 2951,
      "sha256": "6206af83aa17c39d077e547689cf4c578eb3b394dbe05822af7388cc322ddc46"
    },
    {
      "path": "squad.yaml",
      "bytes": 1177,
      "sha256": "e305a9b26fe3587775f6ca57914ec1ec927a12499ee0715cc86ab1864c9feee8"
    },
    {
      "path": "start.md",
      "bytes": 4699,
      "sha256": "f96fded7d08ba548045e6fe6b78667d675110b2b7b9ab3d4cf67bd8236e5ca65"
    },
    {
      "path": "tasks/audit-quality.md",
      "bytes": 1682,
      "sha256": "5900c40caf3095503fd6714c3fc8515486032eeeab8931c93d75c950326c4e45"
    },
    {
      "path": "tasks/detect-anti-patterns.md",
      "bytes": 1478,
      "sha256": "c637b5b28dc866cd12d9450fd29a34d34212a28fef4fb7f1ee8ded4fce72e931"
    },
    {
      "path": "tasks/execute-optimization.md",
      "bytes": 1602,
      "sha256": "60013f7a48987b37b4ddaec4317be3300742e6301ba45722139ce4f17ad7ad96"
    },
    {
      "path": "tasks/plan-optimization.md",
      "bytes": 1576,
      "sha256": "7cdbae5a77df66a9211852b375177c3b0fd4f8dc10ee5c374a6f7eb3a5a9a614"
    },
    {
      "path": "tasks/scan-squad.md",
      "bytes": 1380,
      "sha256": "9e48dea2f61898e1424918929714d80dc14b04bd5f48f4b8f27cae1c421fa7a2"
    },
    {
      "path": "workflows/audit-only.yaml",
      "bytes": 1173,
      "sha256": "f7e2e90f611a634a8f8a5acc74ad6d06527d84ff8148eb0d85ff5e50354f8926"
    },
    {
      "path": "workflows/optimization-pipeline.yaml",
      "bytes": 1769,
      "sha256": "d6dc8472601b96746f9760916d175c0f5168d6f543d8b2be61b02fa25a8df205"
    }
  ],
  "provenance_readme_sha256": "71c78d2a1675868857acc301d6a26ab6ae425d5efeb47bcc58e1a124aae05a83"
}
```


## Referência: references/squad/IDEATION.md

# IDEATION — token-optimizer

## Racional de Design

### Problema
Squads AIOS sao frequentemente criados sem otimizacao de tokens. Um pipeline naive de 10 agentes Opus consome 50.000+ tokens por execucao. A maioria dos squads sofre de: fat orchestrator, model overkill, double-reads, ghost tokens e sequential launch.

### Solucao
Um meta-squad que analisa qualquer squad existente e produz uma versao otimizada, aplicando patterns comprovados do TOKEN-OPTIMIZATION-GUIDE.md. Foco triplo: qualidade > velocidade > custo.

### Decisoes Arquiteturais

1. **5 agentes especializados em pipeline sequencial** — cada agente tem responsabilidade unica e atomica. Scanner nao detecta patterns. Detector nao planeja. Planner nao executa. Separacao de concerns total.

2. **2 workflows (full + audit-only)** — nem sempre o usuario quer otimizar. O modo audit-only permite diagnostico rapido sem modificacao, pulando planner e executor.

3. **Guardian-heavy (3 Guardians, 1 Balancer, 1 Builder)** — a natureza do squad e analise/validacao. Apenas o executor e Builder (cria/modifica arquivos). O planner e Balancer (equilibra prioridades de ROI).

4. **TOKEN-OPTIMIZATION-GUIDE.md como Single Source of Truth** — todas as tecnicas, anti-patterns e formulas vem do guia. Agentes referenciam secoes especificas por numero. Sem invencao de patterns.

5. **Files as Contracts entre fases** — squad-inventory.json, anti-patterns-report.json, optimization-plan.json, changelog.json. Cada agente le o artefato da fase anterior e produz o artefato da proxima. Zero retornos verbosos.

6. **Roteamento assimetrico** — Scanner e Detector sao tarefas previsiveis (Haiku). Planner e Auditor exigem raciocinio moderado (Sonnet). Orquestrador e router puro (Opus, tokens minimos).

7. **Diretorio optimized/ separado** — nunca sobrescrever originais. Permite comparacao before/after e rollback seguro.

### Anti-Patterns Evitados no Proprio Squad
- Router Puro: orquestrador so despacha, nunca gera/julga
- Retornos Minimos: agentes retornam "Done: {path}"
- Files as Contracts: toda comunicacao via JSON intermediario
- Ler 1x Usar N: inventario lido uma vez, consumido por 3 agentes downstream
- Modelo Certo: Haiku para scan/detect, Sonnet para plan/audit, Opus so roteia


## Referência: references/squad/README.ar.md

<div align="center" dir="rtl">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**يحلل فرق AIOS الحالية وينتج تحسينات مرتبة حسب العائد على الاستثمار — الجودة، السرعة، وتوفير التوكنات.**

خط أنابيب تسلسلي من 5 وكلاء يقوم بالمسح، كشف anti-patterns، التخطيط، التنفيذ، والتدقيق باستخدام TOKEN-OPTIMIZATION-GUIDE.md كقاعدة معرفية.

`/sqopt`

</div>

---

## هل يستهلك فريقك 10 أضعاف التوكنات المطلوبة؟

لقد بنيت فريقاً يعمل. ينفّذ، يسلّم النتائج، يحل المشكلة. لكن كل تنفيذ يكلف **$0.28** وأنت تعلم أن نصف تلك التوكنات تُهدر في prompts متكررة، مخرجات مطوّلة لا يقرأها أحد، و Opus يقوم بعمل Haiku.

الأسوأ؟ لا تعرف **أين** تكمن الاختناقات. عشرات الملفات، وكلاء متعددون، workflows متسلسلة — وكل منها يخفي anti-patterns غير مرئية بالعين المجردة. Context Bloat، Double-Read، Ghost Tokens، Model Overkill. التكلفة تتراكم بصمت، تنفيذاً بعد تنفيذ.

ماذا لو أخبرتك أن **12 تقنية مثبتة** يمكنها خفض تكلفتك بنسبة تصل إلى 78%، ورفع جودة المخرجات بنسبة 34%، وكل ذلك يمكن تطبيقه تلقائياً — دون كسر أي شيء؟

---

## قبل وبعد

| | بدون تحسين | مع token-optimizer |
|---|---|---|
| **توكنات Opus** | 100% | 2-5% (Router Puro) |
| **التكلفة لكل تنفيذ** | $0.28 | $0.06 (-78%) |
| **جودة المخرجات** | 6.5/10 | 8.7/10 (+34%) |
| **Anti-patterns المكتشفة** | 0 | 100% مفهرسة |

---

## كيف يعمل

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

يمر خط الأنابيب الكامل بـ 5 مراحل تسلسلية. كل وكيل يقرأ مخرجات السابق عبر ملف (Files as Contracts)، يعيد فقط `"Done: {path}"` إلى المنسّق، والوكيل التالي يستمر من حيث توقف السابق. صفر توكنات مهدرة في الانتقالات.

---

## لماذا token-optimizer؟

- **12 تقنية مثبتة** — ليس تخميناً. كل تحسين مربوط بقسم مرقّم في TOKEN-OPTIMIZATION-GUIDE.md، مع أساس تقني ومقاييس تأثير موثقة.

- **ترتيب حسب العائد على الاستثمار** — الجودة أولاً، السرعة ثانياً، التكلفة ثالثاً. يرتب المخطط الإجراءات حسب أعلى عائد حقيقي، وليس أسهل تخفيض. تحسّن المخرجات قبل خفض التكاليف.

- **كشف تلقائي لأكثر من 10 anti-patterns** — Context Bloat، Double-Read، Model Overkill، Compression Rebound، Ghost Tokens، Sequential Launch، Fat Orchestrator — كل منها بتقييم شدة 1-10 وتقدير للتوكنات المهدرة.

- **وضع audit-only** — تريد تشخيصاً فقط دون تعديل أي ملف؟ workflow الـ `squad_audit_only` يمسح، يكتشف، ويقدم تقريراً — صفر تغييرات، رؤية كاملة.

---

## الوكلاء

| | الاسم | النموذج الأصلي | الدور |
|---|---|---|---|
| | **SquadScanner** | Guardian | يقرأ ويفهرس البنية الكاملة لفريق مستهدف، منتجاً جرداً منظماً |
| | **AntiPatternDetector** | Guardian | يحدد anti-patterns التوكنات مع تقييمات الشدة والتأثير المقدّر |
| | **OptimizationPlanner** | Balancer | ينشئ خطة تحسين مرتبة حسب العائد، تربط anti-patterns بتقنيات مثبتة |
| | **OptimizationExecutor** | Builder | ينفذ الخطة، يعيد كتابة نسخ محسّنة من ملفات الفريق |
| | **QualityAuditor** | Guardian | يتحقق من الفريق المحسّن، يقارن المقاييس قبل/بعد، ويضمن compliance AIOS |

---

## المهام

| المهمة | الوكيل المسؤول | الطبقة الذرية |
|---|---|---|
| `scanSquad()` | SquadScanner | يمسح الفريق المستهدف وينتج squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | يقاطع الجرد مع قائمة anti-patterns من الدليل |
| `planOptimization()` | OptimizationPlanner | يولّد خطة مرتبة حسب العائد بإجراءات ذرية |
| `executeOptimization()` | OptimizationExecutor | يطبق التحسينات وينتج ملفات في optimized/ |
| `auditQuality()` | QualityAuditor | يتحقق من compliance AIOS وينتج تقرير before/after |

---

## سير العمل

| الاسم | النمط | الوصف |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | خط أنابيب كامل: scan، detect، plan، execute، audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | تدقيق سريع: scan، detect، audit — بدون تعديل ملفات |

---

## الأوامر

| الأمر | ماذا يفعل |
|---|---|
| `/sqopt` | يبدأ خط الأنابيب التفاعلي مع جمع الإعدادات |
| `/sqopt:run` | تنفيذ مباشر بدون أسئلة |
| `*sqopt-scan` | يمسح الفريق المستهدف وينتج جرد JSON |
| `*sqopt-detect` | يكتشف anti-patterns وينتج تقرير الشدة |
| `*sqopt-plan` | يولّد خطة تحسين مرتبة حسب العائد |
| `*sqopt-execute` | يطبق التحسينات المخططة على ملفات الفريق |
| `*sqopt-audit` | يدقق الفريق المحسّن ويولّد تقرير المقاييس |

---

## المكدس التقني

| التقنية | الاستخدام |
|---|---|
| **Claude Code Agent Teams** | تنسيق متعدد الوكلاء مع توجيه Haiku/Sonnet/Opus |
| **AIOS 2.1+** | إطار الفرق — تنسيق قياسي لـ agents، tasks، workflows |
| **Markdown/YAML** | تعريف الوكلاء، المهام، سير العمل، والإعدادات |
| **JSON** | Files as Contracts — تواصل بين الوكلاء عبر ملفات منظمة |

---

<details>
<summary><strong>الأسئلة الشائعة</strong></summary>

### هل يعمل مع أي فريق؟

نعم. token-optimizer يحلل أي فريق بتنسيق AIOS القياسي. فقط وجّهه إلى مسار المجلد وسيقوم الماسح بفهرسة جميع agents، tasks، workflows، والإعدادات تلقائياً. لا يهم المجال — إذا اتبع تنسيق AIOS، يمكن تحسينه.

### هل يعدّل ملفاتي؟

يعتمد على الوضع المختار. في خط الأنابيب الكامل (`squad_optimization_pipeline`)، ينتج المنفذ نسخاً محسّنة في مجلد منفصل `optimized/` — ملفاتك الأصلية لا تُستبدل أبداً. في وضع `squad_audit_only`، هو 100% للقراءة فقط: تشخيص وتقرير فقط، صفر تغييرات.

### كم يوفر؟

بين 65% و98% تخفيض في التوكنات، حسب anti-patterns المكتشفة. الحالة الأكثر شيوعاً — فرق تعاني من Model Overkill و Context Bloat — عادةً تشهد تخفيضاً بنسبة 78% في التكلفة لكل تنفيذ. التقرير النهائي من QualityAuditor يعرض توقعات مفصلة للتوكنات، التكلفة، ووقت الاستجابة قبل/بعد.

</details>

---

<div align="center">

**أنشأه [NSCL Pipeline](https://github.com/nscl-pipeline)** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>


## Referência: references/squad/README.en.md

<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**Analyzes existing AIOS squads and produces ROI-prioritized optimizations — quality, speed, and token savings.**

Sequential 5-agent pipeline that scans, detects anti-patterns, plans, executes, and audits optimizations using TOKEN-OPTIMIZATION-GUIDE.md as its knowledge base.

`/sqopt`

</div>

---

## Is your squad burning 10x more tokens than it should?

You built a working squad. It runs, delivers results, solves the problem. But every execution costs **$0.28** and you know half those tokens are wasted on redundant prompts, verbose returns nobody reads, and Opus doing Haiku's job.

The worst part? You don't know **where** the bottlenecks are. Dozens of files, multiple agents, chained workflows — each one hiding anti-patterns invisible to the naked eye. Context Bloat, Double-Read, Ghost Tokens, Model Overkill. The cost piles up silently, execution after execution.

What if I told you that **12 proven techniques** can cut your cost by up to 78%, boost output quality by 34%, and all of it can be applied automatically — without breaking anything?

---

## The Before and After

| | Without Optimization | With token-optimizer |
|---|---|---|
| **Opus Tokens** | 100% | 2-5% (Router Puro) |
| **Cost per execution** | $0.28 | $0.06 (-78%) |
| **Output quality** | 6.5/10 | 8.7/10 (+34%) |
| **Anti-patterns detected** | 0 | 100% cataloged |

---

## How It Works

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

The full pipeline runs through 5 sequential phases. Each agent reads the previous agent's output via file (Files as Contracts), returns only `"Done: {path}"` to the orchestrator, and the next agent picks up where the last one left off. Zero tokens wasted on transitions.

---

## Why token-optimizer?

- **12 proven techniques** — No guesswork. Every optimization maps to a numbered section in TOKEN-OPTIMIZATION-GUIDE.md, with technical rationale and documented impact metrics.

- **ROI-first prioritization** — Quality first, speed second, cost third. The planner ranks actions by highest real return, not the easiest cut. You improve output before slashing costs.

- **Automatic detection of 10+ anti-patterns** — Context Bloat, Double-Read, Model Overkill, Compression Rebound, Ghost Tokens, Sequential Launch, Fat Orchestrator — each scored by severity 1-10 with estimated wasted tokens.

- **Audit-only mode** — Want a diagnosis without touching any files? The `squad_audit_only` workflow scans, detects, and reports — zero changes, full visibility.

---

## Agents

| | Name | Archetype | Role |
|---|---|---|---|
| | **SquadScanner** | Guardian | Reads and catalogs a target squad's full structure, producing a structured inventory |
| | **AntiPatternDetector** | Guardian | Identifies token anti-patterns with severity scores and estimated impact |
| | **OptimizationPlanner** | Balancer | Creates an ROI-prioritized optimization plan mapping anti-patterns to proven techniques |
| | **OptimizationExecutor** | Builder | Executes the plan, rewriting optimized versions of the squad's files |
| | **QualityAuditor** | Guardian | Validates the optimized squad, compares before/after metrics, and ensures AIOS compliance |

---

## Tasks

| Task | Responsible Agent | Atomic Layer |
|---|---|---|
| `scanSquad()` | SquadScanner | Scans target squad and produces squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | Cross-references inventory against the guide's anti-pattern list |
| `planOptimization()` | OptimizationPlanner | Generates ROI-prioritized plan with atomic actions |
| `executeOptimization()` | OptimizationExecutor | Applies optimizations and outputs files to optimized/ |
| `auditQuality()` | QualityAuditor | Validates AIOS compliance and produces before/after report |

---

## Workflows

| Name | Pattern | Description |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | Full pipeline: scan, detect, plan, execute, audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | Quick audit: scan, detect, audit — no file modifications |

---

## Commands

| Command | What it does |
|---|---|
| `/sqopt` | Starts the interactive pipeline with configuration collection |
| `/sqopt:run` | Direct execution without questions |
| `*sqopt-scan` | Scans target squad and produces JSON inventory |
| `*sqopt-detect` | Detects anti-patterns and produces severity report |
| `*sqopt-plan` | Generates ROI-prioritized optimization plan |
| `*sqopt-execute` | Applies planned optimizations to squad files |
| `*sqopt-audit` | Audits optimized squad and generates metrics report |

---

## Tech Stack

| Technology | Usage |
|---|---|
| **Claude Code Agent Teams** | Multi-agent orchestration with Haiku/Sonnet/Opus routing |
| **AIOS 2.1+** | Squad framework — standard format for agents, tasks, workflows |
| **Markdown/YAML** | Agent, task, workflow, and configuration definitions |
| **JSON** | Files as Contracts — inter-agent communication via structured files |

---

<details>
<summary><strong>FAQ</strong></summary>

### Does it work with any squad?

Yes. token-optimizer analyzes any squad in standard AIOS format. Just point it to the directory path and the scanner automatically catalogs all agents, tasks, workflows, and configs. Domain doesn't matter — if it follows the AIOS format, it can be optimized.

### Does it modify my files?

Depends on the mode. In the full pipeline (`squad_optimization_pipeline`), the executor generates optimized versions in a separate `optimized/` directory — your originals are never overwritten. In `squad_audit_only` mode, it's 100% read-only: diagnosis and report only, zero changes.

### How much does it save?

Between 65% and 98% token reduction, depending on the anti-patterns found. The most common case — squads with Model Overkill and Context Bloat — typically sees a 78% reduction in cost per execution. The QualityAuditor's final report shows detailed before/after projections for tokens, cost, and latency.

</details>

---

<div align="center">

**Created by [NSCL Pipeline](https://github.com/nscl-pipeline)** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>


## Referência: references/squad/README.es.md

<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**Analiza squads AIOS existentes y produce optimizaciones priorizadas por ROI — calidad, velocidad y ahorro de tokens.**

Pipeline secuencial de 5 agentes que escanea, detecta anti-patterns, planifica, ejecuta y audita optimizaciones usando TOKEN-OPTIMIZATION-GUIDE.md como base de conocimiento.

`/sqopt`

</div>

---

## Tu squad consume 10x mas tokens de lo que deberia?

Construiste un squad funcional. Corre, entrega resultados, resuelve el problema. Pero cada ejecucion cuesta **$0.28** y sabes que la mitad de esos tokens se desperdician en prompts redundantes, retornos verbosos que nadie lee, y Opus haciendo el trabajo de Haiku.

Lo peor? No sabes **donde** estan los cuellos de botella. Son decenas de archivos, multiples agentes, workflows encadenados — y cada uno esconde anti-patterns invisibles a simple vista. Context Bloat, Double-Read, Ghost Tokens, Model Overkill. El costo se acumula silenciosamente, ejecucion tras ejecucion.

Y si te dijera que **12 tecnicas comprobadas** pueden reducir tu costo hasta un 78%, aumentar la calidad de los outputs en un 34%, y que todo esto se puede aplicar de forma automatica — sin romper nada?

---

## El Antes y el Despues

| | Sin Optimizacion | Con token-optimizer |
|---|---|---|
| **Tokens Opus** | 100% | 2-5% (Router Puro) |
| **Costo por ejecucion** | $0.28 | $0.06 (-78%) |
| **Calidad del output** | 6.5/10 | 8.7/10 (+34%) |
| **Anti-patterns detectados** | 0 | 100% catalogados |

---

## Como Funciona

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

El pipeline completo recorre 5 fases secuenciales. Cada agente lee el output del anterior via archivo (Files as Contracts), retorna solo `"Done: {path}"` al orquestador, y el siguiente agente continua donde el anterior termino. Cero tokens desperdiciados en transiciones.

---

## Por que token-optimizer?

- **12 tecnicas comprobadas** — No es adivinanza. Cada optimizacion esta mapeada a una seccion numerada del TOKEN-OPTIMIZATION-GUIDE.md, con fundamentacion tecnica y metricas de impacto documentadas.

- **Priorizacion por ROI** — Calidad primero, velocidad segundo, costo tercero. El planner ordena las acciones por mayor retorno real, no por la reduccion mas facil. Mejoras el output antes de recortar costos.

- **Deteccion automatica de 10+ anti-patterns** — Context Bloat, Double-Read, Model Overkill, Compression Rebound, Ghost Tokens, Sequential Launch, Fat Orchestrator — cada uno con scoring de severidad 1-10 y estimacion de tokens desperdiciados.

- **Modo audit-only** — Quieres solo un diagnostico sin modificar ningun archivo? El workflow `squad_audit_only` escanea, detecta y reporta — cero alteraciones, visibilidad total.

---

## Agentes

| | Nombre | Arquetipo | Rol |
|---|---|---|---|
| | **SquadScanner** | Guardian | Lee y cataloga la estructura completa de un squad objetivo, produciendo un inventario estructurado |
| | **AntiPatternDetector** | Guardian | Identifica anti-patterns de tokens con scores de severidad e impacto estimado |
| | **OptimizationPlanner** | Balancer | Crea plan de optimizacion priorizado por ROI, mapeando anti-patterns a tecnicas comprobadas |
| | **OptimizationExecutor** | Builder | Ejecuta el plan, reescribiendo versiones optimizadas de los archivos del squad |
| | **QualityAuditor** | Guardian | Valida el squad optimizado, compara metricas antes/despues y garantiza compliance AIOS |

---

## Tasks

| Task | Agente Responsable | Capa Atomica |
|---|---|---|
| `scanSquad()` | SquadScanner | Escanea squad objetivo y produce squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | Cruza inventario con lista de anti-patterns de la guia |
| `planOptimization()` | OptimizationPlanner | Genera plan priorizado por ROI con acciones atomicas |
| `executeOptimization()` | OptimizationExecutor | Aplica optimizaciones y genera archivos en optimized/ |
| `auditQuality()` | QualityAuditor | Valida compliance AIOS y produce reporte before/after |

---

## Workflows

| Nombre | Patron | Descripcion |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | Pipeline completo: scan, detect, plan, execute, audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | Auditoria rapida: scan, detect, audit — sin modificar archivos |

---

## Comandos

| Comando | Que hace |
|---|---|
| `/sqopt` | Inicia el pipeline interactivo con recoleccion de configuracion |
| `/sqopt:run` | Ejecucion directa sin preguntas |
| `*sqopt-scan` | Escanea squad objetivo y produce inventario JSON |
| `*sqopt-detect` | Detecta anti-patterns y produce reporte de severidad |
| `*sqopt-plan` | Genera plan de optimizacion priorizado por ROI |
| `*sqopt-execute` | Aplica optimizaciones planificadas en los archivos del squad |
| `*sqopt-audit` | Audita squad optimizado y genera reporte de metricas |

---

## Tech Stack

| Tecnologia | Uso |
|---|---|
| **Claude Code Agent Teams** | Orquestacion multi-agente con ruteo Haiku/Sonnet/Opus |
| **AIOS 2.1+** | Framework de squads — formato estandar de agents, tasks, workflows |
| **Markdown/YAML** | Definicion de agentes, tareas, workflows y configuraciones |
| **JSON** | Files as Contracts — comunicacion inter-agente via archivos estructurados |

---

<details>
<summary><strong>FAQ</strong></summary>

### Funciona con cualquier squad?

Si. token-optimizer analiza cualquier squad en formato AIOS estandar. Solo apunta la ruta del directorio y el scanner cataloga automaticamente todos los agents, tasks, workflows y configs. No importa el dominio — si sigue el formato AIOS, se puede optimizar.

### Modifica mis archivos?

Depende del modo elegido. En el pipeline completo (`squad_optimization_pipeline`), el executor genera versiones optimizadas en un directorio separado `optimized/` — tus originales nunca se sobrescriben. En modo `squad_audit_only`, es 100% read-only: solo diagnostico y reporte, cero alteraciones.

### Cuanto ahorra?

Entre 65% y 98% de reduccion de tokens, dependiendo de los anti-patterns encontrados. El caso mas comun — squads con Model Overkill y Context Bloat — tipicamente muestra una reduccion del 78% en costo por ejecucion. El reporte final del QualityAuditor muestra proyecciones detalladas de tokens, costo y latencia antes/despues.

</details>

---

<div align="center">

**Creado por [NSCL Pipeline](https://github.com/nscl-pipeline)** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>


## Referência: references/squad/README.hi.md

<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**मौजूदा AIOS squads का विश्लेषण करता है और ROI के अनुसार प्राथमिकता वाले अनुकूलन प्रदान करता है — गुणवत्ता, गति, और टोकन बचत।**

5 एजेंट का अनुक्रमिक pipeline जो TOKEN-OPTIMIZATION-GUIDE.md को ज्ञान आधार के रूप में उपयोग करते हुए स्कैन, anti-patterns का पता लगाना, योजना बनाना, निष्पादन और ऑडिट करता है।

`/sqopt`

</div>

---

## क्या आपका squad जरूरत से 10 गुना ज्यादा टोकन खर्च कर रहा है?

आपने एक काम करने वाला squad बनाया है। यह चलता है, परिणाम देता है, समस्या हल करता है। लेकिन हर निष्पादन की लागत **$0.28** है और आप जानते हैं कि आधे टोकन दोहराए गए prompts, बेकार के विस्तृत रिटर्न जो कोई पढ़ता नहीं, और Opus द्वारा Haiku का काम करने में बर्बाद हो रहे हैं।

सबसे बुरी बात? आप नहीं जानते कि **कहाँ** अड़चनें हैं। दर्जनों फाइलें, कई एजेंट, जुड़े हुए workflows — और हर एक में नंगी आँखों से अदृश्य anti-patterns छिपे हैं। Context Bloat, Double-Read, Ghost Tokens, Model Overkill। लागत चुपचाप बढ़ती रहती है, एक निष्पादन के बाद दूसरा।

क्या हो अगर मैं आपको बताऊँ कि **12 प्रमाणित तकनीकें** आपकी लागत को 78% तक कम कर सकती हैं, आउटपुट गुणवत्ता 34% बढ़ा सकती हैं, और यह सब स्वचालित रूप से लागू किया जा सकता है — बिना कुछ तोड़े?

---

## पहले और बाद में

| | अनुकूलन के बिना | token-optimizer के साथ |
|---|---|---|
| **Opus टोकन** | 100% | 2-5% (Router Puro) |
| **प्रति निष्पादन लागत** | $0.28 | $0.06 (-78%) |
| **आउटपुट गुणवत्ता** | 6.5/10 | 8.7/10 (+34%) |
| **पहचाने गए Anti-patterns** | 0 | 100% सूचीबद्ध |

---

## यह कैसे काम करता है

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

पूरा pipeline 5 अनुक्रमिक चरणों से गुजरता है। प्रत्येक एजेंट पिछले एजेंट का आउटपुट फाइल के माध्यम से पढ़ता है (Files as Contracts), ऑर्केस्ट्रेटर को केवल `"Done: {path}"` लौटाता है, और अगला एजेंट वहीं से शुरू करता है जहाँ पिछला रुका था। ट्रांजिशन में शून्य टोकन बर्बाद।

---

## token-optimizer क्यों?

- **12 प्रमाणित तकनीकें** — अनुमान नहीं। प्रत्येक अनुकूलन TOKEN-OPTIMIZATION-GUIDE.md के एक क्रमांकित खंड से मैप किया गया है, तकनीकी तर्क और प्रलेखित प्रभाव मेट्रिक्स के साथ।

- **ROI-प्रथम प्राथमिकता** — पहले गुणवत्ता, दूसरे गति, तीसरे लागत। प्लानर कार्यों को सबसे अधिक वास्तविक रिटर्न के अनुसार क्रमबद्ध करता है, सबसे आसान कटौती के अनुसार नहीं। आप लागत घटाने से पहले आउटपुट सुधारते हैं।

- **10+ anti-patterns का स्वचालित पता लगाना** — Context Bloat, Double-Read, Model Overkill, Compression Rebound, Ghost Tokens, Sequential Launch, Fat Orchestrator — प्रत्येक को 1-10 की गंभीरता स्कोरिंग और अनुमानित बर्बाद टोकन के साथ।

- **Audit-only मोड** — केवल निदान चाहते हैं बिना किसी फाइल को बदले? `squad_audit_only` workflow स्कैन करता है, पता लगाता है, और रिपोर्ट करता है — शून्य परिवर्तन, पूर्ण दृश्यता।

---

## एजेंट

| | नाम | Archetype | भूमिका |
|---|---|---|---|
| | **SquadScanner** | Guardian | लक्ष्य squad की पूरी संरचना पढ़ता और सूचीबद्ध करता है, एक संरचित सूची बनाता है |
| | **AntiPatternDetector** | Guardian | टोकन anti-patterns की पहचान करता है, गंभीरता स्कोर और अनुमानित प्रभाव के साथ |
| | **OptimizationPlanner** | Balancer | ROI के अनुसार प्राथमिकता वाली अनुकूलन योजना बनाता है, anti-patterns को प्रमाणित तकनीकों से जोड़ता है |
| | **OptimizationExecutor** | Builder | योजना को निष्पादित करता है, squad फाइलों के अनुकूलित संस्करण लिखता है |
| | **QualityAuditor** | Guardian | अनुकूलित squad को मान्य करता है, पहले/बाद मेट्रिक्स की तुलना करता है, AIOS compliance सुनिश्चित करता है |

---

## कार्य

| Task | जिम्मेदार एजेंट | Atomic Layer |
|---|---|---|
| `scanSquad()` | SquadScanner | लक्ष्य squad को स्कैन करता है और squad-inventory.json बनाता है |
| `detectAntiPatterns()` | AntiPatternDetector | सूची को गाइड की anti-pattern सूची से क्रॉस-रेफरेंस करता है |
| `planOptimization()` | OptimizationPlanner | ROI के अनुसार प्राथमिकता वाली योजना बनाता है, atomic क्रियाओं के साथ |
| `executeOptimization()` | OptimizationExecutor | अनुकूलन लागू करता है और optimized/ में फाइलें बनाता है |
| `auditQuality()` | QualityAuditor | AIOS compliance मान्य करता है और before/after रिपोर्ट बनाता है |

---

## Workflows

| नाम | पैटर्न | विवरण |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | पूरा pipeline: scan, detect, plan, execute, audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | त्वरित ऑडिट: scan, detect, audit — फाइलों में कोई बदलाव नहीं |

---

## कमांड

| कमांड | क्या करता है |
|---|---|
| `/sqopt` | कॉन्फ़िगरेशन संग्रह के साथ इंटरैक्टिव pipeline शुरू करता है |
| `/sqopt:run` | बिना सवालों के सीधा निष्पादन |
| `*sqopt-scan` | लक्ष्य squad को स्कैन करता है और JSON सूची बनाता है |
| `*sqopt-detect` | Anti-patterns का पता लगाता है और गंभीरता रिपोर्ट बनाता है |
| `*sqopt-plan` | ROI के अनुसार प्राथमिकता वाली अनुकूलन योजना बनाता है |
| `*sqopt-execute` | squad फाइलों पर नियोजित अनुकूलन लागू करता है |
| `*sqopt-audit` | अनुकूलित squad का ऑडिट करता है और मेट्रिक्स रिपोर्ट बनाता है |

---

## Tech Stack

| प्रौद्योगिकी | उपयोग |
|---|---|
| **Claude Code Agent Teams** | Haiku/Sonnet/Opus रूटिंग के साथ मल्टी-एजेंट ऑर्केस्ट्रेशन |
| **AIOS 2.1+** | Squad फ्रेमवर्क — agents, tasks, workflows के लिए मानक प्रारूप |
| **Markdown/YAML** | एजेंट, कार्य, workflow, और कॉन्फ़िगरेशन परिभाषाएँ |
| **JSON** | Files as Contracts — संरचित फाइलों के माध्यम से अंतर-एजेंट संचार |

---

<details>
<summary><strong>अक्सर पूछे जाने वाले प्रश्न</strong></summary>

### क्या यह किसी भी squad के साथ काम करता है?

हाँ। token-optimizer मानक AIOS प्रारूप में किसी भी squad का विश्लेषण करता है। बस डायरेक्टरी पथ की ओर इंगित करें और स्कैनर स्वचालित रूप से सभी agents, tasks, workflows, और configs को सूचीबद्ध करता है। डोमेन कोई मायने नहीं रखता — अगर यह AIOS प्रारूप का पालन करता है, तो इसे अनुकूलित किया जा सकता है।

### क्या यह मेरी फाइलें बदलता है?

चुने गए मोड पर निर्भर करता है। पूरे pipeline (`squad_optimization_pipeline`) में, executor अलग `optimized/` डायरेक्टरी में अनुकूलित संस्करण बनाता है — आपकी मूल फाइलें कभी ओवरराइट नहीं होतीं। `squad_audit_only` मोड में, यह 100% read-only है: केवल निदान और रिपोर्ट, शून्य परिवर्तन।

### कितनी बचत होती है?

पाए गए anti-patterns के आधार पर 65% से 98% टोकन कमी। सबसे सामान्य मामला — Model Overkill और Context Bloat वाले squads — आमतौर पर प्रति निष्पादन लागत में 78% की कमी दिखाता है। QualityAuditor की अंतिम रिपोर्ट टोकन, लागत, और विलंबता के लिए विस्तृत पहले/बाद अनुमान दिखाती है।

</details>

---

<div align="center">

**[NSCL Pipeline](https://github.com/nscl-pipeline) द्वारा निर्मित** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>


## Referência: references/squad/README.md

<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**Analisa squads AIOS existentes e produz otimizacoes priorizadas por ROI — qualidade, velocidade e economia de tokens.**

Pipeline sequencial de 5 agentes que escaneia, detecta anti-patterns, planeja, executa e audita otimizacoes usando TOKEN-OPTIMIZATION-GUIDE.md como base de conhecimento.

`/sqopt`

</div>

---

## Seu squad consome 10x mais tokens do que deveria?

Voce construiu um squad funcional. Ele roda, entrega resultados, resolve o problema. Mas toda execucao custa **$0.28** e voce sabe que metade desses tokens esta sendo desperdicada em prompts redundantes, retornos verbosos que ninguem le, e Opus fazendo trabalho de Haiku.

O pior? Voce nao sabe **onde** estao os gargalos. Sao dezenas de arquivos, multiplos agentes, workflows encadeados — e cada um esconde anti-patterns invisiveis a olho nu. Context Bloat, Double-Read, Ghost Tokens, Model Overkill. O custo se acumula silenciosamente, execucao apos execucao.

E se eu te dissesse que **12 tecnicas comprovadas** podem reduzir seu custo em ate 78%, aumentar a qualidade dos outputs em 34%, e que tudo isso pode ser aplicado de forma automatica — sem quebrar nada?

---

## O Antes e o Depois

| | Sem Otimizacao | Com token-optimizer |
|---|---|---|
| **Tokens Opus** | 100% | 2-5% (Router Puro) |
| **Custo por execucao** | $0.28 | $0.06 (-78%) |
| **Qualidade output** | 6.5/10 | 8.7/10 (+34%) |
| **Anti-patterns detectados** | 0 | 100% catalogados |

---

## Como Funciona

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

O pipeline completo percorre 5 fases sequenciais. Cada agente le o output do anterior via arquivo (Files as Contracts), retorna apenas `"Done: {path}"` ao orquestrador, e o proximo agente continua de onde o anterior parou. Zero tokens desperdicados em transicoes.

---

## Por que token-optimizer?

- **12 tecnicas comprovadas** — Nao e achismo. Cada otimizacao e mapeada a uma secao numerada do TOKEN-OPTIMIZATION-GUIDE.md, com fundamentacao tecnica e metricas de impacto documentadas.

- **Priorizacao por ROI** — Qualidade primeiro, velocidade segundo, custo terceiro. O planner ordena as acoes pelo maior retorno real, nao pela reducao mais facil. Voce melhora o output antes de cortar custos.

- **Deteccao automatica de 10+ anti-patterns** — Context Bloat, Double-Read, Model Overkill, Compression Rebound, Ghost Tokens, Sequential Launch, Fat Orchestrator — cada um com scoring de severidade 1-10 e estimativa de tokens desperdicados.

- **Modo audit-only** — Quer apenas um diagnostico sem modificar nenhum arquivo? O workflow `squad_audit_only` escaneia, detecta e reporta — zero alteracoes, visibilidade total.

---

## Agentes

| | Nome | Arquetipo | Papel |
|---|---|---|---|
| | **SquadScanner** | Guardian | Le e cataloga a estrutura completa de um squad alvo, produzindo um inventario estruturado |
| | **AntiPatternDetector** | Guardian | Identifica anti-patterns de tokens, scores de severidade e impacto estimado |
| | **OptimizationPlanner** | Balancer | Cria plano de otimizacao priorizado por ROI, mapeando anti-patterns a tecnicas comprovadas |
| | **OptimizationExecutor** | Builder | Executa o plano, reescrevendo versoes otimizadas dos arquivos do squad |
| | **QualityAuditor** | Guardian | Valida o squad otimizado, compara metricas antes/depois e garante compliance AIOS |

---

## Tasks

| Task | Agente Responsavel | Camada Atomica |
|---|---|---|
| `scanSquad()` | SquadScanner | Escaneia squad alvo e produz squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | Cruza inventario com lista de anti-patterns do guia |
| `planOptimization()` | OptimizationPlanner | Gera plano priorizado por ROI com acoes atomicas |
| `executeOptimization()` | OptimizationExecutor | Aplica otimizacoes e gera arquivos em optimized/ |
| `auditQuality()` | QualityAuditor | Valida compliance AIOS e produz relatorio before/after |

---

## Workflows

| Nome | Padrao | Descricao |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | Pipeline completo: scan, detect, plan, execute, audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | Auditoria rapida: scan, detect, audit — sem modificar arquivos |

---

## Comandos

| Comando | O que faz |
|---|---|
| `/sqopt` | Inicia o pipeline interativo com coleta de configuracao |
| `/sqopt:run` | Execucao direta sem perguntas |
| `*sqopt-scan` | Escaneia squad alvo e produz inventario JSON |
| `*sqopt-detect` | Detecta anti-patterns e produz relatorio de severidade |
| `*sqopt-plan` | Gera plano de otimizacao priorizado por ROI |
| `*sqopt-execute` | Aplica otimizacoes planejadas nos arquivos do squad |
| `*sqopt-audit` | Audita squad otimizado e gera relatorio de metricas |

---

## Tech Stack

| Tecnologia | Uso |
|---|---|
| **Claude Code Agent Teams** | Orquestracao multi-agente com roteamento Haiku/Sonnet/Opus |
| **AIOS 2.1+** | Framework de squads — formato padrao de agents, tasks, workflows |
| **Markdown/YAML** | Definicao de agentes, tarefas, workflows e configuracoes |
| **JSON** | Files as Contracts — comunicacao inter-agente via arquivos estruturados |

---

<details>
<summary><strong>FAQ</strong></summary>

### Funciona com qualquer squad?

Sim. O token-optimizer analisa qualquer squad no formato AIOS padrao. Basta apontar o caminho do diretorio e o scanner cataloga automaticamente todos os agents, tasks, workflows e configs. Nao importa o dominio — se segue o formato AIOS, pode ser otimizado.

### Modifica meus arquivos?

Depende do modo escolhido. No pipeline completo (`squad_optimization_pipeline`), o executor gera versoes otimizadas em um diretorio separado `optimized/` — seus originais nunca sao sobrescritos. No modo `squad_audit_only`, e 100% read-only: apenas diagnostico e relatorio, zero alteracoes.

### Quanto economiza?

Entre 65% e 98% de reducao de tokens, dependendo dos anti-patterns encontrados. O caso mais comum — squads com Model Overkill e Context Bloat — costuma ter reducao de 78% no custo por execucao. O relatorio final do QualityAuditor mostra projecoes detalhadas de tokens, custo e latencia antes/depois.

</details>

---

<div align="center">

**Criado por [Renato Medeiros](https://github.com/Renat0z)** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>


## Referência: references/squad/README.zh.md

<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**分析现有 AIOS squads，按 ROI 优先级生成优化方案 — 质量、速度和 token 节省。**

5 个代理的顺序 pipeline，使用 TOKEN-OPTIMIZATION-GUIDE.md 作为知识库进行扫描、检测 anti-patterns、规划、执行和审计优化。

`/sqopt`

</div>

---

## 你的 squad 消耗的 token 是实际需要的 10 倍吗？

你构建了一个能用的 squad。它运行、交付结果、解决问题。但每次执行花费 **$0.28**，你知道其中一半的 token 浪费在了冗余的 prompts、没人读的冗长返回值，以及 Opus 做着 Haiku 的工作上。

最糟糕的是什么？你不知道瓶颈**在哪里**。几十个文件、多个代理、串联的 workflows — 每一个都隐藏着肉眼看不见的 anti-patterns。Context Bloat、Double-Read、Ghost Tokens、Model Overkill。成本在一次又一次的执行中悄然累积。

如果我告诉你，**12 种经过验证的技术**可以将你的成本降低高达 78%，将输出质量提升 34%，而且这一切都可以自动应用 — 不会破坏任何东西呢？

---

## 优化前后对比

| | 未优化 | 使用 token-optimizer |
|---|---|---|
| **Opus Token** | 100% | 2-5% (Router Puro) |
| **每次执行成本** | $0.28 | $0.06 (-78%) |
| **输出质量** | 6.5/10 | 8.7/10 (+34%) |
| **检测到的 Anti-patterns** | 0 | 100% 已编目 |

---

## 工作原理

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

完整 pipeline 经过 5 个顺序阶段。每个代理通过文件读取前一个代理的输出（Files as Contracts），仅向编排器返回 `"Done: {path}"`，下一个代理从上一个停止的地方继续。转换过程中零 token 浪费。

---

## 为什么选择 token-optimizer？

- **12 种经过验证的技术** — 不是猜测。每项优化都映射到 TOKEN-OPTIMIZATION-GUIDE.md 中的编号章节，具有技术依据和记录的影响指标。

- **ROI 优先排序** — 质量第一，速度第二，成本第三。规划器按最高实际回报排列操作，而不是最容易的削减。先改善输出，再降低成本。

- **自动检测 10+ anti-patterns** — Context Bloat、Double-Read、Model Overkill、Compression Rebound、Ghost Tokens、Sequential Launch、Fat Orchestrator — 每个都有 1-10 的严重性评分和估计的浪费 token 数。

- **Audit-only 模式** — 只想要诊断而不修改任何文件？`squad_audit_only` workflow 扫描、检测并报告 — 零更改，完全可见。

---

## 代理

| | 名称 | Archetype | 角色 |
|---|---|---|---|
| | **SquadScanner** | Guardian | 读取并编目目标 squad 的完整结构，生成结构化清单 |
| | **AntiPatternDetector** | Guardian | 识别 token anti-patterns，附带严重性评分和估计影响 |
| | **OptimizationPlanner** | Balancer | 创建按 ROI 优先的优化计划，将 anti-patterns 映射到经过验证的技术 |
| | **OptimizationExecutor** | Builder | 执行计划，重写 squad 文件的优化版本 |
| | **QualityAuditor** | Guardian | 验证优化后的 squad，比较前后指标，确保 AIOS compliance |

---

## 任务

| Task | 负责代理 | Atomic Layer |
|---|---|---|
| `scanSquad()` | SquadScanner | 扫描目标 squad 并生成 squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | 将清单与指南的 anti-pattern 列表交叉引用 |
| `planOptimization()` | OptimizationPlanner | 生成按 ROI 优先的计划，包含原子操作 |
| `executeOptimization()` | OptimizationExecutor | 应用优化并将文件输出到 optimized/ |
| `auditQuality()` | QualityAuditor | 验证 AIOS compliance 并生成 before/after 报告 |

---

## Workflows

| 名称 | 模式 | 描述 |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | 完整 pipeline：scan、detect、plan、execute、audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | 快速审计：scan、detect、audit — 不修改文件 |

---

## 命令

| 命令 | 功能 |
|---|---|
| `/sqopt` | 启动带配置收集的交互式 pipeline |
| `/sqopt:run` | 无提问直接执行 |
| `*sqopt-scan` | 扫描目标 squad 并生成 JSON 清单 |
| `*sqopt-detect` | 检测 anti-patterns 并生成严重性报告 |
| `*sqopt-plan` | 生成按 ROI 优先的优化计划 |
| `*sqopt-execute` | 对 squad 文件应用已规划的优化 |
| `*sqopt-audit` | 审计优化后的 squad 并生成指标报告 |

---

## 技术栈

| 技术 | 用途 |
|---|---|
| **Claude Code Agent Teams** | 多代理编排，支持 Haiku/Sonnet/Opus 路由 |
| **AIOS 2.1+** | Squad 框架 — agents、tasks、workflows 的标准格式 |
| **Markdown/YAML** | 代理、任务、workflow 和配置定义 |
| **JSON** | Files as Contracts — 通过结构化文件进行代理间通信 |

---

<details>
<summary><strong>常见问题</strong></summary>

### 适用于任何 squad 吗？

是的。token-optimizer 分析任何标准 AIOS 格式的 squad。只需指向目录路径，扫描器就会自动编目所有 agents、tasks、workflows 和 configs。领域无关 — 只要遵循 AIOS 格式，就可以优化。

### 会修改我的文件吗？

取决于选择的模式。在完整 pipeline（`squad_optimization_pipeline`）中，执行器在单独的 `optimized/` 目录中生成优化版本 — 你的原始文件永远不会被覆盖。在 `squad_audit_only` 模式下，100% 只读：仅诊断和报告，零更改。

### 能节省多少？

根据发现的 anti-patterns，token 减少 65% 到 98%。最常见的情况 — 存在 Model Overkill 和 Context Bloat 的 squads — 通常每次执行成本降低 78%。QualityAuditor 的最终报告展示 token、成本和延迟的详细前后对比预测。

</details>

---

<div align="center">

**由 [NSCL Pipeline](https://github.com/nscl-pipeline) 创建** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>


## Referência: references/squad/agents/anti-pattern-detector.md

---
agent:
  name: "AntiPatternDetector"
  id: "anti-pattern-detector"
  title: "Detector de Anti-Patterns de Tokens"
  icon: "🚨"
  whenToUse: "Quando precisar identificar anti-patterns de consumo de tokens em um squad existente"
persona_profile:
  archetype: "Guardian"
  communication:
    tone: "analytical"
persona:
  role: "Identifica todos os anti-patterns de tokens presentes no squad, scores de severidade e impacto estimado."
  core_principles:
    - "Deteccao sistematica — checar cada anti-pattern do guia contra o inventario"
    - "Severidade quantificada — score 1-10 com estimativa de tokens desperdicados"
    - "Zero falsos positivos — so reportar com evidencia concreta"
  responsibility_boundaries:
    - "Handles: analise de anti-patterns, scoring de severidade, estimativa de impacto"
    - "Delegates: planejamento de correcao para OptimizationPlanner"
commands:
  - name: "*sqopt-detect"
    visibility: squad
    description: "Detecta anti-patterns de tokens no squad inventariado"
dependencies:
  tasks: ["detect-anti-patterns.md"]
  scripts: []
  templates: []
  checklists: []
  data: ["TOKEN-OPTIMIZATION-GUIDE.md"]
  tools: []
greeting_levels:
  brief: "Agent ready."
  standard: "Agent ready to help."
  detailed: "Agent ready with full context."
---

# Quick Commands
| Command | Description |
|---------|-------------|
| `*sqopt-detect` | Detecta anti-patterns e produz relatorio de severidade |

# Collaboration
- **Receives:** squad-inventory.json do SquadScanner
- **Produces:** anti-patterns-report.json com findings e scores
- **Consumed by:** OptimizationPlanner, QualityAuditor

# Usage Guide

## O que faz
Cruza o inventario do squad com a lista completa de anti-patterns do TOKEN-OPTIMIZATION-GUIDE.md. Para cada anti-pattern encontrado, registra: localizacao (arquivo + linha), severidade (1-10), tokens estimados desperdicados, e tecnica de correcao recomendada.

## Referencia tecnica
- **Secao 13** do TOKEN-OPTIMIZATION-GUIDE.md — Anti-Patterns e Diagnostico (lista completa)
- **Secao 9** — Paradoxo da Compressao Rebote (para evitar falso positivo em compressao)
- **Secao 2** — Os 7 Axiomas (cada violacao e um anti-pattern)

## Anti-patterns checados
1. **Context Bloat** — system prompts com instrucoes redundantes
2. **Double-Read** — multiplos agentes lendo o mesmo arquivo
3. **Model Overkill** — Opus fazendo trabalho de Haiku
4. **Compression Rebound** — compressao excessiva que causa re-expansao
5. **Ghost Tokens** — retornos verbosos ao orquestrador nunca consumidos
6. **Sequential Launch** — agentes independentes lancados em serie
7. **Fat Orchestrator** — orquestrador que gera/julga alem de rotear


## Referência: references/squad/agents/optimization-executor.md

---
agent:
  name: "OptimizationExecutor"
  id: "optimization-executor"
  title: "Executor de Otimizacoes de Squad"
  icon: "⚡"
  whenToUse: "Quando precisar aplicar as otimizacoes planejadas, reescrevendo agents, tasks, workflows e configs do squad"
persona_profile:
  archetype: "Builder"
  communication:
    tone: "pragmatic"
persona:
  role: "Executa o plano de otimizacao, reescrevendo/criando versoes otimizadas dos arquivos do squad."
  core_principles:
    - "Fidelidade ao plano — executar cada acao conforme especificado"
    - "Preservar semantica — otimizar sem alterar funcionalidade"
    - "Arquivos otimizados em diretorio separado — nunca sobrescrever originais"
  responsibility_boundaries:
    - "Handles: reescrita de agents, tasks, workflows, configs com otimizacoes aplicadas"
    - "Delegates: validacao dos resultados para QualityAuditor"
commands:
  - name: "*sqopt-execute"
    visibility: squad
    description: "Aplica otimizacoes planejadas nos arquivos do squad"
dependencies:
  tasks: ["execute-optimization.md"]
  scripts: []
  templates: []
  checklists: []
  data: ["TOKEN-OPTIMIZATION-GUIDE.md"]
  tools: []
greeting_levels:
  brief: "Agent ready."
  standard: "Agent ready to help."
  detailed: "Agent ready with full context."
---

# Quick Commands
| Command | Description |
|---------|-------------|
| `*sqopt-execute` | Executa o plano de otimizacao nos arquivos do squad |

# Collaboration
- **Receives:** optimization-plan.json do OptimizationPlanner + arquivos originais do squad
- **Produces:** arquivos otimizados em diretorio optimized/ + changelog.json
- **Consumed by:** QualityAuditor

# Usage Guide

## O que faz
Executa cada acao do plano de otimizacao, produzindo versoes otimizadas dos arquivos do squad. Aplica: router puro, files as contracts, roteamento assimetrico de modelos, prompts comprimidos, retornos minimos, canary gates, competition patterns, token recycling.

## Referencia tecnica
- **Secao 4** do TOKEN-OPTIMIZATION-GUIDE.md — Orchestrador como Router Puro
- **Secao 5** — Files as Contracts
- **Secao 6** — Roteamento Assimetrico de Modelos
- **Secao 7** — 7 Tecnicas de Reducao de Tokens
- **Secao 10** — Qualidade Superior com Menos Tokens

## Tecnicas aplicadas
1. **Router Puro** — reescrever orquestrador para despachar sem gerar/julgar
2. **Files as Contracts** — substituir retornos por gravacao em arquivo
3. **Model Routing** — anotar cada agente com modelo ideal (Haiku/Sonnet/Opus)
4. **Compressao Cirurgica** — reduzir system prompts ao threshold seguro
5. **Retornos Minimos** — agentes retornam "Done: {path}" em vez de conteudo
6. **Competition Pattern** — adicionar geradores concorrentes onde aplicavel


## Referência: references/squad/agents/optimization-planner.md

---
agent:
  name: "OptimizationPlanner"
  id: "optimization-planner"
  title: "Planejador de Otimizacao por ROI"
  icon: "📐"
  whenToUse: "Quando precisar criar um plano priorizado de otimizacao mapeando anti-patterns a tecnicas especificas"
persona_profile:
  archetype: "Balancer"
  communication:
    tone: "strategic"
persona:
  role: "Cria plano de otimizacao priorizado por ROI, mapeando cada anti-pattern a tecnicas comprovadas do guia."
  core_principles:
    - "ROI primeiro — qualidade > latencia > custo"
    - "Cada acao mapeada a uma tecnica numerada do guia"
    - "Plano executavel — zero ambiguidade, instrucoes atomicas"
  responsibility_boundaries:
    - "Handles: priorizacao por ROI, mapeamento anti-pattern→tecnica, estimativa de impacto"
    - "Delegates: execucao das otimizacoes para OptimizationExecutor"
commands:
  - name: "*sqopt-plan"
    visibility: squad
    description: "Cria plano de otimizacao priorizado por ROI"
dependencies:
  tasks: ["plan-optimization.md"]
  scripts: []
  templates: []
  checklists: []
  data: ["TOKEN-OPTIMIZATION-GUIDE.md"]
  tools: []
greeting_levels:
  brief: "Agent ready."
  standard: "Agent ready to help."
  detailed: "Agent ready with full context."
---

# Quick Commands
| Command | Description |
|---------|-------------|
| `*sqopt-plan` | Gera plano de otimizacao priorizado por ROI |

# Collaboration
- **Receives:** anti-patterns-report.json do AntiPatternDetector
- **Produces:** optimization-plan.json com acoes priorizadas
- **Consumed by:** OptimizationExecutor, QualityAuditor

# Usage Guide

## O que faz
Recebe o relatorio de anti-patterns e cria um plano priorizado por ROI. Prioridade: (1) qualidade dos outputs, (2) velocidade de resposta, (3) economia de tokens. Cada acao do plano referencia a secao exata do guia e inclui instrucoes atomicas para o executor.

## Referencia tecnica
- **Secao 10** do TOKEN-OPTIMIZATION-GUIDE.md — Qualidade Superior com Menos Tokens (prioridade 1)
- **Secao 7** — 7 Tecnicas de Reducao de Tokens (tecnicas aplicaveis)
- **Secao 8** — 5 Tecnicas de Reducao de Latencia (prioridade 2)
- **Secao 6** — Roteamento Assimetrico de Modelos (custo vs qualidade)
- **Apendice B** — Modelo Economico e ROI (para calcular impacto)

## Priorizacao
1. **Qualidade** — competicao entre agentes, token recycling, pressao escalante, validacao inline
2. **Velocidade** — paralelismo, waves de dependencia, eliminacao de round-trips
3. **Custo** — router puro, roteamento assimetrico, context-pack, retornos minimos, canary gate


## Referência: references/squad/agents/quality-auditor.md

---
agent:
  name: "QualityAuditor"
  id: "quality-auditor"
  title: "Auditor de Qualidade de Otimizacao"
  icon: "✅"
  whenToUse: "Quando precisar validar o squad otimizado, comparar metricas antes/depois e garantir compliance AIOS"
persona_profile:
  archetype: "Guardian"
  communication:
    tone: "analytical"
persona:
  role: "Valida o squad otimizado, compara metricas antes/depois e produz relatorio final de otimizacao."
  core_principles:
    - "Validacao AIOS completa — estrutura, cross-references, naming conventions"
    - "Metricas concretas — projecao de tokens, custo e latencia antes/depois"
    - "Deteccao de regressao — otimizacao nao pode quebrar funcionalidade"
  responsibility_boundaries:
    - "Handles: validacao AIOS, comparacao de metricas, relatorio de otimizacao"
    - "Delegates: correcoes necessarias de volta ao OptimizationExecutor"
commands:
  - name: "*sqopt-audit"
    visibility: squad
    description: "Audita o squad otimizado e produz relatorio final"
dependencies:
  tasks: ["audit-quality.md"]
  scripts: []
  templates: []
  checklists: []
  data: ["TOKEN-OPTIMIZATION-GUIDE.md"]
  tools: []
greeting_levels:
  brief: "Agent ready."
  standard: "Agent ready to help."
  detailed: "Agent ready with full context."
---

# Quick Commands
| Command | Description |
|---------|-------------|
| `*sqopt-audit` | Audita squad otimizado e gera relatorio de metricas |

# Collaboration
- **Receives:** arquivos otimizados + changelog.json do OptimizationExecutor, squad-inventory.json original
- **Produces:** optimization-report.md com metricas before/after e compliance status
- **Consumed by:** usuario final

# Usage Guide

## O que faz
Executa validacao completa do squad otimizado: compliance AIOS (7 categorias), cross-references integros, naming conventions corretas. Compara metricas projetadas: tokens estimados antes/depois por agente, custo projetado, latencia estimada, quality score.

## Referencia tecnica
- **Secao 11** do TOKEN-OPTIMIZATION-GUIDE.md — Framework de Elasticidade Token-Qualidade
- **Apendice B** — Modelo Economico e ROI (para calcular savings)
- **Apendice C** — Checklist de Auditoria (validacao completa)

## Metricas do relatorio
1. **Tokens** — estimativa antes/depois por agente e total (% reducao)
2. **Custo** — projecao USD antes/depois usando formulas do Apendice A
3. **Latencia** — estimativa de reducao baseada em paralelismo e waves
4. **Qualidade** — score baseado em patterns de competicao/recycling aplicados
5. **Compliance** — status AIOS das 7 categorias de validacao


## Referência: references/squad/agents/squad-scanner.md

---
agent:
  name: "SquadScanner"
  id: "squad-scanner"
  title: "Analista de Estrutura de Squads"
  icon: "🔍"
  whenToUse: "Quando precisar catalogar a estrutura completa de um squad AIOS existente (agents, tasks, workflows, config, squad.yaml)"
persona_profile:
  archetype: "Guardian"
  communication:
    tone: "analytical"
persona:
  role: "Le e cataloga a estrutura completa de um squad alvo, produzindo um inventario estruturado."
  core_principles:
    - "Inventario exaustivo — nenhum arquivo ignorado"
    - "Extracao precisa de metadados YAML frontmatter"
    - "Output minimo e estruturado — zero narrativa"
  responsibility_boundaries:
    - "Handles: leitura de arquivos, parsing YAML, catalogacao de estrutura"
    - "Delegates: deteccao de anti-patterns para AntiPatternDetector"
commands:
  - name: "*sqopt-scan"
    visibility: squad
    description: "Escaneia um squad alvo e produz inventario estruturado"
dependencies:
  tasks: ["scan-squad.md"]
  scripts: []
  templates: []
  checklists: []
  data: ["TOKEN-OPTIMIZATION-GUIDE.md"]
  tools: []
greeting_levels:
  brief: "Agent ready."
  standard: "Agent ready to help."
  detailed: "Agent ready with full context."
---

# Quick Commands
| Command | Description |
|---------|-------------|
| `*sqopt-scan` | Escaneia squad alvo e produz inventario JSON |

# Collaboration
- **Receives:** caminho do squad alvo (squadPath)
- **Produces:** inventario estruturado (squad-inventory.json)
- **Consumed by:** AntiPatternDetector, QualityAuditor

# Usage Guide

## O que faz
Le todos os arquivos de um squad AIOS e produz um inventario estruturado contendo: lista de agentes (id, archetype, model routing, token estimates), lista de tasks (atomic_layer, contratos Entrada/Saida), workflows (pattern, agent_sequence), e config.

## Referencia tecnica
- **Secao 3** do TOKEN-OPTIMIZATION-GUIDE.md — Anatomia do Fluxo de Tokens (para estimar distribuicao)
- **Secao 12** — Grafo de Dependencia de Campos (para mapear dependencias inter-task)

## Regras criticas
1. Ler cada arquivo UMA UNICA VEZ — gravar resultado no inventario (Axioma 4: Ler 1x, Usar N)
2. Retorno minimo ao orquestrador: apenas "Done: squad-inventory.json salvo em {path}"
3. Inventario deve incluir contagem de tokens estimada por agente (system prompt size + context size)


## Referência: references/squad/config/coding-standards.md

# Coding Standards — token-optimizer

## Convencoes de nomenclatura
- Agent IDs: kebab-case (`squad-scanner`, `anti-pattern-detector`)
- Agent names: PascalCase (`SquadScanner`, `AntiPatternDetector`)
- Task identifiers: camelCase() (`scanSquad()`, `detectAntiPatterns()`)
- Workflow names: snake_case (`squad_optimization_pipeline`)
- Campos Entrada/Saida: camelCase (`squadPath`, `antiPatternsReport`)
- Comandos: `*sqopt-{action}` com prefixo do squad

## Arquivos de saida intermediarios
- Formato: JSON para dados estruturados, Markdown para relatorios
- Naming: kebab-case (`squad-inventory.json`, `anti-patterns-report.json`)
- Local: diretorio de trabalho temporario (`.sqopt-tmp/`)

## Principios de design
1. **Router Puro** — orquestrador nunca gera, nunca le outputs brutos
2. **Files as Contracts** — comunicacao inter-agente exclusivamente via filesystem
3. **Retornos Minimos** — agentes retornam "Done: {path}" ao orquestrador
4. **Ler 1x, Usar N** — Single Source of Truth, zero re-reads


## Referência: references/squad/config/source-tree.md

# Source Tree — token-optimizer

```
token-optimizer/
├── squad.yaml                    # Manifesto do squad
├── start.md                      # Entry point interativo
├── run.md                        # Execucao direta sem perguntas
├── IDEATION.md                   # Racional de design
├── context-manifest.json         # Manifesto de contexto e tech verification
├── agents/
│   ├── squad-scanner.md          # Cataloga estrutura do squad alvo
│   ├── anti-pattern-detector.md  # Detecta anti-patterns de tokens
│   ├── optimization-planner.md   # Planeja otimizacoes por ROI
│   ├── optimization-executor.md  # Executa reescrita otimizada
│   └── quality-auditor.md        # Valida e produz relatorio final
├── tasks/
│   ├── scan-squad.md             # scanSquad() — inventario estruturado
│   ├── detect-anti-patterns.md   # detectAntiPatterns() — findings + severity
│   ├── plan-optimization.md      # planOptimization() — plano priorizado
│   ├── execute-optimization.md   # executeOptimization() — arquivos otimizados
│   └── audit-quality.md          # auditQuality() — relatorio before/after
├── workflows/
│   ├── optimization-pipeline.yaml  # Pipeline completo (5 fases)
│   └── audit-only.yaml             # Auditoria rapida (3 fases)
└── config/
    ├── coding-standards.md       # Convencoes de nomenclatura e design
    ├── tech-stack.md             # Stack tecnica e modelos
    └── source-tree.md            # Este arquivo
```


## Referência: references/squad/config/tech-stack.md

# Tech Stack — token-optimizer

## Runtime
| Tecnologia | Uso |
|---|---|
| **Claude Code Agent Teams** | Execucao multi-agente com roteamento por complexidade |
| **AIOS Protocol** | Formato padrao de squads (agents/, tasks/, workflows/, squad.yaml) |

## Modelos (Roteamento Assimetrico)
| Modelo | Uso no token-optimizer |
|---|---|
| **Opus** | Orquestrador como router puro (despacho e context-pack) |
| **Sonnet** | OptimizationPlanner e QualityAuditor (raciocinio moderado) |
| **Haiku** | SquadScanner e AntiPatternDetector (tarefas previsíveis) |

## Base de Conhecimento
| Recurso | Descricao |
|---|---|
| **TOKEN-OPTIMIZATION-GUIDE.md** | Guia completo de otimizacao de tokens, custo e latencia |

## Dependencias externas
Nenhuma. Squad puramente baseado em analise de arquivos e raciocinio.


## Referência: references/squad/context-manifest.json

```json
{
  "squad": "token-optimizer",
  "objective": "Squad que analisa a estrutura de qualquer squad existente e cria um projeto completo de otimizacao, com foco primario em aumentar a qualidade superior dos outputs e em segundo plano otimizar velocidade e gasto de tokens.",
  "context": "Analisa squads no formato AIOS usando TOKEN-OPTIMIZATION-GUIDE.md como base de conhecimento. Puramente baseado em analise de arquivos e raciocinio. Claude Code Agent Teams com roteamento Haiku/Sonnet/Opus.",
  "agents": [
    "squad-scanner",
    "anti-pattern-detector",
    "optimization-planner",
    "optimization-executor",
    "quality-auditor"
  ],
  "tasks": [
    "scanSquad()",
    "detectAntiPatterns()",
    "planOptimization()",
    "executeOptimization()",
    "auditQuality()"
  ],
  "workflows": [
    "squad_optimization_pipeline",
    "squad_audit_only"
  ],
  "tech_context": {
    "_verified": true,
    "_verified_at": "2026-03-06T12:00:00Z",
    "_verification_notes": [
      "No external APIs, npm packages, webhooks or services used",
      "Purely file-based analysis using TOKEN-OPTIMIZATION-GUIDE.md as knowledge base",
      "All operations are filesystem reads and agent reasoning"
    ],
    "external_apis": [],
    "npm_packages": [],
    "webhooks": [],
    "services": []
  },
  "decomposition": {
    "total_agents": 5,
    "total_tasks": 5,
    "total_workflows": 2,
    "complexity": "high",
    "pattern": "Sequential Pipeline with audit-only shortcut"
  }
}
```


## Referência: references/squad/run.md

---
task: run()
responsavel: "Orchestrator"
responsavel_type: Agente
atomic_layer: Orchestration
Entrada:
  - nome: command
    tipo: string
    descricao: "Comando a executar"
    obrigatorio: true
  - nome: args
    tipo: string[]
    descricao: "Argumentos posicionais"
    obrigatorio: true
  - nome: flags
    tipo: string[]
    descricao: "Flags opcionais"
    obrigatorio: false
Saida:
  - nome: pipelineExecution
    tipo: void
    descricao: "-> execucao direta sem perguntas"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] Comando valido fornecido"
    - "[ ] Argumentos obrigatorios presentes"
  post-conditions:
    - "[ ] Pipeline executado"
    - "[ ] Resultado entregue ao usuario"
---

# run()

/sqopt:run <command> <args> [flags]

Direct execution. Zero questions.

## Sintaxe

/sqopt:run <command> <squadPath> [--priority <value>]

## Comandos disponiveis

| Comando | Workflow | Descricao | Args obrigatorios |
|---------|----------|-----------|-------------------|
| `optimize` | squad_optimization_pipeline | Pipeline completo de otimizacao | `<squadPath>` |
| `audit` | squad_audit_only | Auditoria rapida sem modificacao | `<squadPath>` |
| `scan` | scan_phase only | Apenas escanear e produzir inventario | `<squadPath>` |
| `plan` | scan + detect + plan | Escanear, detectar e planejar (sem executar) | `<squadPath>` |
| `execute` | full pipeline | Alias de optimize | `<squadPath>` |

## Flags opcionais

| Flag | Valores | Default | Descricao |
|------|---------|---------|-----------|
| `--priority` | quality, speed, cost, balanced | balanced | Prioridade de otimizacao |
| `--output` | caminho | ./optimized/ | Diretorio de saida para arquivos otimizados |
| `--verbose` | - | false | Exibir progresso detalhado |

## Exemplos

```bash
# Otimizacao completa com prioridade em qualidade
/sqopt:run optimize ./meu-squad --priority quality

# Auditoria rapida sem modificar nada
/sqopt:run audit /caminho/absoluto/do/squad

# Apenas escanear a estrutura do squad
/sqopt:run scan ./squad-alvo

# Planejar otimizacoes sem executar
/sqopt:run plan ./squad-alvo --priority cost

# Otimizacao com output customizado
/sqopt:run execute ./squad-alvo --output ./squad-alvo-v2
```

## Validacao de Entrada

| Erro | Mensagem |
|------|----------|
| Comando invalido | "Comando '{cmd}' nao reconhecido. Disponiveis: optimize, audit, scan, plan, execute" |
| squadPath ausente | "Argumento obrigatorio: <squadPath>. Ex: /sqopt:run optimize ./meu-squad" |
| squad.yaml nao encontrado | "squad.yaml nao encontrado em '{path}'. Verifique o caminho." |
| --priority invalido | "Prioridade '{val}' invalida. Valores: quality, speed, cost, balanced" |

## Regras

1. Zero perguntas — tudo vem dos argumentos
2. Falhar rapido — validar antes de executar
3. Output limpo — progresso minimo, resultado claro
4. Idioma do usuario


## Referência: references/squad/squad.yaml

```yaml
name: token-optimizer
version: "1.0.0"
description: "Analisa squads AIOS existentes e produz otimizacoes priorizadas por ROI — qualidade, velocidade e economia de tokens — usando TOKEN-OPTIMIZATION-GUIDE.md como base de conhecimento."
author: "Renato Medeiros <@Renat0z>"
license: MIT
slashPrefix: squad-opt
aios:
  minVersion: "2.1.0"
  type: squad
components:
  agents:
    - squad-scanner.md
    - anti-pattern-detector.md
    - optimization-planner.md
    - optimization-executor.md
    - quality-auditor.md
  tasks:
    - scan-squad.md
    - detect-anti-patterns.md
    - plan-optimization.md
    - execute-optimization.md
    - audit-quality.md
  workflows:
    - optimization-pipeline.yaml
    - audit-only.yaml
  commands:
    - start.md
    - run.md
  checklists: []
  templates: []
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
  - token-optimization
  - squad-analysis
  - anti-pattern-detection
  - cost-reduction
  - quality-improvement
  - aios
```


## Referência: references/squad/start.md

---
task: start()
responsavel: "Orchestrator"
responsavel_type: Agente
atomic_layer: Orchestration
Entrada:
  - nome: userTrigger
    tipo: string
    descricao: "usuario -> /sqopt ou /sqopt <input>"
    obrigatorio: true
Saida:
  - nome: configJson
    tipo: JSON
    descricao: "-> .sqopt-tmp/config.json com todas as escolhas"
    obrigatorio: true
  - nome: pipelineExecution
    tipo: void
    descricao: "-> execucao completa do pipeline principal"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] Skill /sqopt invocada"
  post-conditions:
    - "[ ] config.json salvo"
    - "[ ] Pipeline executado ate o final"
    - "[ ] Resultado entregue ao usuario"
---

# start()

```
[/sqopt] ──▶ [Coleta Interativa] ──▶ [config.json] ──▶ [Pipeline] ──▶ [optimization-report.md]
```

Entry point interativo do token-optimizer. Coleta informacoes sobre o squad alvo, escopo de otimizacao e prioridades, depois executa o pipeline correspondente.

## FASE 0 — Apresentacao

Apresentar ao usuario:

```
╔══════════════════════════════════════════════════╗
║  Squad Optimizer                                  ║
║  Analisa e otimiza squads AIOS para              ║
║  qualidade, velocidade e economia de tokens      ║
╠══════════════════════════════════════════════════╣
║  Pipeline:                                        ║
║  1. Scan — inventario completo do squad           ║
║  2. Detect — anti-patterns de tokens              ║
║  3. Plan — otimizacoes priorizadas por ROI        ║
║  4. Execute — reescrita otimizada                 ║
║  5. Audit — relatorio before/after                ║
╚══════════════════════════════════════════════════╝

Vamos configurar sua sessao.
```

## FASE 1 — Coleta Interativa (via AskUserQuestion)

### Pergunta 1 — Squad alvo (obrigatoria)

AskUserQuestion(
  question: "Qual o caminho do squad que voce quer otimizar? (caminho absoluto ou relativo ao diretorio atual)",
)

→ Salvar como `squadPath`. Validar que o diretorio existe e contem `squad.yaml`.

### Pergunta 2 — Escopo de execucao

AskUserQuestion(
  question: "Qual escopo de execucao?",
  options: ["Otimizacao completa (scan + detect + plan + execute + audit)", "Auditoria apenas (scan + detect + audit, sem modificar arquivos)"]
)

→ Mapear para `scope`: "full" ou "audit-only".

### Pergunta 3 — Prioridade de otimizacao

AskUserQuestion(
  question: "Qual a prioridade principal da otimizacao?",
  options: ["Qualidade dos outputs (competicao, recycling, validacao inline)", "Velocidade de resposta (paralelismo, waves, menos round-trips)", "Economia de tokens (router puro, modelo certo, compressao)", "Balanceado (qualidade > velocidade > custo)"]
)

→ Mapear para `optimizationPriority`: "quality" | "speed" | "cost" | "balanced".

### Pergunta 4 — Contexto adicional (opcional)

AskUserQuestion(
  question: "Ha algum contexto adicional sobre este squad? (ex: pontos de dor especificos, restricoes, areas prioritarias)",
  options: ["Sim, quero adicionar contexto", "Nao, seguir com as configuracoes acima"]
)

→ Se "Sim": AskUserQuestion(question: "Descreva o contexto adicional:")
→ Salvar como `additionalContext` ou null.

## FASE 1.5 — Setup e Confirmacao

1. Criar diretorio `.sqopt-tmp/`
2. Salvar config.json:
```json
{
  "squadPath": "{resposta 1}",
  "scope": "{full|audit-only}",
  "optimizationPriority": "{quality|speed|cost|balanced}",
  "additionalContext": "{resposta 4 ou null}",
  "timestamp": "{ISO timestamp}"
}
```
3. Exibir resumo das escolhas
4. Iniciar execucao imediatamente — SEM pedir confirmacao extra

## FASE 2 — Execucao do Pipeline

- Se `scope` = "full" → executar workflow `squad_optimization_pipeline`
- Se `scope` = "audit-only" → executar workflow `squad_audit_only`

## Regras

1. Apresentacao primeiro
2. Uma pergunta por vez — NUNCA todas de uma vez
3. SEMPRE usar AskUserQuestion com options para multipla escolha
4. squadPath obrigatorio — sem ele nao ha pipeline
5. Zero confirmacao pos-setup — coletou, configurou, executa
6. Respeitar scope — executar apenas o workflow correspondente
7. Idioma do usuario — perguntas no mesmo idioma da interacao
8. Cleanup ao final — remover .sqopt-tmp/


## Referência: references/squad/tasks/audit-quality.md

---
task: auditQuality()
responsavel: "QualityAuditor"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: squadInventory
    tipo: JSON
    descricao: "squad-inventory.json → inventario original do SquadScanner"
    obrigatorio: true
  - nome: antiPatternsReport
    tipo: JSON
    descricao: "anti-patterns-report.json → findings do AntiPatternDetector"
    obrigatorio: true
  - nome: optimizedFiles
    tipo: directory
    descricao: "optimized/ → arquivos otimizados do OptimizationExecutor (opcional no modo audit-only)"
    obrigatorio: false
  - nome: changelog
    tipo: JSON
    descricao: "changelog.json → registro de modificacoes (opcional no modo audit-only)"
    obrigatorio: false
Saida:
  - nome: optimizationReport
    tipo: markdown
    descricao: "→ optimization-report.md entregue ao usuario final"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] squad-inventory.json existe"
    - "[ ] anti-patterns-report.json existe"
  post-conditions:
    - "[ ] optimization-report.md salvo com metricas before/after"
    - "[ ] Compliance AIOS validado (7 categorias)"
    - "[ ] Projecao de savings em tokens, custo e latencia calculada"
---
# auditQuality()
```
[inventory + anti-patterns + optimized/] ──▶ [QualityAuditor] ──▶ [optimization-report.md]
```

Modo completo: valida arquivos otimizados (compliance AIOS, cross-references, naming), compara metricas projetadas antes/depois (tokens, custo, latencia, qualidade), produz relatorio final. Modo audit-only: analisa squad original, lista anti-patterns encontrados e projeta savings potenciais sem executar otimizacoes.


## Referência: references/squad/tasks/detect-anti-patterns.md

---
task: detectAntiPatterns()
responsavel: "AntiPatternDetector"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: squadInventory
    tipo: JSON
    descricao: "squad-inventory.json → inventario produzido por SquadScanner"
    obrigatorio: true
  - nome: guideReference
    tipo: filepath
    descricao: "TOKEN-OPTIMIZATION-GUIDE.md → base de conhecimento de anti-patterns"
    obrigatorio: true
Saida:
  - nome: antiPatternsReport
    tipo: JSON
    descricao: "→ anti-patterns-report.json consumido por OptimizationPlanner e QualityAuditor"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] squad-inventory.json existe e esta completo"
    - "[ ] TOKEN-OPTIMIZATION-GUIDE.md acessivel"
  post-conditions:
    - "[ ] anti-patterns-report.json salvo com todos os findings"
    - "[ ] Cada finding tem severidade (1-10) e tokens desperdicados estimados"
    - "[ ] Nenhum anti-pattern do guia foi ignorado na checagem"
---
# detectAntiPatterns()
```
[squad-inventory.json] ──▶ [AntiPatternDetector] ──▶ [anti-patterns-report.json]
```

Itera sobre a lista completa de anti-patterns da Secao 13 do guia. Para cada anti-pattern, verifica no inventario se ha ocorrencias. Registra: tipo do anti-pattern, arquivo(s) afetado(s), severidade (1-10), tokens estimados desperdicados por execucao, e tecnica de correcao recomendada (referencia numerada do guia). Ordena findings por severidade decrescente.


## Referência: references/squad/tasks/execute-optimization.md

---
task: executeOptimization()
responsavel: "OptimizationExecutor"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: optimizationPlan
    tipo: JSON
    descricao: "optimization-plan.json → plano priorizado do OptimizationPlanner"
    obrigatorio: true
  - nome: squadPath
    tipo: string
    descricao: "config.json → caminho do squad original para leitura"
    obrigatorio: true
Saida:
  - nome: optimizedFiles
    tipo: directory
    descricao: "→ diretorio optimized/ com arquivos otimizados consumidos por QualityAuditor"
    obrigatorio: true
  - nome: changelog
    tipo: JSON
    descricao: "→ changelog.json com diff de cada arquivo modificado"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] optimization-plan.json existe com ao menos 1 acao"
    - "[ ] Arquivos originais do squad acessiveis em squadPath"
  post-conditions:
    - "[ ] Diretorio optimized/ criado com todos os arquivos otimizados"
    - "[ ] changelog.json registra cada modificacao com before/after"
    - "[ ] Arquivos originais NAO foram sobrescritos"
---
# executeOptimization()
```
[optimization-plan.json + squadPath] ──▶ [OptimizationExecutor] ──▶ [optimized/ + changelog.json]
```

Executa cada acao do plano de otimizacao em ordem de wave. Para cada arquivo afetado: le o original, aplica a(s) otimizacao(oes) especificada(s), grava versao otimizada em diretorio optimized/ espelhando a estrutura original. Registra cada modificacao no changelog com: arquivo, tecnica aplicada, diff resumido, tokens estimados antes/depois.


## Referência: references/squad/tasks/plan-optimization.md

---
task: planOptimization()
responsavel: "OptimizationPlanner"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: antiPatternsReport
    tipo: JSON
    descricao: "anti-patterns-report.json → findings do AntiPatternDetector"
    obrigatorio: true
  - nome: optimizationPriority
    tipo: string
    descricao: "config.json → prioridade de otimizacao (quality|speed|cost|balanced)"
    obrigatorio: false
Saida:
  - nome: optimizationPlan
    tipo: JSON
    descricao: "→ optimization-plan.json consumido por OptimizationExecutor e QualityAuditor"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] anti-patterns-report.json existe com ao menos 1 finding"
    - "[ ] TOKEN-OPTIMIZATION-GUIDE.md acessivel para mapeamento de tecnicas"
  post-conditions:
    - "[ ] optimization-plan.json salvo com acoes priorizadas por ROI"
    - "[ ] Cada acao mapeia anti-pattern → tecnica do guia → instrucao atomica"
    - "[ ] Estimativa de impacto total (tokens, custo, latencia, qualidade)"
---
# planOptimization()
```
[anti-patterns-report.json] ──▶ [OptimizationPlanner] ──▶ [optimization-plan.json]
```

Recebe anti-patterns detectados e cria plano de otimizacao ordenado por ROI. Prioridade padrao: qualidade > velocidade > custo. Para cada anti-pattern: identifica tecnica(s) corretiva(s) do guia (secao + numero), calcula ROI (impacto estimado / esforco de implementacao), gera instrucao atomica para o executor. Agrupa acoes em waves de implementacao respeitando dependencias entre otimizacoes.


## Referência: references/squad/tasks/scan-squad.md

---
task: scanSquad()
responsavel: "SquadScanner"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: squadPath
    tipo: string
    descricao: "usuario → caminho absoluto do squad alvo"
    obrigatorio: true
  - nome: scope
    tipo: string
    descricao: "config.json → nivel de escaneamento (full|structure-only)"
    obrigatorio: false
Saida:
  - nome: squadInventory
    tipo: JSON
    descricao: "→ squad-inventory.json consumido por AntiPatternDetector e QualityAuditor"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] squadPath aponta para diretorio valido com squad.yaml"
    - "[ ] Diretorios agents/, tasks/, workflows/ existem"
  post-conditions:
    - "[ ] squad-inventory.json salvo no diretorio de trabalho"
    - "[ ] Todos os arquivos do squad catalogados com metadados"
    - "[ ] Estimativa de tokens por agente calculada"
---
# scanSquad()
```
[squadPath] ──▶ [SquadScanner] ──▶ [squad-inventory.json]
```

Le recursivamente a estrutura do squad alvo. Para cada arquivo: extrai YAML frontmatter, identifica tipo (agent/task/workflow/config), cataloga metadados relevantes. Calcula estimativa de tokens por agente baseada no tamanho do system prompt e context size. Mapeia dependencias inter-task usando contratos Entrada/Saida. Grava inventario completo em squad-inventory.json.


## Referência: references/squad/workflows/audit-only.yaml

```yaml
workflow_name: squad_audit_only
description: "Auditoria rapida: escaneia squad, detecta anti-patterns e produz relatorio sem executar otimizacoes"
agent_sequence:
  - squad-scanner
  - anti-pattern-detector
  - quality-auditor
key_commands:
  - "*sqopt-scan"
  - "*sqopt-detect"
  - "*sqopt-audit"
transitions:
  scan_phase:
    trigger: "squadPath fornecido e squad.yaml encontrado"
    confidence: 0.95
    next_steps:
      - command: "*sqopt-detect"
        description: "Detectar anti-patterns no inventario produzido"
        priority: 1
  detection_phase:
    trigger: "squad-inventory.json completo e anti-patterns identificados"
    confidence: 0.90
    next_steps:
      - command: "*sqopt-audit"
        description: "Auditar e gerar relatorio de findings sem otimizar"
        priority: 1
  audit_phase:
    trigger: "optimization-report.md gerado com findings e savings projetados"
    confidence: 0.95
    next_steps: []
success_indicators:
  - "optimization-report.md gerado com findings e savings projetados"
  - "Anti-patterns catalogados com severidade e ROI estimado"
  - "Relatorio completo sem necessidade de execucao"
```


## Referência: references/squad/workflows/optimization-pipeline.yaml

```yaml
workflow_name: squad_optimization_pipeline
description: "Pipeline completo de otimizacao: escaneia squad, detecta anti-patterns, planeja, executa e audita"
agent_sequence:
  - squad-scanner
  - anti-pattern-detector
  - optimization-planner
  - optimization-executor
  - quality-auditor
key_commands:
  - "*sqopt-scan"
  - "*sqopt-detect"
  - "*sqopt-plan"
  - "*sqopt-execute"
  - "*sqopt-audit"
transitions:
  scan_phase:
    trigger: "squadPath fornecido e squad.yaml encontrado"
    confidence: 0.95
    next_steps:
      - command: "*sqopt-detect"
        description: "Detectar anti-patterns no inventario produzido"
        priority: 1
  detection_phase:
    trigger: "squad-inventory.json completo e anti-patterns identificados"
    confidence: 0.90
    next_steps:
      - command: "*sqopt-plan"
        description: "Criar plano de otimizacao priorizado por ROI"
        priority: 1
  planning_phase:
    trigger: "anti-patterns-report.json completo e plano de otimizacao pronto"
    confidence: 0.90
    next_steps:
      - command: "*sqopt-execute"
        description: "Executar otimizacoes nos arquivos do squad"
        priority: 1
  execution_phase:
    trigger: "optimization-plan.json executado e arquivos otimizados gerados"
    confidence: 0.90
    next_steps:
      - command: "*sqopt-audit"
        description: "Auditar resultado e gerar relatorio final"
        priority: 1
  audit_phase:
    trigger: "optimization-report.md gerado com metricas before/after"
    confidence: 0.95
    next_steps: []
success_indicators:
  - "optimization-report.md gerado com metricas before/after"
  - "Todos os arquivos otimizados sem erros de validacao"
  - "Reducao de tokens mensuravel no relatorio final"
```
