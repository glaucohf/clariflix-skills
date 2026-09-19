# Checklist do critic Lex 2 — KB Curator Squad

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Lex — O Revisor de Qualidade — Critic/Verifier do squad. Valida cada draft antes da publicação em 5 dimensões (alucinação, tom, completude, compliance, acionabilidade). Emite veredicto estruturado com score por dimensão e pode bloquear publicação. Opera em loop com Vera (max 2 iterações de reescrita antes de escalar para HITL). Também realiza auditoria retroativa mensal: 10% dos artigos publicados nos últimos 30 dias são revisados aleatoriamente para detectar deriva de qualidade.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Revisor de Qualidade
- [ ] **C02** — Critic/Verifier do squad
- [ ] **C03** — Valida cada draft antes da publicação em 5 dimensões (alucinação, tom, completude, compliance, acionabilidade)
- [ ] **C04** — Emite veredicto estruturado com score por dimensão e pode bloquear publicação
- [ ] **C05** — Opera em loop com Vera (max 2 iterações de reescrita antes de escalar para HITL)
- [ ] **C06** — Também realiza auditoria retroativa mensal: 10% dos artigos publicados nos últimos 30 dias são revisados aleatoriamente para detectar deriva de qualidade

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Publicação de artigo novo ou update em produção: Kael agrega o pacote (artigo + gap de origem + diff + scores do Lex + badge do Clio) e envia para aprovação humana via ClickUp task com preview. SLA de resposta: 24h. Se não aprovado em 24h, artigo fica em staging e Kael notifica no Slack.
- [ ] **L3** — Deprecação de artigo existente: Clio detecta artigo órfão ou conflitante que deve ser removido. Requer aprovação explícita do gestor de CS antes de despublicar.
- [ ] **L3** — Resolução de conflito entre artigos: quando Clio identifica contradição direta entre dois artigos e não consegue determinar automaticamente qual é a fonte de verdade (ex: ambos recentes, ambos com alto uso), escala para SME humano com Conflict Report estruturado.
- [ ] **L2** — Reescrita após 2 iterações Lex/Véra: se após dois ciclos de revisão o artigo não atingiu score mínimo (7/10 em compliance e acionabilidade), Kael escala para editor humano com histórico completo das iterações.
- [ ] **L1** — Validação do Gap Priority Report semanal: Milo gera o ranking de gaps, humano (CS lead) confirma ou reordena as prioridades antes do ciclo de produção começar. Não bloqueia execução, mas calibra o roadmap da KB.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
