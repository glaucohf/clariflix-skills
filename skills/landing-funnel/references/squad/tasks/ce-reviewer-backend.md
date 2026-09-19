---
task: reviewBackendSecurity()
agent: ce-reviewer
description: "Revisar backend: SQL injection, XSS, rate limiting, auth security, LGPD compliance. Score: 0-100"
elicit: false
responsavel: "Audit"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: backendCode
    tipo: file
    obrigatorio: true
    descricao: "Código backend completo"

Saida:
  - nome: backendSecurityScore
    tipo: file
    obrigatorio: true
    descricao: "Score de segurança 0-100: SQL injection, XSS, rate limiting, auth e LGPD compliance"

Checklist:
  pre-conditions:
    - "[ ] Backend implementado"
  post-conditions:
    - "[ ] Score calculado"
    - "[ ] Vulnerabilidades críticas listadas"
    - "[ ] LGPD compliance verificado"
---

# Task: reviewBackendSecurity()

## Objetivo
Realizar um audit de segurança do backend da landing page, verificando proteção contra as vulnerabilidades mais comuns e compliance com a Lei Geral de Proteção de Dados (LGPD). Um backend inseguro não apenas coloca dados dos leads em risco como pode resultar em multas e dano reputacional irreparáveis.

## Inputs Necessários
- Código fonte do backend (FastAPI)
- `setupBackendProject()`, `createLeadEndpoints()`, `setupEventTracking()` implementados
- `scope.md` (integrações ativas)
- Acesso ao ambiente de staging/preview (não produção)

## Processo
1. **Rubrica de avaliação de segurança (100 pontos):**

   **Proteção contra Injection (25 pontos):**
   - SQL Injection via SQLAlchemy ORM (parameterized queries) → 0-10 pts
   - NoSQL Injection (se aplicável) → 0-5 pts
   - Validação de todos os inputs via Pydantic → 0-7 pts
   - Sanitização de dados antes de armazenar → 0-3 pts

   **Autenticação e Autorização (20 pontos):**
   - JWT tokens com expiração configurada → 0-5 pts
   - Verificação de token em todos os endpoints admin → 0-5 pts
   - Rate limiting no endpoint de login (brute force protection) → 0-5 pts
   - Secrets em variáveis de ambiente (não hardcoded) → 0-5 pts

   **Rate Limiting e Anti-Abuse (15 pontos):**
   - Rate limiting em endpoint de leads → 0-5 pts
   - Honeypot implementado → 0-4 pts
   - CORS configurado com origins específicas → 0-3 pts
   - Detecção de spam score → 0-3 pts

   **Headers de Segurança (15 pontos):**
   - `X-Content-Type-Options: nosniff` → 0-3 pts
   - `X-Frame-Options: DENY` → 0-3 pts
   - `X-XSS-Protection: 1; mode=block` → 0-3 pts
   - `Strict-Transport-Security` → 0-3 pts
   - `Content-Security-Policy` básico → 0-3 pts

   **LGPD Compliance (25 pontos):**
   - Coleta apenas dados necessários (minimização) → 0-5 pts
   - Política de privacidade linkada no formulário → 0-4 pts
   - Unsubscribe funcional em emails → 0-4 pts
   - Dados de IP e user agent armazenados (mas sem exposição) → 0-3 pts
   - Mecanismo de exclusão de dados (direito ao esquecimento) → 0-5 pts
   - Dados de PII hasheados antes de enviar a terceiros (Meta) → 0-4 pts

2. **Verificações técnicas de segurança:**

   **SQL Injection — Verificar que ORM é sempre usado:**
   ```python
   # INSEGURO — não deve existir no código:
   query = f"SELECT * FROM leads WHERE email = '{email}'"

   # SEGURO — como deve estar:
   query = select(Lead).where(Lead.email == email)  # SQLAlchemy ORM
   ```

   **Verificar ausência de credenciais no código:**
   ```bash
   # Procurar por padrões de credencial hardcoded:
   grep -r "SECRET_KEY\s*=\s*['\"]" src/
   grep -r "password\s*=\s*['\"]" src/
   grep -r "api_key\s*=\s*['\"]" src/
   # Nenhum resultado = aprovado
   ```

   **Verificar headers de segurança:**
   ```bash
   curl -I https://[staging-url]/api/v1/leads/
   # Verificar presença dos headers de segurança na resposta
   ```

   **Verificar HTTPS:**
   ```bash
   curl http://[staging-url]/ -I
   # Deve retornar redirect 301 para HTTPS, nunca conteúdo em HTTP
   ```

3. **Teste de rate limiting:**
   ```bash
   # Testar que 6ª requisição em 1 minuto é bloqueada:
   for i in $(seq 1 6); do
     curl -X POST https://[staging]/api/v1/leads/ \
       -H "Content-Type: application/json" \
       -d '{"email":"test@test.com","name":"Test User"}'
     echo "Request $i"
   done
   # A 6ª deve retornar 429 Too Many Requests
   ```

4. **Verificação de LGPD:**

   **Dados coletados vs dados necessários:**
   - Listar todos os campos armazenados no banco
   - Justificar a necessidade de cada campo
   - Campos sem justificativa → remover

   **Mecanismo de exclusão:**
   ```python
   # Verificar existência de endpoint para exclusão de dados:
   DELETE /api/v1/leads/{email}  # ou equivalente
   # Deve remover ou anonimizar todos os dados do lead
   ```

   **Política de privacidade:**
   - Link para política de privacidade no formulário?
   - Política de privacidade existe e está acessível?
   - Menciona coleta de dados, finalidade, período de retenção?

5. **Verificação de exposição de dados sensíveis:**
   - API de leads lista retorna IP address para usuário não-admin? → não deve
   - Mensagens de erro expõem detalhes de implementação? ("SQLite error at line X") → não deve
   - Logs de produção armazenam senhas ou tokens? → não devem

6. **Teste de endpoints sem autenticação:**
   ```bash
   # Tentar acessar admin sem token:
   curl https://[staging]/api/v1/admin/leads/ -H "Authorization: Bearer invalid_token"
   # Deve retornar 401, nunca dados
   ```

## Veto Conditions
- SQL Injection possível (query string sem parametrização) → BLOQUEANTE CRÍTICO
- Credenciais hardcoded no código → BLOQUEANTE — nunca lançar
- Endpoints admin sem autenticação → BLOQUEANTE
- PII (email, phone) enviado sem hash para Meta CAPI → BLOQUEANTE (violação de política)
- Score < 70 → não lançar backend até corrigir problemas críticos

## Output Esperado
Arquivo `review-backend.md` contendo:
- Score por critério (injection, auth, rate limiting, headers, LGPD)
- Resultado de cada teste técnico (comandos e outputs)
- Vulnerabilidades encontradas por severidade (crítica / alta / média / baixa)
- Conformidade LGPD avaliada
- Score total (0-100)
- Veredicto: APROVADO / APROVADO COM RESSALVAS / REPROVADO

## Completion Criteria
- [ ] Revisão de código para SQL injection (ORM verificado)
- [ ] Ausência de credenciais hardcoded verificada
- [ ] Rate limiting testado com 6 requisições consecutivas
- [ ] Headers de segurança verificados via curl
- [ ] HTTPS redirect verificado
- [ ] Admin endpoints testados sem autenticação (deve retornar 401)
- [ ] PII hasheado para Meta verificado
- [ ] Mecanismo de exclusão de dados verificado (LGPD)
- [ ] Política de privacidade linkada e verificada
- [ ] Score total calculado (0-100)
- [ ] Veredicto emitido
- [ ] Arquivo `review-backend.md` criado
