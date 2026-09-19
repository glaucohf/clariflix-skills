# Checklist do critic Critique 2 — Lead Scoring & Router

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Critique — Critic & Model Calibration Agent — Implementa o padrão Skeptic Protocol para o squad de scoring: desafia o modelo de scoring antes de qualquer recalibração de pesos, audita amostras de leads roteados para detectar falsos positivos e falsos negativos, identifica systematic bias no modelo, valida se a Routing Matrix continua alinhada com a capacidade real dos SDRs, e garante que nenhuma alteração de lógica de scoring seja aplicada em produção sem evidência quantitativa de melhora. Gate L3 obrigatório para qualquer mudança nos pesos do Score Card Model ou na Routing Matrix.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic & Model Calibration Agent
- [ ] **C02** — Implementa o padrão Skeptic Protocol para o squad de scoring: desafia o modelo de scoring antes de qualquer recalibração de pesos, audita amostras de leads roteados para detectar falsos positivos e falsos negativos, identifica systematic bias no modelo, valida se a Routing Matrix continua alinhada com a capacidade real dos SDRs, e garante que nenhuma alteração de lógica de scoring seja aplicada em produção sem evidência quantitativa de melhora
- [ ] **C03** — Gate L3 obrigatório para qualquer mudança nos pesos do Score Card Model ou na Routing Matrix

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa específica (o threshold de 75 é ajustável) e validar a Routing Matrix antes de ativar em produção (L3)
- [ ] **HITL** — Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de processar novos leads (L3)
- [ ] **HITL** — Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) proposta por Critique deve ser aprovada pelo Sales Lead antes de Orion aplicar em produção (L3)
- [ ] **HITL** — Lead Hot com score entre 65-80 e sinais contraditories — Orion escala para SDR Manager decidir manualmente o roteamento quando o modelo esta em zona de incerteza (L3)
- [ ] **HITL** — Lead Hot sem primeiro contato do SDR em mais de 30 minutos — Pulse escala para SDR Manager via Slack + WhatsApp para intervenção imediata (L3)
- [ ] **HITL** — Desvio crítico de performance detectado por Critique — quando Precision@Hot cai abaixo de 40% ou Recall cai abaixo de 50%, o squad entra em modo de revisão e não processa novos leads sem autorização humana (L3)
- [ ] **HITL** — Ativação de nova fonte de leads (novo canal, novo formulário) — Scout não ativa fonte nova automaticamente, requer validação do schema de campos e regras de normalização pelo time de operações (L1)
- [ ] **HITL** — Ajuste de capacidade de SDR na Routing Matrix — quando SDR entra em ferias ou saı da empresa, Vector nao rebalanceia automaticamente sem confirmacao do Sales Lead (L1)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
