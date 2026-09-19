<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-ai-sre-incident -->
# Proveniência de AI SRE

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-ai-sre-incident`.
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
| `agents/alert-correlator.md` | `fc4da1eddb3682e1145255d4e498283bda9e93a03bcf9577dd5c7c3f8e1b79a7` |
| `agents/fix-executor.md` | `454208c0ede686564c88415ac6a902005ea5c06d907d58cb5daa42b0067003a0` |
| `agents/fix-guardian.md` | `5d17b62a03204a4863638d03c1084c3aadc1fe575f45072a56e2dff157d98127` |
| `agents/fix-proposer.md` | `f88a71047699730a7fb2b7fa66642773501c64d9c9cf836916d5b47578c48f13` |
| `agents/ic.md` | `3fe00b1c6c9ff49835bc01df6a8262e971a87e058688e969c683c2815ca963f0` |
| `agents/incident-communicator.md` | `7ba3ff8ac7db23e57d04dea946a529c300633585dc3616e952116e578521d1e7` |
| `agents/post-mortem-writer.md` | `cffecd426eb4fc3501f80043330198c1c05cae1a0348e9c16a54cca2972b74c8` |
| `agents/root-cause-investigator.md` | `0f697cec8cfebc8dc1987edae3df45d1bde08bd3a008a02f678c26d19b3cd5fa` |
| `CHANGELOG.md` | `473a0aea7e36f8458b28d84a44dae6c6a4922f77a87e4a9fa1288679c023546b` |
| `checklists/critic-fix-guardian.md` | `cc3e6122970cdfe6f3f6d2bdf1be4485a83e426536a05fddd537d268a1eee781` |
| `config/coding-standards.md` | `5590b6e862b46985fc0ab45cf823fb7fedc411332c2d13c036d5838fb1a337ba` |
| `config/source-tree.md` | `30f324bef0917a67d9db0e2800226c61cb7bfb3f88eaa1fac44e7762db67419e` |
| `config/tech-stack.md` | `aae1d4c625d54d982ef2ef0721aa0c501f0224903aa15c75990b9e48d6cff88d` |
| `config.yaml` | `75beb0651fd001d607a8aa416339a461277f44a9ca1be6d8ec709b68caf5e434` |
| `README.md` | `10d18efa3e99aeaa22f169afb8f07f218acf09215c1a557edda2c4d2749be3d9` |
| `squad.yaml` | `079ae29de636c45a9148bad1ee0966c58ac6c7c1ec7082314529038ce4aaaf50` |
| `tasks/analisar-incidentes.md` | `5572bca10512312b9bee2fe7b167fa4a9ecf1bada573021ad17bcdeaed1bfa07` |
| `tasks/analisar-logs-incidente.md` | `3c234e60bc1b7e08317213c8d16a0bc6358e0992cb54d4fd32e8a07b488b6c4b` |
| `tasks/comunicar-incidentes.md` | `bbe1db121acad0cae41686a6e3ddbd06877fd5a801786c4a59513c1dbed4376e` |
| `tasks/correlacionar-alertas.md` | `71961beeb620e21efb085fd31e0c9ae481891309f50a3b4f8606f5fb10d51a89` |
| `tasks/executar-acoes-l2.md` | `238b1963ae4ddbdf87b893538a9365b5452faf1ae10ea0160eb048e2cdf2d608` |
| `tasks/gerar-propostas-de-fix.md` | `1b690fb7aa34a8a823eb72c720fbee6c7e5dfb0da9701a894840bf1a1fe9038b` |
| `tasks/orquestrar-pipeline.md` | `82a0d1c00584edf2660c545206be7b289d550166d208aa32b4f0571a725e631e` |
| `tasks/verificar-saidas.md` | `2ac86930c351036d3337577a07f07671e0e9888a2cf5fdce2467f397b3de6d14` |
| `workflows/ops-cs-ai-sre-incident-pipeline.yaml` | `dc16c7385978d28fe4fdbc68e8330c2aa3d8385f622498729ff21e5371df176b` |
