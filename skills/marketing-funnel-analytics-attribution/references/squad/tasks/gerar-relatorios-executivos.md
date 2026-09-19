---
task: oracle()
responsavel: "Oracle"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Outputs estruturados de Hermes (atribuição), Argus (anomalias do período), Cassandra (forecast), Lumen (UTM health), meta de pipeline do período e resultados reais (CRM), perguntas específicas do usuário/CEO/CMO que precisam ser respondidas no relatório"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatórios executivos em 3 formatos: (1) Executive Brief PDF/Notion"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "2 páginas com highlights, status do pipeline vs meta, top anomalias resolvidas/abertas, forecast e top-3 recomendações"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Marketing Ops Report"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "detalhamento por canal/campanha com atribuição multi-model e UTM health"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Finance Report"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "CAC por canal, LTV estimado, payback period, forecast com confidence interval"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Todo domingo as 20h (relatório semanal, após forecast da Cassandra); primeiro dia útil do mês (relatório mensal); quando Atlas recebe pedido explícito de relatório; quando anomalia P1 é resolvida (re…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Skeptic antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar ou corrigir antes do go-live. SLA: 30min para resposta, após isso o sistema notifica o gestor direto."
    - "[ ] L3: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor de media antes de execucao. O squad gera o racional completo, humano aprova ou rejeita com comentario."
    - "[ ] L3: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing de 5 linhas e aguarda confirmação de que foi visto (acknowledgment) antes de escalar para investigação automática mais profunda."
    - "[ ] L2: Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta. Previne drift de sensibilidade ao longo do tempo."
    - "[ ] L2: Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP de Marketing. Revisão trimestral."
---

# Gerar Relatórios Executivos

**Task ID:** `oracle()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Funnel Analytics & Attribution Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Relatórios Executivos |
| **status** | `pending` |
| **responsible_executor** | Oracle (Oracle — Agente de Relatório e Narrativa Executiva) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 7 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de síntese e comunicação. Recebe todos os outputs dos outros workers (atribuição do Hermes, anomalias do Argus, forecast da Cassandra, qualidade do Lumen) e gera relatórios executivos narrativos adaptados ao público: versão CEO/CMO (2 páginas, foco em ROI e decisões), versão time de marketing (detalhada, com dados por campanha), versão financeiro (foco em CAC, LTV, payback e forecast). Garante que toda narrativa seja baseada exclusivamente nos dados recebidos (não inventa números) e inclui recomendações priorizadas com impacto estimado.

## Input

- Outputs estruturados de Hermes (atribuição), Argus (anomalias do período), Cassandra (forecast), Lumen (UTM health), meta de pipeline do período e resultados reais (CRM), perguntas específicas do usuário/CEO/CMO que precisam ser respondidas no relatório

## Output

- Relatórios executivos em 3 formatos: (1) Executive Brief PDF/Notion
- 2 páginas com highlights, status do pipeline vs meta, top anomalias resolvidas/abertas, forecast e top-3 recomendações
- (2) Marketing Ops Report
- detalhamento por canal/campanha com atribuição multi-model e UTM health
- (3) Finance Report
- CAC por canal, LTV estimado, payback period, forecast com confidence interval
- Todos com data de geração e versionamento

## Trigger

Todo domingo as 20h (relatório semanal, após forecast da Cassandra); primeiro dia útil do mês (relatório mensal); quando Atlas recebe pedido explícito de relatório; quando anomalia P1 é resolvida (relatório de incidente automático); on-demand por pergunta em linguagem natural via interface de chat.

## Knowledge base (o que o executor consulta)

- Templates de relatório por audiência (CEO, CMO, Marketing Ops, Finance), histórico de relatórios anteriores (para contexto de tendências), glossário de métricas padronizadas da empresa, metas de pipeline e budget por período, benchmarks de performance por canal e indústria para contextualização

## Action Items

1. Confirmar o gatilho e carregar a entrada (Outputs estruturados de Hermes (atribuição), Argus (anomalias do período), Cassandra (forecast), Lumen (UTM health), me…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatórios executivos em 3 formatos: (1) Executive Brief PDF/Notion) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatórios executivos em 3 formatos: (1) Executive Brief PDF/Notion
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Skeptic registrado
- [ ] Gate L3 respeitado: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de cam…
- [ ] Gate L3 respeitado: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovaca…
- [ ] Gate L3 respeitado: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor d… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta.… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão de relatório executivo antes de envio ao board: Oracle gera, Skeptic valida, mas um humano (CMO ou analista sênior) faz leitura final antes de envio ao… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Skeptic | BLOQUEIA entrega |

## Handoff

- **to:** Skeptic
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
