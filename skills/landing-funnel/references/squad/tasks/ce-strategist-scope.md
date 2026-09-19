---
task: defineScope()
agent: ce-strategist
description: "Definir escopo final: seções da LP, flags condicionais (backend/analytics/ab/social_proof/email_nurture/whatsapp/payments/crm)"
elicit: false
responsavel: "Vortex"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: elicitedRequirements
    tipo: file
    obrigatorio: true
    descricao: "Respostas do questionário de elicitação"

Saida:
  - nome: projectScope
    tipo: file
    obrigatorio: true
    descricao: "Escopo final: seções da LP e flags condicionais ativadas"

Checklist:
  pre-conditions:
    - "[ ] Questionário de elicitação completo"
  post-conditions:
    - "[ ] Flags condicionais definidas"
    - "[ ] Seções da LP listadas"
    - "[ ] Escopo aprovado pelo usuário"
---

# Task: defineScope()

## Objetivo
Traduzir todo o conhecimento adquirido nas tasks anteriores em um escopo executável e preciso para o squad. Definir quais seções compõem a landing page, quais agentes serão ativados e quais flags condicionais determinam o escopo de cada agente especialista.

## Inputs Necessários
- `product-brief.md` (output de `discoverProduct()`)
- `funnel-map.md` (output de `mapFunnelStages()`)
- `requirements.md` (output de `elicitRequirements()`)
- Intelligence Brief do ce-researcher (quando disponível)

## Processo
1. **Análise de flags condicionais** — Avaliar cada flag baseado nas respostas do requirements e funnel map:

   | Flag | Ativa quando |
   |------|-------------|
   | `backend` | LP precisa capturar leads no próprio servidor, tem checkout, ou requer server-side events |
   | `analytics` | Cliente quer rastreamento avançado (GA4 + GTM + pixels) — RECOMENDADO por padrão |
   | `ab_testing` | Orçamento de tráfego permite teste (mínimo 1000 visitantes/semana) e há hipótese clara |
   | `social_proof` | Há provas sociais a estruturar OU necessidade identificada de construí-las |
   | `email_nurture` | Funil requer sequência pós-lead com duração > 1 email |
   | `whatsapp` | Cliente usa WhatsApp para vendas ou suporte; tráfego móvel > 60% |
   | `payments` | LP tem checkout direto (venda direta, não apenas captura de lead) |
   | `crm` | Cliente já tem ou quer CRM integrado ao pipeline de vendas |

2. **Definição das seções da LP** — Selecionar e ordenar seções baseado no objetivo da LP e nível de consciência do tráfego:

   **Seções obrigatórias (toda LP):**
   - Hero (headline + subheadline + CTA primário + hero image)
   - Benefícios/Diferenciais
   - CTA intermediário

   **Seções condicionais:**
   - VSL / Vídeo hero (se produto complexo ou tráfego frio)
   - Como funciona / Processo (se produto/serviço tem jornada não óbvia)
   - Para quem é (se segmentação é crítica)
   - Prova social / Depoimentos (se `social_proof` ativo)
   - Cases / Resultados (se provas robustas disponíveis)
   - FAQ / Objeções (se ciclo de decisão longo)
   - Pricing / Oferta (se `payments` ou venda direta)
   - Garantia (se risco percebido é alto)
   - Urgência / Escassez (se aplicável e verdadeiro)
   - Footer com legal (LGPD, termos, política de privacidade)

3. **Sequenciamento estratégico de seções** — Ordenar seções segundo a jornada psicológica do visitante: Atenção → Interesse → Desejo → Convicção → Ação. Justificar cada posição.

4. **Definição de agentes ativos** — Com base nas flags, listar quais agentes do squad serão ativados e suas dependências:
   - ce-strategist (sempre)
   - ce-researcher (sempre)
   - ce-copywriter (sempre)
   - ce-design-architect (sempre)
   - ce-image-creator (sempre)
   - ce-frontend-dev (sempre)
   - ce-backend-dev (se `backend`)
   - ce-integrator (se qualquer integração ativa)
   - ce-analytics-architect (se `analytics`)
   - ce-ab-architect (se `ab_testing`)
   - ce-social-proof (se `social_proof`)
   - ce-email-strategist (se `email_nurture`)
   - ce-reviewer (sempre, fase final)

5. **Criação do Scope Document** — Consolidar em `scope.md` com escopo fechado, justificado e rastreável.

## Veto Conditions
- Flag `ab_testing` ativa sem volume de tráfego suficiente (< 1000 visitors/semana) → desativar e registrar como fase futura
- Flag `payments` ativa sem definição de gateway → bloquear até gateway ser escolhido
- Mais de 12 seções na LP → questionar necessidade de cada seção; LP muito longa aumenta friction
- Seções sem copy ou dados para sustentá-las → marcar como "condicional — depende de conteúdo do cliente"

## Output Esperado
Arquivo `scope.md` contendo:
- Lista de flags ativas com justificativa
- Lista de seções da LP ordenadas com objetivo de cada uma
- Lista de agentes ativos e suas dependências
- Estimativa de complexidade (seções × integrações)
- Riscos e condicionais identificados
- Aprovação do escopo necessária antes do início da produção

## Completion Criteria
- [ ] Todas as flags avaliadas (ativas ou inativas com justificativa)
- [ ] Seções da LP definidas e ordenadas (mínimo 5, máximo 12 recomendado)
- [ ] Objetivo de cada seção documentado
- [ ] Agentes ativos listados com dependências mapeadas
- [ ] Escopo aprovado (pelo cliente ou representante do produto)
- [ ] Arquivo `scope.md` criado e disponível como referência central do projeto
- [ ] Handoff preparado para ce-researcher iniciar pesquisa
