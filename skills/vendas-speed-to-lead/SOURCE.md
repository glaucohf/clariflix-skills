<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-speed-to-lead -->
# Proveniência de Speed-to-Lead

- Origem local: `maquina-de-receita/squads-gerados/vendas-speed-to-lead`.
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
| `agents/argos.md` | `26b68342bc3ad0b494159ff905376915c03dc5f865533ac845e109ee9e94a79f` |
| `agents/atlas.md` | `ba0a7de6244207bf4a0eae2b22ff9f8dc70195df3fb24bac4105eb335d901277` |
| `agents/claude-opus.md` | `2ab955b11d9cc6e47de68df20302fc16d6edb498acf0073044c106dd7b3b0509` |
| `agents/eco.md` | `accde79bee3f3bb5b403a9db4fde4750322e2aabab4e60e804baf5866a1489c3` |
| `agents/flash.md` | `049838177f7d2529f706e8826818b648ab5d57764ff55947fe1980420cb8a3b1` |
| `agents/sdr-por-ligacao.md` | `d37143655617b014b25dbaa4dcc8348fd56ae5ece24f45bb72ce8f97485aebea` |
| `agents/sentinel.md` | `984632ff9a9634a041b88270bdb28934aca699f65d2843a39187619cdd082353` |
| `agents/sherlock.md` | `b1dd514cd38ef1522763bec20281a386e303d6b8e624e3aab013d47b38996707` |
| `agents/socrates.md` | `f303252c61462ad4047b0e9bd407aa793073702bc2b6e37e0ff957537e54ce64` |
| `CHANGELOG.md` | `cf92d3b6d63cddcd8a4ad97ea22f3ed83b3d61cf9b6fd83d46f801803b0db7d5` |
| `checklists/critic-sentinel.md` | `6fcb723a04df44fabec6ea599b818ef3854ace52a863eb5385eb1f5f8ceb2405` |
| `config/coding-standards.md` | `e95ea625027a6159609bac14a3aded248544d2c60ffbdbbd946646d982c979fa` |
| `config/source-tree.md` | `50693bd5790f3d18a0f6782bc7c1f8019079f1b1a48acbb680d5a9e02b40cd81` |
| `config/tech-stack.md` | `b7deb562f885ab214b4ca40fe9388e11a05569f83c3729654cb3fe6d4800b4dd` |
| `config.yaml` | `0e788a7d3031a458d6093704ff6424b08d1430d65860c8c691ed88c17a671d3f` |
| `README.md` | `c89e2c3480f81d9a87e6539735325b97597b0016a9e23ab8804c424a6fed6e2e` |
| `squad.yaml` | `8da5f436065eb6baa35f0adfd8df5be573f2f8bba06a00ba9980fe91eb2603f6` |
| `tasks/agendar-reuniao.md` | `abecc9994ba3c0adcbe97a7f5ff134c257041809dc59e6bbb4054b0f3dd210de` |
| `tasks/enriquecer-dossie-lead.md` | `dc4bd776b6814dca467566a622c7a68e5d3df951ea0204a86a18472e1e866519` |
| `tasks/enviar-primeira-resposta-ao-lead.md` | `de9ba754fd4026bc7743c17e648cd5ea2af5816a17b9303eafb8e109a1bc7cdd` |
| `tasks/gerenciar-cadencias-de-follow-up.md` | `63e1a53b9b8e5981d63373b9fc6f2a0359ab60048ad98c53f98508aaab98a48e` |
| `tasks/orquestrar-pipeline.md` | `c38cf3cd20d29f108f73aaa2cf098bd3f50e699722828bd5814b41e4dd44ebba` |
| `tasks/priorizar-leads.md` | `952fc9bd4ccee777264405a31a33528c25f5f1200c460e9c544266c0bf0870a7` |
| `tasks/qualificar-lead-conversacionalmente.md` | `b2640f82da9fdca27feb799f73d24a6ac7616e2fb5380f57c82da517f0e6b2b3` |
| `tasks/realizar-ligacao-qualificadora.md` | `d1cecc45d387a1c0da9b7cc86abfa0e5c8c57a0d423438912632a601f0d0088a` |
| `tasks/verificar-saidas.md` | `87b2ba64d230fa4822a90543217262a56ea2d6afe33d10d0059f363a83a019d3` |
| `workflows/vendas-speed-to-lead-pipeline.yaml` | `70eace7215639e7aed99a33ccf642462a3192902369f9e82db3b404ec11ae257` |
