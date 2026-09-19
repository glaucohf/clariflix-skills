<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-objection-handling-qa-tempo-real -->
# Proveniência de Objection Handling e Q&A em Tempo Real

- Origem local: `maquina-de-receita/squads-gerados/vendas-objection-handling-qa-tempo-real`.
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
| `agents/argus.md` | `a501d6652e31153369283ccaca2b6781ecf762498795ebece676958eeda89012` |
| `agents/arquivo.md` | `94d4c2b680c00c5f86523c29d42db9fecd290f49e14e9fe1b18686e484171cba` |
| `agents/challenger.md` | `f3e38d59d37fcdc70d564d6274d239e4e7f380f48844df76f44a54414c9e0e66` |
| `agents/closer.md` | `b13762b9470fde12e5acadbeb360a8124c59c65180d897c063828a2bbcc9680c` |
| `agents/maestro.md` | `53709446fc6cb6927ca7fa548502f4a1be88688882cd1a174d8d271f4cc6524d` |
| `agents/rebound.md` | `a30c76541007bb9a6ed1a4792497ceba54f3054a9a0aa46a263ab35d0d10a3ed` |
| `agents/tecnico.md` | `90541acc15f963d22353d7f81123ba6b6efe9bc70b8a69bded81436fd7d63b8f` |
| `agents/tempo.md` | `0fc27b2f2e509d7d1fc19236bc7c059d13c5faf02cba203c34b24956e24fe274` |
| `CHANGELOG.md` | `a7fdcdf729df828a833058c5709dc3247f8d0e89394376f0df29a12073d2df82` |
| `checklists/critic-argus.md` | `c2e166695a25fde99c8f805b20c659fc1638e07f645df0e76a9f55c34587b798` |
| `config/coding-standards.md` | `26c2c2968aca23420d22afd83fbe5251de1d3232adc557608a95a10b60069ada` |
| `config/source-tree.md` | `4864f4e0b8752a440898c5e381950f107ccd2668c6f82b9d5dc91c0a61e14c00` |
| `config/tech-stack.md` | `1fc352ec2145b5fa2210aba70399eeb829e64b0eeeb633676576a315b92712e2` |
| `config.yaml` | `3b16fc63d911701622b4dc6fff32e2c3c1bb739ae86f2b23bd39624e1eb2712f` |
| `README.md` | `958ba3ebf3cab80773c1d58e014294c97bd59be2750b68b327dfbfa9a80aac49` |
| `squad.yaml` | `6fba21e926d27bfe6ef66740f6cda02b6db02cfafc3c81072dfc28f1d8bdf000` |
| `tasks/analisar-objecoes-frequentes.md` | `4d6fc24f7774b0ad27c72345f2735815d7f22e62050eb33741ad5de65f362b63` |
| `tasks/orquestrar-pipeline.md` | `9f263e0fef5ff7426838796de75d951d2a91b8bf4e95e4a7d2cf2b538d7bf513` |
| `tasks/rebater-objecoes-concorrente.md` | `1b7271aabbd61348ef6e019d6c73d5f005b1879b361263c8777fffe346b197d5` |
| `tasks/rebater-objecoes-de-preco.md` | `4717b4f4cdb7aa5adefd45e7e869b4501087702b464059108b28a85a64489d21` |
| `tasks/rebater-objecoes-timing.md` | `960c42643e0dbc64218f6511c8a5b932b55c7205804771d560a6994f48d411df` |
| `tasks/resolver-objecao-autoridade.md` | `7972accf350e0ac483cb930b7a208291c48f960d2ad61bf07066cccd3d157523` |
| `tasks/responder-duvidas-tecnicas.md` | `242bb14178068eeb9bedd8d206bb1a8642a833043843b022b0db44ae79548ca8` |
| `tasks/verificar-saidas.md` | `7d0b0c0bd9c97ae36d3b1e2cfc299fce26f767f0093806c8284fe530ffef6c59` |
| `workflows/vendas-objection-handling-qa-tempo-real-pipeline.yaml` | `628cc7490b1544dbfec9c8cdb7a5a6ca21f0ab8f20685e3747d7f888f2fbeb25` |
