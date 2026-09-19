---
task: elicitRequirements()
agent: ce-strategist
description: "Questionário de 12 perguntas estruturadas sobre produto, audience, concorrência, objetivo de conversão"
elicit: true
responsavel: "Vortex"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: productBrief
    tipo: file
    obrigatorio: true
    descricao: "Briefing inicial do produto"

Saida:
  - nome: elicitedRequirements
    tipo: file
    obrigatorio: true
    descricao: "Respostas completas ao questionário de 12 perguntas estruturadas"

Checklist:
  pre-conditions:
    - "[ ] Product brief disponível"
  post-conditions:
    - "[ ] 12 perguntas respondidas"
    - "[ ] Persona definida"
    - "[ ] Concorrentes identificados"
---

# Task: elicitRequirements()

## Objetivo
Conduzir um processo de elicitação profunda e estruturada para extrair todas as informações necessárias antes de iniciar qualquer produção. As 12 perguntas cobrem as dimensões críticas que mais impactam a conversão: produto, audiência, concorrência, prova social, oferta e infraestrutura.

## Inputs Necessários
- `product-brief.md` (output de `discoverProduct()`)
- `funnel-map.md` (output de `mapFunnelStages()`)
- Disponibilidade do cliente para responder o questionário completo
- Quaisquer documentos adicionais que o cliente queira compartilhar

## Processo
1. **Preparação do contexto** — Revisar `product-brief.md` e `funnel-map.md` para formular as perguntas com o contexto já adquirido, evitando redundância.
2. **Aplicação do questionário** — Conduzir as 12 perguntas estruturadas em formato de entrevista ou formulário assíncrono, na seguinte ordem:

   **Bloco 1 — Produto e Oferta (Q1-Q3)**
   - Q1: "Qual é a transformação específica que seu cliente experimenta após usar seu produto? Descreva antes e depois com o máximo de especificidade possível."
   - Q2: "Qual é o maior medo que um potencial cliente tem ao considerar comprar seu produto? O que o faz hesitar?"
   - Q3: "Se você só pudesse comunicar uma coisa sobre seu produto, qual seria? Qual é a 'bala de prata' da sua oferta?"

   **Bloco 2 — Audiência (Q4-Q6)**
   - Q4: "Descreva seu cliente ideal em detalhes: idade, profissão, situação de vida, frustrações do dia a dia e o que ele lê/assiste/segue."
   - Q5: "Qual é a objeção número 1 que você ouve de prospects que NÃO compram? E a segunda maior objeção?"
   - Q6: "Qual linguagem seu cliente usa para descrever o problema que você resolve? Use as palavras dele, não as suas."

   **Bloco 3 — Concorrência (Q7-Q8)**
   - Q7: "Quem são seus 3 principais concorrentes diretos? O que eles fazem bem que você admira? O que fazem mal que você faz melhor?"
   - Q8: "Por que um cliente que já tentou alternativas (concorrentes ou soluções DIY) escolheria você agora?"

   **Bloco 4 — Prova Social e Credibilidade (Q9-Q10)**
   - Q9: "Qual é o melhor resultado que um cliente seu já obteve? Tem números, prazo, situação antes/depois?"
   - Q10: "Você tem depoimentos em texto, áudio ou vídeo? Quantos? São específicos (com resultado) ou genéricos ('adorei o produto')?"

   **Bloco 5 — Objetivo e Infraestrutura (Q11-Q12)**
   - Q11: "Qual é o número que define sucesso para você nessa landing page? (ex: 200 leads/mês, taxa de conversão de 3%, R$50k em vendas no primeiro mês)"
   - Q12: "Quais ferramentas você já usa hoje? (CRM, email marketing, WhatsApp Business, gateway de pagamento, analytics)"

3. **Clarificação de respostas** — Para cada resposta vaga ou genérica, aplicar drill-down: "Pode me dar um exemplo específico?" ou "O que você quer dizer exatamente com [termo]?"
4. **Identificação de gaps** — Registrar quais informações críticas ainda estão ausentes após o questionário e propor plano para obtê-las.
5. **Consolidação em Requirements Doc** — Organizar todas as respostas em documento estruturado `requirements.md` com seções por bloco.

## Veto Conditions
- Menos de 10 das 12 perguntas respondidas com substância → não avançar para próxima fase
- Resposta à Q11 (métrica de sucesso) ausente ou vaga demais → bloquear: sem meta definida não há critério de sucesso
- Contradições críticas entre respostas (ex: "não temos concorrentes" + "nosso principal diferencial é X vs concorrente Y") → confrontar e resolver antes de prosseguir
- Ausência total de provas sociais verificáveis → registrar como bloqueador de conversão e escalar para cliente

## Output Esperado
Arquivo `requirements.md` contendo:
- As 12 perguntas com respostas detalhadas e expandidas
- Gaps identificados e plano de resolução
- Meta de conversão acordada (número concreto)
- Stack de ferramentas existentes mapeada
- Lista de flags de integração ativas (derivada das respostas de Q12)
- Síntese estratégica em 5 bullet points para os demais agentes

## Completion Criteria
- [ ] Todas as 12 perguntas respondidas com substância (mínimo 3 frases por resposta)
- [ ] Transformação antes/depois articulada com especificidade
- [ ] Objeções principais documentadas (mínimo 2)
- [ ] Linguagem nativa do cliente registrada em citações diretas
- [ ] Concorrentes identificados (mínimo 3)
- [ ] Provas sociais inventariadas com qualidade avaliada
- [ ] Meta numérica de sucesso definida
- [ ] Stack de ferramentas mapeada
- [ ] Arquivo `requirements.md` criado e disponível para os demais agentes
- [ ] Síntese estratégica produzida para handoff
