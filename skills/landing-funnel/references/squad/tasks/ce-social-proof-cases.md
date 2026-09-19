---
task: buildCaseStudies()
agent: ce-social-proof
description: "Construir micro cases: situação antes → solução → resultado mensurável (framework STAR)"
elicit: true
responsavel: "Trust"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: clientCases
    tipo: object
    obrigatorio: true
    descricao: "Casos de sucesso de clientes em formato livre"

Saida:
  - nome: microCases
    tipo: file
    obrigatorio: true
    descricao: "Micro cases no framework STAR: Situação → Tarefa → Ação → Resultado com métricas específicas"

Checklist:
  pre-conditions:
    - "[ ] Casos de sucesso documentados"
  post-conditions:
    - "[ ] Cada case com resultado mensurável"
    - "[ ] Framework STAR aplicado"
    - "[ ] Autorização do cliente obtida"
---

# Task: buildCaseStudies()

## Objetivo
Transformar histórias de clientes em micro cases estruturados usando o framework STAR (Situation → Task → Action → Result) adaptado para landing pages. Micro cases são mais convincentes que depoimentos simples porque contam uma história completa com before/after verificável — ativando o pensamento analítico E emocional do prospect.

## Inputs Necessários
- `social-proof-audit.md` (clientes com melhores resultados identificados)
- `testimonials-structured.md` (testimonials — alguns podem ser expandidos em cases)
- `audience-profile.md` (persona — cases devem ser de pessoas parecidas com o avatar)
- `product-brief.md` (produto, benefícios prometidos — cases devem validar as promessas)
- Contato direto com 2-3 clientes para entrevista (intermediado pelo cliente)

## Processo
1. **Elicitação e seleção de clientes para cases** — Identificar os melhores candidatos:
   - Resultados mais expressivos e mensuráveis
   - Situação inicial suficientemente reconhecível pelo público-alvo
   - Cliente disposto a ser citado publicamente (com nome, foto, empresa)
   - Jornada com elementos narrativos interessantes (obstáculo, virada, resultado)
   Selecionar 2-3 clientes para micro cases completos.

2. **Roteiro de entrevista para extração de case** — Conduzir via chamada de 20-30 minutos:

   **Bloco 1 — Situação antes:**
   - "Descreva sua situação antes de começar a usar [produto]. O que estava acontecendo?"
   - "Quais eram os principais problemas ou frustrações que você enfrentava?"
   - "O que você já havia tentado antes de encontrar [produto]? Por que não funcionou?"
   - "Qual era o impacto desse problema no seu negócio/vida em termos concretos?"

   **Bloco 2 — Decisão e implementação:**
   - "O que te levou a experimentar [produto] naquele momento?"
   - "Havia alguma dúvida ou hesitação antes de começar? O que te fez decidir mesmo assim?"
   - "Como foi o processo de começar a usar?"

   **Bloco 3 — Resultados:**
   - "Qual foi o primeiro resultado que você notou? Em quanto tempo?"
   - "Qual é o resultado mais significativo que você conseguiu com [produto]?"
   - "Se você tiver que colocar em números: antes você tinha [X], agora você tem [Y]?"
   - "O que mudou no seu negócio/vida por causa desse resultado?"

   **Bloco 4 — Recomendação:**
   - "Para quem você recomendaria [produto]? Qual perfil de pessoa se beneficiaria mais?"
   - "Qual é o conselho que você daria para quem está na mesma situação que você estava?"

3. **Estrutura do micro case (framework STAR adaptado):**

   ```markdown
   ## [Resultado principal como título]
   Exemplo: "Como [Nome] dobrou sua carteira de clientes em 60 dias"

   ### Situação (antes)
   [2-3 frases descrevendo o problema específico com números quando possível]
   Exemplo: "João gerenciava 45 clientes em planilhas espalhadas. Perdia em média 8h semanais
   em trabalho manual e havia perdido 3 clientes por falta de follow-up no trimestre anterior."

   ### Solução
   [1-2 frases: o que ele fez com o produto]
   Exemplo: "Em 1 semana, João migrou toda a base para [produto] e configurou automações
   de follow-up para os momentos críticos do relacionamento."

   ### Resultado (depois)
   [Resultado principal em destaque + contexto]
   **Resultado:** +90 novos clientes em 60 dias (de 45 para 135)
   **Eficiência:** Redução de 8h para 1h/semana em trabalho manual
   **Receita:** +R$22.000 em receita recorrente mensal

   > "Finalmente consigo escalar sem contratar mais pessoas."
   > — João Silva, CEO Silva Consultoria

   [Foto + nome + cargo + empresa]
   ```

4. **Versão condensada para LP** — Micro case em formato "card" (para uso em seção de cases):

   ```
   [Foto circular - 64px]
   [Nome e Empresa]
   ─────────────────
   ANTES: [Situação em 1 frase]
   ↓
   DEPOIS: [Resultado em 1 frase com número]
   ─────────────────
   "[Citação curta de 10-20 palavras]"
   [Ver case completo →] (link para case detalhado, se existir)
   ```

5. **Construção visual do "antes/depois"** — Elementos gráficos para reforçar:
   - Linha do tempo antes/depois
   - Gráfico simples de crescimento (se há dados de crescimento)
   - Comparativo de números (antes vs depois em destaque visual)
   - Screenshot do resultado (dashboard, email de elogio, comprovante)

6. **Verificação de autorização e veracidade:**
   - Confirmar todos os números com o cliente antes de publicar
   - Obter aprovação do texto final pelo depoente
   - Guardar evidências dos resultados (screenshot, relatório) em arquivo interno
   - Adicionar disclaimer se resultado não é garantido ou típico

7. **Versões por uso:**
   - Versão LP: Micro case condensado (150-250 palavras)
   - Versão Blog/Long-form: Case completo (500-800 palavras) para conteúdo de topo de funil
   - Versão Social: Resultado em destaque para usar em anúncio ou stories

## Veto Conditions
- Case com resultados não verificáveis pelo cliente → adicionar disclaimer ou não publicar
- Case de persona completamente diferente do avatar da LP → não incluir ou criar seção específica
- Case sem pelo menos 1 número concreto → fortalecer antes de publicar
- Publicar case sem aprovação explícita do depoente → obter antes de publicar

## Output Esperado
- 2-3 micro cases completos em `case-studies.md`
- Versão condensada (card) para uso na seção de cases da LP
- Dados estruturados em `src/data/cases.ts` para uso no frontend
- Elementos visuais especificados (gráficos, antes/depois) para ce-image-creator
- Versão long-form para uso em blog/conteúdo (opcional)

## Completion Criteria
- [ ] Mínimo 2 clientes entrevistados com roteiro estruturado
- [ ] Cada case seguindo framework STAR com resultado mensurável
- [ ] Número concreto verificado em TODOS os cases
- [ ] Versão condensada (card) criada para cada case
- [ ] Aprovação do depoente obtida para cada case
- [ ] Dados tipados criados em `src/data/cases.ts`
- [ ] Elementos visuais especificados para ce-image-creator
- [ ] Arquivo `case-studies.md` criado
