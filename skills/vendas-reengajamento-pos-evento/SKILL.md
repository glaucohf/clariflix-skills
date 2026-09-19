---
name: vendas-reengajamento-pos-evento
description: Use para segmentar participantes de eventos e webinars e preparar ações e mensagens de reengajamento comercial.
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

# Reengajamento Pós-Evento e Webinar

Segmentar participantes de eventos e webinars e preparar ações e mensagens de reengajamento comercial.

Adaptação do squad de Vendas da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para segmentar participantes de eventos e webinars e preparar ações e mensagens de reengajamento comercial.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Claude Opus | [papel do orquestrador](references/squad/agents/claude-opus.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/vendas-reengajamento-pos-evento-pipeline.yaml) |
| Verificação das saídas | [critic-vigilia](references/squad/checklists/critic-vigilia.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Claude Opus** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/vendas-reengajamento-pos-evento-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Claude Opus](references/squad/agents/claude-opus.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Processar Lista De Participantes | [Recon](references/squad/agents/recon.md) | [processar-lista-de-participantes](references/squad/tasks/processar-lista-de-participantes.md) |
| Enriquecer Dossiê Contato | [Sherlock Évento](references/squad/agents/sherlock-evento.md) | [enriquecer-dossie-contato](references/squad/tasks/enriquecer-dossie-contato.md) |
| Agendar Reuniao Demo | [Alta Intenção](references/squad/agents/alta-intencao.md) | [agendar-reuniao-demo](references/squad/tasks/agendar-reuniao-demo.md) |
| Enviar Mensagem Adicional | [Engajamento Médio](references/squad/agents/engajamento-medio.md) | [enviar-mensagem-adicional](references/squad/tasks/enviar-mensagem-adicional.md) |
| Conduzir Qualificação Conversacional | [Argos Evento](references/squad/agents/argos-evento.md) | [conduzir-qualificacao-conversacional](references/squad/tasks/conduzir-qualificacao-conversacional.md) |
| Gerenciar Leads Baixo Engajamento | [Eco Evento](references/squad/agents/eco-evento.md) | [gerenciar-leads-baixo-engajamento](references/squad/tasks/gerenciar-leads-baixo-engajamento.md) |
| Agendar Reunião Contextualizada | [Atlas Evento](references/squad/agents/atlas-evento.md) | [agendar-reuniao-contextualizada](references/squad/tasks/agendar-reuniao-contextualizada.md) |
| Verificação do critic | [Vigilia](references/squad/agents/vigilia.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Claude Opus](references/squad/agents/claude-opus.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/vendas-reengajamento-pos-evento/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/vendas-reengajamento-pos-evento-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) — qualquer ação requer aprovação do closer responsável antes do primeiro envio
- **HITL** — Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento
- **HITL** — Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática
- **HITL** — Participante do evento que é funcionário de concorrente identificado — qualquer abordagem requer decisão estratégica humana
- **HITL** — Solicitação de proposta comercial ou orçamento mencionada na resposta do lead — Argos Evento escala imediatamente para closer com ficha de qualificação
- **HITL** — Lead que solicita opt-out ou demonstra irritação com o contato — intervenção humana obrigatória, registro de opt-out e revisão da cadência
- **HITL** — Inconsistência crítica detectada entre dados do evento e CRM (ex: lead do evento e cliente com contrato ativo cancelado) — revisão humana antes de qualquer contato
- **HITL** — Volume de lista acima de 1.000 contatos em evento único — revisão humana da segmentação antes do disparo em massa

7. Aplique [critic-vigilia](references/squad/checklists/critic-vigilia.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
