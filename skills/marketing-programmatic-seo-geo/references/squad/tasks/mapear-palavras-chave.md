---
task: lexus()
responsavel: "Lexus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Acesso ao SemRush ou Frase API (volume, dificuldade, SERP features por termo)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Acesso ao Google Search Console via MCP (queries reais gerando impressões mas sem clique"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "oportunidades de otimização)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Site do cliente para análise de conteúdo existente"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Lista de concorrentes definida no onboarding"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Acesso a web para análise de respostas de ChatGPT e Perplexity para termos-chave (via EXA ou WebSearch)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Universo de keywords estruturado em 4 camadas: (1) Cluster map"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "tópicos temáticos com keyword principal e 5-20 keywords semanticamente relacionadas por cluster, volume e dificuldade de cada uma"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Matriz de oportunidade"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "scoring de prioridade por keyword (volume x dificuldade x GEO potential x ICP fit) com tag de tipo: quick_win / long_game / geo_priority / blue_ocean"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Entidade map"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "lista de entidades do Knowledge Graph a serem estabelecidas na marca com frequência de menção recomendada e contexto ideal de uso"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Trigger inicial no onboarding para construção do universo baseline. Refresh mensal automático via cron. Re-trigger imediato quando Sonar detectar queda de >15% em tráfego de um cluster ou surgimento…"
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

# Mapear Palavras-chave

**Task ID:** `lexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Programmatic SEO + GEO/AEO

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Mapear Palavras-chave |
| **status** | `pending` |
| **responsible_executor** | Lexus (Lexus — O Estrategista de Palavras) |
| **execution_type** | `Worker` |
| **input** | 7 item(ns) |
| **output** | 10 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mapeia e mantém atualizado o universo completo de palavras-chave e entidades semanticas relevantes para o negocio do cliente. Vai alem do keyword research tradicional: identifica as entidades do Knowledge Graph (pessoas, empresas, produtos, conceitos) que precisam ser associadas a marca para que LLMs reconhecam sua autoridade. Segmenta o universo em clusters tematicos por intencao de busca e prioriza por uma matriz de oportunidade (volume x dificuldade x potencial de citacao em IA x fit com ICP). Identifica automaticamente termos em que concorrentes estao ranqueando mas o cliente nao, e termos sem conteudo concorrente forte (blue ocean). Alimenta diretamente o backlog de producao do Scribe e os parametros de otimizacao do Beacon.

## Input

- Acesso ao SemRush ou Frase API (volume, dificuldade, SERP features por termo)
- Acesso ao Google Search Console via MCP (queries reais gerando impressões mas sem clique
- oportunidades de otimização)
- Site do cliente para análise de conteúdo existente
- Lista de concorrentes definida no onboarding
- Acesso a web para análise de respostas de ChatGPT e Perplexity para termos-chave (via EXA ou WebSearch)
- ICP Card do cliente (quais dores e perguntas cada persona tem em cada etapa do funil)

## Output

- Universo de keywords estruturado em 4 camadas: (1) Cluster map
- tópicos temáticos com keyword principal e 5-20 keywords semanticamente relacionadas por cluster, volume e dificuldade de cada uma
- (2) Matriz de oportunidade
- scoring de prioridade por keyword (volume x dificuldade x GEO potential x ICP fit) com tag de tipo: quick_win / long_game / geo_priority / blue_ocean
- (3) Entidade map
- lista de entidades do Knowledge Graph a serem estabelecidas na marca com frequência de menção recomendada e contexto ideal de uso
- (4) Backlog de produção
- lista priorizada de tópicos/páginas a criar com template recomendado (artigo SEO, página programática, glossário, comparativa, calculadora)
- Artefato salvo no ClickUp com versionamento mensal
- Feed de oportunidades em tempo real para o Argo quando Sonar detectar novas janelas

## Trigger

Trigger inicial no onboarding para construção do universo baseline. Refresh mensal automático via cron. Re-trigger imediato quando Sonar detectar queda de >15% em tráfego de um cluster ou surgimento de concorrente novo em posição top 3. Re-trigger manual pelo time de marketing ou Argo quando uma nova vertical/produto é lançada.

## Knowledge base (o que o executor consulta)

- Frameworks de keyword clustering semântico e topical authority (modelo de pillar page + cluster)
- Metodologia de Entity SEO (Google Knowledge Graph, schema.org, NLP entities)
- Criterios de GEO/AEO: quais formatos de conteúdo ganham citação em AI Overviews (listas numeradas, tabelas comparativas, definições concisas com fonte, dados estatísticos com data), quais em Perplexity (conteúdo com múltiplas fontes citadas, estrutura de FAQ), quais no ChatGPT (autoridade estabelecida via menções em outras fontes)
- Biblioteca de tipos de SERP features por intenção de busca (featured snippet, PAA, knowledge panel, AI Overview) e o que é necessário para ganhar cada um
- Histórico de performance de keywords anteriores do cliente para calibragem do modelo de scoring

## Action Items

1. Confirmar o gatilho e carregar a entrada (Acesso ao SemRush ou Frase API (volume, dificuldade, SERP features por termo)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Universo de keywords estruturado em 4 camadas: (1) Cluster map) e persistir no artefato do squad.
4. Entregar ao critic Lumen; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Universo de keywords estruturado em 4 camadas: (1) Cluster map
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

- **to:** Orion
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
