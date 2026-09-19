---
task: parceiroCertoVerificar()
responsavel: "Parceiro Certo"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Contrato Maestro: qualquer proposta comercial acima do threshold configurado no onboarding (ex: colaboracoes acima de R$3.000 ou R$5.000 dependendo do budget do cliente) bloqueia e notifica o gestor de marketing com proposta completa, score do creator e benchmarking de mercado para aprovacao antes de qualquer envio."
    - "[ ] HITL: Parceiro Certo retorna veredicto SINALIZAR em Camada 1: flag de risco reputacional ou de valores apresentado ao gestor de marketing com evidencias coletadas para decisao humana de vetamento ou aprovacao com risco consciente — nunca o squad decide sozinho sobre risco de reputacao da marca."
    - "[ ] HITL: Content Guardian veredicto BLOQUEAR_HITL: conteudo submetido pelo creator contem elemento de brand safety, compliance legal (ausencia de #publi) ou representacao incorreta do produto que requer revisao do time juridico ou de marketing antes de qualquer resposta ao creator."
    - "[ ] HITL: ROAS Tracker detecta ROAS >= 5x em D+7: alerta de oportunidade imediato ao gestor de marketing e ao time de performance para decisao de amplificacao via ads pagos do post do creator — decisao de investimento adicional e sempre humana."
    - "[ ] HITL: ROAS Tracker detecta ROAS < 0.5x em D+14: alerta ao gestor de marketing para revisao da estrategia de creator daquele nicho ou campanha — pode indicar desalinhamento de ICP ou problema de produto que nao deve ser escondido por mais investimento."
---

# Verificar Saídas do Influencer & Creator Outreach Agentico

**Task ID:** `parceiroCertoVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Influencer & Creator Outreach Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Influencer & Creator Outreach Agentico |
| **status** | `pending` |
| **responsible_executor** | Parceiro Certo (Parceiro Certo — O Guardiao de Fit e Reputacao) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Parceiro Certo — O Guardiao de Fit e Reputacao — Valida em duas camadas criticas todo o pipeline de creator outreach antes de acoes irreversiveis. CAMADA 1 — Fit Validation (antes de qualquer abordagem): verifica se o creator aprovado pelo Persona Fit Analyst atende a 6 criterios de brand safety nao capturados pelo score quantitativo: (1) Historico de polêmica ou cancel culture nos ultimos 12 meses — busca em Google News e redes sociais; (2) Alinhamento de valores: o creator defende posicionamentos incompativeis com os valores da marca (politico, religioso, estilo de vida)? (3) Concorrencia direta ativa: o creator tem contrato de exclusividade ou parceria recente com concorrente direto do cliente? (4) Qualidade real do engajamento: os comentarios sao genuinos (comunidade ativa) ou genericos (pods, bots)? (5) Historico de compliance com CONAR: o creator marca posts patrocinados corretamente ou tem historico de ocultar publicidade paga? (6) Consistencia da audiencia: a audiencia real do creator e compativel com o ICP ou e uma audiencia desconectada do produto? Veredicto Camada 1: APTO (segue para abordagem) / SINALIZAR (flag com risco especifico para revisao humana antes de prosseguir) / VETAR (descarte com razao documentada). CAMADA 2 — Communication Validation (antes de qualquer envio externo): valida cada mensagem de abordagem e briefing gerado pelo Brief Architect em 5 dimensoes: (1) Tom e linguagem: e autentico e personalizado ou soou corporativo/generico demais para o creator? (2) Proposta de valor mutua: o pitch deixa claro o beneficio para o creator, nao apenas para a marca? (3) Ausencia de promessas nao autorizadas: nenhum numero de vendas garantido, nenhum alcance prometido, nenhum benchmark nao verificado; (4) Elementos legais presentes: mencao a necessidade de #publi, clausula de uso de imagem para ads no briefing; (5) Rastreabilidade garantida: UTM e codigo de desconto estao presentes e corretos no briefing? Veredicto Camada 2: APROVADO (segue para envio/ativacao) / REESCREVER com instrucoes especificas (volta ao agente responsavel, max 1 ciclo automatico) / BLOQUEAR_HITL para casos de risco reputacional, compliance ou ambiguidade de intencao que exigem revisao do gestor de marketing antes de qualquer acao.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Parceiro Certo
- O Guardiao de Fit e Reputacao
- Valida em duas camadas criticas todo o pipeline de creator outreach antes de acoes irreversiveis
- Fit Validation (antes de qualquer abordagem): verifica se o creator aprovado pelo Persona Fit Analyst atende a 6 criterios de brand safety nao capturados pelo score quantitativo: (1) Historico de polêmica ou cancel culture nos ultimos 12 meses
- busca em Google News e redes sociais
- (2) Alinhamento de valores: o creator defende posicionamentos incompativeis com os valores da marca (politico, religioso, estilo de vida)? (3) Concorrencia direta ativa: o creator tem contrato de exclusividade ou parceria recente com concorrente direto do cliente? (4) Qualidade real do engajamento: os comentarios sao genuinos (comunidade ativa) ou genericos (pods, bots)? (5) Historico de compliance com CONAR: o creator marca posts patrocinados corretamente ou tem historico de ocultar publicidade paga? (6) Consistencia da audiencia: a audiencia real do creator e compativel com o ICP ou e uma audiencia desconectada do produto? Veredicto Camada 1: APTO (segue para abordagem) / SINALIZAR (flag com risco especifico para revisao humana antes de prosseguir) / VETAR (descarte com razao documentada)
- Communication Validation (antes de qualquer envio externo): valida cada mensagem de abordagem e briefing gerado pelo Brief Architect em 5 dimensoes: (1) Tom e linguagem: e autentico e personalizado ou soou corporativo/generico demais para o creator? (2) Proposta de valor mutua: o pitch deixa claro o beneficio para o creator, nao apenas para a marca? (3) Ausencia de promessas nao autorizadas: nenhum numero de vendas garantido, nenhum alcance prometido, nenhum benchmark nao verificado
- (4) Elementos legais presentes: mencao a necessidade de #publi, clausula de uso de imagem para ads no briefing
- (5) Rastreabilidade garantida: UTM e codigo de desconto estao presentes e corretos no briefing? Veredicto Camada 2: APROVADO (segue para envio/ativacao) / REESCREVER com instrucoes especificas (volta ao agente responsavel, max 1 ciclo automatico) / BLOQUEAR_HITL para casos de risco reputacional, compliance ou ambiguidade de intencao que exigem revisao do gestor de marketing antes de qualquer acao

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Curator para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Curator
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
