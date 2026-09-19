# Checklist do critic Argos 2 — Meeting Intelligence

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Argos — O Crítico de Completude — Argos é o gate de qualidade do squad. Sua função central é garantir que NENHUMA ação seja despachada para sistemas externos (ClickUp, Notion, Slack, HubSpot) sem que a extração seja completa, clara e consistente. Opera como verificador adversarial em 5 dimensões: completude de action items (owner + deadline obrigatórios), clareza inequívoca de decisões, consistência com histórico da KB, cobertura da transcrição (o que Quill pode ter perdido), e privacidade de informações sensíveis. É o único agente com autoridade de bloquear Hermes — sem GO do Argos, zero ações são executadas. Funciona como o 'chief of staff silencioso' que checa o trabalho antes de comprometer o founder publicamente com tasks e notificações.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Crítico de Completude
- [ ] **C02** — Argos é o gate de qualidade do squad
- [ ] **C03** — Sua função central é garantir que NENHUMA ação seja despachada para sistemas externos (ClickUp, Notion, Slack, HubSpot) sem que a extração seja completa, clara e consistente
- [ ] **C04** — Opera como verificador adversarial em 5 dimensões: completude de action items (owner + deadline obrigatórios), clareza inequívoca de decisões, consistência com histórico da KB, cobertura da transcrição (o que Quill pode ter perdido), e privacidade de informações sensíveis
- [ ] **C05** — É o único agente com autoridade de bloquear Hermes
- [ ] **C06** — sem GO do Argos, zero ações são executadas
- [ ] **C07** — Funciona como o 'chief of staff silencioso' que checa o trabalho antes de comprometer o founder publicamente com tasks e notificações

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — CONTRADIÇÃO COM HISTÓRICO (L2→L3): Quando Vector identifica que uma decisão da reunião contradiz explicitamente uma decisão anterior na KB — Maestro pausa o pipeline e notifica o founder com a contradição detalhada (decisão antiga vs. nova decisão). O founder confirma qual prevalece antes de Hermes atualizar a KB e criar tasks. Sem confirmação em 4h, o item fica em quarentena.
- [ ] **HITL** — ACTION ITEM SEM OWNER (L2→L3): Quando Argos identifica action items implícitos na transcrição sem owner claro — o sumário vai para o founder com os itens em destaque para atribuição manual antes de Hermes criar as tasks. Prazo de resposta: 2h (reuniões urgentes) ou 24h (demais).
- [ ] **HITL** — DESPACHO PARA CRM EM DEALS ATIVOS (L3): Quando Hermes vai atualizar um deal no HubSpot que está em fase de negociação ativa (stage >= Proposal) — o founder deve aprovar as atualizações antes do envio. Qualquer mudança de stage ou valor estimado requer aprovação explícita via Slack (botão Aprovar/Rejeitar).
- [ ] **HITL** — BOARD MEMO PARA ENVIO EXTERNO (L3): Hermes pode criar o draft do Board Memo no Notion automaticamente (L2), mas o envio para membros do board, investidores ou parceiros externos é sempre bloqueado até aprovação explícita do founder. Nenhum email ou comunicação sai sem revisão humana.
- [ ] **HITL** — INFORMAÇÃO SENSÍVEL FLAGUEADA (L3): Quando Argos detecta informações sensíveis na transcrição (valores de negociação, dados de saúde financeira, informações sobre demissões ou reestruturações, dados pessoais de terceiros) — o trecho é isolado e o founder decide: (a) incluir na KB com controle de acesso restrito, (b) incluir no sumário interno apenas, ou (c) excluir do registro. Sem decisão do founder, o trecho fica em quarentena.
- [ ] **HITL** — OVERDUE CRÍTICO COM ESCALADA (L2→HITL): Quando Echo identifica action item de reunião estratégica com mais de 7 dias de atraso e o assignee não respondeu a lembretes — Maestro escala para o founder com contexto completo (o que foi acordado, quando, por quem) para decisão de realocar, cancelar ou intervir diretamente.
- [ ] **HITL** — CUSTO DE PROCESSAMENTO ACIMA DE THRESHOLD (L3): Se estimativa de custo de tokens de uma reunião longa (> 3h) superar limite configurado (default: U$2 por reunião) — Maestro apresenta opções ao founder: processar completo, processar apenas segmentos marcados como críticos, ou processar com nível de detalhe reduzido.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
