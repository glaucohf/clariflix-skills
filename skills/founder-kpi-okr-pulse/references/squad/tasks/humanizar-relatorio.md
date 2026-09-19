---
task: sigma()
responsavel: "Sigma"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pulse Report estruturado do Atlas (com diagnósticos e recomendações validados) + corpus de treinamento do founder (textos, decisões, frameworks favoritos indexados no Vector DB) + configuração de formato preferido (executivo 1-pager / completo / telegram-style bullets)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pulse Report no tom do founder"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Seção 'Minha Leitura desta Semana' em primeira pessoa (2-3 parágrafos de reflexão estratégica no estilo do founder)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Versão ultra-curta para WhatsApp/Telegram (5 bullets de impacto máximo)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Versão completa para Notion"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Todas as versões mantêm links para dados-fonte e tasks do ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Atlas como etapa final do pipeline semanal se Sigma estiver habilitado na config. Pode ser ativado ad-hoc: '/rewrite-pulse [formato]'. Desabilitado automaticamente em relatórios de alerta…"
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

# Humanizar Relatório

**Task ID:** `sigma()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KPI/OKR Pulse — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Humanizar Relatório |
| **status** | `pending` |
| **responsible_executor** | Sigma (Sigma — O Clone do Founder) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker opcional especializado em reescrita do Pulse Report no tom, linguagem e frameworks de raciocínio do founder. Recebe o relatório estruturado gerado pelo Atlas e o humaniza: elimina jargão técnico de dados, aplica o vocabulário e as analogias características do founder, formata na densidade de informação preferida (bullets densos, narrativa executiva ou tabular), e adiciona a seção 'O que eu faria' em primeira pessoa com o raciocínio estratégico do founder. Treinado no corpus de comunicações, decisões e frameworks do founder. Ativado como etapa final opcional antes da entrega — pode ser desligado por preferência do founder ou quando precisão técnica é mais importante que personalização.

## Input

- Pulse Report estruturado do Atlas (com diagnósticos e recomendações validados) + corpus de treinamento do founder (textos, decisões, frameworks favoritos indexados no Vector DB) + configuração de formato preferido (executivo 1-pager / completo / telegram-style bullets)

## Output

- Pulse Report no tom do founder
- Seção 'Minha Leitura desta Semana' em primeira pessoa (2-3 parágrafos de reflexão estratégica no estilo do founder)
- Versão ultra-curta para WhatsApp/Telegram (5 bullets de impacto máximo)
- Versão completa para Notion
- Todas as versões mantêm links para dados-fonte e tasks do ClickUp

## Trigger

Ativado por Atlas como etapa final do pipeline semanal se Sigma estiver habilitado na config. Pode ser ativado ad-hoc: '/rewrite-pulse [formato]'. Desabilitado automaticamente em relatórios de alerta crítico (L3 HITL) — nesses casos o relatório vai no formato técnico padrão para máxima clareza.

## Knowledge base (o que o executor consulta)

- Corpus do founder: textos públicos (LinkedIn, artigos, apresentações), decisões estratégicas documentadas, frameworks favoritos, vocabulário característico e tom de comunicação (indexados no Vector DB privado)
- Histórico de Pulse Reports aprovados pelo founder (feedback de formato e linguagem)
- Configurações de preferência de entrega (canal, horário, formato preferido por contexto)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pulse Report estruturado do Atlas (com diagnósticos e recomendações validados) + corpus de treinamento do founder (text…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pulse Report no tom do founder) e persistir no artefato do squad.
4. Entregar ao critic Véra 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pulse Report no tom do founder
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

- **to:** Véra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
