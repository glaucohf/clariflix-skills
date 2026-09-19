---
task: arqueologa()
responsavel: "Arqueologa"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Exportação do CRM com todos os campos do lead dormentes: nome, cargo, empresa, email, telefone, fonte de aquisição, data de criação, histórico de atividades (emails enviados com data e assunto, chamadas registradas, notas de SDR), motivo de perda quando registrado, campo de último toque"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Configuração de critérios de dormência do cliente (ex: sem atividade em 90 dias = dormente)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Ficha de Arqueologia por lead em JSON estruturado: { lead_id, archetype_dormência (1-5), angulo_original_falhado (resumo da abordagem anterior), último_toque_canal (email/WhatsApp/chamada/nenhum), último_toque_data, engajamentos_históricos (lista de opens/clicks com datas), motivo_perda_registrado (quando existir), dados_desatualizados (campos que podem ter mudado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "cargo, empresa, email), confiança_dados (alta/média/baixa baseada na completude), trilha_sugerida (qual das trilhas de reativação se aplica a este archetype)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato salvo no ClickUp linkado ao lead no CRM"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Flag de alerta se email provavelmente bounce (mais de 12 meses sem atividade = verificar antes de enviar)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Lázaro no início de cada rodada de reativação para todos os leads do cluster selecionado. Re-trigger se o CRM for atualizado com nova informação sobre o lead enquanto a rodada está em an…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Atena antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex: deal > R$20k) bloqueia completamente e notifica o gestor com draft completo, ficha de arqueologia e sinais novos para aprovacao ou rejeicao com 1 clique — nenhum caracter e enviado antes da aprovacao."
    - "[ ] HITL: Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovação humana obrigatória antes de entrar em sequência — agente não envia para dado não verificado."
    - "[ ] HITL: Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o gestor de marketing com o feedback completo do critic para reescritura ou descisao de nao envio."
    - "[ ] HITL: Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que disse, sugestão de próximo passo) — o squad paralisa qualquer automação para este lead e o vendedor assume o controle total da conversa."
    - "[ ] HITL: Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções de alto valor merecem resposta humana ou pelo menos validação antes de resposta automática."
---

# Reconstruir Histórico Lead

**Task ID:** `arqueologa()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Dormant Lead Reactivation

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Reconstruir Histórico Lead |
| **status** | `pending` |
| **responsible_executor** | Arqueologa (Arqueóloga — A Detetive do Passado) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Para cada lead dormente, reconstroi o histórico completo de interações registradas no CRM: qual campanha gerou o lead, quais mensagens foram enviadas e quando, quais emails foram abertos ou clicados, o que foi dito pelo lead se houve alguma resposta, qual foi o motivo de perda se registrado, quanto tempo de dormência acumulado, e qual era o cargo/empresa no momento do primeiro contato. Identifica o ANGULO FRACASSADO original — a abordagem que não funcionou — para garantir que o squad NUNCA repita o mesmo angulo que já foi rejeitado ou ignorado. Classifica cada lead em um dos 5 archetypes de dormência: (1) Nunca Respondeu — não abriu nem um email, pode ser problema de dados ou timing ruim; (2) Engajou mas Não Converteu — abriu, clicou, mas parou sem comprar; (3) Disse Não por Timing — 'me ligue em 6 meses', 'orçamento ano que vem'; (4) Perdido para Concorrente — registrado no CRM; (5) Fantasma Qualificado — tinha todos os indicadores de fit mas sumiu. Cada archetype tem uma trilha de reativação diferente. Opera de forma deterministicamente sobre os dados do CRM — sem suposição, sem invenção: o que não está registrado e marcado como 'dado ausente'.

## Input

- Exportação do CRM com todos os campos do lead dormentes: nome, cargo, empresa, email, telefone, fonte de aquisição, data de criação, histórico de atividades (emails enviados com data e assunto, chamadas registradas, notas de SDR), motivo de perda quando registrado, campo de último toque
- Configuração de critérios de dormência do cliente (ex: sem atividade em 90 dias = dormente)

## Output

- Ficha de Arqueologia por lead em JSON estruturado: { lead_id, archetype_dormência (1-5), angulo_original_falhado (resumo da abordagem anterior), último_toque_canal (email/WhatsApp/chamada/nenhum), último_toque_data, engajamentos_históricos (lista de opens/clicks com datas), motivo_perda_registrado (quando existir), dados_desatualizados (campos que podem ter mudado
- cargo, empresa, email), confiança_dados (alta/média/baixa baseada na completude), trilha_sugerida (qual das trilhas de reativação se aplica a este archetype)
- Artefato salvo no ClickUp linkado ao lead no CRM
- Flag de alerta se email provavelmente bounce (mais de 12 meses sem atividade = verificar antes de enviar)

## Trigger

Ativado pelo Lázaro no início de cada rodada de reativação para todos os leads do cluster selecionado. Re-trigger se o CRM for atualizado com nova informação sobre o lead enquanto a rodada está em andamento. Trigger de verificação batch semanal para novos leads que acabaram de cruzar o limiar de dormência configurado.

## Knowledge base (o que o executor consulta)

- Mapeamento dos 5 archetypes de dormencia com criterios de classificacao especificos
- Regras de deteccao de 'angulo falhado': como identificar o pitch anterior a partir do assunto do email, notas de SDR e campos de motivo de perda
- Dicionario de motivos de perda mais comuns no CRM do cliente (configurado no onboarding) com mapeamento para archetype
- Threshold de confianca de dados: qual combinacao de campos ausentes resulta em confianca baixa/media/alta
- Regras de fast-track: lead com nota de SDR 'me ligue em X meses' e a data ja passou = FIRE imediato para Oraculo Scorer independente do score

## Action Items

1. Confirmar o gatilho e carregar a entrada (Exportação do CRM com todos os campos do lead dormentes: nome, cargo, empresa, email, telefone, fonte de aquisição, dat…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Ficha de Arqueologia por lead em JSON estruturado: { lead_id, archetype_dormência (1-5), angulo_original_falhado (resum…) e persistir no artefato do squad.
4. Entregar ao critic Atena; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Ficha de Arqueologia por lead em JSON estruturado: { lead_id, archetype_dormência (1-5), angulo_original_falhado (resumo da abordagem anterior), último_toque_c…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Atena registrado
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

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
