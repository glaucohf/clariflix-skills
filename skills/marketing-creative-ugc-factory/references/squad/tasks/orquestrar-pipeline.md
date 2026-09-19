---
task: orionPipeline()
responsavel: "Orion"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Creative Performance Pack"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "entregável semanal automático gerado pelo Nexus e consolidado pelo Orion contendo: (1) Batch de Criativos Aprovados: lote de 30-50 variações aprovadas pelo Aegis com assets prontos para upload (imagens/vídeos + copy estruturada em JSON formatado para importação direta nas plataformas), (2) Preview Sheet Visual: mosaico de todos os assets da semana para revisão rápida do cliente, (3) Status do Banco de Criativos: dashboard de variações em teste / vencedoras / fatigadas / em produção (UGC pendente), (4) Relatório de Vencedores: criativos que atingiram significância estatística na semana com CTR, hook rate, ROAS e recomendação de escala, (5) ICP Brief do Próximo Ciclo: ângulos recomendados pela Stella para a wave seguinte com justificativa baseada em dados, (6) Log de Ações Auditável: todas as tasks executadas pelo squad no ClickUp com input, output e timestamps"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "prova de trabalho completa"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Formato: PDF executivo (para o cliente) + JSON estruturado (para integração com ferramentas de mídia) + ClickUp board atualizado"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central (Ópus lead) da fábrica de criativos. Recebe a meta de iteração (ex: '40 variações para campanha de aquisição Q3, foco em ângulo de dor e prova social para ICP financeiro'), decom…"
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

# Orquestrar Pipeline do Creative UGC Factory

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Creative UGC Factory

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Creative UGC Factory |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — Maestro de Criativos) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central (Ópus lead) da fábrica de criativos. Recebe a meta de iteração (ex: '40 variações para campanha de aquisição Q3, foco em ângulo de dor e prova social para ICP financeiro'), decompõe em sub-tarefas específicas para cada worker, sequencia a execução respeitando dependências (ICP research antes de brief, brief antes de copy, copy antes de critic gate), sintetiza o pacote de criativos aprovados e entrega ao Indexador para rastreamento. Monitora o estado de cada variação no ciclo de vida (briefing -> produção -> em_teste -> winner/arquivado) e dispara novos ciclos de produção quando o banco de criativos ativos cai abaixo do threshold de cobertura. Possui visibilidade completa de performance para priorizar os próximos ângulos a testar com base em dados — não em feeling.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Creative Performance Pack
- entregável semanal automático gerado pelo Nexus e consolidado pelo Orion contendo: (1) Batch de Criativos Aprovados: lote de 30-50 variações aprovadas pelo Aegis com assets prontos para upload (imagens/vídeos + copy estruturada em JSON formatado para importação direta nas plataformas), (2) Preview Sheet Visual: mosaico de todos os assets da semana para revisão rápida do cliente, (3) Status do Banco de Criativos: dashboard de variações em teste / vencedoras / fatigadas / em produção (UGC pendente), (4) Relatório de Vencedores: criativos que atingiram significância estatística na semana com CTR, hook rate, ROAS e recomendação de escala, (5) ICP Brief do Próximo Ciclo: ângulos recomendados pela Stella para a wave seguinte com justificativa baseada em dados, (6) Log de Ações Auditável: todas as tasks executadas pelo squad no ClickUp com input, output e timestamps
- prova de trabalho completa
- Formato: PDF executivo (para o cliente) + JSON estruturado (para integração com ferramentas de mídia) + ClickUp board atualizado

## Trigger

Orquestrador central (Ópus lead) da fábrica de criativos. Recebe a meta de iteração (ex: '40 variações para campanha de aquisição Q3, foco em ângulo de dor e prova social para ICP financeiro'), decompõe em sub-tarefas específicas para cada worker, sequencia a execução respeitando dependências (ICP research antes de brief, brief antes de copy, copy antes de critic gate), sintetiza o pacote de criativos aprovados e entrega ao Indexador para rastreamento. Monitora o estado de cada variação no ciclo de vida (briefing -> produção -> em_teste -> winner/arquivado) e dispara novos ciclos de produção quando o banco de criativos ativos cai abaixo do threshold de cobertura. Possui visibilidade completa de performance para priorizar os próximos ângulos a testar com base em dados — não em feeling.

## Knowledge base (o que o executor consulta)

- Meta Marketing API (MCP server)
- Nexus cria e gerencia ad sets para teste de criativos
- leitura de performance por variação para scoring
- Google Ads API (MCP server)
- Nexus réplica estrutura de teste no Google
- leitura de CTR/ROAS por criativo para o banco de dados
- Hoox / Insense API
- Hoox publica briefs de creator, monitora status de entrega, recebe vídeos entregues automaticamente
- ClickUp (MCP server)
- banco de criativos estruturado (board com todas as variações, status, scores, links de assets)
- toda ação do squad gera uma task auditável como prova de trabalho
- Slack (MCP server)
- gates L3 (aprovação de briefs de UGC, aprovação de escala de vencedores)
- canal de notificação de vencedores identificados e de baixo estoque no banco de criativos
- WhatsApp Business API
- canal alternativo para aprovações L3 urgentes fora do horário comercial
- Google Drive / Dropbox (MCP server)
- repositório de brand assets (logo, fontes, fotos de produto) acessado pelo Sigma para geração de static ads
- Canva API
- Sigma usa para geração programática de static ads com templates do cliente (quando o cliente usa Canva como ferramenta principal)
- HubSpot CRM (MCP server)
- Stella acessa dados de clientes convertidos para extrair perfil de ICP com precisão (cargo, setor, objeção principal no ciclo de vendas)
- Langfuse (observabilidade OTEL)
- rastreamento de todas as execuções de agentes, quality gates por fase (dev 70% / staging 85% / prod 95%), evals de qualidade de copy e de taxa de aprovação do Aegis
- Google Sheets
- dashboard compartilhado com o cliente: score de cada criativo, número de variações ativas, CTR por conceito, vencedores da semana, status do banco de criativos
- automações complementares: webhook de notificação quando vídeo UGC é entregue pelo creator, sincronização de metadados entre ClickUp e planilha de criativos, disparo de email/Slack ao gestor quando vencedor é identificado

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Aegis 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Creative Performance Pack
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

- **to:** Stella
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
