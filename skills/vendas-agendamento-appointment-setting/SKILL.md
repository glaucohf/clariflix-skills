---
name: vendas-agendamento-appointment-setting
description: Use para preparar agendamento comercial com critérios de qualificação, disponibilidade, confirmação e tratamento
  de reagendamentos.
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

# Agendamento

Preparar agendamento comercial com critérios de qualificação, disponibilidade, confirmação e tratamento de reagendamentos.

Adaptação do squad de Vendas da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para preparar agendamento comercial com critérios de qualificação, disponibilidade, confirmação e tratamento de reagendamentos.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Maestro | [papel do orquestrador](references/squad/agents/maestro.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/vendas-agendamento-appointment-setting-pipeline.yaml) |
| Verificação das saídas | [critic-sentinela](references/squad/checklists/critic-sentinela.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Maestro** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/vendas-agendamento-appointment-setting-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Maestro](references/squad/agents/maestro.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Qualificar Lead Conversacionalmente | [Radar](references/squad/agents/radar.md) | [qualificar-lead-conversacionalmente](references/squad/tasks/qualificar-lead-conversacionalmente.md) |
| Criar Evento | [Slot](references/squad/agents/slot.md) | [criar-evento](references/squad/tasks/criar-evento.md) |
| Enviar Lembretes Agendados | [Vigil](references/squad/agents/vigil.md) | [enviar-lembretes-agendados](references/squad/tasks/enviar-lembretes-agendados.md) |
| Reagendar Oportunidades Perdidas | [Bounce](references/squad/agents/bounce.md) | [reagendar-oportunidades-perdidas](references/squad/tasks/reagendar-oportunidades-perdidas.md) |
| Enriquecer Dossiê Lead | [Intell](references/squad/agents/intell.md) | [enriquecer-dossie-lead](references/squad/tasks/enriquecer-dossie-lead.md) |
| Priorizar Leads | [Pulse](references/squad/agents/pulse.md) | [priorizar-leads](references/squad/tasks/priorizar-leads.md) |
| Verificação do critic | [Sentinela](references/squad/agents/sentinela.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Maestro](references/squad/agents/maestro.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/vendas-agendamento-appointment-setting/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/vendas-agendamento-appointment-setting-pipeline.yaml).

### Gates humanos deste squad

- **L3** — Aprovação humana obrigatória antes de qualquer contato com conta estratégica (deal acima de threshold configurado, ex: R$50k+) para revisar abordagem e personalização antes do envio.
- **L3** — Autorização para oferecer desconto ou condição especial durante negociação de horário/formato da reunião (ex: lead pede reunião presencial fora da política padrão).
- **L3** — Aprovação para reativar lead que foi marcado como LOST ou DISQUALIFIED pelo sistema — requer revisão humana do motivo original antes de nova tentativa.
- **L2** — Notificação ao closer/SDR quando lead muda de COLD para HOT (score sobe 30+ pontos em 24h) para decisão de abordar manualmente em vez de deixar o squad rodar sozinho.
- **L2** — Alerta ao gerente de vendas quando taxa de no-show da semana ultrapassar threshold configurado (ex: >20%) — indica problema sistêmico que requer revisão de ICP ou abordagem.
- **L1** — Revisão humana do briefing pre-reunião antes do envio ao closer, opcional mas recomendado nas primeiras 2 semanas de operação do squad para calibragem.

7. Aplique [critic-sentinela](references/squad/checklists/critic-sentinela.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
