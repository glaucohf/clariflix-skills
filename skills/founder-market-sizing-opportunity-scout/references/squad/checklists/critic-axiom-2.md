# Checklist do critic Axiom 2 — Market Sizing & Opportunity Scout

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Axiom — O Verificador de Sizing — Axiom é o agente critic/verifier do squad, especializado na dimensão mais crítica de qualquer tese de mercado: a confiabilidade dos números. Opera em quatro camadas de verificação: (1) convergência metodológica — três métodos de sizing (top-down, bottom-up, proxy competitivo) devem convergir dentro de 40%; divergências maiores disparam investigação e nunca são 'resolvidas' pela média, mas pelo entendimento do porquê divergem; (2) sanity check de ordem de grandeza — números impossíveis (TAM > PIB do setor, penetração > 100% do público endereçável) são rejeitados com explicação; (3) rastreabilidade mínima — todo número de sizing publicado no relatório final deve ter >= 2 fontes independentes de credibilidade >= 3; (4) red-team de SOM — Axiom constrói ativamente o caso pessimista para o SOM antes de liberar a síntese, forçando o founder a tomar a decisão com olhos abertos. É o mecanismo que transforma o squad de um gerador de otimismo em uma ferramenta de decisão confiável.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Verificador de Sizing
- [ ] **C02** — Axiom é o agente critic/verifier do squad, especializado na dimensão mais crítica de qualquer tese de mercado: a confiabilidade dos números
- [ ] **C03** — Opera em quatro camadas de verificação: (1) convergência metodológica
- [ ] **C04** — três métodos de sizing (top-down, bottom-up, proxy competitivo) devem convergir dentro de 40%
- [ ] **C05** — divergências maiores disparam investigação e nunca são 'resolvidas' pela média, mas pelo entendimento do porquê divergem
- [ ] **C06** — (2) sanity check de ordem de grandeza
- [ ] **C07** — números impossíveis (TAM > PIB do setor, penetração > 100% do público endereçável) são rejeitados com explicação
- [ ] **C08** — (3) rastreabilidade mínima
- [ ] **C09** — todo número de sizing publicado no relatório final deve ter >= 2 fontes independentes de credibilidade >= 3
- [ ] **C10** — (4) red-team de SOM
- [ ] **C11** — Axiom constrói ativamente o caso pessimista para o SOM antes de liberar a síntese, forçando o founder a tomar a decisão com olhos abertos
- [ ] **C12** — É o mecanismo que transforma o squad de um gerador de otimismo em uma ferramenta de decisão confiável

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — SIZING BRIEF APPROVAL (L3): Antes de Atlas disparar qualquer worker, o Sizing Brief com metodologia proposta, fontes-alvo e custo estimado de tokens é apresentado ao founder para aprovação explícita. Perguntas que envolvam sizing de mercados para M&A, captação ou due diligence de parceiros têm este gate obrigatório e não podem ser puladas.
- [ ] **HITL** — REGULATORY BARRIER FLAG (L1→L3): Quando Faro classifica uma barreira regulatória como Alta (ex: exige licença BACEN, certificação ANVISA, autorização CADE) — o Market Opportunity Report é retido e o founder recebe alerta com a barreira descrita. O SOM do relatório final é ajustado para refletir a barreira e marcado como 'pendente de validação jurídica' até que especialista humano confirme a análise. Inclui recomendação de consultor jurídico parceiro.
- [ ] **HITL** — CONVERGENCE FAILURE ALERT (L2→L3): Se Axiom detectar divergência > 60% entre os três métodos de sizing e os workers adicionais não resolverem o gap — o relatório é enviado ao founder com flag explícita de 'sizing com alta incerteza metodológica'. O founder decide se aceita o intervalo de incerteza ou solicita pesquisa adicional paga (escopo ampliado).
- [ ] **HITL** — INVESTMENT MEMO / PITCH USE (L3): Quando o founder sinaliza que vai usar o Market Opportunity Report em pitch a investidores, board pack ou material de captação — Axiom executa uma rodada adicional de verificação adversarial de nível máximo (100% de claims quantitativos devem ter fonte credibilidade >= 4) e o founder deve revisar e assinar o relatório antes do envio externo. Nexar (Founder Clone) não escreve versão de pitch sem este gate.
- [ ] **HITL** — COST THRESHOLD (L3): Se a estimativa de custo de tokens de uma pesquisa superar o limite configurado (default: U$8 por análise de sizing completo) — Atlas pausa, apresenta o breakdown de custo por worker e solicita aprovação explícita antes de continuar.
- [ ] **HITL** — NEW MARKET ENTRY RECOMMENDATION (L3): Quando Scout ranquear uma oportunidade com recomendação de ação imediata (ex: janela de entrada fechando em < 3 meses, sinal de concorrente se posicionando) — o alerta é escalado para o founder com nível de urgência explícito antes de qualquer automação de follow-up no ClickUp.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
