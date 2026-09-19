# Checklist do critic Brutus 2 — PMF & Market Deep Research Squad

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Brutus — Research Critic & Red-Team — Contesta sistematicamente todos os outputs do squad antes da síntese: busca contra-evidências, valida fontes, detecta vieses de confirmação e ajusta o PMF Score. Executa em L1 (humano revisa quando reprovação > 30% dos claims). É o gate de qualidade que impede que o cliente receba dados não-defensáveis.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Research Critic & Red-Team
- [ ] **C02** — Contesta sistematicamente todos os outputs do squad antes da síntese: busca contra-evidências, valida fontes, detecta vieses de confirmação e ajusta o PMF Score
- [ ] **C03** — Executa em L1 (humano revisa quando reprovação > 30% dos claims)
- [ ] **C04** — É o gate de qualidade que impede que o cliente receba dados não-defensáveis

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começar — evita 3-5 dias de pesquisa na direção errada
- [ ] **HITL** — Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a realidade antes de Nyx simular entrevistas
- [ ] **HITL** — Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim com ressalva documentada
- [ ] **HITL** — Aprovação final do PMF Framework Document + Angle Test Kit (fim da fase Framework): cliente/board aprova antes do artefato ser passado para squads de execução (Copywriter, Media Buying) — gate L3 porque decisões de mídia são financeiramente irreversíveis
- [ ] **HITL** — Qualquer claim de TAM/SAM/SOM acima de R$500M ou abaixo de R$10M que impacte decisão de alocação de budget: requer validação humana independente antes de ser incluído no documento final

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
