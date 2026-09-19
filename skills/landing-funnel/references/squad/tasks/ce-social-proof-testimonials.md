---
task: structureTestimonials()
agent: ce-social-proof
description: "Estruturar testimonials no formato correto: foto real + nome + cargo + empresa + resultado específico com número"
elicit: true
responsavel: "Trust"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: rawTestimonials
    tipo: object
    obrigatorio: true
    descricao: "Depoimentos brutos de clientes"

Saida:
  - nome: structuredTestimonials
    tipo: file
    obrigatorio: true
    descricao: "Testimonials no formato correto: foto + nome + cargo + empresa + resultado específico com número"

Checklist:
  pre-conditions:
    - "[ ] Depoimentos brutos coletados"
  post-conditions:
    - "[ ] Cada testimonial com resultado mensurável"
    - "[ ] Fotos reais disponíveis"
    - "[ ] Diversidade de perfis representada"
---

# Task: structureTestimonials()

## Objetivo
Transformar o material bruto de depoimentos (respostas informais, screenshots de WhatsApp, emails) em testimonials estruturados no formato que maximiza credibilidade e impacto na conversão. Um depoimento bem estruturado pode ser 3x mais persuasivo do que um depoimento bruto não editado.

## Inputs Necessários
- `social-proof-audit.md` (inventário e scores dos depoimentos)
- Material bruto dos depoimentos classificados como "usar" ou "reformular"
- `audience-profile.md` (persona — para identificar se depoentes representam o público)
- `copy-review-report.md` (tom e linguagem da LP — testimonials devem ser consistentes)

## Processo
1. **Elicitação de informações faltantes** — Para cada depoimento a usar, verificar presença de:
   - Nome completo (ou Nome + Sobrenome inicial para casos onde pessoa prefere parcial)
   - Foto de boa qualidade (80×80px mínimo, rosto claro)
   - Cargo e/ou empresa
   - Resultado específico com número e prazo
   - Permissão explícita do depoente para usar na LP

   Se algum campo crítico estiver faltando: contatar o cliente para que entre em contato com o depoente.

2. **Estrutura obrigatória de testimonial de alta conversão:**

   ```
   [FOTO - circular, 64-96px]
   [TEXTO DO DEPOIMENTO]
   — Nome Sobrenome, @handle opcional
     Cargo | Empresa
   [RESULTADO DESTACADO: "+X% em Y dias"]
   [ESTRELAS - 5/5 se aplicável]
   ```

   **Exemplo de testimonial FRACO → FORTE:**

   Fraco: "O produto é muito bom. Recomendo a todos!"
   — João S.

   Forte: "Antes eu perdia cerca de 6 horas por semana tentando organizar minha agenda de clientes. Em 3 semanas usando [produto], reduzi esse tempo para menos de 1 hora. O ROI se pagou no primeiro mês."
   — João Silva, CEO @JoaoSilvaConsultoria
     Consultor de Vendas | Silva Consultoria
   [+600% de eficiência em 3 semanas]

3. **Edição de depoimentos brutos** — Guia de edição ética:
   - PERMITIDO: Corrigir gramática e ortografia
   - PERMITIDO: Remover informações irrelevantes para a LP
   - PERMITIDO: Reorganizar a ordem de ideias para maior clareza
   - PERMITIDO: Adicionar resultado específico se o cliente mencionou informalmente mas não no depoimento escrito (verificar com cliente)
   - PROIBIDO: Inventar resultados que o cliente não mencionou
   - PROIBIDO: Alterar o sentido ou exagerar a afirmação original
   - PROIBIDO: Usar depoimento sem permissão

4. **Estruturação por nível de destaque** — Definir hierarquia de uso:

   **Tier 1 — Hero Testimonials (score 18-21):**
   - Posição: Acima do fold, junto ao hero OU logo após o hero
   - Formato: Foto grande + texto longo + resultado em destaque
   - Quantidade: 1-2 máximo nesta posição

   **Tier 2 — Grid Testimonials (score 12-17):**
   - Posição: Seção de depoimentos (meio da LP)
   - Formato: Foto + texto médio + resultado
   - Quantidade: 3-6 em grid 3 colunas

   **Tier 3 — Inline Testimonials (score 9-11):**
   - Posição: Entre seções, como reforço pontual
   - Formato: Foto pequena + 1-2 frases + nome
   - Quantidade: 2-3 inline

5. **Testemunhais de vídeo** — Se houver vídeos disponíveis:
   - Criar sumário textual com resultado principal (para quem não assiste)
   - Thumbnail com rosto do depoente + resultado em texto sobreposto
   - Duração ideal: 30-90 segundos por depoimento de vídeo

6. **Formato de dados estruturado** — Para uso pelo frontend:
   ```typescript
   // src/data/testimonials.ts
   export const testimonials: Testimonial[] = [
     {
       id: 'joao-silva',
       quote: "Antes eu perdia cerca de 6 horas por semana...",
       shortQuote: "Reduzi de 6h para 1h por semana em 3 semanas",
       author: {
         name: "João Silva",
         handle: "@joaosilva",
         role: "Consultor de Vendas",
         company: "Silva Consultoria",
         avatarSrc: "/images/social-proof/avatar-joao-silva.webp",
       },
       result: "+600% de eficiência em 3 semanas",
       rating: 5,
       tier: 1,
       videoSrc: null,
     },
     // ...
   ]
   ```

7. **Verificação de autenticidade** — Antes de publicar:
   - Confirmar permissão de todos os depoentes por escrito (email ou WhatsApp com evidência)
   - Guardar registro de permissões no cliente
   - Verificar que fotos são das pessoas reais (não stock photos sem consentimento)

## Veto Conditions
- Depoimento sem resultado específico sendo colocado em destaque → mover para posição secundária ou coletar resultado
- Foto de stock usada como "avatar de depoente" sem a pessoa existir → remover (ilegal e antiético)
- Depoimento editado de forma que altera o sentido original → reverter
- Sem permissão documentada de algum depoente → não usar

## Output Esperado
- Arquivo `testimonials-structured.md` com todos os testimonials formatados e prontos
- Arquivo `src/data/testimonials.ts` com dados tipados para uso no frontend
- Lista de permissões obtidas (documentação interna)
- Definição de tier para cada testimonial (posicionamento na LP)
- Indicação de quais testimonials precisam de avatar gerado pelo ce-image-creator

## Completion Criteria
- [ ] 100% dos testimonials auditados estruturados no formato correto
- [ ] Cada testimonial Tier 1 tem: foto + nome + cargo/empresa + resultado com número
- [ ] Edições documentadas (o que foi alterado e por quê)
- [ ] Permissão confirmada para cada testimonial a ser publicado
- [ ] Hierarquia de tiers definida e justificada
- [ ] Dados tipados TypeScript criados em `testimonials.ts`
- [ ] Indicações de avatares a gerar entregues ao ce-image-creator
- [ ] Arquivo `testimonials-structured.md` criado
