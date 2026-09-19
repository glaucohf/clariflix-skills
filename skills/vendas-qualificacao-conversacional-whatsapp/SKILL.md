---
name: vendas-qualificacao-conversacional-whatsapp
description: Use para preparar conversas de qualificação comercial por WhatsApp com perguntas, critérios de avanço e handoff
  humano.
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

# Qualificação Conversacional

Preparar conversas de qualificação comercial por WhatsApp com perguntas, critérios de avanço e handoff humano.

Adaptação do squad de Vendas da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para preparar conversas de qualificação comercial por WhatsApp com perguntas, critérios de avanço e handoff humano.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Maestro Comercial | [papel do orquestrador](references/squad/agents/maestro-comercial.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/vendas-qualificacao-conversacional-whatsapp-pipeline.yaml) |
| Verificação das saídas | [critic-censor-comercial](references/squad/checklists/critic-censor-comercial.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Maestro Comercial** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/vendas-qualificacao-conversacional-whatsapp-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Maestro Comercial](references/squad/agents/maestro-comercial.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Enriquecer Dossiê Lead | [Investigador de Lead](references/squad/agents/investigador-de-lead.md) | [enriquecer-dossie-lead](references/squad/tasks/enriquecer-dossie-lead.md) |
| Conduzir Conversa Estruturada | [SDR Conversacional](references/squad/agents/sdr-conversacional.md) | [conduzir-conversa-estruturada](references/squad/tasks/conduzir-conversa-estruturada.md) |
| Priorizar Leads | [Juiz de Fit](references/squad/agents/juiz-de-fit.md) | [priorizar-leads](references/squad/tasks/priorizar-leads.md) |
| Agendar Reunião | [Agendador de Reuniões](references/squad/agents/agendador-de-reunioes.md) | [agendar-reuniao](references/squad/tasks/agendar-reuniao.md) |
| Reativar Leads Frios | [Reativador de Pipeline](references/squad/agents/reativador-de-pipeline.md) | [reativar-leads-frios](references/squad/tasks/reativar-leads-frios.md) |
| Auditar Saúde Do Pipeline | [Guardião do CRM](references/squad/agents/guardiao-do-crm.md) | [auditar-saude-do-pipeline](references/squad/tasks/auditar-saude-do-pipeline.md) |
| Analisar Conversas Qualificadas | [Analista de Conversas](references/squad/agents/analista-de-conversas.md) | [analisar-conversas-qualificadas](references/squad/tasks/analisar-conversas-qualificadas.md) |
| Verificação do critic | [Censor Comercial](references/squad/agents/censor-comercial.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Maestro Comercial](references/squad/agents/maestro-comercial.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/vendas-qualificacao-conversacional-whatsapp/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/vendas-qualificacao-conversacional-whatsapp-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputacional. Gestor comercial aprova batch antes do disparo.
- **HITL** — HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se lead pergunta por desconto, Vera responde 'vou verificar com nosso especialista' e escala ao closer via notificação imediata.
- **HITL** — HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente via WhatsApp antes de qualquer ação automática adicional. Closer decide se assume a conversa ou deixa o squad continuar.
- **HITL** — HITL-4 (L2): Reagendamento após segunda recusa do lead — Tempo tenta 2x automaticamente; na 3ª recusa, notifica o closer para abordagem manual personalizada.
- **HITL** — HITL-5 (L2): Objecão não mapeada detectada pelo Veto na conversa da Vera — Vera pausa, escala notificação ao gestor comercial com contexto completo. Gestor responde o que fazer; resposta é adicionada ao playbook para aprendizado.
- **HITL** — HITL-6 (L1): Relatório semanal do Eco com sugestões de ajuste de prompt — gestor revisa e aprova antes de qualquer alteração ser aplicada nos prompts da Vera ou nos pesos do Magnus.

7. Aplique [critic-censor-comercial](references/squad/checklists/critic-censor-comercial.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
