---
task: atlas()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Conteúdo final aprovado pelo Lumen em Markdown com todos os metadados (meta title, meta description, slug, schema markup, sugestões de internal link)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Mapa de cluster do Lexus para internal linking automático"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Acesso à API do CMS do cliente (credenciais configuradas no onboarding)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Acesso ao Google Search Console API para submissão de sitemap e monitoramento de indexação"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Regras de gate L3: lista de URLs estratégicas que requerem aprovação humana antes de publicação ou edição"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Status de indexação atual do domínio para evitar publicação em massa que possa ser interpretada como spam pelo Google"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Confirmação de publicação por página com: URL final publicada, timestamp, status de indexação (submitted to GSC / indexed / crawl_error), internal links inseridos (lista de páginas linkadas), schema markup aplicado, screenshot do preview da página publicada"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Para batches de publicação programática: relatório consolidado do batch com taxa de sucesso, erros de publicação e status de indexação 24h e 72h após publicação"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Para gates L3 ativados: notificação ao gestor de conteúdo com preview completo da página, razão do gate e opção de aprovação/rejeição com 1 clique"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Atualização automática do sitemap e submissão ao GSC a cada novo batch publicado"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Log de todas as publicações e edições no ClickUp como prova de trabalho"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Argo imediatamente após Lumen aprovar o lote de conteúdo. Trigger de publicação incremental para evitar publicação em massa (max configurável de páginas por dia para proteger a reputação…"
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

# Publicar Conteúdo Tecnico

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Programmatic SEO + GEO/AEO

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Publicar Conteúdo Tecnico |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — O Publicador Inteligente) |
| **execution_type** | `Hybrid` |
| **input** | 6 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável pela publicação técnica e pela otimização on-page de cada página aprovada pelo Lumen. Conecta diretamente com o CMS do cliente via API (WordPress REST API, Webflow CMS API, Contentful ou equivalente) e executa a publicação com todos os elementos técnicos corretos: meta tags, schema markup, canonical tags, hreflang quando aplicável, internal linking automático baseado no mapa de cluster do Lexus, imagem com alt text otimizado, URL slug limpo e configuração de indexação. Também gerencia a saúde técnica do conteúdo publicado: redireciona páginas de baixo desempenho, atualiza meta dados quando o Sonar detecta queda de CTR, e submete sitemaps atualizados ao Google Search Console. Para páginas estratégicas (pillar pages, páginas de alta competição, páginas com backlinks externos apontando): bloqueia e notifica para aprovação humana antes de qualquer publicação ou edição.

## Input

- Conteúdo final aprovado pelo Lumen em Markdown com todos os metadados (meta title, meta description, slug, schema markup, sugestões de internal link)
- Mapa de cluster do Lexus para internal linking automático
- Acesso à API do CMS do cliente (credenciais configuradas no onboarding)
- Acesso ao Google Search Console API para submissão de sitemap e monitoramento de indexação
- Regras de gate L3: lista de URLs estratégicas que requerem aprovação humana antes de publicação ou edição
- Status de indexação atual do domínio para evitar publicação em massa que possa ser interpretada como spam pelo Google

## Output

- Confirmação de publicação por página com: URL final publicada, timestamp, status de indexação (submitted to GSC / indexed / crawl_error), internal links inseridos (lista de páginas linkadas), schema markup aplicado, screenshot do preview da página publicada
- Para batches de publicação programática: relatório consolidado do batch com taxa de sucesso, erros de publicação e status de indexação 24h e 72h após publicação
- Para gates L3 ativados: notificação ao gestor de conteúdo com preview completo da página, razão do gate e opção de aprovação/rejeição com 1 clique
- Atualização automática do sitemap e submissão ao GSC a cada novo batch publicado
- Log de todas as publicações e edições no ClickUp como prova de trabalho

## Trigger

Ativado pelo Argo imediatamente após Lumen aprovar o lote de conteúdo. Trigger de publicação incremental para evitar publicação em massa (max configurável de páginas por dia para proteger a reputação do domínio). Trigger de atualização mensal para refresh de conteúdo de páginas com dados desatualizados (preços, estatísticas, rankings). Trigger de urgência para quick wins identificados pelo Sonar. Gate L3 automático para qualquer página na lista de URLs estratégicas.

## Knowledge base (o que o executor consulta)

- Melhores práticas de publicação de conteúdo programático em escala sem penalização do Google (crawl budget, duplicate content, thin content detection)
- Configuração de cada CMS suportado: WordPress (REST API, plugins de SEO como Yoast ou RankMath via API), Webflow CMS API, Contentful API, Ghost API
- Google Search Console API para submissão de sitemap e URL Inspection API para monitoramento de indexação
- Regras de rate limiting de publicação por tamanho de domínio: domínios novos (<1 ano) max 10 páginas/dia, domínios estabelecidos (>2 anos, >DA 30) até 100 páginas/dia
- Técnicas de internal linking automático por relevância semântica vs links manuais
- Schema markup deployment patterns por framework de CMS

## Action Items

1. Confirmar o gatilho e carregar a entrada (Conteúdo final aprovado pelo Lumen em Markdown com todos os metadados (meta title, meta description, slug, schema marku…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Confirmação de publicação por página com: URL final publicada, timestamp, status de indexação (submitted to GSC / index…) e persistir no artefato do squad.
4. Entregar ao critic Lumen; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Confirmação de publicação por página com: URL final publicada, timestamp, status de indexação (submitted to GSC / indexed / crawl_error), internal links inseri…
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

- **to:** Sonar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
