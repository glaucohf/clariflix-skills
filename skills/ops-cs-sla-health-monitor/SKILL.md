---
name: ops-cs-sla-health-monitor
description: Use para analisar prazos de SLA e saúde operacional, priorizar riscos e preparar escalonamentos com contexto.
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
    - operacoes
    - squad
    - maquina-de-receita
    related_skills: []
---

# SLA & Health Monitoring Operacional

Analisar prazos de SLA e saúde operacional, priorizar riscos e preparar escalonamentos com contexto.

Adaptação do squad de Operações & CS da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para analisar prazos de SLA e saúde operacional, priorizar riscos e preparar escalonamentos com contexto.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Sentinela-Mor (persona: Vítor, analista sênior de operações com obsessão por SLA | [papel do orquestrador](references/squad/agents/sentinela-mor-persona-vitor-analista-senior-de-operacoes-com-obsessao-por-sla.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/ops-cs-sla-health-monitor-pipeline.yaml) |
| Verificação das saídas | [critic-cetico-de-sla](references/squad/checklists/critic-cetico-de-sla.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Sentinela-Mor (persona: Vítor, analista sênior de operações com obsessão por SLA** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/ops-cs-sla-health-monitor-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Sentinela-Mor (persona: Vítor, analista sênior de operações com obsessão por SLA](references/squad/agents/sentinela-mor-persona-vitor-analista-senior-de-operacoes-com-obsessao-por-sla.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Coletar Tickets Sla | [Radar](references/squad/agents/radar.md) | [coletar-tickets-sla](references/squad/tasks/coletar-tickets-sla.md) |
| Calcular Complexidade Tickets | [Decifra](references/squad/agents/decifra.md) | [calcular-complexidade-tickets](references/squad/tasks/calcular-complexidade-tickets.md) |
| Calcular Probabilidade De Breach | [Cronos](references/squad/agents/cronos.md) | [calcular-probabilidade-de-breach](references/squad/tasks/calcular-probabilidade-de-breach.md) |
| Escalonar Tickets | [Alarme](references/squad/agents/alarme.md) | [escalonar-tickets](references/squad/tasks/escalonar-tickets.md) |
| Analisar Dados De SLA | [Histos](references/squad/agents/histos.md) | [analisar-dados-de-sla](references/squad/tasks/analisar-dados-de-sla.md) |
| Registrar Prova De Trabalho | [Âncora](references/squad/agents/ancora.md) | [registrar-prova-de-trabalho](references/squad/tasks/registrar-prova-de-trabalho.md) |
| Verificação do critic | [Cético de SLA](references/squad/agents/cetico-de-sla.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Sentinela-Mor (persona: Vítor, analista sênior de operações com obsessão por SLA](references/squad/agents/sentinela-mor-persona-vitor-analista-senior-de-operacoes-com-obsessao-por-sla.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/ops-cs-sla-health-monitor/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/ops-cs-sla-health-monitor-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executar. Reversibilidade baixa (interrompe o fluxo do agente atual).
- **HITL** — Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar múltiplos stakeholders. Ação de alto impacto e irreversível em termos de alarme organizacional.
- **HITL** — Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova a comunicação antes do envio. Toda comunicação com cliente é revisada por humano.
- **HITL** — Cassandra bloqueia um escalonamento por inconsistência no score: humano (supervisor ou ops lead) revisa o caso manualmente antes de decidir se escala ou não. Ocorre quando dados são ambíguos ou incompletos.
- **HITL** — Novo tipo de ticket sem histórico suficiente para calibrar Cronos (confidence_level=LOW): Sentinela-Mor pausa a decisão automática e notifica supervisor para avaliação manual do risco de breach. Cronos não especula sem dados.
- **HITL** — Histos detecta breach rate semanal acima do threshold crítico: relatório é revisado por ops manager antes de publicação, que decide se aciona revisão de processo ou ajuste de SLAs contratuais.
- **HITL** — Recalibração mensal do modelo do Cronos (Histos gera novo dataset): pesos atualizados são revisados por ops lead antes de ir para produção. Mudança no modelo preditivo é sempre revisada por humano.

7. Aplique [critic-cetico-de-sla](references/squad/checklists/critic-cetico-de-sla.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
