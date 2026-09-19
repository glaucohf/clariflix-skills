# Squad de Recuperação de Oportunidades Estagnadas

> Nenhum deal morre de inercial — reativamos receita parada antes que o concorrente a pegue.

**Área:** Vendas · **TopSquad:** V4 Nurture, Follow-up & Reativação · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Oportunidades param no funil sem próximo passo definido e ninguém age a tempo: deals frios no CRM, carrinhos abandonados, leads que responderam uma vez e sumiram. Cada deal estagnado é receita já quase ganha que se perde por inércia operacional — não por falta de interesse do lead.

## Impacto esperado

Recuperação de 15-35% das oportunidades paradas converte em receita incremental sem novo custo de aquisição (CAC zero na recuperação). Para uma carteira de 200 deals estagnados com ticket médio de R$5k, o squad potencializa R$150k-350k de receita recuperável por ciclo. ROI esperado: 8-20x sobre o custo do squad em 90 dias. Redução de 70% no tempo de resposta para reativação (de dias para minutos). Eliminação de 90% do trabalho manual de follow-up.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orquestrador-de-recuperacao` · Orquestrador de Recuperação | Resgate (Orquestrador de Recuperação) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `worker-de-deteccao-e-triagem` · Worker de Detecção e Triagem | Radar (Worker de Detecção e Triagem) | L0 · worker determinístico | `detectar-sinais-de-estagnacao.md` |
| `escavador` · Escavador | Escavador (Worker de Enriquecimento Contextual) | L1 · worker autônomo | `enriquecer-contexto-lead.md` |
| `arquiteto` · Arquiteto | Arquiteto (Worker de Playbook e Roteiro de Recuperação) | L2 · orquestra / decide | `personalizar-sequencia-mensagens.md` |
| `critic-e-verifier-de-mensagens` · Critic e Verifier de Mensagens | Guardião (Critic e Verifier de Mensagens) | L1 · worker autônomo | `verificar-mensagens.md` |
| `worker-de-outreach-multicanal` · Worker de Outreach Multicanal | Mensageiro (Worker de Outreach Multicanal) | L3 · aprovação humana | `enviar-mensagens-multicanal.md` |
| `monge` · Monge | Monge (Worker de Nurture e Cadência Longa) | L2 · orquestra / decide | `nutrir-leads-longo-prazo.md` |
| `forense` · Forense | Forense (Worker de Análise de Perdas e Feedback Loop) | L1 · worker autônomo | `analisar-abandono-em-etapas.md` |
| `critic-e-verifier-de-mensagens-2` · Critic e Verifier de Mensagens 2 | Guardião (Critic e Verifier de Mensagens) | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@vendas-recuperacao-oportunidades-estagnadas:orquestrador-de-recuperacao` (ou instale via `npx squads add ./vendas-recuperacao-oportunidades-estagnadas`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/vendas-recuperacao-oportunidades-estagnadas-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeiro toque automatizado — gate L3 no Mensageiro)
- Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa
- Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável comercial
- Mudança de playbook baseada em proposta do Forense — ajustes em playbooks existentes exigem aprovação humana antes de entrar em produção
- Primeiro contato via voz (Vapi/Retell) para leads de alto valor — script revisado e aprovado pelo responsavel antes do disparo
- Opt-out recebido — registrado imediatamente, comunicado ao comercial, nenhuma acao adicional automatica alem do registro de compliance

## KPIs

- Taxa de Recuperação: % de deals estagnados que retomaram atividade após intervenção do squad (meta: 15-35% em 30 dias)
- Receita Recuperada: R$ de oportunidades reativadas que fecharam em 90 dias pós-ativação do squad
- Tempo Médio de Detecção-a-Primeiro-Toque: minutos entre detecção de estagnação e envío da primeira mensagem (meta: <15 min)
- Taxa de Resposta por Canal: % de mensagens que geraram resposta por canal (WhatsApp, email, LinkedIn, voz)
- Opt-out Rate: % de leads que solicitaram descadastramento (meta: <1% — indica qualidade da personalizacao)
- Playbook Conversion Rate: % de deals em cada playbook que convertêram (identifica playbooks eficazes x ineficazes)
- Task Success Rate: % de tasks completadas com sucesso nos quality gates (meta: dev 70% / staging 85% / prod 95%)
- HITL Trigger Rate: % de deals que necessitaram aprovação humana (calibra o nível de autonomia do squad)
- CAC de Recuperação: R$0 — toda oportunidade recuperada e receita incremental sem novo custo de aquisição

## Integrações

- CRM: HubSpot (MCP disponível), Pipedrive, Salesforce — fonte de verdade de deals e histórico
- WhatsApp Business API: Gupshup, AiSensy ou Interakt — canal principal de recuperação no Brasil
- Email: SMTP/SendGrid ou sequenciador (Apollo, Instantly) — cadências de nurture e follow-up
- LinkedIn Sales Navigator — enriquecimento de contexto e outreach via Escavador
- Voz: Vapi (<600ms latência) ou Retell AI + ElevenLabs TTS — recuperação via ligação para deals de alto valor
- Enriquecimento: Clay ou Apollo (275M+ contatos) — Escavador busca sinais externos
- E-commerce/Carrinho: Shopify, WooCommerce, Hotmart — webhooks de abandono de carrinho
- ClickUp — gestão de tarefas, prova de trabalho, artefatos verificáveis por deal
- Langfuse (OTEL) — observabilidade, evals e quality gates (dev 70% / staging 85% / prod 95%)
- Google Calendar / Calendly — booking de reuniões de reativação pelo Worker de Agendamento (quando integrado)
- Slack / Teams — alertas de resposta e HITL gates para comerciais humanos

## Entregável (prova de trabalho)

Painel de Recuperação Ativa no ClickUp com: (1) Mapa de Oportunidades Estagnadas atualizado em tempo real por bucket e valor em risco, (2) Log de cada tentativa de recuperação com status e resultado (artefato verificável por deal), (3) Relatório semanal de conversões e perdas com análise de padrões do Forense, (4) Biblioteca de playbooks vivos atualizados por feedback loop, (5) Dashboard de KPIs de recuperação com comparativo antes/depois da implantação do squad.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mae Intuitiva CRM (squads.sh) — base para integração CRM, gestão de leads e cadências de follow-up; acelera a construção dos workers Radar e Monge
- Win Proposal Deal (4 agentes, myclaude) — base para o worker Arquiteto de Playbook e o fluxo de proposta/reativação pos-estagnação
- Data Quality Guardian (5 agentes) — base para o worker Forense e o loop de feedback/analise de qualidade dos dados de recuperacao

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**V4 · TopSquad de Nurture, Follow-up & Reativação** — Nenhum lead morto: reaquece deals parados, leads frios e públicos pós-evento.

- **Missão:** O squad da memória longa do funil: detecta qualquer lead/deal que esfriou — sem resposta, estagnado no pipeline ou inerte após um evento/webinar — e dispara a cadência de reaquecimento certa para o motivo certo.
- **Por que consolidar:** Os três faziam a mesma coisa — reaquecer quem parou de avançar — variando só o gatilho (silêncio, deal estagnado, fim de evento). Compartilham biblioteca de cadências, lógica de decaimento e regra de "quando desistir". Um squad só evita três motores de cadência concorrendo pelo mesmo lead.
- **Squads irmãos:** Follow-up, Nurture e Reativação, Recuperação de Oportunidades Estagnadas, Reengajamento Pós-Evento e Webinar

## Estrutura

```
vendas-recuperacao-oportunidades-estagnadas/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
