---
task: columbo()
responsavel: "Columbo"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "5 sub-relatorios dos workers (Fenix, Themis, Sigma, Atlas, Vox) com todos os claims e fontes citadas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de Verificação: lista de claims por worker com status (VERIFIED/UNVERIFIED/DISPUTED), score de confiança geral por sub-relatório (0-100), lista de alucinações detectadas (claims sem fonte), contra-argumentos do vendedor por red flag, recomendação de quais red flags precisam de validação humana adicional antes de avançar"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Nexus automaticamente após recepção dos 5 sub-relatórios. Bloqueia o pipeline: Eco não é ativado até Columbo emitir status APPROVED (confiança >= 75) ou o founder aprovar manualmente no…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Columbo 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complementa com dados adicionais (especialmente se completude < 60). Criticidade: ALTA — avançar com dados incompletos invalida todo o pipeline."
    - "[ ] HITL: HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFIED/DISPUTED para decisão: aceitar o risco e prosseguir, solicitar pesquisa adicional (re-ativa workers específicos), ou cancelar a triagem do target."
    - "[ ] HITL: HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20% do valuation estimado, irregularidade fiscal grave) pausa o pipeline e exige confirmação do founder antes de prosseguir. Pode levar ao cancelamento imediato da triagem."
    - "[ ] HITL: HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilhamento com advisors, bancos, co-investidores ou o próprio target. Ações irreversíveis (envio externo) sempre requerem aprovação humana explícita."
    - "[ ] HITL: HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados pontos. Eco re-executa com instruções específicas. Não é irreversível, mas é um checkpoint de qualidade importante."
---

# Verificar Claims Fontes

**Task ID:** `columbo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Due Diligence / M&A Screening

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Claims Fontes |
| **status** | `pending` |
| **responsible_executor** | Columbo (Columbo — O Cético Verificador) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Crític e Red-Team Agent. Função exclusiva: desafiar e verificar todos os claims dos 5 workers antes da síntese final. Checa rastreabilidade de fontes (toda afirmação precisa de URL ou referência verificável), detecta alucinações (claims sem fonte = marcados como UNVERIFIED), identifica vieses de confirmação (quando o analista só cita evidências favoráveis), e simula o advogado do diabo — quais argumentos um vendedor do target usaria para refutar cada red flag. Output é o relatório com score de confiança por claim.

## Input

- 5 sub-relatorios dos workers (Fenix, Themis, Sigma, Atlas, Vox) com todos os claims e fontes citadas

## Output

- Relatório de Verificação: lista de claims por worker com status (VERIFIED/UNVERIFIED/DISPUTED), score de confiança geral por sub-relatório (0-100), lista de alucinações detectadas (claims sem fonte), contra-argumentos do vendedor por red flag, recomendação de quais red flags precisam de validação humana adicional antes de avançar

## Trigger

Ativado pelo Nexus automaticamente após recepção dos 5 sub-relatórios. Bloqueia o pipeline: Eco não é ativado até Columbo emitir status APPROVED (confiança >= 75) ou o founder aprovar manualmente no HITL Gate.

## Knowledge base (o que o executor consulta)

- Biblioteca de padrões de alucinação (claims típicos falsos em M&A research), base de fontes confiáveis vs não-confiáveis por tipo de dado, histórico de claims verificados/refutados de triagens anteriores do squad (aprende com cada ciclo)

## Action Items

1. Confirmar o gatilho e carregar a entrada (5 sub-relatorios dos workers (Fenix, Themis, Sigma, Atlas, Vox) com todos os claims e fontes citadas).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de Verificação: lista de claims por worker com status (VERIFIED/UNVERIFIED/DISPUTED), score de confiança gera…) e persistir no artefato do squad.
4. Entregar ao critic Columbo 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de Verificação: lista de claims por worker com status (VERIFIED/UNVERIFIED/DISPUTED), score de confiança geral por sub-relatório (0-100), lista de al…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Columbo 2 registrado
- [ ] Gate HITL respeitado: HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude…
- [ ] Gate HITL respeitado: HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a list…
- [ ] Gate HITL respeitado: HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passiv…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complem… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFI… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20%… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilham… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados po… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL Gate L1 — Configuração Inicial do Target: O founder define a intenção estratégica (por que este target, qual a tese inicial, quais setores/mercados são re… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Columbo 2 | BLOQUEIA entrega |

## Handoff

- **to:** Columbo 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
