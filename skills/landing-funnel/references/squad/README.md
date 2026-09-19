# LandingFunnel Squad

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![AIOS](https://img.shields.io/badge/AIOS-2.1.0%2B-purple)
![License](https://img.shields.io/badge/license-Commercial-orange)

> Squad de criação e otimização de landing pages com pipeline end-to-end em 3 fases: construção, lançamento e otimização pós-lançamento.
> 13 agentes especializados, 57 tasks e 10 workflows — do briefing ao A/B test.

---

## Visão Geral

O **LandingFunnel Squad** é um conjunto de agentes de IA que operam em pipeline para transformar uma ideia de produto em uma landing page funcional, mensurada e continuamente otimizada.

O squad cobre três fases distintas:

- **Construção** — Discovery, pesquisa de mercado, copy, design system atômico, imagens por IA, frontend Next.js e backend FastAPI
- **Lançamento** — Checklist pré-lançamento com gates automáticos (PageSpeed, analytics, conversion score)
- **Pós-lançamento** — Analytics (GTM/GA4/Pixels), heatmaps, A/B testing com rigor estatístico, social proof system e sequência de email nurture

### Diferenciais

- **4 agentes exclusivos de pós-lançamento**: analytics, A/B testing, social proof e email nurture
- **Server-side event tracking**: GA4 Measurement Protocol + Meta Conversions API no backend
- **Gates de proteção**: PageSpeed < 90, analytics sem dados e conversion score < 75 bloqueiam lançamento automaticamente
- **A/B testing com rigor estatístico**: declaração de vencedor somente com p-value < 0.05
- Acessibilidade **WCAG AAA** mandatória (contraste 7:1)
- **Light/Dark mode** obrigatório em ambos os modos
- Design system baseado em **Atomic Design** (tokens → pages)
- Licença **Commercial** com Commons Clause — uso livre, revenda bloqueada

---

## Agentes

### Fase 1 — Construção (8 agentes)

| # | Nome | Persona | Título |
|---|------|---------|--------|
| 1 | `ce-strategist` | **Vortex** | Funnel Architect & Conversion Strategist |
| 2 | `ce-researcher` | **Radar** | Market Intelligence Specialist |
| 3 | `ce-copywriter` | **Pulse** | Conversion Copywriter & VSL Specialist |
| 4 | `ce-design-architect` | **Canvas** | UX & CRO Design Architect |
| 5 | `ce-image-creator` | **Flash** | Visual Storyteller & Asset Creator |
| 6 | `ce-frontend-dev` | **Turbo** | Performance Frontend Engineer |
| 7 | `ce-backend-dev` | **Vault** | Backend & Data Layer Engineer |
| 8 | `ce-integrator` | **Link** | Ecosystem Integration Specialist |

### Fase 2 — QA (1 agente)

| # | Nome | Persona | Título |
|---|------|---------|--------|
| 9 | `ce-reviewer` | **Audit** | Conversion QA Lead |

### Fase 3 — Pós-Lançamento (4 agentes exclusivos)

| # | Nome | Persona | Título |
|---|------|---------|--------|
| 10 | `ce-analytics-architect` | **Lens** | Analytics & Tracking Architect |
| 11 | `ce-ab-architect` | **Split** | A/B Test Architect |
| 12 | `ce-social-proof` | **Trust** | Social Proof System Architect |
| 13 | `ce-email-strategist` | **Thread** | Email Nurture Strategist |

> **Agentes condicionais:** Vault (backend), Link (integrações), Lens (analytics), Split (A/B), Trust (social proof) e Thread (email) são ativados pelas flags correspondentes definidas no escopo.

---

## Pipeline — 3 Fases

```
 FASE 1: CONSTRUÇÃO
 ┌──────────┐   ┌──────────┐   ┌────────────────────────────┐
 │  Vortex  │──>│  Radar   │──>│  Pulse   Canvas   Trust    │
 │          │   │          │   │  (copy)  (design) (social) │
 │ *discover│   │ *spy     │   │          (paralelo)        │
 │ *funnel  │   │ *profile │   │                            │
 │ *scope   │   │ *synth   │   └────────────┬───────────────┘
 └──────────┘   └──────────┘                │
                                            v
                              ┌─────────────────────────┐
                              │          Flash          │
                              │      *generate-hero     │
                              │      *generate-sections │
                              └────────────┬────────────┘
                                           │
                                           v
 ┌─────────────────────────┐   ┌──────────────────────────┐
 │  Turbo   Vault   Lens   │──>│          Link            │
 │ (front) (back) (analyt) │   │      *connect-all        │
 │          (paralelo)     │   └──────────────────────────┘
 └─────────────────────────┘

 FASE 2: QA + LANÇAMENTO
 ┌──────────────────────────────────────────────────────────┐
 │                         Audit                            │
 │  *review-copy  *review-design  *review-seo-a11y          │
 │  *review-conversion  *review-backend  *final-report      │
 │                                                          │
 │  Gates (BLOCKING): PageSpeed ≥ 90 | Score ≥ 75 | GA4 ✓  │
 └──────────────────────────────────────────────────────────┘

 FASE 3: PÓS-LANÇAMENTO
 ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
 │   Lens   │──>│  Split   │──>│  Pulse   │   │  Thread  │
 │          │   │          │   │ (variante│   │  (email  │
 │ *gtm     │   │ *hypoth. │   │  venced.)│   │  nurture)│
 │ *ga4     │   │ *variants│   └──────────┘   │          │
 │ *pixels  │   │ *setup   │                  │ *sequence│
 │ *heatmap │   │ *analyze │                  │ *automat.│
 └──────────┘   └──────────┘                  └──────────┘
```

### Fases Detalhadas

| Fase | Agente(s) | Entrada | Saída |
|------|-----------|---------|-------|
| 1. Discovery | Vortex | Ideia do usuário | Product brief + mapa de funil + flags |
| 2. Intelligence | Radar | Product brief | Intelligence brief: concorrentes, audiência, benchmarks de tráfego |
| 3. Copy + Design + Social Proof | Pulse + Canvas + Trust (paralelo) | Intelligence brief | Copy por seção + VSL + design system + social proof assets |
| 4. Images | Flash | Copy + design system | Imagens hero, seções e social proof |
| 5. Build | Turbo + Vault + Lens (paralelo) | Todos os assets | Frontend + backend + analytics configurados |
| 6. Integration | Link | Frontend + backend | WhatsApp, email, CRM, Stripe conectados |
| 7. QA Gate | Audit | Projeto completo | Conversion score por dimensão + GO/NO-GO |
| 8. Post-Launch | Lens + Split + Thread | Dados reais (≥ 500 sessões) | A/B tests rodando + email sequence ativa |

---

## Workflows

| Workflow | Descrição |
|----------|-----------|
| `ce-full-pipeline` | Pipeline master end-to-end |
| `ce-discovery-flow` | Sub-workflow: discovery + mapa de funil + escopo |
| `ce-intelligence-flow` | Sub-workflow: spy competitivo + audience + dados de tráfego |
| `ce-copy-design-parallel` | Sub-workflow paralelo: copy + design + social proof |
| `ce-build-parallel` | Sub-workflow paralelo: frontend + backend + analytics |
| `ce-section-pipeline` | Micro-workflow por seção: copy → design → imagem → código |
| `ce-launch-prep` | Checklist pré-lançamento com gates automáticos |
| `ce-post-launch` | Primeiros 7 dias: heatmap + email + dados iniciais |
| `ce-ab-design` | Ciclo completo de A/B testing (hipótese → análise estatística) |
| `ce-qa-gate` | QA multi-dimensional com conversion score 0–100 por dimensão |

---

## Comandos Rápidos

| Comando | Agente | Descrição |
|---------|--------|-----------|
| `*discover` | Vortex | Absorver produto e mapear funil |
| `*elicit` | Vortex | Questionário de 12 perguntas estruturadas |
| `*scope` | Vortex | Definir escopo e flags condicionais |
| `*spy-competitors` | Radar | Análise de 5+ concorrentes com anúncios ativos |
| `*write-vsl` | Pulse | Script de VSL (Video Sales Letter) |
| `*write-ab-variants` | Pulse | Variantes de copy para A/B test |
| `*cro-audit` | Canvas | Audit de CRO por design (Fogg + Cialdini) |
| `*optimize-performance` | Turbo | PageSpeed 100, LCP < 1.2s, CLS < 0.1 |
| `*setup-events` | Vault | Server-side event tracking GA4 + Meta CAPI |
| `*setup-gtm` | Lens | Google Tag Manager completo |
| `*configure-ga4` | Lens | GA4 com eventos customizados e conversões |
| `*setup-pixels` | Lens | Meta Pixel + Conversions API + Google Ads |
| `*configure-heatmaps` | Lens | Hotjar ou Microsoft Clarity |
| `*formulate-hypothesis` | Split | Hipótese baseada em dados de heatmap/analytics |
| `*design-variants` | Split | Variantes A e B para elementos testáveis |
| `*analyze-results` | Split | Análise estatística (p-value, intervalo de confiança) |
| `*structure-testimonials` | Trust | Testimonials no formato: foto + nome + resultado |
| `*build-cases` | Trust | Micro cases no framework STAR |
| `*map-sequence` | Thread | Sequência de nurture pós-conversão |
| `*write-series` | Thread | Série de emails completa |
| `*review-conversion` | Audit | Conversion score 0–100 |
| `*final-report` | Audit | Relatório com GO/NO-GO e scores por dimensão |

---

## Componentes Condicionais

| Flag | Componente | Quando Ativar |
|------|-----------|---------------|
| `backend: true` | Vault (ce-backend-dev) | Captura de leads, event tracking server-side, admin panel |
| `analytics: true` | Lens (ce-analytics-architect) | GTM, GA4, Meta Pixel, Google Ads, heatmaps |
| `ab_testing: true` | Split (ce-ab-architect) | Ciclo de A/B testing pós-lançamento |
| `social_proof: true` | Trust (ce-social-proof) | Testimonials, cases STAR, trust badges |
| `email_nurture: true` | Thread (ce-email-strategist) | Sequência de nurture pós-conversão |
| `whatsapp: true` | Link (ce-integrator) | WhatsApp via evolution-api |
| `payments: true` | Link (ce-integrator) | Checkout Stripe direto na landing page |
| `crm: true` | Link (ce-integrator) | Sync com HubSpot, ActiveCampaign ou RD Station |

### Cenários de Uso

**Frontend simples:**
```yaml
backend: false
analytics: false
```
Agentes ativos: Vortex, Radar, Pulse, Canvas, Flash, Turbo, Audit

**Com captura de leads e analytics:**
```yaml
backend: true
analytics: true
email_nurture: true
```
Agentes ativos: todos exceto Split e social_proof

**Stack completa:**
```yaml
backend: true
analytics: true
ab_testing: true
social_proof: true
email_nurture: true
whatsapp: true
payments: true
crm: true
```
Todos os 13 agentes ativos.

---

## Pré-requisitos

| Requisito | Versão | Obrigatório |
|-----------|--------|-------------|
| **AIOS CLI** | 2.1.0+ | Sim |
| **Node.js** | 18+ | Sim |
| **Python** | 3.12+ | Condicional (flag `backend`) |
| **Docker** | latest | Condicional (flag `backend`) |

### MCPs Necessários

| MCP | Obrigatório | Uso |
|-----|-------------|-----|
| `nano-banana-pro` | Sim | Geração de imagens (hero, seções, social proof) |
| `playwright` | Opcional | Auditoria de páginas concorrentes em tempo real |
| `dalle3` | Opcional | Geração alternativa de imagens |
| `shadcn` | Opcional | Componentes UI base |

### Chaves de API (conforme flags ativas)

- **Gemini API Key** — imagens via nano-banana-pro
- **GTM Container ID** — flag `analytics`
- **GA4 Measurement ID** — flag `analytics`
- **Meta Pixel ID + Access Token** — flag `analytics`
- **Hotjar Site ID** ou **Microsoft Clarity ID** — flag `analytics`
- **Stripe Secret Key** — flag `payments`
- **evolution-api URL + token** — flag `whatsapp`
- **CRM API Key** — flag `crm`

---

## Instalação

```bash
npx squads add squad-creator-pro/squads-creator/landing-funnel -y
```

### Ativar o squad

```bash
# Pipeline completo
@landing-funnel:ce-strategist *discover

# Ou por agente específico
@landing-funnel:ce-analytics-architect *setup-gtm
@landing-funnel:ce-ab-architect *formulate-hypothesis
@landing-funnel:ce-reviewer *review-conversion
```

---

## Estrutura do Squad

```
squads/landing-funnel/
├── README.md
├── squad.yaml
├── LICENSE
│
├── agents/                          # 13 agentes
│   ├── ce-strategist.md            # Vortex — Funnel Architect
│   ├── ce-researcher.md            # Radar — Market Intelligence
│   ├── ce-copywriter.md            # Pulse — Conversion Copywriter
│   ├── ce-design-architect.md      # Canvas — UX & CRO
│   ├── ce-image-creator.md         # Flash — Visual Storyteller
│   ├── ce-frontend-dev.md          # Turbo — Performance Frontend
│   ├── ce-backend-dev.md           # Vault — Backend (Condicional)
│   ├── ce-integrator.md            # Link — Integrations (Condicional)
│   ├── ce-reviewer.md              # Audit — QA Lead
│   ├── ce-analytics-architect.md   # Lens — Analytics (Condicional)
│   ├── ce-ab-architect.md          # Split — A/B Testing (Condicional)
│   ├── ce-social-proof.md          # Trust — Social Proof (Condicional)
│   └── ce-email-strategist.md      # Thread — Email Nurture (Condicional)
│
├── tasks/                           # 57 tasks executáveis
│   ├── ce-strategist-*.md          # Discovery e escopo (4)
│   ├── ce-researcher-*.md          # Inteligência de mercado (5)
│   ├── ce-copywriter-*.md          # Copy e VSL (4)
│   ├── ce-design-architect-*.md    # Design e CRO (5)
│   ├── ce-image-creator-*.md       # Geração de imagens (3)
│   ├── ce-frontend-dev-*.md        # Frontend e performance (5)
│   ├── ce-backend-dev-*.md         # Backend e event tracking (4)
│   ├── ce-integrator-*.md          # Integrações (5)
│   ├── ce-analytics-architect-*.md # GTM, GA4, pixels, heatmaps (4)
│   ├── ce-ab-architect-*.md        # A/B testing (4)
│   ├── ce-social-proof-*.md        # Social proof system (4)
│   ├── ce-email-strategist-*.md    # Email nurture (4)
│   └── ce-reviewer-*.md            # QA multi-dimensional (6)
│
├── workflows/                       # 10 workflows
│   ├── ce-full-pipeline.yaml       # Pipeline master
│   ├── ce-discovery-flow.yaml      # Sub-workflow: discovery
│   ├── ce-intelligence-flow.yaml   # Sub-workflow: pesquisa
│   ├── ce-copy-design-parallel.yaml # Sub-workflow: paralelo
│   ├── ce-build-parallel.yaml      # Sub-workflow: build paralelo
│   ├── ce-section-pipeline.yaml    # Micro-workflow: por seção
│   ├── ce-launch-prep.yaml         # Checklist pré-lançamento
│   ├── ce-post-launch.yaml         # Pós-lançamento (7 dias)
│   ├── ce-ab-design.yaml           # Ciclo de A/B testing
│   └── ce-qa-gate.yaml             # QA com conversion score
│
├── config/
│   ├── coding-standards.md         # Padrões de código
│   ├── tech-stack.md               # Stack tecnológica completa
│   └── source-tree.md              # Estrutura de diretórios do projeto
│
└── data/
    └── conversion-playbooks.md     # Benchmarks por nicho (SaaS, infoproduto, e-commerce...)
```

---

## Licença

Commercial License with Commons Clause.

Uso livre para projetos próprios. Redistribuição ou revenda comercial requer autorização.

---

*LandingFunnel Squad v1.0.0 — Synkra AIOS 2.1.0+*
