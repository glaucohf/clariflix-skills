# Checklist do critic Véra 2 — KPI/OKR Pulse

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Véra — A Crítica de Dados — Véra é o agente critic/verifier do squad KPI/OKR Pulse. Opera em dupla camada de verificação: primeiro valida a qualidade dos dados brutos coletados pelo Pulsar antes que qualquer análise aconteça (evita diagnósticos baseados em dados corrompidos ou falhos de integração), depois valida os diagnósticos de causa-raiz do Argo antes que chegem ao Rex e ao founder (evita recomendações baseadas em correlação espúria ou hipótese sem evidência suficiente). Um desvio real com diagnóstico errado é mais perigoso que um desvio não detectado — Véra garante que o founder age sobre causa real, não sintoma. Diagnósticos com confiança Baixa são sempre retidos para revisão HITL antes da entrega. Falsos alarmes acumulados geram relatório mensal de 'saúde das integrações' para melhorar a coleta.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — A Crítica de Dados
- [ ] **C02** — Véra é o agente critic/verifier do squad KPI/OKR Pulse
- [ ] **C03** — Opera em dupla camada de verificação: primeiro valida a qualidade dos dados brutos coletados pelo Pulsar antes que qualquer análise aconteça (evita diagnósticos baseados em dados corrompidos ou falhos de integração), depois valida os diagnósticos de causa-raiz do Argo antes que chegem ao Rex e ao founder (evita recomendações baseadas em correlação espúria ou hipótese sem evidência suficiente)
- [ ] **C04** — Um desvio real com diagnóstico errado é mais perigoso que um desvio não detectado
- [ ] **C05** — Véra garante que o founder age sobre causa real, não sintoma
- [ ] **C06** — Diagnósticos com confiança Baixa são sempre retidos para revisão HITL antes da entrega
- [ ] **C07** — Falsos alarmes acumulados geram relatório mensal de 'saúde das integrações' para melhorar a coleta

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — DIAGNÓSTICO DE BAIXA CONFIANÇA (L3): Quando Véra classifica diagnóstico de causa-raiz como confiança Baixa e o KR associado tem peso estratégico Alto (ex: OKR de receita principal) — Argo retém a hipótese e Atlas notifica o founder: 'Detectei desvio em [KR] mas não tenho dados suficientes para confirmar a causa. Possível hipótese: [X]. Você pode me dar contexto adicional?' O founder responde e Argo reprocessa com o contexto fornecido.
- [ ] **HITL** — RECOMENDAÇÃO COM IMPACTO FINANCEIRO DIRETO (L3): Rex nunca cria task automática no ClickUp para recomendações classificadas como 'ação financeira' (ex: cancelar contrato, cortar budget de campanha, demitir fornecedor, alterar pricing) sem aprovação explícita do founder. Essas recomendações chegam como rascunho com flag APPROVAL_REQUIRED — founder aprova, rejeita ou modifica antes de qualquer task ser criada.
- [ ] **HITL** — ALERTA DE DADOS COMPROMETIDOS (L2→L3): Se Véra detectar que >30% dos KPIs de um OKR crítico vieram com data_quality_flag=FAILED (falha de integração, dado zerado, timeout), Atlas pausa o ciclo e envia alerta imediato: 'Pulse desta semana comprometido — [N] KPIs sem dados confiáveis de [sistema X]. Envio relatório parcial ou aguardo resolução?' Founder decide antes do relatório ser publicado.
- [ ] **HITL** — CLONE SIGMA PUBLICAÇÃO EXTERNA (L1→L3): Sigma pode gerar e entregar o Pulse no Slack e Notion de uso interno do founder sem aprovação. Se o founder solicitar versão do Pulse para compartilhar com time, board ou investidores — Sigma gera o draft mas entrega APENAS ao founder para revisão antes de qualquer distribuição externa.
- [ ] **HITL** — RECALIBRAÇÃO DE TARGET DE OKR (L2): Quando Kalinda detecta que um OKR está >120% da trajetória esperada por 2 semanas consecutivas (super-performance) ou que a tendência matemática torna o target inalcançável mesmo com ação corretiva — Atlas sinaliza ao founder para deliberar sobre recalibração de target. Nunca recalibra automaticamente. Founder decide em reunião de check-in mensal.
- [ ] **HITL** — ONBOARDING DE NOVO KPI/SISTEMA (L1): Ao adicionar nova fonte de dados ao catálogo, o primeiro ciclo de coleta opera em modo 'dry-run' — Pulsar coleta e Kalinda calcula desvios, mas Véra bloqueia entrega de diagnóstico e recomendação até que o founder confirme que os dados coletados fazem sentido. Isso evita que erro de mapeamento de campo gere falso alarme na primeira semana.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
