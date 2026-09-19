---
name: ops-cs-handoff-orchestrator-hitl
description: Use para definir quando escalar casos para humanos e preparar handoffs com contexto, evidências e critérios de
  retomada.
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

# Handoff Orchestrator HITL

Definir quando escalar casos para humanos e preparar handoffs com contexto, evidências e critérios de retomada.

Adaptação do squad de Operações & CS da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para definir quando escalar casos para humanos e preparar handoffs com contexto, evidências e critérios de retomada.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Hieronimus | [papel do orquestrador](references/squad/agents/hieronimus.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/ops-cs-handoff-orchestrator-hitl-pipeline.yaml) |
| Verificação das saídas | [critic-vitor](references/squad/checklists/critic-vitor.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Hieronimus** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/ops-cs-handoff-orchestrator-hitl-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Hieronimus](references/squad/agents/hieronimus.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Classificar Criticidade | [Cassio](references/squad/agents/cassio.md) | [classificar-criticidade](references/squad/tasks/classificar-criticidade.md) |
| Empacotar Contexto | [Beatriz](references/squad/agents/beatriz.md) | [empacotar-contexto](references/squad/tasks/empacotar-contexto.md) |
| Monitorar Handoffs L3 | [Renato](references/squad/agents/renato.md) | [monitorar-handoffs-l3](references/squad/tasks/monitorar-handoffs-l3.md) |
| Analisar Falso Positivo | [Selene](references/squad/agents/selene.md) | [analisar-falso-positivo](references/squad/tasks/analisar-falso-positivo.md) |
| Determinar Canal Enviado | [Dora](references/squad/agents/dora.md) | [determinar-canal-enviado](references/squad/tasks/determinar-canal-enviado.md) |
| Registrar Decisão Humana | [Fabio](references/squad/agents/fabio.md) | [registrar-decisao-humana](references/squad/tasks/registrar-decisao-humana.md) |
| Verificação do critic | [Vitor](references/squad/agents/vitor.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Hieronimus](references/squad/agents/hieronimus.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/ops-cs-handoff-orchestrator-hitl/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/ops-cs-handoff-orchestrator-hitl-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — humano aprova antes de qualquer execução, sem exceção.
- **HITL** — L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assinado, alteração de cláusula contratual, bloqueio/banimento de usuário.
- **HITL** — L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qualquer comunicação que mencione termos legais ou rescisão.
- **HITL** — L3 obrigatório: toda ação de impacto reputacional alto — publicação de resposta pública em canal externo (redes sociais, review sites), comunicados de crise, respostas à imprensa.
- **HITL** — Aprovação humana para recalibração da matriz (output do Selene): nenhum threshold de autonomia é alterado sem validação do supervisor CS ou gerente de operações.
- **HITL** — Revisão humana quinzenal do Relatório de Auditoria do Vitor: supervisor CS assina o score de qualidade e valida as correções propostas.
- **HITL** — Gate humano na primeira semana pos-implantacao: humano revisa 100% das classificacoes (nao apenas L3) para construir confianca na matriz antes de operar em modo autonomo.

7. Aplique [critic-vitor](references/squad/checklists/critic-vitor.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
