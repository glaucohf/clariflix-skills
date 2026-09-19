---
name: founder-board-investor-relations
description: Use para preparar materiais de conselho, atualizações a investidores e acompanhamento de decisões e compromissos.
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

# Board & Investor Relations

Preparar materiais de conselho, atualizações a investidores e acompanhamento de decisões e compromissos.

Adaptação do squad de Founder Office da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para preparar materiais de conselho, atualizações a investidores e acompanhamento de decisões e compromissos.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Cassidy | [papel do orquestrador](references/squad/agents/cassidy.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/founder-board-investor-relations-pipeline.yaml) |
| Verificação das saídas | [critic-axiom](references/squad/checklists/critic-axiom.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Cassidy** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/founder-board-investor-relations-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Cassidy](references/squad/agents/cassidy.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Reconciliar Métricas | [Rex](references/squad/agents/rex.md) | [reconciliar-metricas](references/squad/tasks/reconciliar-metricas.md) |
| Sintetizar Contexto Mercado | [Marlowe](references/squad/agents/marlowe.md) | [sintetizar-contexto-mercado](references/squad/tasks/sintetizar-contexto-mercado.md) |
| Auditar Fontes Primárias | [Vera](references/squad/agents/vera.md) | [auditar-fontes-primarias](references/squad/tasks/auditar-fontes-primarias.md) |
| Alinhar Narrativa | [Sage](references/squad/agents/sage.md) | [alinhar-narrativa](references/squad/tasks/alinhar-narrativa.md) |
| Simular Perguntas Board | [Quincy](references/squad/agents/quincy.md) | [simular-perguntas-board](references/squad/tasks/simular-perguntas-board.md) |
| Manter Data Room Atualizado | [Cipher](references/squad/agents/cipher.md) | [manter-data-room-atualizado](references/squad/tasks/manter-data-room-atualizado.md) |
| Controlar Envio Externo | [Gate](references/squad/agents/gate.md) | [controlar-envio-externo](references/squad/tasks/controlar-envio-externo.md) |
| Verificação do critic | [Axiom](references/squad/agents/axiom.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Cassidy](references/squad/agents/cassidy.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/founder-board-investor-relations/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/founder-board-investor-relations-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção
- **HITL** — Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores
- **HITL** — Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%
- **HITL** — Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa não autorizada)
- **HITL** — Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downround) entrarem no draft final
- **HITL** — Aprovação do Q&A Brief do Quincy antes do board meeting — founder confirma quais respostas está confortável em dar publicamente
- **HITL** — Configuração inicial do corpus do Sage — founder revisa e aprova quais comunicações passadas entram no corpus de clonagem narrativa
- **HITL** — Qualquer mudança de metodologia de cálculo de métrica-chave (ex: mudança de definição de ARR, churn líquido vs bruto) requer aprovação explícita antes de ser refletida no board pack

7. Aplique [critic-axiom](references/squad/checklists/critic-axiom.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
