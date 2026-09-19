---
task: reviewCopyTone()
agent: ce-copywriter
description: "Revisar tom, consistência de voz, nível de consciência adequado, ausência de jargões"
elicit: false
responsavel: "Pulse"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: allSectionCopy
    tipo: file
    obrigatorio: true
    descricao: "Todas as seções de copy escritas"
  - nome: audienceProfile
    tipo: file
    obrigatorio: true
    descricao: "Perfil da audiência com nível de consciência"

Saida:
  - nome: copyReviewReport
    tipo: file
    obrigatorio: true
    descricao: "Relatório de revisão de tom: consistência, nível de consciência e ausência de jargões"

Checklist:
  pre-conditions:
    - "[ ] Todas as seções escritas"
  post-conditions:
    - "[ ] Tom consistente em todas as seções"
    - "[ ] Nível de consciência correto"
    - "[ ] Jargões técnicos eliminados"
---

# Task: reviewCopyTone()

## Objetivo
Realizar uma revisão editorial sistemática de todo o copy produzido para a landing page, garantindo consistência de voz, adequação ao nível de consciência do público, ausência de jargões e coerência narrativa entre seções.

## Inputs Necessários
- Todos os arquivos `copy-[seção].md` produzidos
- `vsl-script.md` (se produzido)
- `ab-copy-variants.md` (se produzido)
- `audience-profile.md` (linguagem nativa, nível de consciência, persona)
- `product-brief.md` (voz e tom da marca, se definidos)
- `intelligence-brief.md` (ângulo principal escolhido)

## Processo
1. **Definição do guia de voz** — Antes de revisar, documentar os parâmetros de voz da marca:
   - **Tom predominante:** (escolher 3 de: profissional, íntimo, enérgico, confiante, empático, direto, inspiracional, técnico, conversacional)
   - **Tom a evitar:** (escolher 2-3)
   - **Nível de formalidade:** (1=muito informal/gírias → 5=muito formal/corporativo) — definir o número
   - **Pronomes:** você ou tu? (consistência absoluta)
   - **Voz ativa vs passiva:** preferência
   - **Exemplos de frases on-brand vs off-brand**

2. **Auditoria de consistência de tom** — Ler cada seção em sequência e verificar:
   - O tom muda abruptamente entre seções? (ex: hero emocional → pricing muito frio)
   - O nível de formalidade é consistente?
   - O uso de pronomes é uniforme?
   - A energia do copy se mantém ou cai no meio da página?
   Marcar inconsistências com [INCONSISTÊNCIA] e sugestão de correção.

3. **Auditoria de nível de consciência** — Verificar se o copy responde adequadamente ao nível de consciência definido em `audience-profile.md`:
   - **Unaware:** O copy educa antes de vender? Não assume que o leitor conhece o problema?
   - **Problem-aware:** O copy agita a dor antes de apresentar a solução?
   - **Solution-aware:** O copy diferencia da concorrência antes de apresentar o produto?
   - **Product-aware:** O copy foca em prova, detalhes e oferta, não em educação básica?
   - **Most-aware:** O copy vai direto ao ponto com oferta e urgência?
   Marcar seções que "falam para nível errado" com [NÍVEL INCORRETO].

4. **Caça a jargões e termos técnicos** — Varrer todo o copy em busca de:
   - Termos de marketing que o público não usaria ("funil de conversão", "lead qualificado", "ROI")
   - Termos técnicos do produto sem explicação ("API", "SaaS", "otimização algorítmica")
   - Anglicismos desnecessários que distanciam o público
   - Siglas sem definição
   Para cada jargão encontrado: substituir por linguagem nativa do público (de `audience-profile.md`).

5. **Verificação de fluxo narrativo** — Ler a página completa como um visitante:
   - A narrativa tem início, meio e fim?
   - Cada seção prepara o terreno para a próxima?
   - O ritmo de urgência aumenta progressivamente até o CTA?
   - Há contradições entre seções? (ex: "Fácil de usar" na seção de benefícios + "Requer 2 horas de configuração" no FAQ)

6. **Verificação de especificidade** — Caçar vagas generalizações:
   - "Melhore seus resultados" → "Aumente em X%" ou "Conquiste Y em Z dias"
   - "Empresas líderes" → nomear ou quantificar
   - "Muito tempo" → quantificar
   - "Resultados comprovados" → apresentar prova específica
   Marcar com [ESPECÍFICO] e sugestão de melhoria.

7. **Produção do relatório de revisão** — Documentar todas as alterações com antes/depois e justificativa.

## Veto Conditions
- Copy com jargões de marketing direcionados ao público leigo → corrigir antes de fechar revisão
- Inconsistências de pronome (você vs tu) na mesma seção → corrigir todos
- Copy que trata o público como mais ou menos sofisticado do que o nível de consciência real → corrigir abordagem
- Contradições entre seções → resolver antes de fechar

## Output Esperado
Arquivo `copy-review-report.md` contendo:
- Guia de voz documentado
- Lista de inconsistências encontradas com correções aplicadas
- Lista de jargões substituídos (antes → depois)
- Lista de generalizações corrigidas (antes → depois)
- Avaliação do fluxo narrativo (aprovado / necessita ajuste)
- Copy final aprovado para cada seção (com histórico de alterações)
- Score de qualidade geral: 0-100

## Completion Criteria
- [ ] Guia de voz documentado para referência futura
- [ ] 100% das seções revisadas contra checklist de tom
- [ ] Nível de consciência adequado verificado em todas as seções
- [ ] Zero jargões de marketing direcionados ao público leigo
- [ ] Zero inconsistências de pronome
- [ ] Fluxo narrativo avaliado e aprovado
- [ ] Contradições entre seções resolvidas
- [ ] Score de qualidade calculado
- [ ] Arquivo `copy-review-report.md` criado com copy final aprovado
