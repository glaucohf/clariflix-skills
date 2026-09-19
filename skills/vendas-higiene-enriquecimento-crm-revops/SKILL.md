---
name: vendas-higiene-enriquecimento-crm-revops
description: Use para diagnosticar qualidade dos dados do CRM e preparar correções, deduplicação e enriquecimento para revisão.
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

# Higiene e Enriquecimento de CRM

Diagnosticar qualidade dos dados do CRM e preparar correções, deduplicação e enriquecimento para revisão.

Adaptação do squad de Vendas da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para diagnosticar qualidade dos dados do CRM e preparar correções, deduplicação e enriquecimento para revisão.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Nexus | [papel do orquestrador](references/squad/agents/nexus.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/vendas-higiene-enriquecimento-crm-revops-pipeline.yaml) |
| Verificação das saídas | [critic-sentinel](references/squad/checklists/critic-sentinel.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Nexus** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/vendas-higiene-enriquecimento-crm-revops-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Nexus](references/squad/agents/nexus.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Validar Formato De Entradas | [Validador de Entradas](references/squad/agents/validador-de-entradas.md) | [validar-formato-de-entradas](references/squad/tasks/validar-formato-de-entradas.md) |
| Detectar Duplicatas | [Detector de Duplicatas](references/squad/agents/detector-de-duplicatas.md) | [detectar-duplicatas](references/squad/tasks/detectar-duplicatas.md) |
| Consultar Fontes Confiança | [Enriquecedor de Conta e Lead](references/squad/agents/enriquecedor-de-conta-e-lead.md) | [consultar-fontes-confianca](references/squad/tasks/consultar-fontes-confianca.md) |
| Propagar Atualizações Fonte | [Sincronizador de Fontes](references/squad/agents/sincronizador-de-fontes.md) | [propagar-atualizacoes-fonte](references/squad/tasks/propagar-atualizacoes-fonte.md) |
| Calcular Score Registro | [Pythia](references/squad/agents/pythia.md) | [calcular-score-registro](references/squad/tasks/calcular-score-registro.md) |
| Detectar Sinais De Intencao | [Cassandra](references/squad/agents/cassandra.md) | [detectar-sinais-de-intencao](references/squad/tasks/detectar-sinais-de-intencao.md) |
| Gerar Golden Record | [Gerador de Golden Record](references/squad/agents/gerador-de-golden-record.md) | [gerar-golden-record](references/squad/tasks/gerar-golden-record.md) |
| Verificação do critic | [Sentinel](references/squad/agents/sentinel.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Nexus](references/squad/agents/nexus.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/vendas-higiene-enriquecimento-crm-revops/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/vendas-higiene-enriquecimento-crm-revops-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual)
- **HITL** — Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3)
- **HITL** — Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez)
- **HITL** — Revisão de registros Golden Bronze com deal aberto (operador RevOps decide: enriquecer manualmente ou descartar deal)
- **HITL** — Configuração inicial do playbook de golden record no onboarding (quem decide vence em cada campo — decisão estratégica do cliente)
- **HITL** — Aprovação de integração de nova fonte de dados ao pipeline (ex: adicionar novo formulário ou importação de lista de parceiro)

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
