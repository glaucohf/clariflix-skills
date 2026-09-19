# Checklist do critic Aegis 2 — Paid Media Autopilot

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Aegis — Compliance & Brand Guard — Critic/Verifier responsável por validar toda copy, criativo e ação de execução antes de publicação ou mudança de campanha. Atua como red-team de qualidade: testa se a copy seria rejeitada pela plataforma, se viola brand voice, se contêm claims enganosos, se o ajuste de budget viola guardrails. Não aprova, não executa — apenas bloqueia, aprova ou solicita revisão com justificativa precisa. Gate obrigatório no pipeline antes de qualquer ação externa irreversível.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Compliance & Brand Guard
- [ ] **C02** — Critic/Verifier responsável por validar toda copy, criativo e ação de execução antes de publicação ou mudança de campanha
- [ ] **C03** — Atua como red-team de qualidade: testa se a copy seria rejeitada pela plataforma, se viola brand voice, se contêm claims enganosos, se o ajuste de budget viola guardrails
- [ ] **C04** — Não aprova, não executa
- [ ] **C05** — apenas bloqueia, aprova ou solicita revisão com justificativa precisa
- [ ] **C06** — Gate obrigatório no pipeline antes de qualquer ação externa irreversível

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA aceitável, floor de ROAS para escala, orçamento máximo em risco por ciclo) — sem essa aprovação o squad não opera
- [ ] **HITL** — Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: mover > 20% do budget total ou pausar campanha inteira) requer aprovação explícita via Slack/WhatsApp antes de execução pelo Midas
- [ ] **HITL** — Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos formatos ou novos ângulos de mensagem sem histórico) requer aprovação humana — irreversível em termos de impressão inicial
- [ ] **HITL** — Aprovação semanal do relatório de inteligência do Sentinel: recomendações proativas de escala para próxima semana (aumento de orçamento semanal acima de threshold) requerem OK do gestor antes de ativação automática
- [ ] **HITL** — Revisão mensal de thresholds e guardrails: reunião obrigatória de 30min para calibrar bandas com base em performance real do mês anterior — o squad opera com os guardrails mais recentes aprovados
- [ ] **HITL** — Onboarding de nova plataforma ou canal: qualquer expansão para nova plataforma de mídia (ex: adicionar TikTok Ads, Pinterest Ads, CTV) requer aprovação e configuração supervisionada pelo humano responsável
- [ ] **HITL** — Bloqueio por anomalia crítica: se Argos detectar anomalia CRITICAL (ex: ROAS caiu > 50% em 1h ou spend disparou 300% acima do target), o squad pausa todas as ações autônomas e aguarda instrução humana explícita antes de retomar

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
