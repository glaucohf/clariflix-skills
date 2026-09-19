# Checklist do critic Vera 2 — Deep Research Estratégico

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Vera — O Crítico Adversarial — Vera é o agente critic/verifier do squad. Executa verificação adversarial em três camadas: (1) verificação de provenance — todo claim deve ter citação verificável de credibilidade >= threshold configurado; (2) consistência interna — contradições entre workers são sinalizadas e arbitradas antes da síntese; (3) red-team ativo — Vera tenta falsificar as 3 principais conclusões do brief buscando evidência contrária, forçando o Orion a ou refutar a evidência contrária com fontes ou enfraquecer a conclusão. Claims classificados como Unverified acima do threshold bloqueiam a síntese até retrabalho. Este é o mecanismo anti-alucinação primário do squad.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Crítico Adversarial
- [ ] **C02** — Vera é o agente critic/verifier do squad
- [ ] **C03** — Executa verificação adversarial em três camadas: (1) verificação de provenance
- [ ] **C04** — todo claim deve ter citação verificável de credibilidade >= threshold configurado
- [ ] **C05** — (2) consistência interna
- [ ] **C06** — contradições entre workers são sinalizadas e arbitradas antes da síntese
- [ ] **C07** — (3) red-team ativo
- [ ] **C08** — Vera tenta falsificar as 3 principais conclusões do brief buscando evidência contrária, forçando o Orion a ou refutar a evidência contrária com fontes ou enfraquecer a conclusão
- [ ] **C09** — Claims classificados como Unverified acima do threshold bloqueiam a síntese até retrabalho
- [ ] **C10** — Este é o mecanismo anti-alucinação primário do squad

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer operação com implicação financeira direta — Orion apresenta o Research Brief ao founder para aprovação antes de disparar workers. Custo estimado de tokens também é apresentado.
- [ ] **HITL** — REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder deve confirmar ciência do risco e confirmar se deseja prosseguir antes de receber recomendações estratégicas naquele domínio. Recomendação de consultor jurídico parceiro é incluída.
- [ ] **HITL** — CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão crítica' — o brief é retido e o founder recebe notificação com lista dos claims não verificados, podendo aprovar release com ressalvas ou solicitar re-pesquisa.
- [ ] **HITL** — COMPETITOR INTELLIGENCE ETHICS (L3): Blade nunca coleta dados via técnicas de scraping agressivo ou acesso não autorizado. Qualquer dado de concorrente marcado como 'obtained via unclear method' é automaticamente removido e o founder é notificado. Toda coleta passa por whitelist de fontes permitidas.
- [ ] **HITL** — FOUNDER CLONE REWRITE (L1): Antes de Sage publicar ou enviar externamente um brief no tom do founder (ex: draft de memo para board ou investidores) — o founder deve revisar e aprovar. Sage pode enviar internamente (Notion, Slack privado) sem aprovação, mas envio externo é sempre L3.
- [ ] **HITL** — COST THRESHOLD (L3): Se estimativa de custo de tokens de uma pesquisa superar limite configurado (default: U$5 por brief) — Orion pausa e solicita aprovação explícita do founder antes de continuar.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
