---
task: cruz()
responsavel: "Cruz"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Conceito criativo aprovado pelo Vega (ângulo, formato, estrutura narrativa, perfil de audiência) + ICP Creative Brief da Stella (vocabulário nativo, dores, objeções) + Brand voice guidelines (tom, restrições, claims aprovados) + Histórico de copy top performers (hooks específicos que geraram CTR > threshold) + Especificações técnicas da plataforma (limite de caracteres, posicionamento de texto) + Instrução do Orion sobre nível de urgência e CTA da campanha"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de Copy Estruturado (JSON por conceito): (1) Headlines"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "5-8 variações categorizadas por trigger (curiosidade / dor / aspiração / prova social / urgência), (2) Primary text"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "3-5 variações em extensões S/M/L com o mesmo ângulo tratado de formas diferentes, (3) CTAs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "3-5 opções com nível de assertividade variado, (4) Script completo de vídeo (para UGC ou vídeo gerado) com marcações de tom, pausa e ênfase, (5) Texto de overlay para static (headline + subhead + CTA em hierarquia visual), (6) Legenda otimizada para feed (com hashtags se aplicável), (7) Score de confiança do Cruz para cada variação (0-100, baseado em similaridade com copy historicamente validada)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orion para cada conceito aprovado pelo Vega (pode rodar em paralelo para múltiplos conceitos). Acionado novamente com instruções específicas se o Aegis reprovar copy por desalinhamento…"
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

# Gerar Copy Performatica

**Task ID:** `cruz()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Creative UGC Factory

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Copy Performatica |
| **status** | `pending` |
| **responsible_executor** | Cruz (Cruz — Copy Performance Writer) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de geracao de copy de alta performance para todos os formatos de criativo. Para cada conceito aprovado pelo Vega, gera multiplas variacoes de cada elemento de texto: headlines (5-8 opcoes), primary text (3-5 opcoes em extensoes diferentes — short/medium/long), CTAs (3-5 opcoes), scripts de video word-by-word (com marcacoes de pause, enfase e tom), legendas para UGC, textos de overlay para static. A diversidade de copy e deliberada: testa diferentes triggers emocionais, diferentes niveis de urgencia, diferentes abordagens de prova social (numero / depoimento / case). Toda copy e escrita no vocabulario nativo do ICP extraido pela Stella — nunca no jargao interno da empresa.

## Input

- Conceito criativo aprovado pelo Vega (ângulo, formato, estrutura narrativa, perfil de audiência) + ICP Creative Brief da Stella (vocabulário nativo, dores, objeções) + Brand voice guidelines (tom, restrições, claims aprovados) + Histórico de copy top performers (hooks específicos que geraram CTR > threshold) + Especificações técnicas da plataforma (limite de caracteres, posicionamento de texto) + Instrução do Orion sobre nível de urgência e CTA da campanha

## Output

- Pacote de Copy Estruturado (JSON por conceito): (1) Headlines
- 5-8 variações categorizadas por trigger (curiosidade / dor / aspiração / prova social / urgência), (2) Primary text
- 3-5 variações em extensões S/M/L com o mesmo ângulo tratado de formas diferentes, (3) CTAs
- 3-5 opções com nível de assertividade variado, (4) Script completo de vídeo (para UGC ou vídeo gerado) com marcações de tom, pausa e ênfase, (5) Texto de overlay para static (headline + subhead + CTA em hierarquia visual), (6) Legenda otimizada para feed (com hashtags se aplicável), (7) Score de confiança do Cruz para cada variação (0-100, baseado em similaridade com copy historicamente validada)

## Trigger

Acionado pelo Orion para cada conceito aprovado pelo Vega (pode rodar em paralelo para múltiplos conceitos). Acionado novamente com instruções específicas se o Aegis reprovar copy por desalinhamento de brand voice ou claim não aprovado — retorna apenas as variações reprovadas para reescrita cirúrgica.

## Knowledge base (o que o executor consulta)

- Biblioteca de hooks validados por ROAS histórico (organizada por ângulo e formato), Frameworks de copy de performance (AIDA, PAS, BAB, Before-After-Bridge, Hormozi hooks), Vocabulário nativo do ICP por segmento (extraído da Stella e atualizado a cada ciclo), Brand voice guidelines completos com exemplos de copy aprovada e reprovada, Políticas de copy por plataforma (proibições Meta/Google, restrições setoriais do cliente), Histórico de testes A/B de copy com resultados (qual headline venceu e por que)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Conceito criativo aprovado pelo Vega (ângulo, formato, estrutura narrativa, perfil de audiência) + ICP Creative Brief d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de Copy Estruturado (JSON por conceito): (1) Headlines) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de Copy Estruturado (JSON por conceito): (1) Headlines
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

- **to:** Hoox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
