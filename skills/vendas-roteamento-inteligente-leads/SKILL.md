---
name: vendas-roteamento-inteligente-leads
description: Use para definir regras de distribuição de leads, avaliar responsáveis e preparar roteamento comercial com justificativa.
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

# Roteamento Inteligente de Leads

Definir regras de distribuição de leads, avaliar responsáveis e preparar roteamento comercial com justificativa.

Adaptação do squad de Vendas da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para definir regras de distribuição de leads, avaliar responsáveis e preparar roteamento comercial com justificativa.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Orquestrador Comercial | [papel do orquestrador](references/squad/agents/orquestrador-comercial.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/vendas-roteamento-inteligente-leads-pipeline.yaml) |
| Verificação das saídas | [critic-veredito-2](references/squad/checklists/critic-veredito-2.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Orquestrador Comercial** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/vendas-roteamento-inteligente-leads-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Orquestrador Comercial](references/squad/agents/orquestrador-comercial.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Retornar Dossiê Estruturado | [Worker de Enriquecimento](references/squad/agents/worker-de-enriquecimento.md) | [retornar-dossie-estruturado](references/squad/tasks/retornar-dossie-estruturado.md) |
| Calcular Score Lead | [Worker de Lead Scoring](references/squad/agents/worker-de-lead-scoring.md) | [calcular-score-lead](references/squad/tasks/calcular-score-lead.md) |
| Consultar Capacidade Vendedores | [Atlas](references/squad/agents/atlas.md) | [consultar-capacidade-vendedores](references/squad/tasks/consultar-capacidade-vendedores.md) |
| Notificar Vendedor Lead | [Worker de Notificação e Aceite](references/squad/agents/worker-de-notificacao-e-aceite.md) | [notificar-vendedor-lead](references/squad/tasks/notificar-vendedor-lead.md) |
| Consolidar Dados CRM | [Worker de Higiene de CRM](references/squad/agents/worker-de-higiene-de-crm.md) | [consolidar-dados-crm](references/squad/tasks/consolidar-dados-crm.md) |
| Verificar Roteamento | [Veredito](references/squad/agents/veredito.md) | [verificar-roteamento](references/squad/tasks/verificar-roteamento.md) |
| Monitorar Primeiro Contato | [Farol](references/squad/agents/farol.md) | [monitorar-primeiro-contato](references/squad/tasks/monitorar-primeiro-contato.md) |
| Verificação do critic | [Veredito 2](references/squad/agents/veredito-2.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Orquestrador Comercial](references/squad/agents/orquestrador-comercial.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/vendas-roteamento-inteligente-leads/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/vendas-roteamento-inteligente-leads-pipeline.yaml).

### Gates humanos deste squad

- **L3** — Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro deploy; em produção, amostras aleatórias (10%) passam por revisão humana
- **L3** — Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratamento especial
- **L3** — Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente
- **L3** — Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interface de configuração, com log de auditoria
- **L3** — Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor designado
- **HITL** — Revisão humana semanal do relatório de auditoria do Veredito para identificar vieses sistemáticos e calibrar o modelo de scoring

7. Aplique [critic-veredito-2](references/squad/checklists/critic-veredito-2.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
