---
task: analyzeResults()
agent: ce-ab-architect
description: "Analisar resultados com rigor estatístico: p-value, confidence interval, business impact. Declarar vencedor APENAS com p < 0.05"
elicit: false
responsavel: "Split"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: abTestData
    tipo: file
    obrigatorio: true
    descricao: "Dados do teste com mínimo 100 conversões por variante"

Saida:
  - nome: abAnalysisReport
    tipo: file
    obrigatorio: true
    descricao: "Análise estatística: p-value, confidence interval e business impact — vencedor declarado somente com p < 0.05"

Checklist:
  pre-conditions:
    - "[ ] Mínimo 100 conversões por variante"
    - "[ ] Duração mínima do teste atingida"
  post-conditions:
    - "[ ] p-value calculado"
    - "[ ] Vencedor declarado somente se p < 0.05"
    - "[ ] Próximo teste recomendado"
---

# Task: analyzeResults()

## Objetivo
Analisar os resultados do teste A/B com rigor estatístico completo, produzir um relatório de análise que vai além do "B ganhou ou perdeu" para explicar o que o resultado significa para o negócio e quais ações devem ser tomadas. Declarar vencedor APENAS quando os critérios estatísticos são satisfeitos — resultado inconclusivo também é um resultado válido.

## Inputs Necessários
- `ab-test-setup.md` (parâmetros do teste: MDE, duração, métricas)
- Dados de resultado do GA4 (visitantes, conversões, taxa de conversão por variante)
- Dados de resultado de métricas secundárias (CTR, scroll depth, bounce rate)
- Duração final do teste e número de sessões por variante

## Processo
1. **Coleta de dados do teste** — Extrair do GA4:
   - Variante A: sessões, conversões, taxa de conversão
   - Variante B: sessões, conversões, taxa de conversão
   - Período exato do teste (início e fim)
   - Verificar que o split foi mantido (± 5% de 50/50 é aceitável)

   **Verificar contaminação do teste:**
   - Houve evento externo durante o teste? (mudança de campanha, notícia relevante, sazonalidade)
   - Houve bug técnico em alguma variante?
   - O tráfego foi consistente ao longo do período?
   Se sim a qualquer um: registrar como fator confundidor na análise.

2. **Cálculo de significância estatística** — Nunca declarar vencedor sem este cálculo:

   **Método Chi-Quadrado para taxa de conversão:**
   ```python
   # Exemplo de cálculo
   from scipy import stats
   import numpy as np

   visitors_A = 1250
   conversions_A = 38
   visitors_B = 1248
   conversions_B = 52

   conversion_rate_A = conversions_A / visitors_A  # 3.04%
   conversion_rate_B = conversions_B / visitors_B  # 4.17%

   # Teste Chi-Quadrado
   observed = np.array([[conversions_A, visitors_A - conversions_A],
                        [conversions_B, visitors_B - conversions_B]])
   chi2, p_value, dof, expected = stats.chi2_contingency(observed)

   # Uplift relativo
   uplift = (conversion_rate_B - conversion_rate_A) / conversion_rate_A  # +37%

   # Intervalo de confiança (95%) para a diferença
   se = np.sqrt(conversion_rate_A*(1-conversion_rate_A)/visitors_A +
                conversion_rate_B*(1-conversion_rate_B)/visitors_B)
   ci_low = (conversion_rate_B - conversion_rate_A) - 1.96 * se
   ci_high = (conversion_rate_B - conversion_rate_A) + 1.96 * se
   ```

   **Interpretação dos resultados:**
   - p < 0.05 → Resultado estatisticamente significante → pode declarar vencedor
   - 0.05 ≤ p < 0.10 → Tendência, mas inconclusivo → estender o teste ou novo teste
   - p ≥ 0.10 → Sem evidência de diferença real → resultado nulo
   - Intervalo de confiança cruzando zero → inconclusivo mesmo com p < 0.05

3. **Análise de impacto de negócio** — Traduzir p-value em resultado de negócio:

   **Projeção anual:**
   ```
   Leads atuais/mês: [número] × taxa A (3.04%) = [X] leads/mês
   Leads com variante B: [número] × taxa B (4.17%) = [Y] leads/mês
   Aumento de leads/mês: [Y - X] leads
   Valor médio por lead convertido: R$ [LTV × taxa de fechamento]
   Impacto mensal estimado: R$ [diferença × valor]
   Impacto anual estimado: R$ [impacto mensal × 12]
   ```

4. **Análise de métricas secundárias** — Verificar se a variante B melhorou apenas a métrica primária ou também as secundárias:
   - CTR de outros CTAs na página: aumentou, diminuiu ou manteve?
   - Scroll depth: usuários da variante B engajam mais ou menos?
   - Bounce rate: variante B tem menor rejeição?
   - Tempo na página: usuários da variante B ficam mais tempo?

   Se a variante B melhora a primária mas piora as secundárias: resultado misto — investigar.

5. **Declaração formal do resultado** — Baseada nos critérios:

   **Template de declaração:**
   ```
   RESULTADO DO TESTE AB-001: [VENCEDOR / INCONCLUSIVO / SEM DIFERENÇA]

   Variante A (controle): [X]% de conversão (n=[N])
   Variante B (challenger): [Y]% de conversão (n=[N])
   Uplift: [+/-Z%] (intervalo de confiança 95%: [low%, high%])
   p-value: [valor]
   Significância: [SIM / NÃO — p {'<' if sig else '>='} 0.05]
   Duração: [X] dias
   Total de sessões: [N]

   DECISÃO: [
     "Implementar variante B definitivamente" (se p<0.05 e B>A) |
     "Manter variante A" (se p<0.05 e A>B) |
     "Inconclusivo — estender ou redesenhar" (se p≥0.05) |
     "Resultado nulo — nenhum efeito detectável" (se sem diferença com amostra suficiente)
   ]

   Razão da decisão: [explicação em 2-3 frases]
   Próximo teste recomendado: [hipótese para o próximo ciclo]
   ```

6. **Documentação de aprendizados** — Além do resultado técnico:
   - O que este resultado nos diz sobre a psicologia do nosso público?
   - Qual insight de copy ou design este teste revelou?
   - Como este aprendizado pode ser aplicado em outros elementos da LP?
   - Que nova hipótese emerge deste resultado?

7. **Ação pós-resultado:**
   - Se vencedor identificado: implementar variante B como padrão, remover feature flag
   - Se inconclusivo: documentar e planejar próximo teste
   - Se resultado nulo: documentar (saber o que NÃO funciona também tem valor)
   - Iniciar próxima hipótese do backlog

## Veto Conditions
- Declarar vencedor com p > 0.05 → nunca — é o erro mais grave no A/B testing
- Parar o teste cedo "porque B está ganhando" antes da duração calculada → não fazer
- Ignorar fatores confundidores (mudança de campanha no meio do teste) → registrar e considerar na análise
- Implementar variante "vencedora" sem remover feature flag → criar dívida técnica

## Output Esperado
Arquivo `ab-results-[teste-id].md` contendo:
- Dados brutos do teste (sessões, conversões, taxas por variante)
- Cálculo de p-value e intervalo de confiança
- Análise de impacto de negócio (projeção anual)
- Análise de métricas secundárias
- Declaração formal do resultado com decisão justificada
- Aprendizados documentados
- Próxima hipótese recomendada

## Completion Criteria
- [ ] Dados coletados do GA4 para ambas as variantes
- [ ] Contaminação do teste verificada e documentada
- [ ] p-value calculado com método estatístico adequado
- [ ] Intervalo de confiança de 95% calculado
- [ ] Impacto de negócio projetado (anual)
- [ ] Métricas secundárias analisadas
- [ ] Declaração formal com VENCEDOR / INCONCLUSIVO / SEM DIFERENÇA
- [ ] Decisão implementada (feature flag removida se vencedor declarado)
- [ ] Aprendizados documentados
- [ ] Próxima hipótese identificada para continuidade do ciclo
