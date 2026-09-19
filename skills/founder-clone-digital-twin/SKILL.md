---
name: founder-clone-digital-twin
description: Use para estruturar um perfil de critérios e estilo decisório do founder para simular decisões e revisar recomendações.
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

# Clône Estratégico do Founder

Estruturar um perfil de critérios e estilo decisório do founder para simular decisões e revisar recomendações.

Adaptação do squad de Founder Office da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para estruturar um perfil de critérios e estilo decisório do founder para simular decisões e revisar recomendações.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: ORION | [papel do orquestrador](references/squad/agents/orion.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/founder-clone-digital-twin-pipeline.yaml) |
| Verificação das saídas | [critic-sentinel](references/squad/checklists/critic-sentinel.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **ORION** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/founder-clone-digital-twin-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [ORION](references/squad/agents/orion.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Responder Perguntas | [ECHO](references/squad/agents/echo.md) | [responder-perguntas](references/squad/tasks/responder-perguntas.md) |
| Conduzir Pesquisa Multi-fonte | [ATLAS](references/squad/agents/atlas.md) | [conduzir-pesquisa-multi-fonte](references/squad/tasks/conduzir-pesquisa-multi-fonte.md) |
| Ingerir Fontes De Conhecimento | [CHRONICLE](references/squad/agents/chronicle.md) | [ingerir-fontes-de-conhecimento](references/squad/tasks/ingerir-fontes-de-conhecimento.md) |
| Simular Cenarios Futuros | [STRATEGOS](references/squad/agents/strategos.md) | [simular-cenarios-futuros](references/squad/tasks/simular-cenarios-futuros.md) |
| Gerar Drafts De Board Packs | [HERALD](references/squad/agents/herald.md) | [gerar-drafts-de-board-packs](references/squad/tasks/gerar-drafts-de-board-packs.md) |
| Monitorar Sinais Competitivos | [VIGIL](references/squad/agents/vigil.md) | [monitorar-sinais-competitivos](references/squad/tasks/monitorar-sinais-competitivos.md) |
| Controlar Ações L3 | [GATE](references/squad/agents/gate.md) | [controlar-acoes-l3](references/squad/tasks/controlar-acoes-l3.md) |
| Verificação do critic | [SENTINEL](references/squad/agents/sentinel.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [ORION](references/squad/agents/orion.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/founder-clone-digital-twin/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/founder-clone-digital-twin-pipeline.yaml).

### Gates humanos deste squad

- **L3** — HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio – o squad nunca envia comunicação externa autonomamente
- **L3** — GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política interna – founder aprova com opções claras antes da execução
- **L3** — Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao de pensamento antes de ser persistida no corpus canônico
- **L2** — ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma aproximação e pode escalonar
- **L2** — STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer caminho seja comunicado como recomendacao oficial do squad
- **L1** — VIGIL ao detectar sinal competitivo CRÍTICO fora do ciclo semanal: notificação imediata ao founder com proposta de contra-jogada — founder decide se ativa resposta ou aguarda mais informações
- **L1** — CHRONICLE ao identificar gap crítico no corpus que impacta a confiabilidade do ECHO em categoria de alto volume: agenda sessão de captura de conhecimento com o founder antes de continuar respondendo naquela categoria

7. Aplique [critic-sentinel](references/squad/checklists/critic-sentinel.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
