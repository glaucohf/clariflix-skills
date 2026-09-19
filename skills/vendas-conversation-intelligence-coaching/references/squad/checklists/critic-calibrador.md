# Checklist do critic Calibrador — Conversation Intelligence e Coaching

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Auditor de Insights (Calibrador) — Crític/Verifier que intercepta o Coaching Card gerado pelo Sensei antes da entrega para o vendedor e valida: (1) rastreabilidade — cada ponto de feedback deve ter referência a um momento exato da call com transcrição citada, zero feedback sem evidência; (2) especificidade — counter-scripts devem ser específicos ao contexto da call, não textos de livro gênericos; (3) tom construtivo — feedback não pode ser demotivador ou agressivo, mesmo quando a call foi ruim (princípio: elogio público, feedback privado específico); (4) prioridade coerente — as 3 áreas de melhoria selecionadas devem ser as de maior impacto real no resultado do deal específico, não as mais fáceis de comentar; (5) consistência com histórico — se o vendedor já recebeu feedback sobre a mesma área nas últimas 3 calls e não melhorou, escalar para o gestor em vez de repetir o mesmo coaching; (6) acurácia do score — verificar se o score do Juiz é coerente com a qualidade da call descrita na análise. Score mínimo para liberação: 8/10 nas 6 dimensões. Também audita 20% das calls semanalmente em modo aleatório para detectar drift de qualidade dos agentes de análise.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Auditor de Insights (Calibrador)
- [ ] **C02** — Crític/Verifier que intercepta o Coaching Card gerado pelo Sensei antes da entrega para o vendedor e valida: (1) rastreabilidade
- [ ] **C03** — cada ponto de feedback deve ter referência a um momento exato da call com transcrição citada, zero feedback sem evidência
- [ ] **C04** — (2) especificidade
- [ ] **C05** — counter-scripts devem ser específicos ao contexto da call, não textos de livro gênericos
- [ ] **C06** — (3) tom construtivo
- [ ] **C07** — feedback não pode ser demotivador ou agressivo, mesmo quando a call foi ruim (princípio: elogio público, feedback privado específico)
- [ ] **C08** — (4) prioridade coerente
- [ ] **C09** — as 3 áreas de melhoria selecionadas devem ser as de maior impacto real no resultado do deal específico, não as mais fáceis de comentar
- [ ] **C10** — (5) consistência com histórico
- [ ] **C11** — se o vendedor já recebeu feedback sobre a mesma área nas últimas 3 calls e não melhorou, escalar para o gestor em vez de repetir o mesmo coaching
- [ ] **C12** — (6) acurácia do score
- [ ] **C13** — verificar se o score do Juiz é coerente com a qualidade da call descrita na análise
- [ ] **C14** — Score mínimo para liberação: 8/10 nas 6 dimensões
- [ ] **C15** — Também audita 20% das calls semanalmente em modo aleatório para detectar drift de qualidade dos agentes de análise

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — HITL-1 (L3): Deal Risk Alert de nível ALTO ou CRÍTICO gerado pelo Vigilante — gestor recebe alerta no WhatsApp e deve confirmar qual ação tomar (ligar agora, escalar para diretor, ajustar proposta, aceitar perda) antes de qualquer comunicação automatizada com o prospect. SLA de resposta: 4h em dias úteis.
- [ ] **HITL** — HITL-2 (L3): Objeção de tipo não mapeado detectada pela primeira vez — o Analisador sinaliza objeção nova fora da biblioteca existente. Humano (gestor ou especialista de produto) deve validar a classificação e criar o counter-script antes que o sistema use-o em coachings futuros. Evita ensinar o time a responder errado.
- [ ] **HITL** — HITL-3 (L2): Score da call abaixo de 40/100 (call catastrófica) — além do coaching card automático, o Orchestrator notifica o gestor para que ele decida se faz uma sessão 1:1 urgente com o vendedor ou se o deal precisar de intervenção direta do gestor. Vendedor não é notificado do score crítico sem acompanhamento humano.
- [ ] **HITL** — HITL-4 (L2): Transcrição com qualidade de áudio abaixo de 75% de confiança — a Babel sinaliza e o gestor decide se envia para transcrição manual, descarta a call da análise ou aceita os resultados com baixa confiança. Garante que coaching baseado em transcrição ruim não chegue ao vendedor.
- [ ] **HITL** — HITL-5 (L2): Calibração quinzenal da Rubrica de Avaliação — o gestor revisa um sample de 5 calls para verificar se os scores do Juiz estão alinhados com sua percepção. Ajusta pesos de dimensões se necessário. Previne drift do modelo de scoring ao longo do tempo.
- [ ] **HITL** — HITL-6 (L1): Aprovação do Plano de Role-Play semanal gerado pelo Radar do Time — gestor revisa as objeções priorizadas e o script de simulação antes de compartilhar com o time no próximo standup de vendas. Garante que o treinamento coletivo seja relevante para o contexto atual do mercado.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
