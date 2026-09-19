---
task: oraculo()
responsavel: "Oráculo"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Risk & Scenario Brief completo do ciclo atual + corpus do founder (decisões estratégicas documentadas, princípios estratégicos explicitados no onboarding, frameworks favoritos identificados, posicionamentos anteriores em crises similares) + contexto de prioridades estratégicas do momento (OKRs atuais do founder, apostas em andamento, restrições de capital)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Modo on-demand: founder envia cenário específico e pergunta 'como você abordaria isso?'"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Expert Lens Report: { situation_framing (como o founder enquadraria este momento de risco dentro da narrativa estratégica maior), priority_risks_from_expert_perspective (quais 1-3 riscos o founder priorizaria dado seu modelo mental), strategic_response_recommendation (o que o founder faria nos próximos 30 dias"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "ação, não análise), frameworks_applied (quais frameworks foram usados no raciocínio"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "ex: '2nd-order thinking', 'Inversion', 'JTBD risk frame'), confidence_level (%), founder_voice_flag (se o output soa como o founder ou diverge"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "sinaliza para revisão humana) }"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Máximo 500 palavras"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Tom direto, na primeira pessoa do founder"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Nexus automaticamente após síntese do Risk & Scenario Brief quando corpus do founder está configurado e ativo. Ativado diretamente pelo founder via '/oracle [cenário ou pergunta]' para pe…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argos antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: INTAKE GATE — RISCO CRÍTICO (L3): Antes de disparar workers para investigação profunda, Nexus apresenta o Mapa de Exposição inicial ao founder quando o risco é classificado como Crítico (impacto estimado > R$200k ou impacto em licença/operação). O founder valida o escopo da investigação, confirma as agências e mercados a investigar, e aprova o nível de profundidade (scan rápido vs. deep dive). Para riscos Médios e Baixos, Nexus opera de forma autônoma sem gate obrigatório."
    - "[ ] HITL: RISCO EM MATERIALIZAÇÃO ATIVA — ALERTA CRÍTICO (L3): Quando Vela classifica um alerta como Crítico (risco está se materializando dentro da janela de resposta), o squad pausa toda recomendação de ação com impacto financeiro ou operacional e escalona para o founder com urgência máxima. O founder recebe: (a) o Evidence Report do Argos com fontes primárias que confirmam a materialização, (b) os cenários ativos de Chronos com janelas de resposta restantes, (c) as 3 ações prioritárias de Cipher. O founder deve responder com decisão explícita antes de qualquer ação ser executada."
    - "[ ] HITL: PREMISSA DE CENÁRIO INVERSAMENTE VALIDADA (L2): Quando Argos identifica que uma premissa central de um cenário ativo no Risk Register foi invalidada por nova evidência (ex: a norma que estava em consulta pública foi arquivada, alterando radicalmente o cenário regulatório), o squad notifica o founder com o impacto na matrix de cenários antes de atualizar o Risk Register. O founder confirma a revisão ou solicita novo ciclo de análise."
    - "[ ] HITL: BOARD/INVESTOR RISK UPDATE E COMUNICAÇÕES EXTERNAS (L3): Cipher nunca envia qualquer documento para audiência externa (board, conselheiros, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento produzido para audiência externa vai primeiro para Notion como draft com notificação Slack ao founder. Apenas após founder aprovar explicitamente (clique no botão 'Aprovar para envio' ou mensagem de aprovação no Slack) o envio é autorizado. Este gate é inviolável."
    - "[ ] HITL: CONFIGURAÇÃO DO ORÁCULO E CORPUS DO FOUNDER (L2): A configuração inicial do corpus do Oráculo (quais documentos, transcrições e decisões do founder são ingeridas) requer aprovação explícita item a item pelo founder. O founder define o que entra no corpus (controle de privacidade sobre decisões sensíveis) e o que fica fora. Atualizações mensais automáticas do corpus precisam de revisão semestral do founder para remoção de decisões desatualizadas."
---

# Interpretar Riscos Estratégicos

**Task ID:** `oraculo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Risk & Scenario Sentinel — Founder Early Warning Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Interpretar Riscos Estratégicos |
| **status** | `pending` |
| **responsible_executor** | Oráculo (Oráculo — O Clone Estratégico do Expert) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker que encarna o raciocínio estratégico e os frameworks do founder/expert sênior para contextualizar riscos dentro da lógica de negócio e prioridades específicas do cliente. Oráculo não pesquisa nem monitora — interpreta. Recebe o Risk & Scenario Brief sintetizado por Nexus e passa pelo filtro da visão de mundo, dos frameworks favoritos e das prioridades estratégicas do founder: 'dado este mapa de riscos, o que o founder faria agora, e por quê?'. Opera a partir de um corpus vivo: decisões anteriores documentadas, frameworks estratégicos preferidos do founder, posicionamentos históricos em crises regulatórias ou macro, e os princípios inegociáveis que o founder nunca viola. Produz a 'lente do expert' — uma interpretação da situação de risco na voz, na lógica e nos marcos de referência do próprio founder. Essencial para squads onde o founder tem um corpus estratégico rico e quer um clone que raciocina como ele. Em modo de consultoria Lendar[IA], Oráculo é configurado com o corpus do consultor/expert para entregar perspectiva de nível sênior ao cliente.

## Input

- Risk & Scenario Brief completo do ciclo atual + corpus do founder (decisões estratégicas documentadas, princípios estratégicos explicitados no onboarding, frameworks favoritos identificados, posicionamentos anteriores em crises similares) + contexto de prioridades estratégicas do momento (OKRs atuais do founder, apostas em andamento, restrições de capital)
- Modo on-demand: founder envia cenário específico e pergunta 'como você abordaria isso?'

## Output

- Expert Lens Report: { situation_framing (como o founder enquadraria este momento de risco dentro da narrativa estratégica maior), priority_risks_from_expert_perspective (quais 1-3 riscos o founder priorizaria dado seu modelo mental), strategic_response_recommendation (o que o founder faria nos próximos 30 dias
- ação, não análise), frameworks_applied (quais frameworks foram usados no raciocínio
- ex: '2nd-order thinking', 'Inversion', 'JTBD risk frame'), confidence_level (%), founder_voice_flag (se o output soa como o founder ou diverge
- sinaliza para revisão humana) }
- Máximo 500 palavras
- Tom direto, na primeira pessoa do founder

## Trigger

Ativado por Nexus automaticamente após síntese do Risk & Scenario Brief quando corpus do founder está configurado e ativo. Ativado diretamente pelo founder via '/oracle [cenário ou pergunta]' para perspectiva ad hoc. Requer HITL L1 — output sempre apresentado ao founder para validação antes de ser incorporado a qualquer comunicação externa. Não é ativado sem corpus configurado (fallback silencioso — Nexus entrega Brief sem Expert Lens e sinaliza que corpus não está disponível).

## Knowledge base (o que o executor consulta)

- Corpus vivo do founder: transcrições de reuniões estratégicas indexadas no Vector DB, memos de decisão anteriores, posicionamentos públicos (podcasts, artigos, entrevistas), frameworks estratégicos preferidos explicitados no onboarding, princípios inegociáveis documentados, histórico de apostas e seus racionais
- Atualizado continuamente via integração com Notion e Mem.ai (novas decisões são automaticamente ingeridas)
- Biblioteca de frameworks estratégicos (Inversion, Second-Order Thinking, Charlie Munger Mental Models, Clayton Christensen Disruption Theory, Roger Martin Playing to Win) para seleção contextual
- Corpus do consultor sênior Lendar[IA] como camada base onde corpus proprietário do founder ainda não está disponível

## Action Items

1. Confirmar o gatilho e carregar a entrada (Risk & Scenario Brief completo do ciclo atual + corpus do founder (decisões estratégicas documentadas, princípios estra…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Expert Lens Report: { situation_framing (como o founder enquadraria este momento de risco dentro da narrativa estratégi…) e persistir no artefato do squad.
4. Entregar ao critic Argos; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Expert Lens Report: { situation_framing (como o founder enquadraria este momento de risco dentro da narrativa estratégica maior), priority_risks_from_expert_pe…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argos registrado
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

- **to:** Cipher
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
