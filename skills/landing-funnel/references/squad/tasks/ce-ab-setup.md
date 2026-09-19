---
task: setupABTest()
agent: ce-ab-architect
description: "Configurar teste em plataforma (Google Optimize/VWO/Optimizely): split, duração estimada, MDE (minimum detectable effect)"
elicit: true
responsavel: "Split"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: abVariants
    tipo: file
    obrigatorio: true
    descricao: "Variantes A e B definidas"

Saida:
  - nome: abTestConfig
    tipo: file
    obrigatorio: true
    descricao: "Teste configurado na plataforma com split 50/50, duração estimada e MDE definido"

Checklist:
  pre-conditions:
    - "[ ] Variantes definidas"
  post-conditions:
    - "[ ] Teste criado na plataforma"
    - "[ ] Split 50/50 configurado"
    - "[ ] Meta de conversão definida"
---

# Task: setupABTest()

## Objetivo
Configurar o teste A/B na plataforma escolhida com configurações estatisticamente rigorosas: split correto entre variantes, duração mínima calculada, MDE definido e critérios de parada documentados. Um teste mal configurado gera conclusões falsas — pior do que não testar.

## Inputs Necessários
- `ab-variants-spec.md` (especificações de variantes A e B)
- `ab-hypotheses.md` (métricas e MDE por hipótese)
- `traffic-data-analysis.md` (volume de visitantes/semana para cálculo de duração)
- `ga4-config.md` (conversões configuradas para uso como goal)
- Plataforma de A/B testing escolhida e conta configurada

## Processo
1. **Elicitação e escolha da plataforma:**

   | Plataforma | Custo | Melhor para | Integração |
   |-----------|-------|------------|-----------|
   | Google Optimize | Descontinuado (alternativas abaixo) | — | — |
   | VWO | $314/mês+ | Volume médio, recursos avançados | GA4, Hotjar |
   | Optimizely | Custom ($) | Enterprise, full-stack | Qualquer |
   | AB Tasty | $$/mês | Mid-market | GA4 |
   | **Feature Flags (GrowthBook)** | Gratuito/Open source | Devs técnicos | GA4 |
   | **Vercel Edge Config + Split** | Gratuito tier | Next.js nativo | GA4 |

   **Recomendação para LP:** GrowthBook (open source) integrado com GA4 para análise. Alternativa simples: implementar feature flags nativamente via Next.js + variáveis de ambiente + split via middleware.

2. **Implementação de A/B testing nativo no Next.js** (abordagem recomendada para custo zero):

   ```typescript
   // src/middleware.ts — Split de tráfego via Vercel Edge
   import { NextResponse } from 'next/server'
   import type { NextRequest } from 'next/server'

   export function middleware(request: NextRequest) {
     const url = request.nextUrl.clone()

     // Verificar se usuário já tem variante atribuída
     const variant = request.cookies.get('ab_variant_001')?.value

     if (!variant) {
       // Atribuir variante aleatoriamente (50/50 split)
       const newVariant = Math.random() < 0.5 ? 'A' : 'B'
       const response = NextResponse.next()
       // Cookie por 90 dias (persistir variante para consistência)
       response.cookies.set('ab_variant_001', newVariant, {
         maxAge: 60 * 60 * 24 * 90,
         httpOnly: true,
         sameSite: 'strict',
       })
       // Passar variante via header para o server component
       response.headers.set('x-ab-variant', newVariant)
       return response
     }

     return NextResponse.next()
   }
   ```

   ```tsx
   // src/components/organisms/HeroSection.tsx
   import { cookies, headers } from 'next/headers'

   export function HeroSection() {
     const variant = headers().get('x-ab-variant') ||
                     cookies().get('ab_variant_001')?.value || 'A'

     const headline = variant === 'B'
       ? 'Pare de perder clientes por falta de follow-up'
       : 'Aumente seus resultados com [produto]'

     // Registrar variante no dataLayer para analytics
     return (
       <>
         <script dangerouslySetInnerHTML={{
           __html: `window.dataLayer?.push({event:'ab_assigned', ab_test:'001', ab_variant:'${variant}'})`
         }} />
         <section>
           <h1>{headline}</h1>
           {/* resto da seção */}
         </section>
       </>
     )
   }
   ```

3. **Configuração do goal no GA4** — Para rastrear qual variante converte mais:

   **Dimensão customizada no GA4:**
   - Criar dimensão: `ab_variant` (dimensão de evento)
   - Registrar em Admin → Custom Definitions

   **Relatório de A/B no GA4:**
   - Explorar → Free Form
   - Dimensões: `ab_variant` + `event_name`
   - Métricas: `conversions`, `sessions`, `taxa de conversão`
   - Filtro: event = `ab_assigned`

4. **Cálculo de duração do teste** — Fórmula estatística:

   ```
   Duração (dias) = (N_por_variante × 2) / (visitantes_por_dia)

   N_por_variante = calculado com:
   - α = 0.05 (nível de significância, 95% confiança)
   - β = 0.20 (poder estatístico de 80%)
   - Taxa de conversão atual (baseline)
   - MDE (minimum detectable effect) — diferença mínima que importa para o negócio
   ```

   **Calculadora integrada:**
   | Taxa atual | MDE | N por variante | Visitantes/dia | Duração estimada |
   |-----------|-----|---------------|---------------|-----------------|
   | 2% | 20% relativo (2% → 2.4%) | 4.948 | 100 | 99 dias |
   | 2% | 20% relativo (2% → 2.4%) | 4.948 | 500 | 20 dias |
   | 5% | 20% relativo (5% → 6%) | 1.824 | 200 | 18 dias |
   | 10% | 15% relativo (10% → 11.5%) | 2.027 | 300 | 14 dias |

   **Regras de duração:**
   - Mínimo: 2 semanas (para capturar sazonalidade semanal)
   - Máximo: 6 semanas (além disso, fatores externos contaminam)
   - Nunca parar antes de 1 semana completa

5. **Configuração de critérios de parada:**
   - **Parada normal:** Duração calculada atingida + p-value < 0.05
   - **Parada antecipada (winner):** NÃO parar cedo mesmo com p < 0.05 — risco de falso positivo
   - **Parada antecipada (loser):** Se variante B for claramente inferior (p < 0.05, direção oposta) após mínima 1 semana, pode-se encerrar
   - **Parada por problema técnico:** Bug na variante B afetando UX → parar imediatamente

6. **Documentação do teste** — Criar ficha do teste:
   ```yaml
   Teste: AB-001
   Hipótese: [ID da hipótese]
   Data de início: [data]
   Data de término prevista: [data]
   Plataforma: [plataforma]
   Split: 50/50
   Variante A: [descrição]
   Variante B: [descrição]
   Métrica primária: taxa de conversão de lead
   MDE: 20% relativo
   Tamanho de amostra por variante: [N]
   Visitantes/dia atual: [número]
   Duração estimada: [X] dias
   Status: Em execução
   ```

## Veto Conditions
- Teste com duração < 7 dias → mínimo absoluto de 1 semana inteira
- Split diferente de 50/50 sem justificativa (ex: 90/10 para testar variante "perigosa") → documentar e justificar
- Teste parado cedo por "parecer que B está ganhando" → aguardar duração calculada
- Múltiplos testes no mesmo elemento simultaneamente → serializar

## Output Esperado
- Feature flags ou plataforma de A/B configurada
- Variantes implementadas no código com cookie de persistência
- Dimensão `ab_variant` no GA4 funcionando
- Relatório de A/B no GA4 configurado
- Ficha de cada teste documentada com todos os parâmetros
- Documento `ab-test-setup.md` com configurações completas

## Completion Criteria
- [ ] Mecanismo de split implementado (cookie de persistência de 90 dias)
- [ ] Variante B implementada no código (só muda o elemento testado)
- [ ] Dimensão `ab_variant` registrando no GA4
- [ ] Duração calculada com fórmula estatística (α=0.05, β=0.20)
- [ ] MDE definido e justificado para o negócio
- [ ] Critérios de parada documentados
- [ ] Ficha do teste preenchida para cada teste ativo
- [ ] Relatório de A/B configurado no GA4
- [ ] Teste verificado: ambas as variantes entregando corretamente
