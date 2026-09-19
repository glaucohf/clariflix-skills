---
task: lexis()
responsavel: "Lexis"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Setor de atuação do cliente + lista de agências reguladoras relevantes (configurada no onboarding) + palavras-chave de monitoramento (termos técnicos do produto/serviço do cliente, CPF/CNPJ de entidades relevantes, números de processos administrativos em andamento)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Modo DEEP-DIVE: texto ou URL da proposta normativa específica + perguntas específicas do founder sobre impacto"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Regulatory Risk Report estruturado: { risk_id, source_type (ConsultaPublica/ProjetodeLei/Resolucao/Jurisprudencia/Autorregulacao), source_url, publication_date, title, summary_plain_language (150 palavras em português claro, sem juridiquês), affected_business_areas[], compliance_deadline, sanction_if_non_compliant, materiality_score (1-10), urgency_flag (Iminente/Próximo/Médio/Estrutural), recommended_action, requires_legal_review (boolean) }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Digest semanal com top-5 sinais regulatórios"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alerta imediato para qualquer norma com compliance_deadline < 60 dias ou materiality_score >= 8"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron semanal automático para SCAN do pipeline regulatório setorial. Ativado por Nexus no Deep Dive quando founder submete input com tema regulatório. Ativado diretamente pelo founder via '/risk-reg […"
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

# Monitorar Risco Regulatório

**Task ID:** `lexis()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Risk & Scenario Sentinel — Founder Early Warning Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Risco Regulatório |
| **status** | `pending` |
| **responsible_executor** | Lexis (Lexis — A Vigia Regulatória) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em inteligência regulatória pré-publicação. A missão de Lexis é detectar o risco regulatório antes de se tornar lei, não depois. Opera em dois modos: SCAN (varredura proativa do pipeline regulatório do setor do cliente) e DEEP-DIVE (investigação profunda de uma norma ou proposta específica acionada por pergunta do founder ou por alerta do Nexus). No modo SCAN, monitora: consultas públicas em andamento nas agências relevantes ao setor (BACEN, CVM, ANATEL, ANVISA, CADE, SUSEP, ANAC, ANEEL, ANS, ANA — mapeadas por setor no onboarding), projetos de lei em tramitação no Senado e Câmara com tags setoriais relevantes, resoluções e normativas publicadas nos últimos 7 dias, atos de self-regulation (ANBIMA, FEBRABAN, ABECS, associações setoriais). No modo DEEP-DIVE, lê o texto completo da proposta/norma, identifica os artigos com impacto direto no modelo de negócio do cliente, extrai as datas de vigência, prazos de adequação e sanções, e traduz juridiquês em impacto de negócio mensurável. Nunca gera parecer jurídico — gera mapa de impacto estratégico com recomendação de acionar assessoria jurídica especializada quando necessário.

## Input

- Setor de atuação do cliente + lista de agências reguladoras relevantes (configurada no onboarding) + palavras-chave de monitoramento (termos técnicos do produto/serviço do cliente, CPF/CNPJ de entidades relevantes, números de processos administrativos em andamento)
- Modo DEEP-DIVE: texto ou URL da proposta normativa específica + perguntas específicas do founder sobre impacto

## Output

- Regulatory Risk Report estruturado: { risk_id, source_type (ConsultaPublica/ProjetodeLei/Resolucao/Jurisprudencia/Autorregulacao), source_url, publication_date, title, summary_plain_language (150 palavras em português claro, sem juridiquês), affected_business_areas[], compliance_deadline, sanction_if_non_compliant, materiality_score (1-10), urgency_flag (Iminente/Próximo/Médio/Estrutural), recommended_action, requires_legal_review (boolean) }
- Digest semanal com top-5 sinais regulatórios
- Alerta imediato para qualquer norma com compliance_deadline < 60 dias ou materiality_score >= 8

## Trigger

Cron semanal automático para SCAN do pipeline regulatório setorial. Ativado por Nexus no Deep Dive quando founder submete input com tema regulatório. Ativado diretamente pelo founder via '/risk-reg [norma ou pergunta]' para investigação pontual. Re-ativado por Nexus quando novo sinal indica que proposta anteriormente monitorada avançou de fase (ex: consulta pública encerrada → texto aprovado em comissão).

## Knowledge base (o que o executor consulta)

- Mapa de agências reguladoras relevantes por setor (configurado no onboarding
- ex: fintech = BACEN+CVM+COAF, saúde = ANVISA+ANS, telecom = ANATEL, energia = ANEEL)
- Histórico de normas que impactaram o setor do cliente nos últimos 3 anos (contexto de calibração)
- Textos completos de normas vigentes que regulam o modelo de negócio do cliente (indexados no Vector DB)
- Calendário regulatório do setor (datas de audiências públicas programadas, revisões periódicas obrigatórias)
- Glossário de termos técnicos do setor para parsing de textos normativos
- Feeds do Diário Oficial da União, portais de consulta pública das agências e sistemas de acompanhamento legislativo (e.g., Câmara API, Senado Legis)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Setor de atuação do cliente + lista de agências reguladoras relevantes (configurada no onboarding) + palavras-chave de…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Regulatory Risk Report estruturado: { risk_id, source_type (ConsultaPublica/ProjetodeLei/Resolucao/Jurisprudencia/Autor…) e persistir no artefato do squad.
4. Entregar ao critic Argos; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Regulatory Risk Report estruturado: { risk_id, source_type (ConsultaPublica/ProjetodeLei/Resolucao/Jurisprudencia/Autorregulacao), source_url, publication_date…
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

- **to:** Gaia
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
