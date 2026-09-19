<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-churn-prediction -->
# Proveniência de Predição e Prevenção de Churn

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-churn-prediction`.
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
| `agents/argus.md` | `3c6f9e998f3061d205ee7d85b498692caadac79d837326bed5e94ec86980371a` |
| `agents/echo.md` | `50ed39dd6c6269ea074ddcec660bd5a2760a70041e70aa7dd2bebe60cc2fb7c5` |
| `agents/iris.md` | `c073a09239abb1d26ec429e96ddfaa017d157a64cdcdce25d5c2e4dc953ad8ea` |
| `agents/lumen.md` | `662d2fbc9211e579ff7601d913295f677855e5050a71e8b08bddf73cc8ceba6d` |
| `agents/mira.md` | `b213bd06bfda8d93ffd44a4cc7f5c3e380e8d89693f2cc722d3cd025d1cf4203` |
| `agents/nexus.md` | `4ec1f115376a31e30a7e23cbeec65c44a6c5d610c1c8270772ab38652b84b2e4` |
| `agents/prism.md` | `78590e8e4e977f4706e0f7a2d245f1b260fe59a2d33afd6cc02bbdf35721fd2d` |
| `agents/spark.md` | `719e6bcaecdb411d0d9f358e0743dbeae12d2c95feb413efdf20374a827fff75` |
| `agents/vega.md` | `7f8a6d7cac65b6a61e160127fa2fbcd3569a131fac2301e7cd35802759b5034e` |
| `CHANGELOG.md` | `543f19e3e7175ff1d42f0cb8f9df9382be016ad4b1e774fddf10bcd10862cbe7` |
| `checklists/critic-argus.md` | `28b456f1573efd920257f8f7ca433081fe1f1bedfcea72571e54a6928800c3c5` |
| `config/coding-standards.md` | `2f9dd7750ba69ba26ab1aa5ed7e648be7989291134d8cecccfb6f6677c856104` |
| `config/source-tree.md` | `05b9dde363effda87a85b312bb258e5920c154db64be2de9e35104e6433bde97` |
| `config/tech-stack.md` | `e4fdbe5d1b2a760d9f38d9d9bffb0968ec6c9fb639f7f871d83677ec0d025090` |
| `config.yaml` | `bb31fb6d401828cd40fcbc1ac7660d0541b2fae30f6443cae251b799f57f14f7` |
| `README.md` | `ffeabf96500d319c761755def2647337074769ee84efa87ef28a03a768fd5452` |
| `squad.yaml` | `b4456748fe62ac46a1f2a4e7065963f57c86f3b27d9bb3ad2da5936ef6695623` |
| `tasks/analisar-contexto-comercial.md` | `35612d6b7f2333aa96ec5ceec631528debe8b3785d67eda5240775259b4b17ee` |
| `tasks/analisar-sentimento-cliente.md` | `581c7425c8b06a11cb3a4c1c4d441a9d82605f1bab38f5921d1f761a3cf9faa8` |
| `tasks/calcular-health-score-composito.md` | `6596adce388a270fd5803e94c755e8278d75aae3d861956ecd8399b93e541eef` |
| `tasks/criar-task-retencao.md` | `5d435aefbb703ad9032c63f540faa5a08d612c7ea42d5fc33213af00192a61c7` |
| `tasks/gerar-brief-personalizado.md` | `f47f1cdaf8572cb881ea2ea36974bec83342be8e7bde3c3c43badd95daca340a` |
| `tasks/monitorar-health-score.md` | `266984c3cc996a319421a3d905725e1925279c668514276bdf1216648242e41f` |
| `tasks/monitorar-sinais-de-uso-e-sentimento.md` | `dc327621c544c9be373a983ef4baddb9b4d71db451c081e23a2c0e4b61a6136a` |
| `tasks/orquestrar-pipeline.md` | `5cbd1c2a8c8c97e2a4421cc6eecedcc4de4810cfb4a3f8fc24a45831ca43b324` |
| `tasks/verificar-saidas.md` | `59b7d0954bc9a094473867303f1ed93ff670790730feb71b49b0911fd016c737` |
| `workflows/ops-cs-churn-prediction-pipeline.yaml` | `652875f7c763d0388deffaf77525e9cf5f7ecec5a430871b448767eb7641198c` |
