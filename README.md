# ClariFlix · hub de skills para agentes de IA

Skills instaláveis por comando — copy-paste — para Hermes, Claude, ChatGPT/Codex, Claude Code e outros
agentes. Cada skill é um procedimento com verificação binária, não um prompt solto.

**Catálogo:** https://clariflix.claricia.com.br (em construção) · **Host técnico:** `docs/` deste repo,
via GitHub Pages, em `https://glaucohf.github.io/clariflix-skills`.

Inspirado em [AgentsFlix/skills](https://github.com/AgentsFlix/skills) (MIT, José Carlos Amorim) — mesma
arquitetura (site estático lendo `catalog.json`, skills versionadas, release por tag), catálogo e marca
próprios da Claricia.

## Instalar uma skill

| agente | como |
|---|---|
| Hermes | `hermes skills install https://raw.githubusercontent.com/glaucohf/clariflix-skills/v0.1.0/skills/<slug>/SKILL.md` |
| Claude Code / Codex / outros | `npx skills add https://glaucohf.github.io/clariflix-skills --skill <slug> -a claude-code -g` |
| Claude.ai | baixe o zip da [release](https://github.com/glaucohf/clariflix-skills/releases) e envie em Customize › Skills › Upload |

Veja o comando exato de cada skill na página ou em `catalog.json`.

## Estrutura

```
skills/<slug>/SKILL.md, references/, templates/, manifest.yaml   fonte de cada skill
scripts/hub_common.py            constantes únicas (URLs, limite de description)
scripts/build_catalog.py         gera catalog.json a partir de skills/*/manifest.yaml
catalog.json                     o que o site lê
site/index.html                  a vitrine (Cloudflare Pages) — temas Claricia e Netflix
site/images/skills/<slug>.webp   capas geradas por IA, usadas nos cards e painéis
supabase/migrations/             schema de contas/pagamento (fase 2/3, ainda não ativado)
docs/                             planejamento completo do projeto
```

## Publicar uma skill nova

1. Crie `skills/<slug>/SKILL.md` (frontmatter + When to Use + Quick Reference + Procedure + Pitfalls + Verification) e `manifest.yaml`.
2. `python3 scripts/build_catalog.py --tag v0.1.0` para regerar `catalog.json`.
3. Commit, PR, merge; crie uma tag `vX.Y.Z` quando publicar.

As capas são opcionais: salve a imagem em `site/images/skills/<slug>.webp` antes de gerar o catálogo.
O gerador inclui o campo `image` quando encontra o arquivo. Copie o `catalog.json` atualizado para
`site/catalog.json` antes de publicar a vitrine. Os prompts da coleção estão em
[`docs/skill-image-prompts.json`](docs/skill-image-prompts.json).

## Licença

MIT — veja `LICENSE`.
