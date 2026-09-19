---
task: radar()
responsavel: "RADAR"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de decisoes abertas com premissas e criterios de validacao (do Decision Journal), metricas internas configuradas por decisao (quais dados monitorar"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "pipeline do CRM, metricas de produto, financeiro), fontes externas a rastrear por tipo de premissa, thresholds de alerta configurados (quando um sinal e relevante o suficiente para notificar)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Alertas de premissa com: (1) ID da decisao afetada, (2) Premissa especifica que o sinal impacta, (3) Descricao do sinal detectado com fonte e data, (4) Direcao do impacto: CONFIRMANDO ou REFUTANDO a premissa, (5) Grau de evidencia (FORTE / MODERADO / FRACO), (6) Recomendacao de acao (antecipar postmortem? coletar dado complementar? nenhuma acao"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "apenas registrar), (7) Link para a Decision Journal Entry afetada"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Relatorio semanal consolidado de status de todas as premissas abertas (por decisao: SINAIS POSITIVOS / SINAIS NEGATIVOS / SEM DADOS SUFICIENTES / POSTMORTEM RECOMENDADO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Monitoramento continuo via cron job a cada 24 horas para sinais externos (noticias, publicacoes, dados de mercado via EXA). Monitoramento de metricas internas via webhook do CRM/ClickUp/analytics (ac…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic MIRROR antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao explicita do founder antes de ser persistida — o clone nunca evolui seus principios nucleares sem consentimento explicito do dono do conhecimento"
    - "[ ] L3: ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e criada apos confirmacao do founder de que quer registrar — nenhum trigger automatico substitui a intencao explicita para eventos deste nivel"
    - "[ ] L3: SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar que revisou e decidiu prosseguir, ou que discorda do SKEPTIC com justificativa registrada — garante accountability do processo, nao apenas do resultado"
    - "[ ] L2: ORACLE ao gerar Postmortem Report de decisoes AMBÍGUAS (resultado nao conclusivo apos 180 dias): founder valida se tem mais dados contextuais que o ORACLE nao capturou antes do relatorio ser finalizado e enviado ao CALIBRADOR"
    - "[ ] L2: CALIBRADOR ao identificar padrao de vies persistente que implica mudanca estrutural no processo de decisao do founder (ex: 'voce sistematicamente subestima custo de integracao — recomendamos adicionar gate obrigatorio de validacao tecnica antes de fechar contratos acima de R$X'): founder aprova ou rejeita a mudanca de processo antes de ser codificada"
---

# Monitorar Premissas Decisões

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Decision Journal & Postmortem — Calibrador de Julgamento do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Premissas Decisões |
| **status** | `pending` |
| **responsible_executor** | RADAR (RADAR — O Monitor de Premissas em Tempo Real) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de monitoramento continuo das premissas de decisoes abertas. Cada Decision Journal Entry tem premissas com criterio de validacao observavel — o RADAR rastreia continuamente os sinais externos e internos que indicam se essas premissas estao se confirmando ou sendo refutadas ANTES da data formal de postmortem. Monitora tres categorias: (1) Sinais externos — dados de mercado, movimentos de concorrentes, regulacao, publicacoes setoriais que impactam as premissas; (2) Sinais internos — metricas operacionais do ClickUp/CRM/analytics que indicam performance da decisao (ex: decisao de contratar SDR X: monitorar pipeline gerado, taxa de conexao, custo por oportunidade); (3) Alertas de deadline — decisoes se aproximando da janela de postmortem sem sinais suficientes de resultado. Quando detecta sinal relevante, notifica o VERDICT com contexto: qual premissa, qual sinal, grau de impacto, recomendacao de acao (antecipar postmortem? coletar mais dados? notificar founder agora?). Evita alarme falso: cada notificacao passa por threshold de relevancia configurado.

## Input

- Lista de decisoes abertas com premissas e criterios de validacao (do Decision Journal), metricas internas configuradas por decisao (quais dados monitorar
- pipeline do CRM, metricas de produto, financeiro), fontes externas a rastrear por tipo de premissa, thresholds de alerta configurados (quando um sinal e relevante o suficiente para notificar)

## Output

- Alertas de premissa com: (1) ID da decisao afetada, (2) Premissa especifica que o sinal impacta, (3) Descricao do sinal detectado com fonte e data, (4) Direcao do impacto: CONFIRMANDO ou REFUTANDO a premissa, (5) Grau de evidencia (FORTE / MODERADO / FRACO), (6) Recomendacao de acao (antecipar postmortem? coletar dado complementar? nenhuma acao
- apenas registrar), (7) Link para a Decision Journal Entry afetada
- Relatorio semanal consolidado de status de todas as premissas abertas (por decisao: SINAIS POSITIVOS / SINAIS NEGATIVOS / SEM DADOS SUFICIENTES / POSTMORTEM RECOMENDADO)

## Trigger

Monitoramento continuo via cron job a cada 24 horas para sinais externos (noticias, publicacoes, dados de mercado via EXA). Monitoramento de metricas internas via webhook do CRM/ClickUp/analytics (aciona quando metrica configurada para uma decisao especifica sofre variacao acima do threshold). Alerta de deadline: 7 dias antes da janela de postmortem de qualquer decisao aberta, notifica VERDICT para preparar o ORACLE. Tambem acionado manualmente pelo founder quando percebe um resultado emergindo antes da data prevista.

## Knowledge base (o que o executor consulta)

- Decision Journal completo com premissas abertas e criterios de validacao por decisao, mapeamento de metricas internas por tipo de decisao (quais dados de CRM/ClickUp/analytics indicam resultado de cada categoria de decisao), fontes externas a monitorar por setor e tipo de premissa (configuradas no Discovery), historico de alertas anteriores para calibrar threshold e evitar fadiga de notificacao, EXA MCP para monitoramento de sinais externos em tempo real

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de decisoes abertas com premissas e criterios de validacao (do Decision Journal), metricas internas configuradas…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Alertas de premissa com: (1) ID da decisao afetada, (2) Premissa especifica que o sinal impacta, (3) Descricao do sinal…) e persistir no artefato do squad.
4. Entregar ao critic MIRROR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Alertas de premissa com: (1) ID da decisao afetada, (2) Premissa especifica que o sinal impacta, (3) Descricao do sinal detectado com fonte e data, (4) Direcao…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic MIRROR registrado
- [ ] Gate L3 respeitado: CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao ex…
- [ ] Gate L3 respeitado: ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e…
- [ ] Gate L3 respeitado: SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar q…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao explicita do founder a… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e criada apos confirm… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar que revisou e decidiu… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — ORACLE ao gerar Postmortem Report de decisoes AMBÍGUAS (resultado nao conclusivo apos 180 dias): founder valida se tem mais dados contextuais que o ORACLE nao… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — CALIBRADOR ao identificar padrao de vies persistente que implica mudanca estrutural no processo de decisao do founder (ex: 'voce sistematicamente subestima cus… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — RADAR ao detectar sinal de refutacao FORTE de premissa critica em decisao de alto impacto ANTES da janela de postmortem: notificacao imediata ao founder com su… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — Configuracao inicial de thresholds (Discovery): founder define pessoalmente os criterios de disparo automatico, as janelas de revisao por tipo de decisao e o n… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic MIRROR | BLOQUEIA entrega |

## Handoff

- **to:** ORACLE
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
