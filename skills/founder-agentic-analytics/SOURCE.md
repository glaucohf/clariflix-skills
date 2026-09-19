<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/founder-agentic-analytics -->
# Proveniência de Ágentic Analytics

- Origem local: `maquina-de-receita/squads-gerados/founder-agentic-analytics`.
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
| `agents/anomaly-alert-detector.md` | `7db98e4e666cb23c5c60ff07f117173a44de87bdaa296281d807f0d74ac34578` |
| `agents/context-enricher.md` | `9a50883d3bc157ddf65412d4e001deccccce5d0736ce91eca4127cb06f3ca427` |
| `agents/decision-logger.md` | `2a9c0f9e713d544ee763b33ffc8e7fc68c8716a6dbf9fdaa6051484c5aff778c` |
| `agents/orquestrador-analitico.md` | `e00ddd57d5d837b7bdc57f32a25724da583ef4b7a1fdb55d8b2da01d00733255` |
| `agents/semantic-layer-guardian.md` | `c0b65ac709ea1e8b73084bf8b09ad446a724c1f40d5a46ad9e0085e44e8d8544` |
| `agents/sql-semantic-verifier.md` | `828c1404fffcd5a668b3c677212587d9d6dad36e0948370b331611376afdeb1d` |
| `agents/strategic-query-analyst.md` | `d07ff9cbed5953fd26919b717b2a2c74486e1b03cf2a9bf08d130098337557d2` |
| `agents/text-to-sql-worker.md` | `783b26eaf4b0790597e26171878463ee0ecba8d370eff7785300625410f0292a` |
| `CHANGELOG.md` | `ec3aa500886e5cd4a5650d187d6d32b453f9813f51164a7399431509fa6aeea5` |
| `checklists/critic-sql-semantic-verifier.md` | `48f3ccb54423af1d688a0cd9b6ba237a23303c19297b4e5177ed6d6f3268aa05` |
| `config/coding-standards.md` | `cf438b186db63a7d4ab6ee5c95362bede57d2ba51824f1302c0dec427fe3e484` |
| `config/source-tree.md` | `eb2ba921a0b5f198c38107f88c16e2cabf74b6855f76181e3b94749b73a414bb` |
| `config/tech-stack.md` | `55e971045807196d855399df4f42042633e6a374978787ae2b813391fcaea85c` |
| `config.yaml` | `a6cbbe1d080e8f7e4aaa7a021bfbbcf6daf155c3b8d2926d5c9202edbacc226b` |
| `README.md` | `c42a82d5c5d504c662750be7afd48e18a036dd5aba59383cee898eef157c7642` |
| `squad.yaml` | `a36877cdba866205f852568b193d54035aac1d929d2b34d1a65859f59e5fecb0` |
| `tasks/detectar-anomalias-estatisticas.md` | `111ea9f152feba6e5019573424e6d982223b4f95d00e62c1968419138bde8526` |
| `tasks/enriquecer-resultado-com-contexto.md` | `e174666072c0188267c84b00b1d22b9d6b0c117e6d67c799d308ca38f11be9b9` |
| `tasks/orquestrar-pipeline.md` | `a53f2430f9e09cd1b229c6e7557018052c67bee83d115e8cab6cdca01a2e064d` |
| `tasks/registrar-decisoes-baseadas-em-dados.md` | `56838184a9905fec58ca2cafd31964a7fd8a6e3381bf3ea5f3139e92eec1ecfc` |
| `tasks/registrar-gap-semantico.md` | `067de167ca020885918e8fee6f8232526d366ffa15dfcde56f564250fe55af77` |
| `tasks/sintetizar-respostas-analiticas.md` | `37f890bbe9abbbb43f91169c7be3f483259a9163ab89e751753fb490eadbc226` |
| `tasks/traduzir-pergunta-para-sql.md` | `6c50c8d23d54fe86f80d1ee2c56d704487519481bca93de0265e29e0103b7e4b` |
| `tasks/verificar-saidas.md` | `e47c8d9b7999694894cae65d279db0b9dd76583a079cdb69db6d70143bf56ac0` |
| `workflows/founder-agentic-analytics-pipeline.yaml` | `b6a39889db1ef0782edd1756b1b62e98a4dabbb542076e208f0e95dfee287520` |
