---
task: aegis()
responsavel: "Aegis"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Vendor candidato para avaliacao (nome, URL, categoria, caso de uso pretendido, dados que vao trafegar ou ser armazenados), Stack Audit atual de Nox (context de como o vendor se integra ao restante do stack), nivel de sensibilidade de dados definido pelo founder no Discovery (que categorias de dados sao criticas"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "PII de clientes, dados financeiros, dados de produto, etc.), jurisdicao legal da empresa e setor regulatorio (define quais requisitos de compliance sao obrigatorios versus opcionais), documentos contratuais do vendor para analise (ToS, DPA, SLA"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "quando disponiveis)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Vendor Risk Assessment Report (estrutura padrao: Risk Score agregado 0-10 por dimensao com breakdown, Red Flags listados (qualquer dimensao com score abaixo de 5 e automaticamente Red Flag), Blocking Issues (items que devem ser resolvidos antes da adocao"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "ex: sem DPA disponivel para vendor que vai processar PII e blocking), Conditional Approvals (pode adotar se vendor fornecer X ou se usar apenas para caso de uso Y), Due Diligence Checklist para negociacao contratual com o vendor"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "o que exigir no contrato para mitigar os riscos identificados), Vendor Compliance Status (APPROVED/CONDITIONAL/BLOCKED com justificativa), Compliance Monitoring Alert quando Aegis detecta mudanca em ToS ou DPA de vendor Tier 1 que requer atencao do founder (com prazo estimado para resolver antes de impacto)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Kai finaliza BvB Analysis com recomendacao de vendor especifico para Tier 1 ou Tier 2 (Aegis executa Vendor Risk Assessment antes de qualquer recomendacao final chegar ao founder — gate obrigatorio p…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic ARIA 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criticidade (Tier 1/2/3), e os criterios de threshold que trigam BvB Analysis automatica (custo minimo, nivel de impacto). Gate L3 obrigatorio — sem esta aprovacao o squad nao opera em producao. Define o escopo de toda a operacao"
    - "[ ] HITL: Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/Trial/Assess/Hold, questionam posicionamentos que parecem incorretos com base em contexto interno nao capturado, e assinam o Vendor Risk Register inicial. Gate L3 — este documento se torna a linha de base de toda decisao futura"
    - "[ ] HITL: Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPROVED com condicoes) + Gaia envia Decision Package consolidado para aprovacao explicita do founder/CTO via ClickUp task. Irreversivel por natureza: contratos assinados, integracao implementada e dados migrados sao difficeis e caros de desfazer"
    - "[ ] HITL: Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do threshold (ex: 3 meses de engenheiro ou R$50k) requer aprovacao explicita do founder com ARIA Worst-Case Scenarios documentados. Irreversivel: capacidade de engenheiro desviada nao pode ser recuperada"
    - "[ ] HITL: Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology Roadmap Recommendations para os proximos 2 trimestres. Gate L3: founder/CTO aprovam as recomendacoes antes de se tornarem diretriz tecnica do squad. Incluido no calendario de governanca do founder"
---

# Avaliar Risco Vendor

**Task ID:** `aegis()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Tech Radar & Build-vs-Buy Intelligence

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Avaliar Risco Vendor |
| **status** | `pending` |
| **responsible_executor** | Aegis (Aegis — Assessor de Risco de Vendor & Compliance) |
| **execution_type** | `Agent` |
| **input** | 3 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em due diligence de risco de vendor e compliance tecnico — avalia dimensoes de risco que o BvB-7 de Kai nao cobre em profundidade: seguranca, privacidade de dados, conformidade regulatoria, estabilidade financeira do vendor e riscos de dependencia critica. Opera em dois modos: (1) VENDOR DUE DILIGENCE MODE — para qualquer vendor candidato a Tier 1 ou Tier 2 identificado por Kai ou Vera, Aegis executa o Vendor Risk Assessment de 6 dimensoes: (a) Security Posture — certificacoes de seguranca (SOC 2, ISO 27001, PCI-DSS se relevante), historico de incidentes de seguranca publicos, politicas de responsible disclosure, SLA de resposta a vulnerabilidades; (b) Data Privacy & Compliance — onde os dados sao armazenados (jurisdicao), compliance com LGPD/GDPR, DPA disponivel, clausulas de subprocessadores, politica de retencao e exclusao de dados, transferencia internacional; (c) Vendor Financial Health — indicadores publicos de saude financeira (rodadas recentes, crescimento de receita se publicado, tamanho de time via LinkedIn, sinais de runway), historico de acquisicoes ou pivots que impactaram clientes, concentracao de receita (dependencia de poucos grandes clientes — risco de pivote de produto); (d) Contractual Lock-in — analise do contrato: clausulas de exclusividade, custo de saida, portabilidade de dados (posso exportar tudo em formato aberto?), direitos de auditoria, SLA e penalidades, clausulas de mudanca unilateral de preco; (e) Operational Concentration — se o vendor cai ou e adquirido, qual e o impacto operacional real em horas? existe plano de continuidade documentado?; (f) Regulatory Fit — o vendor e adequado para o setor regulado do cliente? ha restricoes especificas (ex: dados financeiros, saude, educacao infantil)? (2) COMPLIANCE MONITORING MODE — monitora continuamente mudancas regulatorias relevantes para o stack atual (LGPD, novas exigencias de compliance do setor) e mudancas nos ToS e DPAs de vendors Tier 1 que possam gerar risco nao declarado.

## Input

- Vendor candidato para avaliacao (nome, URL, categoria, caso de uso pretendido, dados que vao trafegar ou ser armazenados), Stack Audit atual de Nox (context de como o vendor se integra ao restante do stack), nivel de sensibilidade de dados definido pelo founder no Discovery (que categorias de dados sao criticas
- PII de clientes, dados financeiros, dados de produto, etc.), jurisdicao legal da empresa e setor regulatorio (define quais requisitos de compliance sao obrigatorios versus opcionais), documentos contratuais do vendor para analise (ToS, DPA, SLA
- quando disponiveis)

## Output

- Vendor Risk Assessment Report (estrutura padrao: Risk Score agregado 0-10 por dimensao com breakdown, Red Flags listados (qualquer dimensao com score abaixo de 5 e automaticamente Red Flag), Blocking Issues (items que devem ser resolvidos antes da adocao
- ex: sem DPA disponivel para vendor que vai processar PII e blocking), Conditional Approvals (pode adotar se vendor fornecer X ou se usar apenas para caso de uso Y), Due Diligence Checklist para negociacao contratual com o vendor
- o que exigir no contrato para mitigar os riscos identificados), Vendor Compliance Status (APPROVED/CONDITIONAL/BLOCKED com justificativa), Compliance Monitoring Alert quando Aegis detecta mudanca em ToS ou DPA de vendor Tier 1 que requer atencao do founder (com prazo estimado para resolver antes de impacto)

## Trigger

Kai finaliza BvB Analysis com recomendacao de vendor especifico para Tier 1 ou Tier 2 (Aegis executa Vendor Risk Assessment antes de qualquer recomendacao final chegar ao founder — gate obrigatorio para Tier 1); Vera detecta mudanca em ToS, DPA ou politica de seguranca de vendor Tier 1 ou Tier 2 ativo (Compliance Monitoring Alert em menos de 24h); novo vendor adicionado ao stack pelo CTO sem passar pelo pipeline de BvB (Aegis executa retroativamente — gate de qualidade); ciclo trimestral de revisao de Vendor Risk Scores para todos os Tier 1 (Vendor Health Review); mudanca regulatoria relevante detectada por Vera que impacta dados processados pelo stack atual

## Knowledge base (o que o executor consulta)

- Biblioteca de requisitos de compliance por setor e jurisdicao (LGPD, GDPR, PCI-DSS, HIPAA se aplicavel, Marco Civil da Internet, regulacoes especificas do setor do cliente
- atualizada por Vera), templates de Vendor Risk Assessment por categoria de vendor (SaaS de dados, infraestrutura cloud, ferramentas de comunicacao, processamento de pagamento tem perfis de risco distintos), historico de Vendor Risk Assessments para nao repetir due diligence desnecessaria (se vendor X foi avaliado ha 6 meses e nada mudou, reusar com delta), Red Flags conhecidos de vendors especificos (historico de incidentes publicos, litigios, acquisicoes que degradaram produto
- memoria institucional do squad), DPA templates e clausulas padrao para negociacao contratual (o que um contrato bem estruturado com vendor de dados deve conter)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Vendor candidato para avaliacao (nome, URL, categoria, caso de uso pretendido, dados que vao trafegar ou ser armazenado…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Vendor Risk Assessment Report (estrutura padrao: Risk Score agregado 0-10 por dimensao com breakdown, Red Flags listado…) e persistir no artefato do squad.
4. Entregar ao critic ARIA 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Vendor Risk Assessment Report (estrutura padrao: Risk Score agregado 0-10 por dimensao com breakdown, Red Flags listados (qualquer dimensao com score abaixo de…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic ARIA 2 registrado
- [ ] Gate HITL respeitado: Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as cla…
- [ ] Gate HITL respeitado: Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes n…
- [ ] Gate HITL respeitado: Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adve…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criti… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPRO… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology R… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisao de Vendor Risk Alerts gerados por Aegis para vendors Tier 1 ativos — quando Aegis detecta mudanca em ToS, DPA ou historico de incidente de seguranca em… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Aprovacao de movimentos de quadrante com impacto em sistemas Tier 1 — quando Nox propoe mover componente Tier 1 para HOLD ou Tier 1/2 para ADOPT, gate L2 (CTO… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Conditions Review Reminder de Gaia — quando as condicoes de revisao de um ADR sao atingidas (preco do vendor ultrapassou threshold, data de revisao chegou, Loc… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic ARIA 2 | BLOQUEIA entrega |

## Handoff

- **to:** ARIA
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
