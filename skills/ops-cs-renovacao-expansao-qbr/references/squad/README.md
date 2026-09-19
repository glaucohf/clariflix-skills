# Squad de Renovacao, Expansao e QBR Automatizado

> Nenhuma renovacao chega de surpresa e nenhuma oportunidade de expansao passa batida — o CSM entra na conversa com o brief pronto, os sinais na mao e o timing certo.

**Área:** Operações & CS · **TopSquad:** O3 Customer Success: Onboarding, Retenção & Expansão · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

O CSM nao tem tempo de preparar QBR nem cruzar sinais de uso com sentimento e marcos comerciais antes de uma renovacao ou reuniao de expansao. O resultado: renovacoes negociadas no desespero de ultimo minuto (sem evidencia de valor entregue), upsell oportunistico substituindo expansao consultiva, e QBRs conduzidos de memoria ou com slides genericos que nao refletem o que o cliente realmente usou. O squad agrega automaticamente dados de uso do produto, sentimento (NPS/CSAT/verbatims), marcos de entrega, consumo de features premium e sinais de expansao (aumento de usuarios ativos, uso de integracao enterprise, ticket de pedido de feature paga) para gerar o QBR Brief, o Expansion Signal Report e o Renewal Readiness Score por conta — entregues no ClickUp para o CSM com antecedencia minima de 30 dias antes de cada data-chave.

## Impacto esperado

NRR (Net Revenue Retention) aumentado de 95-105% para 115-125% em 12 meses com o squad ativo: combinacao de churn reduzido (brief de renovacao com evidencia de valor aumenta taxa de retencao em 20-30%) e expansao proativa identificada (sinais de upsell capturados resultam em 15-25% mais contas expandindo antes da renovacao). Para uma base de 150 contas com ARR medio de R$60k: 10 expansoes adicionais de R$18k cada = R$180k ARR incremental/ano; retencao de 8 contas que churnariam = R$480k ARR protegido/ano. Total: R$660k ARR de impacto no primeiro ano. ROI do squad: payback em 60-90 dias. Reducao de 70% no tempo de preparacao de QBR (de 6-8h para < 90 minutos por conta). 100% de renovacoes com brief pronto 30 dias antes vs 0% sem o squad.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro` · Maestro | Maestro — Orchestrator de Renovacao e Expansao | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `radar` · Radar | Radar — Sensor de Janelas de Renovacao e Sinais de Expansao | L0 · worker determinístico | `detectar-sinais-de-expansao.md` |
| `compass` · Compass | Compass — Calculador de Renewal Readiness Score | L0 · worker determinístico | `calcular-renewal-readiness-score.md` |
| `scout` · Scout | Scout — Analista de Propensao a Expansao | L1 · worker autônomo | `analisar-propensao-a-expansao.md` |
| `briefer` · Briefer | Briefer — Gerador de QBR Brief e Renewal Package | L1 · worker autônomo | `gerar-qbr-brief-e-renewal-package.md` |
| `slides` · Slides | Slides — Agente de Deck de QBR | L2 · orquestra / decide | `gerar-deck-de-apresentacao.md` |
| `pulse` · Pulse | Pulse — Agente de Ativacao e Orquestracao de Tarefas | L2 · orquestra / decide | `criar-pacote-de-renovacao.md` |
| `memory` · Memory | Memory — Arquivista de Resultados e Historico de Conta | L1 · worker autônomo | `arquivar-resultados-qbr.md` |
| `verity` · Verity | Verity — Critic de Evidencia e Proporcionalidade | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-renovacao-expansao-qbr:maestro` (ou instale via `npx squads add ./ops-cs-renovacao-expansao-qbr`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-renovacao-expansao-qbr-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de expansao com status 'Aguardando Aprovacao do CSM/Manager' antes de incluir a proposta no deck final para o cliente
- Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CSM (deck e gerado, nunca enviado automaticamente ao cliente)
- Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar qualquer contato de renovacao
- Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de entrada antes de reprocessar
- Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer alinhamento com equipe comercial (AE ou CSM sênior) antes de abordar o cliente
- Comprometimento pendente do fornecedor detectado pelo Memory como nao entregue no periodo anterior — brief inclui o item mas Pulse cria subtask de 'Resolucao de Compromisso Pendente' que requer confirmacao do CSM de que foi resolvido antes de marcar como pronto para QBR
- Conta com Renewal Readiness Score CRITICO (< 50) e renovacao em < 30 dias — escalacao imediata para Head de CS e Account Executive senior com brief de situacao de emergencia; qualquer acao sobre conta fica subordinada a aprovacao do Head de CS
- Feedback de Memory indicando que CSM fez edicao significativa no deck (> 30% do conteudo alterado) — Maestro abre HITL para CSM documentar o motivo da edicao e calibrar o Briefer para futuras geracoes

## KPIs

- NRR (Net Revenue Retention): variacao percentual do NRR mes a mes na base monitorada vs baseline dos 12 meses anteriores (meta: de 100-105% para 115-125% em 12 meses)
- % de Renovacoes com Brief Pronto: percentual de renovacoes que chegam com QBR Brief e Renewal Package gerados pelo squad pelo menos 30 dias antes da data (meta: >= 95% da base monitorada)
- Taxa de Renovacao sem Atrito: % de renovacoes concluidas dentro do prazo esperado sem negociacao reativa de desconto ou extensao de emergencia (meta: > 80% das renovacoes monitoradas)
- Expansion Pipeline Identificado: ARR de oportunidades de expansao qualificadas pelo Scout no mes vs ARR de expansoes efetivamente realizadas (meta: taxa de conversao >= 25% das oportunidades qualificadas)
- Tempo de Preparacao de QBR pelo CSM: horas gastas pelo CSM preparando QBR sem apoio do squad vs com o squad (meta: < 90 minutos de revisao e personalizacao, reducao de 70% vs baseline de 6-8h)
- Score de Avaliacao do Brief pelo CSM: media das avaliacoes de qualidade que CSMs dao ao brief e deck gerados (escala 1-5 coletada no ClickUp) (meta: media >= 4.2)
- Critic Approval Rate: % de briefs aprovados pelo Verity na primeira iteracao sem devolucao ao Briefer (meta: >= 80%)
- Lead Time de Deteccao de Expansao: media de dias entre o sinal de expansao detectado pelo Radar e a conversa de expansao iniciada pelo CSM (meta: <= 14 dias apos deteccao do sinal)
- MRR Incremental de Expansao Atribuivel: soma do MRR de expansoes onde o brief do Scout foi utilizado como base da conversa (campo de atribuicao na task ClickUp), medido mensalmente
- Cobertura de Contas por QBR: % de contas com ARR acima do threshold minimo que tiveram pelo menos 1 QBR nos ultimos 90 dias com brief gerado pelo squad (meta: 100% de contas Enterprise, >= 80% de contas Mid)

## Integrações

- ClickUp (Brain2 / MCP server) — hub central de tasks do pacote de renovacao, checklist de preparacao de QBR, prova de trabalho do squad e monitoramento de ativacao; espelhando arquitetura AIOX
- CRM: HubSpot ou Salesforce — fonte primaria de datas de renovacao, historico de expansao, MRR, atividades do CSM, notas de QBR, executive sponsor, pipeline de renovacao e decisoes comerciais
- Plataforma de produto: Mixpanel, Amplitude, Segment ou analytics nativo — eventos de uso por conta, DAU/MAU, feature adoption, usuarios ativos vs licencas, sessoes por usuario
- CS Platforms: Gainsight, ChurnZero, Custify, Velaris ou Chargebee — health scores existentes, historico de QBRs gerenciados na plataforma, alertas de renovacao e dados de health ja calculados (integracao bidirecional: leitura e escrita de scores)
- Google Workspace (Google Slides + Google Drive) ou Microsoft 365 (PowerPoint + SharePoint) — geracao e armazenamento de decks de QBR via API; webhook de deteccao de edicao pos-geracao
- Helpdesk: Zendesk ou Intercom — volume de tickets recentes por conta, CSAT, categorias de problema, resolucoes documentadas para o brief
- NPS / CSAT: Delighted, Typeform, Wootric ou nativo da CS platform — scores e verbatims para o brief de sentimento
- Call Recording: Gong, Chorus ou Zoom AI (nativo do CRM) — transcricoes de chamadas de QBR anteriores para o Memory e para o Briefer enriquecer o contexto relacional
- Slack — notificacoes ao CSM (brief pronto, deck gerado, renovacao critica), manager (escalacoes, tasks nao abertas) e Head de CS (relatorio semanal de cobertura e NRR tracking)
- Supabase / Postgres — estado dos agentes, Account Memory, Renewal Readiness Score historico, Expansion Signal Reports, log de tasks criadas e outcomes de renovacao
- Langfuse — observabilidade OTEL, tracing do pipeline de geracao de briefs, evals de qualidade de artefatos, quality gates dev/staging/prod, dashboard de NRR e cobertura de renovacoes
- Claude Agent SDK / LangGraph — orquestracao do pipeline multi-agente com gerenciamento de estado, filas de prioridade e retry logic
- Email / SMTP — relatorio semanal de cobertura de renovacoes para Head de CS e resumo mensal de NRR impact para stakeholders

## Entregável (prova de trabalho)

Por conta em janela de renovacao: (1) QBR Brief completo em markdown (max 600 palavras) com Resumo de Valor do Trimestre, Metricas de Adocao com comparativo, Marcos Entregues, Status de Comprometimentos Anteriores, Pontos de Tensao baseados em sentimento e Agenda Proposta de QBR — armazenado no Supabase e na task ClickUp como prova de trabalho auditavel; (2) Deck de QBR gerado automaticamente via API (Google Slides ou PowerPoint) com os dados do brief, salvo no Google Drive na pasta do CSM, link direto na task ClickUp; (3) Renewal Package com Renewal Readiness Score interpretado, Top-5 Evidencias de ROI em linguagem do decisor, e Proposta de Expansao qualificada (se aplicavel) com sinais que a embasam; (4) Pacote de tarefas no ClickUp: task principal de renovacao/QBR com todas as subtasks, prazos calculados e checklists de preparacao — prova de trabalho completa do squad rastreavel por conta, CSM e data. Por semana: relatorio de cobertura de renovacoes (% de renovacoes nos proximos 30 dias com pacote pronto) e pipeline de expansao identificado (numero de oportunidades e ARR total). Por mes: relatorio de NRR impact com MRR protegido em renovacoes e MRR incremental de expansoes atribuiveis ao squad.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (5 ag, red-team/QA) — base para o Critic Verity: estrutura adversarial de validacao multi-dimensao (integridade, proporcionalidade, completude) com logica de rejeicao com feedback especifico por dimensao e controle de iteracoes antes de escalonamento humano
- Data Quality Guardian (5 ag, qualidade de dados) — base para o pipeline de ingestao do Radar e para as validacoes do Compass: logica de deteccao de anomalia em dados, validacao de schema, tratamento de campos faltantes e alertas de inconsistencia que protegem o squad de gerar briefs baseados em dados corrompidos ou incompletos
- Athenaeum (11 ag, inteligencia estrategica) — base para o Briefer e o Scout: estrutura de agregacao e sintese de multiplas fontes de dados heterogeneas (uso, sentimento, comercial) em narrativa coerente e acionavel para tomada de decisao, incluindo logica de priorizacao de insights por relevancia e impacto para o decisor

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O3 · TopSquad de Customer Success: Onboarding, Retenção & Expansão** — O ciclo de vida pós-venda inteiro: ativar, reter, expandir.

- **Missão:** O squad do cliente após a venda: conduz o onboarding/implementação, prevê e previne churn ao longo da vida, e automatiza renovação, expansão e QBRs. Ativar → reter → expandir em um motor único de Customer Success.
- **Por que consolidar:** É a mesma jornada do cliente em três fases — ativar, manter, crescer — e os sinais fluem entre elas: um onboarding fraco prevê churn, que (evitado) abre expansão. Separados, o sinal de saúde vivia em silos; unidos, o health score atravessa todo o ciclo de vida.
- **Squads irmãos:** Onboarding & Implementação (PSA Agêntica), Predição & Prevenção de Churn, Renovação, Expansão & QBR Automatizado

## Estrutura

```
ops-cs-renovacao-expansao-qbr/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
