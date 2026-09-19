---
task: citadel()
responsavel: "Citadel"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Array bruto de chunks de todos os workers (claim + source_url + excerpt + credibility_raw)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Configuração de thresholds de credibilidade mínima por tipo de claim (números de tamanho de mercado: >= 3"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "narrativas estratégicas: >= 2)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Lista de domínios na whitelist de alta credibilidade"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Corpus normalizado com citações padronizadas e índice numerado de fontes"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Score de cobertura: % de claims quantitativos com citação credibilidade >= 3"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Lista de claims órfãos (sem fonte) e de dados com fonte de baixa credibilidade para revisão do Axiom"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Relatório de URLs indisponíveis (fontes que precisam ser substituídas)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Hash de rastreabilidade do corpus para audit trail"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado automaticamente após todos os workers concluírem, antes do Axiom. Processo determinístico — sem geração de conteúdo, apenas normalização, verificação de acessibilidade e classificação. Ativad…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Axiom 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: SIZING BRIEF APPROVAL (L3): Antes de Atlas disparar qualquer worker, o Sizing Brief com metodologia proposta, fontes-alvo e custo estimado de tokens é apresentado ao founder para aprovação explícita. Perguntas que envolvam sizing de mercados para M&A, captação ou due diligence de parceiros têm este gate obrigatório e não podem ser puladas."
    - "[ ] HITL: REGULATORY BARRIER FLAG (L1→L3): Quando Faro classifica uma barreira regulatória como Alta (ex: exige licença BACEN, certificação ANVISA, autorização CADE) — o Market Opportunity Report é retido e o founder recebe alerta com a barreira descrita. O SOM do relatório final é ajustado para refletir a barreira e marcado como 'pendente de validação jurídica' até que especialista humano confirme a análise. Inclui recomendação de consultor jurídico parceiro."
    - "[ ] HITL: CONVERGENCE FAILURE ALERT (L2→L3): Se Axiom detectar divergência > 60% entre os três métodos de sizing e os workers adicionais não resolverem o gap — o relatório é enviado ao founder com flag explícita de 'sizing com alta incerteza metodológica'. O founder decide se aceita o intervalo de incerteza ou solicita pesquisa adicional paga (escopo ampliado)."
    - "[ ] HITL: INVESTMENT MEMO / PITCH USE (L3): Quando o founder sinaliza que vai usar o Market Opportunity Report em pitch a investidores, board pack ou material de captação — Axiom executa uma rodada adicional de verificação adversarial de nível máximo (100% de claims quantitativos devem ter fonte credibilidade >= 4) e o founder deve revisar e assinar o relatório antes do envio externo. Nexar (Founder Clone) não escreve versão de pitch sem este gate."
    - "[ ] HITL: COST THRESHOLD (L3): Se a estimativa de custo de tokens de uma pesquisa superar o limite configurado (default: U$8 por análise de sizing completo) — Atlas pausa, apresenta o breakdown de custo por worker e solicita aprovação explícita antes de continuar."
---

# Classificar Credibilidade Fontes

**Task ID:** `citadel()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Market Sizing & Opportunity Scout — Founder Strategy Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Credibilidade Fontes |
| **status** | `pending` |
| **responsible_executor** | Citadel (Citadel — O Arquivista de Fontes) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de provenance e rastreabilidade. Processa todos os dados retornados pelos workers antes que cheguem ao Axiom. Normaliza citações em formato padrão (APA simplificado + URL + data de acesso + data de publicação da fonte), remove duplicatas, verifica se URLs estão acessíveis, classifica credibilidade da fonte (1-5: 5=dado primário oficial/relatório institucional publicado, 4=consultoria tier-1 ou publicação setorial, 3=veículo de negócios estabelecido/análise de banco, 2=blog de especialista/relatório de startup, 1=fórum/estimativa anedótica), e constrói o índice numerado de fontes do relatório final. Para dados quantitativos (TAM, SAM, SOM), aplica threshold mínimo: claims de tamanho de mercado exigem credibilidade >= 3. Garante que 100% dos números no output final tenham âncora de citação.

## Input

- Array bruto de chunks de todos os workers (claim + source_url + excerpt + credibility_raw)
- Configuração de thresholds de credibilidade mínima por tipo de claim (números de tamanho de mercado: >= 3
- narrativas estratégicas: >= 2)
- Lista de domínios na whitelist de alta credibilidade

## Output

- Corpus normalizado com citações padronizadas e índice numerado de fontes
- Score de cobertura: % de claims quantitativos com citação credibilidade >= 3
- Lista de claims órfãos (sem fonte) e de dados com fonte de baixa credibilidade para revisão do Axiom
- Relatório de URLs indisponíveis (fontes que precisam ser substituídas)
- Hash de rastreabilidade do corpus para audit trail

## Trigger

Ativado automaticamente após todos os workers concluírem, antes do Axiom. Processo determinístico — sem geração de conteúdo, apenas normalização, verificação de acessibilidade e classificação. Ativado novamente se Axiom solicitar dados adicionais e workers forem re-ativados.

## Knowledge base (o que o executor consulta)

- Whitelist de domínios de alta credibilidade por setor (lista curada e atualizada trimestralmente: IBGE, BACEN, CVM, Gartner, McKinsey, BCG, a16z, Statista, Bloomberg, Reuters, FGV, etc.)
- Regras de formatação de citação do squad
- Cache de URLs já verificadas na sessão
- Lista negra de fontes banidas (sites de estimativas não fundamentadas, conteúdo de IA não verificado como fonte primária)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Array bruto de chunks de todos os workers (claim + source_url + excerpt + credibility_raw)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Corpus normalizado com citações padronizadas e índice numerado de fontes) e persistir no artefato do squad.
4. Entregar ao critic Axiom 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Corpus normalizado com citações padronizadas e índice numerado de fontes
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Axiom 2 registrado
- [ ] Gate HITL respeitado: SIZING BRIEF APPROVAL (L3): Antes de Atlas disparar qualquer worker, o Sizing Brief com metodologia proposta, fontes-alvo e custo estimado…
- [ ] Gate HITL respeitado: REGULATORY BARRIER FLAG (L1→L3): Quando Faro classifica uma barreira regulatória como Alta (ex: exige licença BACEN, certificação ANVISA, a…
- [ ] Gate HITL respeitado: CONVERGENCE FAILURE ALERT (L2→L3): Se Axiom detectar divergência > 60% entre os três métodos de sizing e os workers adicionais não resolver…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — SIZING BRIEF APPROVAL (L3): Antes de Atlas disparar qualquer worker, o Sizing Brief com metodologia proposta, fontes-alvo e custo estimado de tokens é apresent… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — REGULATORY BARRIER FLAG (L1→L3): Quando Faro classifica uma barreira regulatória como Alta (ex: exige licença BACEN, certificação ANVISA, autorização CADE) — o… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — CONVERGENCE FAILURE ALERT (L2→L3): Se Axiom detectar divergência > 60% entre os três métodos de sizing e os workers adicionais não resolverem o gap — o relatór… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — INVESTMENT MEMO / PITCH USE (L3): Quando o founder sinaliza que vai usar o Market Opportunity Report em pitch a investidores, board pack ou material de captaçã… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — COST THRESHOLD (L3): Se a estimativa de custo de tokens de uma pesquisa superar o limite configurado (default: U$8 por análise de sizing completo) — Atlas paus… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — NEW MARKET ENTRY RECOMMENDATION (L3): Quando Scout ranquear uma oportunidade com recomendação de ação imediata (ex: janela de entrada fechando em < 3 meses, si… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Axiom 2 | BLOQUEIA entrega |

## Handoff

- **to:** Axiom
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
