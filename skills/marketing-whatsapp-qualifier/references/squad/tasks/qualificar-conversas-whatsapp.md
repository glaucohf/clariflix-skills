---
task: vance()
responsavel: "Vance"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Mensagem de entrada do lead no WhatsApp, contexto de enriquecimento de Rex (empresa, cargo, fonte do lead), Playbook Conversacional v{N} aprovado, historico de conversas anteriores do mesmo contato (se houver), configuracao de thresholds de escalada do Orion"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Conversa qualificada com campos BANT preenchidos, Lead Score pos-qualificacao (0-10), Status do lead (Qualificado/Desqualificado/Escalado/Agendado/Nurture), transcricao estruturada da conversa para CRM, trigger de agendamento para Mia (se qualificado) ou trigger de escalada para SDR humano (se threshold atingido)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Nova mensagem recebida no WhatsApp Business API (webhook em tempo real); lead retoma conversa apos pausa de > 2h; Orion dispara follow-up ativo para leads que entraram mas nao responderam em 24h; SDR…"
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

# Qualificar Conversas WhatsApp

**Task ID:** `vance()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** WhatsApp Qualifier

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Qualificar Conversas WhatsApp |
| **status** | `pending` |
| **responsible_executor** | Vance (Vance — Conversational Qualifier) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executor principal das conversas de qualificacao no WhatsApp. Vance e o agente purpose-built que opera dentro das restricoes Meta pos-proibicao: nao e chatbot generico, e assistente conversacional com playbook estruturado e personalidade de SDR consultivo. Executa o fluxo BANT/MEDDIC adaptado: Budget (orcamento disponivel), Authority (quem decide), Need (dor real e urgencia), Timeline (quando quer resolver). Trata as top 10 objecoes com respostas do playbook aprovado. Detecta sinais de alta intenção (resposta rapida, perguntas tecnicas, mencao de concorrentes) e sinais de baixa intencao (resposta monossilabica, sem urgencia). Escalada automatica para humano quando: lead VIP (empresa acima do threshold de tamanho), irritacao detectada (3 mensagens curtas seguidas), objecao de preco acima de X%, ou lead pede explicitamente falar com pessoa.

## Input

- Mensagem de entrada do lead no WhatsApp, contexto de enriquecimento de Rex (empresa, cargo, fonte do lead), Playbook Conversacional v{N} aprovado, historico de conversas anteriores do mesmo contato (se houver), configuracao de thresholds de escalada do Orion

## Output

- Conversa qualificada com campos BANT preenchidos, Lead Score pos-qualificacao (0-10), Status do lead (Qualificado/Desqualificado/Escalado/Agendado/Nurture), transcricao estruturada da conversa para CRM, trigger de agendamento para Mia (se qualificado) ou trigger de escalada para SDR humano (se threshold atingido)

## Trigger

Nova mensagem recebida no WhatsApp Business API (webhook em tempo real); lead retoma conversa apos pausa de > 2h; Orion dispara follow-up ativo para leads que entraram mas nao responderam em 24h; SDR humano retorna lead para fluxo automatizado apos triagem inicial

## Knowledge base (o que o executor consulta)

- Playbook Conversacional versionado (arvore de decisao com perguntas BANT, respostas a objecoes top 10, mensagens de follow-up por contexto), Personas de ICP do squad Living ICP Profiler (se disponivel) ou perfil de ICP validado manualmente, historico de conversas bem-sucedidas como few-shot examples, regras Meta pos-proibicao (o que pode e nao pode fazer via WhatsApp Business API), brand voice guidelines do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Mensagem de entrada do lead no WhatsApp, contexto de enriquecimento de Rex (empresa, cargo, fonte do lead), Playbook Co…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Conversa qualificada com campos BANT preenchidos, Lead Score pos-qualificacao (0-10), Status do lead (Qualificado/Desqu…) e persistir no artefato do squad.
4. Entregar ao critic Kira 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Conversa qualificada com campos BANT preenchidos, Lead Score pos-qualificacao (0-10), Status do lead (Qualificado/Desqualificado/Escalado/Agendado/Nurture), tr…
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

- **to:** Rex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
