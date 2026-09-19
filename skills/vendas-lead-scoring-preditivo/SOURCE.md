<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-lead-scoring-preditivo -->
# Proveniência de Lead Scoring Preditivo e Priorização

- Origem local: `maquina-de-receita/squads-gerados/vendas-lead-scoring-preditivo`.
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
| `agents/argus.md` | `57b93fda28e266e69a67db075ba0dc6da2b3cb3628a66818f1877276d201c0aa` |
| `agents/atlas.md` | `c05f03c021ef1cb7b5212939d8677f550be705acff76d12ec84ffff53acbc4b2` |
| `agents/nexus.md` | `a3d6276b3904bdc3adf44b28713be9597260cd29ea036885d6cfaed6655ef53c` |
| `agents/oracle.md` | `e8f321e6b0f9756e070947867c9d56525ea5fca33e8fdea137b0d005062d1ede` |
| `agents/orion.md` | `52c17bbc2a5bdf6db3c019a2d2d3a36f9f3b51d4e69a3339c5929407e23001cb` |
| `agents/radar.md` | `c85a6aa6bc15b26407b54986444d2a76e9653ac34be9b9d1c2f63e87b0c114d1` |
| `agents/sherlock.md` | `9a9f3e79bab7f66cf1f15844bb82d8631ac3780ed1784865df61a4c14cc67c86` |
| `agents/vega.md` | `35898f910aeb2bc8a881b3c403fc6d8102672e207153b3514e0998d0560ae5f3` |
| `CHANGELOG.md` | `75435595bcde167c0407af31144a631a9e30a1cccff41219de38e9b807e9096c` |
| `checklists/critic-argus.md` | `b3c65c1b70dec3c18eaf9a3c1ddf03b3bb81d2b1d36b65bf67ec9f1d76cf2d88` |
| `config/coding-standards.md` | `2f9dd7750ba69ba26ab1aa5ed7e648be7989291134d8cecccfb6f6677c856104` |
| `config/source-tree.md` | `0896eed290527d067b8c92ac940203f3579173d25ebf9b6ea09753878c4b51ca` |
| `config/tech-stack.md` | `1a209baa6f5400fb07d5862418cc943ccc0d660dd3cca0b069d5cad3d65255ef` |
| `config.yaml` | `bbb78fad5ea7f8fce6a68206059ffd82e2cbfacf099e04a3bb2e378beb586711` |
| `README.md` | `ccdadea2c6e200796d42d1e567cbd71ab25739c1bf9aa28d80b12439041c1210` |
| `squad.yaml` | `b6704a778c13f03c37d6cb4eed3472993528edb0a1708d21ba7ac0044eb27727` |
| `tasks/cadenciar-leads-multi-canal.md` | `36e4d4418e219c7333df45859f4d0915429bbb3e2d116164e8a5adccb65dfbd3` |
| `tasks/calcular-score-numerico.md` | `fb11dda866e8e421e6bc62dc5dcc3fba82890b12e453884b8898daf5b933da9f` |
| `tasks/capturar-sinais-de-intencao.md` | `a3f7434d14a43a3a091e240898daa44bd97ab1f45941f29d706f72cf24223c9a` |
| `tasks/detectar-risco-deal.md` | `68f39b66f73454a9391bdad9b4aef3eeec8fdb0654683424b31c3d0eab24113a` |
| `tasks/enriquecer-dados-firmograficos.md` | `029f643f1b3fbef674860c69ebeb13f7c92b02bd8dcdba8554022e1c8db791e4` |
| `tasks/orquestrar-pipeline.md` | `7f1b57791cb9070dcaee80d3d3f9b632bbe474f3dcc81c977c76a26c4c970611` |
| `tasks/priorizar-fila-de-contato.md` | `af02f62d92cdbbe0a95a6e41d63416e4eea2c78335c90c6f8c0baf2f5c36403d` |
| `tasks/verificar-saidas.md` | `b5d59654d5cb12573ed1ff5478a125fbe82c8fd4366bf896b06db57f01c9afdb` |
| `workflows/vendas-lead-scoring-preditivo-pipeline.yaml` | `ea0fd7cd6611c9ff38090ac83753a5cb63a51adcd9e8911cf47c7d72ccf70acc` |
