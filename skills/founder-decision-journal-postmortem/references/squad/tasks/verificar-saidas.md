---
task: mirrorVerificar()
responsavel: "MIRROR"
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
    - "[ ] L3: CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao explicita do founder antes de ser persistida — o clone nunca evolui seus principios nucleares sem consentimento explicito do dono do conhecimento"
    - "[ ] L3: ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e criada apos confirmacao do founder de que quer registrar — nenhum trigger automatico substitui a intencao explicita para eventos deste nivel"
    - "[ ] L3: SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar que revisou e decidiu prosseguir, ou que discorda do SKEPTIC com justificativa registrada — garante accountability do processo, nao apenas do resultado"
    - "[ ] L2: ORACLE ao gerar Postmortem Report de decisoes AMBÍGUAS (resultado nao conclusivo apos 180 dias): founder valida se tem mais dados contextuais que o ORACLE nao capturou antes do relatorio ser finalizado e enviado ao CALIBRADOR"
    - "[ ] L2: CALIBRADOR ao identificar padrao de vies persistente que implica mudanca estrutural no processo de decisao do founder (ex: 'voce sistematicamente subestima custo de integracao — recomendamos adicionar gate obrigatorio de validacao tecnica antes de fechar contratos acima de R$X'): founder aprova ou rejeita a mudanca de processo antes de ser codificada"
---

# Verificar Saídas do Decision Journal & Postmortem

**Task ID:** `mirrorVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Decision Journal & Postmortem — Calibrador de Julgamento do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Decision Journal & Postmortem |
| **status** | `pending` |
| **responsible_executor** | MIRROR (MIRROR — O Verificador de Calibracao e Anti-Viés) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

MIRROR — O Verificador de Calibracao e Anti-Viés — Critic/Verifier do squad especializado em duas funcoes criticas: (1) Verificacao de calibracao — antes de qualquer Postmortem Report ser entregue ao founder ou ao CALIBRADOR, o MIRROR audita se a analise do ORACLE esta separando corretamente processo de resultado (uma boa decisao com resultado ruim nao deve baixar o score de calibracao — este e o erro mais comum em postmortems nao rigorosos); verifica se o score de calibracao esta sendo calculado de forma consistente com os criterios definidos na fase Discovery; checa se o aprendizado gerado e especifico e acionavel ou generico e inutil; (2) Red-team do red-team — audita se o SKEPTIC esta genuinamente desafiando as premissas ou apenas validando as intuicoes do founder com uma fachada de ceticismo; detecta se o corpus de vieses esta sendo aplicado corretamente ou se o SKEPTIC esta sendo complacente. Tambem realiza auditoria mensal aleatoria de 20% das entries do journal para verificar aderencia aos criterios de qualidade do SENTINEL-DJ ao longo do tempo. Emite veredicto: VALIDO / VALIDO COM RESSALVAS (especificando o que precisa de ajuste) / INVALIDO (retorna ao agente com feedback detalhado antes de qualquer entrega ao founder).

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- O Verificador de Calibracao e Anti-Viés
- Critic/Verifier do squad especializado em duas funcoes criticas: (1) Verificacao de calibracao
- antes de qualquer Postmortem Report ser entregue ao founder ou ao CALIBRADOR, o MIRROR audita se a analise do ORACLE esta separando corretamente processo de resultado (uma boa decisao com resultado ruim nao deve baixar o score de calibracao
- este e o erro mais comum em postmortems nao rigorosos)
- verifica se o score de calibracao esta sendo calculado de forma consistente com os criterios definidos na fase Discovery
- checa se o aprendizado gerado e especifico e acionavel ou generico e inutil
- (2) Red-team do red-team
- audita se o SKEPTIC esta genuinamente desafiando as premissas ou apenas validando as intuicoes do founder com uma fachada de ceticismo
- detecta se o corpus de vieses esta sendo aplicado corretamente ou se o SKEPTIC esta sendo complacente
- Tambem realiza auditoria mensal aleatoria de 20% das entries do journal para verificar aderencia aos criterios de qualidade do SENTINEL-DJ ao longo do tempo
- Emite veredicto: VALIDO / VALIDO COM RESSALVAS (especificando o que precisa de ajuste) / INVALIDO (retorna ao agente com feedback detalhado antes de qualquer entrega ao founder)

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador VERDICT para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** VERDICT
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
