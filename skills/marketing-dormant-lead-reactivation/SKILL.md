---
name: marketing-dormant-lead-reactivation
description: Use para segmentar leads inativos e preparar campanhas de reativação com mensagens, critérios de elegibilidade
  e revisão.
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

# Dormant Lead Reactivation

Segmentar leads inativos e preparar campanhas de reativação com mensagens, critérios de elegibilidade e revisão.

Adaptação do squad de Marketing da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para segmentar leads inativos e preparar campanhas de reativação com mensagens, critérios de elegibilidade e revisão.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Lazaro | [papel do orquestrador](references/squad/agents/lazaro.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/marketing-dormant-lead-reactivation-pipeline.yaml) |
| Verificação das saídas | [critic-atena](references/squad/checklists/critic-atena.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Lazaro** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/marketing-dormant-lead-reactivation-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Lazaro](references/squad/agents/lazaro.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Reconstruir Histórico Lead | [Arqueologa](references/squad/agents/arqueologa.md) | [reconstruir-historico-lead](references/squad/tasks/reconstruir-historico-lead.md) |
| Verificar Mudanças Em Leads | [Radar](references/squad/agents/radar.md) | [verificar-mudancas-em-leads](references/squad/tasks/verificar-mudancas-em-leads.md) |
| Calcular Score De Reativacao Lead | [Oraculo Scorer](references/squad/agents/oraculo-scorer.md) | [calcular-score-de-reativacao-lead](references/squad/tasks/calcular-score-de-reativacao-lead.md) |
| Redigir Mensagens De Reativacao | [Lázaro Writer](references/squad/agents/lazaro-writer.md) | [redigir-mensagens-de-reativacao](references/squad/tasks/redigir-mensagens-de-reativacao.md) |
| Enviar Mensagens Reativação | [Charon Dispatcher](references/squad/agents/charon-dispatcher.md) | [enviar-mensagens-reativacao](references/squad/tasks/enviar-mensagens-reativacao.md) |
| Analisar Respostas Leads | [Echo Analyst](references/squad/agents/echo-analyst.md) | [analisar-respostas-leads](references/squad/tasks/analisar-respostas-leads.md) |
| Verificação do critic | [Atena](references/squad/agents/atena.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Lazaro](references/squad/agents/lazaro.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/marketing-dormant-lead-reactivation/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/marketing-dormant-lead-reactivation-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex: deal > R$20k) bloqueia completamente e notifica o gestor com draft completo, ficha de arqueologia e sinais novos para aprovacao ou rejeicao com 1 clique — nenhum caracter e enviado antes da aprovacao.
- **HITL** — Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovação humana obrigatória antes de entrar em sequência — agente não envia para dado não verificado.
- **HITL** — Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o gestor de marketing com o feedback completo do critic para reescritura ou descisao de nao envio.
- **HITL** — Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que disse, sugestão de próximo passo) — o squad paralisa qualquer automação para este lead e o vendedor assume o controle total da conversa.
- **HITL** — Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções de alto valor merecem resposta humana ou pelo menos validação antes de resposta automática.
- **HITL** — Sinais de oportunidade detectados em lead que estava em ARQUIVO (score < 40): Radar detecta mudança significativa (investimento, mudança de decisor, sinal de intent forte) em lead que havia sido desprioritizado — alerta ao gestor para decisão de reintegrar o lead na fila ativa ou manter desprioritizado.
- **HITL** — Relatório semanal de performance: Echo Analyst gera relatório de taxa de reativação por trilha e archetype entregue ao gestor todo friday — ponto de HITL estruturado para revisão de qual trilha está funcionando e quais ajustes de playbook são necessários antes da próxima rodada.
- **HITL** — Opt-out recebido: processamento automático cancela a sequência e atualiza o CRM, mas a decisão de blacklist permanente (nunca mais contatar) é sempre humana — o agente sinaliza e aguarda confirmação do gestor antes de registrar blacklist definitiva.

7. Aplique [critic-atena](references/squad/checklists/critic-atena.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
