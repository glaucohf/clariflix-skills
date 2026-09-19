# Proposta Comercial no ClariFlix

Instale o pacote completo para obter o template, as referências e o exportador:

```sh
npx skills add https://github.com/glaucohf/clariflix-skills/tree/v0.2.0 --skill proposta-comercial -a codex -g
```

Troque `codex` por `claude-code` ou `hermes-agent` conforme seu agente. No Claude.ai, envie o ZIP individual da release do ClariFlix. Consulte `LICENSE` e `SOURCE.md` para as condições do material.

Peça: “Crie uma proposta comercial para [cliente]. Seguem o briefing e os materiais da minha marca.” A skill extrai os dados, confirma o briefing e o sumário, prepara o HTML e verifica a exportação. Envie escopo, valores e prazos reais; campos ausentes serão perguntados.

Para exportar, resolva a pasta instalada da skill e execute:

```sh
python "<raiz-da-skill>/scripts/html2pdf.py" "<projeto>/proposta-cliente.html" --check
```

Requisitos: Python 3.8+ e Edge, Chrome ou Chromium. O script usa biblioteca padrão; `pypdf` é opcional. Fontes de internet têm fallback local. Sem exportação automática, abra o HTML e use Imprimir → Salvar como PDF, sem margens e com gráficos de fundo ativados.

Trabalhe numa cópia de `assets/template.html`; preserve a matriz instalada. Siga [SKILL.md](SKILL.md) e os checklists das referências para revisar conteúdo, marca, valores e paginação.
