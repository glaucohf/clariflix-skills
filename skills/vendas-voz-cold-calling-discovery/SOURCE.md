<!-- generated-by: scripts/import_generated_squads.py; source: squads-gerados/vendas-voz-cold-calling-discovery -->
# Proveniência de Voz para Cold Calling e Discovery

- Origem local: `maquina-de-receita/squads-gerados/vendas-voz-cold-calling-discovery`.
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
| `agents/agenda.md` | `abfff745a719e09c9a023d196c6fa1209357bf0b96fafb6b89c0c7e5605bb526` |
| `agents/dossie.md` | `9b29405b968c2077209934f8b692fdbf93350242e2494ec677aeb423e5af75b5` |
| `agents/eco.md` | `9bbaf0b1a15f96c0e62159d1965f624535343667b6fdfb72f5a62ba06e8ea9ea` |
| `agents/filtro-2.md` | `1a57c5611af3dcdceb383d5ef589117bbc2c0919160520a906aae4bbbef946cd` |
| `agents/filtro.md` | `d8feb9df4673c3234df3e22929392037fa9a46ba62687d42335dd93e2fbf7b1c` |
| `agents/insight.md` | `d986f363d1f0a127a1e371c1238ff1ce6fb9ec1e3ea08925824c58914e70b986` |
| `agents/orquestrador-comercial-de-voz.md` | `76db2823dfaef8088dc220158717111eecd97151aefd674e1679ee5a29fe93ec` |
| `agents/radar.md` | `3f76ff5de3144221c6df3dbd1123fecdc5b6310f1f55e1c92dba558b57d6f770` |
| `agents/vox-worker-de-voz.md` | `d6d639b1d3cb52a08a60f02277e483fe359fff03bf671c789746e942f193444b` |
| `CHANGELOG.md` | `6055cfe0b6f2c2b4ca57daa4a005e8e059bd513ffa591fb064e339f0ec842dfd` |
| `checklists/critic-filtro-2.md` | `bcd561b87525bda256f7593b02e3fe661aef15507aee6020cf651f0dc472513e` |
| `config/coding-standards.md` | `196984dbef7e049a315d92ccf823a0d2095282036aecee472e1963fa8edc29fc` |
| `config/source-tree.md` | `407a24a35fb8ac04e5de421ad64bb1a8163e50c93ddf599239aa43c123009bb0` |
| `config/tech-stack.md` | `1abb3d68f0055ccc1b551efe2e2e9c29b27333f9ac58100cfcea9819745591a9` |
| `config.yaml` | `20ec29eb9b0958b319eabfd5def3412585187ab78a914869b878801e551d5419` |
| `README.md` | `fd4a674d7fcff18228c7b8914b9f5674242dc1719cb28e249ba971e2d5cac737` |
| `squad.yaml` | `142c5662a1d91883c6a3baee9d97749feb45b0be08b9d433388f043ded43b777` |
| `tasks/agendar-reuniao.md` | `0bbb86b6bb6c066dfbb4dcabe2880877c11917cf58d665fc5af69a5932ee4f68` |
| `tasks/analisar-padroes-de-conversas.md` | `e758720c7e711abb63c2f057720f609c15a6effdd886f947a8f96cb0bbfcaf50` |
| `tasks/analisar-transcricao-call.md` | `9d61c5ff2b30e7a6b0297a460ad7d4af9a1ce55d5699f80081af23ec5608fc7a` |
| `tasks/enriquecer-dossie-contextual.md` | `ed05a7b6447c22b47ecb90c60bbf3a3f1b337219847926ce7593fa30ee9eff1c` |
| `tasks/orquestrar-pipeline.md` | `8f0e9ce051beef310a64d7c7c967dc8d95a72b4fe0f60a8c6a5f571850631842` |
| `tasks/ranquear-leads.md` | `a2de4309b88c24a9d06baaaf934e3bd672102371c99170fe6c7ffe071a7f12e3` |
| `tasks/realizar-ligacao-cold-call.md` | `bf0315b92bbe04627c55d479b179bd8f4bd8a92fd826d802b9989b73b10a58df` |
| `tasks/reativar-interesse-frios.md` | `9c628fa86ab29a82f7fbdf5cb42b4c07213802512f70c3862ae9bd51985304f0` |
| `tasks/verificar-saidas.md` | `960bab8cf784f25f5a6a991d16f148aa64cb69759082b326e478361e21f412b1` |
| `workflows/vendas-voz-cold-calling-discovery-pipeline.yaml` | `d327aeb5d4464e794dde434ca3b33a3a3bbc60f24be8ff8e0efe8d9787f5193d` |
