---
task: sigma()
responsavel: "Sigma"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Conceito aprovado pelo Vega com especificações visuais (mood board textual, paleta, estilo) + Copy aprovada pelo Cruz (headline, subhead, CTA para overlay) + Brand assets do cliente (logo SVG/PNG, guia de cores hex, fontes aprovadas, fotos de produto) + Specs de formato por plataforma (dimensões, safe zones, specs de arquivo) + Ferramentas de geração disponibilizadas pelo cliente (Canva API, DALL-E API, Midjourney, etc.)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Assets de criativo sintéticos prontos para upload: (1) Static ads em todos os formatos solicitados (feed 1:1, stories 9:16, banner 16:9) com resolução e peso de arquivo conformes com specs de plataforma, (2) Composições de overlay para vídeo (intro card, CTA final, legenda animada), (3) Thumbnails para vídeo UGC, (4) Prompts de IA generativa documentados para reprodução e iteração, (5) Preview sheet (mosaico de todas as variações geradas para aprovação visual rápida), (6) Metadados para o banco de criativos (nome do conceito, formato, ângulo, data de geração, versão)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orion para todos os conceitos que não requerem UGC real (Sigma e o caminho rápido — entrega em horas vs dias do Hoox). Também acionado para complementar UGC real com overlay, thumbnail…"
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

# Gerar Ativos Sinteticos

**Task ID:** `sigma()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Creative UGC Factory

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Ativos Sinteticos |
| **status** | `pending` |
| **responsible_executor** | Sigma (Sigma — Synthetic Asset Generator) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente responsável pela geração sintética de ativos criativos — static ads (imagens), motion graphics simples, thumbnails de vídeo e composições visuais — sem depender de produção humana. Combina brand assets do cliente (logo, cores, fontes, imagens de produto) com os conceitos e copy aprovados para gerar variações de static ads prontas para teste. Para clientes com acesso a ferramentas de IA generativa de imagem (DALL-E, Midjourney, Stable Diffusion via API), gera o prompt otimizado para cada conceito e processa os assets. Também gera thumbnails customizados para vídeos UGC, texto de overlay animado e versões em múltiplos formatos (feed, stories, banner).

## Input

- Conceito aprovado pelo Vega com especificações visuais (mood board textual, paleta, estilo) + Copy aprovada pelo Cruz (headline, subhead, CTA para overlay) + Brand assets do cliente (logo SVG/PNG, guia de cores hex, fontes aprovadas, fotos de produto) + Specs de formato por plataforma (dimensões, safe zones, specs de arquivo) + Ferramentas de geração disponibilizadas pelo cliente (Canva API, DALL-E API, Midjourney, etc.)

## Output

- Assets de criativo sintéticos prontos para upload: (1) Static ads em todos os formatos solicitados (feed 1:1, stories 9:16, banner 16:9) com resolução e peso de arquivo conformes com specs de plataforma, (2) Composições de overlay para vídeo (intro card, CTA final, legenda animada), (3) Thumbnails para vídeo UGC, (4) Prompts de IA generativa documentados para reprodução e iteração, (5) Preview sheet (mosaico de todas as variações geradas para aprovação visual rápida), (6) Metadados para o banco de criativos (nome do conceito, formato, ângulo, data de geração, versão)

## Trigger

Acionado pelo Orion para todos os conceitos que não requerem UGC real (Sigma e o caminho rápido — entrega em horas vs dias do Hoox). Também acionado para complementar UGC real com overlay, thumbnail e versões de formato adicional. Acionado manualmente pelo gestor para iterações rápidas de static a partir de um criativo vencedor já identificado.

## Knowledge base (o que o executor consulta)

- Brand assets completos do cliente (logo, cores, fontes, fotos de produto, imagens aprovadas), Specs técnicas de formato por plataforma (Meta, Google, YouTube, TikTok) atualizadas, Princípios de design de performance (hierarquia visual para ads, regras de contraste para legibilidade, posicionamento de logo em safe zone), Prompts otimizados de IA generativa por estilo visual (fotorrealismo, ilustração, lifestyle, produto em contexto), Histórico de assets gerados e seus resultados de performance (CTR por composição visual)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Conceito aprovado pelo Vega com especificações visuais (mood board textual, paleta, estilo) + Copy aprovada pelo Cruz (…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Assets de criativo sintéticos prontos para upload: (1) Static ads em todos os formatos solicitados (feed 1:1, stories 9…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Assets de criativo sintéticos prontos para upload: (1) Static ads em todos os formatos solicitados (feed 1:1, stories 9:16, banner 16:9) com resolução e peso d…
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

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
