<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-sla-health-monitor -->
# Proveniência de SLA & Health Monitoring Operacional

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-sla-health-monitor`.
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
| `agents/alarme.md` | `ce77389ec1efd6b05d90694eec223aab645a618d98ae003fc074493d802b3a00` |
| `agents/ancora.md` | `80ccc3f1064ccf2964ec26f363fdaf04649de34c04d9bb8a25b44b56ec9a03b4` |
| `agents/cetico-de-sla.md` | `5431abc0928362b8d0d5876000d2e06f2574ae073cd6c52b1b5f16b6abf144d1` |
| `agents/cronos.md` | `8b36aa127554b4645a15a601e1ec73234f26e18fb5e432dc6fe87fc5289a4c95` |
| `agents/decifra.md` | `a1bfdbe9a01aa53b1e3e5e96bd89d6603730cdead04f5907456eaea1b7ae1916` |
| `agents/histos.md` | `3c87018dc37e9dabef6823e45f2b63b86991ffae6519d1caa7a9804713e958ac` |
| `agents/radar.md` | `9de75696fb4bff6e876c03945675037e3303ab1b5965b681bbbfe6ad48533745` |
| `agents/sentinela-mor-persona-vitor-analista-senior-de-operacoes-com-obsessao-por-sla.md` | `60118bed15db6579fae3b753d2046d1dc34e67da5792a0bdb9f9fb53c2d695dc` |
| `CHANGELOG.md` | `b7f4f4c9f4b1a204ed0bb12548e21c7a90ea1279fdd3f6d6dc9457454af0208b` |
| `checklists/critic-cetico-de-sla.md` | `e6de04dc63711d7fb6bb8deeee6e4a39037b9a2824270074f46df9e248f5839e` |
| `config/coding-standards.md` | `cd714e90318e1a0267c4ae505f7d2e653e40f2d6ab7f11ce4fac5b4276a19b09` |
| `config/source-tree.md` | `2a38c176782436c8e90b9d32c0784282dc6b5ca5b11809921aea035051b6a90e` |
| `config/tech-stack.md` | `a45a665623a75953ff3eabd8f2a22c38d1a9faba6666c96d4d96e80ba93b7c54` |
| `config.yaml` | `b0e6c640071bca7568201ed93f8c3d6f127c9dbdf134e191e28642e1095172a5` |
| `README.md` | `613076fe5f5604de9f146212cee937903f8689caced49bd9f73acae986d5dfc9` |
| `squad.yaml` | `df91ac7686fdbd444e4c4d24295ac9b73221fb7473a4255c9c8946b4c3502c5a` |
| `tasks/analisar-dados-de-sla.md` | `fed1d0ca3c7ff5ff0142c4e9b575890ae088f4d85f78a0d483764888e46eae6f` |
| `tasks/calcular-complexidade-tickets.md` | `ca1e7d91c5d1ff0b7e5562712d6edb99754b2a2602d9e00f5812e1a1c6efd291` |
| `tasks/calcular-probabilidade-de-breach.md` | `bcf4fac7ea4e9d4c37fe1aaa16e7a3e9c820ed0d4b7732b74c425670beaaf819` |
| `tasks/coletar-tickets-sla.md` | `987b19de380259d2d4c7b44a33564b5c921aa6606d4e1620bdd3f446718b0a52` |
| `tasks/escalonar-tickets.md` | `b5963076b729f61de01e1cb52eab5357c6b5009f4664be17394cdd0992fd1539` |
| `tasks/orquestrar-pipeline.md` | `91f93a18c27e5f6fba01697f28986c4da217acd0a830f90a58b769ef42229187` |
| `tasks/registrar-prova-de-trabalho.md` | `3f0b178130effb926fbf7b86585883a32616b65eb712f839ffd76745d073e560` |
| `tasks/verificar-saidas.md` | `a8753823d961ccab3a6e425f9059ef4eaf0ba4a55642af492d522257f392c3ce` |
| `workflows/ops-cs-sla-health-monitor-pipeline.yaml` | `425e9089fa16ab4ce4b471faa1bb54d7c8a38a60a777a86ca4b210a83824ae5c` |
