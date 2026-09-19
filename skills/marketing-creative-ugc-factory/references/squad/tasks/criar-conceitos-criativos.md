---
task: vega()
responsavel: "Vega"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "ICP Creative Brief completo da Stella (mapa de dores, vocabulário, ângulos recomendados, hooks) + Brand voice guidelines + Histórico de conceitos já testados (para evitar repetição) + Performance dos top-5 criativos do ciclo anterior (para aprender o que funcionou) + Instruções de formato e plataforma-alvo (Meta Stories, Reels, Google Display, YouTube pre-roll) + Budget de produção disponível para o ciclo (define proporção de UGC real vs sintético)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de Conceitos Criativos (JSON + documento legível): para cada um dos 15-25 conceitos"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(1) Nome do conceito (slug identificador), (2) Ângulo de mensagem principal (dor/aspiração/prova social/autoridade/curiosidade/escassez), (3) Formato e plataforma alvo, (4) Estrutura narrativa detalhada (para vídeo: script de hook word-by-word"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "para static: headline + visual principal + CTA), (5) Tom e estilo visual, (6) Perfil de creator ideal (para UGC: gênero, faixa etária, contexto, nível de polimento), (7) Estimativa de custo de produção (sintético = zero, UGC = R$X por creator), (8) Justificativa de ressonância com ICP com referência ao brief da Stella"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orion após a Stella entregar o ICP Creative Brief validado. Acionado novamente se o Aegis reprovar mais de 40% dos conceitos (sinal de que a conceitualização está sistematicamente errad…"
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

# Criar Conceitos Criativos

**Task ID:** `vega()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Creative UGC Factory

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Criar Conceitos Criativos |
| **status** | `pending` |
| **responsible_executor** | Vega (Vega — Creative Concept Architect) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente especialista em conceitualizacao criativa. Transforma o ICP Creative Brief da Stella em 15-25 conceitos de criativo por ciclo — cada conceito e um pacote completo: angulo de mensagem, formato recomendado (UGC talking head / demo produto / testimonial / static hook + headline / carousel educativo / reel de antes-e-depois), estrutura narrativa (para video: hook 0-3s / desenvolvimento 3-15s / CTA 15-30s), referencias visuais (descricao de cena, paleta, mood board textual), e o argumento de por que esse conceito vai ressoar com o ICP especifico. Prioriza variedade deliberada: garante que nenhum ciclo tenha mais de 30% dos conceitos no mesmo angulo ou formato.

## Input

- ICP Creative Brief completo da Stella (mapa de dores, vocabulário, ângulos recomendados, hooks) + Brand voice guidelines + Histórico de conceitos já testados (para evitar repetição) + Performance dos top-5 criativos do ciclo anterior (para aprender o que funcionou) + Instruções de formato e plataforma-alvo (Meta Stories, Reels, Google Display, YouTube pre-roll) + Budget de produção disponível para o ciclo (define proporção de UGC real vs sintético)

## Output

- Pacote de Conceitos Criativos (JSON + documento legível): para cada um dos 15-25 conceitos
- (1) Nome do conceito (slug identificador), (2) Ângulo de mensagem principal (dor/aspiração/prova social/autoridade/curiosidade/escassez), (3) Formato e plataforma alvo, (4) Estrutura narrativa detalhada (para vídeo: script de hook word-by-word
- para static: headline + visual principal + CTA), (5) Tom e estilo visual, (6) Perfil de creator ideal (para UGC: gênero, faixa etária, contexto, nível de polimento), (7) Estimativa de custo de produção (sintético = zero, UGC = R$X por creator), (8) Justificativa de ressonância com ICP com referência ao brief da Stella

## Trigger

Acionado pelo Orion após a Stella entregar o ICP Creative Brief validado. Acionado novamente se o Aegis reprovar mais de 40% dos conceitos (sinal de que a conceitualização está sistematicamente errada — retorna ao Vega para revisão antes de ir para o Cruz).

## Knowledge base (o que o executor consulta)

- Frameworks de conceitualização criativa para performance (Hormozi creative frameworks, UGC best practices por plataforma, estruturas de hook validadas), Histórico completo de conceitos testados e seus resultados (CTR, hook rate, ROAS por conceito), Brand voice guidelines e restrições visuais, Specs técnicas de formato por plataforma (resolução, duração, safe zones para Meta/Google/TikTok), Banco de referências de criativos top performers do setor (atualizado mensalmente via Insense/AdLibrary research)

## Action Items

1. Confirmar o gatilho e carregar a entrada (ICP Creative Brief completo da Stella (mapa de dores, vocabulário, ângulos recomendados, hooks) + Brand voice guideline…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de Conceitos Criativos (JSON + documento legível): para cada um dos 15-25 conceitos) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de Conceitos Criativos (JSON + documento legível): para cada um dos 15-25 conceitos
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

- **to:** Cruz
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
