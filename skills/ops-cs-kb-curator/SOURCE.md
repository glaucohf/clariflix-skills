<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-kb-curator -->
# Proveniência de KB Curator Squad

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-kb-curator`.
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
| `agents/arco.md` | `778b07b90cc11120e42efd00f8c48ec5fce67b8a121fed5bc3fa609ff90203b6` |
| `agents/clio.md` | `f52516cc9cd707fb0c48248e9da3830e6941edbc8e25a271ac0cf715871cba63` |
| `agents/kael.md` | `f63efa04d9f789ab00800ec6f9cf30c39ef77518269081c0a2bd44fbdee075fb` |
| `agents/lex-2.md` | `539f5bc5546dd35448bdc22bd8ebe1781140958e01d1f90a1509cd7c62abbeee` |
| `agents/lex.md` | `cfc5af564bf3ca436a415d5447718a27b588d421f2e129c2ef449efd93913fc8` |
| `agents/milo.md` | `9f643d6e3ae41ed594c741a85a17c5399e01173a7c5535c8ac3690060e023c62` |
| `agents/petra.md` | `3c06fe6b9fc9b201d7b55abb4fed068e368af392cc5f944fe05773ffdf9eacbc` |
| `agents/vera.md` | `0bbd5b11b24bd649f66a40c51500de3b26594fe20d62d303085b2a5e465db6ee` |
| `CHANGELOG.md` | `c2f3bc751d338f7bac41a72c42642107688b236b16a3a6b36dbedd876c12acf2` |
| `checklists/critic-lex-2.md` | `28063b4402d49a3ae5ed69463e9c93a384c0b150921c39cd1219444472219719` |
| `config/coding-standards.md` | `359b0a47316283547aa7e21ffc23e189ceb4361dfd68666d309bdacec35ad50c` |
| `config/source-tree.md` | `fd59103ae6e108c8944117c47ee62245c3fe2d644d6e68964fa1701989dfbf93` |
| `config/tech-stack.md` | `dad1a8ee3ade797503fb37d7ee5f00af83f8b9d1a853e2cdd88212280b32144e` |
| `config.yaml` | `a18a2d80dc41ab21eb3a7678a349534b4d82e9d20ee4b03d320a170295efb7aa` |
| `README.md` | `a80b337ce02b415ca6dda041607b0720f806ffdf97a8d4662eefc71ec5c0446e` |
| `squad.yaml` | `99b51ee570559840e344aac882ffc4ec77a1c31a8311f4612f943761b5730730` |
| `tasks/controlar-versao-artigo.md` | `8fef75ce1534d9eb39ec1cdaeac380dfbdf7220c7ca2137618d3755ff0df2baa` |
| `tasks/escrever-artigo-de-kb.md` | `fb768d3a4aedc3052f0cc2d3e918cdf3db329d811696312ecf973fa466462896` |
| `tasks/extrair-intencoes-nao-cobertas.md` | `5c5bf468ca70d3b0a827c127565e02f290123a73fba27d6198deeb71845fc52a` |
| `tasks/monitorar-impacto-artigos.md` | `08bc0a99e4612f5cf4c2271f92e605755b5febe7ea8793acbdec38d8b9280cb3` |
| `tasks/orquestrar-pipeline.md` | `466cbeec9cdce21c3ba38a45cc6bb1628819d03923383299b6d5930152db4bb4` |
| `tasks/validar-draft.md` | `c146021ca8491d6f06f24e33bd0efe68bccf5e32144515f1ac73bca4dbbcfe26` |
| `tasks/verificar-consistencia-documental.md` | `3d8968f04eba2fc86826cdeed5cadb302a9934a64757c8d1368b0baab8632bf4` |
| `tasks/verificar-saidas.md` | `7c0e13c989c4b968d1810ceef9638a70fd9a38fea6a04c628a986d735d706ad6` |
| `workflows/ops-cs-kb-curator-pipeline.yaml` | `4b10c3f9c9bff13f5df8790e9788e74b7e3530fa908f13e1ad5dc9f65e78157d` |
