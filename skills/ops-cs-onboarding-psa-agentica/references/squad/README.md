# Squad de Onboarding & Implementação (PSA Agêntica)

> De SOW assinado a cliente com valor entregue em metade do tempo — sem plano de projeto manual, sem marco perdido, sem churn precoce.

**Área:** Operações & CS · **TopSquad:** O3 Customer Success: Onboarding, Retenção & Expansão · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Onboarding lento e desorganizado é a principal causa de churn nos primeiros 90 dias. Planos de implementação são montados à mão por CSMs sobrecarregados, o acompanhamento de delivery é reativo e alertas de risco chegam tarde. O squad PSA Agêntica transforma SOW e calls de kickoff em plano de projeto estruturado automaticamente, monitora cada marco no ClickUp em tempo real e aciona alertas preditivos antes que o atraso se materialize — reduzindo time-to-value (TTV) em ~40%, elevando a taxa de onboardings no prazo de ~55% para >85% e cortando o churn 0-90 dias em 25-35%.

## Impacto esperado

ROI estimado para o cliente: CSM ganha 8-12h/semana (de montagem manual de planos + follow-ups reativos); redução de churn 0-90 dias de 25-35% equivale a ~15-25% de aumento na receita recorrente retida; time-to-value cai de 45-60 dias para 25-35 dias, acelerando expansão e referências. Para a consultoria: prova de trabalho tangível (plano gerado + dashboard de delivery) viabiliza upsell do squad como produto recorrente após o Diagnóstico Lendária.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro` · Maestro | Maestro — Orquestrador PSA | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `atlas` · Átlas | Átlas — Arquiteto de Projeto | L2 · orquestra / decide | `criar-plano-de-implementacao.md` |
| `cassandra` · Cassandra | Cassandra — Agente de Risco e Monitoramento | L2 · orquestra / decide | `monitorar-desvios-de-cronograma.md` |
| `hermes` · Hermes | Hermes — Agente de Comunicação e Notificações | L2 · orquestra / decide | `enviar-mensagens-contextualizadas.md` |
| `iris` · Iris | Iris — Agente de Ingestão e Parsing de SOW | L1 · worker autônomo | `processar-documentos-sow.md` |
| `vitor` · Vitor | Vitor — Agente de Health Score e Churn Prevention | L2 · orquestra / decide | `calcular-health-score-cliente.md` |
| `crono` · Crono | Crono — Agente de Relatório de Delivery | L2 · orquestra / decide | `gerar-relatorio-de-delivery.md` |
| `argus` · Argus | Argus — Crítico de Qualidade e Completude | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-onboarding-psa-agentica:maestro` (ou instale via `npx squads add ./ops-cs-onboarding-psa-agentica`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-onboarding-psa-agentica-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)
- Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)
- Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro
- Aprovação do Delivery Status Report semanal antes do envio ao cliente
- Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente
- Decisão de go/no-go para go-live quando health score < 60 ou mais de 2 marcos críticos em Red

## KPIs

- Time-to-Value (TTV): redução de 45-60 dias para 25-35 dias (meta: -40%)
- % de onboardings concluídos no prazo: de ~55% para >85%
- Churn 0-90 dias: redução de 25-35% vs. baseline
- Tempo de criação do plano de projeto: de 4-8h (manual) para <30min (automatizado)
- Taxa de marcos em Red no momento do alerta: >80% detectados com >=3 dias de antecedência
- Health Score médio no dia 30 de onboarding: >65/100
- Taxa de aprovação do plano sem revisão maior: >70% (qualidade do Átlas)
- NPS de onboarding (pesquisa ao final do processo): aumento de 15+ pontos vs. baseline

## Integrações

- ClickUp (MCP nativo) — hub de tasks, marcos, status e prova de trabalho; espelha estrutura AIOX
- CRM (HubSpot ou Salesforce via MCP) — webhook de deal closed-won para trigger de onboarding; dados de conta e contatos
- WhatsApp Business API — notificações proativas e follow-ups de pendências do cliente
- Slack — alertas internos, notificações de risco, aprovações HITL via workflow de aprovação
- Google Drive / Notion — ingestão de SOW e documentos de kickoff via connector ou URL
- Calendário (Google Calendar / Outlook via MCP) — leitura de calls agendadas para trigger de relatório pré-reunião
- Produto SaaS do cliente (API de uso) — dados de engajamento e ativação para health score
- Supabase / Postgres — estado dos agentes, histórico de onboardings, health scores, risk matrix
- Langfuse — observabilidade OTEL, tracing de chamadas, quality gates (dev 70% / staging 85% / prod 95%)
- Email (SMTP/SendGrid) — envio de relatórios de delivery e notificações formais
- Rocketlane (referência de arquitetura PSA) — benchmark de fluxo de onboarding e estrutura de portal do cliente

## Entregável (prova de trabalho)

Plano de projeto estruturado publicado no ClickUp (com fases, marcos, tasks, owners e critérios de aceite) + Delivery Status Report semanal com semáforo RAG + Health Score Report dos primeiros 90 dias + Log de alertas e ações tomadas. Prova de trabalho: dashboard de delivery público para o cliente com % de conclusão em tempo real e histórico de status por marco.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Incident Response Squad (5 ag) — arquitetura de detecção de anomalia, escalação graduada e loop de resolução reutilizável para o módulo de alertas do Cassandra
- Skeptic Protocol (5 ag) — lógica de red-team e checklist de validação aproveitada diretamente pelo Argus para auditoria de planos e relatórios
- Five Vitals (diagnóstico de sistemas) — framework de health score multi-dimensional adaptável ao Vitor para calcular saúde do cliente por dimensão com pesos configuráveis

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O3 · TopSquad de Customer Success: Onboarding, Retenção & Expansão** — O ciclo de vida pós-venda inteiro: ativar, reter, expandir.

- **Missão:** O squad do cliente após a venda: conduz o onboarding/implementação, prevê e previne churn ao longo da vida, e automatiza renovação, expansão e QBRs. Ativar → reter → expandir em um motor único de Customer Success.
- **Por que consolidar:** É a mesma jornada do cliente em três fases — ativar, manter, crescer — e os sinais fluem entre elas: um onboarding fraco prevê churn, que (evitado) abre expansão. Separados, o sinal de saúde vivia em silos; unidos, o health score atravessa todo o ciclo de vida.
- **Squads irmãos:** Onboarding & Implementação (PSA Agêntica), Predição & Prevenção de Churn, Renovação, Expansão & QBR Automatizado

## Estrutura

```
ops-cs-onboarding-psa-agentica/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
