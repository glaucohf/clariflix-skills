<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/marketing-whatsapp-qualifier -->
# Proveniência de WhatsApp Qualifier

- Origem local: `maquina-de-receita/squads-gerados/marketing-whatsapp-qualifier`.
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
| `agents/kira-2.md` | `ad3c132e3fbfd0ddc9e48b74ace84d1a94e9f4f31b084c7f231ab12f7f9cd7c4` |
| `agents/kira.md` | `b027f1199e7efd9717a44eb983ae0a3a341933972a94fb5b865f3ce2b6b758d1` |
| `agents/lilo.md` | `42f3648388e6f13f90e46739048a91874618096682bd9660a8685c506e5de043` |
| `agents/mia.md` | `e1511de5e4b61da9624ccc262727b6a7700e73bcf76856299bbd637862e4cba7` |
| `agents/nova.md` | `00a13623ba8dce43db7721da62508f48b6a464a3e0736b6d9597f62897db7ab7` |
| `agents/orion.md` | `9d70af213f2d2556cac6ab469a314a83f560c7ec25733cfd8d2250b6a4e66a30` |
| `agents/rex.md` | `653b40719dd401309dc8cb6d1a5f331c64ceea45541f8c21413604427884a3d1` |
| `agents/vance.md` | `3aabe1130d7ed26e7f7a5eb1ad8d7e6de06f468f17535cea1f5a2274d874c1f8` |
| `CHANGELOG.md` | `7236e45f3e4ed287eb589bb0e398d32880f5bbb7c81e8af8bc5931e549bfe0a4` |
| `checklists/critic-kira-2.md` | `680d92abac1479c3223996eb7011f8e2a70fca885878128aa2277e137368f081` |
| `config/coding-standards.md` | `bfdd5ef23dc3e2f17b7425bccbd6f8a63a12db977a47eddca3b173b51eedde6e` |
| `config/source-tree.md` | `f26fb48ac49620c78e066d120ba17da532bc069660ab6f21da5d11496fd47f0b` |
| `config/tech-stack.md` | `a8b31f12df7473466a102e0a50397a09df2d600b8ed04ea25628f810a0332e9b` |
| `config.yaml` | `7c2cd71faa7a7213337f8143a62ea8aac811dff6b6bf88da7222f76e78a32dff` |
| `README.md` | `39b9cdfde797520c559dee047711be8edaddb7b998331ad29a12fe9a8a02e80a` |
| `squad.yaml` | `e983e9208edd9da2c4efd345dfd32a5dbf36bf37243df6c41be9eb02074114d7` |
| `tasks/agendar-reuniao-lead.md` | `15efbe534d9a70561552313286b8a18b2248a6043831eb8376cd1d29b0696f11` |
| `tasks/analisar-funil-de-qualificacao.md` | `d6bc1c21d8e44305684149a2f58381dbd2fc87db325dac967cec265b8a6ad62a` |
| `tasks/calcular-roi-do-squad.md` | `cec2eb2674b3762599a313f0159d7f07af8e5aaa48a6cb0085c0c93d73580a85` |
| `tasks/enriquecer-lead-em-tempo-real.md` | `877c4b15f636a3ac26d107e04dd8933d4fec636e8d895f0bb692c24af4015565` |
| `tasks/orquestrar-pipeline.md` | `70692f4a9853eb3af29932750d844e03dd628aa649fac6d9964d45e5a5554c2d` |
| `tasks/qualificar-conversas-whatsapp.md` | `07878f7486cf53eba16989d4a3e425dc363805a3c36342f4606d2ca1db8543a7` |
| `tasks/validar-mensagem-playbook.md` | `0866c2dc8e14c6c2179a48b8b9aaf86145d4d37ed7548299fc61a8d8efe8e9b9` |
| `tasks/verificar-saidas.md` | `dab03858f701ae02709f7a53293bb1464a4a88dc1c5022cea4fcd1b1f878290a` |
| `workflows/marketing-whatsapp-qualifier-pipeline.yaml` | `e62dceea01e088df9ba8aef48ab145fcd3cbcbbf62841cd1976432a6fba6dd86` |
