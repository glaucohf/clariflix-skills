<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-conversation-intelligence-coaching -->
# Proveniência de Conversation Intelligence e Coaching

- Origem local: `maquina-de-receita/squads-gerados/vendas-conversation-intelligence-coaching`.
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
| `agents/babel.md` | `0587f4a9592c2799fbf5f9f660d51cae16ba70a1ab0ae81aa10c0599e78debd9` |
| `agents/calibrador.md` | `43bf1804a23f7727efe7d3e07cbd709b8ce0364df309fdd8d85f4284ed446854` |
| `agents/juiz.md` | `40f8afefd75c9c5fcc2e1e24b49b35931eecac561fc583471e6d9c5df8127388` |
| `agents/maestro.md` | `a224fa8f1897039e923b31d6035c690790864a8be1af119c01ac666cd4b29bd9` |
| `agents/memoria-do-crm.md` | `4fb3496c78f0505744c496fa866dc82d6d227db574c0b261cda53b0e3b288ce7` |
| `agents/radar-do-time.md` | `5ef0ec4b17d8d756f7c8e7b121f23b2b5859546f00ef232fbd10a9c6e9722d2e` |
| `agents/sensei.md` | `624e5c0028647b5df6ef676f4c5e1fb11069b6544c87e60aa795bf0d605b1c06` |
| `agents/sherlock-da-call.md` | `c701025c574f17260dea2483c5659510303e6fc79c750d164b3fa88ac44b0f24` |
| `agents/vigilante.md` | `075ecea7549d970ce80e697bc957393ead573210396ef3bc8f4327a9a8a45007` |
| `CHANGELOG.md` | `e966d7170152c6ed834dd2f587ecf0541a36f550466b662ac2c72ff5a436bb0f` |
| `checklists/critic-calibrador.md` | `31f439acaa1df9bb0d6beb1854172c31f76f5cce1d8dd67d27f6fd198397a695` |
| `config/coding-standards.md` | `ff75e4abbb0e0bf9200c2ad550c4145bdb5ae6de05fb3da0fe68364e42834eba` |
| `config/source-tree.md` | `1fd79f10ef64704af9a37fbf9e592af5823a292b64b96c474529c84092bcc8e6` |
| `config/tech-stack.md` | `b22d52c0f7cd22148ef433fc6a1cdc4b67b47560fcc772df13aae74e884c4926` |
| `config.yaml` | `d8abfd9f98d3763a075afb2da57ca8069819e5c3af6c276f75a0b640e6315add` |
| `README.md` | `6ed98e548b1ae7db54ad9698a1b847314f2fa92f1837b80cd4f096b1d44f5018` |
| `squad.yaml` | `9893e8ee6774340cadcf05c7af9f8d7088043b3f430256fb8fd17d6c59c39b98` |
| `tasks/analisar-objecoes-frequentes.md` | `2168e3b7b5ad1dac428b7bd1e8bea890403b6aead3a007b1469dfafcc20e9cd5` |
| `tasks/analisar-transcricao.md` | `47b7ad97fa547f590c17271e6dc298d5f1366be649f6e11bb6aebe0a6c873266` |
| `tasks/calcular-percentil.md` | `2066899c6708b0d93f58571ae3b69e6a88e93d9d44904027bdf4cf33444fb78e` |
| `tasks/detectar-risco-deal.md` | `9b8634c088ca528ddee2405f34f6f8e95dcdd7930d6fc4f80ec1de2aabb43c14` |
| `tasks/filtrar-ruidos-tecnicos.md` | `63bbbf7640b13bf5cead6f9ab21642bbc03bf6dc6cc2be03303aba45466d7057` |
| `tasks/gerar-coaching-card.md` | `50621579a461ef5794b5e733da5a5ebe80c92b006564217d4be764769897056c` |
| `tasks/orquestrar-pipeline.md` | `7ac05f1b424067d453195ba5c8af6d022c714b857602ed14a573c80214678b16` |
| `tasks/sincronizar-dados-deal-crm.md` | `a5147484f3d28dcb2616e4d77442c0ad5e6dc19b811f5f8b4a2da5c7e87590e8` |
| `tasks/verificar-saidas.md` | `e40c677fe705d9f73fcbae223bfb9465457782418cfeb32079f307d216e46aeb` |
| `workflows/vendas-conversation-intelligence-coaching-pipeline.yaml` | `cd99693614d3b7acd5e4e41be8ee483cf2828751d3b0524d6019b5a216a26fa3` |
