<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-handoff-orchestrator-hitl -->
# Proveniência de Handoff Orchestrator HITL

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-handoff-orchestrator-hitl`.
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
| `agents/beatriz.md` | `a4a0bd5e146fe8b9d611c5ca454c053030c1e16486a152fce8d04c28c5ce1962` |
| `agents/cassio.md` | `d66c7a9ca32dd25c890226d94d0732eb27129e1803b3b01d7b740ba84d121643` |
| `agents/dora.md` | `b5bd67eba7795a67f8932f6b4358778e79e5b8bf46dc70cb6a2bec53eafeec77` |
| `agents/fabio.md` | `655f727417217120c553f3cf9a64e2b7f588c93c8bea017e4e633e74cf36f03d` |
| `agents/hieronimus.md` | `273ee4b585d856e7ce0d92f45fe1a9fb527cfc09a99309af1f079b26d738d925` |
| `agents/renato.md` | `ee2e5c75d6e1248bfb6fe1e9298757dad1e469490c6b370303521c1c775f5d3e` |
| `agents/selene.md` | `6a868dd0da5c438b81bb0f6337f105a3002c5e6d3ac9b93cc7604e40ca012e14` |
| `agents/vitor.md` | `e880044c8627e80d9dbcd22bb939fe62ac6a86535b9984f681578542b95eb480` |
| `CHANGELOG.md` | `15d31a6f082baccfaf5d47d861b843c3a3d42fca0c3d0b61628b7ffa543cfa1e` |
| `checklists/critic-vitor.md` | `2fe34d1885d7efb2345032776c7c5fd02ccb556779293961f4bfab4b3801173e` |
| `config/coding-standards.md` | `5762d3bda1cd57be3953ba7461da378583311cf8afc185205ba7d5f3f510cc13` |
| `config/source-tree.md` | `f36be4d2432541b6122d2e1f7c536230e8aacf438479041497deff5c86cf2237` |
| `config/tech-stack.md` | `fa267355983f2e6d382208b649ee55686c628eb6d71ffd06ee23d93035b04273` |
| `config.yaml` | `1fa9c59c2bd6cfa3a8b56375026a41529294ef121697aacb942386266fc10b13` |
| `README.md` | `1b563ab0f2826f607e65a1bdf655786ff366e4d7d6e7e287d348f83fee95a66e` |
| `squad.yaml` | `23ac677373bf8da7e3e852280ed5fa402cee585b5931952c4d0e040e73ca7f4e` |
| `tasks/analisar-falso-positivo.md` | `816015e7c797a045eaaa0836b6c9cd1479982e77d0b0587d7f7cc21481f4b888` |
| `tasks/classificar-criticidade.md` | `d17b57d1bd0f3b5d4de27e82d79beb240f04a6c6a213d6eeea25b35b5e396209` |
| `tasks/determinar-canal-enviado.md` | `10d280954030cde5ca0b814fcddd479dad61109d7374177771923fe9cb23f065` |
| `tasks/empacotar-contexto.md` | `854e5cb9735a9b5c30cd25cd7ae0dba24949da38ec1338d7647978ef26e49449` |
| `tasks/monitorar-handoffs-l3.md` | `5e6cc07ce5313698d97d4e83b9fe9f0683fe2957b240a21dd4f7b8b6363e244f` |
| `tasks/orquestrar-pipeline.md` | `6ff91c6f87f0427279e06580b3349e2facbd5f4872248aaa629a932b5d5b2f0d` |
| `tasks/registrar-decisao-humana.md` | `46a462d5b5bbbe6403ee072770b77e26d3d799dcbd54d3d7b82037fbd03a4131` |
| `tasks/verificar-saidas.md` | `fe87a00f0051387ccb93254107936a00d774454e7b8d64670f43c9ac5ad7eba7` |
| `workflows/ops-cs-handoff-orchestrator-hitl-pipeline.yaml` | `d88752902754a9968b322ac608be0a8c571a8e0245481bb433aed5ce651fcd26` |
