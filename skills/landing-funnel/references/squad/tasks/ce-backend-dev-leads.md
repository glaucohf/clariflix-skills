---
task: createLeadEndpoints()
agent: ce-backend-dev
description: "Endpoints de captura de leads com validação, anti-spam, rate limiting"
elicit: false
responsavel: "Vault"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: backendProject
    tipo: file
    obrigatorio: true
    descricao: "Projeto backend configurado"

Saida:
  - nome: leadEndpoints
    tipo: file
    obrigatorio: true
    descricao: "Endpoints de captura de leads com validação, anti-spam e rate limiting"

Checklist:
  pre-conditions:
    - "[ ] Backend configurado"
  post-conditions:
    - "[ ] POST /leads funcional"
    - "[ ] Validação de dados ativa"
    - "[ ] Rate limiting configurado"
---

# Task: createLeadEndpoints()

## Objetivo
Implementar os endpoints de captura e gestão de leads com validação robusta de dados, proteção anti-spam multicamada, rate limiting e armazenamento seguro. A qualidade do lead capturado impacta diretamente a eficiência do time de vendas.

## Inputs Necessários
- Backend setup completo (`setupBackendProject()` concluído)
- `scope.md` (campos do formulário de lead definidos)
- `requirements.md` (campos obrigatórios, integrações de CRM/email)
- `funnel-map.md` (contexto do funil — o que acontece após captura do lead)

## Processo
1. **Modelo de Lead** — `src/models/lead.py`:
   ```python
   from sqlalchemy import Column, String, DateTime, Boolean, Text, Enum
   from sqlalchemy.dialects.postgresql import UUID
   import uuid
   from datetime import datetime

   class Lead(Base):
       __tablename__ = "leads"

       id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
       # Campos base (sempre presentes)
       email = Column(String(255), nullable=False, index=True)
       name = Column(String(255), nullable=False)
       # Campos condicionais (baseados no scope)
       phone = Column(String(20), nullable=True)
       company = Column(String(255), nullable=True)
       # Metadata de rastreamento
       source = Column(String(100), nullable=True)   # UTM source
       medium = Column(String(100), nullable=True)   # UTM medium
       campaign = Column(String(100), nullable=True) # UTM campaign
       landing_page = Column(String(500), nullable=True)
       user_agent = Column(String(500), nullable=True)
       ip_address = Column(String(45), nullable=True)  # IPv6 max 45 chars
       # Status
       status = Column(Enum("new", "contacted", "qualified", "converted", name="lead_status"), default="new")
       email_verified = Column(Boolean, default=False)
       spam_score = Column(Integer, default=0)
       # Timestamps
       created_at = Column(DateTime, default=datetime.utcnow)
       updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
   ```

2. **Schemas Pydantic** — `src/schemas/lead.py`:
   ```python
   from pydantic import BaseModel, EmailStr, field_validator
   import re

   class LeadCreate(BaseModel):
       email: EmailStr
       name: str
       phone: str | None = None
       company: str | None = None
       # Honeypot anti-spam (campo oculto que bots preenchem)
       website: str | None = None  # Se preenchido = spam
       # UTM params
       utm_source: str | None = None
       utm_medium: str | None = None
       utm_campaign: str | None = None

       @field_validator('name')
       def name_valid(cls, v):
           if len(v.strip()) < 2:
               raise ValueError('Nome deve ter pelo menos 2 caracteres')
           if re.search(r'[<>{}]', v):
               raise ValueError('Nome contém caracteres inválidos')
           return v.strip()

       @field_validator('phone')
       def phone_valid(cls, v):
           if v:
               digits = re.sub(r'\D', '', v)
               if len(digits) < 10 or len(digits) > 11:
                   raise ValueError('Telefone inválido')
           return v

   class LeadResponse(BaseModel):
       id: str
       message: str
       class Config:
           from_attributes = True
   ```

3. **Serviço de leads com anti-spam** — `src/services/lead_service.py`:
   ```python
   async def calculate_spam_score(lead_data: LeadCreate, request: Request) -> int:
       score = 0
       # Honeypot preenchido
       if lead_data.website:
           score += 100  # Spam definitivo
       # Email de domínio descartável
       disposable_domains = ['mailinator.com', 'guerrillamail.com', 'temp-mail.org']
       domain = lead_data.email.split('@')[1]
       if domain in disposable_domains:
           score += 50
       # Velocidade de preenchimento (via JavaScript — campo hidden com timestamp)
       # User-agent de bot conhecido
       user_agent = request.headers.get('user-agent', '').lower()
       if any(bot in user_agent for bot in ['bot', 'crawler', 'spider', 'curl', 'wget']):
           score += 80
       return score

   async def create_lead(db: AsyncSession, lead_data: LeadCreate, request: Request):
       spam_score = await calculate_spam_score(lead_data, request)
       if spam_score >= 100:
           # Fingir sucesso mas não salvar
           return {"id": "fake-id", "message": "Lead registrado com sucesso!"}

       lead = Lead(
           email=lead_data.email,
           name=lead_data.name,
           phone=lead_data.phone,
           ip_address=request.client.host,
           user_agent=request.headers.get('user-agent'),
           source=lead_data.utm_source,
           spam_score=spam_score,
       )
       db.add(lead)
       await db.commit()
       return lead
   ```

4. **Endpoints** — `src/api/routes/leads.py`:
   ```python
   from fastapi import APIRouter, Depends, Request, HTTPException
   from slowapi import Limiter
   from slowapi.util import get_remote_address

   router = APIRouter(prefix="/leads", tags=["leads"])
   limiter = Limiter(key_func=get_remote_address)

   @router.post("/", response_model=LeadResponse)
   @limiter.limit("5/minute")  # Max 5 leads por IP por minuto
   async def create_lead(
       request: Request,
       lead_data: LeadCreate,
       db: AsyncSession = Depends(get_db)
   ):
       # Verificar duplicata (mesmo email nas últimas 24h)
       existing = await db.execute(
           select(Lead).where(
               Lead.email == lead_data.email,
               Lead.created_at >= datetime.utcnow() - timedelta(hours=24)
           )
       )
       if existing.scalar_one_or_none():
           return LeadResponse(id="dup", message="Lead já registrado!")

       lead = await lead_service.create_lead(db, lead_data, request)

       # Background tasks (não bloquear resposta)
       background_tasks.add_task(send_confirmation_email, lead.email)
       background_tasks.add_task(sync_to_crm, lead)

       return LeadResponse(id=str(lead.id), message="Obrigado! Entraremos em contato em breve.")

   @router.get("/count")
   async def get_lead_count(db: AsyncSession = Depends(get_db)):
       """Endpoint público para exibir número de leads na LP (prova social)"""
       count = await db.scalar(select(func.count(Lead.id)).where(Lead.spam_score < 50))
       return {"count": count}
   ```

5. **Migration** — Criar e aplicar:
   ```bash
   alembic revision --autogenerate -m "create leads table"
   alembic upgrade head
   ```

6. **Testes** — `tests/test_leads.py`:
   - Teste de criação de lead válido
   - Teste de rejeição de email inválido
   - Teste de honeypot (campo website preenchido)
   - Teste de rate limiting (6ª requisição deve falhar)
   - Teste de duplicata (mesmo email em 24h)

## Veto Conditions
- Endpoint sem rate limiting → adicionar antes de expor
- IP do usuário não salvo (necessário para LGPD e debug) → adicionar
- Honeypot não implementado → adicionar campo `website` hidden no frontend e verificar no backend
- Sem tratamento de duplicatas → implementar verificação

## Output Esperado
- `src/models/lead.py` com modelo completo
- `src/schemas/lead.py` com validação Pydantic
- `src/services/lead_service.py` com lógica de anti-spam
- `src/api/routes/leads.py` com endpoints documentados
- Migration aplicada
- Testes passando

## Completion Criteria
- [ ] Modelo Lead com todos os campos (inclui UTM params e metadata)
- [ ] Validação Pydantic para email, nome, telefone
- [ ] Honeypot implementado (campo website)
- [ ] Rate limiting: máximo 5 leads/minuto por IP
- [ ] Verificação de duplicata (24h)
- [ ] Spam score calculado antes de salvar
- [ ] Background tasks para email e CRM sync
- [ ] Migration criada e aplicada
- [ ] Testes cobrindo os cenários principais
- [ ] Endpoint documentado no Swagger (`/docs`)
