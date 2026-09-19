# ClariFlix · hub de skills para agentes de IA

90 habilidades instaláveis para Hermes, Claude Code, Codex e outros agentes. Cada pacote reúne um procedimento, critérios de verificação e seus arquivos de apoio.

**Catálogo:** https://clariflix.claricia.com.br · **Host técnico:** https://glaucohf.github.io/clariflix-skills

## Instalar uma habilidade

Copie o comando na página da habilidade ou escolha um pacote pelo terminal:

```sh
npx skills add https://github.com/glaucohf/clariflix-skills/tree/v0.2.0 --list
npx skills add https://github.com/glaucohf/clariflix-skills/tree/v0.2.0 --skill proposta-comercial -a codex -g
```

Troque `codex` por `claude-code` ou `hermes-agent` para esses agentes. Para escolher outro destino, omita `-a codex`. O instalador copia o pacote completo, incluindo agentes, workflows, referências, templates e scripts. Ele não executa os workflows nem configura serviços externos.

No Claude.ai, baixe o ZIP individual da [release v0.2.0](https://github.com/glaucohf/clariflix-skills/releases/tag/v0.2.0) e envie em Customize › Skills › Upload. Para chats com arquivos de projeto, a vitrine oferece uma versão Markdown que reúne os suportes textuais; ela não habilita ferramentas ausentes no chat. A proposta em PDF requer navegador e um ambiente capaz de executar a exportação.

## Coleção Máquina de Receita

A versão 0.2.0 acrescenta 78 habilidades às 12 originais:

| Área | Novas habilidades |
|---|---:|
| Vendas | 16 squads + proposta-comercial |
| Marketing | 16 squads |
| Operações & Customer Success | 16 squads |
| Gestão & Estratégia | 16 squads |
| Squads Especialistas | 13 squads |

Cada squad ganhou um `SKILL.md` com instruções para carregar os papéis e executar o workflow com as ferramentas disponíveis. Os arquivos de origem estão em `references/squad/`, com inventário de integridade e proveniência em `SOURCE.md`. Os gates humanos são mantidos; integrações como CRM, WhatsApp e mídia paga exigem configuração e autorização próprias. As metas e estimativas dos materiais de origem não são resultados comprovados do ClariFlix.

## Desenvolvimento e publicação

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
python -m unittest discover -s tests -v
python scripts/build_catalog.py --tag v0.2.0
python scripts/build_distribution.py
```

O catálogo é gerado a partir de `skills/<slug>/manifest.yaml` e `SKILL.md`. A distribuição sincroniza `catalog.json`, `site/catalog.json` e `docs/catalog.json`, gera os arquivos para anexar em `docs/prompt/` e ZIPs completos e reproduzíveis em `dist/`. As capas em `site/images/skills/<slug>.webp` são opcionais.

Para atualizar os snapshots dos squads a partir do acervo local autorizado:

```sh
python scripts/import_generated_squads.py --source-root /caminho/maquina-de-receita
python scripts/import_free_squads.py --source-root /caminho/maquina-de-receita
```

Acrescente `--check` para verificar reprodução sem escrever. Os importadores não sobrescrevem diretórios alheios à própria geração. A proposta-comercial é mantida em `skills/proposta-comercial/`; template, referências e exportador foram preservados da origem.

Use PR e merge para publicar alterações. O CI valida skills, testes e artefatos gerados. Uma tag `vX.Y.Z` aciona o workflow que cria a release e envia um ZIP por habilidade. GitHub Pages serve `docs/`; a vitrine Cloudflare Pages publica `site/`.

## Autoria e licenças

A infraestrutura original do ClariFlix permanece MIT, conforme [LICENSE](LICENSE). Os conteúdos importados mantêm autoria e condições próprias: 64 squads Proprietary, 11 squads MIT, um Commercial, um sem licença declarada e a proposta sob as condições do Máquina de Receita. Consulte `LICENSE` e `SOURCE.md` de cada pacote; a licença da raiz não relicencia conteúdo de terceiros.

Origem da coleção: [Máquina de Receita](https://github.com/educacional-lendario/maquina-de-receita), de Gabriel Marcondes, com montagem e revisão pela Academia Lendária. O mantenedor confirmou em 2026-09-18 possuir autorização dos autores para a disponibilização pública desta coleção. Isso não concede redistribuição irrestrita aos destinatários. A proveniência dos 13 squads de terceiros acompanha cada pacote.
