---
task: integrateEmail()
agent: ce-integrator
description: "Integração SMTP/SendGrid para confirmação de lead e sequência básica"
elicit: true
responsavel: "Link"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: emailConfig
    tipo: object
    obrigatorio: true
    descricao: "Configuração SMTP ou SendGrid API key"

Saida:
  - nome: emailIntegration
    tipo: file
    obrigatorio: true
    descricao: "Integração email para confirmação de lead e sequência básica"

Checklist:
  pre-conditions:
    - "[ ] Credenciais de email disponíveis"
  post-conditions:
    - "[ ] Email de confirmação enviando"
    - "[ ] Template de boas-vindas configurado"
---

# Task: integrateEmail()

## Objetivo
Configurar envio de email transacional via SMTP ou SendGrid para confirmação imediata de lead capturado e disparo da sequência básica de nurture por email. Email é o canal de nurture mais universal e confiável para qualquer produto.

## Inputs Necessários
- `scope.md` (flag `email_nurture` ativa)
- Provider de email escolhido (SendGrid, AWS SES, Postmark, SMTP próprio)
- API Key do provider ou credenciais SMTP
- Email remetente configurado e verificado (SPF/DKIM)
- `ce-email-strategist` output: sequência de emails escrita (`email-series.md`)
- Domínio para links de unsubscribe (LGPD)

## Processo
1. **Elicitação de configuração** — Coletar:
   - Provider preferido (SendGrid recomendado por simplicidade + analytics)
   - Email de remetente (deve ser verificado no provider)
   - Nome do remetente ("[Nome do produto]" ou "Nome da pessoa")
   - Email de reply-to (para respostas dos leads)
   - SendGrid API Key (ou credenciais SMTP)

2. **Instalação e configuração:**
   ```bash
   pip install sendgrid  # ou: pip install aiosmtplib
   ```
   ```env
   # .env
   EMAIL_PROVIDER=sendgrid  # ou: smtp
   SENDGRID_API_KEY=SG.xxxxx
   EMAIL_FROM=hola@seuproduto.com.br
   EMAIL_FROM_NAME=Nome do Produto
   EMAIL_REPLY_TO=suporte@seuproduto.com.br
   # Se SMTP:
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=email@gmail.com
   SMTP_PASS=app-password
   ```

3. **Serviço de email** — `src/services/email_service.py`:
   ```python
   from sendgrid import SendGridAPIClient
   from sendgrid.helpers.mail import Mail, To, From

   async def send_email(
       to_email: str,
       to_name: str,
       subject: str,
       html_content: str,
       text_content: str | None = None,
       template_id: str | None = None,
       template_data: dict | None = None,
   ) -> bool:
       try:
           message = Mail(
               from_email=From(settings.EMAIL_FROM, settings.EMAIL_FROM_NAME),
               to_emails=To(to_email, to_name),
               subject=subject,
               html_content=html_content,
           )
           if template_id:
               message.template_id = template_id
               message.dynamic_template_data = template_data

           sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
           response = sg.send(message)
           return response.status_code in [200, 201, 202]
       except Exception as e:
           logger.error(f"Erro ao enviar email para {to_email}: {e}")
           return False
   ```

4. **Email de confirmação imediata** — Disparado logo após captura do lead:
   ```python
   async def send_lead_confirmation(lead: Lead):
       first_name = lead.name.split()[0]
       html = f"""
       <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
         <h1>Olá, {first_name}!</h1>
         <p>Recebemos seu contato. 🎉</p>
         <p><strong>O que acontece agora:</strong></p>
         <ol>
           <li>[Próximo passo 1]</li>
           <li>[Próximo passo 2]</li>
         </ol>
         <a href="[URL de conversão]" style="background:#[cor-primária];color:white;padding:12px 24px;
            text-decoration:none;border-radius:6px;display:inline-block;margin:16px 0;">
           [CTA do próximo passo]
         </a>
         <p style="color:#6b7280;font-size:12px;margin-top:32px;">
           Você está recebendo este email porque preencheu nosso formulário em [domínio].
           <a href="[unsubscribe-url]">Cancelar inscrição</a>
         </p>
       </div>
       """
       await send_email(
           to_email=lead.email,
           to_name=lead.name,
           subject=f"✅ Recebemos seu contato, {first_name}!",
           html_content=html,
       )
   ```

5. **Modelo de email agendado** — Para sequência de nurture:
   ```python
   class ScheduledEmail(Base):
       __tablename__ = "scheduled_emails"
       id = Column(UUID, primary_key=True, default=uuid.uuid4)
       lead_id = Column(UUID, ForeignKey("leads.id"))
       sequence_step = Column(Integer)
       subject = Column(String(200))
       html_content = Column(Text)
       scheduled_at = Column(DateTime)
       sent_at = Column(DateTime, nullable=True)
       status = Column(String(20), default="pending")
       open_count = Column(Integer, default=0)
       click_count = Column(Integer, default=0)
   ```

6. **Agendamento da sequência:**
   ```python
   async def schedule_email_sequence(lead: Lead, sequence: list[dict]):
       """Agendar série de emails de nurture baseada em sequence do ce-email-strategist"""
       for step in sequence:
           scheduled = ScheduledEmail(
               lead_id=lead.id,
               sequence_step=step["step"],
               subject=step["subject"].replace("[NOME]", lead.name.split()[0]),
               html_content=render_email_template(step["template"], lead),
               scheduled_at=datetime.utcnow() + timedelta(hours=step["delay_hours"]),
           )
           db.add(scheduled)
   ```

7. **Unsubscribe handler** — Obrigatório LGPD:
   ```python
   @router.get("/unsubscribe/{token}")
   async def unsubscribe(token: str, db: AsyncSession = Depends(get_db)):
       lead_id = verify_unsubscribe_token(token)
       lead = await db.get(Lead, lead_id)
       if lead:
           lead.status = "unsubscribed"
           # Cancelar emails pendentes
           await db.execute(
               update(ScheduledEmail)
               .where(ScheduledEmail.lead_id == lead.id, ScheduledEmail.status == "pending")
               .values(status="cancelled")
           )
           await db.commit()
       return HTMLResponse("<h1>Você foi removido da nossa lista. ✅</h1>")
   ```

## Veto Conditions
- Email sem link de unsubscribe → obrigatório por LGPD e política do SendGrid
- Sem domínio verificado (SPF/DKIM) → configurar antes de enviar (risco de spam)
- HTML de email sem versão texto puro → adicionar (melhora entregabilidade)
- Sem tratamento de bounce (email inválido) → implementar webhook de bounce

## Output Esperado
- `src/services/email_service.py` com funções de envio
- `src/models/scheduled_email.py` com modelo de agendamento
- Email de confirmação implementado e testado
- Sequência de nurture agendável
- Unsubscribe handler implementado

## Completion Criteria
- [ ] Provider configurado com API Key e remetente verificado
- [ ] SPF/DKIM configurado no domínio do remetente
- [ ] Email de confirmação disparando após conversão de lead
- [ ] Modelo de email agendado criado
- [ ] Agendamento de sequência de nurture implementado
- [ ] Link de unsubscribe em todos os emails (token seguro)
- [ ] Unsubscribe handler cancelando emails pendentes
- [ ] Versão texto puro incluída em todos os emails
- [ ] Teste de envio bem-sucedido verificado no inbox (não spam)
