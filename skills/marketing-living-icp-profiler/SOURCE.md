<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/marketing-living-icp-profiler -->
# Proveniência de Living ICP Profiler

- Origem local: `maquina-de-receita/squads-gerados/marketing-living-icp-profiler`.
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
| `agents/atlas.md` | `a4600e4167469116f3c94881d956457f687b6365e79c8b48e330322cbdfc2722` |
| `agents/iris.md` | `9ea937aa47ef96fbf98d62c40f60d22231dd38d0e4b3220fd8c2ed289f08afbd` |
| `agents/maestro.md` | `edffa4f983947262faec40e563349efb5116042fafe52d22f21f1925fb138050` |
| `agents/nox.md` | `776653860cd3f646a17283543363d5ae36f5c470025ea607b8926ab5de40bfdc` |
| `agents/rex.md` | `860d920691c02ba25defbc31a8af89e2cce148f1a633c0faacdaf0761e921fe3` |
| `agents/vera-2.md` | `7d290a06d8bf845e75b2364a8b407dddc7d714caee3f6cf0794100d612c4cfa5` |
| `agents/vera.md` | `b602e825ead14e0cd566a7ebcbd7c814468169b7877350c6877d69a657513345` |
| `agents/zara.md` | `02a7ada9483a2c5faba9d1f4db809d7caf6ad9b878f4bed5979a9b2167a883bc` |
| `CHANGELOG.md` | `b196ffbe5b64d9bdc531844c93f794d3aa04977200e7f63e2d2979a58d6cdfaf` |
| `checklists/critic-vera-2.md` | `1113f08744e500e4a7587c847e9c3059470ea85022ef8bdcd0ddc41cb929972b` |
| `config/coding-standards.md` | `0ce696cc35bf8ef390ddc7884d1f06d1172b33d4c2518d3e2870c17fefbc673f` |
| `config/source-tree.md` | `73bff857dd92326c2d537c4d6a68da59bd04dc65e26dcd39cf11ad939e3f3749` |
| `config/tech-stack.md` | `2a53234675132235d9eba84ccf6e7d0d947247b07fdc6b213300b2a64fbb2672` |
| `config.yaml` | `447df326d0891f92b747abd750e36a1337059d21713ec15c23cd97fb85ff36ff` |
| `README.md` | `0e509890495b767551e7eccfb455eae96a20a28d1f26d7a0afe73704ce4b2f3b` |
| `squad.yaml` | `43f0f479dfc36d0f0737f56e7317e45674d718c84609d3a650ac57bc28633da1` |
| `tasks/calcular-icp-score.md` | `be710fc9a982e860b57a00a9863deeca7d696b492cd22a7b3a82fd4ee954119d` |
| `tasks/calibrar-icp-com-dados-de-mercado.md` | `f0ce458243f2a4e2d7a7227ce582adeb877866e17b643e88a5419831347c9434` |
| `tasks/construir-personas-calibradas.md` | `70a2d472552efcbb7f7f2cd33ccdf25e83028275b321cfff3474187f1d0d86de` |
| `tasks/enriquecer-dados-lead.md` | `be9b680893f0fb0cd886a46406107b6c73d7f7ee5d5bbdf86b37a59e86a40583` |
| `tasks/monitorar-sinais-de-compra.md` | `652029e7420f4aaf0202af2a2f708d06ec2e1e3f5bbe5ba237972998df2e2667` |
| `tasks/orquestrar-pipeline.md` | `24212e83c5c35f00e654d666e34da06b389ee6faf4786340419f40a213becdde` |
| `tasks/verificar-qualidade-de-dados.md` | `bdaa17aef520ccb29da9317b4353ff8352ff45c19fdf098fcc2578ade31baf59` |
| `tasks/verificar-saidas.md` | `260dd03f7ea501a8aaa123dc5dd9d2d20679499502b928886d74ef904edf19f1` |
| `workflows/marketing-living-icp-profiler-pipeline.yaml` | `4063e7c9a4b07d186d0326fe02b8177d02836188ff050f444f2338fe4b03d62b` |
