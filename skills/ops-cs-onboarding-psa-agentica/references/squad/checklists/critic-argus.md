# Checklist do critic Argus — Onboarding & Implementação

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Argus — Crítico de Qualidade e Completude — Agente verificador que revisa o plano de implementação antes da publicação no ClickUp (HITL gate) e audita os relatórios de delivery antes do envio ao cliente. Checklists de validação: plano (todos os marcos têm owner? todas as tarefas têm critério de aceite? dependências externas estão sinalizadas? datas são realistas dado o histórico?); relatório (dados batem com o ClickUp? semáforo RAG está correto? linguagem é adequada para o cliente? não há informações confidenciais expostas?). Bloqueia publicação/envio se checklist não passar com score >=85%.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Crítico de Qualidade e Completude
- [ ] **C02** — Agente verificador que revisa o plano de implementação antes da publicação no ClickUp (HITL gate) e audita os relatórios de delivery antes do envio ao cliente
- [ ] **C03** — Checklists de validação: plano (todos os marcos têm owner? todas as tarefas têm critério de aceite? dependências externas estão sinalizadas? datas são realistas dado o histórico?)
- [ ] **C04** — relatório (dados batem com o ClickUp? semáforo RAG está correto? linguagem é adequada para o cliente? não há informações confidenciais expostas?)
- [ ] **C05** — Bloqueia publicação/envio se checklist não passar com score >=85%

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)
- [ ] **HITL** — Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)
- [ ] **HITL** — Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro
- [ ] **HITL** — Aprovação do Delivery Status Report semanal antes do envio ao cliente
- [ ] **HITL** — Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente
- [ ] **HITL** — Decisão de go/no-go para go-live quando health score < 60 ou mais de 2 marcos críticos em Red

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
