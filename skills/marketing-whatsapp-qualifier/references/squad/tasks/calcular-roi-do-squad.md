---
task: nova()
responsavel: "Nova"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados de qualificacao do squad (Lead Score, BANT, fonte), dados de CRM (oportunidades, deals fechados, valor, motivo de perda), dados de campanhas de aquisicao (budget, CPL por fonte), dados de agenda de Mia (reunioes realizadas, no-shows), ciclo de fechamento medio configurado pelo head de vendas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "ROI Report mensal: pipeline gerado pelo squad (R$), deals fechados atribuidos (R$), CAC por fonte de lead qualificado, taxa de conversao por etapa (lead -> qualificado -> reuniao -> oportunidade -> fechado), relatorio de perda pos-qualificacao (onde o closer perdeu leads qualificados pelo squad), recomendacao de redistribuicao de budget por fonte de lead com melhor ROI"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo mensal automatico (primeiro dia util do mes); Orion solicita analise de ROI para apresentacao ao cliente; deal marcado como fechado no CRM (trigger de atribuicao imediata); budget de campanha a…"
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

# Calcular ROI do Squad

**Task ID:** `nova()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** WhatsApp Qualifier

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular ROI do Squad |
| **status** | `pending` |
| **responsible_executor** | Nova (Nova — Attribution & ROI Agent) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Nova fecha o loop de atribuicao: conecta cada lead qualificado pelo squad ao deal fechado (ou perdido) no CRM e calcula o ROI real do squad em tempo real. Atribui pipeline a cada campanha, fonte e tipo de lead que passou pelo funil de qualificacao. Detecta onde o funil pós-qualificacao quebra (lead qualificou mas closer nao fechou — e problema de vendas, nao do squad). Produz o relatorio mensal de ROI que justifica o investimento no squad para o cliente e alimenta decisoes de budget de aquisicao. Diferente de Lilo (que olha para dentro do squad), Nova olha para o impacto de negocio completo.

## Input

- Dados de qualificacao do squad (Lead Score, BANT, fonte), dados de CRM (oportunidades, deals fechados, valor, motivo de perda), dados de campanhas de aquisicao (budget, CPL por fonte), dados de agenda de Mia (reunioes realizadas, no-shows), ciclo de fechamento medio configurado pelo head de vendas

## Output

- ROI Report mensal: pipeline gerado pelo squad (R$), deals fechados atribuidos (R$), CAC por fonte de lead qualificado, taxa de conversao por etapa (lead -> qualificado -> reuniao -> oportunidade -> fechado), relatorio de perda pos-qualificacao (onde o closer perdeu leads qualificados pelo squad), recomendacao de redistribuicao de budget por fonte de lead com melhor ROI

## Trigger

Ciclo mensal automatico (primeiro dia util do mes); Orion solicita analise de ROI para apresentacao ao cliente; deal marcado como fechado no CRM (trigger de atribuicao imediata); budget de campanha alterado (trigger de projecao de impacto)

## Knowledge base (o que o executor consulta)

- Mapeamento de atribuicao multi-touch (primeiro toque, ultimo toque, linear), historico de deals fechados com origem rastreada, modelo de CAC por fonte configurado, ciclo de fechamento medio por segmento, metas mensais de pipeline e revenue configuradas pelo head de vendas

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados de qualificacao do squad (Lead Score, BANT, fonte), dados de CRM (oportunidades, deals fechados, valor, motivo de…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (ROI Report mensal: pipeline gerado pelo squad (R$), deals fechados atribuidos (R$), CAC por fonte de lead qualificado,…) e persistir no artefato do squad.
4. Entregar ao critic Kira 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: ROI Report mensal: pipeline gerado pelo squad (R$), deals fechados atribuidos (R$), CAC por fonte de lead qualificado, taxa de conversao por etapa (lead -> qua…
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

- **to:** Kira 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
