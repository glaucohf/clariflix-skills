---
name: ops-cs-agent-assist-copilot
description: Use para preparar sugestões de resposta e consulta à base de conhecimento para apoiar atendentes humanos em casos
  de suporte.
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

# Copíloto do Agente Humano

Preparar sugestões de resposta e consulta à base de conhecimento para apoiar atendentes humanos em casos de suporte.

Adaptação do squad de Operações & CS da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para preparar sugestões de resposta e consulta à base de conhecimento para apoiar atendentes humanos em casos de suporte.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Compass | [papel do orquestrador](references/squad/agents/compass.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/ops-cs-agent-assist-copilot-pipeline.yaml) |
| Verificação das saídas | [critic-prism](references/squad/checklists/critic-prism.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Compass** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/ops-cs-agent-assist-copilot-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Compass](references/squad/agents/compass.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Classificar Intencao Do Cliente | [Radar](references/squad/agents/radar.md) | [classificar-intencao-do-cliente](references/squad/tasks/classificar-intencao-do-cliente.md) |
| Recuperar Dados De Conta | [Vault](references/squad/agents/vault.md) | [recuperar-dados-de-conta](references/squad/tasks/recuperar-dados-de-conta.md) |
| Gerar Sugestão de Resposta | [Scribe](references/squad/agents/scribe.md) | [gerar-sugestao-de-resposta](references/squad/tasks/gerar-sugestao-de-resposta.md) |
| Gerar Resumo Executivo | [Memo](references/squad/agents/memo.md) | [gerar-resumo-executivo](references/squad/tasks/gerar-resumo-executivo.md) |
| Sugerir Próximo Passo | [Lumen](references/squad/agents/lumen.md) | [sugerir-proximo-passo](references/squad/tasks/sugerir-proximo-passo.md) |
| Analisar Sugestões Atendente | [Echo](references/squad/agents/echo.md) | [analisar-sugestoes-atendente](references/squad/tasks/analisar-sugestoes-atendente.md) |
| Monitorar Mensagens Atendente | [Shield](references/squad/agents/shield.md) | [monitorar-mensagens-atendente](references/squad/tasks/monitorar-mensagens-atendente.md) |
| Verificação do critic | [Prism](references/squad/agents/prism.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Compass](references/squad/agents/compass.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/ops-cs-agent-assist-copilot/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/ops-cs-agent-assist-copilot-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atendente deve confirmar conscientemente ou corrigir
- **HITL** — Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'intencao incerta — responda manualmente'
- **HITL** — Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso específico
- **HITL** — Ticket de cliente em tier VIP/Enterprise ou MRR > R$10k: Lumen dispara alerta 'cliente estratégico' e recomenda envolvimento do CSM antes de qualquer compromisso
- **HITL** — Lumen detecta SLA em risco (< 20% do tempo restante): alerta visual urgente no overlay para o supervisor e para o atendente
- **HITL** — Vault retorna flag 'cliente_em_risco_de_churn' (health score < 50): todas as sugestões do Scribe são marcadas com indicador visual e Lumen adiciona sugestão de escalonamento para CSM
- **HITL** — Echo detecta que uma macro tem rejection_rate > 60% por 7 dias consecutivos: dispara alerta para gestor de CS no Slack pedindo revisão manual da macro antes de continuar exibindo
- **HITL** — Shield detecta promessa de desconto ou benefício financeiro no rascunho do atendente: alerta de policy_violation com valor exato do limite autorizado e botão de consulta ao supervisor

7. Aplique [critic-prism](references/squad/checklists/critic-prism.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
