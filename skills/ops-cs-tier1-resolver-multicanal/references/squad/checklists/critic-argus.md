# Checklist do critic Argus — Suporte Conversacional Multicanal

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Argus — Critic de Qualidade & Compliance — Valida cada resposta gerada pelos workers antes do envio externo ao cliente. Rubrica de 5 dimensoes: (1) TOM — adequado ao canal e sentimento do cliente (0-10); (2) COMPLIANCE — nao promete alem da politica, nao cria obrigacoes nao autorizadas (0-10); (3) ALUCINACAO — toda informacao factual e verificavel na KB ou no sistema consultado (0-10); (4) COMPLETUDE — responde o que foi perguntado sem deixar gaps que forcam novo contato (0-10); (5) SEGURANÇA — nao expoe dados de outros clientes, nao viola LGPD (0-10). Score minimo para envio: 42/50. Abaixo de 42 ou qualquer dimensao < 6: rejeita e devolve para o worker com feedback especifico. Score < 30 ou flag de risco juridico/LGPD: escalona para HITL via Hermes.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic de Qualidade & Compliance
- [ ] **C02** — Valida cada resposta gerada pelos workers antes do envio externo ao cliente
- [ ] **C03** — Rubrica de 5 dimensoes: (1) TOM
- [ ] **C04** — adequado ao canal e sentimento do cliente (0-10)
- [ ] **C05** — (2) COMPLIANCE
- [ ] **C06** — nao promete alem da politica, nao cria obrigacoes nao autorizadas (0-10)
- [ ] **C07** — (3) ALUCINACAO
- [ ] **C08** — toda informacao factual e verificavel na KB ou no sistema consultado (0-10)
- [ ] **C09** — (4) COMPLETUDE
- [ ] **C10** — responde o que foi perguntado sem deixar gaps que forcam novo contato (0-10)
- [ ] **C11** — (5) SEGURANÇA
- [ ] **C12** — nao expoe dados de outros clientes, nao viola LGPD (0-10)
- [ ] **C13** — Score minimo para envio: 42/50
- [ ] **C14** — Abaixo de 42 ou qualquer dimensao < 6: rejeita e devolve para o worker com feedback especifico
- [ ] **C15** — Score < 30 ou flag de risco juridico/LGPD: escalona para HITL via Hermes

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário
- [ ] **HITL** — Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo
- [ ] **HITL** — Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados
- [ ] **HITL** — Terceira interação na mesma sessão sem resolução confirmada pelo cliente
- [ ] **HITL** — Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação
- [ ] **HITL** — Menção de palavras-chave de risco: 'advogado', 'PROCON', 'Reclame Aqui', 'processo', 'imprensa', 'TV'
- [ ] **HITL** — Solicitacao de troca/devolucao fora do prazo de politica ou em categoria inelegivel — Volta escalona para decisao humana com contexto
- [ ] **HITL** — Health score do cliente cai abaixo de 45 durante a interação — Pulse dispara alerta para CSM responsável
- [ ] **HITL** — Áudio com qualidade ASR < 0.80 de confiança — Vox marca para revisão humana antes de processar

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
