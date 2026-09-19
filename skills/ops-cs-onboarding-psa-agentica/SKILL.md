---
name: ops-cs-onboarding-psa-agentica
description: Use para planejar onboarding e implementação de clientes, acompanhando etapas, dependências, riscos e responsáveis.
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

# Onboarding & Implementação

Planejar onboarding e implementação de clientes, acompanhando etapas, dependências, riscos e responsáveis.

Adaptação do squad de Operações & CS da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para planejar onboarding e implementação de clientes, acompanhando etapas, dependências, riscos e responsáveis.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Maestro | [papel do orquestrador](references/squad/agents/maestro.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/ops-cs-onboarding-psa-agentica-pipeline.yaml) |
| Verificação das saídas | [critic-argus](references/squad/checklists/critic-argus.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Maestro** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/ops-cs-onboarding-psa-agentica-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Maestro](references/squad/agents/maestro.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Criar Plano De Implementação | [Átlas](references/squad/agents/atlas.md) | [criar-plano-de-implementacao](references/squad/tasks/criar-plano-de-implementacao.md) |
| Monitorar Desvios De Cronograma | [Cassandra](references/squad/agents/cassandra.md) | [monitorar-desvios-de-cronograma](references/squad/tasks/monitorar-desvios-de-cronograma.md) |
| Enviar Mensagens Contextualizadas | [Hermes](references/squad/agents/hermes.md) | [enviar-mensagens-contextualizadas](references/squad/tasks/enviar-mensagens-contextualizadas.md) |
| Processar Documentos SOW | [Iris](references/squad/agents/iris.md) | [processar-documentos-sow](references/squad/tasks/processar-documentos-sow.md) |
| Calcular Health Score Cliente | [Vitor](references/squad/agents/vitor.md) | [calcular-health-score-cliente](references/squad/tasks/calcular-health-score-cliente.md) |
| Gerar Relatório De Delivery | [Crono](references/squad/agents/crono.md) | [gerar-relatorio-de-delivery](references/squad/tasks/gerar-relatorio-de-delivery.md) |
| Verificação do critic | [Argus](references/squad/agents/argus.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Maestro](references/squad/agents/maestro.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/ops-cs-onboarding-psa-agentica/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/ops-cs-onboarding-psa-agentica-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)
- **HITL** — Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)
- **HITL** — Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro
- **HITL** — Aprovação do Delivery Status Report semanal antes do envio ao cliente
- **HITL** — Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente
- **HITL** — Decisão de go/no-go para go-live quando health score < 60 ou mais de 2 marcos críticos em Red

7. Aplique [critic-argus](references/squad/checklists/critic-argus.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
