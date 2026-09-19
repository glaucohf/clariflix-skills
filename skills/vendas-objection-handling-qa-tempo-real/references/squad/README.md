# Squad de Objection Handling e Q&A em Tempo Real

> Seu vendedor nunca mais trava numa objeção — a resposta certa chega antes do silêncio constrangedor.

**Área:** Vendas · **TopSquad:** V5 Sales Enablement & Conversation Intelligence · **Prioridade:** avançado · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Vendedores travam em objeções ('é muito caro', 'já temos um fornecedor', 'não é o momento') e em dúvidas técnicas durante a conversa de vendas ativa — seja em call, WhatsApp ou reunião presencial. Sem suporte em tempo real, o vendedor improvisa, erra a resposta, perde credibilidade ou simplesmente deixa o momento de fechamento escapar. O resultado é inconsistência de discurso entre vendedores, deals perdidos por causa de objeções que poderiam ser rebatidas, e ciclos de vendas mais longos por falta de resposta técnica no momento certo. Em operações com SDRs e closers separados (modelo agência/imobiliária), o problema é ainda maior: o SDR qualifica mas não sabe responder técnico; o closer fecha mas não tem battlecard de objeção atualizado.

## Impacto esperado

Redução de 30-50% no tempo médio de resposta a objeções em call (de busca manual + improvisação para resposta estruturada em < 15 segundos). Aumento estimado de 15-30% na taxa de conversão de deals que chegam ao momento de objeção — o principal gargalo pre-fechamento. Para uma operação com 5 closers fazendo 10 calls/semana, recuperar 2 deals por semana de deals que travariam em objeção representa, a ticket médio de R$5.000, R$10.000/semana adicional ou R$520.000/ano. ROI estimado: 20-40x sobre o custo do squad no primeiro ano de operação. Benefício adicional: padronização do discurso de objeção — todos os vendedores respondem igual ao melhor do time, eliminando variância de performance.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro` · MAESTRO | MAESTRO — O Regente Comercial | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `rebound` · REBOUND | REBOUND — O Rebatedor de Objeções de Preço e Valor | L1 · worker autônomo | `rebater-objecoes-de-preco.md` |
| `tempo` · TEMPO | TÉMPO — O Rebatedor de Objeções de Timing e Prioridade | L1 · worker autônomo | `rebater-objecoes-timing.md` |
| `challenger` · CHALLENGER | CHALLENGER — O Rebatedor de Objeções de Concorrente e Status Quo | L1 · worker autônomo | `rebater-objecoes-concorrente.md` |
| `tecnico` · TECNICO | TÉCNICO — O Especialista em Q&A de Produto e Integração | L2 · orquestra / decide | `responder-duvidas-tecnicas.md` |
| `closer` · CLOSER | CLOSER — O Especialista em Objeções de Autoridade e Fechamento | L1 · worker autônomo | `resolver-objecao-autoridade.md` |
| `arquivo` · ARQUIVO | ARQUIVO — O Gestor de Inteligência e Aprendizado Contínuo | L3 · aprovação humana | `analisar-objecoes-frequentes.md` |
| `argus` · ARGUS | ARGUS — O Verificador de Factualidade e Tom | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-objection-handling-qa-tempo-real:maestro` (ou instale via `npx squads add ./vendas-objection-handling-qa-tempo-real`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-objection-handling-qa-tempo-real-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Qualquer resposta que envolva promessa de desconto acima do nível autorizado para o vendedor: MAESTRO pausa, notifica supervisor ou gerente de vendas via Slack/WhatsApp, que aprova ou rejeita em tempo real antes da resposta chegar ao vendedor
- L3 — Qualquer resposta a dúvida técnica que envolva prazo de implementação customizado, SLA não padrão, ou integração não documentada na base: TÉCNICO flag como HITL, vendedor recebe instrução 'vou confirmar com a equipe técnica e te retorno em X horas' em vez de uma promessa não verificada
- L3 — Escrita de resultados de call e atualização de stage no CRM pelo ARQUIVO: vendedor confirma o resultado via formulário rápido (1 click) antes de qualquer persistência em CRM de produção
- L2 — Quando ARGUS emite REJEITADO por factualidade: MAESTRO notifica o vendedor que a resposta está sendo verificada e entrega uma resposta genérica segura enquanto o worker corrige — o vendedor decide se usa a genérica ou aguarda a corrigida
- L1 — Objecão nova não catalogada (aparece pela primeira vez): ARQUIVO sinaliza ao líder de vendas ou product owner que uma nova objecão foi detectada e sugere draft de resposta para validação antes de entrar na base — o líder aprova, edita ou rejeita o draft

## KPIs

- Latência end-to-end: tempo do sinal de entrada (objeção digitada/transcrita) até resposta entregue ao vendedor — meta P50 < 8 segundos, P95 < 15 segundos
- Taxa de cobertura: % de objeções recebidas que foram respondidas pela base catalogada (vs nova/não catalogada) — meta > 85% em 60 dias de operação
- Taxa de uso pelo vendedor: % de respostas entregues que o vendedor efetivamente usou (copiou/clicou) — meta > 60% (mede relevância das respostas, não apenas entrega)
- Taxa de aprovação do ARGUS na primeira passagem: meta > 88% (staging) / > 96% (produção) — mede qualidade dos workers
- Taxa de conversão pós-objeção: % de objeções onde a resposta do squad foi usada e o deal avançou de stage — meta > 40% (vs baseline pré-squad a ser medido nos primeiros 30 dias)
- Redução de deals perdidos por objeção de preço/concorrente: comparar cohort de deals com squad ativo vs histórico sem squad — meta -25% de deals perdidos nestas categorias
- Tempo de resposta do vendedor a objeção (medido via conversation intelligence): redução de silêncio/hesitação em call — meta redução de 60% no tempo médio de resposta após ativação do squad
- Crescimento da base de battlecards: número de novas objeções catalogadas e validadas por semana — meta 3-5 novas objeções/semana nos primeiros 90 dias (demonstra aprendizado contínuo)

## Integrações

- CRM: HubSpot (MCP disponível) ou Pipedrive — leitura de contexto do deal e prospect em tempo real pelo MAESTRO; escrita de resultados e atualização de battlecards pelo ARQUIVO (L3 gate)
- WhatsApp Business API (Gupshup, AiSensy, ou QuickReply.ai) — canal primário de acionamento do squad por SDRs e closers no Brasil; entrega de resposta como mensagem rápida copiável
- Interface de call em tempo real: integração com Vapi ou Retell AI para captura de transcrição ao vivo; widget de overlay na tela do vendedor durante a call com resposta em < 15 segundos
- STT em tempo real: Deepgram para transcrição da fala do prospect durante calls, alimentando o MAESTRO com o texto da objeção antes mesmo do vendedor digitar
- Conversation Intelligence: Gong ou Chorus — analise pos-call para identificar objecoes que ocorreram e se foram superadas; dados alimentam ARQUIVO para aprendizado continuo
- ClickUp: registro de cada interação de objection handling como tarefa/artefato verificável com resultado; prova de trabalho do squad por deal
- Slack: notificações de HITL para supervisores (aprovação de desconto, nova objeção detectada); relatório semanal de padrões de objeção para liderança de vendas
- Base vetorial: Supabase pgvector ou Pinecone — armazenamento e busca semântica da base de battlecards, respostas históricas e casos de uso para recuperação em < 3 segundos
- Observabilidade: Langfuse (OTEL) — rastreamento de latência por worker, taxa de aprovação do ARGUS, taxa de uso pelo vendedor (resposta entregue vs resposta efetivamente usada), quality gates dev 70% / staging 85% / prod 95%
- Orquestração: LangGraph ou Claude Agent SDK — controle de estado por sessão de call, paralelismo dos workers de recuperação (battlecard + contexto), retry logic com fallback para resposta genérica se SLA estourar

## Entregável (prova de trabalho)

Pacote de Resposta de Objeção — entregue em < 15 segundos ao vendedor em qualquer canal ativo (widget de call, WhatsApp, chat do CRM): (1) Resposta Principal pronta para falar ou copiar/colar (max 2 linhas, linguagem conversacional do canal), (2) Argumento de Suporte com 2-3 bullets de dado/caso/lógica para aprofundar, (3) Pergunta de Redirecionamento para retomar controle da conversa após a resposta. Artefato verificável registrado no ClickUp por deal com: objeção recebida, worker acionado, resposta entregue, resultado da call. Relatório semanal de inteligência de objeções entregue à liderança de vendas via Slack/email: top objeções da semana, taxas de conversão por tipo, novos padrões detectados, sugestões de atualização de playbook.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Skeptic Protocol (5 agentes, red-team/QA) — arquitetura de critic/verifier multi-camada diretamente reusavel para o ARGUS; padrao de verificacao de factualidade e deteccao de afirmacoes nao suportadas por evidencia aplicavel a auditoria de respostas de objecao antes da entrega ao vendedor
- Win Proposal Deal (4 agentes, propostas comerciais) — lógica de construção de argumentação comercial e estrutura de battlecard competitivo reusável pelos workers REBOUND e CHALLENGER; padrão de personalização por perfil de prospect reusável pelo MAESTRO na injeção de contexto
- Apex Context Supreme (5 agentes, context engineering) — técnicas de compressão de contexto para garantir que a resposta entregue em tempo real seja densa e acionável em < 5 segundos de leitura; padrão de priorização de informação por urgência temporal reusável dado o SLA crítico do squad

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V5 · TopSquad de Sales Enablement & Conversation Intelligence** — O copiloto do closer: contexto antes, respostas durante, coaching depois.

- **Missão:** Tudo que torna o vendedor humano melhor: prepara o contexto da conta e battlecards antes da call, sugere respostas a objeções durante, e analisa a gravação para coaching depois. Um cérebro de enablement do pré ao pós-call.
- **Por que consolidar:** Os três bebem da mesma fonte: a base de conhecimento de produto, concorrência e conversas reais. Battlecards alimentam o objection handling, que alimenta o coaching, que descobre novas objeções para os battlecards. Era um ciclo partido em três; unido, ele se retroalimenta.
- **Squads irmãos:** Conversation Intelligence & Coaching, Objection Handling & Q&A em Tempo Real, Inteligência de Conta & Battlecards

## Estrutura

```
vendas-objection-handling-qa-tempo-real/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
