---
name: marketing-cro-landing-agentico
description: Use para diagnosticar páginas de conversão e preparar hipóteses, textos e planos de experimentos para landing
  pages.
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

# CRO & Landing Page Agêntico

Diagnosticar páginas de conversão e preparar hipóteses, textos e planos de experimentos para landing pages.

Adaptação do squad de Marketing da Máquina de Receita para uso como skill. Os agentes, tarefas, critérios e contratos originais estão preservados nas referências.

## When to Use

- Use para diagnosticar páginas de conversão e preparar hipóteses, textos e planos de experimentos para landing pages.
- Comece com o objetivo, contexto do negócio, dados disponíveis e resultado solicitado; peça somente os insumos que impedem a próxima etapa.
- O pacote oferece procedimentos e papéis especializados. Conexões com CRM, mensageria, mídia, telefonia ou observabilidade dependem das ferramentas disponíveis e da configuração do ambiente.

## Quick Reference

| Necessidade | Referência |
|---|---|
| Contexto, problema, entregável e integrações previstas | [README original](references/squad/README.md) |
| Entrada: Maestro CRO | [papel do orquestrador](references/squad/agents/maestro-cro.md) |
| Intake e decomposição | [tarefa de entrada](references/squad/tasks/orquestrar-pipeline.md) |
| Ordem das fases, contratos, critérios e vetos | [workflow](references/squad/workflows/marketing-cro-landing-agentico-pipeline.yaml) |
| Verificação das saídas | [critic-rex-2](references/squad/checklists/critic-rex-2.md) |
| Dependências e configuração original | [config.yaml](references/squad/config.yaml) |
| Proveniência, integridade e direitos de uso | [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE) |

## Procedure

1. Leia o papel de **Maestro CRO** e a tarefa de entrada. Confirme o recorte solicitado e os dados de entrada exigidos; registre lacunas sem preencher resultados com dados inventados.
2. Leia o [workflow](references/squad/workflows/marketing-cro-landing-agentico-pipeline.yaml) para selecionar as fases pertinentes. Use os critérios de entrada e saída de cada tarefa como contrato e mantenha a rastreabilidade entre evidência e conclusão.
3. Execute a sequência abaixo. Carregue o arquivo do papel e da tarefa somente quando chegar à etapa correspondente. Havendo subagentes disponíveis, delegue etapas independentes; em um runtime sem subagentes, realize os mesmos papéis sequencialmente, separando produção e revisão.

| Etapa | Papel | Instrução |
|---|---|---|
| Intake e decomposição | [Maestro CRO](references/squad/agents/maestro-cro.md) | [orquestrar-pipeline](references/squad/tasks/orquestrar-pipeline.md) |
| Identificar Abandono Página | [Hera](references/squad/agents/hera.md) | [identificar-abandono-pagina](references/squad/tasks/identificar-abandono-pagina.md) |
| Pesquisar Evidências Empíricas | [Sage](references/squad/agents/sage.md) | [pesquisar-evidencias-empiricas](references/squad/tasks/pesquisar-evidencias-empiricas.md) |
| Gerar Copy de Conversao | [Muse](references/squad/agents/muse.md) | [gerar-copy-de-conversao](references/squad/tasks/gerar-copy-de-conversao.md) |
| Traduzir Hipoteses De Layout | [Pixel](references/squad/agents/pixel.md) | [traduzir-hipoteses-de-layout](references/squad/tasks/traduzir-hipoteses-de-layout.md) |
| Monitorar Experimentos Ab | [Darwin](references/squad/agents/darwin.md) | [monitorar-experimentos-ab](references/squad/tasks/monitorar-experimentos-ab.md) |
| Verificar Brand Voice Consistência | [Rex](references/squad/agents/rex.md) | [verificar-brand-voice-consistencia](references/squad/tasks/verificar-brand-voice-consistencia.md) |
| Documentar Experimentos | [Atlas](references/squad/agents/atlas.md) | [documentar-experimentos](references/squad/tasks/documentar-experimentos.md) |
| Verificação do critic | [Rex 2](references/squad/agents/rex-2.md) | [verificar-saidas](references/squad/tasks/verificar-saidas.md) |
| Gates humanos e entrega | [Maestro CRO](references/squad/agents/maestro-cro.md) | Consolidar resultados e gates do workflow |

4. Trate comandos `@squad:agente` e `*tarefa` dos arquivos originais como nomes de papéis e procedimentos; eles não são comandos de shell nem ferramentas nativas do ClariFlix. Resolva caminhos de agentes, tarefas, workflows, checklists e configuração a partir de `references/squad/`, inclusive quando a fonte mencionar `squads/marketing-cro-landing-agentico/`.
5. Use ferramentas externas somente quando estiverem disponíveis, configuradas e autorizadas para a tarefa. Sem integração, trabalhe com os dados fornecidos e entregue análises, minutas ou planos locais; identifique atividades externas pendentes. Não marque campanhas, contatos, registros ou automações como executados apenas por terem sido planejados.
6. Antes de cada ação sujeita a gate, apresente o artefato concreto e registre a decisão humana. A instalação da skill não equivale à aprovação dos gates. Preserve também os checkpoints e vetos do [workflow](references/squad/workflows/marketing-cro-landing-agentico-pipeline.yaml).

### Gates humanos deste squad

- **HITL** — Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3): a empresa precisa concordar com o diagnóstico antes de escalar produção
- **HITL** — Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de produto ou páginas com > 50% do budget de tráfego (L3): mudanças de alto impacto requerem olho humano final
- **HITL** — Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qualquer reescrita (L3)
- **HITL** — Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão estratégica que requer stakeholders (L3)
- **HITL** — Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, métrica primária e budget de tráfego (L3)
- **HITL** — Escalada de experimento inconclusivo após 4 semanas — Darwin alerta, Maestro analisa, mas decisão de encerrar ou aumentar tráfego para o teste e humana (L1): implica realocação de budget
- **HITL** — Revisao trimestral do CRO Playbook — Atlas apresenta o estado do conhecimento acumulado, Growth Lead decide quais learnings viram regras permanentes e quais hipoteses devem ser arquivadas (L1)

7. Aplique [critic-rex-2](references/squad/checklists/critic-rex-2.md) e registre um veredito com evidência por item. Corrija falhas conforme o limite de tentativas do workflow; se persistirem, entregue o bloqueio e a informação necessária para resolvê-lo.
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
