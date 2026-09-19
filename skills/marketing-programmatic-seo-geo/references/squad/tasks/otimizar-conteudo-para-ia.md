---
task: beacon()
responsavel: "Beacon"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Conteúdo completo em Markdown (Scribe)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Keyword principal e entidades-alvo (Lexus)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Dados sobre como concorrentes estão sendo citados nos mesmos termos em ChatGPT, Perplexity e AI Overviews (Sonar)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Guia de entidades da marca: quais associações de entidade o cliente quer estabelecer no Knowledge Graph (ex: '[Marca] é referência em [categoria] para [segmento]')"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Exemplos de passagens que estão sendo citadas em AI Overviews nos termos-alvo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Conteudo otimizado para GEO/AEO em Markdown com as seguintes adicoes/modificacoes sobre o original do Scribe: (1) Citability score por secao"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "identifica e destaca os 3-5 trechos de maior probabilidade de citacao por LLMs com justificativa"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Definition boxes"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "blocos de definicao de entidade-chave formatados explicitamente para knowledge panel e citacao direta (formato: 'ENTIDADE e [definicao em 1-2 sentencas concisas com contexto de aplicacao]')"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Stat blocks"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "paragrafos de dado estatistico reestruturados em formato citavel: '[Dado especifico]"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Argo imediatamente após o Scribe entregar o conteúdo completo — sempre no mesmo batch, nunca em atraso. Re-trigger mensal para páginas publicadas com GEO score em queda (detectado pelo S…"
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

# Otimizar Conteúdo Para IA

**Task ID:** `beacon()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Programmatic SEO + GEO/AEO

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Otimizar Conteúdo Para IA |
| **status** | `pending` |
| **responsible_executor** | Beacon (Beacon — O Otimizador de IA Search) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 14 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

O especialista em GEO (Generative Engine Optimization) e AEO (Answer Engine Optimization) do squad — o unico agente focado especificamente em fazer o conteudo ser citado por LLMs em vez de apenas ranquear no Google tradicional. Recebe o conteudo do Scribe e aplica uma camada adicional de otimizacao especifica para motores de IA: reestrutura paragrafos para responder perguntas de forma direta e citavel, adiciona dados estatisticos com fontes verificaveis que LLMs preferem citar, insere definicoes de entidades de forma que o Google possa construir knowledge panels, formata passagens-chave como snippets de 40-60 palavras altamente citable, e recomenda o schema markup mais avancado para cada tipo de conteudo. Tambem monitora via Sonar se o conteudo publicado esta sendo citado nos motores de IA e propoe otimizacoes nas paginas que nao estao ganhando citacoes.

## Input

- Conteúdo completo em Markdown (Scribe)
- Keyword principal e entidades-alvo (Lexus)
- Dados sobre como concorrentes estão sendo citados nos mesmos termos em ChatGPT, Perplexity e AI Overviews (Sonar)
- Guia de entidades da marca: quais associações de entidade o cliente quer estabelecer no Knowledge Graph (ex: '[Marca] é referência em [categoria] para [segmento]')
- Exemplos de passagens que estão sendo citadas em AI Overviews nos termos-alvo

## Output

- Conteudo otimizado para GEO/AEO em Markdown com as seguintes adicoes/modificacoes sobre o original do Scribe: (1) Citability score por secao
- identifica e destaca os 3-5 trechos de maior probabilidade de citacao por LLMs com justificativa
- (2) Definition boxes
- blocos de definicao de entidade-chave formatados explicitamente para knowledge panel e citacao direta (formato: 'ENTIDADE e [definicao em 1-2 sentencas concisas com contexto de aplicacao]')
- (3) Stat blocks
- paragrafos de dado estatistico reestruturados em formato citavel: '[Dado especifico]
- Fonte: [Nome da fonte], [Ano]
- [1 sentenca de contexto.]'
- (4) Answer snippets
- 5-8 respostas de 40-60 palavras para perguntas de alta frequencia que aparecem no People Also Ask e nas respostas de Perplexity, formatadas para ser copiadas diretamente por LLMs
- (5) Schema markup expandido
- recomendacoes de Schema.org alem do basico: Speakable, Claim, Dataset conforme o tipo de conteudo
- (6) GEO score estimado (0-100) baseado na frequencia de elementos citable, verificabilidade das fontes e alinhamento com entidades-alvo
- Conteudo entregue ao Lumen para validacao final

## Trigger

Ativado pelo Argo imediatamente após o Scribe entregar o conteúdo completo — sempre no mesmo batch, nunca em atraso. Re-trigger mensal para páginas publicadas com GEO score em queda (detectado pelo Sonar). Trigger pontual para páginas estratégicas antes de campanha de lançamento ou evento do cliente.

## Knowledge base (o que o executor consulta)

- Framework GEO (Generative Engine Optimization): princípios de como LLMs selecionam conteúdo para citar
- especificidade factual, verificabilidade de fonte, autoridade da página, estrutura clara, resposta direta à pergunta
- Técnicas AEO: Answer Engine Optimization para Perplexity, ChatGPT e Gemini
- cada motor tem padrões distintos de citação
- Schema.org vocabulário completo com casos de uso por tipo de conteúdo (Article, FAQPage, HowTo, Product, Organization, Person, Claim, Dataset, Speakable)
- Estudo de padrões de AI Overviews do Google: quais tipos de conteúdo ganham citação (listas numeradas, tabelas comparativas, definições com fonte, passagens de 40-60 palavras com dado específico)
- Monitoramento contínuo das mudanças de comportamento de citação dos principais LLMs
- atualização mensal do knowledge base com novos padrões identificados

## Action Items

1. Confirmar o gatilho e carregar a entrada (Conteúdo completo em Markdown (Scribe)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Conteudo otimizado para GEO/AEO em Markdown com as seguintes adicoes/modificacoes sobre o original do Scribe: (1) Citab…) e persistir no artefato do squad.
4. Entregar ao critic Lumen; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Conteudo otimizado para GEO/AEO em Markdown com as seguintes adicoes/modificacoes sobre o original do Scribe: (1) Citability score por secao
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
