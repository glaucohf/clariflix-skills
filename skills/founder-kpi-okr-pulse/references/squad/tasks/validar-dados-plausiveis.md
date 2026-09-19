---
task: vera()
responsavel: "Véra"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Snapshot de coleta do Pulsar (com data_quality_flags) + diagnósticos de causa-raiz do Argo + thresholds de qualidade configurados (% máximo de dados FAILED que permite prosseguir, nível mínimo de confiança para diagnóstico sem HITL)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Snapshot validado com flags de qualidade atualizadas"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Diagnósticos auditados com anotação de confiança revisada"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Relatório de validação: { total_kpis, data_quality_ok, data_quality_partial, data_quality_failed, diagnoses_reviewed, diagnoses_approved, diagnoses_flagged_for_hitl, false_alarm_candidates }"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "GO/CONDITIONAL-GO/BLOCK para síntese"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado automaticamente em dois momentos: (1) após Pulsar concluir coleta, antes de Kalinda calcular desvios; (2) após Argo gerar diagnósticos, antes de Rex gerar recomendações. Pode ser invocado ad-…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Véra 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: DIAGNÓSTICO DE BAIXA CONFIANÇA (L3): Quando Véra classifica diagnóstico de causa-raiz como confiança Baixa e o KR associado tem peso estratégico Alto (ex: OKR de receita principal) — Argo retém a hipótese e Atlas notifica o founder: 'Detectei desvio em [KR] mas não tenho dados suficientes para confirmar a causa. Possível hipótese: [X]. Você pode me dar contexto adicional?' O founder responde e Argo reprocessa com o contexto fornecido."
    - "[ ] HITL: RECOMENDAÇÃO COM IMPACTO FINANCEIRO DIRETO (L3): Rex nunca cria task automática no ClickUp para recomendações classificadas como 'ação financeira' (ex: cancelar contrato, cortar budget de campanha, demitir fornecedor, alterar pricing) sem aprovação explícita do founder. Essas recomendações chegam como rascunho com flag APPROVAL_REQUIRED — founder aprova, rejeita ou modifica antes de qualquer task ser criada."
    - "[ ] HITL: ALERTA DE DADOS COMPROMETIDOS (L2→L3): Se Véra detectar que >30% dos KPIs de um OKR crítico vieram com data_quality_flag=FAILED (falha de integração, dado zerado, timeout), Atlas pausa o ciclo e envia alerta imediato: 'Pulse desta semana comprometido — [N] KPIs sem dados confiáveis de [sistema X]. Envio relatório parcial ou aguardo resolução?' Founder decide antes do relatório ser publicado."
    - "[ ] HITL: CLONE SIGMA PUBLICAÇÃO EXTERNA (L1→L3): Sigma pode gerar e entregar o Pulse no Slack e Notion de uso interno do founder sem aprovação. Se o founder solicitar versão do Pulse para compartilhar com time, board ou investidores — Sigma gera o draft mas entrega APENAS ao founder para revisão antes de qualquer distribuição externa."
    - "[ ] HITL: RECALIBRAÇÃO DE TARGET DE OKR (L2): Quando Kalinda detecta que um OKR está >120% da trajetória esperada por 2 semanas consecutivas (super-performance) ou que a tendência matemática torna o target inalcançável mesmo com ação corretiva — Atlas sinaliza ao founder para deliberar sobre recalibração de target. Nunca recalibra automaticamente. Founder decide em reunião de check-in mensal."
---

# Validar Dados Plausíveis

**Task ID:** `vera()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KPI/OKR Pulse — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Validar Dados Plausíveis |
| **status** | `pending` |
| **responsible_executor** | Véra (Véra — A Crítica de Dados) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente critic/verifier especializado em validação de diagnósticos e prevenção de falsos alarmes. Véra atua em duas camadas: (1) VALIDAÇÃO DE DADOS — antes do diagnóstico, verifica se os valores coletados pelo Pulsar são plausíveis (detecta outliers estáticos, dados de teste, duplicatas, erros de integração que gerariam desvio falso); (2) VALIDAÇÃO DE DIAGNÓSTICO — após Argo gerar hipótese de causa-raiz, verifica se a evidência quantitativa suporta a hipótese (lógica da chain of reasoning, consistência temporal, alternativa mais simples descartada). Marca hipóteses com confiança Baixa para revisão HITL antes de chegarem ao founder. Se taxa de dados com data_quality_flag=FAILED > 30% na coleta, bloqueia o Pulse e aciona alerta de dados comprometidos antes de qualquer análise.

## Input

- Snapshot de coleta do Pulsar (com data_quality_flags) + diagnósticos de causa-raiz do Argo + thresholds de qualidade configurados (% máximo de dados FAILED que permite prosseguir, nível mínimo de confiança para diagnóstico sem HITL)

## Output

- Snapshot validado com flags de qualidade atualizadas
- Diagnósticos auditados com anotação de confiança revisada
- Relatório de validação: { total_kpis, data_quality_ok, data_quality_partial, data_quality_failed, diagnoses_reviewed, diagnoses_approved, diagnoses_flagged_for_hitl, false_alarm_candidates }
- GO/CONDITIONAL-GO/BLOCK para síntese

## Trigger

Ativado automaticamente em dois momentos: (1) após Pulsar concluir coleta, antes de Kalinda calcular desvios; (2) após Argo gerar diagnósticos, antes de Rex gerar recomendações. Pode ser invocado ad-hoc: '/verify-data [kpi_name]' ou '/verify-diagnosis [kr_name]'.

## Knowledge base (o que o executor consulta)

- Histórico de valores dos KPIs dos últimos 12 meses (para detectar outliers estáticos)
- Regras de plausibilidade por KPI (ex: 'MRR não pode crescer >50% em uma semana sem evento de aquisição em massa')
- Padrões de falhas de integração conhecidas por sistema (ex: 'HubSpot retorna 0 em domingos para este campo')
- Heurísticas de diagnóstico falso-positivo por categoria de causa

## Action Items

1. Confirmar o gatilho e carregar a entrada (Snapshot de coleta do Pulsar (com data_quality_flags) + diagnósticos de causa-raiz do Argo + thresholds de qualidade co…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Snapshot validado com flags de qualidade atualizadas) e persistir no artefato do squad.
4. Entregar ao critic Véra 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Snapshot validado com flags de qualidade atualizadas
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Véra 2 registrado
- [ ] Gate HITL respeitado: DIAGNÓSTICO DE BAIXA CONFIANÇA (L3): Quando Véra classifica diagnóstico de causa-raiz como confiança Baixa e o KR associado tem peso estrat…
- [ ] Gate HITL respeitado: RECOMENDAÇÃO COM IMPACTO FINANCEIRO DIRETO (L3): Rex nunca cria task automática no ClickUp para recomendações classificadas como 'ação fina…
- [ ] Gate HITL respeitado: ALERTA DE DADOS COMPROMETIDOS (L2→L3): Se Véra detectar que >30% dos KPIs de um OKR crítico vieram com data_quality_flag=FAILED (falha de i…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — DIAGNÓSTICO DE BAIXA CONFIANÇA (L3): Quando Véra classifica diagnóstico de causa-raiz como confiança Baixa e o KR associado tem peso estratégico Alto (ex: OKR… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — RECOMENDAÇÃO COM IMPACTO FINANCEIRO DIRETO (L3): Rex nunca cria task automática no ClickUp para recomendações classificadas como 'ação financeira' (ex: cancela… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — ALERTA DE DADOS COMPROMETIDOS (L2→L3): Se Véra detectar que >30% dos KPIs de um OKR crítico vieram com data_quality_flag=FAILED (falha de integração, dado zera… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — CLONE SIGMA PUBLICAÇÃO EXTERNA (L1→L3): Sigma pode gerar e entregar o Pulse no Slack e Notion de uso interno do founder sem aprovação. Se o founder solicitar v… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — RECALIBRAÇÃO DE TARGET DE OKR (L2): Quando Kalinda detecta que um OKR está >120% da trajetória esperada por 2 semanas consecutivas (super-performance) ou que a… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — ONBOARDING DE NOVO KPI/SISTEMA (L1): Ao adicionar nova fonte de dados ao catálogo, o primeiro ciclo de coleta opera em modo 'dry-run' — Pulsar coleta e Kalinda… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Véra 2 | BLOQUEIA entrega |

## Handoff

- **to:** Véra 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
