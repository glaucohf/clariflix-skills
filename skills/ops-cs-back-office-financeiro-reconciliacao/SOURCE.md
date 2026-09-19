<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-back-office-financeiro-reconciliacao -->
# Proveniência de Back-Office Financeiro

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-back-office-financeiro-reconciliacao`.
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
| `agents/aurum-2.md` | `daf9c99ff2d535946d492063da4e2a2f584d5a84d3ade75b5c37d230e7d0bd52` |
| `agents/aurum.md` | `9123365e0043def5d17d8b6dfc39bea3e1ada9cb97d775e73df0a1bdef48f70f` |
| `agents/dunna.md` | `84dd69f464c623e80a37675da07988b8a3034bd37ecfdf0727c9865ec4ae2c4a` |
| `agents/fluxo.md` | `68883000bbb32e63feac0d1a197a5f5cdf7201b55ed4fcc540633db41429312d` |
| `agents/iris.md` | `fa191d3d8a28ec3c8550085c07b5050a902294a71a62112d218633161cd82f8d` |
| `agents/ledger.md` | `1c06309198abd5925abb61f5a6f9b547cc2768f1386927210b05228fa67e5570` |
| `agents/maestro-caixa.md` | `8a5cad17c11cb28d43dc5e80fec4b08fa6ae6f0e02627bb75bb328aaad603c84` |
| `agents/nexus.md` | `88bec5a4bb1e29af786fd23a9496db64fa2408d05bbb6a101d3304bfbf0358d2` |
| `agents/solano.md` | `2025cc2382f86fddc7c637e47d17bb5c0423b2c627de645ca71b74c669cdeea3` |
| `CHANGELOG.md` | `a18e8828a1de81c07b836ba12d6770b18384e58bc2c0f0cd146fd07f1e8bdc41` |
| `checklists/critic-aurum-2.md` | `a6bbcbef01fdedd61d1da6e1dfdd79abff23856bc13c6ad15b937ad7927c8e64` |
| `config/coding-standards.md` | `bea4733d7586e50b7d1abdc5c525136396bdea9554548216b71189c1807d1a26` |
| `config/source-tree.md` | `f89b0e696c1a3440378d318ed61685301c9c219a72184b0bf6c167a84636f936` |
| `config/tech-stack.md` | `32c4264b0517e3040d8ce22c8a985e425dfbe6c6371b7124bbbf998b1559e27f` |
| `config.yaml` | `123872551f1267c06be29b0fbce50f01a1cd693eb3a7a72e350ee314f51b9506` |
| `README.md` | `2761ae919ba02d917c6192e5724f9c83bfa00d7911f44ff04294fcff42bc8193` |
| `squad.yaml` | `f81fdba685763a365ede29f0a6776f594d77aeada147b83d3c2a471d13ae052e` |
| `tasks/classificar-exceptions.md` | `731b888ac2add25d5e588bfb10518af146c8b9b76cb36192e83e05bfd5105946` |
| `tasks/cruzar-transacoes.md` | `b6460fe2ba939c827c4d07ab27f8312aec0af3c50a672c1f5031c443dbf253d3` |
| `tasks/extrair-e-normalizar-transacoes.md` | `6db50a5760696973186d1270f247dbaf6f5aa2fefa8d7eec042007a1f26275fc` |
| `tasks/gerar-aging-analysis-automatica.md` | `cae41093c6dcee0aefc0fe2b841d4aa6ce65fcc52cdf08acb55e344c22e84085` |
| `tasks/investigar-exceptions-automaticamente.md` | `591cea0c7fb4ecebf7d1775bad0afc3d05d7c42e24884a47928e22ec91235a94` |
| `tasks/orquestrar-pipeline.md` | `315b2ee272b80fcc75e4c853076cc50e1b4f0e3d4cdcc35566114706c4a5923b` |
| `tasks/preparar-closing-package.md` | `dc114773b9bfd2d3deab013a7d158aa4e69a75148bdb75ee1b9b670be0c85928` |
| `tasks/verificar-qualidade-financeira.md` | `ffd6810407303daaf758ade0d2556ca9d7e8a813d68091fb164a140c9ed26640` |
| `tasks/verificar-saidas.md` | `9dfdf19f1b8da7356164839898749edfdb086566130e5e279cd7ec5e91864e38` |
| `workflows/ops-cs-back-office-financeiro-reconciliacao-pipeline.yaml` | `77a3942a9b539ca4b2a68eb5891f6e18721c8ceba48eabf5295692e78035ddc3` |
