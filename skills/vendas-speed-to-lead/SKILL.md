---
name: vendas-speed-to-lead
description: Use para planejar triagem e primeira resposta a novos leads, com priorização, qualificação e encaminhamento comercial.
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

# Speed-to-Lead

Planejar triagem e primeira resposta a novos leads, com priorização, qualificação e encaminhamento comercial.

Adaptação do squad de Vendas da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para planejar triagem e primeira resposta a novos leads, com priorização, qualificação e encaminhamento comercial.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Claude Opus | [papel do orquestrador](references/squad/agents/claude-opus.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/vendas-speed-to-lead-pipeline.yaml) |
| Verificação das saídas | [critic-sentinel](references/squad/checklists/critic-sentinel.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Claude Opus** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/vendas-speed-to-lead-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Claude Opus](references/squad/agents/claude-opus.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Enviar Primeira Resposta ao Lead | [Flash](references/squad/agents/flash.md) | [enviar-primeira-resposta-ao-lead](references/squad/tasks/enviar-primeira-resposta-ao-lead.md) |
| Enriquecer Dossiê Lead | [Sherlock](references/squad/agents/sherlock.md) | [enriquecer-dossie-lead](references/squad/tasks/enriquecer-dossie-lead.md) |
| Qualificar Lead Conversacionalmente | [Sócrates](references/squad/agents/socrates.md) | [qualificar-lead-conversacionalmente](references/squad/tasks/qualificar-lead-conversacionalmente.md) |
| Agendar Reunião | [Atlas](references/squad/agents/atlas.md) | [agendar-reuniao](references/squad/tasks/agendar-reuniao.md) |
| Priorizar Leads | [Argos](references/squad/agents/argos.md) | [priorizar-leads](references/squad/tasks/priorizar-leads.md) |
| Gerenciar Cadências De Follow-Up | [Eco](references/squad/agents/eco.md) | [gerenciar-cadencias-de-follow-up](references/squad/tasks/gerenciar-cadencias-de-follow-up.md) |
| Realizar Ligação Qualificadora | [SDR por Ligacao](references/squad/agents/sdr-por-ligacao.md) | [realizar-ligacao-qualificadora](references/squad/tasks/realizar-ligacao-qualificadora.md) |
| Verificação do critic | [Sentinel](references/squad/agents/sentinel.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Claude Opus](references/squad/agents/claude-opus.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/vendas-speed-to-lead/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/vendas-speed-to-lead-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead
- **HITL** — Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto
- **HITL** — Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio
- **HITL** — Lead classificado como conta estrategica (lista VIP do CRM) — qualquer acao requer aprovacao do closer responsavel
- **HITL** — Desconto ou concessao comercial mencionada na conversa — Eco/Socrates escalam imediatamente para closer humano
- **HITL** — Reagendamento apos segundo no-show — Atlas escala para closer decidir se continua ou descarta lead
- **HITL** — Lead demonstra sinal negativo forte (reclamacao de contato excessivo, solicitacao de opt-out) — intervencao humana obrigatoria e imediata

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
