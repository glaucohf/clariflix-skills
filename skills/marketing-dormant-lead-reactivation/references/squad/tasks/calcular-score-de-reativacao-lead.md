---
task: oraculoScorer()
responsavel: "Oraculo Scorer"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ficha de Arqueologia (Arqueologa) com archetype e trilha sugerida"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Ficha de Sinais Novos (Radar) com força do sinal e janela de oportunidade"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Configuração de pesos do modelo editável pelo time (YAML)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Histórico de reativações anteriores do cliente (leads reativados vs não reativados e seus atributos) para calibragem do modelo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score de reativacao (0-100) com breakdown por dimensao: Archetype Fit (0-25, archetype que historicamente reativa mais para este cliente tem peso maior), Signal Strength (0-30, forca dos sinais novos e o preditor mais poderoso), Data Quality (0-20, email verificado + dados completos = pre-requisito), Time Sensitivity (0-15, timing prometido + recencia da mudanca), Deal Size Estimate (0-10, baseado em firmografico da empresa)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Tag de prioridade de processamento: RESSURGIR (>80, processar na proxima hora), QUENTE (60-80, processar hoje), MORNO (40-60, proxima rodada), ARQUIVO (< 40, mover para lista de baixa prioridade"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "nao descartar, apenas desprioritizar)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Trilha de Reativacao definitiva atribuida: qual das trilhas configuradas no Deep Dive se aplica"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Atualizacao automatica do CRM com score e trilha atribuida"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Log de auditoria completo com razao do score por dimensao"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado automaticamente após Radar entregar a ficha de sinais de cada lead. Re-trigger se novo sinal de intent for detectado para lead já com score calculado (pixel do site, resposta a email anterior…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Atena antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex: deal > R$20k) bloqueia completamente e notifica o gestor com draft completo, ficha de arqueologia e sinais novos para aprovacao ou rejeicao com 1 clique — nenhum caracter e enviado antes da aprovacao."
    - "[ ] HITL: Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovação humana obrigatória antes de entrar em sequência — agente não envia para dado não verificado."
    - "[ ] HITL: Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o gestor de marketing com o feedback completo do critic para reescritura ou descisao de nao envio."
    - "[ ] HITL: Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que disse, sugestão de próximo passo) — o squad paralisa qualquer automação para este lead e o vendedor assume o controle total da conversa."
    - "[ ] HITL: Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções de alto valor merecem resposta humana ou pelo menos validação antes de resposta automática."
---

# Calcular Score De Reativacao Lead

**Task ID:** `oraculoScorer()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Dormant Lead Reactivation

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Score De Reativacao Lead |
| **status** | `pending` |
| **responsible_executor** | Oraculo Scorer (Oraculo Scorer — O Priorizador de Ressurreicao) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Combina o archetype de dormencia (Arqueologa) com os sinais novos detectados (Radar) para calcular o score de probabilidade de reativacao de cada lead e re-ordenar a fila de trabalho do squad. Opera deterministicamente com os pesos configurados no onboarding — sem subjetividade. E o unico agente autorizado a definir a ordem de processamento da fila e a trilha de reativacao definitiva (confirmando ou ajustando a sugestao da Arqueologa com base nos sinais do Radar). Tambem define a urgencia: leads com janela de oportunidade fechando (timing prometido expirou, decisor recen-promovido que o interesse ja vira ruido em semanas) recebem FIRE independente do score base.

## Input

- Ficha de Arqueologia (Arqueologa) com archetype e trilha sugerida
- Ficha de Sinais Novos (Radar) com força do sinal e janela de oportunidade
- Configuração de pesos do modelo editável pelo time (YAML)
- Histórico de reativações anteriores do cliente (leads reativados vs não reativados e seus atributos) para calibragem do modelo

## Output

- Score de reativacao (0-100) com breakdown por dimensao: Archetype Fit (0-25, archetype que historicamente reativa mais para este cliente tem peso maior), Signal Strength (0-30, forca dos sinais novos e o preditor mais poderoso), Data Quality (0-20, email verificado + dados completos = pre-requisito), Time Sensitivity (0-15, timing prometido + recencia da mudanca), Deal Size Estimate (0-10, baseado em firmografico da empresa)
- Tag de prioridade de processamento: RESSURGIR (>80, processar na proxima hora), QUENTE (60-80, processar hoje), MORNO (40-60, proxima rodada), ARQUIVO (< 40, mover para lista de baixa prioridade
- nao descartar, apenas desprioritizar)
- Trilha de Reativacao definitiva atribuida: qual das trilhas configuradas no Deep Dive se aplica
- Atualizacao automatica do CRM com score e trilha atribuida
- Log de auditoria completo com razao do score por dimensao

## Trigger

Ativado automaticamente após Radar entregar a ficha de sinais de cada lead. Re-trigger se novo sinal de intent for detectado para lead já com score calculado (pixel do site, resposta a email anterior, mudança de cargo detectada pós-scoring). Re-trigger manual para reavaliação de lote pelo gestor quando novos dados de calibragem estiverem disponíveis.

## Knowledge base (o que o executor consulta)

- Modelo de scoring configurável
- pesos por dimensão editáveis sem código via YAML
- Histórico de reativações do cliente (o que o Lazaro consolida por rodada alimenta este KB)
- Tabela de archetype x probabilidade histórica de reativação (calibrada a cada rodada com dados reais)
- Regras de fast-track: lead com timing prometido expirado + email verificado = RESSURGIR automático
- Regras de exclusão: leads com opt-out registrado, leads em oportunidade ativa no CRM, clientes atuais = skip automático sem processamento

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ficha de Arqueologia (Arqueologa) com archetype e trilha sugerida).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score de reativacao (0-100) com breakdown por dimensao: Archetype Fit (0-25, archetype que historicamente reativa mais…) e persistir no artefato do squad.
4. Entregar ao critic Atena; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score de reativacao (0-100) com breakdown por dimensao: Archetype Fit (0-25, archetype que historicamente reativa mais para este cliente tem peso maior), Signa…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Atena registrado
- [ ] Gate HITL respeitado: Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configura…
- [ ] Gate HITL respeitado: Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança…
- [ ] Gate HITL respeitado: Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrig…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovaç… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que di… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Sinais de oportunidade detectados em lead que estava em ARQUIVO (score < 40): Radar detecta mudança significativa (investimento, mudança de decisor, sinal de i… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Relatório semanal de performance: Echo Analyst gera relatório de taxa de reativação por trilha e archetype entregue ao gestor todo friday — ponto de HITL estru… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Opt-out recebido: processamento automático cancela a sequência e atualiza o CRM, mas a decisão de blacklist permanente (nunca mais contatar) é sempre humana —… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Atena | BLOQUEIA entrega |

## Handoff

- **to:** Lázaro Writer
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
