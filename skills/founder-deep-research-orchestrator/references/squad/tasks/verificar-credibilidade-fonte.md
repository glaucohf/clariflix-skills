---
task: parallax()
responsavel: "Parallax"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Array bruto de chunks de todos os workers (claim + source_url + excerpt)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Configuração de thresholds de credibilidade mínima por tipo de claim (ex: claims financeiros requerem fonte credibilidade >= 3)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Corpus normalizado com citações padronizadas e índice numerado de fontes"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Score de cobertura: % de claims com citação verificada"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Lista de claims órfãos (sem fonte) para revisão do Critic"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Relatório de fontes indisponíveis ou de baixa credibilidade"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado automaticamente após todos os workers concluírem, antes do Critic. Processo determinístico — sem geração de conteúdo, apenas normalização e verificação estrutural."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vera 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer operação com implicação financeira direta — Orion apresenta o Research Brief ao founder para aprovação antes de disparar workers. Custo estimado de tokens também é apresentado."
    - "[ ] HITL: REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder deve confirmar ciência do risco e confirmar se deseja prosseguir antes de receber recomendações estratégicas naquele domínio. Recomendação de consultor jurídico parceiro é incluída."
    - "[ ] HITL: CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão crítica' — o brief é retido e o founder recebe notificação com lista dos claims não verificados, podendo aprovar release com ressalvas ou solicitar re-pesquisa."
    - "[ ] HITL: COMPETITOR INTELLIGENCE ETHICS (L3): Blade nunca coleta dados via técnicas de scraping agressivo ou acesso não autorizado. Qualquer dado de concorrente marcado como 'obtained via unclear method' é automaticamente removido e o founder é notificado. Toda coleta passa por whitelist de fontes permitidas."
    - "[ ] HITL: FOUNDER CLONE REWRITE (L1): Antes de Sage publicar ou enviar externamente um brief no tom do founder (ex: draft de memo para board ou investidores) — o founder deve revisar e aprovar. Sage pode enviar internamente (Notion, Slack privado) sem aprovação, mas envio externo é sempre L3."
---

# Verificar Credibilidade Fonte

**Task ID:** `parallax()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Deep Research Estratégico — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Credibilidade Fonte |
| **status** | `pending` |
| **responsible_executor** | Parallax (Parallax — O Guardião de Citações) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de provenance e rastreabilidade. Processa todos os chunks retornados pelos workers antes que cheguem ao Critic. Normaliza citações em formato padrão (APA simplificado + URL + data de acesso), remove duplicatas, verifica se URLs estão acessíveis, classifica credibilidade da fonte (1-5: 5=paper revisado/relatório institucional, 4=publicação setorial estabelecida, 3=veículo de negócios, 2=blog de especialista, 1=fórum/redes sociais), e constrói o índice de fontes do brief final. Garante que 100% dos claims no output final tenham âncora de citação.

## Input

- Array bruto de chunks de todos os workers (claim + source_url + excerpt)
- Configuração de thresholds de credibilidade mínima por tipo de claim (ex: claims financeiros requerem fonte credibilidade >= 3)

## Output

- Corpus normalizado com citações padronizadas e índice numerado de fontes
- Score de cobertura: % de claims com citação verificada
- Lista de claims órfãos (sem fonte) para revisão do Critic
- Relatório de fontes indisponíveis ou de baixa credibilidade

## Trigger

Ativado automaticamente após todos os workers concluírem, antes do Critic. Processo determinístico — sem geração de conteúdo, apenas normalização e verificação estrutural.

## Knowledge base (o que o executor consulta)

- Whitelist de domínios de alta credibilidade por setor (lista curada)
- Regras de formatação de citação do squad
- Cache de URLs já verificadas na sessão
- Histórico de fontes banidas ou de baixa qualidade

## Action Items

1. Confirmar o gatilho e carregar a entrada (Array bruto de chunks de todos os workers (claim + source_url + excerpt)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Corpus normalizado com citações padronizadas e índice numerado de fontes) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Corpus normalizado com citações padronizadas e índice numerado de fontes
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vera 2 registrado
- [ ] Gate HITL respeitado: INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer op…
- [ ] Gate HITL respeitado: REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder…
- [ ] Gate HITL respeitado: CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer operação com implicaçã… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder deve confirmar ciên… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão crítica' — o brief… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — COMPETITOR INTELLIGENCE ETHICS (L3): Blade nunca coleta dados via técnicas de scraping agressivo ou acesso não autorizado. Qualquer dado de concorrente marcado… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — FOUNDER CLONE REWRITE (L1): Antes de Sage publicar ou enviar externamente um brief no tom do founder (ex: draft de memo para board ou investidores) — o founder… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — COST THRESHOLD (L3): Se estimativa de custo de tokens de uma pesquisa superar limite configurado (default: U$5 por brief) — Orion pausa e solicita aprovação ex… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Vera 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vera
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
