<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-qualificacao-conversacional-whatsapp -->
# Proveniência de Qualificação Conversacional

- Origem local: `maquina-de-receita/squads-gerados/vendas-qualificacao-conversacional-whatsapp`.
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
| `agents/agendador-de-reunioes.md` | `05eb719f2813dadd54fe6a8045d912d59ac8f36fb22dcd9790becc512896c905` |
| `agents/analista-de-conversas.md` | `de47ffbfa979630b8d9852af3536e2208856e9ec2c706f39c2cd31170856a36f` |
| `agents/censor-comercial.md` | `7ef2985e6d31949dd5c3c23ef8c950eb7c5ad942d7fb5af0b96f24a6f442b53e` |
| `agents/guardiao-do-crm.md` | `be34acf3593dda4cdca41d49f1112dc19e62efbdb0a9fa1db659a79631def4e6` |
| `agents/investigador-de-lead.md` | `ae9a7a7697a42cc1fa15a10ef3b46684f1d609f6e00cc9e10c26c18a714cba36` |
| `agents/juiz-de-fit.md` | `c3cd14f39e5b4cbbe051a2f75991404d3b81d367c5b8dc1b7e4b3ee77d721513` |
| `agents/maestro-comercial.md` | `1720af533a8b3d01bc49ad1d4c8d36df97260996537e7120a09120b118d67c96` |
| `agents/reativador-de-pipeline.md` | `47b3cf8e0ea748e9023f1bbf6c0c9d3b77e379b9ab4cd49127869eb555159e5c` |
| `agents/sdr-conversacional.md` | `bdcb31022f05f31a3401fc58694bf2ca5dad68c8bf9fb206dfce1ff8ae781490` |
| `CHANGELOG.md` | `80ef63a7f4bc5bf36dad6c8508b497f3fc293af007e47be99b0a0d9a8bff8f7c` |
| `checklists/critic-censor-comercial.md` | `f6dc8f30f2c40273fea9a1e3afecce3521e36c9d0636a7e8baec4fd6d9b08afc` |
| `config/coding-standards.md` | `b520331b7882ef5b57f98e4e958eff67f7a8a2a89a530ea8c1c5cfc60815ca5b` |
| `config/source-tree.md` | `808530e15aedaaf008d5ef36617ba55a87fada6a2f9cdd5322fe15fd8627606d` |
| `config/tech-stack.md` | `f0340d15d0b56ab46de927ad9a6b06ac6d4133be91b3277812d55a7f94c9156d` |
| `config.yaml` | `ad8fa4dd0f31f4c8fabb6f221a3f764e7b30cb6e9cee60a0955141b9d6895f5b` |
| `README.md` | `765cf36fbe61e835a0980a70f35d8fcaab43223946d77531bb3447d46f81d5a4` |
| `squad.yaml` | `0afddd1c64976c0bf32ba17247892200b26b7ae68ef6915edd00e378c6c38fe7` |
| `tasks/agendar-reuniao.md` | `d6f60f165588f921c1c45fcec63f87dfaa22164701b3c6af13896773a3718c2d` |
| `tasks/analisar-conversas-qualificadas.md` | `ff2a9f27fea7e8562f1c46e3fd7c06a1e71ed9b2c0f7787b81d627522d59d455` |
| `tasks/auditar-saude-do-pipeline.md` | `13ec9993522cddb02ead7a95002536bed681dd96f0191cce1fd98de6e17e1834` |
| `tasks/conduzir-conversa-estruturada.md` | `2865528dbe749d250beb7e1c1a24a55fd332ecdcc3df937a998361b9c3e52ed5` |
| `tasks/enriquecer-dossie-lead.md` | `534e371f9c9fe0798cf0227ee582acdf96d85d351c73aa1e2881f2a584cec1ef` |
| `tasks/orquestrar-pipeline.md` | `cf3ba7e399a41e1825b97cf9092338a73a289bac642827c937a0b5069a33f7a5` |
| `tasks/priorizar-leads.md` | `5462bc77eebe93809e9c1573d617974e9d479cfe754b86a9ea9b695b45bb262c` |
| `tasks/reativar-leads-frios.md` | `9dfb6dbafecf1d6d9de260004b1a614b483b3c49d2db171daeed1adccaff2e03` |
| `tasks/verificar-saidas.md` | `daa41b0d34c4d757e041f565f8609f146b0466b7a9d911c14eae9a1c81a9a5ff` |
| `workflows/vendas-qualificacao-conversacional-whatsapp-pipeline.yaml` | `24f38820b8cc780ce2f204e4bac536ade2216c92fefebb1ed99e3781d458150a` |
