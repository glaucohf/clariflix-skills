---
task: stella()
responsavel: "Stella"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados de clientes convertidos do CRM (HubSpot/Salesforce): cargo, setor, tamanho de empresa, fonte de aquisição, objeção principal no ciclo de vendas, tempo de fechamento + Reviews públicos de concorrentes (G2, Capterra, Trustpilot, Google Reviews) + Comentários em grupos e comunidades do setor (LinkedIn, Reddit, grupos de WhatsApp do cliente se disponível) + Histórico de criativos top performers com seus ângulos de mensagem + Calendário de iteração definido pelo Orion (qual o foco da próxima wave de criativos)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "ICP Creative Brief (JSON estruturado): (1) Mapa de dores por segmento de ICP (3-5 dores rankeadas por frequência e intensidade), (2) Vocabulário nativo por dor (as palavras exatas que o ICP usa"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "não o jargão da empresa), (3) Objeções de compra top-3 com os contrapontos mais eficazes, (4) Momentos de decisão (o que precipita a busca por uma solução), (5) Ângulos de mensagem recomendados para o próximo ciclo com justificativa baseada em dados, (6) Hooks sugeridos por formato (vídeo/static/carousel) com exemplos de linguagem"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Sempre inclui fonte de cada insight (dado de CRM, review específico, comunidade)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orion no início de cada ciclo de produção (semanal ou a cada nova wave de criativos). Re-acionado se o Aegis rejeitar mais de 30% dos conceitos por desalinhamento com ICP (sinal de que…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aegis 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do squad operar — sem essa base o Aegis não tem referência para validar, e o squad não ativa"
    - "[ ] HITL: Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento ao creator) — o Hoox gera o brief e aguarda aprovação explícita do humano responsável via Slack/WhatsApp antes de publicar. O cliente vê o brief completo, o perfil de creator selecionado e o custo estimado"
    - "[ ] HITL: Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados anteriormente, o responsavel de midia revisa o preview antes da ativacao — as primeiras impressoes de um criativo novo sao irreversiveis"
    - "[ ] HITL: Gate L3 — Escala de criativo vencedor acima de threshold de budget: quando o Nexus identifica um vencedor e o Orion recomenda escala (aumento de budget > X% acima do threshold pre-definido), o humano aprova o aumento antes da execução pelo squad de media buying (ou pelo cliente diretamente)"
    - "[ ] HITL: Aprovação do ICP Creative Brief (apos cada ciclo da Stella): o cliente valida o mapa de dores/ângulos proposto pela Stella antes do Vega começar a conceitualização — garante que os insights estão corretos e alinhados com o momento estratégico da empresa"
---

# Analisar Dados E Intentões

**Task ID:** `stella()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Creative UGC Factory

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Dados E Intentões |
| **status** | `pending` |
| **responsible_executor** | Stella (Stella — ICP & Insight Analyst) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de pesquisa aprofundada de ICP e inteligencia criativa. Combina dados estruturados do CRM (perfil dos clientes convertidos), pesquisa de mercado (comentarios em reviews, Reddit, grupos do setor, concorrentes), e sinais de intent para construir o mapa de dores/desejos/objecoes/vocabulario nativo do ICP em cada momento da jornada. Gera synthetic personas com nível de detalhe operacional: nao 'empresa de medio porte' mas 'CFO de SaaS B2B com 50-200 funcionarios que ja queimou com implementacao de ERP e agora esta cansado de promessas'. Alimenta todos os outros agentes com o contexto de ICP necessario para que cada criativo fale a lingua certa.

## Input

- Dados de clientes convertidos do CRM (HubSpot/Salesforce): cargo, setor, tamanho de empresa, fonte de aquisição, objeção principal no ciclo de vendas, tempo de fechamento + Reviews públicos de concorrentes (G2, Capterra, Trustpilot, Google Reviews) + Comentários em grupos e comunidades do setor (LinkedIn, Reddit, grupos de WhatsApp do cliente se disponível) + Histórico de criativos top performers com seus ângulos de mensagem + Calendário de iteração definido pelo Orion (qual o foco da próxima wave de criativos)

## Output

- ICP Creative Brief (JSON estruturado): (1) Mapa de dores por segmento de ICP (3-5 dores rankeadas por frequência e intensidade), (2) Vocabulário nativo por dor (as palavras exatas que o ICP usa
- não o jargão da empresa), (3) Objeções de compra top-3 com os contrapontos mais eficazes, (4) Momentos de decisão (o que precipita a busca por uma solução), (5) Ângulos de mensagem recomendados para o próximo ciclo com justificativa baseada em dados, (6) Hooks sugeridos por formato (vídeo/static/carousel) com exemplos de linguagem
- Sempre inclui fonte de cada insight (dado de CRM, review específico, comunidade)

## Trigger

Acionado pelo Orion no início de cada ciclo de produção (semanal ou a cada nova wave de criativos). Re-acionado se o Aegis rejeitar mais de 30% dos conceitos por desalinhamento com ICP (sinal de que o brief de ICP está desatualizado). Acionado manualmente pelo cliente ou gestor quando há mudança de segmento ou lançamento de novo produto.

## Knowledge base (o que o executor consulta)

- Perfis de clientes convertidos (ultimos 12 meses) com dados de firmographia e historico de venda, Banco de reviews de concorrentes (atualizado quinzenalmente), Transcricoes de calls de vendas (se disponivel
- extrair objecoes e linguagem), Brand voice guidelines e claims aprovados, Historico de criativos com performance >= threshold (angulos validados), Benchmarks setoriais de hook rate e CTR por formato e nicho

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados de clientes convertidos do CRM (HubSpot/Salesforce): cargo, setor, tamanho de empresa, fonte de aquisição, objeçã…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (ICP Creative Brief (JSON estruturado): (1) Mapa de dores por segmento de ICP (3-5 dores rankeadas por frequência e inte…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: ICP Creative Brief (JSON estruturado): (1) Mapa de dores por segmento de ICP (3-5 dores rankeadas por frequência e intensidade), (2) Vocabulário nativo por dor…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aegis 2 registrado
- [ ] Gate HITL respeitado: Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do…
- [ ] Gate HITL respeitado: Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento a…
- [ ] Gate HITL respeitado: Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de Brand Voice Guidelines e Claims: o cliente assina o documento de brand voice e a lista de claims aprovados/proibidos antes do squad operar — sem e… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Gate L3 — Publicação de Brief de UGC na plataforma (Hoox/Insense): publicar um brief de creator envolve compromisso financeiro (pagamento ao creator) — o Hoox… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate L3 — Upload de novos criativos para plataforma de anuncio (primeira vez): quando o Nexus cria novos ad sets com criativos nao testados anteriormente, o re… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate L3 — Escala de criativo vencedor acima de threshold de budget: quando o Nexus identifica um vencedor e o Orion recomenda escala (aumento de budget > X% ac… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação do ICP Creative Brief (apos cada ciclo da Stella): o cliente valida o mapa de dores/ângulos proposto pela Stella antes do Vega começar a conceitualiz… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão do Preview Sheet semanal (opcional, recomendado): o Sigma gera um mosaico visual de todos os assets da semana — o cliente pode revisar e vetar conceito… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibração mensal de thresholds: reunião de 30 minutos para revisar os thresholds de vencedor/arquivamento com base na performance real do mês — o squad opera… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Onboarding de novo creator no banco aprovado: qualquer creator novo (nao pre-validado) que va ser contratado pelo Hoox requer aprovacao do cliente antes de rec… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Aegis 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vega
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
