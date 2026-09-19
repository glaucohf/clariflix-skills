<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/founder-strategic-foresight-wargaming -->
# Proveniência de Strategic Foresight & Wargaming

- Origem local: `maquina-de-receita/squads-gerados/founder-strategic-foresight-wargaming`.
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
| `agents/ajax.md` | `d4652652c0ab108cc4eceb73c812c63903fd6872190c243bd9d58cf992afaf0e` |
| `agents/atlas.md` | `a4f7d953faea122ae0a5d0dfaeafc788752dd86f4b4617664e9330047ba8f538` |
| `agents/brutus.md` | `ae5299555a070185fccc0a78d6428f2b74a75a15d94454038ecc479de017d248` |
| `agents/cassandra.md` | `ccc97c45910c0a7c4bac690bf05cd92fa3041182dd642980289075929723f6e6` |
| `agents/chisel.md` | `ed8131235f5ea669a618ed327c8675592e1642aa102c7029a58f72a757493ada` |
| `agents/memo.md` | `518d958d83f1082a46255ec877e436592d44d398e1877e99732c9083912328b9` |
| `agents/pythia.md` | `b9f97caf750a9819093d5da0a7083568a2b45c51664f632afdd6d4517fe69c13` |
| `agents/tripwire.md` | `83c9eec4663c4bb4d08a78f89be3d6457f88e463ca3021d5ab23e9cf16a37fd3` |
| `CHANGELOG.md` | `203684c2a79c8759d469ca5737fa284ace0c1e86ad4f41315f8a81899bf5e132` |
| `checklists/critic-ajax.md` | `4ca47e32a01ebb9bf82d821e614ce101b301863df53591370ede333f4dab45b0` |
| `config/coding-standards.md` | `e497e1f58633e744793b38456aa89de2ecfb11220ccb1a4813d8e6120379a2cf` |
| `config/source-tree.md` | `b970ba53f9f82492e5491737a1e06478bc90a57f3a5580b3a5e759415a5798af` |
| `config/tech-stack.md` | `e5712fc703f6374e6dc7e08c5884b2c4d623c47b53b739c2700cc1f768c403d6` |
| `config.yaml` | `63306fb181930c3eca6c23819ee274d0c9860912049ebe07de67d86d7db38bd5` |
| `README.md` | `75a36d88ab9f8aeaf23d75f2ecf63656f934e6cb66c401f19046c24fc86285d6` |
| `squad.yaml` | `12d39b8a9c7a06f4a64892f74ee2a4070b8363bd93354125e01f56b20a87c253` |
| `tasks/coletar-sinais-fracos.md` | `e95cf8fbc40717971321040d4d7d1eff25d22ab9cd119d72bd78f1fb93e766da` |
| `tasks/destruir-premissas.md` | `5c56d269df5deafd82e762d20a630053a1f0780ee023951a35a42f9e33d688a7` |
| `tasks/mapear-espaco-de-futuros.md` | `0b4f787b8c2012f22edecc66499368e0d46a54c772eb72891c785ce2f0aa66b4` |
| `tasks/monitorar-indicadores-de-alerta.md` | `6c2fee5c4a5baf7363ce9704c74dabb430113ef4a0dd4951f76c2242eb085447` |
| `tasks/orquestrar-pipeline.md` | `8b5b16d39cac1cf7d80c082a53250fff91b79d1a861890205cfece20f6e691b9` |
| `tasks/simular-reacoes-adversarias.md` | `7936aa3e4f3924ff0ec41687394b209331f49bd29a6d3b140755d5b7577a2b58` |
| `tasks/sintetizar-wargaming-report.md` | `4044546acc516e4f5f74bf2118800d0df30859f448324dcc26d6d9e989ac5b38` |
| `tasks/verificar-saidas.md` | `51841451b76db1ead5897bfa4ad53a4e30bf5bf2de7813c00dd797044e2e5b2d` |
| `workflows/founder-strategic-foresight-wargaming-pipeline.yaml` | `10a0f257ad4da40af9217af50ff19341d72967cd47144e84001a28b345f2a3a4` |
