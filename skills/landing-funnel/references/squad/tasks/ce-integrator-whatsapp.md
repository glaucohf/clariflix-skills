---
task: integrateWhatsApp()
agent: ce-integrator
description: "Integração com evolution-api para notificações e nurture via WhatsApp"
elicit: true
responsavel: "Link"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: evolutionApiConfig
    tipo: object
    obrigatorio: true
    descricao: "URL e token da evolution-api"

Saida:
  - nome: whatsappIntegration
    tipo: file
    obrigatorio: true
    descricao: "Integração WhatsApp via evolution-api para notificações de novos leads"

Checklist:
  pre-conditions:
    - "[ ] evolution-api configurada"
    - "[ ] Número WhatsApp Business disponível"
  post-conditions:
    - "[ ] Notificação de lead ativa"
    - "[ ] Mensagem de boas-vindas configurada"
---

# Task: integrateWhatsApp()

## Objetivo
Integrar a plataforma Evolution API para envio automatizado de mensagens WhatsApp no momento da conversão do lead e para sequências de nurture. WhatsApp tem taxa de abertura de 95% vs 20% do email — é o canal de maior alcance para o mercado brasileiro.

## Inputs Necessários
- `scope.md` (flag `whatsapp` ativa)
- URL e API Key da instância Evolution API do cliente
- Número WhatsApp Business configurado na instância
- `funnel-map.md` (fluxo de nurture via WhatsApp definido)
- Templates de mensagem aprovados (Evolution API exige aprovação prévia para template ou usa freeform dentro de 24h)

## Processo
1. **Elicitação de configuração** — Coletar com o cliente:
   - URL da instância Evolution API (ex: `https://evolution.seudominio.com.br`)
   - API Key de autenticação
   - Nome da instância WhatsApp conectada
   - Número de WhatsApp Business (com DDI: `5511999999999`)
   - Mensagem de boas-vindas imediata (enviada no momento do lead)
   - Sequência de nurture: quantas mensagens, conteúdo de cada uma, intervalo

2. **Configuração do serviço** — `src/services/whatsapp_service.py`:
   ```python
   import httpx

   EVOLUTION_BASE = settings.EVOLUTION_API_URL
   EVOLUTION_KEY = settings.EVOLUTION_API_KEY
   EVOLUTION_INSTANCE = settings.EVOLUTION_INSTANCE_NAME

   async def send_whatsapp_message(phone: str, message: str) -> dict:
       """Enviar mensagem de texto simples via Evolution API"""
       clean_phone = ''.join(filter(str.isdigit, phone))
       if not clean_phone.startswith('55'):
           clean_phone = '55' + clean_phone

       async with httpx.AsyncClient() as client:
           response = await client.post(
               f"{EVOLUTION_BASE}/message/sendText/{EVOLUTION_INSTANCE}",
               headers={"apikey": EVOLUTION_KEY, "Content-Type": "application/json"},
               json={
                   "number": clean_phone,
                   "text": message,
                   "delay": 1200,  # Delay humanizado (1.2s)
               },
               timeout=10.0
           )
           return {"status": response.status_code, "data": response.json()}

   async def send_whatsapp_with_image(phone: str, image_url: str, caption: str) -> dict:
       """Enviar imagem com legenda"""
       async with httpx.AsyncClient() as client:
           response = await client.post(
               f"{EVOLUTION_BASE}/message/sendMedia/{EVOLUTION_INSTANCE}",
               headers={"apikey": EVOLUTION_KEY},
               json={
                   "number": '55' + phone.replace('+55', '').replace(' ', '').replace('-', ''),
                   "mediatype": "image",
                   "media": image_url,
                   "caption": caption,
               },
               timeout=10.0
           )
           return response.json()
   ```

3. **Mensagem de boas-vindas imediata** — Disparada no momento da conversão:
   ```python
   async def send_welcome_message(lead: Lead):
       if not lead.phone:
           return  # WhatsApp requer telefone

       first_name = lead.name.split()[0]
       message = f"""Olá, {first_name}! 👋

Recebemos seu contato sobre [Produto].

✅ Suas informações foram registradas com sucesso.

Em breve nossa equipe entrará em contato para [próximo passo específico].

Enquanto isso, caso tenha alguma dúvida, é só responder aqui! 😊"""

       await send_whatsapp_message(lead.phone, message)
   ```

4. **Configuração de sequência de nurture** — Criar scheduler de mensagens:
   ```python
   # src/models/whatsapp_nurture.py
   class WhatsAppNurtureMessage(Base):
       __tablename__ = "whatsapp_nurture"
       id = Column(UUID, primary_key=True, default=uuid.uuid4)
       lead_id = Column(UUID, ForeignKey("leads.id"))
       sequence_step = Column(Integer)
       scheduled_at = Column(DateTime)
       sent_at = Column(DateTime, nullable=True)
       message = Column(Text)
       status = Column(String(20), default="pending")  # pending/sent/failed

   async def schedule_nurture_sequence(lead: Lead):
       """Agendar sequência de mensagens de nurture"""
       sequence = [
           {"delay_hours": 24, "message": "[Mensagem de nurture D+1 — educacional]"},
           {"delay_hours": 48, "message": "[Mensagem de nurture D+2 — prova social]"},
           {"delay_hours": 72, "message": "[Mensagem de nurture D+3 — oferta]"},
       ]
       for step_idx, step in enumerate(sequence):
           scheduled = WhatsAppNurtureMessage(
               lead_id=lead.id,
               sequence_step=step_idx + 1,
               scheduled_at=datetime.utcnow() + timedelta(hours=step["delay_hours"]),
               message=step["message"].replace("[NOME]", lead.name.split()[0]),
           )
           db.add(scheduled)
   ```

5. **Worker de envio de nurture** — Processo que verifica e envia mensagens agendadas:
   ```python
   # Executar via Celery beat, APScheduler ou cron job
   async def process_pending_nurture():
       pending = await db.execute(
           select(WhatsAppNurtureMessage)
           .where(WhatsAppNurtureMessage.status == "pending",
                  WhatsAppNurtureMessage.scheduled_at <= datetime.utcnow())
       )
       for message in pending.scalars().all():
           lead = await db.get(Lead, message.lead_id)
           if lead and lead.phone:
               result = await send_whatsapp_message(lead.phone, message.message)
               message.status = "sent"
               message.sent_at = datetime.utcnow()
   ```

6. **Webhook para respostas** — Receber e registrar respostas do lead:
   ```python
   @router.post("/webhooks/whatsapp")
   async def whatsapp_webhook(payload: dict, db: AsyncSession = Depends(get_db)):
       """Receber notificações da Evolution API (respostas do lead)"""
       if payload.get("event") == "messages.upsert":
           # Lead respondeu — atualizar status e notificar time de vendas
           pass
       return {"status": "ok"}
   ```

## Veto Conditions
- Telefone sem DDI (55 para Brasil) → normalizar antes de enviar
- Mensagem enviada sem delay humanizado → adicionar delay de 1-3 segundos (parece mais natural)
- Sem verificação de opt-out → implementar lista de bloqueio (LGPD)
- Worker de nurture sem retry para falhas → implementar retry com backoff

## Output Esperado
- `src/services/whatsapp_service.py` com funções de envio
- `src/models/whatsapp_nurture.py` com modelo de sequência
- Worker de processamento de fila configurado
- Webhook para respostas implementado
- Templates de mensagem de boas-vindas e sequência documentados

## Completion Criteria
- [ ] Conexão com Evolution API verificada (teste de envio bem-sucedido)
- [ ] Mensagem de boas-vindas disparando no momento da conversão de lead
- [ ] Normalização de telefone implementada (DDI 55, dígitos apenas)
- [ ] Sequência de nurture agendada com delays corretos
- [ ] Worker de processamento da fila implementado
- [ ] Webhook para respostas configurado
- [ ] Opt-out / lista de bloqueio implementado (LGPD)
- [ ] Retry com backoff para falhas de envio
