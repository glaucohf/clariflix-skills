<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-agendamento-appointment-setting -->
# Proveniência de Agendamento

- Origem local: `maquina-de-receita/squads-gerados/vendas-agendamento-appointment-setting`.
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
| `agents/bounce.md` | `793e3faa87d4cff7c202c6de671444bfdfe2b0946fbee7b5b54f7d204872eb57` |
| `agents/intell.md` | `870e4596c1c9562f9efc5063a35f89fa6c5de640ec7597b8a6ea69d73aefb19a` |
| `agents/maestro.md` | `54f55f5f18c049f5f890f1f088dc1f16d81f40de0c749e7046808e867b324230` |
| `agents/pulse.md` | `c1b067d9334156ad5dae0ccc0addbe73a12c611934ee077f81f35b2b83dd47c7` |
| `agents/radar.md` | `8b266b0a27eff5d452d348ce23ae1a044069bc72db611868195deecbb7b47e8e` |
| `agents/sentinela.md` | `cf75405671d6234dea4d1959c6bd6985c8ed409cab3d6d777f52f4fe9343a066` |
| `agents/slot.md` | `4edf22848b97249d18f24533d898bd04e3cbeee287dd3bd13579265fd2aefc39` |
| `agents/vigil.md` | `2cfd548c96ed17b52e3cc173fe6d4eb401a5bcf36e05ed153da9c52005dd885f` |
| `CHANGELOG.md` | `7821a5cfc911039d95d53aa8221109ae26cb2c7dc8ca696e2abc258eeaf5349f` |
| `checklists/critic-sentinela.md` | `c2cf9fd2108e9fcd89bb1f6ab38f2ea76e96393ae57a61992748d0f0caf6f3e1` |
| `config/coding-standards.md` | `81e872573acd8c9f09141bc1bdb82fb3783fce40df60f0d83a8afdd7b24352a1` |
| `config/source-tree.md` | `daeeb32db1ac5a0d6e27127e06ab9c69c34274eb0963c09c492eaa3595e6bf4a` |
| `config/tech-stack.md` | `9861a46e527d1eb82c54461d6d78088f2740343529818d64b3790fd659ebf29a` |
| `config.yaml` | `baa7a62e0fad577a5f5743946499513fa88e6d36ad02113662c9d9b1fc427870` |
| `README.md` | `97586a74f4d2cd97508eb504528671a36d9a59c8a7d326a9b6eef58b969127ad` |
| `squad.yaml` | `935492a709ab1668492ed183f554deaa5cbefe4c699578580ceb72451d994111` |
| `tasks/criar-evento.md` | `2aa14c0a81ff136b85dd0d899df8e5c826022252977e906466f12b4a6889e9cc` |
| `tasks/enriquecer-dossie-lead.md` | `0fbeb94177f78ad97ef1406809fffda82d8b8798653436dd598fbb19d26ea015` |
| `tasks/enviar-lembretes-agendados.md` | `78d2f5dc6bcbc3042a12eef799e5ffd7c71fb56b60c92ad0b44e731021b531be` |
| `tasks/orquestrar-pipeline.md` | `96b5ebaff153af3da01c2dd56b8ab64345d9955867ea67e80c1bdd144dde4697` |
| `tasks/priorizar-leads.md` | `af8f8fe526d2365762c0b3e0bc60e884b32e648e64205653ff5bfd8e8ca2c0de` |
| `tasks/qualificar-lead-conversacionalmente.md` | `80f9b6a24c8f5344ca60d7a5b5ead00bb2b03a3c655194e5a4d6feb82bd31d5b` |
| `tasks/reagendar-oportunidades-perdidas.md` | `4b483ccc9d7e7f90631f1361c38cba34abbfc9742e7206bc4a2bbeeb42f42af8` |
| `tasks/verificar-saidas.md` | `36e3750235890c90cc22b6ec9765b4e58f097855827655549e65893870083d09` |
| `workflows/vendas-agendamento-appointment-setting-pipeline.yaml` | `5f99c684be6fd9e4457598edbc935fabba7d508bde09684bdcc4da4f26149798` |
