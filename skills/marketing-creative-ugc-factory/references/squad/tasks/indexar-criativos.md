---
task: nexus()
responsavel: "Nexus"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Assets aprovados pelo Aegis (pacote completo: visual + copy + metadados do conceito) + Estrutura de campanhas existente nas plataformas (para criar os ad sets no lugar certo) + Parâmetros de teste configurados (budget de teste por variação, duração mínima antes de leitura de performance, threshold de impressões para significância) + Acesso às APIs de plataforma (Meta Marketing API, Google Ads API) + Regras de naming convention para ads (para rastreamento consistente)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Banco de criativos atualizado (planilha/ClickUp board): status de cada variacao (em_teste / vencedor / fatigado / arquivado / pendente_producao), métricas de performance acumuladas por variacao, data de ativação e desativação"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Estrutura de ad sets criados nas plataformas com naming convention correto"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Relatório de status semanal de testes: quais variacoes passaram da significancia estatistica, quais sao os vencedores preliminares, quais estao underperforming e devem ser pausados"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Alertas ao Orion quando vencedor é identificado (para escala) e quando banco de criativos ativos cai abaixo do threshold (para novo ciclo de produção)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado automaticamente quando Aegis aprova um lote de criativos (indexação e criação de ad sets). Varredura diária de performance automática às 09h para atualizar scores e identificar vencedores/fa…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aegis 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do squad operar — sem essa base o Aegis não tem referência para validar, e o squad não ativa"
    - "[ ] HITL: Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento ao creator) — o Hoox gera o brief e aguarda aprovação explícita do humano responsável via Slack/WhatsApp antes de publicar. O cliente vê o brief completo, o perfil de creator selecionado e o custo estimado"
    - "[ ] HITL: Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados anteriormente, o responsavel de midia revisa o preview antes da ativacao — as primeiras impressoes de um criativo novo sao irreversiveis"
    - "[ ] HITL: Gate L3 — Escala de criativo vencedor acima de threshold de budget: quando o Nexus identifica um vencedor e o Orion recomenda escala (aumento de budget > X% acima do threshold pre-definido), o humano aprova o aumento antes da execução pelo squad de media buying (ou pelo cliente diretamente)"
    - "[ ] HITL: Aprovação do ICP Creative Brief (apos cada ciclo da Stella): o cliente valida o mapa de dores/ângulos proposto pela Stella antes do Vega começar a conceitualização — garante que os insights estão corretos e alinhados com o momento estratégico da empresa"
---

# Indexar Criativos

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Creative UGC Factory

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Indexar Criativos |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — Creative Indexer & Tester) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de gestão do banco de criativos e estruturacao dos testes. Recebe todos os assets aprovados pelo Aegis (copy + visual + video UGC), organiza no banco de criativos com metadados completos, cria a estrutura de ad sets no Meta/Google para teste sistematico (cada variacao em seu proprio ad set isolado para leitura limpa de performance), monitora a coleta de dados de cada variacao ate atingir significancia estatistica, identifica o criativo vencedor e aciona o Orion para escala. Tambem é responsavel por arquivar criativos fatigados e manter o banco com mix saudável de criativos em teste / em escala / em standby.

## Input

- Assets aprovados pelo Aegis (pacote completo: visual + copy + metadados do conceito) + Estrutura de campanhas existente nas plataformas (para criar os ad sets no lugar certo) + Parâmetros de teste configurados (budget de teste por variação, duração mínima antes de leitura de performance, threshold de impressões para significância) + Acesso às APIs de plataforma (Meta Marketing API, Google Ads API) + Regras de naming convention para ads (para rastreamento consistente)

## Output

- Banco de criativos atualizado (planilha/ClickUp board): status de cada variacao (em_teste / vencedor / fatigado / arquivado / pendente_producao), métricas de performance acumuladas por variacao, data de ativação e desativação
- Estrutura de ad sets criados nas plataformas com naming convention correto
- Relatório de status semanal de testes: quais variacoes passaram da significancia estatistica, quais sao os vencedores preliminares, quais estao underperforming e devem ser pausados
- Alertas ao Orion quando vencedor é identificado (para escala) e quando banco de criativos ativos cai abaixo do threshold (para novo ciclo de produção)

## Trigger

Acionado automaticamente quando Aegis aprova um lote de criativos (indexação e criação de ad sets). Varredura diária de performance automática às 09h para atualizar scores e identificar vencedores/fatigados. Alerta ao Orion quando: (1) criativo vencedor identificado com >= 95% de confiança estatística, (2) banco de criativos ativos < 10 variações (threshold de reposição), (3) CTR médio das variações em teste cai > 20% vs semana anterior (sinal de saturação de audiência).

## Knowledge base (o que o executor consulta)

- Banco de criativos completo (todos os ativos históricos com performance acumulada), Regras de significância estatística para declarar vencedor (volume mínimo de impressões, intervalo de confiança, duração mínima de teste), Estrutura completa das campanhas nas plataformas (hierarquia, objetivos, audiências), Naming convention de ads do cliente, Histórico de decay de performance por formato e audiência (para calibrar thresholds de arquivamento)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Assets aprovados pelo Aegis (pacote completo: visual + copy + metadados do conceito) + Estrutura de campanhas existente…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Banco de criativos atualizado (planilha/ClickUp board): status de cada variacao (em_teste / vencedor / fatigado / arqui…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Banco de criativos atualizado (planilha/ClickUp board): status de cada variacao (em_teste / vencedor / fatigado / arquivado / pendente_producao), métricas de p…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aegis 2 registrado
- [ ] Gate HITL respeitado: Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do…
- [ ] Gate HITL respeitado: Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento a…
- [ ] Gate HITL respeitado: Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do squad operar — sem e… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento ao creator) — o Hoox… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados anteriormente, o re… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate L3 — Escala de criativo vencedor acima de threshold de budget: quando o Nexus identifica um vencedor e o Orion recomenda escala (aumento de budget > X% ac… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação do ICP Creative Brief (apos cada ciclo da Stella): o cliente valida o mapa de dores/ângulos proposto pela Stella antes do Vega começar a conceitualiz… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão do Preview Sheet semanal (opcional, recomendado): o Sigma gera um mosaico visual de todos os assets da semana — o cliente pode revisar e vetar conceito… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibração mensal de thresholds: reunião de 30 minutos para revisar os thresholds de vencedor/arquivamento com base na performance real do mês — o squad opera… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Onboarding de novo creator no banco aprovado: qualquer creator novo (nao pre-validado) que va ser contratado pelo Hoox requer aprovacao do cliente antes de rec… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Aegis 2 | BLOQUEIA entrega |

## Handoff

- **to:** Aegis
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
