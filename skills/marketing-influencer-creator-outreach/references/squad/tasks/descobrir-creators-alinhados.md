---
task: radarScout()
responsavel: "Radar Scout"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Creator Persona Matrix (nicho, categorias, tier de seguidores, regiao, plataformas prioritarias) gerada no Deep Dive"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Lista de hashtags e categorias de conteudo relevantes por produto/vertical do cliente"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Acesso a APIs de plataformas: Insense (base de creators opt-in), HypeAuditor (metricas de audiencia), Instagram Graph API (dados publicos), TikTok Research API"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Mencoes organicas da marca rastreadas via social listening"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Budget disponivel por tier para pre-filtro de viabilidade"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê bruto de creator por perfil descoberto com 5 secoes: (1) Identificacao"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "handle/URL por plataforma, nome real quando disponivel, nicho principal e secundario, regiao, idioma"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Metricas Brutas"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "seguidores por plataforma, taxa de engajamento bruta (likes+comentarios/seguidores), media de views (Reels/TikToks ultimos 30 dias), frequencia de postagem"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Categorias de Conteudo"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "tags de conteudo dos ultimos 30 posts, presenca de conteudo patrocinado (tag #ad, #publi), categorias de produto que ja promoveu"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Trigger automatico diario para descoberta de novos creators por hashtag e categoria configurada. Trigger em tempo real para mencoes organicas da marca detectadas via social listening (fast-track imed…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Parceiro Certo antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou R$5.000 dependendo do budget do cliente) bloqueia e notifica o gestor de marketing com proposta completa, score do creator e benchmarking de mercado para aprovacao antes de qualquer envio."
    - "[ ] HITL: Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evidencias coletadas para decisao humana de vetamento ou aprovacao com risco consciente — nunca o squad decide sozinho sobre risco de reputacao da marca."
    - "[ ] HITL: Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #publi) ou representacao incorreta do produto que requer revisao do time juridico ou de marketing antes de qualquer resposta ao creator."
    - "[ ] HITL: ROAS Tracker detecta ROAS >= 5x em D+7: alerta de oportunidade imediato ao gestor de marketing e ao time de performance para decisao de amplificacao via ads pagos do post do creator — decisao de investimento adicional e sempre humana."
    - "[ ] HITL: ROAS Tracker detecta ROAS < 0.5x em D+14: alerta ao gestor de marketing para revisao da estrategia de creator daquele nicho ou campanha — pode indicar desalinhamento de ICP ou problema de produto que nao deve ser escondido por mais investimento."
---

# Descobrir Creators Alinhados

**Task ID:** `radarScout()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Influencer & Creator Outreach Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Descobrir Creators Alinhados |
| **status** | `pending` |
| **responsible_executor** | Radar Scout (Radar Scout — O Prospector de Talentos) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 12 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Descobre e mapeia continuamente creators alinhados ao ICP da marca em plataformas como Instagram, TikTok, YouTube e Kwai. Usa a Creator Persona Matrix definida no Deep Dive para filtrar por nicho, categoria de conteudo, tamanho de audiencia e regiao. Extrai dados publicos e via API de plataformas de creator marketplace (Insense, HypeAuditor) para construir o dossiê inicial de cada creator descoberto. Nao avalia fit — apenas descobre e documenta. Alimenta a fila do Persona Fit Analyst com dossiês brutos priorizados por relevancia de nicho. Opera em modo continuo: monitora hashtags, categorias e mencoes da marca para identificar creators que ja falam organicamente do produto — estes recebem fast-track na fila de avaliacao.

## Input

- Creator Persona Matrix (nicho, categorias, tier de seguidores, regiao, plataformas prioritarias) gerada no Deep Dive
- Lista de hashtags e categorias de conteudo relevantes por produto/vertical do cliente
- Acesso a APIs de plataformas: Insense (base de creators opt-in), HypeAuditor (metricas de audiencia), Instagram Graph API (dados publicos), TikTok Research API
- Mencoes organicas da marca rastreadas via social listening
- Budget disponivel por tier para pre-filtro de viabilidade

## Output

- Dossiê bruto de creator por perfil descoberto com 5 secoes: (1) Identificacao
- handle/URL por plataforma, nome real quando disponivel, nicho principal e secundario, regiao, idioma
- (2) Metricas Brutas
- seguidores por plataforma, taxa de engajamento bruta (likes+comentarios/seguidores), media de views (Reels/TikToks ultimos 30 dias), frequencia de postagem
- (3) Categorias de Conteudo
- tags de conteudo dos ultimos 30 posts, presenca de conteudo patrocinado (tag #ad, #publi), categorias de produto que ja promoveu
- (4) Sinal de Afinidade
- mencao organica da marca (sim/nao), categoria de produto do cliente ja na grade de conteudo (sim/nao), linguagem alinhada aos valores da marca (avaliacao preliminar sim/nao/inconclusivo)
- (5) Fontes
- URLs de perfil, data de captura dos dados
- Score de completude do dossiê (0-100)
- Artefato salvo no ClickUp e fila do Persona Fit Analyst atualizada com o creator

## Trigger

Trigger automatico diario para descoberta de novos creators por hashtag e categoria configurada. Trigger em tempo real para mencoes organicas da marca detectadas via social listening (fast-track imediato). Trigger manual pelo time de marketing para pesquisa pontual por categoria ou campanha especifica. Trigger semanal para varredura de creators que interagiram com os posts da marca (curtidas, comentarios, compartilhamentos) mas ainda nao foram mapeados.

## Knowledge base (o que o executor consulta)

- Taxonomia de nichos e micro-nichos por vertical de produto (moda, beleza, saude, fitness, gastronomia, lifestyle, tecnologia, financas pessoais, parentalidade, pets)
- Benchmarks de taxa de engajamento por tier e plataforma: micro Instagram (3-6%), micro TikTok (5-12%), mid-tier Instagram (1.5-3%), macro Instagram (0.5-1.5%)
- Plataformas de creator marketplace com acesso opt-in: Insense (foco e-commerce e DTC), Hoox (foco video UGC), Squid (mercado brasileiro)
- Criterios de brand safety pre-filtro: categorias de conteudo proibidas para o cliente, mencoes a concorrentes diretos, historico de controversia
- Calendario de sazonalidade por vertical para priorizar descoberta nos 60 dias anteriores ao pico de demanda

## Action Items

1. Confirmar o gatilho e carregar a entrada (Creator Persona Matrix (nicho, categorias, tier de seguidores, regiao, plataformas prioritarias) gerada no Deep Dive).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossiê bruto de creator por perfil descoberto com 5 secoes: (1) Identificacao) e persistir no artefato do squad.
4. Entregar ao critic Parceiro Certo; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossiê bruto de creator por perfil descoberto com 5 secoes: (1) Identificacao
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Parceiro Certo registrado
- [ ] Gate HITL respeitado: Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou…
- [ ] Gate HITL respeitado: Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evi…
- [ ] Gate HITL respeitado: Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #p…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou R$5.000 dependendo… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evidencias coletadas pa… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #publi) ou representac… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — ROAS Tracker detecta ROAS >= 5x em D+7: alerta de oportunidade imediato ao gestor de marketing e ao time de performance para decisao de amplificacao via ads pa… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — ROAS Tracker detecta ROAS < 0.5x em D+14: alerta ao gestor de marketing para revisao da estrategia de creator daquele nicho ou campanha — pode indicar desalinh… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Creator solicita ajuste contratual apos assinatura (exclusividade, prazo, valor, direitos de imagem ampliados): qualquer renegociacao apos contrato assinado e… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Content Guardian nao recebe rascunho em D-1 do deadline: escalacao urgente ao time de marketing para decisao sobre extensao de prazo ou substituicao do creator… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Persona Fit Analyst detecta queda >= 25% no score medio de ROAS por categoria de creator em 2 ciclos consecutivos de campanha: alerta estrategico ao gestor de… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Parceiro Certo | BLOQUEIA entrega |

## Handoff

- **to:** Persona Fit Analyst
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
