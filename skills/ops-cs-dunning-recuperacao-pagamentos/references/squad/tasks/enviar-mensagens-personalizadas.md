---
task: zap()
responsavel: "Zap"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Instrução de disparo do Dante (template HSM ID, variáveis de personalização, número do cliente com DDI) + status da janela de conversação no Supabase (aberta/fechada, timestamp do último contato) + credenciais WhatsApp Business API via MCP + lista de templates aprovados com variáveis mapeadas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagem WhatsApp enviada"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registro no Supabase: waba_message_id, status (sent/delivered/read), timestamp"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Notificação ao Cobalt se: entrega falhou (número inválido"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "notificar CSM), mensagem lida-sem-resposta apos 30min (Dante considera follow-up), resposta recebida (encaminha ao Flex com texto completo e contexto da conversa), cliente optou por sair (stop/cancelar"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "encerra canal WA e registra opt-out)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Dante quando canal da instrução é WhatsApp; acionado por webhook de mensagem recebida do cliente via WhatsApp (qualquer resposta dispara o Flex); acionado pelo Cobalt para envio de conf…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes com menos de 3 meses de casa) — Flex classifica e cria task HITL urgente no ClickUp para o time financeiro com histórico completo e valor em risco"
    - "[ ] HITL: Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar no gateway e no CRM, e responde ao cliente confirmando que um humano vai verificar em até X horas"
    - "[ ] HITL: Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task de retenção para o CSM com contexto completo: cliente já estava em inadimplência + agora solicitou cancelamento = risco crítico combinado"
    - "[ ] HITL: Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgente para o Head Financeiro e para o CSM responsável da conta, com sugestão de abordagem via chamada telefônica"
    - "[ ] HITL: Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema no gateway de pagamento, no processador ou na infraestrutura (não é inadimplência — é incidente têcnico)"
---

# Enviar Mensagens Personalizadas

**Task ID:** `zap()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Mensagens Personalizadas |
| **status** | `pending` |
| **responsible_executor** | Zap (Zap — Dispatchêr de WhatsApp Business) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa envio de mensagens de recuperação via WhatsApp Business API com tratamento nativo de templates aprovados pelo Meta e gestão de janela de conversação. Para cada instrução do Dante, Zap: (1) Seleciona o template HSM aprovado no Meta correspondente ao step e ao perfil do cliente — templates pre-aprovados para cobrança são obrigatórios fora da janela de 24h; (2) Monta a mensagem com variáveis de personalização (nome, valor, link de pagamento, opções de negociação) dentro dos limites do template aprovado; (3) Envia via WhatsApp Business API (360dialog / Twilio / Meta Cloud API) e registra o status de entrega (sent, delivered, read); (4) Monitora leitura em tempo real — se lido e não respondido em 30min, sinaliza ao Cobalt para step de follow-up textual simples; (5) Recebe respostas do cliente e encaminha ao Flex para classificação de intenção; (6) Gerencia a janela de 24h: se o cliente respondeu qualquer coisa, abre janela livre para o Flex conversar sem precisar de template HSM.

## Input

- Instrução de disparo do Dante (template HSM ID, variáveis de personalização, número do cliente com DDI) + status da janela de conversação no Supabase (aberta/fechada, timestamp do último contato) + credenciais WhatsApp Business API via MCP + lista de templates aprovados com variáveis mapeadas

## Output

- Mensagem WhatsApp enviada
- Registro no Supabase: waba_message_id, status (sent/delivered/read), timestamp
- Notificação ao Cobalt se: entrega falhou (número inválido
- notificar CSM), mensagem lida-sem-resposta apos 30min (Dante considera follow-up), resposta recebida (encaminha ao Flex com texto completo e contexto da conversa), cliente optou por sair (stop/cancelar
- encerra canal WA e registra opt-out)

## Trigger

Acionado pelo Dante quando canal da instrução é WhatsApp; acionado por webhook de mensagem recebida do cliente via WhatsApp (qualquer resposta dispara o Flex); acionado pelo Cobalt para envio de confirmação de pagamento via WhatsApp após recuperação bem-sucedida

## Knowledge base (o que o executor consulta)

- Catálogo de templates HSM aprovados pelo Meta por step de cobrança e por perfil (com variáveis mapeadas e limites de caracteres), regras de janela de 24h do WhatsApp Business (quando usar HSM vs mensagem livre), números de telefone dos clientes com DDI +55 e validação de número ativo, política de opt-out (parar contatos se cliente solicitar
- registrar no Supabase e CRM), limites de mensagens por número por dia (anti-spam do WhatsApp), configuração de webhook por provedor (360dialog/Twilio/Meta Cloud API)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Instrução de disparo do Dante (template HSM ID, variáveis de personalização, número do cliente com DDI) + status da jan…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagem WhatsApp enviada) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagem WhatsApp enviada
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dia…
- [ ] Gate HITL respeitado: Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time fin…
- [ ] Gate HITL respeitado: Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes c… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task d… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgent… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Sentinel reprova uma mensagem por violação de compliance legal (CDC/LGPD) — bloqueia o disparo, notifica o Head Jurídico e o responsável de CS via Slack, e sus… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Cliente com histórico de chargeback ou de fraude identificado pelo gateway — Cobalt bloqueia a sequência de dunning automática e cria task manual para o time f… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Bad debt confirmado (cobranca nao recuperada apos sequencia completa + tentativas manuais) — Cobalt fecha a sequencia como IRRECUPERAVEL, Atlas atualiza o coho… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Flex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
