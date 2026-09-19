---
task: calibrador()
responsavel: "CALIBRADOR"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Postmortem Reports do ORACLE (aprendizados acionaveis e recomendacoes de atualizacao), Knowledge Graph atual do founder (especialmente o sub-grafo de premissas e frameworks de decisao), Calibration Corpus atual (banco de premissas testadas), score de calibracao historico por tipo de decisao e tipo de premissa, aprovacao do founder para atualizacoes de corpus critico (L3 HITL obrigatorio)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Atualizacoes do Knowledge Graph do founder: (1) Novas entradas no Calibration Corpus (premissa X testada em N decisoes, taxa de acerto Y%, contexto de aplicabilidade Z)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Atualizacoes de premissas existentes com evidencia nova (framework W deve ser aplicado com multiplicador 1.4x em cenarios de alta incerteza"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "evidencia de 4 postmortems)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(3) Calibration Brief mensal"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "1 pagina executiva com: score de calibracao do mes, top 3 aprendizados, areas de melhora e areas de persistencia de vies"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(4) Recomendacoes para proximas sessoes de captura de conhecimento com o founder (gaps identificados entre o que o clone sabe e o que os postmortems revelaram)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo automatico pelo VERDICT apos cada Postmortem Report aprovado pelo ORACLE. Cron job mensal para geracao da Calibration Brief (primeiro dia util de cada mes). Disparo manual quando o founder ou…"
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

# Calibrar Julgamento

**Task ID:** `calibrador()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Decision Journal & Postmortem — Calibrador de Julgamento do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calibrar Julgamento |
| **status** | `pending` |
| **responsible_executor** | CALIBRADOR (CALIBRADOR — O Sintetizador do Clone) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker responsavel por fechar o loop entre postmortem e aprendizado do clone. Recebe os Postmortem Reports do ORACLE e traduz cada aprendizado em atualizacoes concretas do Knowledge Graph do founder — nao versoes generalizadas do que o founder 'costuma pensar', mas aprendizados especificos derivados de evidencia real: 'quando o founder superestima velocidade de ramp em contratacoes de vendas, o multiplicador correto historicamente e 1.8x o estimado'. Cria e atualiza o Calibration Corpus: banco de premissas testadas com seu historico de acerto/erro, nivel de confianca calibrado e contexto de aplicabilidade. Tambem gera a Calibration Brief mensal — relatorio executivo para o founder com: como seu julgamento esta evoluindo, em que tipos de decisao a calibracao melhorou, onde os vieses persistem e o que o clone aprendeu no mes. Toda atualizacao do corpus critico requer aprovacao do founder (L3) para garantir que o clone evolui com intencionalidade, nao ruido.

## Input

- Postmortem Reports do ORACLE (aprendizados acionaveis e recomendacoes de atualizacao), Knowledge Graph atual do founder (especialmente o sub-grafo de premissas e frameworks de decisao), Calibration Corpus atual (banco de premissas testadas), score de calibracao historico por tipo de decisao e tipo de premissa, aprovacao do founder para atualizacoes de corpus critico (L3 HITL obrigatorio)

## Output

- Atualizacoes do Knowledge Graph do founder: (1) Novas entradas no Calibration Corpus (premissa X testada em N decisoes, taxa de acerto Y%, contexto de aplicabilidade Z)
- (2) Atualizacoes de premissas existentes com evidencia nova (framework W deve ser aplicado com multiplicador 1.4x em cenarios de alta incerteza
- evidencia de 4 postmortems)
- (3) Calibration Brief mensal
- 1 pagina executiva com: score de calibracao do mes, top 3 aprendizados, areas de melhora e areas de persistencia de vies
- (4) Recomendacoes para proximas sessoes de captura de conhecimento com o founder (gaps identificados entre o que o clone sabe e o que os postmortems revelaram)
- Toda atualizacao do corpus persistida com timestamp e referencia ao postmortem de origem
- auditavel e reversivel

## Trigger

Disparo automatico pelo VERDICT apos cada Postmortem Report aprovado pelo ORACLE. Cron job mensal para geracao da Calibration Brief (primeiro dia util de cada mes). Disparo manual quando o founder ou VERDICT identificam padrao emergente que merece codificacao imediata no corpus. Atualizacoes de corpus critico dependem de aprovacao HITL do founder antes de persistir.

## Knowledge base (o que o executor consulta)

- Knowledge Graph completo do founder (especialmente sub-grafos de frameworks de decisao, principios de priorizacao e premissas recorrentes), Calibration Corpus atual (banco de premissas testadas com historico de acerto/erro), todos os Postmortem Reports produzidos pelo ORACLE (com referencia cruzada por tipo de decisao e tipo de premissa), score de calibracao historico (serie temporal por categoria), mapa de vieses cognitivos (atualizado a cada postmortem que confirma ou refuta um vies identificado)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Postmortem Reports do ORACLE (aprendizados acionaveis e recomendacoes de atualizacao), Knowledge Graph atual do founder…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Atualizacoes do Knowledge Graph do founder: (1) Novas entradas no Calibration Corpus (premissa X testada em N decisoes,…) e persistir no artefato do squad.
4. Entregar ao critic MIRROR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Atualizacoes do Knowledge Graph do founder: (1) Novas entradas no Calibration Corpus (premissa X testada em N decisoes, taxa de acerto Y%, contexto de aplicabi…
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

- **to:** SENTINEL-DJ
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
