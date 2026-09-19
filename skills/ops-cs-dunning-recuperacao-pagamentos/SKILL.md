---
name: ops-cs-dunning-recuperacao-pagamentos
description: Use para analisar inadimplência e preparar cadências de cobrança e recuperação de pagamentos para revisão humana.
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

# Cobrança e Recuperação de Pagamentos

Analisar inadimplência e preparar cadências de cobrança e recuperação de pagamentos para revisão humana.

Adaptação do squad de Operações & CS da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para analisar inadimplência e preparar cadências de cobrança e recuperação de pagamentos para revisão humana.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Cobalt | [papel do orquestrador](references/squad/agents/cobalt.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/ops-cs-dunning-recuperacao-pagamentos-pipeline.yaml) |
| Verificação das saídas | [critic-sentinel](references/squad/checklists/critic-sentinel.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Cobalt** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/ops-cs-dunning-recuperacao-pagamentos-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Cobalt](references/squad/agents/cobalt.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Calcular Sequência De Cobrança | [Dante](references/squad/agents/dante.md) | [calcular-sequencia-de-cobranca](references/squad/tasks/calcular-sequencia-de-cobranca.md) |
| Enviar Email De Recuperação | [Iris](references/squad/agents/iris.md) | [enviar-email-de-recuperacao](references/squad/tasks/enviar-email-de-recuperacao.md) |
| Enviar Mensagens Personalizadas | [Zap](references/squad/agents/zap.md) | [enviar-mensagens-personalizadas](references/squad/tasks/enviar-mensagens-personalizadas.md) |
| Classificar Respostas Cliente | [Flex](references/squad/agents/flex.md) | [classificar-respostas-cliente](references/squad/tasks/classificar-respostas-cliente.md) |
| Enviar SMS de Reforço | [Pulse](references/squad/agents/pulse.md) | [enviar-sms-de-reforco](references/squad/tasks/enviar-sms-de-reforco.md) |
| Analisar Padroes De Inadimplencia | [Atlas](references/squad/agents/atlas.md) | [analisar-padroes-de-inadimplencia](references/squad/tasks/analisar-padroes-de-inadimplencia.md) |
| Atualizar Dados de Pagamento | [Vault](references/squad/agents/vault.md) | [atualizar-dados-de-pagamento](references/squad/tasks/atualizar-dados-de-pagamento.md) |
| Verificação do critic | [Sentinel](references/squad/agents/sentinel.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Cobalt](references/squad/agents/cobalt.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/ops-cs-dunning-recuperacao-pagamentos/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/ops-cs-dunning-recuperacao-pagamentos-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes com menos de 3 meses de casa) — Flex classifica e cria task HITL urgente no ClickUp para o time financeiro com histórico completo e valor em risco
- **HITL** — Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar no gateway e no CRM, e responde ao cliente confirmando que um humano vai verificar em até X horas
- **HITL** — Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task de retenção para o CSM com contexto completo: cliente já estava em inadimplência + agora solicitou cancelamento = risco crítico combinado
- **HITL** — Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgente para o Head Financeiro e para o CSM responsável da conta, com sugestão de abordagem via chamada telefônica
- **HITL** — Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema no gateway de pagamento, no processador ou na infraestrutura (não é inadimplência — é incidente têcnico)
- **HITL** — Sentinel reprova uma mensagem por violação de compliance legal (CDC/LGPD) — bloqueia o disparo, notifica o Head Jurídico e o responsável de CS via Slack, e suspende o envio para todos os clientes no mesmo step até que o template seja revisado e re-aprovado
- **HITL** — Cliente com histórico de chargeback ou de fraude identificado pelo gateway — Cobalt bloqueia a sequência de dunning automática e cria task manual para o time financeiro gerenciar o caso diretamente (cobrança de fraude tem tratamento jurídico diferente de inadimplência comum)
- **HITL** — Bad debt confirmado (cobranca nao recuperada apos sequencia completa + tentativas manuais) — Cobalt fecha a sequencia como IRRECUPERAVEL, Atlas atualiza o cohort de bad debt, e cria task para o time juridico/financeiro avaliar encaminhamento para assessoria de cobranca ou baixa contabil

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
