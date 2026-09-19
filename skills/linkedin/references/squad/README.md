# LinkedIn Squad

Squad para gestão de presença no LinkedIn: análise de tendências, geração de conteúdo, otimização de perfil e estratégia de personal branding.

**Foco:** Segurança Ofensiva + Automação com IA
**Cadência:** 1 post/semana
**Público:** Profissionais de segurança + Juniores de TI

## Arquitetura

```
linkedin-chief 🔗 (Link - Orchestrator)
├── trend-scout 🔍 (Scout)     Análise de tendências e news
├── ghostwriter 👻 (Ghost)     Geração de conteúdo no estilo Sid
├── profile-analyst 📊 (Pulse) Análise de perfil e métricas
└── carousel-designer 🎨 (Slide) Conteúdo para carrosséis
```

## Quick Start

```bash
# Ativar squad
@linkedin-chief

# Gerar plano semanal
@linkedin-chief *plan

# Criar post sobre um tema
@linkedin-chief *post "AI agents em pentest"

# Criar carrossel
@linkedin-chief *carousel "5 tools de recon"

# Ver tendências
@linkedin-chief *trending

# Analisar perfil
@linkedin-chief *profile
```

## Agentes

| Agente | Persona | Função |
|--------|---------|--------|
| linkedin-chief | 🔗 Link | Orquestra estratégia, roteia requests, plano semanal |
| trend-scout | 🔍 Scout | Monitora tendências em CyberSec/AI, sugere temas |
| ghostwriter | 👻 Ghost | Gera posts e textos no estilo do Sid |
| profile-analyst | 📊 Pulse | Analisa perfil, métricas, sugere otimizações |
| carousel-designer | 🎨 Slide | Cria conteúdo estruturado para carrosséis |

## Tasks

| Task | Agente | Descrição |
|------|--------|-----------|
| analyze-profile | @profile-analyst | Análise completa do perfil LinkedIn |
| suggest-topics | @trend-scout | Sugestões de temas baseadas em expertise + trends |
| generate-post | @ghostwriter | Gerar post completo pronto para publicação |
| generate-carousel | @carousel-designer | Gerar conteúdo de carrossel (slides + post) |
| analyze-trending | @trend-scout | Scan de tendências em CyberSec/AI |
| weekly-content-plan | @linkedin-chief | Plano semanal com tema, formato e rascunho |

## Workflow

| Workflow | Descrição |
|----------|-----------|
| weekly-content-cycle | Ciclo completo: trends → tema → conteúdo → revisão → plano |

## Pilares de Conteúdo

| # | Pilar | Exemplos |
|---|-------|----------|
| 1 | Segurança Ofensiva | Pentesting, Red Team, vulnerabilidades, metodologias |
| 2 | Automação com IA | AI Agents, LLMs, automações práticas |
| 3 | Bastidores | Dia a dia em CyberSec, desafios reais |
| 4 | Mentoria | Dicas para juniores entrando na área |

## Mix de Formatos

| Semana | Formato | Tipo |
|--------|---------|------|
| 1 | Post texto | Insight técnico / opinião |
| 2 | Carrossel | Tutorial / explicação visual |
| 3 | Post texto | Storytelling do dia a dia |
| 4 | Carrossel | Lista / framework / checklist |

## Referências

- **Estilo de escrita:** `data/writing-style.md`
- **Perfil LinkedIn:** [F0livora](https://www.linkedin.com/in/sidney-fernandes-a448152a8/)
- **Inspiração:** Andrew Martinez (HackerSec) — storytelling + técnico

---

*LinkedIn Squad v1.0.0 — F0livora*
*Prefix: /li*
