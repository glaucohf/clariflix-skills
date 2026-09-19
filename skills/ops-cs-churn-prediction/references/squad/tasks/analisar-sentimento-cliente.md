---
task: iris()
responsavel: "Iris"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto bruto de verbatims NPS + transcricoes de tickets + respostas de CSAT + emails de reclamacao coletados pelo Vega nos ultimos 30 dias para a conta, acompanhados de timestamps e canal de origem"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sentiment score normalizado (0-10) por conta com tendência (melhora/piora/estável vs período anterior), top-3 temas de insatisfação com exemplos de verbatim, flag de menção a concorrente (sim/não + concorrente citado), flag de intenção de cancelamento detectada em linguagem natural"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Persistido no Supabase e disponível para o Prism no cálculo da dimensão de Satisfação"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado diariamente pelo Orchestrator apos Vega concluir ingestao (processa novos verbatims das ultimas 24h); acionado em tempo real quando Vega detecta keyword de risco em texto de ticket ou email"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguardando Aprovação' antes de ativar o CSM com essa ação específica"
    - "[ ] HITL: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualquer contato"
    - "[ ] HITL: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analista de dados"
    - "[ ] HITL: Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo batch"
    - "[ ] HITL: Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar"
---

# Analisar Sentimento Cliente

**Task ID:** `iris()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Predição e Prevenção de Churn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Sentimento Cliente |
| **status** | `pending` |
| **responsible_executor** | Iris (Íris — Analista de Sentimento e Voz do Cliente) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em processar e interpretar sinais qualitativos de sentimento que o Vega coleta em formato bruto. Processa: verbatims de NPS (por que o cliente deu aquela nota), transcricoes de chamadas de suporte, respostas abertas de CSAT, emails de reclamacao, respostas de pesquisa de satisfacao. Aplica analise de sentimento PT-BR fine-tuned, identifica temas recorrentes (problema com feature X, falta de treinamento, expectativa nao atendida, comparacao com concorrente), e gera sentiment_score normalizado (0-10) com os 2-3 temas principais por conta. Detecta mencao de concorrentes e intenção explicita de cancelamento.

## Input

- Texto bruto de verbatims NPS + transcricoes de tickets + respostas de CSAT + emails de reclamacao coletados pelo Vega nos ultimos 30 dias para a conta, acompanhados de timestamps e canal de origem

## Output

- Sentiment score normalizado (0-10) por conta com tendência (melhora/piora/estável vs período anterior), top-3 temas de insatisfação com exemplos de verbatim, flag de menção a concorrente (sim/não + concorrente citado), flag de intenção de cancelamento detectada em linguagem natural
- Persistido no Supabase e disponível para o Prism no cálculo da dimensão de Satisfação

## Trigger

Acionado diariamente pelo Orchestrator apos Vega concluir ingestao (processa novos verbatims das ultimas 24h); acionado em tempo real quando Vega detecta keyword de risco em texto de ticket ou email

## Knowledge base (o que o executor consulta)

- Modelo de análise de sentimento PT-BR fine-tuned para linguagem B2B SaaS, taxonomia de temas de insatisfação por produto/segmento (construída no Deep Dive), lista de concorrentes e aliases (nomes informais como são referenciados pelos clientes), exemplos históricos de linguagem de cancelamento iminente para few-shot, dicionário de intensificadores PT-BR ('péssimo', 'horroroso', 'inaceitável' vs 'poderia melhorar')

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto bruto de verbatims NPS + transcricoes de tickets + respostas de CSAT + emails de reclamacao coletados pelo Vega n…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sentiment score normalizado (0-10) por conta com tendência (melhora/piora/estável vs período anterior), top-3 temas de…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sentiment score normalizado (0-10) por conta com tendência (melhora/piora/estável vs período anterior), top-3 temas de insatisfação com exemplos de verbatim, f…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cri…
- [ ] Gate HITL respeitado: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de…
- [ ] Gate HITL respeitado: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguarda… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualque… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analis… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo b… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Brief com conflito entre next-best-action do Mira e comprometimento prévio do CSM registrado no CRM — Argus detecta e eleva para revisão humana antes de criar… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Primeiro alerta de churn em conta que nunca teve nenhuma ação de CS registrada (conta 'orphan') — escalona para Head de CS para atribuição e onboarding de rela… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Critic Argus reprova brief por evidência insuficiente (score < 36/40) após 2 iterações de melhoria — escalona para analista humano revisar os dados de entrada… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Lumen
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
