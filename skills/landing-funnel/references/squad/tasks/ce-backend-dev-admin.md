---
task: buildAdminPanel()
agent: ce-backend-dev
description: "Painel admin com listagem/exportação de leads, métricas básicas, autenticação segura"
elicit: false
responsavel: "Vault"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: leadEndpoints
    tipo: file
    obrigatorio: true
    descricao: "Endpoints de leads implementados"

Saida:
  - nome: adminPanel
    tipo: file
    obrigatorio: true
    descricao: "Painel admin com listagem, exportação CSV, métricas e autenticação segura"

Checklist:
  pre-conditions:
    - "[ ] Endpoints de leads funcionais"
  post-conditions:
    - "[ ] Login seguro implementado"
    - "[ ] Listagem de leads paginada"
    - "[ ] Exportação CSV funcional"
---

# Task: buildAdminPanel()

## Objetivo
Construir um painel administrativo funcional que permita ao cliente visualizar leads capturados, exportar dados, acompanhar métricas básicas de conversão e gerenciar o pipeline. A interface deve ser simples, segura e utilizável sem treinamento.

## Inputs Necessários
- Backend setup completo com leads implementados
- `scope.md` (se admin é via API REST ou interface web)
- `requirements.md` (necessidades de gestão do cliente)

## Processo
1. **Autenticação segura para admin** — `src/api/routes/admin.py`:
   ```python
   @router.post("/auth/login")
   @limiter.limit("5/minute")  # Proteção contra brute force
   async def admin_login(credentials: AdminLogin):
       if credentials.email != settings.ADMIN_EMAIL:
           raise HTTPException(status_code=401, detail="Credenciais inválidas")

       if not verify_password(credentials.password, settings.ADMIN_PASSWORD_HASH):
           # Timing-safe comparison via passlib
           raise HTTPException(status_code=401, detail="Credenciais inválidas")

       token = create_access_token({"sub": credentials.email, "role": "admin"})
       return {"access_token": token, "token_type": "bearer", "expires_in": 1800}

   def get_admin_user(token: str = Depends(oauth2_scheme)):
       payload = verify_token(token)
       if payload.get("role") != "admin":
           raise HTTPException(status_code=403, detail="Sem permissão")
       return payload
   ```

2. **Endpoints de gestão de leads:**
   ```python
   @router.get("/leads")
   async def list_leads(
       page: int = 1,
       per_page: int = 50,
       status: str | None = None,
       search: str | None = None,
       date_from: datetime | None = None,
       date_to: datetime | None = None,
       admin=Depends(get_admin_user),
       db: AsyncSession = Depends(get_db)
   ):
       """Listagem paginada de leads com filtros"""
       query = select(Lead).where(Lead.spam_score < 50)  # Excluir spam
       if status:
           query = query.where(Lead.status == status)
       if search:
           query = query.where(
               or_(Lead.email.ilike(f"%{search}%"), Lead.name.ilike(f"%{search}%"))
           )
       if date_from:
           query = query.where(Lead.created_at >= date_from)
       # Paginação
       total = await db.scalar(select(func.count()).select_from(query.subquery()))
       leads = await db.execute(query.offset((page-1)*per_page).limit(per_page).order_by(Lead.created_at.desc()))
       return {
           "leads": leads.scalars().all(),
           "total": total,
           "page": page,
           "pages": ceil(total / per_page)
       }

   @router.get("/leads/export")
   async def export_leads_csv(admin=Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
       """Exportar todos os leads como CSV"""
       leads = await db.execute(
           select(Lead).where(Lead.spam_score < 50).order_by(Lead.created_at.desc())
       )
       output = io.StringIO()
       writer = csv.DictWriter(output, fieldnames=["id","name","email","phone","company","source","status","created_at"])
       writer.writeheader()
       for lead in leads.scalars().all():
           writer.writerow({...})
       return Response(
           content=output.getvalue(),
           media_type="text/csv",
           headers={"Content-Disposition": f"attachment; filename=leads-{date.today()}.csv"}
       )

   @router.patch("/leads/{lead_id}/status")
   async def update_lead_status(
       lead_id: UUID,
       status_update: LeadStatusUpdate,
       admin=Depends(get_admin_user),
       db: AsyncSession = Depends(get_db)
   ):
       """Atualizar status de um lead"""
       lead = await db.get(Lead, lead_id)
       if not lead:
           raise HTTPException(status_code=404, detail="Lead não encontrado")
       lead.status = status_update.status
       await db.commit()
       return {"success": True}
   ```

3. **Dashboard de métricas** — `src/api/routes/admin.py`:
   ```python
   @router.get("/metrics")
   async def get_metrics(
       period: str = "7d",  # "1d", "7d", "30d", "90d"
       admin=Depends(get_admin_user),
       db: AsyncSession = Depends(get_db)
   ):
       """Métricas básicas de conversão"""
       days = {"1d": 1, "7d": 7, "30d": 30, "90d": 90}[period]
       since = datetime.utcnow() - timedelta(days=days)

       total_leads = await db.scalar(
           select(func.count(Lead.id)).where(Lead.created_at >= since, Lead.spam_score < 50)
       )
       leads_by_day = await db.execute(
           select(
               func.date(Lead.created_at).label("date"),
               func.count(Lead.id).label("count")
           ).where(Lead.created_at >= since, Lead.spam_score < 50)
           .group_by(func.date(Lead.created_at))
           .order_by(func.date(Lead.created_at))
       )
       leads_by_source = await db.execute(
           select(Lead.source, func.count(Lead.id))
           .where(Lead.created_at >= since, Lead.spam_score < 50)
           .group_by(Lead.source)
       )
       return {
           "total_leads": total_leads,
           "leads_by_day": [{"date": str(r.date), "count": r.count} for r in leads_by_day],
           "leads_by_source": dict(leads_by_source.all()),
           "period": period,
       }
   ```

4. **Interface web simples (opcional)** — Se cliente não tem frontend admin:
   - Usar FastAPI + Jinja2 templates para interface básica
   - Ou sugerir uso direto da documentação Swagger (`/docs`) com autenticação Bearer

5. **Segurança adicional:**
   - Rate limiting no login (5 tentativas/minuto por IP)
   - Tokens JWT com expiração curta (30 minutos)
   - Sem exposição de campos sensíveis na listagem (sem `ip_address` no output público)
   - Logs de acesso admin (quem acessou, quando, qual IP)

6. **Testes:**
   - Teste de login com credenciais corretas e incorretas
   - Teste de listagem com paginação
   - Teste de exportação CSV
   - Teste de acesso sem token (deve retornar 401)
   - Teste de brute force (6ª tentativa deve ser bloqueada)

## Veto Conditions
- Endpoint admin sem autenticação → adicionar obrigatoriamente
- Sem rate limiting no login → adicionar (prevenção de brute force)
- Exportação CSV expondo campo de IP ou user agent → remover campos sensíveis do export
- Token sem expiração → definir expiração máxima de 24h

## Output Esperado
- Endpoints admin documentados e funcionais
- Login seguro com JWT
- Listagem de leads com paginação e filtros
- Exportação CSV funcional
- Dashboard de métricas básicas
- Testes de segurança passando

## Completion Criteria
- [ ] Login admin com JWT e expiração configurada
- [ ] Rate limiting no endpoint de login (5/minuto)
- [ ] Listagem de leads com paginação, filtro e busca
- [ ] Exportação CSV com campos corretos (sem PII desnecessário)
- [ ] Atualização de status de lead implementada
- [ ] Dashboard de métricas (total, por dia, por fonte)
- [ ] Testes de autenticação (correto, incorreto, sem token)
- [ ] Teste de brute force protection
- [ ] Todos os endpoints documentados no Swagger
