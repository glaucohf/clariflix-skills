---
task: orquestradorDeRecuperacaoPipeline()
responsavel: "Orquestrador de Recuperação"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Painel de Recuperação Ativa no ClickUp com: (1) Mapa de Oportunidades Estagnadas atualizado em tempo real por bucket e valor em risco, (2) Log de cada tentativa de recuperação com status e resultado (artefato verificável por deal), (3) Relatório semanal de conversões e perdas com análise de padrões do Forense, (4) Biblioteca de playbooks vivos atualizados por feedback loop, (5) Dashboard de KPIs de recuperação com comparativo antes/depois da implantação do squad"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro Comercial do funil morto. Recebe sinais de estagnação do CRM (webhook ou polling), avalia criticidade e valor do deal, decompõe em subtarefas, roteia para os workers corretos, mantém estado d…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Critic e Verifier de Mensagens 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeiro toque automatizado — gate L3 no Mensageiro)"
    - "[ ] HITL: Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa"
    - "[ ] HITL: Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável comercial"
    - "[ ] HITL: Mudança de playbook baseada em proposta do Forense — ajustes em playbooks existentes exigem aprovação humana antes de entrar em produção"
    - "[ ] HITL: Primeiro contato via voz (Vapi/Retell) para leads de alto valor — script revisado e aprovado pelo responsavel antes do disparo"
---

# Orquestrar Pipeline do Recuperação de Oportunidades Estagnadas

**Task ID:** `orquestradorDeRecuperacaoPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Recuperação de Oportunidades Estagnadas

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Recuperação de Oportunidades Estagnadas |
| **status** | `pending` |
| **responsible_executor** | Orquestrador de Recuperação (Resgate (Orquestrador de Recuperação)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Maestro Comercial do funil morto. Recebe sinais de estagnação do CRM (webhook ou polling), avalia criticidade e valor do deal, decompõe em subtarefas, roteia para os workers corretos, mantém estado da máquina de recuperação, consolida resultados e reporta ao squad humano. Opera em modo contínuo (24/7 monitoramento) com batches diários de priorização. Único responsável por orquestrar múltiplos workers em paralelo para um mesmo deal de alto valor.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Painel de Recuperação Ativa no ClickUp com: (1) Mapa de Oportunidades Estagnadas atualizado em tempo real por bucket e valor em risco, (2) Log de cada tentativa de recuperação com status e resultado (artefato verificável por deal), (3) Relatório semanal de conversões e perdas com análise de padrões do Forense, (4) Biblioteca de playbooks vivos atualizados por feedback loop, (5) Dashboard de KPIs de recuperação com comparativo antes/depois da implantação do squad

## Trigger

Maestro Comercial do funil morto. Recebe sinais de estagnação do CRM (webhook ou polling), avalia criticidade e valor do deal, decompõe em subtarefas, roteia para os workers corretos, mantém estado da máquina de recuperação, consolida resultados e reporta ao squad humano. Opera em modo contínuo (24/7 monitoramento) com batches diários de priorização. Único responsável por orquestrar múltiplos workers em paralelo para um mesmo deal de alto valor.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível), Pipedrive, Salesforce
- fonte de verdade de deals e histórico
- WhatsApp Business API: Gupshup, AiSensy ou Interakt
- canal principal de recuperação no Brasil
- Email: SMTP/SendGrid ou sequenciador (Apollo, Instantly)
- cadências de nurture e follow-up
- LinkedIn Sales Navigator
- enriquecimento de contexto e outreach via Escavador
- Voz: Vapi (<600ms latência) ou Retell AI + ElevenLabs TTS
- recuperação via ligação para deals de alto valor
- Enriquecimento: Clay ou Apollo (275M+ contatos)
- Escavador busca sinais externos
- E-commerce/Carrinho: Shopify, WooCommerce, Hotmart
- webhooks de abandono de carrinho
- gestão de tarefas, prova de trabalho, artefatos verificáveis por deal
- Langfuse (OTEL)
- observabilidade, evals e quality gates (dev 70% / staging 85% / prod 95%)
- Google Calendar / Calendly
- booking de reuniões de reativação pelo Worker de Agendamento (quando integrado)
- Slack / Teams
- alertas de resposta e HITL gates para comerciais humanos

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Critic e Verifier de Mensagens 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Painel de Recuperação Ativa no ClickUp com: (1) Mapa de Oportunidades Estagnadas atualizado em tempo real por bucket e valor em risco, (2) Log de cada tentativ…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Critic e Verifier de Mensagens 2 registrado
- [ ] Gate HITL respeitado: Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeir…
- [ ] Gate HITL respeitado: Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa
- [ ] Gate HITL respeitado: Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável c…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeiro toque automatizado… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável comercial | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Mudança de playbook baseada em proposta do Forense — ajustes em playbooks existentes exigem aprovação humana antes de entrar em produção | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Primeiro contato via voz (Vapi/Retell) para leads de alto valor — script revisado e aprovado pelo responsavel antes do disparo | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Opt-out recebido — registrado imediatamente, comunicado ao comercial, nenhuma acao adicional automatica alem do registro de compliance | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Critic e Verifier de Mensagens 2 | BLOQUEIA entrega |

## Handoff

- **to:** Worker de Detecção e Triagem
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
