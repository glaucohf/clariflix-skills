---
task: aura()
responsavel: "Aura"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Schedule de envio preparado por Nexus para as proximas 24h (lista de toques com lead, canal, horario, copy renderizada)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "opt-out list e blacklist atualizadas"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "regras de compliance por canal e regiao"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "configuracao de limites de frequencia por lead por semana"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Channel Health Scores atuais (Pulsar)"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "calendario de campanhas ativas (para deteccao de sobreposicao)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Schedule Auditado com status por toque (APPROVED / BLOCKED / WARNING)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Lista de bloqueios com motivo especifico por toque (ex: 'Lead 4821"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "BLOCKED: opt-out em 2026-06-10 nao sincronizado com Instantly')"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Spot-check Report de qualidade de copy (% de toques com personalizacao incorreta, exemplos especificos)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Compliance Summary por batch (% aprovado, % bloqueado por motivo, flag de risco legal se > 0.1% de violations de compliance)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Nexus prepara cada batch de envio das proximas 24h (gate obrigatorio — Nexus nao executa sem aprovacao de Aura); Kronos solicita auditoria emergencial de campanha ativa; Pulsar dispara alerta de Chan…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aura 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao do Engagement Baseline Report ao final do Discovery — CMO/Head de Aquisicao valida os dados de baseline e confirma qual canal e sequencia sao foco prioritario antes de iniciar o modelo (L3, gate de entrada)"
    - "[ ] HITL: Ativacao da Sequencia Otimizada v1 redesenhada por Vega — time de SDR/Outreach revisa e aprova a nova distribuicao de toques antes de qualquer envio em producao (L3, gate de seguranca antes de go-live)"
    - "[ ] HITL: Qualquer campanha com audiencia > 500 contatos ou que envolva budget de ads — Nexus requer aprovacao manual antes de executar, independente do nivel de automacao configurado (L3, por volume e irreversibilidade)"
    - "[ ] HITL: Quando Channel Health Score de qualquer canal cai abaixo de 50 — Aura bloqueia o canal e Kronos escala para decisao humana sobre pausa, reducao de frequencia ou investigacao de causa raiz (L3, saude de canal critica)"
    - "[ ] HITL: Promocao de modelo candidato de Helios para producao — uplift confirmado no A/B test e condição necessaria mas nao suficiente; Head de Aquisicao aprova a troca de modelo que afeta toda a base (L3, decisao de alto impacto)"
---

# Verificar Compliance E Qualidade

**Task ID:** `aura()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Intelligent Timing Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Compliance E Qualidade |
| **status** | `pending` |
| **responsible_executor** | Aura (Aura — Critic & Compliance Verifier) |
| **execution_type** | `Hybrid` |
| **input** | 6 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gate de qualidade e compliance antes de qualquer batch de envio. Aura opera como um inspetor imparcial: recebe o schedule preparado por Nexus e audita cada toque antes da execucao. Verificacoes obrigatorias: (1) o lead esta em opt-out ou blacklist? (2) o horario de envio respeita as restricoes legais do canal e regiao (ex: nao enviar WhatsApp depois das 21h no Brasil)? (3) a frequencia total de toques na semana para este lead esta dentro do limite configurado? (4) o Canal Health Score do canal esta acima do threshold minimo de uso (padrao: > 50)? (5) existe sobreposicao de toques de outras campanhas ativas para o mesmo lead no mesmo dia? Qualquer violacao bloqueia o toque e reporta para Kronos. Adicionalmente, Aura executa spot-checks de qualidade de copy (amostra de 5-10% do batch) para detectar personalizacao incorreta ({nome} nao substituido, dados de enriquecimento errados no corpo da mensagem).

## Input

- Schedule de envio preparado por Nexus para as proximas 24h (lista de toques com lead, canal, horario, copy renderizada)
- opt-out list e blacklist atualizadas
- regras de compliance por canal e regiao
- configuracao de limites de frequencia por lead por semana
- Channel Health Scores atuais (Pulsar)
- calendario de campanhas ativas (para deteccao de sobreposicao)

## Output

- Schedule Auditado com status por toque (APPROVED / BLOCKED / WARNING)
- Lista de bloqueios com motivo especifico por toque (ex: 'Lead 4821
- BLOCKED: opt-out em 2026-06-10 nao sincronizado com Instantly')
- Spot-check Report de qualidade de copy (% de toques com personalizacao incorreta, exemplos especificos)
- Compliance Summary por batch (% aprovado, % bloqueado por motivo, flag de risco legal se > 0.1% de violations de compliance)

## Trigger

Nexus prepara cada batch de envio das proximas 24h (gate obrigatorio — Nexus nao executa sem aprovacao de Aura); Kronos solicita auditoria emergencial de campanha ativa; Pulsar dispara alerta de Channel Health Score critico (< 50) — Aura bloqueia novos toques naquele canal ate revisao humana; Job semanal de auditoria retroativa para detectar falhas de compliance nao detectadas em tempo real

## Knowledge base (o que o executor consulta)

- Regras de compliance por canal e regiao (LGPD, CAN-SPAM, GDPR, politicas do LinkedIn e WhatsApp Business), Opt-out e blacklist consolidada de todos os sistemas de envio (sincronizacao a cada 15 minutos), Limites de frequencia por canal configurados pelo time, Padroes de personalizacao incorreta conhecidos (lista de placeholders que frequentemente nao sao substituidos), Historico de violacoes anteriores para ajuste proativo de regras

## Action Items

1. Confirmar o gatilho e carregar a entrada (Schedule de envio preparado por Nexus para as proximas 24h (lista de toques com lead, canal, horario, copy renderizada)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Schedule Auditado com status por toque (APPROVED / BLOCKED / WARNING)) e persistir no artefato do squad.
4. Entregar ao critic Aura 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Schedule Auditado com status por toque (APPROVED / BLOCKED / WARNING)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aura 2 registrado
- [ ] Gate HITL respeitado: Aprovacao do Engagement Baseline Report ao final do Discovery — CMO/Head de Aquisicao valida os dados de baseline e confirma qual canal e s…
- [ ] Gate HITL respeitado: Ativacao da Sequencia Otimizada v1 redesenhada por Vega — time de SDR/Outreach revisa e aprova a nova distribuicao de toques antes de qualq…
- [ ] Gate HITL respeitado: Qualquer campanha com audiencia > 500 contatos ou que envolva budget de ads — Nexus requer aprovacao manual antes de executar, independente…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao do Engagement Baseline Report ao final do Discovery — CMO/Head de Aquisicao valida os dados de baseline e confirma qual canal e sequencia sao foco pr… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Ativacao da Sequencia Otimizada v1 redesenhada por Vega — time de SDR/Outreach revisa e aprova a nova distribuicao de toques antes de qualquer envio em produca… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Qualquer campanha com audiencia > 500 contatos ou que envolva budget de ads — Nexus requer aprovacao manual antes de executar, independente do nivel de automac… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Quando Channel Health Score de qualquer canal cai abaixo de 50 — Aura bloqueia o canal e Kronos escala para decisao humana sobre pausa, reducao de frequencia o… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Promocao de modelo candidato de Helios para producao — uplift confirmado no A/B test e condição necessaria mas nao suficiente; Head de Aquisicao aprova a troca… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Quando Aura detecta violacao de compliance legal (opt-out nao respeitado, envio fora de horario legal, campo LGPD violado) — independente de qualquer autonomia… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao trimestral de thresholds de timing e limites de frequencia — calibracao dos parametros do modelo com Sales Lead e CMO para alinhar com estrategia comer… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Aura 2 | BLOQUEIA entrega |

## Handoff

- **to:** Lumina
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
