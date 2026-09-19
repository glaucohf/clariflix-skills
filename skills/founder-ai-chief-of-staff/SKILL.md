---
name: founder-ai-chief-of-staff
description: Use para organizar prioridades, decisões e acompanhamento executivo com um roteiro de Chief of Staff para o founder.
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

# AI Chief of Staff

Organizar prioridades, decisões e acompanhamento executivo com um roteiro de Chief of Staff para o founder.

Adaptação do squad de Founder Office da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para organizar prioridades, decisões e acompanhamento executivo com um roteiro de Chief of Staff para o founder.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Orion | [papel do orquestrador](references/squad/agents/orion.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/founder-ai-chief-of-staff-pipeline.yaml) |
| Verificação das saídas | [critic-skeptic](references/squad/checklists/critic-skeptic.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Orion** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/founder-ai-chief-of-staff-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Orion](references/squad/agents/orion.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Preparar Briefing De Reunião | [Briefing](references/squad/agents/briefing.md) | [preparar-briefing-de-reuniao](references/squad/tasks/preparar-briefing-de-reuniao.md) |
| Sintetizar Fontes Abertas | [Kira](references/squad/agents/kira.md) | [sintetizar-fontes-abertas](references/squad/tasks/sintetizar-fontes-abertas.md) |
| Gerar Relatório Semanal | [Vance](references/squad/agents/vance.md) | [gerar-relatorio-semanal](references/squad/tasks/gerar-relatorio-semanal.md) |
| Validar Output Estratégico | [Sage](references/squad/agents/sage.md) | [validar-output-estrategico](references/squad/tasks/validar-output-estrategico.md) |
| Monitorar Inteligência Competitiva | [Intel](references/squad/agents/intel.md) | [monitorar-inteligencia-competitiva](references/squad/tasks/monitorar-inteligencia-competitiva.md) |
| Gerar Plano Da Semana | [Atlas](references/squad/agents/atlas.md) | [gerar-plano-da-semana](references/squad/tasks/gerar-plano-da-semana.md) |
| Gerar Drafts De Updates | [Memo](references/squad/agents/memo.md) | [gerar-drafts-de-updates](references/squad/tasks/gerar-drafts-de-updates.md) |
| Verificação do critic | [Skeptic](references/squad/agents/skeptic.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Orion](references/squad/agents/orion.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/founder-ai-chief-of-staff/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/founder-ai-chief-of-staff-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovação do founder antes de qualquer envio externo (email, memo, board pack) — Memo Agent é L3 por design
- **HITL** — Confirmação antes de criar compromissos no calendário do founder (bloqueio de foco por Atlas)
- **HITL** — Revisão do Meeting Brief para reuniões de alto valor (deals >R$200k, board, investor) antes de ser considerado finalizado
- **HITL** — Aprovação de escalation quando follow-up crítico está atrasado e envolve terceiros externos
- **HITL** — Validação do Founder Clone Agent antes de qualquer resposta ser enviada em nome do founder
- **HITL** — Configuração inicial do corpus do Sage (founder revisa e aprova quais comunicações entram no corpus de clonagem)

7. Aplique [critic-skeptic](references/squad/checklists/critic-skeptic.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
