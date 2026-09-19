<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-onboarding-psa-agentica -->
# Proveniência de Onboarding & Implementação

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-onboarding-psa-agentica`.
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
| `agents/argus.md` | `e04d1270f97a9de3afe10901607a1a78f9a1edc72359ece79af2dcb360954e39` |
| `agents/atlas.md` | `33c175dd539dac979246fa41319933e128b1cc7845d89668a15a666a2471e5e0` |
| `agents/cassandra.md` | `c3064aefc2886c2defcfe0a871b0d72c3831846616ec968f8883ce070f9172d2` |
| `agents/crono.md` | `2af70e9de0faa17a349b80ce8539f55c9be755b1e0346c1672fa336af04dc517` |
| `agents/hermes.md` | `e88d0123f2caf16fc3fdb8c6de0a587f1f1ad0aa1c137ed6397df76ce40d5a1d` |
| `agents/iris.md` | `e667f8a4a39d9b672cbb23235ab213a1d440fa6d8fd93a07c7a0baf8e7eda166` |
| `agents/maestro.md` | `8de6cdd1a3d26c4017250577a7de74fe2fd95f343459eeb5fed8d2bc486af991` |
| `agents/vitor.md` | `1a98ed9b0ed5fe96a3dad49146770bef9f442cdcc57cf1ee9a9fe32f34208e5b` |
| `CHANGELOG.md` | `34e1c8915f658842ba281813980eea5127dd32fef34f0ab897617ceb64ab8115` |
| `checklists/critic-argus.md` | `4c3ff67586b947959918bda2c45da08052c183b8362b6f238f70dfc0aa16e98b` |
| `config/coding-standards.md` | `2f9dd7750ba69ba26ab1aa5ed7e648be7989291134d8cecccfb6f6677c856104` |
| `config/source-tree.md` | `2154f11ff012822d26a9838bc50f73666ba398f70dde03b938d7469e19e29f86` |
| `config/tech-stack.md` | `c467f08eb743cad629ffa8892d3578dd47bfbe8773bcfb480d9309d566b5dc42` |
| `config.yaml` | `0d33fbe348b36a0f906d4d52eea502df200fedc3c79d8c77986795ed261b0193` |
| `README.md` | `a4a0270fcb96728588e86be12219073bc991587739e8f82728bd1ad8acf602b6` |
| `squad.yaml` | `5824fca2ac773128c013e4cece9dc749cc96dc247b7535777efb748ab9056127` |
| `tasks/calcular-health-score-cliente.md` | `60ef449d534ffd6e3dffcc7e27795753a2f03a40d9a00a9594908de52aa16c50` |
| `tasks/criar-plano-de-implementacao.md` | `543566183c370cd301a144f3f1ccef854c20a8a552abf6626a6e2ff0ebd8d915` |
| `tasks/enviar-mensagens-contextualizadas.md` | `7c4784b43b14251a892fe2fecdf52c11d229d2f6a8b47e7c929c28c13ffce002` |
| `tasks/gerar-relatorio-de-delivery.md` | `1058657279253d1ed9c365607776d5ba28b3a965f54304977ef09858c195942e` |
| `tasks/monitorar-desvios-de-cronograma.md` | `5f19dbc9d48dd91d19ec60035c10ab9e9197d68ef2625ba22ef75bf59732a406` |
| `tasks/orquestrar-pipeline.md` | `e73e4c868a8e67cce5219cd77cd0dec5bb6f51ae0fc0a37a7be721934a16d268` |
| `tasks/processar-documentos-sow.md` | `3c87c8970422f75805d68a7df704594ee69c1275de4da353db22d6ff166a6f72` |
| `tasks/verificar-saidas.md` | `5f999cf749c2f3821095b084d064afaa188467dc805d3e1ff65c5ab8d345b907` |
| `workflows/ops-cs-onboarding-psa-agentica-pipeline.yaml` | `ef831a5715a2a3753ab7b0736e27d14e387a8e712003f66fab790c439fb5d0fe` |
