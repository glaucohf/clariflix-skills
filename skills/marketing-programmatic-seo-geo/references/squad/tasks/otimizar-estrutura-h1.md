---
task: scribe()
responsavel: "Scribe"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Backlog de produção priorizado (Lexus) com keyword principal, intenção de busca, tipo de página e cluster temático"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Dataset estruturado com dados de suporte (Orion)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Brief de otimização por página: keyword density alvo, entidades obrigatórias, concorrentes a superar, SERP features alvo"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Guia de voz da marca do cliente (tom, vocabulário, nível de formalidade, exemplos aprovados)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Conteúdo existente do cliente para garantir consistência e evitar canibalização de keywords"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Conteúdo completo por página em formato Markdown estruturado: (1) Meta title (max 60 chars, keyword na frente), meta description (max 155 chars, CTA incluso), H1 único com keyword principal, slug de URL otimizado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Corpo do conteúdo com estrutura H2-H3 semanticamente rica, parágrafos de 3-5 sentenças máximos para scannability e leitura por LLMs, dados e estatísticas com fonte inline (formato: [Fonte, Ano]), pelo menos 1 tabela ou lista numerada por artigo (ganho de featured snippet e AI citation)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) FAQ section com mínimo 5 perguntas formato PAA com respostas concisas de 40-60 palavras cada"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "otimizadas para AI Overviews"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(4) Schema markup recomendado (Article, FAQPage, HowTo conforme o tipo)"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(5) Sugestões de internal links (3-5 por página) para o Atlas executar"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Argo em batches conforme o calendario editorial programatico configurado (ex: 50 paginas/semana para modo programatico, 4-8 artigos/semana para modo editorial). Re-trigger se Lumen repro…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Lumen antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Atlas: qualquer publicacao ou edicao de paginas na lista de URLs estrategicas (pillar pages, paginas com backlinks externos, paginas de alta competicao definidas no onboarding) bloqueia e notifica o gestor de conteudo com preview completo para aprovacao antes de publicar um caracter."
    - "[ ] HITL: Lumen reprova 2x no mesmo item: conteúdo que falhou no ciclo automático de otimização (Scribe ou Beacon reescreve 1x, Lumen reprova novamente) e escalado para o editor humano com o checklist completo de reprovações e sugestões específicas de correção."
    - "[ ] HITL: Factualidade questionável detectada pelo Lumen: qualquer dado que não tem fonte verificável com URL ativo e data recente é imediatamente bloqueado e sinalizado para o time de conteúdo verificar manualmente antes de qualquer publicação — zero tolerância para afirmação sem rastreabilidade."
    - "[ ] HITL: Batch de publicação programática acima de 50 páginas: qualquer batch acima do threshold configurado (default: 50 páginas/batch) requer aprovação do gestor de SEO antes do Atlas iniciar a publicação — para proteger o crawl budget e a reputação do domínio."
    - "[ ] HITL: Queda abrupta de visibilidade detectada pelo Sonar: queda de >30% em tráfego orgânico em 7 dias ou desaparecimento de cluster inteiro das SERPs = alerta imediato ao time de SEO para investigação manual antes de qualquer ação automática do squad — pode ser update algorítmico que requer análise humana."
---

# Otimizar Estrutura H1

**Task ID:** `scribe()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Programmatic SEO + GEO/AEO

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Otimizar Estrutura H1 |
| **status** | `pending` |
| **responsible_executor** | Scribe (Scribe — O Motor de Conteúdo) |
| **execution_type** | `Agent` |
| **input** | 5 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Produz conteúdo SEO-otimizado em escala usando os datasets do Orion e as diretrizes do Lexus. Opera em dois modos: (1) Programático — gera centenas ou milhares de páginas a partir de templates com variação de dados, mantendo cada página única, substantiva e com pelo menos 800 palavras de conteúdo real (não enchimento); (2) Editorial Assistido — produz artigos longos (1.500-3.000 palavras) para clusters de topical authority com profundidade real, pesquisa integrada e estrutura otimizada para featured snippets e AI Overviews. Em ambos os modos, obrigações inegociáveis: nenhuma afirmação sem dado de suporte, nenhum parágrafo sem valor real para o leitor, estrutura H1-H2-H3 otimizada para entidades semânticas e para leitura por LLMs, FAQ section ao final de cada página com as perguntas reais que o Lexus identificou como People Also Ask.

## Input

- Backlog de produção priorizado (Lexus) com keyword principal, intenção de busca, tipo de página e cluster temático
- Dataset estruturado com dados de suporte (Orion)
- Brief de otimização por página: keyword density alvo, entidades obrigatórias, concorrentes a superar, SERP features alvo
- Guia de voz da marca do cliente (tom, vocabulário, nível de formalidade, exemplos aprovados)
- Conteúdo existente do cliente para garantir consistência e evitar canibalização de keywords

## Output

- Conteúdo completo por página em formato Markdown estruturado: (1) Meta title (max 60 chars, keyword na frente), meta description (max 155 chars, CTA incluso), H1 único com keyword principal, slug de URL otimizado
- (2) Corpo do conteúdo com estrutura H2-H3 semanticamente rica, parágrafos de 3-5 sentenças máximos para scannability e leitura por LLMs, dados e estatísticas com fonte inline (formato: [Fonte, Ano]), pelo menos 1 tabela ou lista numerada por artigo (ganho de featured snippet e AI citation)
- (3) FAQ section com mínimo 5 perguntas formato PAA com respostas concisas de 40-60 palavras cada
- otimizadas para AI Overviews
- (4) Schema markup recomendado (Article, FAQPage, HowTo conforme o tipo)
- (5) Sugestões de internal links (3-5 por página) para o Atlas executar
- Score de SEO estimado por página (Frase ou SemRush grader)
- Conteúdo entregue ao Beacon para otimização GEO antes de ir para o Lumen

## Trigger

Ativado pelo Argo em batches conforme o calendario editorial programatico configurado (ex: 50 paginas/semana para modo programatico, 4-8 artigos/semana para modo editorial). Re-trigger se Lumen reprovar um lote — max 1 reescritura automatica por pagina antes de escalar para HITL. Trigger de urgencia se Sonar detectar oportunidade de quick win em keyword com baixa competicao e alta intencao de compra.

## Knowledge base (o que o executor consulta)

- Frameworks de escrita para SEO: E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness), topical authority, internal linking strategy
- Templates de estrutura por tipo de página: artigo informacional de topo de funil, página de produto/serviço transacional, página comparativa (X vs Y), página de glossário, página programática por região/vertical/atributo, calculadora interativa, estudo de caso estruturado
- Regras de anti-duplicate: nenhuma página do batch pode ter mais de 20% de overlap textual com outra página do mesmo domínio (verified by Lumen)
- Guias de formatação para legibilidade por LLMs: frases curtas, parágrafos curtos, dados explícitos, contexto sem ambiguidade, entidades mencionadas pelo nome completo na primeira referência
- Biblioteca de FAQ patterns por intenção de busca e por setor do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Backlog de produção priorizado (Lexus) com keyword principal, intenção de busca, tipo de página e cluster temático).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Conteúdo completo por página em formato Markdown estruturado: (1) Meta title (max 60 chars, keyword na frente), meta de…) e persistir no artefato do squad.
4. Entregar ao critic Lumen; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Conteúdo completo por página em formato Markdown estruturado: (1) Meta title (max 60 chars, keyword na frente), meta description (max 155 chars, CTA incluso),…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Lumen registrado
- [ ] Gate HITL respeitado: Gate L3 no Atlas: qualquer publicacao ou edicao de paginas na lista de URLs estrategicas (pillar pages, paginas com backlinks externos, pag…
- [ ] Gate HITL respeitado: Lumen reprova 2x no mesmo item: conteúdo que falhou no ciclo automático de otimização (Scribe ou Beacon reescreve 1x, Lumen reprova novamen…
- [ ] Gate HITL respeitado: Factualidade questionável detectada pelo Lumen: qualquer dado que não tem fonte verificável com URL ativo e data recente é imediatamente bl…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Atlas: qualquer publicacao ou edicao de paginas na lista de URLs estrategicas (pillar pages, paginas com backlinks externos, paginas de alta competi… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Lumen reprova 2x no mesmo item: conteúdo que falhou no ciclo automático de otimização (Scribe ou Beacon reescreve 1x, Lumen reprova novamente) e escalado para… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Factualidade questionável detectada pelo Lumen: qualquer dado que não tem fonte verificável com URL ativo e data recente é imediatamente bloqueado e sinalizado… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Batch de publicação programática acima de 50 páginas: qualquer batch acima do threshold configurado (default: 50 páginas/batch) requer aprovação do gestor de S… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Queda abrupta de visibilidade detectada pelo Sonar: queda de >30% em tráfego orgânico em 7 dias ou desaparecimento de cluster inteiro das SERPs = alerta imedia… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Novos templates programáticos: sempre que Lexus ou Argo identificam um novo tipo de página programática não mapeada anteriormente, o template precisa de aprova… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Decisões de redirects e exclusão de conteúdo: qualquer ação que envolva deletar, redirecionar ou desindexar páginas existentes (especialmente com tráfego ou ba… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Lumen | BLOQUEIA entrega |

## Handoff

- **to:** Beacon
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
