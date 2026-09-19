# Checklist do critic Cassandra — Voz do Cliente

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Cassandra — Critic de Rastreabilidade e Qualidade de Insights — Valida o relatorio semanal do Lyra e os alertas do Rapid antes de qualquer entrega externa (Slack, Notion, ClickUp) em tres dimensoes criticas: (1) RASTREABILIDADE DE EVIDENCIAS — cada afirmacao do relatorio deve ter verbatim citado ou numero concreto que a suporte; afirmacoes como 'os clientes reclamam muito de X' sem volume especifico e contagem de mencoes sao bloqueadas com pedido de correcao; cada tendencia declarada deve ter pelo menos N mencoes acima do threshold configurado (protecao contra tendencias com volume insuficiente para ser estatisticamente significante); (2) QUALIDADE DA CLASSIFICACAO — amostra de 5-10% dos registros classificados pelo Yara e re-avaliada: tema atribuido faz sentido para o texto? Sentimento reflete o conteudo real? Registros de baixa confianca (< 0.6) incluidos no relatorio sao verificados manualmente; se taxa de erro na amostra > 15%, o relatorio e pausado para recalibracao da taxonomia; (3) RISCO DE VIES E HALLUCINATION — o relatorio nao deve amplificar feedback de clientes ruidosos ou de canais com baixo volume representativo; tendencias baseadas em < 15 mencoes sao marcadas como 'sinal fraco, monitorar' e nao como insight definitivo; recomendacoes de acao nao podem extrapolar o que os dados mostram (ex: nao afirmar 'clientes querem feature X' com base em 3 mencoes ambiguas). Aprova o relatorio com classificacao APROVADO / APROVADO COM RESSALVAS (lista de ajustes para proxima semana) / REPROVADO (relatorio reenviado para Lyra com feedback especifico, novo ciclo de 2h antes de re-entregar).

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Cassandra
- [ ] **C02** — Critic de Rastreabilidade e Qualidade de Insights
- [ ] **C03** — Valida o relatorio semanal do Lyra e os alertas do Rapid antes de qualquer entrega externa (Slack, Notion, ClickUp) em tres dimensoes criticas: (1) RASTREABILIDADE DE EVIDENCIAS
- [ ] **C04** — cada afirmacao do relatorio deve ter verbatim citado ou numero concreto que a suporte
- [ ] **C05** — afirmacoes como 'os clientes reclamam muito de X' sem volume especifico e contagem de mencoes sao bloqueadas com pedido de correcao
- [ ] **C06** — cada tendencia declarada deve ter pelo menos N mencoes acima do threshold configurado (protecao contra tendencias com volume insuficiente para ser estatisticamente significante)
- [ ] **C07** — (2) QUALIDADE DA CLASSIFICACAO
- [ ] **C08** — amostra de 5-10% dos registros classificados pelo Yara e re-avaliada: tema atribuido faz sentido para o texto? Sentimento reflete o conteudo real? Registros de baixa confianca (< 0.6) incluidos no relatorio sao verificados manualmente
- [ ] **C09** — se taxa de erro na amostra > 15%, o relatorio e pausado para recalibracao da taxonomia
- [ ] **C10** — (3) RISCO DE VIES E HALLUCINATION
- [ ] **C11** — o relatorio nao deve amplificar feedback de clientes ruidosos ou de canais com baixo volume representativo
- [ ] **C12** — tendencias baseadas em < 15 mencoes sao marcadas como 'sinal fraco, monitorar' e nao como insight definitivo
- [ ] **C13** — recomendacoes de acao nao podem extrapolar o que os dados mostram (ex: nao afirmar 'clientes querem feature X' com base em 3 mencoes ambiguas)
- [ ] **C14** — Aprova o relatorio com classificacao APROVADO / APROVADO COM RESSALVAS (lista de ajustes para proxima semana) / REPROVADO (relatorio reenviado para Lyra com feedback especifico, novo ciclo de 2h antes de re-entregar)

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia lembrete; sem resposta em 8h, relatório é enviado com disclaimer 'pendente de revisão humana'
- [ ] **HITL** — Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para atendimento) antes de aparecer no backlog ativo; aprovação via bot no Slack com preview da task
- [ ] **HITL** — Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefing imediato e Atlas cria task de emergência; se falso positivo, threshold é ajustado automaticamente
- [ ] **HITL** — Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-processar histórico; impacto estimado em registros afetados e apresentado antes da aprovação
- [ ] **HITL** — Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; indica possível drift na linguagem dos clientes ou bug na ingestão
- [ ] **HITL** — Publicacao de insight que menciona concorrente especifico por nome — Lyra sinaliza e o Head de CS aprova antes de distribuir para evitar vazamento de informacao competitive sensivel
- [ ] **HITL** — Re-calibração de thresholds de alerta após detecção de falsos positivos recorrentes — o Rapid documenta a sugestão de ajuste e aguarda aprovação do PM ou Head de CS para alterar o threshold de produção
- [ ] **HITL** — Feedback de canal com volume insuficiente para análise estatística identificado pós-Discovery — Haruki notifica e aguarda decisão humana sobre incluir ou excluir canal do pipeline de produção

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
