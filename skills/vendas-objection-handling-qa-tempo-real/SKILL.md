---
name: vendas-objection-handling-qa-tempo-real
description: Use para preparar respostas a objeções e perguntas comerciais com base no contexto do prospect e em informações
  verificadas.
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
    - vendas
    - squad
    - maquina-de-receita
    related_skills: []
---

# Objection Handling e Q&A em Tempo Real

Preparar respostas a objeções e perguntas comerciais com base no contexto do prospect e em informações verificadas.

Adaptação do squad de Vendas da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para preparar respostas a objeções e perguntas comerciais com base no contexto do prospect e em informações verificadas.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: MAESTRO | [papel do orquestrador](references/squad/agents/maestro.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/vendas-objection-handling-qa-tempo-real-pipeline.yaml) |
| Verificação das saídas | [critic-argus](references/squad/checklists/critic-argus.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **MAESTRO** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/vendas-objection-handling-qa-tempo-real-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [MAESTRO](references/squad/agents/maestro.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Rebater Objeções De Preço | [REBOUND](references/squad/agents/rebound.md) | [rebater-objecoes-de-preco](references/squad/tasks/rebater-objecoes-de-preco.md) |
| Rebater Objecoes Timing | [TEMPO](references/squad/agents/tempo.md) | [rebater-objecoes-timing](references/squad/tasks/rebater-objecoes-timing.md) |
| Rebater Objeções Concorrente | [CHALLENGER](references/squad/agents/challenger.md) | [rebater-objecoes-concorrente](references/squad/tasks/rebater-objecoes-concorrente.md) |
| Responder Dúvidas Técnicas | [TECNICO](references/squad/agents/tecnico.md) | [responder-duvidas-tecnicas](references/squad/tasks/responder-duvidas-tecnicas.md) |
| Resolver Objeção Autoridade | [CLOSER](references/squad/agents/closer.md) | [resolver-objecao-autoridade](references/squad/tasks/resolver-objecao-autoridade.md) |
| Analisar Objeções Frequentes | [ARQUIVO](references/squad/agents/arquivo.md) | [analisar-objecoes-frequentes](references/squad/tasks/analisar-objecoes-frequentes.md) |
| Verificação do critic | [ARGUS](references/squad/agents/argus.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [MAESTRO](references/squad/agents/maestro.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/vendas-objection-handling-qa-tempo-real/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/vendas-objection-handling-qa-tempo-real-pipeline.yaml).

### Gates humanos deste squad

- **L3** — Qualquer resposta que envolva promessa de desconto acima do nível autorizado para o vendedor: MAESTRO pausa, notifica supervisor ou gerente de vendas via Slack/WhatsApp, que aprova ou rejeita em tempo real antes da resposta chegar ao vendedor
- **L3** — Qualquer resposta a dúvida técnica que envolva prazo de implementação customizado, SLA não padrão, ou integração não documentada na base: TÉCNICO flag como HITL, vendedor recebe instrução 'vou confirmar com a equipe técnica e te retorno em X horas' em vez de uma promessa não verificada
- **L3** — Escrita de resultados de call e atualização de stage no CRM pelo ARQUIVO: vendedor confirma o resultado via formulário rápido (1 click) antes de qualquer persistência em CRM de produção
- **L2** — Quando ARGUS emite REJEITADO por factualidade: MAESTRO notifica o vendedor que a resposta está sendo verificada e entrega uma resposta genérica segura enquanto o worker corrige — o vendedor decide se usa a genérica ou aguarda a corrigida
- **L1** — Objecão nova não catalogada (aparece pela primeira vez): ARQUIVO sinaliza ao líder de vendas ou product owner que uma nova objecão foi detectada e sugere draft de resposta para validação antes de entrar na base — o líder aprova, edita ou rejeita o draft

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
