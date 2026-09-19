---
task: researchCopyFormulas()
agent: ce-researcher
description: "Identificar fórmulas de copy que funcionam no nicho: hooks, headlines, CTAs, estruturas de oferta"
elicit: false
responsavel: "Radar"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: audienceProfile
    tipo: file
    obrigatorio: true
    descricao: "Perfil da audiência"
  - nome: competitorAnalysis
    tipo: file
    obrigatorio: true
    descricao: "Análise competitiva"

Saida:
  - nome: copyFormulas
    tipo: file
    obrigatorio: true
    descricao: "Fórmulas de copy validadas no nicho: hooks, headlines, CTAs e estruturas de oferta"

Checklist:
  pre-conditions:
    - "[ ] Audiência perfilada"
    - "[ ] Concorrentes analisados"
  post-conditions:
    - "[ ] 3+ fórmulas de headline identificadas"
    - "[ ] CTAs validados no nicho"
---

# Task: researchCopyFormulas()

## Objetivo
Identificar e catalogar as fórmulas de copy comprovadas que funcionam especificamente no nicho do produto. Não se trata de fórmulas genéricas de marketing — mas de padrões observados em anúncios longevos, páginas de alta conversão e copy vencedora do segmento específico.

## Inputs Necessários
- `competitive-analysis.md` (anúncios e copy dos concorrentes)
- `audience-profile.md` (linguagem nativa, dores, nível de consciência)
- `product-brief.md` (nicho e tipo de produto)
- `funnel-map.md` (papel da LP no funil)

## Processo
1. **Catalogação de hooks de alto desempenho** — Analisar anúncios ativos de longa data no nicho (identificados na `competitive-analysis.md`) e extrair padrões de hooks:
   - Hooks de dor direta: "[Dor específica] ainda te perseguindo em [contexto]?"
   - Hooks de resultado: "Como [persona] conseguiu [resultado específico] em [tempo]"
   - Hooks de curiosidade: "O método [X] que [autoridade] não quer que você saiba"
   - Hooks de identidade: "Para quem [identidade específica] que [situação]"
   - Hooks de urgência: "[Evento] muda tudo. Você está preparado?"
   Registrar quais tipos dominam no nicho.

2. **Análise de headlines vencedoras** — Coletar headlines de landing pages de alta conversão no nicho e classificar por estrutura:
   - **Benefício direto:** "Consiga [resultado] em [tempo] sem [objeção]"
   - **Transformação:** "De [estado antes] para [estado depois] em [prazo]"
   - **Curiosidade:** "O único [X] que [promessa surpreendente]"
   - **Especificidade:** "[Número] [nicho] já [resultado] com [método]"
   - **Autoridade:** "O sistema que [credencial] usa para [resultado]"
   Identificar a estrutura dominante no nicho e por quê funciona.

3. **Pesquisa de CTAs eficazes no nicho** — Identificar padrões de CTA que convertem:
   - Tom (urgência, benefício, identidade, comando, curiosidade)
   - Verbos predominantes
   - Especificidade vs generalidade
   - Uso de urgência ou escassez no CTA
   Listar TOP 5 estruturas de CTA do nicho.

4. **Análise de estruturas de oferta** — Identificar como os concorrentes apresentam a oferta:
   - Anchoring de preço (preço original riscado vs preço atual)
   - Bônus e stacking de valor
   - Garantias (tipos, períodos, condições)
   - Urgência real vs artificial (countdown, vagas limitadas, bônus por tempo)
   - Formas de pagamento destacadas

5. **Identificação de frameworks de copy do nicho** — Determinar qual framework predomina:
   - **AIDA** (Atenção → Interesse → Desejo → Ação) — LP clássica, tráfego frio
   - **PAS** (Problema → Agitação → Solução) — Nichos de dor alta, copy de resposta direta
   - **PASTOR** (Problem → Amplify → Story → Testimony → Offer → Response) — Produto complexo
   - **4Ps** (Promise → Picture → Proof → Push) — Produtos de resultado rápido
   - **Before-After-Bridge** — Nichos de transformação
   Justificar escolha com dados do nicho.

6. **Compilação de Copy Swipe File do Nicho** — Criar biblioteca de referências:
   - 5 headlines de referência (com fonte)
   - 3 hooks de anúncio de referência (com fonte)
   - 5 CTAs de referência (com fonte)
   - 3 estruturas de oferta de referência (com fonte)
   - 2 estruturas de bullet points de referência

## Veto Conditions
- Fórmulas catalogadas sem referência a fontes reais do nicho → não aceitar — fórmulas genéricas não servem
- Framework de copy escolhido sem justificativa baseada em dados → repetir análise
- Swipe file com menos de 5 headlines reais de referência → ampliar pesquisa

## Output Esperado
Arquivo `copy-formulas.md` contendo:
- TOP 5 hooks por tipo com exemplos reais do nicho
- TOP 5 estruturas de headline com exemplos e fonte
- TOP 5 CTAs estruturados com exemplos
- Padrões de apresentação de oferta do nicho
- Framework de copy recomendado para a LP com justificativa
- Copy Swipe File do nicho (referências organizadas por elemento)

## Completion Criteria
- [ ] Mínimo 5 hooks analisados com exemplos reais do nicho
- [ ] Mínimo 5 estruturas de headline catalogadas com fontes
- [ ] Padrões de CTA identificados com TOP 5 estruturas
- [ ] Padrões de apresentação de oferta documentados
- [ ] Framework de copy recomendado com justificativa baseada em dados
- [ ] Swipe file criada com referências verificáveis
- [ ] Arquivo `copy-formulas.md` criado e disponível para ce-copywriter
