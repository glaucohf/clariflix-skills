# Investor & Fundraising Ops — Founder Office

> Do mapeamento de investidores ao data room blindado: o founder chega no roadshow com a narrativa testada contra as objeções mais duras — sem gastar meses para preparar.

**Área:** Founder Office · **TopSquad:** F5 Investor Relations, Fundraising & M&A · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Captação consome o founder por 3–6 meses de forma fragmentada: mapeamento de investidores é ad-hoc e sem critério de fit, o data room está sempre incompleto na hora errada, a narrativa nunca foi testada contra as objeções reais de VCs, e o founder entra no roadshow sem saber onde estão os buracos da tese. Mensurável por: (1) cobertura do data room — % de documentos requeridos por VCs tier-1 que estão prontos e atualizados (baseline típico: <50%); (2) número de objeções de VC antecipadas e com contra-argumento preparado (baseline: 0–2, ad-hoc); (3) tempo de preparo do roadshow — horas do founder para estar pronto para primeiro LP/VC meeting (baseline: 4–12 semanas de trabalho intenso).

## Impacto esperado

Uma rodada fechada 60–90 dias mais cedo equivale a 2–3 meses de runway preservado e menor dilução por urgência. Para uma startup em Série A (valuation R$30–80M), cada mês de antecipação vale R$500k–1.5M em equity preservado. Redução de tempo de preparo do roadshow de 8–12 semanas para 2–3 semanas (economia de 6–9 semanas do founder = 200–300h recuperadas). Cobertura do data room de <50% para 95%+ em 30 dias — elimina o motivo mais frequente de atraso em due diligence (dado faltante). Taxa de conversão de first meeting para second meeting estimada +25–40% quando founder chega com contra-argumentos preparados para as 15 objeções mais comuns do perfil do investidor alvo. ROI direto estimado: R$800k–3M em valor preservado por rodada + 200–300h do founder recuperadas.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — Fundraising Ops Orchestrator | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `vega` · Vega | Vega — Investor Intelligence & Universe Mapper | L1 · worker autônomo | `mapear-investidores-relevantes.md` |
| `atlas` · Atlas | Atlas — Data Room Builder & Compliance Auditor | L1 · worker autônomo | `auditar-documentos-faltantes.md` |
| `pallas` · Pallas | Pallas — Narrative Architect & Pitch Strategist | L1 · worker autônomo | `construir-narrativa-investimento.md` |
| `brutus` · Brutus | Brutus — VC Objection Simulator & Stress Tester | L1 · worker autônomo | `simular-objecoes-vcs.md` |
| `hermes` · Hermes | Hermes — Outreach Sequencer & Pipeline Tracker | L2 · orquestra / decide | `gerenciar-funil-investimento.md` |
| `mnemo` · Mnemo | Mnemo — Knowledge Graph & Founder Memory | L0 · worker determinístico | `organizar-conhecimento-estrategico.md` |
| `gate` · Gate | Gate — HITL Compliance & External Send Controller | L3 · aprovação humana | `controlar-envio-externo.md` |
| `hades` · Hades | Hades — Verifier, Hallucination Guard & Red-Team Analyst | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-fundraising-ops:orion` (ou instale via `npx squads add ./founder-fundraising-ops`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-fundraising-ops-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass possível
- Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto, NDA status, versão do documento, nível de acesso)
- Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide quais vulnerabilidades abordar proativamente vs deixar sem abordar
- Aprovação do Investor Universe Map ranqueado antes de iniciar qualquer outreach — founder confirma critérios de fit, remove investidores indesejados e ajusta priorização
- Validação do Data Room Gap Report pelo founder antes de Atlas começar a gerar rascunhos de documentos faltantes — founder decide quais gaps fechar internamente vs delegar à IA para rascunho
- Aprovação da Pitch Narrative Framework pelo founder antes de qualquer variante ser usada em meeting — founder valida o posicionamento, o use of funds e o valuation target antes de comunicar ao mercado
- Configuração inicial do Knowledge Graph do Mnemo — founder autoriza explicitamente quais fontes de dados históricos (emails, transcrições) podem ser ingeridas e quem tem acesso
- Qualquer mudança nos termos da rodada refletida nos artefatos (ticket, valuation, estrutura) requer aprovação explícita antes de Hermes atualizar mensagens de outreach ou Atlas atualizar documentos do data room

## KPIs

- Data Room Readiness Score (Atlas) — baseline <50%, meta: 95%+ em 30 dias de operação
- Número de objeções mapeadas com contra-argumento preparado (Brutus) — baseline 0–2 ad-hoc, meta: 25+ estruturadas antes do roadshow
- Tempo de preparo do roadshow (founder-hours) — baseline 8–12 semanas, meta: 2–3 semanas com squad operacional
- Score de fit médio dos investidores no pipeline ativo (Vega) — meta: média >=7.5/10 nos top 20 abordados
- Taxa de conversão first contact → first meeting — baseline estimado 5–10%, meta: 15–25% com outreach personalizado
- Taxa de conversão first meeting → second meeting — baseline estimado 20–30%, meta: 40–55% com prep de objeções
- % de claims no deck e data room com fonte rastreável (Hades score) — meta: 95%+ antes do primeiro meeting
- Tempo de geração de Investor Intelligence Brief por investidor (Vega) — meta: <30 minutos end-to-end
- % de objeções reais em meetings previstas pelo Objection Playbook do Brutus (validado pelo founder pós-meeting) — meta: >=65% das objeções recebidas já estavam no playbook
- Audit trail completude (Gate) — meta: 100% das comunicações externas logadas com destinatário, versão, timestamp e aprovador
- Task success rate no Langfuse — meta: dev 70% / staging 85% / prod 95%
- NPS do founder com o squad após o primeiro roadshow concluído — meta: >=9/10

## Integrações

- Crunchbase / PitchBook dados públicos (mapeamento de portfólios de VCs e histórico de investimentos para o Vega)
- LinkedIn API / Sales Navigator (warm intro path mapping, perfis de GPs e managing partners para o Vega e Mnemo)
- EXA / Perplexity MCP (pesquisa em tempo real de atividade de investidores, teses publicadas, notícias de mercado)
- Gmail / Outlook MCP (histórico de comunicações com investidores para o Mnemo, envio controlado via Gate)
- Google Drive / Notion (repositório do data room, versionamento de documentos pelo Atlas)
- Dealroom / Captable.io / Carta (cap table atualizado, documentos de rodadas anteriores para o Atlas)
- Stripe / QuickBooks / Conta Azul (dados financeiros reais para o financial model e métricas do Atlas)
- HubSpot / Salesforce CRM (cohort de clientes, churn, expansão, CAC — métricas de tração para Atlas e Brutus)
- Mixpanel / Amplitude / PostHog (métricas de produto, DAU/MAU, NPS, engagement para o data room)
- ClickUp (Roadshow Tracker — pipeline de captação, tasks, follow-ups, audit trail de toda a operação)
- Sembly / Fireflies / Otter.ai (transcrições automáticas de meetings com investidores para o Mnemo)
- Langfuse (observabilidade OTEL — tracing de tokens, custo por agente, task success rate por pipeline)
- Vector DB — Pinecone / Qdrant (Knowledge Graph do Mnemo, corpus de Intelligence Briefs do Vega, histórico de narrativas)
- Slack (interface conversacional do founder com o Orion — recebe alertas, approva mensagens, consulta status do roadshow)
- DocSend / Docsend-compatible viewer (rastreamento de visualização do data room — quem abriu, quanto tempo em cada seção)

## Entregável (prova de trabalho)

Fundraising Readiness Package — artefato verificável e auditável entregue antes do roadshow, composto de: (1) Investor Universe Map ranqueado com 80–150 investidores e score de fit, warm intro paths e Intelligence Briefs individuais para os top 20; (2) Data Room completo e auditado com 95%+ dos documentos requeridos, cada dado rastreável à fonte e versão controlada; (3) Pitch Narrative Framework com one-liner, elevator pitch, estrutura de deck por slide e variantes por perfil de investidor; (4) Objection Playbook com 25–40 objeções categorizadas, contra-argumentos com dado de suporte e Top 5 'buracos da tese' com plano de mitigação; (5) Roadshow Tracker no ClickUp com pipeline de investidores, sequência de outreach personalizada pronta para aprovação e dashboard de funil; (6) Knowledge Graph inicial da operação de captação (Mnemo) populado com histórico disponível. Após roadshow iniciado: atualização contínua do Objection Playbook com objeções reais recebidas, briefing pré-meeting 48h antes de cada reunião e relatório semanal de funil com projeção de fechamento.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — base para o pipeline de deep research do Vega (mapeamento de teses, portfólios e perfis de investidores) e para o modelo de síntese com citações inline do Hades (verificação de claims de mercado e benchmark)
- Skeptic Protocol (5 agentes, red-team/QA) — base para a arquitetura adversarial do Brutus (simulação de VCs com personas distintas, stress test da narrativa) e para o modo red-team narrativo do Hades (challenger de claims do pitch)
- Genius Athena Strange (5 agentes, decisão sob incerteza) — base para o Scenario/Wargaming component do Brutus (simulação de futuros competitivos, análise de cenários de mercado que VCs usarão para questionar a tese) e para o framework de priorização de objeções por nível de risco para a rodada

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F5 · TopSquad de Investor Relations, Fundraising & M&A** — Tudo que toca capital: board, captação e aquisições.

- **Missão:** O squad do capital: gere a relação com board e investidores (updates, comunicação), opera o fundraising (pipeline de investidores, data room) e conduz o screening de due diligence/M&A. Tudo que envolve dinheiro de fora, num motor só.
- **Por que consolidar:** Os três giram em torno do mesmo público — investidores e capital — e da mesma fonte de verdade (métricas, data room, cap table). O update de board usa os mesmos números do fundraising; o due diligence consome o mesmo data room. Separados, mantinham três cópias da verdade financeira; unidos, uma só.
- **Squads irmãos:** Board & Investor Relations, Investor & Fundraising Ops, Due Diligence / M&A Screening

## Estrutura

```
founder-fundraising-ops/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
