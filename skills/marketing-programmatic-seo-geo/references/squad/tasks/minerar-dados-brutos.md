---
task: orion()
responsavel: "Orion"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Templates de página programática definidos no Deep Dive (ex: página por região/vertical/caso de uso)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Acesso a bases de dados do cliente (dados de produto, preços, localizações, casos de uso por segmento)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "APIs de dados abertos relevantes ao setor (IBGE, dados.gov.br, bancos de dados setoriais)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Acesso à web via EXA para coleta de dados públicos verificáveis (estatísticas de mercado, benchmarks setoriais, pesquisas publicadas)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Configuração dos atributos de unicidade por tipo de página"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "o que torna cada página do batch única e não uma cópia"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dataset estruturado em JSON ou CSV por tipo de página programática: cada registro tem os campos obrigatórios para preencher o template (entidade principal, atributos de unicidade, dados de suporte, fontes verificáveis com URL e data, texto de suporte mínimo de 3 sentenças com dados próprios)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Score de qualidade por registro (0-100) baseado em: completude dos campos obrigatórios, verificabilidade das fontes, unicidade dos dados vs outros registros do batch"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Registros abaixo do score mínimo configurado são flagados para revisão humana ou descarte"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Dataset entregue ao Scribe como insumo de produção"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Log de fontes de cada dado"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "rastreabilidade total para o Lumen verificar"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Argo para cada novo template de página programática aprovado pelo time. Re-trigger mensal para atualizar dados de páginas já publicadas (preços, estatísticas, ranking) que ficam desatual…"
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

# Minerar Dados Brutos

**Task ID:** `orion()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Programmatic SEO + GEO/AEO

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Minerar Dados Brutos |
| **status** | `pending` |
| **responsible_executor** | Orion (Órion — O Minerador de Dados) |
| **execution_type** | `Worker` |
| **input** | 6 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Coleta, limpa e estrutura os dados brutos que viram combustível para produção programática de conteúdo em escala. Para páginas de alto volume (ex: '5.000 páginas de [produto] em [cidade]' ou 'comparativas de [categoria] por [atributo]'), Órion é quem transforma datasets em conteúdo único e não-duplicado. Conecta com APIs de dados abertos, bases internas do cliente, ferramentas de scraping e datasets públicos. Garante que CADA página programática tenha pelo menos 3 dados exclusivos e verificáveis — não é content farming, e conteúdo com substância em escala. Também alimenta o Beacon com dados estatísticos, estudos e fontes que aumentam a probabilidade de citação por LLMs.

## Input

- Templates de página programática definidos no Deep Dive (ex: página por região/vertical/caso de uso)
- Acesso a bases de dados do cliente (dados de produto, preços, localizações, casos de uso por segmento)
- APIs de dados abertos relevantes ao setor (IBGE, dados.gov.br, bancos de dados setoriais)
- Acesso à web via EXA para coleta de dados públicos verificáveis (estatísticas de mercado, benchmarks setoriais, pesquisas publicadas)
- Configuração dos atributos de unicidade por tipo de página
- o que torna cada página do batch única e não uma cópia

## Output

- Dataset estruturado em JSON ou CSV por tipo de página programática: cada registro tem os campos obrigatórios para preencher o template (entidade principal, atributos de unicidade, dados de suporte, fontes verificáveis com URL e data, texto de suporte mínimo de 3 sentenças com dados próprios)
- Score de qualidade por registro (0-100) baseado em: completude dos campos obrigatórios, verificabilidade das fontes, unicidade dos dados vs outros registros do batch
- Registros abaixo do score mínimo configurado são flagados para revisão humana ou descarte
- Dataset entregue ao Scribe como insumo de produção
- Log de fontes de cada dado
- rastreabilidade total para o Lumen verificar

## Trigger

Ativado pelo Argo para cada novo template de página programática aprovado pelo time. Re-trigger mensal para atualizar dados de páginas já publicadas (preços, estatísticas, ranking) que ficam desatualizados. Re-trigger pontual quando Sonar detecta que páginas de um batch perderam posição e um refresh de dados pode recuperar relevância. Trigger manual pelo gestor de conteúdo para novos datasets.

## Knowledge base (o que o executor consulta)

- Mapeamento de APIs de dados abertos por setor (imobiliario, saude, educacao, financeiro, varejo, agro, servicos profissionais)
- Tecnicas de web scraping ético e dentro dos terms of service das fontes
- Regras de verificacao de dados: nenhum dado estatistico publicado sem fonte, data da fonte e URL verificavel
- Templates de estrutura de dados por tipo de pagina programatica (local, vertical, comparativa, calculadora, glossario)
- Politica de dados desatualizados: dados com mais de 12 meses para estatisticas dinamicas = flag para revisao
- dados estruturais (localizacoes, atributos de produto) = revisao semestral

## Action Items

1. Confirmar o gatilho e carregar a entrada (Templates de página programática definidos no Deep Dive (ex: página por região/vertical/caso de uso)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dataset estruturado em JSON ou CSV por tipo de página programática: cada registro tem os campos obrigatórios para preen…) e persistir no artefato do squad.
4. Entregar ao critic Lumen; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dataset estruturado em JSON ou CSV por tipo de página programática: cada registro tem os campos obrigatórios para preencher o template (entidade principal, atr…
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

- **to:** Scribe
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
