---
task: kira()
responsavel: "Kira"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Playbook Conversacional draft (para auditoria pre-producao), sample de conversas do dia (para monitoramento em producao), regras Meta atualizadas (webhook de atualizacao de politicas BSP), checklist LGPD configurado, brand voice guidelines do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Audit Report do Playbook: APPROVED / NEEDS_REVISION / BLOCKED com lista de itens a corrigir por severidade (critico/aviso/sugestao), Compliance Score (0-100) por versao do playbook, Daily Monitoring Report com sample de conversas auditadas e flags de violacao detectadas, recomendacao de ajuste com exemplo de mensagem corrigida"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Sempre que uma nova versao do Playbook Conversacional e submetida para producao (gate obrigatorio); ciclo diario de auditoria de conversas (sample de 10-20%); alerta de atualizacao de politica Meta r…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Kira 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do squad ser configurado (L3, sem aprovacao o squad nao avanca)"
    - "[ ] HITL: Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e resposta a objecao. Kira ja auditou conformidade, mas humano decide se o tom esta certo (L3, gate obrigatorio)"
    - "[ ] HITL: Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior para assumir a conversa manualmente antes de Vance responder (L3, acao irreversivel: primeira impressao com conta estrategica)"
    - "[ ] HITL: Gate semanal de 30 minutos — head de vendas revisa 5-10 conversas de baixo desempenho selecionadas por Lilo, aprova ajustes de playbook propostos por Orion antes de Vance ser atualizado (L2, recorrente toda segunda-feira)"
    - "[ ] HITL: Aprovacao de nova versao do Playbook apos ajustes significativos (> 30% das mensagens alteradas) — qualquer revisao estrutural do playbook passa por gate L3 com head de vendas e Kira antes de producao"
---

# Validar Mensagem Playbook

**Task ID:** `kira()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** WhatsApp Qualifier

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Validar Mensagem Playbook |
| **status** | `pending` |
| **responsible_executor** | Kira (Kira — Compliance & Voice Guardian) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Kira e o gate de conformidade do squad: valida cada mensagem do playbook antes de ir para producao e monitora conversas em tempo real para detectar violacoes das regras Meta pos-proibicao, LGPD e brand voice do cliente. Pre-producao: audita o Playbook Conversacional completo contra checklist de restricoes Meta (sem mensagens em massa, sem templates genericos, compliance com BSP — Business Solution Provider), LGPD (consentimento, direito de opt-out, retencao de dados), e brand voice (tom, linguagem proibida, promessas que nao podem ser feitas). Em producao: monitora sample de conversas diariamente e alerta Orion se detectar padrao de violacao. Gate L3 obrigatorio: nenhuma versao do playbook vai para producao sem aprovacao de Kira.

## Input

- Playbook Conversacional draft (para auditoria pre-producao), sample de conversas do dia (para monitoramento em producao), regras Meta atualizadas (webhook de atualizacao de politicas BSP), checklist LGPD configurado, brand voice guidelines do cliente

## Output

- Audit Report do Playbook: APPROVED / NEEDS_REVISION / BLOCKED com lista de itens a corrigir por severidade (critico/aviso/sugestao), Compliance Score (0-100) por versao do playbook, Daily Monitoring Report com sample de conversas auditadas e flags de violacao detectadas, recomendacao de ajuste com exemplo de mensagem corrigida

## Trigger

Sempre que uma nova versao do Playbook Conversacional e submetida para producao (gate obrigatorio); ciclo diario de auditoria de conversas (sample de 10-20%); alerta de atualizacao de politica Meta recebido; Orion solicita auditoria emergencial apos reclamacao de lead

## Knowledge base (o que o executor consulta)

- Regras Meta para WhatsApp Business API pos-proibicao (atualizado mensalmente via BSP newsletters), checklist LGPD para conversas de qualificacao B2B (opt-in, opt-out, retencao), brand voice guidelines do cliente (tom, vocabulario aprovado e proibido, promessas permitidas), historico de violacoes anteriores com resolucao (para evitar reincidencia), politicas dos BSPs parceiros (Patagon AI, Leadsales, BotPenguin)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Playbook Conversacional draft (para auditoria pre-producao), sample de conversas do dia (para monitoramento em producao…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Audit Report do Playbook: APPROVED / NEEDS_REVISION / BLOCKED com lista de itens a corrigir por severidade (critico/avi…) e persistir no artefato do squad.
4. Entregar ao critic Kira 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Audit Report do Playbook: APPROVED / NEEDS_REVISION / BLOCKED com lista de itens a corrigir por severidade (critico/aviso/sugestao), Compliance Score (0-100) p…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Kira 2 registrado
- [ ] Gate HITL respeitado: Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do s…
- [ ] Gate HITL respeitado: Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e…
- [ ] Gate HITL respeitado: Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior par…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do squad ser configurado… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e resposta a objecao.… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior para assumir a conversa… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate semanal de 30 minutos — head de vendas revisa 5-10 conversas de baixo desempenho selecionadas por Lilo, aprova ajustes de playbook propostos por Orion ant… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovacao de nova versao do Playbook apos ajustes significativos (> 30% das mensagens alteradas) — qualquer revisao estrutural do playbook passa por gate L3 co… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Decisao de escalada por irritacao detectada — quando Vance detecta 3+ sinais de irritacao em sequencia, Orion alerta SDR humano via notificacao para assumir a… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao mensal de metricas com Nova — CEO/CMO aprova redistribuicao de budget por fonte de lead com base no ROI report de Nova (L3, envolve gasto financeiro) | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Kira 2 | BLOQUEIA entrega |

## Handoff

- **to:** Nova
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
