<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-voz-ia-telefonia -->
# Proveniência de Voz-IA para Atendimento Telefônico

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-voz-ia-telefonia`.
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
| `agents/eco-2.md` | `51e00166617dd99c202e43945c01361926b16326b136535470402109a58f868f` |
| `agents/eco.md` | `a8cb7c5f0648b8fd1d48a7d7fb2f09fd1092d13533f15880ddf8d369fa348f49` |
| `agents/falco.md` | `81d1b0417f75e8b0a1428729514718a46bacf371a0e95b441bdbd3bd43634c71` |
| `agents/hertz.md` | `e7a244e77cf140303053c4bc18186ff55c8ab5d9f8fa502968a230d9a4bc4924` |
| `agents/maestro.md` | `61e5b2507ff5040f3c9691790fb4fee28d12e4ac62d67fba38a3623e935af8f5` |
| `agents/onda.md` | `fd6d84ec65b0e8bdf60c68ea632fe893e67142cdf8f524a750c9ff73c4c63849` |
| `agents/radar.md` | `d473fdb6f8aa64f6ad105a638db6d23de596143f3836b6091fa2311227f7ecd9` |
| `agents/sono.md` | `6e7b705adb2ce0fdda079718db5c315aad1fa55f0bec94ef4d0003dc58397c11` |
| `agents/vivo.md` | `2f46bc14be59d8afe81a9f9fb7e8f59aeb35da1866886700e89865c0d657367c` |
| `CHANGELOG.md` | `5cfa5dec4a5d984c9f14f3c89eb7ccbe19f4afc0a3f9fb5da335d5f157b6cb8a` |
| `checklists/critic-eco-2.md` | `c80189fa822bab4236a4c92b502367f9b2a98e7398f668cd7b926957d838943a` |
| `config/coding-standards.md` | `95bf43ce2adc9225c8fbfa8681bb7f1deb2c6a7b4dc6c973ebce9039536146b0` |
| `config/source-tree.md` | `f6f335d86fa7dd640c10796a384c7a4e6e75e55644c81b26d25aef1baf088497` |
| `config/tech-stack.md` | `003099b8670d433d655772b607b4ab5d0ff2100fa9efd3f9e954866d71392d51` |
| `config.yaml` | `613404add509f4cdb665b1df14bdb062ce963297fbc51960ed87daeec1f15f4e` |
| `README.md` | `806f460a81550c850c6c2a0eaef8308ddb3677aa1576142fa2c2e193d6a2f146` |
| `squad.yaml` | `e658c8089a1f29ad96551fe6cb2afb7af6ff40fcd2b831eceabf412d5cc8766a` |
| `tasks/analisar-sentimento-e-risco.md` | `625d659f7f26e13d37bab54b7e8bc5391e8baf884b2ab69dccc059c549a940e6` |
| `tasks/coletar-dados-necessarios.md` | `6a2e7717d3619e0515cb812ea77cb7baba9ce388630b6e32ad364241578bf158` |
| `tasks/escrever-acoes-transacionais.md` | `6bb809e3594b32076e3fc501e862f6d0472bb21b6256dcbc88ec71a8bb5b8bff` |
| `tasks/gerenciar-transferencia-para-humanos.md` | `cd3e6f19f8e253ce6f0bf6f81437cb9ee28e4e46cb7f89663791aa0e5041ded8` |
| `tasks/orquestrar-pipeline.md` | `2ea3bce4f57b56bc1ef3aa33e366f909ce641fca456d535e7232fda2e9500ff1` |
| `tasks/resolver-intencoes-de-voz.md` | `cd909368344992c93aa27cda77349097bbbba6d8dc08b3c81c4a29dde12dc301` |
| `tasks/transcrever-e-normalizar-audio.md` | `80c221f968a569faf06e163555399d4d2b2b2afff35fcde8232343ba516331f6` |
| `tasks/validar-qualidade-de-voz.md` | `19d9b82e1008e38e65079216188570e302b3d17d0018b4e0a8532404392eed44` |
| `tasks/verificar-saidas.md` | `8375d0b48fce47d0765ad6e5a8a27ff5f0152fc364d2678dc7d1c090dd0e2930` |
| `workflows/ops-cs-voz-ia-telefonia-pipeline.yaml` | `81cfdcf9d58161b1c04f8a803bc36fa378171d622194148a17bd6488c9b07761` |
