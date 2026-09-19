---
task: mapEmailSequence()
agent: ce-email-strategist
description: "Mapear sequência de nurture pós-conversão: quantos emails, intervalo, objetivo de cada um (welcome/educação/prova social/oferta/urgência)"
elicit: true
responsavel: "Thread"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: audienceProfile
    tipo: file
    obrigatorio: true
    descricao: "Perfil da audiência com jornada de compra mapeada"
  - nome: productBrief
    tipo: file
    obrigatorio: true
    descricao: "Briefing do produto com oferta e preço"

Saida:
  - nome: emailSequenceMap
    tipo: file
    obrigatorio: true
    descricao: "Mapa da sequência: quantos emails, intervalos, objetivo de cada um e segmentação comportamental"

Checklist:
  pre-conditions:
    - "[ ] Audiência perfilada"
    - "[ ] Oferta definida"
  post-conditions:
    - "[ ] Sequência mapeada (mínimo 5 emails)"
    - "[ ] Intervalos definidos"
    - "[ ] Segmentação comportamental planejada"
---

# Task: mapEmailSequence()

## Objetivo
Projetar a arquitetura completa da sequência de emails de nurture que o lead recebe após conversão. Uma sequência bem mapeada conduz o lead por uma jornada deliberada de awareness → consideração → decisão, aumentando a taxa de conversão lead → cliente em até 50% comparado com sem nurture.

## Inputs Necessários
- `funnel-map.md` (papel do email no funil, tempo médio de decisão)
- `audience-profile.md` (nível de consciência, objeções por etapa)
- `product-brief.md` (produto, preço, garantia, próximos passos após conversão)
- `intelligence-brief.md` (dores, diferenciais, ângulos de copy)
- `requirements.md` (objetivo da LP, Q11 sobre meta de conversão)
- Plataforma de email definida (`ce-integrator-email.md`)

## Processo
1. **Elicitação de parâmetros da sequência** — Coletar com o cliente:
   - Qual é o próximo passo após a captura de lead? (call com SDR, acesso a conteúdo, trial, compra direta)
   - Quanto tempo o lead leva em média para decidir comprar?
   - Há segmentação por comportamento disponível? (Se lead clicou em oferta, sequência diferente)
   - O cliente tem restrição de frequência? (Alguns nichos rejeitam mais de 1 email/semana)
   - Qual é o tom desejado: pessoal (como se fosse do fundador) ou corporativo (da empresa)?

2. **Definição da extensão da sequência** — Baseada no ciclo de decisão:

   | Ciclo de decisão | Sequência recomendada | Total de emails |
   |----------------|----------------------|----------------|
   | Curto (< 72h) | Boas-vindas + Oferta rápida + Urgência | 3-4 emails |
   | Médio (3-14 dias) | Welcome + Educação × 2 + Prova social + Oferta + Urgência | 6-7 emails |
   | Longo (> 14 dias) | Welcome + Educação × 3 + Prova social × 2 + Objeções + Oferta + Urgência + Reativação | 10-12 emails |

3. **Mapeamento de cada email** — Para cada email na sequência, definir:

   **Email 1 — Welcome / Confirmação:**
   - Objetivo: Confirmar a ação, criar conexão inicial, estabelecer expectativas
   - Timing: Imediato (< 5 minutos após conversão)
   - Tom: Caloroso, pessoal, grato
   - Conteúdo: O que acontece agora, o que o lead pode esperar, próximo passo claro
   - CTA: Um único próximo passo (agendar call, acessar recurso, etc.)

   **Email 2 — Educação / Valor (D+1):**
   - Objetivo: Entregar valor antes de pedir qualquer coisa
   - Timing: 24h após welcome
   - Conteúdo: Insight útil relacionado ao problema do lead, dica prática, conteúdo exclusivo
   - CTA: Consumir o conteúdo (sem CTA de venda)

   **Email 3 — Prova Social / Inspiração (D+3):**
   - Objetivo: Construir crença de que o resultado é possível PARA ELES
   - Timing: 48h após email 2
   - Conteúdo: Caso de sucesso de cliente com perfil similar ao lead
   - CTA: Agendar call ou ver mais casos

   **Email 4 — Educação / Objeção (D+5):**
   - Objetivo: Neutralizar a maior objeção proativamente
   - Conteúdo: "A pergunta mais comum que recebo sobre [produto] é X. A resposta é..."
   - CTA: Responder email com dúvidas (aumenta engajamento)

   **Email 5 — Oferta / Apresentação (D+7):**
   - Objetivo: Apresentar a oferta de forma natural, não abrupta
   - Conteúdo: Transição suave para a oferta, stack de valor completo, garantia
   - CTA: Aproveitar a oferta (link direto para LP ou checkout)

   **Email 6 — Urgência / Escassez (D+9):**
   - Objetivo: Criar razão para agir agora (se real)
   - Conteúdo: Countdown, prazo, vagas limitadas, bônus expirando
   - CTA: Agir antes do prazo
   - IMPORTANTE: Urgência deve ser legítima, não fabricada

   **Email 7 — Última chance (D+10 ou D+11):**
   - Objetivo: Reativação de leads que ainda não converteram
   - Tom: Direto, sem enrolação
   - Conteúdo: "Última chance para [oferta/bônus]. Após isso, [consequência real]."
   - CTA: Agir agora

4. **Mapa de segmentação comportamental** — Se a plataforma suporta:
   - Lead que abriu todos os emails mas não converteu → sequência de objeção específica
   - Lead que clicou na oferta mas não comprou → sequência de carrinho abandonado
   - Lead que converteu em cliente → remover da sequência + iniciar onboarding
   - Lead que não abriu nenhum email após 7 dias → sequência de reativação

5. **Definição de critérios de saída da sequência:**
   - Saiu da sequência se: converteu em cliente
   - Saiu da sequência se: fez unsubscribe
   - Saiu da sequência se: marcou como spam (automaticamente)
   - Opcionalmente: após X dias sem engajamento → mover para lista fria

6. **Documentação do mapa** — Criar fluxograma textual:
   ```
   Lead converte
   │
   ├─ D+0: [Welcome] → Abriu? → SIM → continua | NÃO → re-envio com subject diferente
   ├─ D+1: [Educação 1]
   ├─ D+3: [Prova Social]
   ├─ D+5: [Objeção]
   ├─ D+7: [Oferta]
   │         └─ Clicou? → SIM → [tag: interesse-alto] → sequência acelerada
   ├─ D+9: [Urgência]
   └─ D+11: [Última Chance]
             └─ Converteu? → SIM → sai da sequência
                           → NÃO → lista fria (nurture mensal)
   ```

## Veto Conditions
- Urgência falsa (prazo inventado que se repete infinitamente) → criar urgência real ou remover
- Mais de 1 email por dia (exceto em sequências de eventos ao vivo) → reduzir frequência
- Sequência sem segmentação de "converteu → sair" → implementar saída automática
- Email 1 (welcome) com mais de 5 minutos de delay → corrigir configuração de automação

## Output Esperado
Arquivo `email-sequence-map.md` contendo:
- Parâmetros definidos (extensão, frequência, tom, plataforma)
- Mapa completo de cada email: timing, objetivo, conteúdo resumido, CTA
- Fluxograma com segmentações comportamentais
- Critérios de saída da sequência
- Especificações para escrita da série (`writeEmailSeries()`)

## Completion Criteria
- [ ] Ciclo de decisão definido (curto/médio/longo)
- [ ] Extensão da sequência definida com justificativa
- [ ] Cada email mapeado com: timing, objetivo, conteúdo resumido, CTA
- [ ] Segmentações comportamentais definidas
- [ ] Critérios de saída da sequência definidos
- [ ] Fluxograma da sequência criado
- [ ] Arquivo `email-sequence-map.md` criado para guiar `writeEmailSeries()`
