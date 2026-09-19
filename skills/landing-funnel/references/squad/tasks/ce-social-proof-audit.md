---
task: auditSocialProof()
agent: ce-social-proof
description: "Auditar prova social existente: quantidade, qualidade, especificidade, credibilidade, diversidade"
elicit: true
responsavel: "Trust"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: existingSocialProof
    tipo: object
    obrigatorio: false
    descricao: "Social proof existente: depoimentos, cases, logos, números"

Saida:
  - nome: socialProofAudit
    tipo: file
    obrigatorio: true
    descricao: "Auditoria de social proof: score de qualidade, gaps identificados e recomendações"

Checklist:
  pre-conditions:
    - "[ ] Material de social proof coletado"
  post-conditions:
    - "[ ] Score de qualidade calculado"
    - "[ ] Gaps documentados"
    - "[ ] Plano de coleta definido"
---

# Task: auditSocialProof()

## Objetivo
Realizar um audit completo e honesto de toda a prova social disponível do cliente — sem inflar nem subestimar o que existe. O audit determina a estratégia de social proof da LP: se o material é forte, usa-se em posição de destaque; se é fraco, esta task inicia o processo de coleta ativa de provas mais impactantes.

## Inputs Necessários
- `requirements.md` (Q9 e Q10 sobre depoimentos e resultados)
- `product-brief.md` (produto, nicho, tempo de mercado)
- `audience-profile.md` (persona — provas precisam ser de pessoas parecidas com o avatar)
- Todos os depoimentos existentes do cliente (texto, áudio, vídeo)
- Cases de sucesso existentes
- Números de resultados (clientes, usuários, faturamento gerado, etc.)
- Certificações, prêmios, menções na mídia, logos de clientes

## Processo
1. **Elicitação de material de prova social** — Coletar do cliente:
   - Todos os depoimentos em qualquer formato (WhatsApp, email, formulário, Google Reviews)
   - Cases de sucesso documentados ou apenas conhecimento informal
   - Números disponíveis: total de clientes, anos de mercado, resultados específicos
   - Screenshots de conversas positivas (com permissão)
   - Vídeos de depoimentos
   - Logos de empresas clientes
   - Certificações, cursos, parcerias de autoridade
   - Menções em mídia, podcasts, entrevistas

2. **Classificação dos depoimentos** — Para cada depoimento coletado, aplicar scorecard:

   | Critério | Fraco (1pt) | Médio (2pt) | Forte (3pt) |
   |---------|-------------|-------------|-------------|
   | **Foto** | Sem foto | Foto genérica | Foto real reconhecível |
   | **Nome** | Anônimo | Nome + inicial | Nome completo + @handle |
   | **Cargo/Empresa** | Ausente | Só cargo | Cargo + empresa |
   | **Especificidade** | "Adorei o produto" | "Melhorou meu processo" | "Economizei 8h/semana no primeiro mês" |
   | **Resultado mensurável** | Nenhum | Qualitativo | Número + prazo específico |
   | **Antes/Depois** | Ausente | Vago | Situação antes clara + resultado depois |
   | **Credibilidade do depoente** | Desconhecido | Cargo relevante | Autoridade reconhecida no nicho |

   Score máximo: 21 pontos
   - 15-21: Depoimento FORTE → Posição de destaque
   - 9-14: Depoimento MÉDIO → Pode ser usado com melhorias
   - 1-8: Depoimento FRACO → Não usar na LP sem reformulação

3. **Audit de diversidade** — Verificar se a prova social representa:
   - Diferentes tipos de cliente (micro, pequeno, médio porte)
   - Diferentes segmentos do nicho
   - Diferentes resultados obtidos (não apenas "o melhor caso")
   - Diferentes tempos de uso (resultado rápido + resultado de longo prazo)
   - Representação geográfica relevante (se produto é nacional)
   - Representação de gênero adequada ao público

4. **Análise de lacunas** — Identificar gaps críticos:
   - Sem depoimentos com foto → lacuna crítica (40% de impacto)
   - Sem resultado mensurável em nenhum depoimento → lacuna crítica
   - Todos os depoimentos genéricos → lacuna crítica
   - Sem video testimonial → lacuna significativa
   - Sem case de sucesso estruturado → lacuna significativa
   - Sem número de clientes → lacuna de credibilidade
   - Sem logos de clientes (B2B) → lacuna de autoridade

5. **Plano de coleta ativa** — Para lacunas identificadas, criar plano de ação:
   - Lista de clientes para contatar pedindo depoimento específico
   - Roteiro de pergunta que extrai depoimento forte: "Qual era sua situação antes de usar [produto]? Qual resultado específico você obteve e em quanto tempo?"
   - Prazo para coleta antes do lançamento da LP

6. **Inventário final** — Classificar todo o material em:
   - "Usar na LP" (score ≥ 15)
   - "Usar com reformulação" (score 9-14)
   - "Não usar" (score < 9)
   - "Coletar ativamente" (gaps identificados)

## Veto Conditions
- Nenhum depoimento com resultado mensurável disponível → priorizar coleta ativa antes de lançar LP
- Todos os depoimentos anônimos (sem nome/foto) → sinalizar risco de credibilidade alto
- Produto muito novo (< 3 meses) sem nenhum cliente → recomendar estratégia de validação antes de LP de escala

## Output Esperado
Arquivo `social-proof-audit.md` contendo:
- Inventário completo de prova social com score por item
- Classificação: usar / reformular / descartar
- Análise de diversidade com gaps identificados
- TOP 5 depoimentos mais fortes com justificativa
- Lacunas críticas priorizadas
- Plano de coleta ativa (lista de clientes + roteiro de pergunta)
- Recomendação estratégica: LP pode lançar com social proof atual ou precisa de mais material?

## Completion Criteria
- [ ] 100% do material de prova social do cliente coletado
- [ ] Scorecard aplicado a cada depoimento
- [ ] Análise de diversidade completada
- [ ] TOP 5 depoimentos selecionados para destaque
- [ ] Lacunas críticas identificadas com prioridade
- [ ] Plano de coleta ativa definido (se necessário)
- [ ] Recomendação estratégica documentada
- [ ] Arquivo `social-proof-audit.md` criado e disponível para todo o squad
