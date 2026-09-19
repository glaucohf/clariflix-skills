---
task: workerDeHigieneDeCrm()
responsavel: "Worker de Higiene de CRM"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Acesso de leitura/escrita ao CRM via MCP + output do Argos (novos enriquecimentos) + relatório de leads órfãos (cron diário)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de higiene: {duplicatas_consolidadas: N, campos_preenchidos: N, leads_normalizados: N, leads_arquivados_órfãos: N, score_qualidade_dados: 0-100}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "campos atualizados diretamente no CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron diário (03:00 AM) para limpeza em batch; também acionado em tempo real quando Argos detecta possível duplicata"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Veredito 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro deploy; em produção, amostras aleatórias (10%) passam por revisão humana"
    - "[ ] L3: Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratamento especial"
    - "[ ] L3: Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente"
    - "[ ] L3: Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interface de configuração, com log de auditoria"
    - "[ ] L3: Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor designado"
---

# Consolidar Dados CRM

**Task ID:** `workerDeHigieneDeCrm()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Roteamento Inteligente de Leads

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Consolidar Dados CRM |
| **status** | `pending` |
| **responsible_executor** | Worker de Higiene de CRM (Mnemosyne (Worker de Higienê de CRM)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora continuamente a qualidade dos dados no CRM: detecta e consolida duplicatas geradas por múltiplas entradas do mesmo lead em canais diferentes, preenche campos vazios com dados do enriquecimento do Argos, normaliza formatação (telefones, nomes de empresa, setores), arquiva leads órfãos (sem atividade >30 dias sem roteamento) para fila de reativação, gera relatório semanal de qualidade de dados para o gestor.

## Input

- Acesso de leitura/escrita ao CRM via MCP + output do Argos (novos enriquecimentos) + relatório de leads órfãos (cron diário)

## Output

- Relatório de higiene: {duplicatas_consolidadas: N, campos_preenchidos: N, leads_normalizados: N, leads_arquivados_órfãos: N, score_qualidade_dados: 0-100}
- campos atualizados diretamente no CRM

## Trigger

Cron diário (03:00 AM) para limpeza em batch; também acionado em tempo real quando Argos detecta possível duplicata

## Knowledge base (o que o executor consulta)

- Regras de dedup do cliente (campos-chave, tolerância de similaridade), dicionário de normalização (sinônimos de empresa, formatação de CNPJ/telefone), política de arquivamento (SLA sem atividade por tier), histórico de merges anteriores

## Action Items

1. Confirmar o gatilho e carregar a entrada (Acesso de leitura/escrita ao CRM via MCP + output do Argos (novos enriquecimentos) + relatório de leads órfãos (cron di…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de higiene: {duplicatas_consolidadas: N, campos_preenchidos: N, leads_normalizados: N, leads_arquivados_órfão…) e persistir no artefato do squad.
4. Entregar ao critic Veredito 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de higiene: {duplicatas_consolidadas: N, campos_preenchidos: N, leads_normalizados: N, leads_arquivados_órfãos: N, score_qualidade_dados: 0-100}
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Veredito 2 registrado
- [ ] Gate L3 respeitado: Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização an…
- [ ] Gate L3 respeitado: Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurtu…
- [ ] Gate L3 respeitado: Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro depl… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratame… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interfac… | BLOQUEIA até decisão humana |
| VETO-005 | L3 — Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor desi… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão humana semanal do relatório de auditoria do Veredito para identificar vieses sistemáticos e calibrar o modelo de scoring | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Veredito 2 | BLOQUEIA entrega |

## Handoff

- **to:** Veredito
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
