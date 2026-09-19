---
task: produceFinalReport()
agent: ce-reviewer
description: "Produzir relatório final com scores por dimensão, average score, itens bloqueantes vs melhorias opcionais, sinal de GO/NO-GO para lançamento"
elicit: false
responsavel: "Audit"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: allReviewScores
    tipo: file
    obrigatorio: true
    descricao: "Todos os scores por dimensão"

Saida:
  - nome: finalReport
    tipo: file
    obrigatorio: true
    descricao: "Relatório final com score médio ponderado, itens bloqueantes, melhorias opcionais e sinal GO/NO-GO"

Checklist:
  pre-conditions:
    - "[ ] Todos os scores disponíveis"
  post-conditions:
    - "[ ] Score médio calculado"
    - "[ ] GO/NO-GO emitido"
    - "[ ] Itens bloqueantes listados com prioridade"
---

# Task: produceFinalReport()

## Objetivo
Consolidar todos os reviews parciais em um único Relatório Final de Lançamento que fornece uma visão completa da qualidade da LP em todas as dimensões, identifica claramente o que bloqueia o lançamento versus o que pode ser melhorado iterativamente, e emite o sinal oficial de GO ou NO-GO.

## Inputs Necessários
- `review-copy.md` (score de copy)
- `review-design.md` (score de design)
- `review-seo-a11y.md` (score de SEO e acessibilidade)
- `review-conversion.md` (score de conversão — inclui GO/NO-GO checklist)
- `review-backend.md` (score de segurança do backend — se aplicável)
- `scope.md` (flags ativas — para saber quais dimensões são aplicáveis)
- `intelligence-brief.md` (benchmarks de conversão do nicho — contexto)

## Processo
1. **Consolidação de scores** — Coletar scores de cada review:

   | Dimensão | Score (0-100) | Peso | Score Ponderado |
   |---------|--------------|------|----------------|
   | Copy | [score] | 25% | [score × 0.25] |
   | Design | [score] | 20% | [score × 0.20] |
   | SEO + Acessibilidade | [score] | 15% | [score × 0.15] |
   | Conversão | [score] | 30% | [score × 0.30] |
   | Segurança Backend | [score] | 10% | [score × 0.10] |
   | **TOTAL** | — | **100%** | **[soma]** |

   O peso de Conversão é maior (30%) porque é o indicador mais diretamente ligado ao objetivo da LP.
   Se backend não está ativo (flag `backend` desativada), redistribuir o peso 10% proporcionalmente.

2. **Classificação do score total:**

   | Score Total | Classificação | Recomendação |
   |------------|--------------|-------------|
   | 90-100 | Excelente | GO — lançar imediatamente |
   | 80-89 | Bom | GO — lançar e melhorar iterativamente |
   | 70-79 | Adequado | GO CONDICIONAL — resolver itens médios antes do lançamento |
   | 60-69 | Abaixo do padrão | NO-GO — resolver críticos antes de lançar |
   | < 60 | Reprovado | NO-GO — revisão significativa necessária |

3. **Mapeamento de todos os problemas encontrados** — Consolidar da lista de TODOS os reviews:

   **Bloqueantes (impedem lançamento):**
   Formato: `[DIMENSÃO] [Problema] → [Correção necessária]`
   Exemplo: `[CONVERSÃO] CTA não visível acima da dobra em mobile 375px → Repositionar CTA no componente HeroSection`

   **Significativos (impactam conversão, mas não bloqueiam):**
   Exemplo: `[COPY] Headline da seção de pricing genérica → Reescrever com benefício específico`

   **Melhorias opcionais (backlog pós-lançamento):**
   Exemplo: `[DESIGN] Animação de stagger poderia ter delay menor para parecer mais ágil`

4. **Priorização de correções** — Se há itens bloqueantes:
   - Listar em ordem de prioridade
   - Atribuir ao agente responsável (ce-frontend-dev, ce-copywriter, etc.)
   - Estimar esforço (horas) para cada correção
   - Definir data de re-review após correções

5. **Análise de risco de lançamento** — Avaliar riscos residuais mesmo com GO:
   - Há funcionalidades críticas não testadas em produção?
   - Há dependências externas (APIs de terceiros) sem plano de fallback?
   - Há volume de tráfego esperado que pode gerar gargalos?
   - Há risco legal não endereçado (promessas não sustentadas, LGPD)?

6. **Comparação com benchmarks do nicho** — Contextualizar o score:
   - A LP está acima ou abaixo dos padrões típicos do nicho?
   - Qual é a expectativa realista de taxa de conversão com este score?
   - Quais as 3 maiores oportunidades de melhoria para fase 2?

7. **Recomendações de otimização contínua** — Para pós-lançamento:
   - TOP 3 hipóteses para A/B testing prioritário
   - Métricas a acompanhar semanalmente
   - Triggers para próxima rodada de otimização (ex: "Se taxa de conversão < X%, revisar headline")

8. **Estrutura do relatório final:**

   ```markdown
   # Relatório Final de Lançamento — [Nome do Produto]
   Data: [DATA]
   Revisado por: ce-reviewer

   ## Executive Summary
   Score Total: [X]/100 — [Classificação]
   Sinal: 🟢 GO / 🟡 GO CONDICIONAL / 🔴 NO-GO
   Itens Bloqueantes: [N]
   Itens Significativos: [N]
   Melhorias Opcionais: [N]

   ## Scores por Dimensão
   [Tabela com scores e pesos]

   ## Bloqueantes para Lançamento
   [Lista de itens bloqueantes com agente responsável e esforço estimado]

   ## Itens Significativos (Pós-Lançamento Imediato)
   [Lista priorizada]

   ## Melhorias Opcionais (Backlog)
   [Lista]

   ## Análise de Risco
   [Riscos residuais e mitigações]

   ## Comparação com Benchmarks do Nicho
   [Contexto de mercado]

   ## Recomendações de Otimização Contínua
   [TOP 3 hipóteses + métricas para acompanhar]

   ## Próximos Passos
   [ ] Resolver bloqueantes [AGENTE RESPONSÁVEL]
   [ ] Re-review de itens críticos
   [ ] Lançamento em [DATA ESTIMADA]
   [ ] Primeira análise de resultados em [D+7]
   ```

## Veto Conditions
- Qualquer item BLOQUEANTE presente → GO/NO-GO = NO-GO (independente do score total)
- Score de Conversão < 70 → NO-GO automático (dimensão mais crítica)
- Score de Segurança Backend < 70 (se backend ativo) → NO-GO automático

## Output Esperado
- Arquivo `FINAL-LAUNCH-REPORT.md` — Relatório completo de lançamento
- `LAUNCH-CHECKLIST.md` — Checklist executável com todos os itens a resolver antes do lançamento
- Sinal oficial GO ou NO-GO documentado e justificado

## Completion Criteria
- [ ] Scores de todos os reviews parciais coletados
- [ ] Score ponderado total calculado
- [ ] Todos os problemas de TODOS os reviews consolidados e classificados (bloqueante/significativo/opcional)
- [ ] Priorização de correções com agente responsável e esforço estimado
- [ ] Análise de risco documentada
- [ ] Comparação com benchmarks do nicho realizada
- [ ] TOP 3 hipóteses de A/B para pós-lançamento identificadas
- [ ] Próximos passos definidos com responsáveis e datas
- [ ] Sinal GO ou NO-GO emitido com justificativa clara
- [ ] Arquivo `FINAL-LAUNCH-REPORT.md` criado e entregue ao cliente/squad
- [ ] Arquivo `LAUNCH-CHECKLIST.md` criado com itens executáveis
