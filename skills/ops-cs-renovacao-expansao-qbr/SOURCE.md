<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-renovacao-expansao-qbr -->
# Proveniência de Renovacao, Expansao e QBR Automatizado

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-renovacao-expansao-qbr`.
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
| `agents/briefer.md` | `93d1e16bcfcfae88309971bba1dfd2f9a7a81f4a9eacf76476c49cc1cd0b0335` |
| `agents/compass.md` | `b75b4b5a76fae73fca1ebacb2c6712a1843fddabf742c079e8a81fc2a29e36e1` |
| `agents/maestro.md` | `fae8abbd7c47f85d57914a34c2e7316f0649cab14280294ec77f6feecac3cd7e` |
| `agents/memory.md` | `64d7cd685cb821172806059100fe778d772c08ea8324de2821e1697af4d810ab` |
| `agents/pulse.md` | `7f232bf51e3cb06c4c4fbd9c99aa5f537f93d3377816b6358e927d6f1bf02396` |
| `agents/radar.md` | `a3eeb141bb39255df5d2ec5a0a9387355e5fcee0476b614a4f18d1c4f1eeb9a4` |
| `agents/scout.md` | `fe422f1d7e26c029f860ceda27e1fa47ba8835f97b9466d0c7ee27532eb59f57` |
| `agents/slides.md` | `e0af6a770fece5e360c7d4fa0845a91b25f3a29785a3ca038c55c53fd2929623` |
| `agents/verity.md` | `8291b9df7bc32d37a88f326c858e335d793901967d480cbe7daff19a9760acea` |
| `CHANGELOG.md` | `242788a38d175c43e1b008cde27b26cf5cd175ca04ba5f81e122ef13d5321a63` |
| `checklists/critic-verity.md` | `92ff138f5ce8ac5262411721cdc67a444eec0843617db5dd4ed4d1dd767586ef` |
| `config/coding-standards.md` | `04a9e257d34de9d8a97765eb61073b90232bb0d79774648cc8ed14bc4fe5190c` |
| `config/source-tree.md` | `8fded66c71cfa9e4f6ac2aa4c6b6ac09b6e954a2e40a5bcb9adc3367780795be` |
| `config/tech-stack.md` | `680f81d5707fb418c7fd9595e42654e2e9b2d62c8a5c2192b0c0612857aadd6f` |
| `config.yaml` | `65670fc56059daaef84dd66da4e30260f50b854b80f4bd9f5bf5798663aefa82` |
| `README.md` | `da7982b99e0b9d5cea7ff44f6f0a2b84193ef22f867cac25ea36774a453427f7` |
| `squad.yaml` | `f423753dd0aefe20ccc98a70dba91a588e48b94d1f1d7dcabc854f67950c2e80` |
| `tasks/analisar-propensao-a-expansao.md` | `a492b7fc3155545ffa1e075997847444f148d1e5ab22234b9005de02601e72b8` |
| `tasks/arquivar-resultados-qbr.md` | `b98c24a6a3c8483705bf15615d59318c10257e968dc60f904f21af063fda6e67` |
| `tasks/calcular-renewal-readiness-score.md` | `a036140f828584a9ee706af79f9ce12aaa8e937abf8998d4f521f772abecefac` |
| `tasks/criar-pacote-de-renovacao.md` | `a432c522f6cca3067588179cc653f9f5810330e919059aa5a7b9569c8f30c8c2` |
| `tasks/detectar-sinais-de-expansao.md` | `a093894d4837e262ccf34e5518d25d9364f1ba07f46992e6970e3f4cb4806176` |
| `tasks/gerar-deck-de-apresentacao.md` | `e950df9f2d5e744f79f072a31605959d82d08ed29d6faa9b03c9e9b3816e4176` |
| `tasks/gerar-qbr-brief-e-renewal-package.md` | `03f930ab712c06f7ea3ec36ca4b252f89c79495744904095e3a3b6d8ac35e86a` |
| `tasks/orquestrar-pipeline.md` | `48178d5b451388bb298efd9c7bfcc0d00587655b50f03e11e5335dbf5e7d99f3` |
| `tasks/verificar-saidas.md` | `6704d92cab5ba1a4710f310758a6fa5018f217a4cf07a85588f922b1f6790ddb` |
| `workflows/ops-cs-renovacao-expansao-qbr-pipeline.yaml` | `f9ea632f3b18dc6a1f3a891225604523ae2240c218656606079beff8d2de2dce` |
