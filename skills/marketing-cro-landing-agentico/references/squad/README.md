# CRO & Landing Page Agêntico

> De landing page estática para máquina de conversão autônoma: o squad gera, testa e itera copy e layout em loop contínuo — sem precisar de um time de CRO.

**Área:** Marketing · **TopSquad:** M2 Performance: Paid Media, CRO & Attribution · **Prioridade:** alta · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Landing pages estáticas são o gargalo silencioso de toda estratégia de aquisição. A empresa investe em tráfego pago (R$20-100k/mês em ads) mas a página converte 1-3% enquanto o benchmark do setor é 5-8%. O motivo não é falta de insight: é falta de mão de obra para rodar experimentos. O time de marketing não tem tempo de escrever 10 variações de headline, configurar testes A/B, esperar resultado, interpretar dados e iterar — e isso se repete em cada página, produto e segmento. Resultado mensurável: taxa de conversão da landing page principal abaixo de 3%, número de experimentos ativos simultâneos menor que 2 e lift por iteração não rastreado. O squad automatiza o ciclo completo: gera hipóteses de CRO baseadas em dados comportamentais, produz variações de copy e layout, configura experimentos, monitora resultados e itera autonomamente — com gate de aprovação humana antes de publicar mudanças no ar.

## Impacto esperado

Um aumento de 1 ponto percentual na taxa de conversão de uma landing page com 10.000 visitas/mês e ticket médio de R$500 representa R$50.000/mês em receita adicional. Empresas que operam CRO sistemático reportam lift acumulado de 30-80% em 6 meses de iteração contínua. Para um budget de R$50k/mês em tráfego pago, sair de 2% para 4% de conversão dobra o retorno sem aumentar um centavo em média. ROI estimado do squad: 3-6x em 90 dias sobre o investimento mensal. KPIs primários: taxa de conversão por página (meta: dobrar baseline em 90 dias), número de experimentos ativos em paralelo (meta: 5+ simultâneos), e lift médio por iteração (meta: > 8% por ciclo).

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro-cro` · Maestro CRO | Maestro CRO — Orquestrador de Experimentação | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `hera` · Hera | Hera — Behavioral Analyst | L2 · orquestra / decide | `identificar-abandono-pagina.md` |
| `sage` · Sage | Sage — CRO Research Agent | L2 · orquestra / decide | `pesquisar-evidencias-empiricas.md` |
| `muse` · Muse | Muse — Conversion Copywriter Agent | L2 · orquestra / decide | `gerar-copy-de-conversao.md` |
| `pixel` · Pixel | Pixel — Layout & UX Specs Agent | L1 · worker autônomo | `traduzir-hipoteses-de-layout.md` |
| `darwin` · Darwin | Darwin — Experiment Manager | L2 · orquestra / decide | `monitorar-experimentos-ab.md` |
| `rex` · Rex | Rex — Crític & Brand Voice Verifier | L3 · aprovação humana | `verificar-brand-voice-consistencia.md` |
| `atlas` · Atlas | Atlas — CRO Knowledge Base Agent | L1 · worker autônomo | `documentar-experimentos.md` |
| `rex-2` · Rex 2 | Rex — Crític & Brand Voice Verifier | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-cro-landing-agentico:maestro-cro` (ou instale via `npx squads add ./marketing-cro-landing-agentico`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-cro-landing-agentico-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3): a empresa precisa concordar com o diagnóstico antes de escalar produção
- Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de produto ou páginas com > 50% do budget de tráfego (L3): mudanças de alto impacto requerem olho humano final
- Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qualquer reescrita (L3)
- Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão estratégica que requer stakeholders (L3)
- Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, métrica primária e budget de tráfego (L3)
- Escalada de experimento inconclusivo após 4 semanas — Darwin alerta, Maestro analisa, mas decisão de encerrar ou aumentar tráfego para o teste e humana (L1): implica realocação de budget
- Revisao trimestral do CRO Playbook — Atlas apresenta o estado do conhecimento acumulado, Growth Lead decide quais learnings viram regras permanentes e quais hipoteses devem ser arquivadas (L1)

## KPIs

- Taxa de conversão por página: meta de dobrar o baseline em 90 dias (ex: de 2% para 4%) — KPI primário do squad
- Número de experimentos ativos em paralelo: meta de 5+ simultâneos após 60 dias de operação (baseline típico: 0-2)
- Lift médio por ciclo de iteração: meta > 8% de melhora por experimento vencedor (rastreado pelo Darwin e Atlas)
- Velocidade de aprendizado (throughput): meta de 2 experimentos concluídos por semana em regime de cruzeiro (30 dias+)
- Taxa de vencedores vs perdedores vs inconclusivos: meta de 30%+ de taxa de vencedores (benchmark indústria: 1 em 7 testes ganha — o squad mira em 1 em 3 com hipóteses mais embasadas)
- Message Match Score (Rex): 100% das variações publicadas com score de alinhamento ad-landing acima de 8/10
- Tempo médio de ciclo (hipótese aprovada -> experimento no ar): meta < 5 dias úteis
- CRO Playbook: >= 20 learnings documentados com evidencia nos primeiros 90 dias
- Lift acumulado em 6 meses: meta de 30-60% de aumento de conversão sobre baseline (compounding de experimentos vencedores)

## Integrações

- Google Analytics 4 — fonte primária de dados de conversão, funil de comportamento por fonte/dispositivo/segmento, eventos de objetivo configurados por página
- Hotjar ou Microsoft Clarity — heatmaps, gravações de sessão, scroll depth maps e pesquisas on-exit; Hera é o principal consumidor desta integração
- Google Optimize / VWO / Unbounce Smart Traffic / Optimizely — ferramentas de teste A/B e multivariado; Darwin configura e monitora experimentos aqui (escolha depende da stack do cliente)
- Unbounce / Webflow / WordPress + Elementor — construtores de landing page onde as variações são implementadas pelo time após aprovação de Rex
- HubSpot CRM — tracking de leads gerados por variação de landing page (UTM parameters por variação para atribuição de pipeline), integração de formulário com campos de source/medium/experiment_id
- Google Ads / Meta Ads — source de tráfego das campanhas; Rex verifica message match entre o ad e a landing page antes de publicar variação
- ClickUp — prova de trabalho: task automática por experimento (hipótese, resultado, learning), dashboard de KPIs de CRO (taxa de conversão por página, experimentos ativos, lift acumulado), backlog de hipóteses como lista priorizada
- Figma / Whimsical — Pixel deposita wireframes e specs de layout como artefatos verificáveis antes de implementação
- Langfuse — observabilidade OTEL de todos os agentes, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de custo por ciclo de experimentação
- n8n — orquestração de webhooks entre GA4, ferramentas de teste e ClickUp (alertas de significância estatística, notificações de anomalia de conversão, triggers de ciclo quinzenal)
- Slack / Email — notificações de experimento encerrado com resultado, alertas de anomalia de conversão e despacho de relatório quinzenal de velocidade de aprendizado para stakeholders

## Entregável (prova de trabalho)

CRO Operations Package — artefato verificável completo por ciclo quinzenal: (1) CRO Audit Report inicial com mapa de fricções e top-10 hipóteses priorizadas por ICE Score; (2) Experiment Packages por wave (hipótese documentada, variações de copy Muse, specs de layout Pixel, configuração Darwin, aprovação Rex); (3) Experiment Conclusion Reports individuais com vencedor/perdedor, lift absoluto/relativo, intervalo de confiança e learning documentado; (4) CRO Playbook vivo e versionado com todos os learnings acumulados (o ativo mais valioso do squad — não vai embora com o agente, fica com o cliente); (5) Velocity Dashboard no ClickUp com taxa de conversão por página, experimentos ativos, lift médio e backlog priorizado; (6) Relatório Executivo Quinzenal para CMO/Growth Lead com resumo de resultados, próximo ciclo planejado e ROI estimado do portfolio de experimentos.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Landing Funnel (13 agentes, landing/CRO) — squad gratuito mais diretamente alinhado: estrutura de geração e otimização de landing pages já implementada, reutilizar a lógica de geração de variações e o pipeline de publicação, customizando para o loop de experimentação autônoma com gate L3
- Skeptic Protocol (5 agentes, red-team/QA) — acelera a construção do agente Rex (Critic): o padrão de verificação adversarial, checklist de qualidade e lógica de APPROVED/NEEDS_REVISION/BLOCKED já está implementado, basta customizar as regras para brand voice e compliance de copy de conversão
- Athenaeum (11 agentes, inteligencia estrategica) — acelera o modulo de research do Sage: estrutura de coleta, sintese e priorizacao de inteligencia competitiva reutilizavel diretamente no benchmark de copy de concorrentes e na fase de Discovery de CRO

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M2 · TopSquad de Performance: Paid Media, CRO & Attribution** — O loop fechado da mídia: investe, otimiza a página, acerta o timing e prova o que deu retorno.

- **Missão:** O ciclo fechado de performance: aloca e otimiza mídia paga, melhora a landing page para converter, dispara no melhor horário e mede a atribuição real — fechando o loop investir → converter → medir → reinvestir.
- **Por que consolidar:** Mídia, CRO, timing e atribuição são o mesmo loop de otimização visto de ângulos diferentes — e a atribuição é justamente o sinal que deveria realimentar a mídia. Em squads isolados, o de mídia não enxergava o que a atribuição via, e o de CRO otimizava cego. Unidos, a medição fecha o ciclo.
- **Squads irmãos:** Paid Media Autopilot, CRO & Landing Page Agêntico, Intelligent Timing Orchestrator, Funnel Analytics & Attribution

## Estrutura

```
marketing-cro-landing-agentico/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
