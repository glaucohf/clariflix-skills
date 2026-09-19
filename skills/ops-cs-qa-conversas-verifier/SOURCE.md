<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/ops-cs-qa-conversas-verifier -->
# Proveniência de QÁ de Conversas 100%

- Origem local: `maquina-de-receita/squads-gerados/ops-cs-qa-conversas-verifier`.
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
| `agents/aria.md` | `755b6bdc29feb8b8014107de915b76dcac92935e8e5a7247fadebfafdffa1119` |
| `agents/calibra.md` | `62393e019d0ce9a0dd22c4777656c1374de97d9079e154abdd2232ffab670f15` |
| `agents/herald.md` | `dae99e7a3a12d82cd4e51b46adaab06ec94068e480e8def56182625338aaaaaa` |
| `agents/kronos.md` | `1fe798bb18a0e25bac5d5b8e3a577899d30bf1ddf639afb7fbb20a9c29e00bd9` |
| `agents/lexis.md` | `bdd99bbb3d56d408e7692bc976e602b53df63bfbddb7598c39b166ce3c1b6bcc` |
| `agents/nexus.md` | `b7c651921a084f77838281dd928bf81cff83e91bbf10ed79eb449b97f54e7910` |
| `agents/veritas-sentinel.md` | `e5c5fee71aef7f273057541a90e32a3ab1da3c9586d920b395afc0645eceb859` |
| `agents/veritas.md` | `7479244c7636cb4b8674ef5e445842dae54ceaf078f08b519e32d6946e6549ed` |
| `CHANGELOG.md` | `34893b7304b8735070c3417d58cb2fccc1e1d2d270b13833310dad79d4b25117` |
| `checklists/critic-veritas-sentinel.md` | `7b40a102cd9fd08156bfca18ee69713c834209baae9fd6801b309885d3b66138` |
| `config/coding-standards.md` | `df9c25531edb3ad44ee4147a4329eb1c3159d22ef10b4c8451c0894dd85540a1` |
| `config/source-tree.md` | `9f661ca12228444a9bcee35daa7b04c15e5d3a681cf536cbe01163070e1d183b` |
| `config/tech-stack.md` | `8a32d02a3cf7842c7e9d918d23266c47e74cc566bf707bf89ccfa0ed07cf8012` |
| `config.yaml` | `b7d6f7cc1f0563517522a65efb6d49d96a83f87bc8205d4199030cd05de0552f` |
| `README.md` | `301cb8b6be69a353c787f08ef438941a964bcb1b491a904fc92b8b999cb941cc` |
| `squad.yaml` | `7056768adf16a6587ce910044d2c1d3124c302ce45639d4ba9e5f7085ca78464` |
| `tasks/avaliar-qualidade-relacional.md` | `9da4e6ef8a6dfc36d6063a547e329533822645f77c468508eb82bfe04a75bf81` |
| `tasks/avaliar-resolucao-problema.md` | `0a6ebf566308a2fd2495572a5873fdc2b02e634b001d199a3e59ea4677c676a9` |
| `tasks/calibrar-rubrica.md` | `fb379264413371d66c9b7da7a4a1842e4c3a9ee48b6ac9bc95a07ee28a25c8c6` |
| `tasks/gerar-scorecard-completo.md` | `8b94e3b9f9883a28f958fd7aac901017f31fc2b9b5500a8ab94fda0b5c9816f3` |
| `tasks/orquestrar-pipeline.md` | `8df45c507faea9934759e9afc0e868bc3754aa2c450340bb63aeb002e417ca24` |
| `tasks/scanner-de-dados-sensiveis.md` | `08ea33f8e517ff466140c28f9f5e42925315213326a107ae14b5cb453f32a2b9` |
| `tasks/verificar-informacoes-tecnicas.md` | `f3e3956dda2d4a6cf7487c3460bb97a1048eef5a06e9ff1a5bf6a1b1ca584599` |
| `tasks/verificar-saidas.md` | `c6ae9e8a484684a6c60b20688b45dcb4819c46fc830a81eb7e2e76a50d6d59f7` |
| `workflows/ops-cs-qa-conversas-verifier-pipeline.yaml` | `7df09a5e55b37ed5904968e0f1bdbfa2c05a9e5065dbc7e5f659db93f6ef4f1b` |
