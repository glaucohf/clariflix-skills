---
task: reviewCopyQuality()
agent: ce-reviewer
description: "Revisar copy: clareza da oferta, força do headline, especificidade dos benefícios, ausência de jargões, CTA irresistível. Score: 0-100"
elicit: false
responsavel: "Audit"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: allCopy
    tipo: file
    obrigatorio: true
    descricao: "Copy completa de todas as seções"
  - nome: audienceProfile
    tipo: file
    obrigatorio: true
    descricao: "Perfil da audiência para validação de tom"

Saida:
  - nome: copyReviewScore
    tipo: file
    obrigatorio: true
    descricao: "Score de copy 0-100: clareza da oferta, força do headline, especificidade dos benefícios e CTA"

Checklist:
  pre-conditions:
    - "[ ] Copy completa disponível"
  post-conditions:
    - "[ ] Score calculado"
    - "[ ] Issues críticos listados"
    - "[ ] Aprovação ou lista de correções emitida"
---

# Task: reviewCopyQuality()

## Objetivo
Realizar uma revisão editorial final e independente de todo o copy da landing page, aplicando uma rubrica objetiva de 0-100 pontos. A revisão é conduzida pelo ce-reviewer — um agente independente, sem viés de autoria — para identificar o que o ce-copywriter pode ter deixado passar.

## Inputs Necessários
- Página final montada (todos os componentes renderizando)
- `copy-review-report.md` (revisão interna do ce-copywriter — para comparação)
- `audience-profile.md` (persona e linguagem nativa — critério de avaliação)
- `intelligence-brief.md` (ângulo principal e promessa central)
- `product-brief.md` (oferta real — para verificar se copy a representa fielmente)

## Processo
1. **Leitura completa como visitante** — Ler a LP do topo ao final como se fosse a primeira vez, sem pular. Anotar:
   - Primeiro pensamento ao ver o headline
   - Onde a atenção cai ou aumenta
   - Qual é a promessa central percebida
   - Qual é a objeção que fica na mente
   - Qual é o próximo passo esperado após a leitura

2. **Rubrica de avaliação de copy (100 pontos):**

   **Headline (25 pontos):**
   - 0-5: Genérico, poderia ser de qualquer produto do nicho
   - 6-15: Comunica benefício, mas vago ("Melhore seus resultados")
   - 16-20: Específico e relevante, mas não urgente
   - 21-25: Específico + relevante + comunica transformação clara em < 10 segundos

   **Clareza da oferta (20 pontos):**
   - 0-10: Oferta confusa após ler a página toda
   - 11-15: Oferta clara mas com elementos ambíguos
   - 16-18: Oferta clara, mas o próximo passo não é óbvio
   - 19-20: Oferta cristalina — qualquer pessoa sabe o que está recebendo e o que precisa fazer

   **Especificidade dos benefícios (20 pontos):**
   - 0-10: Benefícios genéricos ("mais eficiência", "melhores resultados")
   - 11-15: Mix de genérico e específico
   - 16-18: Maioria específico mas falta resultado mensurável
   - 19-20: Todos os benefícios com especificidade e pelo menos 50% com número/prazo

   **Ausência de jargões (15 pontos):**
   - 0-5: Múltiplos jargões de marketing (ROI, funil, leads, KPI para audiência leiga)
   - 6-10: Alguns jargões que o público não usaria
   - 11-13: Jargão pontual (1-2 casos)
   - 14-15: Zero jargões — linguagem 100% nativa do público

   **CTA (20 pontos):**
   - 0-5: CTA genérico ("Enviar", "Clique aqui")
   - 6-10: CTA com ação mas sem benefício
   - 11-15: CTA com benefício mas passivo ("Obtenha X")
   - 16-18: CTA em primeira pessoa com benefício ("Quero X")
   - 19-20: CTA irresistível: 1ª pessoa + benefício + urgência implícita + microcopy de suporte

3. **Checklist adicional (itens de veto que reduzem score a zero no critério):**
   - [ ] Copy promete resultado não suportado por prova → -10 pontos
   - [ ] Copy contradiz informações em outra seção → -10 pontos
   - [ ] Copy excessivamente longo onde deveria ser curto (hero > 3 frases) → -5 pontos
   - [ ] Copy excessivamente curto onde informação é necessária (FAQ muito vago) → -5 pontos
   - [ ] Inconsistência de pronome (você/tu misturado) → -5 pontos

4. **Avaliação de fluxo narrativo:**
   - A página conta uma história coesa do início ao fim?
   - A intensidade emocional aumenta progressivamente?
   - A oferta aparece no momento certo (não muito cedo nem muito tarde)?
   - O CTA final é o climax natural da narrativa?

5. **Benchmarks de score:**
   - 0-59: Reprovado — múltiplos problemas críticos → retornar ao ce-copywriter com lista de correções
   - 60-74: Abaixo do padrão — melhorias significativas necessárias → revisão parcial
   - 75-84: Padrão adequado — LP pode ser lançada com melhorias pontuais
   - 85-94: Bom — LP de alta qualidade, melhorias opcionais
   - 95-100: Excelente — copy de alta conversão, pronto para lançamento

## Veto Conditions
- Score < 75 → retornar ao ce-copywriter com lista priorizada de correções antes de lançar
- Score no critério de Headline < 16/25 → headline deve ser reescrita obrigatoriamente
- Promessa não suportada por prova → remover ou adicionar prova antes de lançar

## Output Esperado
Arquivo `review-copy.md` contendo:
- Leitura como visitante (impressões iniciais documentadas)
- Score por critério com justificativa
- Score total (0-100)
- Lista de problemas identificados (críticos / significativos / opcionais)
- Sugestões de melhoria específicas para cada problema crítico
- Veredicto: APROVADO / APROVADO COM RESSALVAS / REPROVADO

## Completion Criteria
- [ ] LP lida de topo a baixo como visitante (não como revisor)
- [ ] Score calculado para todos os 5 critérios
- [ ] Checklist de veto verificada
- [ ] Fluxo narrativo avaliado
- [ ] Lista de problemas criada e priorizada
- [ ] Score total calculado (0-100)
- [ ] Veredicto emitido com justificativa
- [ ] Arquivo `review-copy.md` criado
