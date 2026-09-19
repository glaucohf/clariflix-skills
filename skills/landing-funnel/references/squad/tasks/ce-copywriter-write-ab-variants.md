---
task: writeABVariants()
agent: ce-copywriter
description: "EXCLUSIVO: criar 2 variantes de copy para cada elemento testável: headline principal, CTA principal, oferta"
elicit: false
responsavel: "Pulse"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: originalCopy
    tipo: file
    obrigatorio: true
    descricao: "Copy original já aprovada"

Saida:
  - nome: abVariants
    tipo: file
    obrigatorio: true
    descricao: "2 variantes de copy por elemento testável: headline principal, CTA principal e oferta"

Checklist:
  pre-conditions:
    - "[ ] Copy original disponível"
  post-conditions:
    - "[ ] Variante A e B para headline"
    - "[ ] Variante A e B para CTA"
    - "[ ] Hipótese documentada por variante"
---

# Task: writeABVariants()

## Objetivo
Produzir variantes de copy sistematicamente fundamentadas em hipóteses claras para os elementos de maior impacto na conversão. Cada variante deve testar uma única dimensão (ângulo, tom, especificidade, urgência) para que os resultados do teste sejam interpretáveis e acionáveis pelo ce-ab-architect.

## Inputs Necessários
- Todos os arquivos `copy-[seção].md` produzidos pelo ce-copywriter
- `intelligence-brief.md` (ângulos alternativos identificados)
- `audience-profile.md` (personas e objeções)
- `traffic-data-analysis.md` (benchmarks para definir o que testar primeiro)
- `scope.md` (flag `ab_testing` deve estar ativa)

## Processo
1. **Priorização de elementos a testar** — Selecionar os 3 elementos com maior impacto esperado na conversão:
   - **Headline principal** (maior impacto — visitante decide em 3s se continua)
   - **CTA principal** (segundo maior impacto — onde a decisão é tomada)
   - **Oferta/Pricing** (terceiro — percepção de valor vs preço)
   Justificar priorização com dados (qual elemento tem maior potencial de melhoria baseado em benchmarks).

2. **Variantes de Headline** — Para cada headline principal, criar 2 variantes que testem dimensões diferentes:

   **Dimensões testáveis:**
   - **Ângulo:** Mesma promessa, abordagem diferente (dor vs resultado vs curiosidade vs autoridade)
   - **Especificidade:** Vaga ("Transforme seu negócio") vs Específica ("Aumente seu faturamento em 40% em 90 dias")
   - **Audiência:** Genérica vs Segmentada ("Para coaches que...")
   - **Urgência:** Sem urgência vs Com urgência ("Antes que seja tarde")
   - **Tom:** Emocional vs Racional; Suave vs Direto

   Para cada variante: nome da dimensão testada, texto da headline, hipótese de por que deve converter melhor.

3. **Variantes de CTA** — Para cada CTA principal, criar 2 variantes:

   **Dimensões testáveis:**
   - **Pessoa gramatical:** 1ª pessoa ("Quero X") vs 2ª pessoa ("Obtenha X") vs Imperativo ("Comece X")
   - **Benefício vs Ação:** Foco no que o visitante recebe vs foco no que ele faz
   - **Urgência:** CTA neutro vs CTA com urgência ("Garantir minha vaga agora")
   - **Especificidade:** Genérico ("Começar") vs Específico ("Quero minha análise gratuita")
   - **Risco:** Sem redução de risco vs Com microcopy de risco ("Sem cartão. Cancele quando quiser.")

4. **Variantes de Oferta** — Criar 2 variantes de apresentação da oferta:

   **Dimensões testáveis:**
   - **Anchoring:** Sem âncora de preço vs Com preço original riscado
   - **Framing:** Custo ("R$297") vs Valor ("Menos que 1 consultoria")
   - **Stack de bônus:** Listagem explícita de bônus vs Apresentação do produto completo sem separar bônus
   - **Garantia em destaque:** Garantia no final vs Garantia próxima ao preço
   - **Parcelamento:** Exibir parcelamento antes vs Exibir preço total antes

5. **Documentação de hipóteses** — Para CADA variante, escrever a hipótese formal:
   "Acreditamos que [variante B] irá [direção esperada da métrica] a taxa de [métrica] para [audiência] porque [evidência ou razão baseada em pesquisa]."

6. **Handoff para ce-ab-architect** — Estruturar output no formato que o ce-ab-architect precisa para configurar os testes.

## Veto Conditions
- Variantes que testam mais de uma dimensão simultaneamente → dividir em testes separados
- Variante sem hipótese documentada → escrever hipótese antes de aprovar
- Variantes que contradizem o posicionamento ou tom da marca → revisar
- Mais de 3 elementos sendo testados simultaneamente → priorizar e serializar testes

## Output Esperado
Arquivo `ab-copy-variants.md` contendo:
- Lista de elementos priorizados para teste (com justificativa)
- Para headline principal: variante A (controle) + variante B + variante C (se relevante), cada uma com hipótese
- Para CTA principal: variante A (controle) + variante B + variante C (se relevante), cada uma com hipótese
- Para oferta: variante A (controle) + variante B, cada uma com hipótese
- Sequência recomendada de testes (qual testar primeiro e por quê)
- Critério de sucesso por elemento (qual métrica determina vencedor)

## Completion Criteria
- [ ] Mínimo 3 elementos priorizados para teste com justificativa
- [ ] 2 variantes escritas para headline principal (além do controle)
- [ ] 2 variantes escritas para CTA principal (além do controle)
- [ ] 2 variantes escritas para apresentação de oferta (além do controle)
- [ ] Hipótese formal documentada para cada variante
- [ ] Cada variante testa exatamente 1 dimensão (não múltiplas)
- [ ] Sequência de testes definida
- [ ] Critério de sucesso definido por elemento
- [ ] Arquivo `ab-copy-variants.md` criado e disponível para ce-ab-architect
