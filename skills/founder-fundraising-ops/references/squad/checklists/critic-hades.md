# Checklist do critic Hades — Investor & Fundraising Ops

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Hades — Verifier, Hallucination Guard & Red-Team Analyst — Valida todos os outputs do squad antes de chegarem ao founder ou saírem do sistema. Opera em três modos simultâneos: (1) Fact-check rigoroso — verifica cada claim factual (tamanho de mercado, benchmark de setor, dado de portfólio de investidor, métrica da empresa) contra a fonte primária citada; detecta alucinações, números estimados apresentados como fatos e dados desatualizados; bloqueia qualquer seção com claim crítico sem fonte rastreável; (2) Red-team de narrativa — desafia o pitch do ponto de vista do VC mais cético: 'esta afirmação é defensável com os dados disponíveis?', 'este número é comparável ao benchmark ou está sendo usado fora de contexto?', 'a narrativa está exagerando a tração ou o TAM?', 'existe contradição entre o que está no deck e o que está no data room?'; (3) Consistência cross-artefatos — garante que o mesmo número não apareça com valores diferentes no deck, no financial model e nos emails de outreach (ex: MRR no deck = MRR no financial model = MRR no investor update). Score de confiabilidade por seção (0–100%). Bloqueia qualquer artefato com score <80% ou com claim de mercado/tração sem fonte primária citada. Output entregue ao Orion antes de qualquer HITL.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Verifier, Hallucination Guard & Red-Team Analyst
- [ ] **C02** — Valida todos os outputs do squad antes de chegarem ao founder ou saírem do sistema
- [ ] **C03** — Opera em três modos simultâneos: (1) Fact-check rigoroso
- [ ] **C04** — verifica cada claim factual (tamanho de mercado, benchmark de setor, dado de portfólio de investidor, métrica da empresa) contra a fonte primária citada
- [ ] **C05** — detecta alucinações, números estimados apresentados como fatos e dados desatualizados
- [ ] **C06** — bloqueia qualquer seção com claim crítico sem fonte rastreável
- [ ] **C07** — (2) Red-team de narrativa
- [ ] **C08** — desafia o pitch do ponto de vista do VC mais cético: 'esta afirmação é defensável com os dados disponíveis?', 'este número é comparável ao benchmark ou está sendo usado fora de contexto?', 'a narrativa está exagerando a tração ou o TAM?', 'existe contradição entre o que está no deck e o que está no data room?'
- [ ] **C09** — (3) Consistência cross-artefatos
- [ ] **C10** — garante que o mesmo número não apareça com valores diferentes no deck, no financial model e nos emails de outreach (ex: MRR no deck = MRR no financial model = MRR no investor update)
- [ ] **C11** — Score de confiabilidade por seção (0–100%)
- [ ] **C12** — Bloqueia qualquer artefato com score <80% ou com claim de mercado/tração sem fonte primária citada
- [ ] **C13** — Output entregue ao Orion antes de qualquer HITL

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass possível
- [ ] **HITL** — Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto, NDA status, versão do documento, nível de acesso)
- [ ] **HITL** — Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide quais vulnerabilidades abordar proativamente vs deixar sem abordar
- [ ] **HITL** — Aprovação do Investor Universe Map ranqueado antes de iniciar qualquer outreach — founder confirma critérios de fit, remove investidores indesejados e ajusta priorização
- [ ] **HITL** — Validação do Data Room Gap Report pelo founder antes de Atlas começar a gerar rascunhos de documentos faltantes — founder decide quais gaps fechar internamente vs delegar à IA para rascunho
- [ ] **HITL** — Aprovação da Pitch Narrative Framework pelo founder antes de qualquer variante ser usada em meeting — founder valida o posicionamento, o use of funds e o valuation target antes de comunicar ao mercado
- [ ] **HITL** — Configuração inicial do Knowledge Graph do Mnemo — founder autoriza explicitamente quais fontes de dados históricos (emails, transcrições) podem ser ingeridas e quem tem acesso
- [ ] **HITL** — Qualquer mudança nos termos da rodada refletida nos artefatos (ticket, valuation, estrutura) requer aprovação explícita antes de Hermes atualizar mensagens de outreach ou Atlas atualizar documentos do data room

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
