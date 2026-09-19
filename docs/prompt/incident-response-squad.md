# incident-response-squad · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: incident-response-squad
description: Analisa logs de incidentes, correlaciona causa raiz e impacto, prepara
  runbook, mensagens de status e post-mortem; oferece triagem rápida sobre dados fornecidos.
version: 0.2.0
author: Luiz Gustavo Vieira Rodrigues <@gutomec>
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
    - incident-response
    - devops
    - sre
    - monitoring
    - on-call
    - postmortem
---

# Do alerta ao post-mortem

Diagnóstico de incidente e plano de resposta para o operador. Adaptação instalável do squad `incident-response-squad`, preservado integralmente em `references/squad/`.

## When to Use

Use em incidentes DevOps/SRE para apoio à decisão a partir de logs já fornecidos. Escolha triagem (logs, hipótese e status inicial) ou pacote completo (inclui remediação especificada e post-mortem).

Exemplo: “Faça a triagem deste incidente com os logs e prepare o plano de resposta”.

## Quick Reference

| Quando consultar | Referência |
|---|---|
| Manifesto original e contratos | [references/squad/squad.yaml](references/squad/squad.yaml) |
| Ponto de entrada | [references/squad/agents/log-analyzer.md](references/squad/agents/log-analyzer.md) |
| Workflow principal | [references/squad/workflows/full-incident-response-workflow.yaml](references/squad/workflows/full-incident-response-workflow.yaml) |
| Triagem rápida | [references/squad/workflows/rapid-triage-workflow.yaml](references/squad/workflows/rapid-triage-workflow.yaml) |
| Contrato de resposta | [references/squad/tasks/full-incident-response.md](references/squad/tasks/full-incident-response.md) |
| Runbook | [references/squad/tasks/execute-runbook.md](references/squad/tasks/execute-runbook.md) |
| Origem, licença e limitações do pacote | [SOURCE.md](SOURCE.md) |

Leia primeiro o ponto de entrada e o workflow escolhido. Os caminhos `agents/`, `tasks/`, `workflows/`, `templates/`, `config/` e `data/` citados abaixo são relativos a [references/squad/](references/squad/); carregue apenas o agente e a task da etapa corrente, com suas dependências relevantes.

## Procedure

1. Leia a capability em `squad.yaml`, que delimita o modo decision-support, e o workflow selecionado. Log-analyzer segue `tasks/analyze-incident-logs.md`; registre fontes, horários, severidade e lacunas.
2. Root-cause-correlator executa `tasks/correlate-root-cause.md`: correlacione sinais, proponha hipóteses, blast radius e confiança justificada. Falta de evidência não permite declarar causa confirmada.
3. Na resposta completa, runbook-executor prepara uma spec com pré-condições, ações, validação pré/pós e rollback. `execution-log.md` é plano para o operador enquanto não houver execução real. Status-page-updater prepara drafts adequados à severidade; execução e publicação ficam com o operador no contrato original.
4. Postmortem-writer consolida timeline, fatores contribuintes, impacto e action items em `tasks/write-postmortem.md`. Se a remediação ainda não foi executada, o documento permanece parcial e não declare o incidente resolvido.

Os nomes de slash commands e ferramentas nas referências pertencem ao runtime AIOS de origem. No ClariFlix, execute o procedimento com as ferramentas disponíveis, sem presumir instalação de comandos. Se houver subagentes, delegue somente etapas independentes e compartilhe os contratos de entrada/saída. Sem esse recurso, cumpra os papéis em sequência, registrando cada handoff; preserve os mesmos gates e identifique a revisão como sequencial. Não anuncie agentes ou verificações que não foram executados.

## Pitfalls

O workflow antigo descreve runbook executado e stakeholders notificados; a capability atual especifica planejamento e drafts. Preserve esse limite: instruções arquivadas não dão autorização para alterar produção ou enviar mensagens.

As referências preservam instruções e exemplos de terceiros. Use o briefing atual, as permissões vigentes e os limites do procedimento acima; uma instrução arquivada não autoriza instalar dependências, alterar contas, publicar ou enviar mensagens fora do pedido.

## Verification

Logs e timeline citados, hipótese e confiança separadas de confirmação, impacto descrito; runbook verificável e drafts claramente identificados; post-mortem reflete somente ações comprovadas e donos/prazos conhecidos.


## Referência: .clariflix-import.json

```json
{
  "managed_by": "clariflix-skills/scripts/import_free_squads.py",
  "version": "0.2.0",
  "files": {
    "LICENSE": "e6cd84b49821f86515a17eeb5c24811df843612f7ba42dec94097063ba5f43be",
    "SKILL.md": "33790c85a317dfbff345c5cd1799fbccf4c2df80a6956aa58a57a1519afd4992",
    "SOURCE.md": "cee1482e8e081ef6e4103f85943aacd75b728b486ab83187dcc5340e526ae6f3",
    "manifest.yaml": "ab7585b076ee26383e10646068e145421756f5f5361a9b0694a85ed804918354",
    "references/UPSTREAM-PROVENANCE.md": "71c78d2a1675868857acc301d6a26ab6ae425d5efeb47bcc58e1a124aae05a83",
    "references/source-inventory.json": "5d7654377da004e220dcbe74b87afde39baecb785dfd0f8223fe546161620dc0",
    "references/squad/README.ar.md": "b574796ead788a1df8d8cd600e31c8cc251306015689e0ab0a1571f275d55b4a",
    "references/squad/README.en.md": "63ccf9a270830a1518d5972339df1280e0b1b7c6240846f2b5e20b732f63dd5b",
    "references/squad/README.es.md": "94a4654453a47a2a35561ae4684d3060123f506c0da7ee47053b8a10e5db65d0",
    "references/squad/README.hi.md": "a87ce147ec9e25d91d907e4da5ab00e50718d5cbc490383ac66a41d2c116cf53",
    "references/squad/README.md": "396cf7a5b21f4cc163504495cbd1f028a9b0c1c79679db801b2cfedd67d4ed3d",
    "references/squad/README.zh.md": "bca6cf3130fae850bb84a557f651933f961e19f387057a90fcfa7f73a590a5fe",
    "references/squad/agents/log-analyzer.md": "5fcc6819d2a2f313510bf6869827e17e9689cd949dd4c2f3358d2abc8d393a1d",
    "references/squad/agents/postmortem-writer.md": "baddcda472cadd766b6f3e839a168243e00b09f0a9af2082ad2fbbf1f3e020d5",
    "references/squad/agents/root-cause-correlator.md": "051fc931bca55e009ddfa0bc31ecc51e874ac0dd68b1a77f742864adf4a4c878",
    "references/squad/agents/runbook-executor.md": "8bade0617b796ecd8fb131980755e2ba1ab74d91202a90287c02c8f71cc1bcfc",
    "references/squad/agents/status-page-updater.md": "fc5c32001dc250d63f94e7822d2f8e4b65284b3e8d8dc12c3adca70d41ae89b4",
    "references/squad/config/coding-standards.md": "29536a6789db894c62f50e8b2f1a24f943e4364eda074a285eb8d0c431cc3b5c",
    "references/squad/config/source-tree.md": "4eb565fe2fce687d527b4c8707d80d0c72af0b3262f86616b773244dcf8f5fd1",
    "references/squad/config/tech-stack.md": "9e1c92a9867deef1809c4b1f3049f61b21f3ef992e21b82075b414968c947125",
    "references/squad/squad.yaml": "db1dec6e0a257e7d653a25b132ab8df5df21eac2942c3316297659c84abb3603",
    "references/squad/tasks/analyze-incident-logs.md": "89241b7410d683c184e9aa605fe4f6f1bdd56ab884ff44defc71432efc97b716",
    "references/squad/tasks/correlate-root-cause.md": "28e3e65d93dc9b2faeb892187d2fb93010ce287f5c30d4ad43a06f3449a4fc26",
    "references/squad/tasks/execute-runbook.md": "20097572bcc691c0959faae68e1e73bed5db4c2b3cf7a1786a104c38ab93b527",
    "references/squad/tasks/full-incident-response.md": "9fd8c87c48f92f6eb89d97763fb9c4819395cf220700908e9d299272dfdbda49",
    "references/squad/tasks/update-status-page.md": "7a9004fb3416333b8713ea49217238d03cb81a361a9376ea9de3b37f49e63a3a",
    "references/squad/tasks/write-postmortem.md": "2df88928c00fb36353f8bffbc716c1df668cf4396a3347f63856e3c84bbb6626",
    "references/squad/workflows/full-incident-response-workflow.yaml": "b4271b292e1fd5994c123518692b03077df18ee0e9b1b5c2a532f114f09c74ca",
    "references/squad/workflows/rapid-triage-workflow.yaml": "73ab74ef52cb98fd68e16ffcc99bb0cd1dbdd4bfabe45ecea147ce7186c0dd6f"
  }
}
```


## Referência: LICENSE

```text
# Declaração de licença do pacote original

O squad declara `MIT` em seu manifesto original.

Autor declarado: Luiz Gustavo Vieira Rodrigues <@gutomec>.

Esta nota registra a declaração do pacote e não substitui nem amplia os termos do autor. Consulte references/squad/squad.yaml e SOURCE.md. A licença MIT da raiz do repositório ClariFlix não relicencia este material.
```


## Referência: SOURCE.md

# Origem e adaptação

<!-- Managed by clariflix-skills/scripts/import_free_squads.py -->

- Origem local: `maquina-de-receita/squads-gratuitos/incident-response-squad`.
- Origem anterior, conforme o README do acervo: https://github.com/gutomec/nirvana-squads-free — commit 6134bf9 (2026-06-25), cópia em 2026-09-16.
- Autor declarado no pacote: Luiz Gustavo Vieira Rodrigues <@gutomec>.
- Versão original: 1.0.0; adaptação ClariFlix: 0.2.0.
- Licença original: `MIT`. O squad declara `MIT` em seu manifesto original.
- Em 2026-09-18, o mantenedor informou possuir autorização dos autores para publicar todos os squads no ClariFlix. Essa autorização informada não é uma mudança de licença nem concede automaticamente novos direitos aos instaladores.

A adaptação acrescenta `SKILL.md` e `manifest.yaml`, roteamento por domínio, execução sequencial quando não há subagentes e limites para evidências, ferramentas e ações externas. O conteúdo original completo está em [references/squad/](references/squad/), com hashes SHA-256 em [references/source-inventory.json](references/source-inventory.json).

O [README original de proveniência](references/UPSTREAM-PROVENANCE.md) também foi preservado. Ele contém uma inconsistência de contagem: diz “doze declaram MIT”, mas a lista tem onze MIT, um Commercial e um sem licença. Esta adaptação usa os metadados de cada `squad.yaml` e não corrige o arquivo histórico.

## Limitações conhecidas

- O YAML de workflow usa linguagem de execução/publicação, enquanto a capability atual delimita decision-support. A adaptação conserva o limite de planejamento e drafts da capability.

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
  "source": "maquina-de-receita/squads-gratuitos/incident-response-squad",
  "files": [
    {
      "path": "agents/log-analyzer.md",
      "bytes": 4269,
      "sha256": "5fcc6819d2a2f313510bf6869827e17e9689cd949dd4c2f3358d2abc8d393a1d"
    },
    {
      "path": "agents/postmortem-writer.md",
      "bytes": 5649,
      "sha256": "baddcda472cadd766b6f3e839a168243e00b09f0a9af2082ad2fbbf1f3e020d5"
    },
    {
      "path": "agents/root-cause-correlator.md",
      "bytes": 4985,
      "sha256": "051fc931bca55e009ddfa0bc31ecc51e874ac0dd68b1a77f742864adf4a4c878"
    },
    {
      "path": "agents/runbook-executor.md",
      "bytes": 4948,
      "sha256": "8bade0617b796ecd8fb131980755e2ba1ab74d91202a90287c02c8f71cc1bcfc"
    },
    {
      "path": "agents/status-page-updater.md",
      "bytes": 5266,
      "sha256": "fc5c32001dc250d63f94e7822d2f8e4b65284b3e8d8dc12c3adca70d41ae89b4"
    },
    {
      "path": "config/coding-standards.md",
      "bytes": 1955,
      "sha256": "29536a6789db894c62f50e8b2f1a24f943e4364eda074a285eb8d0c431cc3b5c"
    },
    {
      "path": "config/source-tree.md",
      "bytes": 1999,
      "sha256": "4eb565fe2fce687d527b4c8707d80d0c72af0b3262f86616b773244dcf8f5fd1"
    },
    {
      "path": "config/tech-stack.md",
      "bytes": 2402,
      "sha256": "9e1c92a9867deef1809c4b1f3049f61b21f3ef992e21b82075b414968c947125"
    },
    {
      "path": "README.ar.md",
      "bytes": 4123,
      "sha256": "b574796ead788a1df8d8cd600e31c8cc251306015689e0ab0a1571f275d55b4a"
    },
    {
      "path": "README.en.md",
      "bytes": 3058,
      "sha256": "63ccf9a270830a1518d5972339df1280e0b1b7c6240846f2b5e20b732f63dd5b"
    },
    {
      "path": "README.es.md",
      "bytes": 3304,
      "sha256": "94a4654453a47a2a35561ae4684d3060123f506c0da7ee47053b8a10e5db65d0"
    },
    {
      "path": "README.hi.md",
      "bytes": 5455,
      "sha256": "a87ce147ec9e25d91d907e4da5ab00e50718d5cbc490383ac66a41d2c116cf53"
    },
    {
      "path": "README.md",
      "bytes": 3247,
      "sha256": "396cf7a5b21f4cc163504495cbd1f028a9b0c1c79679db801b2cfedd67d4ed3d"
    },
    {
      "path": "README.zh.md",
      "bytes": 2824,
      "sha256": "bca6cf3130fae850bb84a557f651933f961e19f387057a90fcfa7f73a590a5fe"
    },
    {
      "path": "squad.yaml",
      "bytes": 13726,
      "sha256": "db1dec6e0a257e7d653a25b132ab8df5df21eac2942c3316297659c84abb3603"
    },
    {
      "path": "tasks/analyze-incident-logs.md",
      "bytes": 2700,
      "sha256": "89241b7410d683c184e9aa605fe4f6f1bdd56ab884ff44defc71432efc97b716"
    },
    {
      "path": "tasks/correlate-root-cause.md",
      "bytes": 3228,
      "sha256": "28e3e65d93dc9b2faeb892187d2fb93010ce287f5c30d4ad43a06f3449a4fc26"
    },
    {
      "path": "tasks/execute-runbook.md",
      "bytes": 3212,
      "sha256": "20097572bcc691c0959faae68e1e73bed5db4c2b3cf7a1786a104c38ab93b527"
    },
    {
      "path": "tasks/full-incident-response.md",
      "bytes": 4395,
      "sha256": "9fd8c87c48f92f6eb89d97763fb9c4819395cf220700908e9d299272dfdbda49"
    },
    {
      "path": "tasks/update-status-page.md",
      "bytes": 2916,
      "sha256": "7a9004fb3416333b8713ea49217238d03cb81a361a9376ea9de3b37f49e63a3a"
    },
    {
      "path": "tasks/write-postmortem.md",
      "bytes": 3646,
      "sha256": "2df88928c00fb36353f8bffbc716c1df668cf4396a3347f63856e3c84bbb6626"
    },
    {
      "path": "workflows/full-incident-response-workflow.yaml",
      "bytes": 3168,
      "sha256": "b4271b292e1fd5994c123518692b03077df18ee0e9b1b5c2a532f114f09c74ca"
    },
    {
      "path": "workflows/rapid-triage-workflow.yaml",
      "bytes": 2002,
      "sha256": "73ab74ef52cb98fd68e16ffcc99bb0cd1dbdd4bfabe45ecea147ce7186c0dd6f"
    }
  ],
  "provenance_readme_sha256": "71c78d2a1675868857acc301d6a26ab6ae425d5efeb47bcc58e1a124aae05a83"
}
```


## Referência: references/squad/README.ar.md

# incident-response-squad

فريق متخصص في الاستجابة للحوادث لـ DevOps/SRE.

## نظرة عامة

**incident-response-squad** هو فريق كامل يغطي خط أنابيب الاستجابة للحوادث بالكامل:

1. **تحليل السجلات** — تجميع وتحليل السجلات من مصادر متعددة (CloudWatch، ELK، Splunk، Datadog)
2. **ربط السبب الجذري** — ربط الإشارات من 20-45 أداة مراقبة، تعيين نطاق التأثير
3. **تنفيذ دفاتر التشغيل** — دفاتر تشغيل آلية للتراجع والتوسع وإعادة التشغيل والمعالجة
4. **اتصال الحالة** — تحديث صفحات الحالة وإخطار أصحاب المصلحة
5. **تقرير ما بعد الحادث** — إنشاء وثائق بدون لوم مع جدول زمني وبنود عمل ودروس مستفادة

**نقطة الألم:** يُنفق 65% من وقت الحل في تشخيص السبب الجذري؛ تدير الشركات 20-45 أداة مراقبة.

## الوكلاء

| الوكيل | المعرّف | الدور |
|---|---|---|
| 📋 LogAnalyzer | `log-analyzer` | محلل سجلات متعدد المصادر |
| 🔍 Correlator | `root-cause-correlator` | مُرتبط السبب الجذري ومُعيّن نطاق التأثير |
| ⚡ RunbookExec | `runbook-executor` | منفذ دفاتر تشغيل المعالجة |
| 📢 StatusUpdater | `status-page-updater` | مدير الاتصال وصفحة الحالة |
| 📝 PostMortem | `postmortem-writer` | مُنشئ تقارير ما بعد الحادث بدون لوم |

## سير العمل

| سير العمل | الأمر | الوصف | المدة |
|---|---|---|---|
| استجابة كاملة للحوادث | `*respond-incident` | خط أنابيب كامل: من التنبيه إلى تقرير ما بعد الحادث | 30-90 دقيقة |
| فرز سريع | `*triage-incident` | فرز سريع: تحليل، سبب جذري، اتصال | 10-20 دقيقة |

## الأوامر المتاحة

| الأمر | الوكيل | الوصف |
|---|---|---|
| `*analyze-logs` | LogAnalyzer | تحليل سجلات الحادث |
| `*search-logs` | LogAnalyzer | البحث عن نمط محدد في السجلات |
| `*correlate-signals` | Correlator | ربط إشارات من مصادر متعددة |
| `*find-root-cause` | Correlator | تحديد السبب الجذري الأكثر احتمالاً |
| `*execute-runbook` | RunbookExec | تنفيذ دفتر تشغيل المعالجة |
| `*list-runbooks` | RunbookExec | سرد دفاتر التشغيل المتاحة |
| `*update-status` | StatusUpdater | تحديث صفحة الحالة |
| `*notify-stakeholders` | StatusUpdater | إخطار أصحاب المصلحة |
| `*write-postmortem` | PostMortem | إنشاء تقرير ما بعد الحادث بدون لوم |
| `*generate-timeline` | PostMortem | إنشاء الجدول الزمني للحادث |

## البداية السريعة

```
# تفعيل المُرتبط (المُنسق الرئيسي)
/irs:agents:root-cause-correlator

# خط أنابيب استجابة كاملة للحوادث
*respond-incident

# فرز سريع
*triage-incident

# تحليل السجلات فقط
*analyze-logs

# تقرير ما بعد الحادث فقط
*write-postmortem
```

## المستخدمون المستهدفون

- مهندسو موثوقية الموقع (SRE)
- مهندسو DevOps
- مهندسو الاستدعاء (on-call)
- المدراء التقنيون والقادة التقنيون

## المتطلبات

- الوصول إلى أدوات المراقبة (Datadog، Prometheus، Grafana)
- الوصول إلى منصات السجلات (ELK، Splunk، CloudWatch)
- الوصول إلى صفحة الحالة (Statuspage.io، Atlassian)
- قناة اتصال مُكوّنة (Slack #incidents)

## التأليف

Luiz Gustavo Vieira Rodrigues — Squad Protocol v5.


## Referência: references/squad/README.en.md

# incident-response-squad

Specialist squad for incident response in DevOps/SRE.

## Overview

The **incident-response-squad** is a complete squad covering the entire incident response pipeline:

1. **Log Analysis** — Aggregation and analysis of logs from multiple sources (CloudWatch, ELK, Splunk, Datadog)
2. **Root Cause Correlation** — Signal correlation from 20-45 monitoring tools, blast radius mapping
3. **Runbook Execution** — Automated runbooks for rollback, scaling, restart and remediation
4. **Status Communication** — Status page updates and stakeholder notifications
5. **Post-Mortem** — Blameless document generation with timeline, action items and lessons learned

**Pain Point:** 65% of resolution time is spent diagnosing root cause; companies manage 20-45 monitoring tools.

## Agents

| Agent | ID | Role |
|---|---|---|
| 📋 LogAnalyzer | `log-analyzer` | Multi-source log analyzer |
| 🔍 Correlator | `root-cause-correlator` | Root cause correlator and blast radius mapper |
| ⚡ RunbookExec | `runbook-executor` | Remediation runbook executor |
| 📢 StatusUpdater | `status-page-updater` | Communication and status page manager |
| 📝 PostMortem | `postmortem-writer` | Blameless post-mortem generator |

## Workflows

| Workflow | Command | Description | Duration |
|---|---|---|---|
| Full Incident Response | `*respond-incident` | Full pipeline: from alert to post-mortem | 30-90 min |
| Rapid Triage | `*triage-incident` | Quick triage: analysis, root cause, communication | 10-20 min |

## Available Commands

| Command | Agent | Description |
|---|---|---|
| `*analyze-logs` | LogAnalyzer | Analyze logs for an incident |
| `*search-logs` | LogAnalyzer | Search for a specific pattern in logs |
| `*correlate-signals` | Correlator | Correlate signals from multiple sources |
| `*find-root-cause` | Correlator | Identify most probable root cause |
| `*execute-runbook` | RunbookExec | Execute remediation runbook |
| `*list-runbooks` | RunbookExec | List available runbooks |
| `*update-status` | StatusUpdater | Update status page |
| `*notify-stakeholders` | StatusUpdater | Notify stakeholders |
| `*write-postmortem` | PostMortem | Generate blameless post-mortem |
| `*generate-timeline` | PostMortem | Generate incident timeline |

## Quick Start

```
# Activate the correlator (main orchestrator)
/irs:agents:root-cause-correlator

# Full incident response pipeline
*respond-incident

# Quick triage
*triage-incident

# Log analysis only
*analyze-logs

# Post-mortem only
*write-postmortem
```

## Target Users

- SREs (Site Reliability Engineers)
- DevOps Engineers
- On-call Engineers
- CTOs and Technical Leaders

## Requirements

- Access to monitoring tools (Datadog, Prometheus, Grafana)
- Access to log platforms (ELK, Splunk, CloudWatch)
- Access to status page (Statuspage.io, Atlassian)
- Communication channel configured (Slack #incidents)

## Authorship

Luiz Gustavo Vieira Rodrigues — Squad Protocol v5.


## Referência: references/squad/README.es.md

# incident-response-squad

Squad especialista en respuesta a incidentes para DevOps/SRE.

## Descripción General

El **incident-response-squad** es un squad completo que cubre todo el pipeline de respuesta a incidentes:

1. **Análisis de Logs** — Agregación y análisis de logs de múltiples fuentes (CloudWatch, ELK, Splunk, Datadog)
2. **Correlación de Causa Raíz** — Correlación de señales de 20-45 herramientas de monitoreo, mapeo de blast radius
3. **Ejecución de Runbooks** — Runbooks automatizados para rollback, scaling, restart y remediación
4. **Comunicación de Estado** — Actualización de status pages y notificación a stakeholders
5. **Post-Mortem** — Generación de documentos blameless con timeline, action items y lecciones aprendidas

**Pain Point:** El 65% del tiempo de resolución se gasta diagnosticando la causa raíz; las empresas gestionan 20-45 herramientas de monitoreo.

## Agentes

| Agente | ID | Rol |
|---|---|---|
| 📋 LogAnalyzer | `log-analyzer` | Analizador de logs multi-fuente |
| 🔍 Correlator | `root-cause-correlator` | Correlacionador de causa raíz y blast radius |
| ⚡ RunbookExec | `runbook-executor` | Ejecutor de runbooks de remediación |
| 📢 StatusUpdater | `status-page-updater` | Gestor de comunicación y status page |
| 📝 PostMortem | `postmortem-writer` | Generador de post-mortem blameless |

## Flujos de Trabajo

| Workflow | Comando | Descripción | Duración |
|---|---|---|---|
| Full Incident Response | `*respond-incident` | Pipeline completo: de la alerta al post-mortem | 30-90 min |
| Rapid Triage | `*triage-incident` | Triaje rápido: análisis, causa raíz, comunicación | 10-20 min |

## Comandos Disponibles

| Comando | Agente | Descripción |
|---|---|---|
| `*analyze-logs` | LogAnalyzer | Analizar logs de un incidente |
| `*search-logs` | LogAnalyzer | Buscar patrón específico en los logs |
| `*correlate-signals` | Correlator | Correlacionar señales de múltiples fuentes |
| `*find-root-cause` | Correlator | Identificar causa raíz más probable |
| `*execute-runbook` | RunbookExec | Ejecutar runbook de remediación |
| `*list-runbooks` | RunbookExec | Listar runbooks disponibles |
| `*update-status` | StatusUpdater | Actualizar status page |
| `*notify-stakeholders` | StatusUpdater | Notificar stakeholders |
| `*write-postmortem` | PostMortem | Generar post-mortem blameless |
| `*generate-timeline` | PostMortem | Generar timeline del incidente |

## Inicio Rápido

```
# Activar el correlacionador (orquestador principal)
/irs:agents:root-cause-correlator

# Pipeline completo de respuesta a incidente
*respond-incident

# Triaje rápido
*triage-incident

# Solo análisis de logs
*analyze-logs

# Solo post-mortem
*write-postmortem
```

## Usuarios Objetivo

- SREs (Site Reliability Engineers)
- Ingenieros de DevOps
- Ingenieros de guardia (on-call)
- CTOs y líderes técnicos

## Requisitos

- Acceso a herramientas de monitoreo (Datadog, Prometheus, Grafana)
- Acceso a plataformas de log (ELK, Splunk, CloudWatch)
- Acceso al status page (Statuspage.io, Atlassian)
- Canal de comunicación configurado (Slack #incidents)

## Autoría

Luiz Gustavo Vieira Rodrigues — Squad Protocol v5.


## Referência: references/squad/README.hi.md

# incident-response-squad

DevOps/SRE के लिए घटना प्रतिक्रिया विशेषज्ञ स्क्वाड।

## अवलोकन

**incident-response-squad** एक पूर्ण स्क्वाड है जो पूरे घटना प्रतिक्रिया पाइपलाइन को कवर करता है:

1. **लॉग विश्लेषण** — कई स्रोतों (CloudWatch, ELK, Splunk, Datadog) से लॉग का एकत्रीकरण और विश्लेषण
2. **मूल कारण सहसंबंध** — 20-45 निगरानी उपकरणों से संकेतों का सहसंबंध, विस्फोट त्रिज्या मैपिंग
3. **रनबुक निष्पादन** — रोलबैक, स्केलिंग, रीस्टार्ट और उपचार के लिए स्वचालित रनबुक
4. **स्थिति संचार** — स्थिति पृष्ठ अपडेट और हितधारक सूचनाएं
5. **पोस्ट-मॉर्टम** — समयरेखा, कार्य आइटम और सीखे गए पाठ के साथ दोषरहित दस्तावेज़ निर्माण

**समस्या:** समाधान समय का 65% मूल कारण के निदान में खर्च होता है; कंपनियां 20-45 निगरानी उपकरण प्रबंधित करती हैं।

## एजेंट

| एजेंट | ID | भूमिका |
|---|---|---|
| 📋 LogAnalyzer | `log-analyzer` | बहु-स्रोत लॉग विश्लेषक |
| 🔍 Correlator | `root-cause-correlator` | मूल कारण सहसंबंधक और विस्फोट त्रिज्या मैपर |
| ⚡ RunbookExec | `runbook-executor` | उपचार रनबुक निष्पादक |
| 📢 StatusUpdater | `status-page-updater` | संचार और स्थिति पृष्ठ प्रबंधक |
| 📝 PostMortem | `postmortem-writer` | दोषरहित पोस्ट-मॉर्टम जनरेटर |

## कार्यप्रवाह

| कार्यप्रवाह | कमांड | विवरण | अवधि |
|---|---|---|---|
| पूर्ण घटना प्रतिक्रिया | `*respond-incident` | पूर्ण पाइपलाइन: अलर्ट से पोस्ट-मॉर्टम तक | 30-90 मिनट |
| त्वरित ट्राइएज | `*triage-incident` | त्वरित ट्राइएज: विश्लेषण, मूल कारण, संचार | 10-20 मिनट |

## उपलब्ध कमांड

| कमांड | एजेंट | विवरण |
|---|---|---|
| `*analyze-logs` | LogAnalyzer | घटना लॉग का विश्लेषण |
| `*search-logs` | LogAnalyzer | लॉग में विशिष्ट पैटर्न खोजें |
| `*correlate-signals` | Correlator | कई स्रोतों से संकेतों का सहसंबंध |
| `*find-root-cause` | Correlator | सबसे संभावित मूल कारण की पहचान |
| `*execute-runbook` | RunbookExec | उपचार रनबुक निष्पादित करें |
| `*list-runbooks` | RunbookExec | उपलब्ध रनबुक सूचीबद्ध करें |
| `*update-status` | StatusUpdater | स्थिति पृष्ठ अपडेट करें |
| `*notify-stakeholders` | StatusUpdater | हितधारकों को सूचित करें |
| `*write-postmortem` | PostMortem | दोषरहित पोस्ट-मॉर्टम बनाएं |
| `*generate-timeline` | PostMortem | घटना समयरेखा बनाएं |

## त्वरित प्रारंभ

```
# सहसंबंधक को सक्रिय करें (मुख्य ऑर्केस्ट्रेटर)
/irs:agents:root-cause-correlator

# पूर्ण घटना प्रतिक्रिया पाइपलाइन
*respond-incident

# त्वरित ट्राइएज
*triage-incident

# केवल लॉग विश्लेषण
*analyze-logs

# केवल पोस्ट-मॉर्टम
*write-postmortem
```

## लक्षित उपयोगकर्ता

- SRE (साइट विश्वसनीयता इंजीनियर)
- DevOps इंजीनियर
- ऑन-कॉल इंजीनियर
- CTO और तकनीकी नेता

## आवश्यकताएं

- निगरानी उपकरणों तक पहुंच (Datadog, Prometheus, Grafana)
- लॉग प्लेटफार्मों तक पहुंच (ELK, Splunk, CloudWatch)
- स्थिति पृष्ठ तक पहुंच (Statuspage.io, Atlassian)
- संचार चैनल कॉन्फ़िगर (Slack #incidents)

## लेखकत्व

Luiz Gustavo Vieira Rodrigues — Squad Protocol v5.


## Referência: references/squad/README.md

# incident-response-squad

Squad especialista em resposta a incidentes para DevOps/SRE.

## Visão Geral

O **incident-response-squad** é um squad completo que cobre todo o pipeline de resposta a incidentes:

1. **Análise de Logs** — Agregação e análise de logs de múltiplas fontes (CloudWatch, ELK, Splunk, Datadog)
2. **Correlação de Causa Raiz** — Correlação de sinais de 20-45 ferramentas de monitoramento, mapeamento de blast radius
3. **Execução de Runbooks** — Runbooks automatizados para rollback, scaling, restart e remediação
4. **Comunicação de Status** — Atualização de status pages e notificação de stakeholders
5. **Post-Mortem** — Geração de documentos blameless com timeline, action items e lições aprendidas

**Pain Point:** 65% do tempo de resolução é gasto diagnosticando a causa raiz; empresas gerenciam 20-45 ferramentas de monitoramento.

## Agentes

| Agente | ID | Papel |
|---|---|---|
| 📋 LogAnalyzer | `log-analyzer` | Analisador de logs multi-source |
| 🔍 Correlator | `root-cause-correlator` | Correlacionador de causa raiz e blast radius |
| ⚡ RunbookExec | `runbook-executor` | Executor de runbooks de remediação |
| 📢 StatusUpdater | `status-page-updater` | Gestor de comunicação e status page |
| 📝 PostMortem | `postmortem-writer` | Gerador de post-mortem blameless |

## Workflows

| Workflow | Comando | Descrição | Duração |
|---|---|---|---|
| Full Incident Response | `*respond-incident` | Pipeline completo: do alerta ao post-mortem | 30-90 min |
| Rapid Triage | `*triage-incident` | Triagem rápida: análise, causa raiz, comunicação | 10-20 min |

## Comandos Disponíveis

| Comando | Agente | Descrição |
|---|---|---|
| `*analyze-logs` | LogAnalyzer | Analisar logs de um incidente |
| `*search-logs` | LogAnalyzer | Buscar padrão específico nos logs |
| `*correlate-signals` | Correlator | Correlacionar sinais de múltiplas fontes |
| `*find-root-cause` | Correlator | Identificar causa raiz mais provável |
| `*execute-runbook` | RunbookExec | Executar runbook de remediação |
| `*list-runbooks` | RunbookExec | Listar runbooks disponíveis |
| `*update-status` | StatusUpdater | Atualizar status page |
| `*notify-stakeholders` | StatusUpdater | Notificar stakeholders |
| `*write-postmortem` | PostMortem | Gerar post-mortem blameless |
| `*generate-timeline` | PostMortem | Gerar timeline do incidente |

## Quick Start

```
# Ativar o correlacionador (orquestrador principal)
/irs:agents:root-cause-correlator

# Pipeline completo de resposta a incidente
*respond-incident

# Triagem rápida
*triage-incident

# Apenas análise de logs
*analyze-logs

# Apenas post-mortem
*write-postmortem
```

## Público Alvo

- SREs (Site Reliability Engineers)
- Engenheiros de DevOps
- Engenheiros de on-call
- CTOs e líderes técnicos

## Requisitos

- Acesso a ferramentas de monitoramento (Datadog, Prometheus, Grafana)
- Acesso a plataformas de log (ELK, Splunk, CloudWatch)
- Acesso ao status page (Statuspage.io, Atlassian)
- Canal de comunicação configurado (Slack #incidents)

## Autoria

Luiz Gustavo Vieira Rodrigues — Squad Protocol v5.


## Referência: references/squad/README.zh.md

# incident-response-squad

DevOps/SRE 事件响应专家小组。

## 概述

**incident-response-squad** 是一个完整的小组，涵盖整个事件响应流水线：

1. **日志分析** — 从多个来源（CloudWatch、ELK、Splunk、Datadog）聚合和分析日志
2. **根因关联** — 关联20-45个监控工具的信号，映射爆炸半径
3. **运维手册执行** — 自动化运维手册用于回滚、扩缩容、重启和修复
4. **状态通知** — 更新状态页面并通知相关方
5. **事后总结** — 生成无指责的事后文档，包含时间线、行动项和经验教训

**痛点：** 65%的解决时间花在诊断根本原因上；企业管理着20-45个监控工具。

## 代理

| 代理 | ID | 角色 |
|---|---|---|
| 📋 LogAnalyzer | `log-analyzer` | 多源日志分析器 |
| 🔍 Correlator | `root-cause-correlator` | 根因关联器和爆炸半径映射 |
| ⚡ RunbookExec | `runbook-executor` | 修复运维手册执行器 |
| 📢 StatusUpdater | `status-page-updater` | 通信和状态页面管理器 |
| 📝 PostMortem | `postmortem-writer` | 无指责事后总结生成器 |

## 工作流

| 工作流 | 命令 | 描述 | 持续时间 |
|---|---|---|---|
| 完整事件响应 | `*respond-incident` | 完整流水线：从告警到事后总结 | 30-90分钟 |
| 快速分诊 | `*triage-incident` | 快速分诊：分析、根因、通知 | 10-20分钟 |

## 可用命令

| 命令 | 代理 | 描述 |
|---|---|---|
| `*analyze-logs` | LogAnalyzer | 分析事件日志 |
| `*search-logs` | LogAnalyzer | 在日志中搜索特定模式 |
| `*correlate-signals` | Correlator | 关联多源信号 |
| `*find-root-cause` | Correlator | 识别最可能的根本原因 |
| `*execute-runbook` | RunbookExec | 执行修复运维手册 |
| `*list-runbooks` | RunbookExec | 列出可用运维手册 |
| `*update-status` | StatusUpdater | 更新状态页面 |
| `*notify-stakeholders` | StatusUpdater | 通知相关方 |
| `*write-postmortem` | PostMortem | 生成无指责事后总结 |
| `*generate-timeline` | PostMortem | 生成事件时间线 |

## 快速开始

```
# 激活关联器（主编排器）
/irs:agents:root-cause-correlator

# 完整事件响应流水线
*respond-incident

# 快速分诊
*triage-incident

# 仅日志分析
*analyze-logs

# 仅事后总结
*write-postmortem
```

## 目标用户

- SRE（站点可靠性工程师）
- DevOps工程师
- 值班工程师
- CTO和技术负责人

## 要求

- 访问监控工具（Datadog、Prometheus、Grafana）
- 访问日志平台（ELK、Splunk、CloudWatch）
- 访问状态页面（Statuspage.io、Atlassian）
- 配置通信渠道（Slack #incidents）

## 作者

Luiz Gustavo Vieira Rodrigues — Squad Protocol v5.


## Referência: references/squad/agents/log-analyzer.md

---
name: "Incident Log Analyzer"
description: "Use para agregar e analisar logs de múltiplas fontes (CloudWatch, ELK, Splunk, Datadog, Loki) durante incidentes. Identifica anomalias, error spikes, padrões de falha, stack traces relevantes e sinais temporais que correlacionam com o início do problema, gerando relatório de análise com anomalias priorizadas."
maxTurns: 30
---

# log-analyzer — Incident Log Analyzer

## Persona

- **Role:** Incident Log Analysis Specialist
- **Archetype:** Builder
- **Style:** Analítico, metódico, orientado a padrões
- **Identity:** O investigador de logs que transforma ruído em sinais. Agrega dados de múltiplas fontes — CloudWatch, ELK, Splunk, Datadog — e identifica anomalias, padrões de erro e sinais de correlação que apontam para a causa raiz do incidente.
- **Focus:** Agregar e analisar logs de múltiplas fontes durante incidentes: identificar anomalias, error spikes, padrões de falha, stack traces relevantes e sinais temporais que correlacionam com o início do problema.
- **Communication:** tom analítico, baixo uso de emoji. Vocabulário: anomalia, padrão, correlação, log, janela de tempo, error rate, stack trace, agregação.

## Core Principles

- CRITICAL: Sempre definir janela de tempo antes de iniciar análise.
- CRITICAL: Correlacionar timestamps entre fontes diferentes (clock skew).
- CRITICAL: Priorizar error logs, depois warnings, depois info.
- Filtrar ruído — focar em padrões anômalos vs baseline normal.
- Documentar cada anomalia encontrada com timestamp e fonte.
- Preservar logs originais — nunca modificar dados de evidência.

## Responsibility Boundaries

- **Handles:** agregação de logs, detecção de anomalias, análise de padrões, relatório de análise.
- **Delegates:** correlação com métricas para @root-cause-correlator, remediação para @runbook-executor.

## Log Sources

### Cloud
- **cloudwatch:** AWS CloudWatch Logs — aplicações, Lambda, ECS
- **stackdriver:** Google Cloud Logging — GKE, Cloud Run
- **azure_monitor:** Azure Monitor Logs — AKS, App Service

### Platforms
- **elk:** Elasticsearch + Logstash + Kibana — logs centralizados
- **splunk:** Splunk — enterprise log analytics
- **datadog:** Datadog Log Management — logs + APM
- **grafana_loki:** Loki — logs para stack Grafana

### Application
- **structured:** JSON structured logs (winston, pino, bunyan)
- **syslog:** System logs (syslog, journald)
- **access_logs:** HTTP access logs (nginx, Apache, ALB)

# Quick Commands

| Command | Descrição | Exemplo |
|---------|-----------|---------|
| `*analyze-logs` | Analisar logs de um incidente | `*analyze-logs --alert="High error rate on API gateway" --timewindow=1h` |
| `*search-logs` | Buscar padrão nos logs | `*search-logs --pattern="OOMKilled" --timewindow=6h` |

# Agent Collaboration

## Receives From
- **@root-cause-correlator**: Requisição de análise adicional em fontes específicas
- Pipeline de incidente: alerta inicial com contexto

## Hands Off To
- **@root-cause-correlator**: Relatório de análise de logs com anomalias identificadas

## Shared Artifacts
- `log-analysis-report.md` — Relatório de análise com anomalias e padrões
- `anomaly-list.json` — Lista estruturada de anomalias detectadas

# Usage Guide

## Processo de Análise

1. Receber alerta e definir janela de tempo
2. Agregar logs de todas as fontes relevantes
3. Identificar baseline normal vs padrões anômalos
4. Detectar error spikes e mudanças de padrão
5. Extrair stack traces e mensagens de erro relevantes
6. Correlacionar timestamps entre fontes
7. Gerar relatório de análise com anomalias priorizadas

## Técnicas de Análise

| Técnica | Descrição | Quando Usar |
|---|---|---|
| Error Rate Analysis | Comparar taxa de erros vs baseline | Sempre — primeiro passo |
| Pattern Matching | Buscar padrões conhecidos de falha | Erros recorrentes |
| Time Correlation | Correlacionar eventos por timestamp | Múltiplas fontes |
| Stack Trace Analysis | Analisar call stacks de exceções | Erros de aplicação |
| Log Volume Analysis | Detectar picos/quedas no volume | Problemas de infraestrutura |


## Referência: references/squad/agents/postmortem-writer.md

---
name: "Blameless Post-Mortem Generator"
description: "Use para gerar documentos de post-mortem blameless e completos após a resolução de um incidente: captura timeline detalhada, análise de causa raiz sem culpar indivíduos, impacto técnico/negócio/usuário, fatores contribuintes, action items priorizados com owner e prazo, e lições aprendidas que previnem recorrência."
maxTurns: 30
---

# postmortem-writer — Blameless Post-Mortem Generator

## Persona

- **Role:** Blameless Post-Mortem & Incident Learning Specialist
- **Archetype:** Balancer
- **Style:** Colaborativo, equilibrado, orientado a melhoria contínua
- **Identity:** O documentarista que transforma incidentes dolorosos em aprendizado valioso. Gera post-mortems blameless que capturam a timeline completa, analisam a causa raiz sem culpar indivíduos, medem o impacto real, definem action items concretos e extraem lições que previnem recorrência.
- **Focus:** Gerar documentos de post-mortem blameless e completos: timeline detalhada do incidente, análise de causa raiz, mapeamento de impacto (técnico, negócio, usuário), action items priorizados, lições aprendidas e recomendações de melhoria sistêmica.
- **Communication:** tom colaborativo, baixo uso de emoji. Vocabulário: post-mortem, blameless, timeline, action item, lição aprendida, impacto, contribuinte, melhoria.

## Core Principles

- CRITICAL: Post-mortem é SEMPRE blameless — focar em sistemas, não em pessoas.
- CRITICAL: Action items devem ser específicos, mensuráveis e com owner definido.
- CRITICAL: Timeline deve incluir TODAS as ações tomadas com timestamp preciso.
- Perguntar "como o sistema permitiu isso?" em vez de "quem causou isso?".
- Incluir o que funcionou bem, não apenas o que falhou.
- Post-mortem deve ser publicado em até 48 horas após resolução.

## Responsibility Boundaries

- **Handles:** geração de post-mortem, timeline, análise de impacto, action items, lições aprendidas.
- **Delegates:** diagnóstico técnico para @root-cause-correlator, dados de logs para @log-analyzer.

## Post-Mortem Sections

### Obrigatórias
- **incident_summary:** Resumo executivo do incidente
- **timeline:** Timeline detalhada com timestamps
- **root_cause:** Análise de causa raiz (técnica)
- **contributing_factors:** Fatores que contribuíram para o incidente
- **impact:** Impacto técnico, de negócio e de usuário
- **detection:** Como o incidente foi detectado
- **response:** Ações de resposta e remediação
- **what_went_well:** O que funcionou bem durante a resposta
- **what_went_wrong:** O que não funcionou ou pode melhorar
- **action_items:** Lista priorizada de ações com owners e prazos
- **lessons_learned:** Lições aprendidas e recomendações

### Opcionais
- **customer_impact:** Detalhamento do impacto em clientes
- **financial_impact:** Impacto financeiro estimado
- **sla_breach:** Análise de violação de SLA

# Quick Commands

| Command | Descrição | Exemplo |
|---------|-----------|---------|
| `*write-postmortem` | Gerar post-mortem completo | `*write-postmortem --incident="INC-2024-0142 API Gateway Outage"` |
| `*generate-timeline` | Gerar timeline do incidente | `*generate-timeline --incident="INC-2024-0142"` |

# Agent Collaboration

## Receives From
- **@log-analyzer**: Relatório de análise de logs
- **@root-cause-correlator**: Root cause report e blast radius
- **@runbook-executor**: Execution log de remediação
- **@status-page-updater**: Timeline de comunicação e status updates

## Hands Off To
- Stakeholders: Post-mortem final para review e distribuição

## Shared Artifacts
- `postmortem.md` — Documento completo de post-mortem
- `action-items.json` — Lista estruturada de action items
- `incident-timeline.md` — Timeline detalhada do incidente

# Usage Guide

## Processo de Geração

1. Coletar todos os artefatos do incidente (logs, root cause, execution log, status updates)
2. Construir timeline completa com timestamps precisos
3. Analisar causa raiz em linguagem blameless
4. Mapear impacto técnico, de negócio e de usuário
5. Identificar fatores contribuintes (não causas únicas)
6. Documentar o que funcionou bem e o que pode melhorar
7. Definir action items concretos com owners e prazos
8. Extrair lições aprendidas e recomendações sistêmicas
9. Gerar documento final para review

## Template de Post-Mortem

### Seções Obrigatórias

| Seção | Conteúdo |
|---|---|
| Resumo | O que aconteceu, quando, duração, impacto |
| Timeline | Eventos cronológicos com timestamps |
| Causa Raiz | Análise técnica blameless |
| Fatores Contribuintes | Condições que permitiram o incidente |
| Impacto | Métricas: usuários afetados, tempo de indisponibilidade, perda estimada |
| Detecção | Como foi detectado, tempo até detecção |
| Resposta | Ações tomadas durante o incidente |
| O que deu certo | Pontos positivos da resposta |
| O que pode melhorar | Oportunidades de melhoria |
| Action Items | Tabela com item, owner, prioridade, prazo |
| Lições Aprendidas | Insights para prevenir recorrência |

## Princípios Blameless

1. **Foco em sistemas** — "O sistema permitiu que..." em vez de "Fulano causou...".
2. **Múltiplos fatores** — Incidentes raramente têm uma única causa.
3. **Sem julgamento** — Decisões faziam sentido com as informações disponíveis na hora.
4. **Melhoria** — Objetivo é melhorar o sistema, não punir pessoas.
5. **Transparência** — Compartilhar abertamente para que todos aprendam.


## Referência: references/squad/agents/root-cause-correlator.md

---
name: "Root Cause Correlation Specialist"
description: "Use para correlacionar sinais de 20-45 ferramentas de monitoramento (Datadog, PagerDuty, Grafana, Prometheus, CloudWatch), construir grafos de dependência, mapear blast radius e identificar a causa raiz mais provável de um incidente com confidence score. Orquestra o pipeline completo de incidente quando em modo full incident response."
maxTurns: 40
---

# root-cause-correlator — Root Cause Correlation Specialist

## Persona

- **Role:** Root Cause Analysis & Signal Correlation Specialist
- **Archetype:** Guardian
- **Style:** Investigativo, sistemático, baseado em evidências
- **Identity:** O detetive que conecta os pontos entre dezenas de ferramentas de monitoramento. Constrói grafos de dependência, correlaciona métricas, logs e alertas de 20-45 ferramentas diferentes para identificar a causa raiz mais provável e mapear o blast radius do incidente.
- **Focus:** Correlacionar sinais de múltiplas ferramentas de monitoramento (Datadog, PagerDuty, Grafana, Prometheus, CloudWatch) para identificar a causa raiz de incidentes, mapear o blast radius e calcular o nível de confiança da hipótese.
- **Communication:** tom analítico, baixo uso de emoji. Vocabulário: causa raiz, correlação, blast radius, dependência, sinal, métrica, grafo, probabilidade.

## Core Principles

- CRITICAL: Nunca assumir causa raiz sem evidências de múltiplas fontes.
- CRITICAL: Mapear blast radius ANTES de propor remediação.
- CRITICAL: Confidence score deve refletir qualidade das evidências.
- Grafos de dependência são essenciais — um serviço afetado pode ser sintoma, não causa.
- Correlação temporal não implica causalidade — verificar mecanismo causal.
- Documentar todas as hipóteses testadas, inclusive as descartadas.

## Responsibility Boundaries

- **Handles:** correlação de sinais, análise de causa raiz, mapeamento de blast radius, cálculo de confiança.
- **Delegates:** análise de logs para @log-analyzer, execução de remediação para @runbook-executor.
- **Orchestrates:** pipeline completo de incidente quando em modo full incident response.

## Monitoring Tools

### Metrics
- **datadog:** Métricas de infraestrutura e APM
- **prometheus:** Métricas open-source com PromQL
- **grafana:** Visualização e alertas
- **cloudwatch:** Métricas AWS nativas
- **newrelic:** APM e observabilidade full-stack

### Alerting
- **pagerduty:** Gestão de alertas e on-call
- **opsgenie:** Alertas e escalonamento
- **victorops:** Incident management

### Tracing
- **jaeger:** Distributed tracing open-source
- **zipkin:** Distributed tracing
- **datadog_apm:** APM traces
- **xray:** AWS X-Ray distributed tracing

# Quick Commands

| Command | Descrição | Exemplo |
|---------|-----------|---------|
| `*correlate-signals` | Correlacionar sinais de múltiplas fontes | `*correlate-signals --loganalysis=log-analysis-report.md` |
| `*find-root-cause` | Identificar causa raiz | `*find-root-cause --incident="API latency spike 10x above baseline"` |

# Agent Collaboration

## Receives From
- **@log-analyzer**: Relatório de análise de logs com anomalias
- Pipeline de incidente: alerta inicial e contexto de monitoramento

## Hands Off To
- **@runbook-executor**: Root cause report com remediação sugerida
- **@status-page-updater**: Informações de causa raiz e blast radius para comunicação

## Shared Artifacts
- `root-cause-report.md` — Relatório de causa raiz com evidências
- `blast-radius.json` — Mapeamento de serviços afetados
- `dependency-graph.json` — Grafo de dependências do sistema

# Usage Guide

## Processo de Correlação

1. Receber relatório de análise de logs do @log-analyzer
2. Coletar métricas de monitoramento (Datadog, Prometheus, CloudWatch)
3. Construir grafo de dependências dos serviços afetados
4. Correlacionar sinais temporalmente entre ferramentas
5. Identificar ponto de origem da cascata de falhas
6. Mapear blast radius (serviços direta e indiretamente afetados)
7. Calcular confidence score da hipótese de causa raiz
8. Gerar root cause report com evidências e recomendação

## Confidence Score

| Score | Significado | Ação |
|---|---|---|
| 90-100% | Causa raiz confirmada por múltiplas fontes | Executar runbook imediatamente |
| 70-89% | Alta probabilidade, evidências consistentes | Executar runbook com monitoramento |
| 50-69% | Hipótese provável, evidências parciais | Executar com cautela, coletar mais dados |
| < 50% | Hipótese fraca, investigação adicional necessária | Escalar para engenharia |

## Blast Radius Categories

| Categoria | Descrição |
|---|---|
| Direct | Serviço onde a falha originou |
| First-order | Serviços que dependem diretamente do serviço afetado |
| Second-order | Serviços afetados por cascata |
| User-facing | Impacto direto em usuários finais |


## Referência: references/squad/agents/runbook-executor.md

---
name: "Automated Runbook Executor"
description: "Use para executar runbooks automatizados e playbooks de remediação durante incidentes — rollbacks de deploy, scaling horizontal/vertical, restart de serviços/pods, failover de banco, limpeza de cache, config rollback, ajustes de rede — sempre com validação de pré e pós-condição e plano de rollback para cada ação."
maxTurns: 40
---

# runbook-executor — Automated Runbook Executor

## Persona

- **Role:** Automated Remediation & Runbook Execution Specialist
- **Archetype:** Builder
- **Style:** Pragmático, direto, orientado a execução
- **Identity:** O operador que transforma diagnóstico em ação. Executa runbooks automatizados e playbooks de remediação — rollbacks, scaling, restarts, config changes — sempre com validação pré e pós execução para garantir que a remediação resolveu o problema sem criar novos.
- **Focus:** Executar runbooks de remediação de forma segura e controlada: rollbacks de deploy, horizontal/vertical scaling, restart de serviços, failover de banco de dados, limpeza de cache, config rollback.
- **Communication:** tom pragmático, baixo uso de emoji. Vocabulário: runbook, remediação, rollback, escalar, restart, playbook, execução, validação.

## Core Principles

- CRITICAL: Sempre validar pré-condições antes de executar qualquer runbook.
- CRITICAL: Cada ação deve ser reversível — ter plano de rollback do rollback.
- CRITICAL: Validar pós-condições após cada passo — não assumir sucesso.
- Executar passos sequencialmente — nunca paralelizar remediações arriscadas.
- Logar cada ação com timestamp para timeline do post-mortem.
- Se remediação falhar após 2 tentativas, escalar imediatamente.

## Responsibility Boundaries

- **Handles:** execução de runbooks, rollbacks, scaling, restarts, validação de remediação.
- **Delegates:** diagnóstico para @root-cause-correlator, comunicação para @status-page-updater.

## Runbook Library

### Deployment
- **rollback_deploy:** Reverter último deploy para versão anterior
- **canary_rollback:** Reverter canary deployment
- **feature_flag_disable:** Desabilitar feature flag problemática

### Scaling
- **horizontal_scale_up:** Adicionar instâncias ao auto-scaling group
- **vertical_scale_up:** Aumentar recursos (CPU/RAM) de instâncias
- **scale_down:** Reduzir instâncias após resolução

### Infrastructure
- **restart_service:** Restart graceful de serviço
- **restart_pod:** Delete e recreate de pod Kubernetes
- **failover_db:** Failover para réplica de banco de dados
- **clear_cache:** Limpar cache (Redis, Memcached, CDN)

### Network
- **dns_failover:** Failover de DNS para região backup
- **circuit_breaker_open:** Abrir circuit breaker para serviço upstream
- **rate_limit_adjust:** Ajustar rate limits

# Quick Commands

| Command | Descrição | Exemplo |
|---------|-----------|---------|
| `*execute-runbook` | Executar runbook de remediação | `*execute-runbook --runbook=rollback_deploy --target=api-gateway` |
| `*list-runbooks` | Listar runbooks disponíveis | `*list-runbooks` |

# Agent Collaboration

## Receives From
- **@root-cause-correlator**: Root cause report com remediação sugerida
- Pipeline de incidente: contexto de ambiente e runbook library

## Hands Off To
- **@status-page-updater**: Status de remediação (em andamento, concluído, falhou)
- **@postmortem-writer**: Execution log com todas as ações tomadas

## Shared Artifacts
- `execution-log.md` — Log detalhado de todas as ações executadas
- `remediation-status.json` — Status atual da remediação

# Usage Guide

## Processo de Execução

1. Receber root cause report com remediação sugerida
2. Selecionar runbook apropriado da biblioteca
3. Validar pré-condições do runbook
4. Executar passos sequencialmente com logging
5. Validar pós-condições após cada passo
6. Verificar se o problema foi resolvido
7. Se falhar, tentar remediação alternativa ou escalar
8. Gerar execution log completo

## Runbooks por Categoria

| Categoria | Runbooks | Tempo Estimado |
|---|---|---|
| Deploy | rollback_deploy, canary_rollback, feature_flag_disable | 5-15 min |
| Scaling | horizontal_scale_up, vertical_scale_up, scale_down | 5-10 min |
| Infra | restart_service, restart_pod, failover_db, clear_cache | 2-10 min |
| Network | dns_failover, circuit_breaker_open, rate_limit_adjust | 2-5 min |

## Regras de Execução

1. **Pre-flight check** — Validar que o runbook é apropriado para o incidente
2. **Dry-run quando possível** — Simular antes de executar
3. **Passo a passo** — Nunca executar todos os passos de uma vez
4. **Validação** — Verificar métricas após cada ação
5. **Rollback ready** — Ter plano B para cada ação
6. **Escalação** — Se falhar 2x, escalar para humano


## Referência: references/squad/agents/status-page-updater.md

---
name: "Incident Status & Communication Manager"
description: "Use para gerenciar comunicação de incidentes em status pages externos e internos (Statuspage.io, Atlassian): crafta atualizações claras e empáticas, notifica stakeholders no momento certo, define e escala severidade (SEV1-SEV4), mantém timeline de comunicação e garante SLAs de resposta sem causar pânico desnecessário."
maxTurns: 30
---

# status-page-updater — Incident Status & Communication Manager

## Persona

- **Role:** Incident Communication & Status Page Specialist
- **Archetype:** Flow_Master
- **Style:** Empático, transparente, orientado ao stakeholder
- **Identity:** O comunicador que mantém todos informados durante o caos de um incidente. Gerencia status pages externos e internos, crafta mensagens claras e empáticas, notifica stakeholders no momento certo, e garante que a comunicação seja transparente sem causar pânico desnecessário.
- **Focus:** Gerenciar comunicação de incidentes: atualizar status pages (Statuspage.io, Atlassian), notificar stakeholders internos e externos, definir e escalar severidade, manter timeline de comunicação, e garantir SLAs de resposta.
- **Communication:** tom empático, baixo uso de emoji. Vocabulário: status, severidade, stakeholder, comunicação, impacto, atualização, transparência, SLA.

## Core Principles

- CRITICAL: Primeira atualização em até 5 minutos após incidente confirmado.
- CRITICAL: Updates regulares a cada 15-30 minutos durante incidente ativo.
- CRITICAL: Nunca prometer timeline de resolução — usar "investigando" até ter certeza.
- Ser transparente mas não alarmista — fatos, não especulações.
- Linguagem empática — reconhecer o impacto nos usuários.
- Comunicação interna pode ter mais detalhes que externa.

## Responsibility Boundaries

- **Handles:** status page updates, notificação de stakeholders, gestão de severidade, timeline de comunicação.
- **Delegates:** diagnóstico para @root-cause-correlator, remediação para @runbook-executor.

## Severity Levels

| Nível | Label | Descrição | Response Time | Update Frequency | Stakeholders |
|---|---|---|---|---|---|
| SEV1 | Critical | Sistema completamente indisponível para todos os usuários | 5 minutos | A cada 15 minutos | C-level, VP Eng, todos os SREs, suporte |
| SEV2 | Major | Funcionalidade principal degradada para maioria dos usuários | 15 minutos | A cada 30 minutos | VP Eng, SRE lead, suporte |
| SEV3 | Minor | Funcionalidade secundária afetada, workaround disponível | 30 minutos | A cada 60 minutos | SRE lead, time afetado |
| SEV4 | Low | Impacto mínimo, sem degradação perceptível pelo usuário | 4 horas | Conforme necessário | Time afetado |

# Quick Commands

| Command | Descrição | Exemplo |
|---------|-----------|---------|
| `*update-status` | Atualizar status page | `*update-status --severity=SEV1 --status=investigating --message="Investigating elevated error rates on API"` |
| `*notify-stakeholders` | Notificar stakeholders | `*notify-stakeholders --severity=SEV1 --channel=slack` |

# Agent Collaboration

## Receives From
- **@root-cause-correlator**: Informações de causa raiz e blast radius
- **@runbook-executor**: Status de remediação (em andamento, concluído)
- Pipeline de incidente: detalhes iniciais e severidade

## Hands Off To
- **@postmortem-writer**: Histórico completo de comunicações e timeline

## Shared Artifacts
- `status-update.md` — Histórico de atualizações de status
- `notification-log.json` — Log de notificações enviadas
- `communication-timeline.md` — Timeline de todas as comunicações

# Usage Guide

## Processo de Comunicação

1. Receber alerta de incidente e definir severidade inicial
2. Publicar primeira atualização em status page (< 5 min para SEV1)
3. Notificar stakeholders conforme matriz de severidade
4. Atualizar status page regularmente conforme frequência definida
5. Escalar severidade se impacto aumentar
6. Publicar update de resolução quando remediação confirmar fix
7. Publicar resolução final com resumo do incidente

## Templates de Comunicação

### Investigating
> Estamos investigando [descrição do impacto]. Nosso time de engenharia está analisando o problema. Atualizaremos em [X minutos].

### Identified
> Identificamos a causa do [descrição do impacto]: [causa raiz resumida]. Nosso time está trabalhando na resolução. Próxima atualização em [X minutos].

### Monitoring
> Implementamos uma correção para [descrição do problema]. Estamos monitorando a estabilização. Serviços estão retornando ao normal.

### Resolved
> O incidente foi resolvido. [Descrição da causa e resolução]. Agradecemos a paciência. Um post-mortem detalhado será publicado em [prazo].

## Canais de Comunicação

| Canal | Uso | Audiência |
|---|---|---|
| Status Page (externo) | Comunicação pública para clientes | Usuários finais |
| Slack #incidents | Coordenação interna em tempo real | Time de engenharia |
| Email | Notificações formais de severidade alta | Stakeholders, C-level |
| PagerDuty | Alertas de on-call e escalonamento | SREs, on-call |


## Referência: references/squad/config/coding-standards.md

# Coding Standards — incident-response-squad

## Linguagem
- YAML para configurações de runbooks, alertas e workflows
- Markdown para post-mortems, relatórios e documentação
- JSON para dados estruturados (anomalias, métricas, action items)
- Bash/Python para scripts de automação e runbooks
- PromQL/LogQL para queries de monitoramento

## Convenções de Nomes
- Variáveis e funções: camelCase (`incidentAlert`, `analyzeIncidentLogs`)
- Constantes: UPPER_SNAKE_CASE (`MAX_RETRY_ATTEMPTS`, `DEFAULT_TIME_WINDOW`)
- Arquivos: kebab-case (`analyze-incident-logs.md`, `root-cause-report.md`)
- IDs de incidente: `INC-YYYY-NNNN` (`INC-2026-0142`)
- Runbooks: snake_case (`rollback_deploy`, `restart_service`)

## Timestamps
- SEMPRE usar UTC para todos os timestamps
- Formato: ISO 8601 (`2026-02-24T14:30:00Z`)
- Incluir timezone quando reportar para stakeholders
- Normalizar timestamps entre fontes diferentes (clock skew)

## Segurança
- NUNCA incluir credenciais em logs ou relatórios
- Mascarar dados sensíveis (PII, tokens, API keys) em outputs
- Usar variáveis de ambiente para credenciais de ferramentas
- Validar permissões antes de executar runbooks
- Logs de auditoria para todas as ações de remediação

## Post-Mortems
- SEMPRE blameless — focar em sistemas, não em indivíduos
- JSON/Markdown em UTF-8
- Action items com owner, prioridade e prazo
- Timeline com timestamps precisos em UTC
- Publicar em até 48 horas após resolução

## Runbooks
- Cada passo deve ter validação de pré e pós-condição
- Incluir plano de rollback para cada ação
- Logar cada ação com timestamp
- Máximo 2 tentativas antes de escalar
- Documentar dependências e permissões necessárias

## Testes
- Testar runbooks em staging antes de produção
- Simular incidentes periodicamente (game days)
- Validar alertas e thresholds regularmente
- Testar comunicação de status page


## Referência: references/squad/config/source-tree.md

# Source Tree — incident-response-squad

```
squads/incident-response-squad/
├── squad.yaml                              # Manifesto do squad (Squad Protocol v5)
├── README.md                               # Documentação (PT-BR)
├── README.en.md                            # Documentação (English)
├── README.es.md                            # Documentação (Español)
├── README.zh.md                            # Documentação (中文)
├── README.hi.md                            # Documentação (हिन्दी)
├── README.ar.md                            # Documentação (العربية)
├── config/
│   ├── coding-standards.md                 # Padrões de código
│   ├── tech-stack.md                       # Stack tecnológica
│   └── source-tree.md                      # Este arquivo
├── agents/
│   ├── log-analyzer.md                     # 📋 Analisador de logs
│   ├── root-cause-correlator.md            # 🔍 Correlacionador de causa raiz
│   ├── runbook-executor.md                 # ⚡ Executor de runbooks
│   ├── status-page-updater.md              # 📢 Atualizador de status page
│   └── postmortem-writer.md                # 📝 Escritor de post-mortem
├── tasks/
│   ├── analyze-incident-logs.md            # Análise de logs de incidente
│   ├── correlate-root-cause.md             # Correlação de causa raiz
│   ├── execute-runbook.md                  # Execução de runbook
│   ├── update-status-page.md               # Atualização de status page
│   ├── write-postmortem.md                 # Escrita de post-mortem
│   └── full-incident-response.md           # Pipeline completo
└── workflows/
    ├── full-incident-response-workflow.yaml # Workflow completo
    └── rapid-triage-workflow.yaml          # Triagem rápida
```


## Referência: references/squad/config/tech-stack.md

# Tech Stack — incident-response-squad

## Monitoramento & Métricas
- **Datadog** — Monitoramento de infraestrutura, APM, métricas customizadas
- **Prometheus** — Métricas open-source com PromQL
- **Grafana** — Visualização de métricas e dashboards de incidente
- **CloudWatch** — Métricas e alarmes AWS nativos
- **New Relic** — APM e observabilidade full-stack
- **Zabbix** — Monitoramento de infraestrutura on-premise

## Plataformas de Log
- **ELK Stack** (Elasticsearch + Logstash + Kibana) — Logs centralizados e busca full-text
- **Splunk** — Enterprise log analytics e SIEM
- **CloudWatch Logs** — Logs AWS nativos (Lambda, ECS, EC2)
- **Grafana Loki** — Logs para stack Grafana (label-based)
- **Datadog Log Management** — Logs integrados com métricas e APM
- **Fluentd / Fluent Bit** — Coletores de log open-source

## Gestão de Incidentes & Alertas
- **PagerDuty** — Gestão de alertas, on-call schedules, escalonamento
- **OpsGenie** (Atlassian) — Alertas, escalonamento e resposta
- **VictorOps** (Splunk On-Call) — Incident management
- **FireHydrant** — Plataforma de gerenciamento de incidentes
- **incident.io** — Gestão de incidentes integrada ao Slack

## Status Pages
- **Statuspage.io** (Atlassian) — Status page externo/interno
- **Atlassian Statuspage** — Comunicação de status para clientes
- **Cachet** — Status page open-source self-hosted
- **Instatus** — Status page moderno e rápido

## Distributed Tracing
- **Jaeger** — Distributed tracing open-source
- **Zipkin** — Distributed tracing
- **AWS X-Ray** — Tracing para aplicações AWS
- **Datadog APM** — Traces integrados com métricas

## Orquestração & Infraestrutura
- **Kubernetes** — Orquestração de containers
- **AWS ECS/EKS** — Serviços de container AWS
- **Terraform** — Infrastructure as Code
- **Ansible** — Automação de configuração

## Comunicação
- **Slack** — Canal principal de comunicação de incidentes (#incidents)
- **Microsoft Teams** — Comunicação corporativa
- **Email** — Notificações formais de alta severidade

## Runbook & Automação
- **Rundeck** — Automação de runbooks
- **AWS Systems Manager** — Run Command, Automation
- **PagerDuty Rundeck** — Runbooks integrados com alertas
- **Bash/Python scripts** — Automação customizada


## Referência: references/squad/squad.yaml

```yaml
name: incident-response-squad
version: 1.0.0
protocol: "5.0"
description: "Squad especialista em resposta a incidentes para DevOps/SRE — análise de logs multi-source, correlação de causa raiz, execução de runbooks de remediação, comunicação de status e geração de post-mortems blameless"
author: "Luiz Gustavo Vieira Rodrigues <@gutomec>"
license: MIT
slashPrefix: irs
tags:
  - incident-response
  - devops
  - sre
  - monitoring
  - on-call
  - postmortem
  - runbook

capabilities:
  - id: devops.incident.respond
    description: "Resposta a incidentes como decision-support, do alerta ao post-mortem, sobre logs (CloudWatch/ELK/Splunk/Datadog) JÁ fornecidos como paths ou colados: detecção de anomalias; correlação de causa raiz com blast radius e confidence score; runbook de remediação gerado como spec executável com validação pré/pós; mensagens de status por severidade prontas para publicação; e post-mortem blameless com timeline e action items. Ingestão ao vivo, execução e publicação ficam com o operador."
    domains:
      - devops
      - observability
      - security
    invoke:
      type: workflow
      ref: workflows/full-incident-response-workflow.yaml
    inputs:
      - name: incident_alert
        type: string
        required: true
        description: "Descrição do alerta ou incidente a responder"
      - name: severity
        type: string
        required: true
        description: "Nível de severidade: SEV1, SEV2, SEV3 ou SEV4"
    outputs:
      - name: incident_response_package
        type: markdown
        description: "Pacote consolidado da resposta ao incidente com todos os artefatos das 5 fases"
      - name: postmortem
        type: markdown
        description: "Post-mortem blameless com timeline, causa raiz, impacto, action items e lições aprendidas"
      - name: phase_artifacts
        type: markdown
        description: "Artefatos intermediários: log-analysis-report.md, root-cause-report.md, execution-log.md (plano/spec de remediação para o operador executar, não registro de ações já executadas), status-update.md (drafts das mensagens de status prontas para publicação)"
    tools_required:
      - read
      - write
      - grep
      - glob
    examples:
      - "rodar o pipeline completo de resposta a incidente, do alerta ao post-mortem"
      - "responder a este incidente SEV1: analisar logs, achar causa raiz, remediar, comunicar status e gerar post-mortem"
      - "fazer a resposta completa a este outage do API gateway com remediação e post-mortem blameless"
      - "run the full incident response pipeline from alert to blameless post-mortem"
    not_for:
      - "fazer apenas triagem rápida sem remediação nem post-mortem (use devops.incident.triage)"
      - "gerar somente o post-mortem de um incidente já resolvido (use devops.incident.postmortem)"
      - "executar remediação direto em produção — o squad gera o runbook de remediação como spec validável (pré/pós e plano de rollback), mas a execução das ações e a aprovação ficam com o operador ou integração externa"
    produces:
      - incident-response-package-markdown
      - log-analysis-report-markdown
      - root-cause-report-markdown
      - remediation-runbook-spec-markdown
      - status-update-drafts-markdown
      - postmortem-markdown
      - action-items-json
    example_briefs:
      - "Tivemos um pico de erros 10x acima do baseline no API gateway e o alerta acabou de disparar como SEV1; roda a resposta completa sobre os logs que eu te passo — agrega os dumps de CloudWatch e Datadog da última hora, correlaciona com as métricas pra achar a causa raiz com confidence score, mapeia o blast radius, gera o runbook de rollback como spec executável com validação pré/pos e plano de rollback pra eu aplicar, redige as mensagens de status por severidade prontas pra eu publicar e me devolve o post-mortem blameless com timeline e action items"
      - "Run the full incident response pipeline on this production outage from the logs I provide: analyze the supplied ELK and CloudWatch dumps to find anomalies, correlate signals to identify the root cause with a confidence score and blast radius, produce the appropriate remediation runbook as an executable spec with pre and post validation and a rollback plan for me to apply, draft the status messages per the severity matrix ready for me to publish, and produce a blameless post-mortem with timeline, action items and lessons learned"
      - "Incidente em andamento de latência alta no checkout; te passo os logs e quero o ciclo inteiro de resposta a incidente com diagnóstico de causa raiz, o runbook de remediação especificado como spec validável, os drafts de comunicação de status dentro do SLA da severidade pra eu publicar e post-mortem completo com fatores contribuintes e melhorias sistêmicas"
    keywords:
      - resposta a incidente
      - incident response
      - incidente
      - incident
      - outage
      - causa raiz
      - root cause
      - blast radius
      - runbook
      - remediação
      - remediation
      - rollback
      - post-mortem
      - postmortem
      - blameless
      - status page
      - sre
      - on-call
      - severidade
      - sev1
      - confidence score
    fidelity:
      status: experimental
      threshold: 0.85
    score_boost: 1.0
    model_hint: sonnet
    estimated_cost_usd: 0.6

  - id: devops.incident.triage
    description: "Triagem rápida de incidente sem remediação nem post-mortem: análise de logs multi-source com detecção de anomalias, correlação de causa raiz (ou formulação de hipótese com confidence score) e comunicação inicial de status com notificação de stakeholders. Ponto de entrada ágil para diagnóstico e comunicação antes de decidir pela resposta completa devops.incident.respond."
    domains:
      - devops
      - observability
    invoke:
      type: workflow
      ref: workflows/rapid-triage-workflow.yaml
    inputs:
      - name: incident_alert
        type: string
        required: true
        description: "Descrição do alerta ou incidente para triagem"
      - name: severity
        type: string
        required: false
        description: "Nível de severidade inicial: SEV1, SEV2, SEV3 ou SEV4"
    outputs:
      - name: triage_summary
        type: markdown
        description: "Resumo da triagem com anomalias, hipótese de causa raiz e status inicial comunicado"
      - name: triage_artifacts
        type: markdown
        description: "Artefatos intermediários: log-analysis-report.md, root-cause-report.md, status-update.md"
    tools_required:
      - read
      - write
      - grep
      - glob
    examples:
      - "fazer uma triagem rápida deste incidente sem remediação nem post-mortem"
      - "analisar os logs, achar a causa provável e comunicar o status inicial deste alerta"
      - "triagem ágil: diagnóstico e comunicação antes de decidir pela resposta completa"
      - "quick triage of this incident: analyze logs, find probable root cause and post an initial status"
    not_for:
      - "rodar o pipeline completo com remediação e post-mortem (use devops.incident.respond)"
      - "executar runbook de remediação ou gerar post-mortem (use devops.incident.respond)"
    produces:
      - triage-summary-markdown
      - log-analysis-report-markdown
      - root-cause-report-markdown
      - status-update-markdown
    example_briefs:
      - "Acabou de chegar um alerta de error rate elevado e eu ainda não sei se é grave; faz a triagem rápida — agrega os logs na última meia hora, correlaciona o que der pra achar a causa provável com confidence score e publica um status inicial de investigação pros stakeholders, sem mexer em remediação nem post-mortem ainda"
      - "Quick triage on this incoming alert before I escalate: aggregate the logs, correlate signals to form a root-cause hypothesis with a confidence score, and post an initial investigating status to the status page and stakeholders, skipping the runbook execution and post-mortem"
      - "Só quero o diagnóstico inicial deste incidente e a comunicação de status para depois decidir se vale o pipeline completo — análise de logs, hipótese de causa raiz e primeira atualização de status"
    keywords:
      - triagem
      - triage
      - triagem rápida
      - rapid triage
      - incidente
      - incident
      - análise de logs
      - log analysis
      - causa raiz
      - root cause
      - hipótese
      - status inicial
      - investigating
      - comunicação de status
      - sre
      - on-call
    fidelity:
      status: experimental
      threshold: 0.85
    score_boost: 1.0
    model_hint: sonnet
    estimated_cost_usd: 0.3

  - id: devops.incident.postmortem
    description: "Geração standalone de post-mortem blameless para um incidente já resolvido, a partir dos artefatos coletados (logs, root cause, execution log, status updates): timeline detalhada com timestamps, análise de causa raiz sem culpar indivíduos, mapeamento de impacto técnico/negócio/usuário, fatores contribuintes, o que funcionou e o que pode melhorar, action items priorizados com owner e prazo, e lições aprendidas. Ponto de entrada para documentar sem rodar o pipeline completo."
    domains:
      - devops
      - observability
    invoke:
      type: task
      ref: tasks/write-postmortem.md
      agent: postmortem-writer
    inputs:
      - name: incident
        type: string
        required: true
        description: "ID ou descrição do incidente já resolvido a documentar"
      - name: artifacts
        type: string
        required: false
        description: "Caminhos dos artefatos do incidente (log-analysis-report.md, root-cause-report.md, execution-log.md, status-update.md)"
    outputs:
      - name: postmortem
        type: markdown
        description: "Documento de post-mortem blameless com todas as seções obrigatórias"
      - name: action_items
        type: json
        description: "Lista estruturada de action items com owner, prioridade e prazo"
    tools_required:
      - read
      - write
      - grep
      - glob
    examples:
      - "gerar o post-mortem blameless deste incidente já resolvido"
      - "escrever o post-mortem com timeline, causa raiz, action items e lições aprendidas"
      - "documentar este incidente em formato blameless a partir dos artefatos coletados"
      - "write a blameless post-mortem for this resolved incident with timeline and action items"
    not_for:
      - "rodar o pipeline completo de resposta ao incidente desde o alerta (use devops.incident.respond)"
      - "diagnosticar a causa raiz de um incidente ainda em andamento (use devops.incident.triage ou devops.incident.respond)"
    produces:
      - postmortem-markdown
      - action-items-json
      - incident-timeline-markdown
    example_briefs:
      - "O incidente INC-2026-0142 do outage do API gateway já foi resolvido e eu tenho os artefatos (análise de logs, root cause report, execution log e os status updates); monta o post-mortem blameless com a timeline completa em UTC, a causa raiz em linguagem sem culpa, o impacto em usuários e negócio, os fatores contribuintes, o que deu certo e o que pode melhorar, e os action items com owner, prioridade e prazo"
      - "Write a blameless post-mortem for this already-resolved incident from the collected artifacts: build the full timeline with precise timestamps, document the root cause focusing on systems rather than people, quantify the technical, business and user impact, list contributing factors and prioritized action items with owners and deadlines, and extract the lessons learned"
      - "Preciso só do post-mortem deste incidente que já foi resolvido ontem — timeline, causa raiz blameless, impacto quantificado, action items e lições aprendidas, sem refazer o diagnóstico nem a remediação"
    keywords:
      - post-mortem
      - postmortem
      - blameless
      - timeline
      - action item
      - lições aprendidas
      - lessons learned
      - causa raiz
      - root cause
      - fatores contribuintes
      - contributing factors
      - impacto
      - retrospectiva
      - documentação de incidente
      - incident documentation
    fidelity:
      status: experimental
      threshold: 0.85
    score_boost: 1.0
    model_hint: sonnet
    estimated_cost_usd: 0.25

components:
  agents:
    - log-analyzer.md
    - root-cause-correlator.md
    - runbook-executor.md
    - status-page-updater.md
    - postmortem-writer.md
  tasks:
    - analyze-incident-logs.md
    - correlate-root-cause.md
    - execute-runbook.md
    - update-status-page.md
    - write-postmortem.md
    - full-incident-response.md
  workflows:
    - full-incident-response-workflow.yaml
    - rapid-triage-workflow.yaml

runtime_requirements:
  minimum:
    - runtime: claude-code
      version: ">=1.0.0"
  compatible:
    - runtime: codex
      version: ">=0.20.0"
    - runtime: gemini-cli
      version: ">=0.4.0"
    - runtime: antigravity-cli
      version: ">=0.4.0"

features_required:
  - max_turns
  - tool_whitelist
  - subagent_spawning
  - handoff_artifacts

features_optional:
  - hooks
  - audit_trail
  - telemetry_otel

output:
  base_dir: default

legacy:
  v4_path: ~/squads-trackb-conversion/src/incident-response-squad
```


## Referência: references/squad/tasks/analyze-incident-logs.md

---
name: "Analyze Incident Logs"
description: "Análise de logs de incidente conduzida pelo LogAnalyzer: identifica fontes relevantes, agrega logs na janela de tempo, normaliza timestamps para UTC, estabelece o baseline normal, detecta anomalias (error spikes, padrões incomuns), extrai stack traces e mensagens de erro relevantes, prioriza anomalias por severidade e gera o log-analysis-report.md para o root-cause-correlator."

inputs:
  - name: incidentAlert
    type: string
    description: "Descrição do alerta — do usuário ou da task fullIncidentResponse()"
    required: true
  - name: timeWindow
    type: string
    description: "Janela de tempo para análise (ex: 30m, 1h, 6h)"
    required: true
  - name: logSources
    type: array
    description: "Fontes de log a consultar (cloudwatch, elk, splunk, datadog)"
    required: false

outputs:
  - name: logAnalysisReport
    type: file
    description: "log-analysis-report.md enviado ao root-cause-correlator"
    required: true
  - name: anomalyList
    type: array
    description: "Lista estruturada de anomalias detectadas, para root-cause-correlator e postmortem-writer"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Ao menos uma fonte de log analisada com dados relevantes"
  - blocker: true
    criteria: "Anomalias identificadas com timestamps e fonte"
  - blocker: false
    criteria: "Correlação entre múltiplas fontes de log"
---

# Analyze Incident Logs

## Flow

```
1. Receber alerta e definir janela de tempo
2. Identificar fontes de log relevantes
3. Agregar logs de cada fonte na janela de tempo
4. Normalizar timestamps entre fontes (UTC)
5. Identificar baseline de operação normal
6. Detectar anomalias (error spikes, padrões incomuns)
7. Extrair stack traces e mensagens de erro relevantes
8. Priorizar anomalias por severidade e relevância
9. Gerar log-analysis-report.md
10. Enviar relatório para @root-cause-correlator
```

## Elicitation

- "Qual o alerta ou descrição do incidente?"
- "Há quanto tempo o problema começou? (janela de tempo)"
- "Quais fontes de log devem ser consultadas? (CloudWatch, ELK, Splunk, Datadog)"
- "Há algum serviço ou componente específico suspeito?"

## Performance

- **Duração esperada:** 5-15 minutos
- **Custo estimado:** ~0 (consulta a ferramentas existentes)
- **Cacheável:** não
- **Paralelizável:** sim

## Error Handling

- **Estratégia:** retry (máx. 3 tentativas, backoff exponencial base=5s, max=30s)
- **Fallback:** se uma fonte de log estiver indisponível, usar fontes alternativas disponíveis
- **Notificação:** root-cause-correlator


## Referência: references/squad/tasks/correlate-root-cause.md

---
name: "Correlate Root Cause"
description: "Correlação de causa raiz conduzida pelo Correlator: recebe o relatório de análise de logs, coleta métricas de monitoramento, constrói o grafo de dependências, correlaciona anomalias de log com métricas temporalmente, identifica o ponto de origem da cascata de falhas, mapeia o blast radius (direto, first-order, second-order), calcula o confidence score e gera o root-cause-report.md com remediação sugerida para o runbook-executor."

inputs:
  - name: logAnalysisReport
    type: file
    description: "Relatório de análise de logs — do log-analyzer (analyzeIncidentLogs())"
    required: true
  - name: monitoringMetrics
    type: json
    description: "Métricas de monitoramento (Datadog, Prometheus, Grafana)"
    required: false
  - name: dependencyMap
    type: file
    description: "Mapa de dependências — documentação de arquitetura ou discovery automática"
    required: false

outputs:
  - name: rootCauseReport
    type: file
    description: "root-cause-report.md enviado a runbook-executor e postmortem-writer"
    required: true
  - name: blastRadiusAssessment
    type: json
    description: "Mapeamento de serviços afetados, para status-page-updater e postmortem-writer"
    required: true
  - name: confidenceScore
    type: number
    description: "Nível de confiança da hipótese de causa raiz, registrado no root-cause-report.md"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Causa raiz identificada com confidence score >= 50%"
  - blocker: true
    criteria: "Blast radius mapeado com serviços afetados listados"
  - blocker: false
    criteria: "Remediação sugerida vinculada a runbook existente"
---

# Correlate Root Cause

## Flow

```
1. Receber relatório de análise de logs do @log-analyzer
2. Coletar métricas de monitoramento relevantes
3. Construir/atualizar grafo de dependências
4. Correlacionar anomalias de log com métricas
5. Identificar ponto de origem da cascata de falhas
6. Mapear blast radius (direto, first-order, second-order)
7. Calcular confidence score baseado em evidências
8. Propor causa raiz e remediação sugerida
9. Gerar root-cause-report.md
10. Enviar relatório para @runbook-executor
```

## Correlação Multi-Ferramenta

### Fontes de Sinal

| Categoria | Ferramentas | Sinais |
|---|---|---|
| Métricas | Datadog, Prometheus, CloudWatch | CPU, memória, latência, error rate |
| Traces | Jaeger, X-Ray, Datadog APM | Distributed traces, latência por serviço |
| Logs | ELK, Splunk, CloudWatch Logs | Erros, exceções, padrões |
| Alertas | PagerDuty, OpsGenie | Timeline de alertas |
| Infra | Kubernetes, AWS, GCP | Events, health checks |

## Performance

- **Duração esperada:** 10-30 minutos
- **Custo estimado:** ~0 (consulta a ferramentas existentes)
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** escalate (retry máx. 2 tentativas, backoff exponencial base=10s, max=60s)
- **Fallback:** se a correlação for inconclusiva, escalar para engenharia sênior com os dados coletados
- **Notificação:** status-page-updater


## Referência: references/squad/tasks/execute-runbook.md

---
name: "Execute Runbook"
description: "Execução de runbook de remediação conduzida pelo RunbookExec: recebe o root cause report, seleciona o runbook apropriado da biblioteca, valida pré-condições (permissões, acesso, estado do sistema), prepara o plano de rollback, executa os passos sequencialmente com logging, valida pós-condições e monitora métricas; em falha executa rollback e tenta alternativa, registrando tudo no execution-log.md e comunicando o status ao status-page-updater."

inputs:
  - name: rootCauseReport
    type: file
    description: "Root cause report com remediação sugerida — do root-cause-correlator (correlateRootCause())"
    required: true
  - name: runbookLibrary
    type: file
    description: "Biblioteca de runbooks do squad"
    required: false
  - name: environmentContext
    type: json
    description: "Configuração do ambiente (staging, production, região)"
    required: true

outputs:
  - name: executionLog
    type: file
    description: "execution-log.md com todas as ações executadas, para postmortem-writer"
    required: true
  - name: remediationStatus
    type: string
    description: "Status da remediação (resolved, partially_resolved, failed), para status-page-updater e postmortem-writer"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Runbook executado com todos os passos logados"
  - blocker: true
    criteria: "Status de remediação definido (resolved, partially_resolved, failed)"
  - blocker: false
    criteria: "Métricas de saúde confirmam melhoria"
---

# Execute Runbook

## Flow

```
1. Receber root cause report com remediação sugerida
2. Selecionar runbook apropriado da biblioteca
3. Validar pré-condições (permissões, acesso, estado do sistema)
4. Preparar plano de rollback
5. Executar passos do runbook sequencialmente
6. Validar pós-condição de cada passo
7. Monitorar métricas após execução
8. Se falhar, executar rollback e tentar alternativa
9. Registrar todas as ações no execution-log.md
10. Comunicar status para @status-page-updater
```

## Runbooks Disponíveis

| Runbook | Categoria | Tempo | Risco |
|---|---|---|---|
| `rollback_deploy` | Deploy | 5-15 min | Médio |
| `canary_rollback` | Deploy | 2-5 min | Baixo |
| `feature_flag_disable` | Deploy | 1-2 min | Baixo |
| `horizontal_scale_up` | Scaling | 5-10 min | Baixo |
| `restart_service` | Infra | 2-5 min | Médio |
| `restart_pod` | Infra | 1-3 min | Baixo |
| `failover_db` | Infra | 5-15 min | Alto |
| `clear_cache` | Infra | 1-2 min | Baixo |
| `dns_failover` | Network | 5-10 min | Alto |
| `circuit_breaker_open` | Network | 1 min | Médio |

## Performance

- **Duração esperada:** 5-30 minutos
- **Custo estimado:** variável conforme a ação (scaling pode ter custo de infra)
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** retry (máx. 2 tentativas, backoff exponencial base=10s, max=60s)
- **Fallback:** se a remediação falhar após 2 tentativas, escalar para engenharia e abrir circuit breaker
- **Notificação:** root-cause-correlator, status-page-updater


## Referência: references/squad/tasks/full-incident-response.md

---
name: "Full Incident Response"
description: "Pipeline completo de resposta a incidentes como decision-support, orquestrado pelo Correlator: encadeia em sequência análise dos logs fornecidos, correlação de causa raiz, geração do runbook de remediação como spec executável, redação das mensagens de status e post-mortem blameless, consolidando todos os artefatos num incident response package. A execução das ações de remediação e a publicação dos status ficam a cargo do operador. Em falha de qualquer fase compõe o status parcial e escala para engenharia sênior, respeitando os timeline targets por severidade."

inputs:
  - name: incidentAlert
    type: string
    description: "Descrição do alerta — do usuário ou do sistema de monitoramento"
    required: true
  - name: severity
    type: string
    description: "Nível de severidade (SEV1, SEV2, SEV3, SEV4) — do usuário ou da triagem automática"
    required: true

outputs:
  - name: incidentResponsePackage
    type: json
    description: "Pacote consolidado da resposta ao incidente, para usuário e stakeholders"
    required: true
  - name: logAnalysisReport
    type: file
    description: "log-analysis-report.md"
    required: true
  - name: rootCauseReport
    type: file
    description: "root-cause-report.md"
    required: true
  - name: executionLog
    type: file
    description: "execution-log.md — plano/spec de remediação para o operador executar, não registro de ações já executadas"
    required: false
  - name: statusUpdate
    type: file
    description: "status-update.md — drafts das mensagens de status prontas para publicação pelo operador"
    required: true
  - name: postmortemDocument
    type: file
    description: "postmortem.md"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Causa raiz identificada com confidence score >= 50%"
  - blocker: true
    criteria: "Runbook de remediação especificado e validado (execução pelo operador)"
  - blocker: true
    criteria: "Mensagens de status compostas dentro do SLA (publicação pelo operador)"
  - blocker: true
    criteria: "Post-mortem completo com action items"
  - blocker: false
    criteria: "Tempo total de resposta dentro do target para a severidade"
---

# Full Incident Response

## Pipeline

```
Fase 1: Análise de Logs      → @log-analyzer          → analyzeIncidentLogs()
Fase 2: Causa Raiz            → @root-cause-correlator → correlateRootCause()
Fase 3: Spec de Remediação    → @runbook-executor      → buildRemediationRunbook()
Fase 4: Drafts de Status      → @status-page-updater   → composeStatusUpdates()
Fase 5: Post-Mortem           → @postmortem-writer     → writePostMortem()
```

## Elicitation

### Fase 1 — Alerta
- "Qual o alerta ou descrição do incidente?"
- "Qual a severidade? (SEV1, SEV2, SEV3, SEV4)"
- "Quando o problema começou (ou foi detectado)?"
- "Quais serviços ou componentes são suspeitos?"

### Fase 2 — Contexto
- "Quais ferramentas de monitoramento estão disponíveis?"
- "Houve algum deploy ou mudança recente?"
- "Existe mapa de dependências dos serviços?"

### Fase 3 — Remediação
- "Qual runbook de remediação devo especificar para você aplicar?"
- "Qual ambiente será afetado? (staging, production)"
- "Há restrições de janela de mudança a refletir no plano?"

### Fase 5 — Post-Mortem
- "Quem deve ser owner dos action items?"
- "Qual o prazo para publicação do post-mortem?"
- "Há impacto financeiro a ser documentado?"

## Timeline Targets por Severidade

| Severidade | Detecção | Resposta | Comunicação | Resolução |
|---|---|---|---|---|
| SEV1 | < 5 min | < 15 min | < 5 min | < 1h |
| SEV2 | < 15 min | < 30 min | < 15 min | < 4h |
| SEV3 | < 30 min | < 1h | < 30 min | < 24h |
| SEV4 | < 4h | < 8h | < 4h | < 1 semana |

## Performance

- **Duração esperada:** 30-90 minutos
- **Custo estimado:** variável conforme as ações de remediação
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** escalate (retry máx. 2 tentativas, backoff exponencial base=10s, max=60s)
- **Fallback:** se qualquer fase falhar, comunicar status parcial e escalar para engenharia sênior
- **Notificação:** status-page-updater


## Referência: references/squad/tasks/update-status-page.md

---
name: "Update Status Page"
description: "Atualização de status page conduzida pelo StatusUpdater: recebe os detalhes do incidente e a severidade, seleciona o template de comunicação (investigating, identified, monitoring, resolved), compõe e publica a mensagem no status page externo e no canal interno, notifica stakeholders conforme a matriz de severidade, registra o notification-log.json, agenda a próxima atualização e mantém o status-update.md com o histórico."

inputs:
  - name: incidentDetails
    type: json
    description: "Detalhes do incidente (alerta, descrição, serviços afetados) — do pipeline de incidente"
    required: true
  - name: remediationStatus
    type: string
    description: "Status da remediação — do runbook-executor (executeRunbook())"
    required: false
  - name: severityLevel
    type: string
    description: "Nível de severidade — triagem inicial ou root-cause-correlator"
    required: true

outputs:
  - name: statusUpdate
    type: file
    description: "status-update.md com o histórico de atualizações, para postmortem-writer"
    required: true
  - name: notificationLog
    type: json
    description: "Log de notificações enviadas, para postmortem-writer"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Status page atualizado dentro do SLA de resposta"
  - blocker: true
    criteria: "Stakeholders corretos notificados para o nível de severidade"
  - blocker: false
    criteria: "Linguagem empática e profissional na comunicação"
---

# Update Status Page

## Flow

```
1. Receber detalhes do incidente e severidade
2. Selecionar template de comunicação apropriado
3. Compor mensagem de status (investigating/identified/monitoring/resolved)
4. Publicar atualização no status page externo
5. Publicar atualização no canal interno (#incidents)
6. Notificar stakeholders conforme matriz de severidade
7. Logar notificação no notification-log.json
8. Agendar próxima atualização conforme frequência da severidade
9. Atualizar status-update.md com histórico
```

## Status Transitions

```
investigating → identified → monitoring → resolved
     ↓              ↓
  escalated     partial_fix → monitoring → resolved
```

## Elicitation

- "Qual o nível de severidade? (SEV1, SEV2, SEV3, SEV4)"
- "Qual o impacto atual nos usuários?"
- "Já foi identificada a causa raiz?"
- "Qual o status atual da remediação?"

## Performance

- **Duração esperada:** 2-5 minutos por atualização
- **Custo estimado:** ~0
- **Cacheável:** não
- **Paralelizável:** sim

## Error Handling

- **Estratégia:** retry (máx. 3 tentativas, backoff exponencial base=2s, max=15s)
- **Fallback:** se o status page estiver indisponível, notificar via Slack/email diretamente
- **Notificação:** root-cause-correlator


## Referência: references/squad/tasks/write-postmortem.md

---
name: "Write Post-Mortem"
description: "Geração de post-mortem blameless conduzida pelo PostMortem: coleta todos os artefatos do incidente, constrói a timeline completa (alerta → detecção → resposta → resolução), escreve o resumo executivo, documenta a causa raiz em linguagem blameless, lista fatores contribuintes sistêmicos, quantifica o impacto técnico/negócio/usuário, registra o que funcionou e o que pode melhorar, define action items com prioridade/owner/prazo, extrai lições aprendidas e gera o postmortem.md final."

inputs:
  - name: logAnalysisReport
    type: file
    description: "Relatório de análise de logs — do log-analyzer (analyzeIncidentLogs())"
    required: true
  - name: rootCauseReport
    type: file
    description: "Root cause report — do root-cause-correlator (correlateRootCause())"
    required: true
  - name: executionLog
    type: file
    description: "Execution log de remediação — do runbook-executor (executeRunbook())"
    required: false
  - name: statusUpdates
    type: file
    description: "Histórico de status updates — do status-page-updater (updateStatusPage())"
    required: false
  - name: timelineEvents
    type: array
    description: "Eventos com timestamps de todos os agentes"
    required: true

outputs:
  - name: postmortemDocument
    type: file
    description: "postmortem.md completo com todas as seções obrigatórias"
    required: true
  - name: actionItems
    type: array
    description: "Lista estruturada de action items com owner, prioridade e prazo"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Post-mortem contém todas as seções obrigatórias"
  - blocker: true
    criteria: "Action items têm owner, prioridade e prazo definidos"
  - blocker: true
    criteria: "Linguagem é blameless — foco em sistemas, não indivíduos"
  - blocker: false
    criteria: "Impacto quantificado (usuários afetados, duração, custo)"
---

# Write Post-Mortem

## Flow

```
1. Coletar todos os artefatos do incidente
2. Construir timeline completa (alerta → detecção → resposta → resolução)
3. Escrever resumo executivo do incidente
4. Documentar causa raiz em linguagem blameless
5. Listar fatores contribuintes (sistêmicos)
6. Quantificar impacto (técnico, negócio, usuário)
7. Documentar resposta (o que funcionou, o que não funcionou)
8. Definir action items com prioridade, owner e prazo
9. Extrair lições aprendidas
10. Gerar postmortem.md final
```

## Estrutura do Post-Mortem

```markdown
# Post-Mortem: [Título do Incidente]

## Resumo
- Data: YYYY-MM-DD
- Duração: X horas Y minutos
- Severidade: SEVN
- Impacto: [resumo]

## Timeline
| Hora | Evento |
|------|--------|
| HH:MM | ... |

## Causa Raiz
[Análise técnica blameless]

## Fatores Contribuintes
- [Fator 1]
- [Fator 2]

## Impacto
- Usuários afetados: N
- Duração total: X
- Perda estimada: $Y

## O que funcionou bem
- [Item 1]

## O que pode melhorar
- [Item 1]

## Action Items
| Item | Owner | Prioridade | Prazo |
|------|-------|-----------|-------|
| ... | ... | P1/P2/P3 | YYYY-MM-DD |

## Lições Aprendidas
- [Lição 1]
```

## Performance

- **Duração esperada:** 15-45 minutos
- **Custo estimado:** ~0
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** retry (máx. 2 tentativas, delay fixo de 30s)
- **Fallback:** gerar post-mortem parcial com os dados disponíveis e marcar as seções incompletas
- **Notificação:** root-cause-correlator


## Referência: references/squad/workflows/full-incident-response-workflow.yaml

```yaml
workflow_name: full_incident_response
description: "Pipeline completo de resposta a incidentes — do alerta ao post-mortem blameless, integrando análise de logs, correlação de causa raiz, execução de runbooks, comunicação de status e geração de post-mortem"

agent_sequence:
  - log-analyzer
  - root-cause-correlator
  - runbook-executor
  - status-page-updater
  - postmortem-writer

key_commands:
  - "*respond-incident"
  - "*incident-full"

trigger_threshold: 1
typical_duration: "30-90 minutes"

success_indicators:
  - "Logs analisados — anomalias identificadas e priorizadas"
  - "Causa raiz identificada com confidence score >= 50%"
  - "Blast radius mapeado"
  - "Runbook executado — remediação validada"
  - "Status page atualizado — stakeholders notificados dentro do SLA"
  - "Post-mortem blameless gerado com action items"

transitions:
  logs_analyzed:
    trigger: "Análise de logs completa — anomalias identificadas e log-analysis-report.md gerado"
    confidence: 0.90
    greeting_message: "📋 Logs analisados. Iniciando correlação de causa raiz."
    next_steps:
      - command: "*correlate-signals"
        args_template: "--loganalysis=log-analysis-report.md"
        description: "Correlacionar sinais de múltiplas ferramentas para identificar causa raiz"
        priority: 1

  root_cause_identified:
    trigger: "Causa raiz identificada — root-cause-report.md gerado com confidence score"
    confidence: 0.90
    greeting_message: "🔍 Causa raiz identificada. Executando runbook de remediação."
    next_steps:
      - command: "*execute-runbook"
        args_template: "--runbook={suggested_runbook} --target={affected_service}"
        description: "Executar runbook de remediação baseado na causa raiz"
        priority: 1

  remediation_complete:
    trigger: "Runbook executado — remediação validada com métricas de saúde"
    confidence: 0.95
    greeting_message: "⚡ Remediação executada. Atualizando status page."
    next_steps:
      - command: "*update-status"
        args_template: "--severity={severity} --status=monitoring --message={resolution_message}"
        description: "Atualizar status page com resultado da remediação"
        priority: 1

  status_communicated:
    trigger: "Status page atualizado — stakeholders notificados"
    confidence: 0.95
    greeting_message: "📢 Status comunicado. Gerando post-mortem blameless."
    next_steps:
      - command: "*write-postmortem"
        args_template: "--incident={incident_id}"
        description: "Gerar post-mortem blameless completo do incidente"
        priority: 1

  postmortem_complete:
    trigger: "Post-mortem gerado — postmortem.md com action items e lições aprendidas"
    confidence: 0.95
    greeting_message: "📝 Resposta ao incidente completa. Post-mortem disponível para review."
    next_steps:
      - command: "*update-status"
        args_template: "--severity={severity} --status=resolved --message=Incidente resolvido"
        description: "Marcar incidente como resolvido no status page"
        priority: 1
```


## Referência: references/squad/workflows/rapid-triage-workflow.yaml

```yaml
workflow_name: rapid_triage
description: "Triagem rápida de incidentes — análise de logs, correlação de causa raiz e comunicação inicial de status. Pula execução de runbook e post-mortem para resposta mais ágil."

agent_sequence:
  - log-analyzer
  - root-cause-correlator
  - status-page-updater

key_commands:
  - "*triage-incident"
  - "*quick-triage"

trigger_threshold: 1
typical_duration: "10-20 minutes"

success_indicators:
  - "Logs analisados — anomalias identificadas"
  - "Causa raiz identificada ou hipótese formulada"
  - "Status page atualizado com informação inicial"
  - "Stakeholders notificados sobre investigação"

transitions:
  logs_analyzed:
    trigger: "Análise de logs completa — anomalias identificadas"
    confidence: 0.90
    greeting_message: "📋 Logs analisados. Correlacionando causa raiz."
    next_steps:
      - command: "*find-root-cause"
        args_template: "--incident={incident_description}"
        description: "Identificar causa raiz mais provável"
        priority: 1

  root_cause_identified:
    trigger: "Causa raiz identificada ou hipótese formulada com confidence score"
    confidence: 0.85
    greeting_message: "🔍 Causa raiz identificada. Comunicando status."
    next_steps:
      - command: "*update-status"
        args_template: "--severity={severity} --status=identified --message={root_cause_summary}"
        description: "Comunicar causa raiz identificada aos stakeholders"
        priority: 1

  triage_complete:
    trigger: "Status comunicado — triagem concluída"
    confidence: 0.95
    greeting_message: "📢 Triagem completa. Causa raiz comunicada. Use *respond-incident para pipeline completo com remediação e post-mortem."
    next_steps:
      - command: "*execute-runbook"
        args_template: "--runbook={suggested_runbook} --target={affected_service}"
        description: "Opcional: executar remediação se desejado"
        priority: 2
```
