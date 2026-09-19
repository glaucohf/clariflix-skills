---
task: lilo()
responsavel: "Lilo"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados de conversas do Vance (status, Lead Score, objecoes registradas, etapa de abandono), dados de agendamento de Mia (show-rate, cancelamentos, no-shows), dados de enriquecimento de Rex (fontes de lead, ICP Fit Score), metricas do CRM (oportunidades criadas, deals fechados de leads qualificados pelo squad)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dashboard semanal de metricas (taxa de qualificacao, show-rate, objecoes top 5, funil de abandono por etapa), Anomaly Report quando KPI cai > 15% vs semana anterior, recomendacao de ajuste de playbook (quais perguntas/objecoes estao gerando mais abandono), analise de correlacao fonte-de-lead vs qualificacao (qual campanha traz o melhor lead), briefing de 5 linhas para gate HITL semanal do head de vendas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo semanal automatico (toda segunda-feira 8h); anomalia detectada em tempo real (taxa de qualificacao cai > 20% em janela de 24h); Orion solicita analise especifica de segmento ou campanha; fim de…"
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

# Analisar Funil De Qualificação

**Task ID:** `lilo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** WhatsApp Qualifier

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Funil De Qualificação |
| **status** | `pending` |
| **responsible_executor** | Lilo (Lilo — Funnel Analyst Agent) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Lilo e o analista de dados do squad: monitora o funil de qualificacao em tempo real e produz os insights que alimentam as decisoes de Orion. Rastreia: taxa de resposta por fonte de lead (qual campanha traz leads mais responsivos), taxa de qualificacao por etapa (onde o funil quebra), objecoes mais frequentes por segmento, tempo medio de resposta vs taxa de qualificacao (correlacao), show-rate por tipo de lead qualificado. Detecta anomalias: queda subita de taxa de qualificacao pode indicar problema no playbook, mudanca no perfil de lead (campanha errada) ou restricao nova da Meta. Entrega relatorio semanal para Orion e gate HITL semanal.

## Input

- Dados de conversas do Vance (status, Lead Score, objecoes registradas, etapa de abandono), dados de agendamento de Mia (show-rate, cancelamentos, no-shows), dados de enriquecimento de Rex (fontes de lead, ICP Fit Score), metricas do CRM (oportunidades criadas, deals fechados de leads qualificados pelo squad)

## Output

- Dashboard semanal de metricas (taxa de qualificacao, show-rate, objecoes top 5, funil de abandono por etapa), Anomaly Report quando KPI cai > 15% vs semana anterior, recomendacao de ajuste de playbook (quais perguntas/objecoes estao gerando mais abandono), analise de correlacao fonte-de-lead vs qualificacao (qual campanha traz o melhor lead), briefing de 5 linhas para gate HITL semanal do head de vendas

## Trigger

Ciclo semanal automatico (toda segunda-feira 8h); anomalia detectada em tempo real (taxa de qualificacao cai > 20% em janela de 24h); Orion solicita analise especifica de segmento ou campanha; fim de mes para relatorio executivo

## Knowledge base (o que o executor consulta)

- Historico de metricas do squad (baseline de taxa de qualificacao, show-rate, tempo de resposta), definicoes de KPIs e thresholds de anomalia configurados por Orion, mapeamento de fontes de lead por campanha (UTMs), historico de conversas classificadas por outcome (qualificado/desqualificado/escalado)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados de conversas do Vance (status, Lead Score, objecoes registradas, etapa de abandono), dados de agendamento de Mia…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dashboard semanal de metricas (taxa de qualificacao, show-rate, objecoes top 5, funil de abandono por etapa), Anomaly R…) e persistir no artefato do squad.
4. Entregar ao critic Kira 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dashboard semanal de metricas (taxa de qualificacao, show-rate, objecoes top 5, funil de abandono por etapa), Anomaly Report quando KPI cai > 15% vs semana ant…
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

- **to:** Kira
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
