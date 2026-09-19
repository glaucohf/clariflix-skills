<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/founder-risk-scenario-sentinel -->
# Proveniência de Risk & Scenario Sentinel

- Origem local: `maquina-de-receita/squads-gerados/founder-risk-scenario-sentinel`.
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
| `agents/argos.md` | `a7bc784afe9c014d8d1b5313c8367ac2bf2baba53f69fa203eafbf4e6a0ada54` |
| `agents/chronos.md` | `5dc1dd912bedaede5281534f58fc16066a54986f543043af278e9205e55c77d7` |
| `agents/cipher.md` | `d2e5be38096aaa89b532af15f002b04ffdf3077b734bb20096cc176afb5eb7ab` |
| `agents/gaia.md` | `4a5a2db618e9f1c6e215eb9e47b49f66b5c10bf6fbb3f15d6a9842246f532c8a` |
| `agents/lexis.md` | `9c808f2ce27d9bdd9497922e06795289604ec2d50a0da98597723394076521f4` |
| `agents/nexus.md` | `cfa0f331a18a41aacdc5b35491ed6406bf83ba008795377795ee6f6030429c2c` |
| `agents/oraculo.md` | `51c772712d76eb9aaaf604c464269344ee534da663553ae6168522f2aff4d6c5` |
| `agents/vela.md` | `d63a4864434b80e46fea5477f31fe7450f27a14330bc5dd2ceda5b308d346025` |
| `CHANGELOG.md` | `5637a291b7adb65e1bc40735fc47127bd4e5b52ef7e74a053b64f42e16abdc37` |
| `checklists/critic-argos.md` | `5e95cb6a98ebea0630b34661d4797e3253d4d26c8a81c5b3fda127e910b38137` |
| `config/coding-standards.md` | `6b82d0d553c1ab460b6faa1b275843ddec3e755978ef68b91915ee4f2c0c06d6` |
| `config/source-tree.md` | `fca84c971dc8b63a0d98d28151ec81f297e6ce5b322c623cb645939b34111550` |
| `config/tech-stack.md` | `9cd166c7855cb5e1013cae762d95b451d33616a2d0daacc9058cc96695634f02` |
| `config.yaml` | `518c929a1709c22d2a5d32de87ef2ceeeea327abf8d100c272ec1cc7b8c97b8c` |
| `README.md` | `e08e7c0c5c4855161a3132deb42aa338037ce6f3986c4db09038173b823bffec` |
| `squad.yaml` | `580d3cac8e50eb90d8db192014d7543b23f1227dcef8ee2641b6f445cfe9b441` |
| `tasks/analisar-riscos-estrategicos.md` | `dc8fec544b78539a76efd3bf0546d62315b5ad703d126f954b920001cfb1b02f` |
| `tasks/estimar-impacto-financeiro.md` | `aebedb4f2aa19227497410310c0fd0558de7ece54228c134d25b46a6f7a709f5` |
| `tasks/interpretar-riscos-estrategicos.md` | `e6d36882390fba6ea4ffca2ef70520fe5a0f64a8bd7c7bf9e831c3d659d926a6` |
| `tasks/monitorar-indicadores-tripwire.md` | `90071bd53d067e0d3aab402dde789d49ba96d02fabe940166b07ce93cd9da51f` |
| `tasks/monitorar-risco-regulatorio.md` | `12093714571cec92cdfabe7cfb5014349f04ed0c75dea0d7a697763c78894a03` |
| `tasks/orquestrar-pipeline.md` | `45d8bf84928b84ac9ae864b0fc65e0109d6c1ee1b21e95258f6a270e17d33082` |
| `tasks/redigir-risk-briefs-executivos.md` | `f8c6246786d12fa47b45a8c26000511cec2cbd90b09f3876bf6d3d3e9f6ff9db` |
| `tasks/verificar-saidas.md` | `aae23267b5b61791d386e1e40ce6673055f7fc79b92a209eccb3e9b2cfa0831e` |
| `workflows/founder-risk-scenario-sentinel-pipeline.yaml` | `b44ece9dc62ef77194d3056160e94d03751a340d4605918d2f55b02c80add24e` |
