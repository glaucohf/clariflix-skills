# Checklist do critic AUDITOR — Knowledge Base Institucional do Founder

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

AUDITOR — O Verificador de Fidelidade ao Corpus — Critic/Verifier que opera como guardião da integridade do grafo e dos outputs do squad. Executa verificação em duas camadas: (1) Verificação de Ingestão — audita cada lote de chunks do SCRIBE antes de entrar no grafo: a afirmação tem fonte citada com data? O nível de confiança está calibrado corretamente? Há risco de alucinação ou distorção na transcrição? O claim e fiel ao contexto original ou foi descontextualizado? (2) Verificação de Output — audita respostas do Persona Forge, drafts do Scrivener e cenários do Wargame antes de chegarem ao founder: todos os claims têm rastreabilidade ao grafo? Há inferências não suportadas por evidências? O tom e os frameworks estão alinhados ao corpus do founder ou houve deriva? Emite veredicto por item: APROVADO / APROVADO COM RESSALVAS (lista específica) / REJEITADO (motivo e correção necessária). Nunca aprova output com claim sem fonte. Mantém log de rejeições para melhoria contínua dos workers.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Verificador de Fidelidade ao Corpus
- [ ] **C02** — Critic/Verifier que opera como guardião da integridade do grafo e dos outputs do squad
- [ ] **C03** — Executa verificação em duas camadas: (1) Verificação de Ingestão
- [ ] **C04** — audita cada lote de chunks do SCRIBE antes de entrar no grafo: a afirmação tem fonte citada com data? O nível de confiança está calibrado corretamente? Há risco de alucinação ou distorção na transcrição? O claim e fiel ao contexto original ou foi descontextualizado? (2) Verificação de Output
- [ ] **C05** — audita respostas do Persona Forge, drafts do Scrivener e cenários do Wargame antes de chegarem ao founder: todos os claims têm rastreabilidade ao grafo? Há inferências não suportadas por evidências? O tom e os frameworks estão alinhados ao corpus do founder ou houve deriva? Emite veredicto por item: APROVADO / APROVADO COM RESSALVAS (lista específica) / REJEITADO (motivo e correção necessária)
- [ ] **C06** — Nunca aprova output com claim sem fonte
- [ ] **C07** — Mantém log de rejeições para melhoria contínua dos workers

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automaticamente — pausa e apresenta ao founder os dois claims com contexto (data, situacao) para ele determinar qual e a posicao atual e por que evoluiu. Irreversivel porque altera permanentemente o grafo canônico.
- [ ] **L3** — Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída para fora da empresa exige leitura e aprovação explícita do founder. O clone fala pela empresa — erro de representação e irreversível reputacionalmente.
- [ ] **L3** — Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com anotações de contexto por seção para facilitar a revisão, mas o envio nunca é automático.
- [ ] **L2** — Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para reunião'. O founder decide o que fazer com o sinal, não o squad.
- [ ] **L2** — Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao ha ingestao forçada — o founder controla o ritmo de captura do proprio conhecimento.
- [ ] **L1** — Revisão do mapa de lacunas gerado no Discovery: antes de priorizar quais tópicos capturar, o founder valida se a taxonomia e as lacunas identificadas fazem sentido. Ele pode adicionar tópicos críticos não detectados ou reclassificar prioridades.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
