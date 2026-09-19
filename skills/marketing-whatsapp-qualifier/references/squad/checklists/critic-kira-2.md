# Checklist do critic Kira 2 — WhatsApp Qualifier

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Kira — Compliance & Voice Guardian — Implementa o papel de critic/verifier do squad com foco em dois vetores: (1) Conformidade operacional — cada versao do Playbook Conversacional e auditada contra as restricoes Meta pos-proibicao, LGPD e brand voice antes de ir para producao. Gate L3 obrigatorio: sem aprovacao de Kira, nenhuma mensagem automatizada e enviada. (2) Monitoramento continuo — audita sample diaria de conversas em producao para detectar desvios de conformidade, mensagens que possam violar politicas e padroes que indiquem risco de banimento da conta WhatsApp Business. Age como advogado do diabo do squad: assume que qualquer mensagem automatizada pode ser interpretada de forma adversa pela Meta e forca o playbook a ser explicitamente seguro.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Compliance & Voice Guardian
- [ ] **C02** — Implementa o papel de critic/verifier do squad com foco em dois vetores: (1) Conformidade operacional
- [ ] **C03** — cada versao do Playbook Conversacional e auditada contra as restricoes Meta pos-proibicao, LGPD e brand voice antes de ir para producao
- [ ] **C04** — Gate L3 obrigatorio: sem aprovacao de Kira, nenhuma mensagem automatizada e enviada
- [ ] **C05** — (2) Monitoramento continuo
- [ ] **C06** — audita sample diaria de conversas em producao para detectar desvios de conformidade, mensagens que possam violar politicas e padroes que indiquem risco de banimento da conta WhatsApp Business
- [ ] **C07** — Age como advogado do diabo do squad: assume que qualquer mensagem automatizada pode ser interpretada de forma adversa pela Meta e forca o playbook a ser explicitamente seguro

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do squad ser configurado (L3, sem aprovacao o squad nao avanca)
- [ ] **HITL** — Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e resposta a objecao. Kira ja auditou conformidade, mas humano decide se o tom esta certo (L3, gate obrigatorio)
- [ ] **HITL** — Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior para assumir a conversa manualmente antes de Vance responder (L3, acao irreversivel: primeira impressao com conta estrategica)
- [ ] **HITL** — Gate semanal de 30 minutos — head de vendas revisa 5-10 conversas de baixo desempenho selecionadas por Lilo, aprova ajustes de playbook propostos por Orion antes de Vance ser atualizado (L2, recorrente toda segunda-feira)
- [ ] **HITL** — Aprovacao de nova versao do Playbook apos ajustes significativos (> 30% das mensagens alteradas) — qualquer revisao estrutural do playbook passa por gate L3 com head de vendas e Kira antes de producao
- [ ] **HITL** — Decisao de escalada por irritacao detectada — quando Vance detecta 3+ sinais de irritacao em sequencia, Orion alerta SDR humano via notificacao para assumir a conversa. Humano decide se assume imediatamente ou deixa Vance tentar uma ultima mensagem de reengajamento (L3)
- [ ] **HITL** — Revisao mensal de metricas com Nova — CEO/CMO aprova redistribuicao de budget por fonte de lead com base no ROI report de Nova (L3, envolve gasto financeiro)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
