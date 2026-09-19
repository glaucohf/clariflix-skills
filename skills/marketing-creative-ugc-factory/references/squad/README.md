# Creative UGC Factory

> De zero a 50 criativos testados por semana — sem esperar aprovação de agência, sem fadiga de anúncio paralisando escala.

**Área:** Marketing · **TopSquad:** M3 Conteúdo & Criativo · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

A escassez de criativos novos e o gargalo silencioso que paralisa o paid media: campanhas entram em fadiga, CTR colapsa, CAC dispara e a equipe nao tem velocidade de producao para cobrir os testes necessarios. O ciclo manual (briefing de agencia -> producao -> aprovacao -> upload -> analise -> novo briefing) leva 2-4 semanas e entrega 3-5 variacoes quando o algoritmo precisa de 30-50 para descobrir o criativo vencedor. O squad substitui esse ciclo por uma fabrica autonoma que, em 48-72h, gera ICP-driven creative briefs, produz variacoes sinteticas de copy e conceito visual, coordena producao de UGC real via plataformas como Hoox/Insense, valida brand voice via critic dedicado e enfileira os criativos aprovados para rotacao sistematica. O ciclo de descoberta de criativo vencedor cai de semanas para dias.

## Impacto esperado

Aumento estimado de 40-70% no CTR médio das campanhas via diversidade de ângulos e formatos testados sistematicamente (vs testar 3-5 variações/mês manualmente). Redução de 30-50% no CAC em 90 dias para clientes com budget >= R$20k/mês em paid media, pela eliminação de períodos de fadiga (que inflacionam CPM e destroem ROAS). Velocidade de descoberta de criativo vencedor reduzida de 3-6 semanas para 7-14 dias (ciclo completo: brief -> produção -> teste -> winner identificado). Volume de variações testadas: de 3-8/mês (manual) para 30-50/iteração (squad). ROI estimado: para cliente com R$50k/mês em mídia, cada ponto percentual de melhoria de CTR equivale a R$1.500-3.000/mês de budget liberado (menos CPM para mesma alcance) — o squad se paga com a primeira iteração vencedora.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — Maestro de Criativos | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `stella` · Stella | Stella — ICP & Insight Analyst | L1 · worker autônomo | `analisar-dados-e-intentoes.md` |
| `vega` · Vega | Vega — Creative Concept Architect | L1 · worker autônomo | `criar-conceitos-criativos.md` |
| `cruz` · Cruz | Cruz — Copy Performance Writer | L2 · orquestra / decide | `gerar-copy-performatica.md` |
| `hoox` · Hoox | Hóox — UGC Production Coordinator | L3 · aprovação humana | `coordenar-producao-de-ugc.md` |
| `sigma` · Sigma | Sigma — Synthetic Asset Generator | L2 · orquestra / decide | `gerar-ativos-sinteticos.md` |
| `nexus` · Nexus | Nexus — Creative Indexer & Tester | L2 · orquestra / decide | `indexar-criativos.md` |
| `aegis` · Aegis | Aegis — Brand Voice & Quality Critic | L2 · orquestra / decide | `avaliar-criativo-brand-voice.md` |
| `aegis-2` · Aegis 2 | Aegis — Brand Voice & Quality Critic | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-creative-ugc-factory:orion` (ou instale via `npx squads add ./marketing-creative-ugc-factory`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-creative-ugc-factory-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do squad operar — sem essa base o Aegis não tem referência para validar, e o squad não ativa
- Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento ao creator) — o Hoox gera o brief e aguarda aprovação explícita do humano responsável via Slack/WhatsApp antes de publicar. O cliente vê o brief completo, o perfil de creator selecionado e o custo estimado
- Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados anteriormente, o responsavel de midia revisa o preview antes da ativacao — as primeiras impressoes de um criativo novo sao irreversiveis
- Gate L3 — Escala de criativo vencedor acima de threshold de budget: quando o Nexus identifica um vencedor e o Orion recomenda escala (aumento de budget > X% acima do threshold pre-definido), o humano aprova o aumento antes da execução pelo squad de media buying (ou pelo cliente diretamente)
- Aprovação do ICP Creative Brief (apos cada ciclo da Stella): o cliente valida o mapa de dores/ângulos proposto pela Stella antes do Vega começar a conceitualização — garante que os insights estão corretos e alinhados com o momento estratégico da empresa
- Revisão do Preview Sheet semanal (opcional, recomendado): o Sigma gera um mosaico visual de todos os assets da semana — o cliente pode revisar e vetar conceitos antes do upload, mesmo que o Aegis já tenha aprovado (segunda camada de controle de qualidade à critério do cliente)
- Calibração mensal de thresholds: reunião de 30 minutos para revisar os thresholds de vencedor/arquivamento com base na performance real do mês — o squad opera com os parâmetros mais recentes aprovados
- Onboarding de novo creator no banco aprovado: qualquer creator novo (nao pre-validado) que va ser contratado pelo Hoox requer aprovacao do cliente antes de receber o brief — o cliente ve o perfil, o portfolio e o budget antes da contratacao

## KPIs

- Variações de criativo produzidas e aprovadas por ciclo semanal (target: >= 30 variações aprovadas pelo Aegis por ciclo — vs 3-5 do processo manual)
- Taxa de aprovação do Aegis na primeira iteração (target: >= 75% de copy e assets aprovados sem necessidade de revisão — indicador de qualidade do pipeline de produção)
- CTR médio das variações em teste por ciclo (target: melhoria de >= 20% no CTR médio vs criativos manuais do período anterior — mesma audiência, novo criativo)
- Tempo de ciclo completo (brief-to-live): do disparo do ciclo pela Stella até o primeiro criativo ativo na plataforma (target: <= 48h para criativos sintéticos; <= 7 dias para UGC real)
- Tempo de descoberta de criativo vencedor: da ativação do teste até declaração de winner com significância estatística (target: <= 10 dias vs 3-6 semanas manual)
- Percentual de criativos ativos no banco com CTR acima do baseline (target: > 60% das variações ativas performando acima do CTR baseline da conta)
- Custo por variação aprovada e ativa (target: <= R$150 por variação sintética; <= R$800 por UGC real com creator — vs R$2.000-5.000 por criativo via agência tradicional)
- Taxa de escala de criativos vencedores (target: >= 1 vencedor por ciclo que justifique escala de budget — indicador de que o sistema está descobrindo ângulos de conversão reais)
- Score de task success do squad no Langfuse (target: >= 95% em produção)
- NPS do cliente com o processo (target: >= 8/10 na avaliação quinzenal — indicador de que a fábrica está entregando qualidade percebida, não só volume)

## Integrações

- Meta Marketing API (MCP server) — Nexus cria e gerencia ad sets para teste de criativos; leitura de performance por variação para scoring
- Google Ads API (MCP server) — Nexus réplica estrutura de teste no Google; leitura de CTR/ROAS por criativo para o banco de dados
- Hoox / Insense API — Hoox publica briefs de creator, monitora status de entrega, recebe vídeos entregues automaticamente
- ClickUp (MCP server) — banco de criativos estruturado (board com todas as variações, status, scores, links de assets); toda ação do squad gera uma task auditável como prova de trabalho
- Slack (MCP server) — gates L3 (aprovação de briefs de UGC, aprovação de escala de vencedores); canal de notificação de vencedores identificados e de baixo estoque no banco de criativos
- WhatsApp Business API — canal alternativo para aprovações L3 urgentes fora do horário comercial
- Google Drive / Dropbox (MCP server) — repositório de brand assets (logo, fontes, fotos de produto) acessado pelo Sigma para geração de static ads
- Canva API — Sigma usa para geração programática de static ads com templates do cliente (quando o cliente usa Canva como ferramenta principal)
- HubSpot CRM (MCP server) — Stella acessa dados de clientes convertidos para extrair perfil de ICP com precisão (cargo, setor, objeção principal no ciclo de vendas)
- Langfuse (observabilidade OTEL) — rastreamento de todas as execuções de agentes, quality gates por fase (dev 70% / staging 85% / prod 95%), evals de qualidade de copy e de taxa de aprovação do Aegis
- Google Sheets — dashboard compartilhado com o cliente: score de cada criativo, número de variações ativas, CTR por conceito, vencedores da semana, status do banco de criativos
- n8n — automações complementares: webhook de notificação quando vídeo UGC é entregue pelo creator, sincronização de metadados entre ClickUp e planilha de criativos, disparo de email/Slack ao gestor quando vencedor é identificado

## Entregável (prova de trabalho)

Creative Performance Pack — entregável semanal automático gerado pelo Nexus e consolidado pelo Orion contendo: (1) Batch de Criativos Aprovados: lote de 30-50 variações aprovadas pelo Aegis com assets prontos para upload (imagens/vídeos + copy estruturada em JSON formatado para importação direta nas plataformas), (2) Preview Sheet Visual: mosaico de todos os assets da semana para revisão rápida do cliente, (3) Status do Banco de Criativos: dashboard de variações em teste / vencedoras / fatigadas / em produção (UGC pendente), (4) Relatório de Vencedores: criativos que atingiram significância estatística na semana com CTR, hook rate, ROAS e recomendação de escala, (5) ICP Brief do Próximo Ciclo: ângulos recomendados pela Stella para a wave seguinte com justificativa baseada em dados, (6) Log de Ações Auditável: todas as tasks executadas pelo squad no ClickUp com input, output e timestamps — prova de trabalho completa. Formato: PDF executivo (para o cliente) + JSON estruturado (para integração com ferramentas de mídia) + ClickUp board atualizado.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Instagram Caption Writer (7 agentes) — base direta para o pipeline de geração de copy do Cruz: reutilizar os padrões de variação de linguagem, estrutura de hooks e geração de múltiplas opções de CTA; adaptar o contexto de feed orgânico para ads pagos com ênfase em conversão
- Brainstormind (swarm 24 agentes, ideacao) — base para a etapa de conceitualizacao do Vega: o modelo de swarm de ideacao paralela pode gerar 20-30 conceitos de criativo simultaneamente com diversidade deliberada de angulos; filtrar os melhores antes de passar para producao
- Skeptic Protocol (5 agentes, red-team/QA) — base direta para o agente Aegis (Brand Voice & Quality Critic): o padrão de adversarial review do Skeptic Protocol se mapeia exatamente na função de critic/verifier do gate de copy e assets visuais antes de qualquer publicação

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M3 · TopSquad de Conteúdo & Criativo (UGC + SEO/GEO)** — Fábrica de criativos e conteúdo que ranqueia em buscadores e em LLMs.

- **Missão:** A máquina de produção de ativos: gera criativos UGC em escala para mídia paga/social e conteúdo programático otimizado para SEO tradicional e para GEO/AEO (ser citado por LLMs e respostas de IA). Um só motor de conteúdo, dois canais de distribuição.
- **Por que consolidar:** UGC e SEO programático são a mesma capacidade — gerar conteúdo de marca em escala — apontada a destinos diferentes (feed pago vs. busca/LLM). Compartilham a voz de marca, o briefing e o critic de qualidade. Um único motor evita duplicar a governança de conteúdo.
- **Squads irmãos:** Creative UGC Factory, Programmatic SEO + GEO/AEO

## Estrutura

```
marketing-creative-ugc-factory/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
