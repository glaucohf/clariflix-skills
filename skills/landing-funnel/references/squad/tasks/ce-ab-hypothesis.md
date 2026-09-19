---
task: formulateHypothesis()
agent: ce-ab-architect
description: "Formular hipótese baseada em dados de heatmap/analytics: 'Acreditamos que [mudança] para [audiência] irá [resultado] porque [evidência]'"
elicit: false
responsavel: "Split"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: analyticsData
    tipo: file
    obrigatorio: true
    descricao: "Dados de analytics e heatmap com mínimo 500 sessões"

Saida:
  - nome: abHypothesis
    tipo: file
    obrigatorio: true
    descricao: "Hipótese estruturada: Acreditamos que [mudança] para [audiência] irá [resultado] porque [evidência]"

Checklist:
  pre-conditions:
    - "[ ] Mínimo 500 sessões registradas"
    - "[ ] Heatmaps com dados suficientes"
  post-conditions:
    - "[ ] Hipótese no formato correto"
    - "[ ] Evidência de dados citada"
    - "[ ] Elemento a testar definido"
---

# Task: formulateHypothesis()

## Objetivo
Formular hipóteses de A/B testing rigorosas, baseadas em dados reais de comportamento e não em preferências pessoais ou suposições. Uma hipótese bem formulada é a diferença entre um teste que gera insight acionável e um teste que apenas desperdiça tráfego.

## Inputs Necessários
- `heatmap-config.md` + dados de heatmap disponíveis (se LP já tem tráfego)
- `ga4-config.md` + dados do funil de conversão GA4
- `intelligence-brief.md` (dores, objeções, comportamento do público)
- `ab-copy-variants.md` (variantes de copy já identificadas pelo ce-copywriter)
- `cro-design-audit.md` (friction points identificados pelo ce-design-architect)
- `traffic-data-analysis.md` (volume de tráfego para calcular duração de teste)

## Processo
1. **Coleta e análise de dados de comportamento** — Antes de formular qualquer hipótese:

   **Dados quantitativos (GA4):**
   - Taxa de conversão atual por dispositivo (mobile vs desktop)
   - Funil: onde ocorre maior abandono?
   - Tempo médio na página antes de converter
   - Scroll depth: qual porcentagem de usuários chega ao CTA principal?
   - CTR de cada CTA (cta_clicked / page_views)

   **Dados qualitativos (Heatmap/Recordings):**
   - Existe click rage em algum elemento não-clicável?
   - O CTA principal está na "zona quente" do heatmap?
   - Usuários que não convertem: onde param de scroll?
   - Formulário: usuários iniciam mas abandonam em qual campo?
   - Mobile: elementos se sobrepõem? CTA está acessível?

2. **Framework de priorização de hipóteses** — Usar o modelo ICE (Impact, Confidence, Ease):

   | Dimensão | Definição | Escala |
   |---------|-----------|-------|
   | **Impact** | Se funcionar, quanto moverá a taxa de conversão? | 1-10 |
   | **Confidence** | Quão forte é a evidência que suporta esta hipótese? | 1-10 |
   | **Ease** | Quão fácil é implementar este teste? | 1-10 |

   ICE Score = (Impact + Confidence + Ease) / 3

   Priorizar hipóteses com ICE ≥ 7.

3. **Formulação de hipóteses** — Para cada oportunidade identificada, escrever no formato padrão:

   **Template:**
   > "Acreditamos que **[mudança específica]** para **[audiência específica ou segmento]** irá **[direção + métrica + magnitude esperada]** porque **[evidência específica: dado de heatmap, analytics, pesquisa de audiência ou princípio comprovado]**."

   **Exemplos de hipóteses bem formuladas:**

   H1 (Headline):
   > "Acreditamos que substituir a headline genérica 'Aumente seus resultados' por uma headline específica de dor 'Pare de perder clientes por falta de follow-up' para empreendedores com times de vendas pequenos irá aumentar a taxa de conversão de leads em 15-25% porque dados de heatmap mostram que 68% dos usuários param de scroll logo após a headline, sugerindo que ela não está capturando atenção suficientemente."

   H2 (CTA):
   > "Acreditamos que mudar o texto do CTA de 'Enviar' para 'Quero minha análise gratuita' para todos os visitantes irá aumentar o CTR do formulário em 20-30% porque pesquisas de copy (Unbounce, 2023) mostram que CTAs em primeira pessoa convertem 90% melhor, e nossos dados de heatmap mostram click rate baixo no botão atual."

   H3 (Posição do formulário):
   > "Acreditamos que mover o formulário de captura de lead do final da página para logo abaixo do hero irá aumentar a taxa de conversão em mobile em 10-20% porque dados de scroll mostram que apenas 34% dos usuários mobile chegam ao formulário atual, e o volume de mobile representa 73% do tráfego total."

4. **Priorização das hipóteses** — Rankear por ICE Score:
   - Calcular ICE para cada hipótese
   - Listar em ordem decrescente
   - Selecionar TOP 3 para desenvolvimento em `designVariants()`
   - Documentar as demais como backlog

5. **Definição de métricas de sucesso por hipótese:**
   - Métrica primária: qual KPI determina vencedor/perdedor?
   - Métricas secundárias: quais métricas monitorar sem usar como critério de decisão?
   - Direção esperada (aumento/redução) e magnitude esperada
   - MDE (Minimum Detectable Effect) — mínima diferença que o teste consegue detectar
   - Duração estimada do teste (calculada baseada no volume de tráfego)

6. **Verificação de independência** — Garantir que hipóteses não se contradizem:
   - Testes simultâneos não devem interagir entre si
   - Se interagem, serializar (executar um após o outro)
   - Registrar dependências no documento de hipóteses

## Veto Conditions
- Hipótese sem evidência (apenas intuição) → rejeitar e buscar dado que suporte
- Hipótese que testa múltiplas mudanças simultaneamente → dividir em hipóteses separadas
- Hipótese com MDE < 5% para volume baixo de tráfego → impossível detectar estatisticamente — revisar
- Hipóteses contraditórias rodando simultaneamente → serializar

## Output Esperado
Arquivo `ab-hypotheses.md` contendo:
- Análise de dados que originou cada hipótese (quantitativo + qualitativo)
- TOP 5 hipóteses no formato template padrão
- ICE Score para cada hipótese com justificativa
- Ranking de prioridade
- Métricas de sucesso e MDE por hipótese
- Backlog de hipóteses (posição 6+)
- Mapa de independência entre testes

## Completion Criteria
- [ ] Dados de GA4 analisados (funil, scroll depth, CTR de CTAs)
- [ ] Dados de heatmap analisados (se disponíveis)
- [ ] Mínimo 5 hipóteses formuladas no template padrão
- [ ] Cada hipótese com evidência documentada (não apenas intuição)
- [ ] ICE Score calculado para todas as hipóteses
- [ ] TOP 3 hipóteses selecionadas para execução imediata
- [ ] Métricas de sucesso definidas para cada hipótese
- [ ] MDE calculado baseado no volume de tráfego real
- [ ] Independência entre testes verificada
- [ ] Arquivo `ab-hypotheses.md` criado e entregue ao squad
