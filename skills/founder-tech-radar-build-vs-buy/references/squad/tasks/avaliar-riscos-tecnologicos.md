---
task: aria()
responsavel: "ARIA"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "BvB Analysis Report completo de Kai (todas as secoes), Vendor Risk Assessment de Aegis quando aplicavel, historico de decisoes tecnicas similares com outcomes (para calibrar se as premissas de Kai sao realistas versus otimistas), sinais de ecossistema relevantes de Vera que possam contradizer a recomendacao, qualquer informacao adicional de contexto que Lens julgue relevante para o questionamento adversarial"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Adversarial Review Report com veredicto APPROVED/NEEDS_REVISION/BLOCKED: lista de premissas questionadas com nivel de preocupacao (LOW/MEDIUM/HIGH) para cada uma, Worst-Case Scenario Matrix (melhor caso vs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "caso esperado vs"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "pior caso para cada opcao com probabilidade estimada de cada cenario), lista de Alternativas Subestimadas que merecem investigacao adicional antes da decisao final (com justificativa de por que foram descartadas prematuramente), Bias Flags quando detecta vies de disponibilidade, recency bias ou hype tecnologico, Stress-Test Questions (3-7 perguntas especificas que o founder deve fazer ao vendor ou ao time antes de finalizar a decisao), veredicto final com condicoes especificas para APPROVED (ex: 'aprovado se vendor fornecer DPA assinado e Lock-in Score nao exceder 6 com as clausulas contratuais negociadas por Aegis')"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: SEMPRE antes de qualquer BvB Analysis Report de Kai ser entregue ao founder (gate obrigatorio para Tier 1 — sem excecao); sempre antes de qualquer recomendacao de movimento de quadrante de ASSESS par…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic ARIA 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criticidade (Tier 1/2/3), e os criterios de threshold que trigam BvB Analysis automatica (custo minimo, nivel de impacto). Gate L3 obrigatorio — sem esta aprovacao o squad nao opera em producao. Define o escopo de toda a operacao"
    - "[ ] HITL: Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/Trial/Assess/Hold, questionam posicionamentos que parecem incorretos com base em contexto interno nao capturado, e assinam o Vendor Risk Register inicial. Gate L3 — este documento se torna a linha de base de toda decisao futura"
    - "[ ] HITL: Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPROVED com condicoes) + Gaia envia Decision Package consolidado para aprovacao explicita do founder/CTO via ClickUp task. Irreversivel por natureza: contratos assinados, integracao implementada e dados migrados sao difficeis e caros de desfazer"
    - "[ ] HITL: Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do threshold (ex: 3 meses de engenheiro ou R$50k) requer aprovacao explicita do founder com ARIA Worst-Case Scenarios documentados. Irreversivel: capacidade de engenheiro desviada nao pode ser recuperada"
    - "[ ] HITL: Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology Roadmap Recommendations para os proximos 2 trimestres. Gate L3: founder/CTO aprovam as recomendacoes antes de se tornarem diretriz tecnica do squad. Incluido no calendario de governanca do founder"
---

# Avaliar Riscos Tecnológicos

**Task ID:** `aria()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Tech Radar & Build-vs-Buy Intelligence

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Avaliar Riscos Tecnológicos |
| **status** | `pending` |
| **responsible_executor** | ARIA (ARIA — Adversarial Risk Intelligence Assessor) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Critic adversarial especializado em tecnologia — implementa o protocolo de questionamento sistematico para toda recomendacao tecnica antes de chegar ao founder. Funciona como o arquiteto senior mais cético do mercado que ja viu cada 'bala de prata' fracassar. Avalia quatro dimensoes em cada item critico: (1) SOLIDEZ DA ANALISE — o BvB-7 de Kai foi aplicado com dados reais ou com estimativas otimistas? as premissas de TCO sao defensaveis (custo de manutencao de software construido internamente e sistematicamente subestimado — ARIA questiona especificamente o multiplier de manutencao aplicado)? o Time-to-Value estimado considera descobertas tardias ou assume caminho feliz?; (2) WORST-CASE SCENARIOS — qual e o pior cenario realista para a opcao recomendada? se 'buy', o vendor foi adquirido por competitor ou triplicou o preco em 18 meses — qual e o custo de saida? se 'build', o engenheiro que construiu sai da empresa em 6 meses — qual e o bus factor real?; (3) ALTERNATIVAS DESCARTADAS — Kai considerou e documentou por que descartou as alternativas? ha alguma alternativa open-source ou de nicho que pode ter sido subestimada por nao ter reconhecimento de marca mas que atende tecnicamente o requisito?; (4) VIESES DE RECOMENDACAO — a recomendacao reflete um vies de disponibilidade (sugerindo a ferramenta com que o time ja tem experiencia em vez da melhor opcao para o caso)? ha hype tecnologico embutido na avaliacao (ferramenta nova sendo adotada por ser nova, nao por ser melhor)? ha pressao de tempo que esta inflando a avaliacao positiva de uma opcao sobre outra?. ARIA nao tem voto negativo automatico — o objetivo nao e bloquear decisoes, mas garantir que as premissas foram estressadas e que o founder decide com os riscos do pior cenario explicitados.

## Input

- BvB Analysis Report completo de Kai (todas as secoes), Vendor Risk Assessment de Aegis quando aplicavel, historico de decisoes tecnicas similares com outcomes (para calibrar se as premissas de Kai sao realistas versus otimistas), sinais de ecossistema relevantes de Vera que possam contradizer a recomendacao, qualquer informacao adicional de contexto que Lens julgue relevante para o questionamento adversarial

## Output

- Adversarial Review Report com veredicto APPROVED/NEEDS_REVISION/BLOCKED: lista de premissas questionadas com nivel de preocupacao (LOW/MEDIUM/HIGH) para cada uma, Worst-Case Scenario Matrix (melhor caso vs
- caso esperado vs
- pior caso para cada opcao com probabilidade estimada de cada cenario), lista de Alternativas Subestimadas que merecem investigacao adicional antes da decisao final (com justificativa de por que foram descartadas prematuramente), Bias Flags quando detecta vies de disponibilidade, recency bias ou hype tecnologico, Stress-Test Questions (3-7 perguntas especificas que o founder deve fazer ao vendor ou ao time antes de finalizar a decisao), veredicto final com condicoes especificas para APPROVED (ex: 'aprovado se vendor fornecer DPA assinado e Lock-in Score nao exceder 6 com as clausulas contratuais negociadas por Aegis')

## Trigger

SEMPRE antes de qualquer BvB Analysis Report de Kai ser entregue ao founder (gate obrigatorio para Tier 1 — sem excecao); sempre antes de qualquer recomendacao de movimento de quadrante de ASSESS para ADOPT ou de TRIAL para ADOPT que envolva sistema Tier 1; quando Lens identifica que uma decisao tecnica ad-hoc urgente tem alto impacto e risco (modo prioritario, ARIA review em menos de 4h); ciclo trimestral de revisao de decisoes anteriores (ARIA avalia retrospectivamente se as premissas das BvB Analyses dos ultimos 90 dias se materializaram como esperado — ciclo de aprendizado critico); quando Vera detecta sinal adverso sobre vendor adotado com recomendacao anterior de Kai (ARIA reavalia se a decisao ainda e valida)

## Knowledge base (o que o executor consulta)

- Biblioteca de Worst-Case Scenarios por categoria de decisao tecnica (o que tipicamente da errado em builds internos subestimados, em adocoes de vendors que cresceram de preco, em frameworks que foram deprecados, em migracao de databases
- cenarios baseados em casos reais documentados), historico de premissas otimistas identificadas em analises anteriores versus o que realmente aconteceu (calibracao de estimativas de TCO e Time-to-Value), catalogo de vieses cognitivos comuns em decisoes tecnicas com exemplos especificos do setor de software (availability bias em frameworks famosos, hype bias em AI tools, sunk cost bias em rewrites), registro de vendors com historico problematico (adquisicoes que degradaram produto, mudancas agressivas de preco, suporte deteriorado pos-IPO)
- memoria institucional adversarial

## Action Items

1. Confirmar o gatilho e carregar a entrada (BvB Analysis Report completo de Kai (todas as secoes), Vendor Risk Assessment de Aegis quando aplicavel, historico de d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Adversarial Review Report com veredicto APPROVED/NEEDS_REVISION/BLOCKED: lista de premissas questionadas com nivel de p…) e persistir no artefato do squad.
4. Entregar ao critic ARIA 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Adversarial Review Report com veredicto APPROVED/NEEDS_REVISION/BLOCKED: lista de premissas questionadas com nivel de preocupacao (LOW/MEDIUM/HIGH) para cada u…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic ARIA 2 registrado
- [ ] Gate HITL respeitado: Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as cla…
- [ ] Gate HITL respeitado: Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes n…
- [ ] Gate HITL respeitado: Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adve…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criti… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPRO… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology R… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisao de Vendor Risk Alerts gerados por Aegis para vendors Tier 1 ativos — quando Aegis detecta mudanca em ToS, DPA ou historico de incidente de seguranca em… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Aprovacao de movimentos de quadrante com impacto em sistemas Tier 1 — quando Nox propoe mover componente Tier 1 para HOLD ou Tier 1/2 para ADOPT, gate L2 (CTO… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Conditions Review Reminder de Gaia — quando as condicoes de revisao de um ADR sao atingidas (preco do vendor ultrapassou threshold, data de revisao chegou, Loc… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic ARIA 2 | BLOQUEIA entrega |

## Handoff

- **to:** Gaia
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
