---
name: vendas-inteligencia-conta-battlecards
description: Use para pesquisar contas e concorrentes e preparar battlecards e inteligência de apoio a oportunidades comerciais.
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

# Inteligência de Conta e Battlecards

Pesquisar contas e concorrentes e preparar battlecards e inteligência de apoio a oportunidades comerciais.

Adaptação do squad de Vendas da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para pesquisar contas e concorrentes e preparar battlecards e inteligência de apoio a oportunidades comerciais.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: NEXUS | [papel do orquestrador](references/squad/agents/nexus.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/vendas-inteligencia-conta-battlecards-pipeline.yaml) |
| Verificação das saídas | [critic-sentinel](references/squad/checklists/critic-sentinel.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **NEXUS** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/vendas-inteligencia-conta-battlecards-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [NEXUS](references/squad/agents/nexus.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Investigar Empresa Completa | [SCOUT](references/squad/agents/scout.md) | [investigar-empresa-completa](references/squad/tasks/investigar-empresa-completa.md) |
| Mapear Stakeholders | [IRIS](references/squad/agents/iris.md) | [mapear-stakeholders](references/squad/tasks/mapear-stakeholders.md) |
| Montar Battlecard Competitiva | [WARFARE](references/squad/agents/warfare.md) | [montar-battlecard-competitiva](references/squad/tasks/montar-battlecard-competitiva.md) |
| Analisar Dores Setoriais | [ORACLE](references/squad/agents/oracle.md) | [analisar-dores-setoriais](references/squad/tasks/analisar-dores-setoriais.md) |
| Entregar Artefatos Formatados | [HERALD](references/squad/agents/herald.md) | [entregar-artefatos-formatados](references/squad/tasks/entregar-artefatos-formatados.md) |
| Persistir Contexto No Crm | [MEMORIA](references/squad/agents/memoria.md) | [persistir-contexto-no-crm](references/squad/tasks/persistir-contexto-no-crm.md) |
| Verificação do critic | [SENTINEL](references/squad/agents/sentinel.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [NEXUS](references/squad/agents/nexus.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/vendas-inteligencia-conta-battlecards/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/vendas-inteligencia-conta-battlecards-pipeline.yaml).

### Gates humanos deste squad

- **L3** — Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistência permanente no CRM de produção
- **L3** — Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do envio, nunca envio automático sem leitura humana
- **L2** — Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que vai usar e descarta o que não se aplica
- **L1** — Quando SENTINEL emite REJEITADO: NEXUS pausa pipeline e notifica o vendedor sobre o gap de qualidade, permitindo que ele decida se quer prosseguir com versão parcial ou aguardar correção
- **L1** — Identificação de stakeholders de alto risco (ex: prospect e ex-funcionário de empresa cliente com conflito): IRIS sinaliza e vendedor decide como abordar antes de qualquer ação

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
