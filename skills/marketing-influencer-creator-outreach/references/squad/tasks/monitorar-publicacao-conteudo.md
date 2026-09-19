---
task: contentGuardian()
responsavel: "Content Guardian"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Briefing gerado pelo Brief Architect com elementos obrigatorios e checklist de conformidade"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Rascunho de conteudo enviado pelo creator (link de video, imagens, texto de legenda)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Deadline de publicacao do contrato"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "UTM e codigo de desconto configurados para verificacao de presenca no post"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Regras de brand safety atualizadas (palavras proibidas, elementos visuais vedados, mencoes a concorrentes)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Para cada entregavel: (1) Resultado da verificacao de conformidade em 7 pontos: mensagens-chave presentes (sim/nao), #publi/publicidade visivel (sim/nao/incorreto), codigo de desconto e UTM corretos (sim/nao), CTA presente e correto (sim/nao), ausencia de concorrentes ou elementos proibidos (sim/nao), especificacoes tecnicas atendidas"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "resolucao, duracao (sim/nao/parcial), tom alinhado ao briefing (sim/nao/revisar)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Veredicto: APROVADO (segue para publicacao), REVISAR (lista especifica de correcoes para o creator), BLOQUEAR_HITL (questao de brand safety ou compliance que requer revisao humana antes de qualquer passo)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(3) Apos publicacao confirmada: URL do post publicado, data/hora de publicacao, primeiras 2 horas de metricas (views, engajamento inicial) para benchmark de performance"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Armazenamento do conteudo aprovado na biblioteca de UGC do cliente com tags de produto, creator, campanha e formato para uso futuro em ads"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Atualizacao do ClickUp com status de cada entregavel e notificacao ao ROAS Tracker para iniciar monitoramento"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado automaticamente quando creator envia rascunho de conteudo via plataforma (webhook ou verificacao diaria de submissions). Alerta em D-3 do deadline se rascunho nao foi submetido: notificacao a…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Parceiro Certo antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou R$5.000 dependendo do budget do cliente) bloqueia e notifica o gestor de marketing com proposta completa, score do creator e benchmarking de mercado para aprovacao antes de qualquer envio."
    - "[ ] HITL: Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evidencias coletadas para decisao humana de vetamento ou aprovacao com risco consciente — nunca o squad decide sozinho sobre risco de reputacao da marca."
    - "[ ] HITL: Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #publi) ou representacao incorreta do produto que requer revisao do time juridico ou de marketing antes de qualquer resposta ao creator."
    - "[ ] HITL: ROAS Tracker detecta ROAS >= 5x em D+7: alerta de oportunidade imediato ao gestor de marketing e ao time de performance para decisao de amplificacao via ads pagos do post do creator — decisao de investimento adicional e sempre humana."
    - "[ ] HITL: ROAS Tracker detecta ROAS < 0.5x em D+14: alerta ao gestor de marketing para revisao da estrategia de creator daquele nicho ou campanha — pode indicar desalinhamento de ICP ou problema de produto que nao deve ser escondido por mais investimento."
---

# Monitorar Publicação Conteúdo

**Task ID:** `contentGuardian()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Influencer & Creator Outreach Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Publicação Conteúdo |
| **status** | `pending` |
| **responsible_executor** | Content Guardian (Content Guardian — O Monitor de Publicacao) |
| **execution_type** | `Agent` |
| **input** | 5 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Acompanha o ciclo de vida de cada entregavel desde a submissao do rascunho pelo creator ate a publicacao e arquivamento do conteudo aprovado. Recebe o rascunho de conteudo via plataforma (link de video, imagem ou texto enviado pelo creator), verifica conformidade com o briefing em 7 pontos criticos, coordena o fluxo de aprovacao e notifica o Curator quando o conteudo esta publicado com os dados de rastreamento ativos. Para conteudos que violam elementos obrigatorios (falta de #publi, codigo de desconto errado, CTA ausente): rejeita automaticamente com instrucoes especificas de correcao para o creator. Para conteudos aprovados: arquiva em biblioteca de UGC para uso futuro em ads pagos.

## Input

- Briefing gerado pelo Brief Architect com elementos obrigatorios e checklist de conformidade
- Rascunho de conteudo enviado pelo creator (link de video, imagens, texto de legenda)
- Deadline de publicacao do contrato
- UTM e codigo de desconto configurados para verificacao de presenca no post
- Regras de brand safety atualizadas (palavras proibidas, elementos visuais vedados, mencoes a concorrentes)

## Output

- Para cada entregavel: (1) Resultado da verificacao de conformidade em 7 pontos: mensagens-chave presentes (sim/nao), #publi/publicidade visivel (sim/nao/incorreto), codigo de desconto e UTM corretos (sim/nao), CTA presente e correto (sim/nao), ausencia de concorrentes ou elementos proibidos (sim/nao), especificacoes tecnicas atendidas
- resolucao, duracao (sim/nao/parcial), tom alinhado ao briefing (sim/nao/revisar)
- (2) Veredicto: APROVADO (segue para publicacao), REVISAR (lista especifica de correcoes para o creator), BLOQUEAR_HITL (questao de brand safety ou compliance que requer revisao humana antes de qualquer passo)
- (3) Apos publicacao confirmada: URL do post publicado, data/hora de publicacao, primeiras 2 horas de metricas (views, engajamento inicial) para benchmark de performance
- Armazenamento do conteudo aprovado na biblioteca de UGC do cliente com tags de produto, creator, campanha e formato para uso futuro em ads
- Atualizacao do ClickUp com status de cada entregavel e notificacao ao ROAS Tracker para iniciar monitoramento

## Trigger

Ativado automaticamente quando creator envia rascunho de conteudo via plataforma (webhook ou verificacao diaria de submissions). Alerta em D-3 do deadline se rascunho nao foi submetido: notificacao ao creator (via mensagem na plataforma) e ao time de marketing (escalacao). Alerta em D-1 se ainda nao submetido: escalacao urgente para o Curator e time de marketing para decisao (extensao de prazo ou substituicao do creator). Trigger de publicacao: verificacao automatica de publicacao no dia e hora acordados (via monitoramento de perfil ou notificacao do creator). Trigger de arquivo: apos 24h da publicacao, conteudo e arquivado na biblioteca de UGC com tags completas.

## Knowledge base (o que o executor consulta)

- Checklist de conformidade detalhado por plataforma e formato: para Reels
- #publi nos primeiros 3 segundos de sobreposicao ou nos primeiros 3 itens de legenda
- para Stories
- frame fixo com 'Parceria paga' em texto visivel
- para TikTok
- texto fixo na descricao e uso de ferramenta nativa de branded content tag
- Critérios de brand safety especificos do cliente: categorias de conteudo proibidas, lista de concorrentes diretos que nao podem aparecer nem ser mencionados, elementos visuais proibidos (logotipos, embalagens de terceiros)
- Fluxo de revisao: ate 2 rodadas de revisao por entregavel estao no contrato
- terceira rodada = HITL obrigatorio do gestor
- Sistema de tags de UGC para biblioteca: formato (Reels/TikTok/Stories/Imagem/Carrossel), produto, objetivo (awareness/conversao), creator tier, campanha, mes, plataforma
- permite busca por criativo semelhante para ads pagos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Briefing gerado pelo Brief Architect com elementos obrigatorios e checklist de conformidade).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Para cada entregavel: (1) Resultado da verificacao de conformidade em 7 pontos: mensagens-chave presentes (sim/nao), #p…) e persistir no artefato do squad.
4. Entregar ao critic Parceiro Certo; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Para cada entregavel: (1) Resultado da verificacao de conformidade em 7 pontos: mensagens-chave presentes (sim/nao), #publi/publicidade visivel (sim/nao/incorr…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Parceiro Certo registrado
- [ ] Gate HITL respeitado: Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou…
- [ ] Gate HITL respeitado: Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evi…
- [ ] Gate HITL respeitado: Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #p…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou R$5.000 dependendo… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evidencias coletadas pa… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #publi) ou representac… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — ROAS Tracker detecta ROAS >= 5x em D+7: alerta de oportunidade imediato ao gestor de marketing e ao time de performance para decisao de amplificacao via ads pa… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — ROAS Tracker detecta ROAS < 0.5x em D+14: alerta ao gestor de marketing para revisao da estrategia de creator daquele nicho ou campanha — pode indicar desalinh… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Creator solicita ajuste contratual apos assinatura (exclusividade, prazo, valor, direitos de imagem ampliados): qualquer renegociacao apos contrato assinado e… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Content Guardian nao recebe rascunho em D-1 do deadline: escalacao urgente ao time de marketing para decisao sobre extensao de prazo ou substituicao do creator… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Persona Fit Analyst detecta queda >= 25% no score medio de ROAS por categoria de creator em 2 ciclos consecutivos de campanha: alerta estrategico ao gestor de… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Parceiro Certo | BLOQUEIA entrega |

## Handoff

- **to:** ROAS Tracker
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
