# Risk & Scenario Sentinel — Founder Early Warning Intelligence Squad

> Enquanto seu concorrente lê o jornal de ontem, o Sentinel já mapeou os três futuros regulatórios que vão remodelar seu mercado amanhã — e o founder recebe o alerta antes do mercado precificar.

**Área:** Founder Office · **TopSquad:** F4 Foresight, Risco & Research Estratégico · **Prioridade:** avançado · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Riscos regulatórios, geopolíticos e macro impactam a estratégia do founder mas são monitorados de forma reativa e fragmentada: o founder descobre a mudança regulatória quando o concorrente já adaptou o produto, o risco geopolítico aparece como choque no P&L em vez de aparecer como alerta no roadmap, e o risco macro (juros, câmbio, crédito) é tratado como força externa imprevisível em vez de variável monitorável com antecedência. O resultado é perda de vantagem competitiva, capital alocado em apostas invalidadas por mudança de ambiente, e energia do founder gasta em apagamento de incêndios que eram detectáveis com 30-90 dias de antecedência. Mensurável por: tempo médio de antecipação de evento de risco material (baseline: 0 dias — descoberta reativa; target: 30-90 dias de antecedência), número de alertas acionáveis emitidos por trimestre (target >= 6 alertas materiais/trimestre com recomendação de ação), % de decisões estratégicas tomadas com Risk Brief anterior à alocação de capital (target: 100% de apostas > R$50k com avaliação de risco prévia vs. baseline < 10%).

## Impacto esperado

ROI direto: uma única decisão de alocação de R$500k protegida por alerta regulatório antecipado — que evita investimento em linha de produto que será bloqueada por regulação — retorna 600x o custo mensal do squad. Estimativa conservadora para empresas com receita R$2M-20M/ano: prevenção de 1 evento de risco regulatório/geopolítico por semestre que custaria R$200k em retrabalho, multa ou perda de mercado gera R$400k/ano em risco protegido. Para a consultoria Lendar[IA]: este squad ancora o pilar Dados & Tecnologia da Founder Office como produto de inteligência estratégica contínua — diferencial de posicionamento máximo ('o único founder do seu setor que recebe alertas de risco antes do mercado precificar'). Ticket de implementação R$18-35k + recorrência R$8-18k/mês. Argumento de fechamento: 'Seu advogado lê o Diário Oficial quando a norma sai. O Sentinel lê a consulta pública 90 dias antes e já te diz o que mudar no produto.'

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `nexus` · Nexus | Nexus — O Estrategista de Riscos | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `lexis` · Lexis | Lexis — A Vigia Regulatória | L2 · orquestra / decide | `monitorar-risco-regulatorio.md` |
| `gaia` · Gaia | Gaia — O Radar Macro-Geopolítico | L2 · orquestra / decide | `estimar-impacto-financeiro.md` |
| `chronos` · Chronos | Chronos — O Arquiteto de Cenários de Risco | L2 · orquestra / decide | `analisar-riscos-estrategicos.md` |
| `vela` · Vela | Vela — A Guardiã de Tripwires | L2 · orquestra / decide | `monitorar-indicadores-tripwire.md` |
| `oraculo` · Oráculo | Oráculo — O Clone Estratégico do Expert | L1 · worker autônomo | `interpretar-riscos-estrategicos.md` |
| `cipher` · Cipher | Cipher — O Redator de Risk Briefs Executivos | L3 · aprovação humana | `redigir-risk-briefs-executivos.md` |
| `argos` · Argos | Argos — O Verificador de Inteligência | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-risk-scenario-sentinel:nexus` (ou instale via `npx squads add ./founder-risk-scenario-sentinel`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-risk-scenario-sentinel-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- INTAKE GATE — RISCO CRÍTICO (L3): Antes de disparar workers para investigação profunda, Nexus apresenta o Mapa de Exposição inicial ao founder quando o risco é classificado como Crítico (impacto estimado > R$200k ou impacto em licença/operação). O founder valida o escopo da investigação, confirma as agências e mercados a investigar, e aprova o nível de profundidade (scan rápido vs. deep dive). Para riscos Médios e Baixos, Nexus opera de forma autônoma sem gate obrigatório.
- RISCO EM MATERIALIZAÇÃO ATIVA — ALERTA CRÍTICO (L3): Quando Vela classifica um alerta como Crítico (risco está se materializando dentro da janela de resposta), o squad pausa toda recomendação de ação com impacto financeiro ou operacional e escalona para o founder com urgência máxima. O founder recebe: (a) o Evidence Report do Argos com fontes primárias que confirmam a materialização, (b) os cenários ativos de Chronos com janelas de resposta restantes, (c) as 3 ações prioritárias de Cipher. O founder deve responder com decisão explícita antes de qualquer ação ser executada.
- PREMISSA DE CENÁRIO INVERSAMENTE VALIDADA (L2): Quando Argos identifica que uma premissa central de um cenário ativo no Risk Register foi invalidada por nova evidência (ex: a norma que estava em consulta pública foi arquivada, alterando radicalmente o cenário regulatório), o squad notifica o founder com o impacto na matrix de cenários antes de atualizar o Risk Register. O founder confirma a revisão ou solicita novo ciclo de análise.
- BOARD/INVESTOR RISK UPDATE E COMUNICAÇÕES EXTERNAS (L3): Cipher nunca envia qualquer documento para audiência externa (board, conselheiros, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento produzido para audiência externa vai primeiro para Notion como draft com notificação Slack ao founder. Apenas após founder aprovar explicitamente (clique no botão 'Aprovar para envio' ou mensagem de aprovação no Slack) o envio é autorizado. Este gate é inviolável.
- CONFIGURAÇÃO DO ORÁCULO E CORPUS DO FOUNDER (L2): A configuração inicial do corpus do Oráculo (quais documentos, transcrições e decisões do founder são ingeridas) requer aprovação explícita item a item pelo founder. O founder define o que entra no corpus (controle de privacidade sobre decisões sensíveis) e o que fica fora. Atualizações mensais automáticas do corpus precisam de revisão semestral do founder para remoção de decisões desatualizadas.
- AJUSTE DE THRESHOLDS DE ALERTA (L2): Os thresholds de early-warning de Vela (o que configura Informativo vs. Atenção vs. Crítico para cada indicador) são configurados no onboarding e revisados trimestralmente com o founder. O founder pode ajustar thresholds via '/risk-config [indicador] [threshold]' mas qualquer ajuste que reduza a sensibilidade (aumenta threshold) requer justificativa explícita para evitar que o founder 'desligue' alertas por conveniência e depois seja pego de surpresa.

## KPIs

- Tempo médio de antecipação de evento de risco material — dias entre o alerta do Sentinel e a materialização pública do risco (target >= 30 dias de antecipação, baseline 0 — descoberta reativa)
- Número de alertas acionáveis emitidos por trimestre (alertas que geraram decisão ou ação do founder, não apenas leitura — target >= 6 alertas materiais/trimestre)
- Taxa de verificação de claims (% de claims materiais no Risk Brief com fonte primária verificada por Argos — target >= 85% para qualquer Brief entregue ao founder)
- False positive rate de alertas (% de alertas classificados como Crítico que não se materializaram em evento de risco real — target < 20%; acima disso indica necessidade de calibração de thresholds)
- % de decisões estratégicas do founder > R$50k com Risk Brief anterior à alocação de capital (target: 100%, baseline < 10%)
- Cobertura do Risk Register — número de riscos ativos monitorados com tripwire configurado (target: 100% dos riscos identificados em ciclos anteriores têm tripwire ativo)
- Tempo de ciclo de Risk & Scenario Brief completo — do intake à entrega ao founder (target < 3 horas para ciclo padrão, < 30 minutos para Emergency Brief)
- Acurácia de cenários: % de cenários materializados dentro do range de probabilidade e horizonte previstos após 6 meses (target >= 65% para cenário-base — proxy de calibração do Chronos)
- NPS do founder com o Risk & Scenario Brief (pesquisa pós-entrega — target >= 9/10; mede se o Brief é acionável e não apenas informativo)
- Custo por ciclo completo em tokens (target < R$600 por Risk Brief padrão, < R$1.200 por Emergency Deep Dive — monitorado via Langfuse)

## Integrações

- Slack (canal #sentinel-alerts — entrega de Risk & Scenario Briefs, alertas Críticos de Vela com menção direta ao founder, notificações de HITL Gates, digest semanal de sinais regulatórios e macro)
- Notion (Risk Knowledge Base central — armazenamento permanente de Risk Registers, Risk & Scenario Briefs históricos, Expert Lens Reports, Board Risk Updates, rastreabilidade completa de todos os riscos identificados e seus status)
- ClickUp (Risk Register integrado — cada risco identificado vira task com status de monitoramento, responsável, prazo de resposta e prova de trabalho do ciclo de análise; conectado ao projeto estratégico do founder)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente — gerencia paralelismo de Lexis/Gaia/Chronos, estado do Risk Register entre sessões, crons de monitoramento contínuo de Vela)
- Langfuse (observabilidade OTEL — tracing de custo por agente/token, evals de qualidade de alertas, dashboard de KPIs do Sentinel — taxa de verificação, false positive rate, tempo de antecipação, latência por fase do pipeline)
- API do Diário Oficial da União — LexML / DOU-API (Lexis usa para monitoramento em tempo real de publicações de normas e resoluções de agências reguladoras)
- Portais de Consulta Pública das Agências Reguladoras — BACEN, CVM, ANVISA, ANATEL, ANEEL, ANS via Web Scraping com MCP (Lexis usa para detectar consultas públicas antes da publicação final)
- API do Senado Federal — Legis / Câmara dos Deputados API (Lexis usa para acompanhamento de projetos de lei em tramitação com tags setoriais relevantes)
- API do BACEN — SGS e PTAX (Gaia e Vela usam para monitoramento em tempo real de Selic, câmbio, spreads de crédito e indicadores financeiros)
- Brave Search API / Perplexity API (Lexis, Gaia e Argos usam para web search de sinais, verificação de fontes primárias e coleta de evidências contrárias em tempo real)
- Google Alerts via RSS (Vela usa para monitoramento contínuo de termos críticos do setor — nome de reguladores relevantes, termos técnicos do produto/serviço, nomes de concorrentes em contexto regulatório)
- LinkedIn via MCP/Apify (Gaia e Vela usam para sinais de movimentos de reguladores, think tanks e policy makers relevantes para o setor do cliente)
- Vector DB — Pinecone ou Qdrant (armazenamento semântico do Risk Register histórico, corpus do founder para Oráculo, normas vigentes, cenários anteriores com outcomes — busca semântica para identificar padrões em riscos similares)
- Mem.ai / Sembly (ingestão contínua do corpus do founder para Oráculo — notas de reunião, decisões estratégicas, reflexões e frameworks explicitados em conversas)
- MCP Servers (camada de integração universal — cada ferramenta acima exposta como tool para os agents via protocolo MCP, permitindo Nexus rotear para as ferramentas corretas sem acoplamento direto)

## Entregável (prova de trabalho)

Risk & Scenario Brief — documento de inteligência estratégica entregue em Notion e Slack contendo: (1) Risk Register Snapshot — status atualizado de todos os riscos ativos com classificação de materialidade e urgência, sinalizando mudanças desde o último ciclo; (2) New Risk Alerts — novos riscos identificados no ciclo com fonte primária verificada por Argos, impacto estimado no modelo de negócio do cliente e janela de resposta disponível; (3) Scenario Matrix de Risco — 3 cenários estruturados (Adaptativo/Disruptivo/Bloqueio Total) com probabilidades bayesianas atualizadas, horizonte de materialização e ações de resposta por cenário; (4) Expert Lens — interpretação do mapa de riscos no raciocínio e frameworks do founder (quando corpus configurado — via Oráculo); (5) Action Recommendations — 3-5 ações concretas priorizadas por urgência com owner sugerido e prazo; (6) Watchlist Update — novos sinais adicionados ao monitoramento de Vela com thresholds configurados; (7) Verification Trail completo via Argos (% de claims verificados, fontes primárias, flags de claims não verificados). Entregue em três formatos: Founder Brief 1-página no Slack (leitura em 5 minutos), Risk Intelligence Report completo no Notion (detalhe técnico para consulta), e Board Risk Update trimestral formatado (L3 aprovação obrigatória). Frequência padrão: semanal para digest de monitoramento, imediato para alertas Críticos de Vela, trimestral para Board Risk Update.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — alinhamento direto com a arquitetura de pesquisa multi-source do Sentinel: a camada de síntese e verificação do Athenaeum pode acelerar a construção dos workers Lexis e Gaia, especialmente o pipeline de coleta de fontes primárias, parsing de documentos oficiais e síntese verificada que Argos precisa executar
- Skeptic Protocol (5 agentes, red-team/QA) — mapeia diretamente para Argos (Verificador): o protocolo de verificação adversarial, detecção de viés e red-team estruturado do Skeptic Protocol pode ser incorporado como base do fluxo de verificação do Argos, reduzindo o tempo de prompt engineering do critic
- Genius Athena Strange (5 agentes, decisão sob incerteza) — complementa o squad na fase de Chronos (Scenario Impact): raciocínio bayesiano e frameworks de decisão sob ambiguidade do Genius Athena Strange mapeiam para a construção de cenários probabilísticos de risco e o cálculo de janelas de resposta com probabilidades incertas

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F4 · TopSquad de Foresight, Risco & Research Estratégico** — Visão de futuro: cenários, riscos e pesquisa profunda para as apostas de alto risco.

- **Missão:** O squad que pensa o futuro: faz pesquisa estratégica profunda, simula cenários e wargaming de decisões grandes, e monitora riscos com alertas precoces. A munição analítica para as apostas de alto risco do founder.
- **Por que consolidar:** Os três alimentam a mesma decisão de alto risco: a pesquisa profunda dá o insumo, o wargaming simula os cenários e o risk sentinel vigia o que pode dar errado. É um pipeline único — pesquisar → simular → monitorar. Separados, a pesquisa não conversava com os cenários; unidos, viram um motor de decisão estratégica.
- **Squads irmãos:** Deep Research Estratégico, Strategic Foresight & Wargaming, Risk & Scenario Sentinel

## Estrutura

```
founder-risk-scenario-sentinel/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
