"""Constantes e funções compartilhadas pelos scripts deste repo.

Fonte única para: URLs base, limite da description, skills que exigem terminal.
Baseado em AgentsFlix/skills (MIT, José Carlos Amorim) — adaptado para a Claricia.
"""
from __future__ import annotations

REPO_SLUG = "glaucohf/clariflix-skills"                              # trocar para "claricia/clariflix-skills" se a org for criada
WELLKNOWN = "https://glaucohf.github.io/clariflix-skills"            # host técnico: catálogo, .well-known, coláveis
HUB_URL = "https://clariflix.claricia.com.br"                        # a página da marca

DESC_MAX = 200                                                        # Claude.ai rejeita description maior; hermes skills search lê os primeiros chars
RUNTIME_ONLY: set[str] = set()                                        # skills que exigem terminal/rede (nenhuma ainda)


def cap200(desc: str) -> str:
    """Normaliza espaços e corta na última palavra inteira antes de DESC_MAX, com reticência."""
    desc = " ".join(desc.split())
    return desc if len(desc) <= DESC_MAX else desc[:DESC_MAX].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def activation_text(slug: str, trig: str) -> str:
    """Texto que a pessoa cola nas instruções de um Projeto (ChatGPT/Claude) para a versão colável funcionar."""
    return (f"Você tem no arquivo `{slug}.md` uma skill chamada {slug}. Quando eu pedir algo como \"{trig}\", siga o `## Procedure` desse arquivo à risca, "
            f"use as seções `Referência:` dele no lugar dos arquivos que ele cita, e termine pela `## Verification`. Se faltar informação, pergunte antes de escrever.")
