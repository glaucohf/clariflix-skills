---
task: writeEmailSeries()
agent: ce-email-strategist
description: "Escrever série completa de emails com subject, preheader, body, CTA para cada email da sequência"
elicit: false
responsavel: "Thread"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: emailSequenceMap
    tipo: file
    obrigatorio: true
    descricao: "Mapa da sequência de emails"

Saida:
  - nome: emailSeries
    tipo: file
    obrigatorio: true
    descricao: "Série completa de emails: subject, preheader, body e CTA para cada email da sequência"

Checklist:
  pre-conditions:
    - "[ ] Mapa da sequência disponível"
  post-conditions:
    - "[ ] Todos os emails escritos"
    - "[ ] Subjects testáveis (A/B)"
    - "[ ] CTAs específicos por email"
---

# Task: writeEmailSeries()

## Objetivo
Produzir o copy completo de cada email da sequência de nurture — subject line, preheader, corpo do email e CTA — aplicando técnicas de copywriting específicas para email marketing e o framework de copy definido para o produto.

## Inputs Necessários
- `email-sequence-map.md` (mapeamento completo da sequência)
- `intelligence-brief.md` (ângulos, dores, linguagem nativa)
- `copy-review-report.md` (guia de voz e tom aprovado)
- `audience-profile.md` (persona, objeções, linguagem)
- `testimonials-structured.md` (para email de prova social)
- `product-brief.md` (produto, preço, garantia)

## Processo
Para cada email mapeado em `email-sequence-map.md`, produzir os seguintes elementos:

1. **Subject line** — O elemento mais crítico (determina se o email será aberto):
   - Máximo 50 caracteres (para não truncar em mobile)
   - Escrever 3 variantes de subject para cada email (testar abertura)
   - Evitar spam triggers: "GRÁTIS", "OFERTA", todos caps, excesso de !!! e $$$
   - Técnicas eficazes: pergunta, curiosidade, benefício específico, personalização ([NOME]), urgência legítima

   **Subject lines por tipo de email:**
   - Welcome: "Bem-vindo(a)! Veja o que preparei para você 👋"
   - Educação: "A técnica que [resultado específico] em 7 dias"
   - Prova Social: "Como [nome de cliente] conseguiu [resultado mensurável]"
   - Objeção: "[NOME], você está com essa dúvida?"
   - Oferta: "Hora de dar o próximo passo — aqui está como"
   - Urgência: "Termina amanhã: [oferta específica]"
   - Última Chance: "Última mensagem sobre [assunto]"

2. **Preheader** — Texto complementar ao subject (aparece no preview do inbox):
   - 85-100 caracteres
   - Complementa sem repetir o subject
   - Adiciona curiosidade ou benefício adicional
   - Se ausente, inbox mostra o início do corpo do email (geralmente ruim)

3. **Corpo do email** — Estrutura por tipo:

   **Email 1 — Welcome:**
   ```
   [Saudação personalizada com nome]

   [Parágrafo de confirmação — o que aconteceu e por que é um bom passo]

   [O que o lead pode esperar receber nos próximos dias — criar antecipação]

   [Próximo passo ÚNICO e claro]

   [CTA principal]

   [Assinatura pessoal — como se fosse do fundador]
   [P.S. — dica rápida ou convite para responder]
   ```

   **Email de Educação:**
   ```
   [Hook — pergunta ou afirmação que captura atenção]

   [Contexto — por que este assunto importa para o lead]

   [Conteúdo de valor — dica, insight ou framework prático]

   [Conexão com o produto — natural, não forçada]

   [CTA secundário — ler mais, assistir vídeo, ou nenhum]

   [Assinatura]
   ```

   **Email de Prova Social:**
   ```
   [Introdução — "Quero te contar a história de [Nome]"]

   [Situação antes — específica e identificável pelo lead]

   [O que mudou — o que [Nome] fez]

   [Resultado — números específicos e prazo]

   [Quote do cliente]

   [Transição para o lead — "E se você..."]

   [CTA — ver mais casos ou próximo passo]
   ```

   **Email de Objeção:**
   ```
   [Introdução — "A pergunta mais comum que recebo é..."]

   [Apresentar a objeção abertamente e sem defensividade]

   [Resposta direta e honesta — sem rodeios]

   [Prova ou evidência da resposta]

   [Convite para responder com dúvidas restantes]

   [CTA — responder email ou ver FAQ]
   ```

   **Email de Oferta:**
   ```
   [Transição natural — "Você chegou até aqui porque..."]

   [Apresentação do produto — o que é, para quem é]

   [Benefícios principais — 3-5 bullets com benefício + resultado]

   [Stack de valor — o que está incluído]

   [Garantia — apresentar como eliminação de risco]

   [Preço — com anchoring se possível]

   [CTA principal — link direto para LP/checkout]

   [P.S. — reforçar o benefício mais importante]
   ```

   **Email de Urgência:**
   ```
   [Abertura direta — sem preâmbulo]

   [A oferta — muito brevemente]

   [O prazo — específico e real]

   [O que acontece depois do prazo — consequência real]

   [CTA com urgência]

   [Reforço do benefício + garantia em 1 linha]
   ```

4. **Boas práticas de formatação de email HTML:**
   - Largura máxima: 600px
   - Fonte: Sistema (Arial, Helvetica) — não depender de web fonts
   - Tamanho mínimo: 14px para body, 18px para heading
   - Espaço em branco abundante — emails densos têm baixa leitura
   - Imagens: opcional, sempre com alt text (muitos clientes bloqueiam imagens)
   - Botão de CTA: mínimo 44px de altura, cor contrastante, texto descritivo
   - Versão plain text obrigatória para entregabilidade

5. **Elementos de cada email produzido:**
   - Subject A (principal)
   - Subject B e C (variantes para teste)
   - Preheader
   - HTML do email (responsivo)
   - Versão plain text
   - Notas de personalização (campos dinâmicos)

## Veto Conditions
- Subject com palavra de spam ("GRÁTIS" em caps, "$$", "urgente urgente") → reescrever
- Email sem preheader → adicionar obrigatoriamente
- Body sem versão plain text → criar antes de finalizar
- Email de urgência com prazo não-real → criar urgência legítima ou remover urgência
- CTA genérico ("Clique aqui") → reescrever com benefício específico

## Output Esperado
Arquivo `email-series.md` contendo, para cada email da sequência:
- Subject A + Subject B + Subject C
- Preheader
- Corpo completo em HTML comentado
- Versão plain text
- Notas de configuração para a plataforma de automação

## Completion Criteria
- [ ] 100% dos emails mapeados em `email-sequence-map.md` escritos
- [ ] 3 variantes de subject para cada email
- [ ] Preheader único e complementar para cada email
- [ ] Corpo seguindo estrutura correta por tipo de email
- [ ] Versão plain text de cada email
- [ ] CTAs específicos e orientados a benefício em cada email
- [ ] Tom consistente com guia de voz aprovado
- [ ] Email de urgência com prazo legítimo
- [ ] Arquivo `email-series.md` criado e entregue para `setupAutomation()`
