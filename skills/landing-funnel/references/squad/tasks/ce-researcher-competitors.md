---
task: spyCompetitors()
agent: ce-researcher
description: "Análise aprofundada de 5+ concorrentes: copy, design, offers, preços, anúncios ativos. Veto: menos de 5 concorrentes = repetir."
elicit: false
responsavel: "Radar"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: productBrief
    tipo: file
    obrigatorio: true
    descricao: "Briefing do produto com nicho e concorrentes conhecidos"

Saida:
  - nome: competitorAnalysis
    tipo: file
    obrigatorio: true
    descricao: "Análise de 5+ concorrentes: copy, design, ofertas, preços e anúncios ativos"

Checklist:
  pre-conditions:
    - "[ ] Nicho definido no product brief"
  post-conditions:
    - "[ ] Mínimo 5 concorrentes analisados"
    - "[ ] Anúncios ativos mapeados"
    - "[ ] Gaps de posicionamento identificados"
---

# Task: spyCompetitors()

## Objetivo
Realizar uma análise competitiva profunda e sistemática de no mínimo 5 concorrentes diretos. O objetivo não é copiar, mas entender o que o mercado já treinou os consumidores a esperar — e onde há lacunas que o produto do cliente pode explorar.

## Inputs Necessários
- `product-brief.md` (nicho, produto, público)
- `requirements.md` (concorrentes mencionados pelo cliente em Q7)
- `scope.md` (contexto de posicionamento)
- Acesso a ferramentas de inteligência competitiva (SimilarWeb, SEMrush, SpyFu, Meta Ads Library, Google Ads Transparency Center)

## Processo
1. **Identificação do universo competitivo** — Expandir lista de concorrentes além dos citados pelo cliente. Incluir:
   - Concorrentes diretos (mesmo produto, mesmo público)
   - Concorrentes indiretos (soluções alternativas para o mesmo problema)
   - Referências de conversão do nicho (líderes de mercado, mesmo que não sejam concorrentes diretos)
   - Players internacionais relevantes (especialmente EUA/UK para tendências futuras)

2. **Análise de landing pages** — Para cada concorrente, documentar:
   - Headline principal e promessa central
   - Estrutura de seções (ordem, quantidade)
   - Oferta de entrada (lead magnet, trial, demo, compra direta)
   - Preço e modelo de pricing (se visível)
   - Provas sociais utilizadas (tipo, quantidade, especificidade)
   - CTA principal (texto, cor, posição)
   - Urgência e escassez (real ou artificial)
   - Garantias oferecidas
   - Design system predominante (cores, fontes, estilo visual)

3. **Análise de anúncios ativos** — Verificar Meta Ads Library e Google Ads Transparency Center para cada concorrente:
   - Formatos usados (vídeo, carrossel, estático, UGC)
   - Ângulos de copy predominantes nos anúncios (dor, curiosidade, resultado, autoridade)
   - Hooks mais recorrentes
   - Há quanto tempo os anúncios estão ativos (anúncios longos = provável winner)
   - Volume estimado de anúncios ativos

4. **Análise de SEO e tráfego** — Verificar via SimilarWeb ou SEMrush:
   - Volume de tráfego estimado
   - Principais fontes de tráfego
   - Palavras-chave que trazem tráfego orgânico
   - Backlink profile básico

5. **Identificação de padrões e lacunas** — Sintetizar padrões recorrentes em todos os concorrentes e identificar:
   - O que TODOS fazem (expectativas de mercado a respeitar)
   - O que NINGUÉM faz (oportunidade de diferenciação)
   - Onde o produto do cliente pode vencer na comparação direta

6. **Scorecard comparativo** — Criar tabela comparativa: cliente vs TOP 3 concorrentes em 10 dimensões (oferta, preço, garantia, prova social, copy, design, velocidade, nurture, suporte, diferencial).

## Veto Conditions
- Menos de 5 concorrentes analisados → repetir pesquisa até atingir o mínimo
- Análise superficial (apenas homepage, sem anúncios) → aprofundar antes de avançar
- Nenhuma lacuna competitiva identificada → rever critérios de análise e expandir para concorrentes internacionais
- Dados de anúncios ausentes (não verificou Meta Ads Library) → completar antes de fechar análise

## Output Esperado
Arquivo `competitive-analysis.md` contendo:
- Perfil detalhado de cada concorrente (mínimo 5)
- Screenshots ou descrições detalhadas de suas LPs
- Análise de anúncios ativos por concorrente
- Padrões recorrentes no nicho
- Lacunas competitivas identificadas (mínimo 3)
- Scorecard comparativo cliente vs TOP 3
- TOP 3 insights acionáveis para a LP do cliente

## Completion Criteria
- [ ] Mínimo 5 concorrentes analisados em profundidade
- [ ] Landing page de cada concorrente documentada (headline, estrutura, oferta, CTA, provas)
- [ ] Anúncios ativos verificados para cada concorrente (Meta Ads Library + Google)
- [ ] Estimativa de tráfego obtida para TOP 3 concorrentes
- [ ] Padrões recorrentes do nicho listados
- [ ] Mínimo 3 lacunas competitivas identificadas
- [ ] Scorecard comparativo preenchido
- [ ] TOP 3 insights acionáveis documentados
- [ ] Arquivo `competitive-analysis.md` criado e disponível para os demais agentes
