<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-tier1-resolver-multicanal -->
# Proveniência de Suporte Conversacional Multicanal

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-tier1-resolver-multicanal`.
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
| `agents/argus.md` | `2f96f86bab2282bcdb1ea067b01682098cd2474dafb33a5612f3a6235de915b9` |
| `agents/flux.md` | `bcf9145b884a6af9bc67cd652eea56c9d84f93c673954d3acb5461b0c03be3e6` |
| `agents/hermes.md` | `7662613af217c72c8c2149d1316284d770d344bbdb1258d81f56acdb71eac66f` |
| `agents/nexus.md` | `9a0dff64973cbf63be3d74631d9991ad492336fdffcfa865ee8d3092292f5d25` |
| `agents/prism.md` | `bbd8c6115dc18b4346942a026eab5e124075f28b26a66b356617f4c4b31b84b7` |
| `agents/pulse.md` | `602be99d77b9a7169035f2d034afa3bdb3783e47c4153781bf5070c3d91a34bf` |
| `agents/sage.md` | `077556051493621c3dff876bfb0762809e672d5f314a8ee5d5570a74f30d3969` |
| `agents/volta.md` | `ba9457b147953b36a7bf4a04406503b0e38190fe72bec48e045b494074a2d98e` |
| `agents/vox.md` | `6c8acb2e4b6c2f589c733ddd556c48afcd83e9604dcd661e7bd1b97f11a9dbdc` |
| `CHANGELOG.md` | `81d6f2c69a7f85579797825c47c185207d36b9ed1d688780e02d59b7977ee0fe` |
| `checklists/critic-argus.md` | `b65f07f6c04495e7ab3dbfa2cfccf2068341994f0f093312b8e4622c46b62398` |
| `config/coding-standards.md` | `2f9dd7750ba69ba26ab1aa5ed7e648be7989291134d8cecccfb6f6677c856104` |
| `config/source-tree.md` | `2a523551b8098a647ed06fe63f19a134723fab702561fc3b4ef498940721221a` |
| `config/tech-stack.md` | `56df0c9be15912836f05760925787f11d995e15376106d75018f902b7ff5a2cc` |
| `config.yaml` | `abd2f7026e4da7395f05b0e7473ea9dc53117169f800ede5c41778033df5394a` |
| `README.md` | `c478bc2f16483f2e285deed76d643b7aa6e1b78fcf3c0223d0cc718212f303c3` |
| `squad.yaml` | `5f9d827e236c0e7d28b0fa28aaf09c1b19bb5a7c89ce565f09a55cd880d239d7` |
| `tasks/consultar-status-de-pedido.md` | `6d15b2f86a2ae490448c674d7a55978db9c15341319c627c6550911de529c9f2` |
| `tasks/gerenciar-escalonamento.md` | `891218e8f57f802cd3f5fd51811a855d3e2419b2f22f0c15a27d71949729c71e` |
| `tasks/monitorar-sinais-de-churn.md` | `a7258ff748ecc1320510104a621215d1d42e77aa885af6a6263e3157d093c8d6` |
| `tasks/orquestrar-pipeline.md` | `dc3a961400f42c751bcd6ba5e50caaf9c7aa652b72e60514edd5ebbfe6e93fc3` |
| `tasks/processar-audio-voz.md` | `88ab9ddf55a6d023e9fcaeb20c66c6e7ff0b66ddcb0cd8f955b9984c73c2f2e8` |
| `tasks/processar-refund-e-cobranca.md` | `9a2506c8104ba53858d00702ffe4009fcce7eaf6b733fa98501fb8037d63f4c8` |
| `tasks/processar-troca-e-devolucao.md` | `8f25fe9f1dbd6049fe4df81c2f04e422c233f6907b4705d0e9383c80d2b9bb65` |
| `tasks/responder-perguntas-frequentes.md` | `4a13e0b617050d1be51770297a998ff0640895f534485aa4fd04391a982587aa` |
| `tasks/verificar-saidas.md` | `f844f4cb91732b7f28a498966e9614dc4e3b812eef8479ef601b58a14e638f9e` |
| `workflows/ops-cs-tier1-resolver-multicanal-pipeline.yaml` | `7e7bcd4fd29d6d11cb6a1411582cdc53e36893b3eee99d2bff4fb8870ea88245` |
