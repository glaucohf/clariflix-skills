---
task: sentinelDj()
responsavel: "SENTINEL-DJ"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Toda nova Decision Journal Entry gerada pelo ARCHIVIST (antes de ser persistida no repositorio), log de edicoes do Notion database (para detectar alteracoes pos-persistencia), metricas de cobertura do journal (decisoes identificadas vs decisoes capturadas), relatorio de qualidade de premissas (vagas, sem criterio de validacao, sem alternativas documentadas)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Verificacao de integridade por entry: APROVADA / APROVADA COM RESSALVAS (premissa X precisa de refinamento"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "enviada de volta ao ARCHIVIST) / REJEITADA (criterio de validacao ausente, entrada incompleta critica)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alertas de violacao de imutabilidade (edicao retroativa detectada"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "notificacao imediata ao founder via canal de alta urgencia)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Relatorio semanal de cobertura: % de decisoes capturadas no periodo, decisoes identificadas mas nao capturadas (com sugestao de captura retroativa), score de qualidade medio das entries da semana"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Nenhuma entry entra no journal sem o SENTINEL-DJ aprovar"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Interceptacao automatica de TODA nova entry antes da persistencia — sem excecao, sem bypass. Monitoramento continuo do log de edicoes do Notion (webhook ou polling a cada hora) para detectar alteraco…"
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

# Verificar Integridade Temporal

**Task ID:** `sentinelDj()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Decision Journal & Postmortem — Calibrador de Julgamento do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Integridade Temporal |
| **status** | `pending` |
| **responsible_executor** | SENTINEL-DJ (SENTINEL-DJ — O Guardiao de Integridade do Journal) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de controle, governanca e qualidade do Decision Journal. Opera em duas dimensoes criticas: (1) Integridade temporal — verifica que nenhuma Decision Journal Entry foi editada pos-resultado (a imutabilidade pre-postmortem e a propriedade mais critica do sistema — sem ela, o founder inconscientemente revisa o que 'sempre pensou' e o calibracao e invalida); detecta qualquer tentativa de edicao retroativa e alerta o founder imediatamente; (2) Qualidade de captura — audita a completude e especificidade das entries: premissas vagas ('o mercado vai crescer') sao sinalizadas para refinamento pelo ARCHIVIST antes de serem aceitas no journal; premissas sem criterio de validacao observavel sao devolvidas; decisions sem alternativas documentadas sao flagadas. Tambem monitora a taxa de cobertura: % de decisoes de alto impacto que estao sendo capturadas vs passando sem registro, e alerta o VERDICT quando a taxa cai abaixo do threshold configurado. E o guardiao de que o sistema nao vire arquivo morto.

## Input

- Toda nova Decision Journal Entry gerada pelo ARCHIVIST (antes de ser persistida no repositorio), log de edicoes do Notion database (para detectar alteracoes pos-persistencia), metricas de cobertura do journal (decisoes identificadas vs decisoes capturadas), relatorio de qualidade de premissas (vagas, sem criterio de validacao, sem alternativas documentadas)

## Output

- Verificacao de integridade por entry: APROVADA / APROVADA COM RESSALVAS (premissa X precisa de refinamento
- enviada de volta ao ARCHIVIST) / REJEITADA (criterio de validacao ausente, entrada incompleta critica)
- Alertas de violacao de imutabilidade (edicao retroativa detectada
- notificacao imediata ao founder via canal de alta urgencia)
- Relatorio semanal de cobertura: % de decisoes capturadas no periodo, decisoes identificadas mas nao capturadas (com sugestao de captura retroativa), score de qualidade medio das entries da semana
- Nenhuma entry entra no journal sem o SENTINEL-DJ aprovar

## Trigger

Interceptacao automatica de TODA nova entry antes da persistencia — sem excecao, sem bypass. Monitoramento continuo do log de edicoes do Notion (webhook ou polling a cada hora) para detectar alteracoes pos-persistencia. Relatorio semanal de cobertura: toda sexta as 17h. Alerta imediato ao VERDICT e ao founder quando taxa de cobertura cai abaixo do threshold ou quando violacao de imutabilidade e detectada.

## Knowledge base (o que o executor consulta)

- Schema de qualidade de Decision Journal Entry (criterios minimos aceitaveis por campo: nivel de especificidade de premissa, obrigatoriedade de criterio de validacao, minimo de alternativas documentadas), log de todas as entries persistidas com hash de imutabilidade (para deteccao de alteracoes), thresholds de cobertura configurados (% minimo de decisoes de alto impacto capturadas por semana/mes), historico de alertas de qualidade (para detectar padroes de captura inadequada recorrentes e gerar treinamento para o ARCHIVIST)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Toda nova Decision Journal Entry gerada pelo ARCHIVIST (antes de ser persistida no repositorio), log de edicoes do Noti…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Verificacao de integridade por entry: APROVADA / APROVADA COM RESSALVAS (premissa X precisa de refinamento) e persistir no artefato do squad.
4. Entregar ao critic MIRROR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Verificacao de integridade por entry: APROVADA / APROVADA COM RESSALVAS (premissa X precisa de refinamento
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

- **to:** MIRROR
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
