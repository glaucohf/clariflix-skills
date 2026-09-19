---
task: personaFitAnalyst()
responsavel: "Persona Fit Analyst"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê bruto do creator (Radar Scout) com score de completude >= 60 para ser processado"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Creator Persona Matrix com pesos por dimensao configurados no Deep Dive"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Acesso a APIs de analise de audiencia: HypeAuditor (audience quality score, demografico real de seguidores, fake follower %) ou Modash (alternativa)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Historico de creators ativados anteriormente com seus ROAS reais para calibragem dos pesos (disponivel apos primeiros 90 dias)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Configuracao de budget por tier para calculo de viabilidade comercial"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Creator Score estruturado (0-100) com breakdown por 5 dimensoes: Audience-ICP Overlap (0-30"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "peso maior, mais preditivo de conversao), Content Relevance (0-25"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "nicho, linguagem, valores), Performance Score (0-20"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "engajamento real vs fake, saves, shares), Brand Safety Score (0-15"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "historico de parceria, red flags detectados), Commercial Track Record (0-10"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "uso de CTA, codigos de desconto, CTR estimado de posts patrocinados anteriores)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Automaticamente apos Radar Scout entregar dossiê com completude >= 60. Re-trigger trimestral para re-avaliar creators MATCH MODERADO ja na base — scores mudam com o crescimento do creator. Trigger ma…"
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

# Analisar Fit Creator

**Task ID:** `personaFitAnalyst()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Influencer & Creator Outreach Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Fit Creator |
| **status** | `pending` |
| **responsible_executor** | Persona Fit Analyst (Persona Fit Analyst — O Juiz de Fit) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 10 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Avalia cada creator descoberto pelo Radar Scout com base na Creator Persona Matrix em 5 dimensoes quantificadas. Cruza dados de audiencia do creator com o ICP do cliente usando ferramentas de analise de audiencia (HypeAuditor, Modash) para medir Audience-ICP Overlap real — nao assume fit por estetica ou nicho. Detecta audiencia fake (seguidores comprados, pods de engajamento) que invalida o creator independente das outras metricas. Produz o Creator Score com breakdown auditavel e classifica o creator em tier de prioridade para o Contrato Maestro. Opera de forma deterministica: pesos configurados, score com razao por dimensao, sem subjetividade. Retroalimenta os criterios de scoring com dados de performance real dos creators ativados (loop de aprendizado trimestral).

## Input

- Dossiê bruto do creator (Radar Scout) com score de completude >= 60 para ser processado
- Creator Persona Matrix com pesos por dimensao configurados no Deep Dive
- Acesso a APIs de analise de audiencia: HypeAuditor (audience quality score, demografico real de seguidores, fake follower %) ou Modash (alternativa)
- Historico de creators ativados anteriormente com seus ROAS reais para calibragem dos pesos (disponivel apos primeiros 90 dias)
- Configuracao de budget por tier para calculo de viabilidade comercial

## Output

- Creator Score estruturado (0-100) com breakdown por 5 dimensoes: Audience-ICP Overlap (0-30
- peso maior, mais preditivo de conversao), Content Relevance (0-25
- nicho, linguagem, valores), Performance Score (0-20
- engajamento real vs fake, saves, shares), Brand Safety Score (0-15
- historico de parceria, red flags detectados), Commercial Track Record (0-10
- uso de CTA, codigos de desconto, CTR estimado de posts patrocinados anteriores)
- Tag de prioridade: MATCH PERFEITO (>80, processar imediatamente), MATCH FORTE (60-80, processar em 24h), MATCH MODERADO (40-60, aguardar campanha especifica), DESCARTE (<40, arquivar com razao registrada)
- Flag de Audiencia Fake: TRUE = descarte automatico independente de outros scores, com razao documentada
- Atualizacao da fila do Curator e ClickUp com score e tier
- Log de auditoria por dimensao para revisao humana quando solicitado

## Trigger

Automaticamente apos Radar Scout entregar dossiê com completude >= 60. Re-trigger trimestral para re-avaliar creators MATCH MODERADO ja na base — scores mudam com o crescimento do creator. Trigger manual pelo Curator para re-avaliacao de creator especifico solicitada pelo time de marketing. Re-trigger automatico se creator MATCH FORTE ou PERFEITO for identificado como mencao organica da marca pelo Radar Scout.

## Knowledge base (o que o executor consulta)

- Modelo de scoring configuravel via YAML
- pesos por dimensao editaveis sem codigo pelo time de marketing
- Metricas de referencia por plataforma para deteccao de fake: HypeAuditor Audience Quality Score < 60 = flag automatico, follower growth suspeito (picos sem conteudo viral), engagement rate artificialmente alto com comentarios genericos
- Benchmarks de Audience-ICP Overlap por vertical: para moda feminina adulta, creator com >40% da audiencia mulheres 25-35 anos = overlap alto
- abaixo de 20% = overlap fraco
- Historico de scores de creators ativados com ROAS real para calibragem do modelo (disponivel apos 90 dias de operacao)
- Criterios de Brand Safety por cliente: categorias proibidas, concorrentes diretos a evitar, historico de polêmica que invalida o creator

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dossiê bruto do creator (Radar Scout) com score de completude >= 60 para ser processado).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Creator Score estruturado (0-100) com breakdown por 5 dimensoes: Audience-ICP Overlap (0-30) e persistir no artefato do squad.
4. Entregar ao critic Parceiro Certo; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Creator Score estruturado (0-100) com breakdown por 5 dimensoes: Audience-ICP Overlap (0-30
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

- **to:** Contrato Maestro
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
