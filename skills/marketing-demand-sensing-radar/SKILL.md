---
name: marketing-demand-sensing-radar
description: Use para pesquisar sinais de demanda e intenção de compra, priorizar oportunidades e propor ações de marketing.
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

# Demand Sensing Radar

Pesquisar sinais de demanda e intenção de compra, priorizar oportunidades e propor ações de marketing.

Adaptação do squad de Marketing da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para pesquisar sinais de demanda e intenção de compra, priorizar oportunidades e propor ações de marketing.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Radar | [papel do orquestrador](references/squad/agents/radar.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/marketing-demand-sensing-radar-pipeline.yaml) |
| Verificação das saídas | [critic-sigma-2](references/squad/checklists/critic-sigma-2.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Radar** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/marketing-demand-sensing-radar-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Radar](references/squad/agents/radar.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Monitorar Sinais Mercado | [Pulse](references/squad/agents/pulse.md) | [monitorar-sinais-mercado](references/squad/tasks/monitorar-sinais-mercado.md) |
| Analisar Sinais De Demanda | [Vortex](references/squad/agents/vortex.md) | [analisar-sinais-de-demanda](references/squad/tasks/analisar-sinais-de-demanda.md) |
| Disparar Playbook Correto | [Nexus](references/squad/agents/nexus.md) | [disparar-playbook-correto](references/squad/tasks/disparar-playbook-correto.md) |
| Calcular ROI Sinal | [Sage](references/squad/agents/sage.md) | [calcular-roi-sinal](references/squad/tasks/calcular-roi-sinal.md) |
| Gerar Anúncio Específico | [Bolt](references/squad/agents/bolt.md) | [gerar-anuncio-especifico](references/squad/tasks/gerar-anuncio-especifico.md) |
| Verificar Conformidade E Qualidade | [Sigma](references/squad/agents/sigma.md) | [verificar-conformidade-e-qualidade](references/squad/tasks/verificar-conformidade-e-qualidade.md) |
| Verificação do critic | [Sigma 2](references/squad/agents/sigma-2.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Radar](references/squad/agents/radar.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/marketing-demand-sensing-radar/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/marketing-demand-sensing-radar-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresholds de urgência antes de qualquer monitoramento ir ao ar (L3, gate obrigatório)
- **HITL** — Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squad ser colocado em produção (L3, calibração crítica)
- **HITL** — Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e financeiro)
- **HITL** — Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprovar a mensagem antes do envio (L3)
- **HITL** — Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L1, ciclo recorrente)
- **HITL** — Ativação de novo tipo de sinal ou integração de nova fonte de dados que implica custo adicional — aprovação financeira antes de habilitar (L3)
- **HITL** — Quando Sigma retorna BLOCKED em gate de compliance LGPD — revisão jurídica humana obrigatória antes de reprocessar (L3, risco legal)

7. Aplique [critic-sigma-2](references/squad/checklists/critic-sigma-2.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
