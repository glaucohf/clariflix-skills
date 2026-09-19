# Squad de Conversation Intelligence e Coaching

> Cada call vira aula: o gestor para de ser bombeiro e o vendedor recebe coaching cirúrgico — automaticamente, antes da próxima ligação.

**Área:** Vendas · **TopSquad:** V5 Sales Enablement & Conversation Intelligence · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Gestores de vendas conseguem ouvir, na melhor das hipoteses, 3-5% das calls do time. Os outros 95-97% somem sem analise: objecoes que se repetem sem resposta treinada, talk-ratio desequilibrado (vendedor falando 80% quando deveria ouvir), sinais de risco de deal ignorados (prospect mencionou 'preciso pensar', 'meu socio decide', 'orcamento apertado' e ninguem registrou). O resultado e um ciclo de coaching esporadico baseado em percepcao do gestor, nao em dados — o time nao melhora de forma sistematica e os mesmos erros se repetem trimestre apos trimestre.

## Impacto esperado

Empresas com conversation intelligence estruturada apresentam 19-27% de aumento na taxa de conversao de proposals (benchmark Gong Research, 2024) por eliminacao das objecoes nao tratadas. Reducao de 40% no tempo de ramp de novos vendedores ao substituir shadowing manual por coaching baseado em calls reais. Gestores recuperam 8-12h/semana gastas em revisao manual de calls. ROI estimado: para um time de 5 closers com taxa de conversao de 25% e ticket medio de R$20k (100 proposals/mes = R$500k pipeline), mover conversao de 25% para 32% representa R$140k/mes adicional em receita fechada — payback do squad em 30-45 dias de operacao com custo de implantacao de R$15-25k.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro` · Maestro | Diretor de Inteligência Comercial (Maestro) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `babel` · Babel | Transcritora de Calls (Babel) | L0 · worker determinístico | `filtrar-ruidos-tecnicos.md` |
| `sherlock-da-call` · Sherlock da Call | Analisador de Padrões (Sherlock da Call) | L1 · worker autônomo | `analisar-transcricao.md` |
| `juiz` · Juiz | Avaliador de Performance (Juiz) | L0 · worker determinístico | `calcular-percentil.md` |
| `sensei` · Sensei | Coach de Vendas (Sênsêi) | L2 · orquestra / decide | `gerar-coaching-card.md` |
| `memoria-do-crm` · Memória do CRM | Atualizador de Deal (Memória do CRM) | L1 · worker autônomo | `sincronizar-dados-deal-crm.md` |
| `radar-do-time` · Radar do Time | Inteligência Coletiva (Radar do Time) | L2 · orquestra / decide | `analisar-objecoes-frequentes.md` |
| `vigilante` · Vigilante | Detector de Risco de Deal (Vigílante) | L3 · aprovação humana | `detectar-risco-deal.md` |
| `calibrador` · Calibrador | Auditor de Insights (Calibrador) | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-conversation-intelligence-coaching:maestro` (ou instale via `npx squads add ./vendas-conversation-intelligence-coaching`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-conversation-intelligence-coaching-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- HITL-1 (L3): Deal Risk Alert de nível ALTO ou CRÍTICO gerado pelo Vigilante — gestor recebe alerta no WhatsApp e deve confirmar qual ação tomar (ligar agora, escalar para diretor, ajustar proposta, aceitar perda) antes de qualquer comunicação automatizada com o prospect. SLA de resposta: 4h em dias úteis.
- HITL-2 (L3): Objeção de tipo não mapeado detectada pela primeira vez — o Analisador sinaliza objeção nova fora da biblioteca existente. Humano (gestor ou especialista de produto) deve validar a classificação e criar o counter-script antes que o sistema use-o em coachings futuros. Evita ensinar o time a responder errado.
- HITL-3 (L2): Score da call abaixo de 40/100 (call catastrófica) — além do coaching card automático, o Orchestrator notifica o gestor para que ele decida se faz uma sessão 1:1 urgente com o vendedor ou se o deal precisar de intervenção direta do gestor. Vendedor não é notificado do score crítico sem acompanhamento humano.
- HITL-4 (L2): Transcrição com qualidade de áudio abaixo de 75% de confiança — a Babel sinaliza e o gestor decide se envia para transcrição manual, descarta a call da análise ou aceita os resultados com baixa confiança. Garante que coaching baseado em transcrição ruim não chegue ao vendedor.
- HITL-5 (L2): Calibração quinzenal da Rubrica de Avaliação — o gestor revisa um sample de 5 calls para verificar se os scores do Juiz estão alinhados com sua percepção. Ajusta pesos de dimensões se necessário. Previne drift do modelo de scoring ao longo do tempo.
- HITL-6 (L1): Aprovação do Plano de Role-Play semanal gerado pelo Radar do Time — gestor revisa as objeções priorizadas e o script de simulação antes de compartilhar com o time no próximo standup de vendas. Garante que o treinamento coletivo seja relevante para o contexto atual do mercado.

## KPIs

- Taxa de cobertura de calls: % de calls de vendas analisadas automaticamente vs total de calls realizadas (meta: > 90% em 30 dias de operação)
- Tempo médio de entrega do coaching card: do encerramento da call até o card no WhatsApp do vendedor (meta: < 30 minutos)
- Taxa de objeções tratadas adequadamente: % de objeções detectadas que receberam counter-script adequado (meta: aumento de 30% em 60 dias vs baseline do Blueprint)
- Talk-ratio médio do time: % de fala do vendedor nas calls (meta: aproximar do benchmark de 43% vendedor / 57% prospect — modelo Gong Research)
- Score médio de call do time: evolução semanal do score médio nas 12 dimensões (meta: +10 pontos em 90 dias vs baseline inicial)
- Taxa de conversao de proposals impactadas: comparar taxa de fechamento de deals onde o vendedor recebeu coaching card vs deals sem coaching aplicado (meta: +20% de conversao em deals com coaching)
- Redução de deals perdidos por risco não detectado: % de deals com Deal Risk Alert ALTO que foram salvos por intervenção do gestor (meta: > 40% de saves apos alerta)
- Engajamento do vendedor com coaching: % de coaching cards lidos e marcados como revisados pelo vendedor (meta: > 80% de abertura, > 60% de confirmação de leitura)
- Qualidade do coaching card (Calibrador): score médio nas 6 dimensões de validação (meta: > 8.5/10 consistentemente)
- Task success rate por ambiente: dev > 70%, staging > 85%, prod > 95% (Langfuse quality gates para cada agente do pipeline)
- ROI mensal: receita incremental atribuída a deals com coaching aplicado / custo total do squad incluindo APIs de STT e LLM (meta: > 8x em 6 meses)

## Integrações

- Plataformas de voz/vídeo: Vapi (webhook pós-call com link de gravação), Retell AI, Zoom (webhook recording.completed), Google Meet (Drive API para gravações), Gupshup/AiSensy para calls gravadas via WhatsApp Business
- STT (Speech-to-Text): Deepgram (latência < 1min/hora de áudio, diarização de speakers, vocabulário customizado) ou AssemblyAI como fallback
- CRM: HubSpot (MCP disponível nativamente) ou Pipedrive — gravação de insights, sinais de risco, score de call, próximo passo como campos customizados no deal e na timeline
- Gestão de tarefas: ClickUp — Coaching Card como task atribuída ao vendedor com link para o trecho da call, proof-of-work verificável por task, Plano de Role-Play semanal como task coletiva
- Comunicação: WhatsApp Business API (Gupshup ou AiSensy) para entrega do coaching card ao vendedor e alertas de risco ao gestor; Slack para integração com times que usam Slack como hub
- Armazenamento de artefatos: Supabase (PostgreSQL) — Transcript Objects, Call Analysis Objects, Call Score Objects, histórico de coaching por vendedor, Feature Store de objeções
- Documentação de coaching: Notion — Coaching Cards formatados, Biblioteca de Counter-Scripts, Plano de Desenvolvimento Individual por vendedor, Briefing Semanal do Gestor
- Observabilidade/Evals: Langfuse (OTEL) — traces de todas as chamadas LLM (análise + coaching), quality gates por ambiente (dev 70% / staging 85% / prod 95%), evals de qualidade do coaching card (rastreabilidade, especificidade, tom)
- Orquestração: LangGraph + Claude Agent SDK — controle de estado do pipeline de análise, workflows determinísticos de sequenciamento (transcrição -> análise -> scoring -> coaching), re-tentativas automáticas em falha
- Armazenamento de áudio: AWS S3 ou Google Cloud Storage — arquivos de áudio/vídeo das calls com retenção configurável (90 dias default, 365 dias para deals fechados)

## Entregável (prova de trabalho)

Conversation Intelligence Dashboard (ClickUp + Notion + CRM): (1) Coaching Card por call — entregue direto ao vendedor via WhatsApp/Notion em até 30 minutos após a call, com transcript, score, top 3 insights acionáveis e counter-scripts específicos; (2) Briefing Semanal do Gestor — 1 página com score médio do time, top objeções da semana, ranking de vendedores, deals em risco e clip da semana; (3) Deal Risk Alerts em tempo real — alerta no WhatsApp do gestor quando call detecta risco alto, com diagnóstico e ação recomendada; (4) Biblioteca de Counter-Scripts viva — atualizada automaticamente com novos padrões detectados nas calls, validados pelo gestor via HITL-2; (5) Plano de Role-Play semanal — roteiro de simulação gerado a partir das objeções mais frequentes da semana. Artefato verificável por task no ClickUp: cada call processada gera um Coaching Card rastreável no Langfuse com trace completo do pipeline (Babel -> Sherlock -> Juiz -> Sensei -> Calibrador) e score de qualidade do Calibrador.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (myclaude/squads.sh) — base para o Critic Calibrador; os 5 agentes de red-team/QA mapeiam diretamente para as 6 dimensões de validação do coaching card (rastreabilidade, especificidade, tom, prioridade, consistência com histórico, acurácia de score); adaptar os prompts de red-team para contexto de avaliação de coaching de vendas
- Apex Context Supreme (myclaude) — base para o Sensei (Coach de Vendas); os 5 agentes de context engineering são ideais para manter o contexto do histórico de coaching por vendedor e gerar counter-scripts ultra-específicos sem perder o fio do que já foi trabalhado nas últimas N calls; adaptar para domínio de vendas e coaching
- Data Quality Guardian (myclaude/squads.sh) — base para a pipeline de qualidade de transcrição da Babel; os 5 agentes de qualidade de dados mapeiam para validação de completude e confiança da transcrição, detecção de anomalias (call muito curta, áudio inaudível, speaker não identificado) e garantia de que apenas transcrições de qualidade entram no pipeline de análise

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V5 · TopSquad de Sales Enablement & Conversation Intelligence** — O copiloto do closer: contexto antes, respostas durante, coaching depois.

- **Missão:** Tudo que torna o vendedor humano melhor: prepara o contexto da conta e battlecards antes da call, sugere respostas a objeções durante, e analisa a gravação para coaching depois. Um cérebro de enablement do pré ao pós-call.
- **Por que consolidar:** Os três bebem da mesma fonte: a base de conhecimento de produto, concorrência e conversas reais. Battlecards alimentam o objection handling, que alimenta o coaching, que descobre novas objeções para os battlecards. Era um ciclo partido em três; unido, ele se retroalimenta.
- **Squads irmãos:** Conversation Intelligence & Coaching, Objection Handling & Q&A em Tempo Real, Inteligência de Conta & Battlecards

## Estrutura

```
vendas-conversation-intelligence-coaching/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
