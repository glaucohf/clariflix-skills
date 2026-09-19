<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/marketing-intelligent-timing -->
# Proveniência de Intelligent Timing Orchestrator

- Origem local: `maquina-de-receita/squads-gerados/marketing-intelligent-timing`.
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
| `agents/aura-2.md` | `32d1291fabeba5da021e00a3af320f0d124ed914ddccb6ae8bbe0644582bdca2` |
| `agents/aura.md` | `a8937aaf1a12f1b6cd60e0a84397af8d6570492b4be7adc5a690a65a65336a4b` |
| `agents/helios.md` | `385a3b31a9c8c0ce01b90a9b45c90c1954b375b0d253b99931d30598843f1dd0` |
| `agents/kronos.md` | `a9eaceb4d53f72d35f8807cd30e6ffc6efe8101cf27e30b8a7c3a3f12e80c66b` |
| `agents/lumina.md` | `c60c386c5589d4e740985ce0029c07c1f52dbf6eb0a3c81440aadf948b768269` |
| `agents/nexus.md` | `e555ec6278f615aaccc01a5a14a903a3133613f8db1978c6f746f26dfadbdfb1` |
| `agents/pulsar.md` | `52c13d930ac8e863956fa9019b6fef7cc5a633a662404f3b0174bd3f567ee901` |
| `agents/sirius.md` | `740eb2c7bd5fcf8bea50d0fae64a08095986f099c50e9dd2f2fb0c44f26db002` |
| `agents/vega.md` | `56a39d9b5cfd8848e4cbb7b08157d08e23c12b52e792948f76f3d9ae4239dace` |
| `CHANGELOG.md` | `f32b96904bc4e955f75d083b2c099771ad05dd80eee346e3ee712073deb47b34` |
| `checklists/critic-aura-2.md` | `c96cfbbbb3989d268cb0825282856b3a3068f71fb1590e4f546b2f369c3ce94d` |
| `config/coding-standards.md` | `2db946ae5ca9c69eb443962a084536585ed0de9444fee3241ed41e61ec52e69b` |
| `config/source-tree.md` | `5f95a3506c0cc95b6b7dbb934cfb5e7f3fe08627e766f4e3a80c35f646d0164d` |
| `config/tech-stack.md` | `34850a83b7202c2b02633c2cd8d3a22891e18af1278f8afd81959c3d29bda625` |
| `config.yaml` | `4b9e99bd5e8e47850c06a3f4851fcc5774d1459a099f2cc7c2a5572dda472203` |
| `README.md` | `857d5ee12c95a035ba639bfb30a8efcf91180e2fcf59e837b30f7d7e7c49852c` |
| `squad.yaml` | `54cf183bc55d883ca2f058a8f725377f93b37222abc6967d94b18f943e90a7e3` |
| `tasks/analisar-dados-de-envio.md` | `78ef6000093a8c6557a94306c06a40c706cd4d34fcd300ba8355c85ff1b3c68c` |
| `tasks/calcular-janelas-receptividade.md` | `38048c1121c7b81aeae4edffed2fdc01dad4a31e0371e80f030f20af0b22d8e7` |
| `tasks/construir-modelo-preditivo-timing.md` | `b12d41b4e336dc6445c8e61674a38edf39512e5ff93ace239ae4db53314bcafe` |
| `tasks/enviar-mensagens-agendadas.md` | `d1534d1116b3ea97d34a9dceccee50721b65f17cf616bbcb8a5c45ade813acc9` |
| `tasks/monitorar-saude-de-canal.md` | `9fe753ed54fac5ad32bcd8ec1538dcebe9de32682ceb32ad2cf4a3739779b0c7` |
| `tasks/orquestrar-pipeline.md` | `4f6bd11dfcdc066c113237731a859e049263faf5b8d3648b8626a3a74c841299` |
| `tasks/otimizar-sequencias-outreach.md` | `4eb49e1c84f8da32f5134b35c8180d6f8a380870b689c4b73f1ac3fa37a528d5` |
| `tasks/verificar-compliance-e-qualidade.md` | `68f211df13c6767768547524e832ca4df2121acf06d0d57dae8d5e117309d39a` |
| `tasks/verificar-saidas.md` | `d3fa4e5c5824196f203426e732e87507a7efd3665ba978ac307f668ee8842f70` |
| `workflows/marketing-intelligent-timing-pipeline.yaml` | `80d8e8f86116784ff2c474929ee95948253b4a93ab8c9ace49a2cf903838239b` |
