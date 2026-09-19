---
task: sonar()
responsavel: "Sonar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Acesso ao Google Search Console API (impressões, cliques, CTR, posição média por URL e query)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Acesso ao SemRush ou Frase API (histórico de posições, backlinks, visibilidade de domínio)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Acesso a Ahrefs ou Moz API quando configurado (para monitoramento de backlinks)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Sistema de monitoramento de citações em IA: queries sistemáticas para ChatGPT API, Perplexity API e Google AI Overviews para os 50 termos prioritários do cliente"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "verificando se a marca e citada e em qual posição na resposta"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Google PageSpeed Insights API para Core Web Vitals em batch"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dashboard de visibilidade atualizado diariamente no ClickUp com: (1) Posições top 100 por keyword com delta 7 dias e 30 dias"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) GEO Score semanal"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "% dos 50 termos prioritários em que a marca é citada em pelo menos 1 motor de IA (ChatGPT, Perplexity, AI Overviews) com breakdown por motor"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(3) Oportunidades detectadas"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "lista priorizada de quick wins (posição 5-20 com potencial de top 3) e GEO gaps (termos em que concorrente é citado mas o cliente não)"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(4) Alertas de queda"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Monitoramento de posições Google: daily via GSC API, weekly via SemRush para top 500 keywords. Monitoramento de citações em IA: a cada 48 horas para os 50 termos prioritários (mais frequente para ter…"
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

# Monitorar Posicoes Keywords

**Task ID:** `sonar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Programmatic SEO + GEO/AEO

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Posicoes Keywords |
| **status** | `pending` |
| **responsible_executor** | Sonar (Sonar — O Vigia de Visibilidade) |
| **execution_type** | `Worker` |
| **input** | 7 item(ns) |
| **output** | 11 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora continuamente a saúde e performance de todo o portfolio de conteúdo publicado — tanto no Google/Bing tradicional quanto nos motores de IA. Acompanha posições de keywords, tráfego orgânico, CTR, Core Web Vitals, citações da marca em ChatGPT, Perplexity e Google AI Overviews, e backlinks novos/perdidos. Detecta oportunidades antes dos concorrentes: keywords subindo rapidamente, Featured Snippets perdidos para concorrente, termos em que o cliente tem posição 5-15 com potencial de chegar ao top 3 com otimização pontual. Fecha o loop de aprendizado: envia alertas ao Argo, retroalimenta o Lexus com novos dados de performance e aciona o Beacon para otimizações de GEO em páginas que perderam citações em IA.

## Input

- Acesso ao Google Search Console API (impressões, cliques, CTR, posição média por URL e query)
- Acesso ao SemRush ou Frase API (histórico de posições, backlinks, visibilidade de domínio)
- Acesso a Ahrefs ou Moz API quando configurado (para monitoramento de backlinks)
- Sistema de monitoramento de citações em IA: queries sistemáticas para ChatGPT API, Perplexity API e Google AI Overviews para os 50 termos prioritários do cliente
- verificando se a marca e citada e em qual posição na resposta
- Google PageSpeed Insights API para Core Web Vitals em batch
- Lista de concorrentes para alertas de movimentação

## Output

- Dashboard de visibilidade atualizado diariamente no ClickUp com: (1) Posições top 100 por keyword com delta 7 dias e 30 dias
- (2) GEO Score semanal
- % dos 50 termos prioritários em que a marca é citada em pelo menos 1 motor de IA (ChatGPT, Perplexity, AI Overviews) com breakdown por motor
- (3) Oportunidades detectadas
- lista priorizada de quick wins (posição 5-20 com potencial de top 3) e GEO gaps (termos em que concorrente é citado mas o cliente não)
- (4) Alertas de queda
- páginas que perderam >3 posições em 7 dias ou que desapareceram do AI Overview que antes tinham
- (5) Backlinks novos e perdidos na semana
- (6) Core Web Vitals por página com flag se alguma página caiu abaixo do threshold
- Relatório semanal consolidado para o time de marketing com insights narrativos, não só dados brutos
- Alertas em tempo real via webhook para o Argo quando uma oportunidade ou queda crítica é detectada

## Trigger

Monitoramento de posições Google: daily via GSC API, weekly via SemRush para top 500 keywords. Monitoramento de citações em IA: a cada 48 horas para os 50 termos prioritários (mais frequente para termos de alta intenção comercial). Monitoramento de Core Web Vitals: weekly batch ou imediatamente após publicação de novo lote. Monitoramento de backlinks: diário via Ahrefs Alert ou equivalente. Relatório semanal: toda segunda-feira às 8h entregue ao Argo para planejamento do batch da semana. Alerta imediato: queda de >5 posições em keyword primária de cluster, perda de Featured Snippet, queda de CTR >30% em 7 dias.

## Knowledge base (o que o executor consulta)

- Metricas de saude de SEO: CTR esperado por posicao (posicao 1 = 28-35%, posicao 3 = 10-14%, posicao 5-10 = 2-6% para busca organica B2B), benchmark de Core Web Vitals (LCP <2.5s, CLS <0.1, INP <200ms)
- Metodologia de monitoramento de citacoes em IA: prompts sistematicos por categoria de query (generica do setor, especifica de produto, comparativa, problema/solucao) para rastrear presenca de marca em respostas de LLMs
- Biblioteca de padroes de flutuacao de ranking para distinguir update algoritmico do Google (afeta muitos termos simultaneamente) vs problema especifico de pagina
- Sinais de alerta de penalizacao: queda abrupta de >50% em visibilidade sem correlacao com sazonalidade = investigacao imediata
- Metodologia de estimativa de GEO Score: formula ponderada de citacoes por motor (AI Overviews peso 40%, Perplexity peso 35%, ChatGPT peso 25% baseado em share de uso em pesquisa de mercado B2B Brasil 2025)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Acesso ao Google Search Console API (impressões, cliques, CTR, posição média por URL e query)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dashboard de visibilidade atualizado diariamente no ClickUp com: (1) Posições top 100 por keyword com delta 7 dias e 30…) e persistir no artefato do squad.
4. Entregar ao critic Lumen; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dashboard de visibilidade atualizado diariamente no ClickUp com: (1) Posições top 100 por keyword com delta 7 dias e 30 dias
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

- **to:** Lumen
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
