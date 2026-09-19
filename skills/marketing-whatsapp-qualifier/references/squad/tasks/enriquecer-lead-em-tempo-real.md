---
task: rex()
responsavel: "Rex"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Numero de telefone e nome do lead (da mensagem de entrada), empresa mencionada (se houver), fonte do lead (utm_source/utm_campaign do CRM), ICP Data Model atual (do squad Living ICP Profiler ou versao simplificada local)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lead enrichment record com: empresa, cargo, tamanho da empresa, setor, stack tecnologico (se disponivel), historico CRM (cliente anterior? lead frio?), ICP Fit Score preliminar (0-10), tier de prioridade (1/2/3), flag de duplicata (lead ja em pipeline ativo?), dados injetados no contexto de Vance antes da segunda mensagem"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Vance recebe primeira mensagem de lead desconhecido (< 10 segundos apos trigger de Vance); ciclo de re-enriquecimento semanal de leads em nurture; Orion solicita enrichment adicional para lead de alt…"
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

# Enriquecer Lead Em Tempo Real

**Task ID:** `rex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** WhatsApp Qualifier

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Lead Em Tempo Real |
| **status** | `pending` |
| **responsible_executor** | Rex (Rex — Real-Time Enrichment Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Em paralelo ao primeiro contato de Vance, Rex enriquece o lead em tempo real para que Vance tenha contexto antes da segunda mensagem. Executa cascata de enriquecimento rapida (< 30 segundos): primeiro tenta match por telefone no CRM (lead ja conhecido?), depois por nome+empresa no Clay/Apollo se disponivel, depois LinkedIn lookup via MCP. Calcula ICP Fit Score preliminar e injeta no contexto de Vance. Se empresa for tier 1 (acima do threshold de tamanho/fit), alerta Orion para escalada prioritaria para SDR humano sênior. Atualiza o registro no CRM com todos os dados coletados.

## Input

- Numero de telefone e nome do lead (da mensagem de entrada), empresa mencionada (se houver), fonte do lead (utm_source/utm_campaign do CRM), ICP Data Model atual (do squad Living ICP Profiler ou versao simplificada local)

## Output

- Lead enrichment record com: empresa, cargo, tamanho da empresa, setor, stack tecnologico (se disponivel), historico CRM (cliente anterior? lead frio?), ICP Fit Score preliminar (0-10), tier de prioridade (1/2/3), flag de duplicata (lead ja em pipeline ativo?), dados injetados no contexto de Vance antes da segunda mensagem

## Trigger

Vance recebe primeira mensagem de lead desconhecido (< 10 segundos apos trigger de Vance); ciclo de re-enriquecimento semanal de leads em nurture; Orion solicita enrichment adicional para lead de alta prioridade

## Knowledge base (o que o executor consulta)

- ICP Fit Score model (atributos e pesos por dimensao), mapeamento de fontes de enriquecimento disponiveis (CRM first, Clay segundo, Apollo terceiro, LinkedIn ultimo), historico de leads CRM (para detectar duplicatas e clientes anteriores), thresholds de tier por tamanho de empresa e setor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Numero de telefone e nome do lead (da mensagem de entrada), empresa mencionada (se houver), fonte do lead (utm_source/u…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lead enrichment record com: empresa, cargo, tamanho da empresa, setor, stack tecnologico (se disponivel), historico CRM…) e persistir no artefato do squad.
4. Entregar ao critic Kira 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lead enrichment record com: empresa, cargo, tamanho da empresa, setor, stack tecnologico (se disponivel), historico CRM (cliente anterior? lead frio?), ICP Fit…
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

- **to:** Mia
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
