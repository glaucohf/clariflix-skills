<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-roteamento-inteligente-leads -->
# Proveniência de Roteamento Inteligente de Leads

- Origem local: `maquina-de-receita/squads-gerados/vendas-roteamento-inteligente-leads`.
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
| `agents/atlas.md` | `a7b10a533e14f5803d21ad0474488cb58ac5118e8f55185dda28e80489de318a` |
| `agents/farol.md` | `cce3f6c20cf8156ec98fa2a1fa8aa83f426a953de641f3b525ae3cbf7d2d9af6` |
| `agents/orquestrador-comercial.md` | `3f746ea647afb8f2d7a9fa146d449a52bed5c3d7b1d74af881ecfa3da0d967b7` |
| `agents/veredito-2.md` | `229797a04b524bf32e7fdf26f0a2fc5f7d3bd65eaaf19e8180f8d85a80216211` |
| `agents/veredito.md` | `6ed097cfe3594131b0afab56458cf31c947e91ee5782d7f89087b9ca353d17f4` |
| `agents/worker-de-enriquecimento.md` | `75682974a97d14fd8d9b28aca905e7023d90de13f2e80ac1f93c6152c18e786d` |
| `agents/worker-de-higiene-de-crm.md` | `c8ec3a9dafa0911f7dba730607ec6d664ece54cd1a61a363b88aedd135959e45` |
| `agents/worker-de-lead-scoring.md` | `95be9d297ed0b18ac59d2e1bc386cd8ff423cdc7b75c7a92b916426c7edeba94` |
| `agents/worker-de-notificacao-e-aceite.md` | `e74cc5f0b1ec8e05ac256c2928ff290b58978be8161d07e653f0a85e778eb7c0` |
| `CHANGELOG.md` | `da7548c6953cbbd7c6754b11c573f91254cf7e7306bd0c52194daad80a50dd57` |
| `checklists/critic-veredito-2.md` | `a3cd51d73857e177337b64b6db02971900b9fec0631167c1af5f3af87c4b29d7` |
| `config/coding-standards.md` | `97d7c7797a33703a99a25d1936289b70824d7448c59e4170720ccfe2f3fc28d9` |
| `config/source-tree.md` | `6ecaf48f2ffb4d1c339243fcd76bc9ddb20a2486916177cf97ce2b5beb97f364` |
| `config/tech-stack.md` | `468988f584ef717afa492735a9d00ab51ec710299ed95634c5e818c7150ff2e7` |
| `config.yaml` | `df536203abcb8857606a736ae4bba104afd1da91cdc33e8b4df9e3a955a4011e` |
| `README.md` | `58dc1ce65087c51d6aae99499a846caeea276385211d472c2a77d5420e82bdd4` |
| `squad.yaml` | `56785ed5344903bce85419edbf14bb04fa7277661e64f26a2079eff3051248b1` |
| `tasks/calcular-score-lead.md` | `18e68e7801114cdd95511588c992cdfab6d1219bb4b2a57c5c68c87623062e08` |
| `tasks/consolidar-dados-crm.md` | `f5861f3dfe4e12d125c7fdc31c2173bb3a4d0045f9d81797223af27d09b9066d` |
| `tasks/consultar-capacidade-vendedores.md` | `83001bc8711cf2a6a43807a90af4bdb1017a57f8eaabda415e29e4e99fdcdfaf` |
| `tasks/monitorar-primeiro-contato.md` | `219b24310bc331fe755a18d315c00b0013e3fcb5fbafc83ea7cd02b61b78e9af` |
| `tasks/notificar-vendedor-lead.md` | `54dd0d292b665f2c0b049cb91205fedefbe7016d1681cde33d92da41676754f0` |
| `tasks/orquestrar-pipeline.md` | `13de0e54f1772f39c63871a20e105f9ceab81bda4ef5d9abb3540bf63fd5fab5` |
| `tasks/retornar-dossie-estruturado.md` | `ef8c004b9c1d02b647c192a4929e8f6bdf6f29afe2226acc2ac1457484f0f42a` |
| `tasks/verificar-roteamento.md` | `32187c5b3b2ab3375474fd9d906b6c9b5d67d3707a34fe4be9ba165475b1af33` |
| `tasks/verificar-saidas.md` | `82eefff1150f6be547e597c715d6ffa007ba906130b2ec866fc7ad96427658f8` |
| `workflows/vendas-roteamento-inteligente-leads-pipeline.yaml` | `bf67019a7c6d68cd60039b40d82ef60c05fe5675fcdfafc9648ca40b723d520f` |
