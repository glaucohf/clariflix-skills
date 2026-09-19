---
task: designVariants()
agent: ce-ab-architect
description: "Desenhar variantes A e B para elementos testáveis: headline, CTA, hero image, oferta, layout de pricing"
elicit: false
responsavel: "Split"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: abHypothesis
    tipo: file
    obrigatorio: true
    descricao: "Hipótese do teste definida"

Saida:
  - nome: abVariants
    tipo: file
    obrigatorio: true
    descricao: "Variantes A e B definidas para headline, CTA, hero image, oferta ou layout de pricing"

Checklist:
  pre-conditions:
    - "[ ] Hipótese formulada"
  post-conditions:
    - "[ ] Controle (A) documentado"
    - "[ ] Variante (B) especificada"
    - "[ ] Diferença entre A e B clara e isolada"
---

# Task: designVariants()

## Objetivo
Traduzir as hipóteses aprovadas em especificações concretas de variantes A (controle) e B (challenger) para cada teste priorizado. As variantes devem isolar exatamente uma variável por vez, ter impacto visual suficiente para mover a métrica e ser tecnicamente implementáveis.

## Inputs Necessários
- `ab-hypotheses.md` (hipóteses priorizadas com ICE scores)
- `ab-copy-variants.md` (variantes de copy já escritas pelo ce-copywriter)
- `sections-design-spec.md` (design de referência — o controle)
- `component-library.md` (componentes disponíveis)
- `intelligence-brief.md` (ângulos de copy alternativos)

## Processo
1. **Para cada hipótese do TOP 3, especificar variante B** — A variante A é sempre o controle (versão atual).

   **Estrutura de especificação de variante:**
   ```yaml
   Teste ID: AB-001
   Hipótese: [número da hipótese em ab-hypotheses.md]
   Elemento testado: [componente específico]
   Métrica primária: [KPI]

   Variante A (Controle):
     Elemento: [descrição exata do estado atual]
     Screenshot/mockup: [referência]

   Variante B (Challenger):
     Elemento: [descrição exata da mudança]
     Screenshot/mockup: [referência]
     Diferença de implementação: [o que precisa mudar no código]
     Custo de implementação: [horas estimadas]

   Isolamento: [confirmação de que apenas 1 variável muda]
   Dependências: [outros elementos que podem ser afetados]
   ```

2. **Especificações por tipo de elemento:**

   **Variante de Headline:**
   ```yaml
   AB-001: Headline Principal
   Controle (A):
     Texto: "Aumente seus resultados com [produto]"
     Tag HTML: h1
     Fonte: 48px desktop, 32px mobile
     Cor: text-foreground
     Posição: Hero, acima do fold

   Challenger (B):
     Texto: "Pare de perder clientes por falta de follow-up"
     Tag HTML: h1
     Fonte: 48px desktop, 32px mobile
     Cor: text-foreground (IDÊNTICO — apenas texto muda)
     Posição: Hero, acima do fold (IDÊNTICA)
     Mudança: APENAS o texto — nada mais
   ```

   **Variante de CTA:**
   ```yaml
   AB-002: Botão CTA Hero
   Controle (A):
     Texto: "Enviar"
     Cor: primary (bg-primary)
     Tamanho: lg (h-12 px-6)
     Microcopy: nenhum

   Challenger (B):
     Texto: "Quero minha análise gratuita"
     Cor: primary (IDÊNTICA)
     Tamanho: lg (IDÊNTICO)
     Microcopy: "Sem cartão de crédito" (adição)
     Mudança: texto + microcopy — apenas 1 "unidade conceitual" de mudança
   ```

   **Variante de Hero Layout:**
   ```yaml
   AB-003: Layout do Hero (Mobile)
   Controle (A):
     Ordem mobile: Imagem hero → Headline → CTA
     CTA posição: Bottom of hero section

   Challenger (B):
     Ordem mobile: Headline → CTA → Imagem hero
     CTA posição: Acima da imagem (mais alto no scroll)
     Mudança: Reordenação de elementos mobile-only
     Desktop: INALTERADO (split por device)
   ```

   **Variante de Oferta/Pricing:**
   ```yaml
   AB-004: Apresentação do Preço
   Controle (A):
     Formato: "R$ 297,00"
     Contexto: nenhum
     Posição: Abaixo da lista de benefícios

   Challenger (B):
     Formato: "R$ 297,00" (idêntico)
     Contexto: "Menos que 3 consultorias avulsas (R$100 cada)"
     Garantia: Próxima ao preço (movida de seção separada)
     Mudança: Adição de ancoragem contextual + reposição da garantia
   ```

3. **Validação de isolamento** — Para cada variante B, verificar:
   - Existe exatamente 1 diferença conceitual entre A e B?
   - A diferença é visualmente perceptível sem ser overwhelming?
   - A mudança pode ser medida com a métrica primária definida?
   - Nenhum outro elemento muda consequentemente?

4. **Avaliação de impacto visual** — A variante deve ser diferente o suficiente para mover resultados:
   - Diferença muito pequena (ex: mudar cor de #1e40af para #1d3faf) → difícil de detectar → ampliar
   - Diferença muito grande (ex: redesign completo da seção) → impossível atribuir causalidade → reduzir escopo

5. **Especificações técnicas de implementação** — Para cada variante:
   - Componente a modificar
   - Props ou estados que mudam
   - Feature flag necessária
   - Estimativa de esforço de implementação (horas)

6. **Mock visual das variantes** — Criar descrição detalhada ou wireframe de texto:
   ```
   [A - CONTROLE]
   ┌─────────────────────────────────────────┐
   │         Aumente seus resultados          │
   │     com [produto] — sem complicação      │
   │                                          │
   │         [───── ENVIAR ─────]             │
   └─────────────────────────────────────────┘

   [B - CHALLENGER]
   ┌─────────────────────────────────────────┐
   │   Pare de perder clientes por falta de   │
   │              follow-up                   │
   │                                          │
   │   [── Quero minha análise gratuita ──]   │
   │      Sem cartão de crédito ✓             │
   └─────────────────────────────────────────┘
   ```

## Veto Conditions
- Variante B com mais de 1 mudança conceitual → dividir em 2 testes separados
- Variante com diferença visual imperceptível → ampliar mudança
- Variante tecnicamente complexa que demora mais de 1 sprint para implementar → simplificar
- Testes que modificam o mesmo elemento ao mesmo tempo → priorizar e serializar

## Output Esperado
Arquivo `ab-variants-spec.md` contendo:
- Especificação completa de variante A e B para cada teste priorizado
- Mock visual (wireframe de texto ou referência de design)
- Validação de isolamento para cada teste
- Especificações técnicas de implementação
- Estimativa de esforço total
- Ordem de implementação recomendada

## Completion Criteria
- [ ] Especificação completa (A + B) para todos os testes do TOP 3
- [ ] Isolamento validado (exatamente 1 variável por teste)
- [ ] Mock visual criado para cada par de variantes
- [ ] Especificações técnicas suficientes para implementação sem dúvidas
- [ ] Estimativa de esforço por teste calculada
- [ ] Ordem de implementação definida (paralelo ou serializado)
- [ ] Arquivo `ab-variants-spec.md` criado e entregue para ce-ab-setup
