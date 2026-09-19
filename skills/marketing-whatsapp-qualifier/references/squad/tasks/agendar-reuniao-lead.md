---
task: mia()
responsavel: "Mia"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal de lead qualificado de Vance (Lead Score >= threshold), dados do lead enriquecidos por Rex, disponibilidade do closer via Calendar API, janelas de horario pre-configuradas por Orion (dias/horas de melhor show-rate), preferencia de horario mencionada pelo lead na conversa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Agendamento confirmado no calendario do closer, evento criado com dados do lead (empresa, cargo, BANT summary, Link CRM), mensagem de confirmacao enviada ao lead via WhatsApp com data/hora e link de videoconferencia, tarefa criada no ClickUp para o closer com briefing pre-reuniao, lembrete automatico agendado (24h e 1h antes)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Vance sinaliza Lead Score >= threshold de qualificacao; lead responde positivamente a convite de reuniao; no-show detectado (reuniao passou sem entrada no meet) — trigger de reengajamento; lead cance…"
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

# Agendar Reunião Lead

**Task ID:** `mia()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** WhatsApp Qualifier

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Agendar Reunião Lead |
| **status** | `pending` |
| **responsible_executor** | Mia (Mia — Smart Scheduling Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Quando Vance qualifica um lead (Lead Score >= threshold configurado), Mia assume o agendamento diretamente na conversa do WhatsApp. Mia consulta a disponibilidade real do closer/SDR sênior via integracao com Google Calendar ou Calendly, oferece 3 opcoes de horario dentro de janelas pre-configuradas (dias/horarios de melhor show-rate baseado em historico), confirma o agendamento e envia o invite. Envia lembrete automatico 24h e 1h antes da reuniao. Se lead cancela, Mia reengaja imediatamente com opcoes alternativas (nao deixa lead esfriar). Detecta no-show e dispara fluxo de reengajamento de Vance.

## Input

- Sinal de lead qualificado de Vance (Lead Score >= threshold), dados do lead enriquecidos por Rex, disponibilidade do closer via Calendar API, janelas de horario pre-configuradas por Orion (dias/horas de melhor show-rate), preferencia de horario mencionada pelo lead na conversa

## Output

- Agendamento confirmado no calendario do closer, evento criado com dados do lead (empresa, cargo, BANT summary, Link CRM), mensagem de confirmacao enviada ao lead via WhatsApp com data/hora e link de videoconferencia, tarefa criada no ClickUp para o closer com briefing pre-reuniao, lembrete automatico agendado (24h e 1h antes)

## Trigger

Vance sinaliza Lead Score >= threshold de qualificacao; lead responde positivamente a convite de reuniao; no-show detectado (reuniao passou sem entrada no meet) — trigger de reengajamento; lead cancela reuniao agendada — trigger de reagendamento imediato

## Knowledge base (o que o executor consulta)

- Historico de show-rate por dia da semana e horario (para priorizar slots de melhor performance), regras de disponibilidade do closer por semana (fora de bloqueios), scripts de confirmacao e lembrete por WhatsApp aprovados pelo head de vendas, fluxo de reengajamento pos-no-show (ate 3 tentativas antes de marcar como lost)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sinal de lead qualificado de Vance (Lead Score >= threshold), dados do lead enriquecidos por Rex, disponibilidade do cl…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Agendamento confirmado no calendario do closer, evento criado com dados do lead (empresa, cargo, BANT summary, Link CRM…) e persistir no artefato do squad.
4. Entregar ao critic Kira 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Agendamento confirmado no calendario do closer, evento criado com dados do lead (empresa, cargo, BANT summary, Link CRM), mensagem de confirmacao enviada ao le…
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

- **to:** Lilo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
