# Checklist do critic Argos — Risk & Scenario Sentinel

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Argos — O Verificador de Inteligência — Argos é o agente critic/verifier do Sentinel. Executa verificação adversarial em quatro camadas antes que qualquer output chegue ao founder: (1) SOURCE VERIFICATION — cada claim dos workers (Lexis, Gaia, Chronos) deve ter link para fonte primária verificável (Diário Oficial, texto de lei, publicação de agência, paper econômico, release oficial). Claims sem fonte primária são marcados como 'unverified' e não podem aparecer no Risk Brief como fatos — apenas como hipóteses a verificar. (2) HALLUCINATION DETECTION — Argos verifica se as normas, eventos ou dados citados existem de fato, se as datas e números são precisos, e se o contexto não foi distorcido na sumarização. Qualquer hallucination confirmada bloqueia o output do worker correspondente e dispara retrabalho. (3) RELEVANCE FILTER — verifica se os riscos identificados são de fato materiais para o modelo de negócio específico do cliente ou se são ruído de mercado que vai poluir o Brief do founder. Remove falsos positivos. (4) BIAS CHECK — identifica se os workers estão gerando viés de confirmação (ignorando riscos que contradizem as crenças do founder, ou exagerando riscos que confirmam seus medos). O output de Argos é um Verification Report que acompanha cada Brief: claim-by-claim, com status (Verified/Unverified/Hallucination/Corrected), fonte primária e confiança. Apenas Briefs com taxa de verificação >= 85% dos claims materiais passam para síntese do Nexus.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Verificador de Inteligência
- [ ] **C02** — Argos é o agente critic/verifier do Sentinel
- [ ] **C03** — Executa verificação adversarial em quatro camadas antes que qualquer output chegue ao founder: (1) SOURCE VERIFICATION
- [ ] **C04** — cada claim dos workers (Lexis, Gaia, Chronos) deve ter link para fonte primária verificável (Diário Oficial, texto de lei, publicação de agência, paper econômico, release oficial)
- [ ] **C05** — Claims sem fonte primária são marcados como 'unverified' e não podem aparecer no Risk Brief como fatos
- [ ] **C06** — apenas como hipóteses a verificar
- [ ] **C07** — (2) HALLUCINATION DETECTION
- [ ] **C08** — Argos verifica se as normas, eventos ou dados citados existem de fato, se as datas e números são precisos, e se o contexto não foi distorcido na sumarização
- [ ] **C09** — Qualquer hallucination confirmada bloqueia o output do worker correspondente e dispara retrabalho
- [ ] **C10** — (3) RELEVANCE FILTER
- [ ] **C11** — verifica se os riscos identificados são de fato materiais para o modelo de negócio específico do cliente ou se são ruído de mercado que vai poluir o Brief do founder
- [ ] **C12** — Remove falsos positivos
- [ ] **C13** — (4) BIAS CHECK
- [ ] **C14** — identifica se os workers estão gerando viés de confirmação (ignorando riscos que contradizem as crenças do founder, ou exagerando riscos que confirmam seus medos)
- [ ] **C15** — O output de Argos é um Verification Report que acompanha cada Brief: claim-by-claim, com status (Verified/Unverified/Hallucination/Corrected), fonte primária e confiança
- [ ] **C16** — Apenas Briefs com taxa de verificação >= 85% dos claims materiais passam para síntese do Nexus

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — INTAKE GATE — RISCO CRÍTICO (L3): Antes de disparar workers para investigação profunda, Nexus apresenta o Mapa de Exposição inicial ao founder quando o risco é classificado como Crítico (impacto estimado > R$200k ou impacto em licença/operação). O founder valida o escopo da investigação, confirma as agências e mercados a investigar, e aprova o nível de profundidade (scan rápido vs. deep dive). Para riscos Médios e Baixos, Nexus opera de forma autônoma sem gate obrigatório.
- [ ] **HITL** — RISCO EM MATERIALIZAÇÃO ATIVA — ALERTA CRÍTICO (L3): Quando Vela classifica um alerta como Crítico (risco está se materializando dentro da janela de resposta), o squad pausa toda recomendação de ação com impacto financeiro ou operacional e escalona para o founder com urgência máxima. O founder recebe: (a) o Evidence Report do Argos com fontes primárias que confirmam a materialização, (b) os cenários ativos de Chronos com janelas de resposta restantes, (c) as 3 ações prioritárias de Cipher. O founder deve responder com decisão explícita antes de qualquer ação ser executada.
- [ ] **HITL** — PREMISSA DE CENÁRIO INVERSAMENTE VALIDADA (L2): Quando Argos identifica que uma premissa central de um cenário ativo no Risk Register foi invalidada por nova evidência (ex: a norma que estava em consulta pública foi arquivada, alterando radicalmente o cenário regulatório), o squad notifica o founder com o impacto na matrix de cenários antes de atualizar o Risk Register. O founder confirma a revisão ou solicita novo ciclo de análise.
- [ ] **HITL** — BOARD/INVESTOR RISK UPDATE E COMUNICAÇÕES EXTERNAS (L3): Cipher nunca envia qualquer documento para audiência externa (board, conselheiros, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento produzido para audiência externa vai primeiro para Notion como draft com notificação Slack ao founder. Apenas após founder aprovar explicitamente (clique no botão 'Aprovar para envio' ou mensagem de aprovação no Slack) o envio é autorizado. Este gate é inviolável.
- [ ] **HITL** — CONFIGURAÇÃO DO ORÁCULO E CORPUS DO FOUNDER (L2): A configuração inicial do corpus do Oráculo (quais documentos, transcrições e decisões do founder são ingeridas) requer aprovação explícita item a item pelo founder. O founder define o que entra no corpus (controle de privacidade sobre decisões sensíveis) e o que fica fora. Atualizações mensais automáticas do corpus precisam de revisão semestral do founder para remoção de decisões desatualizadas.
- [ ] **HITL** — AJUSTE DE THRESHOLDS DE ALERTA (L2): Os thresholds de early-warning de Vela (o que configura Informativo vs. Atenção vs. Crítico para cada indicador) são configurados no onboarding e revisados trimestralmente com o founder. O founder pode ajustar thresholds via '/risk-config [indicador] [threshold]' mas qualquer ajuste que reduza a sensibilidade (aumenta threshold) requer justificativa explícita para evitar que o founder 'desligue' alertas por conveniência e depois seja pego de surpresa.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
