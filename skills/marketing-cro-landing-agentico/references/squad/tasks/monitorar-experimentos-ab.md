---
task: darwin()
responsavel: "Darwin"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Especificações do experimento (hipótese, variações, métrica primária, métrica de guarda), volume de tráfego médio da página (para cálculo de duração), taxa de conversão baseline do controle, configurações da ferramenta de teste (Google Optimize, VWO, Unbounce Smart Traffic, Optimizely)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Experiment Setup Checklist (pre-launch: hipotese documentada, sample size calculado, duracao estimada, metricas configuradas, QA de tracking confirmado), Experiment Status Dashboard diario (variacoes, conversoes, significancia acumulada, velocidade de aprendizado), Experiment Conclusion Report ao encerrar (vencedor/perdedor/inconclusivo com p-value, lift absoluto e relativo, intervalo de confianca, recomendacao de proximo passo), alerta automatico de anomalia (queda subita de conversao em todas as variacoes = problema tecnico, nao CRO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro aprova experimento para go-live (Darwin configura e verifica tracking antes de publicar); job diário de monitoramento de todos os experimentos ativos; detecção de significância estatística (d…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Rex 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3): a empresa precisa concordar com o diagnóstico antes de escalar produção"
    - "[ ] HITL: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de produto ou páginas com > 50% do budget de tráfego (L3): mudanças de alto impacto requerem olho humano final"
    - "[ ] HITL: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qualquer reescrita (L3)"
    - "[ ] HITL: Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão estratégica que requer stakeholders (L3)"
    - "[ ] HITL: Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, métrica primária e budget de tráfego (L3)"
---

# Monitorar Experimentos Ab

**Task ID:** `darwin()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** CRO & Landing Page Agêntico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Experimentos Ab |
| **status** | `pending` |
| **responsible_executor** | Darwin (Darwin — Experiment Manager) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerenciador de experimentos e estatisticas do squad. Configura e monitora todos os testes A/B e multivariados: define splits de trafego, calcula tamanho minimo de amostra com poder estatistico de 80% e significancia de 95%, monitora daily velocity (visitas e conversoes por variacao), detecta automaticamente quando um experimento atingiu significancia estatistica ou quando deve ser encerrado por dano (variacao perdendo > 30% vs controle com p < 0.05). Nunca deixa um teste rodar alem do necessario nem o encerra cedo demais (evita peaking problem). Alias: 'Darwin' — a selecao natural das variacoes mais aptas a converter.

## Input

- Especificações do experimento (hipótese, variações, métrica primária, métrica de guarda), volume de tráfego médio da página (para cálculo de duração), taxa de conversão baseline do controle, configurações da ferramenta de teste (Google Optimize, VWO, Unbounce Smart Traffic, Optimizely)

## Output

- Experiment Setup Checklist (pre-launch: hipotese documentada, sample size calculado, duracao estimada, metricas configuradas, QA de tracking confirmado), Experiment Status Dashboard diario (variacoes, conversoes, significancia acumulada, velocidade de aprendizado), Experiment Conclusion Report ao encerrar (vencedor/perdedor/inconclusivo com p-value, lift absoluto e relativo, intervalo de confianca, recomendacao de proximo passo), alerta automatico de anomalia (queda subita de conversao em todas as variacoes = problema tecnico, nao CRO)

## Trigger

Maestro aprova experimento para go-live (Darwin configura e verifica tracking antes de publicar); job diário de monitoramento de todos os experimentos ativos; detecção de significância estatística (dispara encerramento e relatório); anomalia de conversão (queda > 20% em 24h); experimento ativo há mais de 4 semanas sem significância (dispara revisão de hipótese com Maestro)

## Knowledge base (o que o executor consulta)

- Configurações das ferramentas de teste (Google Optimize, VWO, Unbounce, Optimizely
- por cliente), fórmulas de cálculo de sample size e poder estatístico, histórico de todos os experimentos com resultados e metadados, conhecimento de armadilhas estatísticas comuns (peaking, multiple testing problem, Simpson's paradox em segmentação), mapeamento de métricas de guarda por tipo de página (ex: não aumentar conversão às custas de aumentar churn em 30 dias)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Especificações do experimento (hipótese, variações, métrica primária, métrica de guarda), volume de tráfego médio da pá…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Experiment Setup Checklist (pre-launch: hipotese documentada, sample size calculado, duracao estimada, metricas configu…) e persistir no artefato do squad.
4. Entregar ao critic Rex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Experiment Setup Checklist (pre-launch: hipotese documentada, sample size calculado, duracao estimada, metricas configuradas, QA de tracking confirmado), Exper…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Rex 2 registrado
- [ ] Gate HITL respeitado: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção d…
- [ ] Gate HITL respeitado: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na pág…
- [ ] Gate HITL respeitado: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel lega…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3)… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de pro… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qu… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão es… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, m… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Escalada de experimento inconclusivo após 4 semanas — Darwin alerta, Maestro analisa, mas decisão de encerrar ou aumentar tráfego para o teste e humana (L1): i… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao trimestral do CRO Playbook — Atlas apresenta o estado do conhecimento acumulado, Growth Lead decide quais learnings viram regras permanentes e quais hi… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Rex 2 | BLOQUEIA entrega |

## Handoff

- **to:** Rex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
