<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-voz-do-cliente-sentimento -->
# Proveniência de Voz do Cliente

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-voz-do-cliente-sentimento`.
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
| `agents/atlas.md` | `50760126cf7ffd095ed9dc68a2667902bb733a246e5b6c578d422a889b736549` |
| `agents/cassandra.md` | `7f8ff0869f122b9ad4344dfbea2982591063d241b7807c6794f067865f0debb2` |
| `agents/haruki.md` | `0029a9484ec110ab02fc15bde64f56e83112dee8cebff4568b8a68b8e3c8b403` |
| `agents/lyra.md` | `ccb4de69303e73257004d852b8731ce0f37714374314ec40a801cf0a1a94d83a` |
| `agents/orion-2.md` | `935907108455c08fcc1136e29b4b11940118781d4439c792964453a1addadbcb` |
| `agents/orion.md` | `be9c3abbe629ac762cfb7dfcd639cb57a26b6290e4156929949cb85481771d40` |
| `agents/rapid.md` | `341b840ee92fb8f0f0981858242d796711e3126cc5d5bba750d962002e605068` |
| `agents/yara.md` | `71fa384cd4161e431cc6f60374bc418144acc0256515c4b5a787374e0f02bed2` |
| `CHANGELOG.md` | `57d652c09811d5f90b2e1d4ee238ae304e02660839424e160e61e5a4293ecd78` |
| `checklists/critic-cassandra.md` | `6a52115d8dd7711ced9bd91a57aa62b0f8a9fccc180b62095e5a089b528355aa` |
| `config/coding-standards.md` | `baecb62b08455087d4c0f0430dfcef3c749d1f3cb71c63368d9a006526908ff5` |
| `config/source-tree.md` | `bd4a8032ca14d12b4c38fc641f228a5e40aa0bcfeb7d64e56cca4c77bbe06e70` |
| `config/tech-stack.md` | `4c3f6d153461e0adbd5afa5683ff2016472bfd64a54b29fb9f97039bfadc5d5e` |
| `config.yaml` | `5a59394507b35ddbb65ebb6f91b8169608440b0771eea79beb2d82c63461294e` |
| `README.md` | `864a5e3f1004780a93777a7a0eda0df675acfd7a24a6d13bc540f11ece6ca3df` |
| `squad.yaml` | `00752e6ad0fe01f354584039eefd4ef08b4c1447ee326640b724d1dfe0d328af` |
| `tasks/classificar-temas-e-sentimento.md` | `bf55a036875607eff78899fa33add46ac2c2524cb072ecc512d3a2d30910d912` |
| `tasks/coletar-e-normalizar-feedback.md` | `75cc9dc23f4a1e77581c3c5a4a932e88f4ee60900b6791caf123ba33568dc636` |
| `tasks/criar-tasks-rastreaveis.md` | `296ef97a7d3dcb7125e61b4a3efa10266dcdaa38544708b7ef4512a448261e52` |
| `tasks/detectar-tendencias-acionaveis.md` | `b051baaf8659eaa2601cbd7d8ab0073eb196c307c9b1eec7b1d12296d0136190` |
| `tasks/monitorar-pico-de-volume.md` | `3391fe7edb24a1179254d2eadb5fd93a34219f169a842a6272df0d2f7973dbb2` |
| `tasks/orquestrar-pipeline.md` | `42a81e39c5a5721d0d3f12c0c6cefbb15f4a036f340a6c37ff8e72181abf20c5` |
| `tasks/sintetizar-relatorio-executivo.md` | `000aaf578e2c250c07d56a6810b5902a9f454e7b7ce5d271383fc204a2413364` |
| `tasks/verificar-saidas.md` | `8dfffa2bb6d30ee5bc4956c6b0b9e3f97a2414a21f22044d54760e97604256e8` |
| `workflows/ops-cs-voz-do-cliente-sentimento-pipeline.yaml` | `c8d184bf524add2f728f9978ec38ab7fb69e2abd44fb866cf06a373b585886dc` |
