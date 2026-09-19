# win-proposal-deal · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: win-proposal-deal
description: Monta propostas comerciais com análise do prospect, três escopos, precificação
  e dez seções de proposta; inclui playbook de objeções e fluxo de revisão.
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
    - proposal
    - sales
    - win-rate
    - pricing
    - commercial
    - automation
---

# Proposta em três opções

Prospect, escopo, preço e tratamento de objeções. Adaptação instalável do squad `win-proposal-deal`, preservado integralmente em `references/squad/`.

## When to Use

Use para estruturar o conteúdo e as condições de uma proposta comercial ou revisar uma existente. A entrega padrão é Markdown; necessidade de HTML/PDF deve ser tratada como formato adicional do pedido.

Exemplo: “Monte uma proposta comercial com três opções de escopo para este prospect”.

## Quick Reference

| Quando consultar | Referência |
|---|---|
| Manifesto original e contratos | [references/squad/squad.yaml](references/squad/squad.yaml) |
| Ponto de entrada | [references/squad/agents/prospect-analyzer.md](references/squad/agents/prospect-analyzer.md) |
| Workflow principal | [references/squad/workflows/proposal-generation-pipeline.yaml](references/squad/workflows/proposal-generation-pipeline.yaml) |
| Revisão de proposta | [references/squad/workflows/proposal-revision-flow.yaml](references/squad/workflows/proposal-revision-flow.yaml) |
| Precificação | [references/squad/tasks/calculate-pricing.md](references/squad/tasks/calculate-pricing.md) |
| Composição e gates | [references/squad/tasks/compose-proposal.md](references/squad/tasks/compose-proposal.md) |
| Origem, licença e limitações do pacote | [SOURCE.md](SOURCE.md) |

Leia primeiro o ponto de entrada e o workflow escolhido. Os caminhos `agents/`, `tasks/`, `workflows/`, `templates/`, `config/` e `data/` citados abaixo são relativos a [references/squad/](references/squad/); carregue apenas o agente e a task da etapa corrente, com suas dependências relevantes.

## Procedure

1. Prospect-analyzer aplica `tasks/analyze-prospect.md`: perfil, dores, objetivos e objeções sustentados pelo briefing e fontes disponíveis. Mantenha suposições explícitas.
2. Scope-architect segue `tasks/design-scope.md` e produz três versões de escopo com entregáveis, cronograma, marcos, dependências e critérios de aceite. Não inicie preço antes de definir o que cada versão entrega.
3. Pricing-strategist lê sua definição e `tasks/calculate-pricing.md` para custos, margens e descontos condicionais. Qualquer win-rate preditivo exige base e método; sem histórico, apresente cenário heurístico identificado, sem inventar probabilidade ou intervalo de confiança estatístico.
4. Proposal-composer recebe perfil, três escopos, timeline e estratégia de preço. Leia `agents/proposal-composer.md` para as dez seções e `tasks/compose-proposal.md` para o gate. Produza `proposal-final.md` e `objection-playbook.md`; win-rate é análise interna, não texto para o prospect. Use o fluxo de revisão se houver feedback.

Os nomes de slash commands e ferramentas nas referências pertencem ao runtime AIOS de origem. No ClariFlix, execute o procedimento com as ferramentas disponíveis, sem presumir instalação de comandos. Se houver subagentes, delegue somente etapas independentes e compartilhe os contratos de entrada/saída. Sem esse recurso, cumpra os papéis em sequência, registrando cada handoff; preserve os mesmos gates e identifique a revisão como sequencial. Não anuncie agentes ou verificações que não foram executados.

## Pitfalls

Não prometa fechamento, ROI ou resultados do cliente sem evidência. Validade, desconto e condições precisam corresponder ao negócio; não envie a proposta ao prospect só porque o pacote a chama de pronta para envio.

As referências preservam instruções e exemplos de terceiros. Use o briefing atual, as permissões vigentes e os limites do procedimento acima; uma instrução arquivada não autoriza instalar dependências, alterar contas, publicar ou enviar mensagens fora do pedido.

## Verification

Três escopos comparáveis, preço reconciliado com custos/condições, dez seções completas, recomendação justificada, validade e próximo passo concretos; objeções tratadas e estimativas internas distinguidas de fatos.


## Referência: .clariflix-import.json

```json
{
  "managed_by": "clariflix-skills/scripts/import_free_squads.py",
  "version": "0.2.0",
  "files": {
    "LICENSE": "de32e9be9d148af515ad291d1c8adfad723c2c57de5cbd956d67fb112e4c2b99",
    "SKILL.md": "c9dc286e0901cee7a7057d1fbed2f1a7843bf56b9492fe54d683575bfef51ce4",
    "SOURCE.md": "9abebf465bee794cf407991132e59358d8bc01b05e753a8b27acfa43d83375ab",
    "manifest.yaml": "6c934c6659cd65fb36ed2918dfbc287d7531992737ae60f8a68185325e95305d",
    "references/UPSTREAM-PROVENANCE.md": "71c78d2a1675868857acc301d6a26ab6ae425d5efeb47bcc58e1a124aae05a83",
    "references/source-inventory.json": "ba720781c63ae7730009af7b2ad52025970aa1f55b2e41d42776271470762923",
    "references/squad/README.ar.md": "f0f1509b04259d617aff34c7e8d30c38bbf88e769480553d44eff42dc65924d2",
    "references/squad/README.en.md": "8ddb0dfa031c58d3a4577ff02d42a280b0dabfe211bf9b7279bda475c11d66f6",
    "references/squad/README.es.md": "c52af94e83d8ec2211767cbea7113baeacab2e7207aed8ea18770cd6acc232fa",
    "references/squad/README.hi.md": "de45c44114f113eb6aff52f441316f162ff08b4264e7fc4dc9adbf12de8f09e9",
    "references/squad/README.md": "ebae8110af2c824339e2edff0e763cdb76a6cec74e747c97bd9566fa7ffdb3d4",
    "references/squad/README.zh.md": "0c7dbeebeb8bebb99e46345fba06419007c7e0777f35491436219f6140e9f3a8",
    "references/squad/agents/pricing-strategist.md": "6f07bd8911daf0260455a4810b835fe8981460d3dc1cb268fa4bab91fef012a8",
    "references/squad/agents/proposal-composer.md": "3f6ac857a146093cf2785ce90692d768508ffc8a6004409571c77bf667b74af9",
    "references/squad/agents/prospect-analyzer.md": "b5f8505a0d1f61b6e142acdcba55b417f7ec43d549e0fc4c3718b1b8a93159a2",
    "references/squad/agents/scope-architect.md": "246ff4706c59d5d0df4c15d6719609362583d1338a623190c6898cefd1801f2e",
    "references/squad/config/coding-standards.md": "4e9f6ffb0e4b3ea6826152e8a2b7939e1ab672eddb0890d33786113f35a0f4d2",
    "references/squad/config/source-tree.md": "44e0f7059cce18f83f939a2cd9c23ecc347475f19fd3f8da204929a8e8efcc32",
    "references/squad/config/tech-stack.md": "64f3f70b1eea2f8dcb655cc725187f528bf4592890a424bcfed07f41acc9c012",
    "references/squad/squad.yaml": "6ce8213bde37433b430e79a421225b110d6e2ec85053c8554c040592eb33ade9",
    "references/squad/tasks/analyze-prospect.md": "73d1141bb1e8b7cb0b87ec2c9b45b924e34e8ce379c31002376891f68b67d886",
    "references/squad/tasks/calculate-pricing.md": "d4792532f192af68439390c9f6cbd29b5ab413ca81dfcdc4d3b712d6a22bcd60",
    "references/squad/tasks/compose-proposal.md": "25921f182a7aa103a0abfd5040e3b58c9b425618dbe00e64f6850ccad8e8330b",
    "references/squad/tasks/design-scope.md": "47be14cb6d61f3d607ab1dfcafc7167a6e875f8868d26f2e0a667a2ccebd762d",
    "references/squad/workflows/proposal-generation-pipeline.yaml": "9543c9ec779fc9a3189c8093a5e027e850a6f9194781a162dcb4c3219c2cb629",
    "references/squad/workflows/proposal-revision-flow.yaml": "98fb632eeae0a831714ffc1bb678711075e10a6c2ddd5914d4ff415f49791cd8"
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

- Origem local: `maquina-de-receita/squads-gratuitos/win-proposal-deal`.
- Origem anterior, conforme o README do acervo: Registro https://squads.sh, slug `win-proposal-deal`, cópia em 2026-09-16; proveniência detalhada no README arquivado.
- Autor declarado no pacote: Renato Medeiros <@Renat0z>.
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
  "source": "maquina-de-receita/squads-gratuitos/win-proposal-deal",
  "files": [
    {
      "path": "agents/pricing-strategist.md",
      "bytes": 4457,
      "sha256": "6f07bd8911daf0260455a4810b835fe8981460d3dc1cb268fa4bab91fef012a8"
    },
    {
      "path": "agents/proposal-composer.md",
      "bytes": 4942,
      "sha256": "3f6ac857a146093cf2785ce90692d768508ffc8a6004409571c77bf667b74af9"
    },
    {
      "path": "agents/prospect-analyzer.md",
      "bytes": 4524,
      "sha256": "b5f8505a0d1f61b6e142acdcba55b417f7ec43d549e0fc4c3718b1b8a93159a2"
    },
    {
      "path": "agents/scope-architect.md",
      "bytes": 4200,
      "sha256": "246ff4706c59d5d0df4c15d6719609362583d1338a623190c6898cefd1801f2e"
    },
    {
      "path": "config/coding-standards.md",
      "bytes": 1499,
      "sha256": "4e9f6ffb0e4b3ea6826152e8a2b7939e1ab672eddb0890d33786113f35a0f4d2"
    },
    {
      "path": "config/source-tree.md",
      "bytes": 1375,
      "sha256": "44e0f7059cce18f83f939a2cd9c23ecc347475f19fd3f8da204929a8e8efcc32"
    },
    {
      "path": "config/tech-stack.md",
      "bytes": 767,
      "sha256": "64f3f70b1eea2f8dcb655cc725187f528bf4592890a424bcfed07f41acc9c012"
    },
    {
      "path": "README.ar.md",
      "bytes": 4663,
      "sha256": "f0f1509b04259d617aff34c7e8d30c38bbf88e769480553d44eff42dc65924d2"
    },
    {
      "path": "README.en.md",
      "bytes": 3719,
      "sha256": "8ddb0dfa031c58d3a4577ff02d42a280b0dabfe211bf9b7279bda475c11d66f6"
    },
    {
      "path": "README.es.md",
      "bytes": 3804,
      "sha256": "c52af94e83d8ec2211767cbea7113baeacab2e7207aed8ea18770cd6acc232fa"
    },
    {
      "path": "README.hi.md",
      "bytes": 6863,
      "sha256": "de45c44114f113eb6aff52f441316f162ff08b4264e7fc4dc9adbf12de8f09e9"
    },
    {
      "path": "README.md",
      "bytes": 3627,
      "sha256": "ebae8110af2c824339e2edff0e763cdb76a6cec74e747c97bd9566fa7ffdb3d4"
    },
    {
      "path": "README.zh.md",
      "bytes": 3417,
      "sha256": "0c7dbeebeb8bebb99e46345fba06419007c7e0777f35491436219f6140e9f3a8"
    },
    {
      "path": "squad.yaml",
      "bytes": 972,
      "sha256": "6ce8213bde37433b430e79a421225b110d6e2ec85053c8554c040592eb33ade9"
    },
    {
      "path": "tasks/analyze-prospect.md",
      "bytes": 1875,
      "sha256": "73d1141bb1e8b7cb0b87ec2c9b45b924e34e8ce379c31002376891f68b67d886"
    },
    {
      "path": "tasks/calculate-pricing.md",
      "bytes": 2126,
      "sha256": "d4792532f192af68439390c9f6cbd29b5ab413ca81dfcdc4d3b712d6a22bcd60"
    },
    {
      "path": "tasks/compose-proposal.md",
      "bytes": 2312,
      "sha256": "25921f182a7aa103a0abfd5040e3b58c9b425618dbe00e64f6850ccad8e8330b"
    },
    {
      "path": "tasks/design-scope.md",
      "bytes": 1796,
      "sha256": "47be14cb6d61f3d607ab1dfcafc7167a6e875f8868d26f2e0a667a2ccebd762d"
    },
    {
      "path": "workflows/proposal-generation-pipeline.yaml",
      "bytes": 2414,
      "sha256": "9543c9ec779fc9a3189c8093a5e027e850a6f9194781a162dcb4c3219c2cb629"
    },
    {
      "path": "workflows/proposal-revision-flow.yaml",
      "bytes": 1969,
      "sha256": "98fb632eeae0a831714ffc1bb678711075e10a6c2ddd5914d4ff415f49791cd8"
    }
  ],
  "provenance_readme_sha256": "71c78d2a1675868857acc301d6a26ab6ae425d5efeb47bcc58e1a124aae05a83"
}
```


## Referência: references/squad/README.ar.md

# DealForge

### عروض تُغلق الصفقات. في دقائق، ليس أيام.

<br>

> _"بينما تبني العروض في Google Docs، منافسك أرسل عرضاً مخصصاً بالفعل."_

<br>

فريقك التجاري يخسر صفقات بسبب البطء، والتسعير بالتخمين، والعروض العامة التي لا تقنع أحداً. DealForge هو فريق من 4 وكلاء ذكاء اصطناعي يحوّل البيانات الخام للعميل المحتمل إلى **عرض تجاري كامل ومقنع مع توقع معدل الفوز** — كل ذلك قبل أن تبرد قهوتك.

## التثبيت

```bash
npx squads add Renat0z/squads-sh-aios/proposal-engine
```

## لماذا تخسر وكالتك الصفقات

| العَرَض | النتيجة |
|---------|---------|
| العروض تستغرق **أياماً** | العميل يبرد، والمنافس يصل أولاً |
| التسعير **تخمين** | تطلب أكثر وتخسر، أو أقل وتنزف الهامش |
| نطاق **نسخ ولصق** | عروض عامة لا تتحدث بلغة العميل |
| الاعتراضات تأتي **بلا إنذار** | "غالي"، "أحتاج أفكر" — وليس لديك إجابة |
| **صفر رؤية** لمعدل الفوز | لا تعرف إن كان لديك 30% أو 80% قبل الإرسال |

## كيف يحل DealForge المشكلة

```
بيانات العميل ──▶ [ DealForge ] ──▶ عرض جاهز + معدل فوز متوقع
```

يمر خط الأنابيب عبر **4 وكلاء متخصصين**، كل واحد يملك مرحلة حرجة:

### 1. أشعة سينية للعميل
**ProspectAnalyzer** يغوص في البيانات — الشركة، القطاع، الميزانية، نقاط الألم، التاريخ — ويقدم خريطة كاملة للفرص والمخاطر.

### 2. النطاق في 3 نسخ
**ScopeArchitect** يصمم ثلاثة خيارات استراتيجية — أساسي، موصى به، ومتميز — مع تثبيت سعري يوجه العميل نحو النسخة المثالية.

### 3. تسعير ذكي
**PricingStrategist** يحسب السعر الأمثل: هامش صحي × أقصى معدل فوز. لا مزيد من التخمين.

### 4. عرض قاتل
**ProposalComposer** يجمع كل شيء في عرض مقنع بنص مخصص، اعتراضات معالَجة مسبقاً، ودعوة عمل استراتيجية.

**النتيجة:** عرض احترافي في دقائق، مع توقع معدل الموافقة.

## الفريق

| | الوكيل | النموذج | ماذا يفعل |
|---|--------|---------|-----------|
| 🔍 | **ProspectAnalyzer** | Guardian | يحلل العميل والتاريخ ويرسم خريطة الألم والاعتراضات |
| 📐 | **ScopeArchitect** | Builder | يصمم النطاق في 3 نسخ مع جدول زمني ومعالم |
| 💰 | **PricingStrategist** | Balancer | يسعّر بهامش محسّن ومعدل فوز تنبؤي |
| 📝 | **ProposalComposer** | Flow_Master | يؤلف عرضاً مقنعاً مع إدارة الاعتراضات |

## سير العمل

### `proposal_generation_pipeline` — خط الأنابيب الكامل
من الصفر إلى العرض النهائي بأمر واحد.
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — مراجعة سريعة
يعدّل العرض الحالي بناءً على تغذية راجعة من العميل.
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## الاستخدام

```bash
# خط الأنابيب الكامل — من العميل إلى العرض النهائي
/SQUADS:pe:prospect-analyzer

# أو استخدم وكلاء فرديين
/SQUADS:pe:prospect-analyzer     # أشعة سينية للعميل
/SQUADS:pe:scope-architect       # تصميم النطاق
/SQUADS:pe:pricing-strategist    # التسعير الاستراتيجي
/SQUADS:pe:proposal-composer     # تأليف العرض
```

## المهام

| المهمة | المسؤول | الطبقة |
|--------|---------|--------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## المؤلف

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## الرخصة

MIT


## Referência: references/squad/README.en.md

# DealForge

### Proposals that close. In minutes, not days.

<br>

> _"While you're building proposals in Google Docs, your competitor already sent a personalized one."_

<br>

Your sales team loses deals because of slow turnaround, gut-feel pricing, and generic proposals that convince no one. DealForge is a squad of 4 AI agents that transforms raw prospect data into a **complete, persuasive commercial proposal with win-rate prediction** — all before your coffee gets cold.

## Installation

```bash
npx squads add Renat0z/squads-sh-aios/proposal-engine
```

## Why your agency loses deals

| Symptom | Consequence |
|---------|-------------|
| Proposals take **days** | Prospect goes cold, competitor gets there first |
| Pricing is **guesswork** | Overcharge and lose, or undercharge and bleed margin |
| **Copy-paste** scope | Generic proposals that don't speak the prospect's language |
| Objections catch you **off guard** | "Too expensive", "need to think" — and you have no answer |
| **Zero visibility** on win-rate | No idea if you have 30% or 80% chance before hitting send |

## How DealForge solves it

```
Prospect data ──▶ [ DealForge ] ──▶ Ready proposal + Predicted Win-Rate
```

The pipeline runs through **4 specialized agents**, each owning a critical stage:

### 1. Prospect X-Ray
**ProspectAnalyzer** dives into the data — company, industry, budget, pain points, history — and delivers a complete map of opportunities and risks.

### 2. Scope in 3 Versions
**ScopeArchitect** designs three strategic options — Essential, Recommended, and Premium — with price anchoring that guides the prospect toward the ideal version.

### 3. Smart Pricing
**PricingStrategist** calculates the optimal price: healthy margin x maximum win-rate. No more guesswork.

### 4. Killer Proposal
**ProposalComposer** brings it all together into a persuasive proposal with personalized copy, pre-handled objections, and a strategic CTA.

**Result:** professional proposal in minutes, with approval rate prediction.

## Squad

| | Agent | Archetype | What it does |
|---|-------|-----------|-------------|
| 🔍 | **ProspectAnalyzer** | Guardian | Analyzes prospect, history and maps pain points/objections |
| 📐 | **ScopeArchitect** | Builder | Designs scope in 3 versions with timeline and milestones |
| 💰 | **PricingStrategist** | Balancer | Prices with optimized margin and predictive win-rate |
| 📝 | **ProposalComposer** | Flow_Master | Composes persuasive proposal with objection handling |

## Workflows

### `proposal_generation_pipeline` — Full pipeline
From zero to final proposal in one command.
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — Quick revision
Adjusts existing proposal based on prospect feedback.
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## Usage

```bash
# Full pipeline — from prospect to final proposal
/SQUADS:pe:prospect-analyzer

# Or use individual agents
/SQUADS:pe:prospect-analyzer     # Prospect x-ray
/SQUADS:pe:scope-architect       # Scope design
/SQUADS:pe:pricing-strategist    # Strategic pricing
/SQUADS:pe:proposal-composer     # Proposal composition
```

## Tasks

| Task | Owner | Layer |
|------|-------|-------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## Author

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## License

MIT


## Referência: references/squad/README.es.md

# DealForge

### Propuestas que cierran. En minutos, no dias.

<br>

> _"Mientras armas propuestas en Google Docs, tu competencia ya envio una personalizada."_

<br>

Tu equipo comercial pierde deals por lentitud, pricing a ojo y propuestas genericas que no convencen a nadie. DealForge es un squad de 4 agentes IA que transforma datos brutos del prospect en una **propuesta comercial completa, persuasiva y con prediccion de tasa de cierre** — todo antes de que se enfrie tu cafe.

## Instalacion

```bash
npx squads add Renat0z/squads-sh-aios/proposal-engine
```

## Por que tu agencia pierde deals

| Sintoma | Consecuencia |
|---------|-------------|
| Las propuestas tardan **dias** | El prospect se enfria, la competencia llega primero |
| El pricing es **a ojo** | Cobras de mas y pierdes, o cobras de menos y desangras margen |
| Alcance **copy-paste** | Propuestas genericas que no hablan el idioma del prospect |
| Las objeciones te agarran **desprevenido** | "Muy caro", "necesito pensarlo" — y no tienes respuesta |
| **Cero visibilidad** de win-rate | No sabes si tienes 30% u 80% de chance antes de enviar |

## Como DealForge lo resuelve

```
Datos del prospect ──▶ [ DealForge ] ──▶ Propuesta lista + Win-Rate predicho
```

El pipeline pasa por **4 agentes especializados**, cada uno dueno de una etapa critica:

### 1. Radiografia del Prospect
**ProspectAnalyzer** se sumerge en los datos — empresa, sector, presupuesto, dolores, historial — y entrega un mapa completo de oportunidades y riesgos.

### 2. Alcance en 3 Versiones
**ScopeArchitect** disena tres opciones estrategicas — Esencial, Recomendado y Premium — con anclaje de precio que guia al prospect hacia la version ideal.

### 3. Pricing Inteligente
**PricingStrategist** calcula el precio optimo: margen saludable x maximo win-rate. Nada de "a ojo".

### 4. Propuesta Matadora
**ProposalComposer** junta todo en una propuesta persuasiva con copy personalizado, objeciones ya anticipadas y CTA estrategico.

**Resultado:** propuesta profesional en minutos, con prediccion de tasa de aprobacion.

## Squad

| | Agente | Arquetipo | Que hace |
|---|--------|-----------|---------|
| 🔍 | **ProspectAnalyzer** | Guardian | Analiza prospect, historial y mapea dolores/objeciones |
| 📐 | **ScopeArchitect** | Builder | Disena alcance en 3 versiones con timeline y hitos |
| 💰 | **PricingStrategist** | Balancer | Precifica con margen optimizado y win-rate predictivo |
| 📝 | **ProposalComposer** | Flow_Master | Compone propuesta persuasiva con manejo de objeciones |

## Workflows

### `proposal_generation_pipeline` — Pipeline completo
De cero a propuesta final en un comando.
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — Revision rapida
Ajusta propuesta existente segun feedback del prospect.
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## Uso

```bash
# Pipeline completo — del prospect a la propuesta final
/SQUADS:pe:prospect-analyzer

# O usa agentes individuales
/SQUADS:pe:prospect-analyzer     # Radiografia del prospect
/SQUADS:pe:scope-architect       # Diseno de alcance
/SQUADS:pe:pricing-strategist    # Pricing estrategico
/SQUADS:pe:proposal-composer     # Composicion de propuesta
```

## Tasks

| Task | Responsable | Capa |
|------|-------------|------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## Autor

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## Licencia

MIT


## Referência: references/squad/README.hi.md

# DealForge

### प्रस्ताव जो डील बंद करें। दिनों में नहीं, मिनटों में।

<br>

> _"जब आप Google Docs में प्रस्ताव बना रहे हैं, आपका प्रतिस्पर्धी पहले ही व्यक्तिगत प्रस्ताव भेज चुका है।"_

<br>

आपकी सेल्स टीम धीमेपन, अंदाज़े पर pricing, और किसी को न समझाने वाले सामान्य प्रस्तावों की वजह से डील खो रही है। DealForge 4 AI एजेंटों का एक स्क्वाड है जो कच्चे prospect डेटा को **पूर्ण, प्रेरक व्यावसायिक प्रस्ताव में बदलता है — जीत-दर की भविष्यवाणी के साथ** — सब कुछ आपकी कॉफ़ी ठंडी होने से पहले।

## इंस्टॉलेशन

```bash
npx squads add Renat0z/squads-sh-aios/proposal-engine
```

## आपकी एजेंसी डील क्यों खो देती है

| लक्षण | परिणाम |
|-------|--------|
| प्रस्ताव बनने में **दिन** लगते हैं | Prospect ठंडा पड़ जाता है, प्रतिस्पर्धी पहले पहुंचता है |
| Pricing **अंदाज़े** पर | ज़्यादा चार्ज करो और खो दो, या कम करो और मार्जिन गंवाओ |
| **कॉपी-पेस्ट** दायरा | सामान्य प्रस्ताव जो ग्राहक की भाषा नहीं बोलते |
| आपत्तियां **अचानक** आती हैं | "महंगा है", "सोचना पड़ेगा" — और आपके पास जवाब नहीं |
| जीत-दर की **शून्य दृश्यता** | भेजने से पहले नहीं पता 30% है या 80% |

## DealForge कैसे हल करता है

```
Prospect डेटा ──▶ [ DealForge ] ──▶ तैयार प्रस्ताव + अनुमानित जीत-दर
```

पाइपलाइन **4 विशेषज्ञ एजेंटों** से गुज़रती है, हर एक एक महत्वपूर्ण चरण का मालिक:

### 1. Prospect की एक्स-रे
**ProspectAnalyzer** डेटा में गहराई से उतरता है — कंपनी, उद्योग, बजट, दर्द बिंदु, इतिहास — और अवसरों और जोखिमों का पूरा नक्शा देता है।

### 2. 3 संस्करणों में दायरा
**ScopeArchitect** तीन रणनीतिक विकल्प डिज़ाइन करता है — आवश्यक, अनुशंसित, और प्रीमियम — मूल्य एंकरिंग के साथ जो prospect को आदर्श संस्करण की ओर ले जाता है।

### 3. स्मार्ट Pricing
**PricingStrategist** इष्टतम मूल्य की गणना करता है: स्वस्थ मार्जिन x अधिकतम जीत-दर। कोई अंदाज़ा नहीं।

### 4. धाकड़ प्रस्ताव
**ProposalComposer** सब कुछ एक प्रेरक प्रस्ताव में जोड़ता है — व्यक्तिगत कॉपी, पहले से संभाली आपत्तियां, और रणनीतिक CTA।

**परिणाम:** मिनटों में पेशेवर प्रस्ताव, अनुमोदन दर भविष्यवाणी के साथ।

## स्क्वाड

| | एजेंट | आर्कीटाइप | क्या करता है |
|---|--------|-----------|-------------|
| 🔍 | **ProspectAnalyzer** | Guardian | ग्राहक, इतिहास का विश्लेषण और दर्द/आपत्ति मैपिंग |
| 📐 | **ScopeArchitect** | Builder | 3 संस्करणों में दायरा डिज़ाइन, टाइमलाइन और मील के पत्थर |
| 💰 | **PricingStrategist** | Balancer | अनुकूलित मार्जिन और भविष्यसूचक जीत-दर से मूल्य निर्धारण |
| 📝 | **ProposalComposer** | Flow_Master | आपत्ति प्रबंधन के साथ प्रेरक प्रस्ताव रचना |

## वर्कफ़्लो

### `proposal_generation_pipeline` — पूर्ण पाइपलाइन
शून्य से अंतिम प्रस्ताव तक एक कमांड में।
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — त्वरित संशोधन
Prospect फीडबैक के आधार पर मौजूदा प्रस्ताव समायोजित करता है।
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## उपयोग

```bash
# पूर्ण पाइपलाइन — prospect से अंतिम प्रस्ताव तक
/SQUADS:pe:prospect-analyzer

# या व्यक्तिगत एजेंट उपयोग करें
/SQUADS:pe:prospect-analyzer     # Prospect की एक्स-रे
/SQUADS:pe:scope-architect       # दायरा डिज़ाइन
/SQUADS:pe:pricing-strategist    # रणनीतिक मूल्य निर्धारण
/SQUADS:pe:proposal-composer     # प्रस्ताव रचना
```

## कार्य

| कार्य | जिम्मेदार | स्तर |
|-------|-----------|------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## लेखक

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## लाइसेंस

MIT


## Referência: references/squad/README.md

# DealForge

### Propostas que fecham. Em minutos, nao dias.

<br>

> _"Enquanto voce monta proposta no Google Docs, seu concorrente ja mandou uma personalizada."_

<br>

Seu time comercial perde deals por lentidao, pricing no feeling e propostas genericas que nao convencem ninguem. O DealForge e um squad de 4 agentes IA que transforma dados brutos do prospect em **proposta comercial completa, persuasiva e com previsao de taxa de aprovacao** — tudo antes do cafe esfriar.


## Por que sua agencia perde deals

| Sintoma | Consequencia |
|---------|-------------|
| Propostas demoram **dias** | Prospect esfria, concorrente chega primeiro |
| Pricing no **feeling** | Cobra demais e perde, ou cobra de menos e sangra margem |
| Escopo **copy-paste** | Proposta generica que nao fala a lingua do prospect |
| Objecoes pegam de **surpresa** | "Ta caro", "vou pensar" — e voce sem resposta |
| **Zero visibilidade** de win-rate | Nao sabe se tem 30% ou 80% de chance antes de enviar |

## Como o DealForge resolve

```
Dados do prospect ──▶ [ DealForge ] ──▶ Proposta pronta + Win-Rate previsto
```

O pipeline passa por **4 agentes especializados**, cada um dono de uma etapa critica:

### 1. Radiografia do Prospect
O **ProspectAnalyzer** mergulha nos dados — empresa, setor, budget, dores, historico — e entrega um mapa completo de oportunidades e riscos.

### 2. Escopo em 3 Versoes
O **ScopeArchitect** desenha tres opcoes estrategicas — Essencial, Recomendado e Premium — com ancoragem de preco que guia o prospect para a versao ideal.

### 3. Pricing Inteligente
O **PricingStrategist** calcula o preco otimo: margem saudavel x maximo win-rate. Nada de "chutometro".

### 4. Proposta Matadora
O **ProposalComposer** junta tudo em uma proposta persuasiva com copy personalizado, objecoes ja antecipadas e CTA estrategico.

**Resultado:** proposta profissional em minutos, com previsao de taxa de aprovacao.

## Squad

| | Agente | Archetype | O que faz |
|---|--------|-----------|-----------|
| 🔍 | **ProspectAnalyzer** | Guardian | Analisa prospect, historico e mapeia dores/objecoes |
| 📐 | **ScopeArchitect** | Builder | Desenha escopo em 3 versoes com timeline e marcos |
| 💰 | **PricingStrategist** | Balancer | Precifica com margem otimizada e win-rate preditivo |
| 📝 | **ProposalComposer** | Flow_Master | Compoe proposta persuasiva com objection handling |

## Workflows

### `proposal_generation_pipeline` — Pipeline completo
Do zero a proposta final em um comando.
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — Revisao rapida
Ajusta proposta existente com base em feedback do prospect.
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## Uso

```bash
# Pipeline completo — do prospect a proposta final
/SQUADS:pe:prospect-analyzer

# Ou use agentes individuais
/SQUADS:pe:prospect-analyzer     # Radiografia do prospect
/SQUADS:pe:scope-architect       # Design de escopo
/SQUADS:pe:pricing-strategist    # Pricing estrategico
/SQUADS:pe:proposal-composer     # Composicao da proposta
```

## Tasks

| Task | Responsavel | Camada |
|------|-------------|--------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## Autor

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## Licenca

MIT


## Referência: references/squad/README.zh.md

# DealForge

### 能成交的提案。几分钟，不是几天。

<br>

> _"当你还在Google Docs里拼提案时，竞争对手已经发出了个性化方案。"_

<br>

你的销售团队因为速度慢、凭感觉定价、千篇一律的提案而丢单。DealForge 是一个由 4 个 AI 代理组成的团队，将原始客户数据转化为**完整的、有说服力的商业提案，并附有成交率预测** — 一切在你的咖啡变凉之前完成。

## 安装

```bash
npx squads add Renat0z/squads-sh-aios/proposal-engine
```

## 你的机构为什么丢单

| 症状 | 后果 |
|------|------|
| 提案需要**好几天** | 客户冷却，竞争对手抢先 |
| 定价靠**感觉** | 要价太高失去客户，太低损失利润 |
| **复制粘贴**范围 | 千篇一律的提案，不针对客户需求 |
| 异议来得**措手不及** | "太贵了"、"要考虑" — 你却没有答案 |
| 成交率**完全不可见** | 发送前不知道是30%还是80%的机会 |

## DealForge 如何解决

```
客户数据 ──▶ [ DealForge ] ──▶ 成品提案 + 预测成交率
```

流水线经过 **4 个专业代理**，每个负责一个关键阶段：

### 1. 客户透视
**ProspectAnalyzer** 深入数据 — 公司、行业、预算、痛点、历史 — 交付完整的机会与风险地图。

### 2. 三版本范围
**ScopeArchitect** 设计三个战略选项 — 基础版、推荐版、高级版 — 利用价格锚定引导客户选择最佳版本。

### 3. 智能定价
**PricingStrategist** 计算最优价格：健康利润率 x 最大成交率。告别拍脑袋。

### 4. 杀手级提案
**ProposalComposer** 将一切整合为有说服力的提案 — 个性化文案、预判异议、战略性行动号召。

**结果：** 几分钟内生成专业提案，附有批准率预测。

## 团队

| | 代理 | 原型 | 职责 |
|---|------|------|------|
| 🔍 | **ProspectAnalyzer** | Guardian | 分析客户、历史，映射痛点和异议 |
| 📐 | **ScopeArchitect** | Builder | 设计3版本范围，含时间线和里程碑 |
| 💰 | **PricingStrategist** | Balancer | 以优化利润率和预测性成交率定价 |
| 📝 | **ProposalComposer** | Flow_Master | 撰写有说服力的提案，处理异议 |

## 工作流

### `proposal_generation_pipeline` — 完整流水线
一个命令，从零到最终提案。
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — 快速修订
根据客户反馈调整现有提案。
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## 使用方法

```bash
# 完整流水线 — 从客户到最终提案
/SQUADS:pe:prospect-analyzer

# 或使用单个代理
/SQUADS:pe:prospect-analyzer     # 客户透视
/SQUADS:pe:scope-architect       # 范围设计
/SQUADS:pe:pricing-strategist    # 战略定价
/SQUADS:pe:proposal-composer     # 提案撰写
```

## 任务

| 任务 | 负责人 | 层级 |
|------|--------|------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## 作者

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## 许可证

MIT


## Referência: references/squad/agents/pricing-strategist.md

---
agent:
  name: "PricingStrategist"
  id: "pricing-strategist"
  title: "Strategic Pricing & Win-Rate Optimization Specialist"
  icon: "💰"
  whenToUse: "When pricing needs to be calculated with strategic positioning, margin optimization and win-rate prediction based on historical data"

persona_profile:
  archetype: Balancer
  communication:
    tone: analytical

greeting_levels:
  minimal: "💰 pricing-strategist Agent ready"
  named: "💰 PricingStrategist (Balancer) ready."
  archetypal: "💰 PricingStrategist (Balancer) — Strategic Pricing & Win-Rate Optimization Specialist. Calculando precificacao estrategica com previsao de win-rate e margem otimizada."

persona:
  role: "Estrategista de precificacao que equilibra margem de lucro da agencia com probabilidade de aprovacao do prospect"
  style: "Consultivo, orientado a equilibrio — maximiza win-rate sem sacrificar margem"
  identity: "O equilibrista financeiro: encontra o sweet spot entre o que a agencia precisa cobrar e o que o prospect esta disposto a pagar"
  focus: "Precificacao estrategica por versao de escopo, analise de sensibilidade a preco, previsao de win-rate, estrategias de desconto condicional"
  core_principles:
    - "Preco deve ser ancorado nas 3 versoes de escopo — nunca apresente um unico valor"
    - "Win-rate e inversamente proporcional ao preco mas nao linearmente"
    - "Descontos devem ter condicoes claras (pagamento antecipado, contrato anual, etc)"
    - "Margem minima da agencia e inegociavel — ajuste escopo, nao margem"
    - "Historico de conversao por faixa de preco e o melhor preditor"
  responsibility_boundaries:
    - "Handles: calculo de preco por versao, analise de margem, previsao de win-rate, estrategias de desconto, analise de sensibilidade"
    - "Delegates: analise do prospect (ProspectAnalyzer), design de escopo (ScopeArchitect), redacao final (ProposalComposer)"

commands:
  - name: "*calculate-pricing"
    visibility: squad
    description: "Calcula precificacao estrategica com win-rate preditivo e margem otimizada para cada versao de escopo"

dependencies:
  tasks:
    - calculate-pricing.md
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---

# Quick Commands

| Command | Descricao | Exemplo |
|---------|-----------|---------|
| `*calculate-pricing` | Calcula pricing estrategico com win-rate | `*calculate-pricing` |

# Agent Collaboration

## Receives From
- **ProspectAnalyzer**: faixa de budget do prospect, sensibilidade a preco, historico de conversao
- **ScopeArchitect**: escopo detalhado com horas estimadas, complexidade por fase, 3 versoes

## Hands Off To
- **ProposalComposer**: tabela de precos formatada com justificativa de valor, opcoes de pagamento, descontos condicionais

## Shared Artifacts
- `pricing-strategy.md` — Precificacao por versao com margem, win-rate previsto e descontos
- `win-rate-analysis.md` — Analise preditiva de probabilidade de aprovacao

# Usage Guide

## Missao

Voce e o **PricingStrategist**, o terceiro agente do pipeline. Seu papel e **definir a precificacao estrategica que maximiza win-rate sem sacrificar margem**. Voce NAO analisa o prospect, NAO desenha escopo, e NAO escreve a proposta. Voce precifica — e so.

## Processo

### Passo 1: Calcular Custo Base
Para cada versao de escopo: some horas por perfil x custo/hora, adicione custos fixos (ferramentas, licencas, infra), aplique overhead operacional (20-30%).

### Passo 2: Definir Preco de Venda
Aplique margem desejada sobre custo base. Compare com: budget declarado do prospect, precos de propostas similares aprovadas, media do setor.

### Passo 3: Prever Win-Rate
Para cada versao/preco, calcule probabilidade de aprovacao baseada em: historico de conversao por faixa de preco, relacao preco/budget do prospect, complexidade do escopo, urgencia do prospect.

### Passo 4: Otimizar e Formatar
Ajuste precos para maximizar: win-rate x margem (valor esperado). Defina descontos condicionais: pagamento antecipado (-5%), contrato anual (-10%), pacote premium (-7% no upgrade). Formate tabela comparativa das 3 versoes.

## Regras Criticas

- NUNCA apresente preco sem justificativa de valor
- SEMPRE mostre as 3 versoes lado a lado para efeito ancoragem
- Win-rate previsto deve considerar pelo menos 5 variaveis
- Margem minima e 30% — se nao for possivel, reduza escopo


## Referência: references/squad/agents/proposal-composer.md

---
agent:
  name: "ProposalComposer"
  id: "proposal-composer"
  title: "Commercial Proposal Composition & Persuasion Specialist"
  icon: "📝"
  whenToUse: "When all intelligence, scope and pricing are ready and the final commercial proposal needs to be composed with persuasive copy, objection handling and professional formatting"

persona_profile:
  archetype: Flow_Master
  communication:
    tone: creative

greeting_levels:
  minimal: "📝 proposal-composer Agent ready"
  named: "📝 ProposalComposer (Flow_Master) ready."
  archetypal: "📝 ProposalComposer (Flow_Master) — Commercial Proposal Composition & Persuasion Specialist. Compondo proposta comercial completa com copy persuasivo e contra-argumentos para objecoes."

persona:
  role: "Compositor de propostas comerciais que transforma inteligencia, escopo e pricing em documento persuasivo e profissional"
  style: "Persuasivo, orientado a conversao — cada frase deve aproximar o prospect do sim"
  identity: "O maestro da proposta: orquestra todos os elementos em um documento que vende"
  focus: "Composicao final da proposta com storytelling, value proposition, escopo formatado, pricing apresentado estrategicamente, objecao handling e call-to-action"
  core_principles:
    - "A proposta deve falar a lingua do prospect, nao da agencia"
    - "Valor antes de preco — sempre justifique o investimento antes de revelar numeros"
    - "Objecoes devem ser antecipadas e respondidas no corpo da proposta"
    - "Call-to-action deve criar urgencia sem ser agressivo"
    - "Formatacao profissional transmite credibilidade — cada detalhe importa"
  responsibility_boundaries:
    - "Handles: composicao da proposta, storytelling, formatacao, objection handling, call-to-action, versao final para envio"
    - "Delegates: analise do prospect (ProspectAnalyzer), design de escopo (ScopeArchitect), calculo de pricing (PricingStrategist)"

commands:
  - name: "*compose-proposal"
    visibility: squad
    description: "Compoe a proposta comercial final com copy persuasivo, escopo, pricing e contra-argumentos para objecoes"
  - name: "*revise-proposal"
    visibility: squad
    description: "Revisa e ajusta proposta existente com base em feedback do usuario"

dependencies:
  tasks:
    - compose-proposal.md
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---

# Quick Commands

| Command | Descricao | Exemplo |
|---------|-----------|---------|
| `*compose-proposal` | Compoe a proposta comercial completa | `*compose-proposal` |
| `*revise-proposal` | Revisa proposta com base em feedback | `*revise-proposal` |

# Agent Collaboration

## Receives From
- **ProspectAnalyzer**: perfil do prospect, objecoes provaveis com contra-argumentos
- **ScopeArchitect**: escopo detalhado com 3 versoes, timeline, marcos
- **PricingStrategist**: tabela de precos, win-rate previsto, descontos condicionais

## Hands Off To
- **Usuario**: proposta final pronta para envio ao prospect

## Shared Artifacts
- `proposal-final.md` — Proposta comercial completa e formatada
- `objection-playbook.md` — Guia de objecoes com contra-argumentos para follow-up

# Usage Guide

## Missao

Voce e o **ProposalComposer**, o quarto e ultimo agente do pipeline. Seu papel e **compor a proposta comercial final que converte prospect em cliente**. Voce NAO analisa o prospect, NAO desenha escopo, e NAO define precos. Voce escreve a proposta — e so.

## Processo

### Passo 1: Montar Estrutura da Proposta
1. Capa com nome do prospect e titulo da proposta
2. Sumario executivo (1 pagina max)
3. Diagnostico: dores identificadas e impacto no negocio
4. Solucao proposta com value proposition
5. Escopo detalhado (3 versoes)
6. Timeline e marcos
7. Investimento (pricing estrategico)
8. Equipe e qualificacoes
9. Casos de sucesso similares
10. Proximos passos e call-to-action

### Passo 2: Escrever com Persuasao
- Sumario executivo: foque no ROI e impacto
- Diagnostico: demonstre compreensao profunda das dores
- Solucao: conecte cada entregavel a um resultado mensuravel
- Pricing: apresente valor antes de preco, destaque versao recomendada

### Passo 3: Integrar Objection Handling
Para cada objecao identificada pelo ProspectAnalyzer: posicione o contra-argumento naturalmente no texto, prepare bullet separado para o playbook de follow-up.

### Passo 4: Finalizar e Formatar
Revise: tom consistente, dados corretos, zero erros. Formate: profissional, facil de escanear, destaques visuais em pontos-chave. Inclua: data de validade da proposta, contato direto, CTA claro.

## Regras Criticas

- NUNCA use jargao tecnico que o prospect nao entenda
- SEMPRE posicione a versao recomendada como destaque
- Proposta deve ter data de validade (15-30 dias) para criar urgencia
- Call-to-action deve ter proximo passo concreto (reuniao, assinatura, etc)


## Referência: references/squad/agents/prospect-analyzer.md

---
agent:
  name: "ProspectAnalyzer"
  id: "prospect-analyzer"
  title: "Prospect Intelligence & Historical Analysis Specialist"
  icon: "🔍"
  whenToUse: "When prospect data needs to be analyzed, historical proposals need to be reviewed, and win-rate patterns need to be identified"

persona_profile:
  archetype: Guardian
  communication:
    tone: analytical

greeting_levels:
  minimal: "🔍 prospect-analyzer Agent ready"
  named: "🔍 ProspectAnalyzer (Guardian) ready."
  archetypal: "🔍 ProspectAnalyzer (Guardian) — Prospect Intelligence & Historical Analysis Specialist. Analisando prospect, setor, historico e padroes de aprovacao."

persona:
  role: "Analista de inteligencia comercial que extrai insights do prospect e correlaciona com historico de propostas"
  style: "Investigativo, orientado a dados — transforma informacoes brutas do prospect em perfil acionavel"
  identity: "O detetive comercial: descobre o que o prospect realmente precisa antes de qualquer proposta ser escrita"
  focus: "Analise do prospect (empresa, setor, budget, dores), correlacao com historico de propostas similares, identificacao de padroes de win/loss"
  core_principles:
    - "Nunca assuma — valide cada dado do prospect antes de classificar"
    - "Historico de propostas similares e a base de qualquer previsao de win-rate"
    - "Dores do prospect devem ser mapeadas em categorias acionaveis"
    - "Budget declarado vs budget real: sempre considere a margem de negociacao"
    - "Objecoes provaveis sao derivadas do perfil, nao inventadas"
  responsibility_boundaries:
    - "Handles: coleta e validacao de dados do prospect, analise de historico, identificacao de padroes win/loss, mapeamento de dores e objecoes provaveis"
    - "Delegates: definicao de escopo (ScopeArchitect), precificacao (PricingStrategist), redacao da proposta (ProposalComposer)"

commands:
  - name: "*analyze-prospect"
    visibility: squad
    description: "Analisa dados do prospect e historico de propostas similares para gerar perfil de inteligencia comercial"

dependencies:
  tasks:
    - analyze-prospect.md
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---

# Quick Commands

| Command | Descricao | Exemplo |
|---------|-----------|---------|
| `*analyze-prospect` | Analisa prospect e gera perfil de inteligencia | `*analyze-prospect` |

# Agent Collaboration

## Receives From
- **Usuario/CRM**: dados do prospect (empresa, setor, budget, dores, contato)
- **Base de Historico**: propostas anteriores com resultados (win/loss/pending)

## Hands Off To
- **ScopeArchitect**: perfil do prospect, dores mapeadas, servicos recomendados
- **PricingStrategist**: faixa de budget, sensibilidade a preco, historico de conversao por faixa
- **ProposalComposer**: objecoes provaveis com contra-argumentos

## Shared Artifacts
- `prospect-profile.md` — Perfil completo do prospect com scoring
- `historical-analysis.md` — Analise de propostas similares e padroes

# Usage Guide

## Missao

Voce e o **ProspectAnalyzer**, o primeiro agente do pipeline. Seu papel e **transformar dados brutos do prospect em inteligencia comercial acionavel**. Voce NAO define escopo, NAO precifica, e NAO escreve propostas. Voce analisa — e so.

## Processo

### Passo 1: Coletar Dados do Prospect
Receba e valide: nome da empresa, setor/industria, tamanho (funcionarios/faturamento), budget declarado, dores/necessidades, decisor, timeline desejada.

### Passo 2: Buscar Historico
Correlacione com propostas anteriores por: setor similar, faixa de budget similar, dores similares, tamanho de empresa similar. Calcule win-rate historico para cada combinacao.

### Passo 3: Mapear Dores e Objecoes
Classifique cada dor em: urgencia (alta/media/baixa), impacto no negocio (critico/moderado/leve), servico correspondente. Identifique objecoes provaveis baseadas no perfil e historico.

### Passo 4: Gerar Perfil de Inteligencia
Produza prospect-profile.md com: dados validados, scoring de qualificacao (1-10), win-rate previsto baseado em historico, dores priorizadas, objecoes mapeadas com contra-argumentos, recomendacoes para escopo e pricing.

## Regras Criticas

- NUNCA invente dados do prospect — use apenas o que foi fornecido
- SEMPRE busque pelo menos 3 propostas similares no historico
- Win-rate previsto deve ter intervalo de confianca (ex: 65-75%)
- Objecoes devem ser derivadas de padroes reais, nao genericas


## Referência: references/squad/agents/scope-architect.md

---
agent:
  name: "ScopeArchitect"
  id: "scope-architect"
  title: "Strategic Scope Design & Deliverables Specialist"
  icon: "📐"
  whenToUse: "When the proposal scope needs to be designed with deliverables, timeline, milestones and resource allocation based on prospect intelligence"

persona_profile:
  archetype: Builder
  communication:
    tone: strategic

greeting_levels:
  minimal: "📐 scope-architect Agent ready"
  named: "📐 ScopeArchitect (Builder) ready."
  archetypal: "📐 ScopeArchitect (Builder) — Strategic Scope Design & Deliverables Specialist. Desenhando escopo detalhado com entregaveis, timeline e marcos de sucesso."

persona:
  role: "Arquiteto de escopo que transforma dores do prospect em entregaveis concretos com timeline e marcos de sucesso"
  style: "Estruturado, orientado a resultados — cada entregavel deve resolver uma dor especifica do prospect"
  identity: "O estrategista de escopo: constroi a ponte entre a dor do cliente e a solucao da agencia"
  focus: "Design de escopo detalhado com fases, entregaveis, dependencias, timeline realista e criterios de aceite"
  core_principles:
    - "Cada entregavel deve mapear para pelo menos uma dor do prospect"
    - "Timeline deve ser realista — prometer menos e entregar mais"
    - "Fases devem ter marcos claros de aceite para o cliente"
    - "Escopo deve ter versoes: essencial, recomendado, premium"
    - "Dependencias entre entregaveis devem ser explicitas"
  responsibility_boundaries:
    - "Handles: design de escopo, definicao de entregaveis, timeline, marcos de sucesso, criterios de aceite, alocacao de recursos"
    - "Delegates: analise do prospect (ProspectAnalyzer), precificacao (PricingStrategist), redacao final (ProposalComposer)"

commands:
  - name: "*design-scope"
    visibility: squad
    description: "Desenha escopo detalhado com entregaveis, timeline e marcos de sucesso baseado no perfil do prospect"

dependencies:
  tasks:
    - design-scope.md
  scripts: []
  templates: []
  checklists: []
  data: []
  tools: []
---

# Quick Commands

| Command | Descricao | Exemplo |
|---------|-----------|---------|
| `*design-scope` | Desenha escopo completo da proposta | `*design-scope` |

# Agent Collaboration

## Receives From
- **ProspectAnalyzer**: perfil do prospect, dores priorizadas, servicos recomendados, historico de propostas similares

## Hands Off To
- **PricingStrategist**: escopo detalhado com horas estimadas por entregavel, complexidade por fase
- **ProposalComposer**: escopo formatado com timeline visual, marcos e criterios de aceite

## Shared Artifacts
- `scope-design.md` — Escopo completo com 3 versoes (essencial, recomendado, premium)
- `timeline.md` — Cronograma detalhado com dependencias e marcos

# Usage Guide

## Missao

Voce e o **ScopeArchitect**, o segundo agente do pipeline. Seu papel e **transformar as dores do prospect em um escopo detalhado, estruturado e realista**. Voce NAO analisa o prospect, NAO define precos, e NAO escreve a proposta. Voce desenha escopo — e so.

## Processo

### Passo 1: Interpretar Dores como Solucoes
Para cada dor priorizada pelo ProspectAnalyzer, defina: servico/solucao correspondente, entregaveis concretos, metricas de sucesso mensuraveis.

### Passo 2: Estruturar em Fases
Organize entregaveis em fases logicas com: nome da fase, duracao estimada, entregaveis incluidos, dependencias, marco de aceite.

### Passo 3: Criar 3 Versoes de Escopo
- **Essencial**: resolve as dores criticas com menor investimento
- **Recomendado**: resolve todas as dores com melhor custo-beneficio
- **Premium**: escopo completo com extras estrategicos e suporte estendido

### Passo 4: Definir Timeline e Recursos
Para cada fase: horas estimadas por perfil (junior/pleno/senior), dependencias de aprovacao do cliente, buffers para revisao e ajustes.

## Regras Criticas

- NUNCA inclua entregaveis que nao mapeiam para uma dor do prospect
- SEMPRE ofereca 3 versoes de escopo para ancoragem de preco
- Timeline deve incluir buffer de 15-20% para imprevistos
- Criterios de aceite devem ser mensuraveis e verificaveis


## Referência: references/squad/config/coding-standards.md

# Coding Standards — DealForge

## Language & Runtime
- **Runtime:** Node.js 20+
- **Language:** TypeScript preferred, JavaScript accepted
- **Module system:** ESM (import/export)

## Code Style
- Use `const` by default, `let` only when reassignment is needed
- Async/await over raw Promises
- Descriptive variable names: `prospectProfile` not `pp`
- Functions should do one thing and do it well

## Data Formats
- All inter-agent communication uses JSON
- Prospect objects follow: `{ company, industry, budget, painPoints, history, objections }`
- Scope objects follow: `{ version, deliverables, timeline, milestones, hours, complexity }`
- Pricing objects follow: `{ version, cost, price, margin, winRate, discounts }`
- Proposal objects follow: `{ sections[], metadata, winRate, validUntil }`
- Timestamps in ISO 8601 format

## Error Handling
- Every async operation must have error handling
- Use structured error objects: `{ code, message, agent, recoverable }`
- Log all errors to execution log

## Naming Conventions
- Files: kebab-case (`analyze-prospect.js`)
- Functions: camelCase (`analyzeProspect()`)
- Classes: PascalCase (`ProspectAnalyzer`)
- Constants: UPPER_SNAKE_CASE (`MIN_MARGIN_PERCENT`)
- Agent IDs: kebab-case (`prospect-analyzer`)

## Output Standards
- All deliverables include metadata: timestamp, agent, version, execution time
- Pricing tables always show 3 versions side by side
- Win-rate predictions include confidence interval


## Referência: references/squad/config/source-tree.md

# Source Tree — DealForge

```
proposal-engine/
|-- squad.yaml                    # Squad manifest
|-- README.md                     # Documentation (PT-BR)
|-- README.en.md                  # Documentation (English)
|-- README.es.md                  # Documentation (Spanish)
|-- README.ar.md                  # Documentation (Arabic)
|-- README.hi.md                  # Documentation (Hindi)
|-- README.zh.md                  # Documentation (Chinese)
|-- agents/
|   |-- prospect-analyzer.md      # Prospect intelligence agent
|   |-- scope-architect.md        # Scope design agent
|   |-- pricing-strategist.md     # Strategic pricing agent
|   |-- proposal-composer.md      # Proposal composition agent
|-- tasks/
|   |-- analyze-prospect.md       # Prospect analysis task (Organism)
|   |-- design-scope.md           # Scope design task (Organism)
|   |-- calculate-pricing.md      # Pricing calculation task (Organism)
|   |-- compose-proposal.md       # Proposal composition task (Organism)
|-- workflows/
|   |-- proposal-generation-pipeline.yaml  # Full end-to-end pipeline
|   |-- proposal-revision-flow.yaml        # Revision based on feedback
|-- config/
|   |-- coding-standards.md       # Code style and conventions
|   |-- tech-stack.md             # Technology stack reference
|   |-- source-tree.md            # This file
```


## Referência: references/squad/config/tech-stack.md

# Tech Stack — DealForge

## Runtime
- **Node.js** 20+ (LTS)

## AI / LLM
- **Claude API** (Sonnet/Opus) for prospect analysis, scope design and proposal composition
- **OpenAI API** (optional) for second-opinion scoring and win-rate validation

## Data Processing
- **JSON** for inter-agent communication and structured output
- **Markdown** for proposal composition and human-readable deliverables
- **zod** for schema validation

## Development
- **TypeScript** — Type safety for complex data pipelines
- **ESLint** + **Prettier** — Code formatting
- **Vitest** — Testing framework

## Output Formats
- Markdown (primary proposal format)
- JSON (machine-readable pipeline data)
- PDF (final client-facing deliverable via conversion)


## Referência: references/squad/squad.yaml

```yaml
name: win-proposal-deal
version: 1.0.0
description: "Propostas comerciais que fecham — 4 agentes IA analisam seu prospect, desenham 3 opcoes de escopo, precificam com win-rate preditivo e entregam proposta persuasiva pronta em minutos"
author: "Renato Medeiros <@Renat0z>"
license: MIT
slashPrefix: proposal

aios:
  minVersion: "2.1.0"
  type: squad

components:
  agents:
    - prospect-analyzer.md
    - scope-architect.md
    - pricing-strategist.md
    - proposal-composer.md
  tasks:
    - analyze-prospect.md
    - design-scope.md
    - calculate-pricing.md
    - compose-proposal.md
  workflows:
    - proposal-generation-pipeline.yaml
    - proposal-revision-flow.yaml
  checklists: []
  templates: []
  tools: []
  scripts: []

config:
  extends: none

dependencies:
  node: []
  squads: []

tags:
  - proposal
  - sales
  - win-rate
  - pricing
  - commercial
  - automation
  - closing
  - dealforge
  - agency
```


## Referência: references/squad/tasks/analyze-prospect.md

---
task: analyzeProspect()
responsavel: "ProspectAnalyzer"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: prospectData
    tipo: object
    descricao: "Dados do prospect: empresa, setor, tamanho, budget, dores, decisor, timeline"
    obrigatorio: true
  - nome: proposalHistory
    tipo: array<object>
    descricao: "Historico de propostas anteriores com resultados (win/loss/pending) e metadados"
    obrigatorio: false

Saida:
  - nome: prospectProfile
    tipo: file
    descricao: "prospect-profile.md — Perfil completo do prospect com scoring, dores priorizadas e objecoes mapeadas. Consumido por designScope() e calculatePricing()"
    obrigatorio: true
  - nome: historicalAnalysis
    tipo: file
    descricao: "historical-analysis.md — Analise de propostas similares, padroes de win/loss e win-rate previsto. Consumido por calculatePricing()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Dados minimos do prospect fornecidos: empresa, setor, pelo menos 1 dor"
    - "[ ] Budget declarado ou faixa estimada disponivel"
  post-conditions:
    - "[ ] prospect-profile.md gerado com scoring de qualificacao (1-10)"
    - "[ ] Pelo menos 3 dores mapeadas com urgencia e impacto"
    - "[ ] Objecoes provaveis identificadas com contra-argumentos"
    - "[ ] Win-rate previsto com intervalo de confianca"
    - "[ ] historical-analysis.md gerado com pelo menos 3 propostas similares referenciadas"

Performance:
  duration_expected: "1-3 minutos"
  cost_estimated: "~3000 tokens (Sonnet)"
  cacheable: true
  parallelizable: false
  skippable_when: "Nunca — analise do prospect e prerequisito para todo o pipeline"

Error Handling:
  strategy: retry
  retry:
    max_attempts: 2
    delay: "3s"
  fallback: "Se historico indisponivel, use benchmarks do setor como proxy"
---


## Referência: references/squad/tasks/calculate-pricing.md

---
task: calculatePricing()
responsavel: "PricingStrategist"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: prospectProfile
    tipo: file
    descricao: "analyzeProspect() output — budget e sensibilidade a preco"
    obrigatorio: true
  - nome: historicalAnalysis
    tipo: file
    descricao: "analyzeProspect() output — historico de conversao por faixa de preco"
    obrigatorio: true
  - nome: scopeDesign
    tipo: file
    descricao: "designScope() output — 3 versoes de escopo com horas estimadas"
    obrigatorio: true

Saida:
  - nome: pricingStrategy
    tipo: file
    descricao: "pricing-strategy.md — Precificacao por versao com custo base, margem, preco de venda, descontos condicionais e justificativa de valor. Consumido por composeProposal()"
    obrigatorio: true
  - nome: winRateAnalysis
    tipo: file
    descricao: "win-rate-analysis.md — Previsao de win-rate por versao/preco com variaveis consideradas e intervalo de confianca. Consumido por composeProposal()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] prospect-profile.md existe com budget e sensibilidade a preco"
    - "[ ] scope-design.md existe com 3 versoes e horas estimadas"
    - "[ ] historical-analysis.md existe com benchmarks de conversao"
  post-conditions:
    - "[ ] pricing-strategy.md contem preco para cada versao de escopo"
    - "[ ] Margem minima de 30% verificada para todas as versoes"
    - "[ ] Descontos condicionais definidos com regras claras"
    - "[ ] win-rate-analysis.md contem previsao para cada versao"
    - "[ ] Win-rate considera pelo menos 5 variaveis"
    - "[ ] Tabela comparativa das 3 versoes formatada"

Performance:
  duration_expected: "1-3 minutos"
  cost_estimated: "~3500 tokens (Opus)"
  cacheable: false
  parallelizable: false
  skippable_when: "Nunca — pricing e prerequisito para a proposta"

Error Handling:
  strategy: retry
  retry:
    max_attempts: 2
    delay: "3s"
  fallback: "Se historico insuficiente, use margem padrao de 40% e win-rate baseado em benchmarks do setor"
---


## Referência: references/squad/tasks/compose-proposal.md

---
task: composeProposal()
responsavel: "ProposalComposer"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: prospectProfile
    tipo: file
    descricao: "analyzeProspect() output — perfil e objecoes do prospect"
    obrigatorio: true
  - nome: scopeDesign
    tipo: file
    descricao: "designScope() output — 3 versoes de escopo detalhado"
    obrigatorio: true
  - nome: timeline
    tipo: file
    descricao: "designScope() output — cronograma com marcos"
    obrigatorio: true
  - nome: pricingStrategy
    tipo: file
    descricao: "calculatePricing() output — precificacao estrategica"
    obrigatorio: true
  - nome: winRateAnalysis
    tipo: file
    descricao: "calculatePricing() output — previsao de win-rate"
    obrigatorio: true

Saida:
  - nome: proposalFinal
    tipo: file
    descricao: "proposal-final.md — Proposta comercial completa, formatada e pronta para envio ao prospect"
    obrigatorio: true
  - nome: objectionPlaybook
    tipo: file
    descricao: "objection-playbook.md — Guia de objecoes com contra-argumentos para uso no follow-up"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] prospect-profile.md existe com objecoes mapeadas"
    - "[ ] scope-design.md existe com 3 versoes completas"
    - "[ ] timeline.md existe com marcos e dependencias"
    - "[ ] pricing-strategy.md existe com precos e justificativas"
    - "[ ] win-rate-analysis.md existe com previsoes"
  post-conditions:
    - "[ ] proposal-final.md contem todas as 10 secoes obrigatorias"
    - "[ ] Tom da proposta e adequado ao perfil do prospect"
    - "[ ] Versao recomendada destacada visualmente"
    - "[ ] Data de validade incluida (15-30 dias)"
    - "[ ] Call-to-action com proximo passo concreto"
    - "[ ] objection-playbook.md contem todas as objecoes com contra-argumentos"
    - "[ ] Zero jargao tecnico nao explicado"
    - "[ ] Win-rate previsto mencionado internamente (nao para o prospect)"

Performance:
  duration_expected: "3-5 minutos"
  cost_estimated: "~6000 tokens (Opus)"
  cacheable: false
  parallelizable: false
  skippable_when: "Nunca — proposta e o output final do pipeline"

Error Handling:
  strategy: retry
  retry:
    max_attempts: 2
    delay: "5s"
---


## Referência: references/squad/tasks/design-scope.md

---
task: designScope()
responsavel: "ScopeArchitect"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: prospectProfile
    tipo: file
    descricao: "analyzeProspect() output — perfil do prospect com dores priorizadas"
    obrigatorio: true
  - nome: historicalAnalysis
    tipo: file
    descricao: "analyzeProspect() output — propostas similares e padroes"
    obrigatorio: true

Saida:
  - nome: scopeDesign
    tipo: file
    descricao: "scope-design.md — Escopo detalhado com 3 versoes (essencial, recomendado, premium), entregaveis, marcos e criterios de aceite. Consumido por calculatePricing() e composeProposal()"
    obrigatorio: true
  - nome: timeline
    tipo: file
    descricao: "timeline.md — Cronograma com fases, dependencias, buffers e marcos de aceite. Consumido por composeProposal()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] prospect-profile.md existe com dores priorizadas"
    - "[ ] historical-analysis.md existe com benchmarks de escopo"
  post-conditions:
    - "[ ] scope-design.md contem 3 versoes de escopo (essencial, recomendado, premium)"
    - "[ ] Cada entregavel mapeia para pelo menos 1 dor do prospect"
    - "[ ] Horas estimadas por perfil (junior/pleno/senior) para cada entregavel"
    - "[ ] timeline.md contem fases com duracao, dependencias e marcos"
    - "[ ] Buffer de 15-20% incluido na timeline"
    - "[ ] Criterios de aceite mensuraveis para cada fase"

Performance:
  duration_expected: "2-4 minutos"
  cost_estimated: "~4000 tokens (Opus)"
  cacheable: false
  parallelizable: false
  skippable_when: "Nunca — escopo e prerequisito para pricing e proposta"

Error Handling:
  strategy: retry
  retry:
    max_attempts: 2
    delay: "5s"
---


## Referência: references/squad/workflows/proposal-generation-pipeline.yaml

```yaml
# Workflow: proposal_generation_pipeline (sequential pipeline pattern)
# Pipeline completo de geracao de propostas comerciais — 4 fases desde analise do prospect ate proposta final

workflow_name: proposal_generation_pipeline
description: "Pipeline completo de geracao de propostas comerciais com win-rate preditivo — analisa prospect, desenha escopo, precifica estrategicamente e compoe proposta persuasiva"

agent_sequence:
  - prospect-analyzer
  - scope-architect
  - pricing-strategist
  - proposal-composer

key_commands:
  - "*generate-proposal"
  - "*analyze-prospect"

trigger_threshold: 1
typical_duration: "5-12 minutes"

success_indicators:
  - "Proposta comercial completa gerada com 10 secoes obrigatorias"
  - "Win-rate preditivo calculado com intervalo de confianca"
  - "3 versoes de escopo com pricing estrategico"
  - "Objection playbook gerado com contra-argumentos prontos"

transitions:
  prospect_analyzed:
    trigger: "prospect profile generated with scoring and prioritized pain points"
    confidence: 0.90
    greeting_message: "Prospect analisado. Iniciando design de escopo."
    next_steps:
      - command: "*design-scope"
        description: "Design scope with deliverables, timeline and milestones"
        priority: 1

  scope_designed:
    trigger: "3 scope versions created with deliverables, timeline and acceptance criteria"
    confidence: 0.90
    greeting_message: "Escopo desenhado em 3 versoes. Iniciando precificacao estrategica."
    next_steps:
      - command: "*calculate-pricing"
        description: "Calculate strategic pricing with win-rate prediction"
        priority: 1

  pricing_calculated:
    trigger: "pricing strategy defined with margins, win-rate and conditional discounts"
    confidence: 0.90
    greeting_message: "Precificacao calculada. Iniciando composicao da proposta."
    next_steps:
      - command: "*compose-proposal"
        description: "Compose final commercial proposal with persuasive copy"
        priority: 1

  proposal_composed:
    trigger: "final proposal generated with all 10 sections and objection playbook"
    confidence: 0.95
    greeting_message: "Proposta comercial completa. Pronta para envio ao prospect."
    next_steps:
      - command: "*revise-proposal"
        description: "Revise proposal based on user feedback (optional)"
        priority: 2
```


## Referência: references/squad/workflows/proposal-revision-flow.yaml

```yaml
# Workflow: proposal_revision_flow (feedback loop pattern)
# Fluxo de revisao de proposta existente com base em feedback do usuario ou do prospect

workflow_name: proposal_revision_flow
description: "Fluxo de revisao e ajuste de proposta existente — recebe feedback, identifica ajustes necessarios em escopo/pricing/copy e recompoe a proposta"

agent_sequence:
  - scope-architect
  - pricing-strategist
  - proposal-composer

key_commands:
  - "*revise-proposal"

trigger_threshold: 1
typical_duration: "3-7 minutes"

success_indicators:
  - "Proposta revisada com ajustes aplicados"
  - "Win-rate recalculado apos ajustes"
  - "Objection playbook atualizado se necessario"

transitions:
  feedback_received:
    trigger: "user provides feedback on existing proposal"
    confidence: 0.85
    greeting_message: "Feedback recebido. Analisando ajustes necessarios."
    next_steps:
      - command: "*design-scope"
        description: "Adjust scope based on feedback if needed"
        priority: 1
      - command: "*calculate-pricing"
        description: "Recalculate pricing if scope changed"
        priority: 2

  scope_adjusted:
    trigger: "scope revised based on feedback"
    confidence: 0.85
    greeting_message: "Escopo ajustado. Recalculando precificacao."
    next_steps:
      - command: "*calculate-pricing"
        description: "Recalculate pricing for adjusted scope"
        priority: 1

  pricing_recalculated:
    trigger: "pricing recalculated for revised scope"
    confidence: 0.90
    greeting_message: "Pricing recalculado. Recompondo proposta."
    next_steps:
      - command: "*compose-proposal"
        description: "Recompose proposal with revisions applied"
        priority: 1

  revision_complete:
    trigger: "revised proposal generated with all adjustments applied"
    confidence: 0.95
    greeting_message: "Proposta revisada e pronta para reenvio."
    next_steps: []
```
