---
name: founder-competitive-intelligence
description: Use para pesquisar concorrentes, consolidar mudanças de mercado e preparar inteligência competitiva com fontes
  verificáveis.
version: 0.2.0
author: Gerado da especificação de Gabriel Marcondes (Máquina de Receita · A Máquina) pela Academia Lendária
license: Proprietary
platforms:
- linux
- macos
- windows
required_environment_variables: []
metadata:
  hermes:
    tags:
    - gestao
    - squad
    - maquina-de-receita
    related_skills: []
---

# Inteligência Competitiva Contínua

Pesquisar concorrentes, consolidar mudanças de mercado e preparar inteligência competitiva com fontes verificáveis.

Adaptação do squad de Founder Office da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para pesquisar concorrentes, consolidar mudanças de mercado e preparar inteligência competitiva com fontes verificáveis.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Atlas | [papel do orquestrador](references/squad/agents/atlas.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/founder-competitive-intelligence-pipeline.yaml) |
| Verificação das saídas | [critic-veritas-2](references/squad/checklists/critic-veritas-2.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Atlas** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/founder-competitive-intelligence-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Atlas](references/squad/agents/atlas.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Coletar Sinais Competitivos | [Hawk](references/squad/agents/hawk.md) | [coletar-sinais-competitivos](references/squad/tasks/coletar-sinais-competitivos.md) |
| Classificar Movimentos Estrategicos | [Lynx](references/squad/agents/lynx.md) | [classificar-movimentos-estrategicos](references/squad/tasks/classificar-movimentos-estrategicos.md) |
| Simular Cenários Estratégicos | [Ares](references/squad/agents/ares.md) | [simular-cenarios-estrategicos](references/squad/tasks/simular-cenarios-estrategicos.md) |
| Enviar Alertas Formatados | [Hermes](references/squad/agents/hermes.md) | [enviar-alertas-formatados](references/squad/tasks/enviar-alertas-formatados.md) |
| Sintetizar Inteligência Competitiva | [Memo](references/squad/agents/memo.md) | [sintetizar-inteligencia-competitiva](references/squad/tasks/sintetizar-inteligencia-competitiva.md) |
| Verificar Qualidade Da Evidencia | [Veritas](references/squad/agents/veritas.md) | [verificar-qualidade-da-evidencia](references/squad/tasks/verificar-qualidade-da-evidencia.md) |
| Verificação do critic | [Veritas 2](references/squad/agents/veritas-2.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Atlas](references/squad/agents/atlas.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/founder-competitive-intelligence/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/founder-competitive-intelligence-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovação do Competitive Map no Discovery (Semana 2) — founder valida e assina a lista de concorrentes por tier, fontes de monitoramento por concorrente, critérios de alerta por categoria de movimento e janela de reação por tipo antes de qualquer monitoramento ir ao ar (L3, gate obrigatório — define o escopo de toda a operação e a sensibilidade dos alertas)
- **HITL** — Calibração do Corpus do Founder para Ares (Semana 3-4) — founder revisa e valida os frameworks de decisão estratégica, o posicionamento atual e as restrições reais do negócio capturados por Atlas para alimentar o Wargame Engine — sem calibração, as contra-jogadas de Ares são genéricas (L3, input crítico que define qualidade das recomendações)
- **HITL** — Validação do Competitive Intelligence Baseline (fim do Deep Dive) — founder revisa o primeiro snapshot completo de todos os Tier 1, confirma se as classificações de movimento fazem sentido para o contexto real do mercado e calibra thresholds de scoring de Lynx (L3, calibração crítica antes de produção)
- **HITL** — Aprovação de Competitive Flash antes de Counter-Play urgente (score >= 9 em Tier 1) — quando Hermes recebe sinal CRÍTICO aprovado por Veritás, o founder deve confirmar ciência e decisão antes de qualquer ação irreversível ser executada (L3, irreversível por natureza — resposta competitiva errada pode ser pior que nenhuma resposta)
- **HITL** — Revisão mensal do Competitive Landscape Report — founder revisa com Atlas o cenário competitivo do mês, valida os cenários de wargame de Ares para os próximos 90 dias, aprova os playbooks de resposta como diretriz estratégica e ajusta os critérios de alerta do Competitive Map se necessário (L3, governança estratégica mensal obrigatória)
- **HITL** — Aprovação pré-distribuição de Board Intelligence Pack e Decision Intelligence Brief de Memo — qualquer documento de Memo deve ser revisado e aprovado pelo founder antes de chegar à board ou investidores (L3, irreversível — documento compartilhado externamente não tem recall)
- **HITL** — Calibracao trimestral de scoring de Lynx — founder revisa junto com Atlas e Veritas os falsos positivos e falsos negativos dos ultimos 90 dias, ajusta os pesos de scoring por categoria e tier, e valida se os Movement Profiles de concorrentes Tier 1 estao acurados (L1, ciclo de melhoria continua da qualidade do squad)
- **HITL** — Quando Veritas retorna BLOCKED em gate de rastreabilidade ou hipótese inflatada — revisão obrigatória do founder antes de reprocessamento ou descarte do item, com log da razão do bloqueio para calibração futura (L3, risco de decisão estratégica baseada em inteligência de baixa qualidade)

7. Aplique [critic-veritas-2](references/squad/checklists/critic-veritas-2.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
8. Consolide o entregável definido no workflow para o escopo solicitado, distinguindo resultado produzido, hipótese, pendência e ação externa confirmada. Preserve aprovações e fontes junto dos artefatos.

## Pitfalls

- Os percentuais, SLAs, benchmarks e projeções do material original são hipóteses ou metas da especificação; não são resultados comprovados nem garantias desta skill.
- Serviços e bases externas mencionados nas referências não são instalados por este pacote. Verifique disponibilidade e documentação vigente quando forem necessários.
- Não aceite uma saída só por estar bem formatada: aplique o critic e os vetos antes de qualquer entrega ou ação dependente.
- Os arquivos originais são um snapshot. Referências a outros squads ou ao workspace do autor não autorizam execução nem substituem um recurso realmente disponível.

## Verification

- As tarefas selecionadas têm entradas suficientes e saídas rastreáveis aos dados usados.
- O checklist do critic foi aplicado, com evidência e veredito por item.
- Gates aplicáveis possuem decisão humana registrada; etapas bloqueadas estão identificadas.
- O entregável contém fontes, hipóteses e pendências, sem apresentar simulação ou planejamento como execução externa.
- Métricas realizadas foram medidas; metas do material original permanecem identificadas como metas.
