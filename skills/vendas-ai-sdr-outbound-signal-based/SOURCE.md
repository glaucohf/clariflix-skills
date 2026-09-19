<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-ai-sdr-outbound-signal-based -->
# Proveniência de AI SDR Outbound Signal-Based

- Origem local: `maquina-de-receita/squads-gerados/vendas-ai-sdr-outbound-signal-based`.
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
| `agents/argus.md` | `9c03900f4b9411c3247447149d3f76dc979cffa20bb81dc4532e79edb8d42060` |
| `agents/lumen.md` | `8e9c4ace6189b165d183d3e617ff47ae2891d488e4e5505eaa6e4b7e2271b828` |
| `agents/magnus.md` | `2e658996608aa1a6649febbe43a65f224653e8b6957f2aef06651aeb25eb443f` |
| `agents/nexus.md` | `ea1b07f36cec874a84b02a352026b05a23f8dd66a3e4ce8946add25c5bd8ffed` |
| `agents/penna.md` | `b2469d198e74643d9ca86bf454063db7b6453e4bbff6a917ff74332d2643619f` |
| `agents/radar.md` | `eac7f2fa117fb8a20a44ba7e5b631a9c9703dc69e4d0bd264d048b26219de300` |
| `agents/sherlock.md` | `597e8d00e2eff931843b5d9a4c9329921b0d9e71ac2d8a3b0742f9462102d987` |
| `agents/vox.md` | `2474513d6bec5573c209711672b3d35257edffc679f95afb6a6d3b82df770c91` |
| `CHANGELOG.md` | `a2d938bc8686568a820eb3fb694511cc9ed4d01d26cca6ed52791a5380c00132` |
| `checklists/critic-argus.md` | `701e5fd8a84ca09705a829a4a66ce66f3d888f8298ba2291981e81a7220b67f6` |
| `config/coding-standards.md` | `2f9dd7750ba69ba26ab1aa5ed7e648be7989291134d8cecccfb6f6677c856104` |
| `config/source-tree.md` | `abf1b4d9f32a412722c094d029eb85e753e32eda4910c1a5b8afbc9bcb84efd3` |
| `config/tech-stack.md` | `fdc853d33527f3211dad77cbd09299518e3e2311c1d89536b16aaef3560f5cc2` |
| `config.yaml` | `aff48d88dc92f3ed22fc99c1382e32cc7ec721032b21fd8296a8592c1109d2cd` |
| `README.md` | `bc1af7078a6cf132b8181e48b92bfc240af6718b88111d58fb85ceda1481adce` |
| `squad.yaml` | `7de690a03c47bc8218ee8b840a043d62202063983cf36e0dbb9a556cc73603ce` |
| `tasks/agendar-mensagens.md` | `e0f5788557c2474a09c0a4c4c32d495701acdfc65e253864e47c4ee760d5ea8b` |
| `tasks/analisar-respostas-recebidas.md` | `21b01c916657f3bfd1504ec919e75d62823016e035bcc80d85e6dd09ef0e2ea6` |
| `tasks/classificar-leads.md` | `a3f112b878f3762b34cf3a8dc19f6dec99569e1483b823080a09a6a2b67c6a5d` |
| `tasks/construir-dossie-completo.md` | `de947cdf1ae0531ac55dadc7c3003ba5e7230ce9e810038ca4aff29c713dce4a` |
| `tasks/detectar-sinais-intencao.md` | `5e41c920bb73821fad3b9b46ca99396d25ae179d9634fc8d33a41ffd67a70efb` |
| `tasks/orquestrar-pipeline.md` | `1f690a3e7591970145c7d8ed1b53c87ecaef6675642752aba7d8dd41cd0af24a` |
| `tasks/redigir-mensagens-personalizadas.md` | `01f02861751927a1464afe0216bd6a73af87fa76461149b95f320e063238f9b7` |
| `tasks/verificar-saidas.md` | `8eee6062b820d029e11da8d0ad13f87690072e71a76213ff55d75f2810c7a123` |
| `workflows/vendas-ai-sdr-outbound-signal-based-pipeline.yaml` | `0470b42d4fe08eb1db72991f6eb5036e2abf088a836d05e604879397de8eae0e` |
