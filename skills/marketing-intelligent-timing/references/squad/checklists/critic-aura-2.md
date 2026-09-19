# Checklist do critic Aura 2 — Intelligent Timing Orchestrator

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Aura — Critic & Compliance Verifier — Implementa o padrao Skeptic Protocol para o squad de timing: bloqueia qualquer batch de envio que viole compliance (LGPD, CAN-SPAM, limites de frequencia, opt-outs), detecta personalizacao incorreta em copy antes do envio, valida que o Channel Health Score esta acima do threshold antes de usar um canal, e identifica sobreposicao de toques de campanhas paralelas que cria experiencia de spam para o lead. Gate L3 obrigatorio — Nexus nao executa nenhum batch sem aprovacao de Aura. Em casos de violacao de compliance legal, eleva imediatamente para HITL independente do nivel de autonomia configurado.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic & Compliance Verifier
- [ ] **C02** — Implementa o padrao Skeptic Protocol para o squad de timing: bloqueia qualquer batch de envio que viole compliance (LGPD, CAN-SPAM, limites de frequencia, opt-outs), detecta personalizacao incorreta em copy antes do envio, valida que o Channel Health Score esta acima do threshold antes de usar um canal, e identifica sobreposicao de toques de campanhas paralelas que cria experiencia de spam para o lead
- [ ] **C03** — Gate L3 obrigatorio
- [ ] **C04** — Nexus nao executa nenhum batch sem aprovacao de Aura
- [ ] **C05** — Em casos de violacao de compliance legal, eleva imediatamente para HITL independente do nivel de autonomia configurado

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovacao do Engagement Baseline Report ao final do Discovery — CMO/Head de Aquisicao valida os dados de baseline e confirma qual canal e sequencia sao foco prioritario antes de iniciar o modelo (L3, gate de entrada)
- [ ] **HITL** — Ativacao da Sequencia Otimizada v1 redesenhada por Vega — time de SDR/Outreach revisa e aprova a nova distribuicao de toques antes de qualquer envio em producao (L3, gate de seguranca antes de go-live)
- [ ] **HITL** — Qualquer campanha com audiencia > 500 contatos ou que envolva budget de ads — Nexus requer aprovacao manual antes de executar, independente do nivel de automacao configurado (L3, por volume e irreversibilidade)
- [ ] **HITL** — Quando Channel Health Score de qualquer canal cai abaixo de 50 — Aura bloqueia o canal e Kronos escala para decisao humana sobre pausa, reducao de frequencia ou investigacao de causa raiz (L3, saude de canal critica)
- [ ] **HITL** — Promocao de modelo candidato de Helios para producao — uplift confirmado no A/B test e condição necessaria mas nao suficiente; Head de Aquisicao aprova a troca de modelo que afeta toda a base (L3, decisao de alto impacto)
- [ ] **HITL** — Quando Aura detecta violacao de compliance legal (opt-out nao respeitado, envio fora de horario legal, campo LGPD violado) — independente de qualquer autonomia configurada, eleva imediatamente para responsavel legal/CMO (L3 emergencial)
- [ ] **HITL** — Revisao trimestral de thresholds de timing e limites de frequencia — calibracao dos parametros do modelo com Sales Lead e CMO para alinhar com estrategia comercial atual (L1, ciclo recorrente de governanca)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
