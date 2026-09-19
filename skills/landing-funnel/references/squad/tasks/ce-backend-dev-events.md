---
task: setupEventTracking()
agent: ce-backend-dev
description: "EXCLUSIVO: implementar server-side event tracking para GA4 Measurement Protocol e Meta Conversions API (dados mais precisos que client-side)"
elicit: false
responsavel: "Vault"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: analyticsConfig
    tipo: file
    obrigatorio: true
    descricao: "Configuração de GA4 e Meta Pixel do Lens"

Saida:
  - nome: serverSideTracking
    tipo: file
    obrigatorio: true
    descricao: "Server-side event tracking: GA4 Measurement Protocol + Meta Conversions API com deduplication"

Checklist:
  pre-conditions:
    - "[ ] GA4 Measurement ID disponível"
    - "[ ] Meta Pixel Access Token disponível"
  post-conditions:
    - "[ ] Eventos server-side enviando para GA4"
    - "[ ] Conversions API configurada"
    - "[ ] Deduplication implementada"
---

# Task: setupEventTracking()

## Objetivo
Implementar server-side event tracking via GA4 Measurement Protocol e Meta Conversions API. O tracking server-side captura eventos que o client-side perde (adblockers, iOS ITP, Safari) — garantindo dados muito mais precisos para otimização de campanhas. É o DIFERENCIAL técnico que permite ROAS real em vez de ROAS aproximado.

## Inputs Necessários
- Backend setup completo (`setupBackendProject()` concluído)
- Leads endpoint implementado (`createLeadEndpoints()` concluído)
- `scope.md` (analytics flag ativa, pixels configurados)
- GA4 Measurement ID e API Secret (obtidos no GA4)
- Meta Pixel ID e Access Token (obtidos no Meta Business Manager)
- Domínio da LP para event deduplication

## Processo
1. **Modelo de Evento** — `src/models/event.py`:
   ```python
   class ServerEvent(Base):
       __tablename__ = "server_events"

       id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
       event_name = Column(String(100), nullable=False, index=True)
       event_time = Column(DateTime, default=datetime.utcnow, index=True)
       # User identifiers (para deduplication)
       client_id = Column(String(100), nullable=True)    # GA4 client_id
       session_id = Column(String(100), nullable=True)   # GA4 session_id
       fbp = Column(String(100), nullable=True)          # Meta _fbp cookie
       fbc = Column(String(100), nullable=True)          # Meta _fbc param
       # Lead reference
       lead_id = Column(UUID(as_uuid=True), ForeignKey("leads.id"), nullable=True)
       email_hash = Column(String(64), nullable=True)    # SHA256 hash
       phone_hash = Column(String(64), nullable=True)
       # Event data
       event_data = Column(JSON, nullable=True)
       # Request metadata
       ip_address = Column(String(45), nullable=True)
       user_agent = Column(String(500), nullable=True)
       page_url = Column(String(1000), nullable=True)
       # Delivery status
       ga4_sent = Column(Boolean, default=False)
       meta_sent = Column(Boolean, default=False)
       ga4_response = Column(String(500), nullable=True)
       meta_response = Column(String(500), nullable=True)
   ```

2. **Serviço GA4 Measurement Protocol** — `src/services/ga4_service.py`:
   ```python
   import httpx
   import hashlib

   GA4_ENDPOINT = "https://www.google-analytics.com/mp/collect"

   async def send_ga4_event(
       event_name: str,
       client_id: str,
       session_id: str | None,
       event_params: dict,
       user_properties: dict | None = None
   ) -> dict:
       payload = {
           "client_id": client_id,
           "events": [{
               "name": event_name,
               "params": {
                   **event_params,
                   "session_id": session_id,
                   "engagement_time_msec": 1,
               }
           }]
       }
       if user_properties:
           payload["user_properties"] = user_properties

       async with httpx.AsyncClient() as client:
           response = await client.post(
               GA4_ENDPOINT,
               params={
                   "measurement_id": settings.GA4_MEASUREMENT_ID,
                   "api_secret": settings.GA4_API_SECRET,
               },
               json=payload,
               timeout=5.0
           )
           return {"status": response.status_code, "body": response.text}

   async def track_lead_conversion(lead: Lead, client_id: str, session_id: str):
       """Track conversão de lead para GA4 server-side"""
       await send_ga4_event(
           event_name="generate_lead",
           client_id=client_id,
           session_id=session_id,
           event_params={
               "currency": "BRL",
               "value": 0,  # Valor do lead (se conhecido)
               "lead_source": lead.source or "direct",
           },
           user_properties={
               "lead_id": {"value": str(lead.id)},
           }
       )
   ```

3. **Serviço Meta Conversions API** — `src/services/meta_service.py`:
   ```python
   META_CAPI_ENDPOINT = "https://graph.facebook.com/v18.0/{pixel_id}/events"

   def hash_pii(value: str) -> str:
       """Hash SHA256 de dados pessoais (obrigatório pela Meta)"""
       return hashlib.sha256(value.strip().lower().encode()).hexdigest()

   async def send_meta_event(
       event_name: str,
       event_data: dict,
       user_data: dict,
       event_id: str,  # Para deduplication com client-side
   ) -> dict:
       payload = {
           "data": [{
               "event_name": event_name,
               "event_time": int(datetime.utcnow().timestamp()),
               "event_id": event_id,  # Mesmo ID usado no pixel client-side
               "event_source_url": event_data.get("page_url"),
               "action_source": "website",
               "user_data": {
                   **user_data,
                   # PII sempre hasheado
                   "em": [hash_pii(user_data["email"])] if "email" in user_data else [],
                   "ph": [hash_pii(user_data["phone"])] if "phone" in user_data else [],
                   "client_ip_address": event_data.get("ip_address"),
                   "client_user_agent": event_data.get("user_agent"),
                   "fbp": event_data.get("fbp"),
                   "fbc": event_data.get("fbc"),
               },
               "custom_data": event_data.get("custom_data", {}),
           }],
           "test_event_code": settings.META_TEST_EVENT_CODE if settings.META_TEST_EVENT_CODE else None,
       }

       async with httpx.AsyncClient() as client:
           response = await client.post(
               META_CAPI_ENDPOINT.format(pixel_id=settings.META_PIXEL_ID),
               params={"access_token": settings.META_ACCESS_TOKEN},
               json=payload,
               timeout=5.0
           )
           return {"status": response.status_code, "body": response.json()}

   async def track_lead_conversion(lead: Lead, fbp: str, fbc: str, ip: str, ua: str, page_url: str, event_id: str):
       """Track Lead event para Meta CAPI (server-side)"""
       await send_meta_event(
           event_name="Lead",
           event_data={"ip_address": ip, "user_agent": ua, "page_url": page_url, "fbp": fbp, "fbc": fbc},
           user_data={"email": lead.email, "fn": lead.name.split()[0] if lead.name else ""},
           event_id=event_id,
       )
   ```

4. **Endpoint de eventos** — `src/api/routes/events.py`:
   ```python
   @router.post("/track")
   async def track_event(
       request: Request,
       event_data: EventCreate,
       background_tasks: BackgroundTasks,
       db: AsyncSession = Depends(get_db)
   ):
       """Endpoint para client-side enviar eventos para server-side processing"""
       event = ServerEvent(
           event_name=event_data.event_name,
           client_id=event_data.client_id,
           fbp=event_data.fbp,
           fbc=event_data.fbc,
           ip_address=request.client.host,
           user_agent=request.headers.get("user-agent"),
           page_url=event_data.page_url,
           event_data=event_data.custom_data,
       )
       db.add(event)
       await db.commit()

       # Envio assíncrono (não bloqueia resposta)
       background_tasks.add_task(process_server_event, event)

       return {"success": True, "event_id": str(event.id)}
   ```

5. **Eventos a rastrear:**
   - `page_view` — Visualização da página
   - `scroll_depth` — 25%, 50%, 75%, 90% de scroll
   - `cta_click` — Clique em qualquer CTA
   - `form_start` — Usuário começou a preencher o formulário
   - `form_submit` — Formulário enviado
   - `lead_generated` — Lead confirmado (após validação backend) — EVENTO MAIS IMPORTANTE
   - `video_play` / `video_complete` — Se VSL presente

6. **Deduplication** — Garantir que o mesmo evento não seja contado duas vezes:
   - Usar `event_id` único por evento (gerado no client, enviado ao server)
   - Meta CAPI: `event_id` deve ser idêntico ao enviado pelo Pixel client-side
   - GA4: `client_id` consistente entre client e server

## Veto Conditions
- PII (email, phone) enviado sem hash para Meta → bloquear — violação da política da Meta
- Sem deduplication implementado → eventos serão contados em dobro, inflando dados
- Timeout de chamadas externas sem try/except → background task não pode falhar silenciosamente

## Output Esperado
- `src/models/event.py` com modelo de evento
- `src/services/ga4_service.py` com integração GA4 Measurement Protocol
- `src/services/meta_service.py` com integração Meta CAPI (com hash PII)
- `src/api/routes/events.py` com endpoint `/track`
- Migration para tabela de eventos
- Configuração de deduplication documentada

## Completion Criteria
- [ ] Modelo ServerEvent criado com todos os campos de deduplication
- [ ] GA4 Measurement Protocol implementado com send_ga4_event()
- [ ] Meta Conversions API implementado com hash SHA256 de PII
- [ ] Endpoint `/api/v1/track` funcionando
- [ ] Deduplication via event_id implementado
- [ ] Background tasks para envio assíncrono (não bloqueia resposta)
- [ ] 6 eventos mapeados e implementados
- [ ] Migration criada e aplicada
- [ ] Testado com GA4 DebugView e Meta Test Events
