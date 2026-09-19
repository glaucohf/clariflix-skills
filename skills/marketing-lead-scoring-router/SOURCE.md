<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/marketing-lead-scoring-router -->
# Proveniência de Lead Scoring & Router

- Origem local: `maquina-de-receita/squads-gerados/marketing-lead-scoring-router`.
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
| `agents/apex.md` | `fd7d2c2b26108c848df5ec632d834bb09bf482be539a5459cf3bbe1530755195` |
| `agents/critique-2.md` | `320f235b30e42c2ccb100815a0902a551fdc3002a5f08e773ab845b1b72c27a2` |
| `agents/critique.md` | `62b4fa13a05eddc35b22f0034c67d62b690e4cee922c9805a82b7a1ade54db76` |
| `agents/iris.md` | `f5ec7d9fea3dd03022f815b702aed2c3f625691505c8d6698fbb03f64374b495` |
| `agents/orion.md` | `5bd32542067db0dd783a97732843aff678c453d1628dd09e4c55a27835e1c108` |
| `agents/pulse.md` | `64ddd43770b2c2708db1ddf61f9cac4e47351eb5822a71dcb5b173dfbdfb2b3c` |
| `agents/scout.md` | `86dd4357c1f694c7092c469008c20d9d8a0d899f37dcc1b3bf73e07f218d12da` |
| `agents/vector.md` | `861392e38a95b9e02e2bf42ccc7707abe31e5ddc4d08f9e1c457567f3f3e56cd` |
| `CHANGELOG.md` | `c866527ee478fcc3d4551d3bc7f11db44b4730a3ec0aaf86267e384eaba206f4` |
| `checklists/critic-critique-2.md` | `bdc851110b5d74ef324ebdc6bc1e8ea1f5436fecdd29f0c98ff5d14e1f950b36` |
| `config/coding-standards.md` | `9fec311a3969b4b896af9023878fc710064fc0c6fd53ee43434e2857ff4b52de` |
| `config/source-tree.md` | `426f9a5899ddc96957199bea3f9866a856d67021492e144845b1a14598280877` |
| `config/tech-stack.md` | `4e0368c461d015a1b195efbe971b4175f269f305df76ffe8224493a5a01b5eb0` |
| `config.yaml` | `3fbf269c42943064fb562d0bc3cc1bfc9a3956d7cdc8b2eb527d33d90c1337f2` |
| `README.md` | `f596a316364fc76815faf75fcd35caa688e50fe6022a34fb0c09916c943d28fd` |
| `squad.yaml` | `7cce2b093e321e7d46bca9f90037a0b35a9730b4f60cb73ccd6916df2ab8268c` |
| `tasks/calcular-score-lead.md` | `f2f4bdd9c7ff44be7420aab6d600305c5e767b425d7ce765cf8e4679f581be2f` |
| `tasks/calibrar-modelo-scoring.md` | `36baf2f43d86ad5ed67d6b1036120aa0ea20367fd4d8f1cf7a9c222519f7d4cf` |
| `tasks/enriquecer-dados-lead.md` | `64707bfa4250c32a4dfc8cd3c9e0840def68efa7e3f862d46eb1f29ed42c7b91` |
| `tasks/monitorar-e-normalizar-leads.md` | `d66146dcc5df5098b7e773835546f071014fa3eb9b61bdedc7fa51660a91f5ea` |
| `tasks/monitorar-pipeline-de-scoring.md` | `63c6bedb4eb25957b80192f83de26d90d9b77bb07ef515d648eb83ab24734272` |
| `tasks/orquestrar-pipeline.md` | `0cde35bc508f6e71423836a5b78c4ab1b65e4fc0f52cd4a3108fb0e6d3222fb0` |
| `tasks/rotear-lead-para-destino-correto.md` | `69e4602d25bf5a28867a065eaf663c939c85d6238916de9db05b4c103dca4c78` |
| `tasks/verificar-saidas.md` | `3f3b3a07bd0dd416bcfd70cb73ff962f7871ac13dafe15c478576172f9c923c6` |
| `workflows/marketing-lead-scoring-router-pipeline.yaml` | `926a7d75829a6a8d6d0ff515d76d4837d1b2e0c4a5396cc47e8557e607bf4875` |
