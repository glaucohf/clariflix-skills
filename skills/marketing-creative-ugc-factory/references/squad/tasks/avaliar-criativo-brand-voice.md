---
task: aegis()
responsavel: "Aegis"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Asset criativo completo para validação: (a) Para static/video sintético: arquivo + copy + metadados do conceito + ângulo de mensagem"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "(b) Para UGC: vídeo do creator + script de referência + brief original"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "(c) Para brief de UGC (pré-publicação): draft do brief + conceito aprovado pelo Vega"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Brand voice guidelines completos"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Políticas vigentes de publicidade das plataformas-alvo"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "ICP Creative Brief da Stella (para validar ressonância)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Verdict estruturado por item e por dimensao: APPROVED / NEEDS_REVISION / BLOCKED"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Para cada item nao aprovado: (1) Dimensao da violacao (brand voice / Icp resonance / compliance / qualidade tecnica), (2) Problema especifico descrito sem ambiguidade ('o claim X nao tem evidencia"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "viola politica de saude do Meta, sessao 4.2'), (3) Sugestao de correcao cirurgica ('substituir X por Y' ou 'remover o trecho Z e usar o claim aprovado W'), (4) Score de conformidade 0-100 por dimensao"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Lote aprovado e encaminhado ao Nexus para indexacao"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Lote com revisao retorna ao agente responsavel (Cruz para copy, Sigma para visual, Hoox para UGC) com instrucoes precisas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Gate obrigatório — acionado pelo Orion antes de qualquer asset chegar em plataforma externa. Também acionado antes da publicação de brief de UGC no Hoox/Insense (ação com custo financeiro = L3 com ve…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aegis 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do squad operar — sem essa base o Aegis não tem referência para validar, e o squad não ativa"
    - "[ ] HITL: Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento ao creator) — o Hoox gera o brief e aguarda aprovação explícita do humano responsável via Slack/WhatsApp antes de publicar. O cliente vê o brief completo, o perfil de creator selecionado e o custo estimado"
    - "[ ] HITL: Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados anteriormente, o responsavel de midia revisa o preview antes da ativacao — as primeiras impressoes de um criativo novo sao irreversiveis"
    - "[ ] HITL: Gate L3 — Escala de criativo vencedor acima de threshold de budget: quando o Nexus identifica um vencedor e o Orion recomenda escala (aumento de budget > X% acima do threshold pre-definido), o humano aprova o aumento antes da execução pelo squad de media buying (ou pelo cliente diretamente)"
    - "[ ] HITL: Aprovação do ICP Creative Brief (apos cada ciclo da Stella): o cliente valida o mapa de dores/ângulos proposto pela Stella antes do Vega começar a conceitualização — garante que os insights estão corretos e alinhados com o momento estratégico da empresa"
---

# Avaliar Criativo Brand Voice

**Task ID:** `aegis()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Creative UGC Factory

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Avaliar Criativo Brand Voice |
| **status** | `pending` |
| **responsible_executor** | Aegis (Aegis — Brand Voice & Quality Critic) |
| **execution_type** | `Agent` |
| **input** | 7 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente critico/verificador que atua como gate de qualidade obrigatorio antes de qualquer criativo chegar na plataforma de anuncio ou brief de UGC ser publicado. Avalia em quatro dimensoes: (1) Brand Voice — o tom, vocabulario e personalidade da marca estao presentes? Ha words proibidas ou claims nao aprovados? (2) ICP Resonance — o criativo fala a lingua do ICP definido pela Stella? O angulo de mensagem e relevante para a dor/desejo mapeado? (3) Compliance de Plataforma — viola alguma politica do Meta/Google (claims de saude, financeiros, comparativos sem evidencia, imagens proibidas)? (4) Qualidade Tecnica — os specs de formato estao corretos? O asset esta legivel e visualmente coerente? Emite verdict com justificativa precisa e sugestao de correcao especifica para cada item reprovado — nunca bloqueia sem explicar como resolver.

## Input

- Asset criativo completo para validação: (a) Para static/video sintético: arquivo + copy + metadados do conceito + ângulo de mensagem
- (b) Para UGC: vídeo do creator + script de referência + brief original
- (c) Para brief de UGC (pré-publicação): draft do brief + conceito aprovado pelo Vega
- Brand voice guidelines completos
- Políticas vigentes de publicidade das plataformas-alvo
- ICP Creative Brief da Stella (para validar ressonância)
- Claims aprovados e não aprovados pelo cliente

## Output

- Verdict estruturado por item e por dimensao: APPROVED / NEEDS_REVISION / BLOCKED
- Para cada item nao aprovado: (1) Dimensao da violacao (brand voice / Icp resonance / compliance / qualidade tecnica), (2) Problema especifico descrito sem ambiguidade ('o claim X nao tem evidencia
- viola politica de saude do Meta, sessao 4.2'), (3) Sugestao de correcao cirurgica ('substituir X por Y' ou 'remover o trecho Z e usar o claim aprovado W'), (4) Score de conformidade 0-100 por dimensao
- Lote aprovado e encaminhado ao Nexus para indexacao
- Lote com revisao retorna ao agente responsavel (Cruz para copy, Sigma para visual, Hoox para UGC) com instrucoes precisas

## Trigger

Gate obrigatório — acionado pelo Orion antes de qualquer asset chegar em plataforma externa. Também acionado antes da publicação de brief de UGC no Hoox/Insense (ação com custo financeiro = L3 com verificação adicional do Aegis). Acionado automaticamente quando novo lote de assets é entregue por qualquer agente produtor (Cruz, Sigma, Hoox).

## Knowledge base (o que o executor consulta)

- Brand voice guidelines completos (tom, vocabulário proibido, claims aprovados e com evidência, claims proibidos, exemplos de copy boa e ruim do cliente), Políticas vigentes de publicidade Meta Ads e Google Ads (atualizado mensalmente
- especial atenção a claims financeiros, de saúde, comparativos), ICP Creative Brief atualizado pela Stella, Histórico de reprovações anteriores (por plataforma e por dimensão
- aprendizado de erros recorrentes), Legislação aplicável ao setor do cliente (CONAR, LGPD, regulações setoriais)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Asset criativo completo para validação: (a) Para static/video sintético: arquivo + copy + metadados do conceito + ângul…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Verdict estruturado por item e por dimensao: APPROVED / NEEDS_REVISION / BLOCKED) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Verdict estruturado por item e por dimensao: APPROVED / NEEDS_REVISION / BLOCKED
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aegis 2 registrado
- [ ] Gate HITL respeitado: Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do…
- [ ] Gate HITL respeitado: Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento a…
- [ ] Gate HITL respeitado: Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do squad operar — sem e… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento ao creator) — o Hoox… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados anteriormente, o re… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate L3 — Escala de criativo vencedor acima de threshold de budget: quando o Nexus identifica um vencedor e o Orion recomenda escala (aumento de budget > X% ac… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação do ICP Creative Brief (apos cada ciclo da Stella): o cliente valida o mapa de dores/ângulos proposto pela Stella antes do Vega começar a conceitualiz… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão do Preview Sheet semanal (opcional, recomendado): o Sigma gera um mosaico visual de todos os assets da semana — o cliente pode revisar e vetar conceito… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibração mensal de thresholds: reunião de 30 minutos para revisar os thresholds de vencedor/arquivamento com base na performance real do mês — o squad opera… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Onboarding de novo creator no banco aprovado: qualquer creator novo (nao pre-validado) que va ser contratado pelo Hoox requer aprovacao do cliente antes de rec… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Aegis 2 | BLOQUEIA entrega |

## Handoff

- **to:** Aegis 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
