---
name: founder-agentic-analytics
description: Use para analisar indicadores do negócio, investigar variações e preparar recomendações rastreáveis para o founder.
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

# Ágentic Analytics

Analisar indicadores do negócio, investigar variações e preparar recomendações rastreáveis para o founder.

Adaptação do squad de Founder Office da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para analisar indicadores do negócio, investigar variações e preparar recomendações rastreáveis para o founder.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Orquestrador Analítico | [papel do orquestrador](references/squad/agents/orquestrador-analitico.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/founder-agentic-analytics-pipeline.yaml) |
| Verificação das saídas | [critic-sql-semantic-verifier](references/squad/checklists/critic-sql-semantic-verifier.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Orquestrador Analítico** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/founder-agentic-analytics-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Orquestrador Analítico](references/squad/agents/orquestrador-analitico.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Traduzir Pergunta Para Sql | [Text-to-SQL Worker](references/squad/agents/text-to-sql-worker.md) | [traduzir-pergunta-para-sql](references/squad/tasks/traduzir-pergunta-para-sql.md) |
| Enriquecer Resultado Com Contexto | [Context Enricher](references/squad/agents/context-enricher.md) | [enriquecer-resultado-com-contexto](references/squad/tasks/enriquecer-resultado-com-contexto.md) |
| Detectar Anomalias Estatísticas | [Anomaly & Alert Detector](references/squad/agents/anomaly-alert-detector.md) | [detectar-anomalias-estatisticas](references/squad/tasks/detectar-anomalias-estatisticas.md) |
| Sintetizar Respostas Analíticas | [Strategic Query Analyst](references/squad/agents/strategic-query-analyst.md) | [sintetizar-respostas-analiticas](references/squad/tasks/sintetizar-respostas-analiticas.md) |
| Registrar Gap Semantico | [Semantic Layer Guardian](references/squad/agents/semantic-layer-guardian.md) | [registrar-gap-semantico](references/squad/tasks/registrar-gap-semantico.md) |
| Registrar Decisões Baseadas em Dados | [Decision Logger](references/squad/agents/decision-logger.md) | [registrar-decisoes-baseadas-em-dados](references/squad/tasks/registrar-decisoes-baseadas-em-dados.md) |
| Verificação do critic | [SQL & Semantic Verifier](references/squad/agents/sql-semantic-verifier.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Orquestrador Analítico](references/squad/agents/orquestrador-analitico.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/founder-agentic-analytics/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/founder-agentic-analytics-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovação de nova métrica na camada semântica (Ariadne propõe, founder ou data owner aprova antes de adicionar ao schema — L3, irreversível pois altera definições que afetam todas as queries futuras)
- **HITL** — Resolução de conflito de definição entre métricas (quando duas métricas existentes têm definições inconsistentes, founder decide qual é a oficial — L3)
- **HITL** — Configuração de thresholds de alerta para Cassandra (founder define o que é 'crítico' vs 'atenção' para cada métrica do seu negócio — L3 no setup inicial, L2 depois)
- **HITL** — Confirmação de decisão tomada com base em dados para o Clío registrar (founder confirma que vai agir — não é automático para evitar log de decisões não tomadas)
- **HITL** — Acesso a novas fontes de dados não mapeadas (conectar novo banco, nova planilha, nova API ao schema — L3 por impacto na governança)

7. Aplique [critic-sql-semantic-verifier](references/squad/checklists/critic-sql-semantic-verifier.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
