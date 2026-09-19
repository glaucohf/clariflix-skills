<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/founder-kpi-okr-pulse -->
# Proveniência de KPI/OKR Pulse

- Origem local: `maquina-de-receita/squads-gerados/founder-kpi-okr-pulse`.
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
| `agents/argo.md` | `b0b8abf3b0007af24fb10d18ca3054438e02491a40500f68244413cd1a3a9a5e` |
| `agents/atlas.md` | `3f96825255096664ab6e73fcf20bd9790fd10c9855d5dc8934a884652646ce42` |
| `agents/kalinda.md` | `78a6dc8c6e03773d1273fd06a43f590bb3942fecc9ee35beccace1ecd5a95c13` |
| `agents/pulsar.md` | `4c721b511ca3a1663b8f2eed391edf91bedfb05cabb3bb284bad91bf0d0bcd65` |
| `agents/rex.md` | `dba5321f8acff8b03c7624c6109878187e53e7677aac8728bff1d438ad9ff3e1` |
| `agents/sigma.md` | `ff0be0c68f3d69beaae2ede85a47b939b0944a68b95a1b1542d08a6979642a21` |
| `agents/vera-2.md` | `2fa80008a873d39a89df5e02b01fb987388d738437f37c95ded627a150b0c079` |
| `agents/vera.md` | `ccc0788b806a1f8df8e0e65b85d1ce53e1b4b95e0b6f2a660a5cb459f6199598` |
| `CHANGELOG.md` | `3cd86ace8b4f30d8d1e1a48fddcde56bf325f1f915f832aa21ea032cd1a0be32` |
| `checklists/critic-vera-2.md` | `47cb6979358a9af6a02816bb59d0adeec9b31f8e39d612c34a514de5335aff6d` |
| `config/coding-standards.md` | `be312116d8bc4598c8fc4d8d28208bd5ca14840bfe33e8d6633791cfc36d49b5` |
| `config/source-tree.md` | `cad5e0708f66318dbca79593e621652809d0e8a9796f41f4dd5a6de21e445f93` |
| `config/tech-stack.md` | `53ec4b81bada493087811c2dab49f33d8787768e45cc96b3b324d57d88ff4150` |
| `config.yaml` | `a3c76c7a8b4c4c68a578affd586ff4f15698ad32d7b793e7ecd9c21868080566` |
| `README.md` | `88aefb08c0a6faf04bff2f883baa7b6e64d98502f3f2d59a6139a77467c86b58` |
| `squad.yaml` | `bd8cec05ffda3599ed0ae874521e3045e65fef1b121af18e28e7433c73c39f61` |
| `tasks/analisar-causa-raiz.md` | `c6c8b5a458648c24a5dd9811b7b26fe709d3bd6d02fa119bc1160ad9e5732c21` |
| `tasks/calcular-trajetorias-okr.md` | `44d69e30953466937017649dce148b2cf34da1722f7159ea43a82400c5ba48a3` |
| `tasks/coletar-dados-kpi.md` | `f7af48360fd2ecf2509b52a7458df6d35c5b3691b9ff4942510064b803a73d25` |
| `tasks/gerar-recomendacoes-acionaveis.md` | `ca48664955ed498a2978f258ee2f120e1afd7c27a30ca6d2a19a151804961ff1` |
| `tasks/humanizar-relatorio.md` | `5c2a0565425832fcc4e5a16502b0cc68b002ca35e9f15c48b2ef979647f5e123` |
| `tasks/orquestrar-pipeline.md` | `5f85d3d848ff3592ef7024a02147f638c5f9cf37ffc00680be1f1ff5af87188a` |
| `tasks/validar-dados-plausiveis.md` | `8682acbc42304f3062577fc55ff357c190a1ea572891281aa6ffe2b147e3836e` |
| `tasks/verificar-saidas.md` | `79c403363dba359fa218dfb1b415de4a506961e502af08c04e664ffbe995fa97` |
| `workflows/founder-kpi-okr-pulse-pipeline.yaml` | `2f1acc3efa4ef0051cd21d6633ad32032873b6fd0c68092e2ad7fc656841530f` |
