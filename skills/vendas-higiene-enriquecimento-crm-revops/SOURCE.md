<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-higiene-enriquecimento-crm-revops -->
# Proveniência de Higiene e Enriquecimento de CRM

- Origem local: `maquina-de-receita/squads-gerados/vendas-higiene-enriquecimento-crm-revops`.
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
| `agents/cassandra.md` | `84deeb0a0c7020127ae08ddb577f4ca3b258266ce5411bfc9af7d32a82b1c6a9` |
| `agents/detector-de-duplicatas.md` | `96f67d742b3b8a84b5a4579828cf61efcf5b1ef60f74ee42d86bdf67c47103fa` |
| `agents/enriquecedor-de-conta-e-lead.md` | `0d52c1e4306138d314d5ec99032bd3aab13644438f16ceb92f245963c54eaea3` |
| `agents/gerador-de-golden-record.md` | `effb3bb37fcf36323a52ce6c55dbb9ba9d3166c24a2bcaf7ae312db6e6c408dc` |
| `agents/nexus.md` | `3f8e70d69dbac8516866837c290b2d54e32a8a494ba8cb0846fb02e956f49fe3` |
| `agents/pythia.md` | `e5fa9a62f81333c789ce5beae004bf8b663f1c79577554a22d8801d4682b4022` |
| `agents/sentinel.md` | `7ba600de9892f6f421c4090dd114ab9ed801a9c3421cf9ab48283c45347ee4d3` |
| `agents/sincronizador-de-fontes.md` | `10129fdea4c5b5b1919039a9247cad08023b075efba2d4dcf9c685bfb4207069` |
| `agents/validador-de-entradas.md` | `a526dea8b2da1f70b4ed2906d7db7ce215a8112277c3c30517ba408f860dfb91` |
| `CHANGELOG.md` | `1d6168f366d3b3dc0050a67bbcafa6a991c961ea623a9e1fbf1a53098e991dc8` |
| `checklists/critic-sentinel.md` | `c3de3bdf5a34e0fb7a074688fda2453be07f687125e569310e8c3ca167b31f41` |
| `config/coding-standards.md` | `e95ea625027a6159609bac14a3aded248544d2c60ffbdbbd946646d982c979fa` |
| `config/source-tree.md` | `1a54450479a755a5d748eb7fde8727c0c704e7b9f78cc78b37709f534b263f9d` |
| `config/tech-stack.md` | `5907e3b7572060ba8646369bc1f2bd23187c3c5dd6f3dd9413c387e1a2ac6a32` |
| `config.yaml` | `9424428fcd8c00e8d912a4b4d37b205330b7ca12f0adb5c5936d4ac80b90ad19` |
| `README.md` | `6459b8e76f3a57a94b599110c1b418b3f9b16b4451e4d84d00ac4421f0201d3a` |
| `squad.yaml` | `a4dcfd84355806a22613a491046ef37ef25783b3d02570da18f5a91499f0f871` |
| `tasks/calcular-score-registro.md` | `d093fb6ddb9a0126b339bcdbb96e280d65aec1478362cf7ec5a560cb62542859` |
| `tasks/consultar-fontes-confianca.md` | `c176ef5c9fe3cf05f362adb9f02e4235bc8d28b5ea701e3faf2f2efff7f62ebd` |
| `tasks/detectar-duplicatas.md` | `765068c921d6072c084cfd60de4526afb1d530cf43d5aedab8b2d70fd68f61da` |
| `tasks/detectar-sinais-de-intencao.md` | `aa32dbd371f85bfc4447065ecd5462415c37b9d68f475c1d3cab8e799cd2aa00` |
| `tasks/gerar-golden-record.md` | `374a1f4f6a967c5ffba38534ea97c452f4038b426181a9bed3256d9aa4faf288` |
| `tasks/orquestrar-pipeline.md` | `929e010ee76e9898d5e86319787662d74c08a6779d6f6e32f541e843d8c6ad3c` |
| `tasks/propagar-atualizacoes-fonte.md` | `c645f469b4144007680d16c9ad4fc5753e5aa32665b590ca575ef3bceff57559` |
| `tasks/validar-formato-de-entradas.md` | `6f583cf0bb8eadc6e78c14d714dcddb09fccbed55832f4b6d2a295112cdfe2f5` |
| `tasks/verificar-saidas.md` | `e20d8fcd8d18456a37f1abb44dcab4d057e82d83e20ffe422edceb34c690cdc7` |
| `workflows/vendas-higiene-enriquecimento-crm-revops-pipeline.yaml` | `bca1506ccb90b74a2171e360cd8e58bffa02ca0a3d57a9e4c7a5e42f8fe65308` |
