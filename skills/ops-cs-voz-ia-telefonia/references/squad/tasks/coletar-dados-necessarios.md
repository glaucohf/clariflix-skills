---
task: vivo()
responsavel: "Vivo"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal de 'dados insuficientes' do Maestro + intencao parcialmente classificada + transcricao do que o cliente ja disse + campos em falta para roteamento (ex: 'preciso de: numero_pedido') + historico de turns anteriores na sessao"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de dados coletados e validados: {intencao_confirmada, numero_pedido, cpf_cliente, nome_confirmado, descricao_problema_em_1_frase}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Audio TTS da pergunta de coleta enviado ao cliente"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Registro de cada turn de coleta no log de sessao"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Maximo 3 turns de coleta"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "se nao obtiver dados, sinaliza para escalonamento HITL"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro identifica confianca de intencao entre 0.55-0.75 (ambigua); dados obrigatorios ausentes para roteamento ao worker especializado; cliente respondeu de forma muito curta ou muito longa sem info…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Eco 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket prioritario antes de executar"
    - "[ ] HITL: Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona para humano"
    - "[ ] HITL: Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente para supervisor"
    - "[ ] HITL: Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana"
    - "[ ] HITL: Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especialista"
---

# Coletar Dados Necessários

**Task ID:** `vivo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz-IA para Atendimento Telefônico (PT-BR)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Coletar Dados Necessários |
| **status** | `pending` |
| **responsible_executor** | Vivo (Vivo — Worker de Dialogo & Coleta de Dados) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerencia o fluxo conversacional quando o Maestro identifica que ha dados insuficientes para resolucao (cliente nao forneceu numero do pedido, CPF nao reconhecido, intencao ambigua). Conduz um dialogo curto e diretivo em PT-BR coloquial para coletar os dados necessarios, valida os dados coletados (formato de CPF, existencia do pedido no ERP), confirma o entendimento da necessidade do cliente em uma frase, e devolve o pacote de dados completo para o Maestro redirecionar ao worker especializado correto. Especializado em lidar com clientes agitados: usa tecnica de validacao emocional antes de pedir dados ('Entendo sua frustração, vou te ajudar agora. Pode me passar o numero do pedido?').

## Input

- Sinal de 'dados insuficientes' do Maestro + intencao parcialmente classificada + transcricao do que o cliente ja disse + campos em falta para roteamento (ex: 'preciso de: numero_pedido') + historico de turns anteriores na sessao

## Output

- Pacote de dados coletados e validados: {intencao_confirmada, numero_pedido, cpf_cliente, nome_confirmado, descricao_problema_em_1_frase}
- Audio TTS da pergunta de coleta enviado ao cliente
- Registro de cada turn de coleta no log de sessao
- Maximo 3 turns de coleta
- se nao obtiver dados, sinaliza para escalonamento HITL

## Trigger

Maestro identifica confianca de intencao entre 0.55-0.75 (ambigua); dados obrigatorios ausentes para roteamento ao worker especializado; cliente respondeu de forma muito curta ou muito longa sem informar o dado solicitado; primeira turn de qualquer chamada nova quando o cliente nao se identificou

## Knowledge base (o que o executor consulta)

- Scripts de dialogo por intencao (arvore de decisao de perguntas x dados necessarios)
- Validadores de formato PT-BR (CPF/CNPJ, numero de pedido por regex de cada ERP integrado)
- Banco de frases de validacao emocional em PT-BR segmentadas por nivel de frustacao detectado
- Limites de turns por tipo de dado (max 2 tentativas por campo antes de pedir de outra forma)
- Historico de padroes de resposta vocal por tipo de cliente (clientes mais velhos falam mais devagar, clientes jovens usam mais girias)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sinal de 'dados insuficientes' do Maestro + intencao parcialmente classificada + transcricao do que o cliente ja disse…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de dados coletados e validados: {intencao_confirmada, numero_pedido, cpf_cliente, nome_confirmado, descricao_pro…) e persistir no artefato do squad.
4. Entregar ao critic Eco 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de dados coletados e validados: {intencao_confirmada, numero_pedido, cpf_cliente, nome_confirmado, descricao_problema_em_1_frase}
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Eco 2 registrado
- [ ] Gate HITL respeitado: Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3…
- [ ] Gate HITL respeitado: Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa fa…
- [ ] Gate HITL respeitado: Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz tra…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especiali… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Cliente VIP, Enterprise ou MRR > R$5k: toda acao irreversivel (cancelamento, mudanca de plano, refund parcial) requer aprovacao do CSM responsavel antes da exe… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Audio com duracao > 3 minutos e confianca media ASR < 0.82 — transcricao marcada para revisao humana antes do processamento completo pelo Maestro | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Intencao nao reconhecida apos 2 turns de coleta pelo Vivo (confianca < 0.55) — Hertz escalona com transcricao completa para o humano interpretar e resolver | BLOQUEIA até decisão humana |
| VETO-009 | HITL — Solicitacao de dados de terceiros, portabilidade de dados, ou qualquer direito LGPD em voz — Hertz bloqueia automacao e direciona para DPO/time juridico | BLOQUEIA até decisão humana |
| VETO-010 | Saída sem veredito do critic Eco 2 | BLOQUEIA entrega |

## Handoff

- **to:** Falco
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
