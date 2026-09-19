<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-agent-assist-copilot -->
# Proveniência de Copíloto do Agente Humano

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-agent-assist-copilot`.
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
| `agents/compass.md` | `10bdc2b9cdd9642d1f74ffc0c86618bf737b7e0365b25d5efa9addf4e347de11` |
| `agents/echo.md` | `a877863f701e4d42d35f4612c9ec25575e1f05cc0f2e0132ae8e84fa72eda581` |
| `agents/lumen.md` | `8a9aa5dc5e78d71cbeaaf0aeedaac932f19a46a02fe6d92871664fe5bd6dea4b` |
| `agents/memo.md` | `84f3e615f48929c445699a2e7131390285def2169a890b292bae2651361e7f97` |
| `agents/prism.md` | `0ba19f39892566f84bd217b18d2d2a14b300fc51e5a27f35079958946a9024b7` |
| `agents/radar.md` | `f3dc1aaa0ac3b474c99cdd1bee0393e5f1e7cbd8bd2ef832647b7fd62da67ac8` |
| `agents/scribe.md` | `6f43337747b18c89b2c70ed2e53001cd87796bcefd9eeb627f7d8809259b302e` |
| `agents/shield.md` | `90b44450eea12bc000b7f1139c7fc8a408df3d03248f90078e610f12e129fa02` |
| `agents/vault.md` | `2b8190637ce998355b2d57e83ddf27bde6d12b418030db08bbe95ccca4be7c86` |
| `CHANGELOG.md` | `081a75ae719688c6b8fcffddfbe58cae0742bacf30bf1aba06b8d175e3474463` |
| `checklists/critic-prism.md` | `51b5ac53d6b88fab6bf1df36a2994f91d84d814fda5cf5050e2963511dfe75b8` |
| `config/coding-standards.md` | `e1285f9bbd7a716a0bbc19562ccd74680c27926c366fd37653f8ea7103c5bd6d` |
| `config/source-tree.md` | `fb3a376915870a854c91a88aaa67d3fbeefa9b23a9ef1ef4e2efd8ec0324513d` |
| `config/tech-stack.md` | `3067d1fa390a7bd6fa47758a2b66b92cf49ab68c4b5bb818e3007fbe808293ec` |
| `config.yaml` | `84535dc7b815d6cd957881765a0f24a201e5fe70425fe512578c4b3cf2dda79d` |
| `README.md` | `166353b27437998521cd4c4312267caf6478a55230f69a5ecd8e753d973fec68` |
| `squad.yaml` | `e4baedf16425f73a69f7e6aa6c08782cc7a9b5ace4af068a70ea78ecf94644d9` |
| `tasks/analisar-sugestoes-atendente.md` | `8e20a69c297ca57538499910226705ba02e2460666bcef351602caa18083ae5b` |
| `tasks/classificar-intencao-do-cliente.md` | `3c5951938d12436e433e72347a58e5c1c99231203854229cf6b7aed67f9dda4c` |
| `tasks/gerar-resumo-executivo.md` | `97daec600964273cfa04abea03c1e628deff0c1812b867d4e91ec71a52e25eed` |
| `tasks/gerar-sugestao-de-resposta.md` | `db9e53b429a01ddc0ee5c99a9c0f93fdf73b63de9b6b28ac71538d15d3ebb7b7` |
| `tasks/monitorar-mensagens-atendente.md` | `b39d040842498f94853bcf3c064455dbe75a8d77be456033b625b2552038f545` |
| `tasks/orquestrar-pipeline.md` | `d08d7a18ce83466406205b5a1a9d9fcc3b9cff83ae6a938ac362b9bb424f7ead` |
| `tasks/recuperar-dados-de-conta.md` | `f09d05ed3ab97b7f6f4dbe065b792b6f83f033d2bf398314b52c448960dea1aa` |
| `tasks/sugerir-proximo-passo.md` | `5da2524900f5c076bf80c2e02254f88ad71ab6acb5acbf962b20d3bb792d66dc` |
| `tasks/verificar-saidas.md` | `b834f3ff879292a9551e95c5dad110d1f80d39b9756be5d344210f19d65704d5` |
| `workflows/ops-cs-agent-assist-copilot-pipeline.yaml` | `0846327e5549465825b49474db5268a4cb66ecf8c8191f9d7d78257beda9b105` |
