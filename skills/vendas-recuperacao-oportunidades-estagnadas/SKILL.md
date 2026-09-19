---
name: vendas-recuperacao-oportunidades-estagnadas
description: Use para diagnosticar oportunidades paradas e preparar planos de recuperação com próximos passos e mensagens
  para revisão.
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

# Recuperação de Oportunidades Estagnadas

Diagnosticar oportunidades paradas e preparar planos de recuperação com próximos passos e mensagens para revisão.

Adaptação do squad de Vendas da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para diagnosticar oportunidades paradas e preparar planos de recuperação com próximos passos e mensagens para revisão.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Orquestrador de Recuperação | [papel do orquestrador](references/squad/agents/orquestrador-de-recuperacao.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/vendas-recuperacao-oportunidades-estagnadas-pipeline.yaml) |
| Verificação das saídas | [critic-critic-e-verifier-de-mensagens-2](references/squad/checklists/critic-critic-e-verifier-de-mensagens-2.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Orquestrador de Recuperação** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/vendas-recuperacao-oportunidades-estagnadas-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Orquestrador de Recuperação](references/squad/agents/orquestrador-de-recuperacao.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Detectar Sinais De Estagnação | [Worker de Detecção e Triagem](references/squad/agents/worker-de-deteccao-e-triagem.md) | [detectar-sinais-de-estagnacao](references/squad/tasks/detectar-sinais-de-estagnacao.md) |
| Enriquecer Contexto Lead | [Escavador](references/squad/agents/escavador.md) | [enriquecer-contexto-lead](references/squad/tasks/enriquecer-contexto-lead.md) |
| Personalizar Sequência Mensagens | [Arquiteto](references/squad/agents/arquiteto.md) | [personalizar-sequencia-mensagens](references/squad/tasks/personalizar-sequencia-mensagens.md) |
| Verificar Mensagens | [Critic e Verifier de Mensagens](references/squad/agents/critic-e-verifier-de-mensagens.md) | [verificar-mensagens](references/squad/tasks/verificar-mensagens.md) |
| Enviar Mensagens Multicanal | [Worker de Outreach Multicanal](references/squad/agents/worker-de-outreach-multicanal.md) | [enviar-mensagens-multicanal](references/squad/tasks/enviar-mensagens-multicanal.md) |
| Nutrir Leads Longo Prazo | [Monge](references/squad/agents/monge.md) | [nutrir-leads-longo-prazo](references/squad/tasks/nutrir-leads-longo-prazo.md) |
| Analisar Abandono Em Etapas | [Forense](references/squad/agents/forense.md) | [analisar-abandono-em-etapas](references/squad/tasks/analisar-abandono-em-etapas.md) |
| Verificação do critic | [Critic e Verifier de Mensagens 2](references/squad/agents/critic-e-verifier-de-mensagens-2.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Orquestrador de Recuperação](references/squad/agents/orquestrador-de-recuperacao.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/vendas-recuperacao-oportunidades-estagnadas/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/vendas-recuperacao-oportunidades-estagnadas-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeiro toque automatizado — gate L3 no Mensageiro)
- **HITL** — Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa
- **HITL** — Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável comercial
- **HITL** — Mudança de playbook baseada em proposta do Forense — ajustes em playbooks existentes exigem aprovação humana antes de entrar em produção
- **HITL** — Primeiro contato via voz (Vapi/Retell) para leads de alto valor — script revisado e aprovado pelo responsavel antes do disparo
- **HITL** — Opt-out recebido — registrado imediatamente, comunicado ao comercial, nenhuma acao adicional automatica alem do registro de compliance

7. Aplique [critic-critic-e-verifier-de-mensagens-2](references/squad/checklists/critic-critic-e-verifier-de-mensagens-2.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
