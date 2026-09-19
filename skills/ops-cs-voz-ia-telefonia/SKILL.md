---
name: ops-cs-voz-ia-telefonia
description: Use para planejar atendimento por voz, analisar transcrições e preparar fluxos de resolução e escalonamento para
  revisão.
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

# Voz-IA para Atendimento Telefônico

Planejar atendimento por voz, analisar transcrições e preparar fluxos de resolução e escalonamento para revisão.

Adaptação do squad de Operações & CS da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para planejar atendimento por voz, analisar transcrições e preparar fluxos de resolução e escalonamento para revisão.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Maestro | [papel do orquestrador](references/squad/agents/maestro.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/ops-cs-voz-ia-telefonia-pipeline.yaml) |
| Verificação das saídas | [critic-eco-2](references/squad/checklists/critic-eco-2.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Maestro** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/ops-cs-voz-ia-telefonia-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Maestro](references/squad/agents/maestro.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Transcrever E Normalizar Audio | [Sono](references/squad/agents/sono.md) | [transcrever-e-normalizar-audio](references/squad/tasks/transcrever-e-normalizar-audio.md) |
| Coletar Dados Necessários | [Vivo](references/squad/agents/vivo.md) | [coletar-dados-necessarios](references/squad/tasks/coletar-dados-necessarios.md) |
| Resolver Intenções de Voz | [Falco](references/squad/agents/falco.md) | [resolver-intencoes-de-voz](references/squad/tasks/resolver-intencoes-de-voz.md) |
| Escrever Ações Transacionais | [Onda](references/squad/agents/onda.md) | [escrever-acoes-transacionais](references/squad/tasks/escrever-acoes-transacionais.md) |
| Analisar Sentimento E Risco | [Radar](references/squad/agents/radar.md) | [analisar-sentimento-e-risco](references/squad/tasks/analisar-sentimento-e-risco.md) |
| Validar Qualidade De Voz | [Eco](references/squad/agents/eco.md) | [validar-qualidade-de-voz](references/squad/tasks/validar-qualidade-de-voz.md) |
| Gerenciar Transferência para Humanos | [Hertz](references/squad/agents/hertz.md) | [gerenciar-transferencia-para-humanos](references/squad/tasks/gerenciar-transferencia-para-humanos.md) |
| Verificação do critic | [Eco 2](references/squad/agents/eco-2.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Maestro](references/squad/agents/maestro.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/ops-cs-voz-ia-telefonia/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/ops-cs-voz-ia-telefonia-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket prioritario antes de executar
- **HITL** — Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona para humano
- **HITL** — Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente para supervisor
- **HITL** — Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana
- **HITL** — Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especialista
- **HITL** — Cliente VIP, Enterprise ou MRR > R$5k: toda acao irreversivel (cancelamento, mudanca de plano, refund parcial) requer aprovacao do CSM responsavel antes da execucao
- **HITL** — Audio com duracao > 3 minutos e confianca media ASR < 0.82 — transcricao marcada para revisao humana antes do processamento completo pelo Maestro
- **HITL** — Intencao nao reconhecida apos 2 turns de coleta pelo Vivo (confianca < 0.55) — Hertz escalona com transcricao completa para o humano interpretar e resolver
- **HITL** — Solicitacao de dados de terceiros, portabilidade de dados, ou qualquer direito LGPD em voz — Hertz bloqueia automacao e direciona para DPO/time juridico

7. Aplique [critic-eco-2](references/squad/checklists/critic-eco-2.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
