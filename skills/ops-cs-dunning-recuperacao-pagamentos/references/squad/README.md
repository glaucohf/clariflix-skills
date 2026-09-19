# Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

> Transforma falhas de pagamento em receita recuperada — sem depender de humano para perseguir cada inadimplente com a cadência e o tom certos.

**Área:** Operações & CS · **TopSquad:** O4 Back-Office Financeiro & Cobrança · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Pagamentos falhos (cartão expirado, saldo insuficiente, limite estourado) e inadimplência geram churn involuntário silencioso: o cliente nem queria sair, mas ninguém correu atrás com urgência, cadência e tom adequados. O time financeiro/CS dispara um email padrão e abandona. A taxa de recuperação manual gira em torno de 15-25% — deixando 75%+ de receita recuperável na mesa. O Dunning Agent executa sequências multicanal automáticas (email, WhatsApp, SMS) com timing calibrado por janela de tentativa de cobrança, tom progressivo por dia de atraso, regras de negociação (parcelamento, extensão, desconto de multa) por segmento e valor, e escalação HITL para negociação financeira real quando o valor ou a complexidade superam o threshold. Cada ação é registrada como task no ClickUp com prova de trabalho rastreável.

## Impacto esperado

Taxa de recuperacao de receita: de 15-25% (manual) para 55-70% em 90 dias com sequencias calibradas. Reducao de churn involuntario: 40-60% dos cancelamentos por falha de pagamento sao evitados quando a sequencia correta e executada. Dias ate recuperacao: de 15-30 dias (manual) para 3-7 dias com sequencia automatica de alta cadencia. Para uma base com 5% de inadimplencia mensal sobre MRR de R$200k: R$10k/mes em risco. Recuperar 60% = R$6k/mes preservados = R$72k ARR. ROI: payback em < 30 dias. Reducao de 80% do tempo do time financeiro/CS em follow-up manual de cobracas (de 15h/semana para < 3h).

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `cobalt` · Cobalt | Cobalt — Maestro de Recuperação de Receita | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `dante` · Dante | Dante — Sequencer de Cadência e Timing | L0 · worker determinístico | `calcular-sequencia-de-cobranca.md` |
| `iris` · Iris | Iris — Dispatcher de Email de Cobrança | L1 · worker autônomo | `enviar-email-de-recuperacao.md` |
| `zap` · Zap | Zap — Dispatchêr de WhatsApp Business | L1 · worker autônomo | `enviar-mensagens-personalizadas.md` |
| `flex` · Flex | Flex — Agente de Negociação e Classificação de Respostas | L2 · orquestra / decide | `classificar-respostas-cliente.md` |
| `pulse` · Pulse | Pulse — Dispatcher de SMS de Reforço | L0 · worker determinístico | `enviar-sms-de-reforco.md` |
| `atlas` · Atlas | Atlas — Analista de Performance e Padrões de Inadimplência | L2 · orquestra / decide | `analisar-padroes-de-inadimplencia.md` |
| `vault` · Vault | Vault — Agente de Atualização de Dados de Pagamento | L1 · worker autônomo | `atualizar-dados-de-pagamento.md` |
| `sentinel` · Sentinel | Sentinel — Critic de Compliance e Tom de Cobrança | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-dunning-recuperacao-pagamentos:cobalt` (ou instale via `npx squads add ./ops-cs-dunning-recuperacao-pagamentos`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-dunning-recuperacao-pagamentos-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes com menos de 3 meses de casa) — Flex classifica e cria task HITL urgente no ClickUp para o time financeiro com histórico completo e valor em risco
- Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar no gateway e no CRM, e responde ao cliente confirmando que um humano vai verificar em até X horas
- Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task de retenção para o CSM com contexto completo: cliente já estava em inadimplência + agora solicitou cancelamento = risco crítico combinado
- Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgente para o Head Financeiro e para o CSM responsável da conta, com sugestão de abordagem via chamada telefônica
- Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema no gateway de pagamento, no processador ou na infraestrutura (não é inadimplência — é incidente têcnico)
- Sentinel reprova uma mensagem por violação de compliance legal (CDC/LGPD) — bloqueia o disparo, notifica o Head Jurídico e o responsável de CS via Slack, e suspende o envio para todos os clientes no mesmo step até que o template seja revisado e re-aprovado
- Cliente com histórico de chargeback ou de fraude identificado pelo gateway — Cobalt bloqueia a sequência de dunning automática e cria task manual para o time financeiro gerenciar o caso diretamente (cobrança de fraude tem tratamento jurídico diferente de inadimplência comum)
- Bad debt confirmado (cobranca nao recuperada apos sequencia completa + tentativas manuais) — Cobalt fecha a sequencia como IRRECUPERAVEL, Atlas atualiza o cohort de bad debt, e cria task para o time juridico/financeiro avaliar encaminhamento para assessoria de cobranca ou baixa contabil

## KPIs

- Taxa de Recuperação de Receita: % do MRR em falha de pagamento que é recuperado dentro de 14 dias pelo squad vs baseline pre-implementação (meta: >= 55%, vs 15-25% manual)
- Reducao de Churn Involuntario: % de cancelamentos por falha de pagamento que sao prevenidos pelo squad vs baseline (meta: -40% a -60% de churn por inadimplencia)
- Dias Até Recuperação (MTTR): média de dias entre a falha de pagamento e o pagamento confirmado (meta: <= 5 dias, vs 15-30 dias manual)
- Taxa de Recuperação por Step da Sequência: distribuição de em qual step da sequência o pagamento é realizado (meta: >= 40% no step D0-D1 — quanto mais rápido, menor o custo e o risco de churn)
- Taxa de Prevenção por Cartão Expirado (Vault): % de falhas potenciais por cartão expirado evitadas pela comunicação proativa do Vault (meta: >= 60% dos cartões próximos de expiração atualizados antes da falha)
- Taxa de Aprovação do Critic Sentinel: % de mensagens aprovadas pelo Sentinel na primeira verificação sem bloqueio (meta: >= 95% — indica qualidade e compliance dos templates)
- Taxa de Resposta por Canal: % de clientes que respondem ou clicam no link de pagamento por canal (meta: WhatsApp >= 30%, Email >= 20%, SMS >= 10% — para calibração de prioridade de canal)
- Volume de HITL por Semana: numero de escalacoes para time humano por semana (meta: decrescente ao longo do tempo, com reducao de 30% em 60 dias por melhoria das regras de negociacao autonomas do Flex)
- MRR Recuperado por Real Investido: ROI do squad calculado mensalmente (meta: >= 5x — para cada R$1 investido no squad, R$5 em MRR recuperado)
- Taxa de Bad Debt: % do MRR que chega ao status IRRECUPERÁVEL após sequência completa (meta: monitorar tendência — redução indica que a segmentação de sequências está correta e o Flex está negociando bem antes do esgotamento)

## Integrações

- Gateway de Pagamento: Stripe (Payment Intents, Customer Portal, Account Updater, webhooks de falha em tempo real), Asaas, Iugu, Vindi ou PagSeguro — fonte primária de eventos de falha e endpoint de retry de cobrança
- WhatsApp Business API: 360dialog, Twilio ou Meta Cloud API direta — canal #1 de recuperação no Brasil, com gestão de templates HSM aprovados e janela de conversação de 24h
- Email: SendGrid ou Amazon SES — canal de cobrança formal com rastreamento de abertura, clique e resposta
- SMS: Twilio, Zenvia ou Sinch — canal de reforço para steps críticos de última chance
- ClickUp (Brain2 / MCP server) — hub de tasks de cobranca, prova de trabalho, historico de sequencias, HITL queue e registro de outcomes, espelhando arquitetura AIOX
- CRM: HubSpot ou Salesforce — dados de conta (MRR, segmento, CSM responsável, tempo de casa, histórico de pagamentos, contatos autorizados)
- Supabase / Postgres — estado das sequências de dunning, log de mensagens enviadas, histórico de tentativas de cobrança, negociações registradas, cohorts de inadimplentes e bad debt
- Langfuse — observabilidade OTEL, tracing de cada sequência de dunning, evals de qualidade das mensagens geradas pelo Flex, quality gates dev/staging/prod, rastreamento de custo por cobrança recuperada
- Claude Agent SDK / LangGraph — orquestração do workflow de recuperação com estado persistido, retry logic e gerenciamento de eventos assíncronos (resposta de cliente pode chegar horas depois)
- Slack — notificações HITL urgentes para time financeiro (negociação acima do threshold), alertas de spike de falhas para time técnico, relatório semanal de recuperação para Head Financeiro
- Plataforma de CS (ChurnZero, Custify, Gainsight) — integração bidirecional: leitura de segmento e health score do cliente para personalizar a abordagem, escrita de eventos de dunning no timeline do cliente para o CSM ter contexto completo

## Entregável (prova de trabalho)

Por evento de falha de pagamento: (1) Task no ClickUp criada automaticamente no momento da falha com dados completos da cobrança — cliente, valor, categoria de falha, sequência selecionada, canal priorizado — como ponto de entrada rastreável de toda a sequência; (2) Log completo no Supabase de cada mensagem enviada (canal, template, timestamp, status de entrega, leitura e resposta) e de cada tentativa de débito (timestamp, resultado, decline_code) — prova de trabalho auditável e rastreável por cobrança; (3) Registro de outcome final da cobrança (RECUPERADO_AUTOMÁTICO / RECUPERADO_NEGOCIAÇÃO / RECUPERADO_HITL / BAD_DEBT / CANCELAMENTO) com atribuição ao step e ao canal que converteu — para calibração contínua do Atlas. Por semana: relatório executivo de recuperação entregue no Slack do Head Financeiro com MRR recuperado, MRR em bad debt, breakdown por causa de falha, top-5 segmentos com maior taxa de inadimplência, performance de cada canal e recomendações de ajuste do playbook para a próxima semana. Por mês: análise de cohort de inadimplentes com identificação de clientes com padrão recorrente e recomendação de ações preventivas (mudança de data de cobrança, troca de método de pagamento, contato proativo do CSM).

## Bases gratuitas reutilizáveis (citadas na especificação)

- Incident Response Squad (5 ag) — base para o fluxo de deteccao e resposta a spikes de falha de pagamento do Atlas: logica de deteccao de anomalia estatistica, correlacao de eventos, escalacao estruturada e comunicacao de incidente para stakeholders; adaptar substituindo 'incidente de infra' por 'spike de falhas no gateway de pagamento'
- Skeptic Protocol (5 ag, red-team/QA) — base direta para o Critic Sentinel: estrutura adversarial de validação multi-dimensão com rubricas por categoria (compliance, tom, dados, frequência), lógica de bloqueio com feedback específico e registro de violações — adaptar as dimensões de validação para compliance de cobrança (CDC/LGPD) em vez de qualidade de código
- Data Quality Guardian (5 ag, qualidade de dados) — base para o pipeline de ingestão e validação do Vault e do Atlas: lógica de detecção de dados faltantes ou corrompidos (cartões sem data de expiração, emails inválidos, números de telefone mal formatados), validação de schema e alertas de qualidade antes que dados ruins cheguem ao Dispatcher e gerem falhas de entrega

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O4 · TopSquad de Back-Office Financeiro & Cobrança** — Fatura, reconcilia e recupera pagamento — com HITL em todo movimento financeiro.

- **Missão:** A operação financeira da empresa: faturamento, contas a pagar/receber, reconciliação bancária e a cobrança agêntica (dunning) que recupera pagamentos em atraso. Do faturar ao receber, em um motor só.
- **Por que consolidar:** Cobrança é a continuação natural do billing — a fatura emitida pelo back-office é exatamente a que o dunning persegue. Separados, duplicavam o conhecimento do estado da fatura. Unidos, o ciclo fatura → vencimento → cobrança → reconciliação é contínuo, com um único critic financeiro.
- **Squads irmãos:** Back-Office Financeiro (Reconciliação / AP-AR / Billing), Cobrança & Recuperação de Pagamentos (Dunning)

## Estrutura

```
ops-cs-dunning-recuperacao-pagamentos/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
