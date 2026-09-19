# Squad de QÁ de Conversas 100% (Quality Verifier)

> Cada conversa auditada, nenhuma violação escapando — o QÁ que nunca dorme e revisa 100% sem custar 100% do seu time.

**Área:** Operações & CS · **TopSquad:** O2 Qualidade, Voz do Cliente & Knowledge Base · **Prioridade:** must‑have · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

QA tradicional depende de amostragem manual: um analista humano consegue revisar no maximo 1-2% das conversas por semana, selecionadas de forma nao sistematica. O resultado e um ponto cego estrutural: quebras de compliance passam despercebidas ate virarem reclamacao formal ou processo; tom inadequado corrode o relacionamento com o cliente sem que o gestor saiba; respostas erradas ou desatualizadas sao repetidas dezenas de vezes antes de alguem notar; agentes de IA alucinam ou saem do escopo sem deteccao. Sem evidencia por conversa, nao ha dados para coaching de time, nao ha rastro de violacoes para auditoria regulatoria e nao ha metrica confiavel de qualidade — apenas a percepcao subjetiva de quem lembra de ter lido uma conversa ruim. O squad avalia 100% das interacoes (humanas, de IA ou mistas) contra uma rubrica multi-eixo (tom, compliance, precisao, resolucao, handoff), gera scorecard por conversa com evidencia citada e abre tasks de coaching ou correcao automaticamente no ClickUp para cada violacao detectada.

## Impacto esperado

Uma operação de CS com 500 conversas/dia e 1% de taxa de violação tem 5 incidentes diários passando sem detecção — 150/mês. Com QÁ humano a R$3.500/mês por analista (que cobre ~50 conversas/dia), cobrir 500 conversas exigiria 10 analistas = R$35.000/mês. O Quality Verifier cobre o mesmo volume por estimativa de R$2.000 a R$4.500/mês em tokens + infra (Claude Sonnet workers + Opus spot para casos complexos), representando economia de 85-90% no custo de QÁ com cobertura 50x maior. Além do custo, o impacto real: redução de 70-85% nas violações de compliance não detectadas (que em setores regulados como financeiro e saúde podem gerar multas de R$50k-500k por incidente), redução de churn por atendimento ruim estimada em 5-15% nos clientes de alto risco detectados pelo squad, e aceleração de coaching de time — o gestor recebe uma lista priorizada das piores conversas da semana, já com evidência citada e ação recomendada, em vez de gastar 4-8 horas por semana ouvindo gravações. ROI estimado: 8-15x sobre o custo do squad nos primeiros 6 meses, mensurável via redução de churn, evitação de multas e redução de custo de QÁ.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `kronos` · KRONOS | KRONOS — O Crônista de Qualidade | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `lexis` · LEXIS | LEXIS — O Guardião de Compliance | L1 · worker autônomo | `scanner-de-dados-sensiveis.md` |
| `aria` · ARIA | ARIA — A Auditora de Tom e Empatia | L1 · worker autônomo | `avaliar-qualidade-relacional.md` |
| `veritas` · VERITAS | VERITAS — O Verificador de Precisão Técnica | L1 · worker autônomo | `verificar-informacoes-tecnicas.md` |
| `nexus` · NEXUS | NEXUS — O Avaliador de Resolução e Handoff | L1 · worker autônomo | `avaliar-resolucao-problema.md` |
| `herald` · HERALD | HERALD — O Repórter e Gestor de Acoes | L3 · aprovação humana | `gerar-scorecard-completo.md` |
| `calibra` · CALIBRA | CALIBRA — O Curador da Rubrica e do Aprendizado | L3 · aprovação humana | `calibrar-rubrica.md` |
| `veritas-sentinel` · VERITAS-SENTINEL | VERITAS-SENTINEL — O Anti-Falso-Positivo | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@ops-cs-qa-conversas-verifier:kronos` (ou instale via `npx squads add ./ops-cs-qa-conversas-verifier`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/ops-cs-qa-conversas-verifier-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Criação de tasks de coaching ALTA prioridade no ClickUp para violações VERMELHAS: o VERITAS-SENTINEL revisa primeiro; após confirmação, HERALD cria a task — o gestor recebe o alerta e decide se escala para ação disciplinar ou coaching
- L3 — Envio de alertas externos (Slack, email) para gestores sobre violações críticas de compliance: sempre passa pelo VERITAS-SENTINEL antes do envio; nenhum alerta crítico é enviado sem revisão de falso positivo
- L3 — Qualquer modificação na rubrica de auditoria (thresholds, pesos por eixo, novos termos proibidos, atualização de política): CALIBRA prepara a proposta de mudança, gestor responsável aprova via ClickUp task antes de entrar em produção — nunca modificação autônoma da rubrica
- L3 — Ações que afetam o agente humano diretamente (notificação formal de violação, registro em prontuário de RH, bloqueio de acesso): o squad gera a evidência e a recomendação, mas a ação sobre pessoas exige aprovação humana obrigatória
- L2 — Conversas de clientes VIP (acima de threshold configurado de valor anual) ou conversas envolvendo processos juridicos ou ameacas: KRONOS pausa o pipeline automatico e notifica o gestor para revisar manualmente antes de qualquer acao do squad
- L2 — Contestação de scorecard pelo agente auditado: CALIBRA recebe a contestação, analisa e gera recomendação (confirmar ou reverter veredicto), mas a decisão final de reversão é do gestor que aprova via ClickUp — nunca reversão autônoma
- L1 — Calibragem inicial da rubrica no onboarding: os pesos dos eixos, os thresholds de VERDE/AMARELO/VERMELHO e a lista inicial de termos proibidos são definidos pelo cliente em workshop com o consultor Lendar[IA] antes da ativação do squad em produção

## KPIs

- Taxa de cobertura de conversas auditadas: % do total de conversas encerradas que passaram pelo pipeline de QA — meta 100% para helpdesk integrado; > 95% contando erros de ingestão e retries
- Latência de auditoria: tempo do encerramento da conversa até scorecard disponível — meta P50 < 3 minutos, P95 < 10 minutos para o lote padrão; < 2 minutos para conversas de risco crítico (keywords de escalação)
- Precisão de detecção de violações (validada contra set anotado): taxa de verdadeiros positivos (violações reais detectadas) e taxa de falso positivo (alertas indevidos) — meta > 92% de precisão e < 8% de falso positivo em produção (quality gate Langfuse)
- Taxa de falso positivo contestado: % de scorecards VERMELHO que foram revertidos pelo SENTINEL ou contestados e aprovados pelo gestor — meta < 5%; acima disso dispara recalibragem da rubrica pelo CALIBRA
- Taxa de violação por eixo (semanal): % de conversas auditadas com pelo menos uma violação em compliance (LEXIS), tom (ARIA), precisão (VERITAS) e resolução (NEXUS) — linha de base medida nos primeiros 30 dias, meta de redução de 30-50% em 90 dias
- Taxa de conclusão de tasks de coaching no ClickUp: % de tasks abertas que foram concluídas dentro do prazo estabelecido — meta > 80% em 14 dias; mede se o QA está gerando ação real ou apenas relatório ignorado
- Score médio de qualidade por agente (trend semanal): evolução do score compósito médio por agente ao longo do tempo — meta: agentes com coaching mostram melhora mensurável de pelo menos 10 pontos em 4 semanas
- Custo por conversa auditada (tokens + infra): meta < R$0,05 por conversa para operações de até 1.000 conversas/dia; calculado automaticamente via Langfuse e reportado no dashboard mensal
- Redução de re-contato desnecessário (medida via NEXUS): % de conversas com flag de 're-contato provável' que efetivamente geraram um novo ticket em 48h — baseline nos primeiros 30 dias, meta redução de 20% em 90 dias após ativação do squad

## Integrações

- Zendesk / Intercom (Fin) / Freshdesk — helpdesks primarios para ingestao de tickets; webhook ou polling via MCP para receber conversas encerradas em tempo quasi-real; leitura de metadados de ticket (agente, categoria, resolucao) para contexto do NEXUS
- WhatsApp Business API (Gupshup, AiSensy, Twilio) — canal #1 no Brasil; ingestão de conversas completas incluindo áudio transcrito via Deepgram/Whisper para audit trail completo
- Gong / Chorus / NICE — conversation intelligence para calls de voz; transcrições automáticas alimentam VERITAS e ARIA; dados de sentimento pré-processados reduzem latência do squad
- ClickUp (MCP disponível / Brain2 / Super Agents) — hub de tasks de coaching e correção; cada violação vira uma task rastreável com evidência citada, responsável, prazo e status; dashboard de qualidade agregado no ClickUp; prova de trabalho do squad
- Slack — canal de alertas críticos para gestores (violações VERMELHAS confirmadas pelo SENTINEL); relatório semanal de tendências de qualidade; notificações de HITL para aprovação de mudanças de rubrica
- HubSpot / Salesforce (MCP disponivel) — leitura de perfil de cliente (tier, valor, historico) para contextualizacao de prioridade na fila e ponderacao de score; dados de churn historico para calibrar flag de risco do ARIA
- ChurnZero / Custify / Velaris — CS platforms para leitura de health score do cliente; conversas de clientes com health score baixo recebem prioridade de auditoria e peso maior no flag de risco de churn
- Supabase / Postgres — estado persistente do squad: fila de processamento, scorecards históricos, rubrica ativa, log de contestações, métricas de produção; pgvector para busca semântica na base de conhecimento do VERITAS
- Langfuse (OTEL) — observabilidade completa: tracing por conversa (latência por worker, custo por auditoria, tokens consumidos), quality gates (dev 70% / staging 85% / prod 95% de precisão de detecção validada contra set de conversas anotadas), dashboard de drift de qualidade do squad
- Claude Agent SDK / LangGraph — orquestração do pipeline multi-agente; paralelismo dos 4 workers de auditoria (LEXIS, ARIA, VERITAS, NEXUS rodando simultaneamente por conversa); retry logic com fallback; controle de estado de processamento por batch
- Deepgram / Whisper — ASR para transcrição de áudios do WhatsApp e chamadas de voz não processadas por Gong/Chorus; PT-BR como língua primária com fallback para ES e EN

## Entregável (prova de trabalho)

Scorecard de Qualidade por Conversa — artefato verificável entregue para 100% das conversas auditadas: score total de 0-100 + score por eixo (Compliance/Tom/Precisão/Resolução) + veredicto (VERDE/AMARELO/VERMELHO) + lista de violações com trecho exato citado + ação recomendada. Para conversas AMARELAS e VERMELHAS: task automática no ClickUp com evidência, responsável, prazo e prioridade — prova de trabalho rastreável do squad. Relatório consolidado semanal entregue ao gestor via Slack: distribuição de scores, top violações da semana, agentes que mais melhoraram e que mais precisam de atenção, evolução da taxa de violação por eixo vs semana anterior. Dashboard de qualidade em tempo real (ClickUp ou Supabase-backed) com métricas de produção do squad (volume auditado, taxa de cobertura, custo por auditoria) e métricas de impacto (taxa de violação trend, FCR, churn risk conversas).

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (5 agentes, red-team/QA) — arquitetura de critic/verifier multi-camada diretamente reusavel para o VERITAS-SENTINEL; padrao de verificacao adversarial onde um agente critica o output de outro antes da acao externa; pipeline de 'challenge your own output' adaptavel ao fluxo KRONOS -> SENTINEL -> HERALD
- Data Quality Guardian (5 agentes, qualidade de dados) — lógica de validação multi-eixo e detecção de anomalias reutilizável para o pipeline de auditoria de conversas; padrão de score ponderado por dimensão (similar ao que KRONOS aplica sobre os 4 workers) e sistema de alertas por desvio de threshold já implementado neste squad
- Incident Response Squad (5 agentes) — padrao de escalacao estruturada e handoff de informacao entre agentes aplicavel ao fluxo de violacoes VERMELHAS (deteccao -> validacao -> alerta -> acao); logica de priorizacao por severidade e roteamento de alertas para o responsavel correto reusavel pelo HERALD

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**O2 · TopSquad de Qualidade, Voz do Cliente & Knowledge Base** — Audita 100% das conversas, ouve o que o cliente sente e devolve isso à base.

- **Missão:** A camada de aprendizado da operação: audita 100% das conversas (não amostra), extrai sentimento e tendências da voz do cliente, e converte tudo em atualizações da base de conhecimento. Fecha o loop qualidade → insight → conhecimento.
- **Por que consolidar:** Os três processam o mesmo material — as conversas de atendimento — para fins encadeados: auditar, entender e documentar. O QA descobre lacunas, a voz do cliente explica o porquê e o KB Curator corrige a fonte. Separados, ninguém fechava o loop; juntos, é um ciclo de melhoria contínua.
- **Squads irmãos:** QA de Conversas 100% (Quality Verifier), Voz do Cliente — Sentimento & Tendências, KB Curator

## Estrutura

```
ops-cs-qa-conversas-verifier/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
