---
task: briefArchitect()
responsavel: "Brief Architect"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Contrato assinado com escopo de entregaveis (Contrato Maestro)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Dossiê completo do creator com analise de estilo, formatos de melhor performance e linguagem caracteristica (Radar Scout + Persona Fit Analyst)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Guia de marca do cliente (mensagens-chave, beneficios do produto, elementos obrigatorios, proibicoes de comunicacao, paleta visual, exemplos aprovados)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Objetivo especifico da campanha (awareness, consideracao, conversao) que determina o CTA e a estrutura do briefing"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Codigo de desconto unico e parametros de UTM gerados pelo sistema"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Briefing criativo estruturado em 7 secoes adaptado ao creator: (1) Contexto da Parceria"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "porque o creator foi escolhido (dados de fit especificos, mencao ao que o brand admira no conteudo dele), tom de parceria real nao corporativo"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Objetivo da Campanha"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "o que queremos que o publico FACA (nao apenas veja), metrica de sucesso da peca"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Mensagens-Chave"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "3 mensagens obrigatorias a transmitir, em linguagem simples, sem jargao corporativo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Curator imediatamente apos confirmacao de contrato assinado e codigo de desconto/UTM gerado. Re-trigger se creator solicitar ajuste no briefing (max 1 revisao autonoma pelo Brief Archite…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Parceiro Certo antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou R$5.000 dependendo do budget do cliente) bloqueia e notifica o gestor de marketing com proposta completa, score do creator e benchmarking de mercado para aprovacao antes de qualquer envio."
    - "[ ] HITL: Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evidencias coletadas para decisao humana de vetamento ou aprovacao com risco consciente — nunca o squad decide sozinho sobre risco de reputacao da marca."
    - "[ ] HITL: Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #publi) ou representacao incorreta do produto que requer revisao do time juridico ou de marketing antes de qualquer resposta ao creator."
    - "[ ] HITL: ROAS Tracker detecta ROAS >= 5x em D+7: alerta de oportunidade imediato ao gestor de marketing e ao time de performance para decisao de amplificacao via ads pagos do post do creator — decisao de investimento adicional e sempre humana."
    - "[ ] HITL: ROAS Tracker detecta ROAS < 0.5x em D+14: alerta ao gestor de marketing para revisao da estrategia de creator daquele nicho ou campanha — pode indicar desalinhamento de ICP ou problema de produto que nao deve ser escondido por mais investimento."
---

# Gerar Briefing Criativo Personalizado

**Task ID:** `briefArchitect()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Influencer & Creator Outreach Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Briefing Criativo Personalizado |
| **status** | `pending` |
| **responsible_executor** | Brief Architect (Brief Architect — O Criador de Briefings) |
| **execution_type** | `Agent` |
| **input** | 5 item(ns) |
| **output** | 15 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gera o briefing criativo personalizado para cada creator ativado, adaptando o objetivo da campanha, as mensagens-chave e as diretrizes de conteudo ao estilo autentico e a linguagem do creator especifico — sem engessar a criatividade, que e o ativo do creator. Usa o dossiê do creator para identificar o formato que mais performa no perfil dele (Reels vs Stories vs carrossel vs TikTok), o tom que usa naturalmente e os elementos visuais da sua estetica. Gera a estrutura de rastreabilidade obrigatoria: UTM unico, codigo de desconto exclusivo do creator, instrucoes de CTA. O briefing e uma sugestao estruturada, nao um roteiro rigido — o Brief Architect define O QUE comunicar e QUAIS elementos rastrear, nao COMO o creator deve falar. Toda peca de briefing passa pelo Critic antes de ser enviada ao creator.

## Input

- Contrato assinado com escopo de entregaveis (Contrato Maestro)
- Dossiê completo do creator com analise de estilo, formatos de melhor performance e linguagem caracteristica (Radar Scout + Persona Fit Analyst)
- Guia de marca do cliente (mensagens-chave, beneficios do produto, elementos obrigatorios, proibicoes de comunicacao, paleta visual, exemplos aprovados)
- Objetivo especifico da campanha (awareness, consideracao, conversao) que determina o CTA e a estrutura do briefing
- Codigo de desconto unico e parametros de UTM gerados pelo sistema

## Output

- Briefing criativo estruturado em 7 secoes adaptado ao creator: (1) Contexto da Parceria
- porque o creator foi escolhido (dados de fit especificos, mencao ao que o brand admira no conteudo dele), tom de parceria real nao corporativo
- (2) Objetivo da Campanha
- o que queremos que o publico FACA (nao apenas veja), metrica de sucesso da peca
- (3) Mensagens-Chave
- 3 mensagens obrigatorias a transmitir, em linguagem simples, sem jargao corporativo
- (4) Liberdade Criativa
- o que o creator pode e deve adaptar ao proprio estilo, lista de formatos sugeridos com referencia a posts anteriores dele que tiveram alto engajamento
- (5) Elementos Obrigatorios
- elementos fixos de marca, texto legal de publicidade obrigatorio por lei (CONAR), link com UTM e codigo de desconto unicos
- (6) Especificacoes Tecnicas
- resolucao, duracao de video, numero de entregaveis, prazo de submissao para aprovacao, prazo de publicacao
- (7) Processo de Aprovacao
- quem aprova, prazo de revisao, quantas rodadas permitidas
- Formato Markdown legivel pelo creator + JSON estruturado para o Content Guardian acompanhar os entregaveis

## Trigger

Ativado pelo Curator imediatamente apos confirmacao de contrato assinado e codigo de desconto/UTM gerado. Re-trigger se creator solicitar ajuste no briefing (max 1 revisao autonoma pelo Brief Architect antes de escalar para time de marketing). Trigger de campanha especial: o Curator pode ativar o Brief Architect para criar uma versao especifica de briefing para datas sazonais (Black Friday, Natal, Dia das Maes) com diretivas especificas da campanha.

## Knowledge base (o que o executor consulta)

- Formatos de melhor performance por plataforma em 2025-2026: TikTok (15-30s para conversao, 60s para storytelling), Instagram Reels (7-15s para discovery, 30-60s para engajamento), Stories (3-5 slides com CTA no ultimo)
- Frameworks de briefing por objetivo: awareness (hook emocional + beneficio principal + CTA suave de seguir), consideracao (storytelling de problema-solucao + prova social + CTA de explorar), conversao (beneficio especifico + urgencia + CTA com codigo de desconto)
- Elementos de CONAR obrigatorios para publi pago no Brasil: uso visivel de #publi ou #publicidade nos primeiros 3 linhas de legenda ou sobreposicao em videos
- Tecnicas de personalizacao de briefing por categoria de creator: lifestyle (foco em rotina/contexto de uso), review/unboxing (foco em beneficios especificos e comparacao), humor (foco no problema de forma divertida sem engessar o formato)
- Templates de rastreabilidade: estrutura de UTM (utm_source=influencer&utm_medium=instagram&utm_campaign={campaign}&utm_content={creator_handle}) e instrucoes de geracao de codigos de desconto no e-commerce/CRM

## Action Items

1. Confirmar o gatilho e carregar a entrada (Contrato assinado com escopo de entregaveis (Contrato Maestro)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Briefing criativo estruturado em 7 secoes adaptado ao creator: (1) Contexto da Parceria) e persistir no artefato do squad.
4. Entregar ao critic Parceiro Certo; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Briefing criativo estruturado em 7 secoes adaptado ao creator: (1) Contexto da Parceria
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Parceiro Certo registrado
- [ ] Gate HITL respeitado: Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou…
- [ ] Gate HITL respeitado: Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evi…
- [ ] Gate HITL respeitado: Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #p…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou R$5.000 dependendo… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evidencias coletadas pa… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #publi) ou representac… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — ROAS Tracker detecta ROAS >= 5x em D+7: alerta de oportunidade imediato ao gestor de marketing e ao time de performance para decisao de amplificacao via ads pa… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — ROAS Tracker detecta ROAS < 0.5x em D+14: alerta ao gestor de marketing para revisao da estrategia de creator daquele nicho ou campanha — pode indicar desalinh… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Creator solicita ajuste contratual apos assinatura (exclusividade, prazo, valor, direitos de imagem ampliados): qualquer renegociacao apos contrato assinado e… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Content Guardian nao recebe rascunho em D-1 do deadline: escalacao urgente ao time de marketing para decisao sobre extensao de prazo ou substituicao do creator… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Persona Fit Analyst detecta queda >= 25% no score medio de ROAS por categoria de creator em 2 ciclos consecutivos de campanha: alerta estrategico ao gestor de… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Parceiro Certo | BLOQUEIA entrega |

## Handoff

- **to:** Content Guardian
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
