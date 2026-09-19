<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/marketing-dormant-lead-reactivation -->
# Proveniência de Dormant Lead Reactivation

- Origem local: `maquina-de-receita/squads-gerados/marketing-dormant-lead-reactivation`.
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
| `agents/arqueologa.md` | `bece375d2bfbc576392765a34b95567aaeffccdcde4eaf2ca294f9a0958bca2e` |
| `agents/atena.md` | `9ec474f11a6fc8fa214455f30398a59af04baab4de2d5bb4e3fa68a5cafad876` |
| `agents/charon-dispatcher.md` | `7e94600dedf30244a417074afa13440af0b3f19d4726a37818d8d2eb26c81646` |
| `agents/echo-analyst.md` | `b5188f8e6508e4d0360630c89504e2a9d01515b8fe960da5502203d84898beda` |
| `agents/lazaro-writer.md` | `683d639160187791a691d0aabec9f575fd89a62a06b68a6f9dae29c35c4ec032` |
| `agents/lazaro.md` | `f339e52d1eeb30f0612379f82b61b37e68ebf2b359bb1923288abd2b8c54086c` |
| `agents/oraculo-scorer.md` | `f530fd389e7ed7dc1e872374e0eba3ecda8309474815b0f8bc353d09146affc1` |
| `agents/radar.md` | `37255987375f6b582f92ffa35c01c125d812b0f533583d05dda323552ca96a71` |
| `CHANGELOG.md` | `c646e4b5e85b1da7971d319b0b28a39ab1133d23fb2d56827b2f1f9e3318cbaa` |
| `checklists/critic-atena.md` | `c2c2ee9118c674c7cded3dbf6a3b3a68eabe321711d327329e4234f677f91e86` |
| `config/coding-standards.md` | `07084ef9507af64645fb5c121c6ba1e4ea30a47dabf443f101ccd4da7203051f` |
| `config/source-tree.md` | `48e16412fc45c4882e2b1c06375e0343c2b29c2eb7ac48e881c06facd0795c4e` |
| `config/tech-stack.md` | `42eeb607f5f82dfeefffb0b67846f3476dc3be0aa2ac31754096473fccb36bd3` |
| `config.yaml` | `bd949eacea7f18393e4905b4fe21b9682cfc5d2df85dba4e643e0232b92c123f` |
| `README.md` | `528d8f1e25299d303f354d8f1459e7cd51e4d7fba9894c56b5163bfb1ccbddc3` |
| `squad.yaml` | `128a7428d146b60cbf4e998b9f350a45101117d1c4af5ee26e8e1def2fd05b34` |
| `tasks/analisar-respostas-leads.md` | `872634edcd3b096cd5d09c653422d2acf75888e5475ed793b5f77a8ab43cc3ff` |
| `tasks/calcular-score-de-reativacao-lead.md` | `f878ec2b533ee8c6105960b3a0e6b77d314d5dd5672d285cb7a448a5d7f51c29` |
| `tasks/enviar-mensagens-reativacao.md` | `c052a424f76424c3475dcc8e78aaf653f06515aa7694650bc5de453098be0484` |
| `tasks/orquestrar-pipeline.md` | `9dc6967cb6065ee9332378bcb2717b8742c685534473641e7b5f1a76e42f6d53` |
| `tasks/reconstruir-historico-lead.md` | `982563cac6a516ccf5cc89610d0426d77b230496630a8339496bd97ee8542f0d` |
| `tasks/redigir-mensagens-de-reativacao.md` | `37363c595fc733863235c27acb43315e74af623ad4d6bee68809b8a573dd9d7f` |
| `tasks/verificar-mudancas-em-leads.md` | `fd05b000f0a03a9bd70881f6ac3877147ad8435394ea140c997e477a815dc0c2` |
| `tasks/verificar-saidas.md` | `5afcf28359a9ab1ce77bb0d19acb4ed4b354153c61ad23a6d035bfabbcb87cf5` |
| `workflows/marketing-dormant-lead-reactivation-pipeline.yaml` | `4eb880bd02858bc716d1b70c3d7e5196cb257f9ff5b04722bc1d132383c78109` |
