# Checklist do critic Sentinel — Higiene e Enriquecimento de CRM

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Sentinel (Verificador de Integridade e Red-Team) — Apos cada ciclo de higiene (validacao + dedup + enriquecimento + sync), Sentinel amostra 5% dos registros processados e verifica: (1) nenhum campo humano foi sobrescrito indevidamente, (2) merges nao criaram perda de informacao, (3) dados enriquecidos sao plaussiveis (ex: CEO de empresa com 2 funcionarios e receita de R$500M = flag), (4) sync propagou corretamente para todos os sistemas downstream, (5) score de qualidade reflete realidade. Gera relatorio de anomalias e bloqueia ciclo seguinte se taxa de erro >5%.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Sentinel (Verificador de Integridade e Red-Team)
- [ ] **C02** — Apos cada ciclo de higiene (validacao + dedup + enriquecimento + sync), Sentinel amostra 5% dos registros processados e verifica: (1) nenhum campo humano foi sobrescrito indevidamente, (2) merges nao criaram perda de informacao, (3) dados enriquecidos sao plaussiveis (ex: CEO de empresa com 2 funcionarios e receita de R$500M = flag), (4) sync propagou corretamente para todos os sistemas downstream, (5) score de qualidade reflete realidade
- [ ] **C03** — Gera relatorio de anomalias e bloqueia ciclo seguinte se taxa de erro >5%

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual)
- [ ] **HITL** — Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3)
- [ ] **HITL** — Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez)
- [ ] **HITL** — Revisão de registros Golden Bronze com deal aberto (operador RevOps decide: enriquecer manualmente ou descartar deal)
- [ ] **HITL** — Configuração inicial do playbook de golden record no onboarding (quem decide vence em cada campo — decisão estratégica do cliente)
- [ ] **HITL** — Aprovação de integração de nova fonte de dados ao pipeline (ex: adicionar novo formulário ou importação de lista de parceiro)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
