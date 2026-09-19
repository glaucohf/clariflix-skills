# Checklist do critic Vigilia — Reengajamento Pós-Evento e Webinar

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Vigília — Critic de Mensagem, Personalização e Compliance — Intercepta toda mensagem ANTES do envio externo para validar: (1) personalização correta e contextualizada no evento — nome, empresa, produto certo, referência ao momento REAL do evento (sem inventar perguntas que o lead não fez); (2) tom adequado ao canal, score de engajamento e estágio do funil (Score A = direto e urgente; Score B = educativo; Score C = suave e sem pressão); (3) compliance LGPD — verificação de opt-in do participante do evento e ausência de dados de terceiros indevidamente usados; (4) factualidade — sem promessas comerciais não autorizadas, sem preço ou condição inventada, sem claims sobre o evento que não ocorreram; (5) sem erros de merge tag ({{campo_vazio}} visível na mensagem). Retorna APROVADO com score de qualidade (0-100) ou BLOQUEADO com raiz específica do problema e sugestão de correção. Máximo 2 iterações de correção automática — na 3ª, escala para HITL com log completo. Também valida se o contato não solicitou opt-out em qualquer ponto anterior.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic de Mensagem, Personalização e Compliance
- [ ] **C02** — Intercepta toda mensagem ANTES do envio externo para validar: (1) personalização correta e contextualizada no evento
- [ ] **C03** — nome, empresa, produto certo, referência ao momento REAL do evento (sem inventar perguntas que o lead não fez)
- [ ] **C04** — (2) tom adequado ao canal, score de engajamento e estágio do funil (Score A = direto e urgente
- [ ] **C05** — Score B = educativo
- [ ] **C06** — Score C = suave e sem pressão)
- [ ] **C07** — (3) compliance LGPD
- [ ] **C08** — verificação de opt-in do participante do evento e ausência de dados de terceiros indevidamente usados
- [ ] **C09** — (4) factualidade
- [ ] **C10** — sem promessas comerciais não autorizadas, sem preço ou condição inventada, sem claims sobre o evento que não ocorreram
- [ ] **C11** — (5) sem erros de merge tag ({{campo_vazio}} visível na mensagem)
- [ ] **C12** — Retorna APROVADO com score de qualidade (0-100) ou BLOQUEADO com raiz específica do problema e sugestão de correção
- [ ] **C13** — Máximo 2 iterações de correção automática
- [ ] **C14** — na 3ª, escala para HITL com log completo
- [ ] **C15** — Também valida se o contato não solicitou opt-out em qualquer ponto anterior

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) — qualquer ação requer aprovação do closer responsável antes do primeiro envio
- [ ] **HITL** — Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento
- [ ] **HITL** — Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática
- [ ] **HITL** — Participante do evento que é funcionário de concorrente identificado — qualquer abordagem requer decisão estratégica humana
- [ ] **HITL** — Solicitação de proposta comercial ou orçamento mencionada na resposta do lead — Argos Evento escala imediatamente para closer com ficha de qualificação
- [ ] **HITL** — Lead que solicita opt-out ou demonstra irritação com o contato — intervenção humana obrigatória, registro de opt-out e revisão da cadência
- [ ] **HITL** — Inconsistência crítica detectada entre dados do evento e CRM (ex: lead do evento e cliente com contrato ativo cancelado) — revisão humana antes de qualquer contato
- [ ] **HITL** — Volume de lista acima de 1.000 contatos em evento único — revisão humana da segmentação antes do disparo em massa

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
