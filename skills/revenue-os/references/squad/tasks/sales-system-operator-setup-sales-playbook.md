---
task: Setup Sales Playbook
responsavel: "@sales-system-operator"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - funnel_map: Mapa de funil com etapas
  - offer_stack: Estrutura da oferta e objecoes
  - icp_profile: ICP com dores e jobs
Saida: |
  - sales_playbook: Playbook completo (pipeline + scripts + SLAs)
  - handoff_rules: Regras de transicao MQL -> SQL -> Demo -> Won
  - qualification_framework: Framework BANT/MEDDIC adaptado
Checklist:
  - "[ ] Definir estagios do pipeline com criterios de entrada e saida"
  - "[ ] Definir script de discovery (perguntas de qualificacao)"
  - "[ ] Definir script de demo (flow + talking points)"
  - "[ ] Definir script de fechamento (objecoes + CTA final)"
  - "[ ] Definir SLA de resposta por etapa"
---

# *setup-sales-playbook

Estrutura o playbook comercial para padronizar execucao e elevar taxa de fechamento.

## Step-by-Step

1. **Mapear estagios do pipeline** — Lead -> MQL -> SQL -> Demo -> Proposta -> Won/Lost.
2. **Definir criterios de entrada e saida por estagio** — O que faz avancar, o que faz regredir.
3. **Criar qualification framework** — Adaptar BANT (Budget/Authority/Need/Timeline) ou MEDDIC para o ICP.
4. **Escrever script de discovery** — 5-7 perguntas que qualificam SQL e mapeiam dor.
5. **Escrever script de demo** — Flow + talking points + uso de cases.
6. **Escrever script de fechamento** — Respostas as top 5 objecoes + CTA final claro.
7. **Definir SLAs** — Tempo maximo entre etapas antes de acao corretiva.

## Veto Conditions

- VETO se script for decorado palavra-a-palavra → soa falso, prospect sente
- VETO se qualificacao pular ao menos Budget ou Timeline → deals sem urgencia ficam zombie
- VETO se SLA de resposta >2h no primeiro contato → prospect esfria
- VETO se playbook nao tiver resposta para top 5 objecoes do objection_matrix

## Output Example

```yaml
sales_playbook:
  pipeline:
    - estagio: "Lead"
      criterio_entrada: "Preencheu form ou veio de outbound"
      criterio_saida_para_mql: "Respondeu 1 email ou abriu 3+ emails em 7 dias"
      sla_primeira_acao: "15 min"
      owner: "@commercial-senior-analyst"

    - estagio: "MQL"
      criterio_entrada: "Engajou com conteudo/email"
      criterio_saida_para_sql: "Agendou demo OU confirmou interesse com clarificacao"
      sla_para_contato: "1 dia util"

    - estagio: "SQL"
      criterio_entrada: "BANT qualificado (>=3 de 4 criterios)"
      criterio_saida_para_demo: "Demo agendada no calendario"
      sla_agendamento: "48h"

    - estagio: "Demo Realizada"
      criterio_entrada: "Demo de 30 min completa"
      criterio_saida_para_proposta: "Prospect pediu proposta escrita"
      sla_envio_proposta: "24h pos-demo"

    - estagio: "Proposta Enviada"
      criterio_entrada: "Proposta enviada por email com link checkout"
      criterio_saida_won: "Pagamento confirmado"
      criterio_saida_lost: "14 dias sem movimento + email de close-loop"
      sla_follow_up: "3, 7, 14 dias"

qualification_framework:
  modelo: "BANT adaptado"
  perguntas_discovery:
    - "Qual seu contexto de negocio atual? (Need)"
    - "Quanto ja esta faturando ou qual a meta de 90 dias? (Timeline + Need)"
    - "Qual seu budget mensal pra investir em receita? (Budget)"
    - "Voce decide ou precisa validar com socio/time? (Authority)"
    - "Pra quando precisa comecar a faturar? (Timeline)"
    - "O que voce ja tentou e nao funcionou? (Need + dor)"
    - "Se nao resolvermos isso em 90 dias, qual o impacto no seu negocio? (Urgencia)"

  criterio_sql:
    minimo: "3 de 4 BANT (mas Budget OR Need sempre obrigatorio)"
    exemplos_sql: "Tem meta + budget + dor clara + decisor"
    exemplos_nao_sql: "Curiosidade apenas, sem budget"

scripts:
  discovery_script:
    abertura: "Obrigado por agendar. Vou te fazer 5-7 perguntas pra entender melhor seu contexto, ok?"
    perguntas: [discovery_above]
    fechamento_discovery: "Baseado no que voce me contou, faz sentido uma demo de 30 min onde te mostro exatamente como resolver {dor_principal}?"

  demo_script:
    duracao: "30 min"
    flow:
      - "5 min: Recap do contexto do prospect + dor identificada"
      - "15 min: Walkthrough do squad resolvendo a dor especifica (nao tour generico)"
      - "5 min: Case real relevante ao segmento do prospect"
      - "5 min: Q&A + proxima step"
    talking_points:
      - "Enfatizar skin in the game (dogfooding)"
      - "Mostrar dashboard real, nao mockup"
      - "Deixar o prospect fazer 2-3 perguntas antes do pitch final"

  fechamento_script:
    cta_final: "Vou te enviar a proposta com link de checkout. Se fechar ate sexta, temos bonus X. Faz sentido?"
    top_5_objecoes_responses:
      "Preciso pensar": "Claro. O que especificamente te deixa em duvida? Posso clarear agora?"
      "Esta caro": "Entendo. Comparado a contratar CCO (R$ 25k/mes) ou fazer sozinho (custo de oportunidade), onde voce compara?"
      "Nao tenho tempo": "O squad te diz o proximo passo. Sao 2-4h/semana. Mais que isso?"
      "Vou rodar depois": "Quando? Posso te colocar num slot garantido pra daqui X semanas"
      "Preciso falar com meu socio": "Faz sentido. Podemos fazer call a 3 amanha as 14h?"

handoff_rules:
  mql_para_sql:
    owner_anterior: "Marketing (email nurturing)"
    owner_posterior: "@commercial-senior-analyst"
    artefato: "Handoff note com contexto do prospect"

  sql_para_demo:
    owner: "@commercial-senior-analyst"
    artefato: "Prep call com BANT preenchido"

  demo_para_proposta:
    artefato: "Proposta personalizada em 24h"

  won_para_customer_success:
    owner_anterior: "@commercial-senior-analyst"
    owner_posterior: "@revenue-chief"
    artefato: "Welcome package + onboarding call agendada"
```

## Completion Criteria

- Pipeline com 5-6 estagios + criterios objetivos de entrada/saida
- Discovery script com 5-7 perguntas cobrindo BANT
- Demo script estruturado em flow + talking points
- Top 5 objecoes com resposta preparada
- SLAs definidos por estagio

## Handoff

Playbook treinado com `@commercial-senior-analyst`. Scripts viram snippets no CRM. Review mensal em `*control-weekly-metrics`.
