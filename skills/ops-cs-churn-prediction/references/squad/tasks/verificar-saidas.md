---
task: argusVerificar()
responsavel: "Argus"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguardando Aprovação' antes de ativar o CSM com essa ação específica"
    - "[ ] HITL: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualquer contato"
    - "[ ] HITL: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analista de dados"
    - "[ ] HITL: Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo batch"
    - "[ ] HITL: Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar"
---

# Verificar Saídas do Predição e Prevenção de Churn

**Task ID:** `argusVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Predição e Prevenção de Churn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Predição e Prevenção de Churn |
| **status** | `pending` |
| **responsible_executor** | Argus (Argus — Critic de Qualidade de Score e Ações) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Argus — Critic de Qualidade de Score e Acoes — Valida dois artefatos antes de qualquer disparo externo: (A) HEALTH SCORE — verifica se o score calculado pelo Prism e plausivel e consistente: score nao pode ter variacao > 25 pontos em 24h sem evento critico documentado (protecao contra anomalia de dados), os sinais de entrada devem estar todos presentes e dentro de range esperado (deteccao de dados faltantes ou corrompidos), o segmento correto foi aplicado para o modelo de pesos. Score invalido = reenvia para Prism com flag de dado suspeito. (B) BRIEF E NEXT-BEST-ACTION — valida o brief gerado pelo Mira em 4 dimensoes: (1) EVIDENCIA — toda afirmacao do brief tem sinal concreto que a suporta, nada inventado; (2) ACAO PROPORCIONAL — a acao recomendada e proporcional ao risco e ao perfil da conta (nao oferece desconto imediato para risco MEDIO, nao sugere email generativo para conta Enterprise em risco CRITICO); (3) COMPLETUDE — o CSM tem tudo que precisa para agir sem buscar mais informacao; (4) RISCO DE ACAO — acoes sensiveis (desconto acima de X%, cancelamento de feature, reuniao de exec sponsor) sao flaggeadas como L3 e requerem aprovacao humana antes do Spark criar a task com essa acao. Score minimo para aprovacao do brief: 36/40. Abaixo disso: devolve para Mira com feedback especifico.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Critic de Qualidade de Score e Acoes
- Valida dois artefatos antes de qualquer disparo externo: (A) HEALTH SCORE
- verifica se o score calculado pelo Prism e plausivel e consistente: score nao pode ter variacao > 25 pontos em 24h sem evento critico documentado (protecao contra anomalia de dados), os sinais de entrada devem estar todos presentes e dentro de range esperado (deteccao de dados faltantes ou corrompidos), o segmento correto foi aplicado para o modelo de pesos
- Score invalido = reenvia para Prism com flag de dado suspeito
- (B) BRIEF E NEXT-BEST-ACTION
- valida o brief gerado pelo Mira em 4 dimensoes: (1) EVIDENCIA
- toda afirmacao do brief tem sinal concreto que a suporta, nada inventado
- (2) ACAO PROPORCIONAL
- a acao recomendada e proporcional ao risco e ao perfil da conta (nao oferece desconto imediato para risco MEDIO, nao sugere email generativo para conta Enterprise em risco CRITICO)
- (3) COMPLETUDE
- o CSM tem tudo que precisa para agir sem buscar mais informacao
- (4) RISCO DE ACAO
- acoes sensiveis (desconto acima de X%, cancelamento de feature, reuniao de exec sponsor) sao flaggeadas como L3 e requerem aprovacao humana antes do Spark criar a task com essa acao
- Score minimo para aprovacao do brief: 36/40
- Abaixo disso: devolve para Mira com feedback especifico

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Nexus para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cri…
- [ ] Gate HITL respeitado: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de…
- [ ] Gate HITL respeitado: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguarda… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualque… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analis… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo b… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Brief com conflito entre next-best-action do Mira e comprometimento prévio do CSM registrado no CRM — Argus detecta e eleva para revisão humana antes de criar… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Primeiro alerta de churn em conta que nunca teve nenhuma ação de CS registrada (conta 'orphan') — escalona para Head de CS para atribuição e onboarding de rela… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Critic Argus reprova brief por evidência insuficiente (score < 36/40) após 2 iterações de melhoria — escalona para analista humano revisar os dados de entrada… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
