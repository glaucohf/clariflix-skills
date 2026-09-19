---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ficha de Arqueologia completa (Arqueologa)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Nome completo, empresa e LinkedIn URL do lead quando disponível"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Acesso a APIs de enriquecimento: Clay (waterfall de 100+ fontes, intent signals), Apollo.io (verificação de email atual e cargo), LinkedIn Sales Navigator (mudanças de cargo/empresa, atividade recente)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Acesso à web para notícias recentes sobre a empresa (EXA/WebSearch)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Pixel de rastreamento do site do cliente se configurado (leads que voltaram ao site = sinal quente)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Ficha de Sinais Novos por lead: { lead_id, email_atual_verificado (booleano + email), cargo_atual_confirmado, empresa_atual, mudancas_detectadas: [lista com tipo (mudanca_cargo / expansao_empresa / investimento / novo_decisor / sinal_intent_site / mencao_social / nenhuma)], data_da_mudanca_quando_disponivel, angulo_de_reativacao_sugerido (texto de 2-3 frases baseado exclusivamente nos sinais detectados"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "nao em suposicao), forca_do_sinal (forte / medio / fraco / nenhum), flag_contato_desatualizado (booleano"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "email invalido ou lead mudou de empresa)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Score de 'janela de oportunidade' (0-100): quao oportuno e o momento de reativar baseado nos sinais"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato salvo no ClickUp e dados verificados atualizados no CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Lázaro imediatamente após Arqueologa entregar a ficha de cada lead. Prioridade de processamento: leads com flag de 'dado desatualizados' são processados primeiro para garantir validação…"
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

# Verificar Mudanças Em Leads

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Dormant Lead Reactivation

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Mudanças Em Leads |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — O Caçador de Sinais Novos) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Dado o contexto arqueologico do lead (o que era verdade antes), o Radar investiga o que MUDOU desde o ultimo contato para construir um novo angulo de entrada. Executa cascata de enriquecimento externo: verifica se a empresa do lead cresceu (headcount, novas contratacoes, expansao geografica), se houve mudanca de lideranca no cargo decisor, se a empresa recebeu investimento ou passou por M&A, se ha sinais de intent digitais (visitas ao site do cliente via pixel, engajamento com conteudo, mencao do produto em redes), e se o proprio lead mudou de cargo ou empresa. A mudanca de contexto e o GATILHO MAIS PODEROSO para reativacao — 'vi que voce esta liderando agora a expansao para o Sul' converte 5x mais que qualquer desconto. Para leads com dados desatualizados identificados pela Arqueologa: verifica o email atual e o cargo atual antes de qualquer envio.

## Input

- Ficha de Arqueologia completa (Arqueologa)
- Nome completo, empresa e LinkedIn URL do lead quando disponível
- Acesso a APIs de enriquecimento: Clay (waterfall de 100+ fontes, intent signals), Apollo.io (verificação de email atual e cargo), LinkedIn Sales Navigator (mudanças de cargo/empresa, atividade recente)
- Acesso à web para notícias recentes sobre a empresa (EXA/WebSearch)
- Pixel de rastreamento do site do cliente se configurado (leads que voltaram ao site = sinal quente)

## Output

- Ficha de Sinais Novos por lead: { lead_id, email_atual_verificado (booleano + email), cargo_atual_confirmado, empresa_atual, mudancas_detectadas: [lista com tipo (mudanca_cargo / expansao_empresa / investimento / novo_decisor / sinal_intent_site / mencao_social / nenhuma)], data_da_mudanca_quando_disponivel, angulo_de_reativacao_sugerido (texto de 2-3 frases baseado exclusivamente nos sinais detectados
- nao em suposicao), forca_do_sinal (forte / medio / fraco / nenhum), flag_contato_desatualizado (booleano
- email invalido ou lead mudou de empresa)
- Score de 'janela de oportunidade' (0-100): quao oportuno e o momento de reativar baseado nos sinais
- Artefato salvo no ClickUp e dados verificados atualizados no CRM

## Trigger

Ativado pelo Lázaro imediatamente após Arqueologa entregar a ficha de cada lead. Prioridade de processamento: leads com flag de 'dado desatualizados' são processados primeiro para garantir validação antes do envio. Re-trigger se um lead na fila mostrar sinal de intent no pixel do site (real-time trigger via webhook). Trigger batch diário para leads que estão na faixa de 'timing prometido' (lead disse 'me ligue em X meses' e o prazo se aproxima).

## Knowledge base (o que o executor consulta)

- Hierarquia de fontes de enriquecimento por tipo de dado: email atual (Apollo > Clay > Hunter.io em cascata), cargo atual (LinkedIn > Apollo > Clay), eventos da empresa (EXA + Google News + LinkedIn Company Page), intent signals (Clay intent + pixel do site do cliente + Bombora quando disponivel)
- Regras de confianca: email sem verificacao dupla via envio de teste = nao entra em sequencia
- Mapeamento de tipos de mudanca para angulo de reativacao: mudanca de cargo do decisor = 'parabenize + nova perspectiva', investimento recebido = 'vocês agora tem budget para X', expansao de headcount = 'crescimento rapido normalmente cria o problema que resolvemos'
- Threshold de forca de sinal para cada tipo de mudanca

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ficha de Arqueologia completa (Arqueologa)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Ficha de Sinais Novos por lead: { lead_id, email_atual_verificado (booleano + email), cargo_atual_confirmado, empresa_a…) e persistir no artefato do squad.
4. Entregar ao critic Atena; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Ficha de Sinais Novos por lead: { lead_id, email_atual_verificado (booleano + email), cargo_atual_confirmado, empresa_atual, mudancas_detectadas: [lista com ti…
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

- **to:** Oraculo Scorer
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
