# Handoff Orchestrator HITL

> Nenhuma ação irreversível sem aprovação humana — e nenhum humano sobrecarregado com trivialidades.

**Área:** Operações & CS · **TopSquad:** O1 Atendimento & Suporte Conversacional · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Agentes de IA erram por dois extremos opostos: escalam de menos (decidem autonomamente em casos críticos, causando dano financeiro ou legal irreversível) ou de mais (entopem o humano com aprovações desnecessárias, destruindo a eficiência prometida pela automação). O Handoff Orchestrator resolve isso aplicando uma matriz binária criticidade x reversibilidade: toda ação é classificada em um tier de autonomia (L0 a L3) antes de ser executada. Ações reversíveis e de baixo impacto rodam autônomas. Ações irreversíveis, com gasto financeiro, envio externo ou risco legal vão obrigatoriamente para L3 — o humano recebe contexto empacotado e decide em segundos, não em minutos. Resultado mensurável: zero ações irreversíveis sem aprovação + redução de 60-80% nos handoffs desnecessários.

## Impacto esperado

ROI estimado em 90 dias: (1) Reducao de 70% no volume de escalonamentos humanos em suporte (baseline: 40% das interacoes escalam hoje, meta: 12%), liberando 2-4 FTEs para trabalho de alto valor. (2) Zero incidentes de acao autonoma irreversivel — elimina reembolsos indevidos, alteracoes contratuais nao autorizadas e envios de dados sensíveis sem aprovacao. (3) Tempo medio de resolucao de handoff L3 cai de 4h para 8min (contexto pre-empacotado). (4) NPS de atendimento +18 pontos por reducao de escalacoes internas desnecessarias. Payback estimado: 45-60 dias para empresas com >500 tickets/mes.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `hieronimus` · Hieronimus | Hieronimus — O Juiz de Fronteira | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `cassio` · Cassio | Cássio — Classificador de Criticidade | L1 · worker autônomo | `classificar-criticidade.md` |
| `beatriz` · Beatriz | Beatriz — Empacotadora de Contexto | L1 · worker autônomo | `empacotar-contexto.md` |
| `renato` · Renato | Renato — Monitor de SLA e Escalonamento | L0 · worker determinístico | `monitorar-handoffs-l3.md` |
| `selene` · Selene | Selêne — Analista de Padrão de Falso Positivo | L2 · orquestra / decide | `analisar-falso-positivo.md` |
| `dora` · Dora | Dora — Roteadora de Canal e Responsável | L0 · worker determinístico | `determinar-canal-enviado.md` |
| `fabio` · Fabio | Fábio — Agente de Feedback Loop | L1 · worker autônomo | `registrar-decisao-humana.md` |
| `vitor` · Vitor | Vitor — Auditor da Matriz de Autonomia | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-handoff-orchestrator-hitl:hieronimus` (ou instale via `npx squads add ./ops-cs-handoff-orchestrator-hitl`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-handoff-orchestrator-hitl-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — humano aprova antes de qualquer execução, sem exceção.
- L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assinado, alteração de cláusula contratual, bloqueio/banimento de usuário.
- L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qualquer comunicação que mencione termos legais ou rescisão.
- L3 obrigatório: toda ação de impacto reputacional alto — publicação de resposta pública em canal externo (redes sociais, review sites), comunicados de crise, respostas à imprensa.
- Aprovação humana para recalibração da matriz (output do Selene): nenhum threshold de autonomia é alterado sem validação do supervisor CS ou gerente de operações.
- Revisão humana quinzenal do Relatório de Auditoria do Vitor: supervisor CS assina o score de qualidade e valida as correções propostas.
- Gate humano na primeira semana pos-implantacao: humano revisa 100% das classificacoes (nao apenas L3) para construir confianca na matriz antes de operar em modo autonomo.

## KPIs

- Taxa de ações irreversíveis sem aprovação L3: meta ZERO (tolerância zero, alerta P0 se >0)
- Taxa de handoffs desnecessários (falso positivo L3): meta <10% (baseline estimado: 35-50% nos sistemas atuais)
- Tempo médio de resolução de handoff L3: meta <8 minutos para urgentes, <2h para normais (baseline: 4h+)
- Taxa de acerto da classificação Cassio (validada pelo Vitor): meta >92% na auditoria semanal
- Cobertura de prova de trabalho no ClickUp: meta 100% das decisões L3 registradas como task com decisor e timestamp
- SLA compliance de notificação: meta 100% dos handoffs L3 notificados em <2 minutos após classificação
- Score de qualidade Vitor: meta >85/100 na auditoria quinzenal (abre plano de ação se <80)
- Volume de handoffs por tier (distribuição saudável): L0 >60%, L1 20-25%, L2 10-15%, L3 <8% do total de ações

## Integrações

- ClickUp (Brain2/Autopilot Agents) — hub de tasks, prova de trabalho, registro de cada decisão de handoff como task com checklist, espelho do AIOX
- Claude Agent SDK + LangGraph — orquestração multi-agente, grafo de decisão do Hieronimus, estados de handoff
- Langfuse — observabilidade OTEL completa, tracing de cada classificação, dashboard de KPIs, quality gates (dev 70% / staging 85% / prod 95%)
- Supabase/Postgres — estado persistente dos handoffs abertos, log de decisões, banco de treinamento da matriz, histórico de feedbacks
- Slack (Webhooks + Workflow Builder) — canal #hitl-approvals para briefings L3, botões de ação direta (Aprovar/Rejeitar/Modificar), lembretes de SLA
- Zendesk / Intercom — webhook de interceptação de ações antes da execução, registro de decisões em tickets, integração com filas de atendimento
- WhatsApp Business API — interceptação de ações de alto risco iniciadas em atendimentos via WhatsApp antes do envio
- HubSpot / Salesforce — contexto do cliente (LTV, tier, histórico de contratos, health score) para enriquecer classificação de criticidade
- MCP Servers (camada universal) — ClickUp MCP, CRM MCP, helpdesk MCP para acesso unificado sem hardcode de API keys

## Entregável (prova de trabalho)

Artefato central — Decisão de Handoff Registrada: cada interação do squad gera uma task no ClickUp com: (1) action_id único, (2) tier atribuído com justificativa, (3) briefing de contexto empacotado, (4) quem recebeu o handoff e quando, (5) decisão tomada (aprovado/rejeitado/modificado) com timestamp, (6) tempo de resolução, (7) feedback de qualidade da classificação. Dashboard semanal: Relatório de Saúde da Matriz com distribuição de tiers, taxa de acerto, volume de handoffs por tipo, SLA compliance e proposta de recalibração.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (5 ag, red-team/QA) — base direta para o Crític Vitor: arquitetura de auditoria adversarial e amostragem estratificada reutilizável como blueprint do loop de verificação da matriz.
- Incident Response Squad (5 ag) — base para o Renato (Monitor de SLA): lógica de escalonamento progressivo, cadeia de notificação e fallback de responsável já implementada, adaptável para handoffs L3.
- Five Vitals (diagnóstico de sistemas) — base para o Selene (Analista de Padrão): estrutura de detecção de anomalia e proposta de correção com evidências reutilizável para o loop de recalibração da matriz.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O1 · TopSquad de Atendimento & Suporte Conversacional** — Resolve, tria, escala e assiste — toda a linha de frente em um cérebro só.

- **Missão:** A linha de frente inteira: resolve o Tier-1 em texto e voz (PT-BR), tria e prioriza tickets, decide quando escalar para humano (handoff) e assiste o agente humano quando ele assume. Um único cérebro de atendimento, multicanal.
- **Por que consolidar:** Os cinco vivem na mesma conversa do cliente — só atuam em momentos diferentes (resolver, triar, escalar, assistir). Mantê-los separados quebrava o contexto a cada passagem de bastão. Unidos, a conversa flui do bot ao humano e de volta sem reiniciar, com triagem e copiloto compartilhando o mesmo estado.
- **Squads irmãos:** Suporte Conversacional Multicanal (Tier-1), Voz-IA para Atendimento Telefônico (PT-BR), Triagem, Roteamento e Priorização de Tickets, Handoff Orchestrator HITL, Copiloto do Agente Humano

## Estrutura

```
ops-cs-handoff-orchestrator-hitl/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
