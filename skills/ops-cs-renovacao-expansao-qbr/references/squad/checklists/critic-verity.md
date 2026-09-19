# Checklist do critic Verity — Renovacao, Expansao e QBR Automatizado

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Verity — Critic de Evidencia e Proporcionalidade — Valida todos os artefatos gerados pelo squad antes de qualquer disparo externo (criacao de task no ClickUp, envio de notificacao, geracao de deck) em tres dimensoes: (A) INTEGRIDADE DE DADOS — cada numero, metrica ou afirmacao no brief tem uma fonte rastreavel no Supabase ou no CRM; nenhum dado foi interpolado, estimado sem base ou inventado; campos faltantes sao sinalizados como 'dado nao disponivel' em vez de omitidos silenciosamente. (B) PROPORCIONALIDADE — a urgencia e o tipo de acao recomendada sao proporcionais ao Renewal Readiness Score e ao MRR da conta: nao recomenda reuniao de executive sponsor para conta SMB de baixo MRR; nao gera deck completo de 12 slides para renovacao de R$5k; nao sinaliza oportunidade de expansao para conta que usa menos de 60% do tier atual. (C) COMPLETUDE PARA ACAO — o CSM pode entrar na reuniao ou fazer o contato de renovacao usando apenas o brief, sem precisar buscar informacao adicional; agenda proposta esta completa com tempos; objecoes previstas tem resposta pronta; proximos passos estao claros. Score de aprovacao: minimo 36/40 (9/10 em cada dimensao). Abaixo do threshold: devolve ao Briefer com feedback especifico por dimensao. Maximo de 2 iteracoes antes de escalar para humano. Tambem valida o Renewal Readiness Score do Compass: score nao pode variar mais de 20 pontos em 48h sem evento documentado (protecao contra anomalia de dados de entrada).

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic de Evidencia e Proporcionalidade
- [ ] **C02** — Valida todos os artefatos gerados pelo squad antes de qualquer disparo externo (criacao de task no ClickUp, envio de notificacao, geracao de deck) em tres dimensoes: (A) INTEGRIDADE DE DADOS
- [ ] **C03** — cada numero, metrica ou afirmacao no brief tem uma fonte rastreavel no Supabase ou no CRM
- [ ] **C04** — nenhum dado foi interpolado, estimado sem base ou inventado
- [ ] **C05** — campos faltantes sao sinalizados como 'dado nao disponivel' em vez de omitidos silenciosamente
- [ ] **C06** — (B) PROPORCIONALIDADE
- [ ] **C07** — a urgencia e o tipo de acao recomendada sao proporcionais ao Renewal Readiness Score e ao MRR da conta: nao recomenda reuniao de executive sponsor para conta SMB de baixo MRR
- [ ] **C08** — nao gera deck completo de 12 slides para renovacao de R$5k
- [ ] **C09** — nao sinaliza oportunidade de expansao para conta que usa menos de 60% do tier atual
- [ ] **C10** — (C) COMPLETUDE PARA ACAO
- [ ] **C11** — o CSM pode entrar na reuniao ou fazer o contato de renovacao usando apenas o brief, sem precisar buscar informacao adicional
- [ ] **C12** — agenda proposta esta completa com tempos
- [ ] **C13** — objecoes previstas tem resposta pronta
- [ ] **C14** — proximos passos estao claros
- [ ] **C15** — Score de aprovacao: minimo 36/40 (9/10 em cada dimensao)
- [ ] **C16** — Abaixo do threshold: devolve ao Briefer com feedback especifico por dimensao
- [ ] **C17** — Maximo de 2 iteracoes antes de escalar para humano
- [ ] **C18** — Tambem valida o Renewal Readiness Score do Compass: score nao pode variar mais de 20 pontos em 48h sem evento documentado (protecao contra anomalia de dados de entrada)

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de expansao com status 'Aguardando Aprovacao do CSM/Manager' antes de incluir a proposta no deck final para o cliente
- [ ] **HITL** — Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CSM (deck e gerado, nunca enviado automaticamente ao cliente)
- [ ] **HITL** — Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar qualquer contato de renovacao
- [ ] **HITL** — Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de entrada antes de reprocessar
- [ ] **HITL** — Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer alinhamento com equipe comercial (AE ou CSM sênior) antes de abordar o cliente
- [ ] **HITL** — Comprometimento pendente do fornecedor detectado pelo Memory como nao entregue no periodo anterior — brief inclui o item mas Pulse cria subtask de 'Resolucao de Compromisso Pendente' que requer confirmacao do CSM de que foi resolvido antes de marcar como pronto para QBR
- [ ] **HITL** — Conta com Renewal Readiness Score CRITICO (< 50) e renovacao em < 30 dias — escalacao imediata para Head de CS e Account Executive senior com brief de situacao de emergencia; qualquer acao sobre conta fica subordinada a aprovacao do Head de CS
- [ ] **HITL** — Feedback de Memory indicando que CSM fez edicao significativa no deck (> 30% do conteudo alterado) — Maestro abre HITL para CSM documentar o motivo da edicao e calibrar o Briefer para futuras geracoes

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
