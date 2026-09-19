---
task: argosVerificar()
responsavel: "Argos"
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
    - "[ ] HITL: INTAKE GATE — RISCO CRÍTICO (L3): Antes de disparar workers para investigação profunda, Nexus apresenta o Mapa de Exposição inicial ao founder quando o risco é classificado como Crítico (impacto estimado > R$200k ou impacto em licença/operação). O founder valida o escopo da investigação, confirma as agências e mercados a investigar, e aprova o nível de profundidade (scan rápido vs. deep dive). Para riscos Médios e Baixos, Nexus opera de forma autônoma sem gate obrigatório."
    - "[ ] HITL: RISCO EM MATERIALIZAÇÃO ATIVA — ALERTA CRÍTICO (L3): Quando Vela classifica um alerta como Crítico (risco está se materializando dentro da janela de resposta), o squad pausa toda recomendação de ação com impacto financeiro ou operacional e escalona para o founder com urgência máxima. O founder recebe: (a) o Evidence Report do Argos com fontes primárias que confirmam a materialização, (b) os cenários ativos de Chronos com janelas de resposta restantes, (c) as 3 ações prioritárias de Cipher. O founder deve responder com decisão explícita antes de qualquer ação ser executada."
    - "[ ] HITL: PREMISSA DE CENÁRIO INVERSAMENTE VALIDADA (L2): Quando Argos identifica que uma premissa central de um cenário ativo no Risk Register foi invalidada por nova evidência (ex: a norma que estava em consulta pública foi arquivada, alterando radicalmente o cenário regulatório), o squad notifica o founder com o impacto na matrix de cenários antes de atualizar o Risk Register. O founder confirma a revisão ou solicita novo ciclo de análise."
    - "[ ] HITL: BOARD/INVESTOR RISK UPDATE E COMUNICAÇÕES EXTERNAS (L3): Cipher nunca envia qualquer documento para audiência externa (board, conselheiros, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento produzido para audiência externa vai primeiro para Notion como draft com notificação Slack ao founder. Apenas após founder aprovar explicitamente (clique no botão 'Aprovar para envio' ou mensagem de aprovação no Slack) o envio é autorizado. Este gate é inviolável."
    - "[ ] HITL: CONFIGURAÇÃO DO ORÁCULO E CORPUS DO FOUNDER (L2): A configuração inicial do corpus do Oráculo (quais documentos, transcrições e decisões do founder são ingeridas) requer aprovação explícita item a item pelo founder. O founder define o que entra no corpus (controle de privacidade sobre decisões sensíveis) e o que fica fora. Atualizações mensais automáticas do corpus precisam de revisão semestral do founder para remoção de decisões desatualizadas."
---

# Verificar Saídas do Risk & Scenario Sentinel

**Task ID:** `argosVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Risk & Scenario Sentinel — Founder Early Warning Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Risk & Scenario Sentinel |
| **status** | `pending` |
| **responsible_executor** | Argos (Argos — O Verificador de Inteligência) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Argos — O Verificador de Inteligência — Argos é o agente critic/verifier do Sentinel. Executa verificação adversarial em quatro camadas antes que qualquer output chegue ao founder: (1) SOURCE VERIFICATION — cada claim dos workers (Lexis, Gaia, Chronos) deve ter link para fonte primária verificável (Diário Oficial, texto de lei, publicação de agência, paper econômico, release oficial). Claims sem fonte primária são marcados como 'unverified' e não podem aparecer no Risk Brief como fatos — apenas como hipóteses a verificar. (2) HALLUCINATION DETECTION — Argos verifica se as normas, eventos ou dados citados existem de fato, se as datas e números são precisos, e se o contexto não foi distorcido na sumarização. Qualquer hallucination confirmada bloqueia o output do worker correspondente e dispara retrabalho. (3) RELEVANCE FILTER — verifica se os riscos identificados são de fato materiais para o modelo de negócio específico do cliente ou se são ruído de mercado que vai poluir o Brief do founder. Remove falsos positivos. (4) BIAS CHECK — identifica se os workers estão gerando viés de confirmação (ignorando riscos que contradizem as crenças do founder, ou exagerando riscos que confirmam seus medos). O output de Argos é um Verification Report que acompanha cada Brief: claim-by-claim, com status (Verified/Unverified/Hallucination/Corrected), fonte primária e confiança. Apenas Briefs com taxa de verificação >= 85% dos claims materiais passam para síntese do Nexus.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- O Verificador de Inteligência
- Argos é o agente critic/verifier do Sentinel
- Executa verificação adversarial em quatro camadas antes que qualquer output chegue ao founder: (1) SOURCE VERIFICATION
- cada claim dos workers (Lexis, Gaia, Chronos) deve ter link para fonte primária verificável (Diário Oficial, texto de lei, publicação de agência, paper econômico, release oficial)
- Claims sem fonte primária são marcados como 'unverified' e não podem aparecer no Risk Brief como fatos
- apenas como hipóteses a verificar
- (2) HALLUCINATION DETECTION
- Argos verifica se as normas, eventos ou dados citados existem de fato, se as datas e números são precisos, e se o contexto não foi distorcido na sumarização
- Qualquer hallucination confirmada bloqueia o output do worker correspondente e dispara retrabalho
- (3) RELEVANCE FILTER
- verifica se os riscos identificados são de fato materiais para o modelo de negócio específico do cliente ou se são ruído de mercado que vai poluir o Brief do founder
- Remove falsos positivos
- (4) BIAS CHECK
- identifica se os workers estão gerando viés de confirmação (ignorando riscos que contradizem as crenças do founder, ou exagerando riscos que confirmam seus medos)
- O output de Argos é um Verification Report que acompanha cada Brief: claim-by-claim, com status (Verified/Unverified/Hallucination/Corrected), fonte primária e confiança
- Apenas Briefs com taxa de verificação >= 85% dos claims materiais passam para síntese do Nexus

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Nexus para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: INTAKE GATE — RISCO CRÍTICO (L3): Antes de disparar workers para investigação profunda, Nexus apresenta o Mapa de Exposição inicial ao foun…
- [ ] Gate HITL respeitado: RISCO EM MATERIALIZAÇÃO ATIVA — ALERTA CRÍTICO (L3): Quando Vela classifica um alerta como Crítico (risco está se materializando dentro da…
- [ ] Gate HITL respeitado: PREMISSA DE CENÁRIO INVERSAMENTE VALIDADA (L2): Quando Argos identifica que uma premissa central de um cenário ativo no Risk Register foi i…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — INTAKE GATE — RISCO CRÍTICO (L3): Antes de disparar workers para investigação profunda, Nexus apresenta o Mapa de Exposição inicial ao founder quando o risco é… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — RISCO EM MATERIALIZAÇÃO ATIVA — ALERTA CRÍTICO (L3): Quando Vela classifica um alerta como Crítico (risco está se materializando dentro da janela de resposta),… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — PREMISSA DE CENÁRIO INVERSAMENTE VALIDADA (L2): Quando Argos identifica que uma premissa central de um cenário ativo no Risk Register foi invalidada por nova e… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — BOARD/INVESTOR RISK UPDATE E COMUNICAÇÕES EXTERNAS (L3): Cipher nunca envia qualquer documento para audiência externa (board, conselheiros, investidores, parce… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — CONFIGURAÇÃO DO ORÁCULO E CORPUS DO FOUNDER (L2): A configuração inicial do corpus do Oráculo (quais documentos, transcrições e decisões do founder são ingerid… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — AJUSTE DE THRESHOLDS DE ALERTA (L2): Os thresholds de early-warning de Vela (o que configura Informativo vs. Atenção vs. Crítico para cada indicador) são confi… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argos | BLOQUEIA entrega |

## Handoff

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
