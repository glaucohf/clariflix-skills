<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-forecast-deal-risk -->
# Proveniência de Forecast de Pipeline e Risco de Deal

- Origem local: `maquina-de-receita/squads-gerados/vendas-forecast-deal-risk`.
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
| `agents/argus.md` | `33735a1c2452882d0d3e5e6371ac6a54b9c35d4d4864466df15feaeb321b3f28` |
| `agents/cassandra.md` | `8d8ec33344d33188cd6b2ef0381a4282f142e35c01fac55f9d2576a2a9280bfe` |
| `agents/cronos.md` | `efbdd6323fa1f3e6cf7ce16f11bacfa15bf3cb36b32ac69692c33ae75d694251` |
| `agents/hermes.md` | `c4425ee67da5f5deac647fa238240aba59efaa623045fdd3987b07ba76dfd1e9` |
| `agents/mnemosine.md` | `ab5eeaea2f28679a6f6150159aa21239635746f0743bd9b623b8d7f97ba86775` |
| `agents/nemesis.md` | `20776c9690cc23f16f82e8e8d7b24e9b021db9253a29ced5ff85750390537448` |
| `agents/oracle.md` | `3b05f9a661f6d9e8389e605f1db47d75e2ccd957f3bf819446898db802c37a4c` |
| `agents/sibila.md` | `186869d333c167230e2a0230aedfabdf18ef9b9fecdda55e73836b04c2513388` |
| `CHANGELOG.md` | `26d83a5ac0502020636a9ffc185e670f3f10c63ffccc12018b9d21282314549a` |
| `checklists/critic-nemesis.md` | `860afd86981b3e092f14f0fc7dec830854d87b9b1ecda3ac53d7a770637bfcb0` |
| `config/coding-standards.md` | `6ebe54c563bbafae969ebd929926ce138dbc36ab2dac6d276eae7895cc2b2830` |
| `config/source-tree.md` | `52551d9edcc63ec84efd55a0042062e5062f485dbd182beca6a4535e8eef7483` |
| `config/tech-stack.md` | `7e9a19ee8697f5da6cf50e07ebbd5f31441007308d9ac70d3bfe8430fe674718` |
| `config.yaml` | `784716cedcdade8f717f56bb5e27b2e0a897528f9f7da42e0a26755902545d48` |
| `README.md` | `218f66844ff57fe79f4bd7a32036acc5c53e1ba1df83c355cde35a333b965d3d` |
| `squad.yaml` | `2308f4e54e8eccf8c4d3cd250b9c38aa83640534af9eba2e6a8714871ab1191f` |
| `tasks/analisar-deals-fechados.md` | `2e592d821a8ceacbe4893b1887a16d096c63dbbd2e32f8fe91094258f6818c34` |
| `tasks/calcular-score-risco-deal.md` | `74805b81f8a1381544b95a3b81638a3b24a10850931522270f7f4cae37457c7f` |
| `tasks/formatar-alertas-contextualizados.md` | `7402741f3cef870a4b1aaed0e0eb541c43178292f8b1377dbc8c88a5575e3e86` |
| `tasks/gerar-forecast-pipeline.md` | `30fc552333785eaae786aa4edb56a2cf18e10ea5fae4b3e892b35d58b435e769` |
| `tasks/monitorar-deals-ativos.md` | `1e411b9e63cc1a3ef1b89b85549e9499224c55b4deffa7c2487ef1d97a6774bf` |
| `tasks/orquestrar-pipeline.md` | `73454ac02aeea7277c50cf6005d0383c6795bd48387c4fdd29515081dddda513` |
| `tasks/sugerir-proximo-passo.md` | `818203355517f94758b0a9d5081322351eaa8ea5f5bc66c2e6c9cd580bbb7b9d` |
| `tasks/verificar-saidas.md` | `feee6a086fce7dee775b8952d3c998ca425e0ab9749dfd99d28c07f543bbc4cd` |
| `workflows/vendas-forecast-deal-risk-pipeline.yaml` | `5f1836e8d40e0fc45ff84f662c05088b0bfc1ed27faf637ea29c393d667d86f4` |
