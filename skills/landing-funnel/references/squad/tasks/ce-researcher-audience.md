---
task: profileAudience()
agent: ce-researcher
description: "Perfil detalhado: dores, desejos, objeções, linguagem, nível de consciência (Schwartz awareness levels)"
elicit: false
responsavel: "Radar"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: productBrief
    tipo: file
    obrigatorio: true
    descricao: "Briefing do produto"

Saida:
  - nome: audienceProfile
    tipo: file
    obrigatorio: true
    descricao: "Perfil detalhado: dores, desejos, objeções, linguagem e nível de consciência (Schwartz)"

Checklist:
  pre-conditions:
    - "[ ] Product brief disponível"
  post-conditions:
    - "[ ] Nível de consciência definido (Schwartz)"
    - "[ ] Top 5 dores documentadas"
    - "[ ] Top 5 objeções listadas"
---

# Task: profileAudience()

## Objetivo
Construir um perfil de audiência profundo e multidimensional que vai além de demografia básica. O objetivo é entender a psicologia do comprador — seus medos, desejos, linguagem e estágio de consciência — para que o copy e o design falem diretamente com o estado mental do visitante no momento da chegada à LP.

## Inputs Necessários
- `product-brief.md` (descrição do público-alvo pelo cliente)
- `requirements.md` (Q4 sobre cliente ideal, Q5 sobre objeções, Q6 sobre linguagem)
- `funnel-map.md` (temperatura e nível de consciência do tráfego)
- `competitive-analysis.md` (como concorrentes posicionam sua audiência)
- Fontes de pesquisa primária: Reddit, grupos do Facebook, reviews Amazon, Reclame Aqui, comentários YouTube, fóruns do nicho

## Processo
1. **Pesquisa de linguagem nativa** — Varrer fontes onde o público se expressa organicamente:
   - Reddit (subreddits do nicho)
   - Grupos do Facebook relacionados ao problema
   - Reviews de produtos concorrentes (Amazon, G2, Capterra)
   - Comentários em vídeos do YouTube sobre o tema
   - Reclame Aqui (dores com soluções existentes)
   - Fóruns especializados do nicho
   Coletar frases EXATAS que o público usa — estas frases são ouro para headlines e bullets.

2. **Mapeamento de dores e desejos** — Criar lista priorizada:
   - TOP 5 dores (o que mais irrita, frustra ou preocupa)
   - TOP 5 desejos (o que mais querem conquistar ou experimentar)
   - TOP 3 medos (o que os impede de agir — medos de comprar errado, de não ter resultado)
   - TOP 3 frustrações com soluções anteriores (por que já tentaram e falharam)

3. **Mapeamento de objeções** — Classificar objeções por tipo:
   - **Objeções de preço:** "É caro", "Não tenho dinheiro agora", "Preciso de resultado antes de investir"
   - **Objeções de tempo:** "Não tenho tempo para aprender/implementar"
   - **Objeções de credibilidade:** "Será que funciona para mim?", "Já tentei coisas parecidas"
   - **Objeções de prioridade:** "Não é urgente agora"
   Para cada objeção, identificar o argumento de contra-objeção mais eficaz.

4. **Classificação pelo Schwartz Awareness Level** — Determinar o nível de consciência predominante do tráfego:
   - **Unaware:** Não sabe que tem o problema → copy foca na dor latente
   - **Problem-aware:** Sabe do problema, não sabe da solução → copy foca no problema e agitação
   - **Solution-aware:** Sabe que soluções existem, não conhece o produto → copy foca na solução superior
   - **Product-aware:** Conhece o produto, não decidiu comprar → copy foca em diferenciais e provas
   - **Most-aware:** Já quer comprar, precisa da oferta → copy foca em urgência e condições

5. **Criação de Persona Primária** — Sintetizar em 1 persona detalhada:
   - Nome fictício, idade, profissão, situação de vida
   - Dia típico e contexto de chegada à LP
   - Frase que diria ao ver a LP pela primeira vez
   - O que precisa VER, SENTIR e CRER para converter

6. **Persona Secundária** — Se houver segmento significativo distinto, criar segunda persona mais breve.

## Veto Conditions
- Perfil baseado apenas em percepção do cliente sem pesquisa em fontes primárias → repetir com fontes reais
- Nível de consciência não definido → bloquear: afeta diretamente a estratégia de copy
- Menos de 5 frases nativas do público coletadas de fontes reais → ampliar pesquisa

## Output Esperado
Arquivo `audience-profile.md` contendo:
- Pesquisa de linguagem nativa (mínimo 15 frases coletadas com fonte)
- TOP 5 dores priorizadas
- TOP 5 desejos priorizados
- TOP 3 medos mapeados com contra-objeções
- TOP 3 frustrações com soluções anteriores
- Mapeamento de objeções por categoria com contra-argumentos
- Nível de consciência definido com justificativa
- Persona primária completa
- Persona secundária (se aplicável)

## Completion Criteria
- [ ] Mínimo 15 frases nativas do público coletadas de fontes primárias (com referência)
- [ ] TOP 5 dores priorizadas e descritas
- [ ] TOP 5 desejos priorizados e descritos
- [ ] Objeções mapeadas por categoria com contra-argumentos
- [ ] Nível de consciência Schwartz definido com justificativa
- [ ] Persona primária criada com todos os campos
- [ ] Arquivo `audience-profile.md` criado e disponível para ce-copywriter e ce-design-architect
