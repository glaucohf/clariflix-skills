<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-self-healing-etl -->
# Proveniência de Self-Healing ETL Squad

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-self-healing-etl`.
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
| `agents/argus.md` | `df21c65049a6bbc9d37461fb5145ee8e69958ec32554f86706f717e0dae1757b` |
| `agents/coda.md` | `dad748c2a05b92234d3fafea977289eec8ec0629e6417ca7092374ebb04a4e95` |
| `agents/finn.md` | `7dbffec63bd514b202e79412b5e7c5de008d7e7824aa8e95bc7b8ab77e46f8fd` |
| `agents/loki.md` | `39b9f87e8f37b0c0239a6d185972a13920e38909c3ce251dbbecad03aff7aae9` |
| `agents/nexus.md` | `2bc8c22d2bd1854a80003193f7cd165dbc1115ff90474b6b986f55c267bc3627` |
| `agents/orion.md` | `5a6f19173873bd61f52de56aff9b617d52764137a8456458e081ed7f02c7ab82` |
| `agents/remi.md` | `cdef3a3f762869ef974b137921ae2a60c19a6162e58dad5219b16b06547cec8c` |
| `agents/vega-2.md` | `61c2fe39b4650a25b861ccb5b93945e5cddb4aa63edf30eab501fb5f268e8dba` |
| `agents/vega.md` | `960d9e74a29423d73026db65b733be87e020c099051a334cb7966f3b455fb805` |
| `CHANGELOG.md` | `7fb581e2d1d56fe8c33cdcf275b934b68138096badf98475518b3634c1dca9d0` |
| `checklists/critic-vega-2.md` | `61618cf5a1f22da038164a184ec94e38089cb8f811c323ed310fb6299bfcf849` |
| `config/coding-standards.md` | `d6254519d3336bc2e175ffaecae4945a6c6cac15fb6b56b24237bc9c5fb31d9f` |
| `config/source-tree.md` | `68b14d1369291c1961c9d3352a56934a349fae80aa1261ca6f618092f77da841` |
| `config/tech-stack.md` | `f2483a4b3eb7bffe6df4b371ab60e5ec421fce1ae172ea4930320d9bf8a5f61a` |
| `config.yaml` | `233365fc7265ccaf5a4a56fa943d90b57f42ced4b8c0b39bb8f7b48f54ec2f1c` |
| `README.md` | `28aeb3e66480b49b1d7428e6e5bf6464940f14bfd6d422cd63ffd45696ab196a` |
| `squad.yaml` | `4d82d1eef3c42535a7f58497d3c6c868c1537dd3ae5298d11d843d3af046458e` |
| `tasks/calibrar-thresholds-baseline.md` | `3cc25d6eb1a7f38207b60e1bf30dcb2629ad2ec70d9a8510866fb3e8df39bd73` |
| `tasks/curar-falhas-reversiveis.md` | `ca20d4137f197f76a571df17daae3290b484703f891a3b490ba07938ad926d9b` |
| `tasks/documentar-incidente.md` | `40f3d0789a759974e20cdf3f488546d15ff75a7cb43d28c060907981c78a3b9f` |
| `tasks/gerar-plano-de-remediacao.md` | `c24c370a3ebe9ac7c0a3797bf65467e1010fc8fdda500797703747f5b6cfd614` |
| `tasks/monitorar-pipelines.md` | `e1307e881d241dcb6bf0f4df50f0f8855f220fb219a14a4f228ad9a7b3b1e797` |
| `tasks/orquestrar-pipeline.md` | `f2ab3fbb5fd5ae160a1787919900a1e824bf6c785bd20737b9b471bdd5f2f601` |
| `tasks/testar-hipoteses-sequenciais.md` | `0e5f807787e24a18b4aa3ed4b1c1902d92d1433fdef3f4c45b9c76d228abdbbb` |
| `tasks/verificar-acoes-automaticas.md` | `a2b020854635174956f49456e8534e87470805cdec73443338f0ddb624bf6be2` |
| `tasks/verificar-saidas.md` | `49abd536ceda309d836fa43e54a251e1a44d542879ce39854653edfa5745d259` |
| `workflows/ops-cs-self-healing-etl-pipeline.yaml` | `0f744a49310c8e1dd712b274fb7ca86d051e74bdbc4be87ce4ef8aeb437b5d5d` |
