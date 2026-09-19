# Checklist do critic SENTINEL — Inteligência de Conta e Battlecards

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

SENTINEL — O Verificador de Inteligencia — Critic/Verifier que audita o dossie e o battlecard antes da entrega ao vendedor. Verifica: (1) Factualidade — todas as afirmacoes tem fonte citada e data? Nenhuma informacao inventada ou desatualizada (> 90 dias sem sinalizacao)? (2) Relevancia — o conteudo e especifico para esta conta ou generico demais? (3) Acionabilidade — o dossie gera acoes concretas ou e apenas informacao passiva? (4) Riscos — ha informacoes sensiveis ou potencialmente incorretas que podem constranger o vendedor se usadas? (5) Completude — os 4 workers entregaram seus outputs? Ha gaps criticos? Emite veredicto: APROVADO / APROVADO COM RESSALVAS / REJEITADO com lista de correcoes especificas.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Verificador de Inteligencia
- [ ] **C02** — Critic/Verifier que audita o dossie e o battlecard antes da entrega ao vendedor
- [ ] **C03** — Verifica: (1) Factualidade
- [ ] **C04** — todas as afirmacoes tem fonte citada e data? Nenhuma informacao inventada ou desatualizada (> 90 dias sem sinalizacao)? (2) Relevancia
- [ ] **C05** — o conteudo e especifico para esta conta ou generico demais? (3) Acionabilidade
- [ ] **C06** — o dossie gera acoes concretas ou e apenas informacao passiva? (4) Riscos
- [ ] **C07** — ha informacoes sensiveis ou potencialmente incorretas que podem constranger o vendedor se usadas? (5) Completude
- [ ] **C08** — os 4 workers entregaram seus outputs? Ha gaps criticos? Emite veredicto: APROVADO / APROVADO COM RESSALVAS / REJEITADO com lista de correcoes especificas

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistência permanente no CRM de produção
- [ ] **L3** — Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do envio, nunca envio automático sem leitura humana
- [ ] **L2** — Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que vai usar e descarta o que não se aplica
- [ ] **L1** — Quando SENTINEL emite REJEITADO: NEXUS pausa pipeline e notifica o vendedor sobre o gap de qualidade, permitindo que ele decida se quer prosseguir com versão parcial ou aguardar correção
- [ ] **L1** — Identificação de stakeholders de alto risco (ex: prospect e ex-funcionário de empresa cliente com conflito): IRIS sinaliza e vendedor decide como abordar antes de qualquer ação

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
