---
task: auditCROByDesign()
agent: ce-design-architect
description: "EXCLUSIVO: audit de CRO por design usando Fogg Behavior Model + Cialdini principles. Verificar: CTA acima da dobra, hierarquia visual, direção de olhar, friction points"
elicit: false
responsavel: "Canvas"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: sectionLayouts
    tipo: file
    obrigatorio: true
    descricao: "Layouts propostos para as seções da LP"

Saida:
  - nome: croAuditReport
    tipo: file
    obrigatorio: true
    descricao: "Relatório de CRO por design com Fogg Behavior Model e Cialdini principles aplicados"

Checklist:
  pre-conditions:
    - "[ ] Layouts das seções disponíveis"
  post-conditions:
    - "[ ] CTA acima da dobra confirmado"
    - "[ ] Hierarquia visual validada"
    - "[ ] Friction points eliminados"
---

# Task: auditCROByDesign()

## Objetivo
Realizar um audit de Conversion Rate Optimization (CRO) centrado em decisões de design antes que qualquer linha de código seja escrita. Este processo garante que a arquitetura visual da LP seja construída para converter desde o início — não corrigida depois. É o DIFERENCIAL que separa LPs de alta performance de LPs bonitas que não convertem.

## Inputs Necessários
- `scope.md` (lista de seções e objetivos)
- `audience-profile.md` (persona, dispositivos predominantes, comportamento esperado)
- `traffic-data-analysis.md` (scroll depth típico, tempo de sessão, mobile/desktop split)
- `copy-review-report.md` (copy final aprovado — para entender hierarquia de informação)
- `intelligence-brief.md` (briefing de design do nicho)
- `design-system-decision.md` (paleta, tipografia, estilo visual)

## Processo
1. **Aplicação do Fogg Behavior Model** — Avaliar os 3 elementos do modelo B = MAT (Behavior = Motivation × Ability × Trigger):

   **Motivation (Motivação):**
   - O hero comunica claramente a transformação desejada antes do fold?
   - A proposta de valor está em linguagem do cliente (não do produto)?
   - O benefício emocional está visualmente em destaque (tamanho, contraste, posição)?
   - Há elementos que geram prazer antecipado (imagens de resultado, depoimentos acima do fold)?

   **Ability (Facilidade de agir):**
   - O formulário/CTA tem o menor número de campos possível (mínimo viável)?
   - O caminho para conversão é visualmente óbvio (máximo 2 cliques para chegar ao formulário)?
   - Há friction visual desnecessária (CAPTCHA visível, formulário complexo, muitos campos obrigatórios)?
   - O CTA está acessível sem scroll em mobile? E em desktop?

   **Trigger (Gatilho):**
   - O CTA está posicionado acima da dobra em TODAS as resoluções (320px, 375px, 768px, 1280px)?
   - Existe CTA repetido em pontos estratégicos do scroll (após prova social, após oferta, no footer)?
   - Há elemento de urgência ou escassez próximo ao CTA principal?
   - O CTA contrasta visualmente com o ambiente (cor, tamanho, espaço em branco)?

2. **Aplicação dos Princípios de Cialdini** — Verificar presença e posicionamento visual de cada princípio:

   | Princípio | Implementação esperada | Posição recomendada |
   |-----------|----------------------|-------------------|
   | Reciprocidade | Lead magnet, conteúdo gratuito, garantia generosa | Hero ou abaixo do hero |
   | Comprometimento | Micro-sim inicial antes do CTA principal | Antes do formulário |
   | Prova Social | Número de clientes, depoimentos, logos | Acima e abaixo do fold |
   | Autoridade | Credenciais, mídia, parceiros, certificações | Abaixo do hero |
   | Afinidade | Foto do fundador, linguagem do público, identidade compartilhada | Hero ou "Para quem é" |
   | Escassez | Vagas limitadas, timer, prazo | Próximo ao CTA |
   | Unidade | "Família", "Comunidade", pertencimento ao grupo | Seção de comunidade ou depoimentos |

3. **Mapa de hierarquia visual** — Definir ordem de atenção em cada seção:
   - Elemento de maior peso visual → Deve ser o headline ou elemento de conversão principal
   - Elemento de segundo nível → Subheadline ou imagem
   - Elemento de terceiro nível → Body copy e bullets
   - Elemento de menor peso → Elementos secundários (logos, certificações)
   Garantir que o olho do visitante seja guiado naturalmente para o CTA.

4. **Análise de direção de olhar** — Verificar se imagens direcionam atenção para o CTA:
   - Fotos de pessoas devem olhar para o texto/CTA, não para fora da tela
   - Setas e elementos direcionais devem apontar para o CTA
   - Whitespace deve criar "canalização" visual em direção ao elemento de conversão
   - Evitar elementos visuais que competem com o CTA pela atenção

5. **Mapeamento de friction points visuais** — Identificar e eliminar:
   - Menus de navegação que permitem escape da página (LP sem nav = melhor conversão)
   - Links externos desnecessários
   - Footer com excesso de links
   - Pop-ups de saída (planejar vs impacto na UX)
   - Animações que distraem do CTA
   - Elementos visuais sem propósito de conversão

6. **Audit de mobile-first CRO** — Verificar especificamente para mobile:
   - CTA acessível sem scroll no viewport 375px × 667px (iPhone SE)?
   - Botões com área de toque mínima de 44×44px?
   - Fontes legíveis sem zoom (mínimo 16px para body)?
   - Imagens que não quebram o layout em mobile?
   - Formulário utilizável com teclado mobile visível?

7. **Produção do CRO Design Brief** — Documentar todas as decisões de design motivadas por CRO com justificativa e referência ao modelo (Fogg/Cialdini/Best Practice).

## Veto Conditions
- CTA não visível acima da dobra em nenhuma resolução → reposicionar antes de avançar
- Formulário com mais de 5 campos obrigatórios sem justificativa → simplificar
- Prova social inexistente acima do fold → adicionar pelo menos 1 elemento
- Imagens de pessoas olhando para fora da tela ou para cima → corrigir direção

## Output Esperado
Arquivo `cro-design-audit.md` contendo:
- Avaliação B=MAT com checklist de Motivação, Facilidade e Trigger
- Mapa de princípios de Cialdini aplicados (presentes + ausentes)
- Mapa de hierarquia visual por seção
- Lista de friction points com ações corretivas
- Especificações de CRO mobile
- Decisões de design motivadas por CRO (documentadas com justificativa)
- Score de prontidão de CRO: 0-100

## Completion Criteria
- [ ] Modelo Fogg B=MAT avaliado completamente
- [ ] Todos os 7 princípios de Cialdini verificados e posicionados
- [ ] Hierarquia visual definida para cada seção
- [ ] Direção de olhar verificada para todas as imagens planejadas
- [ ] Friction points identificados e eliminados
- [ ] CTA acima da dobra verificado em 320px, 375px, 768px, 1280px
- [ ] Mobile CRO auditado
- [ ] Score de CRO calculado
- [ ] Arquivo `cro-design-audit.md` criado para guiar ce-design-architect-sections e ce-frontend-dev
