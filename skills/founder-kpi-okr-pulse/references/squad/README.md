# KPI/OKR Pulse — Founder Intelligence Squad

> Transforma métricas dispersas em diagnóstico de desvio com recomendação acionável toda segunda-feira — antes que o trimestre seja perdido.

**Área:** Founder Office · **TopSquad:** F2 Performance, KPIs & Calibração de Decisões · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

KPIs críticos vivem fragmentados em 6-12 sistemas distintos (CRM, financeiro, produto, ads, planilhas, analytics) sem consolidação automática. Desvios de OKR só são percebidos semanas após ocorrer — quando a janela de correção é pequena ou inexistente. O founder não tem diagnóstico de causa-raiz, apenas números frios, sem saber qual alavanca puxar. Mensurável por: latência de detecção de desvio (atual: 2-4 semanas → target: <48h), % de KPIs consolidados automaticamente com recomendação acionável (atual: ~15% → target: >85%), tempo do founder gasto em coleta e análise de dados (atual: 6-10h/semana → target: <1h/semana com Pulse Review), e % de OKRs do trimestre com diagnóstico de causa-raiz documentado (atual: ~20% → target: 100%).

## Impacto esperado

ROI direto: 8h/semana × R$1.500/h do founder = R$12.000/semana recuperados em alavancagem de atenção. Indireto: desvios detectados com 3 semanas de antecedência permitem correção de curso — um OKR crítico recuperado por trimestre equivale a R$50-500k em receita preservada dependendo do setor. Para a consultoria Lendar[IA]: este squad ancora o pilar Dados & Tecnologia do diagnóstico de 7 pilares, é o produto de recorrência mais natural (entrega toda semana, impossível de pausar), justifica ticket mensal R$4-12k e serve como prova de valor contínua que sustenta a relação de longo prazo pós-implementação. NPS esperado >92 por ser o squad que o founder usa toda segunda-feira sem exceção.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `atlas` · Atlas | Atlas — O Controlador de Performance | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `pulsar` · Pulsar | Pulsar — O Coletor de Dados | L0 · worker determinístico | `coletar-dados-kpi.md` |
| `kalinda` · Kalinda | Kalinda — A Estrategista de OKR | L1 · worker autônomo | `calcular-trajetorias-okr.md` |
| `argo` · Argo | Argo — O Detetive de Causa-Raiz | L2 · orquestra / decide | `analisar-causa-raiz.md` |
| `rex` · Rex | Rex — O Motor de Recomendações | L2 · orquestra / decide | `gerar-recomendacoes-acionaveis.md` |
| `sigma` · Sigma | Sigma — O Clone do Founder | L2 · orquestra / decide | `humanizar-relatorio.md` |
| `vera` · Véra | Véra — A Crítica de Dados | L1 · worker autônomo | `validar-dados-plausiveis.md` |
| `vera-2` · Véra 2 | Véra — A Crítica de Dados | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-kpi-okr-pulse:atlas` (ou instale via `npx squads add ./founder-kpi-okr-pulse`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-kpi-okr-pulse-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- DIAGNÓSTICO DE BAIXA CONFIANÇA (L3): Quando Véra classifica diagnóstico de causa-raiz como confiança Baixa e o KR associado tem peso estratégico Alto (ex: OKR de receita principal) — Argo retém a hipótese e Atlas notifica o founder: 'Detectei desvio em [KR] mas não tenho dados suficientes para confirmar a causa. Possível hipótese: [X]. Você pode me dar contexto adicional?' O founder responde e Argo reprocessa com o contexto fornecido.
- RECOMENDAÇÃO COM IMPACTO FINANCEIRO DIRETO (L3): Rex nunca cria task automática no ClickUp para recomendações classificadas como 'ação financeira' (ex: cancelar contrato, cortar budget de campanha, demitir fornecedor, alterar pricing) sem aprovação explícita do founder. Essas recomendações chegam como rascunho com flag APPROVAL_REQUIRED — founder aprova, rejeita ou modifica antes de qualquer task ser criada.
- ALERTA DE DADOS COMPROMETIDOS (L2→L3): Se Véra detectar que >30% dos KPIs de um OKR crítico vieram com data_quality_flag=FAILED (falha de integração, dado zerado, timeout), Atlas pausa o ciclo e envia alerta imediato: 'Pulse desta semana comprometido — [N] KPIs sem dados confiáveis de [sistema X]. Envio relatório parcial ou aguardo resolução?' Founder decide antes do relatório ser publicado.
- CLONE SIGMA PUBLICAÇÃO EXTERNA (L1→L3): Sigma pode gerar e entregar o Pulse no Slack e Notion de uso interno do founder sem aprovação. Se o founder solicitar versão do Pulse para compartilhar com time, board ou investidores — Sigma gera o draft mas entrega APENAS ao founder para revisão antes de qualquer distribuição externa.
- RECALIBRAÇÃO DE TARGET DE OKR (L2): Quando Kalinda detecta que um OKR está >120% da trajetória esperada por 2 semanas consecutivas (super-performance) ou que a tendência matemática torna o target inalcançável mesmo com ação corretiva — Atlas sinaliza ao founder para deliberar sobre recalibração de target. Nunca recalibra automaticamente. Founder decide em reunião de check-in mensal.
- ONBOARDING DE NOVO KPI/SISTEMA (L1): Ao adicionar nova fonte de dados ao catálogo, o primeiro ciclo de coleta opera em modo 'dry-run' — Pulsar coleta e Kalinda calcula desvios, mas Véra bloqueia entrega de diagnóstico e recomendação até que o founder confirme que os dados coletados fazem sentido. Isso evita que erro de mapeamento de campo gere falso alarme na primeira semana.

## KPIs

- Latência de detecção de desvio: tempo entre ocorrência do desvio e notificação ao founder (target <48h vs. baseline 2-4 semanas)
- Taxa de KPIs consolidados automaticamente com dados OK por ciclo semanal (target >85% sem intervenção manual)
- Taxa de diagnósticos de causa-raiz com confiança Alta ou Média validados pela Véra (target >80%)
- Taxa de recomendações aceitas pelo founder (task criada no ClickUp sem modificação) (target >60%)
- Número de falsos alarmes por mês (desvios reportados que founder classifica como 'não-acionável') (target <2/mês)
- Tempo do founder gasto em coleta e análise manual de dados por semana (target <1h vs. baseline 6-10h)
- SLA de entrega do Pulse Report completo após início da coleta (target <90 min)
- Cobertura do catálogo de métricas: % dos OKRs do trimestre com pelo menos 1 KPI coletado automaticamente (target 100%)
- Custo por ciclo semanal em tokens (target <U$2 por Pulse semanal padrão)
- NPS do founder com o Pulse semanal após 90 dias (target >=9/10)

## Integrações

- HubSpot / Salesforce (CRM — pipeline de vendas, MRR, churn, NPS, métricas de CS via MCP)
- Stripe / Conta Azul / Omie (financeiro — receita, MRR, ARR, inadimplência, unit economics via MCP ou API)
- Google Analytics 4 / Mixpanel / Amplitude (produto/analytics — DAU, MAU, activation, retention, engagement via MCP)
- Meta Ads / Google Ads (mídia paga — CPL, CAC, ROAS, impressões, conversões via MCP ou API)
- Google Sheets / Airtable (planilhas operacionais — KPIs que ainda não têm sistema dedicado, coletados via MCP)
- ClickUp (OKRs source-of-truth + criação automática de tasks de recomendação + prova de trabalho do squad)
- Notion (Knowledge Base — armazenamento permanente do Pulse Report, OKRs, histórico de diagnósticos e playbook de alavancas)
- Slack (entrega do Pulse semanal via canal privado #founder-pulse + alertas de desvio crítico em tempo real)
- WhatsApp Business API (versão ultra-curta do Pulse em 5 bullets via Sigma — opcional, para founders mobile-first)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente — gerencia ciclo semanal e queries ad-hoc)
- Langfuse (observabilidade OTEL — tracing de custo por agente/token, evals de qualidade do diagnóstico, dashboard de KPIs do squad)
- Vector DB — Pinecone ou Qdrant (histórico de KPIs, corpus do founder para Sigma, playbook de alavancas, heurísticas de Véra)
- MCP Servers (camada de integração universal — cada sistema exposto como tool para Pulsar via protocolo MCP)

## Entregável (prova de trabalho)

Pulse Report Semanal — entregue toda segunda-feira via Slack (resumo em 5 bullets acionáveis) + Notion (relatório completo permanente) + ClickUp (tasks de recomendação já criadas). Estrutura do relatório completo: (1) Semáforo Geral do Portfólio de OKRs (Verde/Amarelo/Vermelho por OKR, % de progresso vs. trajetória esperada); (2) Desvios da Semana — para cada KR desviado: valor atual vs. esperado, desvio percentual, diagnóstico de causa-raiz com evidência numérica, categoria (Operacional/Mercado/Produto/Financeiro/Pessoas) e nível de confiança do diagnóstico; (3) Recomendações Acionáveis — 1-3 recomendações por KR desviado com lógica explícita, owner sugerido, prazo esperado de efeito e KPI de confirmação; (4) Quick Wins — top 3 ações de alto impacto e baixo esforço da semana; (5) Tendências de Médio Prazo — projeção de encerramento do trimestre em cenário base, otimista e pessimista; (6) Log de Dados — quais sistemas foram coletados, quais falharam, qualidade geral dos dados desta semana; (7) Pulse em 5 Bullets (Sigma) — versão ultra-condensada para consumo imediato. Audit trail completo (timestamp de cada etapa, custo de tokens, agentes acionados) armazenado no Langfuse.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Five Vitals (diagnóstico de sistemas) — estrutura de diagnóstico multi-dimensional com semáforos e drill-down mapeia diretamente para a lógica de Kalinda + Argo: adaptar os 5 vitais para os pilares de OKR do cliente e reutilizar o protocolo de drill-down para análise de causa-raiz
- Athenaeum (11 agentes, inteligência estratégica) — a camada de síntese e recomendação do Athenaeum serve de base para o Rex: estrutura de geração de recomendações acionáveis com lógica explícita e ranqueamento por impacto, adaptando o contexto de pesquisa para contexto de métricas de negócio
- Data Quality Guardian (5 agentes, qualidade de dados) — o protocolo de verificação de qualidade de dados do Data Quality Guardian alimenta diretamente a Véra: regras de detecção de outlier, flags de dado comprometido e thresholds de qualidade por tipo de métrica

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F2 · TopSquad de Performance, KPIs & Calibração de Decisões** — Pergunte aos dados, acompanhe as metas e calibre o próprio julgamento ao longo do tempo.

- **Missão:** O squad que mede e aprende: responde perguntas em linguagem natural sobre os dados, monitora KPIs/OKRs com alertas, e registra decisões + postmortems para calibrar o julgamento do founder ao longo do tempo.
- **Por que consolidar:** Os três giram o mesmo ciclo: medir (analytics), comparar com a meta (KPI/OKR) e refletir sobre a decisão (journal). O KPI Pulse lê os mesmos dados do analytics; o decision journal precisa do resultado dos KPIs para o postmortem. Unidos, formam um loop fechado de decisão informada → resultado medido → aprendizado.
- **Squads irmãos:** Agentic Analytics (Pergunte aos Seus Dados), KPI/OKR Pulse, Decision Journal & Postmortem

## Estrutura

```
founder-kpi-okr-pulse/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
