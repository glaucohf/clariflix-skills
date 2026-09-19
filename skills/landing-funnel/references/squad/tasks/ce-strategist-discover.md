---
task: discoverProduct()
agent: ce-strategist
description: "Absorver o produto: nome, oferta, preço, diferencial, objetivo da página"
elicit: true
responsavel: "Vortex"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: productDescription
    tipo: string
    obrigatorio: true
    descricao: "Descrição do produto ou serviço fornecida pelo usuário"
  - nome: existingMaterials
    tipo: object
    obrigatorio: false
    descricao: "Materiais existentes: pitch deck, PDF, landing pages anteriores"

Saida:
  - nome: productBrief
    tipo: file
    obrigatorio: true
    descricao: "Briefing completo do produto com USP, oferta, preço e objetivos"

Checklist:
  pre-conditions:
    - "[ ] Usuário forneceu descrição do produto"
  post-conditions:
    - "[ ] Product brief gerado e validado"
    - "[ ] Objetivo da LP definido"
---

# Task: discoverProduct()

## Objetivo
Realizar uma imersão profunda no produto do cliente para construir uma base de conhecimento sólida antes de qualquer decisão estratégica ou criativa. O output desta task alimenta todas as demais tasks do squad.

## Inputs Necessários
- Nome do produto ou serviço
- URL do site atual (se existir)
- Materiais de vendas existentes (pitch deck, PDF, landing pages anteriores)
- Preço atual e modelo de cobrança (único, recorrente, freemium)
- Objetivo principal da página (captura de lead, venda direta, agendamento, download)
- Diferencial competitivo percebido pelo cliente
- Resultados já obtidos por clientes (se houver)

## Processo
1. **Briefing inicial** — Conduzir entrevista estruturada com o cliente ou representante, cobrindo produto, mercado e objetivos. Fazer perguntas abertas antes das fechadas.
2. **Análise de materiais existentes** — Revisar todos os materiais fornecidos: identificar linguagem usada, promessas feitas, provas apresentadas e inconsistências.
3. **Mapeamento da oferta** — Decompor a oferta em: o que é entregue (features), o que o cliente recebe (benefícios), qual transformação é prometida (outcome) e qual é o prazo esperado.
4. **Identificação do modelo de precificação** — Documentar preço, comparativos de mercado percebidos, garantias oferecidas e condições especiais.
5. **Definição do objetivo primário da LP** — Classificar o objetivo em: geração de lead qualificado, venda direta (checkout), agendamento de call, download de lead magnet ou acesso a evento.
6. **Consolidação do Product Brief** — Organizar todas as informações em documento estruturado `product-brief.md` que será referência para todos os agentes.

## Veto Conditions
- Cliente não consegue articular o diferencial do produto com clareza → interromper e solicitar sessão de posicionamento antes de prosseguir
- Oferta contém promessas não comprovadas ou potencialmente abusivas (garantias impossíveis, resultados financeiros sem disclaimer) → sinalizar risco legal antes de escrever copy
- Ausência total de provas sociais ou resultados → anotar como risco de conversão crítico no brief
- Preço inconsistente com o posicionamento declarado → sinalizar e registrar no brief

## Output Esperado
Arquivo `product-brief.md` contendo:
- Nome, tagline e descrição em 1 parágrafo
- Oferta decomposta (features → benefícios → outcomes)
- Modelo de precificação completo
- Objetivo primário e secundário da LP
- Diferencial articulado em 1 frase de posicionamento
- Provas disponíveis (depoimentos, cases, números, certificações)
- Riscos e alertas identificados

## Completion Criteria
- [ ] Produto compreendido e descrito com precisão em 1 parágrafo sem jargões
- [ ] Oferta decomposta em features, benefícios e outcomes mensuráveis
- [ ] Preço e modelo de cobrança documentados com clareza
- [ ] Objetivo primário da LP definido e acordado com o cliente
- [ ] Diferencial articulado em frase única testável
- [ ] Provas sociais inventariadas (quantidade e qualidade registradas)
- [ ] Arquivo `product-brief.md` criado e disponível para os demais agentes
- [ ] Riscos e alertas documentados no brief
