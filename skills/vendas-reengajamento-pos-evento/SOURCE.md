<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-reengajamento-pos-evento -->
# Proveniência de Reengajamento Pós-Evento e Webinar

- Origem local: `maquina-de-receita/squads-gerados/vendas-reengajamento-pos-evento`.
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
| `agents/alta-intencao.md` | `d3239f74b11e2890ed14c5a953efd4f369bba57344476db3365bad356a2737bf` |
| `agents/argos-evento.md` | `781ea2a32b750e3ee30f64e393f367ec2740394b0d7acef3dbab93dffa3fb411` |
| `agents/atlas-evento.md` | `d4e3cfe842f99c95a4ca85663310175ab4788d26b02fcd57a5f118034e13b7e6` |
| `agents/claude-opus.md` | `3a6bdb8a8be44f1eb7da9652a64d87d40a0a6f91cf395210100aaf821dd462b4` |
| `agents/eco-evento.md` | `a90fe24bb6d7c2c9b6728a14931ec24d6938367236826954c62d5ec2030ce07e` |
| `agents/engajamento-medio.md` | `023fa97ce47fe8458b38510a0502ee2165c22e081d451ff92d8b2fcd362c4346` |
| `agents/recon.md` | `ad995be0d4324c09faa82ceb7354f634f232337f4fec5a2d9cbea0ee29679537` |
| `agents/sherlock-evento.md` | `b4b9202d1a8071efcae2a6017efddab77a3a3fcdf797b403ccf78b7456c5275f` |
| `agents/vigilia.md` | `06922771d93244a40f781ddaf70b9cd56fe24f1c033dd8b4bb7253e9b98d4376` |
| `CHANGELOG.md` | `6397d341dfc405b57a9e61f3c33776ecc73f6af064ae8551325c7c1f48aa96b2` |
| `checklists/critic-vigilia.md` | `a1c2a0d3bc2e8fec507d4b1dc2f875932fc010fbd91446b3283a77b876bba8ad` |
| `config/coding-standards.md` | `3897a2f7349dda758d57da38baf1645954183615f380eae0012955e1ae3da5f7` |
| `config/source-tree.md` | `18d4d54ebfd49c88482bd355af72deddac62796e6b74bfa4b7e949d9e8ae1d8b` |
| `config/tech-stack.md` | `4c8f2faad9a7dab9276a335ec8d2ae644e57ccaba6598b95444d4248e19f0be4` |
| `config.yaml` | `ea4417c720e4edbeaf37593a1f60597955d9ec168877d88fa1cde1d5a247b24b` |
| `README.md` | `09fc04c2a004afa13730b7dfbf7761d93b11c939b218bccab28520e3d05bb829` |
| `squad.yaml` | `366d3ead808fa23a92f702b0d12259eae4b942ae0ea460244aee9ab282fc56e1` |
| `tasks/agendar-reuniao-contextualizada.md` | `4e41e10b3dcd3e9b4436c2078780a0a813d8b2101586f611b37af387c15edb4a` |
| `tasks/agendar-reuniao-demo.md` | `1f73162779befa3ab2f06770314f4db68206f9aa90c8ea3f5c8ff36c3f965eda` |
| `tasks/conduzir-qualificacao-conversacional.md` | `cb8a542722bdaecff4484c68a5c1a6138b410c4cae4286704a2167c01ec6c026` |
| `tasks/enriquecer-dossie-contato.md` | `6b4225a6f3abe542d5d7cd5ae4eaaea8217a2cf406847e9360805d032e4cd984` |
| `tasks/enviar-mensagem-adicional.md` | `b1de79ba59780d43d9ddcd99c22f01005fddb39a0c5a6eccdda74cb74d6d4e4e` |
| `tasks/gerenciar-leads-baixo-engajamento.md` | `16e8cd35e5e3dc6669ae79d8bc832968b46ee92d7b0060c6d9518afd780c477d` |
| `tasks/orquestrar-pipeline.md` | `ec0563e80ec625a2b9f03847555bbcc45c78677caf82f0b52468abe1c43d769b` |
| `tasks/processar-lista-de-participantes.md` | `09f3c1ad848a7f6cc416ce225a3e4b21aab9e077cb1fd4810eead6c4d75359d6` |
| `tasks/verificar-saidas.md` | `86b01bc13707bfd8a3237b4c397f6ddba4a9408f78c26968cb511b0c8e98e31e` |
| `workflows/vendas-reengajamento-pos-evento-pipeline.yaml` | `d47c5b9f01aae0841ee2c9780f9bc5f08d9ee3d8ab7d1cd535e167a8f4d8694f` |
