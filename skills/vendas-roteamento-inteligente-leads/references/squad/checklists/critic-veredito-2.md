# Checklist do critic Veredito 2 — Roteamento Inteligente de Leads

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Veredito (Critic / Verifier de Roteamento) — Auditor independente e red-team do Maestro. Valida cada decisao de roteamento antes da execucao verificando consistencia de scoring, adequacao do vendedor, personalizacao da mensagem e ausencia de vieses sistematicos. Funciona como gate de qualidade obrigatorio entre a decisao do Maestro e a notificacao pelo Hermes. Gera relatorio semanal de auditoria identificando padroes de erro e sugestoes de melhoria nas regras de roteamento.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Veredito (Critic / Verifier de Roteamento)
- [ ] **C02** — Auditor independente e red-team do Maestro
- [ ] **C03** — Valida cada decisao de roteamento antes da execucao verificando consistencia de scoring, adequacao do vendedor, personalizacao da mensagem e ausencia de vieses sistematicos
- [ ] **C04** — Funciona como gate de qualidade obrigatorio entre a decisao do Maestro e a notificacao pelo Hermes
- [ ] **C05** — Gera relatorio semanal de auditoria identificando padroes de erro e sugestoes de melhoria nas regras de roteamento

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro deploy; em produção, amostras aleatórias (10%) passam por revisão humana
- [ ] **L3** — Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratamento especial
- [ ] **L3** — Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente
- [ ] **L3** — Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interface de configuração, com log de auditoria
- [ ] **L3** — Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor designado
- [ ] **HITL** — Revisão humana semanal do relatório de auditoria do Veredito para identificar vieses sistemáticos e calibrar o modelo de scoring

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
