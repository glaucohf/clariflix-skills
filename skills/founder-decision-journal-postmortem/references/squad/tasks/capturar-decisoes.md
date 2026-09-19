---
task: archivist()
responsavel: "ARCHIVIST"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Trigger de nova decisao (manual pelo founder, automatico por threshold de impacto, ou deteccao em canal monitorado pelo VERDICT), contexto minimo disponivel (qual decisao, valor envolvido, urgencia), perfil do tipo de decisao (taxonomia definida no Discovery) para selecionar template correto de captura"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Decision Journal Entry estruturada com: (1) ID unico da decisao (DEC-AAAA-MM-NNN), (2) Metadados: data, tipo, impacto estimado, canal de captura, tempo ate deadline, (3) Contexto narrativo: problema, pressao, stakeholders, (4) Alternativas descartadas com justificativa, (5) Premissas declaradas numeradas com nivel de confianca por premissa, (6) Criterio de sucesso observavel e metrica de validacao, (7) Data de revisao agendada (30/90/180 dias), (8) Hash de imutabilidade do registro pre-resultado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Entry persistida no Notion (database estruturado) e task criada no ClickUp com status 'Aberta"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Aguardando Resultado'"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Trigger automatico por: (1) Valor financeiro acima do threshold configurado detectado em email/Slack/ClickUp, (2) Mudanca de headcount (contratacao ou desligamento acima de nivel X), (3) Novo contrat…"
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

# Capturar Decisões

**Task ID:** `archivist()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Decision Journal & Postmortem — Calibrador de Julgamento do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Capturar Decisões |
| **status** | `pending` |
| **responsible_executor** | ARCHIVIST (ARCHIVIST — O Capturador de Premissas) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de captura e estruturacao de journal entries. Quando uma nova decisao e identificada (por trigger automatico ou manual), conduz uma sessao de captura conversacional de 5-10 minutos com o founder via canal preferido (Slack/WhatsApp). Extrai e estrutura: contexto da decisao (problema que resolve, pressao temporal, stakeholders afetados), alternativas que foram descartadas e por que, premissas declaradas (o que precisa ser verdade para esta decisao ser correta), nivel de confianca do founder em cada premissa (ALTA / MEDIA / BAIXA), criterio de sucesso observavel (como saberemos em X dias se foi certa), e data prevista de revisao. Tambem executa captura retroativa de decisoes historicas identificadas na fase Discovery. Formata cada entrada no schema padrao do Decision Journal e persiste no Notion + ClickUp com timestamps imutaveis. A imutabilidade e critica: o registro do momento da decisao nunca pode ser editado pos-resultado — apenas o postmortem e adicionado como campo separado.

## Input

- Trigger de nova decisao (manual pelo founder, automatico por threshold de impacto, ou deteccao em canal monitorado pelo VERDICT), contexto minimo disponivel (qual decisao, valor envolvido, urgencia), perfil do tipo de decisao (taxonomia definida no Discovery) para selecionar template correto de captura

## Output

- Decision Journal Entry estruturada com: (1) ID unico da decisao (DEC-AAAA-MM-NNN), (2) Metadados: data, tipo, impacto estimado, canal de captura, tempo ate deadline, (3) Contexto narrativo: problema, pressao, stakeholders, (4) Alternativas descartadas com justificativa, (5) Premissas declaradas numeradas com nivel de confianca por premissa, (6) Criterio de sucesso observavel e metrica de validacao, (7) Data de revisao agendada (30/90/180 dias), (8) Hash de imutabilidade do registro pre-resultado
- Entry persistida no Notion (database estruturado) e task criada no ClickUp com status 'Aberta
- Aguardando Resultado'

## Trigger

Trigger automatico por: (1) Valor financeiro acima do threshold configurado detectado em email/Slack/ClickUp, (2) Mudanca de headcount (contratacao ou desligamento acima de nivel X), (3) Novo contrato ou parceria acima de valor Y, (4) Mudanca de produto ou posicionamento aprovada em reuniao, (5) Alerta do RADAR de decisao imminente nao registrada. Trigger manual: founder ou assistente executivo envia comando '@VERDICT nova decisao' em qualquer canal monitorado.

## Knowledge base (o que o executor consulta)

- Taxonomia de tipos de decisao do founder (definida no Discovery), templates de captura por tipo de decisao (com perguntas especificas calibradas para cada categoria
- ex: template de contratacao vs template de alocacao de capital vs template de posicionamento), perfil de premissas recorrentes do founder (para sugerir premissas implicitas que o founder costuma nao declarar explicitamente), historico de entries anteriores para evitar duplicatas, schema do Decision Journal (Notion database estruturado)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Trigger de nova decisao (manual pelo founder, automatico por threshold de impacto, ou deteccao em canal monitorado pelo…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Decision Journal Entry estruturada com: (1) ID unico da decisao (DEC-AAAA-MM-NNN), (2) Metadados: data, tipo, impacto e…) e persistir no artefato do squad.
4. Entregar ao critic MIRROR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Decision Journal Entry estruturada com: (1) ID unico da decisao (DEC-AAAA-MM-NNN), (2) Metadados: data, tipo, impacto estimado, canal de captura, tempo ate dea…
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

- **to:** SKEPTIC
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
