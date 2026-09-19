---
task: voxWorkerDeVoz()
responsavel: "Vox (Worker de Voz"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê do lead (output do Dossiê Agent), roteiro base da vertical, histórico de tentativas anteriores, janela horária autorizada para discagem"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Transcrição da call (STT), classificação do lead (Qualificado/Não Qualificado/Aguardar/Sem Resposta), campos BANT preenchidos (Budget, Authority, Need, Timeline), gravação de áudio armazenada, registro de call no CRM, próximo passo definido"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead aprovado pelo Dossie Agent com score >= 60. Horário dentro da janela de discagem configurada. Tentativa de recontato conforme cadência definida."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Filtro 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3)."
    - "[ ] HITL: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3)."
    - "[ ] HITL: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3)."
    - "[ ] HITL: Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3)."
    - "[ ] HITL: Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation)."
---

# Realizar Ligação Cold Call

**Task ID:** `voxWorkerDeVoz()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz para Cold Calling e Discovery

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Realizar Ligação Cold Call |
| **status** | `pending` |
| **responsible_executor** | Vox (Worker de Voz (Vox (Worker de Voz — Cold Call e Abertura)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Conduz a ligação de cold call com latência sub-600ms. Executa roteiro dinâmico de abertura (pattern interrupt + pitch de valor em 15s), trata objeções de primeiro nível (sem tempo, não é o momento, já tenho fornecedor), faz as 3-4 perguntas de discovery BANT/MEDDIC e conduz ao CTA de agendamento. Se lead qualifica, transfere para Worker de Agendamento. Se não qualifica, registra motivo e propõe nurture.

## Input

- Dossiê do lead (output do Dossiê Agent), roteiro base da vertical, histórico de tentativas anteriores, janela horária autorizada para discagem

## Output

- Transcrição da call (STT), classificação do lead (Qualificado/Não Qualificado/Aguardar/Sem Resposta), campos BANT preenchidos (Budget, Authority, Need, Timeline), gravação de áudio armazenada, registro de call no CRM, próximo passo definido

## Trigger

Lead aprovado pelo Dossie Agent com score >= 60. Horário dentro da janela de discagem configurada. Tentativa de recontato conforme cadência definida.

## Knowledge base (o que o executor consulta)

- Roteiros de voz por vertical (imobiliária, agência, SaaS B2B), biblioteca de respostas a objeções (top 20 objeções mapeadas), perfil de voz calibrado (ElevenLabs voice ID), limites de duração por fase de call, script de fallback para secretaria/caixa postal

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dossiê do lead (output do Dossiê Agent), roteiro base da vertical, histórico de tentativas anteriores, janela horária a…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Transcrição da call (STT), classificação do lead (Qualificado/Não Qualificado/Aguardar/Sem Resposta), campos BANT preen…) e persistir no artefato do squad.
4. Entregar ao critic Filtro 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Transcrição da call (STT), classificação do lead (Qualificado/Não Qualificado/Aguardar/Sem Resposta), campos BANT preenchidos (Budget, Authority, Need, Timelin…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Filtro 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3).
- [ ] Gate HITL respeitado: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3).
- [ ] Gate HITL respeitado: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3).

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3). | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3). | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3). | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3). | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation). | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Confirmação de reagendamento quando prospect cancela reunião pela segunda vez consecutiva (decisão humana sobre continuar ou desqualificar — L3). | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibragem quinzenal de voz e persona do Vox Agent com gestor de vendas (revisão humana de amostras de áudio — L1). | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Filtro 2 | BLOQUEIA entrega |

## Handoff

- **to:** Filtro
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
