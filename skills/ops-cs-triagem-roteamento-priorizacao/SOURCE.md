<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-triagem-roteamento-priorizacao -->
# Proveniência de Triagem, Roteamento e Priorização de Tickets

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-triagem-roteamento-priorizacao`.
- Repositório de origem: https://github.com/educacional-lendario/maquina-de-receita .
- Especificação: Máquina de Receita · Organograma da Máquina (Gabriel Marcondes).
- Autoria declarada: Gerado da especificação de Gabriel Marcondes (Máquina de Receita · A Máquina) pela Academia Lendária.
- Versão original: 0.1.0; geração original: 2026-09-16.
- Adaptação para ClariFlix: 0.2.0, em 2026-09-18.
- A inclusão no repositório ClariFlix foi autorizada pelo mantenedor em 2026-09-18, que confirmou possuir autorização dos autores para publicação. Essa declaração não altera os direitos de terceiros nem concede nova licença sobre o material original.

## Licença e restrição de origem

O manifesto original declara `Proprietary`. A restrição fornecida com o material é preservada:

> Material da turma, para uso próprio e nos seus projetos, sem republicação em canais abertos

Consulte [LICENSE](LICENSE). A licença geral MIT do catálogo não substitui a licença deste pacote.

## Adaptação e limites

`SKILL.md` e `manifest.yaml` adicionam entrada instalável, descrição de capacidade, roteamento dos papéis e execução sequencial quando não houver runtime multiagente. Todos os arquivos originais estão copiados sem alteração de bytes em `references/squad/`. Somente caches Python/de ferramentas são ignorados, se existirem.

Os caminhos e links históricos internos do snapshot continuam como na fonte; referências a `../../squads-gratuitos/` ou ao workspace do autor não indicam dependências instaladas. O ponto de entrada da adaptação liga diretamente aos recursos presentes neste pacote. Integrações externas, ativação AIOX, observabilidade e resultados operacionais não são provisionados pelo importador.

## Reproduzir e conferir

No checkout do catálogo, use `python scripts/import_generated_squads.py --source-root /caminho/maquina-de-receita`. Acrescente `--check` para comparar os pacotes sem escrever arquivos. O importador recusa diretórios de destino não gerenciados por ele.

## Integridade dos arquivos originais

25 arquivos preservados. Hashes SHA-256 calculados sobre os bytes originais:

| Arquivo em references/squad | SHA-256 |
|---|---|
| `agents/auditor-de-roteamento.md` | `1633e40f1bf3f3db22968bbda8eb9b426cfb11aebba8b106c2bec275c918b1ef` |
| `agents/bela.md` | `59be0a53b0f09e7ad6ab68c98227a2b22e569d45e14fc767d58d9af692ca4070` |
| `agents/dante.md` | `1a58e908da0e427d509c31542e3de0ed78a88cd2bda6c6f374e50157c9027df3` |
| `agents/enzo.md` | `a9238ddc87d5bf03e24620dccc06a11387d9238ba02b3d53ba1c88d796065fd1` |
| `agents/faq-l0.md` | `235b4409600a1cb77a6b6adc2996b51df2c08979e3c86fd93433cc8e00941e74` |
| `agents/lara.md` | `dc0a18a95deb3c8160e0334cba817940510c28ec78a2338418dd8f63a00cf2a5` |
| `agents/rex.md` | `504c103d305dab431dd7bdae8e3ae3be0a0de498b657cbf6fdda73c291b36dbd` |
| `agents/triador-mor.md` | `3a29a7b21798ea3a43ce66c5a1f34fb5edb413d9b494a647233b4692af732873` |
| `CHANGELOG.md` | `b9e5353426b502a1a1a29035563099a6ec1a2f90e7bb17979effb2503c7411dc` |
| `checklists/critic-auditor-de-roteamento.md` | `8caae763af1a7d77eadc3e613ec8459fe71fc7adf8ae1add252ef21bb054ca71` |
| `config/coding-standards.md` | `c9febcc2dc9fba17a32ecbf5ee65d72200f403cd653930aaaf0f4c088722757f` |
| `config/source-tree.md` | `c9ebd3a8e90fd2f6cb9e34cd2e6a8efdfb0490a56f8bd47641fb973306532e08` |
| `config/tech-stack.md` | `7e63f08e8e939c7eebf1d7cb8dd0ed21a9c90c2d673bf724498bac1bda575f18` |
| `config.yaml` | `95e83d6b40c27c3c833d82f28d0f9df4fc11fd97f8d9fd4b319455cab9b487ab` |
| `README.md` | `7b51656e26c43c25ccac2fa691a6f11c5c9d43c603923c1e8e2e66c774443cd2` |
| `squad.yaml` | `c2f7ad08816382b8787946fc12d30185532ed1588ac2196292249e0c244895c2` |
| `tasks/autoresponder-consultas.md` | `837696ffad334149e87d56c19371b2fe90dd9db3905a7fcb1bf60edd5cd7d43d` |
| `tasks/classificar-intencao.md` | `f183a97805b4be7664f68dc138ea40cdd0cf197dd6c024b2889af5ba79d40be2` |
| `tasks/classificar-prioridade-ticket.md` | `19ad399e3b0ef21d29aa49f226f60d2658216dd8360c8e4885dd1f5e3addafd8` |
| `tasks/detectar-e-agrupar-duplicatas.md` | `a4ea2e49cfadd07f1a9eff63f84152bae5cba480ab82c7fb7419343d8f7f5020` |
| `tasks/enriquecer-contexto-cliente.md` | `6f72b4bbfbe168400e44eecb9809756bfe0127ceff3d4c96acf68ce00061c163` |
| `tasks/orquestrar-pipeline.md` | `475d05046dadb183ca9afc6a46306415857ca4b1817b0927bcd5e0befa45e7a8` |
| `tasks/selecionar-fila-destino.md` | `fd5e1c7f42100d66a769c83d81be5c8b808cc59d481f796728d630274b78b8c5` |
| `tasks/verificar-saidas.md` | `8fd2756fcb8ef973c60e286df37fa2af33af6ea5c690d4a1357e4d3409309907` |
| `workflows/ops-cs-triagem-roteamento-priorizacao-pipeline.yaml` | `89f56507c1c528265f923091899db2cdc8e42ffad5751ef9fd2d962e52ebc0bd` |
