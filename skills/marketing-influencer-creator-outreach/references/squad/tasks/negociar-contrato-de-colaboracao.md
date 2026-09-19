---
task: contratoMaestro()
responsavel: "Contrato Maestro"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Creator Score e tier (Persona Fit Analyst)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Dossiê completo do creator (Radar Scout + dados de audiencia do Persona Fit Analyst)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Tabela de remuneracao por tier e tipo de entregavel configurada no onboarding (fee fixo por post, CPV, gifting + comissao, modelo hibrido)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Benchmarks de mercado atualizados por nicho e tier de seguidores (via pesquisa do Radar Scout + base historica de colaboracoes)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Template de contrato do cliente revisado pelo juridico"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Regras de gate L3: valor maximo para negociacao autonoma, categorias de creator que requerem aprovacao humana, tipos de entregavel que requerem aprovacao"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Para cada creator ativado: (1) Log de abordagem"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "canal usado, mensagem enviada, data, status de resposta"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Proposta comercial estruturada"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "escopo de entregaveis (quantidade, formato, prazo, plataforma), modelo de remuneracao com valor total e breakdown, clausulas especificas negociadas"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Contrato gerado a partir do template aprovado com dados do creator, escopo acordado e clausulas de LGPD, uso de imagem e rastreabilidade obrigatorias"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(4) Status de negociacao no ClickUp: Abordado / Em Negociacao / Proposta Enviada / Aguardando Aprovacao L3 / Contrato Assinado / Recusado"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Curator para creators com tag MATCH PERFEITO ou MATCH FORTE apos aprovacao pelo Parceiro Certo. Trigger de oportunidade: creator com mencao organica da marca detectado pelo Radar Scout c…"
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

# Negociar Contrato De Colaboração

**Task ID:** `contratoMaestro()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Influencer & Creator Outreach Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Negociar Contrato De Colaboração |
| **status** | `pending` |
| **responsible_executor** | Contrato Maestro (Contrato Maestro — O Negociador Estrategico) |
| **execution_type** | `Hybrid` |
| **input** | 6 item(ns) |
| **output** | 7 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Conduz o processo completo de ativacao do creator: primeiro contato via plataforma ou email, apresentacao da oportunidade de colaboracao com contexto personalizado, negociacao de escopo e remuneracao com base em benchmarks de mercado atualizados, e geracao do contrato de colaboracao. Usa o Score do Persona Fit Analyst e o historico de colaboracoes similares para negociar dentro dos parametros de budget com argumentacao baseada em dados. Personaliza o pitch de abordagem por tier de creator: micro-creators recebem abordagem mais proxima e informal com enfase no crescimento da parceria; mid-tier e macro recebem proposta formal com dados de audiencia do produto e historico de ROAS do canal. NUNCA envia proposta comercial sem aprovacao do Critic Parceiro Certo. NUNCA assina ou gera contrato acima do threshold L3 configurado sem aprovacao humana.

## Input

- Creator Score e tier (Persona Fit Analyst)
- Dossiê completo do creator (Radar Scout + dados de audiencia do Persona Fit Analyst)
- Tabela de remuneracao por tier e tipo de entregavel configurada no onboarding (fee fixo por post, CPV, gifting + comissao, modelo hibrido)
- Benchmarks de mercado atualizados por nicho e tier de seguidores (via pesquisa do Radar Scout + base historica de colaboracoes)
- Template de contrato do cliente revisado pelo juridico
- Regras de gate L3: valor maximo para negociacao autonoma, categorias de creator que requerem aprovacao humana, tipos de entregavel que requerem aprovacao

## Output

- Para cada creator ativado: (1) Log de abordagem
- canal usado, mensagem enviada, data, status de resposta
- (2) Proposta comercial estruturada
- escopo de entregaveis (quantidade, formato, prazo, plataforma), modelo de remuneracao com valor total e breakdown, clausulas especificas negociadas
- (3) Contrato gerado a partir do template aprovado com dados do creator, escopo acordado e clausulas de LGPD, uso de imagem e rastreabilidade obrigatorias
- (4) Status de negociacao no ClickUp: Abordado / Em Negociacao / Proposta Enviada / Aguardando Aprovacao L3 / Contrato Assinado / Recusado
- Para gates L3 ativados: notificacao ao gestor de marketing com proposta completa, score do creator e benchmarking de mercado para aprovacao com contexto total antes de qualquer envio

## Trigger

Ativado pelo Curator para creators com tag MATCH PERFEITO ou MATCH FORTE apos aprovacao pelo Parceiro Certo. Trigger de oportunidade: creator com mencao organica da marca detectado pelo Radar Scout com score >= 70 recebe abordagem prioritaria. Trigger de campanha: quando nova campanha e criada pelo time de marketing com budget e categoria definidos, Curator aciona o Contrato Maestro para os top creators elegidos da fila filtrada pelo Persona Fit Analyst. Re-trigger automatico em D+7 e D+14 se creator nao respondeu ao primeiro contato (follow-up com mensagem diferente).

## Knowledge base (o que o executor consulta)

- Benchmarks de remuneracao por plataforma, nicho e tier (2025-2026): micro Instagram fashion/beauty 10k-50k seguidores = R$300-800/post, 50k-100k = R$800-2.000/post
- TikTok micro = 30-40% a menos que Instagram por alcance mais organico
- macro 500k+ = R$3.000-15.000+/post dependendo do nicho
- Modelos de contrato por tipo de colaboracao: post patrocinado unico, pacote mensal com stories + Reels, embaixadora com exclusividade parcial, UGC para uso em ads (requer clausula especifica de direito de uso)
- Clausulas obrigatorias por modelo: LGPD e uso de dados, declaracao de publicidade (obrigacao legal CONAR), direito de uso de imagem para ads pagos (prazo, plataformas), clausula de exclusividade quando aplicavel
- Scripts de abordagem personalizados por tier: micro (tom de comunidade, enfase em co-criacao), mid-tier (dados de audiencia + proposta de valor mutua), macro (proposta executiva com deck se necessario)
- Historico de negociacoes anteriores do cliente: o que funcionou, o que nao funcionou, creators que recusaram e motivo

## Action Items

1. Confirmar o gatilho e carregar a entrada (Creator Score e tier (Persona Fit Analyst)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Para cada creator ativado: (1) Log de abordagem) e persistir no artefato do squad.
4. Entregar ao critic Parceiro Certo; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Para cada creator ativado: (1) Log de abordagem
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

- **to:** Brief Architect
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
