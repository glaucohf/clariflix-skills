# Squad de Follow-up, Nurture e Reativacao

> Cada lead que voce abandona e dinheiro que o concorrente embolsa — nos nao deixamos nenhum esfriar.

**Área:** Vendas · **TopSquad:** V4 Nurture, Follow-up & Reativação · **Prioridade:** must‑have · **Agentes:** 10 (8 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

A maioria das vendas exige 5 a 12 toques, mas 80% dos vendedores desistem após 2 tentativas. Leads que não converteram no primeiro contato (no-shows, ghostings, frios, oportunidades estagnadas no CRM) acumulam custo de aquisição sem retorno. Sem cadência estruturada e persistente, o pipeline apodrece — e a empresa continua pagando por novos leads para cobrir o buraco dos antigos.

## Impacto esperado

ROI estimado: recuperação de 15-35% de leads frios/no-show converte a custo zero de aquisição (CAC já pago). Para operações com 500 leads/mês e ticket médio de R$8k, a reativação de 20% representa R$800k de receita adicional por trimestre sem incremento de verba de ads. Redução de 60-70% no tempo de vendedor gasto em follow-up manual. Aumento de 2-3x na taxa de comparecimento em reuniões (reminders + re-agendamento automático). Pipeline score melhora em 40%+ pela higiene e enriquecimento contínuo. Benchmark: AI SDRs como 11x/Alice e Artisan/Ava reportam 3-5x mais tentativas de contato que SDRs humanos no mesmo período.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro` · Maestro | Maestro — Orquestrador de Cadencias | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `radar` · Radar | Radar — Worker de Sinais e Segmentação | L1 · worker autônomo | `monitorar-eventos-de-reativacao.md` |
| `cronos` · Cronos | Cronos — Worker de Cadência e Sequenciamento | L1 · worker autônomo | `sequenciar-toques-lead.md` |
| `volta` · Volta | Volta — Worker de Outreach Multicanal | L3 · aprovação humana | `enviar-mensagem-personalizada.md` |
| `sherlock` · Sherlock | Sherlock – Worker de Enriquecimento e Dossiê | L1 · worker autônomo | `enriquecer-dados-lead.md` |
| `atlas` · Atlas | Atlas — Worker de Lead Scoring e Priorização | L1 · worker autônomo | `calcular-score-lead.md` |
| `agenda` · Agenda | Agenda — Worker de Re-agendamento e Booking | L2 · orquestra / decide | `reagendar-reunioes.md` |
| `memento` · Memento | Memento — Worker de Histórico e Contexto Conversacional | L0 · worker determinístico | `recuperar-historico-de-interacoes.md` |
| `vigia` · Vigia | Vigia — Crític / Verifier de Mensagens | L2 · orquestra / decide | `verificar-mensagem.md` |
| `vigia-2` · Vigia 2 | Vigia — Critic de Mensagens e Compliance | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-followup-nurture-reativacao:maestro` (ou instale via `npx squads add ./vendas-followup-nurture-reativacao`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-followup-nurture-reativacao-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 – Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico; humano aprova ou edita antes do envio pelo Volta
- L3 – Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio
- L3 – Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualificar
- L3 – Lead que responde negativamente (não tenho interesse, cancela definitivamente): Maestro notifica o closer para decisão de desqualificação ou mudança de abordagem antes de qualquer novo toque
- Escalation do Vigia – Quando o Volta falha 2x na correção de uma mensagem reprovada: Vigia escala para humano com o draft e o feedback detalhado para revisão manual
- Revisão semanal de cadências — Atlas gera relatório de performance; gestor aprova ajustes de parâmetros (intervalos, canais, thresholds de score) antes de serem aplicados
- Opt-out recebido — Qualquer pedido de descadastro é interrompido imediatamente pelo Cronos e notificado ao responsável para confirmação de remoção do CRM

## KPIs

- Taxa de reativação: % de leads frios/no-show que respondem positivamente dentro da cadência (meta: 15-25%)
- Taxa de re-agendamento pós no-show: % de no-shows que remarcam em até 48h (meta: 40-60%)
- Taxa de comparecimento em reuniões: redução de no-shows com reminders automáticos (meta: redução de 50%+ vs baseline)
- Mensagens enviadas por lead reativado: eficiência da cadência (meta: conversão antes do toque 6 em média)
- Taxa de aprovação do Vigia na primeira tentativa: qualidade de mensagens geradas pelo Volta (meta: >85% aprovadas sem retrabalho)
- Leads qualificados reativados por semana: volume de pipeline resgatado (depende do funil do cliente)
- CAC de lead reativado vs novo lead: ROI da reativação vs aquisição nova (meta: CAC de reativado < 10% do CAC novo)
- Score médio de cadência ativa: saúde do pipeline em reativação (Atlas) — meta de score médio acima de 45/100
- Task success rate por Langfuse: dev 70% / staging 85% / prod 95% em todas as execuções do squad
- Tempo médio de primeiro toque pós no-show: velocidade de reação do Agenda (meta: <10 minutos)

## Integrações

- CRM: HubSpot (MCP disponível) ou Pipedrive — fonte de verdade de leads, status de cadência, score, histórico
- WhatsApp Business API: Gupshup, AiSensy ou Evolution API (open-source) — canal principal de reativação no Brasil
- Email: SMTP/SendGrid/Amazon SES via HubSpot ou Instantly.ai para sequências frias
- Calendário: Google Calendar / Outlook Calendar / Calendly — re-agendamento e reminders do Agenda
- Enriquecimento: Clay (orquestrador de enriquecimento) + Apollo (base de contatos) — alimentam o Sherlock
- Voz: Vapi (<600ms latência) ou Retell AI + ElevenLabs TTS — para toques de voz em cadências de alto valor
- LinkedIn: LinkedIn Sales Navigator API ou PhantomBuster — outreach e sinal de mudança de cargo
- Conversation Intelligence: Gong ou Chorus (webhook de transcrição pós-call) — alimenta o Memento
- Gestão de tarefas / Prova de trabalho: ClickUp (cada ação do squad gera task verificável)
- Observabilidade: Langfuse (OTEL) — tracking de todas as execuções, quality gates, evals de mensagem
- Orquestração: LangGraph (controle fino do fluxo de cadências) + Claude Agent SDK (Maestro como orchestrator)
- Sinais de intenção: G2, Bombora ou Apollo Intent — triggeram reativação de leads que pesquisam a categoria

## Entregável (prova de trabalho)

Pacote de Cadências Ativas: conjunto de workflows LangGraph deployados com (1) 4 cadências codificadas (no-show, frio 30/60/90d, proposta fria, nurture longo) com todos os templates de mensagem aprovados pelo Vigia; (2) dashboard de pipeline de reativação no ClickUp com tasks verificáveis por lead e por toque; (3) relatório semanal automático com leads trabalhados, toques realizados, respostas obtidas, reuniões reagendadas e pipeline resgatado em R$; (4) mapa de calor de performance por canal x segmento x horário para otimização contínua.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mãe Intuitiva CRM (squads.sh) — squad gratuito focado em CRM e gestão de leads, serve como base para a lógica de segmentação e priorização do Radar e do Atlas, evitando construir do zero o estado de funil e os triggers de CRM
- Data Quality Guardian (5 agentes, squads.sh/myclaude) — squad gratuito de qualidade de dados, reutilizável diretamente como base do Sherlock para enriquecimento, deduplicação e higiene do CRM antes de iniciar as cadências
- Skeptic Protocol (5 agentes, squads.sh/myclaude) — squad gratuito de red-team e QA, serve como arquitetura de referência para o Vigia (critic), incluindo o padrão de checklist multidimensional, lógica de reprovação com instrução de correção e escalonamento para HITL

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V4 · TopSquad de Nurture, Follow-up & Reativação** — Nenhum lead morto: reaquece deals parados, leads frios e públicos pós-evento.

- **Missão:** O squad da memória longa do funil: detecta qualquer lead/deal que esfriou — sem resposta, estagnado no pipeline ou inerte após um evento/webinar — e dispara a cadência de reaquecimento certa para o motivo certo.
- **Por que consolidar:** Os três faziam a mesma coisa — reaquecer quem parou de avançar — variando só o gatilho (silêncio, deal estagnado, fim de evento). Compartilham biblioteca de cadências, lógica de decaimento e regra de "quando desistir". Um squad só evita três motores de cadência concorrendo pelo mesmo lead.
- **Squads irmãos:** Follow-up, Nurture e Reativação, Recuperação de Oportunidades Estagnadas, Reengajamento Pós-Evento e Webinar

## Estrutura

```
vendas-followup-nurture-reativacao/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
