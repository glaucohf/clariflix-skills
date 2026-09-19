---
task: optimizeDeliverability()
agent: ce-email-strategist
description: "Otimizar entregabilidade: SPF/DKIM/DMARC verificação, texto:imagem ratio, subject A/B, horário de envio"
elicit: false
responsavel: "Thread"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: automationSetup
    tipo: file
    obrigatorio: true
    descricao: "Automação configurada na plataforma"

Saida:
  - nome: deliverabilityReport
    tipo: file
    obrigatorio: true
    descricao: "Relatório de entregabilidade: SPF/DKIM/DMARC, ratio texto:imagem e horário de envio otimizado"

Checklist:
  pre-conditions:
    - "[ ] Automação configurada"
  post-conditions:
    - "[ ] SPF/DKIM/DMARC verificados"
    - "[ ] Taxa de spam < 0.1%"
    - "[ ] Horário de envio otimizado por fuso"
---

# Task: optimizeDeliverability()

## Objetivo
Garantir que os emails da sequência de nurture chegam na caixa de entrada — não no spam. Um email perfeito que vai para spam tem taxa de conversão zero. Entregabilidade é o fundamento técnico e estratégico que determina se todo o trabalho de copy e automação terá impacto.

## Inputs Necessários
- `email-series.md` (emails escritos)
- `automation-config.md` (plataforma configurada)
- Domínio do remetente e acesso ao DNS
- Dados históricos de abertura (se existirem)

## Processo
1. **Verificação e configuração de autenticação de email:**

   **SPF (Sender Policy Framework):**
   Verificar que registro SPF existe e inclui o servidor da plataforma de email:
   ```
   # Verificar via DNS lookup:
   dig TXT seudomain.com.br | grep spf

   # Deve conter algo como:
   v=spf1 include:sendgrid.net include:servers.mcsv.net ~all

   # Se ausente, adicionar ao DNS:
   TXT @ "v=spf1 include:[plataforma.com] ~all"
   ```

   **DKIM (DomainKeys Identified Mail):**
   - Cada plataforma fornece registros DKIM para adicionar ao DNS
   - Verificar na configuração da plataforma (SendGrid, ActiveCampaign, etc.)
   - Adicionar os registros CNAME ou TXT fornecidos
   - Verificar: `dig TXT s1._domainkey.seudomain.com.br`
   - Aguardar propagação DNS (pode levar até 48h)

   **DMARC (Domain-based Message Authentication):**
   ```
   # Adicionar registro DMARC ao DNS:
   TXT _dmarc "v=DMARC1; p=none; rua=mailto:dmarc@seudomain.com.br; ruf=mailto:dmarc@seudomain.com.br; fo=1"

   # Começar com p=none (monitorar sem rejeitar)
   # Após 30 dias com dados limpos, mover para p=quarantine e depois p=reject
   ```

   **Verificação completa:**
   - Usar MXToolbox.com → Email Health Check
   - Usar mail-tester.com → Score deve ser ≥ 8/10

2. **Otimização da razão texto:imagem** — Para evitar spam filters:
   - Ratio ideal: 60% texto, 40% imagens (ou menos imagens)
   - Emails 100% imagem → spam filter quase certo
   - Imagens decorativas: opcional, nunca essencial para entender o email
   - Todas as imagens com alt text (muitos clients bloqueiam imagens por padrão)
   - Não usar GIFs grandes que aumentam o tamanho do email além de 100KB

3. **Auditoria de spam triggers** — Varrer o copy de cada email:

   **Palavras de spam a evitar no subject e preheader:**
   - Financeiro: "grátis", "dinheiro", "ganhe", "lucro", "renda extra"
   - Urgência falsa: "urgente", "aja agora", "não perca"
   - Médico/Milagre: "garantido", "100%", "resultado imediato"
   - Pontuação excessiva: "!!!", "???"
   - CAPS LOCK excessivo

   **Verificar com SpamAssassin score:**
   - Usar mail-tester.com → enviar email de teste → ver score
   - Score ≥ 8/10 → aprovado para envio
   - Score < 7/10 → identificar problemas e corrigir antes de ativar

4. **Otimização de horário de envio:**
   Pesquisa de benchmarks por nicho:

   | Tipo de público | Melhor dia | Melhor horário |
   |----------------|-----------|----------------|
   | Empreendedores/CEOs | Ter-Qui | 8h-10h |
   | Profissionais B2B | Ter-Qui | 10h-11h |
   | Público B2C geral | Ter, Qui | 19h-21h |
   | Donos de pequenos negócios | Qua | 8h-9h |
   | Estudantes/jovens | Sab | 10h-14h |

   Configurar o horário de envio de cada email na automação para o horário adequado ao fuso local.
   Se a plataforma suporta "Send Time Optimization" → ativar.

5. **Warm-up do domínio de envio** — Se é novo domínio ou novo provedor:
   - Semana 1: Máximo 50 emails/dia
   - Semana 2: Máximo 200 emails/dia
   - Semana 3: Máximo 500 emails/dia
   - Semana 4+: Volume normal
   Enviar primeiro para lista de subscribers mais engajados (abre frequentemente).

6. **Configuração de Email de Resposta:**
   - `reply-to` deve ser um email real que alguém monitora
   - Responder replies de leads MANUALMENTE aumenta reputação do domínio
   - Configurar auto-resposta para replies durante horário comercial

7. **Métricas de entregabilidade para monitorar:**
   - Open rate: ≥ 25% (bom), ≥ 40% (excelente)
   - Click rate: ≥ 2.5% (bom), ≥ 5% (excelente)
   - Bounce rate: < 2% (acima disso, limpar lista)
   - Spam complaint rate: < 0.1% (acima disso, problema grave)
   - Unsubscribe rate: < 0.5% por email

8. **A/B de subjects** — Configurar split de subject lines:
   - Plataformas como ActiveCampaign e Mailchimp suportam A/B de subject nativo
   - Testar variante A vs B por 4 horas → vencedor enviado para o restante
   - Testar uma variável por vez (curiosidade vs benefício, curto vs longo)
   - Registrar resultados de cada teste para biblioteca de subjects

## Veto Conditions
- SPF ou DKIM ausente → não ativar sequência até configurar (emails vão para spam)
- Score de spam < 7/10 → identificar e corrigir problema antes de ativar
- Open rate < 10% após 500 envios → problema grave de entregabilidade — investigar
- Taxa de bounce > 5% → limpar lista imediatamente (risco de blacklist)

## Output Esperado
- SPF, DKIM e DMARC verificados e funcionando (print de verificação MXToolbox)
- Score de spam mail-tester.com ≥ 8/10 para cada email
- Horários de envio otimizados configurados na automação
- A/B de subjects configurado
- Documento `deliverability-report.md` com status de cada verificação

## Completion Criteria
- [ ] SPF configurado e verificado via DNS lookup
- [ ] DKIM configurado e verificado via DNS lookup
- [ ] DMARC configurado (p=none para início)
- [ ] Score mail-tester.com ≥ 8/10 para Email 1 (Welcome)
- [ ] Spam triggers removidos de todos os subjects e preheaders
- [ ] Horários de envio configurados na automação
- [ ] A/B de subject configurado para email de Welcome e Oferta
- [ ] Métricas de monitoramento definidas
- [ ] Warm-up plan documentado (se domínio novo)
- [ ] Documento `deliverability-report.md` com evidências de verificação
