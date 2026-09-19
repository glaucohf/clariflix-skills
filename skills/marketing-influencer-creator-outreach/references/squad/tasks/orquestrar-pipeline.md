---
task: curatorPipeline()
responsavel: "Curator"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de campanha de creator verificado, rastreavel e com ROAS mensuravel por criativo: (1) Creator Score Card por creator ativado (Persona Fit Analyst) com breakdown por 5 dimensoes, flag de audiencia fake e tier de prioridade"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "salvo no ClickUp e linkado ao lead no CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Dossiê de brand safety verificado (Parceiro Certo Camada 1) com validacao de historico de polêmica, compliance com CONAR e alinhamento de valores"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "artefato obrigatorio antes de qualquer contrato"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Proposta comercial e contrato assinado digitalmente (Contrato Maestro) com escopo, remuneracao, clausulas de uso de imagem para ads e rastreabilidade"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "versionado no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Decompoe a meta de creators ativados por mes em subtarefas distribuidas aos workers na sequencia correta. Mantem o estado de cada creator no pipeline — desde a descoberta ate o pagamento e analise de…"
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

# Orquestrar Pipeline do Influencer & Creator Outreach Agentico

**Task ID:** `curatorPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Influencer & Creator Outreach Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Influencer & Creator Outreach Agentico |
| **status** | `pending` |
| **responsible_executor** | Curator (Curator — O Diretor de Parcerias) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 13 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Decompoe a meta de creators ativados por mes em subtarefas distribuidas aos workers na sequencia correta. Mantem o estado de cada creator no pipeline — desde a descoberta ate o pagamento e analise de ROAS. Decide a prioridade de processamento com base no score de fit, urgencia da campanha e disponibilidade de budget. Orquestra o fluxo Radar Scout -> Persona Fit Analyst -> Contrato Maestro -> Brief Architect -> Content Guardian -> ROAS Tracker. Consolida todos os artefatos de uma campanha em um pacote rastreavel no ClickUp. Monitora os quality gates no Langfuse e escalona para HITL sempre que um gate falha ou uma acao irreversivel (contrato, pagamento, publicacao) esta prestes a acontecer. Gerencia o calendario de campanhas, a distribuicao de budget por tier de creator e a coerencia do mix de conteudo (awareness vs conversao). Opera em L2: executa o ciclo completo de orquestracao autonomamente, com gates L3 bloqueando o fluxo para aprovacao humana antes de contratos, pagamentos e aprovacao final de conteudo.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pacote de campanha de creator verificado, rastreavel e com ROAS mensuravel por criativo: (1) Creator Score Card por creator ativado (Persona Fit Analyst) com breakdown por 5 dimensoes, flag de audiencia fake e tier de prioridade
- salvo no ClickUp e linkado ao lead no CRM
- (2) Dossiê de brand safety verificado (Parceiro Certo Camada 1) com validacao de historico de polêmica, compliance com CONAR e alinhamento de valores
- artefato obrigatorio antes de qualquer contrato
- (3) Proposta comercial e contrato assinado digitalmente (Contrato Maestro) com escopo, remuneracao, clausulas de uso de imagem para ads e rastreabilidade
- versionado no ClickUp
- (4) Briefing criativo personalizado aprovado pelo Parceiro Certo (Brief Architect) com UTM unico, codigo de desconto exclusivo e checklist de conformidade
- enviado ao creator e arquivado
- (5) Log de publicacao verificado (Content Guardian) com URL do post, data/hora, resultado da verificacao de 7 pontos e status de arquivo no banco de UGC
- (6) Dashboard de ROAS por creator (ROAS Tracker) com metricas em D+1, D+7, D+14 e D+30, atribuicao cruzada de UTM + codigo de desconto e recomendacao de renovacao ou encerramento de parceria
- relatorio executivo mensal com mix recomendado para proxima campanha
- Todo o pipeline e auditavel por design: cada artefato tem agente responsavel, timestamp, veredicto do Parceiro Certo e rastro no Langfuse
- O gestor de marketing opera os gates L3 e ve o contexto completo de cada creator e campanha em um unico painel no ClickUp

## Trigger

Decompoe a meta de creators ativados por mes em subtarefas distribuidas aos workers na sequencia correta. Mantem o estado de cada creator no pipeline — desde a descoberta ate o pagamento e analise de ROAS. Decide a prioridade de processamento com base no score de fit, urgencia da campanha e disponibilidade de budget. Orquestra o fluxo Radar Scout -> Persona Fit Analyst -> Contrato Maestro -> Brief Architect -> Content Guardian -> ROAS Tracker. Consolida todos os artefatos de uma campanha em um pacote rastreavel no ClickUp. Monitora os quality gates no Langfuse e escalona para HITL sempre que um gate falha ou uma acao irreversivel (contrato, pagamento, publicacao) esta prestes a acontecer. Gerencia o calendario de campanhas, a distribuicao de budget por tier de creator e a coerencia do mix de conteudo (awareness vs conversao). Opera em L2: executa o ciclo completo de orquestracao autonomamente, com gates L3 bloqueando o fluxo para aprovacao humana antes de contratos, pagamentos e aprovacao final de conteudo.

## Knowledge base (o que o executor consulta)

- Creator Marketplaces com base opt-in: Insense (foco em e-commerce e DTC, creators ja acostumados a UGC para ads), Hoox (video UGC com IA), Squid (maior marketplace brasileiro de influenciadores)
- Analise de audiencia de creators: HypeAuditor (audience quality score, demografico real de seguidores, fake follower detection, historico de crescimento) ou Modash como alternativa, ambos com API
- CRM: HubSpot (MCP disponivel
- gestao do pipeline de creators como leads, historico de colaboracoes, status de contrato, log de pagamentos) ou Salesforce como alternativa
- Analytics e atribuicao: Google Analytics 4 (conversoes por UTM, sessoes, receita atribuida ao canal de creator), Meta Pixel e TikTok Pixel para rastreamento de conversoes em posts amplificados
- E-commerce: Shopify ou WooCommerce (geracao e rastreamento de codigos de desconto unicos por creator, receita diretamente atribuida por codigo)
- Plataformas de ads para amplificacao: Meta Ads Manager (boost de posts de creators aprovados, criacao de Dark Posts com UGC de alta performance) e TikTok Ads Manager (Spark Ads com autorizacao do creator)
- Gestao de tarefas e prova de trabalho: ClickUp (artefatos verificaveis por creator e por campanha
- dossiê, score, contrato, briefing aprovado, log de publicacao, relatorio de ROAS) conectado ao Curator via MCP ou webhook
- Biblioteca de UGC: Google Drive ou Notion (armazenamento e tagging de conteudos aprovados para reutilizacao em ads pagos)
- pode ser substituido por DAM dedicado como Bynder ou Brandfolder em operacoes maiores
- Comunicacao com creators: email (contato formal, contratos), WhatsApp Business API para creators brasileiros (followup de prazo, confirmacao de publicacao), DM via plataforma quando aplicavel
- Orquestracao multi-agente: LangGraph (controle de estado do pipeline por creator
- desde descoberta ate ROAS final) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (traces OTEL por agente, quality gates dev 70% / staging 85% / prod 95% task success, alertas de anomalia no pipeline)
- No-code complementar: n8n para automacoes de integracao (webhooks de publicacao, sincronizacao de CRM, notificacoes de HITL, alertas de deadline) sem codigo custom adicional
- Social listening para mencoes organicas: Mention, Brand24 ou Sprout Social para detectar creators que falam da marca sem parceria (fast-track para abordagem prioritaria)
- Assinatura digital de contratos: DocuSign ou Contraktor (mercado brasileiro) para contratos com creators assinados digitalmente com validade juridica

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Parceiro Certo antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de campanha de creator verificado, rastreavel e com ROAS mensuravel por criativo: (1) Creator Score Card por creator ativado (Persona Fit Analyst) com b…
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

- **to:** Radar Scout
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
