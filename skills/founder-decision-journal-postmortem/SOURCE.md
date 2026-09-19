<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/founder-decision-journal-postmortem -->
# Proveniência de Decision Journal & Postmortem

- Origem local: `maquina-de-receita/squads-gerados/founder-decision-journal-postmortem`.
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

27 arquivos preservados. Hashes SHA-256 calculados sobre os bytes originais:

| Arquivo em references/squad | SHA-256 |
|---|---|
| `agents/archivist.md` | `6b50566ff741c225a8165d5ee30d75950181f9b4116e33dcb30aa47fa706140f` |
| `agents/calibrador.md` | `0a8a48f86d970892e7c24ba7b84e2342f6e67235058ae2064c40a19309591f6f` |
| `agents/mirror.md` | `dbef7cdf1ff282f73878ca1188abd89bbbcb214f7e75eebb3261a41396e80c55` |
| `agents/oracle.md` | `7a492718cb08300d550528d5292dfd522e26d5cdd95b790a050c8e6835566862` |
| `agents/radar.md` | `915713966dde6214c64c9900e999404af9d540a893d3ec85bd5da0fbc8c22385` |
| `agents/scout.md` | `8c9f979627ca914291c0c75ad16fd0ddd19c076712150e2766b2c7e0e36aca83` |
| `agents/sentinel-dj.md` | `6856f638ca1eb4c46a6606ced2f9d266927341e25f364a26d6859f1f05fc54dd` |
| `agents/skeptic.md` | `9365d640adaff4afb58aa7f8a008f3077c951572a044688076161ef68ce49f4e` |
| `agents/verdict.md` | `78eee7d717680526439fb3ea5c9f6aa638e8650a0ce614c3c0de7bb7b5a18b09` |
| `CHANGELOG.md` | `df11d743b13ba506181344342b64d0776227affe6383983158afd85d1494908e` |
| `checklists/critic-mirror.md` | `b5d86d6de521cf71643db1122ff04a2485971fabb54d116f0bbec0b1848fc1f3` |
| `config/coding-standards.md` | `e60b246487e0baf20c324359eb621dd309101c35feaf71da1e8881f700a0dc4e` |
| `config/source-tree.md` | `c310643226431d18c8e1b81850d8fc9f435986aa411f3428668b6fa2baab1b32` |
| `config/tech-stack.md` | `b05cfee6d00fdce15717d6d4ad51a1810521bb5775be5a1e10b4f6a1becfb957` |
| `config.yaml` | `61d89b6bdaaf8ec646e9a8a95b3bfe81a597669b415876c44451547a6b3f35b3` |
| `README.md` | `0c8be412ddf7efd48aa435f6463e6bfaaa12f93d089008a285319c28ffa686f8` |
| `squad.yaml` | `3d89643604472da22cb66847fe0c005a7e481cd074a01169de20e29ddb6d6823` |
| `tasks/analisar-decisoes-postmortem.md` | `13269710fc9fb5258655eaadc39c05c1438a0f28cb334d0f43adb91397456641` |
| `tasks/calibrar-julgamento.md` | `70a8dc2800a39201e80596b2bf2f111ad98e02aff5a5da035ab78b5f8180b570` |
| `tasks/capturar-decisoes.md` | `a9f7bd28717ed909b9d7e37ad7021fb7f0bf6b0a0ea2540d7925725a63339638` |
| `tasks/desafiar-premissas-declarativas.md` | `e4238c0f782a6085631de9cd285fe1c7acde1bcd5024d58b374fe15019083b3b` |
| `tasks/monitorar-premissas-decisoes.md` | `45d295bfd36a20b9d6a2641606145b730d9c27b899c500e8dc689d0e237e6dca` |
| `tasks/orquestrar-pipeline.md` | `0d53ede687be80969d9f7f80c6e279136ca8552aec93d38b7ee285777d7d4bcb` |
| `tasks/pesquisar-dados-referenciais.md` | `00f5868ba6b3ab27020e8963f5ba7f2af0c06571312ba1c4c9c1d9757a5af061` |
| `tasks/verificar-integridade-temporal.md` | `433beff92b486232fa5a5028ed1304f9d43372777c9d0ae742c7fec70bc91fba` |
| `tasks/verificar-saidas.md` | `bbf5cfc1377c899314cdc17657b9af1989166114fe098997ad6e89ba38446729` |
| `workflows/founder-decision-journal-postmortem-pipeline.yaml` | `e15a9a8dfb1c99ed230a25f897585b570179e8ddb1286123d1dd0438f1475967` |
