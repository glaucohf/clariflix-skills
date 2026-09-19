---
task: writeVSLScript()
agent: ce-copywriter
description: "EXCLUSIVO: escrever script de VSL (Video Sales Letter) de 3-7 min com estrutura: hook → problema → agitação → solução → prova → oferta → CTA"
elicit: true
responsavel: "Pulse"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: intelligenceBrief
    tipo: file
    obrigatorio: true
    descricao: "Intelligence Brief completo"
  - nome: productBrief
    tipo: file
    obrigatorio: true
    descricao: "Briefing do produto"

Saida:
  - nome: vslScript
    tipo: file
    obrigatorio: true
    descricao: "Script de VSL de 3-7 min: hook → problema → agitação → solução → prova → oferta → CTA"

Checklist:
  pre-conditions:
    - "[ ] Intelligence Brief disponível"
  post-conditions:
    - "[ ] Hook nos primeiros 30 segundos"
    - "[ ] Prova social incluída"
    - "[ ] CTA claro no final"
---

# Task: writeVSLScript()

## Objetivo
Produzir o script completo de um Video Sales Letter (VSL) de 3 a 7 minutos otimizado para conversão. O VSL é um dos elementos de maior impacto em landing pages de produtos complexos ou de ticket médio/alto — quando bem executado, pode duplicar ou triplicar a taxa de conversão da página.

## Inputs Necessários
- `intelligence-brief.md` (ângulos, dores, diferenciais, linguagem nativa)
- `audience-profile.md` (persona, nível de consciência, objeções principais)
- `copy-formulas.md` (hooks e frameworks do nicho)
- `product-brief.md` (produto, preço, garantia, provas disponíveis)
- Duração-alvo do VSL (3, 5 ou 7 minutos — impacta extensão do script)
- Quem irá apresentar o VSL (fundador, avatar, voz over, animação)
- Recursos visuais disponíveis (slides, demonstração de produto, depoimentos em vídeo)

## Processo
1. **Definição de parâmetros** — Antes de escrever, definir com o cliente:
   - Duração-alvo (3min = produto simples/barato; 5min = ticket médio; 7min = ticket alto/complexo)
   - Formato (talking head, slides + voz, animação, screen recording + voz)
   - Tom (pessoal/íntimo, profissional/autoridade, energia/motivacional)
   - CTA ao vivo ou somente pós-vídeo

2. **Construção do hook (0:00-0:30)** — O hook é o elemento mais crítico. Primeiros 5 segundos determinam se o visitante vai assistir. Escrever 3 opções de hook:
   - Hook de dor: Declaração que articula a dor de forma tão precisa que o espectador pensa "ele está falando de mim"
   - Hook de resultado: Uma promessa de resultado específico e crível logo de cara
   - Hook de curiosidade: Uma afirmação que gera pergunta imediata na mente do espectador
   Escolher o melhor para o ângulo principal; guardar outros para teste.

3. **Desenvolvimento do problema (0:30-1:30)** — Aprofundar o problema com:
   - Contextualização da situação atual do espectador
   - Identificação das tentativas fracassadas anteriores (e por que falharam)
   - Agitação emocional: consequências de não resolver o problema
   - "Você não está sozinho" — validar sem vitimizar

4. **Apresentação da solução (1:30-3:00)** — Introduzir o produto/serviço como a resposta:
   - Apresentação do mecanismo único: por que esta solução é diferente
   - Explicação do método em termos simples (sem jargão técnico)
   - Demonstração ou visual do produto em ação (roteiro para produção)
   - Conexão emocional: o que muda na vida do espectador

5. **Prova social (3:00-4:30)** — Construir credibilidade:
   - Apresentação de cases/depoimentos mais impactantes (específicos com números)
   - Credenciais do criador/empresa (contextualizado, não exibicionista)
   - Dados de mercado que validam a abordagem
   - Demonstração de resultado se possível (screenshot, gráfico, antes/depois)

6. **Apresentação da oferta (4:30-6:00)** — A revelação do que está sendo oferecido:
   - Descrição do produto/serviço principal com seus componentes
   - Stack de valor: listar cada componente com valor individual
   - Bônus (se aplicável): apresentar como surpresas positivas, não como enchimento
   - Valor total somado vs preço real — anchoring
   - Garantia: apresentar como eliminação total de risco, não como formalidade

7. **CTA e urgência (6:00-7:00)** — Fechar com clareza e urgência:
   - Instruções claras de ação (o que clicar, o que preencher)
   - Urgência legítima (vagas, prazo, bônus limitado — se real)
   - Resumo da transformação em 2-3 frases
   - CTA final com reforço do benefício principal

8. **Revisão de ritmo e legibilidade** — Contar palavras por segmento (150 palavras/min é ritmo natural de fala). Verificar transições, pausas e momentos de ênfase.

## Veto Conditions
- Script sem hook testado contra pelo menos 2 alternativas → produzir alternativas
- Promessas no VSL não sustentadas por provas disponíveis → adaptar promessas
- Duração calculada superior a 7 minutos para ticket abaixo de R$500 → cortar
- Ausência de urgência ou razão para agir agora → adicionar elemento legítimo
- Tom inconsistente entre seções (ex: início muito emocional, oferta muito fria) → revisar fluxo

## Output Esperado
Arquivo `vsl-script.md` contendo:
- Script completo com marcações de tempo por segmento
- 3 opções de hook (com o principal destacado)
- Notas de produção (o que mostrar em cada momento, tom de voz, ênfases)
- Indicações de onde inserir depoimentos em vídeo ou B-roll
- Contagem de palavras total e por segmento
- Checklist de produção para quem irá gravar

## Completion Criteria
- [ ] Duração-alvo definida e acordada
- [ ] Hook principal escrito + 2 alternativas testadas
- [ ] Segmento de problema com agitação emocional real
- [ ] Mecanismo único da solução explicado claramente
- [ ] Provas sociais roteirizadas com especificidade
- [ ] Stack de valor apresentado com anchoring de preço
- [ ] Garantia apresentada com eliminação de risco
- [ ] CTA claro com urgência legítima
- [ ] Contagem de palavras compatível com duração-alvo
- [ ] Notas de produção incluídas para cada segmento
- [ ] Arquivo `vsl-script.md` criado
