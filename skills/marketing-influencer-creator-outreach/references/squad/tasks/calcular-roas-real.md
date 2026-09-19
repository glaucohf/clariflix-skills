---
task: roasTracker()
responsavel: "ROAS Tracker"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "URL de post publicado + data de publicacao (Content Guardian)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "UTM unico por creator configurado no sistema"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Codigo de desconto unico por creator com volume de usos (CRM ou plataforma de e-commerce)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Acesso a Google Analytics 4 (conversoes por UTM, sessoes, receita atribuida)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Meta Ads Manager e TikTok Ads Manager para rastreamento de conversoes em campanhas de amplificacao (boost de post de creator)"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Metricas de engajamento das plataformas (Instagram Graph API, TikTok Research API) para views, likes, comentarios, saves, shares, alcance estimado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dashboard de performance por creator (atualizado em 24h, 7 dias e 30 dias apos publicacao): { creator_handle, plataforma, campanha, data_publicacao, alcance_estimado, engajamento_total (likes+comentarios+saves+shares), taxa_engajamento_real, cliques_no_link (UTM), conversoes_atribuidas (codigos de desconto + UTM), receita_atribuida (R$), custo_da_colaboracao (R$), CPV (custo por visualizacao), CPA (custo por aquisicao), ROAS (receita/custo), ROI_vs_benchmark_do_tier }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatorio executivo mensal por campanha: top 5 creators por ROAS, top 5 por engajamento, padroes de conteudo que mais converteram (formato, duracao, tipo de hook, CTA usado), distribuicao de ROAS por tier (micro vs mid-tier vs macro), recomendacao de mix para proxima campanha"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Retroalimentacao automatica ao Persona Fit Analyst: atributos dos creators com ROAS >= 3x alimentam o modelo de scoring como sinais de alta predicao"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Recomendacao de renovacao de parceria: lista de creators com ROAS >= 2x e recomendacao de novo escopo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado automaticamente 24h apos confirmacao de publicacao pelo Content Guardian. Coleta de dados em D+1, D+7, D+14 e D+30 para cada post publicado. Trigger de alerta: ROAS abaixo de 0.5x em D+7 = no…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Parceiro Certo antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou R$5.000 dependendo do budget do cliente) bloqueia e notifica o gestor de marketing com proposta completa, score do creator e benchmarking de mercado para aprovacao antes de qualquer envio."
    - "[ ] HITL: Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evidencias coletadas para decisao humana de vetamento ou aprovacao com risco consciente — nunca o squad decide sozinho sobre risco de reputacao da marca."
    - "[ ] HITL: Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #publi) ou representacao incorreta do produto que requer revisao do time juridico ou de marketing antes de qualquer resposta ao creator."
    - "[ ] HITL: ROAS Tracker detecta ROAS >= 5x em D+7: alerta de oportunidade imediato ao gestor de marketing e ao time de performance para decisao de amplificacao via ads pagos do post do creator — decisao de investimento adicional e sempre humana."
    - "[ ] HITL: ROAS Tracker detecta ROAS < 0.5x em D+14: alerta ao gestor de marketing para revisao da estrategia de creator daquele nicho ou campanha — pode indicar desalinhamento de ICP ou problema de produto que nao deve ser escondido por mais investimento."
---

# Calcular Roas Real

**Task ID:** `roasTracker()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Influencer & Creator Outreach Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Roas Real |
| **status** | `pending` |
| **responsible_executor** | ROAS Tracker (ROAS Tracker — O Analistade Performance de Creator) |
| **execution_type** | `Worker` |
| **input** | 6 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora e consolida a performance de cada creator ativado desde a publicacao ate o final da janela de atribuicao (tipicamente 30 dias). Coleta metricas de engajamento da plataforma, rastreia conversoes via UTMs no Analytics e codigos de desconto no e-commerce/CRM, e calcula o ROAS real por creator, por campanha e por tier. Identifica os creators com melhor ROAS para priorizacao de renovacao de parceria e os padroes de conteudo que mais convertem para retroalimentar o Brief Architect. Entrega relatorio executivo de performance ao gestor de marketing e ao Curator para decisoes de investimento no canal. Fecha o loop de aprendizado do squad: todo ROAS real retroalimenta o modelo de scoring do Persona Fit Analyst (quais atributos de creator realmente predizem conversao para este cliente especifico).

## Input

- URL de post publicado + data de publicacao (Content Guardian)
- UTM unico por creator configurado no sistema
- Codigo de desconto unico por creator com volume de usos (CRM ou plataforma de e-commerce)
- Acesso a Google Analytics 4 (conversoes por UTM, sessoes, receita atribuida)
- Meta Ads Manager e TikTok Ads Manager para rastreamento de conversoes em campanhas de amplificacao (boost de post de creator)
- Metricas de engajamento das plataformas (Instagram Graph API, TikTok Research API) para views, likes, comentarios, saves, shares, alcance estimado

## Output

- Dashboard de performance por creator (atualizado em 24h, 7 dias e 30 dias apos publicacao): { creator_handle, plataforma, campanha, data_publicacao, alcance_estimado, engajamento_total (likes+comentarios+saves+shares), taxa_engajamento_real, cliques_no_link (UTM), conversoes_atribuidas (codigos de desconto + UTM), receita_atribuida (R$), custo_da_colaboracao (R$), CPV (custo por visualizacao), CPA (custo por aquisicao), ROAS (receita/custo), ROI_vs_benchmark_do_tier }
- Relatorio executivo mensal por campanha: top 5 creators por ROAS, top 5 por engajamento, padroes de conteudo que mais converteram (formato, duracao, tipo de hook, CTA usado), distribuicao de ROAS por tier (micro vs mid-tier vs macro), recomendacao de mix para proxima campanha
- Retroalimentacao automatica ao Persona Fit Analyst: atributos dos creators com ROAS >= 3x alimentam o modelo de scoring como sinais de alta predicao
- Recomendacao de renovacao de parceria: lista de creators com ROAS >= 2x e recomendacao de novo escopo

## Trigger

Ativado automaticamente 24h apos confirmacao de publicacao pelo Content Guardian. Coleta de dados em D+1, D+7, D+14 e D+30 para cada post publicado. Trigger de alerta: ROAS abaixo de 0.5x em D+7 = notificacao ao gestor de marketing para decisao de amplificacao (boost pago) ou encerramento da observacao. Trigger de sucesso: ROAS acima de 5x em D+7 = alerta imediato ao time de marketing para amplificacao via ads pagos (boost do post) e ao Curator para priorizar renovacao do creator. Trigger mensal automatico para relatorio executivo consolidado de campanha e retroalimentacao do modelo de scoring.

## Knowledge base (o que o executor consulta)

- Modelos de atribuicao por canal: last-click (codigo de desconto), data-driven (GA4 com UTM), view-through (amplificacao em Meta Ads)
- Janelas de atribuicao por produto: e-commerce impulso (7-14 dias), produto de maior ticket (14-30 dias), app/servico de assinatura (30-60 dias)
- Benchmarks de ROAS por categoria e tier para contextualizacao dos resultados: micro-creator fashion DTC ROAS benchmark 2-4x, micro-creator beleza 2.5-5x, mid-tier lifestyle 1.5-3x
- Metodologia de calculo de earned media value (EMV) para justificar campanhas de awareness onde conversao direta nao e o objetivo primario: alcance x CPM de referencia do nicho
- Padroes de conteudo com maior correlacao com conversao historica: videos com hook nos primeiros 2 segundos, uso do produto de forma integrada (nao so mostrando), CTA especifico com codigo de desconto exclusivo no final, depoimento genuino sem roteiro rigido perceptivel

## Action Items

1. Confirmar o gatilho e carregar a entrada (URL de post publicado + data de publicacao (Content Guardian)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dashboard de performance por creator (atualizado em 24h, 7 dias e 30 dias apos publicacao): { creator_handle, plataform…) e persistir no artefato do squad.
4. Entregar ao critic Parceiro Certo; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dashboard de performance por creator (atualizado em 24h, 7 dias e 30 dias apos publicacao): { creator_handle, plataforma, campanha, data_publicacao, alcance_es…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Parceiro Certo registrado
- [ ] Gate HITL respeitado: Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou…
- [ ] Gate HITL respeitado: Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evi…
- [ ] Gate HITL respeitado: Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #p…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou R$5.000 dependendo… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evidencias coletadas pa… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #publi) ou representac… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — ROAS Tracker detecta ROAS >= 5x em D+7: alerta de oportunidade imediato ao gestor de marketing e ao time de performance para decisao de amplificacao via ads pa… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — ROAS Tracker detecta ROAS < 0.5x em D+14: alerta ao gestor de marketing para revisao da estrategia de creator daquele nicho ou campanha — pode indicar desalinh… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Creator solicita ajuste contratual apos assinatura (exclusividade, prazo, valor, direitos de imagem ampliados): qualquer renegociacao apos contrato assinado e… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Content Guardian nao recebe rascunho em D-1 do deadline: escalacao urgente ao time de marketing para decisao sobre extensao de prazo ou substituicao do creator… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Persona Fit Analyst detecta queda >= 25% no score medio de ROAS por categoria de creator em 2 ciclos consecutivos de campanha: alerta estrategico ao gestor de… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Parceiro Certo | BLOQUEIA entrega |

## Handoff

- **to:** Parceiro Certo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
