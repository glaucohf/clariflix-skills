---
task: setupBackendProject()
agent: ce-backend-dev
description: "Setup FastAPI, SQLAlchemy, Alembic, autenticação JWT"
elicit: false
responsavel: "Vault"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: projectScope
    tipo: file
    obrigatorio: true
    descricao: "Escopo com flag backend ativa"

Saida:
  - nome: backendProject
    tipo: file
    obrigatorio: true
    descricao: "Projeto FastAPI configurado com SQLAlchemy, Alembic e JWT auth"

Checklist:
  pre-conditions:
    - "[ ] Flag backend ativa no escopo"
  post-conditions:
    - "[ ] FastAPI instalado e configurado"
    - "[ ] Banco de dados conectado"
    - "[ ] JWT auth implementado"
---

# Task: setupBackendProject()

## Objetivo
Inicializar o projeto backend com FastAPI, configurar ORM (SQLAlchemy), migrations (Alembic), autenticação JWT e estrutura de projeto escalável. O backend deve estar production-ready com segurança, performance e manutenibilidade desde o setup inicial.

## Inputs Necessários
- `scope.md` (flag `backend` ativa, integrações necessárias)
- `product-brief.md` (contexto do produto)
- Python 3.11+ e pip/poetry instalados
- Banco de dados definido (PostgreSQL recomendado para produção)

## Processo
1. **Inicialização do projeto com Poetry:**
   ```bash
   poetry new [nome-projeto]-api
   cd [nome-projeto]-api
   poetry add fastapi uvicorn[standard] sqlalchemy alembic pydantic[email] \
     python-jose[cryptography] passlib[bcrypt] python-multipart \
     asyncpg databases psycopg2-binary python-dotenv httpx
   poetry add --dev pytest pytest-asyncio httpx black ruff mypy
   ```

2. **Estrutura de pastas:**
   ```
   src/
   ├── api/
   │   ├── __init__.py
   │   ├── deps.py           # Dependências compartilhadas (db, auth)
   │   └── routes/
   │       ├── leads.py      # Endpoints de leads
   │       ├── events.py     # Tracking de eventos
   │       └── admin.py      # Painel admin
   ├── core/
   │   ├── config.py         # Settings via pydantic-settings
   │   ├── security.py       # JWT, hashing
   │   └── database.py       # Engine, session, base
   ├── models/
   │   ├── lead.py           # SQLAlchemy models
   │   └── event.py
   ├── schemas/
   │   ├── lead.py           # Pydantic schemas (input/output)
   │   └── event.py
   ├── services/
   │   ├── lead_service.py   # Lógica de negócio
   │   └── email_service.py  # Integração de email
   ├── middleware/
   │   ├── cors.py
   │   └── rate_limit.py
   └── main.py               # App FastAPI entry point
   alembic/
   ├── env.py
   └── versions/             # Migration files
   tests/
   ├── conftest.py
   ├── test_leads.py
   └── test_auth.py
   .env.example
   .env
   alembic.ini
   pyproject.toml
   ```

3. **Configuração central** — `src/core/config.py`:
   ```python
   from pydantic_settings import BaseSettings

   class Settings(BaseSettings):
       # Database
       DATABASE_URL: str
       # JWT
       SECRET_KEY: str
       ALGORITHM: str = "HS256"
       ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
       # Admin
       ADMIN_EMAIL: str
       ADMIN_PASSWORD_HASH: str
       # CORS
       ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]
       # Rate limiting
       RATE_LIMIT_PER_MINUTE: int = 10

       class Config:
           env_file = ".env"

   settings = Settings()
   ```

4. **Database setup** — `src/core/database.py`:
   ```python
   from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
   from sqlalchemy.orm import sessionmaker, declarative_base

   engine = create_async_engine(settings.DATABASE_URL, echo=False)
   AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
   Base = declarative_base()

   async def get_db():
       async with AsyncSessionLocal() as session:
           yield session
   ```

5. **Autenticação JWT** — `src/core/security.py`:
   ```python
   from jose import JWTError, jwt
   from passlib.context import CryptContext
   from datetime import datetime, timedelta

   pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

   def create_access_token(data: dict) -> str:
       expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
       return jwt.encode({**data, "exp": expire}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

   def verify_token(token: str) -> dict:
       try:
           return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
       except JWTError:
           raise HTTPException(status_code=401, detail="Token inválido")
   ```

6. **App principal** — `src/main.py`:
   ```python
   from fastapi import FastAPI
   from fastapi.middleware.cors import CORSMiddleware
   from slowapi import Limiter, _rate_limit_exceeded_handler
   from slowapi.util import get_remote_address

   app = FastAPI(title="[Produto] API", version="1.0.0")

   # CORS
   app.add_middleware(CORSMiddleware,
     allow_origins=settings.ALLOWED_ORIGINS,
     allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

   # Rate limiting
   limiter = Limiter(key_func=get_remote_address)
   app.state.limiter = limiter

   # Routes
   app.include_router(leads_router, prefix="/api/v1")
   app.include_router(events_router, prefix="/api/v1")
   app.include_router(admin_router, prefix="/api/v1/admin")
   ```

7. **Alembic setup:**
   ```bash
   alembic init alembic
   # Configurar env.py para usar DATABASE_URL do .env
   alembic revision --autogenerate -m "initial schema"
   alembic upgrade head
   ```

8. **Arquivo .env.example:**
   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
   SECRET_KEY=your-super-secret-key-min-32-chars
   ADMIN_EMAIL=admin@exemplo.com
   ADMIN_PASSWORD_HASH=bcrypt-hash-here
   ALLOWED_ORIGINS=["https://seu-dominio.com.br"]
   ```

## Veto Conditions
- `SECRET_KEY` com menos de 32 caracteres → usar `openssl rand -hex 32`
- Database URL com credenciais hardcoded no código → mover para .env
- CORS com `allow_origins=["*"]` em produção → restringir para domínio da LP
- Sem rate limiting implementado → adicionar antes de expor à internet

## Output Esperado
Backend FastAPI rodando com:
- `uvicorn src.main:app --reload` sem erros
- Documentação automática em `/docs` (Swagger)
- Migrations aplicadas ao banco
- Autenticação JWT funcional
- Rate limiting ativo

## Completion Criteria
- [ ] Estrutura de pastas criada conforme especificação
- [ ] Dependências instaladas sem conflitos
- [ ] Settings via pydantic-settings com .env
- [ ] Database async com SQLAlchemy configurado
- [ ] JWT auth implementado (create + verify token)
- [ ] CORS configurado para domínio da LP
- [ ] Rate limiting configurado
- [ ] Alembic inicializado com migration inicial
- [ ] `uvicorn src.main:app` rodando sem erros
- [ ] `/docs` acessível com documentação Swagger
