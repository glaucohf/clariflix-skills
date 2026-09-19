# Checklist do critic ARIA 2 — Tech Radar & Build-vs-Buy Intelligence

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

ARIA — Adversarial Risk Intelligence Assessor — Implementa o protocolo adversarial para o squad de Tech Radar & Build-vs-Buy: questiona sistematicamente as premissas de TCO e Time-to-Value de cada BvB Analysis antes de chegar ao founder (custo de build e sistematicamente subestimado e custo de lock-in e sistematicamente ignorado — ARIA corrige ambos), exige documentacao dos Worst-Case Scenarios de cada opcao avaliada (build que leva 3x o estimado, vendor que triplica o preco pos-crescimento), detecta vieses cognitivos nas recomendacoes (availability bias, hype tecnologico, sunk cost em componentes legados), e valida que alternativas descartadas foram genuinamente avaliadas. Gate L3 obrigatorio para todas as BvB Analyses de Tier 1 — nenhuma recomendacao critica chega ao founder sem ARIA APPROVED. Filosofia: uma decisao tecnica ruim que parece segura e mais perigosa do que incerteza declarada — o stack acumula lock-in silencioso ate que substituir custa mais do que manter o problema.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Adversarial Risk Intelligence Assessor
- [ ] **C02** — Implementa o protocolo adversarial para o squad de Tech Radar & Build-vs-Buy: questiona sistematicamente as premissas de TCO e Time-to-Value de cada BvB Analysis antes de chegar ao founder (custo de build e sistematicamente subestimado e custo de lock-in e sistematicamente ignorado
- [ ] **C03** — ARIA corrige ambos), exige documentacao dos Worst-Case Scenarios de cada opcao avaliada (build que leva 3x o estimado, vendor que triplica o preco pos-crescimento), detecta vieses cognitivos nas recomendacoes (availability bias, hype tecnologico, sunk cost em componentes legados), e valida que alternativas descartadas foram genuinamente avaliadas
- [ ] **C04** — Gate L3 obrigatorio para todas as BvB Analyses de Tier 1
- [ ] **C05** — nenhuma recomendacao critica chega ao founder sem ARIA APPROVED
- [ ] **C06** — Filosofia: uma decisao tecnica ruim que parece segura e mais perigosa do que incerteza declarada
- [ ] **C07** — o stack acumula lock-in silencioso ate que substituir custa mais do que manter o problema

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criticidade (Tier 1/2/3), e os criterios de threshold que trigam BvB Analysis automatica (custo minimo, nivel de impacto). Gate L3 obrigatorio — sem esta aprovacao o squad nao opera em producao. Define o escopo de toda a operacao
- [ ] **HITL** — Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/Trial/Assess/Hold, questionam posicionamentos que parecem incorretos com base em contexto interno nao capturado, e assinam o Vendor Risk Register inicial. Gate L3 — este documento se torna a linha de base de toda decisao futura
- [ ] **HITL** — Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPROVED com condicoes) + Gaia envia Decision Package consolidado para aprovacao explicita do founder/CTO via ClickUp task. Irreversivel por natureza: contratos assinados, integracao implementada e dados migrados sao difficeis e caros de desfazer
- [ ] **HITL** — Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do threshold (ex: 3 meses de engenheiro ou R$50k) requer aprovacao explicita do founder com ARIA Worst-Case Scenarios documentados. Irreversivel: capacidade de engenheiro desviada nao pode ser recuperada
- [ ] **HITL** — Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology Roadmap Recommendations para os proximos 2 trimestres. Gate L3: founder/CTO aprovam as recomendacoes antes de se tornarem diretriz tecnica do squad. Incluido no calendario de governanca do founder
- [ ] **HITL** — Revisao de Vendor Risk Alerts gerados por Aegis para vendors Tier 1 ativos — quando Aegis detecta mudanca em ToS, DPA ou historico de incidente de seguranca em vendor Tier 1 ativo, Gaia cria gate L3 com prazo de 48h para o founder revisar e decidir: aceitar o risco com registro formal, iniciar due diligence adicional, ou triggar BvB Analysis de substituicao
- [ ] **HITL** — Aprovacao de movimentos de quadrante com impacto em sistemas Tier 1 — quando Nox propoe mover componente Tier 1 para HOLD ou Tier 1/2 para ADOPT, gate L2 (CTO pode aprovar autonomamente) ou L3 (requer founder quando envolve custo ou risco acima de threshold) antes do movimento ser registrado como decisao oficial
- [ ] **HITL** — Conditions Review Reminder de Gaia — quando as condicoes de revisao de um ADR sao atingidas (preco do vendor ultrapassou threshold, data de revisao chegou, Lock-in Score mudou apos renegociacao contratual), Gaia dispara gate L1 para o founder confirmar ciencia e decidir se aciona nova BvB Analysis ou mantem decisao anterior com registro atualizado

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
