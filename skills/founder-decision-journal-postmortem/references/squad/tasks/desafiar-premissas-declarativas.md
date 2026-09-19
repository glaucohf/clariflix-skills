---
task: skeptic()
responsavel: "SKEPTIC"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Decision Journal Entry completa (premissas declaradas, contexto, alternativas descartadas), mapa de vieses cognitivos do founder (calibrado no Deep Dive), request de benchmark setorial para o SCOUT se premissas requerem dados externos, tipo de decisao para selecionar framework de red-team adequado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Red-Team Report com: (1) Para cada premissa declarada: rating de solidez (SOLIDA / FRAGIL / CRITICA"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "requer mais validacao), evidencias contrarias encontradas, pergunta de desafio especifica"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Premissas implicitas NAO declaradas que tambem precisariam ser verdadeiras para a decisao ser correta"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "lista de 'premissas fantasma'"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Vieses cognitivos do founder ativados nesta decisao (com referencia ao corpus historico: 'em 3 decisoes similares anteriores, voce subestimou X')"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(4) Base rate do setor para decisoes analogas quando disponivel"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo automatico pelo VERDICT imediatamente apos nova Decision Journal Entry ser persistida pelo ARCHIVIST. Tambem acionado manualmente pelo founder para decisoes em curso que ainda nao passaram pe…"
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

# Desafiar Premissas Declarativas

**Task ID:** `skeptic()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Decision Journal & Postmortem — Calibrador de Julgamento do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Desafiar Premissas Declarativas |
| **status** | `pending` |
| **responsible_executor** | SKEPTIC (SKEPTIC — O Red-Team de Premissas) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 9 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de desafio estruturado de premissas. Imediatamente apos o ARCHIVIST fechar uma Decision Journal Entry, o SKEPTIC recebe as premissas declaradas e executa um red-team rigoroso: para cada premissa, busca evidencias contrárias, questiona a logica causal, identifica premissas implicitas nao declaradas que tambem precisariam ser verdadeiras, e aplica os vieses cognitivos mapeados do founder (corpus do Discovery) para sinalizar onde o julgamento pode estar distorcido. Nao decide pela decisao — desafia as premissas que a sustentam. Entrega o Red-Team Report ao founder ANTES do resultado, enquanto ainda ha possibilidade de ajuste. Tambem pesquisa base rates relevantes: qual a taxa historica de sucesso de decisoes analogas no setor? O founder esta otimizando contra os dados ou contra sua intuicao?

## Input

- Decision Journal Entry completa (premissas declaradas, contexto, alternativas descartadas), mapa de vieses cognitivos do founder (calibrado no Deep Dive), request de benchmark setorial para o SCOUT se premissas requerem dados externos, tipo de decisao para selecionar framework de red-team adequado

## Output

- Red-Team Report com: (1) Para cada premissa declarada: rating de solidez (SOLIDA / FRAGIL / CRITICA
- requer mais validacao), evidencias contrarias encontradas, pergunta de desafio especifica
- (2) Premissas implicitas NAO declaradas que tambem precisariam ser verdadeiras para a decisao ser correta
- lista de 'premissas fantasma'
- (3) Vieses cognitivos do founder ativados nesta decisao (com referencia ao corpus historico: 'em 3 decisoes similares anteriores, voce subestimou X')
- (4) Base rate do setor para decisoes analogas quando disponivel
- (5) Score de solidez agregado das premissas (0-10)
- (6) Recomendacao: PROSSEGUIR / PROSSEGUIR COM CAUTELA / REVISAR PREMISSA X ANTES DE EXECUTAR
- Report entregue ao founder via Slack com botao de resposta: 'Confirmar e fechar', 'Revisar premissa' ou 'Registrar discordancia com SKEPTIC'

## Trigger

Disparo automatico pelo VERDICT imediatamente apos nova Decision Journal Entry ser persistida pelo ARCHIVIST. Tambem acionado manualmente pelo founder para decisoes em curso que ainda nao passaram pelo processo formal. Prioridade ALTA para decisoes classificadas como ALTO IMPACTO + IRREVERSIVEL.

## Knowledge base (o que o executor consulta)

- Mapa de vieses cognitivos calibrado do founder (do Deep Dive
- otimismo em timelines? subestimacao de custo? excesso de confianca em premissas de mercado?), base de decisoes historicas do founder com outcomes conhecidos (para identificar padroes de erro recorrente), frameworks de red-team (pre-mortem de Gary Klein, inversao de Charlie Munger, 10/10/10 de Suzy Welch, Steel Man), base de benchmarks setoriais coletados pelo SCOUT (base rates de sucesso por tipo de decisao no setor do founder)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Decision Journal Entry completa (premissas declaradas, contexto, alternativas descartadas), mapa de vieses cognitivos d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Red-Team Report com: (1) Para cada premissa declarada: rating de solidez (SOLIDA / FRAGIL / CRITICA) e persistir no artefato do squad.
4. Entregar ao critic MIRROR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Red-Team Report com: (1) Para cada premissa declarada: rating de solidez (SOLIDA / FRAGIL / CRITICA
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

- **to:** SCOUT
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
