# Squad de Higiene e Enriquecimento de CRM (RevOps)

> Seu CRM e o solo onde toda venda cresce — se o solo é lixo, a colheita também é.

**Área:** Vendas · **TopSquad:** V6 RevOps: Higiene de CRM & Forecast · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Dados sujos, duplicados e incompletos no CRM destroem scoring, roteamento e personalização. SDRs perdem 30-40% do tempo corrigindo registros manualmente. Closers ligam para leads mortos. Automações disparam para o contato errado. O squad elimina deduplicação manual, preenche campos críticos em branco (cargo, setor, CNPJ, telefone, intent), sincroniza entre fontes e mantém um golden record atualizado continuamente — transformando o CRM em fundação confiável para todos os squads downstream.

## Impacto esperado

Reduz tempo de limpeza manual de CRM de ~8h/semana para <30min (economia de 93%). Aumenta taxa de entrega de email de 62% para >90% com dados validados. Melhora acurácia do lead scoring em +35% com campos enriquecidos. Reduz custo de outreach desperdiçado em leads duplicados/inválidos em ~25%. ROI estimado: R$15k-40k/mês em produtividade recuperada para equipes de 3-10 vendedores. Payback em 30-60 dias pós-implantação.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `nexus` · Nexus | Nexus (Orquestrador de Integridade de Dados) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `validador-de-entradas` · Validador de Entradas | Argos (Validador de Entradas) | L0 · worker determinístico | `validar-formato-de-entradas.md` |
| `detector-de-duplicatas` · Detector de Duplicatas | Gemini (Detector de Duplicatas) | L1 · worker autônomo | `detectar-duplicatas.md` |
| `enriquecedor-de-conta-e-lead` · Enriquecedor de Conta e Lead | Atlas (Enriquecedor de Conta e Lead) | L2 · orquestra / decide | `consultar-fontes-confianca.md` |
| `sincronizador-de-fontes` · Sincronizador de Fontes | Hermes (Sincronizador de Fontes) | L2 · orquestra / decide | `propagar-atualizacoes-fonte.md` |
| `pythia` · Pythia | Pythia (Scorer de Qualidade de Registro) | L0 · worker determinístico | `calcular-score-registro.md` |
| `cassandra` · Cassandra | Cassandra (Detectora de Sinais de Intenção e Rotting) | L2 · orquestra / decide | `detectar-sinais-de-intencao.md` |
| `gerador-de-golden-record` · Gerador de Golden Record | Midas (Gerador de Golden Record) | L3 · aprovação humana | `gerar-golden-record.md` |
| `sentinel` · Sentinel | Sentinel (Verificador de Integridade e Red-Team) | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-higiene-enriquecimento-crm-revops:nexus` (ou instale via `npx squads add ./vendas-higiene-enriquecimento-crm-revops`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-higiene-enriquecimento-crm-revops-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual)
- Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3)
- Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez)
- Revisão de registros Golden Bronze com deal aberto (operador RevOps decide: enriquecer manualmente ou descartar deal)
- Configuração inicial do playbook de golden record no onboarding (quem decide vence em cada campo — decisão estratégica do cliente)
- Aprovação de integração de nova fonte de dados ao pipeline (ex: adicionar novo formulário ou importação de lista de parceiro)

## KPIs

- Taxa de completude de campos criticos (target: >90% dos registros com cargo, email, telefone e empresa preenchidos)
- Taxa de duplicatas na base (target: <2% após implantação, medido mensalmente)
- Score médio de qualidade de registro (target: média Gold >80 para base ativa)
- Tempo médio de enriquecimento por registro (target: <90 segundos do trigger ao golden record atualizado)
- Taxa de bounce de email na base (target: <5% apos higiene continua)
- Custo por registro enriquecido (target: <R$0.50/registro usando waterfall com fallback entre provedores)
- Taxa de mérges revertidos pelo húmano (índicador de qualidadê do Gemini — târget: <10% de réversal ratê)
- Cobertura de sync downstream (target: 100% dos campos críticos sincronizados em <1h após update no CRM)

## Integrações

- CRM: HubSpot (MCP disponível), Pipedrive, Salesforce — source of truth de contatos e companies
- Enriquecimento: Apollo.io (275M+ contatos B2B), Clay (waterfall multi-source), Clearbit (dados de empresa)
- Email validation: ZeroBounce ou NeverBounce (verificação de MX record e caixa ativa)
- WhatsApp Business API: sync de numero validado e opt-in status
- Plataforma de email (ActiveCampaign / Mailchimp / RD Station): sync de contatos e status de bounce
- ClickUp: artefatos verificáveis por task, fila HITL, dashboard de qualidade de CRM
- Langfuse (OTEL): observabilidade de cada agente, quality gates dev 70% / staging 85% / prod 95%
- Slack: alertas de anomalia, fila HITL para aprovação de merges
- LangGraph: orquestração do pipeline com estado persistente entre etapas
- N8N (opcional): webhook receiver para fontes de entrada não-nativas (ex: formulário do site, planilha do SDR)

## Entregável (prova de trabalho)

Golden Record Dashboard: relatório semanal exportado para ClickUp e enviado ao operador RevOps com: score agregado da base (Gold/Silver/Bronze distribution), top 20 registros Bronze com deal aberto (prioritários para ação manual), log de merges da semana (quantidade, campos afetados, revertidos), custo de enriquecimento consumido vs budget, alertas de Cassandra pendentes de ação, e gráficos de tendência de qualidade ao longo do tempo. Cada ciclo de processamento gera um artefato imutável de auditoria no ClickUp com hash de integridade.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 ag, qualidade de dados) — base direta para lógica de validação, deduplicação e scoring de qualidade; adaptar os agentes de detecção de anomalia e validação de schema para o contexto de CRM B2B brasileiro
- Mae Intuitiva CRM (CRM/leads) — lógica de enriquecimento e gestão de leads no contexto brasileiro; reutilizar padrões de integração com HubSpot e fluxo de qualificação de contatos
- Skeptic Protocol (5 ag, red-team/QA) — estrutura do crític/verifier para o Sentinel; adaptar o loop de red-team para verificação pós-higiene e detecção de falsos positivos em merges

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V6 · TopSquad de RevOps: Higiene de CRM & Forecast** — Dados limpos viram previsão confiável — o sistema nervoso do pipeline.

- **Missão:** A camada de verdade do funil: mantém o CRM limpo e enriquecido (dedupe, normalização, campos faltantes) e, sobre esses dados confiáveis, projeta o forecast e sinaliza deals em risco antes que escorreguem.
- **Por que consolidar:** Forecast só é confiável sobre dados limpos — eram causa e efeito separados em dois squads. O squad de higiene gerava o insumo que o de forecast consumia. Unidos, a limpeza acontece a serviço da previsão, num loop contínuo de qualidade-de-dado → previsão.
- **Squads irmãos:** Higiene e Enriquecimento de CRM (RevOps), Forecast de Pipeline & Risco de Deal

## Estrutura

```
vendas-higiene-enriquecimento-crm-revops/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
