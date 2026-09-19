---
task: writeSectionCopy()
agent: ce-copywriter
description: "Escrever copy de uma seção com framework AIDA ou PAS, headline testável, subheadline, body, CTA"
elicit: false
responsavel: "Pulse"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: intelligenceBrief
    tipo: file
    obrigatorio: true
    descricao: "Intelligence Brief da pesquisa"
  - nome: sectionName
    tipo: string
    obrigatorio: true
    descricao: "Nome da seção a ser escrita"

Saida:
  - nome: sectionCopy
    tipo: file
    obrigatorio: true
    descricao: "Copy completo da seção: headline, subheadline, body e CTA com framework AIDA ou PAS"

Checklist:
  pre-conditions:
    - "[ ] Intelligence Brief disponível"
    - "[ ] Seção definida no escopo"
  post-conditions:
    - "[ ] Headline testável escrita"
    - "[ ] CTA claro e específico"
    - "[ ] Tom alinhado à audiência"
---

# Task: writeSectionCopy()

## Objetivo
Produzir o copy completo de uma seção específica da landing page, aplicando o framework selecionado, a linguagem nativa do público e os diferenciais do produto. Cada seção deve funcionar autonomamente (visitante pode entrar na seção em qualquer ponto do scroll) e como parte do fluxo narrativo da página.

## Inputs Necessários
- `intelligence-brief.md` (ângulos, dores, diferenciais, linguagem nativa)
- `copy-formulas.md` (frameworks e swipe file do nicho)
- `scope.md` (lista de seções e objetivos de cada uma)
- `audience-profile.md` (persona, nível de consciência, objeções)
- Identificação da seção a ser escrita (nome + objetivo específico)

## Processo
1. **Definição do papel da seção no fluxo narrativo** — Antes de escrever, responder:
   - Qual o estado emocional do visitante ao chegar nesta seção?
   - O que ele precisa sentir/crer ao sair desta seção para continuar?
   - Como esta seção conecta com a anterior e a próxima?

2. **Seleção do framework** — Escolher AIDA ou PAS com base no objetivo da seção:
   - **AIDA** para seções de: Hero, Benefícios, Pricing, oferta geral
   - **PAS** para seções de: Por que isso importa, Agitação de dor, antes-depois
   - **BAB (Before-After-Bridge)** para seções de: Transformação, depoimentos contextualizados
   - **FAB (Features-Advantages-Benefits)** para seções de: Como funciona, características técnicas

3. **Produção do copy da seção** — Escrever todos os elementos:
   - **Headline:** 1 frase principal que captura atenção e comunica o benefício central. Testar 3 variações antes de escolher.
   - **Subheadline:** 1-2 frases que ampliam a headline e qualificam o visitante ideal.
   - **Body copy:** Texto que desenvolve a promessa, apresenta provas, supera objeções. Usar frases curtas, parágrafos de no máximo 3 linhas, marcadores quando apropriado.
   - **Bullet points (se aplicável):** Estrutura: "[Verbo de ação] + [benefício específico] + [detalhe que aumenta credibilidade]". Evitar bullets genéricos.
   - **CTA:** Texto do botão + microcopy de suporte (eliminar hesitação). CTA deve ser específico do benefício, não genérico ("Comece agora" é fraco; "Quero minha primeira semana grátis" é forte).
   - **Elemento de prova (se aplicável):** Depoimento, número, certificação, logo de cliente.

4. **Revisão de qualidade de copy** — Verificar cada elemento contra checklist:
   - Headline: específica, clara, testável, comunica benefício real?
   - Body: usa linguagem nativa do público (das pesquisas)? Evita jargões? Fala de benefícios, não de features?
   - CTA: específico, orientado a benefício, primeira pessoa ("Quero X" funciona melhor que "Obtenha X")?
   - Tom: consistente com a voz da marca e nível de consciência do público?

5. **Geração de variantes para headline e CTA** — Produzir 2 variantes adicionais de headline e CTA para uso nos testes A/B (ce-ab-architect consumirá estes dados).

## Veto Conditions
- Copy usa jargões de marketing que o público não usaria → reescrever com linguagem nativa
- Headline genérica que se aplicaria a qualquer produto do nicho → reescrever com especificidade
- CTA com verbo passivo ("Saiba mais", "Clique aqui") sem benefício → reescrever
- Body copy com mais de 50% do texto sobre features em vez de benefícios → rebalancear
- Promessas não sustentadas por prova disponível → adaptar à prova real ou remover

## Output Esperado
Para cada seção, arquivo `copy-[nome-da-secao].md` contendo:
- Versão principal completa (headline + subheadline + body + bullets + CTA)
- 2 variantes de headline alternativas
- 2 variantes de CTA alternativas
- Justificativa de escolhas de copy (qual dor endereça, qual diferencial usa, qual framework aplica)
- Notas para o ce-design-architect (hierarquia visual desejada, elementos de ênfase)

## Completion Criteria
- [ ] Headline principal escrita e testada contra 2 alternativas
- [ ] Subheadline complementar e qualificadora produzida
- [ ] Body copy com framework definido (AIDA/PAS/BAB/FAB) aplicado
- [ ] Bullet points específicos (não genéricos) escritos
- [ ] CTA principal específico e orientado a benefício
- [ ] 2 variantes de headline e CTA geradas para A/B
- [ ] Copy revisada contra checklist de qualidade
- [ ] Notas para ce-design-architect incluídas
- [ ] Arquivo `copy-[nome-da-secao].md` criado
