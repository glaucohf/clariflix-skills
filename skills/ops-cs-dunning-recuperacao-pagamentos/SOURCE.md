<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-dunning-recuperacao-pagamentos -->
# Proveniência de Cobrança e Recuperação de Pagamentos

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-dunning-recuperacao-pagamentos`.
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
| `agents/atlas.md` | `4449876476697f158dd0b54ebe92b05ad93b63268307e459d5272aaa821be444` |
| `agents/cobalt.md` | `6b5fdfec29e62873aea23d36aead51a206b3abb58bb3bb20d98685022d275aa0` |
| `agents/dante.md` | `b300582a26c08e37ec2802b1009423dd12468bba9942f7341738b6952f152351` |
| `agents/flex.md` | `5b2a85acbde6f22302757f682d8fa5084c421557ff88cef84a62a0c442d4a40e` |
| `agents/iris.md` | `0ba474a939a8fb169e6e1276ab8cfcf0fcd380b991e0b17171720ab0ebc4ac4c` |
| `agents/pulse.md` | `4586e5c317f1e1b16fd374210aea2f7bde9e2cb062fc9d3b52107dd8c9d07ebb` |
| `agents/sentinel.md` | `03992494d359f016900e2f7b1e619582ed2904dca73b12567bf66b9bcc25261a` |
| `agents/vault.md` | `86f4f846c186c0aae858d4829e6316a5069c339015afd80cb741bc7138e71bb8` |
| `agents/zap.md` | `554cb47fa2db82b3fdb0dcaff1de7eedfd81fba14f8d4a1adcd4d983ea098af5` |
| `CHANGELOG.md` | `82bef197e5c4b138b55d044815801d706c706c37179f51211294bd876fc4dffd` |
| `checklists/critic-sentinel.md` | `7d308190fbe029c5134a7c2ec912f5d421c984d606eeed6c6b4da3bb09fbb931` |
| `config/coding-standards.md` | `e95ea625027a6159609bac14a3aded248544d2c60ffbdbbd946646d982c979fa` |
| `config/source-tree.md` | `478a35de2ddefe19cf70ac164ff15f2e8556feb76a75cc92f93273e66ba6a2ee` |
| `config/tech-stack.md` | `0e83b6a23791c6fc60214a58463e4b01c7f3be4424d198b9008b2a46b2d95ca7` |
| `config.yaml` | `619510091eed826a79a7fe360fde36c78a2f00af98a3cba29c85991d9fa01793` |
| `README.md` | `035609f4275abf2fe8ff9f0794ca3ec2f2e2d87bd406e25bcd043e77788af29e` |
| `squad.yaml` | `c66b866775e379078f9a31f792d878c956ba2d6dda176ae6114dd343c83875cd` |
| `tasks/analisar-padroes-de-inadimplencia.md` | `3c803bc1953e27926e700a51c19b2bda6d9eb74ebc9bf26bf1f0ec95285ef078` |
| `tasks/atualizar-dados-de-pagamento.md` | `4353bef2ade33143f8b0d2e0618be3167486a54a4bee6b877f392d9067558414` |
| `tasks/calcular-sequencia-de-cobranca.md` | `91bdbad052c49c1eb99c775867d9c218fdc8d7608aabb2eb7a6f34eb4085ee69` |
| `tasks/classificar-respostas-cliente.md` | `b03261c30fce470b4178b0018e1a0b19f0156758cb9b4e71a19b08c3e7135d05` |
| `tasks/enviar-email-de-recuperacao.md` | `695f3ce1e9f95030091252d43fc44c2b4785a8c386c487f99793c1c44b83bc41` |
| `tasks/enviar-mensagens-personalizadas.md` | `a06553fba3d2c113b4f71ed62ae58c4842273357575328be9d0cf74b43d22dc2` |
| `tasks/enviar-sms-de-reforco.md` | `087b1bcaf51d50f5120f057af57537d74bd4f4fdb8676f899a295cdae7774114` |
| `tasks/orquestrar-pipeline.md` | `d368c9cefbd210eedd1d9ad507413833f8aa09286f66b19561672ace53165b0f` |
| `tasks/verificar-saidas.md` | `de24881d7378c773ad0812bd8a795416ed1e73195644f85a9feb35e316125aa0` |
| `workflows/ops-cs-dunning-recuperacao-pagamentos-pipeline.yaml` | `f48ee61113db60fdd5c0984853cbe6ec14f619ab990bb72219aa66bfc79e2b49` |
