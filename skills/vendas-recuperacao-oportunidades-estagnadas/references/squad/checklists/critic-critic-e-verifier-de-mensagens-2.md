# Checklist do critic Critic e Verifier de Mensagens 2 — Recuperação de Oportunidades Estagnadas

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Guardião (Critic e Verifier de Mensagens) — Red-team de qualidade pre-envio. Valida personalização genuína, compliance, tom, ausência de promessas não autorizadas e correção factual em TODA mensagem antes de sair para o lead. Opera como gate obrigatório entre Arquiteto e Mensageiro — nenhuma mensagem externa passa sem aprovação. Também audita retrospectivamente os playbooks que geraram opt-out ou reclamação.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Guardião (Critic e Verifier de Mensagens)
- [ ] **C02** — Red-team de qualidade pre-envio
- [ ] **C03** — Valida personalização genuína, compliance, tom, ausência de promessas não autorizadas e correção factual em TODA mensagem antes de sair para o lead
- [ ] **C04** — Opera como gate obrigatório entre Arquiteto e Mensageiro
- [ ] **C05** — nenhuma mensagem externa passa sem aprovação
- [ ] **C06** — Também audita retrospectivamente os playbooks que geraram opt-out ou reclamação

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeiro toque automatizado — gate L3 no Mensageiro)
- [ ] **HITL** — Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa
- [ ] **HITL** — Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável comercial
- [ ] **HITL** — Mudança de playbook baseada em proposta do Forense — ajustes em playbooks existentes exigem aprovação humana antes de entrar em produção
- [ ] **HITL** — Primeiro contato via voz (Vapi/Retell) para leads de alto valor — script revisado e aprovado pelo responsavel antes do disparo
- [ ] **HITL** — Opt-out recebido — registrado imediatamente, comunicado ao comercial, nenhuma acao adicional automatica alem do registro de compliance

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
