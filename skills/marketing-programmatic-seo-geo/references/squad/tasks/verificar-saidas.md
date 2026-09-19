---
task: lumenVerificar()
responsavel: "Lumen"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Atlas: qualquer publicacao ou edicao de paginas na lista de URLs estrategicas (pillar pages, paginas com backlinks externos, paginas de alta competicao definidas no onboarding) bloqueia e notifica o gestor de conteudo com preview completo para aprovacao antes de publicar um caracter."
    - "[ ] HITL: Lumen reprova 2x no mesmo item: conteúdo que falhou no ciclo automático de otimização (Scribe ou Beacon reescreve 1x, Lumen reprova novamente) e escalado para o editor humano com o checklist completo de reprovações e sugestões específicas de correção."
    - "[ ] HITL: Factualidade questionável detectada pelo Lumen: qualquer dado que não tem fonte verificável com URL ativo e data recente é imediatamente bloqueado e sinalizado para o time de conteúdo verificar manualmente antes de qualquer publicação — zero tolerância para afirmação sem rastreabilidade."
    - "[ ] HITL: Batch de publicação programática acima de 50 páginas: qualquer batch acima do threshold configurado (default: 50 páginas/batch) requer aprovação do gestor de SEO antes do Atlas iniciar a publicação — para proteger o crawl budget e a reputação do domínio."
    - "[ ] HITL: Queda abrupta de visibilidade detectada pelo Sonar: queda de >30% em tráfego orgânico em 7 dias ou desaparecimento de cluster inteiro das SERPs = alerta imediato ao time de SEO para investigação manual antes de qualquer ação automática do squad — pode ser update algorítmico que requer análise humana."
---

# Verificar Saídas do Programmatic SEO + GEO/AEO

**Task ID:** `lumenVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Programmatic SEO + GEO/AEO

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Programmatic SEO + GEO/AEO |
| **status** | `pending` |
| **responsible_executor** | Lumen (Lumen — O Guardião da Qualidade Editorial) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Lumen — O Guardiao da Qualidade Editorial — Valida TODO conteudo gerado pelo Scribe e otimizado pelo Beacon antes de qualquer publicacao. Checklist obrigatorio de 10 pontos — reprovar em qualquer ponto critico bloqueia a publicacao: (1) SEO Score minimo: o conteudo atinge o score minimo configurado no Frase ou SemRush (baseline: 70/100 para producao programatica, 80/100 para artigos editoriais)? Abaixo do threshold = REESCREVER com instrucoes especificas; (2) Factualidade: CADA afirmacao factual tem fonte verificavel com URL e data? Zero tolerancia para dados sem fonte — qualquer dado sem rastreabilidade = REPROVAR; (3) Unicidade: a pagina tem menos de 20% de overlap textual com outras paginas do mesmo dominio (canibalizacao) e menos de 10% com conteudo externo (plágio)? Verificado via ferramenta de similarity check; (4) GEO Score minimo: o conteudo tem pelo menos 3 elementos explicitamente citable por LLMs (stat block, definition box, answer snippet, tabela comparativa com dados)? Abaixo do threshold = OTIMIZAR com Beacon antes de publicar; (5) Brand compliance: o tom, vocabulario e posicionamento estao alinhados com o guia de voz da marca? Nenhuma afirmacao que o cliente nao possa defender publicamente; (6) E-E-A-T signals: o conteudo demonstra experiencia e especialidade reais? Links para fontes autoritativas, dados de primeira parte quando disponiveis, perspectiva especialista — nao conteudo generico de IA sem substantia; (7) Internal linking: as sugestoes de internal link do Atlas fazem sentido contextual? Links forcados ou irrelevantes = corrigir antes de publicar; (8) Conteudo thin: cada pagina tem no minimo 800 palavras de conteudo real (nao contando boilerplate de navegacao, footer, etc)? Paginas thin abaixo de 800 palavras = expandir ou combinar com outra pagina do batch; (9) Metadata quality: meta title <= 60 chars com keyword, meta description <= 155 chars com CTA, slug limpo sem stopwords? Qualquer campo fora do spec = corrigir automaticamente; (10) Duplicate metadata: os campos de meta title e meta description sao unicos no dominio inteiro? Duplicata encontrada = gerar nova variacao automaticamente. Veredicto: APROVADO (segue para Atlas publicar) / OTIMIZAR com instrucoes especificas por ponto (volta para Scribe ou Beacon, max 1 ciclo automatico) / BLOQUEAR_HITL para casos que exigem revisao humana (factualidade questionavel, compliance de marca, conteudo em cluster estrategico de alta competicao). Opera em paralelo em todos os itens do batch — nunca um a um sequencialmente.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- O Guardiao da Qualidade Editorial
- Valida TODO conteudo gerado pelo Scribe e otimizado pelo Beacon antes de qualquer publicacao
- Checklist obrigatorio de 10 pontos
- reprovar em qualquer ponto critico bloqueia a publicacao: (1) SEO Score minimo: o conteudo atinge o score minimo configurado no Frase ou SemRush (baseline: 70/100 para producao programatica, 80/100 para artigos editoriais)? Abaixo do threshold = REESCREVER com instrucoes especificas
- (2) Factualidade: CADA afirmacao factual tem fonte verificavel com URL e data? Zero tolerancia para dados sem fonte
- qualquer dado sem rastreabilidade = REPROVAR
- (3) Unicidade: a pagina tem menos de 20% de overlap textual com outras paginas do mesmo dominio (canibalizacao) e menos de 10% com conteudo externo (plágio)? Verificado via ferramenta de similarity check
- (4) GEO Score minimo: o conteudo tem pelo menos 3 elementos explicitamente citable por LLMs (stat block, definition box, answer snippet, tabela comparativa com dados)? Abaixo do threshold = OTIMIZAR com Beacon antes de publicar
- (5) Brand compliance: o tom, vocabulario e posicionamento estao alinhados com o guia de voz da marca? Nenhuma afirmacao que o cliente nao possa defender publicamente
- (6) E-E-A-T signals: o conteudo demonstra experiencia e especialidade reais? Links para fontes autoritativas, dados de primeira parte quando disponiveis, perspectiva especialista
- nao conteudo generico de IA sem substantia
- (7) Internal linking: as sugestoes de internal link do Atlas fazem sentido contextual? Links forcados ou irrelevantes = corrigir antes de publicar
- (8) Conteudo thin: cada pagina tem no minimo 800 palavras de conteudo real (nao contando boilerplate de navegacao, footer, etc)? Paginas thin abaixo de 800 palavras = expandir ou combinar com outra pagina do batch
- (9) Metadata quality: meta title <= 60 chars com keyword, meta description <= 155 chars com CTA, slug limpo sem stopwords? Qualquer campo fora do spec = corrigir automaticamente
- (10) Duplicate metadata: os campos de meta title e meta description sao unicos no dominio inteiro? Duplicata encontrada = gerar nova variacao automaticamente
- Veredicto: APROVADO (segue para Atlas publicar) / OTIMIZAR com instrucoes especificas por ponto (volta para Scribe ou Beacon, max 1 ciclo automatico) / BLOQUEAR_HITL para casos que exigem revisao humana (factualidade questionavel, compliance de marca, conteudo em cluster estrategico de alta competicao)
- Opera em paralelo em todos os itens do batch
- nunca um a um sequencialmente

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Argo para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Argo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
