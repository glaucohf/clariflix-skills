# Checklist do critic Atena — Dormant Lead Reactivation

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Atena — A Guardiã da Segunda Chance — Valida CADA draft de reativação gerado pelo Lázaro Writer antes de qualquer envio. Checklist obrigatório de 10 pontos — reprovar em qualquer item bloqueia o envio: (1) Ausência do ângulo falhado: a mensagem usa ZERO elementos da abordagem original que não funcionou? Qualquer repetição do ângulo arquivado pela Arqueóloga = REPROVADO automaticamente — reativação com o mesmo pitch que já falhou e pior que não enviar; (2) Ancoragem em mudança real: a mensagem referencia pelo menos UMA mudança detectada pelo Radar com dado específico e verificável? 'Vi que voces expandiram para o Sul em março' e aprovado; 'vi que voces cresceram muito' = REPROVADO; (3) Reconhecimento respeitoso do histórico: a mensagem menciona o contato anterior de forma natural e sem constrangimento? Nunca fingir que é um primeiro contato quando não é; (4) CTA calibrado ao archetype: o chamado para ação está alinhado com o archetype de dormência — lead que disse 'não é o momento' recebe CTA leve (recurso, conteúdo), não proposta comercial direta; (5) Tom não-desesperado: mensagem de reativação não pode soar como desespero de vendas ou pressão — tom de genuína curiosidade e proposta de valor é o único aprovado; (6) Compliance LGPD reativação: menção explícita ao contato anterior (evidência de relação previa e base legal), mecanismo de opt-out claro, não usa dados que o lead não tornou públicos além do contexto B2B normal; (7) Brevidade e respeito: email de reativação max 120 palavras (menos que cold outreach porque o lead já conhece a empresa — não precisa de educação, precisa de razão para retomar), WhatsApp max 2 blocos curtos, LinkedIn max 250 caracteres; (8) Subject line verificada: max 50 caracteres, sem 'Re:' falso, sem 'follow-up' (clichê que reduz abertura em 30%), sem emojis excessivos para B2B, contendo pelo menos 1 elemento específico do lead ou da mudança detectada; (9) Sequência coerente: se é toque 2 ou 3, a mensagem constroi sobre o silêncio anterior de forma natural — não repete o mesmo pitch, escala sutilmente o valor ou muda o ângulo; (10) Última mensagem com graça: se é o toque final da sequência (fechamento), tem a 'porta aberta' — frase de encerramento respeitosa que não queima a relação e facilita opt-out sem drama. Veredicto: APROVADO (segue para Charon Dispatcher) / REESCREVER com instruções específicas por ponto reprovado (volta ao Lázaro Writer, max 1 ciclo automático) / BLOQUEAR_HITL para casos que exigem revisão humana (dados inconsistentes no dossiê, ângulo de reativação ambíguo, flag de compliance crítico).

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — A Guardiã da Segunda Chance
- [ ] **C02** — Valida CADA draft de reativação gerado pelo Lázaro Writer antes de qualquer envio
- [ ] **C03** — Checklist obrigatório de 10 pontos
- [ ] **C04** — reprovar em qualquer item bloqueia o envio: (1) Ausência do ângulo falhado: a mensagem usa ZERO elementos da abordagem original que não funcionou? Qualquer repetição do ângulo arquivado pela Arqueóloga = REPROVADO automaticamente
- [ ] **C05** — reativação com o mesmo pitch que já falhou e pior que não enviar
- [ ] **C06** — (2) Ancoragem em mudança real: a mensagem referencia pelo menos UMA mudança detectada pelo Radar com dado específico e verificável? 'Vi que voces expandiram para o Sul em março' e aprovado
- [ ] **C07** — 'vi que voces cresceram muito' = REPROVADO
- [ ] **C08** — (3) Reconhecimento respeitoso do histórico: a mensagem menciona o contato anterior de forma natural e sem constrangimento? Nunca fingir que é um primeiro contato quando não é
- [ ] **C09** — (4) CTA calibrado ao archetype: o chamado para ação está alinhado com o archetype de dormência
- [ ] **C10** — lead que disse 'não é o momento' recebe CTA leve (recurso, conteúdo), não proposta comercial direta
- [ ] **C11** — (5) Tom não-desesperado: mensagem de reativação não pode soar como desespero de vendas ou pressão
- [ ] **C12** — tom de genuína curiosidade e proposta de valor é o único aprovado
- [ ] **C13** — (6) Compliance LGPD reativação: menção explícita ao contato anterior (evidência de relação previa e base legal), mecanismo de opt-out claro, não usa dados que o lead não tornou públicos além do contexto B2B normal
- [ ] **C14** — (7) Brevidade e respeito: email de reativação max 120 palavras (menos que cold outreach porque o lead já conhece a empresa
- [ ] **C15** — não precisa de educação, precisa de razão para retomar), WhatsApp max 2 blocos curtos, LinkedIn max 250 caracteres
- [ ] **C16** — (8) Subject line verificada: max 50 caracteres, sem 'Re:' falso, sem 'follow-up' (clichê que reduz abertura em 30%), sem emojis excessivos para B2B, contendo pelo menos 1 elemento específico do lead ou da mudança detectada
- [ ] **C17** — (9) Sequência coerente: se é toque 2 ou 3, a mensagem constroi sobre o silêncio anterior de forma natural
- [ ] **C18** — não repete o mesmo pitch, escala sutilmente o valor ou muda o ângulo
- [ ] **C19** — (10) Última mensagem com graça: se é o toque final da sequência (fechamento), tem a 'porta aberta'
- [ ] **C20** — frase de encerramento respeitosa que não queima a relação e facilita opt-out sem drama
- [ ] **C21** — Veredicto: APROVADO (segue para Charon Dispatcher) / REESCREVER com instruções específicas por ponto reprovado (volta ao Lázaro Writer, max 1 ciclo automático) / BLOQUEAR_HITL para casos que exigem revisão humana (dados inconsistentes no dossiê, ângulo de reativação ambíguo, flag de compliance crítico)

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex: deal > R$20k) bloqueia completamente e notifica o gestor com draft completo, ficha de arqueologia e sinais novos para aprovacao ou rejeicao com 1 clique — nenhum caracter e enviado antes da aprovacao.
- [ ] **HITL** — Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovação humana obrigatória antes de entrar em sequência — agente não envia para dado não verificado.
- [ ] **HITL** — Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o gestor de marketing com o feedback completo do critic para reescritura ou descisao de nao envio.
- [ ] **HITL** — Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que disse, sugestão de próximo passo) — o squad paralisa qualquer automação para este lead e o vendedor assume o controle total da conversa.
- [ ] **HITL** — Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções de alto valor merecem resposta humana ou pelo menos validação antes de resposta automática.
- [ ] **HITL** — Sinais de oportunidade detectados em lead que estava em ARQUIVO (score < 40): Radar detecta mudança significativa (investimento, mudança de decisor, sinal de intent forte) em lead que havia sido desprioritizado — alerta ao gestor para decisão de reintegrar o lead na fila ativa ou manter desprioritizado.
- [ ] **HITL** — Relatório semanal de performance: Echo Analyst gera relatório de taxa de reativação por trilha e archetype entregue ao gestor todo friday — ponto de HITL estruturado para revisão de qual trilha está funcionando e quais ajustes de playbook são necessários antes da próxima rodada.
- [ ] **HITL** — Opt-out recebido: processamento automático cancela a sequência e atualiza o CRM, mas a decisão de blacklist permanente (nunca mais contatar) é sempre humana — o agente sinaliza e aguarda confirmação do gestor antes de registrar blacklist definitiva.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
