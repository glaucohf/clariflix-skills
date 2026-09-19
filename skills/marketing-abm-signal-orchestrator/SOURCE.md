<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/marketing-abm-signal-orchestrator -->
# Proveniência de ABM Signal Orchestrator

- Origem local: `maquina-de-receita/squads-gerados/marketing-abm-signal-orchestrator`.
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
| `agents/aegis.md` | `db821fb4e95cc8d042693e0556dce6136e346fe6cc5a96cf9ef2b0e02ad69b26` |
| `agents/atlas.md` | `dd8222c24f1e13725cb9b4f41875950b2b5094303bac869bb2ee3d5704e2b32c` |
| `agents/chronos.md` | `f1d11ab680f189e952cdeb5615b16f571d797b9c7fa947333c805ae4b98cfb67` |
| `agents/hermes.md` | `4af94e7c5cd69eb9d206460ec0d869e2d47b9aa582f335ba001711d78effc470` |
| `agents/nexus.md` | `8901f1cf9640884249e5a32278616f0682c098fc2e93d69f6c21ca0ddb242dfd` |
| `agents/pixel.md` | `d2ea029dbaae42a44cc7fd2c00684918b42f20e26e79764805b796d52667884a` |
| `agents/prism.md` | `22e66b15a7b5c19d0f4cded03487badfca70eb107b5ffe2f89294b4835b98d67` |
| `agents/radar.md` | `6dba18b822af67372d73f3d8f2e22749dae157e714b676985336cafee833beaa` |
| `agents/vox.md` | `526972961a70adbe550799c4a1bc97ab10a419c2a94030328491d8ea85d1150a` |
| `CHANGELOG.md` | `44c5d54c59deed851db63ed0bfce4bc7df19531bc6a4a64b1ebf0fe726939497` |
| `checklists/critic-aegis.md` | `9970bf3a7a41d8fdaca3baefc9836d4e61af673be0db5ab1d563aee50b1e48be` |
| `config/coding-standards.md` | `48529daa57b490be7f80e06bfb94cd4112fd7864bc0182eb6d3272a53e34c6c4` |
| `config/source-tree.md` | `683b00eb6a34eba95f36bf43963edcf763773efde8e63325c29a4619b8a85ff7` |
| `config/tech-stack.md` | `a89697a3aaad27a82463c8d2eaf265564a2cd7ca385b4685e16cca4897cb6a8e` |
| `config.yaml` | `481f54ec0b57d83aed96a6a5ec414464da15c2fccc9d8d3155fa8a464ac19064` |
| `README.md` | `4e8bc490f70a32fdb42791404f389a7a43d27cb0868240f10048d6c29215fa72` |
| `squad.yaml` | `c135cf8d1e74c00964763bfda8c4401829de9d5a4f509ab21a41edc22e6aac88` |
| `tasks/consolidar-sinais-engajamento-conta.md` | `e67dd969cbc4e7cab35ce733fe2d616c736c3608bb12d7bf36e32ccdcf0aad1d` |
| `tasks/criar-audiencias-customizadas.md` | `f8c57c3b7f95fb63ce59a92533ab08023a5d20bc32787aa475377f285db951f8` |
| `tasks/enriquecer-conta-icp.md` | `00f3740fb71887d099e3284c01f8f4577aad3f3b1c128eea2f046b613a714424` |
| `tasks/gerar-copy-personalizada.md` | `a752ed22c5d03aae58bf797976c2b65d72daa76a1e1d6d407fc0c2b8ad434b12` |
| `tasks/monitorar-sinais-de-intent.md` | `b7d6b626857b960d0ec1be0b4f27b17c5ca9a06f0526f707bc427198e207c38c` |
| `tasks/orquestrar-canais-de-mensagens.md` | `f6621de74b3113bc78947b6711f5c818b4008351513c05508743fac3717eba96` |
| `tasks/orquestrar-pipeline.md` | `b3f5f379c77880e1e8925fd28634c2d1096ca5131970a5eef7215637fbee4ff2` |
| `tasks/sequenciar-contato-multicanal.md` | `47309a586c0271392589411056c4c2826102ae200338dca82fea04a9f5e31011` |
| `tasks/verificar-saidas.md` | `685eb4c46a7afa92f43035edf9a24506f2d344c2fed6ffa7294ac93a0fa76d4e` |
| `workflows/marketing-abm-signal-orchestrator-pipeline.yaml` | `d180aa1d0f58cc33b36d1d8ccb232e3dd7ba784572df0ed3cc8e80bbd24f6b63` |
