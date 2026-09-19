---
task: oracle()
responsavel: "ORACLE"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Decision Journal Entry completa da decisao a ser revisada (premissas, nivel de confianca, alternativas descartadas, criterio de sucesso), resultado observado ate o momento (metricas coletadas pelo RADAR + dados fornecidos pelo founder ou assistente), sinais e alertas do RADAR para esta decisao, benchmarks setoriais relevantes do SCOUT, historico de postmortems anteriores para analise de padroes"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Postmortem Report estruturado com: (1) Resumo executivo: decisao foi ACERTO / ERRO / AMBIGUA (cedo demais), score de calibracao agregado (0-10)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Analise premissa a premissa: estava correta? grau de acerto? o que foi subestimado ou superestimado? qual evidencia valida o resultado?"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) Analise de processo: a decisao foi boa independente do resultado? as alternativas descartadas foram corretamente descartadas?"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) Diagnostico de viés: qual vies cognitivo mais impactou esta decisao"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "confirmado ou refutado pelo resultado?"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(5) Score de calibracao historico atualizado: como esta decisao afeta o perfil de calibracao do founder (por tipo de decisao, por tipo de premissa)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo automatico pelo VERDICT nas janelas de revisao configuradas (cron job verificando diariamente decisoes que atingiram 30/90/180 dias). Disparo antecipado quando o RADAR sinaliza resultado emer…"
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

# Analisar Decisões Postmortem

**Task ID:** `oracle()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Decision Journal & Postmortem — Calibrador de Julgamento do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Decisões Postmortem |
| **status** | `pending` |
| **responsible_executor** | ORACLE (ORACLE — O Analista de Postmortem) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 10 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de analise de postmortem estruturado. Nas janelas configuradas (30, 90, 180 dias) ou quando o RADAR sinaliza resultado emergente, o ORACLE conduz o postmortem de uma decisao: compara sistematicamente cada premissa declarada no momento da decisao com o resultado observado, calcula o score de calibracao por premissa e agregado, identifica o que o founder estava certo, onde errou e com que grau de confianca cada erro ou acerto pode ser atribuido. Diferencia entre 'decisao boa com resultado ruim' (azar) e 'decisao ruim com resultado bom' (sorte) — a calibracao do julgamento exige essa separacao. Gera o Postmortem Report com aprendizados acionaveis e recomendacoes de atualizacao do corpus do clone. Tambem identifica padroes entre decisoes: os erros de calibracao estao concentrados em algum tipo de decisao? em algum tipo de premissa? em alguma fase do ciclo da empresa?

## Input

- Decision Journal Entry completa da decisao a ser revisada (premissas, nivel de confianca, alternativas descartadas, criterio de sucesso), resultado observado ate o momento (metricas coletadas pelo RADAR + dados fornecidos pelo founder ou assistente), sinais e alertas do RADAR para esta decisao, benchmarks setoriais relevantes do SCOUT, historico de postmortems anteriores para analise de padroes

## Output

- Postmortem Report estruturado com: (1) Resumo executivo: decisao foi ACERTO / ERRO / AMBIGUA (cedo demais), score de calibracao agregado (0-10)
- (2) Analise premissa a premissa: estava correta? grau de acerto? o que foi subestimado ou superestimado? qual evidencia valida o resultado?
- (3) Analise de processo: a decisao foi boa independente do resultado? as alternativas descartadas foram corretamente descartadas?
- (4) Diagnostico de viés: qual vies cognitivo mais impactou esta decisao
- confirmado ou refutado pelo resultado?
- (5) Score de calibracao historico atualizado: como esta decisao afeta o perfil de calibracao do founder (por tipo de decisao, por tipo de premissa)
- (6) Aprendizados acionaveis
- 3 a 5 bullet points especificos e verificaveis
- (7) Recomendacoes para o CALIBRADOR: quais premissas recorrentes devem ser atualizadas no corpus do clone com base neste postmortem
- Postmortem registrado no Notion vinculado a Decision Journal Entry original (campo separado, imutabilidade da entry preservada)

## Trigger

Disparo automatico pelo VERDICT nas janelas de revisao configuradas (cron job verificando diariamente decisoes que atingiram 30/90/180 dias). Disparo antecipado quando o RADAR sinaliza resultado emergente com evidencia FORTE antes da janela formal. Disparo manual pelo founder quando tem clareza do resultado antes da data prevista. Prioridade ALTA para decisoes classificadas como ALTO IMPACTO cujo postmortem esta em atraso.

## Knowledge base (o que o executor consulta)

- Decision Journal completo com todas as entries e seus metadados imutaveis, historico de postmortems anteriores (para analise de padroes de calibracao), mapa de vieses cognitivos do founder (atualizado iterativamente), benchmarks setoriais do SCOUT (para contextualizar resultado vs base rate), metricas internas coletadas pelo RADAR, frameworks de analise de decisao sob incerteza (Annie Duke
- Thinking in Bets, separacao de processo vs resultado), score de calibracao historico do founder por tipo de decisao

## Action Items

1. Confirmar o gatilho e carregar a entrada (Decision Journal Entry completa da decisao a ser revisada (premissas, nivel de confianca, alternativas descartadas, cri…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Postmortem Report estruturado com: (1) Resumo executivo: decisao foi ACERTO / ERRO / AMBIGUA (cedo demais), score de ca…) e persistir no artefato do squad.
4. Entregar ao critic MIRROR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Postmortem Report estruturado com: (1) Resumo executivo: decisao foi ACERTO / ERRO / AMBIGUA (cedo demais), score de calibracao agregado (0-10)
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

- **to:** CALIBRADOR
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
