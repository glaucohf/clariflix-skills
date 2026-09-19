<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-inteligencia-conta-battlecards -->
# Proveniência de Inteligência de Conta e Battlecards

- Origem local: `maquina-de-receita/squads-gerados/vendas-inteligencia-conta-battlecards`.
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
| `agents/herald.md` | `15f39a415936a436f4a69cb958d9abd4e01db7499a90d2db1db8defef2baf987` |
| `agents/iris.md` | `a61a05c5e42f0174b7d5ebfd5d912a6f760c3e9790e3381150e7d10dcdf1bdda` |
| `agents/memoria.md` | `e4bdc2c330dcf775cbf1fd1d74775a25c2384524f89cd44853e4d481c1fa0437` |
| `agents/nexus.md` | `35557dfe46ee37fe2081b75877dc4ed23eb3287aa1fa660b5bedf8339e37eb27` |
| `agents/oracle.md` | `c43455fa699eec2fcfd9f258def51ca0f130c591abb50c7ab96a8075726f305c` |
| `agents/scout.md` | `0b7d0ec9bebd00b8fbfda7bb0299ee68ce2de3bc9d7319346fa0658b7bad5661` |
| `agents/sentinel.md` | `646b419a76293dadf7d14ee45e289415a479141a34b736c2952d17e2e3d65c8b` |
| `agents/warfare.md` | `03c25e680e8622c3afe7cee1eb3bb50d66776bb98839b7ad34975be86d29e32b` |
| `CHANGELOG.md` | `7304cd610d331f3603e3505460f6ad94684525195e2047667dcaf6b10b161724` |
| `checklists/critic-sentinel.md` | `c67bfca8c6d1648c7a5b2f9b3a4c0bf4a939df8437a1ab488cd5c96e8d15fa6f` |
| `config/coding-standards.md` | `537fa42adb8b9ce37abb1f642682cc95bc7b3a1420a17d003866cf515a068316` |
| `config/source-tree.md` | `8a39ddb304ec2b8728bfcc5b79f8ac68ae291fdb4ece0a0e18f8ec583dd8f389` |
| `config/tech-stack.md` | `ab8544a853975471f686dbc0aff18750a32dc451714320f5bccd72ff7482654e` |
| `config.yaml` | `3166818a98776f0d4cbdef10a17fd11567fbe911f86ff5bf992a9b77f473f9d9` |
| `README.md` | `4b923b87adf1244b5fe7aa84962125f6a72b5590a3cca420e7833d3025d60925` |
| `squad.yaml` | `02f7a18d1a950d91e71bfe5c7a40511d1c42c7b348fd08e8f6847a55f3a1d0a9` |
| `tasks/analisar-dores-setoriais.md` | `59b6031190b04933f8ff281424a6ae65355d830f06498be0e84d255bb8c76039` |
| `tasks/entregar-artefatos-formatados.md` | `25404e5983fed6d4b92d1febb639eb6bba145ce1b9072b7d125ce17996ec66f3` |
| `tasks/investigar-empresa-completa.md` | `5b7fe9ff7837e979fae5276a1d6972b2fefe324f84596e22d7ac2b830a61148f` |
| `tasks/mapear-stakeholders.md` | `f5d62aab853c74fa3ea2ed087b8a5afbf60899b361e37762d9e69c8e2bf801c5` |
| `tasks/montar-battlecard-competitiva.md` | `0d73bae086e21511a88ab0649397ba7ea75307306d4368df7b8c59643d0edb5f` |
| `tasks/orquestrar-pipeline.md` | `c14af08815258208324c85ae2c75cf75d721d17734397bca17035ae05903a73b` |
| `tasks/persistir-contexto-no-crm.md` | `09a64c8e3fff6b2a01307e51ebb9b48c94efd67143708a81c9c1216c68c63f11` |
| `tasks/verificar-saidas.md` | `b24450ffd689856387827f5283651217539a708eec0ca9964aa3e813ad5e1719` |
| `workflows/vendas-inteligencia-conta-battlecards-pipeline.yaml` | `2ffc55469a16b63b2a537163bd20d57c6d0b805f48193d5be2f081d80c5db2ba` |
