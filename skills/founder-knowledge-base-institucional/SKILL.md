---
name: founder-knowledge-base-institucional
description: Use para estruturar conhecimento institucional, registrar decisões e organizar fontes para consulta e atualização
  pelo founder.
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

# Knowledge Base Institucional do Founder

Estruturar conhecimento institucional, registrar decisões e organizar fontes para consulta e atualização pelo founder.

Adaptação do squad de Founder Office da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para estruturar conhecimento institucional, registrar decisões e organizar fontes para consulta e atualização pelo founder.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: ORION | [papel do orquestrador](references/squad/agents/orion.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/founder-knowledge-base-institucional-pipeline.yaml) |
| Verificação das saídas | [critic-auditor](references/squad/checklists/critic-auditor.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **ORION** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/founder-knowledge-base-institucional-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [ORION](references/squad/agents/orion.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Transformar Conhecimento Tacito | [SCRIBE](references/squad/agents/scribe.md) | [transformar-conhecimento-tacito](references/squad/tasks/transformar-conhecimento-tacito.md) |
| Construir Grafo Conhecimento | [CARTOGRAPHER](references/squad/agents/cartographer.md) | [construir-grafo-conhecimento](references/squad/tasks/construir-grafo-conhecimento.md) |
| Sintetizar Respostas Confidentes | [PERSONA FORGE](references/squad/agents/persona-forge.md) | [sintetizar-respostas-confidentes](references/squad/tasks/sintetizar-respostas-confidentes.md) |
| Gerar Drafts Narrativos | [SCRIVENER](references/squad/agents/scrivener.md) | [gerar-drafts-narrativos](references/squad/tasks/gerar-drafts-narrativos.md) |
| Monitorar Sinais Estratégicos | [RADAR](references/squad/agents/radar.md) | [monitorar-sinais-estrategicos](references/squad/tasks/monitorar-sinais-estrategicos.md) |
| Preparar Reuniões Importantes | [CHIEF OF STAFF](references/squad/agents/chief-of-staff.md) | [preparar-reunioes-importantes](references/squad/tasks/preparar-reunioes-importantes.md) |
| Simular Cenários Futuros | [WARGAME](references/squad/agents/wargame.md) | [simular-cenarios-futuros](references/squad/tasks/simular-cenarios-futuros.md) |
| Verificação do critic | [AUDITOR](references/squad/agents/auditor.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [ORION](references/squad/agents/orion.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/founder-knowledge-base-institucional/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/founder-knowledge-base-institucional-pipeline.yaml).

### Gates humanos deste squad

- **L3** — Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automaticamente — pausa e apresenta ao founder os dois claims com contexto (data, situacao) para ele determinar qual e a posicao atual e por que evoluiu. Irreversivel porque altera permanentemente o grafo canônico.
- **L3** — Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída para fora da empresa exige leitura e aprovação explícita do founder. O clone fala pela empresa — erro de representação e irreversível reputacionalmente.
- **L3** — Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com anotações de contexto por seção para facilitar a revisão, mas o envio nunca é automático.
- **L2** — Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para reunião'. O founder decide o que fazer com o sinal, não o squad.
- **L2** — Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao ha ingestao forçada — o founder controla o ritmo de captura do proprio conhecimento.
- **L1** — Revisão do mapa de lacunas gerado no Discovery: antes de priorizar quais tópicos capturar, o founder valida se a taxonomia e as lacunas identificadas fazem sentido. Ele pode adicionar tópicos críticos não detectados ou reclassificar prioridades.

7. Aplique [critic-auditor](references/squad/checklists/critic-auditor.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
