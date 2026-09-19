# Squad de Back-Office Financeiro (Reconciliacao / AP-AR / Billing)

> Planilha de reconciliacao e auditoria de confiabilidade zero: o squad faz o matching de transacoes, classifica exceptions e prepara os lancamentos — o humano so aprova o que o agente nao consegue resolver sozinho.

**Área:** Operações & CS · **TopSquad:** O4 Back-Office Financeiro & Cobrança · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Reconciliacao financeira e gestao de exceptions de billing sao executadas manualmente em planilhas Excel/Google Sheets por analistas financeiros. O processo tipico: exportar extratos bancarios, exportar registros do ERP/CRM, cruzar manualmente por VLOOKUP ou INDEX/MATCH, identificar divergencias, investigar cada exception individualmente, contatar fornecedores/clientes para clarificacao, registrar o tratamento e finalmente fechar o periodo. Em empresas com 500-5.000 transacoes/mes, esse ciclo consome 40-80h de analista por fechamento mensal, com taxa de erro humano de 2-5% (divergencias nao detectadas, lancamentos duplicados, exceptions mal classificadas). O atraso medio no fechamento contabil e de 5-10 dias uteis apos o fim do periodo. O squad Reconciliation/AP-AR faz o matching automatico de transacoes (banco vs. ERP/CRM vs. billing system), classifica e prioriza cada exception por tipo e impacto financeiro, investiga automaticamente as exceptions resolvtveis (valor fora de tolerancia, duplicata, timing difference), e prepara o package de fechamento com lancamentos contabeis prontos para revisao. Para exceptions que requerem decisao humana (credito acima de threshold, cancelamento de contrato, disputa formal), escalona com contexto completo para aprovacao HITL L3.

## Impacto esperado

Reducao do ciclo de fechamento de 5-10 dias uteis para 1-2 dias uteis (70-80% de reducao). Taxa de transacoes auto-reconciliadas meta: 85-92% (empresas com processos mais padronizados atingem 95%+). Reducao de exceptions nao detectadas: de 2-5% para < 0.3% (o agente nao se cansa nem pula linha). Economia direta: analista financeiro senior (R$8.000-15.000/mes) libera 60-70% do tempo de reconciliacao para analise estrategica. Em volumes de 2.000 transacoes/mes: R$6.000-10.000/mes em horas salvas + reducao de multas por atraso no fechamento. ROI tipico: 4-8x o custo do squad em 6 meses. Impacto indireto: auditoria simplificada (trilha de audit completa por transacao), compliance automatico com politicas de AP (prazo de pagamento, aprovacoes por valor), reducao de litigios com fornecedores por divergencias nao resolvidas.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro-caixa` · Maestro Caixa | Maestro Caixa — O Controlador do Ciclo de Fechamento | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `fluxo` · Fluxo | Fluxo — O Extrator e Normalizador de Transacoes | L0 · worker determinístico | `extrair-e-normalizar-transacoes.md` |
| `nexus` · Nexus | Nexus — O Matcher de Transacoes | L1 · worker autônomo | `cruzar-transacoes.md` |
| `iris` · Iris | Iris — A Classificadora de Exceptions | L1 · worker autônomo | `classificar-exceptions.md` |
| `solano` · Solano | Solano — O Investigador de Exceptions | L2 · orquestra / decide | `investigar-exceptions-automaticamente.md` |
| `ledger` · Ledger | Ledger — O Preparador do Closing Package | L1 · worker autônomo | `preparar-closing-package.md` |
| `aurum` · Aurum | Aurum — O Verificador de Qualidade Financeira | L1 · worker autônomo | `verificar-qualidade-financeira.md` |
| `dunna` · Dunna | Dunna — A Gestora de AP-AR e Cobranca | L2 · orquestra / decide | `gerar-aging-analysis-automatica.md` |
| `aurum-2` · Aurum 2 | Aurum — O Verificador de Qualidade Financeira | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-back-office-financeiro-reconciliacao:maestro-caixa` (ou instale via `npx squads add ./ops-cs-back-office-financeiro-reconciliacao`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-back-office-financeiro-reconciliacao-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Lancamentos contabeis acima do threshold de aprovacao autonoma: qualquer lancamento (de reconciliacao automatica ou de resolucao de exception) acima do valor configurado (ex: R$10.000 por lancamento, configuravel por cliente) requer aprovacao explicita do Controller via task no ClickUp. O Ledger gera o lancamento formatado e o Aurum escala para HITL com contexto completo (origem, evidencia, impact no resultado).
- L3 — Exceptions classificadas como DISPUTED_CHARGE ou BILLING_DISCREPANCY de alto valor: qualquer disputa formal com fornecedor/cliente ou divergencia de billing acima do threshold configurado requer decisao humana. O Solano prepara o dossie de investigacao completo (evidencias, historico, opcoes de resolucao com pros/contras) para o Controller tomar a decisao.
- L3 — Closing Package com veredicto BLOCKED do Aurum: quando o Aurum bloqueia o Closing Package (inconsistencia matematica, violacao de compliance, exceptions acima do threshold de fechamento), o Maestro Caixa cria task urgente no ClickUp com lista priorizada de problemas e acoes corretivas. Nenhum fechamento ocorre sem resolucao dos blocking issues.
- L3 — Pagamentos (AP): a Dunna gera a fila de pagamentos aprovados e o dossie de cada pagamento, mas a execucao NUNCA e automatica. Todo pagamento requer aprovacao humana explicita (Controller ou Financeiro, conforme alçada configurada) via task no ClickUp com o botao de aprovacao integrado ao ERP.
- L2 — Matches de baixa confianca (score 0.70-0.85): o Aurum sinaliza esses matches no Verification Report para confirmacao do analista antes do Closing Package ser finalizado. Nao bloqueia o processo, mas exige confirmacao explicita de cada match de baixa confianca acima de R$500 (configuravel).
- L2 — Comunicacoes de cobranca (AR): a Dunna prepara os templates de cobranca mas a aprovacao depende do tier: para clientes estrategicos (acima de determinado ARR ou marcados como VIP no CRM), toda comunicacao requer aprovacao humana antes do envio. Para clientes standard, a sequencia pode ser aprovada em batch semanalmente.
- L1 — Revisao do Exception Playbook trimestral: analista financeiro revisa as regras de classificacao e os thresholds de tolerancia calibrados pelo squad, podendo ajustar parametros. Nao bloqueia operacao continua, mas garante que o playbook evolui com as mudancas no negocio do cliente.

## KPIs

- Taxa de auto-reconciliacao: % de transacoes do periodo reconciliadas automaticamente sem intervencao humana (meta: 85-92% em 90 dias; baseline tipico do cliente: 0% — tudo manual)
- Tempo de fechamento: dias uteis entre fim do periodo e Closing Package aprovado (meta: 1-2 dias uteis; baseline tipico: 5-10 dias uteis)
- Exceptions resolvidas automaticamente: % de exceptions classificadas pelo Iris que foram resolvidas pelo Solano sem HITL (meta: 60-75% das exceptions por volume; exceptions de alto valor sempre HITL)
- Precisao do matching: % de matches automaticos confirmados como corretos pelo Controller na revisao do Closing Package (meta: > 99.5% para exact match; > 97% para fuzzy match; > 92% para probabilistic match)
- Falsos positivos de exceptions: % de transacoes erroneamente classificadas como exception quando eram match valido (meta: < 1%)
- Valor em exceptions residuais: R$ total em exceptions abertas (nao resolvidas) ao fechar o periodo, como % do volume total do periodo (meta: < 0.5% do valor total)
- SLA de aprovacao HITL: % de tasks HITL L3 respondidas dentro do SLA configurado (meta: > 90% de aprovacoes em < 4h uteis; pagamentos urgentes em < 1h uteis)
- Reducao de divergencias nao detectadas: numero de lancamentos incorretos identificados na auditoria externa ou no proximo ciclo que escaparam do squad (meta: zero divergencias acima de R$100 nao detectadas pelo Aurum)
- Custo por transacao reconciliada: custo total do squad (infra + tokens) dividido pelo numero de transacoes processadas (meta: < R$0,50/transacao em volumes de 2.000+/mes)

## Integrações

- ERP (SAP / Omie / Conta Azul / Totvs / Netsuite) — fonte primaria de lancamentos contabeis: API de leitura para extrair transacoes, NFs, contratos, saldos de AP e AR; API de escrita para importacao de journal entries aprovados (somente apos HITL); acesso ao plano de contas
- Bancos via Open Finance / OFX / API Bancaria (Bradesco, Itau, Banco do Brasil, Nubank Business, BTG, Inter) — extrato bancario automatizado diario ou mensal; integracao via Open Finance API (BACEN) para bancos disponiveis ou exportacao OFX para os demais
- Billing Systems (Stripe / Chargebee / Vindi / Iugu / Hotmart / Eduzz) — historico de cobranças, assinaturas, mudancas de plano, descontos, estornos, webhooks de eventos de pagamento em tempo real
- ClickUp (Brain2 / Super Agents / Autopilot Agents + MCP) — hub de tasks e prova de trabalho: task por excecao HITL L3, Closing Package como task de aprovacao click-to-approve, filas de AP e AR como tasks com due date, integracao com AIOX espelhando o workflow de aprovacao
- Slack — notificacoes em tempo real: alerta de Closing Package pronto para aprovacao, exceptions de alto valor detectadas, pagamentos vencendo hoje sem aprovacao, Closing Readiness Score no canal #financeiro
- CRM (HubSpot / Salesforce / Pipedrive) — dados de conta do cliente para AR: historico de relacionamento, tier do cliente, health score, open tickets de suporte (contexto para cobranca empatetica)
- CS Platforms (ChurnZero / Custify / Chargebee / Gainsight) — health score para priorizacao de cobranca: clientes em risco de churn recebem abordagem diferente de cobranca (empatetica, com oferta de renegociacao) vs. clientes saudaveis
- WhatsApp Business API — canal de cobranca AR: envio de lembretes de vencimento e comunicacoes de cobranca na sequencia configurada pela Dunna, com templates pre-aprovados pela politica de cobranca
- Supabase / Postgres — estado do squad: Canonical Transaction Set, Exception Queue, status de cada ciclo de fechamento, historico de matches e exceptions, Closing Packages gerados e aprovados
- Langfuse — observabilidade OTEL: tracing de cada ciclo de reconciliacao (source collection -> matching -> exception classification -> investigation -> closing package -> approval), evals por tipo de match e exception, quality gates (dev 70% / staging 85% / prod 95% de precisao de matching)
- Claude Agent SDK / LangGraph — orquestracao multi-agente do ciclo de reconciliacao, state management do ciclo de fechamento, embedding similarity para matching probabilistico de descricoes de transacoes
- MCP Servers (camada de integracao universal) — ClickUp MCP, Supabase MCP para acesso padronizado; integracao com bancos via MCP customizado de Open Finance

## Entregável (prova de trabalho)

Closing Package no ClickUp como prova de trabalho verificavel por ciclo de fechamento: (1) Reconciliation Statement por conta bancaria (saldo extrato vs. saldo ERP + itens conciliantes + saldo ajustado — formato auditavel), (2) Journal Entry Batch no formato do ERP do cliente (pronto para importacao click-to-approve), (3) Exception Log completo (cada exception com tipo, valor, investigacao do Solano, resolucao aplicada ou pendente, audit trail), (4) Closing Readiness Score com breakdown por dimensao, (5) Verification Report do Aurum (veredicto e flags), (6) AP-AR Status Report da Dunna (pagamentos pendentes de aprovacao, cobrancas enviadas na semana, titulos em risco). Cada lancamento rastreavel de volta a transacao de origem via audit trail imutavel. Task no ClickUp por exception HITL L3 com dossie de investigacao completo e botao de aprovacao integrado ao ERP.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 ag, squads.sh) — arquitetura de validacao multi-dimensional e anomaly detection diretamente reutilizavel pelo Aurum e pelo Nexus. O pipeline de schema validation, null rate monitoring e consistency checks do DQG e a base do gate de qualidade do Aurum (5 dimensoes de validacao do Closing Package) e do matching probabilistico do Nexus.
- Skeptic Protocol (5 ag, red-team/QA, myclaude) — padrao de critic/verifier adversarial com multi-dimensao de validacao adaptado para o Aurum. O protocolo de verificacao em camadas (assume que esta errado ate provar o contrario) e o modelo de veredicto estruturado (APPROVED / APPROVED_WITH_FLAGS / BLOCKED) espelham diretamente o Skeptic Protocol.
- Incident Response Squad (5 ag, squads.sh) — o padrao de deteccao -> classificacao -> investigacao -> resolucao -> documentacao do Incident Response Squad e estruturalmente identico ao pipeline de exceptions do squad financeiro (Iris classifica, Solano investiga, Ledger documenta, HITL resolve o que e P1-P2). Reutilizar o modelo de severity (P1-P4), o escalation flow e o post-mortem como base do Exception Log.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O4 · TopSquad de Back-Office Financeiro & Cobrança** — Fatura, reconcilia e recupera pagamento — com HITL em todo movimento financeiro.

- **Missão:** A operação financeira da empresa: faturamento, contas a pagar/receber, reconciliação bancária e a cobrança agêntica (dunning) que recupera pagamentos em atraso. Do faturar ao receber, em um motor só.
- **Por que consolidar:** Cobrança é a continuação natural do billing — a fatura emitida pelo back-office é exatamente a que o dunning persegue. Separados, duplicavam o conhecimento do estado da fatura. Unidos, o ciclo fatura → vencimento → cobrança → reconciliação é contínuo, com um único critic financeiro.
- **Squads irmãos:** Back-Office Financeiro (Reconciliação / AP-AR / Billing), Cobrança & Recuperação de Pagamentos (Dunning)

## Estrutura

```
ops-cs-back-office-financeiro-reconciliacao/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
