# Origem e adaptação

<!-- Managed by clariflix-skills/scripts/import_free_squads.py -->

- Origem local: `maquina-de-receita/squads-gratuitos/brainstormind`.
- Origem anterior, conforme o README do acervo: Registro https://squads.sh, slug `brainstormind`, cópia em 2026-09-16; proveniência detalhada no README arquivado.
- Autor declarado no pacote: Brain Squad.
- Versão original: 1.0.0; adaptação ClariFlix: 0.2.0.
- Licença original: `MIT`. O squad declara `MIT` em seu manifesto original.
- Em 2026-09-18, o mantenedor informou possuir autorização dos autores para publicar todos os squads no ClariFlix. Essa autorização informada não é uma mudança de licença nem concede automaticamente novos direitos aos instaladores.

A adaptação acrescenta `SKILL.md` e `manifest.yaml`, roteamento por domínio, execução sequencial quando não há subagentes e limites para evidências, ferramentas e ações externas. O conteúdo original completo está em [references/squad/](references/squad/), com hashes SHA-256 em [references/source-inventory.json](references/source-inventory.json).

O [README original de proveniência](references/UPSTREAM-PROVENANCE.md) também foi preservado. Ele contém uma inconsistência de contagem: diz “doze declaram MIT”, mas a lista tem onze MIT, um Commercial e um sem licença. Esta adaptação usa os metadados de cada `squad.yaml` e não corrige o arquivo histórico.

## Limitações conhecidas

- Os arquivos originais foram preservados sem alteração; comandos e dependências AIOS não são instalados nem executados pelo ClariFlix.

## Reprodução

Na raiz do repositório, execute `python scripts/import_free_squads.py --source-root <pasta-maquina-de-receita>`. Para verificar sem alterar arquivos, acrescente `--check`. O importador recusa destinos que não gerencia e valida referências diretas e integridade da cópia; ele não executa squads nem verifica suas alegações de desempenho.
