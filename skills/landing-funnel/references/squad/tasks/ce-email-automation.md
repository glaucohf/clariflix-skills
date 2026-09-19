---
task: setupAutomation()
agent: ce-email-strategist
description: "Configurar automação na plataforma (Mailchimp/ActiveCampaign/Brevo): triggers, delays, tags, condicionais"
elicit: true
responsavel: "Thread"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: emailSeries
    tipo: file
    obrigatorio: true
    descricao: "Série de emails escrita"
  - nome: emailPlatformConfig
    tipo: object
    obrigatorio: true
    descricao: "Credenciais da plataforma de email (Mailchimp/ActiveCampaign/Brevo)"

Saida:
  - nome: automationSetup
    tipo: file
    obrigatorio: true
    descricao: "Automação configurada: triggers, delays, tags e condicionais na plataforma"

Checklist:
  pre-conditions:
    - "[ ] Emails escritos"
    - "[ ] Plataforma de email configurada"
  post-conditions:
    - "[ ] Trigger de entrada configurado"
    - "[ ] Delays entre emails definidos"
    - "[ ] Condicionais de segmentação ativas"
---

# Task: setupAutomation()

## Objetivo
Configurar a automação completa da sequência de emails na plataforma escolhida, incluindo triggers de entrada, delays corretos entre emails, tags de comportamento e condicionais que adaptam a sequência com base nas ações do lead. A automação bem configurada trabalha 24/7 sem intervenção manual.

## Inputs Necessários
- `email-sequence-map.md` (mapeamento da sequência)
- `email-series.md` (copy completo de cada email)
- Plataforma de email definida e conta configurada (`ce-integrator-email.md`)
- API ou integração com o backend para receber leads
- Tags e listas definidas

## Processo
1. **Elicitação de configuração da plataforma:**
   - Plataforma: Mailchimp / ActiveCampaign / Brevo / ConvertKit / SendGrid?
   - Conta já existe ou precisa criar?
   - SPF/DKIM já configurado para o domínio?
   - Qual é o método de entrada do lead na automação? (API, webhook, formulário nativo)

2. **Estrutura de listas e tags** — Antes de criar automações:

   **Listas/Audiences:**
   - Lista principal: "Leads [Nome do Produto]" — todos os leads capturados
   - Lista de clientes: "Clientes [Nome do Produto]" — para sair da sequência de nurture
   - Lista fria: "Sem engajamento 30d" — leads que nunca abriram

   **Tags de entrada:**
   - `source:lp` — veio da landing page
   - `utm:{{utm_source}}-{{utm_medium}}` — fonte de tráfego
   - `interest:{{produto}}` — produto de interesse

   **Tags de comportamento (aplicadas pela automação):**
   - `engaged:email` — abriu pelo menos 3 emails
   - `clicked:offer` — clicou no link da oferta
   - `converted` — tornou-se cliente (aplicada externamente pelo backend)
   - `unresponsive:7d` — não abriu em 7 dias
   - `unsubscribed` — fez unsubscribe

3. **Configuração no ActiveCampaign (exemplo detalhado):**

   **Automação: "Nurture [Produto] — Sequência Principal"**

   ```
   TRIGGER: Tag adicionada "source:lp"
   │
   ├─ AGUARDAR: 0 minutos
   ├─ ENVIAR: Email 1 — Welcome
   │
   ├─ AGUARDAR: 1 dia
   ├─ CONDIÇÃO: Email 1 foi aberto?
   │   ├─ SIM → ENVIAR: Email 2 — Educação
   │   └─ NÃO → AGUARDAR: 1 dia adicional
   │             └─ ENVIAR: Email 2 com subject alternativo
   │
   ├─ AGUARDAR: 2 dias
   ├─ ENVIAR: Email 3 — Prova Social
   │
   ├─ AGUARDAR: 2 dias
   ├─ ENVIAR: Email 4 — Objeção
   │
   ├─ AGUARDAR: 2 dias
   ├─ ENVIAR: Email 5 — Oferta
   │   ├─ ADICIONAR TAG: "recebeu:oferta"
   │   └─ [AGUARDAR CLIQUE]
   │       └─ SE clicou em link da oferta → ADICIONAR TAG: "clicked:offer"
   │
   ├─ AGUARDAR: 2 dias
   ├─ CONDIÇÃO: Tag "converted" existe?
   │   ├─ SIM → FIM da sequência (lead já comprou)
   │   └─ NÃO → ENVIAR: Email 6 — Urgência
   │
   ├─ AGUARDAR: 1 dia
   ├─ CONDIÇÃO: Tag "converted" existe?
   │   ├─ SIM → FIM
   │   └─ NÃO → ENVIAR: Email 7 — Última Chance
   │
   └─ FIM da sequência ativa
       └─ MOVER para: Lista "Leads Frios" (nurture mensal)
   ```

4. **Configuração no Mailchimp (alternativa):**
   - Criar Customer Journey (ou Classic Automation)
   - Starting point: "Joins audience" ou "Tag applied"
   - Adicionar emails com delays configurados
   - Adicionar condicionais "IF/ELSE" por abertura de email
   - Configurar saída automática se tag "converted" for aplicada

5. **Configuração no Brevo (ex-Sendinblue):**
   - Marketing Automation → Criar workflow
   - Trigger: "Contact added to list" ou "API event"
   - Blocos: Email send, Wait, Condition, Update contact attribute
   - Configurar condição de saída por tag/atributo "status = converted"

6. **Integração backend → plataforma** — Configurar envio de leads:

   **Via API direta (recomendado para precisão):**
   ```python
   # src/services/email_service.py — já implementado
   async def add_lead_to_automation(lead: Lead):
       """Adicionar lead à plataforma de email e iniciar automação"""
       # ActiveCampaign exemplo:
       contact_id = await ac.create_contact(lead)
       await ac.add_tag(contact_id, f"source:lp")
       await ac.add_tag(contact_id, f"utm:{lead.source or 'direct'}")
       # A automação dispara automaticamente quando a tag "source:lp" é adicionada
   ```

   **Via webhook (alternativa):**
   - Configurar webhook no backend para POST para URL da plataforma
   - Incluir todos os campos necessários (email, nome, tags, UTM)

7. **Configuração de unsubscribe** — Garantir compliance:
   - Link de unsubscribe em TODOS os emails (obrigatório pela plataforma)
   - Configurar unsubscribe global (não apenas de lista específica)
   - Verificar que unsubscribe na plataforma sync com backend (via webhook da plataforma)

8. **Teste completo da automação antes de ativar:**
   - Adicionar email de teste à lista com tags corretas
   - Verificar que Email 1 dispara imediatamente (< 5 min)
   - Verificar que delays estão corretos
   - Verificar que condicionais funcionam (testar abrindo e não abrindo)
   - Verificar unsubscribe
   - Verificar que lead "converted" sai da sequência

## Veto Conditions
- Automação sem condição de saída para clientes que já compraram → implementar antes de ativar
- Delay do Email 1 > 10 minutos → otimizar para < 5 minutos (janela de atenção)
- Sem teste completo antes de ativar → testar com email real do squad
- Urgência com prazo fixo (não dinâmico) em automação que roda por meses → usar urgência relativa ao lead ou prazo real de promoção

## Output Esperado
- Automação completa configurada e testada na plataforma
- Integração backend → plataforma funcionando (leads chegando automaticamente)
- Unsubscribe configurado e funcionando
- Documento `automation-config.md` com print/documentação de cada etapa configurada

## Completion Criteria
- [ ] Listas e tags criadas na plataforma
- [ ] Automação com todos os emails carregados com copy correto
- [ ] Delays configurados conforme `email-sequence-map.md`
- [ ] Condicionais por abertura de email implementadas
- [ ] Condição de saída para clientes convertidos implementada
- [ ] Integração backend → plataforma: lead novo disparando automação automaticamente
- [ ] Unsubscribe global funcionando
- [ ] Teste completo com email real passando por toda a sequência
- [ ] Documento `automation-config.md` criado com configurações documentadas
