<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-followup-nurture-reativacao -->
# Proveniência de Follow-up, Nurture e Reativacao

- Origem local: `maquina-de-receita/squads-gerados/vendas-followup-nurture-reativacao`.
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

29 arquivos preservados. Hashes SHA-256 calculados sobre os bytes originais:

| Arquivo em references/squad | SHA-256 |
|---|---|
| `agents/agenda.md` | `5adac60351f12cb7bc905d6efa9856a4efbc34357316e99fd67aabffd78374da` |
| `agents/atlas.md` | `b35378127caafdfdf7e34f4d2564e0e3850ec3d598856af9924e9745cad372b9` |
| `agents/cronos.md` | `f4f5dabce142a5779cd97376630f311e4d567e78a4d14cd948647404cc8b04d4` |
| `agents/maestro.md` | `ba3eda703e69aec39054043191db4e1c2c5dc4ae32431a6e14377c3ccf1e4ecb` |
| `agents/memento.md` | `f6eefadfbcea4096d222bb62549768fac6ab275c76931754a9b53cd4a2ced2c5` |
| `agents/radar.md` | `a18a79eea4743dc8fe4bba1b8946fe7ec2a67614c01ca50190d55824fc75247e` |
| `agents/sherlock.md` | `25ff3fd143882e499cf3db70d7c5e7a1451c1c3f30a4f55a15efe0b6a38ca80f` |
| `agents/vigia-2.md` | `0e4540a4943aef1046c37ad780e4c7077adac1f9ce5a1233ba7ebbcc9dd5269d` |
| `agents/vigia.md` | `30c98fece04e80b35f8d7491d993431c3f97e2872c5cd329d82bf6c833adb722` |
| `agents/volta.md` | `c4f7aabcff1db3e0d03b312819f1095194b0d3c10b61acd0d0dec0375fb3447f` |
| `CHANGELOG.md` | `83ce58286796e84866d5fd8558b8b039bad5a7c7e546dc06251092ee07fd6417` |
| `checklists/critic-vigia-2.md` | `b95375a3c4ebfaa741aa28b618730084ef79107e6c96e027c1a54de857ba1841` |
| `config/coding-standards.md` | `21358295facc8183dfccf5c8a3193d2a8244452c3ebafff386087af97f68ebca` |
| `config/source-tree.md` | `b0b3bc38db91057b43025c36ae8bbfeb225a1926f90a3af21ce3b1c59b7e1bf2` |
| `config/tech-stack.md` | `bad175ffc2711d97657e89c338902603ed85b40190b35f52945e0ea659836071` |
| `config.yaml` | `2c017708a88a88d9438ab754647f204f2ac205c30cd684979c35f0d3b9bce415` |
| `README.md` | `71d85bab42fbd894ae250f8c29436deff1208b0715990010498e5bc72a1d0cff` |
| `squad.yaml` | `812c8a18cb3d7730a499c38b21c1f7c0a718f60af442ab2955a9538d5837ce00` |
| `tasks/calcular-score-lead.md` | `fbd1425e7bf57893dc78ab9d6a8fbc8b37e84707a78f137e11b130b85484a4f8` |
| `tasks/enriquecer-dados-lead.md` | `349b378a66ca682f7ac21836145a91d3090af613c6d356ef6e49942f582002e7` |
| `tasks/enviar-mensagem-personalizada.md` | `02c37368ded1be804f5a0c4fb6c476ce397b5a405c38761cb37606a3f1c7bc5e` |
| `tasks/monitorar-eventos-de-reativacao.md` | `4b882b221ebc108c8d1a5a0876ba512b0e17e12eca76e6a14ad5168d99df04ba` |
| `tasks/orquestrar-pipeline.md` | `3409b78e1240151f2407ce1aea3d2a19498b649d11e0fdad475aeb54135fad9b` |
| `tasks/reagendar-reunioes.md` | `b8cf7ad84fb899fc0632f173eecb4bb16a75a803f255715f143effb94a126fa9` |
| `tasks/recuperar-historico-de-interacoes.md` | `778a290169369cc09cfe7dfd41e4dbadfbf9c09d193f394c471311d927cd366b` |
| `tasks/sequenciar-toques-lead.md` | `0c53bb12b91d8bab8b24ee46f2635981c58d4fecced5b9d0f175fc26a69dfb21` |
| `tasks/verificar-mensagem.md` | `46b44ade77425b69e0f8a4fadc222ae670a3ba4625199c570efcc97e80ee5ee4` |
| `tasks/verificar-saidas.md` | `5480b505c39252169da5c52fbcf9b0ba42fdeaf3b5f47016aa557fb327917a2b` |
| `workflows/vendas-followup-nurture-reativacao-pipeline.yaml` | `ea67728e800484a1e305a3b01a43e9bceb4465451025828204789222d5339cfd` |
