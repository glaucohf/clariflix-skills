# Checklist do critic Vera 2 — Living ICP Profiler

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Vera — Critic & Data Quality Verifier — Implementa o padrão Skeptic Protocol para o squad: desafia cada versão do ICP antes de publicação, detecta data quality issues, valida conformidade LGPD/GDPR, identifica inconsistências entre fontes de enriquecimento e alerta quando o ICP proposto contradiz o histórico de performance. Gate L3 obrigatório — nenhuma versão de ICP é publicada sem aprovação de Vera.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic & Data Quality Verifier
- [ ] **C02** — Implementa o padrão Skeptic Protocol para o squad: desafia cada versão do ICP antes de publicação, detecta data quality issues, valida conformidade LGPD/GDPR, identifica inconsistências entre fontes de enriquecimento e alerta quando o ICP proposto contradiz o histórico de performance
- [ ] **C03** — Gate L3 obrigatório
- [ ] **C04** — nenhuma versão de ICP é publicada sem aprovação de Vera

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3)
- [ ] **HITL** — Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3)
- [ ] **HITL** — Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)
- [ ] **HITL** — Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3)
- [ ] **HITL** — Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1)
- [ ] **HITL** — Aprovação de integração com nova fonte de dados de enriquecimento que implica custo adicional — qualquer nova ferramenta paga requer validação financeira (L3)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
