---
task: hoox()
responsavel: "Hoox"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Conceito criativo aprovado + Script detalhado do Cruz (incluindo script de vídeo word-by-word com marcações) + Perfil de creator especificado pelo Vega (gênero, faixa etária, contexto, tom, nível de polimento) + Budget disponível para produção de UGC no ciclo + Acesso à plataforma Hóox/Insense do cliente + Instrução do Orion sobre urgência e volume de UGCs necessários no ciclo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Brief de creator publicado na plataforma Hóox/Insense (formato padronizado: contexto da marca, o que fazer, o que NÃO fazer, script detalhado, especificações técnicas, exemplos de referências, prazo e remuneração), Notificação ao humano responsável para aprovação do brief antes de publicação (gate L3"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "publicar o brief é uma ação com custo financeiro), Status tracker de UGCs em produção (creator contratado / vídeo em edição / entregue / aprovado/reprovado), Pre-screening report para cada vídeo recebido (aderência ao brief 0-100, problemas identificados antes do gate do Aegis), Assets organizados no banco de criativos com metadados completos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orion quando o conceito aprovado requer UGC real (vs sintético). Gate L3 obrigatório antes de publicar o brief na plataforma (envolve contrato e pagamento à creator). Acionado automatic…"
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

# Coordenar Produção De UGC

**Task ID:** `hoox()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Creative UGC Factory

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Coordenar Produção De UGC |
| **status** | `pending` |
| **responsible_executor** | Hoox (Hóox — UGC Production Coordinator) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente especialista em coordenacao de producao de UGC real com creators. Para cada conceito que requer video UGC autêntico (vs sintetico), gera o brief completo de producao para plataformas como Hoox e Insense, seleciona o perfil de creator ideal, monitora o status de entrega, faz o pre-screening do video recebido (verifica aderencia ao brief antes de enviar para o Aegis), e organiza os assets entregues no banco de criativos. Nao cria o video — coordena quem cria. Tambem e responsavel por gerar scripts de video para ferramentas de geracao sintetica de UGC (Runway, Pika, HeyGen para avatares) quando o cliente tem acesso.

## Input

- Conceito criativo aprovado + Script detalhado do Cruz (incluindo script de vídeo word-by-word com marcações) + Perfil de creator especificado pelo Vega (gênero, faixa etária, contexto, tom, nível de polimento) + Budget disponível para produção de UGC no ciclo + Acesso à plataforma Hóox/Insense do cliente + Instrução do Orion sobre urgência e volume de UGCs necessários no ciclo

## Output

- Brief de creator publicado na plataforma Hóox/Insense (formato padronizado: contexto da marca, o que fazer, o que NÃO fazer, script detalhado, especificações técnicas, exemplos de referências, prazo e remuneração), Notificação ao humano responsável para aprovação do brief antes de publicação (gate L3
- publicar o brief é uma ação com custo financeiro), Status tracker de UGCs em produção (creator contratado / vídeo em edição / entregue / aprovado/reprovado), Pre-screening report para cada vídeo recebido (aderência ao brief 0-100, problemas identificados antes do gate do Aegis), Assets organizados no banco de criativos com metadados completos

## Trigger

Acionado pelo Orion quando o conceito aprovado requer UGC real (vs sintético). Gate L3 obrigatório antes de publicar o brief na plataforma (envolve contrato e pagamento à creator). Acionado automaticamente quando vídeo é entregue pelo creator para iniciar o pré-screening e encaminhar ao Aegis para aprovação final.

## Knowledge base (o que o executor consulta)

- Guidelines de brief de UGC (o que incluir para maximizar aderência do creator ao conceito), Catálogo de creators aprovados pelo cliente (perfis pré-validados com histórico de entregas), Tabela de remuneração de market (faixas de preço por tipo de UGC no mercado brasileiro), Specs técnicas de vídeo por plataforma (resolução, orientação, duração, safe zones), Brand voice e restrições visuais do cliente, Histórico de briefs que geraram bons e maus resultados (aprendizado de produção)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Conceito criativo aprovado + Script detalhado do Cruz (incluindo script de vídeo word-by-word com marcações) + Perfil d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Brief de creator publicado na plataforma Hóox/Insense (formato padronizado: contexto da marca, o que fazer, o que NÃO f…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Brief de creator publicado na plataforma Hóox/Insense (formato padronizado: contexto da marca, o que fazer, o que NÃO fazer, script detalhado, especificações t…
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

- **to:** Sigma
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
