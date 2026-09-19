---
task: quincy()
responsavel: "Quincy"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Draft final do board pack/investor update com Source Manifest"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Perfis dos board members e investidores que receberão o material (nome, background, histórico de perguntas em ciclos anteriores, área de foco preferida)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Guidance do ciclo anterior (o que ficou em aberto, quais temas são sensíveis)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Board Q&A Brief: lista das top 10 perguntas previstas ordenadas por dificuldade, com (1) contexto de por que esta pergunta vai surgir, (2) resposta recomendada no tom do founder, (3) dado de suporte para ter na ponta da língua, (4) o que NÃO dizer"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Formato: Notion page entregue junto com o board pack final"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Draft final aprovado pelo founder antes de envio (D-3 antes do meeting). Founder solicita prep de reunião específica com investidor. Novo board member ou investidor sendo apresentado à empresa pela p…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Axiom antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção"
    - "[ ] HITL: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores"
    - "[ ] HITL: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%"
    - "[ ] HITL: Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa não autorizada)"
    - "[ ] HITL: Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downround) entrarem no draft final"
---

# Simular Perguntas Board

**Task ID:** `quincy()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Board & Investor Relations — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Simular Perguntas Board |
| **status** | `pending` |
| **responsible_executor** | Quincy (Quincy — Board Q&A Simulator) |
| **execution_type** | `Worker` |
| **input** | 3 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Simula as perguntas difíceis que o board e investidores farão com base no draft do board pack. Atua como um board member adversarial: identifica as 5–10 perguntas mais desconfortáveis que o conteúdo vai gerar, escreve a pergunta no estilo de cada perfil de board member (financeiro, operacional, estratégico), e sugere a melhor resposta para cada uma no tom do founder. Prepara o founder para não ser surpreendido.

## Input

- Draft final do board pack/investor update com Source Manifest
- Perfis dos board members e investidores que receberão o material (nome, background, histórico de perguntas em ciclos anteriores, área de foco preferida)
- Guidance do ciclo anterior (o que ficou em aberto, quais temas são sensíveis)

## Output

- Board Q&A Brief: lista das top 10 perguntas previstas ordenadas por dificuldade, com (1) contexto de por que esta pergunta vai surgir, (2) resposta recomendada no tom do founder, (3) dado de suporte para ter na ponta da língua, (4) o que NÃO dizer
- Formato: Notion page entregue junto com o board pack final

## Trigger

Draft final aprovado pelo founder antes de envio (D-3 antes do meeting). Founder solicita prep de reunião específica com investidor. Novo board member ou investidor sendo apresentado à empresa pela primeira vez.

## Knowledge base (o que o executor consulta)

- Histórico de perguntas de board meetings anteriores (transcrições/notas)
- Perfis dos board members e investors (LinkedIn, background financeiro, portfolio)
- Draft do board pack atual
- Métricas de performance vs guidance anterior (para antecipar perguntas de accountability)
- Benchmarks de setor (para comparação que o board pode trazer)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Draft final do board pack/investor update com Source Manifest).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Board Q&A Brief: lista das top 10 perguntas previstas ordenadas por dificuldade, com (1) contexto de por que esta pergu…) e persistir no artefato do squad.
4. Entregar ao critic Axiom; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Board Q&A Brief: lista das top 10 perguntas previstas ordenadas por dificuldade, com (1) contexto de por que esta pergunta vai surgir, (2) resposta recomendada…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Axiom registrado
- [ ] Gate HITL respeitado: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção
- [ ] Gate HITL respeitado: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao b…
- [ ] Gate HITL respeitado: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90% | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa nã… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downr… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação do Q&A Brief do Quincy antes do board meeting — founder confirma quais respostas está confortável em dar publicamente | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Configuração inicial do corpus do Sage — founder revisa e aprova quais comunicações passadas entram no corpus de clonagem narrativa | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Qualquer mudança de metodologia de cálculo de métrica-chave (ex: mudança de definição de ARR, churn líquido vs bruto) requer aprovação explícita antes de ser r… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Axiom | BLOQUEIA entrega |

## Handoff

- **to:** Cipher
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
