# Instagram Caption Writer

> Squad especializado na criação de legendas para Instagram com estrutura de copy persuasivo. 7 agentes orquestrados, 4 tasks e 2 workflows para produzir 3 variações de legenda + 30 hashtags segmentadas por sessão.

---

## Visão Geral

O **Instagram Caption Writer** é um conjunto de agentes de IA especializados que trabalham em pipeline para transformar um tópico de post em legendas completas, prontas para publicar.

O squad cobre todo o ciclo de produção de copy para Instagram:

- **Estratégia** — Diagnóstico de nicho, objetivo e formato antes de escrever
- **Escrita** — 3 variações completas por post (emocional / lógica / provocativa)
- **Ganchos** — 7+ opções de hook por tipo antes de definir a abertura
- **Hashtags** — 30 hashtags segmentadas por volume (grandes / médias / pequenas)
- **Teste A/B** — Pontuação das variações com recomendação fundamentada
- **Repurposing** — Adaptação automática para LinkedIn, Twitter/X, TikTok e YouTube Shorts

### Diferenciais

- Estrutura fixa de copy: **hook + desenvolvimento + CTA** em toda variação
- 3 variações por post = abordagens distintas com o mesmo tópico
- Hashtags segmentadas por competitividade — não apenas por volume
- Fluxo com checkpoint: a IA apresenta estratégia antes de escrever

---

## Agentes

| # | Ícone | Nome | Título | Tier |
|---|-------|------|--------|------|
| 1 | 🎯 | `instagram-caption-chief` | Orquestrador do Squad | Orchestrator |
| 2 | 🧠 | `caption-strategist` | Estrategista de Conteúdo | Tier 0 |
| 3 | ✍️ | `caption-writer` | Redator de Legendas | Tier 1 |
| 4 | 🪝 | `hook-generator` | Gerador de Ganchos | Tier 1 |
| 5 | #️⃣ | `hashtag-researcher` | Pesquisador de Hashtags | Tier 2 |
| 6 | ⚖️ | `caption-ab-tester` | Analista de Variações | Tier 2 |
| 7 | 🔄 | `caption-repurposer` | Adaptador Multiplataforma | Tier 2 |

---

## Pipeline — Fluxo Principal

```
Entrada → caption-strategist → caption-writer (3 variações) → hashtag-researcher → Saída
```

### Fases Detalhadas

| Fase | Agente(s) | Entrada | Saída |
|------|-----------|---------|-------|
| 1. Estratégia | `caption-strategist` | Tópico + formato + objetivo | Ângulo + estrutura da legenda |
| 2. Escrita | `caption-writer` | Estratégia + tópico | 3 variações completas |
| 3. Hashtags | `hashtag-researcher` | Nicho + tópico | 30 hashtags segmentadas |
| 4. Análise (opcional) | `caption-ab-tester` | 2–3 variações | Pontuação + recomendação |
| 5. Repurposing (opcional) | `caption-repurposer` | Legenda finalizada | Versões para outras plataformas |

---

## Comandos Rápidos

| Comando | Descrição | Agente |
|---------|-----------|--------|
| `*write-caption` | Fluxo principal: tópico → 3 legendas + hashtags | Chief |
| `*diagnose-caption` | Auditar legenda existente e reescrever pontos fracos | Strategist |
| `*generate-hooks-batch` | Gerar 20+ hooks para um nicho | Hook Generator |
| `*create-content-pillars` | Definir 4–5 pilares de conteúdo para um perfil | Strategist |
| `*content-week-in-one-shot` | Semana completa de conteúdo (5 posts) em uma sessão | Chief |
| `*viral-post-anatomy` | Analisar post viral, extrair padrão e replicar | Strategist + Writer |

---

## Formatos Suportados

| Formato | Comprimento | Estrutura |
|---------|-------------|-----------|
| Feed | 300–500 palavras | Hook + desenvolvimento + CTA |
| Reels | 50–150 palavras | Hook + CTA direto |
| Carrossel | Copy por slide + legenda principal | Abertura + corpo por slide + CTA |
| Stories | 10–30 palavras | Texto de impacto para overlay |

---

## Inputs Obrigatórios

| Campo | Obrigatório |
|-------|-------------|
| Tópico do post | Sim |
| Formato (feed / reels / carousel / stories) | Sim |
| Objetivo (engajamento / autoridade / venda) | Sim |
| Tom de voz | Sim |
| Produto ou serviço | Condicional (apenas em posts de venda) |

---

## Output Entregue

- 3 variações completas de legenda
- 30 hashtags em 3 segmentos (10 grandes + 10 médias + 10 pequenas)
- CTA recomendado por objetivo
- Melhor horário de publicação por nicho

---

## Instalação

```bash
npx squads add [owner]/squads/instagram-caption-writer -y
```

---

## Estrutura do Squad

```
squads/instagram-caption-writer/
├── README.md
├── config.yaml
│
├── agents/
│   ├── instagram-caption-chief.md    # Orchestrator
│   ├── caption-strategist.md         # Tier 0 — Estratégia e diagnóstico
│   ├── caption-writer.md             # Tier 1 — Redação das 3 variações
│   ├── hook-generator.md             # Tier 1 — Geração de ganchos
│   ├── hashtag-researcher.md         # Tier 2 — Pesquisa de hashtags
│   ├── caption-ab-tester.md          # Tier 2 — Análise e pontuação
│   └── caption-repurposer.md         # Tier 2 — Adaptação multiplataforma
│
├── tasks/
│   ├── write-caption.md              # Fluxo principal
│   ├── diagnose-caption.md           # Auditoria e reescrita
│   ├── generate-hooks-batch.md       # Geração em lote de ganchos
│   └── create-content-pillars.md     # Definição de pilares de conteúdo
│
├── workflows/
│   ├── content-week-in-one-shot.md   # Semana completa em uma sessão
│   └── viral-post-anatomy.md         # Análise e replicação de post viral
│
└── templates/
    └── caption-output.md             # Template de saída padronizado
```

---

## Pré-requisitos

| Requisito | Versão | Obrigatório |
|-----------|--------|-------------|
| Node.js | 18+ | Sim |
| npm / pnpm | latest | Sim |
| AIOS CLI | 2.1.0+ | Sim |

---

## Licença

MIT

---

*Instagram Caption Writer v1.0.0*
