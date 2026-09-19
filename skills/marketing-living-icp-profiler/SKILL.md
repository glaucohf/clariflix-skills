---
name: marketing-living-icp-profiler
description: Use para construir e revisar o perfil de cliente ideal com dados de contas, evidências e critérios de segmentação.
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
    - marketing
    - squad
    - maquina-de-receita
    related_skills: []
---

# Living ICP Profiler

Construir e revisar o perfil de cliente ideal com dados de contas, evidências e critérios de segmentação.

Adaptação do squad de Marketing da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para construir e revisar o perfil de cliente ideal com dados de contas, evidências e critérios de segmentação.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Maestro | [papel do orquestrador](references/squad/agents/maestro.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/marketing-living-icp-profiler-pipeline.yaml) |
| Verificação das saídas | [critic-vera-2](references/squad/checklists/critic-vera-2.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Maestro** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/marketing-living-icp-profiler-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Maestro](references/squad/agents/maestro.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Construir Personas Calibradas | [Atlas](references/squad/agents/atlas.md) | [construir-personas-calibradas](references/squad/tasks/construir-personas-calibradas.md) |
| Enriquecer Dados Lead | [Iris](references/squad/agents/iris.md) | [enriquecer-dados-lead](references/squad/tasks/enriquecer-dados-lead.md) |
| Monitorar Sinais De Compra | [Zara](references/squad/agents/zara.md) | [monitorar-sinais-de-compra](references/squad/tasks/monitorar-sinais-de-compra.md) |
| Calibrar Icp Com Dados De Mercado | [Nox](references/squad/agents/nox.md) | [calibrar-icp-com-dados-de-mercado](references/squad/tasks/calibrar-icp-com-dados-de-mercado.md) |
| Calcular Icp Score | [Rex](references/squad/agents/rex.md) | [calcular-icp-score](references/squad/tasks/calcular-icp-score.md) |
| Verificar Qualidade De Dados | [Vera](references/squad/agents/vera.md) | [verificar-qualidade-de-dados](references/squad/tasks/verificar-qualidade-de-dados.md) |
| Verificação do critic | [Vera 2](references/squad/agents/vera-2.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Maestro](references/squad/agents/maestro.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/marketing-living-icp-profiler/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/marketing-living-icp-profiler-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3)
- **HITL** — Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3)
- **HITL** — Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)
- **HITL** — Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3)
- **HITL** — Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1)
- **HITL** — Aprovação de integração com nova fonte de dados de enriquecimento que implica custo adicional — qualquer nova ferramenta paga requer validação financeira (L3)

7. Aplique [critic-vera-2](references/squad/checklists/critic-vera-2.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
