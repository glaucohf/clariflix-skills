---
task: atenaVerificar()
responsavel: "Atena"
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
    - "[ ] HITL: Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex: deal > R$20k) bloqueia completamente e notifica o gestor com draft completo, ficha de arqueologia e sinais novos para aprovacao ou rejeicao com 1 clique — nenhum caracter e enviado antes da aprovacao."
    - "[ ] HITL: Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovação humana obrigatória antes de entrar em sequência — agente não envia para dado não verificado."
    - "[ ] HITL: Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o gestor de marketing com o feedback completo do critic para reescritura ou descisao de nao envio."
    - "[ ] HITL: Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que disse, sugestão de próximo passo) — o squad paralisa qualquer automação para este lead e o vendedor assume o controle total da conversa."
    - "[ ] HITL: Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções de alto valor merecem resposta humana ou pelo menos validação antes de resposta automática."
---

# Verificar Saídas do Dormant Lead Reactivation

**Task ID:** `atenaVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Dormant Lead Reactivation

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Dormant Lead Reactivation |
| **status** | `pending` |
| **responsible_executor** | Atena (Atena — A Guardiã da Segunda Chance) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Atena — A Guardiã da Segunda Chance — Valida CADA draft de reativação gerado pelo Lázaro Writer antes de qualquer envio. Checklist obrigatório de 10 pontos — reprovar em qualquer item bloqueia o envio: (1) Ausência do ângulo falhado: a mensagem usa ZERO elementos da abordagem original que não funcionou? Qualquer repetição do ângulo arquivado pela Arqueóloga = REPROVADO automaticamente — reativação com o mesmo pitch que já falhou e pior que não enviar; (2) Ancoragem em mudança real: a mensagem referencia pelo menos UMA mudança detectada pelo Radar com dado específico e verificável? 'Vi que voces expandiram para o Sul em março' e aprovado; 'vi que voces cresceram muito' = REPROVADO; (3) Reconhecimento respeitoso do histórico: a mensagem menciona o contato anterior de forma natural e sem constrangimento? Nunca fingir que é um primeiro contato quando não é; (4) CTA calibrado ao archetype: o chamado para ação está alinhado com o archetype de dormência — lead que disse 'não é o momento' recebe CTA leve (recurso, conteúdo), não proposta comercial direta; (5) Tom não-desesperado: mensagem de reativação não pode soar como desespero de vendas ou pressão — tom de genuína curiosidade e proposta de valor é o único aprovado; (6) Compliance LGPD reativação: menção explícita ao contato anterior (evidência de relação previa e base legal), mecanismo de opt-out claro, não usa dados que o lead não tornou públicos além do contexto B2B normal; (7) Brevidade e respeito: email de reativação max 120 palavras (menos que cold outreach porque o lead já conhece a empresa — não precisa de educação, precisa de razão para retomar), WhatsApp max 2 blocos curtos, LinkedIn max 250 caracteres; (8) Subject line verificada: max 50 caracteres, sem 'Re:' falso, sem 'follow-up' (clichê que reduz abertura em 30%), sem emojis excessivos para B2B, contendo pelo menos 1 elemento específico do lead ou da mudança detectada; (9) Sequência coerente: se é toque 2 ou 3, a mensagem constroi sobre o silêncio anterior de forma natural — não repete o mesmo pitch, escala sutilmente o valor ou muda o ângulo; (10) Última mensagem com graça: se é o toque final da sequência (fechamento), tem a 'porta aberta' — frase de encerramento respeitosa que não queima a relação e facilita opt-out sem drama. Veredicto: APROVADO (segue para Charon Dispatcher) / REESCREVER com instruções específicas por ponto reprovado (volta ao Lázaro Writer, max 1 ciclo automático) / BLOQUEAR_HITL para casos que exigem revisão humana (dados inconsistentes no dossiê, ângulo de reativação ambíguo, flag de compliance crítico).

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- A Guardiã da Segunda Chance
- Valida CADA draft de reativação gerado pelo Lázaro Writer antes de qualquer envio
- Checklist obrigatório de 10 pontos
- reprovar em qualquer item bloqueia o envio: (1) Ausência do ângulo falhado: a mensagem usa ZERO elementos da abordagem original que não funcionou? Qualquer repetição do ângulo arquivado pela Arqueóloga = REPROVADO automaticamente
- reativação com o mesmo pitch que já falhou e pior que não enviar
- (2) Ancoragem em mudança real: a mensagem referencia pelo menos UMA mudança detectada pelo Radar com dado específico e verificável? 'Vi que voces expandiram para o Sul em março' e aprovado
- 'vi que voces cresceram muito' = REPROVADO
- (3) Reconhecimento respeitoso do histórico: a mensagem menciona o contato anterior de forma natural e sem constrangimento? Nunca fingir que é um primeiro contato quando não é
- (4) CTA calibrado ao archetype: o chamado para ação está alinhado com o archetype de dormência
- lead que disse 'não é o momento' recebe CTA leve (recurso, conteúdo), não proposta comercial direta
- (5) Tom não-desesperado: mensagem de reativação não pode soar como desespero de vendas ou pressão
- tom de genuína curiosidade e proposta de valor é o único aprovado
- (6) Compliance LGPD reativação: menção explícita ao contato anterior (evidência de relação previa e base legal), mecanismo de opt-out claro, não usa dados que o lead não tornou públicos além do contexto B2B normal
- (7) Brevidade e respeito: email de reativação max 120 palavras (menos que cold outreach porque o lead já conhece a empresa
- não precisa de educação, precisa de razão para retomar), WhatsApp max 2 blocos curtos, LinkedIn max 250 caracteres
- (8) Subject line verificada: max 50 caracteres, sem 'Re:' falso, sem 'follow-up' (clichê que reduz abertura em 30%), sem emojis excessivos para B2B, contendo pelo menos 1 elemento específico do lead ou da mudança detectada
- (9) Sequência coerente: se é toque 2 ou 3, a mensagem constroi sobre o silêncio anterior de forma natural
- não repete o mesmo pitch, escala sutilmente o valor ou muda o ângulo
- (10) Última mensagem com graça: se é o toque final da sequência (fechamento), tem a 'porta aberta'
- frase de encerramento respeitosa que não queima a relação e facilita opt-out sem drama
- Veredicto: APROVADO (segue para Charon Dispatcher) / REESCREVER com instruções específicas por ponto reprovado (volta ao Lázaro Writer, max 1 ciclo automático) / BLOQUEAR_HITL para casos que exigem revisão humana (dados inconsistentes no dossiê, ângulo de reativação ambíguo, flag de compliance crítico)

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Lazaro para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Lazaro
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
