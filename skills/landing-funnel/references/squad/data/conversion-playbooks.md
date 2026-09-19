# Conversion Playbooks — Convert Engine Squad

> Base de conhecimento de referência para os agentes do squad `convert-engine`. Contém benchmarks reais de conversão, padrões de copy comprovados, estruturas de página e estratégias de otimização por nicho. Todos os agentes devem consultar o playbook do nicho correspondente antes de gerar qualquer conteúdo.

---

## Como usar este documento

Cada agente deve:

1. Identificar o nicho do projeto (campo `niche` no brief do cliente)
2. Ler o playbook completo do nicho correspondente
3. Usar os benchmarks como referência para definir metas de conversão realistas
4. Aplicar as copy formulas e estruturas recomendadas
5. Adaptar os trust signals e provas sociais ao contexto específico do cliente
6. Registrar resultados reais em `docs/conversion-report.md` para enriquecer esta base

---

## Benchmarks Globais de Referência

> Fonte: HubSpot State of Marketing 2024, WordStream 2024, Unbounce Conversion Benchmark Report 2024

| Métrica | Mediana Global | Top 10% | Top 1% |
|---|---|---|---|
| Taxa de conversão (lead) | 2.35% | 5.31% | 11.45% |
| Taxa de conversão (venda) | 0.5% – 1.5% | 3% – 5% | 8%+ |
| Taxa de abertura de email | 21.5% | 35%+ | 50%+ |
| CTR email | 2.3% | 5%+ | 10%+ |
| Bounce rate landing page | 60% – 70% | 40% – 50% | < 35% |

---

## Nicho 1: SaaS (Software as a Service)

### Benchmarks de Conversão

| Funil | Mediana | Top quartil | Referência |
|---|---|---|---|
| Visitante → Trial gratuito | 2% – 5% | 8% – 12% | Drift, Intercom |
| Trial → Pago | 15% – 25% | 30% – 40% | Benchmark: 25% |
| Demo request (B2B) | 1% – 3% | 4% – 8% | — |
| Freemium → Pago | 2% – 5% | 8% – 12% | Spotify, Dropbox |
| Lead magnet (B2B) | 10% – 15% | 25% – 40% | — |

**Custo de Aquisição (CAC) de referência:**
- SaaS SMB: US$100 – US$500
- SaaS Mid-Market: US$500 – US$2.000
- SaaS Enterprise: US$5.000 – US$50.000+

### Estrutura de Página Recomendada

```
1. Hero — Proposta de Valor Clara
   ├── Headline: O que o software faz + para quem + resultado
   ├── Subheadline: Como ele faz (mecanismo único)
   ├── CTA primário: "Começar grátis" / "Ver demonstração"
   └── Social proof instantâneo: logos + "X empresas confiam"

2. Prova Social Imediata
   ├── Logos de clientes reconhecidos (acima do fold se possível)
   └── Número: "X+ equipes" ou "Y+ projetos gerenciados"

3. Problema → Agitação → Solução
   ├── Reconhecimento da dor atual (sem o produto)
   ├── Custo do problema (tempo, dinheiro, oportunidade perdida)
   └── Transição suave para a solução

4. Demonstração Visual
   ├── GIF animado ou vídeo curto (< 60s) do produto em ação
   ├── Capturas de tela das funcionalidades-chave
   └── Tooltip / callout destacando o diferencial

5. Features como Benefícios
   ├── Máximo 3-5 features principais (não listar tudo)
   ├── Cada feature: título (benefício) + descrição + ícone
   └── CTA intermediário

6. Prova Social Detalhada
   ├── Case studies: empresa + problema + resultado mensurável
   ├── Depoimentos com foto real + cargo + empresa
   └── G2, Capterra, Trustpilot ratings (embeds ou screenshots)

7. Pricing
   ├── Máximo 3 planos (Starter / Pro / Enterprise)
   ├── Highlight no plano recomendado ("Mais popular")
   ├── Comparativo: o que inclui vs. não inclui
   └── FAQ de preços inline

8. FAQ
   └── 5-8 perguntas focadas em objeções de compra

9. CTA Final
   └── Repetição do hero com urgência adicional se aplicável
```

### Copy Formulas que Funcionam (SaaS)

**Headline Formulas:**

```
[VERBO DE AÇÃO] [TAREFA] [3x / 10x] mais rápido com [NOME DO PRODUTO]
Ex: "Feche propostas 3x mais rápido com o Proposal AI"

[RESULTADO DESEJADO] sem [DOR / OBSTÁCULO]
Ex: "Relatórios de vendas perfeitos sem planilhas manuais"

O [CATEGORIA] que as equipes de [EMPRESA DE REFERÊNCIA] usam para [RESULTADO]
Ex: "O CRM que as equipes da HubSpot usam para escalar"

Pare de [PROBLEMA]. Comece a [RESULTADO POSITIVO].
Ex: "Pare de perder leads. Comece a converter mais."
```

**CTA Button Copy (ordem de eficácia testada):**
1. "Começar grátis agora" (urgência + gratuidade)
2. "Ver demonstração em 2 minutos" (baixo comprometimento)
3. "Experimente por 14 dias grátis" (trial + tempo definido)
4. "Quero aumentar minhas conversões" (orientado ao resultado)

**Microcopy abaixo do CTA:**
- "Sem cartão de crédito. Sem burocracia. Cancel quando quiser."
- "Setup em menos de 5 minutos."
- "Junte-se a X.XXX empresas que já usam."

### Social Proof Types (SaaS)

| Tipo | Impacto | Quando usar |
|---|---|---|
| Logos de clientes enterprise | Alto | Always — acima do fold se possível |
| G2 / Capterra rating (4.8+) | Alto | Próximo ao pricing |
| Case study com ROI mensurável | Muito alto | Middle of page |
| Video testimonial (30-60s) | Muito alto | Seção dedicada |
| Quote + foto + cargo | Médio | Ao longo da página |
| Press mentions | Médio | Após hero |
| NPS / CSAT score | Médio | Próximo ao pricing |

### Objeções Comuns e Respostas

| Objeção | Resposta no copy |
|---|---|
| "É muito caro" | ROI calculator / "paga-se em X dias" |
| "Minha equipe não vai adotar" | "Onboarding em 2h" + suporte dedicado |
| "Preciso migrar meus dados" | "Migração gratuita incluída" |
| "E se não funcionar?" | Garantia de devolução + trial sem risco |
| "É seguro?" | SOC2, GDPR, LGPD badges + uptime SLA |

---

## Nicho 2: Infoprodutos e Cursos Online

### Benchmarks de Conversão

| Funil | Mediana | Top quartil | Referência |
|---|---|---|---|
| Visitante → Lead (isca digital) | 15% – 35% | 40% – 60% | — |
| Lead → Webinar | 20% – 40% | 50%+ | — |
| Webinar → Venda | 3% – 8% | 10% – 20% | — |
| Página de vendas direta | 1% – 3% | 5% – 10% | — |
| Lançamento (lista quente) | 3% – 8% | 10% – 25% | — |
| Upsell pós-compra | 10% – 25% | 30% – 50% | — |

**Ticket Médio por Formato:**
- Mini-curso (< R$200): conversão mais fácil, volume
- Curso principal (R$500 – R$2.000): sweet spot brasileiro
- Mentoria/Programa (R$3.000 – R$15.000): qualificação de lead crítica
- High-ticket / Mastermind (R$15.000+): funil de aplicação

### Estrutura de VSL (Video Sales Letter)

```
[0:00 – 0:30] HOOK — Disrupt Pattern
├── Afirmação controversa ou promessa ousada
└── "Continue assistindo porque vou te mostrar [promessa específica]"

[0:30 – 2:00] IDENTIFICAÇÃO DO PROBLEMA
├── Agitação: o custo real de não resolver
├── Validação: "Eu sei como você se sente"
└── História pessoal de identificação

[2:00 – 5:00] HISTÓRIA DE TRANSFORMAÇÃO
├── De → Para (o próprio criador ou cliente)
├── O momento de virada (revelação do mecanismo)
└── Credenciais legitimadoras (resultados, não títulos)

[5:00 – 8:00] MECANISMO ÚNICO
├── Por que as outras soluções não funcionam
├── A descoberta / método proprietário
└── Como funciona (sem revelar tudo)

[8:00 – 12:00] APRESENTAÇÃO DO PRODUTO
├── O que é + o que não é
├── Módulos / etapas do método
└── Resultados de alunos (específicos e verificáveis)

[12:00 – 15:00] EMPILHAMENTO DE VALOR
├── Valor de cada módulo / bônus
├── Total "real" vs. preço de hoje
└── Bônus por ação imediata

[15:00 – 17:00] PROVA SOCIAL
└── Depoimentos em vídeo de alunos reais

[17:00 – 19:00] GARANTIA
└── Garantia incondicional de X dias

[19:00 – 20:00] CTA COM URGÊNCIA
├── Por que agir agora (prazo, vagas, preço)
└── Chamada clara para o botão

[20:00+] FAQ E OBJEÇÕES
└── Resposta às principais objeções em vídeo
```

### Copy Formulas (Infoprodutos)

**Headline Formulas:**

```
Como [RESULTADO ESPECÍFICO] em [PRAZO] mesmo que [OBJEÇÃO PRINCIPAL]
Ex: "Como faturar R$10.000/mês como freelancer em 90 dias mesmo que você nunca tenha tido clientes"

O método [NOME] que me permitiu [RESULTADO] sem [SACRIFÍCIO]
Ex: "O método ARCA que me permitiu perder 20kg sem academia e sem dieta restritiva"

[NÚMERO] [NICHO] já estão usando este método para [RESULTADO]
Ex: "14.000 médicos já estão usando este método para atrair pacientes pelo Instagram"
```

**Empilhamento de Valor (Stack):**
```
Módulo 1: [Nome] — Valor: R$497
Módulo 2: [Nome] — Valor: R$397
Módulo 3: [Nome] — Valor: R$297
Bônus 1: [Nome] — Valor: R$197
Bônus 2: [Nome] — Valor: R$197
Bônus 3 (exclusivo para quem comprar hoje): [Nome] — Valor: R$497

Total real: R$2.082
Hoje por apenas: R$997
```

### Urgência e Escassez (Ética e Eficaz)

**Urgência Genuína (preferível):**
- Prazo de lançamento real (72h, 7 dias)
- Próxima turma começa em X dias
- Preço aumenta em X horas
- Bônus disponível apenas até [data]

**Escassez Genuína:**
- Vagas limitadas em mentoria/grupo de suporte
- Acesso às lives ao vivo (não apenas gravações)
- Acompanhamento personalizado limitado por capacidade

**Implementação no copy:**
```
Headline do timer: "Esta oferta encerra em:"
[COUNTDOWN TIMER]
Subtext: "Após esse prazo, o preço volta para R$1.997 — ou encerramos as inscrições."
```

**Nota:** nunca usar urgência/escassez falsa. Isso destrói credibilidade a longo prazo e viola o CDC.

### Pricing Psychology (Cursos)

| Estratégia | Como implementar | Efeito |
|---|---|---|
| Anchor Pricing | Mostrar "De R$1.997 por R$997" | +40% percepção de valor |
| Charm Pricing | R$997 vs. R$1.000 | Pequeno mas positivo |
| Parcelamento | "Apenas R$97/mês" abaixo do preço cheio | Reduz barreira de entrada |
| Garantia reversa | "Você arriscou mais em [algo menor]" | Reduz percepção de risco |
| Comparação de custo | "Menos de R$3,30/dia" | Trivializa o valor |
| Comparação de alternativas | "1 sessão de coaching = R$500" | Ancora em alternativa cara |

---

## Nicho 3: E-commerce

### Benchmarks de Conversão

| Métrica | Mediana Global | Top quartil | Top 1% |
|---|---|---|---|
| Taxa de conversão geral | 1% – 3% | 3% – 5% | 8%+ |
| Abandono de carrinho | 69% – 75% | 55% – 65% | < 50% |
| Taxa de recuperação de carrinho | 5% – 8% | 10% – 15% | 20%+ |
| Retorno de clientes (repeat) | 20% – 30% | 40% – 50% | 60%+ |
| AOV (Ticket Médio) | Varia por categoria | — | — |
| Email CTR | 2% – 4% | 5% – 8% | 10%+ |

**Conversão por Fonte de Tráfego (referência):**
- Email list: 4% – 8%
- SEO/Orgânico: 2% – 4%
- Paid Social (Meta): 0.9% – 2%
- Google Shopping: 1.5% – 3%
- Retargeting: 2% – 5%

### Above-the-Fold Elements Essenciais

```
Header
├── Logo
├── Navegação principal (categorias)
├── Carrinho com item counter
└── Barra de benefícios: "Frete grátis acima de R$X | Troca fácil | Parcele em X×"

Hero
├── Oferta principal (produto hero ou coleção)
├── Headline: proposta de valor única ou oferta
├── Imagem de produto em alta qualidade (fundo branco ou lifestyle)
├── CTA: "Comprar agora" / "Ver coleção"
└── Social proof: "X avaliações 5 estrelas" ou "Mais vendido"
```

### Trust Signals por Posição na Página

| Posição | Trust Signal | Impacto |
|---|---|---|
| Header | Selos de segurança (SSL, Reclame Aqui) | Alto — visibilidade constante |
| Próximo ao CTA de compra | Formas de pagamento aceitas | Muito alto |
| Próximo ao preço | Parcelas sem juros | Alto |
| Página de produto | Reviews com fotos | Muito alto |
| Checkout | Garantia de satisfação + prazo devolução | Muito alto |
| Footer | CNPJ, endereço, certificações | Médio — credibilidade legal |

### Checkout Optimization

**Regras de ouro:**
1. Máximo 3 etapas: Dados pessoais → Entrega → Pagamento
2. Mostrar resumo do pedido em todas as etapas
3. Progresso visual (step indicator)
4. Guest checkout disponível (não forçar cadastro)
5. Autofill de endereço via CEP
6. Múltiplas formas de pagamento: Pix, cartão, boleto
7. Selos de segurança visíveis na etapa de pagamento
8. "Seu pedido está seguro" + ícone de cadeado

**Micro-conversões de recuperação:**
- Popup de exit intent com desconto (5-10%) ou frete grátis
- Email de carrinho abandonado: série de 3 emails (1h, 24h, 72h)
- Retargeting dinâmico com produto do carrinho
- WhatsApp de recuperação (opt-in explícito)

### Copy para E-commerce

**Títulos de produto:**
```
[MARCA] [PRODUTO] [ATRIBUTO CHAVE] — [BENEFIT]
Ex: "Nike Air Max 2024 Masculino — Amortecimento máximo para corrida"

[ADJETIVO EMOCIONAL] [PRODUTO] para [OCASIÃO]
Ex: "Vestido elegante midi para festas e formaturas"
```

**Descrição de produto (fórmula F-A-B):**
```
Feature: O que é / o que tem
Advantage: O que faz / como funciona
Benefit: O que significa para você

Ex:
Feature: "Tecido 100% algodão Pima peruano"
Advantage: "2x mais macio que o algodão convencional, com durabilidade 3x maior"
Benefit: "Você vai querer usar essa camiseta todo dia — e ela vai durar anos"
```

---

## Nicho 4: Serviços e Agências

### Benchmarks de Conversão

| Funil | Mediana | Top quartil |
|---|---|---|
| Visitante → Lead (contato/orçamento) | 2% – 5% | 8% – 15% |
| Lead → Reunião qualificada | 20% – 40% | 50% – 70% |
| Reunião → Proposta enviada | 60% – 80% | 85%+ |
| Proposta → Fechamento | 20% – 35% | 40% – 60% |
| Ticket médio por nicho | R$2.000 – R$30.000/mês | — |

**Ciclo de vendas médio:**
- Serviços SMB: 1 – 4 semanas
- Serviços Mid-Market: 1 – 3 meses
- Serviços Enterprise: 3 – 12 meses

### Estrutura de Página para Agências

```
1. Hero — Posicionamento Claro
   ├── Para quem você é (nicho/segmento específico)
   ├── O que entrega (resultado, não serviço)
   └── CTA: "Agendar conversa estratégica" (não "fale conosco")

2. Credenciais Imediatas
   ├── Anos de experiência + número de projetos
   ├── Logos de clientes reconhecidos
   └── Premiações e certificações relevantes

3. O Problema que Você Resolve
   ├── Sintomas que o cliente sente (não jargão técnico)
   └── Custo de não resolver (oportunidade perdida, concorrência)

4. Metodologia / Processo
   ├── Etapas claras e numeradas (3-5 etapas)
   ├── O que o cliente faz vs. o que você faz
   └── Prazo esperado para cada fase

5. Cases de Sucesso
   ├── Formato: Empresa → Desafio → Solução → Resultado
   ├── Resultado SEMPRE mensurável: %, R$, tempo, ranking
   └── Testemunho do responsável pelo projeto

6. Prova Social
   ├── Depoimentos em vídeo de clientes reais
   └── NPS / avaliações verificáveis

7. Garantias e Diferenciais
   ├── O que torna seu trabalho único (não "qualidade" ou "comprometimento")
   └── Garantia de resultado ou de processo

8. Pricing / Transparência
   ├── Modelos de contratação disponíveis
   ├── Faixa de investimento (mesmo que "a partir de")
   └── O que está e não está incluído

9. CTA Final
   └── Formulário de briefing ou calendário de reunião
```

### Formato de Case Study (ROI Proof)

```markdown
## [Nome da Empresa] — [Setor]

### O Desafio
[Empresa] enfrentava [problema específico e mensurável]. Em [período],
[consequência quantificada do problema].

### A Solução
Implementamos [metodologia/serviço] com foco em [3 ações principais].
O processo levou [prazo] e envolveu [recursos/equipe].

### Os Resultados (em [prazo])
- [Métrica principal]: de X para Y (+Z%)
- [Métrica secundária]: de X para Y
- [Resultado em R$]: R$ X gerados / economizados
- [Resultado qualitativo]: equipe, processos, posicionamento

### O que o cliente diz
> "[Citação direta do tomador de decisão, com cargo e empresa]"
> — [Nome], [Cargo], [Empresa]
```

### Copy Formulas (Agências/Serviços)

**Headline Formulas:**

```
Ajudamos [NICHO] a [RESULTADO MENSURÁVEL] em [PRAZO]
Ex: "Ajudamos e-commerces a reduzir CAC em 40% em 90 dias"

[RESULTADO] para [NICHO] — Sem [OBSTÁCULO]
Ex: "Mais clientes qualificados para clínicas — Sem depender de indicações"

A agência de [SERVIÇO] que [PROVA SOCIAL ESPECÍFICA]
Ex: "A agência de tráfego que gerou R$2M em vendas para nossos clientes em 2024"
```

**CTA para Agências:**
- "Quero uma análise gratuita do meu negócio" (valor claro)
- "Agendar conversa estratégica" (menos ameaçador que "venda")
- "Ver se tenho perfil para trabalhar com vocês" (inversão de qualificação)
- "Solicitar proposta personalizada"

### Garantias que Convertem

| Tipo de Garantia | Eficácia | Como oferecer |
|---|---|---|
| Garantia de resultado (ex: "X leads ou devolvemos") | Muito alta | Apenas se você tem certeza de entrega |
| Garantia de processo ("reuniões semanais, relatórios semanais") | Alta | Sempre — é o mínimo |
| Garantia de satisfação (30 dias de cancelamento) | Alta | Baixo risco para a agência |
| Garantia de exclusividade por região/nicho | Média | Diferencial de posicionamento |
| Garantia de prazo | Média | Com cláusulas claras |

---

## Nicho 5: Saúde e Bem-estar

### Benchmarks de Conversão

| Funil | Mediana | Top quartil |
|---|---|---|
| Visitante → Lead (conteúdo gratuito) | 10% – 25% | 30% – 50% |
| Lead → Consulta agendada | 15% – 30% | 40%+ |
| Consulta → Venda de programa | 30% – 50% | 60%+ |
| Programa online → Renovação | 20% – 40% | 50%+ |
| Ticket médio (programa 3 meses) | R$1.500 – R$6.000 | — |

### Compliance e Considerações Regulatórias

**CFM (Medicina), CFO (Odontologia), CFF (Farmácia), CRN (Nutrição):**

| Proibido | Permitido |
|---|---|
| Garantir resultados específicos ("emagreça X kg") | Descrever o método e o processo |
| Comparativo com concorrentes | Depoimentos de pacientes (com consentimento expresso) |
| Preço de procedimento em anúncio | Preço em página de destino (não em ad criativo) |
| "Cura" de doenças | "Auxílio no tratamento", "bem-estar", "qualidade de vida" |
| Antes e depois em anúncios Meta/Google | Antes e depois na landing page com disclaimer |
| Assegurar eficácia de tratamento | Compartilhar estudos científicos |

**Disclaimers obrigatórios:**
```
"Os resultados podem variar de pessoa para pessoa. Este [programa/conteúdo]
não substitui acompanhamento médico/nutricional individualizado. Consulte
sempre um profissional de saúde habilitado."

"As informações contidas nesta página têm caráter educativo e não constituem
prescrição médica, diagnóstico ou tratamento."
```

**Aviso para Meta Ads:**
- Categoria Especial: Saúde deve ser declarada na conta de anúncios
- Antes/depois proibido nos criativos de anúncio (ok na landing page)
- Não usar linguagem de "cura" ou "tratamento" nos ads

### Proof Standards (Saúde)

**Hierarquia de evidências (maior para menor impacto):**

1. Estudos clínicos / artigos científicos revisados por pares
2. Dados próprios agregados (ex: "em X pacientes, média de Y resultado")
3. Depoimentos verificáveis com nome completo e consentimento
4. Antes e depois com dados objetivos (peso, exames, medidas)
5. Endorsement de autoridades da área (com CRM/CRN/CRO visível)

**Formato de depoimento para saúde:**
```
[Foto real do cliente — com autorização]
"[Depoimento em primeira pessoa, específico e honesto]"
— [Nome Completo], [Cidade/Estado]
[Resultado específico: "Perdi 12kg em 4 meses" ou "Minhas dores reduziram 80%"]
*Resultados individuais. Os resultados podem variar.
```

### Estrutura de Página (Saúde/Bem-estar)

```
1. Hero — Transformação e Esperança
   ├── Headline: estado atual (dor) → estado desejado (resultado)
   ├── Sem promessas impossíveis
   └── CTA: "Agendar avaliação gratuita" / "Quero melhorar minha saúde"

2. Identificação e Empatia
   ├── "Você se identifica com isso?" + lista de sintomas/situações
   └── Validação emocional — o cliente se sente compreendido

3. Por que não funcionou antes
   ├── Explicação do problema raiz (educacional, não crítico)
   └── Apresentação do método diferenciado

4. Credenciais do Profissional
   ├── Formação + pós-graduação + registro no conselho (CRM/CRN etc.)
   ├── Publicações, pesquisas, palestras
   └── Foto profissional de qualidade

5. O Método / Programa
   ├── Etapas claras
   ├── Frequência de atendimentos/acompanhamento
   └── O que está incluído

6. Resultados de Pacientes/Clientes
   ├── Antes e depois com dados objetivos
   └── Depoimentos em vídeo (maior credibilidade)

7. Garantias e Segurança
   ├── Satisfação garantida (se aplicável ao modelo)
   └── Sigilo e ética profissional

8. FAQ — Objeções Específicas de Saúde
   └── "É seguro?", "Para meu caso específico funciona?", "Quanto tempo leva?"

9. CTA Final
   └── Agendamento ou formulário de aplicação
```

### Copy Formulas (Saúde)

**Headline Formulas (compliance-safe):**

```
Descubra como [RESULTADO] sem [SACRIFÍCIO OU RISCO]
Ex: "Descubra como recuperar sua energia sem depender de café e estimulantes"

[PROFISSIONAL] ajuda [PÚBLICO] a [RESULTADO] com [MÉTODO]
Ex: "Nutricionista especializada ajuda mulheres acima de 40 a emagrecer com saúde e sem restrições"

Chega de [DOR/FRUSTRAÇÃO]. Conheça [MÉTODO/SOLUÇÃO]
Ex: "Chega de dores nas costas que limitam sua vida. Conheça o método de fisioterapia postural que está transformando nossos pacientes"
```

**Copywriting de Empatia (eficaz em saúde):**
```
"Eu sei o que é acordar todo dia se sentindo [dor/limitação]."
"Você já tentou [solução comum] e não funcionou?"
"Não é fraqueza. É falta da abordagem certa."
"Você merece [estado desejado]. E isso é possível."
```

---

## Top Copy Formulas Universais

### Fórmula PAS (Problem → Agitation → Solution)

```
[PROBLEMA]: Você está cansado de [problema específico]?
[AGITAÇÃO]: Enquanto isso, você continua [consequência negativa 1],
             [consequência negativa 2], e [consequência emocional].
[SOLUÇÃO]: Agora existe uma forma diferente. [PRODUTO] é [definição + resultado].
```

### Fórmula AIDA (Attention → Interest → Desire → Action)

```
[ATENÇÃO]: [Afirmação ousada ou pergunta provocativa]
[INTERESSE]: [Por que isso importa para você — contexto e problema]
[DESEJO]: [A vida com a solução — benefícios específicos e concretos]
[AÇÃO]: [CTA claro com urgência ou benefício imediato]
```

### Fórmula 4 Us (Urgent, Unique, Useful, Ultra-Specific)

```
Urgent: "Nos próximos 7 dias, você pode..."
Unique: "O único método que combina X + Y + Z"
Useful: "Aprenda a [habilidade específica e valiosa]"
Ultra-specific: "Como gerei R$47.832 em 90 dias com [método]"
```

### Fórmula BAB (Before → After → Bridge)

```
[BEFORE]: Hoje, você [situação atual negativa e reconhecível]
[AFTER]: Imagine poder [situação futura desejada, específica]
[BRIDGE]: [PRODUTO/SERVIÇO] é o caminho entre onde você está e onde quer estar.
```

---

## Referências e Fontes

- **Benchmarks de conversão:** WordStream (2024), HubSpot State of Marketing (2024), Unbounce Conversion Benchmark Report (2024)
- **E-commerce:** Baymard Institute (abandono de carrinho), Statista (taxas por categoria)
- **SaaS:** OpenView SaaS Benchmarks (2024), ChartMogul SaaS Metrics Report
- **Infoprodutos:** dados internos de lançamentos brasileiros (2022-2024), Hotmart Trends
- **Saúde:** CFM/CFO resoluções de publicidade médica (2024), CONAR regulamentações
- **Copy formulas:** Breakthrough Advertising (Eugene Schwartz), The Copywriter's Handbook (Robert Bly), Cashvertising (Drew Eric Whitman)

---

*Versão: 1.0.0 — Convert Engine Squad*
*Atualizar benchmarks a cada 6 meses com dados mais recentes.*
