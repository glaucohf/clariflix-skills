# Checklist do critic Eco 2 — Voz-IA para Atendimento Telefônico

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Eco — Critic de Qualidade de Voz — Valida cada resposta gerada pelos workers antes da sintese TTS e envio ao cliente. Rubrica especifica para voz em 5 dimensoes: NATURALIDADE (soa como humano em voz alta, sem bullets ou linguagem de email), BREVIDADE (max 3 frases para telefone, max 5 para WhatsApp audio), FACTUALIDADE (informacoes verificaveis nos sistemas consultados, sem dados inventados), COMPLIANCE (nao cria obrigacoes nao autorizadas, nao promete fora do escopo autonomo), EMPATIA (tom adequado ao sentimento detectado pelo Radar — validacao emocional antes de dados quando cliente esta frustrado). Score minimo para TTS: 42/50. Abaixo de 42 ou qualquer dimensao < 6: rejeita e devolve ao worker com feedback especifico e sugestao de reformulacao. Score < 30 ou flag de risco legal/LGPD: bloqueia pipeline e escalona para HITL via Hertz imediatamente.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic de Qualidade de Voz
- [ ] **C02** — Valida cada resposta gerada pelos workers antes da sintese TTS e envio ao cliente
- [ ] **C03** — Rubrica especifica para voz em 5 dimensoes: NATURALIDADE (soa como humano em voz alta, sem bullets ou linguagem de email), BREVIDADE (max 3 frases para telefone, max 5 para WhatsApp audio), FACTUALIDADE (informacoes verificaveis nos sistemas consultados, sem dados inventados), COMPLIANCE (nao cria obrigacoes nao autorizadas, nao promete fora do escopo autonomo), EMPATIA (tom adequado ao sentimento detectado pelo Radar
- [ ] **C04** — validacao emocional antes de dados quando cliente esta frustrado)
- [ ] **C05** — Score minimo para TTS: 42/50
- [ ] **C06** — Abaixo de 42 ou qualquer dimensao < 6: rejeita e devolve ao worker com feedback especifico e sugestao de reformulacao
- [ ] **C07** — Score < 30 ou flag de risco legal/LGPD: bloqueia pipeline e escalona para HITL via Hertz imediatamente

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket prioritario antes de executar
- [ ] **HITL** — Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona para humano
- [ ] **HITL** — Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente para supervisor
- [ ] **HITL** — Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana
- [ ] **HITL** — Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especialista
- [ ] **HITL** — Cliente VIP, Enterprise ou MRR > R$5k: toda acao irreversivel (cancelamento, mudanca de plano, refund parcial) requer aprovacao do CSM responsavel antes da execucao
- [ ] **HITL** — Audio com duracao > 3 minutos e confianca media ASR < 0.82 — transcricao marcada para revisao humana antes do processamento completo pelo Maestro
- [ ] **HITL** — Intencao nao reconhecida apos 2 turns de coleta pelo Vivo (confianca < 0.55) — Hertz escalona com transcricao completa para o humano interpretar e resolver
- [ ] **HITL** — Solicitacao de dados de terceiros, portabilidade de dados, ou qualquer direito LGPD em voz — Hertz bloqueia automacao e direciona para DPO/time juridico

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
