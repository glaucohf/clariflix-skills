---
task: synthesizeIntelligence()
agent: ce-researcher
description: "Consolidar toda pesquisa em Intelligence Brief: TOP 3 ângulos de copy, TOP 5 dores, TOP 3 diferenciais, benchmarks de conversão do nicho"
elicit: false
responsavel: "Radar"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: competitorAnalysis
    tipo: file
    obrigatorio: true
    descricao: "Análise competitiva completa"
  - nome: audienceProfile
    tipo: file
    obrigatorio: true
    descricao: "Perfil da audiência"
  - nome: copyFormulas
    tipo: file
    obrigatorio: true
    descricao: "Fórmulas de copy do nicho"

Saida:
  - nome: intelligenceBrief
    tipo: file
    obrigatorio: true
    descricao: "Intelligence Brief consolidado: top 3 ângulos de copy, top 5 dores, diferenciais e benchmarks"

Checklist:
  pre-conditions:
    - "[ ] Todos os inputs de pesquisa disponíveis"
  post-conditions:
    - "[ ] Intelligence Brief gerado"
    - "[ ] Top 3 ângulos de copy definidos"
    - "[ ] Benchmarks de conversão incluídos"
---

# Task: synthesizeIntelligence()

## Objetivo
Consolidar toda a inteligência coletada nas tasks anteriores em um único Intelligence Brief de alta densidade que servirá como referência definitiva para todos os agentes produtivos do squad. Esta task transforma dados em insights acionáveis.

## Inputs Necessários
- `competitive-analysis.md` (output de `spyCompetitors()`)
- `audience-profile.md` (output de `profileAudience()`)
- `copy-formulas.md` (output de `researchCopyFormulas()`)
- `traffic-data-analysis.md` (output de `analyzeTrafficData()`)
- `product-brief.md` e `requirements.md` (contexto do produto)

## Processo
1. **Síntese dos ângulos de copy** — Cruzar dores do público, diferenciais do produto e lacunas competitivas para identificar os 3 ângulos de copy mais promissores:
   - **Ângulo 1 (Principal):** O mais forte, alinha maior dor com maior diferencial
   - **Ângulo 2 (Alternativo):** Para teste A/B ou segmento secundário
   - **Ângulo 3 (Disruptivo):** Vai contra a convenção do nicho — alto risco, alto retorno
   Para cada ângulo: nome, promessa central, audiência primária, nível de consciência alvo.

2. **Priorização das TOP 5 dores** — Ranquear as dores do público por:
   - Frequência de menção (quantas pessoas expressam esta dor)
   - Intensidade emocional (nível de urgência e frustração)
   - Relevância para o produto (o produto resolve diretamente?)
   - Aproveitamento pela concorrência (dor explorada ou virgem?)
   Resultado: TOP 5 dores com score de prioridade e linguagem nativa a usar.

3. **Definição dos TOP 3 diferenciais** — Identificar os 3 diferenciais do produto mais relevantes para o público:
   - Diferencial 1: O mais forte e verificável (com prova)
   - Diferencial 2: O mais emocional (gera desejo)
   - Diferencial 3: O que elimina a maior objeção
   Para cada diferencial: como articular em 1 frase, qual prova sustenta, onde posicionar na LP.

4. **Consolidação de benchmarks** — Sintetizar em tabela única:
   - Taxa de conversão LP: conservador/realista/otimista
   - CPL alvo e CPL benchmark do nicho
   - CTR esperado por plataforma de tráfego
   - Tempo médio de sessão esperado
   - Taxa de rejeição esperada
   - Mobile/desktop split

5. **Mapa de prioridades para o squad** — Definir prioridades de execução:
   - O que é NON-NEGOTIABLE na LP (sem isso não lança)
   - O que é de alta prioridade (impacto direto na conversão)
   - O que é desejável (melhoria incremental)
   - O que é para fase 2 (backlog)

6. **Briefing por agente** — Criar seção específica para cada agente ativo com os insights mais relevantes para sua função:
   - Para ce-copywriter: ângulos, dores, linguagem nativa, framework de copy
   - Para ce-design-architect: perfil de dispositivos, CRO insights, estilo visual do nicho
   - Para ce-analytics-architect: métricas-alvo, eventos críticos, benchmarks
   - Para ce-social-proof: qualidade das provas existentes, gaps a preencher
   - Para ce-ab-architect: elementos com maior potencial de teste, hipóteses iniciais

## Veto Conditions
- Síntese produzida sem cruzar dados de todas as tasks anteriores → voltar e completar inputs
- Ângulos de copy sem respaldo em dados de audiência reais → reformular com base na pesquisa
- Benchmarks ausentes ou sem fonte → completar antes de fechar o brief

## Output Esperado
Arquivo `intelligence-brief.md` contendo:
- Resumo executivo (1 página)
- TOP 3 ângulos de copy com desenvolvimento
- TOP 5 dores priorizadas com linguagem nativa
- TOP 3 diferenciais articulados com prova
- Tabela de benchmarks consolidada
- Mapa de prioridades (NON-NEGOTIABLE → fase 2)
- Briefing por agente (seção para cada agente ativo)

## Completion Criteria
- [ ] Todos os 4 documentos de pesquisa consumidos e cruzados
- [ ] TOP 3 ângulos de copy definidos e desenvolvidos
- [ ] TOP 5 dores priorizadas com score e linguagem nativa
- [ ] TOP 3 diferenciais articulados com prova verificável
- [ ] Benchmarks consolidados em tabela única com fontes
- [ ] Mapa de prioridades definido
- [ ] Briefing específico criado para cada agente ativo
- [ ] Arquivo `intelligence-brief.md` criado como referência central para produção
