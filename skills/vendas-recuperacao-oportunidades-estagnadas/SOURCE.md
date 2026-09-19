<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-recuperacao-oportunidades-estagnadas -->
# Proveniência de Recuperação de Oportunidades Estagnadas

- Origem local: `maquina-de-receita/squads-gerados/vendas-recuperacao-oportunidades-estagnadas`.
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
| `agents/arquiteto.md` | `ce9815880a2a14d3a401628b9e8166c4c10d818a3da696ec2cd1b608171072a7` |
| `agents/critic-e-verifier-de-mensagens-2.md` | `6b56dab89d3c032df762846f3239e8c5532f7ec106f034fb6eee43b5c09285bd` |
| `agents/critic-e-verifier-de-mensagens.md` | `d3398a782f8f6cd8f36bf27cd9baf2a3996e3e5278a252fa505b6dd180678fa8` |
| `agents/escavador.md` | `16f5f67e6eeb4b849be738c7f1dc2a9f1395ccfd1e0901c289921f580b0b7784` |
| `agents/forense.md` | `715dcd74fdb691cba6a9664ad881fa81477a7bd299f3b9040c8e87cb1176049e` |
| `agents/monge.md` | `d04cebac5908f58df2e8e39174577c18f594606601dfd5c6dddc9f2ed3c44cbd` |
| `agents/orquestrador-de-recuperacao.md` | `e11d62f7914153473989e672143df98c89c780959a76aca94e8d9325de14ecab` |
| `agents/worker-de-deteccao-e-triagem.md` | `6054ce7587d870ea13b17e0433da032a7716e0d514c47e9f2a04d05e0c34f009` |
| `agents/worker-de-outreach-multicanal.md` | `77887787b0ca80abf4538af1f503f9024d894cb6dd02497a4a08e8517536bbef` |
| `CHANGELOG.md` | `bf369338ad877a788093f60358c17246f6f5614b099c8fc8b581ccde39d4db0e` |
| `checklists/critic-critic-e-verifier-de-mensagens-2.md` | `135f1e798743c51d9ed89d6cac74f20120eb910ca8530a39967ac8395794aca0` |
| `config/coding-standards.md` | `da51849d7811f63189615d4785e967b04c6e46d509bb56144bcff8345a3f090d` |
| `config/source-tree.md` | `a01be074c8ec42134bf5723e76c0ac1baa05d46aee3b9172456f086437c50acf` |
| `config/tech-stack.md` | `7f5fd09e083fed2154beef92182a3c698676935dbb54e6c682855fee59c353f1` |
| `config.yaml` | `8d9dcf7e2e8379555f8d6864d4f6b2b484faaf21c2f2cf1bd87921e5a6a3fec9` |
| `README.md` | `ea8b5efd12ec2ea835e1440c1c97ab2c0f4420382a9ae9596f70f1697dca7fa5` |
| `squad.yaml` | `6e13d902507d7dde8b959c2f78b4ab4fe0ce880544ad3e10ee57a39be587f037` |
| `tasks/analisar-abandono-em-etapas.md` | `d7726c3ef5dec0074b4557ffc450de46161b663f6cc01e7573689eb604d3c1bb` |
| `tasks/detectar-sinais-de-estagnacao.md` | `4a4ce068c2e521542e1ae4b29b78543f12e53c556293c2534aca66b815f765d7` |
| `tasks/enriquecer-contexto-lead.md` | `b915f5498c819a6df80ac16a32824872490afdb399902dd58dcf12108ebff0d1` |
| `tasks/enviar-mensagens-multicanal.md` | `477a32c9bfab06e9e324b03f93683648994987d50c0fbbcded35ef2474a13df6` |
| `tasks/nutrir-leads-longo-prazo.md` | `97dc2e23fd4c7a611e6bd212b2b86caf843e7ad4c7479e93f0680d89a7765bf1` |
| `tasks/orquestrar-pipeline.md` | `6e72a4e5b031202eb824aec5d0d2ecb885139dd24dd2707a4df9e1f4a47d31b0` |
| `tasks/personalizar-sequencia-mensagens.md` | `56dd5c22bbdf5ef6eb5b4e42094768bd9a6f851eecdb3bcedd6cdbfb86c943c2` |
| `tasks/verificar-mensagens.md` | `87f84cf441d57be9fc7efe407da8731262bda0f317d6f2628e5f766214455551` |
| `tasks/verificar-saidas.md` | `8722c0c720661d5010a6e5d3b096b128fb7fe285d36d41e752a12c9556107ef6` |
| `workflows/vendas-recuperacao-oportunidades-estagnadas-pipeline.yaml` | `fced01596210641362b4719b486a41823aaa2c6f0f40114816c2feb1defb08f8` |
