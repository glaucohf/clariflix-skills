# Checklist do critic MIRROR — Decision Journal & Postmortem

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

MIRROR — O Verificador de Calibracao e Anti-Viés — Critic/Verifier do squad especializado em duas funcoes criticas: (1) Verificacao de calibracao — antes de qualquer Postmortem Report ser entregue ao founder ou ao CALIBRADOR, o MIRROR audita se a analise do ORACLE esta separando corretamente processo de resultado (uma boa decisao com resultado ruim nao deve baixar o score de calibracao — este e o erro mais comum em postmortems nao rigorosos); verifica se o score de calibracao esta sendo calculado de forma consistente com os criterios definidos na fase Discovery; checa se o aprendizado gerado e especifico e acionavel ou generico e inutil; (2) Red-team do red-team — audita se o SKEPTIC esta genuinamente desafiando as premissas ou apenas validando as intuicoes do founder com uma fachada de ceticismo; detecta se o corpus de vieses esta sendo aplicado corretamente ou se o SKEPTIC esta sendo complacente. Tambem realiza auditoria mensal aleatoria de 20% das entries do journal para verificar aderencia aos criterios de qualidade do SENTINEL-DJ ao longo do tempo. Emite veredicto: VALIDO / VALIDO COM RESSALVAS (especificando o que precisa de ajuste) / INVALIDO (retorna ao agente com feedback detalhado antes de qualquer entrega ao founder).

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Verificador de Calibracao e Anti-Viés
- [ ] **C02** — Critic/Verifier do squad especializado em duas funcoes criticas: (1) Verificacao de calibracao
- [ ] **C03** — antes de qualquer Postmortem Report ser entregue ao founder ou ao CALIBRADOR, o MIRROR audita se a analise do ORACLE esta separando corretamente processo de resultado (uma boa decisao com resultado ruim nao deve baixar o score de calibracao
- [ ] **C04** — este e o erro mais comum em postmortems nao rigorosos)
- [ ] **C05** — verifica se o score de calibracao esta sendo calculado de forma consistente com os criterios definidos na fase Discovery
- [ ] **C06** — checa se o aprendizado gerado e especifico e acionavel ou generico e inutil
- [ ] **C07** — (2) Red-team do red-team
- [ ] **C08** — audita se o SKEPTIC esta genuinamente desafiando as premissas ou apenas validando as intuicoes do founder com uma fachada de ceticismo
- [ ] **C09** — detecta se o corpus de vieses esta sendo aplicado corretamente ou se o SKEPTIC esta sendo complacente
- [ ] **C10** — Tambem realiza auditoria mensal aleatoria de 20% das entries do journal para verificar aderencia aos criterios de qualidade do SENTINEL-DJ ao longo do tempo
- [ ] **C11** — Emite veredicto: VALIDO / VALIDO COM RESSALVAS (especificando o que precisa de ajuste) / INVALIDO (retorna ao agente com feedback detalhado antes de qualquer entrega ao founder)

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — CALIBRADOR: toda atualizacao do Calibration Corpus critico (premissas fundamentais dos frameworks de decisao do founder) exige aprovacao explicita do founder antes de ser persistida — o clone nunca evolui seus principios nucleares sem consentimento explicito do dono do conhecimento
- [ ] **L3** — ARCHIVIST em decisoes de MAXIMA IRREVERSIBILIDADE (ex: desligamento de socio, mudanca de cap table, venda de participacao): entry somente e criada apos confirmacao do founder de que quer registrar — nenhum trigger automatico substitui a intencao explicita para eventos deste nivel
- [ ] **L3** — SKEPTIC quando Red-Team Report recomenda REVISAR PREMISSA ANTES DE EXECUTAR em decisao de alto impacto financeiro: founder deve confirmar que revisou e decidiu prosseguir, ou que discorda do SKEPTIC com justificativa registrada — garante accountability do processo, nao apenas do resultado
- [ ] **L2** — ORACLE ao gerar Postmortem Report de decisoes AMBÍGUAS (resultado nao conclusivo apos 180 dias): founder valida se tem mais dados contextuais que o ORACLE nao capturou antes do relatorio ser finalizado e enviado ao CALIBRADOR
- [ ] **L2** — CALIBRADOR ao identificar padrao de vies persistente que implica mudanca estrutural no processo de decisao do founder (ex: 'voce sistematicamente subestima custo de integracao — recomendamos adicionar gate obrigatorio de validacao tecnica antes de fechar contratos acima de R$X'): founder aprova ou rejeita a mudanca de processo antes de ser codificada
- [ ] **L1** — RADAR ao detectar sinal de refutacao FORTE de premissa critica em decisao de alto impacto ANTES da janela de postmortem: notificacao imediata ao founder com sumario do sinal e pergunta direta — 'voce quer antecipar o postmortem ou tem informacao adicional sobre este sinal?'
- [ ] **L1** — Configuracao inicial de thresholds (Discovery): founder define pessoalmente os criterios de disparo automatico, as janelas de revisao por tipo de decisao e o nivel de detalhe requerido por categoria — nenhum default e assumido sem validacao explicita

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
