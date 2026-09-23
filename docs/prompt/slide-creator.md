# slide-creator · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

Esta skill exige ferramentas de execução para parte do procedimento. Anexar este arquivo a um chat não habilita essas ferramentas; confira os requisitos da skill antes de prometer o resultado.

---

---
name: slide-creator
description: Cria decks com narrativa, direção visual, roteiro e critérios de qualidade Use quando o pedido corresponder a slide creator.
version: 0.4.0
license: Authorized redistribution
author: AIOX Embaixadores
---

# Apresentações que contam

As instruções originais e seus suportes estão preservados em [references/source/](references/source/).

## When to Use

Use quando a necessidade corresponder à skill de origem. Leia [references/source/SKILL.md](references/source/SKILL.md) antes de iniciar; algumas skills requerem AIOX Core e a squad indicada pela própria fonte.

## Quick Reference

Forneça o contexto solicitado pela fonte e mantenha as dependências externas, integrações e ações de publicação sob revisão humana.

## Procedure

1. Leia a fonte para identificar entradas, dependências e entregáveis.
2. Reúna o contexto mínimo e siga o fluxo documentado pela skill.
3. Apresente o resultado para revisão antes de ações externas ou irreversíveis.

## Pitfalls

Não presuma que AIOX Core, squads, integrações ou credenciais estão disponíveis. Não execute comandos da fonte sem verificar os pré-requisitos locais.

## Verification

Confirme que as dependências necessárias estão instaladas, as entradas foram usadas e os limites e próximos passos ficaram claros.


## Referência: LICENSE.source

```text
A fonte não declara licença pública. O mantenedor do ClariFlix confirmou autorização dos autores para republicação em 2026-09-23.
```


## Referência: SOURCE.md

# Proveniência

- Fonte: [https://github.com/aiox-embaixadores/aiox-embaixador-pro](https://github.com/aiox-embaixadores/aiox-embaixador-pro/tree/a137d3b87af63a8b05ef51cab8ea293d44a2a1c4/skills/slide-creator)
- Commit: `a137d3b87af63a8b05ef51cab8ea293d44a2a1c4`
- Licença: não declarada publicamente; autorização de redistribuição confirmada pelo mantenedor do ClariFlix em 2026-09-23.
- Arquivos de origem preservados em `references/source/`; inventário e hashes em `references/aiox-source-inventory.json`.


## Referência: references/aiox-source-inventory.json

```json
{
  "source_url": "https://github.com/aiox-embaixadores/aiox-embaixador-pro/tree/a137d3b87af63a8b05ef51cab8ea293d44a2a1c4/skills/slide-creator",
  "source_repository": "https://github.com/aiox-embaixadores/aiox-embaixador-pro",
  "source_commit": "a137d3b87af63a8b05ef51cab8ea293d44a2a1c4",
  "license": "Authorized redistribution",
  "files": [
    {
      "path": "agents/openai.yaml",
      "sha256": "b342d1b9b33e1cc066760268d61982c97edd260c4478c99e87015d1445cd6ee2"
    },
    {
      "path": "examples/design-100-fixture/brand-template-manifest.yaml",
      "sha256": "206af10049eb5b2d5cf33a8db4e97fec38d966c0797efd7f4918fde2d5e539cf"
    },
    {
      "path": "examples/design-100-fixture/design-mastery-report.yaml",
      "sha256": "6488a7e2b520c7a3c5b4c504d299f517d1664884bf3de55e1a16fe7313779707"
    },
    {
      "path": "examples/design-100-fixture/key-slide-render-review.yaml",
      "sha256": "7395ef0d7f48a87a5ce21eb05f57a49137b3d7dc13b95e010fe5404bc29b552d"
    },
    {
      "path": "examples/design-100-fixture/render-lock.yaml",
      "sha256": "ef1578ed1b361d840664f9b854a89c6c012ebc4bceb2d1f3484b4cf1a18ef4ef"
    },
    {
      "path": "examples/design-100-fixture/template-selection-report.yaml",
      "sha256": "1f09679a7e04512b5a23db1f6cb6139863b81a50feaa3f7fd7fcba3a6d3b2115"
    },
    {
      "path": "examples/design-100-fixture/visual-regression-checklist.yaml",
      "sha256": "5b0df7858aabfd18474804334b5fae35a382a363f77ce8c23c68862cdcc71e81"
    },
    {
      "path": "references/anti-patterns.md",
      "sha256": "4dbf748f4ccf85fb2a597fa0a9976fa59de7266c224c9c52793345a8af71d81c"
    },
    {
      "path": "references/bench-absorption-map.md",
      "sha256": "b6223787e60a1bc0fab2d1ee8f6fd90f1eba3ad98fa0d2ace0148ab64f09a8f5"
    },
    {
      "path": "references/design-system.md",
      "sha256": "59ef2a27b447878a93a8e254357190dc52cad45b06c803cb2e14fc594e113699"
    },
    {
      "path": "references/narrative-patterns.md",
      "sha256": "c1a3b839dbbd50246e08ecb9b76c64ef6510f2219076e9b51aea75c3edb6370e"
    },
    {
      "path": "references/output-contracts.md",
      "sha256": "91d6b26ea4d5eb0a4d1071ec68ac2388595c058b1affa3bf559ea8904686e244"
    },
    {
      "path": "references/regression-test-protocol.md",
      "sha256": "39595665c0e16593c34afda4ab3b6a64f92b5a2c30d5035d88cffde0df173d3c"
    },
    {
      "path": "references/roteiro-template-library.md",
      "sha256": "3a07928225dde1e3d3a25fd9ca7991975a260b7a61613a17b459b7c81534fc86"
    },
    {
      "path": "references/rubrics.md",
      "sha256": "ede332d59678261e9620523bcc1cb06046d91c1bf1d569e65c8b65797bd91d52"
    },
    {
      "path": "references/slide-structure-library.md",
      "sha256": "5dabd13ae594247d35e624be9dc92d6a22d132f76a36eead22696ff7f27f2096"
    },
    {
      "path": "references/template-selection-guide.md",
      "sha256": "c80479463e628c7b25ffff95d1e79323bf2d9398a4cf2d9b1680c7458fd6e183"
    },
    {
      "path": "SKILL.md",
      "sha256": "32d9551081f1284f25bac545082d70ac48cda04144c73e38e46a69176bf44dfc"
    },
    {
      "path": "templates/deck/copy-derived.yaml",
      "sha256": "a04e7b4076c39488539e50ae49afbcc3b7b0b19b56ab9370ebbc4282b19a4719"
    },
    {
      "path": "templates/deck/playbook-routing.yaml",
      "sha256": "38f6746dacfecf764321f21e73f10fb385f4878101410d7ffd1d6537b9061c33"
    },
    {
      "path": "templates/deck/route-map.yaml",
      "sha256": "3acc8b5f70b444eedc00a8e065ec59d24b345b3de21fa1c28d0d1af8f47f5de5"
    },
    {
      "path": "templates/eval/design-regression-corpus.yaml",
      "sha256": "5f2ccc36e60b56e43d32e4eeb64e8bbfff58ba94f0fb3118526ebb96fec79883"
    },
    {
      "path": "templates/eval/rendered-design-fixture-set.yaml",
      "sha256": "5d5d80ac95490faff9f7120473d6aebcaf5a19021898e9cd8228edfd42614926"
    },
    {
      "path": "templates/eval/rendered-eval.yaml",
      "sha256": "7de3733d2172082497949317359356b82e5f7c766c24b51c2a97f5c30aba6bec"
    },
    {
      "path": "templates/import/document-extraction.yaml",
      "sha256": "1fb8d2d662bc030568372efe3b671b4f3f3d0ed5f1471b65596d7755d9d7e724"
    },
    {
      "path": "templates/import/induced-layout-packs.yaml",
      "sha256": "6a3ec870a7dfcafee669a04b6d089938b26238419f2dc31df8f4384a26275779"
    },
    {
      "path": "templates/import/pptx-template-manifest.yaml",
      "sha256": "5f2f72dc3b656ee4bc6e88f6dbbb346ba8f6984527b7eae05f348a936eaf753d"
    },
    {
      "path": "templates/import/source-deck-fixtures.yaml",
      "sha256": "9c6b586730e6597ab6378321a63ea8f97ca3b8272cf94fb0b9dcd8fcca0c308b"
    },
    {
      "path": "templates/import/template-import-regression-corpus.yaml",
      "sha256": "327c0947ba6bf57c177b6b69f93f47f3847c48ee19b54e6aef5daaac970bb95f"
    },
    {
      "path": "templates/index.yaml",
      "sha256": "6cbb69e9260718e95600147054e89ab28a2356c8d1e22b4d33567893e8599392"
    },
    {
      "path": "templates/qa/copy-gates.yaml",
      "sha256": "1a38b1053265a6310d91b9ae5193ae047f7fc7f5886cf7ae18a07b43d93a7328"
    },
    {
      "path": "templates/qa/narrative-gates.yaml",
      "sha256": "5eec1b92069a63408701dd86245643fe5d0d7e71baa10ae5250b957160b93cb8"
    },
    {
      "path": "templates/qa/pptx-technical-gates.yaml",
      "sha256": "498d11720e607f727b65b5d63caf89bc5a491704868b03bd58021907eaf5d523"
    },
    {
      "path": "templates/qa/regression-fixtures.yaml",
      "sha256": "20ab8673950075fa84a73e4ea7792cef63048b5a06134f4dc889993ad7e88900"
    },
    {
      "path": "templates/qa/squad-quality-rubric.yaml",
      "sha256": "7a3b4d28c3bace2271969d05c847b8f551e5063c8a810bb88af05dea7c95aad3"
    },
    {
      "path": "templates/qa/template-selection-gates.yaml",
      "sha256": "bf0792682a00389ce32b4f4c8adc0f7dab0b00b411e2611276caafc096ef0090"
    },
    {
      "path": "templates/qa/visual-gates.yaml",
      "sha256": "1d174e281ef03c851d5ed29819a2da0feff162327b69c04ce41190c7fede7f1e"
    },
    {
      "path": "templates/research/evidence-ledger.yaml",
      "sha256": "66941cd01e7c61e8336d617fed6cc9f1f210a698246196daa541fbc2530f6dbc"
    },
    {
      "path": "templates/research/source-routing.yaml",
      "sha256": "526350e2447bf774b22c780bec45972ed49ca68e573b7135a0660d7a09387a6d"
    },
    {
      "path": "templates/runtime/api-mcp-cli-contract.yaml",
      "sha256": "e965b059cf7672aca59629ebed2fb8e9f6e37690d46ae2a6c65406d1c696243d"
    },
    {
      "path": "templates/runtime/delivery-package-contract.yaml",
      "sha256": "459e0e18a4bed90fbcf55535ddd5e4f55c5ef9bc6ed9acff342897716ba12507"
    },
    {
      "path": "templates/runtime/design-direction-contract.yaml",
      "sha256": "d1787099b3b5e692b6f7b3a8f4bf707c658b76e6afae4266388a6ce8f770eac3"
    },
    {
      "path": "templates/runtime/design-score-evidence.yaml",
      "sha256": "11a30a2a6b89cdf9f59e60498b3f530914afffbe3a10def3c2b56b4f425524b3"
    },
    {
      "path": "templates/runtime/diagram-rendering.yaml",
      "sha256": "475f34fb878e368e628d0247ce032eb56fa873336cd628fefe70eaa9956e13ce"
    },
    {
      "path": "templates/runtime/edit-history.yaml",
      "sha256": "13f36ccbe8d095d04a507b8f565578c52127bd88c5914e42ad0ccd72f7912c34"
    },
    {
      "path": "templates/runtime/edit-operations.yaml",
      "sha256": "240a2d4544056fc1e0397ede62b5590301dd32b56305dbfd50b4a9e13e4a7151"
    },
    {
      "path": "templates/runtime/export-contract.yaml",
      "sha256": "c61be95dff3e4c85e0ea457df03e1de926f9b76e2076788f4d20fa5ba6af29aa"
    },
    {
      "path": "templates/runtime/html-to-pptx.yaml",
      "sha256": "1bbc8052c0ef2eb89b7acc16c6f0d54bc1d413d352a10046f455fac032c83465"
    },
    {
      "path": "templates/runtime/import-template.yaml",
      "sha256": "f695451a9a49a6f077d490c07c3ee2576141466d25fb1b7b41d5423355ea1cb0"
    },
    {
      "path": "templates/runtime/job-state.schema.yaml",
      "sha256": "d835ca6c18a4aa356021bb590acd8b1a0db9cf3c5472a1aac0fb87ff49a36f66"
    },
    {
      "path": "templates/runtime/jobs.yaml",
      "sha256": "56282693b6ac8a27fd9ac7787b88df7815010e63ec31891fa38d73867487d4de"
    },
    {
      "path": "templates/runtime/manuscript-pipeline.yaml",
      "sha256": "17e71336d406a6cb45e72ee059e29f6d5ada51bb398fdbc13038c22a385e76f4"
    },
    {
      "path": "templates/runtime/narrative-design-moment-grammar.yaml",
      "sha256": "061857d6e23d7a8046df2ce3b7145c7d0f9169af265f5fd6ce8d499ec7e998c1"
    },
    {
      "path": "templates/runtime/narrative-regression-corpus.yaml",
      "sha256": "d858faa6b27f51c5e7f2b5dc9af32a02461c90302c5100f1390219a7dc729cfb"
    },
    {
      "path": "templates/runtime/provider-routing.yaml",
      "sha256": "fb51e760ba8a03da31a389ccb9ceb251878dacafe3404ea9b51a4f6d8b0a4088"
    },
    {
      "path": "templates/runtime/render-lock.yaml",
      "sha256": "a95ae512dd74681a21a8685c6aa2fc929374bd1887c6f47b6423ad4a642c3fb3"
    },
    {
      "path": "templates/runtime/runtime-gap-absorption-corpus.yaml",
      "sha256": "2c5e1fcd6931aa7c5fb727c000e7f15c7203c5d29bd6dccaead5398f97025655"
    },
    {
      "path": "templates/runtime/slide-function-map-contract.yaml",
      "sha256": "09a4dc2270ee0f8afb210b537bf8555843e7d8e4bcd6714dceed258d036e878d"
    },
    {
      "path": "templates/runtime/source-of-truth-policy.yaml",
      "sha256": "bd8cd33413f2aaf3a3e93adef1095be0ce1e8c5845a1b1bb21865d6ea7356424"
    },
    {
      "path": "templates/runtime/speaker-notes-narration-contract.yaml",
      "sha256": "05719c7cf238e48177ef7ebb2bbb0fe01192dd9010546e386132d7ccd580cce5"
    },
    {
      "path": "templates/runtime/story-arc-contract.yaml",
      "sha256": "75928de6b8c0cebc847cf8674dc63e078ba69a717f990380423dec43e9dfe789"
    },
    {
      "path": "templates/runtime/storyboard-edit-contract.yaml",
      "sha256": "380175f7e41e7fd8e2971210c4ae6766ef9b6af33ea6ff50e4da2f3a0bb7e458"
    },
    {
      "path": "templates/runtime/storyboard-render-bridge.yaml",
      "sha256": "27ccddbdf79fedf7c57916bb5f6d754f06e1892f0863c2f9d4afe488eae65788"
    },
    {
      "path": "templates/runtime/template-example-routing.yaml",
      "sha256": "9c1d550d5ec76c7616830e282b899cf10ecfba58c7691f9c24c3df990d179ec4"
    },
    {
      "path": "templates/runtime/template-selection-report.yaml",
      "sha256": "6fbd42fc81140c9651ca29c81e8a642ac7dd0a4a920ddc4bbf91af7be63e3c2d"
    },
    {
      "path": "templates/runtime/theme-runtime-snapshot-suite.yaml",
      "sha256": "d298b5eaf844cbd018dd87110c504a1ea12668946c68d5c5acc53f1150abb9e3"
    },
    {
      "path": "templates/runtime/trace-handoff.yaml",
      "sha256": "dd598c15bfb5c64c1d0d8d3aa458cbfcd227e264a1d1b4eafd42c20c7f3a287f"
    },
    {
      "path": "templates/runtime/workflow-modes.yaml",
      "sha256": "362cbe5652b7e92d64dca79887a5eeddb9249b07c7bd2b7183a3214a3594d782"
    },
    {
      "path": "templates/schemas/deck-template.schema.yaml",
      "sha256": "8bb9331cc4c691642264ebc98c33541a3370fe56daa6f9afaeaf55aaff812073"
    },
    {
      "path": "templates/schemas/qa-gate.schema.yaml",
      "sha256": "7172cbba45478f163e6bfefd02c5ede5cfe6c14c7714ca31b4ca57532ace5033"
    },
    {
      "path": "templates/schemas/runtime-job.schema.yaml",
      "sha256": "8cd2eddf71492622aa28bbe67190da34dfb737d49562dfa0689ed441444ab39e"
    },
    {
      "path": "templates/schemas/slide-template.schema.yaml",
      "sha256": "fce59b820855f7d23b8471aefd22e176dccca4be2c85a85ae3e3949409600650"
    },
    {
      "path": "templates/schemas/theme.schema.yaml",
      "sha256": "fe72b37216f045f91e4bfd3d254e11921065d7c759770fd1a82ed864e91463af"
    },
    {
      "path": "templates/schemas/visual-template.schema.yaml",
      "sha256": "46c847651353e4dd6c210b2189c8c63fdb29b70b2d3e65fb9c170fc5b289e0b5"
    },
    {
      "path": "templates/slide/function-library.yaml",
      "sha256": "dd92cb7c4be6b98f00bb267ea35a5522f7dbdc48af6615a398a670ce13c089d5"
    },
    {
      "path": "templates/theme/brand-systems.yaml",
      "sha256": "3392246fcc070d92bc6c3b6ba2c6bd3fbffacb494c8fe4436da7b58eeb6156e2"
    },
    {
      "path": "templates/theme/design-philosophy-routing.yaml",
      "sha256": "a61205409f5803ef6a615e26f39a7a9bd2a343baf3617dfb86d14503e218fe15"
    },
    {
      "path": "templates/theme/theme-tokens.yaml",
      "sha256": "30dae982d78d86755f2a1ee93f4ca38fbd79e3431bc41957c81d96dba85c9d21"
    },
    {
      "path": "templates/visual/ai-image-type-routing.yaml",
      "sha256": "81ef3c10dd7dbbcd0165038638d9041ac795efadcc85bfd6febc26db96492ff4"
    },
    {
      "path": "templates/visual/aiox-brandbook-deep-patterns.yaml",
      "sha256": "d297432fcebf8516938cf1d2507703e0c6294be09539fd3eb5ffeb1a2c54885a"
    },
    {
      "path": "templates/visual/brand-fidelity-playbooks.yaml",
      "sha256": "3020df7492774ab4f4c7fcf1e659bd63a2c878e41796a10de5c4208d8a6ce639"
    },
    {
      "path": "templates/visual/brand-system-patterns.yaml",
      "sha256": "da972ff0f56f56de8217efee0cd1bd3b36deaf1781446fc8a3331fc68c3c2e00"
    },
    {
      "path": "templates/visual/brand-template-manifest.yaml",
      "sha256": "da64108c50b90a0b0d0e51912d75fdce16df90c8818ad8e74e27c7a9329e2508"
    },
    {
      "path": "templates/visual/chart-data-contracts.yaml",
      "sha256": "a7b47d6f19e12172c32528e2847a18ac65f3538dc50202bfea11cd82f570565f"
    },
    {
      "path": "templates/visual/charts-and-diagrams.yaml",
      "sha256": "e1258115513ea0c3e7e504cf73a8a6495783c352d2c6ad79ff2efedd93683189"
    },
    {
      "path": "templates/visual/composition-patterns.yaml",
      "sha256": "62201d2fe531d589d2989ecff4ff5c03568948c05a24d7d2b1d15114106809f7"
    },
    {
      "path": "templates/visual/design-mastery-contract.yaml",
      "sha256": "048770ca66acc55754d664c6f78fcb092574660432bc9a0cdc085db88c8ac82d"
    },
    {
      "path": "templates/visual/design-mastery-report.yaml",
      "sha256": "3e80bd7e809edc94290088c267fe3722d7f29de1e9b4810ff67412cc71646e72"
    },
    {
      "path": "templates/visual/key-slide-render-review.yaml",
      "sha256": "465ec0a375df9c5d2e0dd9a92bf6b0576055115ac2edb743e3e388f51413eb2e"
    },
    {
      "path": "templates/visual/layout-families.yaml",
      "sha256": "24fda5e4c90b01bbdaabfcc31350a2e91b8d7a519e90a77115c44a0fa2576565"
    },
    {
      "path": "templates/visual/media-layouts.yaml",
      "sha256": "74c92482d0f2de8e5229ece8a73b0e856401ebc8eb6a42ed174b88097633559f"
    },
    {
      "path": "templates/visual/redpine-deep-patterns.yaml",
      "sha256": "66841b02b26f62e64e5af3beb236bf2dfbd1cc0b3a5e47d0861767142569e7ad"
    },
    {
      "path": "templates/visual/visual-regression-checklist.yaml",
      "sha256": "20a85f78e0cb3f908ee15317aa6a3423d8456940fdd7098792bb2b7daf4d8072"
    },
    {
      "path": "templates/wireframes/agenda-timeline.html",
      "sha256": "b06d93ec6e3147c1c751082a06ec10e2d351dac4d48bfba381dd34a0711b1650"
    },
    {
      "path": "templates/wireframes/api-request-response.html",
      "sha256": "7ca24d4864f3e99e63f4c36f9a7b67e6c1c692c18425f5576fd4d66d7735b178"
    },
    {
      "path": "templates/wireframes/architecture-tradeoff-table.html",
      "sha256": "ed96412ae95989ba0caa51be098233ca0015d31e4c2894232ea69207582da25a"
    },
    {
      "path": "templates/wireframes/benchmark-matrix.html",
      "sha256": "dc23dc4f77dea7b222782edae1493ee7c4c3706f406a9e9cb8007748dc317b2c"
    },
    {
      "path": "templates/wireframes/brand-principles.html",
      "sha256": "1cb0760f0043beb163d9d56954f9ceb3fe82220961a0b88abc4d8b9de6b361ae"
    },
    {
      "path": "templates/wireframes/business-challenges.html",
      "sha256": "566e7e10942481585ac1c1a4a0aeae3dcd984325068180ab0db3d12acb51e2bb"
    },
    {
      "path": "templates/wireframes/case-study-proof.html",
      "sha256": "9c8a213f2b992713e9fc9ddba3798f5f594d7b663d0bd20531cfb1a45349b2fe"
    },
    {
      "path": "templates/wireframes/code-explanation.html",
      "sha256": "931a664222d404997a4851fe4aaa3e3d60cefb055bcbbf965f375fa31d596075"
    },
    {
      "path": "templates/wireframes/cohort-retention.html",
      "sha256": "348be60bab38fa05712a91c2e3e41993ff3e3602893c0bb8cdbc7e66d26e3755"
    },
    {
      "path": "templates/wireframes/competitive-landscape.html",
      "sha256": "534959cd9aff1a4051ea810bf5fc4dd4b5bfac4b7bc4cac35b085994b053bab5"
    },
    {
      "path": "templates/wireframes/compliance-grid.html",
      "sha256": "ad15a6599def9ec54c3846fbe0685fb59e665e5610b88a4bff0bb0e211f5f012"
    },
    {
      "path": "templates/wireframes/contact-next-step.html",
      "sha256": "02580b154306c5f9c2ff9f776c57f450d8a6360611926deafb76253baf7d7f29"
    },
    {
      "path": "templates/wireframes/dashboard-grid.html",
      "sha256": "a2766b51bce845a211c0a0ae7c93e2f928b87a18eebe196197896e5cd30d37ef"
    },
    {
      "path": "templates/wireframes/data-lineage.html",
      "sha256": "188b343b31281c76b96cf6c34c401e89725f1a8a99b344213a85df070e569b1d"
    },
    {
      "path": "templates/wireframes/decision-options.html",
      "sha256": "6b62cf0ea5e93dff3e8275ea122a265075589c5fdcd5709649b461b8b46d56e1"
    },
    {
      "path": "templates/wireframes/decision-tree.html",
      "sha256": "8771d77e8ab68b61e9e80f79bde563a8f7fb5c570371ee82c5d9b809ef0ecb50"
    },
    {
      "path": "templates/wireframes/dependency-map.html",
      "sha256": "a63b87808d76c005dc988ca11af5fa53b42b4b05a1f6c997219212e7ad069abf"
    },
    {
      "path": "templates/wireframes/design-system-audit.html",
      "sha256": "9032d49149a2c1186c762bad15f84426fa90fb7bde8f65db2205c632edbeb2bf"
    },
    {
      "path": "templates/wireframes/executive-summary.html",
      "sha256": "737a30ea5bd513a01dd0468bab6b5a4958e1a0137db15747944119f527a71977"
    },
    {
      "path": "templates/wireframes/experiment-grid.html",
      "sha256": "a18e359cf13dcf57759acdf4e013830108b2812c02198fc04762fd60570baec7"
    },
    {
      "path": "templates/wireframes/feature-matrix.html",
      "sha256": "7a3f18fc183282bf5835adf391793e37cd4a0e554500bdd7252c5f7bfa21a6b6"
    },
    {
      "path": "templates/wireframes/financial-waterfall.html",
      "sha256": "f21acf35819ee8222207865f40d56075c9bf584a36b7eb10f22dfdebe3aacd18"
    },
    {
      "path": "templates/wireframes/gallery.html",
      "sha256": "2f8b1c27b438f7eacd99dfb301d6be5dc041129ed84ab7b547b873e16a957b8d"
    },
    {
      "path": "templates/wireframes/harvey-balls-table.html",
      "sha256": "0a0052c935d8bafabac45083515e549c08fef0e7b2a029e25a885be74624eff4"
    },
    {
      "path": "templates/wireframes/hiring-scorecard.html",
      "sha256": "d509a21c8a73766530847c0b8d252e5ae74d5caf974396a017f72c2dab0b572c"
    },
    {
      "path": "templates/wireframes/incident-timeline.html",
      "sha256": "0d1468e41a7e0810721694c689d8c2670b91c94deb15490cbbee4fb7334b8fbd"
    },
    {
      "path": "templates/wireframes/launch-calendar.html",
      "sha256": "2e770d75d4a5c32ed073d4b26274f19e4159093c7804dc537e8df6d52bd62dad"
    },
    {
      "path": "templates/wireframes/maturity-ladder.html",
      "sha256": "1a9356158cb5eaf47a3ebb2818520fe011a33d7c15b022167f3fc8230ce7ceef"
    },
    {
      "path": "templates/wireframes/mechanism-map.html",
      "sha256": "dbfd1f840761ae914ce3d01a84b708043d45e79164015aea6312873f792cac8a"
    },
    {
      "path": "templates/wireframes/mission-vision.html",
      "sha256": "565660df5e9288dd3921f6f8e33d78f5980381bd3f48f271836473d81b256d9e"
    },
    {
      "path": "templates/wireframes/moodboard-grid.html",
      "sha256": "0f2c7e0a10c4357fb2c8a17974250dfc1d69d0ccfcd44cee6b68bc320f4ce89c"
    },
    {
      "path": "templates/wireframes/objection-matrix.html",
      "sha256": "a99f251196d00ce04020b5ae898ccd7f07dd112fa7bd7b57fd5470aa7a9f4637"
    },
    {
      "path": "templates/wireframes/org-chart.html",
      "sha256": "02de0122d6d1a9c44582a4a3ebb2fada50afc31d35f7b54ec9fedf30daa7f2fe"
    },
    {
      "path": "templates/wireframes/persona-fit-matrix.html",
      "sha256": "c151cc4c007e5a88d7cb5f4683c4942b3b0fa38d5a62c74d5159e043521a16d3"
    },
    {
      "path": "templates/wireframes/portfolio-allocation.html",
      "sha256": "5d4db40dc4c1a79cdf6ad456b124c6985c9e4675308a30bee8b62bdeadb9c387"
    },
    {
      "path": "templates/wireframes/pricing-table.html",
      "sha256": "f49a1fd98d5d274157d138e06c6a3fe992349ce3afe764633ddd9a1a2e151c6d"
    },
    {
      "path": "templates/wireframes/proof-stack.html",
      "sha256": "287a2fe5623f2f6a4c1f0aa399a544ff0dfd4a2c57d2dad8a9a82f3ea7495c8a"
    },
    {
      "path": "templates/wireframes/quote-evidence-panel.html",
      "sha256": "9a6d5c6ce38fcb6f4db4d4b5eccf3b6f4f6f0d767cddfb69eb8b58c9c92b338a"
    },
    {
      "path": "templates/wireframes/responsibility-matrix.html",
      "sha256": "3ecb9cdbf6e8c67211fefd5ad67695269dd063128971cddcb4094f5fc4fdf43c"
    },
    {
      "path": "templates/wireframes/risk-heatmap.html",
      "sha256": "e2e25ae9bc26cb5964722eb6319a92fdd454708e041929d6dc5831ad19f84bd8"
    },
    {
      "path": "templates/wireframes/roadmap-decision.html",
      "sha256": "294a76d88532d98d772eb32534f25fb9b45b728aa45a12ee8001dcdaad76cb8b"
    },
    {
      "path": "templates/wireframes/roadmap-status.html",
      "sha256": "aa56a57c7793e1e0093b63630acbb2cb80c351b158d2385b878be5166098acac"
    },
    {
      "path": "templates/wireframes/sankey-flow.html",
      "sha256": "9d887ab11d4c5af75a7042bb8f1545009075efa8ac4744d16e7c7869a93a40b6"
    },
    {
      "path": "templates/wireframes/scatter-plot.html",
      "sha256": "ddec72ab11cf747584a1ba5af1b95c72bd946b28e8e357d66d6cf9d20aa3da1d"
    },
    {
      "path": "templates/wireframes/scoring-rubric.html",
      "sha256": "5ebe73237aabe84f7415d8b4f317e5cf21ae5ca09b15ca0edbb23f5e89376236"
    },
    {
      "path": "templates/wireframes/screen-sequence.html",
      "sha256": "153565d9dc7f653891af1e598d2b13c63d71aca4f5746ea56a02fa1d05eb23b0"
    },
    {
      "path": "templates/wireframes/service-catalog.html",
      "sha256": "1b41b9f24658dcf1a7d2167260db04930f394701971cf7636fbf3bdddf2a8e65"
    },
    {
      "path": "templates/wireframes/social-proof-wall.html",
      "sha256": "5c6c57f1dc2165267f8f2f73858c12af4057b23faade7f8585c5d74e9579f689"
    },
    {
      "path": "templates/wireframes/survey-results.html",
      "sha256": "c1013e990a4c65d2ed5236f85f633cdf2181bdaf9dad2032f409223f89a8852e"
    },
    {
      "path": "templates/wireframes/table-of-contents.html",
      "sha256": "ef0d8adb1a779ed4aea4a758b5fe953344100c5a929e6ec2bb35df6f64ab4c46"
    },
    {
      "path": "templates/wireframes/team-credentials.html",
      "sha256": "8d9eac02fce8b95828f53ce0f9048408862abb4dd020909802c4bf2254a5d3de"
    },
    {
      "path": "templates/wireframes/technical-architecture.html",
      "sha256": "31c3b26258331b7319813d5acef24a4dfe4ea871ad64f68028e0c04650abda6b"
    },
    {
      "path": "templates/wireframes/traceability-matrix.html",
      "sha256": "265a9232543c8fb110fffd7eec92dd89b9968b1ed6004840b411c41d0636a28a"
    },
    {
      "path": "templates/wireframes/unit-economics.html",
      "sha256": "69ee2d4cef8c544d1f057fa56332b5123c466d2193e1f933f8a309dfe521e35f"
    },
    {
      "path": "templates/wireframes/user-story-map.html",
      "sha256": "1dadb9a4886c66bf40e86a5c2581e2c7669a8b553a7215fa443af982ed88d1be"
    },
    {
      "path": "templates/wireframes/value-chain.html",
      "sha256": "096cbb94acb8ad4cf4d55abdac5e5d5f06b149574b11c2f90f08d9beac69cd71"
    },
    {
      "path": "templates/wireframes/webinar-flow.html",
      "sha256": "f242698ae838b21d755ec90d8a5d4a679a04748246909194c25211e6b9c12444"
    },
    {
      "path": "templates/wireframes/workshop-canvas.html",
      "sha256": "f4391136c3ab785133bab4f5cbc1fc4e005fc17ad8a31fe58e31308c603ae4ae"
    }
  ]
}
```


## Referência: references/source/SKILL.md

---
name: slide-creator
description: "Self-contained narrative-first presentation deck creation skill. Use when Codex needs to create, improve, critique, or rewrite slide decks from a briefing, outline, document, webinar script, workshop, pitch, sales narrative, board update, course, or rough notes. Produces a complete deck package with narrative arc, slide-function map, design direction, slide-by-slide spec, speaker notes, QA report, and optional HTML-ready slide content without requiring the SINKRA monorepo or external squad files."
version: "1.0.0"
owner_squad: slides-creator
user-invocable: true
---

# Slide Creator

Create presentation decks as directed narrative experiences, not outline dumps. Optimize first for story, audience belief shift, editorial design, proof, and clarity. Export format is secondary.

This skill is self-contained. Do not require `squads/slides-creator`, external agents, SINKRA tasks, or private repo files. Use bundled templates and references only when needed.

The evolved slides-creator squad patterns have been absorbed as bundled contracts. Treat `templates/runtime/workflow-modes.yaml`, `templates/deck/playbook-routing.yaml`, `templates/runtime/story-arc-contract.yaml`, `templates/runtime/slide-function-map-contract.yaml`, `templates/runtime/design-direction-contract.yaml`, `templates/qa/squad-quality-rubric.yaml`, and `templates/theme/design-philosophy-routing.yaml` as the local source of truth.

## Operating Rule

Never render or draft slides directly from an outline. First produce:

`briefing -> thesis -> story arc -> slide-function map -> design direction -> deck spec -> critique -> revision -> QA`

If a user asks for quick slides, compress the workflow, but keep the narrative and design gates.

If the user provides a bad prior deck, process log, benchmark, or says a previous slide process was weak, create a regression/forward-test before generating a new full deck. The goal is to prevent the exact failure from recurring.

## Quick Workflow

1. **Normalize briefing**
   Extract audience, objective, context, constraints, source material, required CTA, tone, format, and unknowns.
   Select a workflow mode from `templates/runtime/workflow-modes.yaml` so quick asks stay light and shareable/exportable decks get full contracts.

2. **Define belief shift**
   State what the audience currently believes, what they must believe by the end, and what proof will move them.

3. **Build story arc**
   Use a narrative structure suited to the deck type. Default for persuasive decks:
   `reframe -> tension -> stakes -> mechanism -> proof -> plan -> CTA`.
   For full decks, follow `templates/runtime/story-arc-contract.yaml`.

4. **Create slide-function map**
   Each slide must have one primary function such as hook, diagnosis, contrast, proof, mechanism, demo setup, offer, objection handling, decision, or appendix. Merge slides with duplicate function unless repetition is intentional.
   Each slide also needs an `audience_movement`; "explicar/apresentar/mostrar tópico" is a blocker, not a function.

5. **Select canonical templates**
   Load `templates/index.yaml` first. Select workflow mode, deck playbook, deck template, slide-function templates, visual templates, theme profile, research route, import pipeline, runtime job, rendered-eval contract, and QA gates before drafting content. For key slides, produce a template-selection report with rejected runners-up and deck-specific rejection reasons. Use `references/template-selection-guide.md`, `references/roteiro-template-library.md`, and `references/slide-structure-library.md` only as explanatory backup.

6. **Apply bench-derived capabilities**
   Load `templates/index.yaml`, then the relevant files under `templates/research/`, `templates/import/`, `templates/runtime/`, `templates/visual/`, `templates/eval/`, and `templates/qa/` when the user asks for PPTX, API, MCP, local models, prompt-to-edit, diagrams, research, sharing, import/export, rendered QA, or product/runtime design. Use `references/bench-absorption-map.md` for rationale.

7. **Define design direction**
   Choose visual thesis, grid, type scale, density limits, motifs, layout variety, chart style, and anti-patterns before writing slide content.
   Use `templates/runtime/design-direction-contract.yaml`; design direction must define density limits, variation rules, composition rules, and audience context before slide copy.

7.5. **Lock execution**
   For full decks or any PPTX/exportable deck, produce `render-lock.yaml` before rendering/exporting. Treat it as the execution source of truth for colors, fonts, chart palette, image style, visual composition, forbidden features, and asset status.

8. **Draft deck spec**
   Produce one spec per slide with action title, function, key message, layout, visible copy, visual treatment, speaker notes, evidence, and QA checklist.

9. **Run key-slide gate**
   For important decks, draft and critique the 5 decisive slides before full production: cover, reframe, mechanism, proof/demo, and CTA. If these fail, revise the deck spec before rendering the rest.

10. **Critique before delivery**
   Run narrative, design, proof, clarity, CTA, and technical checks. Revise once before showing final output.

11. **Package**
   Deliver a deck package: `briefing-normalized`, `story-arc`, `slide-function-map`, `design-direction`, `deck-spec`, `speaker-notes`, `qa-report`, and optional HTML-ready slides.

12. **Use deterministic helpers when writing files**
   When producing reusable artifacts, prefer bundled scripts over hand-built repetitive output:
   `scripts/build_template_examples.py`, `scripts/build_evidence_ledger.py`, `scripts/run_regression_fixtures.py`, `scripts/validate_rendered_eval.py`, `scripts/validate_runtime_contracts.py`, `scripts/validate_deck_package.py`, `scripts/validate_design_mastery.py`, `scripts/validate_design_capability.py`, `scripts/validate_narrative_capability.py`, `scripts/validate_narrative_design_capability.py`, `scripts/validate_runtime_gap_capability.py`, `scripts/validate_delivery_capability.py`, `scripts/check_pptx_placeholders.py`, and `scripts/validate_chart_data.py`.

## Decision Tree

- If the user provides only a topic, ask up to 3 missing questions unless they requested speed. Minimum needed: audience, desired outcome, slide count/time.
- If the user provides a long document, load `templates/import/document-extraction.yaml`, then extract sections, metadata, claims, evidence, tables, and media; do not preserve document order by default.
- If the user provides a bad deck, diagnose against `references/rubrics.md`, then produce a revised slide-function map before rewriting.
- If the user asks for design improvement, load `references/design-system.md`.
- If the user asks for a full deck artifact, load `references/output-contracts.md`, plus `templates/runtime/export-contract.yaml` when a real file export is expected.
- If deciding how heavy the process should be, load `templates/runtime/workflow-modes.yaml`.
- If choosing the presentation scenario, load `templates/deck/playbook-routing.yaml`.
- If the deck is sales/webinar/pitch, load `references/narrative-patterns.md`.
- If selecting deck sequence, load `references/roteiro-template-library.md`.
- If selecting per-slide structure, load `references/slide-structure-library.md`.
- If choosing among many templates or avoiding repetition, load `references/template-selection-guide.md`.
- If the user asks for a full deck, benchmark deck, sales deck, webinar, VSL, offer deck, board update, financial deck, product strategy deck, or deck rewrite, load `templates/index.yaml`.
- If the deck depends on factual research, source selection, motion media, scholar evidence, or local files, load `templates/research/source-routing.yaml`.
- If factual claims, benchmarks, market statements, financial numbers, case studies, or technical comparisons appear, load `templates/research/evidence-ledger.yaml`.
- If importing or deriving behavior from existing PPTX/template families, load `templates/import/induced-layout-packs.yaml`.
- If importing a concrete PPTX template or brand deck, load `templates/import/pptx-template-manifest.yaml` and produce a template import report before promising fidelity.
- If matching a known source deck family without relying on external repos, load `templates/import/source-deck-fixtures.yaml` and select the closest fixture pack before selecting visual templates.
- If claiming best-in-class template import or brand deck replication, load `templates/import/template-import-regression-corpus.yaml`; the claim must map to source-family cases and fidelity checks.
- If user asks for local models, BYOK, Ollama, LM Studio, OpenAI-compatible APIs, image providers, or privacy-preserving generation, load `templates/runtime/provider-routing.yaml`.
- If the deck is research-heavy, technical, strategic, educational, or the prior process failed from outline-to-slide literalism, load `templates/runtime/manuscript-pipeline.yaml`.
- If building a story arc, load `templates/runtime/story-arc-contract.yaml`.
- If claiming narrative superiority or improving a weak deck process, load `templates/runtime/narrative-regression-corpus.yaml` and map the deck to a narrative case with an executable failure test.
- If creating or validating a slide-function map, load `templates/runtime/slide-function-map-contract.yaml`.
- If moving from narrative/design into renderable execution, load `templates/runtime/storyboard-render-bridge.yaml` before export or implementation.
- If the deck quality depends on premium narrative + design fit, load `templates/runtime/narrative-design-moment-grammar.yaml` and assign a moment archetype to every key slide.
- If defining visual direction, load `templates/runtime/design-direction-contract.yaml`.
- If the goal is premium visual quality, brand fidelity, imported template replication, or "gabaritar Design", load `templates/visual/design-mastery-contract.yaml` and treat Design as a measurable release gate, not subjective taste.
- If the goal is brand fidelity, matching a reference deck, or closing Design benchmark gaps, load `templates/visual/brand-fidelity-playbooks.yaml` and produce a brand fidelity report before claiming template/brand replication.
- If explaining or updating Design benchmark scores, load `templates/runtime/design-score-evidence.yaml` and cite the concrete evidence behind each score band.
- If claiming theme/runtime superiority, load `templates/runtime/theme-runtime-snapshot-suite.yaml` and verify that tokens reach charts, diagrams, tables, media, metadata, and export fallbacks.
- If `design-mastery-contract.yaml` is selected, produce `brand-template-manifest.yaml`, `design-mastery-report.yaml`, `key-slide-render-review.yaml`, and `visual-regression-checklist.yaml`; run `scripts/validate_design_mastery.py` before final delivery when files exist.
- Use `examples/design-100-fixture/` as the minimum passing reference for Design 100 package shape and evidence depth.
- If the visual brief is weak and there is no brand/reference/imported template, load `templates/theme/design-philosophy-routing.yaml`.
- If slide templates must guide the model directly, load `templates/runtime/template-example-routing.yaml`.
- If selected slide templates must be injected into a prompt, run `scripts/build_template_examples.py` where practical.
- If selecting templates for key slides or charts, load `templates/runtime/template-selection-report.yaml` and record rejected runners-up.
- If the deck is long, exported, branded, image-heavy, or PPTX-bound, load `templates/runtime/render-lock.yaml`.
- If speaker notes, recorded delivery, narration, video, async pitch, or webinar replay matter, load `templates/runtime/speaker-notes-narration-contract.yaml`.
- If improving non-design/non-narrative benchmark gaps, load `templates/runtime/runtime-gap-absorption-corpus.yaml` and do not raise runtime scores without acceptance artifacts.
- If the deck must be shared, handed off, published, analyzed, or packaged for another person/tool, load `templates/runtime/delivery-package-contract.yaml` and produce `delivery-manifest.yaml`.
- If the process must run as CLI, API, MCP, batch, or reusable automation, load `templates/runtime/api-mcp-cli-contract.yaml`; CLI/API/MCP must share the same job-state semantics.
- If the process is resumable, batched, exposed as CLI/API/MCP, or has export tasks, load `templates/runtime/job-state.schema.yaml` and produce `job-state.yaml`.
- If multiple sources, older decks, imported templates, memory, or process logs can conflict, load `templates/runtime/source-of-truth-policy.yaml`.
- If editing an existing deck or producing prompt-to-edit output, load `templates/runtime/edit-history.yaml`.
- If editing should preserve story, visual rhythm, selected regions, or render-lock, load `templates/runtime/storyboard-edit-contract.yaml` before applying the edit.
- If the slide process must be audited, shared, debugged, or improved across runs, load `templates/runtime/trace-handoff.yaml`.
- If the deck needs generated images, hero scenes, visual concepts, or internal image composition, load `templates/visual/ai-image-type-routing.yaml` and `templates/visual/composition-patterns.yaml`; separate image type from slide layout and declare Primary + Modifier composition.
- If the deck includes chart datasets or a chart editor contract, load `templates/visual/chart-data-contracts.yaml`; run `scripts/validate_chart_data.py` where practical.
- If the deck needs architecture diagrams, sequence diagrams, mathematical figures, sourced paper figures, or technical visual rendering, load `templates/runtime/diagram-rendering.yaml`.
- If authoring in HTML/CSS before PPTX/PDF, load `templates/runtime/html-to-pptx.yaml`.
- If exporting PPTX/PDF/screenshots/thumbnails, load `templates/runtime/export-contract.yaml`.
- If generating or validating PPTX, load `templates/qa/pptx-technical-gates.yaml`; run `scripts/check_pptx_placeholders.py` when a PPTX file exists and placeholder safety matters.
- If scoring a full deck, load `templates/qa/squad-quality-rubric.yaml`; killer items block release regardless of aggregate score.
- If key slides are rendered or the user complains the deck looks bad, load `templates/eval/rendered-eval.yaml`.
- If claiming high visual/rendered quality or "Design 100", load `templates/eval/rendered-design-fixture-set.yaml` and select the fixture set that matches the deck job.
- If claiming Design category leadership, load `templates/eval/design-regression-corpus.yaml` and run `scripts/validate_design_capability.py` when updating the skill or bench.
- If `rendered-eval.yaml` exists, run `scripts/validate_rendered_eval.py` or rely on `scripts/validate_deck_package.py` to enforce rendered score thresholds.
- If a prior failure mode is known, load `templates/qa/regression-fixtures.yaml`.
- If the user asks for editable PPTX, native runtime, or "real .pptx output", route through `@sinkra/slides-renderer` (Native IR → DrawingML via `packages/@sinkra/slides-renderer`); never emit raster as default.
- If the user asks for real deck generation (not just spec), set `provider.mode = "codex"` in the runtime call. `provider.mode = "dummy"` is smoke-only and is forced when `CI=true`. On codex failure the runtime falls back to the structured composer (`composeStructuredFallback`), never the 5-slide crude stub. Surface `job_state.errors[]` `provider_fallback:*` entries to the operator.
- If the user asks for "an API for this", "an MCP for this", "expose this as a service", or "run this in CI/batch", route to `apps/squad-engine` REST (`/api/v1/slides/*`), `@sinkra/slides-mcp` tools (`slides.generate|review|export|edit|show`), or `scripts/sinkra/slides-cli.mjs` — all three share `@sinkra/slides-core` so parity is mandatory.
- If you generate a deck via runtime and the user requests premium/Design 100, run `scripts/validate_design_100_runtime.py outputs/slides-creator/{run_id} --strict` and respect the verdict (`DESIGN_100` only when overall >= 95 and zero blockers).
- If the runtime touches any of CLI/API/MCP, run `scripts/validate_runtime_parity.py` before publishing — surfaces drift = release block.
- If a forward test or previous failure mode exists, run `scripts/run_regression_fixtures.py` before final delivery.
- If updating or packaging narrative capability, run `scripts/validate_narrative_capability.py`.
- If updating narrative/design integration or storyboard edit capability, run `scripts/validate_narrative_design_capability.py`.
- If updating runtime/editor/export/distribution/multimedia capability, run `scripts/validate_runtime_gap_capability.py`.
- If updating delivery, sharing, API, MCP, CLI, or packaging capability, run `scripts/validate_delivery_capability.py`.
- If writing a machine-readable deck package, run `scripts/build_evidence_ledger.py` after `deck-spec.yaml` exists, then `scripts/validate_runtime_contracts.py` and `scripts/validate_deck_package.py` before final delivery.
- If updating or packaging this skill, run `scripts/validate_skill_independence.py .` from the skill directory to ensure no external squad path is required.
- If selecting deck sequence, load `templates/deck/route-map.yaml` and `templates/deck/copy-derived.yaml` before using legacy reference libraries.
- If selecting per-slide structures, load `templates/slide/function-library.yaml`.
- If choosing visual layouts, diagrams, charts, media, or matrix behavior, load the relevant files in `templates/visual/`.
- If choosing style, load `templates/theme/theme-tokens.yaml`.
- If the user asks "how should this work as product/runtime" or mentions PPTX/API/MCP/editor/prompt-to-edit/local models, load `templates/runtime/` and `references/bench-absorption-map.md`.
- If the user asks for QA/review, load `references/rubrics.md`.
- If the user asks to improve a weak process/deck or mentions a prior bad run, load `references/regression-test-protocol.md`.

## Required Outputs

For full deck creation, produce these sections or files:

1. `briefing-normalized`
2. `audience-belief-shift`
3. `story-arc`
4. `slide-function-map`
5. `design-direction`
6. `roteiro-template-selection`
7. `slide-structure-selection`
8. `visual-template-selection`
9. `template-selection-report`
10. `theme-profile-selection`
11. `render-lock`
12. `runtime-job-selection`
13. `job-state`
14. `source-of-truth-policy`
15. `research-route-selection`
16. `import-pipeline-selection`
17. `rendered-eval-selection`
18. `bench-capability-selection`
19. `deck-spec`
20. `speaker-notes`
21. `qa-report`
22. `revision-notes`
23. `forward-test` when improving a known weak process
24. `source-ledger` when the deck contains factual or comparison claims
25. `package-validation-report` when files are created
26. `design-mastery-report` when the user requests premium/reference-level design or Design 100
27. `delivery-manifest` when the output must be shared, handed off, published, or consumed by another tool/runtime

Use Markdown by default. Use JSON/YAML only when the user asks for machine-readable output or when generating assets for code.

## Non-Negotiable Gates

- **Narrative compression:** slides are moments, not topics.
- **Narrative capability corpus:** narrative leadership claims require a matched narrative regression case with current belief, desired belief, proof standard, and failure test.
- **Storyboard bridge:** full decks must connect story arc, slide function, visual template, density, proof, and render risk before implementation.
- **Narrative-design moment:** key slides must declare the moment archetype they perform, including audience state before/after, density budget, proof visibility, visual move, and failure mode.
- **Workflow fit:** use micro, standard, full-package, repair, benchmark, or export mode according to the request; do not produce full-package overhead for a quick critique.
- **Playbook routing:** choose a deck playbook before selecting slide templates so the deck follows a proven scenario arc.
- **Slide function:** every slide has a job in the audience journey.
- **Audience movement:** every slide states the belief, question, confidence, or decision state it changes.
- **No explain-topic functions:** `explicar`, `apresentar`, `mostrar`, `listar`, and equivalent English verbs are blockers when used as slide movement.
- **Action title:** every title makes a claim; no generic topic labels.
- **Density:** default max 45 visible words per slide, except tables/appendices.
- **Layout variety:** no more than 2 consecutive slides with the same structure.
- **Template selection:** every slide must declare one structure template and why that template fits the slide function.
- **Selection audit:** key slide/template/chart decisions must include rejected runners-up with deck-specific reasons.
- **Template registry first:** use `templates/` contracts before drafting full decks. Do not rely only on free-form Markdown references.
- **Render lock:** full decks and exportable decks must lock colors, fonts, chart palette, image style, visual composition, and forbidden features before rendering.
- **Provenance:** when a template is selected, keep its absorbed source visible in the reasoning when useful.
- **Visual grammar:** charts and diagrams must match data shape, not aesthetic preference.
- **Bench absorption:** when solving a known capability, reuse the mapped benchmark pattern rather than inventing a new one.
- **Research routing:** HTML sources, motion media, scholar evidence, and local files use different routes.
- **Evidence ledger:** high-stakes factual or comparison claims must be mapped to sources, confidence, freshness, and slide use.
- **Induced pack selection:** imported templates are selected by deck job, media behavior, and audience, not by aesthetics alone.
- **Provider routing:** local/privacy/provider requirements must be explicit before selecting model, image, vision, or research capability.
- **Manuscript-first:** research-heavy or failed-process decks must create a manuscript before slide copy.
- **Edit history:** prompt edits must produce scoped diffs and rerun local QA for changed slides.
- **Storyboard-safe edits:** prompt edits must preserve belief shift, source truth, render-lock, design moment, and unselected regions unless the user explicitly overrides them.
- **Traceable handoffs:** reusable processes must keep compact stage traces and revision decisions.
- **Source-of-truth:** when deck state, source ledger, briefing, imported templates, memory, or user instructions conflict, declare which source wins.
- **Job state:** resumable, batch, CLI, API, MCP, or export jobs must record task state, progress events, artifacts, policy, and verdict.
- **Delivery package:** shareable outputs must declare artifacts, permissions, export targets, validation reports, known blockers, and follow-up signals when analytics exist.
- **Automation parity:** CLI, API, and MCP surfaces must map to the same commands, job states, safety boundaries, and artifacts.
- **Regression fixtures:** known failure modes become forward tests before the process is called improved.
- **Rendered evaluation:** important final decks must evaluate rendered key slides, not only source text.
- **Verified export:** never claim PPTX/PDF export success before output-path verification.
- **Native runtime parity:** CLI/API/MCP surfaces MUST share `@sinkra/slides-core`. A behavioral difference between surfaces is a release blocker — enforced by `validate_runtime_parity.py`.
- **Design 100 runtime gate:** any deck claiming Design 100 MUST emit `design-mastery-report.yaml` with verdict `DESIGN_100`, editability_score ≥ 95, and zero BLOCKER findings. Subjective taste is not evidence.
- **PPTX technical safety:** no residual placeholders, unsafe math, overlap, clipping, theme-mismatched diagrams, or unverified text fit.
- **Image type routing:** AI image prompts must declare internal composition, container size, text policy, and whether the visual is decorative, explanatory, evidentiary, or product-representational.
- **Visual composition:** image-heavy slides must declare Primary + Modifier composition and native overlay plan.
- **Chart data validation:** chart data shape must match the selected chart mode before visual styling.
- **Diagram engine routing:** technical diagrams must declare Graphviz, Mermaid, TikZ, native shapes, or extracted-figure policy before rendering.
- **Template import honesty:** imported PPTX templates produce metadata/manifests first; fidelity claims require render comparison.
- **Executable helpers:** when a bundled script exists for a repeated artifact, use it instead of recreating the artifact by hand.
- **Skill independence:** runtime must not require `squads/`, squad agents, or private source paths; absorbed patterns must be bundled locally.
- **Proof:** factual claims need source, artifact, example, demo, or explicit assumption label.
- **Design direction:** visual system must exist before draft and must not be just brand colors applied as a skin.
- **Design mastery:** premium deck design requires template/brand manifest, layout variety, theme runtime, rendered proof, and explicit anti-pattern checks before final delivery.
- **Design 100 validation:** when Design 100 is requested, final delivery must include the four Design artifacts and pass `validate_design_mastery.py` if a package directory is available.
- **Design capability corpus:** Design leadership claims require template import corpus, rendered fixture corpus, and theme runtime snapshot suite; validate them with `validate_design_capability.py`.
- **Killer items:** use `templates/qa/squad-quality-rubric.yaml`; any killer item blocks final release.
- **Key-slide gate:** important decks must validate cover, reframe, mechanism, proof/demo, and CTA before full render.
- **Regression gate:** if a prior process failed, map old failure modes to new blockers before rerendering.
- **Critique loop:** final answer must include what was improved after critique.

## Quality Bar

Score the deck with this weighting:

| Dimension | Weight |
|---|---:|
| Narrativa | 25 |
| Design editorial | 25 |
| Acurácia/prova | 20 |
| Editabilidade | 10 |
| Brand | 10 |
| Técnica/export | 10 |

If the weighted score is below 85, revise. If below 75, do not present it as final; present it as a diagnostic draft.

## Bundled References

- `scripts/build_template_examples.py`: converts selected slide-function templates into compact Markdown/XML prompt examples.
- `scripts/build_evidence_ledger.py`: extracts slide evidence from `deck-spec.yaml` into `source-ledger.yaml`.
- `scripts/validate_deck_package.py`: validates required package files, basic slide shape, repeated structures, and sourced evidence.
- `scripts/run_regression_fixtures.py`: runs forward-test fixtures for narrative, design, research, render, and template-selection failure modes.
- `scripts/validate_rendered_eval.py`: validates rendered slide scores, blockers, descriptions, revision actions, and referenced image paths.
- `scripts/validate_runtime_contracts.py`: validates render-lock, template-selection-report, job-state, source-of-truth-policy, and speaker-notes preservation.
- `scripts/validate_design_capability.py`: validates bundled Design corpora for regression coverage, source-family coverage, and theme runtime snapshots.
- `scripts/validate_narrative_capability.py`: validates bundled narrative regression cases across deck jobs, belief shifts, proof standards, and failure tests.
- `scripts/validate_runtime_gap_capability.py`: validates storyboard, speaker-note/narration, and remaining runtime gap acceptance contracts.
- `scripts/check_pptx_placeholders.py`: checks PPTX slide XML for residual placeholders such as `{{MATH:`.
- `scripts/validate_chart_data.py`: validates chart datasets against label-value, xy, multi-series, range, waterfall, OHLC, box-plot, hierarchical, flow, funnel, heatmap, histogram, and gauge modes.
- `scripts/validate_skill_independence.py`: validates that the skill does not require external squad files at runtime.
- `scripts/validate_design_100_runtime.py`: bridges runtime artifacts (Native IR + editability-report) with the design-mastery contracts; emits `design-mastery-report.yaml` and refuses Design 100 unless overall ≥ 95 and zero blockers.
- `scripts/validate_runtime_parity.py`: smoke-runs the CLI/API/MCP surfaces against the same dummy briefing and proves the three produce identical artifact shapes (CLI ↔ API ↔ MCP parity gate).
- `templates/index.yaml`: canonical template registry and routing order.
- `templates/deck/route-map.yaml`: deck roteiro templates for benchmarks, webinars, finance, sales, board, product strategy, and discovery.
- `templates/deck/copy-derived.yaml`: offer, VSL, cohort launch, and investor pitch templates absorbed from SINKRA copy and pitch squads.
- `templates/deck/playbook-routing.yaml`: fast scenario routing for benchmark, webinar, sales, VSL, finance, product, investor, and course/workshop decks.
- `templates/slide/function-library.yaml`: slide-function templates with slots, constraints, and QA.
- `templates/visual/`: chart, chart-data, AI-image, diagram, layout family, and media-fit rules absorbed from benchmark projects.
- `templates/visual/chart-data-contracts.yaml`: chart dataset modes, required fields, editor-mode mapping, and validation blockers.
- `templates/visual/ai-image-type-routing.yaml`: AI image composition types, purpose routing, text policy, and container-size rules.
- `templates/visual/composition-patterns.yaml`: Primary + Modifier visual composition grammar, native overlays, PPTX fallbacks, and audit ids.
- `templates/visual/aiox-brandbook-deep-patterns.yaml`: AIOX editorial spreads, proof walls, pitch components, category creation, roadmap, offer and problem sections.
- `templates/visual/redpine-deep-patterns.yaml`: Redpine report grid, palette stack, component/a11y manifest cards, status rows, decision panels, tabs, and briefing fields.
- `templates/theme/theme-tokens.yaml`: theme profiles separated from slide structure.
- `templates/theme/brand-systems.yaml`: Redpine and AIOX Brandbook theme profiles extracted from local design-system sources.
- `templates/theme/design-philosophy-routing.yaml`: 20 fallback design philosophies across 5 schools for visually vague briefs.
- `templates/runtime/`: generation, edit, batch, import, and prompt-to-edit job contracts.
- `templates/runtime/workflow-modes.yaml`: process depth selector for micro replies, standard specs, full packages, repairs, benchmarks, and exportable decks.
- `templates/runtime/story-arc-contract.yaml`: deck arc types, beat schema, validation, and anti-patterns.
- `templates/runtime/slide-function-map-contract.yaml`: function enum, audience movement rules, density targets, and compression rules.
- `templates/runtime/design-direction-contract.yaml`: visual reference, motif, density, variation, composition, and audience-context contract.
- `templates/runtime/render-lock.yaml`: anti-drift execution contract for colors, typography, chart palette, image style, forbidden features, and slide visual locks.
- `templates/runtime/template-selection-report.yaml`: selected template/chart plus rejected runners-up and deck-specific rationale.
- `templates/runtime/job-state.schema.yaml`: resumable job state, progress events, artifacts, export policy, and final verdict.
- `templates/runtime/source-of-truth-policy.yaml`: precedence and conflict-resolution policy for long or source-heavy deck jobs.
- `templates/runtime/manuscript-pipeline.yaml`: planner, research manuscript, claim/evidence, and renderer handoff pipeline.
- `templates/runtime/html-to-pptx.yaml`: browser-rendered HTML to PPTX/PDF conversion, placeholder extraction, overflow, and rasterization rules.
- `templates/runtime/export-contract.yaml`: reproducible export task, worker response, output verification, and preview contract.
- `templates/runtime/template-example-routing.yaml`: selected template examples and per-outline template override routing.
- `templates/runtime/trace-handoff.yaml`: traceable stage flow, typed handoffs, review universes, and synthesis report.
- `templates/runtime/provider-routing.yaml`: provider, local model, image, vision, research, and fallback capability routing.
- `templates/runtime/edit-history.yaml`: undo/redo-inspired edit snapshots, diff summaries, and local QA reruns.
- `templates/runtime/diagram-rendering.yaml`: Graphviz, Mermaid, TikZ, native-shape, and PDF-figure extraction routing.
- `templates/research/source-routing.yaml`: separate routes for HTML sources, motion media, scholar/benchmark evidence, and local files.
- `templates/research/evidence-ledger.yaml`: slide-level claim/source/confidence/freshness ledger.
- `templates/import/document-extraction.yaml`: structured document extraction, captions, metadata, claim/evidence inventory.
- `templates/import/induced-layout-packs.yaml`: PPTAgent-derived pack selection for academic, technical, institutional, and UI decks.
- `templates/import/pptx-template-manifest.yaml`: PPTX template manifest extraction, placeholder geometry, theme metadata, assets, and import report.
- `templates/eval/rendered-eval.yaml`: multimodal rendered slide scoring for vision, content, logic, and technical integrity.
- `templates/qa/regression-fixtures.yaml`: forward tests for narrative, design, research, render, and template-selection failures.
- `templates/qa/pptx-technical-gates.yaml`: PPTX overlap, clipping, text-fit, math, diagram, density, and scoring gates.
- `templates/qa/squad-quality-rubric.yaml`: self-contained 6-dimension score, killer items, release criteria, and corrective actions.
- `templates/qa/`: narrative, visual, template-selection, and copy gates.
- `templates/wireframes/`: simple HTML visual references for matrix, mechanism, proof, and webinar flow.
- `references/narrative-patterns.md`: deck types, story arcs, slide functions.
- `references/template-selection-guide.md`: template routing by deck job and slide function.
- `references/roteiro-template-library.md`: 45 complete deck roteiro templates by use case.
- `references/slide-structure-library.md`: 240+ slide structure templates with use/avoid rules.
- `references/bench-absorption-map.md`: what to absorb from Presenton, Gamma, ppt-master, PPTAgent, presentation-ai, banana-slides, powerpoint-skill, slide-deck-ai, and PresentAgent-2.
- `references/design-system.md`: visual direction, layout patterns, density rules.
- `references/rubrics.md`: QA scoring and critique protocol.
- `references/output-contracts.md`: reusable artifact schemas and final package format.
- `references/anti-patterns.md`: known failure modes, especially outline-to-deck literalism.
- `references/regression-test-protocol.md`: forward-test format for preventing known deck/process failures from recurring.

Load only the reference needed for the current task.

## Default Final Response

When returning work to the user, keep it concise:

- State the recommended deck thesis.
- Show slide list with function + action title.
- Mention design direction.
- Mention QA score and the main remaining risk.
- Provide the generated artifact or file path when files were created.


## Referência: references/source/agents/openai.yaml

```yaml
interface:
  display_name: "Slide Creator"
  short_description: "Narrative-first slide deck system"
  brand_color: "#D7FF3F"
  default_prompt: "Use $slide-creator to turn this briefing into a complete narrative-first deck with story arc, slide-function map, design direction, and QA."
policy:
  allow_implicit_invocation: true
```


## Referência: references/source/examples/design-100-fixture/brand-template-manifest.yaml

```yaml
brand_template_manifest:
  deck_id: design-100-fixture
  generated_at: "2026-05-18"
  source_reference:
    type: bundled_theme
    path_or_url: templates/theme/theme-tokens.yaml#sinkra_observatory_dark
    license_or_usage_note: Bundled skill reference.
    confidence: high
  visual_dna:
    summary: Dark editorial benchmark system with square surfaces, hairline borders, sparse neon accent, compressed uppercase metadata, and large claim-first hierarchy.
    non_color_traits:
      - Square panel geometry with low-radius or no-radius containers.
      - Hairline dividers separate metadata, evidence, and primary claims.
      - Action title dominates before supporting copy.
      - Accent is used as sparse signal, never as full-slide decoration.
      - Mono metadata labels identify stage, source, and confidence.
    must_preserve:
      - Claim-first hierarchy.
      - Sparse accent usage under 18 percent of visible area.
      - Consistent 12-column grid and safe margins.
      - Source/provenance treatment for evidence slides.
    must_avoid:
      - Decorative card stacks.
      - Atmospheric stock imagery.
      - Gradient orb backgrounds.
      - Generic section title slides.
  token_map:
    colors:
      background: "#050505"
      surface: "#111111"
      surface_alt: "#171717"
      text: "#F5F5EF"
      muted_text: "#9A9A92"
      accent: "#D7FF3F"
      border: "#2A2A2A"
      positive: "#41C875"
      negative: "#EF5350"
      warning: "#F0B35A"
    typography:
      heading_family: Inter Tight
      body_family: Inter
      mono_family: IBM Plex Mono
      title_px: 64
      body_px: 28
      min_px: 20
      weights: [400, 600, 700, 800]
    spacing:
      canvas: "16:9"
      grid_columns: 12
      margin_px: 56
      gutter_px: 24
      section_gap_px: 40
    shape_language:
      corner_radius_px: 0
      stroke_px: 1
      shadow_policy: none
      surface_policy: flat dark panels with hairline border
    chart_palette:
      primary: ["#D7FF3F", "#5E8CFF", "#F0B35A", "#9EAD4D"]
      neutral: "#777777"
      grid: "#2A2A2A"
      highlight: "#D7FF3F"
  layout_families:
    - id: hero_claim
      role: cover/reframe
      use_when:
        - The slide must anchor a thesis or audience belief shift.
      avoid_when:
        - Dense evidence is required on the same slide.
      density: low
      slots:
        - id: metadata_strip
          role: orientation
          bounds_hint: top 8 percent
        - id: claim
          role: dominant action title
          bounds_hint: left 60 percent
    - id: evidence_matrix
      role: proof/comparison
      use_when:
        - Multiple proof points need scanning and comparison.
      avoid_when:
        - The slide has a single emotional point.
      density: high
      slots:
        - id: row_header
          role: dimension label
          bounds_hint: left rail
        - id: evidence_cells
          role: scores and proof
          bounds_hint: main grid
  component_patterns:
    - id: mono_metadata_label
      role: stage/source/confidence label
      visual_rules:
        - uppercase
        - letter-spaced mono
        - muted text
      reuse_for_slide_functions: [cover, proof, mechanism]
    - id: evidence_card
      role: compact proof cell
      visual_rules:
        - square panel
        - hairline border
        - score large, reason small
      reuse_for_slide_functions: [proof, contrast, benchmark]
    - id: accent_rule
      role: directional emphasis
      visual_rules:
        - one-pixel line
        - accent color only
        - never decorative orb
      reuse_for_slide_functions: [reframe, synthesis, cta_concrete]
  chart_language:
    chart_types_allowed: [bar, bullet, matrix, slope, waterfall]
    label_policy: native text labels, no chart-as-image for core data
    axis_policy: show baselines and units when quantitative
    annotation_policy: use sparse accent callouts for decision points
  media_language:
    image_treatment: evidence-first screenshots or product-representational images only
    crop_policy: preserve inspection detail; avoid dark blurred crops
    icon_policy: mono line icons only when they clarify a tool/action
    product_or_evidence_media_policy: screenshots must preserve readable UI and source context
  anti_patterns:
    - id: identity_as_skin
      description: Using only logo/colors while ignoring layout, type, density, and component behavior.
    - id: generic_stock_visual
      description: Using atmospheric images that do not prove, demonstrate, or clarify the slide claim.
    - id: neon_overuse
      description: Using accent as decoration instead of signal.
  evidence:
    inspected_assets:
      - path: templates/theme/theme-tokens.yaml#sinkra_observatory_dark
        observed_rule: Dark benchmark palette, Inter/mono typography, sparse accent, high contrast.
      - path: templates/visual/layout-families.yaml#executive_dense
        observed_rule: Dense slides must preserve scanability and reserve detail for appendix.
    unresolved_questions: []
```


## Referência: references/source/examples/design-100-fixture/design-mastery-report.yaml

```yaml
design_mastery_report:
  deck_id: design-100-fixture
  generated_at: "2026-05-18"
  target_score: 95
  verdict: pass
  source_artifacts:
    brand_template_manifest: brand-template-manifest.yaml
    design_direction: design-direction.yaml
    render_lock: render-lock.yaml
    template_selection_report: template-selection-report.yaml
    key_slide_render_review: key-slide-render-review.yaml
    visual_regression_checklist: visual-regression-checklist.yaml
  score_lenses:
    - id: template_manifest
      weight: 15
      score: 97
      evidence: brand-template-manifest.yaml covers tokens, type, grid, component patterns, chart language, media language, and anti-patterns.
      blockers: []
    - id: brand_fidelity
      weight: 20
      score: 96
      evidence: brand-template-manifest.yaml and key-slide-render-review.yaml verify non-color traits, sparse accent, hairlines, metadata labels, and claim-first hierarchy.
      blockers: []
    - id: layout_intelligence
      weight: 20
      score: 96
      evidence: template-selection-report.yaml ties layouts to slide function and records rejected runners-up with deck-specific reasons.
      blockers: []
    - id: rendered_quality
      weight: 20
      score: 96
      evidence: key-slide-render-review.yaml reviews five decisive roles with aggregate score above 95 and no unresolved blockers.
      blockers: []
    - id: theme_runtime
      weight: 15
      score: 96
      evidence: render-lock.yaml maps theme tokens to backgrounds, text, borders, charts, image policy, and slide visual locks.
      blockers: []
    - id: iteration_loop
      weight: 10
      score: 95
      evidence: key-slide-render-review.yaml records an applied spacing patch and no open visual patches.
      blockers: []
  calculated_score: 96.1
  microdimension_mapping:
    visual_layout_quality__layout_variety:
      evidence: template-selection-report.yaml
      target_met: true
    visual_layout_quality__visual_density_control:
      evidence: visual-regression-checklist.yaml
      target_met: true
    visual_layout_quality__rendered_visual_quality:
      evidence: key-slide-render-review.yaml
      target_met: true
    template_import_replication__template_manifest:
      evidence: brand-template-manifest.yaml
      target_met: true
    template_import_replication__brand_fidelity:
      evidence: brand-template-manifest.yaml
      target_met: true
    template_import_replication__template_selection_logic:
      evidence: template-selection-report.yaml
      target_met: true
    theme_tokens_branding__token_schema:
      evidence: render-lock.yaml
      target_met: true
    theme_tokens_branding__theme_runtime:
      evidence: render-lock.yaml
      target_met: true
    theme_tokens_branding__brand_guardrails:
      evidence: visual-regression-checklist.yaml
      target_met: true
  required_fixes:
    - slide_id: s01
      issue: Cover metadata was too close to the title in first review.
      patch_type: spacing_fix
      owner: slide-creator
      status: fixed
```


## Referência: references/source/examples/design-100-fixture/key-slide-render-review.yaml

```yaml
key_slide_render_review:
  deck_id: design-100-fixture
  generated_at: "2026-05-18"
  render_source: manual_preview
  reviewed_slides:
    - slide_id: s01
      required_role: cover
      screenshot_or_preview_path: previews/s01.png
      score:
        hierarchy: 98
        scan_path: 96
        whitespace: 96
        contrast: 98
        alignment: 96
        crop_and_media_relevance: 95
        title_claim_visibility: 99
        body_text_fit: 96
        chart_or_diagram_readability: 95
        brand_fidelity: 97
      average_score: 96.6
      blockers: []
      visual_patches:
        - patch_type: spacing_fix
          instruction: Increased top metadata gap to keep the action title dominant.
          status: applied
    - slide_id: s02
      required_role: reframe
      screenshot_or_preview_path: previews/s02.png
      score: {hierarchy: 96, scan_path: 95, whitespace: 95, contrast: 97, alignment: 96, crop_and_media_relevance: 95, title_claim_visibility: 96, body_text_fit: 96, chart_or_diagram_readability: 95, brand_fidelity: 96}
      average_score: 95.7
      blockers: []
      visual_patches: []
    - slide_id: s03
      required_role: mechanism
      screenshot_or_preview_path: previews/s03.png
      score: {hierarchy: 95, scan_path: 96, whitespace: 95, contrast: 97, alignment: 96, crop_and_media_relevance: 95, title_claim_visibility: 96, body_text_fit: 95, chart_or_diagram_readability: 96, brand_fidelity: 96}
      average_score: 95.7
      blockers: []
      visual_patches: []
    - slide_id: s04
      required_role: proof_or_demo
      screenshot_or_preview_path: previews/s04.png
      score: {hierarchy: 96, scan_path: 95, whitespace: 95, contrast: 97, alignment: 95, crop_and_media_relevance: 95, title_claim_visibility: 96, body_text_fit: 95, chart_or_diagram_readability: 97, brand_fidelity: 96}
      average_score: 95.7
      blockers: []
      visual_patches: []
    - slide_id: s05
      required_role: cta_or_decision
      screenshot_or_preview_path: previews/s05.png
      score: {hierarchy: 97, scan_path: 96, whitespace: 96, contrast: 98, alignment: 96, crop_and_media_relevance: 95, title_claim_visibility: 98, body_text_fit: 96, chart_or_diagram_readability: 95, brand_fidelity: 97}
      average_score: 96.4
      blockers: []
      visual_patches: []
  aggregate:
    average_score: 96.02
    lowest_slide_score: 95.7
    verdict: pass
```


## Referência: references/source/examples/design-100-fixture/render-lock.yaml

```yaml
canvas:
  aspect_ratio: "16:9"
  width_px: 1920
  height_px: 1080
  safe_margin_px: 72
colors:
  background: "#050505"
  surface: "#111111"
  surface_alt: "#171717"
  text: "#F5F5EF"
  muted_text: "#9A9A92"
  border: "#2A2A2A"
  accent: "#D7FF3F"
  warning: "#F0B35A"
  positive: "#41C875"
  negative: "#EF5350"
typography:
  heading_family: Inter Tight
  body_family: Inter
  mono_family: IBM Plex Mono
  heading_weight: 800
  body_weight: 400
  body_px: 28
  title_px: 64
  min_body_px: 20
chart_palette:
  primary: ["#D7FF3F", "#5E8CFF", "#F0B35A", "#9EAD4D"]
  neutral: "#777777"
  grid: "#2A2A2A"
  highlight: "#D7FF3F"
  rules:
    - Chart colors must come from chart_palette.
    - Axis, labels, and legends remain native/editable when PPTX output is requested.
image_style_lock:
  rendering_family: interface_capture
  palette_policy: brand_exact
  texture_policy: none
  text_policy_default: native_overlay
  prompt_rules:
    - Exact labels, numbers, formulas, citations, UI copy, and chart text remain native.
slide_visual_locks:
  - slide_id: s01
    slide_function: cover
    layout_family: hero_claim
    composition_pattern: metadata_strip_plus_large_claim
    image_type: none
    chart_or_diagram_template: none
    native_overlay_plan: all text native
    allowed_overrides: [accent_rule_position]
  - slide_id: s03
    slide_function: proof
    layout_family: evidence_matrix
    composition_pattern: left_dimension_rail_plus_score_cells
    image_type: none
    chart_or_diagram_template: matrix
    native_overlay_plan: all scores and labels native
    allowed_overrides: [cell_count]
forbidden_features:
  svg: [foreignObject, script, iframe, animate, textPath]
  pptx: [rasterized_action_title, residual_placeholder_tokens, uneditable_core_claim_text]
asset_status: []
```


## Referência: references/source/examples/design-100-fixture/template-selection-report.yaml

```yaml
template_selection_report:
  deck_id: design-100-fixture
  generated_at: "2026-05-18"
  selection_scope: slide
  rules:
    - Every key slide records selected template and at least two rejected runners-up.
    - Rejected runners-up cite slide function, audience, evidence, or media constraints.
  selections:
    - slide_id: s01
      key_slide: true
      slide_function: cover
      selected:
        id: hero_claim
        name: Claim-first cover
        source_registry: visual/layout-families.yaml
        source_quote: Editorial persuasive decks require action-title hierarchy and low-medium density.
      selected_reason: The cover must establish the thesis instantly for an executive benchmark audience; hero_claim keeps the action title dominant and avoids decorative context.
      fit_scores:
        content_fit: 96
        visual_fit: 97
        evidence_fit: 92
        audience_fit: 96
        export_fit: 95
      rejected_runners_up:
        - id: executive_dense
          name: Dense KPI cover
          rejected_reason: Too much tabular density for the first belief-shift moment; it would make the thesis feel like a report index instead of a decision frame.
        - id: visual_story
          name: Full-bleed media cover
          rejected_reason: The deck has no evidentiary product image for the opener, so a full-bleed media treatment would become atmospheric.
      constraints_checked: [slot_count, text_length, media_area, evidence_visibility, pptx_editability]
      final_confidence: high
      qa_status: pass
    - slide_id: s03
      key_slide: true
      slide_function: proof
      selected:
        id: evidence_matrix
        name: Evidence matrix
        source_registry: visual/layout-families.yaml
        source_quote: Executive dense slides can use comparison tables when scanability is preserved.
      selected_reason: The proof slide needs to compare Design gaps by microdimension while keeping source and score readable.
      fit_scores:
        content_fit: 97
        visual_fit: 95
        evidence_fit: 98
        audience_fit: 94
        export_fit: 95
      rejected_runners_up:
        - id: hero_claim
          name: Single claim proof
          rejected_reason: A single-claim proof layout hides the microdimension spread that makes the Design gap actionable.
        - id: journey_map
          name: Journey map
          rejected_reason: The evidence is a capability matrix, not a time-based audience journey.
      constraints_checked: [slot_count, text_length, media_area, evidence_visibility, pptx_editability]
      final_confidence: high
      qa_status: pass
```


## Referência: references/source/examples/design-100-fixture/visual-regression-checklist.yaml

```yaml
visual_regression_checklist:
  deck_id: design-100-fixture
  generated_at: "2026-05-18"
  checks:
    - id: no_identity_as_skin
      question: "Does the deck use brand language beyond logo/colors?"
      status: pass
      evidence: brand-template-manifest.yaml maps type, grid, panels, metadata labels, chart language, and anti-patterns.
    - id: no_generic_stock_visual
      question: "Does every meaningful image prove, demonstrate, or clarify a claim?"
      status: pass
      evidence: render-lock.yaml uses no atmospheric media; image policy requires evidence-first screenshots.
    - id: no_repeated_layout_monotony
      question: "Are there no more than two consecutive slides in the same layout family?"
      status: pass
      evidence: template-selection-report.yaml alternates hero_claim and evidence_matrix for decisive slide roles.
    - id: no_dense_bullet_wall
      question: "Are dense slides intentionally structured as tables, diagrams, or appendix?"
      status: pass
      evidence: evidence_matrix uses row headers and score cells instead of bullet walls.
    - id: no_unmapped_theme_usage
      question: "Do charts, diagrams, tables, and shapes use mapped theme tokens?"
      status: pass
      evidence: render-lock.yaml maps chart_palette, text, borders, surfaces, and accent usage.
    - id: no_unrendered_key_slides
      question: "Were decisive slides reviewed in render or preview?"
      status: pass
      evidence: key-slide-render-review.yaml reviews all five decisive roles.
    - id: no_weak_action_title_hierarchy
      question: "Is the action title visually dominant on each decisive slide?"
      status: pass
      evidence: key-slide-render-review.yaml title_claim_visibility scores are all 96 or higher.
    - id: no_unresolved_overlap_clipping
      question: "Are overlap, clipping, and text-fit issues resolved?"
      status: pass
      evidence: key-slide-render-review.yaml has no blockers and all body_text_fit scores are 95 or higher.
  verdict: pass
  release_blockers: []
```


## Referência: references/source/references/anti-patterns.md

# Anti-Patterns

Use this reference when critiquing or improving a weak deck.

## Outline-To-Deck Literalism

Signal:

- each outline heading becomes one slide;
- slide order mirrors the source document;
- no belief shift or tension curve;
- deck feels like a document split into pages.

Correction:

- compress source into story arc;
- define slide functions;
- merge repeated functions;
- move detail to notes or appendix.

## Card Wall

Signal:

- many slides use the same grid of cards;
- every idea has equal visual weight;
- no editorial hierarchy.

Correction:

- convert key moments into proof artifacts, diagrams, contrasts, or big-claim slides;
- vary layout by slide function;
- limit repeated card layouts to intentional sequences.

## Brand Skinning

Signal:

- colors and logo are present, but composition is generic;
- brand tokens cover a weak wireframe;
- visual system does not help memory.

Correction:

- define visual thesis and motif;
- make design choices structural;
- tie motif to narrative, not decoration.

## Density Blindness

Signal:

- paragraphs on slides;
- small type;
- slide requires reading instead of presenting.

Correction:

- max 45 visible words;
- move nuance to speaker notes;
- replace text clusters with one diagram, table, or artifact.

## Weak Action Titles

Signal:

- titles name topics: `Market`, `Problem`, `Solution`, `Next Steps`;
- audience cannot understand the story by reading titles.

Correction:

- rewrite titles as claims with consequence;
- run a vertical test: title-only story should make sense in two minutes.

## Generic Proof

Signal:

- claims sound plausible but unsupported;
- examples are abstract;
- proof arrives too late.

Correction:

- attach source, artifact, case, demo, or assumption label to each major claim;
- place proof immediately after the claim that needs credibility.


## Referência: references/source/references/bench-absorption-map.md

# Bench Absorption Map

Use this reference whenever the task touches capabilities already covered by the slide benchmarks. Do not reinvent the workflow. Absorb the pattern, not the external code.

Sources synthesized from:

- `docs/bench/slides-creator-open-source-absorption/`
- `docs/bench/slides-creator-open-source-absorption/slide-creator-skill-blueprint.md`
- `docs/bench/presenton-vs-gamma/`

Canonical bench artifact: `slide-creator-skill-blueprint.md`. This file is the packaged skill-local version.

## Core Composition

No single project is the model. Use class winners by layer:

| Layer | Primary inspiration | Secondary inspiration | Absorb |
|---|---|---|---|
| App/product | Presenton | presentation-ai, Gamma | self-hosting, API, MCP, providers, editor/share UX |
| Skill/agentic reasoning | PPTAgent | slide creator skill | planning, reflection, critique, QA routing |
| Renderer/runtime | ppt-master | powerpoint-skill | native editable PPTX, template import, editability QA |
| Prompt-to-edit | banana-slides | presentation-ai, ppt-master | region/block edit UX, preview, diff, approval |
| Research/multimodal | PresentAgent-2 | PPTAgent | query -> research -> grounded deck, Q&A future |
| CLI/local | slide-deck-ai | Presenton | simple command path, provider abstraction, Ollama |

## What To Absorb By Project

### Presenton

Absorb:

- self-hosted runtime;
- `generate/review/export` API shape;
- MCP tools: `slides.generate`, `slides.review`, `slides.export`;
- provider registry with BYOK, Ollama, OpenAI-compatible models;
- provider capability routing across text, image, vision, research, local model, and fallback needs;
- source-of-truth policy: live tool/deck state beats stale memory;
- schema validation before saving or claiming slide updates;
- automatic retry/shortening for schema length failures;
- model-pull/download state for local Ollama-style workflows;
- workspace per deck run;
- template upload/import idea.

Use when:

- user asks for local/private operation;
- user asks to turn skill into product/API/MCP;
- user asks for automations or batch generation.

Do not absorb:

- full UI before core contracts;
- rigid dependency on one web renderer;
- desktop/cloud packaging before the headless workflow works.

### Gamma

Absorb as UX benchmark, not as implementation:

- low-friction creation flow;
- import from many sources;
- editor + present + share in one loop;
- analytics/distribution expectations;
- reduced design cognitive load for non-designers.

Use when:

- user asks "como ficar à altura do Gamma";
- sharing, analytics, collaboration, or commercial polish matters.

### ppt-master

Absorb:

- native editable PPTX as a first-class requirement;
- template replication/import from existing PPTX;
- lightweight PPTX template manifest extraction: slide size, theme fonts/colors, backgrounds, assets, placeholders, text samples, and page type;
- constrained visual/native IR before export;
- render-lock anti-drift pattern: execution contract separate from design rationale;
- Primary + Modifier visual composition grammar for image-heavy slides;
- runners-up audit trail for chart/template decisions;
- editability QA report;
- AI image type routing as a layer separate from slide layout: background, hero, portrait, typography, infographic, flowchart, framework, matrix, cycle, funnel, pyramid, comparison, timeline, map, scene;
- live preview/annotation pattern for later editor UX;
- narration/animation only as future layer.

Use when:

- output must be PowerPoint-editable;
- client will modify slides;
- template fidelity matters;
- B2B delivery quality matters.

Hard rule:

- never let the LLM generate PPTX directly. Generate a valid spec/IR and let a renderer convert it.

### PPTAgent

Absorb:

- explicit planner before generation;
- research/design specialist mental split;
- reflection history;
- critique pass and revision pass;
- PPTEval-like dimensions: content, design, coherence.
- manuscript-first `Planner -> Research -> PPTAgent` flow for research-heavy decks;
- rendered slide evaluation from images, not only text specs;
- structured document extraction with headings, metadata, image captions, and table captions;
- HTML-to-PPTX conversion rules for placeholders, locked slide size, overflow, and rasterized complex CSS.
- non-default induced template packs (`beamer`, `cip`, `hit`, `thu`, `ucas`) and media-area statistics.
- slide layout constraints: suggested characters, variable-length layout mappings, local media validation, and rewrite of overlong text.
- speaker notes preservation during PPTX reconstruction.

Use when:

- deck quality matters more than speed;
- user asks to improve a weak deck;
- slide-by-slide reasoning and critique are needed.

Required artifact:

```json
{"phase":"design","slide":"s05","issue":"chart too dense","decision":"split into two slides","delta_expected":"readability + design"}
```

### presentation-ai

Absorb:

- outline-first review;
- theme picker and reusable themes;
- editor/present/share loop;
- local model support with Ollama/LM Studio;
- public sharing as later product layer.
- serialized template examples inside prompts;
- per-outline template overrides;
- history snapshots for slide/theme/full changes and rate-limited same-slide edits;
- undo/redo semantics with restore guard, future clearing, and merged rapid same-slide changes;
- rich visual DSL covering bullets, columns, process, compare, charts, stats, media, and infographic blocks.
- chart-data editor contracts for label-value, xy, xyz, multi-series, range, waterfall, OHLC, box-plot, hierarchical, flow, funnel, heatmap, histogram, and gauge data.

Use when:

- user wants a daily editing workflow;
- brand/theme iteration matters;
- non-technical users must adjust decks.

### banana-slides

Absorb:

- prompt-to-edit UX;
- slide/block/region targeted edits;
- resumable job lifecycle: task ids, progress events, polling, export policy, and batch job records;
- preview before applying;
- style-reference mental model;
- reverse editable-PPTX extraction from rendered images as an import/rescue capability;
- video only as future direction.

License caution:

- treat as black-box inspiration because AGPL can be incompatible with private product use. Do not copy code or structure verbatim without legal decision.

Prompt-to-edit contract:

```yaml
edit_operation:
  target:
    slide_id: "s04"
    region_id: "chart_area"
  intent: "make the chart easier to read"
  before: ""
  after: ""
  qa_required: ["visual", "readability"]
  approval: "pending"
```

### powerpoint-skill

Absorb:

- OMML/math native output;
- Mermaid, Graphviz, TikZ, and diagram engines;
- five-layer diagram routing: Graphviz for architecture/flow/dependencies, Mermaid for sequence/gantt/state/ER, TikZ for math/geometric figures, native shapes for annotations, and PDF extraction for sourced paper figures;
- deterministic technical QA;
- strict text-fit, math, diagram, figure, overlap, clipping, and rendered-density rules;
- fallback rules for unsupported renderer capabilities;
- distinction between PowerPoint vs LibreOffice validation limits.

Use when:

- deck is academic, technical, scientific, financial, engineering, or diagram-heavy.

### slide-deck-ai

Absorb:

- minimal CLI smoke-test path;
- provider abstraction via LiteLLM-like interface;
- offline/Ollama smoke tests;
- simple Python/PPTX baseline only for prototypes.

Use when:

- the user asks for a quick local baseline;
- CI/smoke test matters more than design quality.

### PresentAgent-2

Absorb:

- query -> research -> source document -> refined document -> deck;
- research grounding before slides;
- separate retrieval routes for HTML source pages, direct motion media, scholar/benchmark evidence, and local uploaded files;
- source usefulness checks before adding material to the manuscript;
- media usefulness checks before using video/GIF/demo assets;
- slide-level evidence ledger for claims, source confidence, freshness, and use in visible copy or speaker notes;
- multimodal preservation as future product layer;
- interactive Q&A grounded in deck sources as future layer.

Use when:

- source material is a broad question;
- deck needs research before narrative;
- user asks for video/narrated/interactive presentation.

### deepH

Absorb:

- typed handoffs between stages;
- traceable runtime flows;
- multiverse review + synthesis for high-stakes critique;
- focused working set principle: pass only the useful context to each stage;
- validation before claiming completion;
- regression fixtures that turn known process failures into named forward tests.

Use when:

- the slide process itself must be shareable, repeatable, and auditable;
- multiple evaluators or perspectives are useful before final synthesis;
- user asks why a process failed and how to prevent recurrence.

## Capability Selection Matrix

| User asks for | Use pattern from | Required artifact |
|---|---|---|
| "Gere slides localmente" | Presenton + slide-deck-ai | provider registry + workspace |
| "Quero API/MCP" | Presenton | API/MCP contract |
| "Quero BYOK/local/Ollama" | Presenton + presentation-ai | provider routing report |
| "Preciso PPTX editável" | ppt-master | native IR + editability report |
| "Preciso validar PPTX" | powerpoint-skill | pptx technical gate + placeholder check |
| "Use meu template PowerPoint" | ppt-master + Presenton | template import report |
| "Extraia padrões desse PPTX" | ppt-master | template manifest + summary + assets |
| "Melhore esse deck ruim" | PPTAgent | planning-reflection + critique report |
| "Edite esse slide por prompt" | banana-slides + presentation-ai | edit operation diff |
| "Quero histórico/diff de edição" | Presenton + presentation-ai | edit history + scoped diff |
| "Crie apresentação financeira" | powerpoint-skill + ppt-master | charts/tables/native editability |
| "Use fórmula/diagrama" | powerpoint-skill | diagram source + technical QA |
| "Renderize arquitetura/sequence/math" | powerpoint-skill | diagram manifest + engine-specific source |
| "Crie imagem com IA" | ppt-master image templates | image resource list + text policy |
| "Valide dados de gráfico" | presentation-ai chart editor | chart dataset + validation report |
| "Pesquise e gere deck" | PresentAgent-2 + PPTAgent | source ledger + refined doc |
| "Preciso de pesquisa profunda" | PresentAgent-2 DeepResearch | source route report + manuscript |
| "Quero vídeo/demo no slide" | PresentAgent-2 media route | playable media ledger |
| "Importe documento longo" | PPTAgent document extractor | document tree + claim/evidence inventory |
| "Use esse template existente" | PPTAgent induced packs | pack selection + media area policy |
| "Evite drift visual em deck grande" | ppt-master spec_lock | render-lock.yaml |
| "Explique por que escolheu esse template" | ppt-master + PPTAgent | template-selection-report.yaml |
| "Preciso retomar/ver progresso" | banana-slides | job-state.yaml |
| "Fontes antigas conflitarem com estado atual" | Presenton | source-of-truth-policy.yaml |
| "Preserve minhas notas do apresentador" | PresentAgent-2 | speaker-notes preservation gate |
| "Esse claim precisa ser confiável" | PresentAgent-2 + PPTAgent | evidence ledger |
| "Renderizei e ficou ruim" | PPTAgent PPTEval + powerpoint-skill | rendered-eval report |
| "HTML para PPTX/PDF" | PPTAgent html2pptx + Presenton export | render/export task + overflow report |
| "Torne o processo repetível" | deepH | trace + typed handoff contract |
| "Não repetir o erro anterior" | deepH + PPTEval + powerpoint-skill | regression fixture report |
| "Compartilhe por link" | Gamma + presentation-ai | publication/permissions artifact |
| "Quero analytics" | Gamma benchmark + PostHog/Umami/Plausible pattern | analytics event map |

## Artifact Contracts To Prefer

### Workspace

```text
outputs/slide-creator/{deck_id}/
  inputs/
  briefing-normalized.yaml
  story-arc.yaml
  slide-function-map.yaml
  design-direction.yaml
  deck-spec.yaml
  planning-reflection.jsonl
  qa-report.yaml
  exports/
```

### Native IR

Use when PPTX editability matters:

```yaml
native_slide_ir:
  schema: "native-slide-ir.v1"
  canvas:
    width_pt: 960
    height_pt: 540
    ratio: "16:9"
  slides:
    - id: "s01"
      elements:
        - id: "headline"
          type: "text_box"
          role: "action_title"
          content: ""
          fit: "shrink_to_bounds"
          raster_allowed: false
```

### Editability Report

```yaml
editability_report:
  overall_editability_score: 0.0
  slides:
    - slide_id: "s01"
      native_objects: 0
      raster_objects: 0
      editable_text_boxes: 0
      unsupported_features: []
```

### Publication

Use only when the user needs web/share:

```yaml
deck_publication:
  visibility: "private | public | restricted"
  permissions: []
  analytics_events:
    - "deck_opened"
    - "slide_viewed"
    - "cta_clicked"
```

## Priority Rules

1. Narrative/design quality gates first for this skill.
2. If user requires B2B delivery, add ppt-master-style native PPTX/editability.
3. If user requires productization, add Presenton-style API/MCP/provider/workspace.
4. If user requires daily editing, add presentation-ai/banana prompt-to-edit contracts.
5. If user requires technical/academic slides, add powerpoint-skill math/diagram rules.
6. If user starts from a question, add PresentAgent-2 research grounding before slides.

## Do Not Copy

- AGPL code or uniquely structured implementation from banana-slides without legal review.
- Full product UI before artifact contracts are stable.
- Screenshot-only PPTX as a final B2B answer.
- Direct PPTX generation by the LLM.
- SaaS-only assumptions when user asks for privacy/local-first.


## Referência: references/source/references/design-system.md

# Design System

Use this reference before drafting visible slide content or when improving a weak deck.

## Design Direction Template

```yaml
design_direction:
  visual_thesis: ""
  audience_feel: ""
  format: "16:9"
  grid: ""
  type_scale:
    title: ""
    body: ""
    label: ""
  palette:
    background: ""
    text: ""
    accent: ""
    support: []
  motifs:
    - ""
  layout_rules:
    - ""
  density_limits:
    default_visible_words: 45
    max_blocks_per_slide: 4
  anti_patterns:
    - ""
```

## Editorial Design Principles

1. Start with hierarchy, not decoration.
2. Make the audience see the claim before reading details.
3. Use whitespace as structure.
4. Keep repeated components consistent, but vary composition by narrative function.
5. Treat charts, diagrams, matrices, demos, and screenshots as primary evidence, not ornaments.
6. Never use brand colors as superficial skin when the composition is weak.

## Layout Patterns

For full template selection, use `slide-structure-library.md`. The table below is only a compact starter set.

| Pattern | Use For | Avoid When |
|---|---|---|
| Big claim + proof artifact | Hook, proof, decision | Claim is vague |
| Split contrast | Before/after, old/new | More than 2 comparison axes |
| Mechanism diagram | Process, system, model | Steps are not causal |
| Evidence wall | Case proof, testimonials, logos | Sources are weak |
| Matrix | Prioritization, positioning | Axes are unclear |
| Timeline | Phases, rollout | No sequence or dates |
| Scorecard | Evaluation, benchmark | Too many metrics |
| Demo frame | Product/process walkthrough | Screenshot is unreadable |
| CTA panel | Offer, next step | CTA is not specific |

## Density Rules

- Default: <=45 visible words per slide.
- Title: <=16 words.
- Body blocks: <=4.
- Bullets per block: <=3.
- No paragraph should exceed 2 lines.
- Speaker notes can hold nuance; slide surface carries the argument.

## Layout Variety Rule

No more than 2 consecutive slides with the same layout pattern unless the repetition is intentionally used as a sequence, such as `three objections` or `three proof cases`.

## Typography Rules

- Use a clear type hierarchy: title, subhead, body, label, metadata.
- Do not use tiny explanatory text as a crutch.
- Do not rely on all caps for long content.
- If a slide needs text smaller than 18px in 16:9, it is too dense for presentation.

## Visual Quality Checks

Ask:

1. Can the audience identify the main claim in 3 seconds?
2. Does the layout express the slide function?
3. Does the visual system create memory, not just decoration?
4. Is any element present only because the slide looked empty?
5. Would the slide still work in a live room from the back row?


## Referência: references/source/references/narrative-patterns.md

# Narrative Patterns

Use this reference when creating a persuasive, educational, strategic, sales, webinar, pitch, or board deck.

## Core Principle

An outline organizes information. A presentation changes belief. Convert source material into audience movement before writing slides.

## Belief Shift Template

```yaml
audience_belief_shift:
  audience: ""
  current_belief: ""
  desired_belief: ""
  resistance: ""
  proof_needed:
    - ""
  final_action: ""
```

## Deck Type Patterns

### Sales / Webinar

Use when the goal is demand creation, offer presentation, or conversion.

Arc:

1. Hook: name the expensive misconception.
2. Reframe: show why the old path is failing.
3. Stakes: quantify cost of inaction.
4. Mechanism: reveal the new operating model.
5. Proof: demo, case, artifact, before/after, data.
6. Path: show implementation steps.
7. Offer/CTA: make the next action obvious.

Recommended length: 12-16 slides for a focused webinar, 8-12 for a short sales deck.

### Executive / Board

Arc:

1. Executive answer first.
2. Context and decision required.
3. Performance facts.
4. Drivers.
5. Options.
6. Recommendation.
7. Risks and asks.

Use action titles with consequence and decision language.

### Teaching / Course

Arc:

1. Learning promise.
2. Mental model.
3. Worked example.
4. Practice or application.
5. Common mistakes.
6. Checklist.
7. Next action.

Favor clarity and retention over persuasion.

### Product / Strategy Pitch

Arc:

1. Market or user tension.
2. Existing alternatives fail.
3. Product thesis.
4. Mechanism or workflow.
5. Evidence.
6. Business model or rollout.
7. Ask.

## Slide Functions

Every slide must declare exactly one primary function:

| Function | Purpose |
|---|---|
| `hook` | Capture attention with a high-signal claim |
| `reframe` | Replace the audience's old model |
| `diagnosis` | Explain why the current problem persists |
| `stakes` | Quantify cost, upside, urgency, or risk |
| `contrast` | Compare old vs new, before vs after, option A vs B |
| `mechanism` | Explain how the proposed system works |
| `proof` | Make a claim credible through evidence |
| `demo_setup` | Prepare audience to understand a live or visual demo |
| `artifact_reveal` | Show the concrete asset, workflow, map, or system |
| `objection_handling` | Address likely resistance |
| `decision` | Force a choice or recommendation |
| `cta` | Drive the next action |
| `appendix` | Support detail, not core narrative |

Avoid `explain_topic` as a function. If a slide only explains a topic, merge, rewrite, or move to appendix.

## Action Title Rules

An action title must make a claim. Good titles include:

- what changed;
- why it matters;
- who is affected;
- magnitude, timing, or implication when available.

Weak: `Market Overview`

Strong: `AI service demand is rising, but buyers still reject vague automation pitches`

## Compression Rules

- One source section does not equal one slide.
- Merge consecutive slides with the same function.
- Move detail-heavy explanation to speaker notes or appendix.
- Prefer one strong artifact over five generic bullets.
- If a deck exceeds 18 slides, justify why the audience needs that many moments.


## Referência: references/source/references/output-contracts.md

# Output Contracts

Use these contracts when the user asks for a complete deck package, machine-readable outputs, or reusable artifacts.

## Full Package Structure

```text
slide-creator-output/
  briefing-normalized.yaml
  audience-belief-shift.yaml
  story-arc.yaml
  slide-function-map.yaml
  roteiro-template-selection.yaml
  slide-structure-selection.yaml
  visual-template-selection.yaml
  template-selection-report.yaml
  theme-profile-selection.yaml
  render-lock.yaml
  runtime-job-selection.yaml
  job-state.yaml
  source-of-truth-policy.yaml
  research-route-selection.yaml
  import-pipeline-selection.yaml
  template-import-report.yaml
  rendered-eval-selection.yaml
  bench-capability-selection.yaml
  design-direction.yaml
  deck-spec.yaml
  chart-datasets/
  diagrams/
  diagram-manifest.yaml
  image-resource-list.yaml
  source-ledger.yaml
  planning-reflection.jsonl
  key-slide-gate.yaml
  speaker-notes.md
  qa-report.yaml
  rendered-eval.yaml
  package-validation-report.json
  editability-report.yaml
  revision-notes.md
  forward-test.yaml
```

If writing files, place them in a user-specified directory. If no directory is specified in this repository, use `outputs/slide-creator/{deck-slug}/`.

When writing machine-readable files, prefer YAML for core deck artifacts and JSON for validation reports. Before final delivery, run:

```bash
python scripts/build_evidence_ledger.py slide-creator-output/deck-spec.yaml --output slide-creator-output/source-ledger.yaml
python scripts/run_regression_fixtures.py slide-creator-output --json > slide-creator-output/regression-fixture-report.json
python scripts/validate_rendered_eval.py slide-creator-output/rendered-eval.yaml --package-root slide-creator-output --json > slide-creator-output/rendered-eval.validation.json
python scripts/validate_runtime_contracts.py slide-creator-output --json > slide-creator-output/runtime-contracts.validation.json
python scripts/validate_deck_package.py slide-creator-output --json > slide-creator-output/package-validation-report.json
```

`validate_deck_package.py` uses `--profile full` by default. Use `--profile minimal` only for smoke tests or partial drafts that are not being delivered as a complete skill package.

Use paths relative to the skill folder when running bundled scripts directly, or pass absolute paths when running from another working directory.

## Briefing Normalized

```yaml
briefing_normalized:
  title: ""
  deck_type: "sales | webinar | board | pitch | course | workshop | report | other"
  audience: ""
  objective: ""
  desired_action: ""
  duration_minutes: null
  slide_count_target: null
  tone: ""
  source_material:
    - ""
  constraints:
    - ""
  unknowns:
    - ""
```

## Story Arc

```yaml
story_arc:
  deck_id: ""
  arc_type: "educational_workshop | executive_pitch | sales_narrative | thought_leadership | product_demo | board_update | case_study | webinar | financial_update | strategy_memo"
  governing_thought: ""
  audience_belief_shift:
    from: ""
    to: ""
  beats:
    - beat_id: "b01"
      beat_type: "hook | tension | reframe | proof | mechanism | demo_payoff | artifact_reveal | cta"
      narrative_function: ""
      slides_estimated: 1
      source_topics: []
      evidence_refs: []
      design_hints: []
```

Story arc must include opening/tension, reframe/thesis, proof/mechanism/payoff, and close/CTA. Keep beats at 8 or fewer.

## Slide Function Map

```yaml
slide_function_map:
  deck_id: ""
  story_arc_ref: "story-arc.yaml"
  entries:
    - slide_id: "s01"
      beat_ref: "b01"
      function: "cover | reframe | proof | contrast | mechanism_step | demo_setup | demo_payoff | artifact_reveal | objection_neutralize | synthesis | tension_amplify | emotional_anchor | quiet_pause | cta_concrete | close | appendix"
      audience_movement: ""
      slide_type: ""
      density_target: "low | medium | high"
      merged_from_topics: []
      could_be_cut_if: ""
      action_title_draft: ""
      proof_requirement: ""
```

`audience_movement` must state a belief, question, confidence, or decision shift. Do not use topic verbs such as "explicar", "apresentar", "mostrar", "listar", "explain", "present", or "show".

## Design Direction

```yaml
design_direction:
  deck_id: ""
  visual_reference:
    type: "provided_brand | provided_screenshot | imported_pptx | existing_design_system | bundled_theme | design_philosophy_fallback"
    rationale: ""
    paths: []
    must_follow: []
    must_avoid: []
  dominant_motif: ""
  density_limits:
    max_governing_claims_per_slide: 1
    max_supporting_claims_per_slide: 3
    max_visible_words_default: 45
    max_visual_elements: 5
    forbidden_patterns:
      - dense_bullet_wall
      - repeated_two_column_monotony
      - identity_as_skin
  variation_rules:
    layout_count_min: 5
    layout_repetition_max: 2
    quiet_slide_ratio_min: 0.15
    accent_color_density: "sparse"
    motion_policy: "none unless output is web/native motion"
  composition_rules:
    grid_columns: 12
    baseline_padding_pt: 32
    title_anchor: "top_left_or_deliberately_centered"
    footer_policy: ""
    slide_number_policy: ""
    safe_area_pct: 6
  audience_context:
    audience: ""
    viewing_context: ""
    expected_reading_mode: ""
```

Design direction is a blocker-level artifact. It must be written before deck copy so the design system controls content density, layout variation, and visual rhythm.

## Roteiro Template Selection

```yaml
roteiro_template_selection:
  primary_template: ""
  secondary_template: ""
  reason: ""
  modules_added:
    - ""
  modules_removed:
    - ""
  target_slide_count: 0
```

## Slide Structure Selection

Every slide must declare one structure from `references/slide-structure-library.md`.

```yaml
slide_structure_selection:
  slides:
    - slide: 1
      function: ""
      structure_id: "H01"
      structure_name: "Big claim hero"
      why_this_structure: ""
      avoid_risk: ""
```

## Template Selection Report

Use this for every full deck and every key slide. A template choice is incomplete until rejected alternatives are documented.

```yaml
template_selection_report:
  deck_id: ""
  selections:
    - slide_id: "s01"
      slide_function: ""
      selected:
        id: ""
        name: ""
        source_registry: ""
        source_quote: ""
      selected_reason: ""
      rejected_runners_up:
        - id: ""
          name: ""
          rejected_reason: ""
        - id: ""
          name: ""
          rejected_reason: ""
      constraints_checked: [slot_count, text_length, media_area, evidence_visibility, pptx_editability]
      final_confidence: "high | medium | low"
      qa_status: "pass | warn | fail"
```

## Render Lock

Use this as the execution lock before rendering/exporting. It prevents visual drift across long decks.

```yaml
render_lock:
  canvas:
    aspect_ratio: "16:9"
    width_px: 1920
    height_px: 1080
  colors:
    background: ""
    text: ""
    accent: ""
  typography:
    heading_family: ""
    body_family: ""
    body_px: 28
  image_style_lock:
    rendering_family: "editorial_photo | vector_illustration | 3d_isometric | none"
    palette_policy: "native_theme | brand_exact"
    text_policy_default: "native_overlay"
  slide_visual_locks:
    - slide_id: "s01"
      composition_pattern: "C01"
      image_type: ""
      native_overlay_plan: ""
```

## Job State

Use this when work is resumable, batched, exported, or exposed by CLI/API/MCP.

```yaml
job_id: ""
run_id: ""
job_type: "full_generation | source_document_generation | improve_existing_deck | prompt_to_edit | export_only | batch_generation"
status: "queued | running | waiting | completed | failed | cancelled | partial"
inputs: {}
task_records:
  - task_id: ""
    type: ""
    status: ""
progress_events:
  - event: "task_started"
    task_id: ""
artifacts:
  - artifact_id: ""
    kind: "deck_spec"
    path_or_url: ""
    status: "created | verified | failed"
policy:
  continue_on_error: false
  timeout_sec: 1800
final_verdict: "pass | warn | fail | blocked"
```

## Source Of Truth Policy

Use this when multiple sources, previous decks, imported templates, process logs, or memory can conflict.

```yaml
source_of_truth_policy:
  precedence_order:
    - latest_verified_export
    - latest_deck_spec
    - explicit_user_instruction_current_turn
    - source_ledger
    - imported_template_manifest
    - briefing_normalized
    - research_notes
    - prior_chat_or_memory
conflict_resolution: []
```

## Deck Spec

Use this for each slide:

```yaml
slides:
  - number: 1
    function: ""
    structure_id: ""
    structure_name: ""
    action_title: ""
    visible_copy:
      headline: ""
      subhead: ""
      blocks:
        - label: ""
          text: ""
    visual:
      layout_pattern: ""
      primary_asset: ""
      chart_or_diagram: ""
      design_notes: ""
    speaker_notes: ""
    evidence:
      - claim: ""
        source: ""
        status: "sourced | assumption | validate"
        freshness: "unknown"
    qa:
      visible_word_count: 0
      passes_density: true
      has_action_title: true
      has_clear_function: true
```

## Source Ledger

Generate after `deck-spec.yaml` exists.

```yaml
evidence_ledger:
  source: "deck-spec.yaml"
  claim_count: 0
  claims:
    - claim_id: "s01-c1"
      slide_id: "s01"
      claim: ""
      evidence_type: "official_source | benchmark_result | academic_paper | product_documentation | user_provided_document | screenshot_or_media | internal_artifact | explicit_assumption"
      source: ""
      confidence: "high | medium | low"
      visible_or_speaker_notes: "visible | speaker_notes"
      risk: "none | needs_source"
      freshness: "unknown"
  blockers: []
```

## Package Validation Report

Generate before final delivery when files were created.

```json
{
  "package": "slide-creator-output",
  "slide_count": 0,
  "status": "pass",
  "errors": [],
  "warnings": []
}
```

## Key-Slide Gate

Use before full visual production for important decks.

```yaml
key_slide_gate:
  required: true
  slides:
    - role: "cover"
      slide: 1
      pass_condition: "promise is understood in under 5 seconds"
      status: "pass | revise | fail"
    - role: "reframe"
      slide: 2
      pass_condition: "old belief and new belief are visually obvious"
      status: "pass | revise | fail"
    - role: "mechanism"
      slide: 0
      pass_condition: "method is memorable without long explanation"
      status: "pass | revise | fail"
    - role: "proof_or_demo"
      slide: 0
      pass_condition: "audience can see proof or expected artifact"
      status: "pass | revise | fail"
    - role: "cta"
      slide: 0
      pass_condition: "next action is concrete and low-friction"
      status: "pass | revise | fail"
  blockers:
    - ""
```

## Bench Capability Selection

Use when the user asks for runtime, export, editor, API, MCP, prompt-to-edit, research, or local operation.

```yaml
bench_capability_selection:
  capabilities:
    - capability: "native_editable_pptx"
      source_pattern: "ppt-master"
      reason: ""
      artifacts_required:
        - "native-slide-ir.yaml"
        - "editability-report.yaml"
    - capability: "api_mcp_runtime"
      source_pattern: "Presenton"
      reason: ""
      artifacts_required:
        - "workspace"
        - "provider-registry"
```

## Template Import Report

Use when a concrete PPTX/template deck is imported.

```yaml
template_import_report:
  source_file: ""
  status: "pass | partial | fail"
  manifest_file: "manifest.json"
  summary_file: "summary.md"
  asset_dir: "assets"
  slide_size: ""
  theme_fonts_detected: []
  theme_colors_detected: []
  reusable_layouts: 0
  reusable_assets: 0
  partial_layouts: []
  unsupported_features: []
  fidelity_checks:
    rendered_reference_compared: false
    notes: []
```

## Chart Dataset

Use for every chart before visual styling or export.

```yaml
chart_dataset:
  id: "chart-s01-01"
  slide_id: "s01"
  mode: "label-value | xy | xyz | multi-series | range | waterfall | ohlc | box-plot | hierarchical | flow | funnel | heatmap | histogram | gauge"
  title: ""
  source: ""
  unit: ""
  rows:
    - label: ""
      value: 0
  validation_report: "chart-s01-01.validation.json"
```

Validate with:

```bash
python scripts/validate_chart_data.py slide-creator-output/chart-datasets/chart-s01-01.yaml --json > slide-creator-output/chart-datasets/chart-s01-01.validation.json
```

## Diagram Manifest

Use for architecture, sequence, mathematical, or sourced figure diagrams.

```yaml
diagram_manifest:
  output_dir: "diagrams"
  diagrams:
    - diagram_id: "d01"
      slide_id: "s01"
      engine: "graphviz | mermaid | tikz | native_shapes | pdf_figure_extraction"
      source_file: ""
      output_file: ""
      editable_level: "native | source_editable | raster_only"
      attributed: false
      qa:
        rendered: false
        fits_container: false
        legible_at_thumbnail: false
        issues: []
  blockers: []
```

## Image Resource List

Use when AI/stock/generated visuals are part of the deck.

```yaml
image_resource_list:
  images:
    - image_id: "img-s01-01"
      slide_id: "s01"
      image_type: "hero | background | portrait | typography | infographic | flowchart | framework | matrix | cycle | funnel | pyramid | comparison | timeline | map | scene"
      role: "decorative | explanatory | evidentiary | product_representational"
      container: "hero_large | evidence_panel | icon_or_support | full_canvas"
      text_policy: "none | embedded"
      prompt: ""
      output_file: ""
      qa:
        no_critical_embedded_text: true
        fits_container: false
        source_or_generation_model: ""
```

## Forward Test

Use when improving a known weak deck/process.

```yaml
forward_test:
  case_id: ""
  source_inputs:
    - ""
  old_failure_modes:
    - failure: ""
      evidence: ""
      blocked_by_gate: ""
  expected_outputs:
    - "briefing-normalized"
    - "story-arc"
    - "slide-function-map"
    - "slide-structure-selection"
    - "design-direction"
    - "deck-spec"
    - "key-slide-gate"
    - "qa-report"
  pass_thresholds:
    weighted_score_minimum: 90
  current_gap: ""
```

## Planning Reflection

```jsonl
{"phase":"narrative","slide":"s03","issue":"action title is generic","decision":"rewrite as claim","expected_delta":"narrative"}
{"phase":"design","slide":"s05","issue":"layout repeats previous two slides","decision":"switch to mechanism diagram","expected_delta":"editorial_design"}
```

## Editability Report

Use when PPTX is required.

```yaml
editability_report:
  overall_editability_score: 0.0
  native_object_count: 0
  raster_object_count: 0
  editable_text_count: 0
  killer_items:
    - ""
```

## Final Answer Format

For a full deck in chat, use:

```markdown
## Deck Thesis

...

## Design Direction

...

## Slide Plan

| # | Function | Action Title | Visual |
|---:|---|---|---|

## Deck Spec

### Slide 1
...

## QA

...
```


## Referência: references/source/references/regression-test-protocol.md

# Regression Test Protocol

Use this reference when improving an existing deck process, testing the skill, or preventing a known failure from recurring.

## Purpose

A regression test converts a bad slide creation process into a reusable quality gate. It answers:

1. What went wrong?
2. What should the skill produce instead?
3. What artifacts prove the process is now better?
4. What must block rendering or delivery?

## When To Use

Use this protocol when:

- the user says a deck “ficou ruim”;
- there is a process log, bad output, or postmortem;
- the skill is being hardened;
- a benchmark has identified best practices that must become gates;
- a deck is important enough that repeating the same error is unacceptable.

## Required Regression Artifact

```yaml
regression_test:
  case_id: ""
  source_inputs:
    - ""
  old_failure_modes:
    - failure: ""
      evidence: ""
      blocked_by_gate: ""
  expected_skill_outputs:
    - "briefing-normalized"
    - "audience-belief-shift"
    - "roteiro-template-selection"
    - "slide-function-map"
    - "slide-structure-selection"
    - "design-direction"
    - "deck-spec"
    - "qa-report"
  key_slide_gate:
    required: true
    slides:
      - "cover"
      - "reframe"
      - "mechanism"
      - "proof/demo"
      - "cta"
  pass_threshold:
    weighted_score: 90
  render_blockers:
    - ""
```

## Hard Gates

- Do not render a full deck before the key-slide gate is defined.
- Do not deliver visual slides without a QA report.
- Do not accept a deck spec where slides lack function, action title, and structure ID.
- Do not treat brand tokens as design quality.
- Do not use an outline as slide sequence unless the roteiro template supports it.

## Forward-Test Output

For a real case, produce:

1. `forward-test.md`: human-readable diagnosis and expected behavior.
2. `forward-test.yaml`: machine-readable gates and thresholds.
3. `revision-notes.md`: what changed in the skill or process.

## Scoring

A regression passes only if:

- the old failure modes are explicitly mapped to new gates;
- the new output has a stronger slide-function map than the old outline;
- key slides are identified before full production;
- QA thresholds are higher than the previous output;
- remaining gaps are named instead of hidden.


## Referência: references/source/references/roteiro-template-library.md

# Roteiro Template Library

Use this reference before building the slide-function map. Select one primary roteiro and optionally borrow modules from one secondary roteiro. Do not invent a sequence from scratch when a template fits.

## Selection Rule

Choose by audience job:

- Need money/approval: financial, board, investment, budget, strategy decision.
- Need belief change: webinar, sales, pitch, category design, transformation.
- Need learning: course, workshop, training, playbook.
- Need adoption: product demo, onboarding, enablement, change management.
- Need trust: case study, research report, audit, postmortem.

## Roteiro Templates

### 1. Webinar de venda educacional

Use for 45-120 minute live sales/education sessions.

1. Promise and enemy belief.
2. Reframe.
3. Stakes and cost of current path.
4. Proof that the new path works.
5. Mechanism.
6. Criteria/checklist.
7. Demonstration or worked example.
8. Result artifact.
9. Why execution fails alone.
10. Offer bridge.
11. Who it is for/not for.
12. CTA and urgency.
13. Q&A holding slide.

### 2. Apresentação financeira executiva

Use for CFO, board, investor, or leadership financial updates.

1. Executive answer.
2. KPI snapshot.
3. Revenue bridge.
4. Margin bridge.
5. Cash/runway/liquidity.
6. Variance vs plan.
7. Drivers and sensitivities.
8. Risks.
9. Options.
10. Recommendation.
11. Decision required.
12. Appendix.

### 3. Board update

1. One-page board memo.
2. Decision asks.
3. Performance snapshot.
4. Strategic progress.
5. Key risks.
6. Talent/org.
7. Financials.
8. Product/customer.
9. Options and tradeoffs.
10. Next-quarter commitments.

### 4. Investor pitch

1. Category tension.
2. Problem.
3. Why now.
4. Solution.
5. Product/demo.
6. Market.
7. Business model.
8. Traction.
9. Go-to-market.
10. Moat.
11. Team.
12. Financial plan.
13. Ask.

### 5. Sales deck B2B

1. Buyer pain.
2. Cost of status quo.
3. Desired outcome.
4. New mechanism.
5. Product/service fit.
6. Proof.
7. Implementation path.
8. Risk reversal.
9. Commercial model.
10. Next step.

### 6. Product demo narrative

1. User context.
2. Painful current workflow.
3. Demo promise.
4. Setup and data.
5. Step 1 moment.
6. Step 2 moment.
7. Step 3 moment.
8. Output/result.
9. Before/after.
10. Adoption path.
11. CTA.

### 7. Strategy recommendation

1. Recommendation headline.
2. Context.
3. Strategic question.
4. Criteria.
5. Option A.
6. Option B.
7. Option C.
8. Comparative matrix.
9. Risks.
10. Recommended path.
11. Implementation roadmap.
12. Decision ask.

### 8. Market research report

1. Research question.
2. Executive findings.
3. Market map.
4. Segment sizing.
5. Customer insight.
6. Competitive landscape.
7. Trend drivers.
8. Implications.
9. Opportunities.
10. Recommended actions.
11. Methodology.
12. Appendix.

### 9. Case study

1. Client/context.
2. Before state.
3. Constraint.
4. Intervention.
5. Mechanism.
6. Implementation timeline.
7. Results.
8. Proof artifacts.
9. Lessons.
10. Replication path.
11. CTA.

### 10. Training / course module

1. Learning promise.
2. Mental model.
3. Vocabulary.
4. Example.
5. Step-by-step method.
6. Practice.
7. Common mistakes.
8. Checklist.
9. Assessment.
10. Next module.

### 11. Workshop facilitation deck

1. Outcome of the session.
2. Rules and roles.
3. Context primer.
4. Exercise 1 prompt.
5. Share-out.
6. Synthesis frame.
7. Exercise 2 prompt.
8. Prioritization.
9. Decision.
10. Owner/action plan.
11. Close.

### 12. Change management / transformation

1. Why change.
2. What stays true.
3. What changes.
4. Impact by persona.
5. New operating model.
6. Migration path.
7. Enablement plan.
8. Risks and support.
9. Success metrics.
10. Next actions.

### 13. Product launch

1. Launch thesis.
2. Market/user pain.
3. Product promise.
4. Hero feature.
5. Use cases.
6. Proof/beta.
7. Positioning.
8. GTM plan.
9. Launch timeline.
10. Metrics.
11. Ask.

### 14. Internal operating review

1. Scorecard.
2. What changed.
3. What worked.
4. What broke.
5. Root causes.
6. Decisions.
7. Owner map.
8. Next cycle.

### 15. Postmortem

1. Incident summary.
2. Timeline.
3. Impact.
4. Root cause.
5. Contributing factors.
6. What worked.
7. What failed.
8. Remediation.
9. Prevention.
10. Accountability.

### 16. Audit / diagnostic

1. Diagnostic thesis.
2. Scope.
3. Rubric.
4. Score summary.
5. Gap cluster 1.
6. Gap cluster 2.
7. Gap cluster 3.
8. Risk map.
9. Quick wins.
10. Roadmap.
11. Decision ask.

### 17. Fundraising update

1. Company one-liner.
2. Progress since last update.
3. Traction.
4. Product velocity.
5. Pipeline.
6. Financial runway.
7. Round plan.
8. Use of funds.
9. Investor ask.

### 18. Proposal / SOW

1. Client situation.
2. Desired outcome.
3. Diagnosis.
4. Proposed approach.
5. Workstreams.
6. Timeline.
7. Deliverables.
8. Investment.
9. Governance.
10. Next step.

### 19. Thought leadership keynote

1. Provocation.
2. Cultural/business shift.
3. Old model fails.
4. New model.
5. Stories/examples.
6. Framework.
7. Implications.
8. Call to action.

### 20. Benchmark / competitive analysis

1. Decision question.
2. Players.
3. Method.
4. Segment comparison.
5. Capability matrix.
6. Evidence.
7. Gap analysis.
8. Risks.
9. Recommendation.
10. Roadmap.

### 21. Founder-led sales webinar

Use when the founder is the main persuasion asset and the deck must combine worldview, proof, offer, and personal authority.

1. Founder provocation.
2. Personal observation from the field.
3. Enemy belief.
4. Cost of staying average.
5. New category/mechanism.
6. Founder story or case.
7. Proof stack.
8. Method walkthrough.
9. Live application.
10. Why the founder/company can help.
11. Offer bridge.
12. Objection handling.
13. CTA.

### 22. Tactical masterclass

Use when the audience expects concrete execution, templates, examples, and a skill upgrade.

1. Learning promise.
2. Outcome artifact preview.
3. Baseline mistake.
4. Mental model.
5. Step 1.
6. Worked example.
7. Step 2.
8. Worked example.
9. Step 3.
10. Checklist.
11. Practice prompt.
12. Common failure modes.
13. Next action.

### 23. Technical architecture pitch

Use for CTO, engineering, platform, AI, data, or infrastructure proposals.

1. Architecture answer.
2. Current-state constraints.
3. Non-functional requirements.
4. Target architecture.
5. Component map.
6. Data/control flow.
7. Integration points.
8. Security/privacy model.
9. Scalability and failure modes.
10. Migration plan.
11. Build/buy tradeoffs.
12. Decision ask.

### 24. AI agent / automation demo

Use when presenting an agent, automation, workflow, or AI system live.

1. User job.
2. Current workflow pain.
3. Demo promise.
4. Input artifact.
5. Agent/workflow map.
6. Step-by-step run.
7. Intermediate reasoning or checkpoints.
8. Output artifact.
9. Human review point.
10. Before/after workflow.
11. Operational limits.
12. Adoption next step.

### 25. Offer creation workshop

Use when the audience must build an offer during the session.

1. Workshop outcome.
2. Offer quality rubric.
3. Bad offer teardown.
4. Audience input capture.
5. Pain selection.
6. Outcome definition.
7. Mechanism design.
8. Proof/risk reducer.
9. Price/scope frame.
10. Pitch assembly.
11. Peer/self review.
12. CTA or homework.

### 26. Sales call deck / live close

Use when slides support a live commercial conversation, not a lecture.

1. Meeting objective.
2. Buyer situation.
3. Diagnosis recap.
4. Cost of inaction.
5. Desired outcome.
6. Proposed path.
7. Proof relevant to buyer.
8. Scope and responsibilities.
9. Investment and terms.
10. Risk reversal.
11. Decision options.
12. Next step.

### 27. Customer success QBR

Use for quarterly business reviews, account expansion, renewals, and strategic customer updates.

1. Executive summary.
2. Goals agreed.
3. Adoption snapshot.
4. Outcome progress.
5. Usage insights.
6. Wins.
7. Gaps/risks.
8. Expansion opportunities.
9. Next-quarter plan.
10. Asks/decisions.

### 28. Product strategy memo deck

Use when converting a product memo into an executive slide narrative.

1. Product decision.
2. User problem.
3. Strategic context.
4. Options considered.
5. Chosen bet.
6. Why now.
7. Scope boundaries.
8. Success metrics.
9. Risks.
10. Roadmap.
11. Decision ask.

### 29. Design critique / creative review

Use for reviewing designs, brands, decks, landing pages, or creative systems.

1. Review objective.
2. Design intent.
3. Evaluation criteria.
4. What works.
5. What breaks.
6. Pattern diagnosis.
7. Priority fixes.
8. Revised direction.
9. Example application.
10. Decision/request.

### 30. Brand strategy deck

Use for positioning, messaging, identity, naming, category, or brand system decisions.

1. Brand problem.
2. Audience tension.
3. Category context.
4. Positioning thesis.
5. Enemy/alternative.
6. Core promise.
7. Messaging pillars.
8. Visual/verbal principles.
9. Proof and reasons to believe.
10. Activation plan.
11. Decision ask.

### 31. Content strategy / editorial plan

Use for content engines, thought leadership, social channels, GEO/SEO, or editorial calendars.

1. Audience job.
2. Content thesis.
3. Current content gap.
4. Pillar map.
5. Format strategy.
6. Distribution channels.
7. Cadence.
8. Example issue/post/video.
9. Measurement.
10. Operating model.
11. Next sprint.

### 32. Course sales / cohort launch

Use for selling a cohort, bootcamp, mentorship, or education product.

1. Transformation promise.
2. Why the old learning path fails.
3. Student before/after.
4. Mechanism/curriculum.
5. Proof/results.
6. Inside the cohort.
7. Deliverables and support.
8. Who it is for/not for.
9. Time and investment.
10. Bonus/risk reducer.
11. CTA.

### 33. Community / membership pitch

Use for communities, paid memberships, masterminds, or private networks.

1. Belonging tension.
2. Why solo execution fails.
3. Member identity.
4. Community promise.
5. Rituals and cadence.
6. Access and resources.
7. Member proof.
8. Rules/standards.
9. Membership path.
10. CTA.

### 34. Research-to-action briefing

Use when a broad research effort must become executive action.

1. Decision the research informs.
2. Method and source base.
3. Finding 1.
4. Finding 2.
5. Finding 3.
6. Implications.
7. Strategic options.
8. Recommendation.
9. Risks and unknowns.
10. Action plan.

### 35. Regulatory / compliance briefing

Use when legal, privacy, AI governance, security, or compliance is central.

1. Compliance answer.
2. Scope and applicability.
3. Current exposure.
4. Obligations.
5. Risk severity.
6. Control map.
7. Remediation plan.
8. Owner model.
9. Evidence/audit trail.
10. Decision ask.

### 36. Procurement / vendor selection

Use for selecting software, agencies, vendors, platforms, or implementation partners.

1. Decision question.
2. Requirements.
3. Evaluation method.
4. Shortlist.
5. Comparison matrix.
6. Cost/risk analysis.
7. Reference checks.
8. Recommendation.
9. Contract considerations.
10. Implementation plan.

### 37. Investor data room narrative

Use when creating a deck to guide investors through diligence, not just pitch.

1. Investment thesis.
2. Company snapshot.
3. Market evidence.
4. Product evidence.
5. Customer evidence.
6. Revenue quality.
7. Unit economics.
8. Team and operating cadence.
9. Risks and mitigations.
10. Data room map.
11. Ask and process.

### 38. Transformation roadmap

Use for multi-quarter operating model, AI transformation, digital transformation, or org redesign.

1. Transformation thesis.
2. Current maturity.
3. North-star operating model.
4. Workstream map.
5. Phase 1.
6. Phase 2.
7. Phase 3.
8. Capability gaps.
9. Governance.
10. Success metrics.
11. Decision ask.

### 39. Executive one-decision deck

Use when the deck exists to get one specific yes/no/resource decision.

1. Decision required.
2. Recommendation.
3. Why now.
4. Criteria.
5. Evidence.
6. Options rejected.
7. Risk/mitigation.
8. Cost/resources.
9. Next 30 days.
10. Explicit ask.

### 40. Demo day / showcase

Use for presenting multiple projects, prototypes, squads, or experiments.

1. Showcase thesis.
2. Selection criteria.
3. Project 1: problem/result.
4. Project 2: problem/result.
5. Project 3: problem/result.
6. Cross-cutting lessons.
7. What should scale.
8. What should stop.
9. Resource ask.
10. Next cycle.

### 41. Transformation story / before-after keynote

Use when emotion, identity, and momentum matter as much as facts.

1. Before world.
2. Inciting tension.
3. Breaking point.
4. New insight.
5. First proof.
6. New method.
7. Transformation evidence.
8. What this means for the audience.
9. Invitation.

### 42. Data story / analytics narrative

Use when a dashboard, analysis, or dataset must drive a decision.

1. Decision question.
2. Executive finding.
3. Data source and trust.
4. Trend.
5. Driver decomposition.
6. Segment contrast.
7. Exception/outlier.
8. Forecast/scenario.
9. Recommendation.
10. Monitoring plan.

### 43. Crisis / turnaround briefing

Use when the organization needs urgency, trust, and a recovery plan.

1. Situation in one sentence.
2. What changed.
3. Impact.
4. Root causes.
5. Immediate containment.
6. Recovery plan.
7. Owner map.
8. Risks.
9. Communication plan.
10. Decision ask.

### 44. Partnership pitch

Use when proposing strategic partnership, channel, integration, co-selling, or ecosystem motion.

1. Shared market opportunity.
2. Why both sides win.
3. Customer/use-case fit.
4. Partnership model.
5. Joint motion.
6. Economics.
7. Proof or pilot.
8. Risks and boundaries.
9. Next step.

### 45. Personal portfolio / authority deck

Use for founder, consultant, creator, speaker, or expert positioning.

1. Positioning statement.
2. Who you help.
3. Problem you solve.
4. Signature method.
5. Proof and work samples.
6. Point of view.
7. Offers/speaking/topics.
8. Contact/next step.

## Module Swaps

- Add `demo` module after mechanism when trust is low.
- Add `objection` module before CTA when audience is skeptical.
- Add `financial model` module before decision when money approval is needed.
- Add `persona impact` module when change affects multiple roles.
- Add `appendix` only after the core narrative, never as a substitute for clarity.


## Referência: references/source/references/rubrics.md

# Rubrics

Use this reference for QA, critique, scoring, or revision.

## Weighted Score

| Dimension | Weight | Pass |
|---|---:|---:|
| Narrative | 30 | >=85 |
| Editorial design | 25 | >=85 |
| Proof and credibility | 15 | >=80 |
| Didactic clarity | 10 | >=85 |
| CTA/conversion | 10 | >=80 |
| Technical deliverability | 10 | >=80 |

Weighted score:

`sum(dimension_score * weight) / 100`

## Narrative Rubric

Score 0-100:

- Clear belief shift: 20
- Strong governing thought: 15
- Coherent story arc: 20
- MECE structure: 10
- Slide functions move the audience: 20
- Action titles make claims: 15

Failure triggers:

- slide order follows source document order without transformation;
- titles are topic labels;
- multiple slides repeat the same function;
- deck lacks decision, CTA, or audience transformation.

## Editorial Design Rubric

Score 0-100:

- Visual thesis and motif: 15
- Hierarchy and readability: 20
- Density control: 20
- Structure-template fit and layout variety: 15
- Evidence visualization: 15
- Brand depth, not skinning: 15

Failure triggers:

- card wall;
- brand colors applied to weak wireframes;
- unreadable screenshots/charts;
- too many blocks;
- no visual difference between hook, proof, mechanism, and CTA slides.
- slides do not declare structure IDs from the template library.
- important decks skip the key-slide gate before full render.

## Template Fit Rubric

Score 0-100:

- Correct roteiro selected for deck type: 25
- Secondary modules added only when justified: 10
- Every slide declares a structure ID: 20
- Structure fits slide function: 25
- No more than 2 consecutive slides use equivalent structures: 10
- Weak/noisy templates are rejected with rationale: 10

Failure triggers:

- deck sequence is invented despite a matching roteiro template;
- slides use generic cards because no structure was selected;
- structure selection happens after visible copy;
- template is chosen for aesthetics rather than rhetorical job.

## Proof and Credibility Rubric

Score 0-100:

- Claims have evidence or explicit assumption label: 35
- Sources are attributable: 20
- Proof is placed at the right narrative moment: 20
- Examples are specific: 15
- Caveats are visible when needed: 10

## Didactic Clarity Rubric

Score 0-100:

- Concept progression is simple: 25
- Examples support abstraction: 20
- Jargon is controlled: 15
- Speaker notes carry nuance: 15
- Audience can retell the core idea: 25

## CTA / Conversion Rubric

Score 0-100:

- Next action is explicit: 30
- Value of action is clear: 25
- Friction and objection are handled: 20
- CTA timing fits the story: 15
- Follow-up artifact is specified: 10

## Technical Deliverability Rubric

Score 0-100:

- Consistent 16:9 framing: 15
- Export/render target is clear: 10
- Assets are identified: 15
- Accessibility and contrast considered: 20
- Content can be converted to HTML/PPT/Google Slides: 15
- File/package structure is clear: 10
- If PPTX is requested, editability report exists: 15

## Bench Absorption Rubric

Use when the output claims product/runtime capability.

Score 0-100:

- Correct source pattern selected from `bench-absorption-map.md`: 25
- Required artifacts named: 20
- License/risk handled: 15
- QA/reporting contract included: 20
- Scope avoids copying full external product prematurely: 20

## Regression / Forward-Test Rubric

Use when improving a known bad deck or process.

Score 0-100:

- Old failure modes are named with evidence: 20
- Each failure maps to a concrete new gate: 25
- Expected skill outputs are machine-checkable: 20
- Key-slide gate exists before full render: 15
- QA threshold is higher than the previous process: 10
- Remaining gaps are explicit: 10

Failure triggers:

- postmortem stays descriptive and does not become a gate;
- new process can repeat the old bypass;
- visual output is produced before the regression gate;
- success is claimed without thresholds.

## Critique Protocol

Before final answer:

1. Score each dimension.
2. List top 5 issues by severity.
3. Revise the deck spec, not just the wording.
4. Record what changed.
5. If score remains below 85, label as draft and name the blocker.

## QA Report Template

```yaml
qa_report:
  weighted_score: 0
  verdict: "PASS | REVIEW | FAIL"
  scores:
    narrative: 0
    editorial_design: 0
    proof_credibility: 0
    didactic_clarity: 0
    cta_conversion: 0
    technical_deliverability: 0
  killer_issues:
    - ""
  revisions_applied:
    - ""
  residual_risks:
    - ""
```


## Referência: references/source/references/slide-structure-library.md

# Slide Structure Library

Use this reference after the slide-function map and before writing visible copy. Every slide must choose one primary structure template. Use the `Use when` and `Avoid when` rules.

## Hook / Opening

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| H01 | Big claim hero | One provocative thesis must dominate | Claim is not specific |
| H02 | Myth vs truth | Audience holds a wrong belief | There is no clear myth |
| H03 | Cost of inaction | Urgency depends on quantified loss | Cost is speculative |
| H04 | Before/after snapshot | Transformation is visual or measurable | Before/after is weak |
| H05 | One number opener | A metric can carry the hook | Number lacks source |
| H06 | Contrarian question | Opening needs curiosity | Answer is obvious |
| H07 | Enemy statement | Deck has a shared villain/problem | Tone must be neutral |
| H08 | Future-back opening | Audience needs to see end-state first | Future state is vague |
| H09 | Cold open scene | A short scene can place audience inside the problem | Scene is decorative |
| H10 | Founder field note | Founder/subject-matter authority opens with observation | Founder has no credibility in topic |
| H11 | Impossible promise check | A bold promise needs immediate guardrails | Promise cannot be supported |
| H12 | Audience mirror | Audience must recognize themselves quickly | Audience is broad or mixed |
| H13 | Time-box challenge | Session promises a concrete outcome in a fixed time | Outcome is vague |
| H14 | Shock contrast | Extreme contrast creates urgency | Contrast is exaggerated |
| H15 | Artifact preview | Showing final output creates pull | Artifact is unimpressive |
| H16 | Decision-first opener | Executives need the ask upfront | Audience expects inspiration |

## Thesis / Reframe

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| R01 | Old model / new model | Category or strategy is changing | Difference is cosmetic |
| R02 | Tool behind outcome | Need to separate means from value | Audience already agrees |
| R03 | Causal chain | Need to explain why X creates Y | Causality is unproven |
| R04 | Belief ladder | Audience needs staged persuasion | Deck is only informational |
| R05 | Principle stack | A few rules govern the argument | Rules are not memorable |
| R06 | Category map | Positioning requires a new frame | Categories overlap |
| R07 | From-to bridge | Transformation is the core story | From/to states are broad |
| R08 | Strategic equation | A formula clarifies value drivers | Variables are fuzzy |
| R09 | Means vs end | Audience confuses tool/activity with outcome | The distinction is already obvious |
| R10 | Constraint reversal | The accepted blocker is not the true blocker | New blocker is unproven |
| R11 | Value chain shift | Show how value migrates between actors | Chain is too complex |
| R12 | Assumption teardown | A hidden assumption drives bad decisions | Assumption is not widely held |
| R13 | Maturity shift | Audience must move from stage A to B | Maturity stages are arbitrary |
| R14 | Market map reframe | Buyer/category boundaries are misunderstood | Map lacks evidence |
| R15 | Operating principle | One principle changes many decisions | Principle is too generic |
| R16 | Lens swap | Same data looks different through a new lens | Lens is clever but not useful |

## Diagnosis / Problem

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| D01 | Symptom vs root cause | Audience treats symptoms | Root cause is not proven |
| D02 | Friction map | Workflow has many pain points | No process is involved |
| D03 | Bottleneck diagram | One constraint explains failure | Multiple constraints matter equally |
| D04 | Failure loop | Behavior repeats and compounds | Loop is not causal |
| D05 | Waste stack | Need to show accumulated inefficiency | Waste cannot be estimated |
| D06 | Persona pain split | Different roles feel different pain | Persona differences do not matter |
| D07 | Risk heatmap | Need severity/probability | Risk list is immature |
| D08 | Broken funnel | Conversion/drop-off matters | Funnel data is absent |
| D09 | Root-cause tree | Problem has layered causes | Causes are speculative |
| D10 | Constraint stack | Several constraints accumulate | Constraints are not ordered |
| D11 | Cost leak map | Money/time leaks across process | Leaks cannot be estimated |
| D12 | Decision bottleneck | Slow decisions are the problem | No decision process exists |
| D13 | Capability gap | Current capability does not match ambition | Capability target is unclear |
| D14 | Trust gap | Buyer/user skepticism is central | Trust is not the blocker |
| D15 | Process autopsy | A failed process needs dissection | No evidence from the process |
| D16 | Anti-pattern gallery | Multiple recurring mistakes need naming | Mistakes are isolated |

## Evidence / Proof

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| P01 | Number wall | 3-5 proof metrics tell the story | More than 5 metrics |
| P02 | Case card | One customer/story proves a claim | Case is generic |
| P03 | Before/after metric | Improvement is measurable | No baseline exists |
| P04 | Source-backed claim | Credibility is crucial | Source is weak |
| P05 | Screenshot evidence | Product/output artifact matters | Screenshot is unreadable |
| P06 | Testimonial pullquote | Social proof matters | Quote is vague |
| P07 | Benchmark bar | Comparison persuades | Method is unclear |
| P08 | Proof timeline | Progress over time builds trust | Timeline has no milestones |
| P09 | Demo result | Live/recorded demo has output | Demo output is not impressive |
| P10 | Evidence stack | Multiple proof types reinforce | Looks like clutter |
| P11 | Case teardown | A case needs problem -> action -> result | Case lacks details |
| P12 | Before/after artifact | Artifact quality changed visibly | Artifact cannot be shown |
| P13 | Source ledger slice | Research credibility depends on traceability | Too much detail for live flow |
| P14 | Customer quote map | Several quotes support one pattern | Quotes are repetitive |
| P15 | Experiment result | A test/experiment proves direction | Sample is too small |
| P16 | Validation ladder | Proof moves from weak to strong | Audience needs one decisive proof |
| P17 | Credibility bridge | External authority supports claim | Authority is not relevant |
| P18 | Objection-proof pair | Proof directly answers objection | Objection is weak |

## Mechanism / Framework

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| M01 | 3-step process | Method is simple and sequential | More than 5 steps required |
| M02 | 4-block operating model | Need roles/capabilities | Blocks overlap |
| M03 | Flywheel | Momentum/compounding matters | No reinforcing loop |
| M04 | Layer cake | Architecture or maturity levels | Layers are not hierarchical |
| M05 | Pipeline | Work moves through stages | No linear flow |
| M06 | System map | Components interact | Too many nodes |
| M07 | Scorecard | Evaluation criteria matter | Criteria are not independent |
| M08 | Checklist | Audience needs decision criteria | Items are too generic |
| M09 | Decision tree | Path differs by condition | Conditions are unclear |
| M10 | Formula | Simple equation unlocks idea | Formula feels forced |
| M11 | Loop with checkpoints | Process repeats with quality gates | Process is linear |
| M12 | Stack model | Capabilities layer into a system | Layers overlap |
| M13 | Maturity ladder | Audience needs staged progression | Stages imply false hierarchy |
| M14 | Operating cadence | Method depends on repeated rhythm | Cadence is not important |
| M15 | Role choreography | People/agents/functions interact | Roles are not distinct |
| M16 | Input-process-output | Need show transformation from source to artifact | Output is vague |
| M17 | Control panel | Many settings/choices require governance | Too many controls for slide |
| M18 | Flywheel with friction | Momentum and blockers both matter | No compounding motion |

## Comparison / Choice

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| C01 | Two-column contrast | Binary contrast is enough | More than two options |
| C02 | Option matrix | Need compare multiple options | Criteria are not weighted |
| C03 | Tradeoff frontier | Need show impossible triangle | Axes are arbitrary |
| C04 | Good/better/best | Tiers clarify choice | Audience needs exact spec |
| C05 | Build/buy/partner | Strategic sourcing decision | Options are not exhaustive |
| C06 | Now/next/later | Roadmap prioritization | Sequence is not time-based |
| C07 | Winner by dimension | Benchmark or bench deck | Evidence per dimension is weak |
| C08 | Risk/reward map | Portfolio or initiative choice | Risk/reward cannot be scored |
| C09 | Tradeoff table | Decision depends on explicit compromises | Tradeoffs are political, not analytical |
| C10 | Segment split | Different segments need different choices | Segments are not actionable |
| C11 | Status quo vs recommended | Recommendation must beat inertia | Status quo not viable as option |
| C12 | Option scorecard | Multiple options need weighted evaluation | Weights are unjustified |
| C13 | Scenario fork | Future paths diverge | Scenarios are not plausible |
| C14 | Capability frontier | Show what each player can/cannot do | Capabilities are unverified |
| C15 | Decision matrix mini | Small choice needs compact criteria | Too many criteria |
| C16 | Replacement map | Show what new system replaces | Old system is unknown |

## Data / Finance

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| F01 | KPI scorecard | Executive status update | Metrics lack targets |
| F02 | Revenue bridge | Explain revenue movement | Drivers do not sum |
| F03 | Margin bridge | Explain profit movement | Costs not categorized |
| F04 | Waterfall | Need plus/minus reconciliation | Too many small bars |
| F05 | Scenario table | Compare base/upside/downside | Assumptions are missing |
| F06 | Sensitivity matrix | Two variables drive outcome | Audience dislikes modeling |
| F07 | Cohort chart | Retention/adoption over time | Cohorts are too small |
| F08 | Funnel metrics | Conversion path matters | Funnel is not measured |
| F09 | Unit economics card | LTV/CAC/payback matters | Inputs are unreliable |
| F10 | Budget allocation | Show where money goes | Categories overlap |
| F11 | Forecast bridge | Explain path from current to future number | Forecast assumptions absent |
| F12 | Cost-to-serve stack | Profit depends on delivery cost | Costs cannot be allocated |
| F13 | Payback timeline | Investment needs recovery period | Cash timing is irrelevant |
| F14 | Waterline chart | Show threshold for survival/target | Threshold is arbitrary |
| F15 | Driver tree | Metric is driven by multiple levers | Levers are correlated |
| F16 | Variance waterfall | Explain actual vs plan | Variance drivers do not reconcile |
| F17 | Portfolio allocation | Compare investment across bets | Bets have incomparable units |
| F18 | Pricing ladder | Price tiers/anchors need framing | Pricing is not approved |

## Roadmap / Execution

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| E01 | Milestone timeline | Dates matter | Dates are unknown |
| E02 | Workstream swimlane | Parallel teams execute | Too few workstreams |
| E03 | 30/60/90 plan | Early execution clarity | Longer roadmap needed |
| E04 | Now/next/future | Product/strategy phasing | Timing is contractual |
| E05 | Owner action grid | Accountability matters | Owners not known |
| E06 | Dependency map | Sequencing risk matters | Dependencies are simple |
| E07 | Rollout staircase | Gradual adoption | Rollout is big-bang |
| E08 | Operating cadence | Meetings/rituals/governance | Execution is one-off |
| E09 | Critical path | One sequence controls delivery date | Work is exploratory |
| E10 | Risk burn-down | Plan reduces risk over time | Risks are static |
| E11 | Resource ramp | Team/capacity changes over time | Headcount not part of decision |
| E12 | Governance loop | Decisions/feedback recur | Governance would be overkill |
| E13 | Milestone proof | Each phase must produce evidence | Milestones are administrative |
| E14 | Pilot-to-scale path | Need move from experiment to rollout | No scale ambition |
| E15 | Owner/RACI grid | Accountability is unclear | Too much process for audience |
| E16 | Execution scoreboard | Progress needs ongoing tracking | Metrics are not defined |

## Product / Demo

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| PD01 | Hero screenshot | Product UI is persuasive | UI is unfinished |
| PD02 | Use-case storyboard | Need user journey | Journey is not visual |
| PD03 | Feature-to-outcome map | Features need value translation | Features are too many |
| PD04 | Workflow before/after | Product reduces steps | Workflow not known |
| PD05 | Demo frame | Live demo needs orientation | Demo is self-explanatory |
| PD06 | Output artifact | Result matters more than UI | Output is not concrete |
| PD07 | Integration map | Ecosystem/connectors matter | Integrations are not a concern |
| PD08 | Adoption path | Buyer asks "how do we start?" | No implementation story |
| PD09 | Prompt/run trace | AI/agent demo needs transparent steps | Trace is too technical |
| PD10 | Human-in-the-loop | Review/control matters | Fully automated flow is the point |
| PD11 | Data-to-output | Input data becomes visible result | Data is unavailable |
| PD12 | Use-case chooser | Audience must pick relevant use case | Use cases are too many |
| PD13 | Sandbox vs production | Need separate demo from live reality | Audience does not care about deployment |
| PD14 | Failure boundary | Product limits build trust | Limits would distract from sale |
| PD15 | Workflow compression | Show fewer steps/time saved | Baseline workflow unknown |
| PD16 | Agent role map | Multi-agent system needs role clarity | Agents are just internal implementation |

## Offer / CTA

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| O01 | Offer stack | Multiple deliverables create value | Offer is simple |
| O02 | Pricing anchor | Price needs framing | Price not confirmed |
| O03 | Scope box | Boundaries reduce risk | Scope still unknown |
| O04 | Who it is for/not for | Qualification matters | Audience is already qualified |
| O05 | Objection handling | Resistance is predictable | Objections are unknown |
| O06 | Risk reversal | Buyer fears loss | No guarantee/support exists |
| O07 | Next-step ladder | Multiple conversion paths | One action is enough |
| O08 | CTA hero | One action should dominate | CTA not finalized |
| O09 | Value stack | Offer value comes from layered components | Components are weak |
| O10 | ROI frame | Buyer needs economic justification | ROI inputs are speculative |
| O11 | Guarantee box | Risk reversal is central | Guarantee is not approved |
| O12 | Application filter | Scarcity/qualification matters | Offer is open to all |
| O13 | Objection stack | Several objections must be answered quickly | Objections require nuance |
| O14 | Implementation promise | Buyer cares how delivery happens | Delivery details are not ready |
| O15 | Choice architecture | Present multiple packages/options | Too many options confuse |
| O16 | Commitment ladder | Audience needs a small first commitment | Direct purchase is expected |

## Teaching / Workshop

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| T01 | Mental model | Teach abstraction | Audience needs action first |
| T02 | Worked example | Show how method applies | Example is too complex |
| T03 | Exercise prompt | Live workshop | No facilitation time |
| T04 | Checklist handout | Audience needs retention | Checklist is generic |
| T05 | Mistake gallery | Prevent common errors | Mistakes are not known |
| T06 | Rubric | Evaluate work | Criteria are subjective |
| T07 | Fill-in template | Audience creates artifact | Input data unavailable |
| T08 | Recap ladder | Reinforce learning sequence | Deck is not educational |
| T09 | Drill-down example | Need zoom from principle to detail | Detail is too niche |
| T10 | Practice loop | Audience repeats a skill | No workshop time |
| T11 | Error correction | Show wrong answer becoming right | Error is obvious |
| T12 | Concept map | Multiple concepts need relationships | Map becomes taxonomy soup |
| T13 | Cheat sheet | Audience needs take-home reference | Live persuasion is priority |
| T14 | Facilitation board | Group input must be captured | No live interaction |
| T15 | Assessment checkpoint | Need verify understanding | Stakes are low |
| T16 | Skill progression | Show novice -> competent -> advanced | Progression is unclear |

## Research / Audit / Benchmark

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| A01 | Method card | Need credibility for analysis | Method is simple |
| A02 | Evidence ledger | Claims need traceability | Too much detail for live deck |
| A03 | Capability matrix | Compare features/capabilities | Criteria are weak |
| A04 | Weighted scorecard | Ranking needs weights | Weights are not justified |
| A05 | Gap cluster | Many findings need synthesis | Gaps are unrelated |
| A06 | Risk register | Decision depends on risk | Risks are speculative |
| A07 | Persona lens | Different users value different things | Personas are invented |
| A08 | Recommendation path | Analysis must become action | No decision required |
| A09 | Evidence strength heatmap | Need show confidence by claim | Audience does not need methodology |
| A10 | Coverage map | Need show what research covers/misses | Coverage is complete or irrelevant |
| A11 | Method comparison | Need compare evaluation approaches | Method debate distracts |
| A12 | Finding-to-action map | Findings must become backlog/actions | No implementation path |
| A13 | Source triangulation | Several sources support/contradict | Sources are weak |
| A14 | Benchmark quadrant | Players cluster on two axes | Axes are arbitrary |
| A15 | Capability gap radar | Many capabilities differ by player | Radar will be unreadable |
| A16 | Confidence note | Important uncertainty must be explicit | Confidence caveats weaken persuasion |

## Closing / Appendix

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| X01 | Executive summary | Deck also read async | Live only and short |
| X02 | Decision log | Need governance | No formal decision |
| X03 | FAQ | Objections/questions recur | Adds noise |
| X04 | Appendix table | Detail supports claims | Detail is core story |
| X05 | Source list | Research deck | Sources are informal |
| X06 | Glossary | Jargon unavoidable | Terms are common |
| X07 | Backup calculation | Finance/technical deck | Calc too fragile |
| X08 | Thank you / contact | Formal close | CTA needs stronger close |
| X09 | Source appendix | Audience may audit claims later | Sources are informal |
| X10 | Method appendix | Analysis needs reproducibility | Method is obvious |
| X11 | Detail table | Core slide must stay clean | Detail is actually central |
| X12 | Speaker notes page | Deck will be reused by presenters | Presenter is always the author |
| X13 | FAQ appendix | Questions are predictable but not core | FAQ repeats main slides |
| X14 | Glossary with examples | Terms need contextual examples | Definitions are enough |
| X15 | Implementation checklist | Audience must act after deck | No action expected |
| X16 | Decision record | Need preserve final decision and rationale | No formal governance |

## Visual / Editorial Composition

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| V01 | Full-bleed quote | A sentence should land emotionally | Quote is generic |
| V02 | Editorial split | Text and artifact need equal weight | Artifact is weak |
| V03 | Annotated screenshot | Screenshot needs guided attention | Screenshot is unreadable |
| V04 | Object spotlight | One artifact/object is the hero | Object is not meaningful |
| V05 | Diagram over photo | Need explain system over real context | Photo is decorative |
| V06 | Dense appendix table | Detail matters after narrative | Detail belongs in core flow |
| V07 | Command center | Multiple status signals need hierarchy | Signals do not relate |
| V08 | Tear-down markup | Critique needs visible annotations | Markups would embarrass stakeholder |
| V09 | Storyboard strip | Sequence of scenes explains change | Scenes are repetitive |
| V10 | Magazine opener | Strong editorial title with atmosphere | Deck is operational/technical |
| V11 | Minimal statement | One line needs silence/weight | Line is not strong |
| V12 | Reference board | Visual direction needs examples | References are off-brand |

## Interaction / Live Session

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| L01 | Poll prompt | Need audience input live | No polling mechanism |
| L02 | Chat capture | Audience suggestions drive demo | Chat will be too noisy |
| L03 | Hot seat frame | One participant/example becomes case | Privacy is a concern |
| L04 | Exercise timer | Live work needs pacing | Session is async |
| L05 | Decision vote | Group must choose option | Decision owner is not group |
| L06 | Q&A parking lot | Questions should be captured without derailing | Q&A is informal |
| L07 | Live build canvas | Presenter builds artifact in real time | Build may fail live |
| L08 | Breakout instruction | Groups need clear task | No facilitation support |

## Native PPT / Export Structures

| ID | Template | Use when | Avoid when |
|---|---|---|---|
| N01 | Editable title + shape grid | PPTX editability matters | Design needs complex raster |
| N02 | Native chart slide | Data must stay editable | Chart type unsupported |
| N03 | Native table slide | Client will edit table | Table is too dense |
| N04 | SmartArt-like process | PowerPoint users will edit process | Layout needs custom geometry |
| N05 | Template master variant | Corporate template controls style | No template source exists |
| N06 | Screenshot with native callouts | UI proof plus editable annotations | Screenshot itself needs editing |
| N07 | Math/diagram native | Technical notation must remain editable | Renderer cannot support notation |
| N08 | Print-safe appendix | Deck will be exported to PDF | Live presentation is priority |

## Selection Heuristics

- Hook slides use H, R, or P templates; never start with agenda unless required.
- Mechanism slides use M templates; avoid card walls.
- Financial decks need at least one F template before a recommendation.
- Benchmarks need A03 or A04 plus A08.
- Webinars need H/R early, M in the middle, O near the end.
- Demo decks need PD05 before showing live workflow.
- Live webinars/workshops should consider L templates for audience interaction.
- PPTX/client-delivery work should prefer N templates where editability matters.
- Visual design reviews should use V templates for critique and reference surfaces.
- If a slide has no suitable template, its function is probably unclear.


## Referência: references/source/references/template-selection-guide.md

# Template Selection Guide

Use this guide after normalizing the briefing and before selecting roteiro/slide structures. It prevents the skill from choosing templates by aesthetics instead of rhetorical job.

## Selection Order

1. Choose the deck job.
2. Choose the primary roteiro.
3. Choose one secondary roteiro only if it adds a missing module.
4. Choose slide structures by function.
5. Reject templates that create repetition, density, or weak proof.

## Deck Job To Roteiro

| User asks for | Primary roteiro | Secondary roteiro to borrow |
|---|---|---|
| Webinar that sells | 1. Webinar de venda educacional | 21. Founder-led sales webinar, 24. AI agent / automation demo |
| Founder webinar | 21. Founder-led sales webinar | 1. Webinar de venda educacional |
| Practical class/masterclass | 22. Tactical masterclass | 25. Offer creation workshop |
| Sales proposal | 18. Proposal / SOW | 26. Sales call deck / live close |
| Live sales call | 26. Sales call deck / live close | 5. Sales deck B2B |
| Product demo | 6. Product demo narrative | 24. AI agent / automation demo |
| AI/agent demo | 24. AI agent / automation demo | 23. Technical architecture pitch |
| Technical architecture | 23. Technical architecture pitch | 7. Strategy recommendation |
| Board or executive update | 3. Board update | 39. Executive one-decision deck |
| One decision | 39. Executive one-decision deck | 7. Strategy recommendation |
| Financial update | 2. Apresentação financeira executiva | 42. Data story / analytics narrative |
| Benchmark | 20. Benchmark / competitive analysis | 36. Procurement / vendor selection |
| Research briefing | 34. Research-to-action briefing | 8. Market research report |
| Data analysis | 42. Data story / analytics narrative | 2. Apresentação financeira executiva |
| Product strategy | 28. Product strategy memo deck | 13. Product launch |
| Product launch | 13. Product launch | 31. Content strategy / editorial plan |
| Course/cohort launch | 32. Course sales / cohort launch | 22. Tactical masterclass |
| Community pitch | 33. Community / membership pitch | 21. Founder-led sales webinar |
| Brand strategy | 30. Brand strategy deck | 19. Thought leadership keynote |
| Design critique | 29. Design critique / creative review | 16. Audit / diagnostic |
| Content strategy | 31. Content strategy / editorial plan | 34. Research-to-action briefing |
| Compliance | 35. Regulatory / compliance briefing | 43. Crisis / turnaround briefing |
| Vendor selection | 36. Procurement / vendor selection | 20. Benchmark / competitive analysis |
| Investor diligence | 37. Investor data room narrative | 17. Fundraising update |
| Transformation roadmap | 38. Transformation roadmap | 12. Change management / transformation |
| Crisis/turnaround | 43. Crisis / turnaround briefing | 15. Postmortem |
| Partnership | 44. Partnership pitch | 5. Sales deck B2B |
| Personal authority | 45. Personal portfolio / authority deck | 19. Thought leadership keynote |

## Slide Function To Structure Families

| Slide function | Prefer | Avoid |
|---|---|---|
| hook | H01-H16, V10, V11 | Agenda unless formally required |
| reframe | R01-R16 | Generic definition slides |
| diagnosis | D01-D16 | Unranked problem lists |
| proof | P01-P18, V03, V04 | Unsourced number walls |
| mechanism | M01-M18 | Card walls with overlapping concepts |
| comparison | C01-C16, A14 | Matrices without criteria |
| finance/data | F01-F18, A09, A13 | Charts without interpretation |
| execution | E01-E16 | Timelines with no owners |
| demo/product | PD01-PD16, L07 | UI screenshots without callouts |
| offer/CTA | O01-O16 | CTA slides with multiple competing actions |
| teaching/workshop | T01-T16, L01-L08 | Passive lecture templates |
| research/benchmark | A01-A16 | Ranking without evidence/method |
| appendix/close | X01-X16, N08 | Appendix detail in core narrative |
| visual critique | V01-V12 | Decorative visual moodboards |
| live interaction | L01-L08 | Interaction slides in async decks |
| PPT/native export | N01-N08 | Screenshot-only final PPTX when editability matters |

## Repetition Rules

- Do not use equivalent structures more than twice in a row.
- If three slides are all lists, convert one into proof, one into mechanism, and one into action.
- If a deck has more than 12 slides, include at least:
  - one proof template;
  - one mechanism template;
  - one decision/action template;
  - one visual/artifact template.
- If a sales/webinar deck has no objection or CTA structure, it is incomplete.
- If a benchmark deck has no methodology and evidence structure, it is not credible.
- If a product/demo deck has no output artifact, it is not persuasive.

## Template Rejection Checklist

Reject a selected template when:

- it was chosen because it “looks good” but does not fit slide function;
- it forces too much copy;
- it requires evidence or assets the user does not have;
- it repeats the previous slide's rhetorical job;
- it weakens editability for a PPTX/client-delivery requirement;
- it makes a live session passive when interaction is needed.

## Default Combinations

### High-conversion webinar

Roteiro: `1 + 21 + 24`

Structures:

`H01 -> R02 -> P10 -> D01 -> M07 -> A03 -> M01 -> PD05 -> O05 -> O08`

### Technical AI demo

Roteiro: `24 + 23`

Structures:

`PD02 -> D02 -> PD05 -> M16 -> PD09 -> PD06 -> PD10 -> PD14 -> E14`

### Executive decision deck

Roteiro: `39 + 7`

Structures:

`H16 -> X01 -> C12 -> P04 -> C09 -> A08 -> E09 -> O08`

### Benchmark / absorption deck

Roteiro: `20 + 34`

Structures:

`A01 -> A03 -> A04 -> A09 -> C14 -> A12 -> E14 -> X09`

### Tactical masterclass

Roteiro: `22 + 25`

Structures:

`H13 -> R04 -> T01 -> T02 -> T07 -> T10 -> T11 -> T13 -> O16`

### Proposal / SOW

Roteiro: `18 + 26`

Structures:

`D01 -> R08 -> M05 -> O03 -> E02 -> F18 -> O06 -> O08`


## Referência: references/source/templates/deck/copy-derived.yaml

```yaml
version: 1
historical_sources:
  - copy_hormozi_offer_systems
  - copy_jon_benson_vsl_frameworks
  - copy_ry_schwartz_course_launch_frameworks
  - copy_mappings
  - pitch_deck_matrix
independence_note: >
  These frameworks are absorbed into this file. Runtime use must not require
  squads/copy, squads/pitch-deck, or any external squad path.

deck_templates:
  - id: grand_slam_offer_deck
    name: Grand Slam Offer Deck
    job: Present an offer that becomes hard to compare on price.
    audience: [prospects, buyers, sales_team, launch_team]
    pick_when:
      - The deck must sell an offer, package, cohort, service, or program.
      - The user needs value stack, guarantee, urgency, and clear CTA.
    skip_when:
      - There is no defined product or commercial next step.
      - The audience is internal and not evaluating an offer.
    default_slide_count: {min: 10, ideal: 16, max: 24}
    narrative_arc:
      - proof
      - promise
      - plan
      - obstacles
      - deliverables
      - value_stack
      - guarantee
      - urgency
      - decision
    slide_sequence:
      - {slot: proof_first, function: credibility, required: true, visual_family: proof_stack}
      - {slot: dream_outcome, function: desire, required: true, visual_family: hero_claim}
      - {slot: obstacles, function: diagnosis, required: true, visual_family: fishbone_diagram}
      - {slot: solution_map, function: mechanism, required: true, visual_family: module_composition}
      - {slot: deliverables, function: offer, required: true, visual_family: offer_stack}
      - {slot: bonuses, function: value_stack, required: false, visual_family: comparison_columns}
      - {slot: guarantee, function: risk_reversal, required: true, visual_family: decision_card}
      - {slot: urgency_scarcity, function: urgency, required: false, visual_family: timeline}
      - {slot: price_anchor, function: commercial, required: false, visual_family: waterfall_chart}
      - {slot: cta, function: action, required: true, visual_family: decision_card}
    evidence_policy:
      - Start with proof if audience is skeptical.
      - Every bonus must solve a real obstacle.
      - Urgency and scarcity must be real, not decorative pressure.
    qa_gates: [offer_clarity_gate, proof_gate, cta_gate, ethical_persuasion_gate]
    absorbed_from: [copy_hormozi_offer_systems, copy_mappings]

  - id: vsl_slide_sequence
    name: VSL Slide Sequence
    job: Convert a video sales letter into slide-by-slide spoken narrative.
    audience: [cold_leads, warm_leads, product_aware_buyers]
    pick_when:
      - The deck is a VSL, recorded sales presentation, or high-conversion webinar.
      - The user needs timed script beats, not just static slides.
    skip_when:
      - The deck is a board update, academic lecture, or neutral report.
    default_slide_count: {min: 30, ideal: 55, max: 90}
    narrative_arc:
      - snap_suggestion_opening
      - problem_amplification
      - reluctant_hero_story
      - solution_preview
      - proof
      - offer
      - ethical_close
    slide_sequence:
      - {slot: snap_suggestion, function: hook, required: true, visual_family: hero_claim}
      - {slot: usp_within_first_10, function: differentiation, required: true, visual_family: contrast}
      - {slot: problem_amplification, function: tension, required: true, visual_family: diagnosis_fishbone}
      - {slot: story_failure, function: empathy, required: true, visual_family: visual_story}
      - {slot: discovery, function: mechanism_reveal, required: true, visual_family: mechanism_layered_system}
      - {slot: transformation_preview, function: desire, required: true, visual_family: before_after}
      - {slot: social_proof, function: proof, required: true, visual_family: proof_stack}
      - {slot: offer_presentation, function: conversion, required: true, visual_family: offer_stack}
      - {slot: guarantee, function: risk_reversal, required: true, visual_family: decision_card}
      - {slot: close, function: action, required: true, visual_family: decision_card}
    evidence_policy:
      - First ten slides must include USP or reason to continue watching.
      - Pain amplification must be empathetic, not manipulative.
      - Close must include offer, guarantee, urgency, and a single CTA.
    qa_gates: [belief_shift_gate, ethical_persuasion_gate, offer_clarity_gate, cta_gate]
    absorbed_from: [copy_jon_benson_vsl_frameworks]

  - id: cohort_launch_masterclass
    name: Cohort Launch Masterclass
    job: Help the prospect become ready to decide for or against a cohort offer.
    audience: [course_buyers, high_ticket_leads, cohort_candidates]
    pick_when:
      - The deck is for course launch, cohort enrollment, masterclass, or application funnel.
      - The sales motion should reduce pressure and facilitate decision.
    skip_when:
      - The offer is low-ticket impulse purchase with no transformation journey.
    default_slide_count: {min: 20, ideal: 34, max: 50}
    narrative_arc:
      - avatar_language
      - transformation_map
      - objections
      - decision_criteria
      - method
      - fit_filter
      - enrollment_path
    slide_sequence:
      - {slot: mirror_language, function: empathy, required: true, visual_family: hero_claim}
      - {slot: before_after_identity, function: transformation, required: true, visual_family: before_after}
      - {slot: hidden_obstacles, function: diagnosis, required: true, visual_family: fishbone_diagram}
      - {slot: method, function: teaching, required: true, visual_family: numbered_steps}
      - {slot: objection_matrix, function: objection_handling, required: true, visual_family: comparison_table}
      - {slot: who_is_for, function: qualification, required: true, visual_family: pros_cons_chart}
      - {slot: pressure_release, function: trust, required: true, visual_family: decision_card}
      - {slot: enrollment_path, function: action, required: true, visual_family: pipeline_with_stages}
    evidence_policy:
      - Use actual prospect language when available.
      - State who the offer is not for.
      - Objections must be handled before the close.
    qa_gates: [avatar_language_gate, objection_gate, ethical_persuasion_gate, cta_gate]
    absorbed_from: [copy_ry_schwartz_course_launch_frameworks]

  - id: investor_pitch_deck
    name: Investor Pitch Deck
    job: Earn the next investor meeting with conviction and compression.
    audience: [investors, angels, venture_capital, strategic_partners]
    pick_when:
      - The deck explains startup/product opportunity, market, traction, and ask.
    skip_when:
      - The deck is primarily customer sales or internal board review.
    default_slide_count: {min: 10, ideal: 12, max: 16}
    narrative_arc:
      - shift
      - problem
      - promised_land
      - solution
      - market
      - traction
      - model
      - team
      - ask
    slide_sequence:
      - {slot: shift, function: why_now, required: true, visual_family: contrast}
      - {slot: problem, function: diagnosis, required: true, visual_family: journey_map}
      - {slot: promised_land, function: desire, required: true, visual_family: hero_claim}
      - {slot: solution, function: mechanism, required: true, visual_family: module_composition}
      - {slot: market, function: opportunity, required: true, visual_family: nested_market}
      - {slot: traction, function: proof, required: true, visual_family: kpi_cards}
      - {slot: model, function: economics, required: true, visual_family: unit_economics}
      - {slot: team, function: credibility, required: true, visual_family: team_roster}
      - {slot: ask, function: action, required: true, visual_family: decision_card}
    evidence_policy:
      - Use the deck to earn next meeting, not answer every diligence question.
      - Traction must be specific or clearly labeled as pipeline/assumption.
    qa_gates: [investor_clarity_gate, proof_gate, decision_gate]
    absorbed_from: [pitch_deck_matrix, copy_mappings]
```


## Referência: references/source/templates/deck/playbook-routing.yaml

```yaml
version: 1
name: deck-playbook-routing
purpose: >
  Fast scenario routing for choosing a deck template, story arc, proof standard,
  and key-slide gate without rereading every long reference.

playbooks:
  benchmark_absorption:
    route_to_template: research_benchmark
    use_when: "Comparing tools, skills, apps, engines, repos, competitors, or open-source projects."
    mandatory_beats: [why_now, evaluation_frame, category_split, evidence, matrix, absorption_map, roadmap, decision]
    key_slides: [scope, matrix, absorption_map, build_vs_absorb, roadmap]
    proof_standard: "Each score needs source path, observed behavior, or explicit assumption."
    common_failure: "Mixed categories compared as if they were equivalent."
    force_split_when:
      - app_vs_skill_vs_engine_are_mixed
      - hosted_product_vs_local_skill_are_mixed
  webinar:
    route_to_template: webinar_conversion
    use_when: "Live or recorded event meant to teach and convert."
    mandatory_beats: [promise, enemy, false_beliefs, mechanism, proof, implementation, offer, cta]
    key_slides: [promise, mechanism, proof, offer, cta]
    proof_standard: "At least one concrete demo, artifact, case, or before/after."
    common_failure: "Teaching becomes generic and the offer appears too late."
  sales_or_offer:
    route_to_template: grand_slam_offer_deck
    use_when: "Selling a service, product, cohort, proposal, or high-ticket offer."
    mandatory_beats: [proof, dream_outcome, obstacles, mechanism, deliverables, guarantee, decision]
    key_slides: [proof_first, dream_outcome, solution_map, deliverables, cta]
    proof_standard: "Every feature must connect to outcome, obstacle, or risk reversal."
    common_failure: "Feature stack without buyer pain or decision criteria."
  vsl:
    route_to_template: vsl_slide_sequence
    use_when: "Scripted video sales letter or long-form conversion presentation."
    mandatory_beats: [snap_suggestion_opening, usp, problem_amplification, story, mechanism, proof, offer, close]
    key_slides: [snap_suggestion, usp_within_first_10, mechanism_reveal, offer_presentation, close]
    proof_standard: "USP appears early; proof precedes offer; close has one CTA."
    common_failure: "Long setup with no reason to keep watching."
  financial_or_board:
    route_to_template: financial_presentation
    use_when: "Revenue, margin, runway, variance, forecast, budget, or board decision."
    mandatory_beats: [answer_first, drivers, variance, risk, options, recommendation, ask]
    key_slides: [executive_summary, revenue_trend, variance_bridge, scenarios, ask]
    proof_standard: "Every number has source, period, unit, and assumption label."
    common_failure: "Charts show numbers but do not explain variance or decision."
  product_strategy:
    route_to_template: product_strategy
    use_when: "What to build, why, in what order, and with what tradeoffs."
    mandatory_beats: [market_shift, customer_gap, product_thesis, mechanism, capability_map, tradeoffs, roadmap]
    key_slides: [thesis, customer_gap, system, capability_map, roadmap]
    proof_standard: "Every roadmap item traces to customer gap, benchmark, or strategic constraint."
    common_failure: "Roadmap becomes feature inventory."
  investor_pitch:
    route_to_template: investor_pitch_deck
    use_when: "Startup, product, market, traction, team, and investment ask."
    mandatory_beats: [shift, problem, promised_land, solution, market, traction, model, team, ask]
    key_slides: [shift, problem, solution, traction, ask]
    proof_standard: "Traction, market, and model are sourced or labeled as assumption."
    common_failure: "Too much diligence detail before earning the next meeting."
  course_or_workshop:
    route_to_template: cohort_launch_masterclass
    use_when: "Teaching, training, cohort launch, masterclass, or workshop."
    mandatory_beats: [mirror_language, transformation, hidden_obstacles, method, objections, fit_filter, enrollment_path]
    key_slides: [mirror_language, method, objection_matrix, who_is_for, enrollment_path]
    proof_standard: "Use learner language and concrete examples; state who it is not for."
    common_failure: "Curriculum outline replaces audience transformation."

selection_output:
  required_fields:
    - selected_playbook
    - route_to_template
    - reason
    - rejected_playbooks
    - forced_splits
    - key_slide_gate
```


## Referência: references/source/templates/deck/route-map.yaml

```yaml
version: 1
deck_templates:
  - id: research_benchmark
    name: Research Benchmark
    job: Compare players and convert findings into product/design decisions.
    audience: [founders, product_leads, technical_leads, strategy_team]
    pick_when:
      - The deck compares tools, competitors, repos, skills, agents, or products.
      - The user needs a decision, absorption map, or roadmap from research.
    skip_when:
      - The goal is only a feature list with no decision.
      - The evidence base is too weak to rank; use discovery_report first.
    default_slide_count: {min: 12, ideal: 18, max: 28}
    narrative_arc:
      - why_the_benchmark_exists
      - evaluation_frame
      - category_split
      - matrix
      - unfair_advantages
      - absorption_map
      - product_implications
      - roadmap
      - decision
    slide_sequence:
      - {slot: cover, function: hook, required: true, visual_family: hero_claim}
      - {slot: context, function: reframe, required: true, visual_family: contrast}
      - {slot: scope, function: evaluation_frame, required: true, visual_family: layered_architecture}
      - {slot: category_split, function: segmentation, required: true, visual_family: matrix_2x2}
      - {slot: score_summary, function: proof, required: true, visual_family: horizontal_bar_chart}
      - {slot: matrix, function: comparison, required: true, visual_family: harvey_balls_table}
      - {slot: winner_is_not_enough, function: nuance, required: true, visual_family: quadrant_text_bullets}
      - {slot: absorption_map, function: mechanism, required: true, visual_family: module_composition}
      - {slot: build_vs_absorb, function: decision, required: true, visual_family: comparison_columns}
      - {slot: roadmap, function: plan, required: true, visual_family: roadmap_vertical}
      - {slot: qa, function: credibility, required: false, visual_family: checklist}
      - {slot: appendix, function: evidence, required: false, visual_family: basic_table}
    evidence_policy:
      - Every score must cite source path, observed behavior, or explicit assumption.
      - Matrix summaries must avoid repeating the same sentence under every score.
      - Comparisons must separate app, skill, engine, and runtime categories when mixed players are present.
    qa_gates: [template_selection_gate, evidence_gate, matrix_noise_gate, decision_gate]
    absorbed_from: [ppt-master, Presenton, presentation-ai, PPTAgent, banana-slides]

  - id: webinar_conversion
    name: Webinar Conversion
    job: Move a cold or warm audience from attention to a concrete CTA.
    audience: [leads, prospects, community, students]
    pick_when:
      - The deck supports a webinar, masterclass, live training, or recorded event.
      - The deck must educate and convert.
    skip_when:
      - The deck is a neutral technical tutorial with no CTA.
    default_slide_count: {min: 18, ideal: 32, max: 45}
    narrative_arc:
      - promise
      - enemy
      - mistake
      - new_mechanism
      - proof
      - framework
      - implementation
      - offer
      - objections
      - action
    slide_sequence:
      - {slot: promise, function: hook, required: true, visual_family: hero_claim}
      - {slot: stakes, function: tension, required: true, visual_family: contrast}
      - {slot: enemy, function: diagnosis, required: true, visual_family: fishbone_diagram}
      - {slot: false_beliefs, function: objection_preempt, required: true, visual_family: pros_cons_chart}
      - {slot: mechanism, function: mechanism, required: true, visual_family: layered_architecture}
      - {slot: framework, function: teaching, required: true, visual_family: numbered_steps}
      - {slot: example, function: proof, required: true, visual_family: before_after}
      - {slot: implementation, function: plan, required: true, visual_family: pipeline_with_stages}
      - {slot: offer, function: conversion, required: true, visual_family: offer_stack}
      - {slot: objections, function: risk_reversal, required: true, visual_family: comparison_table}
      - {slot: cta, function: action, required: true, visual_family: decision}
    evidence_policy:
      - Use at least one concrete before/after, demo, artifact, or case.
      - Do not keep generic motivational slides.
    qa_gates: [belief_shift_gate, offer_clarity_gate, visual_density_gate]
    absorbed_from: [slide-deck-ai, presentation-ai, banana-slides]

  - id: financial_presentation
    name: Financial Presentation
    job: Explain performance, variance, financial risk, and decision asks.
    audience: [founders, board, finance, investors]
    pick_when:
      - The deck contains revenue, margin, burn, CAC, LTV, forecast, budget, or variance.
    skip_when:
      - The content is a marketing pitch with only one financial slide.
    default_slide_count: {min: 8, ideal: 14, max: 24}
    narrative_arc:
      - headline_result
      - context
      - drivers
      - variance
      - risk
      - options
      - recommendation
      - decision_ask
    slide_sequence:
      - {slot: executive_summary, function: answer_first, required: true, visual_family: kpi_cards}
      - {slot: revenue_trend, function: proof, required: true, visual_family: line_chart}
      - {slot: variance_bridge, function: explanation, required: true, visual_family: waterfall_chart}
      - {slot: segment_breakdown, function: comparison, required: false, visual_family: stacked_bar_chart}
      - {slot: unit_economics, function: diagnosis, required: false, visual_family: bullet_chart}
      - {slot: scenarios, function: decision, required: true, visual_family: comparison_columns}
      - {slot: ask, function: action, required: true, visual_family: decision}
    evidence_policy:
      - Numbers need source or assumption label.
      - Tables must be right-aligned and totals visually distinct.
    qa_gates: [data_integrity_gate, chart_selection_gate, decision_gate]
    absorbed_from: [ppt-master, powerpoint-skill, slide-deck-ai]

  - id: sales_deck
    name: Sales Deck
    job: Turn customer pain into urgency, trust, and next step.
    audience: [prospects, buyers, champions, economic_buyer]
    pick_when:
      - The deck must support a sales conversation, proposal, or product pitch.
    skip_when:
      - The user wants a purely educational training deck.
    default_slide_count: {min: 8, ideal: 14, max: 22}
    narrative_arc:
      - customer_problem
      - cost_of_inaction
      - new_way
      - solution
      - proof
      - implementation
      - commercial_next_step
    slide_sequence:
      - {slot: customer_truth, function: hook, required: true, visual_family: hero_claim}
      - {slot: pain_map, function: diagnosis, required: true, visual_family: fishbone_diagram}
      - {slot: new_way, function: reframe, required: true, visual_family: contrast}
      - {slot: solution_system, function: mechanism, required: true, visual_family: module_composition}
      - {slot: proof, function: proof, required: true, visual_family: before_after}
      - {slot: plan, function: plan, required: true, visual_family: numbered_steps}
      - {slot: investment, function: commercial, required: false, visual_family: comparison_columns}
      - {slot: next_step, function: action, required: true, visual_family: decision}
    evidence_policy:
      - Claims must connect to buyer pain or measurable outcome.
      - Product features cannot appear before problem and new mechanism.
    qa_gates: [buyer_relevance_gate, proof_gate, cta_gate]
    absorbed_from: [presentation-ai, slide-deck-ai, ppt-master]

  - id: board_update
    name: Board Update
    job: Give leaders a high-signal update and force the right decisions.
    audience: [board, founders, executives]
    pick_when:
      - The deck reviews company status, risks, priorities, or asks.
    skip_when:
      - The deck is for external marketing.
    default_slide_count: {min: 8, ideal: 12, max: 18}
    narrative_arc:
      - answer_first
      - what_changed
      - metrics
      - strategic_tension
      - risks
      - decisions_needed
      - next_90_days
    slide_sequence:
      - {slot: answer_first, function: executive_summary, required: true, visual_family: kpi_cards}
      - {slot: what_changed, function: update, required: true, visual_family: timeline}
      - {slot: metrics, function: proof, required: true, visual_family: bullet_chart}
      - {slot: risks, function: risk, required: true, visual_family: matrix_2x2}
      - {slot: decisions, function: decision, required: true, visual_family: decision}
      - {slot: roadmap, function: plan, required: true, visual_family: roadmap_vertical}
    evidence_policy:
      - Use explicit decision asks, not passive updates.
    qa_gates: [executive_density_gate, decision_gate, data_integrity_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: product_strategy
    name: Product Strategy
    job: Align product bets, architecture, market insight, and roadmap.
    audience: [product, engineering, founders, GTM]
    pick_when:
      - The deck must explain what to build, why, and in what order.
    skip_when:
      - The goal is only implementation documentation.
    default_slide_count: {min: 10, ideal: 18, max: 28}
    narrative_arc:
      - market_shift
      - customer_gap
      - product_thesis
      - mechanism
      - capability_map
      - tradeoffs
      - roadmap
      - operating_model
    slide_sequence:
      - {slot: thesis, function: reframe, required: true, visual_family: hero_claim}
      - {slot: customer_gap, function: diagnosis, required: true, visual_family: journey_map}
      - {slot: system, function: mechanism, required: true, visual_family: layered_architecture}
      - {slot: capability_map, function: comparison, required: true, visual_family: harvey_balls_table}
      - {slot: tradeoffs, function: decision, required: true, visual_family: pros_cons_chart}
      - {slot: roadmap, function: plan, required: true, visual_family: roadmap_vertical}
    evidence_policy:
      - Every roadmap item must tie to customer gap or strategic constraint.
    qa_gates: [strategy_traceability_gate, roadmap_gate, visual_density_gate]
    absorbed_from: [Presenton, presentation-ai, ppt-master, PPTAgent]

  - id: discovery_report
    name: Discovery Report
    job: Convert exploratory research into a clear map of what is known, unknown, and next.
    audience: [founders, analysts, product, strategy]
    pick_when:
      - Evidence is incomplete and the honest output is a research map, not a final decision.
    skip_when:
      - The user already has enough evidence for a recommendation.
    default_slide_count: {min: 8, ideal: 12, max: 18}
    narrative_arc:
      - question
      - method
      - findings
      - uncertainty
      - hypotheses
      - next_tests
    slide_sequence:
      - {slot: question, function: scope, required: true, visual_family: hero_claim}
      - {slot: method, function: credibility, required: true, visual_family: process_flow}
      - {slot: findings, function: synthesis, required: true, visual_family: vertical_list}
      - {slot: unknowns, function: uncertainty, required: true, visual_family: matrix_2x2}
      - {slot: next_tests, function: plan, required: true, visual_family: numbered_steps}
    evidence_policy:
      - Unverified claims must be marked as hypotheses.
    qa_gates: [evidence_gate, uncertainty_gate]
    absorbed_from: [banana-slides, slide-deck-ai, ppt-master]

  - id: ai_product_demo
    name: AI Product Demo
    job: Prove an AI workflow through a controlled demo, artifact trail, and decision path.
    audience: [founders, product_leads, technical_buyers, operators]
    pick_when:
      - The deck supports a live demo, product walkthrough, or AI workflow proof.
      - The user must show how the system works, not only what it promises.
    skip_when:
      - There is no product, workflow, or demonstrable artifact yet.
    default_slide_count: {min: 8, ideal: 14, max: 22}
    narrative_arc:
      - user_job
      - broken_workflow
      - new_workflow
      - demo_contract
      - proof_artifacts
      - risk_controls
      - rollout_plan
      - decision
    slide_sequence:
      - {slot: job_to_be_done, function: hook, required: true, visual_family: hero_claim}
      - {slot: current_workflow, function: diagnosis, required: true, visual_family: journey_map}
      - {slot: new_workflow, function: mechanism, required: true, visual_family: system_flow}
      - {slot: demo_script, function: demo_setup, required: true, visual_family: screen_sequence}
      - {slot: proof_artifacts, function: proof, required: true, visual_family: evidence_cards}
      - {slot: risks, function: risk, required: true, visual_family: risk_heatmap}
      - {slot: rollout, function: plan, required: true, visual_family: numbered_steps}
      - {slot: decision, function: decision, required: true, visual_family: decision_card}
    evidence_policy:
      - Demo claims need a visible artifact, expected output, or observed behavior.
      - Model limitations and human review points must be explicit.
    qa_gates: [demo_gate, proof_gate, risk_gate, decision_gate]
    absorbed_from: [Presenton, PPTAgent, powerpoint-skill]

  - id: design_system_audit
    name: Design System Audit
    job: Turn design-system inspection into a prioritized improvement roadmap.
    audience: [design_leads, product_leads, engineering_leads, founders]
    pick_when:
      - The deck evaluates tokens, components, templates, brand fidelity, or design debt.
      - The user wants to improve visual quality, consistency, or implementation readiness.
    skip_when:
      - The ask is only a brand moodboard with no system audit.
    default_slide_count: {min: 10, ideal: 16, max: 24}
    narrative_arc:
      - design_mandate
      - current_state
      - token_quality
      - component_coverage
      - template_coverage
      - accessibility
      - absorption_plan
      - roadmap
    slide_sequence:
      - {slot: mandate, function: hook, required: true, visual_family: hero_claim}
      - {slot: current_state, function: diagnosis, required: true, visual_family: dashboard_grid}
      - {slot: token_audit, function: comparison, required: true, visual_family: harvey_balls_table}
      - {slot: component_gap, function: comparison, required: true, visual_family: feature_matrix_table}
      - {slot: template_gap, function: comparison, required: true, visual_family: matrix_2x2}
      - {slot: accessibility, function: risk, required: true, visual_family: checklist}
      - {slot: reference_standard, function: proof, required: true, visual_family: evidence_cards}
      - {slot: roadmap, function: plan, required: true, visual_family: gantt_chart}
    evidence_policy:
      - Every design score must map to a rendered example, token, component, or screenshot.
      - Avoid subjective taste labels without observable criteria.
    qa_gates: [design_mastery_gate, visual_regression_gate, accessibility_gate]
    absorbed_from: [ppt-master, presentation-ai, redpine-ds, aiox-brandbook]

  - id: investor_update
    name: Investor Update
    job: Explain traction, risks, asks, and strategic next steps with high executive density.
    audience: [investors, board, founders, finance]
    pick_when:
      - The deck updates external or internal capital stakeholders.
      - The user needs a crisp view of progress, constraints, and ask.
    skip_when:
      - The deck is a full fundraising pitch with first-time company narrative.
    default_slide_count: {min: 8, ideal: 12, max: 18}
    narrative_arc:
      - headline
      - traction
      - market_signal
      - product_progress
      - financials
      - risks
      - next_asks
    slide_sequence:
      - {slot: headline_update, function: answer_first, required: true, visual_family: executive_snapshot}
      - {slot: traction, function: proof, required: true, visual_family: line_chart}
      - {slot: market_signal, function: proof, required: false, visual_family: evidence_cards}
      - {slot: product_progress, function: update, required: true, visual_family: timeline}
      - {slot: financials, function: financial_update, required: true, visual_family: waterfall_chart}
      - {slot: risks, function: risk, required: true, visual_family: risk_heatmap}
      - {slot: asks, function: decision, required: true, visual_family: decision_card}
    evidence_policy:
      - Every metric must state source period and whether actual, forecast, or assumption.
    qa_gates: [executive_density_gate, data_integrity_gate, decision_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: technical_architecture_review
    name: Technical Architecture Review
    job: Make system tradeoffs, risks, migration path, and decision asks legible.
    audience: [engineering_leads, architects, CTOs, product_leads]
    pick_when:
      - The deck explains architecture, migration, integration, or technical decision tradeoffs.
    skip_when:
      - The content is purely product strategy without technical flow.
    default_slide_count: {min: 10, ideal: 16, max: 26}
    narrative_arc:
      - context
      - current_architecture
      - constraints
      - target_architecture
      - tradeoffs
      - migration
      - risks
      - decision
    slide_sequence:
      - {slot: context, function: hook, required: true, visual_family: hero_claim}
      - {slot: current_system, function: architecture, required: true, visual_family: system_flow}
      - {slot: constraints, function: diagnosis, required: true, visual_family: vertical_list}
      - {slot: target_system, function: mechanism, required: true, visual_family: layered_architecture}
      - {slot: tradeoffs, function: decision, required: true, visual_family: pros_cons_chart}
      - {slot: migration, function: plan, required: true, visual_family: swimlane_process}
      - {slot: risks, function: risk, required: true, visual_family: risk_heatmap}
      - {slot: decision, function: decision, required: true, visual_family: decision_card}
    evidence_policy:
      - Architecture claims need code path, observed behavior, diagram source, or explicit assumption.
      - Security and data-boundary risks must be labeled when relevant.
    qa_gates: [architecture_gate, risk_gate, decision_gate]
    absorbed_from: [PPTAgent, powerpoint-skill, ppt-master]

  - id: customer_case_study
    name: Customer Case Study
    job: Convert one project or customer outcome into repeatable proof.
    audience: [prospects, sales, customer_success, executives]
    pick_when:
      - The user has a customer story, internal case, implementation result, or before/after evidence.
    skip_when:
      - There is no named baseline, intervention, or result.
    default_slide_count: {min: 6, ideal: 10, max: 16}
    narrative_arc:
      - customer_context
      - baseline_problem
      - intervention
      - implementation_path
      - measurable_result
      - repeatable_pattern
      - next_step
    slide_sequence:
      - {slot: context, function: hook, required: true, visual_family: hero_claim}
      - {slot: baseline, function: diagnosis, required: true, visual_family: journey_map}
      - {slot: intervention, function: mechanism, required: true, visual_family: module_composition}
      - {slot: implementation, function: plan, required: true, visual_family: process_flow}
      - {slot: result, function: proof, required: true, visual_family: case_study_panel}
      - {slot: repeatable_pattern, function: teaching, required: true, visual_family: numbered_steps}
      - {slot: next_step, function: action, required: false, visual_family: decision_card}
    evidence_policy:
      - Case results need metric, artifact, quote, or dated before/after.
    qa_gates: [case_study_gate, proof_gate, cta_gate]
    absorbed_from: [slide-deck-ai, banana-slides, ppt-master]

  - id: fundraising_pitch
    name: Fundraising Pitch
    job: Move investors from market belief to company-specific conviction and next meeting.
    audience: [investors, founders, board, advisors]
    pick_when:
      - The deck is for seed, series, angel, or strategic fundraising.
    skip_when:
      - The ask is a routine investor update; use investor_update.
    default_slide_count: {min: 10, ideal: 14, max: 18}
    narrative_arc: [market_shift, pain, solution, traction, moat, business_model, GTM, team, financials, ask]
    slide_sequence:
      - {slot: market_shift, function: reframe, required: true, visual_family: market_map}
      - {slot: customer_pain, function: diagnosis, required: true, visual_family: journey_map}
      - {slot: solution, function: mechanism, required: true, visual_family: module_composition}
      - {slot: traction, function: proof, required: true, visual_family: kpi_cards}
      - {slot: moat, function: positioning, required: true, visual_family: competitive_landscape_table}
      - {slot: business_model, function: commercial, required: true, visual_family: unit_economics_panel}
      - {slot: ask, function: action, required: true, visual_family: decision_card}
    evidence_policy:
      - Traction, market and financial claims need source, period, or explicit assumption.
    qa_gates: [proof_gate, investor_density_gate, decision_gate]
    absorbed_from: [presentation-ai, ppt-master, Presenton]

  - id: sales_proposal
    name: Sales Proposal
    job: Convert a qualified opportunity into scope, investment, risk reversal, and next step.
    audience: [economic_buyer, champion, procurement, delivery_lead]
    pick_when:
      - The deck responds to a qualified prospect or proposal request.
    skip_when:
      - The audience has not recognized the problem yet; use sales_deck.
    default_slide_count: {min: 8, ideal: 12, max: 18}
    narrative_arc: [buyer_context, diagnosed_gap, proposed_solution, delivery_model, proof, investment, risks, next_step]
    slide_sequence:
      - {slot: buyer_context, function: hook, required: true, visual_family: executive_snapshot}
      - {slot: diagnosed_gap, function: diagnosis, required: true, visual_family: evidence_cards}
      - {slot: solution_scope, function: mechanism, required: true, visual_family: module_composition}
      - {slot: delivery_model, function: operating_model, required: true, visual_family: swimlane_process}
      - {slot: proof, function: proof, required: true, visual_family: case_study_panel}
      - {slot: investment, function: commercial, required: true, visual_family: pricing_table}
      - {slot: next_step, function: action, required: true, visual_family: decision_card}
    evidence_policy:
      - Proposal scope must tie each component to a diagnosed buyer gap.
    qa_gates: [buyer_relevance_gate, offer_clarity_gate, cta_gate]
    absorbed_from: [banana-slides, presentation-ai, ppt-master]

  - id: qbr_operating_review
    name: QBR Operating Review
    job: Review performance, explain variance, expose risks, and lock next-quarter priorities.
    audience: [executives, operators, board, client_leadership]
    pick_when:
      - The deck is a quarterly/monthly business review or operating review.
    skip_when:
      - The deck is only financial performance; use financial_presentation.
    default_slide_count: {min: 10, ideal: 16, max: 24}
    narrative_arc: [headline, KPI_snapshot, variance, customer_health, initiatives, risks, priorities, decisions]
    slide_sequence:
      - {slot: headline, function: answer_first, required: true, visual_family: executive_snapshot}
      - {slot: KPIs, function: proof, required: true, visual_family: dashboard_grid}
      - {slot: variance, function: explanation, required: true, visual_family: waterfall_chart}
      - {slot: customer_health, function: diagnosis, required: false, visual_family: cohort_retention}
      - {slot: initiatives, function: update, required: true, visual_family: timeline}
      - {slot: risks, function: risk, required: true, visual_family: risk_heatmap}
      - {slot: decisions, function: decision, required: true, visual_family: decision_card}
    evidence_policy:
      - KPI pages need period, baseline, target, and owner when available.
    qa_gates: [executive_density_gate, data_integrity_gate, decision_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: training_course
    name: Training Course
    job: Teach a repeatable capability through concept, examples, exercises, and assessment.
    audience: [students, team_members, customers, workshop_participants]
    pick_when:
      - The deck is a course, internal training, onboarding module, or enablement session.
    skip_when:
      - The session is primarily collaborative; use workshop_facilitation.
    default_slide_count: {min: 18, ideal: 32, max: 60}
    narrative_arc: [learning_outcome, why_it_matters, mental_model, examples, guided_practice, assessment, next_practice]
    slide_sequence:
      - {slot: outcome, function: hook, required: true, visual_family: hero_claim}
      - {slot: mental_model, function: teaching, required: true, visual_family: numbered_steps}
      - {slot: example, function: proof, required: true, visual_family: before_after}
      - {slot: exercise, function: practice, required: true, visual_family: workshop_canvas}
      - {slot: checklist, function: qa, required: true, visual_family: checklist}
      - {slot: next_practice, function: action, required: true, visual_family: agenda_timeline}
    evidence_policy:
      - Every lesson block needs an example or exercise before moving to the next concept.
    qa_gates: [didactic_clarity_gate, example_gate, practice_gate]
    absorbed_from: [slide-deck-ai, presentation-ai]

  - id: workshop_facilitation
    name: Workshop Facilitation
    job: Guide a group through alignment, exercises, decisions, and artifact creation.
    audience: [founders, product_team, GTM_team, leadership_team, clients]
    pick_when:
      - The deck is used live to facilitate decisions or co-creation.
    skip_when:
      - The deck is consumed asynchronously; use training_course or board_update.
    default_slide_count: {min: 12, ideal: 24, max: 40}
    narrative_arc: [goal, rules, context, divergent_thinking, synthesis, decision, ownership, next_steps]
    slide_sequence:
      - {slot: goal, function: hook, required: true, visual_family: hero_claim}
      - {slot: agenda, function: plan, required: true, visual_family: agenda_timeline}
      - {slot: exercise_1, function: practice, required: true, visual_family: workshop_canvas}
      - {slot: synthesis, function: synthesis, required: true, visual_family: affinity_map}
      - {slot: decision, function: decision, required: true, visual_family: decision_tree}
      - {slot: owners, function: operating_model, required: true, visual_family: responsibility_matrix}
    evidence_policy:
      - Workshop outputs must define artifact, timebox, and decision owner.
    qa_gates: [facilitation_gate, decision_gate, accountability_gate]
    absorbed_from: [presentation-ai, banana-slides]

  - id: product_launch
    name: Product Launch
    job: Align market message, release plan, channels, risks, and launch success metrics.
    audience: [product, marketing, sales, customer_success, founders]
    pick_when:
      - The deck plans or announces a launch, release, campaign, or GTM motion.
    skip_when:
      - The deck is only product strategy without launch execution.
    default_slide_count: {min: 10, ideal: 16, max: 24}
    narrative_arc: [launch_thesis, audience, positioning, offer, channel_plan, readiness, risks, launch_calendar]
    slide_sequence:
      - {slot: thesis, function: hook, required: true, visual_family: hero_claim}
      - {slot: audience, function: segmentation, required: true, visual_family: stakeholder_map}
      - {slot: positioning, function: positioning, required: true, visual_family: market_map}
      - {slot: offer, function: commercial, required: true, visual_family: offer_stack}
      - {slot: channel_plan, function: plan, required: true, visual_family: launch_calendar}
      - {slot: readiness, function: qa, required: true, visual_family: checklist}
      - {slot: risks, function: risk, required: true, visual_family: risk_heatmap}
    evidence_policy:
      - Launch bets need audience signal, channel rationale, and readiness criteria.
    qa_gates: [positioning_gate, readiness_gate, risk_gate]
    absorbed_from: [Presenton, presentation-ai, ppt-master]

  - id: incident_postmortem
    name: Incident Postmortem
    job: Explain what happened, why, user impact, corrective actions, and prevention.
    audience: [engineering, leadership, customer_success, clients]
    pick_when:
      - The deck reviews an outage, failure, quality incident, or process breakdown.
    skip_when:
      - The deck is a generic risk review; use board_update or qbr_operating_review.
    default_slide_count: {min: 8, ideal: 12, max: 18}
    narrative_arc: [summary, timeline, impact, root_cause, contributing_factors, fixes, prevention, owner_commitments]
    slide_sequence:
      - {slot: summary, function: answer_first, required: true, visual_family: executive_snapshot}
      - {slot: timeline, function: proof, required: true, visual_family: incident_timeline}
      - {slot: impact, function: proof, required: true, visual_family: kpi_cards}
      - {slot: root_cause, function: diagnosis, required: true, visual_family: fishbone_diagram}
      - {slot: fixes, function: plan, required: true, visual_family: corrective_action_table}
      - {slot: prevention, function: operating_model, required: true, visual_family: checklist}
    evidence_policy:
      - Postmortem claims require timestamps, owner, affected scope, and fix status.
    qa_gates: [incident_clarity_gate, accountability_gate, risk_gate]
    absorbed_from: [powerpoint-skill, ppt-master]

  - id: hiring_onboarding
    name: Hiring and Onboarding
    job: Align role scorecard, interview criteria, ramp plan, and success expectations.
    audience: [hiring_managers, candidates, people_ops, team_leads]
    pick_when:
      - The deck supports hiring, onboarding, enablement, or role clarity.
    skip_when:
      - The deck is a broad company culture presentation with no role decision.
    default_slide_count: {min: 8, ideal: 12, max: 18}
    narrative_arc: [role_mission, scorecard, operating_context, interview_criteria, ramp_plan, success_metrics, decision]
    slide_sequence:
      - {slot: role_mission, function: hook, required: true, visual_family: hero_claim}
      - {slot: scorecard, function: comparison, required: true, visual_family: hiring_scorecard}
      - {slot: operating_context, function: operating_model, required: true, visual_family: responsibility_matrix}
      - {slot: ramp_plan, function: plan, required: true, visual_family: ramp_plan}
      - {slot: success_metrics, function: proof, required: true, visual_family: bullet_chart}
      - {slot: decision, function: decision, required: false, visual_family: decision_card}
    evidence_policy:
      - Role expectations must separate skills, outcomes, behaviors, and first-90-day outputs.
    qa_gates: [role_clarity_gate, accountability_gate, decision_gate]
    absorbed_from: [ppt-master, presentation-ai]
```


## Referência: references/source/templates/eval/design-regression-corpus.yaml

```yaml
version: 1
name: design-regression-corpus
purpose: >
  Regression corpus for proving that slide design quality is repeatable across
  deck jobs, themes, density levels, and source-template families.

minimum_reference_bar:
  fixture_cases: 30
  deck_jobs: 10
  theme_profiles: 8
  density_levels: [low, medium, high, appendix]
  required_review_roles: [cover, reframe, mechanism, proof_or_demo, cta_or_decision]

review_lenses:
  - {id: hierarchy, max_points: 20, pass_floor: 18}
  - {id: scan_path, max_points: 20, pass_floor: 18}
  - {id: spacing_density, max_points: 20, pass_floor: 18}
  - {id: theme_fidelity, max_points: 20, pass_floor: 18}
  - {id: evidence_visibility, max_points: 20, pass_floor: 18}

fixture_cases:
  - {id: board_update_executive_summary, deck_job: board_update, fixture_set: executive_strategy_design_set, wireframes: [executive-summary.html, financial-waterfall.html, roadmap-decision.html], theme_profile: boardroom_graphite, density: high, required_checks: [action_title_scan_path, dense_table_readability, source_line_fit]}
  - {id: strategy_benchmark_matrix, deck_job: benchmark_analysis, fixture_set: executive_strategy_design_set, wireframes: [benchmark-matrix.html, decision-options.html, risk-heatmap.html], theme_profile: consulting_midnight, density: high, required_checks: [matrix_scan_path, row_column_legibility, leader_highlight_clarity]}
  - {id: investor_update_operating_metrics, deck_job: investor_update, fixture_set: executive_strategy_design_set, wireframes: [unit-economics.html, cohort-retention.html, portfolio-allocation.html], theme_profile: founder_pitch_light, density: medium, required_checks: [metric_hierarchy, chart_label_legibility, narrative_takeaway_visibility]}
  - {id: product_demo_api_flow, deck_job: product_demo, fixture_set: product_demo_design_set, wireframes: [api-request-response.html, screen-sequence.html, service-catalog.html], theme_profile: product_saas_clean, density: medium, required_checks: [code_text_fit, demo_flow_continuity, provider_badge_spacing]}
  - {id: technical_architecture_mechanism, deck_job: technical_architecture_review, fixture_set: product_demo_design_set, wireframes: [technical-architecture.html, dependency-map.html, code-explanation.html], theme_profile: technical_blueprint, density: high, required_checks: [diagram_node_readability, edge_label_spacing, code_text_fit]}
  - {id: api_mcp_demo_sequence, deck_job: api_or_mcp_demo, fixture_set: product_demo_design_set, wireframes: [api-request-response.html, data-lineage.html, traceability-matrix.html], theme_profile: startup_demo_neon, density: medium, required_checks: [request_response_alignment, trace_visibility, theme_contrast]}
  - {id: brand_manifesto_belief_shift, deck_job: brand_manifesto, fixture_set: brand_manifesto_design_set, wireframes: [brand-principles.html, mission-vision.html, quote-evidence-panel.html], theme_profile: brandbook_editorial, density: low, required_checks: [motif_supports_message, quote_hierarchy, visual_rhythm_variation]}
  - {id: category_creation_evidence_wall, deck_job: category_creation, fixture_set: brand_manifesto_design_set, wireframes: [proof-stack.html, social-proof-wall.html, competitive-landscape.html], theme_profile: aiox_cockpit_dark, density: medium, required_checks: [evidence_credibility, no_decorative_stock_filler, source_visibility]}
  - {id: founder_story_proof_arc, deck_job: founder_story, fixture_set: brand_manifesto_design_set, wireframes: [mission-vision.html, case-study-proof.html, contact-next-step.html], theme_profile: luxury_minimal, density: low, required_checks: [emotional_temperature, visual_pacing, cta_visual_priority]}
  - {id: webinar_offer_stack, deck_job: webinar, fixture_set: webinar_sales_design_set, wireframes: [webinar-flow.html, objection-matrix.html, pricing-table.html], theme_profile: creator_webinar, density: medium, required_checks: [tension_to_offer_progression, objection_visibility, pricing_scan_path]}
  - {id: vsl_objection_resolution, deck_job: vsl, fixture_set: webinar_sales_design_set, wireframes: [objection-matrix.html, proof-stack.html, contact-next-step.html], theme_profile: product_launch_vivid, density: medium, required_checks: [testimonial_legibility, cta_visual_priority, claim_proof_distance]}
  - {id: sales_proposal_service_catalog, deck_job: sales_proposal, fixture_set: webinar_sales_design_set, wireframes: [service-catalog.html, pricing-table.html, team-credentials.html], theme_profile: enterprise_rfp, density: medium, required_checks: [offer_scan_path, table_legibility, credential_hierarchy]}
  - {id: academic_method_deck, deck_job: academic_talk, fixture_set: research_academic_design_set, wireframes: [data-lineage.html, experiment-grid.html, scatter-plot.html], theme_profile: academic_paper, density: high, required_checks: [figure_inspection_size, caption_separation, citation_visibility]}
  - {id: research_results_flow, deck_job: research_paper_deck, fixture_set: research_academic_design_set, wireframes: [sankey-flow.html, scatter-plot.html, traceability-matrix.html], theme_profile: data_analytics_lab, density: high, required_checks: [method_flow_readability, table_density_control, chart_label_legibility]}
  - {id: technical_method_appendix, deck_job: technical_method_deck, fixture_set: research_academic_design_set, wireframes: [traceability-matrix.html, compliance-grid.html, feature-matrix.html], theme_profile: academic_paper, density: appendix, required_checks: [appendix_readability, citation_visibility, hierarchy_under_zoom_out]}
  - {id: design_system_audit_components, deck_job: design_system_audit, fixture_set: executive_strategy_design_set, wireframes: [design-system-audit.html, brand-principles.html, feature-matrix.html], theme_profile: redpine_operational, density: high, required_checks: [component_state_visibility, semantic_status_tokens, accessibility_signal]}
  - {id: incident_postmortem_timeline, deck_job: incident_postmortem, fixture_set: executive_strategy_design_set, wireframes: [incident-timeline.html, risk-heatmap.html, responsibility-matrix.html], theme_profile: cyber_security_dark, density: high, required_checks: [timeline_readability, severity_color_redundancy, action_owner_clarity]}
  - {id: hiring_onboarding_scorecard, deck_job: hiring_onboarding, fixture_set: executive_strategy_design_set, wireframes: [hiring-scorecard.html, team-credentials.html, roadmap-status.html], theme_profile: education_workshop, density: medium, required_checks: [scorecard_legibility, role_hierarchy, onboarding_sequence]}
  - {id: workshop_canvas_facilitation, deck_job: workshop_facilitation, fixture_set: brand_manifesto_design_set, wireframes: [workshop-canvas.html, agenda-timeline.html, table-of-contents.html], theme_profile: education_workshop, density: medium, required_checks: [facilitation_affordance, section_navigation, participant_task_clarity]}
  - {id: product_launch_calendar, deck_job: product_launch, fixture_set: executive_strategy_design_set, wireframes: [launch-calendar.html, roadmap-status.html, social-proof-wall.html], theme_profile: product_launch_vivid, density: medium, required_checks: [date_grid_legibility, launch_phase_clarity, proof_wall_balance]}
  - {id: qbr_status_dashboard, deck_job: qbr_operating_review, fixture_set: executive_strategy_design_set, wireframes: [dashboard-grid.html, roadmap-status.html, risk-heatmap.html], theme_profile: redpine_operational, density: high, required_checks: [status_row_scan, metric_grouping, risk_priority_visibility]}
  - {id: compliance_readiness_grid, deck_job: compliance_review, fixture_set: executive_strategy_design_set, wireframes: [compliance-grid.html, traceability-matrix.html, responsibility-matrix.html], theme_profile: legal_compliance, density: high, required_checks: [control_id_visibility, status_redundancy, owner_column_readability]}
  - {id: survey_insight_story, deck_job: survey_report, fixture_set: research_academic_design_set, wireframes: [survey-results.html, persona-fit-matrix.html, quote-evidence-panel.html], theme_profile: data_analytics_lab, density: medium, required_checks: [sample_size_visibility, quote_balance, insight_hierarchy]}
  - {id: portfolio_allocation_decision, deck_job: portfolio_review, fixture_set: executive_strategy_design_set, wireframes: [portfolio-allocation.html, decision-options.html, value-chain.html], theme_profile: boardroom_graphite, density: high, required_checks: [allocation_label_fit, option_tradeoff_clarity, decision_highlight]}
  - {id: architecture_tradeoff_decision, deck_job: architecture_decision, fixture_set: product_demo_design_set, wireframes: [architecture-tradeoff-table.html, technical-architecture.html, decision-tree.html], theme_profile: technical_blueprint, density: high, required_checks: [tradeoff_columns_fit, decision_path_visibility, diagram_label_hierarchy]}
  - {id: market_landscape_positioning, deck_job: market_landscape, fixture_set: executive_strategy_design_set, wireframes: [competitive-landscape.html, scatter-plot.html, brand-principles.html], theme_profile: consulting_midnight, density: medium, required_checks: [axis_label_legibility, quadrant_meaning, positioning_claim_visibility]}
  - {id: roadmap_dependency_map, deck_job: roadmap_planning, fixture_set: executive_strategy_design_set, wireframes: [dependency-map.html, roadmap-decision.html, launch-calendar.html], theme_profile: enterprise_rfp, density: high, required_checks: [dependency_edge_readability, milestone_grouping, decision_gate_visibility]}
  - {id: org_value_chain_strategy, deck_job: operating_model, fixture_set: executive_strategy_design_set, wireframes: [org-chart.html, value-chain.html, responsibility-matrix.html], theme_profile: consulting_midnight, density: high, required_checks: [org_depth_fit, value_chain_flow, raci_cell_legibility]}
  - {id: proof_case_study_wall, deck_job: customer_case_study, fixture_set: webinar_sales_design_set, wireframes: [case-study-proof.html, proof-stack.html, social-proof-wall.html], theme_profile: founder_pitch_light, density: medium, required_checks: [before_after_clarity, proof_specificity, testimonial_legibility]}
  - {id: final_contact_next_step, deck_job: proposal_close, fixture_set: webinar_sales_design_set, wireframes: [contact-next-step.html, closing-card.html, table-of-contents.html], theme_profile: product_saas_clean, density: low, required_checks: [cta_visual_priority, contact_legibility, next_step_specificity]}

release_policy:
  pass_if:
    - at_least_30_fixture_cases_defined
    - every_case_has_deck_job_fixture_set_wireframes_theme_density_checks
    - all_required_review_roles_mapped_in_rendered_design_fixture_set
    - no_case_uses_generic_visual_without_proof_or_function
  block_if:
    - fixture_count_below_reference_bar
    - only_one_density_level
    - fewer_than_8_theme_profiles
    - missing_key_slide_roles
```


## Referência: references/source/templates/eval/rendered-design-fixture-set.yaml

```yaml
version: 1
name: rendered-design-fixture-set
purpose: >
  Fixture routing for rendered design evaluation. Use this to decide which
  wireframes/key slides must be previewed or screenshot-reviewed before claiming
  high design quality.

fixture_contract:
  required_inputs:
    - deck_job
    - selected_theme
    - selected_brand_or_template_manifest
    - slide_function_map
    - rendered_key_slides
  required_outputs:
    - key-slide-render-review.yaml
    - visual-regression-checklist.yaml
    - visual_patch_list
    - final_render_verdict

design_fixture_sets:
  - id: executive_strategy_design_set
    deck_jobs:
      - board_update
      - strategy_recommendation
      - benchmark_analysis
    required_wireframes:
      - executive-summary.html
      - benchmark-matrix.html
      - decision-options.html
      - roadmap-decision.html
      - risk-heatmap.html
    dominant_checks:
      - action_title_scan_path
      - dense_table_readability
      - chart_label_legibility
      - source_line_fit
      - visual_hierarchy_under_zoom_out

  - id: product_demo_design_set
    deck_jobs:
      - product_overview
      - api_demo
      - technical_demo
    required_wireframes:
      - api-request-response.html
      - code-explanation.html
      - screen-sequence.html
      - technical-architecture.html
      - service-catalog.html
    dominant_checks:
      - code_text_fit
      - interface_crop_relevance
      - diagram_node_readability
      - provider_badge_spacing
      - demo_flow_continuity

  - id: brand_manifesto_design_set
    deck_jobs:
      - brand_manifesto
      - category_creation
      - founder_story
    required_wireframes:
      - brand-principles.html
      - mission-vision.html
      - proof-stack.html
      - quote-evidence-panel.html
      - social-proof-wall.html
    dominant_checks:
      - motif_supports_message
      - quote_hierarchy
      - evidence_credibility
      - visual_rhythm_variation
      - no_decorative_stock_filler

  - id: webinar_sales_design_set
    deck_jobs:
      - webinar
      - vsl
      - offer_presentation
    required_wireframes:
      - webinar-flow.html
      - objection-matrix.html
      - pricing-table.html
      - case-study-proof.html
      - contact-next-step.html
    dominant_checks:
      - tension_to_offer_progression
      - objection_visibility
      - pricing_scan_path
      - testimonial_legibility
      - cta_visual_priority

  - id: research_academic_design_set
    deck_jobs:
      - academic_talk
      - research_paper_deck
      - technical_method_deck
    required_wireframes:
      - data-lineage.html
      - experiment-grid.html
      - scatter-plot.html
      - traceability-matrix.html
      - sankey-flow.html
    dominant_checks:
      - figure_inspection_size
      - caption_separation
      - method_flow_readability
      - table_density_control
      - citation_or_source_visibility

score_mapping:
  visual_layout_quality__rendered_visual_quality:
    85_89: "Contracts exist and at least key-slide review is documented."
    90_94: "Fixture set selected, key slides reviewed, and patch list produced."
    95_97: "Multiple fixture sets have rendered previews with before/after visual debt closure."
    98_100: "Automated screenshot regression exists across fixture sets and themes."
```


## Referência: references/source/templates/eval/rendered-eval.yaml

```yaml
version: 1
rendered_eval:
  id: multimodal_rendered_slide_evaluation
  pick_when:
    - Key slides have been rendered as images or HTML screenshots.
    - User asks why a deck feels weak, ugly, confusing, or below benchmark quality.
    - Final artifact needs evidence that narrative and visual execution survived rendering.
  absorbed_from:
    - PPTAgent/pptagent/ppteval.py
    - PPTAgent/pptagent/prompts/ppteval
    - powerpoint-skill/check_overlaps.py
  inputs:
    - rendered_slide_images
    - deck_spec
    - story_arc
    - audience
  outputs:
    - slide_descriptions
    - category_scores
    - overall_score
    - failure_modes
    - revision_actions

evaluation_categories:
  - id: vision
    name: Visual appeal and rendered design
    scale: 1-5
    score_5: Harmonious, engaging, readable, and visually supports the message.
    score_3: Adequate but generic, with minor hierarchy or composition weaknesses.
    score_1: Unappealing, cluttered, broken, or visually confusing.
  - id: content
    name: Content clarity and slide focus
    scale: 1-5
    score_5: One clear focus; text and visuals complement each other.
    score_3: Mostly understandable but contains extra or weakly connected material.
    score_1: Unclear focus, missing context, or text/visual mismatch.
  - id: logic
    name: Narrative flow and coherence
    scale: 1-5
    score_5: Slide sequence feels organized, complete, and persuasive.
    score_3: Flow is followable but transitions or proof are thin.
    score_1: Sequence feels disconnected, repetitive, or unsupported.
  - id: technical_render
    name: Export and layout integrity
    scale: 1-5
    score_5: No clipping, overlap, illegible text, broken media, or unsafe margins.
    score_3: Minor render issues that do not block comprehension.
    score_1: Render artifacts materially damage the slide.

process:
  - render_or_collect_slide_images
  - describe_each_slide_content
  - describe_each_slide_style
  - score_each_category
  - average_category_scores
  - identify_lowest_category_per_slide
  - convert_failures_into_revision_actions
  - rerun_eval_for_changed_key_slides

blockers:
  - key_slide_vision_score_below_4
  - key_slide_content_score_below_4
  - key_slide_logic_score_below_4
  - any_slide_technical_render_score_below_4
  - overall_score_below_4_for_final_delivery

cache_contract:
  file_name: rendered-eval.json
  required_fields:
    - slide_id
    - content_description
    - style_description
    - scores
    - revision_actions
  rules:
    - Cache is invalidated when slide image or deck spec changes.
    - Final QA report must include category averages and unresolved blockers.
```


## Referência: references/source/templates/import/document-extraction.yaml

```yaml
version: 1
import_pipelines:
  - id: structured_document_extraction
    pick_when:
      - Source material is a Markdown, PDF, DOCX, PPTX, transcript, article, report, or process log.
      - User wants a deck from existing content rather than from a short prompt.
    inputs:
      - source_document
      - image_dir
      - objective
      - audience
    steps:
      - normalize_to_markdown
      - detect_document_language
      - build_heading_tree
      - split_by_semantic_top_level_headings
      - extract_sections_and_subsections
      - extract_metadata_per_section
      - generate_section_summaries
      - caption_images_and_tables
      - merge_metadata
      - link_media_to_sections
      - create_claim_evidence_inventory
    outputs:
      - document_tree
      - merged_metadata
      - sections
      - subsection_inventory
      - media_inventory
      - table_inventory
      - claim_evidence_inventory
    absorbed_from:
      - PPTAgent/pptagent/document/document.py
      - PPTAgent/pptagent/roles/doc_extractor.yaml
      - PPTAgent/pptagent/prompts/document

section_contract:
  required_fields:
    - title
    - summary
    - content
    - metadata
    - markdown_content
  subsection_fields:
    - title
    - content
  rules:
    - Preserve original valid text; do not summarize away evidence during extraction.
    - Merge logical paragraphs into subsections, but do not split paragraphs arbitrarily.
    - Generate subsection titles of five words or fewer.
    - Section summary must stay under 100 words.

media_contract:
  image_caption:
    format: "<type>:<description>"
    max_words: 50
    allowed_types:
      - Table
      - Chart
      - Diagram
      - Banner
      - Background
      - Icon
      - Logo
      - Picture
  table_caption:
    prefix: "Table:"
    max_words: 50
  rules:
    - Prioritize actual image or table content over nearby unreliable chunks.
    - Validate media path exists before referencing it in deck spec.
    - Missing media blocks final render unless an explicit fallback is declared.

metadata_rules:
  - Extract only explicit metadata.
  - Merge duplicate or inconsistent metadata into one coherent dictionary.
  - Do not confuse dataset metadata with document metadata.

deck_synthesis_rules:
  - Document order is input, not destiny.
  - Claims, evidence, and media must be mapped to slide functions before drafting.
  - Weak source sections may become appendix, not core story.
```


## Referência: references/source/templates/import/induced-layout-packs.yaml

```yaml
version: 1
import_pipelines:
  - id: induced_layout_pack_selection
    pick_when:
      - A deck needs style/layout induction from existing presentation templates.
      - User provides a reference PPTX, academic deck, institutional template, or technical report deck.
      - The generator must choose among template families instead of one generic layout library.
    inputs:
      - deck_job
      - audience
      - source_template_family
      - media_inventory
      - slide_function_map
    steps:
      - identify_template_pack_candidate
      - inspect_layout_count_and_media_stats
      - map_pack_to_deck_job
      - choose_slide_layouts_by_function
      - bind_media_area_expectations
      - enforce_suggested_character_limits
      - produce_pack_selection_report
    outputs:
      - selected_pack
      - compatible_slide_functions
      - media_area_policy
      - layout_selection_report
    absorbed_from:
      - PPTAgent/pptagent/templates/beamer/slide_induction.json
      - PPTAgent/pptagent/templates/cip/slide_induction.json
      - PPTAgent/pptagent/templates/default/slide_induction.json
      - PPTAgent/pptagent/templates/hit/slide_induction.json
      - PPTAgent/pptagent/templates/thu/slide_induction.json
      - PPTAgent/pptagent/templates/ucas/slide_induction.json
      - PPTAgent/pptagent/templates/*/image_stats.json

packs:
  - id: pptagent_beamer
    layout_count: 8
    best_for:
      - academic_talk
      - technical_lecture
      - theorem_or_mechanism_explanation
    media_profile:
      dominant_media: diagram
      typical_relative_area_pct: 34
      guidance: Use for slides where a single technical diagram needs breathing room.
    avoid_when:
      - commercial_pitch
      - image_heavy_storytelling

  - id: pptagent_cip
    layout_count: 9
    best_for:
      - research_method_deck
      - benchmark_explanation
      - system_pipeline
      - eval_results
    media_profile:
      dominant_media:
        - flowchart
        - benchmark_chart
        - heatmap
      typical_relative_area_pct: 34-38
      guidance: Use for method/process/result slides with technical evidence.
    avoid_when:
      - low_context_executive_summary

  - id: pptagent_default
    layout_count: 9
    best_for:
      - general_source_deck
      - cultural_or_historical_narrative
      - mixed_photo_and_diagram_story
    media_profile:
      dominant_media:
        - picture
        - diagram
      typical_relative_area_pct: 23-47
      guidance: Use only when the deck benefits from varied media storytelling.
    avoid_when:
      - strict_b2b_product_benchmark
      - data_dense_financial_deck

  - id: pptagent_hit
    layout_count: 10
    best_for:
      - engineering_presentation
      - institutional_technical_deck
      - layout_training_or_template_demo
    media_profile:
      dominant_media:
        - diagram
        - layout_grid
      typical_relative_area_pct: 34-56
      guidance: Use when one large technical visual anchors the slide.
    avoid_when:
      - highly_editorial_brand_deck

  - id: pptagent_thu
    layout_count: 10
    best_for:
      - university_research_deck
      - academic_defense
      - technical_framework_deck
    media_profile:
      dominant_media:
        - vector_diagram
        - layout_preview
      typical_relative_area_pct: 34-53
      guidance: Use for academically credible, restrained technical explanation.
    avoid_when:
      - high_emotion_sales_webinar

  - id: pptagent_ucas
    layout_count: 9
    best_for:
      - design_system_explanation
      - theme_palette_or_visual_identity_deck
      - tool_interface_walkthrough
    media_profile:
      dominant_media:
        - interface_screenshot
        - palette_diagram
      typical_relative_area_pct: 29
      guidance: Use when screenshots or UI configuration are the evidence.
    avoid_when:
      - text_only_strategy_deck

selection_rules:
  - Pick a pack for its evidence and media behavior, not its aesthetic alone.
  - A pack may influence layout rhythm without overriding the deck narrative arc.
  - If no pack matches the audience and job, fall back to `slide/function-library.yaml`.
  - Pack choice must appear in the deck package when a reference template is used.
  - Do not copy source template assets; extract reusable behavior and constraints.
```


## Referência: references/source/templates/import/pptx-template-manifest.yaml

```yaml
version: 1
source_principle: >
  Importing a PPTX template means extracting reusable behavior, constraints,
  assets, and style metadata. It does not mean copying every arbitrary shape
  into a new visual system or trusting screenshots as editable output.
absorbed_from:
  - ../../../../../../bench/ppt-master/skills/ppt-master/scripts/template_import/manifest.py

import_pipelines:
  - id: pptx_template_manifest_import
    pick_when:
      - User provides an existing PowerPoint template or brand deck.
      - A deck must match a client template while keeping slide output editable.
      - A benchmark project needs to learn placeholder geometry, theme fonts, or media behavior.
    inputs:
      - pptx_path
      - output_workspace
      - optional_reference_images
      - target_deck_job
    outputs:
      - manifest.json
      - summary.md
      - assets/
      - template-import-report.yaml
    steps:
      - read_presentation_package
      - extract_slide_size
      - extract_theme_fonts_and_colors
      - resolve_master_layout_slide_inheritance
      - extract_backgrounds
      - extract_media_assets
      - extract_placeholders
      - extract_text_samples
      - classify_page_type
      - write_manifest_and_summary

manifest_contract:
  presentation:
    slide_size:
      width_emu: 0
      height_emu: 0
      aspect_ratio: ""
    theme:
      fonts: []
      colors: []
    asset_dir: "assets"
  slides:
    - index: 1
      slide_path: "ppt/slides/slide1.xml"
      layout_path: ""
      master_path: ""
      page_type: "cover | toc | chapter | content | thanks | contact | unknown"
      background:
        source: "slide | layout | master | none"
        asset_id: ""
      text_count: 0
      shape_count: 0
      image_assets: []
      text_samples: []
      placeholders: []
  layouts:
    - path: ""
      name: ""
      placeholder_count: 0
  masters:
    - path: ""
      name: ""

placeholder_contract:
  fields:
    - name: placeholder_type
      examples: [title, body, picture, table, chart, footer, date, slide_number]
    - name: idx
      description: Original placeholder index when present.
    - name: geometry
      required_keys: [x, y, width, height]
    - name: orientation
      examples: [horizontal, vertical, square]
    - name: text_style
      required_keys: [font_family, font_size, bold, italic, color]

page_type_keywords:
  cover: [title, subtitle, hero, portada, capa]
  toc: [agenda, contents, sumario, índice, indice, table_of_contents]
  chapter: [section, chapter, divider, separador, parte]
  thanks: [thanks, thank_you, obrigado, obrigada]
  contact: [contact, email, website, telefone, phone]
  content: [content, body, default]

quality_rules:
  - Preserve source inheritance: slide overrides layout; layout overrides master.
  - Extract assets into a sanitized local asset directory with stable ids.
  - Keep screenshots and SVG exports as references, not as the main editable representation.
  - Do not claim template fidelity until at least one imported layout is rendered and compared.
  - If placeholder geometry is missing, mark the layout as partial and route to manual design reconstruction.
  - If page type is unknown, classify by actual slide function during deck planning instead of guessing from filename only.

template_import_report:
  template_import_report:
    source_file: ""
    status: "pass | partial | fail"
    slide_size: ""
    theme_fonts_detected: []
    theme_colors_detected: []
    reusable_assets: 0
    reusable_layouts: 0
    partial_layouts: []
    unsupported_features: []
    recommended_use:
      - ""
```


## Referência: references/source/templates/import/source-deck-fixtures.yaml

```yaml
version: 1
name: source-deck-fixtures
purpose: >
  Reference fixture packs for learning deck/template behavior without requiring
  the original benchmark repositories at runtime. Use these packs when a user
  asks to match, import, or absorb a template family, brand deck, academic deck,
  consulting deck, product deck, or technical slide system.

scoring_relevance:
  template_import_replication__template_manifest: >
    Each fixture defines the minimum manifest fields that must be extracted or
    synthesized before claiming template coverage.
  template_import_replication__brand_fidelity: >
    Each fixture records non-color visual language, component behavior, density,
    media policy, and failure modes.
  template_import_replication__template_selection_logic: >
    Each fixture maps slide functions to layout families and rejection logic.

fixture_contract:
  required_fields:
    - source_family
    - best_for
    - manifest_required
    - visual_dna
    - layout_families
    - slide_function_fit
    - density_policy
    - theme_tokens_required
    - rendered_checks
    - avoid_when

fixtures:
  - id: ppt_master_consulting_pack
    source_family: ppt-master
    best_for:
      - board_update
      - strategy_recommendation
      - operating_review
      - executive_benchmark
    manifest_required:
      - master_layouts
      - placeholder_geometry
      - native_chart_regions
      - table_regions
      - section_divider_behavior
      - footer_provenance_slots
    visual_dna:
      non_color_traits:
        - precise grid with strong left/right alignment
        - action-title hierarchy before body detail
        - native editable shapes instead of flattened screenshots
      component_patterns:
        - executive_header
        - metric_strip
        - comparison_table
        - decision_panel
        - footnote_source_line
    layout_families:
      - decision_one_page
      - kpi_waterfall
      - side_by_side_options
      - appendix_table
    slide_function_fit:
      recommendation: decision_one_page
      proof: kpi_waterfall
      comparison: side_by_side_options
      appendix: appendix_table
    density_policy: high executive density allowed only with strict hierarchy and source line.
    theme_tokens_required:
      - table_border
      - chart_palette
      - muted_footnote
      - decision_accent
    rendered_checks:
      - table text remains readable at 16:9 screenshot scale
      - action title is the dominant scan-path anchor
      - source/provenance line does not collide with chart labels
    avoid_when:
      - emotional webinar story
      - image-led brand manifesto

  - id: ppt_master_template_import_pack
    source_family: ppt-master
    best_for:
      - imported_client_template
      - pptx_theme_replication
      - editable_powerpoint_delivery
    manifest_required:
      - slide_size
      - theme_fonts
      - theme_colors
      - layout_inheritance
      - media_assets
      - placeholder_geometry
      - page_type_classification
    visual_dna:
      non_color_traits:
        - source inheritance preserved from master to layout to slide
        - screenshots used as reference only
        - extracted placeholders remain editable
      component_patterns:
        - title_placeholder
        - body_placeholder
        - media_placeholder
        - footer_placeholder
    layout_families:
      - cover
      - section
      - content
      - chart
      - closing
    slide_function_fit:
      cover: cover
      transition: section
      evidence: chart
      explanation: content
      cta: closing
    density_policy: follow source placeholder limits unless design direction explicitly overrides.
    theme_tokens_required:
      - source_font_map
      - source_color_map
      - placeholder_spacing
      - export_fallback_fonts
    rendered_checks:
      - imported layout geometry matches reference within declared tolerance
      - no flattened reference image replaces editable content
      - fallback fonts do not reflow title/body
    avoid_when:
      - no reference deck or template exists

  - id: presentation_ai_theme_runtime_pack
    source_family: presentation-ai
    best_for:
      - web_editor_theme
      - brand_system_deck
      - multi_theme_template_library
    manifest_required:
      - theme_id
      - font_pair
      - palette_roles
      - chart_template_bindings
      - component_template_bindings
    visual_dna:
      non_color_traits:
        - theme drives charts, tables, shapes, and slide backgrounds
        - templates serialize examples for reliable generation
        - brand tone is encoded as reusable profile, not post-processing
      component_patterns:
        - theme_card
        - chart_module
        - outline_block
        - callout_block
    layout_families:
      - editorial_cover
      - insight_block
      - chart_story
      - visual_grid
    slide_function_fit:
      hook: editorial_cover
      insight: insight_block
      evidence: chart_story
      synthesis: visual_grid
    density_policy: medium density with theme-consistent blocks and generous rhythm.
    theme_tokens_required:
      - palette_roles
      - text_style_roles
      - chart_series_roles
      - surface_roles
    rendered_checks:
      - chart and table colors use theme roles
      - theme switch does not break contrast
      - all slide components resolve a style token
    avoid_when:
      - strict imported PPTX fidelity is the primary requirement

  - id: banana_slides_visual_polish_pack
    source_family: banana-slides
    best_for:
      - prompt_to_edit_design_iteration
      - visual_polish_pass
      - web_shareable_deck
    manifest_required:
      - prompt_revision_history
      - visual_patch_list
      - before_after_preview
      - export_policy
    visual_dna:
      non_color_traits:
        - strong visual defaults with immediate polish
        - prompt edits operate at deck and slide region levels
        - visual iteration is treated as normal workflow
      component_patterns:
        - hero_visual
        - dense_card_grid
        - quote_panel
        - polished_metric_card
    layout_families:
      - immersive_hero
      - card_wall
      - gallery
      - statement_slide
    slide_function_fit:
      hook: immersive_hero
      social_proof: card_wall
      inspiration: gallery
      key_claim: statement_slide
    density_policy: low to medium; visual polish degrades when slides become appendix tables.
    theme_tokens_required:
      - hero_overlay
      - card_surface
      - image_treatment
      - accent_glow_policy
    rendered_checks:
      - no generic decorative image replaces proof
      - prompt edit has visible before/after effect
      - slide still scans after visual embellishment
    avoid_when:
      - native editable PPTX is mandatory
      - legal/financial appendix density dominates

  - id: pptagent_academic_induction_pack
    source_family: PPTAgent
    best_for:
      - academic_talk
      - research_paper_deck
      - technical_method_deck
      - experiment_results
    manifest_required:
      - induced_layout_keys
      - media_area_statistics
      - suggested_character_limits
      - functional_element_roles
    visual_dna:
      non_color_traits:
        - layout selected from induced examples
        - media region size matches evidence type
        - text limits are explicit per layout
      component_patterns:
        - method_diagram
        - result_table
        - theorem_panel
        - figure_caption
    layout_families:
      - single_figure_explanation
      - method_pipeline
      - results_grid
      - related_work_matrix
    slide_function_fit:
      mechanism: method_pipeline
      proof: results_grid
      explanation: single_figure_explanation
      comparison: related_work_matrix
    density_policy: medium/high allowed when figure caption and takeaway remain separate.
    theme_tokens_required:
      - figure_caption
      - diagram_node
      - table_header
      - academic_footer
    rendered_checks:
      - figure is large enough to inspect
      - caption does not compete with action title
      - method arrows remain readable
    avoid_when:
      - brand-led sales deck

  - id: presenton_product_story_pack
    source_family: Presenton
    best_for:
      - product_overview
      - prompt_to_deck_app
      - self_hosted_ai_slide_tool
      - api_or_mcp_demo
    manifest_required:
      - template_schema
      - provider_routes
      - image_provider_policy
      - html_tailwind_regions
      - export_modes
    visual_dna:
      non_color_traits:
        - prompt-generated outline remains editable before final slides
        - HTML/Tailwind template maps content into defined regions
        - self-hosted/product capabilities are visible in the slide logic
      component_patterns:
        - product_capability_grid
        - provider_route_table
        - api_sequence
        - workflow_timeline
    layout_families:
      - product_capability_grid
      - integration_map
      - api_flow
      - before_after_workflow
    slide_function_fit:
      product_value: product_capability_grid
      architecture: integration_map
      demo: api_flow
      process: before_after_workflow
    density_policy: medium; favor editable region blocks over long text.
    theme_tokens_required:
      - code_mono
      - integration_accent
      - provider_badge
      - export_status
    rendered_checks:
      - code/API elements are legible
      - provider badges do not crowd primary message
      - outline-to-slide trace remains visible in package
    avoid_when:
      - pure academic defense

  - id: redpine_operational_design_pack
    source_family: redpine-ds
    best_for:
      - operational_dashboard_deck
      - incident_review
      - design_system_audit
      - governance_report
    manifest_required:
      - semantic_tokens
      - status_components
      - table_density
      - grid_rules
      - accessibility_contract
    visual_dna:
      non_color_traits:
        - square hairline containers
        - operational status rows with restrained accents
        - high-density evidence tables remain calm and readable
      component_patterns:
        - status_row
        - risk_panel
        - decision_panel
        - component_health_card
    layout_families:
      - status_dashboard
      - incident_timeline
      - risk_register
      - component_matrix
    slide_function_fit:
      status: status_dashboard
      diagnosis: incident_timeline
      risk: risk_register
      audit: component_matrix
    density_policy: high density allowed only with semantic grouping and grid discipline.
    theme_tokens_required:
      - status_positive
      - status_warning
      - status_negative
      - hairline_border
      - table_surface
    rendered_checks:
      - status colors are redundant with labels
      - dense rows retain line-height and contrast
      - hierarchy is not dependent on color alone
    avoid_when:
      - emotional brand launch

  - id: aiox_brandbook_editorial_pack
    source_family: aiox-brandbook
    best_for:
      - brand_manifesto
      - category_creation
      - strategic_narrative
      - premium_workshop
    manifest_required:
      - editorial_grid
      - mono_navigation_language
      - manifesto_quote_rules
      - evidence_wall_rules
      - hero_stage_rules
    visual_dna:
      non_color_traits:
        - dark cockpit editorial rhythm
        - bracket navigation and mono metadata
        - large narrative moments balanced by evidence strips
      component_patterns:
        - manifesto_quote
        - evidence_wall
        - hero_journey
        - pillar_grid
    layout_families:
      - cinematic_cover
      - manifesto_spread
      - evidence_wall
      - category_matrix
    slide_function_fit:
      hook: cinematic_cover
      belief_shift: manifesto_spread
      proof: evidence_wall
      category_design: category_matrix
    density_policy: low/medium on narrative slides; move detail to evidence wall or appendix.
    theme_tokens_required:
      - cockpit_background
      - mono_metadata
      - neon_accent
      - editorial_divider
    rendered_checks:
      - decorative HUD language does not obscure reading order
      - quote remains the visual center when used
      - evidence walls preserve source credibility
    avoid_when:
      - plain operational KPI report
```


## Referência: references/source/templates/import/template-import-regression-corpus.yaml

```yaml
version: 1
name: template-import-regression-corpus
purpose: >
  Corpus for validating template import, brand deck replication, and manifest
  completeness across the source families absorbed from the benchmark.

minimum_reference_bar:
  source_family_cases: 20
  required_source_families: [ppt-master, presentation-ai, PPTAgent, Presenton, banana-slides, Redpine, AIOX brandbook]
  manifest_sections:
    - source_reference
    - token_map
    - typography_system
    - grid_system
    - layout_families
    - component_patterns
    - chart_language
    - media_language
    - anti_patterns
    - rendered_comparison_policy

source_family_cases:
  - {id: ppt_master_consulting_layouts, source_family: ppt-master, use_for: [board_update, strategy_recommendation, executive_benchmark], expected_manifest: [slide_size, theme_fonts, native_chart_regions, table_regions, placeholder_geometry], fidelity_checks: [editable_shapes_preserved, action_title_hierarchy, source_line_fit]}
  - {id: ppt_master_chart_library, source_family: ppt-master, use_for: [financial_deck, benchmark_analysis, operating_review], expected_manifest: [chart_palette, chart_regions, label_policy, annotation_policy], fidelity_checks: [chart_editability, label_legibility, highlight_consistency]}
  - {id: ppt_master_image_type_templates, source_family: ppt-master, use_for: [hero_slide, visual_metaphor, proof_scene], expected_manifest: [image_type, text_overlay_policy, crop_policy, native_overlay_slots], fidelity_checks: [no_text_inside_generated_image, media_relevance, overlay_readability]}
  - {id: ppt_master_import_parser_contract, source_family: ppt-master, use_for: [imported_client_template, editable_powerpoint_delivery], expected_manifest: [layout_inheritance, media_assets, page_type_classification, fallback_fonts], fidelity_checks: [master_layout_inheritance, editable_placeholders, no_flattened_reference_image]}
  - {id: presentation_ai_theme_profiles, source_family: presentation-ai, use_for: [brand_system_deck, web_editor_theme, multi_theme_library], expected_manifest: [palette_roles, font_pair, component_bindings, chart_bindings], fidelity_checks: [theme_switch_contrast, chart_token_binding, component_token_resolution]}
  - {id: presentation_ai_template_serializer, source_family: presentation-ai, use_for: [template_example_prompting, outline_template_override], expected_manifest: [serialized_template_example, slot_schema, sample_content], fidelity_checks: [example_matches_slot_schema, selected_template_reason, rejected_runner_up_reason]}
  - {id: presentation_ai_chart_editor_modes, source_family: presentation-ai, use_for: [data_story, survey_report, analytics_deck], expected_manifest: [chart_data_mode, editor_fields, validation_rules], fidelity_checks: [data_shape_matches_chart, chart_theme_applied, label_fit]}
  - {id: pptagent_beamer_academic, source_family: PPTAgent, use_for: [academic_talk, theorem_explanation, technical_lecture], expected_manifest: [induced_layout_keys, media_area_stats, character_limits], fidelity_checks: [figure_size, caption_separation, title_claim_visibility]}
  - {id: pptagent_cip_method_results, source_family: PPTAgent, use_for: [research_method_deck, benchmark_method, eval_results], expected_manifest: [flowchart_slots, heatmap_slots, result_table_slots], fidelity_checks: [method_flow_readability, result_table_hierarchy, evidence_visibility]}
  - {id: pptagent_hit_engineering, source_family: PPTAgent, use_for: [engineering_update, system_pipeline, architecture_review], expected_manifest: [technical_diagram_slots, media_area_stats, label_constraints], fidelity_checks: [diagram_label_fit, line_weight_consistency, code_or_formula_legibility]}
  - {id: pptagent_ucas_design_system, source_family: PPTAgent, use_for: [design_system_audit, ui_walkthrough, palette_explanation], expected_manifest: [interface_screenshot_slots, palette_regions, component_grid], fidelity_checks: [screenshot_crop_relevance, palette_label_fit, component_state_visibility]}
  - {id: presenton_template_schema, source_family: Presenton, use_for: [prompt_to_deck_app, product_overview, self_hosted_ai_slide_tool], expected_manifest: [template_schema, html_tailwind_regions, export_modes], fidelity_checks: [region_schema_fit, outline_to_slide_trace, export_region_integrity]}
  - {id: presenton_provider_routes, source_family: Presenton, use_for: [api_demo, local_model_story, byok_capability], expected_manifest: [provider_routes, image_provider_policy, privacy_mode], fidelity_checks: [provider_badge_spacing, privacy_claim_visibility, route_table_legibility]}
  - {id: presenton_product_story, source_family: Presenton, use_for: [product_capability_grid, workflow_timeline, integration_map], expected_manifest: [capability_components, workflow_regions, integration_nodes], fidelity_checks: [capability_grouping, workflow_sequence, integration_node_hierarchy]}
  - {id: banana_prompt_to_edit_history, source_family: banana-slides, use_for: [visual_iteration, prompt_to_edit_polish, shareable_deck], expected_manifest: [prompt_revision_history, before_after_preview, visual_patch_list], fidelity_checks: [patch_scope_clear, before_after_visible, no_untracked_visual_drift]}
  - {id: banana_visual_polish_defaults, source_family: banana-slides, use_for: [hero_visual, polished_story, testimonial_deck], expected_manifest: [hero_overlay, card_surface, image_treatment], fidelity_checks: [visual_polish_without_obscuring_message, proof_media_relevance, hierarchy_preserved]}
  - {id: redpine_operational_dashboard, source_family: Redpine, use_for: [operational_dashboard, incident_review, governance_report], expected_manifest: [semantic_tokens, status_components, table_density, a11y_contract], fidelity_checks: [status_redundancy, dense_row_readability, hairline_grid_consistency]}
  - {id: redpine_component_audit, source_family: Redpine, use_for: [design_system_audit, component_manifest, accessibility_review], expected_manifest: [component_states, a11y_cards, status_rows], fidelity_checks: [component_state_visibility, a11y_signal_legibility, semantic_color_mapping]}
  - {id: aiox_editorial_cockpit, source_family: AIOX brandbook, use_for: [brand_manifesto, category_creation, strategic_narrative], expected_manifest: [editorial_grid, mono_navigation, evidence_wall, hero_stage_rules], fidelity_checks: [bracket_metadata_language, evidence_wall_credibility, dark_theme_contrast]}
  - {id: aiox_offer_story, source_family: AIOX brandbook, use_for: [offer_deck, founder_strategy, premium_workshop], expected_manifest: [offer_two_column_stack, problem_ticker_stage, proof_wall_rules], fidelity_checks: [offer_stack_hierarchy, problem_tension_visibility, proof_specificity]}

manifest_score_policy:
  score_85_89: "Manifest exists but covers only tokens/layouts or has weak render comparison."
  score_90_94: "Manifest covers source, tokens, typography, layout families, components, charts, media and anti-patterns."
  score_95_99: "Manifest is paired with source-family regression cases and rendered comparison policy."
  score_100: "Manifest corpus covers all required source families, sections, fidelity checks and local validation passes."
```


## Referência: references/source/templates/index.yaml

```yaml
version: 1
name: slide-creator-template-system
purpose: >
  Canonical self-contained template registry for narrative-first slide creation.
  The registry absorbs benchmark behavior from open-source slide systems without
  copying their UI or implementation.

selection_order:
  - deck_template
  - story_arc_contract
  - slide_function_template
  - slide_function_map_contract
  - design_direction_contract
  - visual_template
  - template_selection_report
  - theme_profile
  - render_lock
  - research_route
  - import_pipeline
  - runtime_job
  - job_state
  - source_of_truth_policy
  - rendered_eval
  - qa_gates

registries:
  deck:
    files:
      - deck/route-map.yaml
      - deck/copy-derived.yaml
      - deck/playbook-routing.yaml
    description: Complete roteiro templates by presentation job.
  slide:
    file: slide/function-library.yaml
    description: Slide-level structures by audience function.
  visual:
    files:
      - visual/charts-and-diagrams.yaml
      - visual/chart-data-contracts.yaml
      - visual/ai-image-type-routing.yaml
      - visual/composition-patterns.yaml
      - visual/design-mastery-contract.yaml
      - visual/brand-template-manifest.yaml
      - visual/brand-fidelity-playbooks.yaml
      - visual/design-mastery-report.yaml
      - visual/key-slide-render-review.yaml
      - visual/visual-regression-checklist.yaml
      - visual/layout-families.yaml
      - visual/media-layouts.yaml
      - visual/brand-system-patterns.yaml
      - visual/aiox-brandbook-deep-patterns.yaml
      - visual/redpine-deep-patterns.yaml
    description: Visual pattern grammar, layout families, media-fit rules.
  wireframes:
    files:
      - wireframes/agenda-timeline.html
      - wireframes/api-request-response.html
      - wireframes/architecture-tradeoff-table.html
      - wireframes/benchmark-matrix.html
      - wireframes/brand-principles.html
      - wireframes/business-challenges.html
      - wireframes/case-study-proof.html
      - wireframes/cohort-retention.html
      - wireframes/code-explanation.html
      - wireframes/compliance-grid.html
      - wireframes/contact-next-step.html
      - wireframes/competitive-landscape.html
      - wireframes/dashboard-grid.html
      - wireframes/data-lineage.html
      - wireframes/decision-options.html
      - wireframes/decision-tree.html
      - wireframes/dependency-map.html
      - wireframes/design-system-audit.html
      - wireframes/executive-summary.html
      - wireframes/experiment-grid.html
      - wireframes/feature-matrix.html
      - wireframes/financial-waterfall.html
      - wireframes/gallery.html
      - wireframes/harvey-balls-table.html
      - wireframes/hiring-scorecard.html
      - wireframes/incident-timeline.html
      - wireframes/launch-calendar.html
      - wireframes/maturity-ladder.html
      - wireframes/mechanism-map.html
      - wireframes/mission-vision.html
      - wireframes/moodboard-grid.html
      - wireframes/objection-matrix.html
      - wireframes/org-chart.html
      - wireframes/persona-fit-matrix.html
      - wireframes/portfolio-allocation.html
      - wireframes/pricing-table.html
      - wireframes/proof-stack.html
      - wireframes/quote-evidence-panel.html
      - wireframes/responsibility-matrix.html
      - wireframes/risk-heatmap.html
      - wireframes/roadmap-status.html
      - wireframes/roadmap-decision.html
      - wireframes/sankey-flow.html
      - wireframes/scatter-plot.html
      - wireframes/scoring-rubric.html
      - wireframes/screen-sequence.html
      - wireframes/service-catalog.html
      - wireframes/social-proof-wall.html
      - wireframes/survey-results.html
      - wireframes/table-of-contents.html
      - wireframes/team-credentials.html
      - wireframes/technical-architecture.html
      - wireframes/traceability-matrix.html
      - wireframes/unit-economics.html
      - wireframes/user-story-map.html
      - wireframes/value-chain.html
      - wireframes/webinar-flow.html
      - wireframes/workshop-canvas.html
    description: HTML-ready slide wireframes for high-use deck moments.
  theme:
    files:
      - theme/theme-tokens.yaml
      - theme/brand-systems.yaml
      - theme/design-philosophy-routing.yaml
    description: Theme tokens separated from slide structure.
  runtime:
    files:
      - runtime/story-arc-contract.yaml
      - runtime/narrative-regression-corpus.yaml
      - runtime/slide-function-map-contract.yaml
      - runtime/storyboard-render-bridge.yaml
      - runtime/narrative-design-moment-grammar.yaml
      - runtime/storyboard-edit-contract.yaml
      - runtime/design-direction-contract.yaml
      - runtime/workflow-modes.yaml
      - runtime/jobs.yaml
      - runtime/job-state.schema.yaml
      - runtime/render-lock.yaml
      - runtime/design-score-evidence.yaml
      - runtime/theme-runtime-snapshot-suite.yaml
      - runtime/speaker-notes-narration-contract.yaml
      - runtime/runtime-gap-absorption-corpus.yaml
      - runtime/delivery-package-contract.yaml
      - runtime/api-mcp-cli-contract.yaml
      - runtime/template-selection-report.yaml
      - runtime/source-of-truth-policy.yaml
      - runtime/edit-operations.yaml
      - runtime/import-template.yaml
      - runtime/diagram-rendering.yaml
      - runtime/manuscript-pipeline.yaml
      - runtime/html-to-pptx.yaml
      - runtime/export-contract.yaml
      - runtime/template-example-routing.yaml
      - runtime/trace-handoff.yaml
      - runtime/provider-routing.yaml
      - runtime/edit-history.yaml
    description: Generation, manuscript, edit, batch, import, prompt-to-edit, render, and export contracts.
  research:
    files:
      - research/source-routing.yaml
      - research/evidence-ledger.yaml
    description: Source, media, scholar, and local-file retrieval routes for evidence-backed slide creation.
  import:
    files:
      - import/document-extraction.yaml
      - import/induced-layout-packs.yaml
      - import/pptx-template-manifest.yaml
      - import/source-deck-fixtures.yaml
      - import/template-import-regression-corpus.yaml
    description: Structured extraction of documents, metadata, sections, claims, media, and tables.
  qa:
    files:
      - qa/narrative-gates.yaml
      - qa/visual-gates.yaml
      - qa/template-selection-gates.yaml
      - qa/copy-gates.yaml
      - qa/regression-fixtures.yaml
      - qa/pptx-technical-gates.yaml
      - qa/squad-quality-rubric.yaml
    description: Blockers, scoring, and regression checks.
  eval:
    files:
      - eval/rendered-eval.yaml
      - eval/rendered-design-fixture-set.yaml
      - eval/design-regression-corpus.yaml
    description: Rendered multimodal slide evaluation using vision/content/logic/technical-render categories.

bench_absorption:
  presenton:
    paths:
      - ../../../../../../bench/presenton/servers/nextjs/lib/compile-template-schema.ts
      - ../../../../../../bench/presenton/servers/nextjs/app/presentation-templates
    absorbed:
      - template_family_metadata
      - layout_schema
      - sample_data
      - prompt_to_edit_layout
      - template_import_pipeline
      - provider_capability_routing
      - local_model_download_state
      - schema_validation_before_save
      - source_of_truth_policy
  ppt_master:
    paths:
      - ../../../../../../bench/ppt-master/skills/ppt-master/templates/charts/charts_index.json
      - ../../../../../../bench/ppt-master/skills/ppt-master/templates/layouts/layouts_index.json
      - ../../../../../../bench/ppt-master/skills/ppt-master/templates/spec_lock_reference.md
      - ../../../../../../bench/ppt-master/skills/ppt-master/references/image-type-templates/_index.md
      - ../../../../../../bench/ppt-master/skills/ppt-master/scripts/template_import/manifest.py
    absorbed:
      - visual_selection_grammar
      - design_spec_vs_execution_lock
      - chart_layout_indexing
      - strict_forbidden_rules
      - ai_image_type_routing
      - pptx_template_manifest_import
      - render_lock_anti_drift
      - primary_modifier_visual_composition
      - rejected_runners_up_audit
      - brand_template_manifest_as_design_truth
      - rendered_design_regression_comparison
  pptagent:
    paths:
      - ../../../../../../bench/PPTAgent/pptagent/templates/default/slide_induction.json
      - ../../../../../../bench/PresentAgent-2/pptagent/roles/layout_selector.yaml
      - ../../../../../../bench/PPTAgent/pptagent/ppteval.py
      - ../../../../../../bench/PPTAgent/deeppresenter/roles/Planner.yaml
      - ../../../../../../bench/PPTAgent/deeppresenter/roles/Research.yaml
      - ../../../../../../bench/PPTAgent/deeppresenter/html2pptx/html2pptx.js
      - ../../../../../../bench/PPTAgent/pptagent/document/document.py
      - ../../../../../../bench/PPTAgent/pptagent/prompts/document
      - ../../../../../../bench/PPTAgent/pptagent/templates/beamer/slide_induction.json
      - ../../../../../../bench/PPTAgent/pptagent/templates/cip/slide_induction.json
      - ../../../../../../bench/PPTAgent/pptagent/templates/hit/slide_induction.json
      - ../../../../../../bench/PPTAgent/pptagent/templates/thu/slide_induction.json
      - ../../../../../../bench/PPTAgent/pptagent/templates/ucas/slide_induction.json
      - ../../../../../../bench/PPTAgent/pptagent/templates/*/image_stats.json
    absorbed:
      - induced_layout_elements
      - suggested_character_limits
      - media_fit_reasoning
      - functional_keys
      - multimodal_rendered_eval
      - manuscript_first_pipeline
      - html_to_pptx_render_contract
      - structured_document_extraction
      - induced_layout_pack_selection
      - media_area_statistics
  presentation_ai:
    paths:
      - ../../../../../../bench/presentation-ai/src/ai/tools/presentation/tools.ts
      - ../../../../../../bench/presentation-ai/src/lib/presentation/themes.ts
      - ../../../../../../bench/presentation-ai/src/constants/antv-templates.ts
      - ../../../../../../bench/presentation-ai/src/components/notebook/presentation/utils/template-serializer.ts
      - ../../../../../../bench/presentation-ai/src/components/notebook/presentation/utils/templates.tsx
      - ../../../../../../bench/presentation-ai/src/components/notebook/presentation/charts/chart-data-editor/types.ts
      - ../../../../../../bench/presentation-ai/src/components/notebook/presentation/charts/chart-data-editor/use-chart-editor.ts
    absorbed:
      - edit_operations
      - theme_profiles
      - scenario_audience_tone
      - visual_component_dsl
      - serialized_template_examples
      - outline_template_overrides
      - chart_data_mode_contracts
      - chart_editor_mode_mapping
      - edit_history_snapshot_semantics
  banana_slides:
    paths:
      - ../../../../../../bench/banana-slides/scripts/job_templates
      - ../../../../../../bench/banana-slides/skills/banana-cli/SKILL.md
    absorbed:
      - job_presets
      - job_state_progress_resume
      - reference_files
      - material_files
      - batch_generation
      - export_policy
      - editable_pptx_reverse_export
  powerpoint_skill:
    paths:
      - ../../../../../../bench/powerpoint-skill/powerpoint-slides/SKILL.md
      - ../../../../../../bench/powerpoint-skill/powerpoint-slides/scripts/check_overlaps.py
      - ../../../../../../bench/powerpoint-skill/powerpoint-slides/diagram-rendering.md
    absorbed:
      - visual_qa
      - overlap_boundary_checks
      - pptx_generation_constraints
      - pptx_technical_scoring
      - text_fit_and_math_safety
      - diagram_engine_routing
      - figure_extraction_policy
  slide_deck_ai:
    paths:
      - ../../../../../../bench/slide-deck-ai/src/slidedeckai/prompts/initial_template_v4_two_cols_img.txt
      - ../../../../../../bench/slide-deck-ai/src/slidedeckai/prompts/refinement_template_v4_two_cols_img.txt
    absorbed:
      - narrative_arc_prompting
      - structure_markers
      - table_process_icon_patterns
  presentagent_deepresearch:
    paths:
      - ../../../../../../bench/PresentAgent-2/DeepResearch/inference/prompt.py
      - ../../../../../../bench/PresentAgent-2/DeepResearch/inference/prompt_media.py
      - ../../../../../../bench/PresentAgent-2/DeepResearch/inference/file_tools
      - ../../../../../../bench/PresentAgent-2/DeepResearch/evaluation
    absorbed:
      - html_source_retrieval
      - motion_media_retrieval
      - scholar_and_benchmark_routing
      - local_file_retrieval
      - deep_research_evaluation_contract
      - evidence_ledger
  deeph:
    paths:
      - ../../../../../../bench/deepH/docs/AGENTS_AND_SPECS.md
      - ../../../../../../bench/deepH/docs/WORKFLOWS_AND_UNIVERSES.md
      - ../../../../../../bench/deepH/crews/reviewflow.yaml
    absorbed:
      - typed_handoffs
      - multiverse_review_synthesis
      - traceable_runtime_flows
      - focused_working_set_principle
      - process_regression_fixtures
      - edit_history_handoff_patterns
  sinkra_copy_squad:
    historical_sources:
      - copy_hormozi_offer_systems
      - copy_jon_benson_vsl_frameworks
      - copy_ry_schwartz_course_launch_frameworks
      - copy_mappings
      - pitch_deck_matrix
    independence_note: "Absorbed into deck/copy-derived.yaml; runtime must not require copy or pitch-deck squad files."
    absorbed:
      - grand_slam_offer_sequence
      - proof_promise_plan_argument
      - five_step_vsl_process
      - coaching_the_conversion_method
      - awareness_level_routing
      - proof_hierarchy
  redpine_ds:
    paths:
      - ../../../../apps/redpine-ds/src/design-system/tokens.json
      - ../../../../apps/redpine-ds/src/design-system/components.manifest.json
      - ../../../../apps/design/src/data/designs/redpine/DESIGN.md
    absorbed:
      - editorial_precision_theme
      - square_hairline_surface_system
      - component_status_and_a11y_cards
      - risk_incident_table_pattern
      - twelve_column_report_grid
      - semantic_palette_surface_stack
      - accessible_status_rows
      - decision_panels
  aiox_brandbook:
    paths:
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/README.md
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/slides/index.html
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/ui_kits/brandbook/README.md
    absorbed:
      - cockpit_dark_theme
      - four_column_hero_grid
      - manifesto_quote_slide
      - bordered_stat_strip
      - hud_pillar_cards
      - mono_bracket_navigation_language
      - editorial_book_spreads
      - evidence_wall
      - hero_journey_four_acts
      - problem_ticker_stage
      - offer_two_column_stack
      - pitch_page_header_metric_insight_components
      - category_creation_matrix
      - gate_driven_roadmap
  slides_creator_squad:
    historical_sources:
      - story-arc.schema.yaml
      - slide-function-map.schema.yaml
      - design-direction.schema.yaml
      - qa-rubric.yaml
      - qa-routing-table.yaml
      - design-philosophies.md
    independence_note: "Absorbed into bundled contracts; runtime must not require squad files or agents."
    absorbed:
      - workflow_mode_selection
      - deck_playbook_routing
      - story_arc_contract_with_beat_types
      - slide_function_map_audience_movement
      - design_direction_as_required_artifact
      - six_dimension_quality_rubric
      - killer_items_release_gate
      - corrective_action_routing_without_agents
      - twenty_design_philosophy_fallbacks

quality_target:
  minimum_score: 90
  excellent_score: 95
  block_if:
    - no_declared_deck_template
    - no_story_arc_contract_for_full_deck
    - no_slide_function_map_contract_for_full_deck
    - no_design_direction_contract_for_full_deck
    - no_declared_slide_function_template
    - no_visual_template_for_key_slides
    - no_reason_for_template_selection
    - no_rejected_runners_up_for_key_template_selection
    - no_render_lock_for_exportable_deck
    - no_job_state_for_cli_api_mcp_or_batch
    - unresolved_source_of_truth_conflict
    - repeated_layout_more_than_two_times
    - no_qa_gate_report
    - any_killer_item_detected
    - slide_function_is_explain_topic
    - missing_audience_movement
    - design_direction_applied_as_skin
    - research_required_but_no_source_route
    - high_stakes_claim_without_evidence_ledger
    - rendered_key_slide_not_evaluated
    - export_claimed_without_verified_output
    - known_failure_without_regression_fixture
    - pptx_requested_without_technical_gate
    - provider_required_but_not_declared
```


## Referência: references/source/templates/qa/copy-gates.yaml

```yaml
version: 1
gates:
  - id: offer_clarity_gate
    gate: The offer is legible as outcome, mechanism, deliverables, guarantee, and next step.
    blocks_if:
      - Offer is only a feature list.
      - CTA is ambiguous.
      - Guarantee or risk reversal is missing for a paid offer.
    pass_if:
      - Buyer can answer what they get, why it works, why now, and what to do next.
    score_weight: 15
    absorbed_from: [copy_hormozi_offer_systems]

  - id: ethical_persuasion_gate
    gate: Persuasion is strong without fake urgency or manipulation.
    blocks_if:
      - Scarcity is not tied to real capacity, time, cohort, or bonus constraint.
      - Pain is amplified without empathy or solution path.
      - Claims exceed what evidence supports.
    pass_if:
      - Urgency, proof, and promise are honest and decision-helpful.
    score_weight: 15
    absorbed_from: [copy_jon_benson_vsl_frameworks, copy_hormozi_offer_systems]

  - id: avatar_language_gate
    gate: The deck uses the prospect's actual language where possible.
    blocks_if:
      - Copy uses generic marketing language while user supplied calls, DMs, surveys, or notes.
      - Objections are written from seller perspective only.
    pass_if:
      - Key slides mirror audience language, stage of awareness, and decision criteria.
    score_weight: 10
    absorbed_from: [copy_ry_schwartz_course_launch_frameworks, copy_mappings]

  - id: objection_gate
    gate: Objections are handled before the close.
    blocks_if:
      - Price, trust, time, ability, fit, or risk objections are ignored.
      - Objection slide argues instead of facilitating decision.
    pass_if:
      - Each major objection has a reframe, proof, or fit filter.
    score_weight: 10
    absorbed_from: [copy_ry_schwartz_course_launch_frameworks]
```


## Referência: references/source/templates/qa/narrative-gates.yaml

```yaml
version: 1
gates:
  - id: belief_shift_gate
    gate: The deck changes what the audience believes.
    blocks_if:
      - Audience current belief is not stated.
      - Desired belief is not stated.
      - Slides list topics instead of moving belief.
    pass_if:
      - Current belief, desired belief, and proof path are explicit.
      - Every section advances the belief shift.
    score_weight: 20
    absorbed_from: [slide-deck-ai]
  - id: slide_function_gate
    gate: Every slide has one primary job.
    blocks_if:
      - A slide has more than one primary function.
      - Two adjacent slides repeat the same function without escalation.
    pass_if:
      - Every slide declares function, template, and reason.
    score_weight: 15
    absorbed_from: [slide-creator, ppt-master]
  - id: action_title_gate
    gate: Titles are claims, not labels.
    blocks_if:
      - Title is a generic noun phrase.
      - Title does not communicate the slide's answer.
    pass_if:
      - Every key slide title can stand alone as an executive summary.
    score_weight: 10
    absorbed_from: [powerpoint-skill]
  - id: proof_gate
    gate: Important claims are supported.
    blocks_if:
      - Claim has no source, artifact, example, demo, or assumption label.
    pass_if:
      - Key claims map to evidence or are labeled as assumptions.
    score_weight: 15
    absorbed_from: [ppt-master, slide-deck-ai]
  - id: decision_gate
    gate: Decision slides make the ask explicit.
    blocks_if:
      - Options are presented without recommendation.
      - Tradeoff is hidden.
    pass_if:
      - Recommendation, alternatives, tradeoff, and next action are visible.
    score_weight: 10
    absorbed_from: [ppt-master]
```


## Referência: references/source/templates/qa/pptx-technical-gates.yaml

```yaml
version: 1
gates:
  - id: pptx_boundary_and_overlap_gate
    gate: PPTX elements must not overlap, clip, or violate safe margins.
    blocks_if:
      - Element bottom edge exceeds slide safe area.
      - Text visually overflows its box.
      - Card title overlaps card body.
      - Elements overlap without intentional grouping.
      - More than two consecutive slides repeat the same layout.
    pass_if:
      - Rendered preview or PPTX structural checker reports no critical overlap, clipping, or boundary issue.
    score_weight: 15
    absorbed_from:
      - powerpoint-skill/check_overlaps.py
      - powerpoint-skill/SKILL.md

  - id: pptx_text_fit_gate
    gate: Text boxes must use shrink-safe behavior and disciplined spacing.
    blocks_if:
      - A text box expands shape instead of shrinking text.
      - Body copy exceeds four short lines per inch of available body height.
      - Element below another starts less than 0.1in after previous bottom.
      - Long card title wraps into body region.
    pass_if:
      - Text fit is explicitly handled by shrink or slide split.
    score_weight: 10
    absorbed_from:
      - powerpoint-skill/SKILL.md

  - id: pptx_math_and_diagram_gate
    gate: Math, diagrams, and extracted figures must be PowerPoint-safe.
    blocks_if:
      - Math notation is represented as Unicode approximation instead of native math or image.
      - Residual math placeholders remain in PPTX XML.
      - Diagram uses default engine colors instead of deck theme.
      - Diagram labels are unreadable or nodes overlap.
      - Extracted figure lacks attribution.
    pass_if:
      - Math, diagrams, and figures are readable, attributed, and theme-consistent.
    score_weight: 10
    absorbed_from:
      - powerpoint-skill/SKILL.md
      - powerpoint-skill/references/themes.md

  - id: pptx_rendered_density_gate
    gate: Rendered content should occupy enough visual area.
    blocks_if:
      - Visible content occupies less than 75% of the area below title bar on a content slide.
      - Text-only slides exceed 20% of the deck without deliberate pacing reason.
      - Cards visually contain too little content and feel empty.
    pass_if:
      - Rendered slide feels intentionally composed, not sparse or accidentally empty.
    score_weight: 8
    absorbed_from:
      - powerpoint-skill/SKILL.md
      - powerpoint-skill/references/themes.md

technical_scoring:
  start_score: 100
  deliver_threshold: 90
  warning_threshold: 80
  deductions:
    - issue: script_or_export_failure
      severity: critical
      points: 100
    - issue: element_overlap
      severity: critical
      points: 15
      cap: 45
    - issue: bottom_edge_clipping
      severity: critical
      points: 15
      cap: 45
    - issue: formula_missing_or_corrupted
      severity: critical
      points: 20
      cap: 60
    - issue: visual_blank_space
      severity: major
      points: 8
    - issue: diagram_theme_mismatch
      severity: major
      points: 8
    - issue: missing_figure_attribution
      severity: major
      points: 5
    - issue: tight_margin
      severity: minor
      points: 2
```


## Referência: references/source/templates/qa/regression-fixtures.yaml

```yaml
version: 1
regression_fixtures:
  id: deck_process_regression_suite
  pick_when:
    - A previous slide process produced weak narrative, weak design, repeated layouts, bad export, or unsupported claims.
    - The skill is being improved and needs forward tests.
    - User asks to make the process 100% shareable and reliable.
  absorbed_from:
    - powerpoint-skill/check_overlaps.py
    - PPTAgent/ppteval
    - deepH/reviewflow
    - slide-deck-ai/smoke-test-baseline
  fixture_types:
    - id: narrative_failure_fixture
      catches:
        - outline_dump
        - no_belief_shift
        - duplicate_slide_function
        - weak_cta
      required_inputs:
        - rough_topic
        - audience
        - desired_outcome
      pass_if:
        - story_arc_exists_before_deck_spec
        - every_slide_has_function
        - key_slides_pass_narrative_gate

    - id: design_failure_fixture
      catches:
        - repeated_layout
        - dense_text
        - weak_hierarchy
        - decorative_media
      required_inputs:
        - deck_spec
        - visual_template_selection
      pass_if:
        - no_more_than_two_consecutive_same_layouts
        - key_slides_have_visual_job
        - media_has_proof_demo_or_clarity_reason

    - id: research_failure_fixture
      catches:
        - generic_sources
        - unsupported_claims
        - stale_or_low_confidence_fact
        - media_found_but_not_useful
      required_inputs:
        - source_route_report
        - evidence_ledger
      pass_if:
        - high_stakes_claims_have_ledger_rows
        - source_routes_match_evidence_type
        - assumptions_are_labeled

    - id: render_failure_fixture
      catches:
        - overlap
        - clipping
        - illegible_text
        - broken_export
      required_inputs:
        - rendered_slide_images
        - export_report
      pass_if:
        - rendered_eval_scores_are_above_threshold
        - export_output_path_verified
        - preview_artifact_exists_or_reason_reported

    - id: template_selection_failure_fixture
      catches:
        - template_chosen_by_aesthetic_only
        - template_cannot_host_evidence
        - pack_mismatch_with_deck_job
      required_inputs:
        - slide_function_map
        - selected_templates
        - induced_pack_selection
      pass_if:
        - every_template_has_pick_reason
        - pack_choice_matches_media_and_audience
        - overrides_are_justified

forward_test_report:
  required_sections:
    - old_failure_mode
    - fixture_used
    - expected_blocker
    - actual_result
    - revision_made
    - remaining_risk
  rules:
    - A known failure must become a named blocker.
    - Do not mark process improved until fixture passes or risk is accepted.
```


## Referência: references/source/templates/qa/squad-quality-rubric.yaml

```yaml
version: 1
name: squad-quality-rubric
purpose: >
  Self-contained quality rubric absorbed from the evolved slides-creator squad.
  It keeps the stronger narrative/design gates while removing dependency on
  squad agents, squad tasks, or private process files.

score_scale: "0-100"

dimensions:
  narrativa:
    weight: 25
    description: "Pyramid, vertical flow, action titles, governing thought, SCQA, story arc, slide function."
    sub_dimensions:
      - pyramid_mece
      - vertical_flow
      - action_title_rhetoric
      - governing_thought_strength
      - scqa_depth
      - story_arc
      - slide_function_map
  design:
    weight: 25
    description: "Density, hierarchy, contrast, readability, visual coherence."
    sub_dimensions:
      - density
      - hierarchy
      - contrast
      - readability
      - visual_coherence
  acuracia:
    weight: 20
    description: "APA-quality sources, source fidelity, no invented claims, visual enumeration."
    sub_dimensions:
      - fontes_apa
      - source_fidelity
      - enumeration_universal
  editabilidade:
    weight: 10
    description: "PPTX/editable delivery when export is requested."
    sub_dimensions:
      - opens_without_repair
      - action_title_text_layer
  brand:
    weight: 10
    description: "Token compliance, palette adherence, assets."
    sub_dimensions:
      - brand_token_compliance
      - palette_adherence
      - asset_resolution
  tecnica:
    weight: 10
    description: "Export integrity, diagram/math safety, rendered technical QA."
    sub_dimensions:
      - export_integrity
      - diagrams_math
      - rendered_eval_composite

killer_items:
  - id: KI-01
    description: "PPTX does not open or asks for repair."
    dimension: editabilidade
  - id: KI-02
    description: "Action title is rasterized when editable PPTX was requested."
    dimension: editabilidade
  - id: KI-03
    description: "Critical claim has no complete source."
    dimension: acuracia
  - id: KI-04
    description: "Main slide text is clipped or unreadable."
    dimension: design
  - id: KI-05
    description: "Primary text/background contrast below WCAG AA."
    dimension: design
  - id: KI-06
    description: "Deck violates the approved briefing or user instruction."
    dimension: narrativa
  - id: KI-07
    description: "Action title is descriptive instead of claim-driven."
    dimension: narrativa
  - id: KI-08
    description: "Slide has no declared narrative function or function means 'explain topic'."
    dimension: narrativa
  - id: KI-09
    description: "Final slide count exceeds 2x the planned slide-function map without explicit rationale."
    dimension: narrativa
  - id: KI-10
    description: "Design direction is missing or brand identity is applied only as a skin."
    dimension: design

release_criteria:
  pass:
    overall_score_min: 85
    killer_items_max: 0
    narrativa_min: 70
    design_min: 70
    acuracia_min: 70
  concerns:
    overall_score_min: 75
    overall_score_max: 84
    killer_items_max: 0
    requires_user_ack: true
  fail:
    overall_score_max: 74
    killer_items_min: 1

corrective_actions:
  pyramid_mece: "Rebuild the governing thought and pyramid tree before editing slides."
  vertical_flow: "Read action titles only; rewrite/reorder until the deck tells the story without body copy."
  action_title_rhetoric: "Rewrite titles as claim + magnitude/contrast + implication."
  governing_thought_strength: "Reduce to one executive sentence with claim, stakes, and implication."
  scqa_depth: "Strengthen situation, complication, question, and answer before slide production."
  story_arc: "Rebuild story-arc.yaml with tension, proof/mechanism/payoff, and close."
  slide_function_map: "Compress source topics into audience movements; remove 'explain topic' slides."
  density: "Limit to 1 governing claim and 3 supporting claims; split or cut content."
  hierarchy: "Re-compose grid and type scale so reading order is obvious at a glance."
  contrast: "Change foreground/background pair until text reaches WCAG AA."
  readability: "Reduce line length, increase font size, and move nuance into speaker notes."
  visual_coherence: "Reassert design-direction.yaml and align motif, spacing, and layout rhythm."
  fontes_apa: "Add complete source metadata or mark the claim as assumption/client validation."
  source_fidelity: "Replace invented or untraceable data with sourced text."
  enumeration_universal: "Give each table, chart, figure, or artifact a stable ID."
  brand_token_compliance: "Resolve active tokens and replace unregistered custom colors/fonts."
  export_integrity: "Verify output path, media embeds, links, and text layers."

aggregation:
  overall_formula: "weighted_sum(dimension_score * dimension_weight)"
  revise_if_below: 85
  do_not_call_final_if_below: 75
```


## Referência: references/source/templates/qa/template-selection-gates.yaml

```yaml
version: 1
gates:
  - id: template_selection_gate
    gate: Template choice is explicit and defensible.
    blocks_if:
      - Deck template is missing.
      - Slide template is missing.
      - Visual template is missing for key slides.
      - Selection reason is absent.
    pass_if:
      - Every slide has deck, function, visual, and pick/skip rationale.
    score_weight: 20
    absorbed_from: [ppt-master, Presenton]
  - id: matrix_noise_gate
    gate: Comparison matrices do not repeat useless text.
    blocks_if:
      - Every score cell repeats the same sentence pattern.
      - Row/column labels render as object placeholders.
      - Matrix mixes apps, skills, engines, and runtimes without segmentation.
    pass_if:
      - Cells show scores visually and details appear on selection, side panel, or appendix.
    score_weight: 15
    absorbed_from: [ppt-master, presentation-ai]
  - id: benchmark_category_gate
    gate: Mixed competitors are compared fairly.
    blocks_if:
      - App, skill, engine, and runtime are ranked in one undifferentiated score.
      - Persona weights do not match persona jobs.
    pass_if:
      - Benchmark has at least category-specific comparisons or explicit normalization.
    score_weight: 15
    absorbed_from: [current_sinkra_bench]
  - id: regression_gate
    gate: Known prior failures cannot reappear.
    blocks_if:
      - A prior bad process is mentioned but not mapped to blockers.
      - Forward-test is missing.
    pass_if:
      - Failure mode, new blocker, and verification method are explicit.
    score_weight: 10
    absorbed_from: [powerpoint-skill, slide-creator]
```


## Referência: references/source/templates/qa/visual-gates.yaml

```yaml
version: 1
gates:
  - id: visual_density_gate
    gate: Slides fit their visual role.
    blocks_if:
      - Visible words exceed template limit without appendix reason.
      - More than two consecutive slides use the same layout family.
      - A key slide has no visual structure.
    pass_if:
      - Density is appropriate for audience and slide function.
    score_weight: 15
    absorbed_from: [powerpoint-skill, ppt-master]
  - id: chart_selection_gate
    gate: Chart matches data shape.
    blocks_if:
      - Chart type is chosen for aesthetics instead of data shape.
      - Axes, units, or target baselines are missing.
    pass_if:
      - Pick/skip rule justifies the selected chart.
    score_weight: 10
    absorbed_from: [ppt-master]
  - id: media_relevance_gate
    gate: Images and videos carry meaning.
    blocks_if:
      - Media is atmospheric or decorative.
      - Media lacks relevance reason.
    pass_if:
      - Media either proves, demonstrates, or clarifies the claim.
    score_weight: 10
    absorbed_from: [PPTAgent, banana-slides]
  - id: overlap_boundary_gate
    gate: Rendered slides have no overlap or boundary violations.
    blocks_if:
      - Text overlaps charts, cards, or other text.
      - Element exceeds canvas bounds.
      - Font is too small for intended display.
    pass_if:
      - Layout can pass visual inspection or automated overlap check.
    score_weight: 10
    absorbed_from: [powerpoint-skill]
  - id: brand_fidelity_gate
    gate: Deck follows the selected brand/template system, not just its colors.
    blocks_if:
      - Brand deck or imported template exists but no manifest was produced.
      - Typography, spacing, grid, surface treatment, or chart style contradicts the reference.
      - The deck applies logo/colors while ignoring composition and density rules.
    pass_if:
      - Brand/template manifest maps tokens, layout families, type scale, chart style, imagery, and anti-patterns.
    score_weight: 15
    absorbed_from: [ppt-master, presentation-ai]
  - id: rendered_design_quality_gate
    gate: Key slides look premium after rendering, not only in source spec.
    blocks_if:
      - Cover, reframe, mechanism, proof, or CTA slide lacks rendered review.
      - Rendered review finds generic layout, weak hierarchy, clutter, poor crop, or unreadable text.
      - More than one key slide scores below 90 in visual hierarchy or brand fidelity.
    pass_if:
      - Rendered key slides pass hierarchy, spacing, contrast, crop, emphasis, and scan-path checks.
    score_weight: 20
    absorbed_from: [PPTAgent, powerpoint-skill, banana-slides]
  - id: template_replication_gate
    gate: Imported or selected templates are replicated as reusable behavior.
    blocks_if:
      - Template selection has no rejected runners-up.
      - Layout choice is based on taste rather than slide function.
      - Imported template elements are not mapped to reusable slide roles.
    pass_if:
      - Each key slide declares layout family, source pattern, function fit, and replication constraints.
    score_weight: 15
    absorbed_from: [ppt-master, presentation-ai, PPTAgent]
```


## Referência: references/source/templates/research/evidence-ledger.yaml

```yaml
version: 1
evidence_ledger:
  id: slide_claim_evidence_ledger
  pick_when:
    - Factual claims, benchmarks, market statements, financial numbers, case studies, or technical comparisons appear in the deck.
    - User asks for research depth or a benchmark-grade deck.
    - A slide uses source material, media, demo, chart, or imported document evidence.
  absorbed_from:
    - PresentAgent-2/DeepResearch
    - PPTAgent/document/document.py
    - PPTAgent/ppteval
  required_fields:
    - claim_id
    - slide_id
    - claim
    - evidence_type
    - source
    - confidence
    - visible_or_speaker_notes
    - risk
    - freshness
  evidence_types:
    - official_source
    - benchmark_result
    - academic_paper
    - product_documentation
    - user_provided_document
    - screenshot_or_media
    - internal_artifact
    - explicit_assumption
  confidence_scale:
    high: Source is primary, recent enough, and directly supports the claim.
    medium: Source supports the claim with interpretation or limited scope.
    low: Claim is plausible but weakly sourced; must be labeled or removed.
  rules:
    - Every high-stakes claim must have one ledger row.
    - Low-confidence claims cannot appear as action titles.
    - Speaker notes may carry nuance that would overload slide copy.
    - A chart needs units, timeframe, source, and calculation note.
    - User-provided process logs are evidence of process behavior, not external truth.

ledger_outputs:
  - source_ledger.yaml
  - claim_to_slide_map.yaml
  - unresolved_assumptions.md

blockers:
  - benchmark_claim_without_metric
  - market_claim_without_source
  - comparison_claim_without_scope
  - financial_number_without_period
  - screenshot_or_media_without_reuse_reason
```


## Referência: references/source/templates/research/source-routing.yaml

```yaml
version: 1
research_routes:
  - id: html_source_retrieval
    pick_when:
      - Need explanatory source pages for claims, frameworks, tutorials, technical concepts, or market context.
    preferred_sources:
      - official_docs
      - complete_explainer_pages
      - technical_blogs_with_substance
      - research_project_pages
      - pages_with_figures_or_diagrams
    reject:
      - thin_landing_pages
      - citation_only_pages
      - index_pages
      - pages_that_only_link_elsewhere
    output_fields:
      - source_url
      - source_type
      - why_it_is_useful
      - has_media
      - media_urls
    absorbed_from:
      - PresentAgent-2/DeepResearch/inference/prompt.py

  - id: motion_media_retrieval
    pick_when:
      - Slide would benefit from concrete video, GIF, screen recording, animation, demo, or walkthrough.
    first_search_scope:
      - x.com
      - twitter.com
      - youtube.com/watch
      - youtu.be
      - vimeo.com
      - bilibili.com/video
      - slideslive.com
      - huggingface.co/spaces
      - github.com_with_demo_media
    reject:
      - article_without_playable_media
      - paper_page
      - static_diagram_only
      - profile_or_channel_page
      - media_mentioned_but_not_playable
    output_fields:
      - media_url
      - platform
      - exact_slide_need
      - media_type
      - reuse_reason
      - fallback_static_asset
    absorbed_from:
      - PresentAgent-2/DeepResearch/inference/prompt_media.py

  - id: scholar_or_benchmark_retrieval
    pick_when:
      - Claim needs academic backing, benchmark methodology, paper comparison, or technical evidence.
    rules:
      - Use only when academic evidence improves the slide.
      - Extract benchmark name, metric, dataset, and limitation.
      - Do not overload visible slides with citation prose.
    output_fields:
      - paper_or_benchmark_url
      - claim_supported
      - metric_or_result
      - limitation
      - slide_use
    absorbed_from:
      - PresentAgent-2/DeepResearch/evaluation

  - id: local_file_retrieval
    pick_when:
      - User uploads or points to PDF, DOCX, PPTX, TXT, CSV, XLSX, MP4, MP3, or ZIP.
    rules:
      - Parse files into claim inventory before slide creation.
      - Separate factual extraction from narrative synthesis.
      - Preserve metadata and media captions where available.
    output_fields:
      - parsed_file_id
      - metadata
      - claim_inventory
      - evidence_inventory
      - media_inventory
    absorbed_from:
      - PPTAgent/document/document.py
      - PresentAgent-2/DeepResearch/inference/file_tools

route_selection_rules:
  - Never use one generic research prompt for all source types.
  - Search for media only when the slide has a clear media job.
  - Prefer fewer stronger sources over a long bibliography.
  - Research output feeds manuscript, not final slide copy directly.
```


## Referência: references/source/templates/runtime/api-mcp-cli-contract.yaml

```yaml
version: 1
name: api-mcp-cli-contract
purpose: >
  Define a self-contained automation surface for slide-creator so deck
  generation, critique, edit, export, and package validation can be exposed via
  CLI, REST-style API, and MCP tools with the same job-state semantics.

shared_job_lifecycle:
  states:
    - queued
    - planning
    - drafting
    - reviewing
    - rendering
    - packaging
    - completed
    - failed
    - cancelled
  required_job_fields:
    - job_id
    - command
    - mode
    - created_at
    - updated_at
    - state
    - progress
    - inputs
    - artifacts
    - errors
    - source_of_truth_policy
  event_types:
    - job_created
    - stage_started
    - artifact_written
    - validation_passed
    - validation_failed
    - export_verified
    - job_completed
    - job_failed

cli_commands:
  - id: slide-creator plan
    purpose: Produce briefing, belief shift, story arc, slide-function map, and design direction.
    required_inputs: [brief, audience, outcome]
    required_outputs: [story-arc.yaml, slide-function-map.yaml, design-direction.yaml]
  - id: slide-creator draft
    purpose: Produce the complete deck spec from an approved plan.
    required_inputs: [story-arc.yaml, slide-function-map.yaml, design-direction.yaml]
    required_outputs: [deck-spec.yaml, speaker-notes.yaml, qa-report.yaml]
  - id: slide-creator critique
    purpose: Score an existing deck package against narrative, design, proof, and technical gates.
    required_inputs: [deck-package-path]
    required_outputs: [critique-report.yaml, revision-plan.yaml]
  - id: slide-creator edit
    purpose: Apply a scoped prompt-to-edit operation while preserving locked regions.
    required_inputs: [deck-package-path, edit-prompt]
    required_outputs: [edit-history.yaml, changed-slides.yaml, qa-report.yaml]
  - id: slide-creator package
    purpose: Build delivery manifest, share manifest, and package validation report.
    required_inputs: [deck-package-path]
    required_outputs: [delivery-manifest.yaml, package-validation-report.yaml]
  - id: slide-creator export
    purpose: Run export job and verify output files when a renderer exists.
    required_inputs: [deck-package-path, format]
    required_outputs: [export-report.yaml]

api_routes:
  - method: POST
    path: /v1/decks/plan
    command_equivalent: slide-creator plan
    response_artifacts: [job-state.yaml, story-arc.yaml, slide-function-map.yaml]
  - method: POST
    path: /v1/decks/draft
    command_equivalent: slide-creator draft
    response_artifacts: [job-state.yaml, deck-spec.yaml, qa-report.yaml]
  - method: POST
    path: /v1/decks/critique
    command_equivalent: slide-creator critique
    response_artifacts: [job-state.yaml, critique-report.yaml]
  - method: POST
    path: /v1/decks/edit
    command_equivalent: slide-creator edit
    response_artifacts: [job-state.yaml, edit-history.yaml]
  - method: POST
    path: /v1/decks/package
    command_equivalent: slide-creator package
    response_artifacts: [job-state.yaml, delivery-manifest.yaml, package-validation-report.yaml]
  - method: POST
    path: /v1/decks/export
    command_equivalent: slide-creator export
    response_artifacts: [job-state.yaml, export-report.yaml]
  - method: GET
    path: /v1/jobs/{job_id}
    command_equivalent: job-state read
    response_artifacts: [job-state.yaml]

mcp_tools:
  - id: plan_deck
    purpose: Return narrative plan and slide-function map.
    safety_boundary: Does not render or publish.
    required_artifacts: [story-arc.yaml, slide-function-map.yaml, design-direction.yaml]
  - id: draft_deck_spec
    purpose: Return slide-by-slide deck spec and speaker notes.
    safety_boundary: Requires approved or supplied plan.
    required_artifacts: [deck-spec.yaml, speaker-notes.yaml, qa-report.yaml]
  - id: critique_deck_package
    purpose: Review an existing deck package against gates.
    safety_boundary: Read-only unless explicit edit command follows.
    required_artifacts: [critique-report.yaml, revision-plan.yaml]
  - id: edit_deck_package
    purpose: Apply scoped prompt edit with before/after diff.
    safety_boundary: Cannot edit locked claims, sources, or brand rules without override.
    required_artifacts: [edit-history.yaml, changed-slides.yaml, qa-report.yaml]
  - id: validate_deck_package
    purpose: Validate package completeness and internal references.
    safety_boundary: Validation-only.
    required_artifacts: [package-validation-report.yaml]
  - id: export_deck
    purpose: Invoke external renderer and verify export paths when configured.
    safety_boundary: Cannot claim success without export report and readable file.
    required_artifacts: [export-report.yaml]

safety_rules:
  - CLI, API, and MCP must write the same job-state schema.
  - MCP tools cannot bypass source-of-truth policy or render-lock.
  - Edit commands must preserve unselected regions and produce before/after diffs.
  - Export commands must return a blocker when no renderer is configured.
  - API responses must distinguish generated artifact, verified artifact, and planned artifact.
  - Batch jobs must be resumable or fail with structured errors.

quality_gates:
  pass_if:
    - every_api_route_maps_to_cli_command
    - every_mcp_tool_has_safety_boundary
    - shared_job_lifecycle_has_terminal_states
    - each_command_declares_required_inputs_and_outputs
    - export_route_requires_verification_artifact
  block_if:
    - automation_surface_without_job_state
    - write_tool_without_safety_boundary
    - api_route_without_cli_equivalent
    - export_success_without_verified_export_report
```


## Referência: references/source/templates/runtime/delivery-package-contract.yaml

```yaml
version: 1
name: delivery-package-contract
purpose: >
  Define the minimum shareable delivery package for a generated deck so the
  slide-creator output can move from narrative/design specification to a
  reproducible artifact bundle without depending on the original squad repo.

package_contract:
  required_files:
    - briefing-normalized.md
    - story-arc.yaml
    - slide-function-map.yaml
    - design-direction.yaml
    - storyboard-render-bridge.yaml
    - deck-spec.yaml
    - speaker-notes.yaml
    - qa-report.yaml
    - delivery-manifest.yaml
  optional_files:
    - source-ledger.yaml
    - render-lock.yaml
    - export-report.yaml
    - share-manifest.yaml
    - analytics-events.ndjson
    - follow-up-signal.yaml
  delivery_manifest_required_fields:
    - deck_id
    - title
    - created_at
    - skill_version
    - mode
    - owner
    - source_policy
    - artifacts
    - export_targets
    - permission_policy
    - validation_reports

share_modes:
  - id: private_package
    purpose: Work-in-progress package for internal review.
    required_controls:
      - no_public_url
      - local_paths_only_or_authenticated_storage
      - source_ledger_visible
      - edit_history_visible
  - id: public_review_link
    purpose: Shareable deck review with comments or async stakeholder feedback.
    required_controls:
      - generated_public_url_or_declared_blocker
      - readonly_default
      - optional_password_or_token
      - expiry_policy
      - comment_scope
  - id: handoff_bundle
    purpose: Transfer deck package to another agent, renderer, or presentation tool.
    required_controls:
      - deterministic_file_tree
      - manifest_checksums
      - source_of_truth_policy
      - known_gaps
      - next_actions
  - id: sales_followup
    purpose: Track stakeholder engagement and produce follow-up signals.
    required_controls:
      - event_schema
      - viewer_privacy_notice
      - slide_level_engagement
      - crm_safe_summary

permission_policy:
  roles:
    - id: owner
      can: [read, edit, export, publish, revoke, delete]
    - id: reviewer
      can: [read, comment]
    - id: presenter
      can: [read, present, export_pdf]
    - id: public_viewer
      can: [read]
  rules:
    - Public links default to readonly.
    - Source files and private notes are excluded from public bundles unless explicitly allowed.
    - Exported artifacts must declare whether they are editable, rasterized, or mixed.
    - Every shareable package must expose known limitations rather than hiding unsupported formats.

analytics_event_schema:
  required_fields:
    - event_id
    - deck_id
    - session_id
    - event_type
    - occurred_at
    - slide_id
  event_types:
    - deck_opened
    - slide_viewed
    - cta_clicked
    - comment_added
    - export_downloaded
    - replay_completed
  privacy_rules:
    - Do not require personally identifiable information for aggregate analytics.
    - Viewer identity must be optional and explicitly marked as provided, inferred, or unknown.
    - Follow-up signals must summarize behavior without exposing raw private notes.

follow_up_signal:
  required_fields:
    - deck_id
    - audience_segment
    - strongest_interest
    - unresolved_objections
    - recommended_next_action
    - confidence
    - evidence_events
  action_types:
    - send_appendix
    - schedule_demo
    - clarify_pricing
    - send_case_study
    - request_decision
    - no_action

quality_gates:
  pass_if:
    - delivery_manifest_has_all_required_fields
    - each_artifact_declares_path_type_and_status
    - share_mode_has_permission_policy
    - analytics_events_match_schema_when_present
    - follow_up_signal_references_observed_events_when_present
  block_if:
    - public_link_claim_without_url_or_blocker
    - export_success_claim_without_export_report
    - permission_policy_missing_for_shared_package
    - hidden_private_sources_in_public_package
```


## Referência: references/source/templates/runtime/design-direction-contract.yaml

```yaml
version: 1
name: design-direction-contract
purpose: >
  Self-contained visual direction contract for making design a deck-level
  operating system instead of a late-stage skin.

independence_rule: >
  This contract is bundled in the skill and must work without SINKRA squad
  files, brand workspace paths, or design-renderer agents.

required_output:
  file: design-direction.yaml
  root_key: design_direction
  required_fields:
    - deck_id
    - visual_reference
    - dominant_motif
    - density_limits
    - variation_rules
    - composition_rules
    - audience_context

visual_reference:
  type_enum:
    - provided_brand
    - provided_screenshot
    - imported_pptx
    - existing_design_system
    - bundled_theme
    - design_philosophy_fallback
  required_fields:
    - type
    - rationale
  optional_fields:
    - paths
    - notes
    - must_follow
    - must_avoid

density_limits:
  required_fields:
    - max_governing_claims_per_slide
    - max_supporting_claims_per_slide
    - max_visible_words_default
    - max_visual_elements
    - forbidden_patterns
  defaults:
    max_governing_claims_per_slide: 1
    max_supporting_claims_per_slide: 3
    max_visible_words_default: 45
    max_visual_elements: 5
    forbidden_patterns:
      - dense_bullet_wall
      - decorative_card_stack
      - repeated_two_column_monotony
      - identity_as_skin

variation_rules:
  required_fields:
    - layout_count_min
    - layout_repetition_max
    - quiet_slide_ratio_min
    - accent_color_density
    - motion_policy
  defaults:
    layout_count_min: 5
    layout_repetition_max: 2
    quiet_slide_ratio_min: 0.15
    accent_color_density: "sparse"
    motion_policy: "none unless output is web/native motion"

composition_rules:
  required_fields:
    - grid_columns
    - baseline_padding_pt
    - title_anchor
    - footer_policy
    - slide_number_policy
    - safe_area_pct
  defaults:
    grid_columns: 12
    baseline_padding_pt: 32
    title_anchor: "top_left_or_deliberately_centered"
    footer_policy: "source/provenance only when it adds trust"
    slide_number_policy: "subtle, never primary"
    safe_area_pct: 6

audience_context:
  required_fields:
    - audience
    - viewing_context
    - expected_reading_mode
  examples:
    - audience: "executive committee"
      viewing_context: "live 20-minute decision meeting"
      expected_reading_mode: "scan first, detail second"
    - audience: "webinar attendees"
      viewing_context: "screen-share with speaker narration"
      expected_reading_mode: "big idea first, notes carry nuance"

validation:
  block_if:
    - design_direction_missing
    - visual_reference_missing
    - density_limits_missing
    - composition_rules_missing
    - identity_as_skin_without_stage_specific_motif
    - no_layout_variation_rule
  warn_if:
    - no_visual_reference_paths_when_type_is_provided_brand_or_imported_pptx
    - quiet_slide_ratio_below_10_percent
    - accent_color_density_unspecified
```


## Referência: references/source/templates/runtime/design-score-evidence.yaml

```yaml
version: 1
name: design-score-evidence
purpose: 'Transparent scoring ledger for the Design category. This file explains why
  a score is 86, 92, 96, or 100 by tying each microdimension to concrete bundled evidence
  and release gates.

  '
score_formula:
  cell_score: coverage + depth + fidelity + evidence + absorption
  lens_max: 20
  max_score: 100
  lenses:
    coverage: How much of the capability is implemented for real deck work?
    depth: How detailed and reusable is the implementation?
    fidelity: How well does it preserve design intent during generation/export?
    evidence: How directly can we point to files, fixtures, validators, or rendered
      review?
    absorption: How usable is it inside the self-contained skill without external
      squad dependency?
band_calibration:
  85-89: 'Strong capability exists, but at least one important proof is partial: limited
    fixture depth, weak rendered evidence, missing import pack coverage, or inconsistent
    runtime binding.

    '
  90-94: 'Operationally strong and reusable. Has explicit contracts, registries, examples,
    and QA gates, but still lacks enough rendered/source-deck fixtures to call it
    reference-level across all scenarios.

    '
  95-97: 'Reference-level for most practical scenarios. Requires bundled fixtures,
    selection logic, manifest depth, design QA, and clear anti-patterns. Remaining
    gap is usually scale of real-world rendered comparisons.

    '
  98-100: 'Dominant capability with broad fixtures, validated render evidence, source
    deck manifests, automated checks, and repeated proof across deck types. 100 is
    reserved for executable/imported/rendered proof, not intent.

    '
microdimensions:
- id: visual_layout_quality__layout_variety
  target_score: 99
  current_evidence:
  - templates/visual/charts-and-diagrams.yaml
  - templates/visual/layout-families.yaml
  - templates/visual/media-layouts.yaml
  - templates/slide/function-library.yaml
  - templates/wireframes/
  why_not_100: Ainda abaixo de 100 apenas porque screenshot/render automation externo
    amplo continua sendo melhoria futura.
- id: visual_layout_quality__visual_density_control
  target_score: 99
  current_evidence:
  - templates/runtime/design-direction-contract.yaml
  - templates/runtime/render-lock.yaml
  - templates/qa/visual-gates.yaml
  - templates/visual/design-mastery-contract.yaml
  why_not_100: Ainda abaixo de 100 apenas porque screenshot/render automation externo
    amplo continua sendo melhoria futura.
- id: visual_layout_quality__rendered_visual_quality
  target_score: 98
  current_evidence:
  - templates/eval/rendered-eval.yaml
  - templates/eval/rendered-design-fixture-set.yaml
  - templates/visual/key-slide-render-review.yaml
  - examples/design-100-fixture/key-slide-render-review.yaml
  - templates/eval/design-regression-corpus.yaml
  why_not_100: Ainda abaixo de 100 apenas porque screenshot/render automation externo
    amplo continua sendo melhoria futura.
- id: template_import_replication__template_manifest
  target_score: 100
  current_evidence:
  - templates/import/pptx-template-manifest.yaml
  - templates/import/induced-layout-packs.yaml
  - templates/import/source-deck-fixtures.yaml
  - templates/visual/brand-template-manifest.yaml
  - templates/import/template-import-regression-corpus.yaml
  - scripts/validate_design_capability.py
  why_not_100: 100 atingido nesta microdimensão por corpus local validado.
- id: template_import_replication__brand_fidelity
  target_score: 100
  current_evidence:
  - templates/visual/brand-fidelity-playbooks.yaml
  - templates/visual/brand-system-patterns.yaml
  - templates/visual/aiox-brandbook-deep-patterns.yaml
  - templates/visual/redpine-deep-patterns.yaml
  - templates/theme/brand-systems.yaml
  - templates/import/template-import-regression-corpus.yaml
  - templates/eval/design-regression-corpus.yaml
  why_not_100: 100 atingido nesta microdimensão por corpus local validado.
- id: template_import_replication__template_selection_logic
  target_score: 100
  current_evidence:
  - templates/runtime/template-selection-report.yaml
  - templates/qa/template-selection-gates.yaml
  - templates/import/source-deck-fixtures.yaml
  - templates/deck/route-map.yaml
  - templates/slide/function-library.yaml
  - templates/visual/charts-and-diagrams.yaml
  why_not_100: 100 atingido nesta microdimensão por corpus local validado.
- id: theme_tokens_branding__token_schema
  target_score: 99
  current_evidence:
  - templates/theme/theme-tokens.yaml
  - templates/theme/brand-systems.yaml
  - templates/visual/brand-template-manifest.yaml
  - templates/runtime/render-lock.yaml
  why_not_100: Ainda abaixo de 100 apenas porque screenshot/render automation externo
    amplo continua sendo melhoria futura.
- id: theme_tokens_branding__theme_runtime
  target_score: 99
  current_evidence:
  - templates/runtime/render-lock.yaml
  - templates/runtime/design-direction-contract.yaml
  - templates/runtime/design-score-evidence.yaml
  - templates/eval/rendered-design-fixture-set.yaml
  - templates/runtime/theme-runtime-snapshot-suite.yaml
  - scripts/validate_design_capability.py
  why_not_100: Ainda abaixo de 100 apenas porque screenshot/render automation externo
    amplo continua sendo melhoria futura.
- id: theme_tokens_branding__brand_guardrails
  target_score: 100
  current_evidence:
  - templates/visual/design-mastery-contract.yaml
  - templates/visual/brand-fidelity-playbooks.yaml
  - templates/qa/visual-gates.yaml
  - references/anti-patterns.md
  - templates/eval/design-regression-corpus.yaml
  - templates/import/template-import-regression-corpus.yaml
  why_not_100: 100 atingido nesta microdimensão por corpus local validado.
required_for_design_100:
- design_regression_corpus_with_30_fixture_cases
- template_import_regression_corpus_with_20_source_family_cases
- theme_runtime_snapshot_suite_with_16_snapshot_cases
- validate_design_capability_passes
- design_mastery_fixture_passes
```


## Referência: references/source/templates/runtime/diagram-rendering.yaml

```yaml
version: 1
source_principle: >
  Diagrams need engine routing. Pick the rendering layer by diagram semantics,
  editability, math precision, and fidelity needs before generating source code
  or slide shapes.
absorbed_from:
  - ../../../../../../bench/powerpoint-skill/powerpoint-slides/diagram-rendering.md

engine_layers:
  - id: graphviz
    output: svg
    best_for:
      - architecture
      - flow
      - dependency_graph
      - tree
      - comparison_graph
    constraints:
      max_nodes: 15
      preferred_rankdir: "LR | TB"
      use_clusters_for_groups: true
      avoid_cluttered_edge_labels: true
    export_policy:
      convert_to_svg: true
      embed_or_trace_as_native: "renderer-dependent"
  - id: mermaid
    output: svg
    best_for:
      - sequence
      - gantt
      - pie
      - state
      - er
    constraints:
      max_sequence_participants: 6
      use_cli_fallback_when_available: true
    export_policy:
      convert_to_svg: true
  - id: tikz
    output: "svg | png"
    best_for:
      - math_diagram
      - geometric_construction
      - paper_faithful_technical_figure
    constraints:
      prefer_for_formula_adjacent_diagrams: true
      require_latex_available: "when rendering locally"
    export_policy:
      png_allowed_for_complex_latex: true
  - id: native_shapes
    output: pptx_native
    best_for:
      - simple_arrows
      - annotations
      - highlights
      - callouts
      - basic_process
    constraints:
      keep_text_editable: true
      avoid_complex_auto_layout: true
    export_policy:
      raster_allowed: false
  - id: pdf_figure_extraction
    output: png
    best_for:
      - paper_figures
      - externally_sourced_diagrams
      - screenshots_that_are_evidence
    constraints:
      dpi: 300
      min_width_px_warn: 800
      require_source_attribution: true
      never_extract_tables_as_images: true
    export_policy:
      rebuild_tables_natively: true

diagram_routing:
  architecture: graphviz
  dependency: graphviz
  process_with_branches: graphviz
  sequence: mermaid
  gantt: mermaid
  state_machine: mermaid
  entity_relationship: mermaid
  math_or_geometry: tikz
  simple_annotation: native_shapes
  simple_arrow_flow: native_shapes
  extracted_paper_figure: pdf_figure_extraction

diagrams_json_contract:
  diagrams:
    - diagram_id: "d01"
      slide_id: "s01"
      purpose: ""
      engine: "graphviz | mermaid | tikz | native_shapes | pdf_figure_extraction"
      source_file: ""
      output_file: ""
      editable_level: "native | source_editable | raster_only"
      theme:
        colors: []
        fonts: []
      qa:
        rendered: false
        fits_container: false
        legible_at_thumbnail: false
        attributed: false
        issues: []

manifest_contract:
  diagram_manifest:
    output_dir: "diagrams"
    generated_at: ""
    diagrams: []
    blockers: []

theme_injection_rules:
  - Inject deck fonts and colors into Graphviz/Mermaid/TikZ where the engine allows it.
  - If SVG ignores theme tokens, post-process or mark as theme mismatch.
  - Diagrams used as proof must include source or assumption in speaker notes.
  - Diagram labels should be native overlay text when exact wording, accents, or numbers matter.

quality_gates:
  - diagram_source_exists
  - diagram_output_exists
  - output_matches_selected_engine
  - no_unattributed_extracted_figures
  - no_table_as_image
  - no_unreadable_edge_labels
  - no_theme_mismatch_unless_waived
  - no_raster_only_when_editable_diagram_required
```


## Referência: references/source/templates/runtime/edit-history.yaml

```yaml
version: 1
runtime_jobs:
  - id: edit_history_and_diff_contract
    mode: edit_history
    pick_when:
      - User edits an existing deck or asks for prompt-to-edit behavior.
      - Multiple revisions are expected and undo/redo or diff clarity matters.
      - A generated deck should preserve revision accountability.
    inputs:
      - previous_deck_spec
      - edit_prompt
      - changed_slide_ids
      - change_type
    steps:
      - capture_pre_edit_snapshot
      - classify_change_type
      - apply_edit_to_target_scope
      - merge_rapid_same_slide_changes
      - clear_future_on_new_change
      - produce_diff_summary
      - run_local_qa_on_changed_scope
    outputs:
      - edit_history
      - changed_slides
      - diff_summary
      - local_qa_report
    failure_policy:
      continue_on_error: true
      block_if_missing:
        - edit_prompt
    absorbed_from:
      - Presenton/undoRedoSlice.ts
      - presentation-ai/presentation-history-state.ts

history_contract:
  max_history_size: 50
  rate_limit_ms_for_same_slide: 300
  change_types:
    - slide
    - theme
    - structure
    - full
  entry_fields:
    - timestamp
    - change_type
    - slide_id
    - before_summary
    - after_summary
    - affected_artifacts
    - qa_status
  rules:
    - Do not add history entry if serialized content is identical.
    - Merge rapid changes to the same slide when they are part of one user intent.
    - Clear future history when a new change is made after undo.
    - During undo/redo restore, skip automatic history capture once to avoid loops.

diff_summary_contract:
  required_sections:
    - user_intent
    - slides_changed
    - claims_changed
    - templates_changed
    - visual_changes
    - risks_introduced
    - qa_rerun
  block_if:
    - A sourced claim changed without evidence-ledger update.
    - A template changed without rerunning template-selection gate.
    - A visual change affects rendered key slide but rendered eval was skipped.
```


## Referência: references/source/templates/runtime/edit-operations.yaml

```yaml
version: 1
edit_operations:
  - id: change_theme
    user_intents: [change_visual_style, match_brand, make_more_premium]
    requires: [theme_profile]
    preserves: [story_arc, slide_functions, evidence]
    qa_after: [contrast_gate, density_gate, brand_consistency_gate]
    absorbed_from: [presentation-ai]
  - id: regenerate_slide
    user_intents: [rewrite_slide, make_clearer, improve_design, reduce_text]
    requires: [slide_id, reason]
    preserves: [deck_thesis, slide_function]
    qa_after: [slide_function_gate, density_gate, visual_fit_gate]
    absorbed_from: [presentation-ai, Presenton]
  - id: replace_visual
    user_intents: [change_image, replace_chart, use_better_diagram]
    requires: [slide_id, visual_template_or_media]
    preserves: [action_title, key_message]
    qa_after: [media_relevance_gate, chart_selection_gate]
    absorbed_from: [presentation-ai, banana-slides]
  - id: split_slide
    user_intents: [too_dense, too_many_messages, hard_to_read]
    requires: [slide_id]
    preserves: [evidence, sequence_position]
    qa_after: [narrative_continuity_gate, density_gate]
    absorbed_from: [powerpoint-skill]
  - id: merge_slides
    user_intents: [repetitive, too_long, duplicate_function]
    requires: [slide_ids]
    preserves: [strongest_claim, strongest_evidence]
    qa_after: [slide_function_gate, repetition_gate]
    absorbed_from: [slide-deck-ai]
  - id: local_prompt_to_edit
    user_intents: [vibe_edit, natural_language_edit, partial_redraw]
    requires: [selected_slide_or_region, edit_prompt]
    preserves: [unselected_regions, deck_thesis]
    qa_after: [diff_gate, visual_integrity_gate]
    absorbed_from: [banana-slides, Presenton]
```


## Referência: references/source/templates/runtime/export-contract.yaml

```yaml
version: 1
runtime_jobs:
  - id: verified_export_job
    mode: export
    pick_when:
      - User requests PPTX, PDF, screenshots, thumbnails, or shareable deck artifacts.
      - A local app or renderer must produce a final file, not just a Markdown spec.
    inputs:
      - deck_id
      - title
      - export_format
      - render_url
      - session_context
    steps:
      - create_export_task_json
      - run_export_worker
      - capture_stdout_stderr
      - parse_response_json
      - verify_output_path_exists
      - verify_file_readable
      - generate_preview_or_thumbnail
      - attach_export_report
    outputs:
      - output_file_path
      - export_task_json
      - export_response_json
      - export_log
      - preview_artifact
    failure_policy:
      continue_on_error: false
      block_if_missing:
        - export_format
        - render_url
      retryable_errors:
        - renderer_timeout
        - session_cookie_expired
        - temporary_converter_failure
    absorbed_from:
      - Presenton/run-bundled-presentation-export.ts
      - banana-slides/scripts/export_editable_pptx.py

export_task_contract:
  required_fields:
    - type
    - url
    - format
    - title
  optional_fields:
    - cookie_header
    - fastapi_url
    - output_directory
    - converter_path
  rules:
    - Export task must be serializable and reproducible.
    - Filename must be sanitized before worker execution.
    - The final answer cannot claim export success before output path verification.

verification:
  pass_if:
    - Output file exists.
    - Output file is readable.
    - Export worker returned structured response.
    - Preview or thumbnail can be generated or explicit reason is reported.
  blocks_if:
    - Worker exits nonzero without surfaced stderr/stdout.
    - Response JSON has no path or URL.
    - Exported file is missing, zero bytes, or unreadable.
```


## Referência: references/source/templates/runtime/html-to-pptx.yaml

```yaml
version: 1
runtime_jobs:
  - id: html_to_pptx_render_contract
    mode: render_export
    pick_when:
      - Slides are authored as HTML/CSS before PowerPoint export.
      - User needs editable PPTX/PDF after visual-first slide design.
      - A wireframe or browser-rendered deck must become a deliverable deck.
    inputs:
      - html_slide_pages
      - slide_aspect_ratio
      - theme_tokens
      - export_format
    steps:
      - render_each_slide_in_browser
      - lock_deck_dimensions_from_first_slide
      - extract_placeholders_and_named_regions
      - convert_text_images_shapes_tables_and_backgrounds
      - rasterize_css_that_pptx_cannot_represent
      - check_overflow_and_bottom_margin
      - export_pptx_or_pdf
      - inspect_rendered_output
    outputs:
      - converted_pptx
      - converted_pdf
      - placeholder_map
      - overflow_report
      - rasterization_report
    failure_policy:
      continue_on_error: false
      block_if_missing:
        - slide_aspect_ratio
        - html_slide_pages
    absorbed_from:
      - PPTAgent/deeppresenter/html2pptx/html2pptx.js
      - powerpoint-skill/check_overlaps.py
      - Presenton/presentation-export

conversion_rules:
  dimensions:
    - First slide defines canonical width and height.
    - Every later slide must match dimensions or declare an intentional format change.
    - Do not allow viewport-dependent text scaling to change slide geometry.
  placeholders:
    selector: ".placeholder"
    required_metadata:
      - name
      - x
      - y
      - width
      - height
    use_when:
      - A later agent or user may replace chart, image, quote, logo, or table content.
  text:
    - Preserve font family, weight, size, alignment, color, and line spacing when supported.
    - Block export if text exceeds region bounds and cannot be reduced without losing hierarchy.
    - Keep at least 0.5in bottom safety margin for presenter display and PDF export.
  rasterization:
    rasterize_when:
      - gradient_or_shadow_is_core_to_visual
      - complex_css_has_no_pptx_equivalent
      - browser_render_is_more_faithful_than_native_shape
    do_not_rasterize_when:
      - text_must_remain_editable
      - chart_data_must_remain_editable
      - simple_shape_can_be_native
  tables:
    - Use native table only when editing matters and styling is simple.
    - Use image snapshot when table is a designed artifact or contains complex visual formatting.

qa_requirements:
  - No slide may export with clipped title, chart, CTA, or source label.
  - HTML screenshot and exported PDF/PPTX preview must be visually comparable.
  - Export report must list every rasterized element and why it was rasterized.
```


## Referência: references/source/templates/runtime/import-template.yaml

```yaml
version: 1
import_template_pipeline:
  id: import_existing_pptx_or_visual_reference
  pick_when:
    - User provides a PPTX, screenshots, reference image, or existing branded deck.
  absorbed_from: [Presenton, PPTAgent, PresentAgent-2]
  steps:
    - inspect_source_assets
    - extract_fonts_colors_and_grid
    - identify_slide_layouts
    - induce_elements_per_layout
    - assign_functional_keys
    - infer_suggested_character_limits
    - create_template_family_metadata
    - create_sample_data
    - run_template_selection_gate
  output_contract:
    template_family:
      fields: [id, name, source, description, ordered, default_theme]
    slide_layout:
      fields: [id, name, description, elements, schema, sample_data, compatible_slide_functions]
    element:
      fields: [name, type, description, required, suggested_characters, variable_length]
  blockers:
    - Cannot import layout without element names and roles.
    - Cannot use a reference image as style if it conflicts with readability gates.
    - Cannot preserve source order if source deck has duplicate slide functions.
```


## Referência: references/source/templates/runtime/job-state.schema.yaml

```yaml
type: object
required:
  - job_id
  - run_id
  - job_type
  - status
  - inputs
  - task_records
  - progress_events
  - artifacts
  - policy
  - final_verdict
properties:
  job_id:
    type: string
  run_id:
    type: string
  job_type:
    type: string
    enum:
      - full_generation
      - source_document_generation
      - improve_existing_deck
      - prompt_to_edit
      - export_only
      - batch_generation
  mode:
    type: string
  status:
    type: string
    enum: [queued, running, waiting, completed, failed, cancelled, partial]
  inputs:
    type: object
  task_records:
    type: array
    items:
      type: object
      required: [task_id, type, status]
      properties:
        task_id:
          type: string
        type:
          type: string
        status:
          type: string
        started_at:
          type: string
        completed_at:
          type: string
        error:
          type: string
  progress_events:
    type: array
    items:
      type: object
      required: [event, task_id]
      properties:
        event:
          type: string
        task_id:
          type: string
        task_type:
          type: string
        progress:
          type: object
        message:
          type: string
  artifacts:
    type: array
    items:
      type: object
      required: [artifact_id, kind, path_or_url, status]
      properties:
        artifact_id:
          type: string
        kind:
          type: string
        path_or_url:
          type: string
        status:
          type: string
          enum: [planned, created, verified, failed]
        checksum:
          type: string
  export_policy:
    type: object
    properties:
      formats:
        type: array
        items:
          type: string
      editable_required:
        type: boolean
      verify_outputs:
        type: boolean
  policy:
    type: object
    required: [continue_on_error, timeout_sec]
    properties:
      continue_on_error:
        type: boolean
      timeout_sec:
        type: integer
      resume_allowed:
        type: boolean
      resume_from:
        type: string
  error_details:
    type: array
    items:
      type: object
  final_verdict:
    type: string
    enum: [pass, warn, fail, blocked]
```


## Referência: references/source/templates/runtime/jobs.yaml

```yaml
version: 1
runtime_jobs:
  - id: full_deck_from_brief
    mode: generation
    pick_when:
      - User gives topic, brief, rough notes, or objective and wants a new deck.
    inputs: [briefing, audience, objective, constraints]
    steps:
      - normalize_briefing
      - select_deck_template
      - create_story_arc
      - map_slide_functions
      - select_visual_templates
      - draft_deck_spec
      - run_key_slide_gate
      - revise
      - package_outputs
    outputs: [briefing_normalized, story_arc, slide_function_map, deck_spec, qa_report]
    failure_policy:
      continue_on_error: false
      block_if_missing: [audience, objective, deck_template]
    absorbed_from: [slide-deck-ai, banana-slides]

  - id: deck_from_source_document
    mode: ingestion
    pick_when:
      - User provides PDF, DOCX, PPTX, MD, transcript, process log, or research notes.
    inputs: [source_document, objective, audience]
    steps:
      - extract_claims
      - extract_evidence
      - discard_source_order_if_weak
      - select_deck_template
      - map_claims_to_slide_functions
      - produce_deck_spec
    outputs: [claim_inventory, evidence_inventory, deck_spec, qa_report]
    failure_policy:
      continue_on_error: true
      block_if_missing: [objective]
    absorbed_from: [Presenton, banana-slides, slide-deck-ai]

  - id: improve_bad_deck_or_process
    mode: regression
    pick_when:
      - User provides a weak prior deck, process log, or says the previous output was bad.
    inputs: [prior_deck_or_process, desired_outcome]
    steps:
      - diagnose_failure_modes
      - create_forward_test
      - select_replacement_templates
      - rewrite_slide_function_map
      - redesign_key_slides
      - run_regression_gate
    outputs: [diagnostic, forward_test, revised_slide_map, revised_deck_spec]
    failure_policy:
      continue_on_error: false
      block_if_missing: [failure_modes]
    absorbed_from: [powerpoint-skill, slide-deck-ai]

  - id: prompt_to_edit_existing_deck
    mode: edit
    pick_when:
      - User asks to change tone, layout, structure, narrative, or specific slides.
    inputs: [existing_deck_spec, edit_prompt]
    steps:
      - classify_edit_intent
      - preserve_locked_claims
      - update_affected_slide_templates
      - rerun_local_qa
      - report_diffs
    outputs: [changed_slides, revision_notes, qa_report]
    failure_policy:
      continue_on_error: true
      block_if_missing: [edit_prompt]
    absorbed_from: [Presenton, presentation-ai, banana-slides]

  - id: batch_benchmark_generation
    mode: batch
    pick_when:
      - Multiple benchmarks, personas, or scenarios must be generated consistently.
    inputs: [jobs, shared_template_registry, export_policy]
    steps:
      - validate_jobs
      - apply_shared_weights
      - generate_each_deck_spec
      - produce_comparative_index
      - summarize_cross_job_learnings
    outputs: [job_results, comparative_index, qa_report]
    failure_policy:
      continue_on_error: true
      timeout_sec: 1800
    absorbed_from: [banana-slides]
```


## Referência: references/source/templates/runtime/manuscript-pipeline.yaml

```yaml
version: 1
runtime_jobs:
  - id: manuscript_first_deck_pipeline
    mode: manuscript
    pick_when:
      - Deck depends on research, explanation, proof quality, or complex narrative.
      - User provides only a broad topic but expects a strong presentation.
      - Previous output failed because slides were generated directly from an outline.
    inputs:
      - user_goal
      - audience
      - desired_belief_shift
      - source_material
      - constraints
    steps:
      - planner_creates_outline_json
      - research_creates_markdown_manuscript
      - manuscript_sections_are_mapped_to_slide_functions
      - evidence_and_media_are_bound_to_claims
      - slide_structure_templates_are_selected
      - visual_templates_are_selected
      - deck_spec_is_generated_from_manuscript
      - key_slides_are_render_checked_before_full_deck
    outputs:
      - outline_json
      - research_manuscript
      - claim_to_evidence_map
      - media_inventory
      - slide_function_map
      - deck_spec
      - qa_report
    failure_policy:
      continue_on_error: false
      block_if_missing:
        - audience
        - desired_belief_shift
        - slide_function_map
    absorbed_from:
      - PPTAgent/deeppresenter/roles/Planner.yaml
      - PPTAgent/deeppresenter/roles/Research.yaml
      - PPTAgent/deeppresenter/roles/PPTAgent.yaml

contracts:
  outline_json:
    required_fields:
      - index
      - title
      - context
    rules:
      - Each outline item must describe why it exists in the audience journey.
      - Outline order is allowed to diverge from source order.
      - No slide count is final until key-slide gate passes.

  research_manuscript:
    format: markdown
    section_separator: "---"
    required_per_section:
      - section_title
      - concise_argument
      - source_notes
      - candidate_visuals
    rules:
      - Keep claims and evidence together.
      - Prefer local or cited media references over vague image ideas.
      - Mark uncertain facts as assumptions instead of presenting them as proof.
      - Remove source material that does not serve the belief shift.

  renderer_handoff:
    required_fields:
      - slide_index
      - slide_function
      - action_title
      - source_section_ids
      - template_id
      - visual_template_id
      - speaker_note_intent
    rules:
      - Renderer receives structured slide intent, not raw research dump.
      - Tables become visual artifacts only when they clarify the claim.
      - Dense source sections must be compressed before slide drafting.

quality_gates:
  - Manuscript must contain more proof than the final deck shows.
  - Every decisive slide must trace to one manuscript section or explicit synthesis.
  - A deck cannot skip manuscript when topic requires research or prior process failed.
```


## Referência: references/source/templates/runtime/narrative-design-moment-grammar.yaml

```yaml
version: 1
name: narrative-design-moment-grammar
purpose: >
  Bind narrative intent to visual execution at slide-moment level. Use this
  when a deck must feel designed, not merely styled, and when the story arc
  must control layout, density, proof, pacing, and visual contrast.

moment_schema:
  required_fields:
    - moment_id
    - narrative_job
    - audience_state_before
    - audience_state_after
    - emotional_temperature
    - cognitive_load
    - primary_visual_move
    - density_budget
    - proof_visibility
    - layout_family
    - transition_role
    - failure_mode
  optional_fields:
    - compatible_slide_functions
    - compatible_wireframes
    - forbidden_visual_moves
    - speaker_note_rhythm
    - edit_sensitivity

moment_archetypes:
  - id: shock_reframe
    narrative_job: break_default_frame
    audience_state_before: "They think the category is familiar."
    audience_state_after: "They see the old frame is insufficient."
    emotional_temperature: high
    cognitive_load: low
    primary_visual_move: one_big_contrast
    density_budget: 18_visible_words
    proof_visibility: one_evidence_anchor_or_visual_before_after
    layout_family: contrast
    transition_role: opens_attention_loop
    compatible_slide_functions: [reframe, tension_amplify]
    compatible_wireframes: [myth-truth, competitive-landscape, quote-evidence-panel]
    forbidden_visual_moves: [multi_card_grid, dense_table, decorative_stock_image]
    speaker_note_rhythm: "short claim, pause, explain why the default frame fails"
    edit_sensitivity: high
    failure_mode: "If the slide explains a topic instead of changing the frame, it fails."
  - id: executive_answer_first
    narrative_job: give_decision_context
    audience_state_before: "They expect a walkthrough."
    audience_state_after: "They know the answer and can inspect drivers."
    emotional_temperature: medium
    cognitive_load: medium
    primary_visual_move: answer_plus_driver_stack
    density_budget: 38_visible_words
    proof_visibility: metrics_above_fold_with_units
    layout_family: executive_snapshot
    transition_role: establishes_orientation
    compatible_slide_functions: [cover, synthesis, proof]
    compatible_wireframes: [executive-summary, dashboard-grid, financial-waterfall]
    forbidden_visual_moves: [chronological_intro, decorative_hero, unranked_metric_wall]
    speaker_note_rhythm: "answer, consequence, two drivers, decision implication"
    edit_sensitivity: medium
    failure_mode: "If the audience must hunt for the answer, it fails."
  - id: tension_ladder
    narrative_job: increase_cost_of_inaction
    audience_state_before: "They agree mildly but feel no urgency."
    audience_state_after: "They feel the accumulating cost or risk."
    emotional_temperature: high
    cognitive_load: medium
    primary_visual_move: escalating_sequence
    density_budget: 32_visible_words
    proof_visibility: trend_or_consequence_per_step
    layout_family: timeline_or_ladder
    transition_role: raises_stakes
    compatible_slide_functions: [tension_amplify, proof]
    compatible_wireframes: [incident-timeline, maturity-ladder, risk-heatmap]
    forbidden_visual_moves: [flat_bullets, equal_weight_cards, low_contrast_risk_tokens]
    speaker_note_rhythm: "step, consequence, escalation, next step"
    edit_sensitivity: high
    failure_mode: "If all risks feel equal, it fails."
  - id: mechanism_reveal
    narrative_job: explain_why_the_solution_works
    audience_state_before: "They see the desired outcome but not the engine."
    audience_state_after: "They understand the causal mechanism."
    emotional_temperature: medium
    cognitive_load: high
    primary_visual_move: labeled_system_flow
    density_budget: 45_visible_words
    proof_visibility: cause_effect_labels_and_one_example
    layout_family: system_diagram
    transition_role: converts_interest_into_belief
    compatible_slide_functions: [mechanism_step, demo_setup]
    compatible_wireframes: [mechanism-map, technical-architecture, dependency-map]
    forbidden_visual_moves: [logo_soup, unlabeled_arrows, pure_concept_art]
    speaker_note_rhythm: "input, transformation, output, why it matters"
    edit_sensitivity: high
    failure_mode: "If arrows do not express causality, it fails."
  - id: proof_stack
    narrative_job: make_claim_credible
    audience_state_before: "They like the claim but need evidence."
    audience_state_after: "They can repeat why the claim is credible."
    emotional_temperature: medium
    cognitive_load: medium
    primary_visual_move: ranked_evidence_stack
    density_budget: 42_visible_words
    proof_visibility: source_metric_quote_artifact
    layout_family: evidence_panel
    transition_role: reduces_perceived_risk
    compatible_slide_functions: [proof, objection_neutralize]
    compatible_wireframes: [proof-stack, case-study-proof, quote-evidence-panel]
    forbidden_visual_moves: [testimonial_without_specificity, unsourced_metric, equal_weight_evidence]
    speaker_note_rhythm: "claim, strongest proof, corroborating proof, implication"
    edit_sensitivity: high
    failure_mode: "If evidence is decorative or unsourced, it fails."
  - id: demo_payoff
    narrative_job: show_before_after_result
    audience_state_before: "They expect feature navigation."
    audience_state_after: "They see a concrete artifact or workflow payoff."
    emotional_temperature: high
    cognitive_load: medium
    primary_visual_move: before_after_or_input_output
    density_budget: 28_visible_words
    proof_visibility: output_artifact_visible
    layout_family: demo_sequence
    transition_role: turns_mechanism_into_desire
    compatible_slide_functions: [demo_payoff, artifact_reveal]
    compatible_wireframes: [screen-sequence, api-request-response, data-lineage]
    forbidden_visual_moves: [feature_list, screenshot_wall, hidden_output]
    speaker_note_rhythm: "before, action, after, why this changes the workflow"
    edit_sensitivity: high
    failure_mode: "If no artifact/result is visible, it fails."
  - id: decision_tradeoff
    narrative_job: make_options comparable
    audience_state_before: "They see multiple plausible choices."
    audience_state_after: "They understand the recommended tradeoff."
    emotional_temperature: medium
    cognitive_load: high
    primary_visual_move: option_matrix_with_recommendation
    density_budget: 55_visible_words
    proof_visibility: criteria_weights_and_consequences
    layout_family: matrix
    transition_role: prepares_decision
    compatible_slide_functions: [contrast, synthesis, cta_concrete]
    compatible_wireframes: [decision-options, architecture-tradeoff-table, scoring-rubric]
    forbidden_visual_moves: [unweighted_table, hidden_recommendation, ornamental_badges]
    speaker_note_rhythm: "criteria, option contrast, tradeoff, recommendation"
    edit_sensitivity: medium
    failure_mode: "If the recommendation is visually timid or criteria are unclear, it fails."
  - id: breathing_room_transition
    narrative_job: let_audience_absorb
    audience_state_before: "They just processed a dense proof or mechanism."
    audience_state_after: "They retain the point and are ready for the next beat."
    emotional_temperature: low
    cognitive_load: low
    primary_visual_move: single_claim_with_space
    density_budget: 14_visible_words
    proof_visibility: no_new_proof
    layout_family: sparse_claim
    transition_role: resets_attention
    compatible_slide_functions: [section_divider, emotional_anchor, close]
    compatible_wireframes: [section-divider, closing-card, mission-vision]
    forbidden_visual_moves: [new_dense_chart, multi_metric_grid, appendix_table]
    speaker_note_rhythm: "recap, pause, bridge to next section"
    edit_sensitivity: low
    failure_mode: "If it introduces another complex idea, it fails."
  - id: close_with_specific_next_step
    narrative_job: convert belief into action
    audience_state_before: "They understand the case but may defer."
    audience_state_after: "They know the next step, owner, artifact, and date."
    emotional_temperature: high
    cognitive_load: low
    primary_visual_move: cta_with_commitment_frame
    density_budget: 30_visible_words
    proof_visibility: recap_of_one_decisive_proof
    layout_family: cta_panel
    transition_role: closes_open_loop
    compatible_slide_functions: [cta_concrete, close]
    compatible_wireframes: [contact-next-step, decision-options, pricing-table]
    forbidden_visual_moves: [generic_thank_you, multiple_ctas, vague_contact_us]
    speaker_note_rhythm: "why now, what happens next, who owns it, when"
    edit_sensitivity: medium
    failure_mode: "If the CTA could be copied to any deck, it fails."

continuity_rules:
  - id: dense_then_breathing_room
    rule: "A high-density proof/mechanism moment should be followed by a lower-density synthesis or transition unless the deck is an appendix."
  - id: proof_before_ask
    rule: "A CTA or decision ask must be preceded by a proof, demo payoff, or tradeoff moment."
  - id: emotion_load_alternation
    rule: "Do not stack more than two high-emotion moments without a grounding proof or mechanism."
  - id: layout_follows_belief_shift
    rule: "Layout family changes must map to a narrative shift: frame, stakes, mechanism, proof, decision, or close."
  - id: visual_repetition_has_reason
    rule: "Repeated layout is allowed only for deliberate comparison, sequence, or rhythm."

score_relevance:
  consultative_narrative__belief_shift: "Audience state before/after is required per moment."
  narrative_governance_qa__key_slide_gate: "Key moments make cover/reframe/mechanism/proof/CTA inspectable."
  visual_layout_quality__layout_variety: "Layout variation is driven by narrative role."
  visual_layout_quality__visual_density_control: "Density budget is attached to each moment."
  rendered_visual_quality__rendered_visual_quality: "Failure modes are visual and narrative at once."
```


## Referência: references/source/templates/runtime/narrative-regression-corpus.yaml

```yaml
version: 1
name: narrative-regression-corpus
purpose: >
  Regression corpus for proving that narrative quality is repeatable across
  deck jobs. It prevents outline dumps, weak belief shifts, weak proof
  sequencing, and unclear CTAs.

minimum_reference_bar:
  narrative_cases: 24
  deck_jobs: 12
  required_case_fields:
    - deck_job
    - audience_current_belief
    - desired_belief
    - narrative_risk
    - required_beats
    - key_slide_functions
    - proof_standard
    - failure_test

narrative_cases:
  - id: benchmark_absorption_decision
    deck_job: benchmark_analysis
    audience_current_belief: "We should choose the highest-ranked tool."
    desired_belief: "We should compose capabilities by segment because apps, skills, and engines are not interchangeable."
    narrative_risk: "ranking absolutism"
    required_beats: [scope_split, evaluation_frame, evidence_matrix, absorption_map, decision]
    key_slide_functions: [reframe, proof, contrast, synthesis, cta_concrete]
    proof_standard: "Every score maps to source path, observed behavior, or explicit assumption."
    failure_test: "If the deck can be read as a generic top-10 list, it fails."
  - id: board_update_decision
    deck_job: board_update
    audience_current_belief: "The numbers speak for themselves."
    desired_belief: "The variance has drivers, options, and one recommended decision."
    narrative_risk: "dashboard dump"
    required_beats: [answer_first, driver_tree, risk, options, recommendation, ask]
    key_slide_functions: [cover, proof, contrast, synthesis, cta_concrete]
    proof_standard: "Every number has period, unit, source, and assumption label."
    failure_test: "If no decision owner/deadline appears, it fails."
  - id: investor_pitch_next_meeting
    deck_job: investor_pitch
    audience_current_belief: "This is another early-stage pitch."
    desired_belief: "This is a sharp wedge in a timely market with enough proof for the next meeting."
    narrative_risk: "too much diligence before desire"
    required_beats: [market_shift, problem, promised_land, solution, traction, ask]
    key_slide_functions: [tension_amplify, reframe, proof, mechanism_step, cta_concrete]
    proof_standard: "Traction, market, and model are sourced or labeled as assumptions."
    failure_test: "If the first five slides do not earn curiosity, it fails."
  - id: sales_offer_decision
    deck_job: sales_proposal
    audience_current_belief: "This is a vendor feature list."
    desired_belief: "This offer reduces a specific risk and makes the buying decision easier."
    narrative_risk: "feature stack"
    required_beats: [pain, desired_outcome, obstacles, mechanism, deliverables, risk_reversal, next_step]
    key_slide_functions: [tension_amplify, mechanism_step, proof, objection_neutralize, cta_concrete]
    proof_standard: "Every feature maps to outcome, obstacle, or risk reversal."
    failure_test: "If deliverables appear before pain/outcome, it fails."
  - id: webinar_conversion
    deck_job: webinar
    audience_current_belief: "I need information."
    desired_belief: "I need this mechanism and the next step is concrete."
    narrative_risk: "free training with late offer"
    required_beats: [promise, false_beliefs, mechanism, proof, implementation, offer, cta]
    key_slide_functions: [cover, reframe, mechanism_step, proof, objection_neutralize, cta_concrete]
    proof_standard: "At least one concrete demo, artifact, case, or before/after appears before the offer."
    failure_test: "If the offer feels bolted on, it fails."
  - id: vsl_watch_retention
    deck_job: vsl
    audience_current_belief: "This may be another long pitch."
    desired_belief: "The hook is specific enough to keep watching and the mechanism is novel."
    narrative_risk: "slow setup"
    required_beats: [snap_suggestion, usp, problem_amplification, story, mechanism, proof, offer, close]
    key_slide_functions: [cover, tension_amplify, reframe, emotional_anchor, proof, cta_concrete]
    proof_standard: "USP appears early; proof precedes offer; close has one CTA."
    failure_test: "If no strong claim appears in first 10 percent, it fails."
  - id: product_demo_payoff
    deck_job: product_demo
    audience_current_belief: "Show me features."
    desired_belief: "This workflow produces a valuable before/after that I can imagine using."
    narrative_risk: "feature tour"
    required_beats: [user_pain, workflow_thesis, demo_setup, demo_payoff, proof, adoption_path]
    key_slide_functions: [reframe, demo_setup, demo_payoff, proof, cta_concrete]
    proof_standard: "Demo payoff must show artifact/result, not only UI navigation."
    failure_test: "If the demo never reveals a concrete artifact, it fails."
  - id: architecture_decision
    deck_job: architecture_decision
    audience_current_belief: "There are many possible designs."
    desired_belief: "One architecture is the best tradeoff under the declared constraints."
    narrative_risk: "diagram catalog"
    required_beats: [constraint, options, tradeoff, recommendation, migration_plan]
    key_slide_functions: [tension_amplify, contrast, mechanism_step, synthesis, cta_concrete]
    proof_standard: "Each tradeoff names constraint, consequence, and mitigation."
    failure_test: "If no recommendation is made, it fails."
  - id: research_paper_explanation
    deck_job: research_paper_deck
    audience_current_belief: "This paper has many details."
    desired_belief: "The core method, evidence, and limitation are clear enough to evaluate."
    narrative_risk: "paper-order slide dump"
    required_beats: [problem_context, method_thesis, mechanism, results, limitation, implication]
    key_slide_functions: [reframe, mechanism_step, proof, synthesis, close]
    proof_standard: "Figures/tables must support the action title, not decorate it."
    failure_test: "If source order equals slide order, it fails."
  - id: course_transformation
    deck_job: course_or_workshop
    audience_current_belief: "I will learn a curriculum."
    desired_belief: "I will move from current constraint to a concrete capability."
    narrative_risk: "module list"
    required_beats: [mirror_language, transformation, hidden_obstacles, method, practice, enrollment_path]
    key_slide_functions: [emotional_anchor, reframe, mechanism_step, artifact_reveal, cta_concrete]
    proof_standard: "Learner examples and practice moments must be concrete."
    failure_test: "If it reads like a syllabus before transformation, it fails."
  - id: design_system_audit
    deck_job: design_system_audit
    audience_current_belief: "The UI needs polish."
    desired_belief: "The design system has structural gaps with prioritized remediation."
    narrative_risk: "subjective design critique"
    required_beats: [standard, observed_gaps, impact, root_cause, remediation_map, decision]
    key_slide_functions: [reframe, proof, contrast, synthesis, cta_concrete]
    proof_standard: "Every critique maps to component/token/evidence and user impact."
    failure_test: "If feedback is taste-based, it fails."
  - id: incident_postmortem_learning
    deck_job: incident_postmortem
    audience_current_belief: "A thing broke and was fixed."
    desired_belief: "The system failure has causes, controls, and owners to prevent recurrence."
    narrative_risk: "blame or chronology only"
    required_beats: [impact, timeline, contributing_factors, root_cause, controls, owners]
    key_slide_functions: [proof, mechanism_step, contrast, synthesis, cta_concrete]
    proof_standard: "Each action has owner, due date, and prevention logic."
    failure_test: "If it ends at timeline without controls, it fails."
  - id: qbr_operating_review
    deck_job: qbr_operating_review
    audience_current_belief: "We are reviewing status."
    desired_belief: "We know what changed, why, what matters next, and what to decide."
    narrative_risk: "status theater"
    required_beats: [executive_answer, changes, drivers, blockers, decisions, next_commitments]
    key_slide_functions: [cover, proof, contrast, synthesis, cta_concrete]
    proof_standard: "Every status signal maps to driver or decision."
    failure_test: "If no decision changes after the meeting, it fails."
  - id: compliance_readiness
    deck_job: compliance_review
    audience_current_belief: "Compliance is a checklist."
    desired_belief: "Readiness depends on evidence quality, control owners, and residual risk."
    narrative_risk: "checkbox theater"
    required_beats: [standard, control_map, evidence_quality, residual_risk, remediation, signoff]
    key_slide_functions: [reframe, proof, contrast, synthesis, cta_concrete]
    proof_standard: "Each control has evidence, owner, status, and residual risk."
    failure_test: "If green status lacks evidence, it fails."
  - id: market_landscape_positioning
    deck_job: market_landscape
    audience_current_belief: "The market is crowded."
    desired_belief: "The landscape reveals a clear positioning wedge."
    narrative_risk: "logo soup"
    required_beats: [category_frame, axes, clusters, whitespace, wedge, implication]
    key_slide_functions: [reframe, contrast, proof, synthesis, close]
    proof_standard: "Axes and clusters must be justified with observable criteria."
    failure_test: "If the map is decorative, it fails."
  - id: roadmap_planning
    deck_job: roadmap_planning
    audience_current_belief: "We need to plan features."
    desired_belief: "Sequencing follows constraints, dependencies, and value unlock."
    narrative_risk: "feature inventory"
    required_beats: [strategy_constraint, dependency_map, sequencing_logic, tradeoffs, decision]
    key_slide_functions: [reframe, mechanism_step, contrast, synthesis, cta_concrete]
    proof_standard: "Each roadmap item traces to value, dependency, risk, or requirement."
    failure_test: "If order is unexplained, it fails."
  - id: customer_case_study
    deck_job: customer_case_study
    audience_current_belief: "This is a success story."
    desired_belief: "The mechanism created a specific before/after that can transfer."
    narrative_risk: "testimonial fluff"
    required_beats: [before, constraint, intervention, mechanism, result, transfer]
    key_slide_functions: [tension_amplify, mechanism_step, proof, synthesis, cta_concrete]
    proof_standard: "Before/after must use concrete metric, artifact, or quote."
    failure_test: "If transferability is not explained, it fails."
  - id: hiring_onboarding
    deck_job: hiring_onboarding
    audience_current_belief: "We need role information."
    desired_belief: "The candidate/new hire knows the mission, standards, first outcomes, and fit criteria."
    narrative_risk: "HR checklist"
    required_beats: [mission, role_context, success_profile, first_30_days, support_system, next_step]
    key_slide_functions: [cover, reframe, mechanism_step, synthesis, cta_concrete]
    proof_standard: "Expectations must map to outcomes and evaluation criteria."
    failure_test: "If it only lists responsibilities, it fails."
  - id: survey_report
    deck_job: survey_report
    audience_current_belief: "Survey results are descriptive."
    desired_belief: "Responses reveal a decision-relevant pattern and its implication."
    narrative_risk: "chart parade"
    required_beats: [question, sample, pattern, interpretation, implication, decision]
    key_slide_functions: [proof, reframe, contrast, synthesis, cta_concrete]
    proof_standard: "Sample, method, and confidence caveat must be explicit."
    failure_test: "If every chart gets equal weight, it fails."
  - id: portfolio_review
    deck_job: portfolio_review
    audience_current_belief: "We need to review allocations."
    desired_belief: "Capital/resource allocation should shift based on value, risk, and optionality."
    narrative_risk: "static allocation report"
    required_beats: [current_allocation, performance, risk, opportunity, recommendation, decision]
    key_slide_functions: [proof, contrast, synthesis, cta_concrete]
    proof_standard: "Each recommendation has tradeoff and downside."
    failure_test: "If allocation changes are not proposed, it fails."
  - id: operating_model
    deck_job: operating_model
    audience_current_belief: "We need an org/process chart."
    desired_belief: "The operating model changes accountability, handoffs, and decision speed."
    narrative_risk: "org chart theater"
    required_beats: [constraint, current_state, target_model, handoffs, governance, rollout]
    key_slide_functions: [reframe, contrast, mechanism_step, synthesis, cta_concrete]
    proof_standard: "Every role/process change maps to a bottleneck or decision."
    failure_test: "If governance is missing, it fails."
  - id: proposal_close
    deck_job: proposal_close
    audience_current_belief: "We are evaluating a proposal."
    desired_belief: "The next step is low-friction, specific, and worth taking now."
    narrative_risk: "weak close"
    required_beats: [recap, fit, risk_reversal, next_step, owner_date]
    key_slide_functions: [synthesis, objection_neutralize, cta_concrete, close]
    proof_standard: "CTA includes owner, date, artifact, and consequence of delay."
    failure_test: "If CTA is 'let us know', it fails."
  - id: product_strategy
    deck_job: product_strategy
    audience_current_belief: "We need a roadmap."
    desired_belief: "The product strategy follows a customer gap and capability thesis."
    narrative_risk: "feature backlog in slide form"
    required_beats: [market_shift, customer_gap, product_thesis, capability_map, tradeoffs, roadmap]
    key_slide_functions: [tension_amplify, reframe, mechanism_step, contrast, synthesis]
    proof_standard: "Every roadmap move traces to customer gap, benchmark, or strategic constraint."
    failure_test: "If roadmap can be shuffled without changing logic, it fails."
  - id: thought_leadership_category
    deck_job: thought_leadership
    audience_current_belief: "This is a perspective piece."
    desired_belief: "The category frame changes how they interpret the problem."
    narrative_risk: "essay in slides"
    required_beats: [pattern, enemy, category_frame, proof, implication, invitation]
    key_slide_functions: [emotional_anchor, reframe, proof, synthesis, close]
    proof_standard: "The category frame needs evidence, contrast, and implication."
    failure_test: "If the idea does not change a decision or behavior, it fails."
  - id: internal_strategy_memo
    deck_job: strategy_memo
    audience_current_belief: "We need alignment."
    desired_belief: "We agree on the strategic choice, tradeoff, and operating consequence."
    narrative_risk: "alignment without choice"
    required_beats: [context, choice, tradeoff, operating_implication, risks, decision]
    key_slide_functions: [reframe, contrast, mechanism_step, synthesis, cta_concrete]
    proof_standard: "Every strategic choice states what it rejects."
    failure_test: "If no tradeoff is explicit, it fails."

release_policy:
  pass_if:
    - at_least_24_narrative_cases_defined
    - every_case_has_current_and_desired_belief
    - every_case_has_failure_test
    - every_case_has_required_beats_and_key_slide_functions
  block_if:
    - case_is_topic_outline
    - no_proof_standard
    - no_decision_or_close_path
```


## Referência: references/source/templates/runtime/provider-routing.yaml

```yaml
version: 1
runtime_jobs:
  - id: provider_capability_routing
    mode: provider_selection
    pick_when:
      - User asks for local/private generation, BYOK, Ollama, LM Studio, OpenAI-compatible API, or image generation.
      - A deck run needs text, image, research, vision, or export providers with different capabilities.
      - The skill must be shared with users who will bring their own model/provider.
    inputs:
      - privacy_requirement
      - model_provider_preference
      - image_provider_preference
      - required_capabilities
      - available_environment
    steps:
      - classify_required_capabilities
      - select_text_provider
      - select_image_provider
      - select_vision_provider
      - declare_missing_keys_or_local_models
      - define_fallbacks
      - record_provider_decisions
    outputs:
      - provider_selection
      - required_env_vars
      - fallback_policy
      - provider_risk_notes
    failure_policy:
      continue_on_error: true
      block_if_missing:
        - required_capabilities
    absorbed_from:
      - Presenton/providerUtils.ts
      - Presenton/providerConstants.ts
      - presentation-ai/modelProvider state

capability_matrix:
  text_generation:
    primary:
      - codex
      - openai
      - anthropic
      - google
      - openrouter
      - litellm
      - ollama
      - lmstudio
      - custom_openai_compatible
    local_first:
      - ollama
      - lmstudio
      - custom_openai_compatible
  image_generation:
    primary:
      - gpt_image
      - gemini_flash
      - pexels
      - pixabay
      - comfyui
      - open_webui
    fallback_by_text_provider:
      openai: gpt_image
      google: gemini_flash
      local: pexels
      unknown: pexels
  vision_eval:
    primary:
      - openai_vision
      - google_vision
      - local_multimodal
    fallback:
      - manual_rendered_eval
  research:
    primary:
      - web_search
      - scholar_search
      - local_file_parser
    fallback:
      - user_supplied_sources

required_env_vars_by_provider:
  openai: [OPENAI_API_KEY, OPENAI_MODEL]
  anthropic: [ANTHROPIC_API_KEY, ANTHROPIC_MODEL]
  google: [GOOGLE_API_KEY, GOOGLE_MODEL]
  azure: [AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT]
  openrouter: [OPENROUTER_API_KEY, OPENROUTER_MODEL]
  litellm: [LITELLM_BASE_URL, LITELLM_MODEL]
  ollama: [OLLAMA_URL, OLLAMA_MODEL]
  lmstudio: [LMSTUDIO_BASE_URL, LMSTUDIO_MODEL]
  custom_openai_compatible: [CUSTOM_LLM_URL, CUSTOM_MODEL]
  pexels: [PEXELS_API_KEY]
  pixabay: [PIXABAY_API_KEY]
  comfyui: [COMFYUI_URL]

selection_rules:
  - If privacy is strict, prefer local providers and avoid external image/search calls unless user approves.
  - Text, image, vision, and research providers may differ.
  - Missing provider keys are blockers only when the selected runtime truly needs that capability.
  - If local model is requested, record whether the model must already be pulled or downloaded.
  - Do not hardcode one vendor into deck logic; provider choice is a runtime decision.
```


## Referência: references/source/templates/runtime/render-lock.yaml

```yaml
version: 1
purpose: >
  Machine-readable execution lock for deck rendering. This is the anti-drift
  companion to design-direction/deck-spec: agents and renderers re-read this
  short contract before authoring or exporting each slide.
absorbed_from:
  - ppt-master/spec_lock.md
  - ppt-master/docs/technical-design.md

render_lock_contract:
  required_sections:
    - canvas
    - colors
    - typography
    - chart_palette
    - image_style_lock
    - slide_visual_locks
    - forbidden_features
    - asset_status
  rules:
    - Renderers must use values from render-lock instead of reinterpreting design-direction prose.
    - A deck-wide visual style change updates render-lock first, then affected slide specs.
    - Slide-specific overrides must be explicit; silent visual drift is a QA failure.
    - If render-lock conflicts with design-direction prose, render-lock wins for execution.

canvas:
  aspect_ratio: "16:9"
  width_px: 1920
  height_px: 1080
  safe_margin_px: 72

colors:
  background: ""
  surface: ""
  surface_alt: ""
  text: ""
  muted_text: ""
  border: ""
  accent: ""
  warning: ""
  positive: ""
  negative: ""

typography:
  heading_family: ""
  body_family: ""
  mono_family: ""
  heading_weight: 700
  body_weight: 400
  body_px: 28
  title_px: 56
  min_body_px: 20

chart_palette:
  primary: []
  neutral: ""
  grid: ""
  highlight: ""
  rules:
    - Chart colors must come from chart_palette unless a sourced brand override is declared.
    - Axis, labels, and legends remain native/editable when PPTX output is requested.

image_style_lock:
  rendering_family: "none | editorial_photo | vector_illustration | 3d_isometric | sketch_notes | product_mockup | interface_capture"
  palette_policy: "native_theme | warm_accent | cool_accent | grayscale_accent | brand_exact"
  texture_policy: "none | subtle | strong"
  text_policy_default: "native_overlay"
  prompt_rules:
    - The deck-wide rendering_family and palette_policy must be reused across generated images.
    - Exact labels, numbers, formulas, citations, UI copy, and chart text must remain native.
    - Product-representational images require source_or_generation_model and conceptual/real flag.

slide_visual_locks:
  - slide_id: "s01"
    slide_function: ""
    layout_family: ""
    composition_pattern: ""
    image_type: ""
    chart_or_diagram_template: ""
    native_overlay_plan: ""
    allowed_overrides: []

forbidden_features:
  svg:
    - foreignObject
    - script
    - iframe
    - animate
    - textPath
    - symbol_use_without_expansion
    - mask_without_powerpoint_fallback
  pptx:
    - rasterized_action_title
    - residual_placeholder_tokens
    - uneditable_core_claim_text
    - chart_as_image_when_data_editability_required

asset_status:
  - asset_id: ""
    slide_id: ""
    role: ""
    source: ""
    status: "resolved | degraded | blocked"
    attribution_required: false
    local_path: ""

qa_blockers:
  - missing_required_section
  - empty_canonical_colors
  - undeclared_slide_visual_lock_for_key_slide
  - generated_image_without_style_lock
  - pptx_requested_with_forbidden_feature
```


## Referência: references/source/templates/runtime/runtime-gap-absorption-corpus.yaml

```yaml
version: 1
name: runtime-gap-absorption-corpus
purpose: >
  Capability corpus for the non-narrative gaps that still limit the consolidated
  benchmark score. These are not claims of finished app/runtime implementation;
  they are acceptance contracts that turn remaining gaps into buildable slices.

gap_groups:
  - id: render_pptx
    group: Renderização
    target_score_path: "65 -> 85 -> 95"
    absorbed_from: [ppt-master, powerpoint-skill, PPTAgent]
    must_build:
      - drawingml_shape_export
      - native_chart_export
      - html_to_pptx_render_equivalence
      - overlap_boundary_checker
      - powerpoint_roundtrip_report
    acceptance:
      - exported_file_exists_and_reopens
      - text_boxes_do_not_clip
      - charts_keep_editable_data_when_required
      - rasterized_elements_are_reported
      - screenshot_preview_matches_html_with_declared_tolerance
  - id: editor_prompt_to_edit
    group: Editor
    target_score_path: "50 -> 75 -> 90"
    absorbed_from: [banana-slides, presentation-ai, Presenton]
    must_build:
      - region_selection_model
      - scoped_edit_diff
      - undo_redo_history
      - live_preview_contract
      - review_comment_model
    acceptance:
      - edit_preserves_unselected_regions
      - every_edit_has_before_after_diff
      - undo_restores_prior_slide_state
      - localized_regen_reruns_visual_qa
      - comments_attach_to_slide_or_region
  - id: distribution_analytics
    group: Distribuição
    target_score_path: "33 -> 65 -> 85"
    absorbed_from: [presentation-ai]
    must_build:
      - export_package_manifest
      - share_link_contract
      - permission_policy
      - view_event_schema
      - crm_followup_signal
    acceptance:
      - share_artifact_has_public_private_mode
      - export_manifest_lists_formats_and_paths
      - view_event_has_deck_slide_session_timestamp
      - engagement_summary_produces_actionable_followup
  - id: multimedia_narration
    group: Multimídia
    target_score_path: "41 -> 70 -> 90"
    absorbed_from: [PresentAgent-2, ppt-master]
    must_build:
      - speaker_notes_narration_contract
      - tts_provider_routing
      - slide_audio_sync_map
      - video_export_job_contract
      - media_asset_pipeline
    acceptance:
      - notes_have_timing_and_transition
      - spoken_cues_match_visible_slide_elements
      - media_assets_have_ids_and_usage_policy
      - video_export_report_lists_audio_and_slide_timing
  - id: infra_local_packaging
    group: Infra
    target_score_path: "40 -> 65 -> 85"
    absorbed_from: [Presenton]
    must_build:
      - local_runtime_manifest
      - docker_compose_contract
      - desktop_packaging_contract
      - offline_model_policy
      - upgrade_and_storage_policy
    acceptance:
      - local_runtime_can_run_without_remote_required_services
      - env_vars_are_documented_without_secrets
      - storage_paths_are_declared
      - upgrade_policy_preserves_user_decks
  - id: automation_api_mcp
    group: Automação
    target_score_path: "69 -> 85 -> 95"
    absorbed_from: [Presenton, banana-slides]
    must_build:
      - job_state_events
      - api_create_edit_export_routes
      - mcp_tool_contract
      - batch_queue_policy
      - resumable_job_report
    acceptance:
      - every_job_has_state_progress_artifacts_and_errors
      - api_routes_are_reproducible_from_cli_contract
      - mcp_tools_do_not_bypass_source_of_truth_policy
      - batch_jobs_can_resume_or_fail_cleanly

release_policy:
  pass_if:
    - every_gap_group_has_target_score_path
    - every_gap_group_has_must_build_and_acceptance
    - every_gap_group_maps_to_benchmark_group
  block_if:
    - capability_claim_without_acceptance_contract
    - runtime_score_raised_without_artifact_or_test_plan
```


## Referência: references/source/templates/runtime/slide-function-map-contract.yaml

```yaml
version: 1
name: slide-function-map-contract
purpose: >
  Self-contained contract for mapping every slide to an audience movement and
  narrative function before slide copy is written.

independence_rule: >
  Use this bundled map contract inside slide-creator. It replaces any need for
  squad-local validators or tasks.

required_output:
  file: slide-function-map.yaml
  root_key: slide_function_map
  required_fields:
    - deck_id
    - story_arc_ref
    - entries

entry_schema:
  required_fields:
    - slide_id
    - beat_ref
    - function
    - audience_movement
  recommended_fields:
    - slide_type
    - density_target
    - merged_from_topics
    - could_be_cut_if
    - action_title_draft
    - proof_requirement

function_enum:
  - cover
  - section_divider
  - reframe
  - proof
  - contrast
  - mechanism_step
  - demo_setup
  - demo_payoff
  - artifact_reveal
  - objection_neutralize
  - synthesis
  - tension_amplify
  - emotional_anchor
  - quiet_pause
  - cta_concrete
  - close
  - appendix

density_targets:
  low:
    max_visible_words: 24
    use_when: "Cover, reframe, emotional anchor, quiet pause, close."
  medium:
    max_visible_words: 45
    use_when: "Mechanism, proof, contrast, synthesis."
  high:
    max_visible_words: 90
    use_when: "Tables, appendices, benchmark matrix, financial detail."

audience_movement_rules:
  must_describe: "The belief, question, confidence, or decision state the audience moves into."
  forbidden_prefixes:
    - explicar
    - apresentar
    - falar
    - mostrar
    - listar
    - descrever
    - explain
    - present
    - show
    - list
    - describe
  bad_examples:
    - "Explicar o mercado"
    - "Mostrar o produto"
    - "Apresentar os diferenciais"
  good_examples:
    - "They stop treating the problem as tooling and see it as a throughput constraint."
    - "They believe the mechanism is repeatable because the artifact proves the workflow."
    - "They know the next decision, owner, and deadline."

validation:
  block_if:
    - any_slide_without_function
    - any_slide_without_audience_movement
    - audience_movement_starts_with_forbidden_prefix
    - function_not_in_enum
    - no_demo_payoff_or_artifact_reveal_for_product_or_process_deck
    - no_cta_concrete_or_close
    - slide_count_more_than_2x_planned_entries
  warn_if:
    - three_consecutive_slides_same_function
    - more_than_two_consecutive_same_layout_family
    - slide_could_be_cut_if_is_empty_on_long_deck

compression_rule: >
  Preserve functions, not topics. Multiple source topics can merge into one
  slide when they produce the same audience movement.
```


## Referência: references/source/templates/runtime/source-of-truth-policy.yaml

```yaml
version: 1
purpose: >
  Conflict-resolution policy for long slide jobs. Prevents stale memory,
  old process logs, imported decks, and newer user instructions from silently
  overriding the live deck package.
absorbed_from:
  - Presenton source-of-truth policy

source_of_truth_policy:
  precedence_order:
    - latest_verified_export
    - latest_deck_spec
    - explicit_user_instruction_current_turn
    - source_ledger
    - imported_template_manifest
    - briefing_normalized
    - research_notes
    - prior_chat_or_memory
  rules:
    - Tool/readback output from the current run wins over memory.
    - Latest explicit user constraint wins over older briefing text.
    - Factual claims must resolve through source-ledger before being promoted to visible copy.
    - Imported template metadata informs layout and style but cannot override the deck objective.
    - If a conflict changes audience, offer, claim, or export requirement, record conflict_resolution.

conflict_resolution:
  - conflict_id: ""
    field: ""
    sources_in_conflict: []
    winning_source: ""
    reason: ""
    affected_artifacts: []
    qa_required: []

blockers:
  - factual_claim_conflict_unresolved
  - user_instruction_conflict_unresolved
  - export_requirement_conflict_unresolved
  - deck_spec_changed_without_policy_update
```


## Referência: references/source/templates/runtime/speaker-notes-narration-contract.yaml

```yaml
version: 1
name: speaker-notes-narration-contract
purpose: >
  Contract for speaker notes, narration, and timing. It keeps talk track,
  slide content, proof, and CTA aligned without turning notes into a script
  dump.

required_output:
  file: speaker-notes-narration.yaml
  root_key: speaker_notes_narration

note_modes:
  - id: executive_talk_track
    use_when: [board_update, sales_proposal, investor_pitch, strategy_memo]
    max_words_per_slide: 90
    style: "crisp, decision-oriented, no transcript feel"
  - id: teaching_talk_track
    use_when: [webinar, course_or_workshop, training]
    max_words_per_slide: 130
    style: "clear explanation with examples and transitions"
  - id: demo_talk_track
    use_when: [product_demo, api_or_mcp_demo, technical_architecture_review]
    max_words_per_slide: 110
    style: "setup, action, observation, payoff"
  - id: narrative_talk_track
    use_when: [brand_manifesto, thought_leadership, case_study]
    max_words_per_slide: 100
    style: "memorable, paced, emotionally restrained"

slide_note_schema:
  required_fields:
    - slide_id
    - talk_track_goal
    - opening_line
    - proof_or_example_to_voice
    - transition_out
    - timing_seconds
  optional_fields:
    - demo_action
    - pause_or_question
    - objection_to_preempt
    - words_to_avoid

narration_sync:
  required_for:
    - video_export
    - recorded_webinar
    - async_pitch
  fields:
    - slide_id
    - start_time
    - end_time
    - spoken_cue
    - visual_cue
    - asset_refs
  block_if:
    - spoken_cue_references_visual_not_on_slide
    - narration_exceeds_slide_timing_by_more_than_20_percent
    - proof_claim_spoken_without_source_or_assumption_label
    - cta_spoken_without_visible_next_step

qa:
  pass_if:
    - notes_support_action_title
    - notes_do_not_repeat_visible_copy_verbatim
    - every_transition_preserves_story_flow
    - timing_total_matches_requested_duration_within_15_percent
  block_if:
    - notes_are_full_transcript_without_slide_intent
    - notes_introduce_unsourced_claims
    - notes_change_the_offer_or_decision
    - demo_action_missing_for_demo_slide

score_relevance:
  narration_audio__speaker_notes: "Structured talk track with timing, proof, transition and mode."
  narration_audio__audio_sync: "Explicit spoken/visual cue mapping for recorded decks."
  video_export__media_asset_pipeline: "Asset refs and cue timing prepare video export workers."
```


## Referência: references/source/templates/runtime/story-arc-contract.yaml

```yaml
version: 1
name: story-arc-contract
purpose: >
  Self-contained narrative arc contract for slide-creator decks. This absorbs
  the evolved slides-creator squad arc discipline without requiring any squad
  file, agent, task, or repository path at runtime.

independence_rule: >
  This bundled contract is the authority inside the skill. Do not reference
  squads/slides-creator or route to squad agents to make the deck work.

required_output:
  file: story-arc.yaml
  root_key: story_arc
  required_fields:
    - deck_id
    - arc_type
    - beats

arc_types:
  - educational_workshop
  - executive_pitch
  - sales_narrative
  - thought_leadership
  - product_demo
  - board_update
  - case_study
  - webinar
  - financial_update
  - strategy_memo

beat_types:
  opening:
    valid_values: [hook, situation, context, cold_open]
    job: "Create relevance and orientation without becoming an agenda slide."
  tension:
    valid_values: [complication, tension, stakes, cost_of_inaction]
    job: "Make the current belief or current process feel insufficient."
  reframe:
    valid_values: [reframe, insight, thesis, governing_thought]
    job: "Replace the old frame with the central deck thesis."
  proof:
    valid_values: [proof, evidence, case, benchmark, data, demo_setup]
    job: "Earn belief with sourced facts, examples, demo, or artifacts."
  mechanism:
    valid_values: [mechanism, model, framework, process, operating_system]
    job: "Show how the thesis becomes repeatable action."
  payoff:
    valid_values: [demo_payoff, artifact_reveal, before_after, result]
    job: "Let the audience see the promised outcome concretely."
  close:
    valid_values: [plan, decision, cta, next_steps, close]
    job: "Convert belief into an explicit decision or action."

beat_schema:
  required_fields:
    - beat_id
    - beat_type
    - narrative_function
    - slides_estimated
  optional_fields:
    - source_topics
    - evidence_refs
    - design_hints
    - objection_addressed
    - emotional_state_before
    - emotional_state_after
  constraints:
    max_beats: 8
    slides_estimated_min: 1
    narrative_function_min_chars: 32

validation:
  required_sequence_presence:
    - at_least_one_opening_or_tension
    - at_least_one_reframe_or_thesis
    - at_least_one_proof_mechanism_or_payoff
    - at_least_one_close_or_cta
  consistency_checks:
    - beat_ids_are_unique
    - slide_function_map_entries_reference_existing_beats
    - sum_slides_estimated_matches_slide_function_map_with_tolerance_20_percent
    - no_more_than_8_beats
  block_if:
    - beats_missing
    - topic_list_arc
    - missing_payoff
    - missing_cta_or_close
    - narrative_function_is_generic_topic

anti_patterns:
  topic_list_arc:
    symptom: "Beat names are only content categories such as mercado, produto, preço."
    fix: "Rewrite beats as audience movement: what must change in belief at that moment."
  missing_payoff:
    symptom: "Deck explains the mechanism but never shows an artifact, demo, result, or before/after."
    fix: "Add proof/demo/artifact_reveal before CTA."
  monolog_deck:
    symptom: "Every beat pushes more information without objection, contrast, or decision."
    fix: "Insert tension, objection neutralization, and a concrete decision point."
  apostila:
    symptom: "The arc preserves source-document order and behaves like a handout."
    fix: "Compress source material into a persuasive or didactic journey."
```


## Referência: references/source/templates/runtime/storyboard-edit-contract.yaml

```yaml
version: 1
name: storyboard-edit-contract
purpose: >
  Define prompt-to-edit behavior at storyboard level. This is the bridge between
  the current deck package and a future executable editor: edits must preserve
  narrative intent, source truth, design rhythm, and unselected slide regions.

edit_request_schema:
  required_fields:
    - edit_id
    - user_prompt
    - target_scope
    - target_slides
    - intended_outcome
    - protected_artifacts
    - expected_diff_type
  target_scopes:
    - deck
    - section
    - slide
    - region
    - object
    - speaker_notes
  expected_diff_types:
    - narrative_reframe
    - tighten_copy
    - redesign_layout
    - change_theme
    - replace_visual
    - add_proof
    - reduce_density
    - change_cta

preservation_rules:
  - id: preserve_belief_shift
    applies_to: [deck, section, slide]
    rule: "The desired belief and audience movement cannot change unless the edit explicitly asks for strategy change."
  - id: preserve_sources
    applies_to: [deck, section, slide, region, object]
    rule: "Sourced claims cannot be rewritten materially without source-ledger update."
  - id: preserve_unselected_regions
    applies_to: [region, object]
    rule: "A region/object edit must leave other regions byte-identical or report the unavoidable cascade."
  - id: preserve_design_moment
    applies_to: [slide, region]
    rule: "The selected narrative-design moment archetype stays unless edit explicitly changes the slide job."
  - id: preserve_render_lock
    applies_to: [deck, section, slide]
    rule: "Theme, fonts, grid, image policy, and forbidden features remain locked unless the edit targets them."

diff_contract:
  required_sections:
    - edit_summary
    - before
    - after
    - changed_artifacts
    - unchanged_artifacts
    - qa_rerun
    - risks_introduced
  before_after_required_fields:
    - slide_id
    - action_title
    - slide_function
    - narrative_design_moment
    - selected_template
    - visible_copy_summary
    - visual_summary
  qa_rerun_by_diff_type:
    narrative_reframe: [belief_shift_gate, slide_function_gate, cta_gate]
    tighten_copy: [density_gate, action_title_gate, claim_integrity_gate]
    redesign_layout: [visual_fit_gate, density_gate, rendered_key_slide_gate]
    change_theme: [contrast_gate, brand_consistency_gate, theme_runtime_gate]
    replace_visual: [media_relevance_gate, proof_visibility_gate, render_risk_gate]
    add_proof: [source_ledger_gate, evidence_visibility_gate, claim_integrity_gate]
    reduce_density: [meaning_preservation_gate, scan_path_gate, speaker_note_gate]
    change_cta: [proof_before_ask_gate, specificity_gate, owner_date_gate]

edit_resolution_policy:
  if_prompt_is_ambiguous:
    - infer_low_risk_scope
    - keep_strategy_constant
    - return_assumptions_in_diff
  if_edit_conflicts_with_source_truth:
    - block_or_request_source_update
    - do_not_silently_change_evidence
  if_edit_conflicts_with_render_lock:
    - report_render_lock_conflict
    - require_explicit_override
  if_edit_breaks_story_arc:
    - propose_alternative_edit_that_preserves_arc
    - mark_original_request_as_story_risk

acceptance:
  pass_if:
    - every_edit_has_before_after_diff
    - every_changed_slide_reruns_relevant_qa
    - unselected_regions_are_listed_as_preserved_or_cascade_reported
    - source_or_render_lock_conflicts_are_explicit
  block_if:
    - edit_changes_sourced_claim_without_ledger
    - edit_changes_story_arc_without_strategy_override
    - edit_hides_visual_or_density_regression
    - region_edit_modifies_unselected_region_without_reporting_it
```


## Referência: references/source/templates/runtime/storyboard-render-bridge.yaml

```yaml
version: 1
name: storyboard-render-bridge
purpose: >
  Bridge narrative and design into an execution-ready storyboard. Use this
  before rendering/export so the deck keeps the belief shift, slide function,
  visual system, density, proof, and export constraints connected.

required_output:
  file: storyboard-render-bridge.yaml
  root_key: storyboard_render_bridge

storyboard_contract:
  required_fields:
    - deck_id
    - selected_narrative_case
    - selected_design_fixture_set
    - slides
    - continuity_checks
    - render_readiness

slide_storyboard_schema:
  required_fields:
    - slide_id
    - beat_ref
    - audience_movement
    - action_title
    - slide_function
    - selected_slide_template
    - selected_visual_template
    - selected_wireframe
    - density_target
    - proof_requirement
    - design_role
    - render_risk
  optional_fields:
    - rejected_templates
    - speaker_note_intent
    - interaction_or_demo_moment
    - export_notes

design_roles:
  - cover
  - reframe
  - tension
  - mechanism
  - proof
  - demo
  - decision
  - appendix
  - close

continuity_checks:
  - id: belief_shift_continuity
    question: "Does each slide move the audience closer to the desired belief?"
    block_if:
      - audience_movement_missing
      - slide_only_explains_topic
      - no_escalation_between_adjacent_slides
  - id: visual_rhythm_continuity
    question: "Does visual variety support the story instead of becoming a gallery?"
    block_if:
      - three_consecutive_same_layout_family
      - visual_style_changes_without_narrative_reason
      - dense_slide_not_followed_by_breathing_room_when_needed
  - id: proof_path_continuity
    question: "Does proof appear before asks and risky claims?"
    block_if:
      - claim_without_evidence_or_assumption_label
      - offer_or_decision_before_proof
      - demo_without_payoff
  - id: render_export_continuity
    question: "Can the storyboard survive render/export without losing meaning?"
    block_if:
      - action_title_too_long_for_selected_wireframe
      - chart_or_table_has_no_data_contract
      - source_label_or_cta_at_clipping_risk

render_readiness:
  pass_if:
    - every_slide_has_template_visual_wireframe_and_density
    - every_key_slide_has_render_risk_and_mitigation
    - every_claim_heavy_slide_has_proof_requirement
    - every_exportable_slide_has_export_notes_or_no_export_risk
  block_if:
    - storyboard_skips_design_direction
    - slide_function_and_visual_template_conflict
    - density_target_exceeds_selected_wireframe_capacity
    - key_slide_missing_render_risk

score_relevance:
  consultative_narrative__belief_shift: "Keeps belief movement visible at slide level."
  slide_structure_planning__slide_function_map: "Makes slide function executable through visual/template selection."
  visual_layout_quality__visual_density_control: "Connects density target to selected wireframe capacity."
  qa_evaluation_rubric__visual_qa: "Creates a render-risk checklist before output."
  html_to_pptx_export__render_equivalence: "Prepares slide-level export notes before conversion."
```


## Referência: references/source/templates/runtime/template-example-routing.yaml

```yaml
version: 1
runtime_jobs:
  - id: template_examples_for_prompt
    mode: template_selection
    pick_when:
      - The generator needs examples of allowed slide structures.
      - User requests many slides and layout consistency matters.
      - A slide should override the default template selected for the deck.
    inputs:
      - selected_template_ids
      - outline_items
      - template_registry
    steps:
      - select_template_candidates_by_slide_function
      - serialize_template_examples_for_prompt
      - attach_usage_hint_per_template
      - apply_outline_template_overrides
      - reject_templates_that_violate_density_or_media_rules
    outputs:
      - serialized_template_examples
      - outline_template_overrides
      - template_selection_rationale
    failure_policy:
      continue_on_error: true
      block_if_missing:
        - template_registry
    absorbed_from:
      - presentation-ai/template-serializer.ts
      - presentation-ai/templates.tsx

template_example_contract:
  required_fields:
    - template_id
    - template_name
    - category
    - use_for
    - example_structure
  serialization_rules:
    - Include structure examples only for selected templates.
    - Keep examples short enough to guide the model without crowding the prompt.
    - Include category usage hint, not just template name.
    - Per-outline override wins over automatic category selection.

override_rules:
  - If a slide has a decisive function, allow explicit template override.
  - If an override repeats the same layout more than twice in sequence, reroute or justify.
  - If selected template cannot host the required evidence/media, choose a more suitable visual template.
```


## Referência: references/source/templates/runtime/template-selection-report.yaml

```yaml
version: 1
purpose: >
  Auditable template and visual selection report. A selection is not complete
  until the chosen template and runners-up are recorded with deck-specific
  rejection reasons.
absorbed_from:
  - ppt-master/design_spec_reference.md runners-up audit rule
  - PPTAgent/layout_selector.yaml reasoning output

template_selection_report:
  deck_id: ""
  generated_at: ""
  selection_scope: "deck | slide | visual | chart | import_pack"
  rules:
    - Every key slide must record selected template and at least two runners-up when alternatives exist.
    - Rejected runners-up must cite this deck's slide function, evidence, audience, or media constraints.
    - Do not use generic rejection reasons such as "less suitable" without a concrete mismatch.
    - If using an indexed chart/template catalog, preserve the source summary quote when available.

selections:
  - slide_id: "s01"
    slide_function: ""
    selected:
      id: ""
      name: ""
      source_registry: ""
      source_quote: ""
    selected_reason: ""
    fit_scores:
      content_fit: 0
      visual_fit: 0
      evidence_fit: 0
      audience_fit: 0
      export_fit: 0
    rejected_runners_up:
      - id: ""
        name: ""
        rejected_reason: ""
      - id: ""
        name: ""
        rejected_reason: ""
    constraints_checked:
      - slot_count
      - text_length
      - media_area
      - evidence_visibility
      - pptx_editability
    final_confidence: "high | medium | low"
    qa_status: "pass | warn | fail"

blockers:
  - selected_template_missing_reason
  - no_runners_up_for_key_slide
  - rejected_reason_not_deck_specific
  - source_quote_missing_when_catalog_requires_quote
  - selected_template_conflicts_with_export_requirement
```


## Referência: references/source/templates/runtime/theme-runtime-snapshot-suite.yaml

```yaml
version: 1
name: theme-runtime-snapshot-suite
purpose: >
  Snapshot suite for proving that theme tokens are not decorative metadata.
  A theme must reach slide backgrounds, text styles, charts, diagrams, tables,
  callouts, media treatment, metadata, and export fallbacks.

minimum_reference_bar:
  theme_profiles_sampled: 12
  component_families: 10
  snapshot_cases: 16
  pass_floor_per_case: 95

component_families:
  - slide_background
  - title_block
  - body_text
  - metric_card
  - chart
  - diagram
  - table
  - callout
  - image_treatment
  - metadata_footer

snapshot_cases:
  - {id: boardroom_chart_table, theme_profile: boardroom_graphite, component_families: [slide_background, title_block, chart, table, metadata_footer], required_bindings: [background, text, muted_text, chart_palette, table_border]}
  - {id: consulting_matrix_decision, theme_profile: consulting_midnight, component_families: [title_block, metric_card, table, callout, metadata_footer], required_bindings: [accent, surface, border, muted_text, decision_accent]}
  - {id: founder_pitch_hero_proof, theme_profile: founder_pitch_light, component_families: [slide_background, title_block, image_treatment, metric_card, callout], required_bindings: [hero_overlay, accent, surface, text, proof_highlight]}
  - {id: technical_blueprint_diagram, theme_profile: technical_blueprint, component_families: [diagram, code_block, title_block, metadata_footer], required_bindings: [diagram_node, diagram_edge, code_mono, muted_text]}
  - {id: academic_paper_figure, theme_profile: academic_paper, component_families: [chart, table, body_text, metadata_footer], required_bindings: [figure_caption, table_header, citation_text, chart_palette]}
  - {id: saas_clean_product_demo, theme_profile: product_saas_clean, component_families: [slide_background, title_block, metric_card, image_treatment], required_bindings: [surface, accent, provider_badge, image_border]}
  - {id: high_contrast_accessible_table, theme_profile: high_contrast_accessible, component_families: [table, chart, callout, metadata_footer], required_bindings: [text, background, border, focus_ring, chart_palette]}
  - {id: brandbook_editorial_quote, theme_profile: brandbook_editorial, component_families: [title_block, callout, image_treatment, metadata_footer], required_bindings: [editorial_divider, mono_metadata, quote_text, accent]}
  - {id: redpine_operational_status, theme_profile: redpine_operational, component_families: [table, metric_card, diagram, metadata_footer], required_bindings: [status_positive, status_warning, status_negative, hairline_border]}
  - {id: aiox_cockpit_evidence_wall, theme_profile: aiox_cockpit_dark, component_families: [slide_background, metric_card, callout, metadata_footer], required_bindings: [cockpit_background, neon_accent, mono_metadata, evidence_border]}
  - {id: cyber_security_dark_incident, theme_profile: cyber_security_dark, component_families: [diagram, table, callout, chart], required_bindings: [severity_high, severity_medium, severity_low, diagram_edge]}
  - {id: legal_compliance_grid, theme_profile: legal_compliance, component_families: [table, metadata_footer, callout, body_text], required_bindings: [control_id, status_token, muted_text, border]}
  - {id: data_analytics_lab_scatter, theme_profile: data_analytics_lab, component_families: [chart, table, title_block, metadata_footer], required_bindings: [axis_grid, series_primary, series_secondary, annotation]}
  - {id: creator_webinar_offer, theme_profile: creator_webinar, component_families: [title_block, image_treatment, metric_card, callout], required_bindings: [cta_accent, testimonial_surface, hero_overlay, price_highlight]}
  - {id: startup_demo_neon_api, theme_profile: startup_demo_neon, component_families: [code_block, diagram, provider_badge, title_block], required_bindings: [code_mono, integration_accent, provider_badge, diagram_node]}
  - {id: enterprise_rfp_service_catalog, theme_profile: enterprise_rfp, component_families: [table, metric_card, callout, metadata_footer], required_bindings: [section_header, service_card, table_border, muted_text]}

snapshot_policy:
  pass_if:
    - every_case_has_theme_profile_component_families_required_bindings
    - every_required_binding_maps_to_declared_token_or_render_lock_role
    - charts_diagrams_tables_do_not_use_unmapped_default_colors
    - fallback_font_policy_is_declared_for_exportable_decks
  block_if:
    - theme_used_only_for_background_and_title
    - chart_or_diagram_ignores_theme
    - table_density_breaks_when_theme_switches
    - contrast_fails_after_theme_switch
```


## Referência: references/source/templates/runtime/trace-handoff.yaml

```yaml
version: 1
runtime_jobs:
  - id: traceable_slide_creation_flow
    mode: orchestration
    pick_when:
      - The process must be auditable, shareable, or reusable by other people.
      - User asks why a deck/process failed or wants the skill to improve over time.
      - Multiple critique perspectives are useful before final synthesis.
    inputs:
      - briefing
      - selected_templates
      - research_outputs
      - draft_deck_spec
      - rendered_eval
    steps:
      - compile_focused_working_set
      - run_parallel_review_universes
      - compact_handoffs_by_output_kind
      - synthesize_findings
      - produce_trace_report
      - update_revision_actions
    outputs:
      - working_set_manifest
      - stage_trace
      - typed_handoffs
      - synthesis_report
      - revision_actions
    failure_policy:
      continue_on_error: true
      block_if_missing:
        - stage_trace
    absorbed_from:
      - deepH/docs/AGENTS_AND_SPECS.md
      - deepH/docs/WORKFLOWS_AND_UNIVERSES.md
      - deepH/crews/reviewflow.yaml

handoff_contract:
  required_fields:
    - from_stage
    - to_stage
    - output_kind
    - status
    - compact_summary
  output_kinds:
    - summary/text
    - diagnostic/narrative
    - diagnostic/design
    - diagnostic/proof
    - diagnostic/render
    - test/regression
    - plan/revision
  rules:
    - Downstream stages receive compact structured context, not raw transcripts.
    - Handoffs must state assumptions, unresolved blockers, and confidence.
    - Final synthesis deduplicates findings and ranks by impact on audience outcome.

review_universes:
  - name: baseline
    focus: Overall deck quality, clarity, and fit to brief.
    output_kind: summary/text
  - name: strict
    focus: Regressions, weak assumptions, missing proof, and overconfident claims.
    output_kind: diagnostic/proof
  - name: narrative_focus
    focus: Belief shift, story flow, tension, slide function, CTA.
    output_kind: diagnostic/narrative
  - name: design_focus
    focus: Layout rhythm, hierarchy, density, media fit, brand consistency.
    output_kind: diagnostic/design
  - name: render_focus
    focus: Clipping, overlap, export fidelity, screenshots, PPTX/PDF issues.
    output_kind: diagnostic/render
  - name: synth
    focus: Merge upstream findings, remove duplicates, produce revision plan.
    depends_on:
      - baseline
      - strict
      - narrative_focus
      - design_focus
      - render_focus
    output_kind: plan/revision

trace_report:
  required_sections:
    - selected_context
    - skipped_context_and_reason
    - stage_decisions
    - handoff_summary
    - blockers
    - revision_actions
  block_if:
    - Important source material was ignored without reason.
    - Final deck changed core claim without trace.
    - Reviewer findings were not synthesized into action.
```


## Referência: references/source/templates/runtime/workflow-modes.yaml

```yaml
version: 1
name: workflow-modes
purpose: >
  Choose how much process to run for the user's actual need. This prevents the
  skill from overproducing artifacts for quick work while preserving strict
  gates for reusable or exportable decks.

modes:
  micro_reply:
    use_when:
      - User asks for a quick outline, slide list, critique, or direction.
      - No files or export are requested.
    max_user_questions: 3
    required_outputs:
      - thesis
      - slide_list_with_function
      - design_direction_summary
      - top_risks
    skip_outputs:
      - job-state.yaml
      - render-lock.yaml
      - full_package_validation
    gates:
      - no_topic_dump
      - action_titles_are_claims
      - one_function_per_slide

  standard_deck_spec:
    use_when:
      - User wants a usable deck plan or rewrite but not a file export.
      - The deck will be reviewed before production.
    required_outputs:
      - briefing-normalized
      - audience-belief-shift
      - story-arc
      - slide-function-map
      - design-direction
      - deck-spec
      - speaker-notes
      - qa-report
    gates:
      - story_arc_contract
      - slide_function_map_contract
      - design_direction_contract
      - squad_quality_rubric

  full_package:
    use_when:
      - User wants a reusable, shareable, or machine-readable deck package.
      - The skill is being tested, benchmarked, or packaged.
    required_outputs:
      - all_required_outputs_from_SKILL_md
      - package-validation-report
    required_scripts:
      - scripts/validate_runtime_contracts.py
      - scripts/validate_deck_package.py
    gates:
      - no_killer_items
      - package_validates
      - source_of_truth_policy
      - template_selection_report

  repair_existing_deck:
    use_when:
      - User provides an existing weak deck, process log, screenshots, or prior output.
      - User says the slides are bad, noisy, repetitive, or not persuasive.
    required_outputs:
      - failure_inventory
      - forward-test
      - revised_story_arc
      - revised_slide_function_map
      - revised_design_direction
      - before_after_critique
    gates:
      - old_failure_modes_mapped_to_blockers
      - key_slide_gate_before_full_rewrite
      - regression_fixture_passed

  benchmark_or_absorption:
    use_when:
      - The deck compares tools, competitors, repos, skills, agents, or products.
      - User needs what to absorb, build, ignore, or roadmap.
    required_outputs:
      - comparison_scope
      - category_split
      - weighted_matrix
      - evidence_ledger
      - absorption_map
      - roadmap
      - decision
    gates:
      - players_are_comparable_or_split
      - every_score_has_evidence_or_assumption
      - matrix_cells_are_clean_not_repetitive
      - documents_and_comparativo_preserved_when_useful

  exportable_pptx_or_pdf:
    use_when:
      - User asks for PPTX, PDF, Google Slides, screenshots, or rendered assets.
    required_outputs:
      - render-lock
      - export-contract
      - editability-report
      - rendered-eval
      - verified_output_path
    required_scripts:
      - scripts/check_pptx_placeholders.py
      - scripts/validate_rendered_eval.py
      - scripts/validate_deck_package.py
    gates:
      - no_claimed_export_without_file
      - no_text_clipping_or_overlap
      - no_rasterized_action_titles_when_pptx_requested
      - rendered_key_slides_reviewed

selection_rules:
  default_mode: standard_deck_spec
  prefer_micro_when:
    - user_asks_for_direction_only
    - answer_in_chat_is_enough
  prefer_full_when:
    - user_says_shareable
    - user_says_self_contained
    - package_or_validation_requested
    - benchmark_quality_is_being_improved
  prefer_repair_when:
    - process_log_or_bad_deck_provided
    - user_mentions_previous_failure
  prefer_export_when:
    - output_file_requested
    - pptx_or_pdf_requested
```


## Referência: references/source/templates/schemas/deck-template.schema.yaml

```yaml
type: object
required:
  - id
  - name
  - job
  - pick_when
  - skip_when
  - narrative_arc
  - slide_sequence
  - absorbed_from
properties:
  id:
    type: string
  name:
    type: string
  job:
    type: string
  audience:
    type: array
    items:
      type: string
  pick_when:
    type: array
    items:
      type: string
  skip_when:
    type: array
    items:
      type: string
  narrative_arc:
    type: array
    items:
      type: string
  default_slide_count:
    type: object
    properties:
      min:
        type: integer
      ideal:
        type: integer
      max:
        type: integer
  slide_sequence:
    type: array
    items:
      type: object
      required: [slot, function, required]
      properties:
        slot:
          type: string
        function:
          type: string
        required:
          type: boolean
        visual_family:
          type: string
        notes:
          type: string
  evidence_policy:
    type: array
    items:
      type: string
  qa_gates:
    type: array
    items:
      type: string
  absorbed_from:
    type: array
    items:
      type: string
```


## Referência: references/source/templates/schemas/qa-gate.schema.yaml

```yaml
type: object
required:
  - id
  - gate
  - blocks_if
  - pass_if
properties:
  id:
    type: string
  gate:
    type: string
  blocks_if:
    type: array
    items:
      type: string
  pass_if:
    type: array
    items:
      type: string
  score_weight:
    type: integer
  absorbed_from:
    type: array
    items:
      type: string
```


## Referência: references/source/templates/schemas/runtime-job.schema.yaml

```yaml
type: object
required:
  - id
  - mode
  - pick_when
  - inputs
  - outputs
  - failure_policy
properties:
  id:
    type: string
  mode:
    type: string
  pick_when:
    type: array
    items:
      type: string
  inputs:
    type: array
    items:
      type: string
  steps:
    type: array
    items:
      type: string
  outputs:
    type: array
    items:
      type: string
  failure_policy:
    type: object
  absorbed_from:
    type: array
    items:
      type: string
```


## Referência: references/source/templates/schemas/slide-template.schema.yaml

```yaml
type: object
required:
  - id
  - function
  - pick_when
  - skip_when
  - slots
  - constraints
  - absorbed_from
properties:
  id:
    type: string
  function:
    type: string
  pick_when:
    type: array
    items:
      type: string
  skip_when:
    type: array
    items:
      type: string
  compatible_visuals:
    type: array
    items:
      type: string
  slots:
    type: array
    items:
      type: object
      required: [name, type, required]
      properties:
        name:
          type: string
        type:
          type: string
        required:
          type: boolean
        max_chars:
          type: integer
        suggested_characters:
          type: integer
        min_items:
          type: integer
        max_items:
          type: integer
        rewrite_if_exceeds:
          type: boolean
        must_exist_locally:
          type: boolean
        required_when:
          type: array
          items:
            type: string
        role:
          type: string
  variable_layouts:
    type: object
    properties:
      by_item_count:
        type: object
  selection_audit:
    type: object
    properties:
      requires_runners_up:
        type: boolean
      minimum_runners_up:
        type: integer
  constraints:
    type: object
    properties:
      max_visible_words:
        type: integer
      max_bullets:
        type: integer
      requires_evidence:
        type: boolean
      avoid:
        type: array
        items:
          type: string
  qa:
    type: array
    items:
      type: string
  absorbed_from:
    type: array
    items:
      type: string
```


## Referência: references/source/templates/schemas/theme.schema.yaml

```yaml
type: object
required:
  - id
  - pick_when
  - tokens
  - constraints
properties:
  id:
    type: string
  pick_when:
    type: array
    items:
      type: string
  tokens:
    type: object
    properties:
      colors:
        type: object
      typography:
        type: object
      spacing:
        type: object
      chart:
        type: object
  constraints:
    type: object
  absorbed_from:
    type: array
    items:
      type: string
```


## Referência: references/source/templates/schemas/visual-template.schema.yaml

```yaml
type: object
required:
  - id
  - category
  - pick_when
  - skip_when
  - data_shape
  - constraints
  - absorbed_from
properties:
  id:
    type: string
  category:
    type: string
  pick_when:
    type: array
    items:
      type: string
  skip_when:
    type: array
    items:
      type: string
  data_shape:
    type: object
  slots:
    type: array
    items:
      type: string
  constraints:
    type: object
  compatible_slide_functions:
    type: array
    items:
      type: string
  absorbed_from:
    type: array
    items:
      type: string
```


## Referência: references/source/templates/slide/function-library.yaml

```yaml
version: 1
slide_templates:
  - id: hook_hero_claim
    function: hook
    pick_when:
      - The audience must immediately understand the central claim or promise.
    skip_when:
      - The slide needs dense evidence or comparison.
    compatible_visuals: [hero_claim, full_bleed_image, kpi_cards]
    slots:
      - {name: action_title, type: text, required: true, max_chars: 90, role: claim}
      - {name: subtitle, type: text, required: false, max_chars: 140, role: context}
      - {name: proof_chip, type: text, required: false, max_chars: 40, role: credibility}
    constraints:
      max_visible_words: 28
      max_bullets: 0
      requires_evidence: false
      avoid: [generic_topic_title, decorative_background_only]
    qa: [action_title_gate, density_gate]
    absorbed_from: [slide-deck-ai, Presenton]

  - id: reframe_contrast
    function: reframe
    pick_when:
      - The deck must replace an old mental model with a new one.
    skip_when:
      - There are more than four comparison dimensions; use comparison_table.
    compatible_visuals: [comparison_columns, before_after, pros_cons_chart]
    slots:
      - {name: old_belief, type: text, required: true, max_chars: 120, role: contrast_left}
      - {name: new_belief, type: text, required: true, max_chars: 120, role: contrast_right}
      - {name: bridge, type: text, required: false, max_chars: 90, role: transition}
    constraints:
      max_visible_words: 45
      max_bullets: 4
      requires_evidence: false
      avoid: [balanced_but_no_point_of_view, vague_old_way]
    qa: [belief_shift_gate, contrast_gate]
    absorbed_from: [presentation-ai, ppt-master]

  - id: diagnosis_fishbone
    function: diagnosis
    pick_when:
      - The audience sees symptoms but not root causes.
    skip_when:
      - The message is a simple linear process; use process_flow.
    compatible_visuals: [fishbone_diagram, module_composition, layered_architecture]
    slots:
      - {name: symptom, type: text, required: true, max_chars: 90, role: observed_problem}
      - {name: causes, type: list, required: true, max_chars: 240, role: root_causes}
      - {name: implication, type: text, required: true, max_chars: 120, role: why_it_matters}
    constraints:
      max_visible_words: 65
      max_bullets: 8
      requires_evidence: true
      avoid: [blame_without_mechanism, too_many_causes]
    qa: [evidence_gate, causality_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: mechanism_layered_system
    function: mechanism
    pick_when:
      - The deck must explain how a system creates the promised result.
    skip_when:
      - The idea is only a sequence of steps; use process_flow or numbered_steps.
    compatible_visuals: [layered_architecture, module_composition, hub_spoke]
    slots:
      - {name: mechanism_name, type: text, required: true, max_chars: 70, role: system_name}
      - {name: layers_or_modules, type: list, required: true, max_chars: 360, role: components}
      - {name: causality, type: text, required: true, max_chars: 140, role: why_it_works}
    constraints:
      max_visible_words: 75
      max_bullets: 9
      requires_evidence: true
      avoid: [feature_dump, unlabeled_arrows, no_causal_link]
    qa: [mechanism_gate, visual_density_gate]
    absorbed_from: [Presenton, ppt-master, PPTAgent]

  - id: proof_before_after
    function: proof
    pick_when:
      - The audience needs to see a concrete state change.
    skip_when:
      - The proof is a time series; use line_chart.
    compatible_visuals: [before_after, dumbbell_chart, waterfall_chart]
    slots:
      - {name: before, type: text, required: true, max_chars: 100, role: baseline}
      - {name: after, type: text, required: true, max_chars: 100, role: outcome}
      - {name: evidence_source, type: text, required: true, max_chars: 140, role: source}
    constraints:
      max_visible_words: 50
      max_bullets: 4
      requires_evidence: true
      avoid: [testimonial_without_specifics, fake_precision]
    qa: [proof_gate, source_gate]
    absorbed_from: [banana-slides, ppt-master, slide-deck-ai]

  - id: comparison_matrix
    function: comparison
    pick_when:
      - Multiple players are compared across multiple dimensions.
    skip_when:
      - There are fewer than three dimensions; use comparison_columns.
    compatible_visuals: [harvey_balls_table, feature_matrix_table, heatmap_chart]
    slots:
      - {name: players, type: list, required: true, max_chars: 240, role: compared_entities}
      - {name: dimensions, type: list, required: true, max_chars: 360, role: criteria}
      - {name: scoring_note, type: text, required: true, max_chars: 180, role: method}
    constraints:
      max_visible_words: 110
      max_bullets: 0
      requires_evidence: true
      avoid: [repeated_cell_text, mixed_categories_without_split, no_method]
    qa: [matrix_noise_gate, scoring_method_gate]
    absorbed_from: [ppt-master, presentation-ai]

  - id: decision_options
    function: decision
    pick_when:
      - The audience must choose among options.
    skip_when:
      - The slide only lists pros and cons with no recommendation.
    compatible_visuals: [comparison_columns, matrix_2x2, decision_card]
    slots:
      - {name: options, type: list, required: true, max_chars: 220, role: choices}
      - {name: recommendation, type: text, required: true, max_chars: 120, role: preferred_choice}
      - {name: tradeoff, type: text, required: true, max_chars: 140, role: cost}
    constraints:
      max_visible_words: 65
      max_bullets: 5
      requires_evidence: true
      avoid: [no_recommendation, equal_weight_everything]
    qa: [decision_gate, tradeoff_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: roadmap_vertical
    function: plan
    pick_when:
      - The deck needs ordered phases or milestones with ownership/status.
    skip_when:
      - The timeline has real task durations; use gantt_chart.
    compatible_visuals: [roadmap_vertical, gantt_chart, numbered_steps]
    slots:
      - {name: phases, type: list, required: true, max_chars: 320, role: sequence}
      - {name: owners, type: list, required: false, max_chars: 160, role: accountability}
      - {name: success_metric, type: text, required: false, max_chars: 90, role: measurable_outcome}
    constraints:
      max_visible_words: 80
      max_bullets: 8
      requires_evidence: false
      avoid: [roadmap_without_dates_or_order, overloaded_phase]
    qa: [roadmap_gate, accountability_gate]
    absorbed_from: [ppt-master, banana-slides]

  - id: teaching_framework
    function: teaching
    pick_when:
      - The audience must learn a repeatable method.
    skip_when:
      - The method is not sequential or repeatable.
    compatible_visuals: [numbered_steps, circular_stages, chevron_process]
    slots:
      - {name: framework_name, type: text, required: true, max_chars: 70, role: model}
      - {name: steps, type: list, required: true, max_chars: 300, role: method}
      - {name: example, type: text, required: true, max_chars: 140, role: concrete_use}
    constraints:
      max_visible_words: 80
      max_bullets: 6
      requires_evidence: false
      avoid: [abstract_steps_without_example, too_many_steps]
    qa: [didactic_clarity_gate, example_gate]
    absorbed_from: [slide-deck-ai, presentation-ai]

  - id: offer_stack
    function: conversion
    pick_when:
      - The slide needs to make the offer legible and valuable.
    skip_when:
      - There is no commercial CTA.
    compatible_visuals: [comparison_columns, module_composition, kpi_cards]
    slots:
      - {name: offer_name, type: text, required: true, max_chars: 70, role: product}
      - {name: components, type: list, required: true, max_chars: 260, role: value_stack}
      - {name: risk_reversal, type: text, required: false, max_chars: 120, role: trust}
      - {name: cta, type: text, required: true, max_chars: 80, role: next_step}
    constraints:
      max_visible_words: 85
      max_bullets: 7
      requires_evidence: false
      avoid: [feature_list_without_outcome, unclear_next_step]
    qa: [offer_clarity_gate, cta_gate]
    absorbed_from: [presentation-ai, banana-slides]

  - id: executive_summary_kpi
    function: answer_first
    pick_when:
      - Executives need the answer, status, and decision signal before details.
    skip_when:
      - The slide is a detailed analysis or appendix table.
    compatible_visuals: [executive_snapshot, kpi_cards, bullet_chart]
    slots:
      - {name: headline_answer, type: text, required: true, max_chars: 90, role: conclusion}
      - {name: metrics, type: list, required: true, max_chars: 220, role: evidence}
      - {name: implication, type: text, required: true, max_chars: 120, role: decision_signal}
    constraints:
      max_visible_words: 55
      max_bullets: 5
      requires_evidence: true
      avoid: [status_without_so_what, metric_dump]
    qa: [executive_density_gate, data_integrity_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: evidence_stack
    function: credibility
    pick_when:
      - A claim needs multiple compact proof points and source traceability.
    skip_when:
      - There is only one metric; use proof_before_after or kpi_cards.
    compatible_visuals: [evidence_cards, source_panel, basic_table]
    slots:
      - {name: claim, type: text, required: true, max_chars: 90, role: thesis}
      - {name: evidence_items, type: list, required: true, max_chars: 320, role: proof_points}
      - {name: confidence_note, type: text, required: false, max_chars: 120, role: caveat}
    constraints:
      max_visible_words: 80
      max_bullets: 6
      requires_evidence: true
      avoid: [unsourced_superlatives, repeated_sources]
    qa: [evidence_gate, source_gate]
    absorbed_from: [PPTAgent, ppt-master]

  - id: risk_register_heatmap
    function: risk
    pick_when:
      - Risks need severity, likelihood, mitigation, and owner.
    skip_when:
      - The slide only compares strategic options; use decision_options.
    compatible_visuals: [risk_heatmap, matrix_2x2, basic_table]
    slots:
      - {name: risks, type: list, required: true, max_chars: 300, role: risk_items}
      - {name: mitigations, type: list, required: true, max_chars: 300, role: controls}
      - {name: owner_or_decision, type: text, required: false, max_chars: 100, role: accountability}
    constraints:
      max_visible_words: 90
      max_bullets: 8
      requires_evidence: true
      avoid: [risk_without_mitigation, no_owner]
    qa: [risk_gate, accountability_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: customer_journey_gap
    function: diagnosis
    pick_when:
      - The story depends on where users stall, churn, or lose confidence.
    skip_when:
      - The journey is a pure acquisition funnel; use funnel_diagnosis.
    compatible_visuals: [journey_map, stakeholder_map, evidence_cards]
    slots:
      - {name: journey_phases, type: list, required: true, max_chars: 240, role: phases}
      - {name: pain_points, type: list, required: true, max_chars: 300, role: friction}
      - {name: opportunity, type: text, required: true, max_chars: 120, role: intervention}
    constraints:
      max_visible_words: 90
      max_bullets: 8
      requires_evidence: true
      avoid: [generic_persona_journey, no_behavioral_signal]
    qa: [customer_relevance_gate, evidence_gate]
    absorbed_from: [ppt-master, presentation-ai]

  - id: architecture_flow
    function: architecture
    pick_when:
      - The audience needs to understand system boundaries, data flow, or integration flow.
    skip_when:
      - The message is business process, not technical architecture.
    compatible_visuals: [system_flow, layered_architecture, client_server_flow]
    slots:
      - {name: system_boundary, type: text, required: true, max_chars: 90, role: scope}
      - {name: components, type: list, required: true, max_chars: 320, role: system_parts}
      - {name: critical_flow, type: text, required: true, max_chars: 160, role: data_or_control_flow}
    constraints:
      max_visible_words: 85
      max_bullets: 7
      requires_evidence: true
      avoid: [unlabeled_arrows, mixed_abstraction_levels]
    qa: [architecture_gate, diagram_legibility_gate]
    absorbed_from: [ppt-master, PPTAgent]

  - id: demo_script
    function: demo_setup
    pick_when:
      - A live or recorded demo needs a scripted sequence with expected proof moments.
    skip_when:
      - The slide only reports a final outcome; use case_study_result.
    compatible_visuals: [screen_sequence, process_flow, before_after]
    slots:
      - {name: demo_goal, type: text, required: true, max_chars: 90, role: promise}
      - {name: steps, type: list, required: true, max_chars: 260, role: sequence}
      - {name: proof_moment, type: text, required: true, max_chars: 120, role: validation}
    constraints:
      max_visible_words: 70
      max_bullets: 6
      requires_evidence: false
      avoid: [demo_without_expected_result, too_many_clicks]
    qa: [demo_gate, sequence_gate]
    absorbed_from: [Presenton, presentation-ai]

  - id: objection_response
    function: objection_handling
    pick_when:
      - The audience likely has a named objection that can block action.
    skip_when:
      - There is no clear objection; use reframe_contrast.
    compatible_visuals: [myth_truth, comparison_columns, decision_card]
    slots:
      - {name: objection, type: text, required: true, max_chars: 100, role: audience_fear}
      - {name: response, type: text, required: true, max_chars: 140, role: answer}
      - {name: proof_or_tradeoff, type: text, required: true, max_chars: 140, role: evidence}
    constraints:
      max_visible_words: 65
      max_bullets: 4
      requires_evidence: true
      avoid: [strawman_objection, dismissive_tone]
    qa: [objection_gate, proof_gate]
    absorbed_from: [banana-slides, presentation-ai]

  - id: case_study_result
    function: proof
    pick_when:
      - A customer, project, or internal case proves a repeatable outcome.
    skip_when:
      - There is no measurable before/after or named intervention.
    compatible_visuals: [case_study_panel, before_after, waterfall_chart]
    slots:
      - {name: baseline, type: text, required: true, max_chars: 120, role: before}
      - {name: intervention, type: text, required: true, max_chars: 120, role: what_changed}
      - {name: result, type: text, required: true, max_chars: 120, role: outcome}
      - {name: repeatable_lesson, type: text, required: false, max_chars: 120, role: pattern}
    constraints:
      max_visible_words: 85
      max_bullets: 5
      requires_evidence: true
      avoid: [testimonial_without_metric, anonymous_vague_case]
    qa: [case_study_gate, proof_gate]
    absorbed_from: [slide-deck-ai, ppt-master]

  - id: pricing_tiers
    function: commercial
    pick_when:
      - A proposal needs package tiers, plan comparison, or buying path.
    skip_when:
      - The commercial slide has only one offer; use offer_stack.
    compatible_visuals: [pricing_table, feature_matrix_table, comparison_columns]
    slots:
      - {name: tiers, type: list, required: true, max_chars: 260, role: packages}
      - {name: best_fit, type: text, required: true, max_chars: 120, role: recommendation}
      - {name: buying_note, type: text, required: false, max_chars: 100, role: next_step}
    constraints:
      max_visible_words: 110
      max_bullets: 0
      requires_evidence: false
      avoid: [hidden_tradeoffs, no_recommended_path]
    qa: [offer_clarity_gate, decision_gate]
    absorbed_from: [presentation-ai, ppt-master]

  - id: market_map
    function: positioning
    pick_when:
      - The audience must see where players, segments, or alternatives sit in the market.
    skip_when:
      - The goal is a scored benchmark matrix; use comparison_matrix.
    compatible_visuals: [market_map, matrix_2x2, horizontal_bar_chart]
    slots:
      - {name: axes_or_segments, type: list, required: true, max_chars: 180, role: frame}
      - {name: players, type: list, required: true, max_chars: 260, role: entities}
      - {name: strategic_takeaway, type: text, required: true, max_chars: 140, role: implication}
    constraints:
      max_visible_words: 75
      max_bullets: 5
      requires_evidence: true
      avoid: [unlabeled_axes, arbitrary_positioning]
    qa: [positioning_gate, evidence_gate]
    absorbed_from: [ppt-master, Presenton]

  - id: implementation_operating_model
    function: operating_model
    pick_when:
      - A plan needs roles, cadence, inputs, outputs, and governance.
    skip_when:
      - The slide is only a timeline; use roadmap_vertical.
    compatible_visuals: [swimlane_process, pipeline_with_stages, responsibility_matrix]
    slots:
      - {name: workstreams, type: list, required: true, max_chars: 260, role: operating_lanes}
      - {name: cadence, type: text, required: true, max_chars: 120, role: rhythm}
      - {name: outputs, type: list, required: true, max_chars: 220, role: artifacts}
    constraints:
      max_visible_words: 90
      max_bullets: 8
      requires_evidence: false
      avoid: [roles_without_outputs, meeting_cadence_without_decisions]
    qa: [operating_model_gate, accountability_gate]
    absorbed_from: [banana-slides, ppt-master]

  - id: appendix_source_table
    function: appendix
    pick_when:
      - A deck needs transparent source, assumption, or scoring backup.
    skip_when:
      - The source detail belongs on the main proof slide.
    compatible_visuals: [source_panel, basic_table, evidence_cards]
    slots:
      - {name: sources, type: list, required: true, max_chars: 420, role: citations}
      - {name: assumptions, type: list, required: false, max_chars: 260, role: assumptions}
      - {name: confidence, type: text, required: false, max_chars: 120, role: confidence}
    constraints:
      max_visible_words: 130
      max_bullets: 0
      requires_evidence: true
      avoid: [source_without_claim_mapping, decorative_appendix]
    qa: [source_gate, appendix_gate]
    absorbed_from: [PPTAgent, powerpoint-skill]

  - id: agenda_contract
    function: facilitation
    pick_when:
      - A live session needs timeboxes, outcomes, rules, and decision moments.
    skip_when:
      - The deck is asynchronous or purely narrative.
    compatible_visuals: [agenda_timeline, checklist, numbered_steps]
    slots:
      - {name: session_goal, type: text, required: true, max_chars: 90, role: outcome}
      - {name: agenda_blocks, type: list, required: true, max_chars: 300, role: timeboxes}
      - {name: decision_points, type: list, required: false, max_chars: 160, role: decisions}
    constraints: {max_visible_words: 75, max_bullets: 7, requires_evidence: false, avoid: [agenda_without_outcomes]}
    qa: [facilitation_gate, decision_gate]
    absorbed_from: [presentation-ai, banana-slides]

  - id: audience_segmentation
    function: segmentation
    pick_when:
      - Different audiences, personas, or buyer roles need distinct messages or actions.
    skip_when:
      - There is only one target audience; use hook_hero_claim.
    compatible_visuals: [stakeholder_map, market_map, quadrant_text_bullets]
    slots:
      - {name: segments, type: list, required: true, max_chars: 260, role: audience_groups}
      - {name: needs, type: list, required: true, max_chars: 260, role: motivations}
      - {name: message_strategy, type: text, required: true, max_chars: 140, role: implication}
    constraints: {max_visible_words: 90, max_bullets: 8, requires_evidence: true, avoid: [demographic_only_segments]}
    qa: [customer_relevance_gate, positioning_gate]
    absorbed_from: [ppt-master, presentation-ai]

  - id: problem_cost
    function: stakes
    pick_when:
      - The audience understands the problem but not its economic, time, risk, or trust cost.
    skip_when:
      - There is no measurable impact or credible proxy.
    compatible_visuals: [waterfall_chart, kpi_cards, evidence_cards]
    slots:
      - {name: problem, type: text, required: true, max_chars: 90, role: issue}
      - {name: cost_drivers, type: list, required: true, max_chars: 260, role: impact}
      - {name: quantified_stake, type: text, required: true, max_chars: 120, role: consequence}
    constraints: {max_visible_words: 75, max_bullets: 5, requires_evidence: true, avoid: [fear_without_quantification]}
    qa: [stakes_gate, evidence_gate]
    absorbed_from: [banana-slides, ppt-master]

  - id: data_insight
    function: insight
    pick_when:
      - One chart or table must yield a specific implication.
    skip_when:
      - The slide is just a metric dashboard; use executive_summary_kpi.
    compatible_visuals: [line_chart, horizontal_bar_chart, stacked_bar_chart]
    slots:
      - {name: observation, type: text, required: true, max_chars: 90, role: observed_pattern}
      - {name: data_view, type: list, required: true, max_chars: 220, role: chart_inputs}
      - {name: implication, type: text, required: true, max_chars: 130, role: so_what}
    constraints: {max_visible_words: 65, max_bullets: 4, requires_evidence: true, avoid: [chart_without_takeaway]}
    qa: [chart_selection_gate, data_integrity_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: experiment_results
    function: proof
    pick_when:
      - A test, pilot, or experiment needs hypothesis, result, and decision.
    skip_when:
      - There is no clear baseline or success criterion.
    compatible_visuals: [experiment_card_grid, bullet_chart, before_after]
    slots:
      - {name: hypothesis, type: text, required: true, max_chars: 120, role: test_claim}
      - {name: result, type: text, required: true, max_chars: 120, role: outcome}
      - {name: decision, type: text, required: true, max_chars: 120, role: next_action}
    constraints: {max_visible_words: 80, max_bullets: 5, requires_evidence: true, avoid: [test_without_success_metric]}
    qa: [experiment_gate, decision_gate]
    absorbed_from: [PPTAgent, ppt-master]

  - id: retention_cohort
    function: diagnosis
    pick_when:
      - Retention, repeat behavior, cohort decay, or customer health is central.
    skip_when:
      - The metric is a single aggregate; use kpi_cards.
    compatible_visuals: [cohort_retention, line_chart, heatmap_chart]
    slots:
      - {name: cohort_definition, type: text, required: true, max_chars: 120, role: scope}
      - {name: retention_pattern, type: text, required: true, max_chars: 140, role: finding}
      - {name: action, type: text, required: true, max_chars: 120, role: response}
    constraints: {max_visible_words: 70, max_bullets: 4, requires_evidence: true, avoid: [cohort_without_period]}
    qa: [data_integrity_gate, customer_relevance_gate]
    absorbed_from: [ppt-master]

  - id: unit_economics
    function: financial_update
    pick_when:
      - CAC, LTV, margin, payback, ARPA, or contribution economics drive the decision.
    skip_when:
      - Only top-line revenue trend matters; use line_chart.
    compatible_visuals: [unit_economics_panel, bullet_chart, waterfall_chart]
    slots:
      - {name: economics_snapshot, type: list, required: true, max_chars: 260, role: metrics}
      - {name: driver, type: text, required: true, max_chars: 120, role: cause}
      - {name: decision, type: text, required: true, max_chars: 120, role: action}
    constraints: {max_visible_words: 90, max_bullets: 6, requires_evidence: true, avoid: [finance_without_source_period]}
    qa: [data_integrity_gate, decision_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: capability_maturity
    function: capability_map
    pick_when:
      - Capabilities need staged maturity, current state, target state, and gaps.
    skip_when:
      - The comparison is between products; use comparison_matrix.
    compatible_visuals: [maturity_ladder, harvey_balls_table, roadmap_vertical]
    slots:
      - {name: capabilities, type: list, required: true, max_chars: 300, role: capabilities}
      - {name: current_state, type: text, required: true, max_chars: 120, role: baseline}
      - {name: target_state, type: text, required: true, max_chars: 120, role: aspiration}
    constraints: {max_visible_words: 90, max_bullets: 7, requires_evidence: true, avoid: [maturity_without_criteria]}
    qa: [scoring_method_gate, roadmap_gate]
    absorbed_from: [ppt-master, presentation-ai]

  - id: launch_plan
    function: plan
    pick_when:
      - A launch needs dates, channels, assets, owners, and readiness gates.
    skip_when:
      - The plan is not date-driven; use implementation_operating_model.
    compatible_visuals: [launch_calendar, checklist, gantt_chart]
    slots:
      - {name: launch_moments, type: list, required: true, max_chars: 260, role: milestones}
      - {name: owners, type: list, required: true, max_chars: 180, role: accountability}
      - {name: readiness_gate, type: text, required: true, max_chars: 120, role: criteria}
    constraints: {max_visible_words: 85, max_bullets: 8, requires_evidence: false, avoid: [date_without_owner]}
    qa: [readiness_gate, accountability_gate]
    absorbed_from: [Presenton, presentation-ai]

  - id: training_exercise
    function: practice
    pick_when:
      - A course or workshop needs participant action, not passive explanation.
    skip_when:
      - The audience only needs a reference framework.
    compatible_visuals: [workshop_canvas, checklist, numbered_steps]
    slots:
      - {name: prompt, type: text, required: true, max_chars: 140, role: exercise_prompt}
      - {name: inputs, type: list, required: true, max_chars: 180, role: materials}
      - {name: output, type: text, required: true, max_chars: 120, role: artifact}
    constraints: {max_visible_words: 80, max_bullets: 6, requires_evidence: false, avoid: [exercise_without_output]}
    qa: [practice_gate, didactic_clarity_gate]
    absorbed_from: [slide-deck-ai, banana-slides]

  - id: workshop_canvas
    function: facilitation
    pick_when:
      - A live group needs to fill a canvas, map, or decision artifact.
    skip_when:
      - The slide is informational only.
    compatible_visuals: [workshop_canvas, affinity_map, decision_tree]
    slots:
      - {name: canvas_goal, type: text, required: true, max_chars: 100, role: outcome}
      - {name: fields, type: list, required: true, max_chars: 260, role: canvas_sections}
      - {name: timebox, type: text, required: true, max_chars: 80, role: constraint}
    constraints: {max_visible_words: 75, max_bullets: 6, requires_evidence: false, avoid: [canvas_without_decision_use]}
    qa: [facilitation_gate, decision_gate]
    absorbed_from: [presentation-ai]

  - id: governance_model
    function: governance
    pick_when:
      - Decisions, ownership, escalation, and cadence must be explicit.
    skip_when:
      - There is only a simple task plan; use roadmap_vertical.
    compatible_visuals: [responsibility_matrix, org_chart, swimlane_process]
    slots:
      - {name: decision_rights, type: list, required: true, max_chars: 260, role: ownership}
      - {name: cadence, type: text, required: true, max_chars: 100, role: rhythm}
      - {name: escalation, type: text, required: false, max_chars: 120, role: exception_path}
    constraints: {max_visible_words: 90, max_bullets: 8, requires_evidence: false, avoid: [governance_without_decisions]}
    qa: [governance_gate, accountability_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: migration_plan
    function: implementation
    pick_when:
      - The deck needs phased migration, dependencies, rollback, or cutover plan.
    skip_when:
      - There is no technical or operational transition.
    compatible_visuals: [dependency_map, gantt_chart, swimlane_process]
    slots:
      - {name: phases, type: list, required: true, max_chars: 280, role: sequence}
      - {name: dependencies, type: list, required: true, max_chars: 220, role: blockers}
      - {name: rollback_or_guardrail, type: text, required: false, max_chars: 120, role: safety}
    constraints: {max_visible_words: 95, max_bullets: 8, requires_evidence: true, avoid: [migration_without_risk_controls]}
    qa: [implementation_gate, risk_gate]
    absorbed_from: [PPTAgent, powerpoint-skill]

  - id: incident_postmortem
    function: diagnosis
    pick_when:
      - A failure must be explained through timeline, impact, root cause, and corrective action.
    skip_when:
      - The issue is hypothetical risk; use risk_register_heatmap.
    compatible_visuals: [incident_timeline, corrective_action_table, fishbone_diagram]
    slots:
      - {name: incident_summary, type: text, required: true, max_chars: 120, role: summary}
      - {name: root_cause, type: text, required: true, max_chars: 140, role: cause}
      - {name: corrective_actions, type: list, required: true, max_chars: 260, role: fixes}
    constraints: {max_visible_words: 90, max_bullets: 7, requires_evidence: true, avoid: [blame_without_timeline]}
    qa: [incident_clarity_gate, accountability_gate]
    absorbed_from: [powerpoint-skill, ppt-master]

  - id: hiring_scorecard
    function: evaluation
    pick_when:
      - A role, candidate, or team capability needs structured evaluation criteria.
    skip_when:
      - The deck is a generic onboarding narrative.
    compatible_visuals: [hiring_scorecard, maturity_ladder, basic_table]
    slots:
      - {name: criteria, type: list, required: true, max_chars: 260, role: scorecard}
      - {name: evidence_required, type: list, required: true, max_chars: 220, role: proof}
      - {name: decision_rule, type: text, required: true, max_chars: 120, role: threshold}
    constraints: {max_visible_words: 95, max_bullets: 8, requires_evidence: true, avoid: [criteria_without_behavioral_signal]}
    qa: [evaluation_gate, decision_gate]
    absorbed_from: [ppt-master]

  - id: roadmap_decision
    function: prioritization
    pick_when:
      - A roadmap needs tradeoffs, sequencing, and explicit chosen bets.
    skip_when:
      - It is only a status timeline; use roadmap_vertical.
    compatible_visuals: [roadmap_vertical, matrix_2x2, dependency_map]
    slots:
      - {name: candidate_bets, type: list, required: true, max_chars: 280, role: options}
      - {name: sequencing_logic, type: text, required: true, max_chars: 140, role: rationale}
      - {name: rejected_or_deferred, type: list, required: false, max_chars: 180, role: tradeoffs}
    constraints: {max_visible_words: 90, max_bullets: 8, requires_evidence: true, avoid: [roadmap_without_tradeoffs]}
    qa: [roadmap_gate, decision_gate]
    absorbed_from: [ppt-master, Presenton]

  - id: narrative_section_divider
    function: transition
    pick_when:
      - A long deck needs a clear chapter turn with one sentence of momentum.
    skip_when:
      - The deck has fewer than eight slides.
    compatible_visuals: [section_divider, hero_claim, full_bleed_image]
    slots:
      - {name: chapter_label, type: text, required: true, max_chars: 40, role: section}
      - {name: transition_claim, type: text, required: true, max_chars: 100, role: momentum}
    constraints: {max_visible_words: 18, max_bullets: 0, requires_evidence: false, avoid: [decorative_only_divider]}
    qa: [narrative_flow_gate, density_gate]
    absorbed_from: [Presenton, presentation-ai]

  - id: closing_next_steps
    function: action
    pick_when:
      - The deck must end with concrete next step, owner, date, or decision ask.
    skip_when:
      - The deck is only reference material with no action.
    compatible_visuals: [decision_card, checklist, agenda_timeline]
    slots:
      - {name: requested_action, type: text, required: true, max_chars: 100, role: ask}
      - {name: owner_and_date, type: text, required: true, max_chars: 100, role: accountability}
      - {name: success_condition, type: text, required: false, max_chars: 120, role: outcome}
    constraints: {max_visible_words: 55, max_bullets: 4, requires_evidence: false, avoid: [generic_thank_you_slide]}
    qa: [cta_gate, accountability_gate]
    absorbed_from: [banana-slides, powerpoint-skill]

  - id: scoring_transparency
    function: method
    pick_when:
      - A benchmark, score, grade, or ranking needs to explain how numbers are assigned.
    skip_when:
      - There is no scoring or weighting model.
    compatible_visuals: [scoring_rubric_table, scoring_band_ladder, source_panel]
    slots:
      - {name: score_formula, type: text, required: true, max_chars: 140, role: formula}
      - {name: bands, type: list, required: true, max_chars: 260, role: scoring_bands}
      - {name: evidence_rule, type: text, required: true, max_chars: 140, role: confidence}
    constraints: {max_visible_words: 100, max_bullets: 8, requires_evidence: true, avoid: [score_without_band_definition]}
    qa: [scoring_method_gate, evidence_gate]
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: persona_fit
    function: decision
    pick_when:
      - Different personas need different winners, priorities, or tradeoffs.
    skip_when:
      - There is a single audience with one decision criterion.
    compatible_visuals: [persona_fit_matrix, stakeholder_map, radar_chart]
    slots:
      - {name: personas, type: list, required: true, max_chars: 220, role: audience_types}
      - {name: criteria_shift, type: list, required: true, max_chars: 260, role: weights}
      - {name: recommendation_by_persona, type: list, required: true, max_chars: 260, role: decisions}
    constraints: {max_visible_words: 100, max_bullets: 8, requires_evidence: true, avoid: [same_winner_for_every_persona_without_reason]}
    qa: [persona_gate, decision_gate]
    absorbed_from: [presentation-ai, ppt-master]

  - id: requirements_traceability
    function: governance
    pick_when:
      - Requirements, acceptance criteria, or promises must map to implementation/evidence.
    skip_when:
      - The slide is a general roadmap with no formal requirements.
    compatible_visuals: [traceability_matrix, checklist, basic_table]
    slots:
      - {name: requirements, type: list, required: true, max_chars: 280, role: requirements}
      - {name: evidence_or_owner, type: list, required: true, max_chars: 260, role: trace}
      - {name: gaps, type: list, required: false, max_chars: 200, role: missing}
    constraints: {max_visible_words: 120, max_bullets: 0, requires_evidence: true, avoid: [requirement_without_trace]}
    qa: [traceability_gate, source_gate]
    absorbed_from: [powerpoint-skill, PPTAgent]

  - id: compliance_readiness
    function: risk
    pick_when:
      - A deck must show policy, legal, privacy, security, or audit readiness.
    skip_when:
      - Risks are business execution risks; use risk_register_heatmap.
    compatible_visuals: [compliance_grid, checklist, risk_heatmap]
    slots:
      - {name: controls, type: list, required: true, max_chars: 280, role: controls}
      - {name: evidence, type: list, required: true, max_chars: 260, role: proof}
      - {name: open_risks, type: list, required: false, max_chars: 220, role: gaps}
    constraints: {max_visible_words: 110, max_bullets: 8, requires_evidence: true, avoid: [compliance_claim_without_artifact]}
    qa: [compliance_gate, evidence_gate]
    absorbed_from: [powerpoint-skill, ppt-master]

  - id: survey_results
    function: insight
    pick_when:
      - Survey, poll, NPS, CSAT, or qualitative feedback must become an insight.
    skip_when:
      - There is no sample size or response context.
    compatible_visuals: [survey_result_panel, horizontal_bar_chart, quote_evidence_panel]
    slots:
      - {name: question, type: text, required: true, max_chars: 120, role: prompt}
      - {name: results, type: list, required: true, max_chars: 260, role: responses}
      - {name: interpretation, type: text, required: true, max_chars: 140, role: implication}
    constraints: {max_visible_words: 90, max_bullets: 6, requires_evidence: true, avoid: [survey_without_n_or_context]}
    qa: [data_integrity_gate, insight_gate]
    absorbed_from: [ppt-master, presentation-ai]

  - id: roadmap_status
    function: update
    pick_when:
      - Roadmap initiatives need status, blocker, owner, and next checkpoint.
    skip_when:
      - The roadmap is only future plan; use roadmap_decision.
    compatible_visuals: [roadmap_status_board, gantt_chart, checklist]
    slots:
      - {name: initiatives, type: list, required: true, max_chars: 280, role: initiatives}
      - {name: blockers, type: list, required: false, max_chars: 220, role: constraints}
      - {name: next_checkpoint, type: text, required: true, max_chars: 120, role: cadence}
    constraints: {max_visible_words: 110, max_bullets: 8, requires_evidence: true, avoid: [status_without_owner]}
    qa: [roadmap_gate, accountability_gate]
    absorbed_from: [ppt-master, banana-slides]

  - id: portfolio_allocation
    function: prioritization
    pick_when:
      - Investments, roadmap bets, budget, headcount, or effort need allocation logic.
    skip_when:
      - There is no limited resource to allocate.
    compatible_visuals: [portfolio_allocation, treemap_chart, stacked_bar_chart]
    slots:
      - {name: allocation_categories, type: list, required: true, max_chars: 260, role: categories}
      - {name: rationale, type: text, required: true, max_chars: 140, role: why}
      - {name: tradeoffs, type: list, required: false, max_chars: 220, role: what_not_funded}
    constraints: {max_visible_words: 90, max_bullets: 7, requires_evidence: true, avoid: [allocation_without_tradeoff]}
    qa: [prioritization_gate, decision_gate]
    absorbed_from: [ppt-master]

  - id: brand_principles
    function: creative_direction
    pick_when:
      - A deck needs brand principles, visual rules, or creative territories.
    skip_when:
      - The deck only needs a theme profile; use theme selection.
    compatible_visuals: [brand_principle_cards, moodboard_grid, section_divider]
    slots:
      - {name: principles, type: list, required: true, max_chars: 280, role: principles}
      - {name: proof_of_style, type: list, required: true, max_chars: 220, role: examples}
      - {name: anti_patterns, type: list, required: true, max_chars: 220, role: avoid}
    constraints: {max_visible_words: 100, max_bullets: 8, requires_evidence: false, avoid: [taste_words_without_rule]}
    qa: [design_mastery_gate, brand_consistency_gate]
    absorbed_from: [aiox-brandbook, redpine-ds]

  - id: social_proof_wall
    function: credibility
    pick_when:
      - The argument depends on testimonials, logos, quotes, or adoption proof.
    skip_when:
      - Proof is primarily numeric; use evidence_stack or data_insight.
    compatible_visuals: [logo_wall, testimonial_grid, quote_evidence_panel]
    slots:
      - {name: proof_items, type: list, required: true, max_chars: 320, role: social_proof}
      - {name: relevance_note, type: text, required: true, max_chars: 120, role: why_it_matters}
      - {name: source_note, type: text, required: true, max_chars: 120, role: source}
    constraints: {max_visible_words: 85, max_bullets: 0, requires_evidence: true, avoid: [unsourced_logo_or_quote]}
    qa: [proof_gate, source_gate]
    absorbed_from: [Presenton, presentation-ai]

  - id: objections_matrix
    function: objection_handling
    pick_when:
      - Multiple objections need response, proof, and residual risk in one view.
    skip_when:
      - There is only one core objection; use objection_response.
    compatible_visuals: [objection_matrix, myth_truth, basic_table]
    slots:
      - {name: objections, type: list, required: true, max_chars: 260, role: objections}
      - {name: responses, type: list, required: true, max_chars: 260, role: answers}
      - {name: proof, type: list, required: true, max_chars: 220, role: evidence}
    constraints: {max_visible_words: 120, max_bullets: 0, requires_evidence: true, avoid: [dismissive_or_unproven_response]}
    qa: [objection_gate, proof_gate]
    absorbed_from: [banana-slides, ppt-master]

  - id: user_story_map
    function: product_strategy
    pick_when:
      - Product work needs user activities, tasks, releases, and MVP boundaries.
    skip_when:
      - The content is a linear project plan; use migration_plan or roadmap_status.
    compatible_visuals: [user_story_map, journey_map, roadmap_status_board]
    slots:
      - {name: activities, type: list, required: true, max_chars: 260, role: user_activities}
      - {name: stories, type: list, required: true, max_chars: 320, role: capabilities}
      - {name: release_slice, type: text, required: true, max_chars: 140, role: MVP}
    constraints: {max_visible_words: 115, max_bullets: 0, requires_evidence: true, avoid: [feature_list_without_user_activity]}
    qa: [product_traceability_gate, roadmap_gate]
    absorbed_from: [ppt-master, presentation-ai]

  - id: architecture_tradeoff_table
    function: decision
    pick_when:
      - Technical options need tradeoff comparison by latency, cost, complexity, risk, and operability.
    skip_when:
      - The slide only explains one architecture; use architecture_flow.
    compatible_visuals: [architecture_tradeoff_table, pros_cons_chart, decision_card]
    slots:
      - {name: options, type: list, required: true, max_chars: 240, role: technical_options}
      - {name: criteria, type: list, required: true, max_chars: 220, role: evaluation_criteria}
      - {name: recommendation, type: text, required: true, max_chars: 140, role: decision}
    constraints: {max_visible_words: 120, max_bullets: 0, requires_evidence: true, avoid: [tradeoff_without_operational_criteria]}
    qa: [architecture_gate, decision_gate]
    absorbed_from: [PPTAgent, powerpoint-skill]

  - id: api_request_response
    function: technical_demo
    pick_when:
      - A technical deck must explain an API call, webhook, MCP tool, or integration contract.
    skip_when:
      - There is no concrete request, response, schema, or endpoint.
    compatible_visuals: [api_request_response, code_explanation_split, client_server_flow]
    slots:
      - {name: endpoint_or_tool, type: text, required: true, max_chars: 120, role: interface}
      - {name: request, type: text, required: true, max_chars: 320, role: input}
      - {name: response, type: text, required: true, max_chars: 320, role: output}
      - {name: behavior_note, type: text, required: true, max_chars: 140, role: implication}
    constraints: {max_visible_words: 120, max_bullets: 0, requires_evidence: true, avoid: [pseudo_api_without_schema]}
    qa: [architecture_gate, technical_accuracy_gate]
    absorbed_from: [Presenton, PPTAgent]

  - id: code_explanation
    function: technical_teaching
    pick_when:
      - A deck must explain a code path, config, CLI command, or algorithm.
    skip_when:
      - The audience does not need implementation detail.
    compatible_visuals: [code_explanation_split, basic_table, numbered_steps]
    slots:
      - {name: code_excerpt, type: text, required: true, max_chars: 520, role: code}
      - {name: annotations, type: list, required: true, max_chars: 280, role: explanation}
      - {name: consequence, type: text, required: false, max_chars: 120, role: why_it_matters}
    constraints: {max_visible_words: 140, max_bullets: 6, requires_evidence: true, avoid: [unreadable_code_wall]}
    qa: [code_legibility_gate, technical_accuracy_gate]
    absorbed_from: [Presenton, powerpoint-skill]

  - id: mission_vision
    function: alignment
    pick_when:
      - A product, company, squad, or initiative needs mission, vision, and principles.
    skip_when:
      - The slide is a decorative manifesto with no operating implications.
    compatible_visuals: [mission_vision_panel, brand_principle_cards, section_divider]
    slots:
      - {name: mission, type: text, required: true, max_chars: 140, role: purpose}
      - {name: vision, type: text, required: true, max_chars: 140, role: future_state}
      - {name: principles, type: list, required: false, max_chars: 220, role: decision_rules}
    constraints: {max_visible_words: 80, max_bullets: 5, requires_evidence: false, avoid: [vague_values_without_decision_rule]}
    qa: [alignment_gate, brand_consistency_gate]
    absorbed_from: [Presenton, aiox-brandbook]

  - id: business_challenges
    function: diagnosis
    pick_when:
      - A product overview or proposal must show the main business constraints before the solution.
    skip_when:
      - There is only one root cause; use diagnosis_fishbone.
    compatible_visuals: [business_challenges_grid, risk_heatmap, evidence_cards]
    slots:
      - {name: challenges, type: list, required: true, max_chars: 320, role: constraints}
      - {name: impact, type: list, required: true, max_chars: 260, role: consequences}
      - {name: solution_bridge, type: text, required: true, max_chars: 140, role: transition}
    constraints: {max_visible_words: 95, max_bullets: 8, requires_evidence: true, avoid: [generic_pain_without_business_impact]}
    qa: [buyer_relevance_gate, evidence_gate]
    absorbed_from: [Presenton, banana-slides]

  - id: service_catalog
    function: offer
    pick_when:
      - A deck needs to explain service lines, modules, deliverables, or scope boundaries.
    skip_when:
      - There is one bundled offer; use offer_stack.
    compatible_visuals: [service_catalog_grid, pricing_table, module_composition]
    slots:
      - {name: services, type: list, required: true, max_chars: 320, role: service_lines}
      - {name: deliverables, type: list, required: true, max_chars: 260, role: outputs}
      - {name: fit_note, type: text, required: false, max_chars: 120, role: buyer_fit}
    constraints: {max_visible_words: 100, max_bullets: 8, requires_evidence: false, avoid: [service_list_without_outcomes]}
    qa: [offer_clarity_gate, buyer_relevance_gate]
    absorbed_from: [Presenton, presentation-ai]

  - id: team_credentials
    function: credibility
    pick_when:
      - People, roles, expertise, or delivery capacity are part of the proof.
    skip_when:
      - The audience does not need team trust to decide.
    compatible_visuals: [team_credentials_grid, org_chart, social_proof_wall]
    slots:
      - {name: members, type: list, required: true, max_chars: 260, role: people}
      - {name: credentials, type: list, required: true, max_chars: 260, role: proof}
      - {name: delivery_relevance, type: text, required: true, max_chars: 120, role: why_this_team}
    constraints: {max_visible_words: 95, max_bullets: 0, requires_evidence: true, avoid: [bio_without_relevance]}
    qa: [proof_gate, relevance_gate]
    absorbed_from: [Presenton, ppt-master]

  - id: table_of_contents
    function: navigation
    pick_when:
      - A long deck needs sections, sequence, and audience orientation.
    skip_when:
      - The deck has fewer than eight slides or is meant to feel continuous.
    compatible_visuals: [table_of_contents, agenda_timeline, section_divider]
    slots:
      - {name: sections, type: list, required: true, max_chars: 260, role: chapters}
      - {name: flow_note, type: text, required: false, max_chars: 120, role: narrative_logic}
    constraints: {max_visible_words: 70, max_bullets: 8, requires_evidence: false, avoid: [toc_without_story_flow]}
    qa: [narrative_flow_gate, density_gate]
    absorbed_from: [Presenton]

  - id: contact_next_step
    function: action
    pick_when:
      - The final slide needs contact, QR/link, owner, meeting, or next action.
    skip_when:
      - The final decision has already been specified elsewhere.
    compatible_visuals: [contact_footer, decision_card, closing_card]
    slots:
      - {name: next_action, type: text, required: true, max_chars: 100, role: cta}
      - {name: contact_channels, type: list, required: true, max_chars: 180, role: contact}
      - {name: owner_or_date, type: text, required: false, max_chars: 100, role: accountability}
    constraints: {max_visible_words: 55, max_bullets: 4, requires_evidence: false, avoid: [generic_thank_you_without_action]}
    qa: [cta_gate, accountability_gate]
    absorbed_from: [Presenton, powerpoint-skill]
```


## Referência: references/source/templates/theme/brand-systems.yaml

```yaml
version: 1
brand_system_profiles:
  - id: redpine_editorial_precision
    name: Redpine Editorial Precision
    pick_when:
      - The deck should feel institutional, restrained, engineering-grade, or premium operational.
      - The subject benefits from warm off-white surfaces, hairline rules, and one disciplined red accent.
    skip_when:
      - The deck needs neon cockpit energy, manifesto drama, or high-contrast dark HUD.
      - The user asks for rounded playful SaaS styling.
    historical_sources:
      - ../../../../apps/redpine-ds/src/design-system/tokens.json
      - ../../../../apps/redpine-ds/src/design-system/components.manifest.json
      - ../../../../apps/design/src/data/designs/redpine/DESIGN.md
    tokens:
      colors:
        page: "#FAF8F8"
        elevated: "#FFFFFF"
        panel: "#F4F1F1"
        inset: "#E8E3E3"
        text: "#11090A"
        text_secondary: "#3C3134"
        text_muted: "#5A4F52"
        border: "#E8E3E3"
        border_strong: "#BFB6B6"
        accent: "#AB2832"
        accent_hover: "#8E2129"
        accent_pressed: "#6E1A20"
        success: "#2E6F55"
        warning: "#9E6418"
        info: "#2A4E6E"
      typography:
        display: "'neue-haas-grotesk-display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
        body: "'neue-haas-grotesk-text', 'Helvetica Neue', Helvetica, Arial, sans-serif"
        mono: "SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace"
        display_tracking: "-0.022em"
        body_tracking: "-0.005em"
        eyebrow_tracking: "0.12em"
      shape:
        dominant_radius: "0px"
        input_focus_radius: "2px"
        card_radius: "0px"
        pill_radius: "999px"
      spacing:
        base: "4px"
        scale: [0, 4, 8, 12, 16, 20, 24, 32, 40, 56, 72, 96, 128]
      motion:
        standard: "cubic-bezier(0.2, 0, 0, 1)"
        emphasized: "cubic-bezier(0.2, 0, 0.1, 1)"
        durations: ["120ms", "200ms", "360ms"]
    slide_translation:
      use_for:
        - executive_report
        - financial_presentation
        - safety_or_risk_review
        - institutional_brand_deck
        - engineering_strategy
      patterns:
        - square_cards
        - hairline_tables
        - red_top_rule
        - warm_surface_stack
        - large_serious_display_numbers
      constraints:
        - Do not add a second accent hue.
        - Do not round cards, buttons, or inputs.
        - Prefer borders and surface steps over shadows.
        - Use red for decision, risk, CTA, and focus only.
    absorbed_from: [redpine_ds_tokens, redpine_design_md, redpine_components_manifest]

  - id: aiox_brandbook_cockpit
    name: AIOX Brandbook Cockpit
    pick_when:
      - The deck should feel like AIOX: dark, technical, manifesto-grade, operational, and high-signal.
      - The subject is AI orchestration, SINKRA, benchmark cockpit, product narrative, or movement building.
    skip_when:
      - The deck needs conservative finance/investor neutrality.
      - The user wants a light editorial institutional surface.
    historical_sources:
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/README.md
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/slides/index.html
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/ui_kits/brandbook/README.md
    tokens:
      colors:
        canvas: "#050505"
        surface: "#0F0F11"
        surface_alt: "#1C1E19"
        surface_panel: "#18181B"
        text: "#F4F4E8"
        muted: "#9C9C9C"
        border: "rgba(156,156,156,0.15)"
        accent: "#D1FF00"
        secondary_blue: "#0099FF"
        flare_orange: "#ED4609"
        gold_variant: "#DDD1BB"
      typography:
        display: "TASA Orbiter Display Bold"
        body: "Geist"
        mono: "Geist Mono"
        display_case: "uppercase"
        display_tracking: "-0.05em"
        label_case: "uppercase"
      shape:
        dominant_radius: "0px"
        small_radius: "4px"
        card_radius: "12px"
        full_radius: "999px"
      motion:
        ease_expo: "cubic-bezier(0.16, 1, 0.3, 1)"
        durations: ["200ms", "400ms", "700ms"]
    slide_translation:
      use_for:
        - benchmark_observatory
        - ai_product_strategy
        - movement_manifesto
        - technical_webinar
        - internal_operating_system_deck
      patterns:
        - four_column_architectural_grid
        - oversized_background_wordmark
        - bracket_eyebrow
        - lime_hud_corners
        - bordered_stat_cells
        - manifesto_quote_left_bar
        - ticker_or_mono_footer
      constraints:
        - Never use emoji.
        - Avoid photographic backgrounds.
        - Use lime as the primary signal, not as decoration everywhere.
        - Keep secondary blue/orange sparse for charts or destructive states.
        - Prefer dense operational panels over marketing cards.
    absorbed_from: [aiox_brandbook_bundle, aiox_brandbook_slides, aiox_marketing_ui_kit]
```


## Referência: references/source/templates/theme/design-philosophy-routing.yaml

```yaml
version: 1
name: design-philosophy-routing
purpose: >
  Fallback visual taxonomy for briefs with weak or absent visual direction. Use
  after brand specs, user references, imported PPTX templates, and existing
  design systems have been checked.

precedence:
  - provided_brand_or_brandbook
  - user_reference_screenshot_link_or_deck
  - imported_pptx_or_existing_design_system
  - bundled_theme_profile
  - design_philosophy_fallback

selection_rule: >
  When offering three options, choose three different schools. Do not offer
  three minor variants of the same minimalist or tech style.

schools:
  information_architecture:
    principle: "Data is construction material, not decoration."
    best_for:
      - executive_summary
      - research_report
      - benchmark
      - financial_analysis
    philosophies:
      editorial_typography:
        use_when: "The argument can be carried by strong type, grid, and negative space."
        visual_traits: [strict_grid, extreme_type_hierarchy, one_accent_color, high_whitespace]
      scientific_data_visualization:
        use_when: "The deck must earn belief through precise charts, citations, and dense evidence."
        visual_traits: [rational_sans, integrated_footnotes, precise_axes, neutral_palette]
      content_first_reading:
        use_when: "The deck behaves like a readable essay, memo, or policy paper."
        visual_traits: [system_fonts, long_form_readability, progressive_disclosure, zero_decoration]
      cartographic_information:
        use_when: "Networks, ecosystems, flows, or geography need to feel spatial."
        visual_traits: [layered_data, topographic_depth, warm_dataviz_palette, organic_patterns]
  motion_poetics:
    principle: "Technology has rhythm."
    best_for:
      - product_launch
      - immersive_demo
      - web_native_deck
      - course_promo
    philosophies:
      cinematic_scroll:
        use_when: "The experience should feel like scenes in a journey."
        visual_traits: [film_composition, deep_spacing, parallax_ready, dark_base]
      webgl_particles:
        use_when: "Invisible data, AI, or system flow must become visible."
        visual_traits: [particle_systems, neon_accents, depth_space, reactive_environment]
      algorithmic_generative:
        use_when: "The brand should feel computational, precise, and original."
        visual_traits: [generated_geometry, mathematical_spacing, monochrome_base, vibrant_accent]
      narrative_interaction:
        use_when: "Learning or onboarding should feel like exploration."
        visual_traits: [progress_indicators, illustrative_ui, warm_palette, scroll_reveals]
  minimalism:
    principle: "Reduce until the idea remains."
    best_for:
      - premium_pitch
      - luxury_offer
      - executive_decision
      - manifesto
    philosophies:
      conceptual_monochrome:
        use_when: "One metaphor should govern the whole deck."
        visual_traits: [black_white_primary_colors, typography_as_graphic, rule_breaking_grid]
      swiss_grid_purity:
        use_when: "The deck needs timeless institutional authority."
        visual_traits: [mathematical_grid, strict_alignment, two_colors_max, no_ornament]
      premium_restraint:
        use_when: "High-ticket work needs calm authority and polish."
        visual_traits: [seventy_percent_whitespace, subtle_weight_shifts, sparse_accent, premium_photo]
      joyful_minimalism:
        use_when: "A human service needs clarity with emotional warmth."
        visual_traits: [color_bursts, handmade_detail, optimistic_language, legible_experiment]
  experimental_avant_garde:
    principle: "Breaking rules can create the rule."
    best_for:
      - creative_campaign
      - cultural_deck
      - speculative_technology
      - technical_depth_showcase
    philosophies:
      code_as_drawing:
        use_when: "The making process should be visible and expressive."
        visual_traits: [sketch_lines, construction_marks, pure_black_white, generative_patterns]
      parametric_architecture:
        use_when: "System complexity is the point."
        visual_traits: [recursive_structures, fractal_detail, architectural_data, high_contrast]
      cyber_poetics:
        use_when: "A future-facing story needs warmth, solitude, and cinematic depth."
        visual_traits: [warm_cyberpunk, film_lighting, industrial_luxury, volumetric_light]
      fui_fantasy_interface:
        use_when: "Speculative interfaces and data streams are part of the story."
        visual_traits: [holographic_layers, amber_or_cyan, technical_readouts, believable_future_ui]
  eastern_philosophy:
    principle: "Empty space is content."
    best_for:
      - reflective_manifesto
      - artisan_brand
      - strategic_foresight
      - premium_minimal_brand
    philosophies:
      speculative_design:
        use_when: "The deck should feel like thoughtful technology research."
        visual_traits: [soft_tech, concept_prototypes, gentle_shadows, natural_neutrals]
      emptiness_design:
        use_when: "Luxury or reflection needs extreme restraint."
        visual_traits: [eighty_percent_whitespace, paper_texture, desaturated_palette, zen_simplicity]
      book_architecture:
        use_when: "Dense storytelling should feel editorial and tactile."
        visual_traits: [non_linear_grid, margin_play, unexpected_colors, archival_density]
      ink_wash_digital:
        use_when: "The work needs emotional temperature and poetic negative space."
        visual_traits: [soft_glow, ink_wash_reference, deep_blues, warm_grays, calligraphic_influence]

prompting_rule:
  good: "Describe mood and subject, then let the renderer handle layout."
  bad: "Over-constrain the image prompt with exact slide layout, font sizes, and margins."

output_when_used:
  - selected_school
  - selected_philosophy
  - rejected_options_from_other_schools
  - visual_traits_to_apply
  - traits_to_avoid
  - reason_this_fits_the_audience_and_deck_job
```


## Referência: references/source/templates/theme/theme-tokens.yaml

```yaml
version: 1
theme_profiles:
  - id: sinkra_observatory_dark
    pick_when:
      - Benchmark, observatory, technical strategy, or competitive intelligence deck.
    tokens:
      colors:
        background: "#050505"
        panel: "#111111"
        panel_alt: "#171717"
        text: "#F5F5EF"
        muted: "#9A9A92"
        border: "#2A2A2A"
        accent: "#D7FF3F"
        warning: "#F0B35A"
      typography:
        heading: "Inter Tight"
        body: "Inter"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 48
        grid_columns: 12
      chart:
        grid: "#2A2A2A"
        neutral: "#777777"
        highlight: "#D7FF3F"
    constraints:
      no_gradient_orbs: true
      max_accent_area_percent: 18
      high_contrast_required: true
    absorbed_from: [presentation-ai, ppt-master, current_sinkra_bench]

  - id: executive_clean
    pick_when:
      - Board, finance, investor, or operating review.
    tokens:
      colors:
        background: "#FAFAF7"
        panel: "#FFFFFF"
        text: "#151515"
        muted: "#666666"
        border: "#D9D9D2"
        accent: "#2347FF"
        positive: "#168A4A"
        negative: "#B42318"
      typography:
        heading: "Inter"
        body: "Inter"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 56
        grid_columns: 12
      chart:
        grid: "#E6E6E0"
        neutral: "#7A7A72"
        highlight: "#2347FF"
    constraints:
      chart_labels_required: true
      avoid_decorative_cards: true
      min_body_px: 18
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: editorial_webinar
    pick_when:
      - Webinar, masterclass, persuasive training, or sales education.
    tokens:
      colors:
        background: "#101010"
        panel: "#181818"
        text: "#F7F3EA"
        muted: "#B3ACA1"
        border: "#32302C"
        accent: "#FFB84D"
        secondary: "#7DD3C7"
      typography:
        heading: "Sora"
        body: "Inter"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 52
        grid_columns: 12
      chart:
        grid: "#35322D"
        neutral: "#8A8378"
        highlight: "#FFB84D"
    constraints:
      max_visible_words: 70
      every_section_needs_visual: true
      avoid_motivational_filler: true
    absorbed_from: [presentation-ai, slide-deck-ai]

  - id: consulting_midnight
    pick_when:
      - High-stakes benchmark, strategy, or transformation deck with dense evidence.
    tokens:
      colors:
        background: "#090A0B"
        panel: "#14161A"
        text: "#F3F1E8"
        muted: "#A4A09A"
        border: "#2D3138"
        accent: "#B6F04A"
        secondary: "#62C6FF"
        critical: "#FF5E5B"
      typography:
        heading: "Inter Tight"
        body: "Inter"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 48
        grid_columns: 12
      chart:
        grid: "#2D3138"
        neutral: "#7C828C"
        highlight: "#B6F04A"
    constraints:
      high_contrast_required: true
      no_gradient_orbs: true
      table_density_allowed: true
    absorbed_from: [current_sinkra_bench, ppt-master]

  - id: boardroom_graphite
    pick_when:
      - Board, investor update, operating review, or risk decision deck.
    tokens:
      colors:
        background: "#F7F7F4"
        panel: "#FFFFFF"
        panel_alt: "#ECECE7"
        text: "#171717"
        muted: "#666A70"
        border: "#D7D7D0"
        accent: "#2457D6"
        positive: "#0F8B5F"
        negative: "#C13A2F"
      typography:
        heading: "Aptos Display"
        body: "Aptos"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 56
        grid_columns: 12
      chart:
        grid: "#E1E1DB"
        neutral: "#777B80"
        highlight: "#2457D6"
    constraints:
      chart_labels_required: true
      min_body_px: 18
      avoid_decorative_cards: true
    absorbed_from: [powerpoint-skill, ppt-master]

  - id: founder_pitch_light
    pick_when:
      - Fundraising, product pitch, founder narrative, or strategic company story.
    tokens:
      colors:
        background: "#FBFAF5"
        panel: "#FFFFFF"
        text: "#111315"
        muted: "#67615A"
        border: "#DDD8CD"
        accent: "#E5484D"
        secondary: "#1F9D8A"
        tertiary: "#F2C94C"
      typography:
        heading: "Sora"
        body: "Inter"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 52
        grid_columns: 12
      chart:
        grid: "#E5DFD3"
        neutral: "#8E887E"
        highlight: "#E5484D"
    constraints:
      every_section_needs_visual: true
      max_accent_area_percent: 14
      avoid_stock_like_blur: true
    absorbed_from: [presentation-ai, Presenton]

  - id: technical_blueprint
    pick_when:
      - Architecture, system design, technical review, API, MCP, or integration deck.
    tokens:
      colors:
        background: "#071018"
        panel: "#0E1B26"
        text: "#EAF6FF"
        muted: "#8EA5B6"
        border: "#233747"
        accent: "#51D6FF"
        secondary: "#9BDB7B"
        warning: "#F6C85F"
      typography:
        heading: "IBM Plex Sans"
        body: "Inter"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 48
        grid_columns: 12
      chart:
        grid: "#233747"
        neutral: "#7890A0"
        highlight: "#51D6FF"
    constraints:
      diagram_labels_required: true
      arrow_labels_required: true
      max_visible_words: 85
    absorbed_from: [PPTAgent, powerpoint-skill]

  - id: academic_paper
    pick_when:
      - Research, academic, literature review, technical evidence, or methods deck.
    tokens:
      colors:
        background: "#FFFFFF"
        panel: "#F4F6F8"
        text: "#1A1D21"
        muted: "#626A73"
        border: "#DDE3EA"
        accent: "#2F6FED"
        secondary: "#7A4DD8"
        highlight: "#F5B841"
      typography:
        heading: "Source Serif 4"
        body: "Inter"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 58
        grid_columns: 12
      chart:
        grid: "#DDE3EA"
        neutral: "#7F8791"
        highlight: "#2F6FED"
    constraints:
      source_labels_required: true
      appendix_allowed: true
      avoid_unverified_claims: true
    absorbed_from: [PPTAgent, ppt-master]

  - id: product_saas_clean
    pick_when:
      - Product strategy, roadmap, customer journey, demo, or SaaS operating deck.
    tokens:
      colors:
        background: "#F8FAFC"
        panel: "#FFFFFF"
        text: "#101828"
        muted: "#667085"
        border: "#D0D5DD"
        accent: "#155EEF"
        secondary: "#12B76A"
        warning: "#FDB022"
      typography:
        heading: "Inter Tight"
        body: "Inter"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 52
        grid_columns: 12
      chart:
        grid: "#EAECF0"
        neutral: "#98A2B3"
        highlight: "#155EEF"
    constraints:
      component_like_layouts_allowed: true
      cards_max_radius_px: 8
      no_nested_cards: true
    absorbed_from: [presentation-ai, Presenton]

  - id: high_contrast_accessible
    pick_when:
      - The audience, venue, or export medium requires maximum legibility and accessibility.
    tokens:
      colors:
        background: "#000000"
        panel: "#111111"
        text: "#FFFFFF"
        muted: "#C7C7C7"
        border: "#4A4A4A"
        accent: "#FFE500"
        secondary: "#00D4FF"
        negative: "#FF4D4F"
      typography:
        heading: "Atkinson Hyperlegible"
        body: "Atkinson Hyperlegible"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 60
        grid_columns: 12
      chart:
        grid: "#4A4A4A"
        neutral: "#B0B0B0"
        highlight: "#FFE500"
    constraints:
      minimum_contrast_ratio: 7
      min_body_px: 22
      avoid_thin_lines: true
    absorbed_from: [powerpoint-skill, ppt-master]

  - id: brandbook_editorial
    pick_when:
      - Brand strategy, design narrative, manifesto, or visually expressive leadership deck.
    tokens:
      colors:
        background: "#11100E"
        panel: "#1C1915"
        text: "#F6F0E6"
        muted: "#B8AA99"
        border: "#39332B"
        accent: "#F2613F"
        secondary: "#55C2A2"
        highlight: "#F2CB57"
      typography:
        heading: "Space Grotesk"
        body: "Inter"
        mono: "IBM Plex Mono"
      spacing:
        canvas: "16:9"
        margin_px: 54
        grid_columns: 12
      chart:
        grid: "#39332B"
        neutral: "#8D8173"
        highlight: "#F2613F"
    constraints:
      expressive_but_readable: true
      image_motif_required: true
      max_accent_area_percent: 20
    absorbed_from: [aiox-brandbook, redpine-ds, presentation-ai]

  - id: healthcare_trust
    pick_when:
      - Healthcare, wellbeing, clinical operations, or trust-sensitive service deck.
    tokens:
      colors: {background: "#F7FBFA", panel: "#FFFFFF", text: "#10201D", muted: "#5F716D", border: "#D9E7E3", accent: "#087F73", secondary: "#2F80ED", warning: "#E9A23B"}
      typography: {heading: "Inter Tight", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 56, grid_columns: 12}
      chart: {grid: "#D9E7E3", neutral: "#7A8D89", highlight: "#087F73"}
    constraints: {high_trust_tone: true, avoid_alarmist_color_use: true, source_labels_required: true}
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: fintech_precision
    pick_when:
      - Finance, fintech, pricing, unit economics, investment, or risk deck.
    tokens:
      colors: {background: "#F5F7FA", panel: "#FFFFFF", text: "#121826", muted: "#5D6678", border: "#D8DEE8", accent: "#0052CC", secondary: "#00A76F", negative: "#D92D20"}
      typography: {heading: "Aptos Display", body: "Aptos", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 56, grid_columns: 12}
      chart: {grid: "#D8DEE8", neutral: "#7B8496", highlight: "#0052CC"}
    constraints: {right_align_numbers: true, chart_labels_required: true, fake_precision_forbidden: true}
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: education_workshop
    pick_when:
      - Course, workshop, enablement, classroom, or internal training deck.
    tokens:
      colors: {background: "#FFFCF5", panel: "#FFFFFF", text: "#1F2933", muted: "#6B7280", border: "#E7E1D2", accent: "#7C3AED", secondary: "#F59E0B", positive: "#059669"}
      typography: {heading: "Sora", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 54, grid_columns: 12}
      chart: {grid: "#E7E1D2", neutral: "#8B8790", highlight: "#7C3AED"}
    constraints: {exercise_blocks_required: true, max_visible_words: 80, example_density_required: true}
    absorbed_from: [presentation-ai, slide-deck-ai]

  - id: enterprise_rfp
    pick_when:
      - Enterprise proposal, procurement, RFP, implementation plan, or compliance deck.
    tokens:
      colors: {background: "#F8F9FB", panel: "#FFFFFF", text: "#172033", muted: "#667085", border: "#D9DFEA", accent: "#1849A9", secondary: "#6172F3", warning: "#DC6803"}
      typography: {heading: "Inter", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 52, grid_columns: 12}
      chart: {grid: "#D9DFEA", neutral: "#8A93A5", highlight: "#1849A9"}
    constraints: {decision_tables_allowed: true, source_labels_required: true, avoid_marketing_fluff: true}
    absorbed_from: [ppt-master, presentation-ai]

  - id: product_launch_vivid
    pick_when:
      - Product launch, GTM, campaign, community announcement, or release narrative.
    tokens:
      colors: {background: "#0D0F14", panel: "#171A22", text: "#F8FAFC", muted: "#AEB7C7", border: "#2B3140", accent: "#FF6B35", secondary: "#00C2A8", highlight: "#FFD166"}
      typography: {heading: "Space Grotesk", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 50, grid_columns: 12}
      chart: {grid: "#2B3140", neutral: "#8792A6", highlight: "#FF6B35"}
    constraints: {launch_motif_allowed: true, max_accent_area_percent: 18, no_gradient_orbs: true}
    absorbed_from: [Presenton, presentation-ai]

  - id: nonprofit_policy
    pick_when:
      - Policy, impact, nonprofit, institutional, public-interest, or stakeholder trust deck.
    tokens:
      colors: {background: "#FAFAF8", panel: "#FFFFFF", text: "#1C1D1F", muted: "#63666A", border: "#DCDDD8", accent: "#2E7D5B", secondary: "#4A6FA5", warning: "#B7791F"}
      typography: {heading: "Source Serif 4", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 58, grid_columns: 12}
      chart: {grid: "#DCDDD8", neutral: "#7B7F82", highlight: "#2E7D5B"}
    constraints: {plain_language_required: true, source_labels_required: true, avoid_overstatement: true}
    absorbed_from: [ppt-master]

  - id: luxury_minimal
    pick_when:
      - Premium brand, portfolio, private client, executive keynote, or high-end service deck.
    tokens:
      colors: {background: "#F6F3EE", panel: "#FFFFFF", text: "#171412", muted: "#756E66", border: "#DED6CA", accent: "#8A6F3D", secondary: "#2E5E5E", highlight: "#C9A646"}
      typography: {heading: "Cormorant Garamond", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 64, grid_columns: 12}
      chart: {grid: "#DED6CA", neutral: "#8B8278", highlight: "#8A6F3D"}
    constraints: {low_density_required: true, max_visible_words: 55, avoid_decorative_clutter: true}
    absorbed_from: [aiox-brandbook, Presenton]

  - id: cyber_security_dark
    pick_when:
      - Security, incident, infrastructure, reliability, compliance, or technical risk deck.
    tokens:
      colors: {background: "#05070A", panel: "#10151D", text: "#EEF6FF", muted: "#9AABBC", border: "#263241", accent: "#00E5A8", secondary: "#4D8DFF", negative: "#FF4D6D"}
      typography: {heading: "IBM Plex Sans", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 48, grid_columns: 12}
      chart: {grid: "#263241", neutral: "#7D8FA3", highlight: "#00E5A8"}
    constraints: {secret_values_forbidden: true, boundary_labels_required: true, high_contrast_required: true}
    absorbed_from: [PPTAgent, powerpoint-skill]

  - id: creator_webinar
    pick_when:
      - Creator-led webinar, community launch, educational sales, or public masterclass.
    tokens:
      colors: {background: "#15110F", panel: "#211B18", text: "#FFF7ED", muted: "#C8B8AA", border: "#3A302A", accent: "#FF7A1A", secondary: "#8B5CF6", highlight: "#FACC15"}
      typography: {heading: "Sora", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 52, grid_columns: 12}
      chart: {grid: "#3A302A", neutral: "#9A8B7E", highlight: "#FF7A1A"}
    constraints: {belief_shift_required: true, offer_slide_allowed: true, avoid_motivational_filler: true}
    absorbed_from: [banana-slides, presentation-ai]

  - id: legal_compliance
    pick_when:
      - Legal, privacy, compliance, audit, procurement, or board risk deck.
    tokens:
      colors: {background: "#F9FAFB", panel: "#FFFFFF", text: "#111827", muted: "#6B7280", border: "#D1D5DB", accent: "#1D4ED8", secondary: "#374151", warning: "#B45309"}
      typography: {heading: "Aptos Display", body: "Aptos", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 58, grid_columns: 12}
      chart: {grid: "#E5E7EB", neutral: "#808896", highlight: "#1D4ED8"}
    constraints: {source_labels_required: true, legal_overstatement_forbidden: true, high_contrast_required: true}
    absorbed_from: [powerpoint-skill, ppt-master]

  - id: data_analytics_lab
    pick_when:
      - Analytics, data science, experimentation, BI, product metrics, or research deck.
    tokens:
      colors: {background: "#08111F", panel: "#111C2E", text: "#EAF2FF", muted: "#9BAFCC", border: "#26364F", accent: "#38BDF8", secondary: "#A78BFA", positive: "#34D399"}
      typography: {heading: "IBM Plex Sans", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 48, grid_columns: 12}
      chart: {grid: "#26364F", neutral: "#7D90AD", highlight: "#38BDF8"}
    constraints: {chart_labels_required: true, statistical_context_required: true, no_decorative_chartjunk: true}
    absorbed_from: [ppt-master, presentation-ai]

  - id: creative_agency
    pick_when:
      - Creative pitch, campaign platform, brand territory, content concept, or portfolio deck.
    tokens:
      colors: {background: "#FAF7F2", panel: "#FFFFFF", text: "#17120F", muted: "#756B61", border: "#E5D8C8", accent: "#D946EF", secondary: "#F97316", highlight: "#0EA5E9"}
      typography: {heading: "Space Grotesk", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 54, grid_columns: 12}
      chart: {grid: "#E5D8C8", neutral: "#8D8177", highlight: "#D946EF"}
    constraints: {visual_reference_required: true, max_accent_area_percent: 16, avoid_generic_stock: true}
    absorbed_from: [aiox-brandbook, presentation-ai]

  - id: government_policy
    pick_when:
      - Public policy, institutional reporting, civic impact, grant, or public-sector deck.
    tokens:
      colors: {background: "#F8FAFC", panel: "#FFFFFF", text: "#0F172A", muted: "#64748B", border: "#CBD5E1", accent: "#1E3A8A", secondary: "#0F766E", warning: "#92400E"}
      typography: {heading: "Source Serif 4", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 60, grid_columns: 12}
      chart: {grid: "#CBD5E1", neutral: "#8491A3", highlight: "#1E3A8A"}
    constraints: {plain_language_required: true, source_labels_required: true, accessibility_required: true}
    absorbed_from: [ppt-master]

  - id: startup_demo_neon
    pick_when:
      - AI demo, product reveal, hackathon, developer tool, or technical product showcase.
    tokens:
      colors: {background: "#06070D", panel: "#101322", text: "#F8FBFF", muted: "#AAB4C5", border: "#2B3147", accent: "#7CFF6B", secondary: "#5B8CFF", highlight: "#FF4FD8"}
      typography: {heading: "Inter Tight", body: "Inter", mono: "IBM Plex Mono"}
      spacing: {canvas: "16:9", margin_px: 48, grid_columns: 12}
      chart: {grid: "#2B3147", neutral: "#8490A8", highlight: "#7CFF6B"}
    constraints: {demo_artifact_required: true, no_gradient_orbs: true, high_contrast_required: true}
    absorbed_from: [Presenton, PPTAgent]
```


## Referência: references/source/templates/visual/ai-image-type-routing.yaml

```yaml
version: 1
source_principle: >
  Image type is the internal composition of an AI-generated visual block, not
  the whole slide layout. Select it after the slide function and before prompt
  writing so visuals support the narrative instead of becoming decoration.
absorbed_from:
  - ../../../../../../bench/ppt-master/skills/ppt-master/references/image-type-templates/_index.md
  - ../../../../../../bench/ppt-master/skills/ppt-master/references/image-type-templates/hero.md
  - ../../../../../../bench/ppt-master/skills/ppt-master/references/image-type-templates/matrix.md

route_order:
  - slide_function
  - visual_purpose_keywords
  - image_type
  - container_size
  - text_policy
  - prompt_skeleton
  - overlay_or_native_text_plan

text_policies:
  none:
    use_when:
      - The slide needs precise copy, labels, numbers, axis names, or citations.
      - Text must remain editable in PPTX/HTML.
    rule: Generate image without text and overlay native text in the slide.
  embedded:
    use_when:
      - The text is ornamental, short, non-critical, or part of a realistic scene.
    rule: Keep embedded text under 3 words and validate rendered output.

default_container_sizes:
  hero_large:
    aspect_ratio: "16:9"
    slide_area: "60-85%"
    use_for: [hero, background, scene]
  evidence_panel:
    aspect_ratio: "4:3 | 3:2"
    slide_area: "35-60%"
    use_for: [infographic, flowchart, framework, comparison, timeline]
  icon_or_support:
    aspect_ratio: "1:1"
    slide_area: "12-30%"
    use_for: [portrait, typography, map]
  full_canvas:
    aspect_ratio: "slide"
    slide_area: "100%"
    use_for: [background]

purpose_keyword_routing:
  - keywords: [atmosphere, opening, mood, context, texture]
    image_type: background
  - keywords: [main, protagonist, hero, product, device, object]
    image_type: hero
  - keywords: [person, founder, customer, audience, persona]
    image_type: portrait
  - keywords: [wordmark, lettering, headline, typographic]
    image_type: typography
  - keywords: [data, concept, education, explainer, infographic]
    image_type: infographic
  - keywords: [steps, process, sequence, workflow]
    image_type: flowchart
  - keywords: [model, method, system, mental_model, framework]
    image_type: framework
  - keywords: [quadrant, position, map, tradeoff, axis]
    image_type: matrix
  - keywords: [loop, flywheel, cycle, recurring]
    image_type: cycle
  - keywords: [conversion, narrowing, funnel, pipeline]
    image_type: funnel
  - keywords: [hierarchy, levels, maturity, pyramid]
    image_type: pyramid
  - keywords: [before_after, versus, alternative, compare]
    image_type: comparison
  - keywords: [history, roadmap, phases, milestones]
    image_type: timeline
  - keywords: [geography, territory, route, location]
    image_type: map
  - keywords: [environment, realistic_context, demo_scene, use_case]
    image_type: scene

image_types:
  - id: background
    composition: Full-bleed atmospheric or contextual canvas with low focal competition.
    default_container: full_canvas
    text_policy: none
    use_when:
      - A slide needs atmosphere behind native copy.
      - Hero copy must sit over an image without losing contrast.
    avoid_when:
      - The message needs inspectable product detail.

  - id: hero
    composition: One dominant subject using 60-70% of the visual, minimal supporting detail, generous margin.
    default_container: hero_large
    text_policy: none
    rules:
      - Subject must be identifiable at thumbnail size.
      - Keep at least 15% clean space for native title/caption.
    use_when:
      - The slide needs a single product, object, person, or concept to anchor attention.

  - id: portrait
    composition: Person or archetype with controlled background and expression aligned to audience role.
    default_container: icon_or_support
    text_policy: none
    use_when:
      - Personas, customer stakes, founder story, or role-based narrative matter.
    avoid_when:
      - The deck should avoid synthetic people or unsupported identity signals.

  - id: typography
    composition: Lettering or wordmark-like visual texture.
    default_container: icon_or_support
    text_policy: embedded
    use_when:
      - Decorative short type is the visual subject.
    avoid_when:
      - The text is a claim, number, citation, or instruction.

  - id: infographic
    composition: Visual explanation with icons, simplified objects, and clear hierarchy.
    default_container: evidence_panel
    text_policy: none
    use_when:
      - A concept needs visual explanation but exact labels stay native.

  - id: flowchart
    composition: Connected nodes with directional flow and clear start/end.
    default_container: evidence_panel
    text_policy: none
    use_when:
      - Steps or dependencies are important but should remain editable via overlays.

  - id: framework
    composition: Named model or system structure with modular regions.
    default_container: evidence_panel
    text_policy: none
    use_when:
      - The slide explains a method, operating model, or mechanism.

  - id: matrix
    composition: Equal 2x2 quadrant skeleton with balanced visual weight and visible axes.
    default_container: evidence_panel
    text_policy: none
    rules:
      - Use equal quadrant sizes.
      - Do not place the main message in the center crossing.
      - Keep quadrant icons or objects at 40-60% of each quadrant.
      - Overlay axis labels and quadrant labels as native text.
    use_when:
      - Two independent axes explain positioning, priority, risk, or strategy.

  - id: cycle
    composition: Circular or flywheel process with repeating stages.
    default_container: evidence_panel
    text_policy: none
    use_when:
      - Recurrence matters more than sequence completion.

  - id: funnel
    composition: Wide-to-narrow or stage-gated conversion shape.
    default_container: evidence_panel
    text_policy: none
    use_when:
      - Attrition, qualification, or narrowing choice is the message.

  - id: pyramid
    composition: Stacked hierarchy with stable base and clear levels.
    default_container: evidence_panel
    text_policy: none
    use_when:
      - Maturity, hierarchy, or dependency levels are the concept.

  - id: comparison
    composition: Two or three alternatives shown with symmetrical visual treatment.
    default_container: evidence_panel
    text_policy: none
    use_when:
      - The slide contrasts states, options, products, or before/after.

  - id: timeline
    composition: Horizontal or vertical progression with milestones.
    default_container: evidence_panel
    text_policy: none
    use_when:
      - Time, phases, or roadmap sequence is the proof.

  - id: map
    composition: Geographic or territory representation with region emphasis.
    default_container: icon_or_support
    text_policy: none
    use_when:
      - Location, territory, or route is meaningful.

  - id: scene
    composition: Realistic or stylized use-case environment with subject and context.
    default_container: hero_large
    text_policy: none
    use_when:
      - A demo moment, operating environment, or customer context must feel concrete.

rules:
  - Most decks should use 2-5 image types. More than that usually creates visual noise.
  - Never ask an image model to render exact data tables, long labels, formulas, or citations.
  - Every generated visual must declare whether it is decorative, explanatory, evidentiary, or product-representational.
  - Product-representational visuals must not invent UI, logos, charts, or screenshots unless clearly labeled as conceptual.
```


## Referência: references/source/templates/visual/aiox-brandbook-deep-patterns.yaml

```yaml
version: 1
historical_sources:
  - ../../../../apps/aiox-brandbook/src/components/brandbook-sections/editorial/spread-section.tsx
  - ../../../../apps/aiox-brandbook/src/components/brandbook-sections/editorial/evidence-spread.tsx
  - ../../../../apps/aiox-brandbook/src/components/brandbook-sections/editorial/narrative-spread.tsx
  - ../../../../apps/aiox-brandbook/src/components/brandbook/molecules/bb-stat-cell.tsx
  - ../../../../apps/aiox-brandbook/src/components/blocks/cohort/problem-section.tsx
  - ../../../../apps/aiox-brandbook/src/components/blocks/cohort/proof-section.tsx
  - ../../../../apps/aiox-brandbook/src/components/blocks/cohort/offer-section.tsx
  - ../../../../apps/aiox-brandbook/src/components/pitch-deck/page-header.tsx
  - ../../../../apps/aiox-brandbook/src/components/pitch-deck/metric-card.tsx
  - ../../../../apps/aiox-brandbook/src/components/pitch-deck/investor-insight.tsx
  - ../../../../apps/aiox-brandbook/src/app/(pitch-deck)/pitch-deck/competitive-analysis/page.tsx
  - ../../../../apps/aiox-brandbook/src/app/(pitch-deck)/pitch-deck/finance/page.tsx
  - ../../../../apps/aiox-brandbook/src/app/(pitch-deck)/pitch-deck/roadmap/page.tsx

patterns:
  - id: aiox_editorial_book_spread
    category: editorial_spread
    pick_when:
      - A deck needs brandbook-like two-page editorial pacing.
      - One side carries thesis or framework and the other carries proof, voice, or examples.
    skip_when:
      - The slide must be a single-screen dashboard or dense matrix.
    structure:
      container: two_page_spread
      left_page: thesis_or_framework
      right_page: proof_or_application
      footer: page_number_section_name_brandline
    constraints:
      min_height_px: 800
      page_padding: "4rem"
      page_divider_required: true
      mono_footer_required: true
      lime_page_number_chip: true
    absorbed_from: [aiox_editorial_spread_section]

  - id: aiox_evidence_wall
    category: proof
    pick_when:
      - The slide needs many compact proof points with source labels.
      - Results are more persuasive as a wall than as a single case study.
    skip_when:
      - There are fewer than three proof points; use proof_before_after.
    structure:
      grid: "2x3 or 3x2 stat cells"
      cell_slots: [value, label, description, source]
      highlight_cells: "1-2 allowed"
      secondary_badges: [license, agents, integrations]
    constraints:
      source_required_per_cell: true
      highlight_cells_max: 2
      value_uses_display_font: true
      grid_gap: "1px"
    absorbed_from: [aiox_evidence_spread, aiox_proof_section]

  - id: aiox_hero_journey_four_acts
    category: narrative
    pick_when:
      - The deck uses transformation narrative, community story, or founder/customer awakening.
    skip_when:
      - The message is purely operational with no identity shift.
    structure:
      acts:
        - sleep_or_old_world
        - call_or_red_pill
        - descent_or_learning_loop
        - awakening_or_new_identity
      slots: [roman_index, act_title, act_description, metaphor_line]
    constraints:
      acts_exactly: 4
      metaphor_must_match_brand: true
      use_testimonials_on_adjacent_slide: true
    absorbed_from: [aiox_narrative_spread]

  - id: aiox_voice_testimonial_column
    category: proof_voice
    pick_when:
      - The deck needs social proof that sounds like real audience language.
    skip_when:
      - Testimonials are generic or fabricated.
    structure:
      cards: "4-8 quote strips"
      slots: [quote, author, proof_type]
      emphasis_rule: "empowerment quotes get lime left border"
    constraints:
      exact_language_preferred: true
      author_or_source_required: true
      proof_type_required: true
    absorbed_from: [aiox_narrative_spread, aiox_proof_section]

  - id: aiox_problem_ticker_stage
    category: tension
    pick_when:
      - A problem must feel systemic and recurring, not isolated.
      - Statistics and hidden costs can run as ambient proof.
    skip_when:
      - The proof is too sparse for ticker repetition.
    structure:
      top_ticker: statistics
      center: mono_label_plus_big_claim
      bottom_ticker: hidden_costs
      followup_grid: statistics_plus_cost_cards
    constraints:
      ticker_items_min: 4
      center_claim_max_words: 18
      hidden_costs_use_warning_or_error_accent: true
    absorbed_from: [aiox_cohort_problem_section]

  - id: aiox_offer_two_column_stack
    category: conversion
    pick_when:
      - A paid offer needs benefits, anti-features, ownership claim, tiers, ROI, and testimonial.
    skip_when:
      - There is no price, package, or CTA.
    structure:
      left_column: [included_benefits, anti_features, ownership_claim]
      right_column: [pricing_tiers, recommended_badge, payback, roi, cta]
      bottom: testimonial_dark_card
    constraints:
      benefits_required: true
      anti_features_required: true
      primary_tier_required: true
      payback_or_roi_required_for_financial_claims: true
      testimonial_required: true
    absorbed_from: [aiox_cohort_offer_section]

  - id: aiox_pitch_page_header
    category: pitch_component
    pick_when:
      - A pitch or strategy section needs compact navigation context.
    skip_when:
      - The slide is a cinematic hero or section divider.
    structure:
      icon_box: primary_tint
      title: h1
      badge: optional
      subtitle: one_sentence
    constraints:
      subtitle_required: true
      icon_must_match_section: true
      badge_max_words: 3
    absorbed_from: [aiox_pitch_page_header]

  - id: aiox_metric_card_row
    category: pitch_component
    pick_when:
      - Unit economics, traction, KPI, or operational metrics need scannable cards.
    skip_when:
      - Metrics require target/actual; use bullet_chart.
    structure:
      card_slots: [icon, value, label, caption]
      row_layout: "2-3 columns desktop, 1 column mobile"
    constraints:
      caption_required: true
      value_unit_required: true
      icon_not_decorative: true
    absorbed_from: [aiox_pitch_metric_card, aiox_finance_page]

  - id: aiox_investor_insight_callout
    category: pitch_component
    pick_when:
      - A slide needs a labeled investor-facing interpretation of data.
    skip_when:
      - The content is raw data only or a generic note.
    variants:
      - why_it_matters
      - market_advantage
      - investor_insight
      - benchmark
      - highlight
    structure:
      left_border: variant
      icon: variant
      label: uppercase
      body: concise_interpretation
    constraints:
      interpretation_required: true
      not_for_repeating_the_same_data: true
      max_visible_words: 65
    absorbed_from: [aiox_pitch_investor_insight]

  - id: aiox_category_creation_matrix
    category: competitive_analysis
    pick_when:
      - The deck must show that the product belongs to a new category, not merely a better existing tool.
    skip_when:
      - Competitors are truly same-category alternatives.
    structure:
      market_categories: [category, players, description, is_our_category]
      competitor_table: [competitor, category, strength, limitation, our_advantage]
      differentiators: [icon, title, description, contrast]
      moat_reasons: [title, description]
    constraints:
      separate_category_cards_before_matrix: true
      our_category_badge_required: true
      strength_and_limitation_required: true
      advantage_must_be_structural: true
    absorbed_from: [aiox_pitch_competitive_analysis]

  - id: aiox_gate_driven_roadmap
    category: roadmap
    pick_when:
      - Roadmap should communicate milestones unlocked by evidence, not arbitrary dates.
    skip_when:
      - The roadmap is a strict Gantt with durations and dependencies.
    structure:
      philosophy_card: gate_driven_statement
      timeline: [quarter, phase, items, status]
      status_types: [completed, in_progress, planned]
      milestone_table: [quarter, milestone, status]
      post_seed_vision: optional
    constraints:
      status_badges_required: true
      connector_line_required: true
      each_phase_needs_unlock_metric_or_condition: true
    absorbed_from: [aiox_pitch_roadmap_page]
```


## Referência: references/source/templates/visual/brand-fidelity-playbooks.yaml

```yaml
version: 1
name: brand-fidelity-playbooks
purpose: >
  Playbooks for replicating the visual language of a reference deck or brand
  system without reducing fidelity to logo and colors.

score_target:
  template_import_replication__brand_fidelity: 95
  theme_tokens_branding__brand_guardrails: 95

fidelity_lenses:
  - id: non_color_identity
    question: "What makes the deck recognizable if all brand colors are removed?"
    required_evidence:
      - grid_behavior
      - type_scale_behavior
      - component_shape_language
      - density_rhythm
      - image_or_diagram_treatment
  - id: component_reuse
    question: "Which repeated components carry the brand system?"
    required_evidence:
      - component_name
      - visual_rules
      - slot_rules
      - slide_functions_supported
      - anti_patterns
  - id: narrative_visual_fit
    question: "Does the visual style support the deck's persuasion job?"
    required_evidence:
      - audience_context
      - slide_function_map_alignment
      - proof_visibility
      - emotional_temperature
  - id: render_fidelity
    question: "Does the rendered slide preserve the locked brand behavior?"
    required_evidence:
      - key_slide_render_review
      - before_after_patch_list
      - unresolved_visual_debt

playbooks:
  - id: imported_template_fidelity
    use_when:
      - user_provides_pptx_template
      - user_provides_client_brand_deck
      - output_must_feel_like_existing_deck
    steps:
      - create_or_load_brand_template_manifest
      - extract_non_color_identity
      - map_source_components_to_slide_functions
      - define_theme_runtime_mapping
      - select_layouts_by_function
      - render_key_slides
      - compare_against_manifest
      - patch_only_scoped_visual_debt
    block_if:
      - source_reference_missing
      - no_non_color_traits
      - no_component_patterns
      - no_rendered_key_slide_review
      - visual_copy_depends_on_flat_screenshot
    pass_definition: >
      Key slides are visibly in the same language family as the reference deck,
      while content remains editable and slide functions remain explicit.

  - id: editorial_brand_system
    use_when:
      - brand_manifesto
      - category_creation_deck
      - premium_workshop_deck
      - founder_strategy_deck
    steps:
      - choose_brand_system_or_design_philosophy
      - define_visual_thesis
      - assign_hero_evidence_quiet_slide_ratio
      - map_motifs_to_slide_functions
      - lock_typographic_and_metadata_language
      - review_cover_reframe_proof_cta
    block_if:
      - every_slide_uses_same_hero_or_card_pattern
      - motif_is_decorative_only
      - evidence_slide_does_not_match_editorial_language
    pass_definition: >
      The deck has a recognizable editorial system, not a set of isolated nice
      slides.

  - id: operational_design_system
    use_when:
      - dashboard_or_benchmark_deck
      - incident_review
      - board_operating_review
      - product_metrics_review
    steps:
      - define_semantic_status_tokens
      - define_table_and_chart_density_budget
      - map_status_components_to_slide_functions
      - lock_accessibility_and_contrast_rules
      - render_dense_key_slide
      - inspect_at_screenshot_scale
    block_if:
      - status_meaning_depends_on_color_only
      - dense_table_has_no_grouping_or_scan_path
      - charts_ignore_theme_tokens
    pass_definition: >
      High-density slides look intentional and scannable rather than crowded.

  - id: technical_diagram_brand_system
    use_when:
      - architecture_deck
      - api_demo
      - research_method_deck
      - engineering_update
    steps:
      - select_diagram_engine
      - define_node_edge_label_tokens
      - map_diagram_type_to_slide_function
      - keep_code_or_formula_text_fit_rules
      - render_mechanism_slide
      - inspect_line_weight_and_label_hierarchy
    block_if:
      - diagram_uses_unmapped_default_colors
      - code_or_formula_is_unreadable
      - diagram_is_visual_decoration_without_explanatory_job
    pass_definition: >
      Diagrams carry the same visual system as the rest of the deck and clarify
      the argument.

brand_fidelity_report:
  deck_id: ""
  source_reference: ""
  selected_playbook: ""
  non_color_identity:
    - trait: ""
      evidence: ""
      applied_to_slides: []
  component_map:
    - component: ""
      source_behavior: ""
      local_template_or_wireframe: ""
      slide_functions: []
  theme_runtime_map:
    colors: "pass | warn | fail"
    typography: "pass | warn | fail"
    charts: "pass | warn | fail"
    diagrams: "pass | warn | fail"
    tables: "pass | warn | fail"
  rendered_findings:
    - slide_id: ""
      verdict: "pass | warn | fail"
      visual_debt: []
  final_score: 0
```


## Referência: references/source/templates/visual/brand-system-patterns.yaml

```yaml
version: 1
brand_system_patterns:
  - id: aiox_four_column_hero
    brand_profile: aiox_brandbook_cockpit
    category: slide_layout
    pick_when:
      - The slide needs a manifesto-grade opening or section thesis.
    skip_when:
      - The slide is data dense or requires many comparison dimensions.
    slots:
      - eyebrow
      - oversized_background_wordmark
      - action_title
      - subtitle
      - mono_footer
    constraints:
      max_visible_words: 38
      grid_columns: 4
      accent_usage: "title token, cursor, or key word only"
    historical_sources:
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/slides/index.html
    absorbed_from: [aiox_brandbook_slides]

  - id: aiox_agenda_table
    brand_profile: aiox_brandbook_cockpit
    category: slide_layout
    pick_when:
      - A deck roadmap or agenda needs to feel operational, not decorative.
    skip_when:
      - The agenda has fewer than three items.
    slots:
      - index
      - section_title
      - duration_or_owner
    constraints:
      row_borders_required: true
      mono_metadata_required: true
      max_rows: 8
    historical_sources:
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/slides/index.html
    absorbed_from: [aiox_brandbook_slides]

  - id: aiox_manifesto_quote
    brand_profile: aiox_brandbook_cockpit
    category: slide_layout
    pick_when:
      - A brand, movement, or point-of-view slide needs one memorable quote.
    skip_when:
      - The quote is generic or not central to the deck thesis.
    slots:
      - quote
      - highlighted_words
      - attribution
    constraints:
      quote_left_bar_required: true
      max_visible_words: 70
      highlighted_words_max: 8
    historical_sources:
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/slides/index.html
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/README.md
    absorbed_from: [aiox_brandbook_slides, aiox_brandbook_bundle]

  - id: aiox_bordered_stat_strip
    brand_profile: aiox_brandbook_cockpit
    category: slide_layout
    pick_when:
      - 3-4 numeric claims need executive impact.
    skip_when:
      - Metrics need target/actual comparison; use bullet_chart.
    slots:
      - metric_label
      - metric_value
      - metric_caption
    constraints:
      max_metrics: 4
      bordered_cells_required: true
      value_uses_display_font: true
    historical_sources:
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/slides/index.html
    absorbed_from: [aiox_brandbook_slides]

  - id: aiox_hud_pillars
    brand_profile: aiox_brandbook_cockpit
    category: slide_layout
    pick_when:
      - Three independent principles, pillars, modules, or offers need equal emphasis.
    skip_when:
      - The items are sequential; use process_flow.
    slots:
      - pillar_index
      - pillar_title
      - pillar_description
    constraints:
      max_pillars: 3
      corner_brackets_required: true
      border_grid_required: true
    historical_sources:
      - ../../../../outputs/design-system/aiox-brandbook-gaps-bundle-2026-04-18/project/slides/index.html
    absorbed_from: [aiox_brandbook_slides]

  - id: redpine_hairline_report
    brand_profile: redpine_editorial_precision
    category: slide_layout
    pick_when:
      - A report slide needs restrained editorial clarity and table-like structure.
    skip_when:
      - The slide needs high-drama manifesto energy.
    slots:
      - eyebrow
      - action_title
      - content_rows
      - source_note
    constraints:
      square_corners_required: true
      hairline_rules_required: true
      red_accent_area_percent_max: 8
      shadows_default: "none"
    historical_sources:
      - ../../../../apps/design/src/data/designs/redpine/DESIGN.md
      - ../../../../apps/redpine-ds/src/design-system/tokens.json
    absorbed_from: [redpine_design_md, redpine_ds_tokens]

  - id: redpine_component_card_grid
    brand_profile: redpine_editorial_precision
    category: slide_layout
    pick_when:
      - A component, capability, or feature set needs production-ready status and accessibility notes.
    skip_when:
      - The items are a customer journey or emotional story.
    slots:
      - component_name
      - status
      - variants
      - accessibility_note
      - token_note
    constraints:
      status_text_required: true
      color_not_only_channel: true
      decorative_top_rule_optional: true
      max_cards: 6
    historical_sources:
      - ../../../../apps/redpine-ds/src/design-system/components.manifest.json
      - ../../../../apps/redpine-ds/src/design-system/components.map.json
    absorbed_from: [redpine_components_manifest]

  - id: redpine_risk_incident_table
    brand_profile: redpine_editorial_precision
    category: slide_layout
    pick_when:
      - Safety, risk, incidents, QA, or compliance data must be scanned quickly.
    skip_when:
      - The message is a marketing offer or narrative transformation.
    slots:
      - incident_id
      - site
      - type
      - owner
      - status
      - severity
      - risk_score
    constraints:
      row_density: high
      semantic_status_text_required: true
      red_reserved_for_critical_or_action: true
      max_rows: 10
    historical_sources:
      - ../../../../apps/redpine-ds/src/components/system/data.ts
      - ../../../../apps/redpine-ds/src/design-system/components.manifest.json
    absorbed_from: [redpine_system_data, redpine_components_manifest]
```


## Referência: references/source/templates/visual/brand-template-manifest.yaml

```yaml
version: 1
name: brand-template-manifest
purpose: >
  Extract reusable visual language from a brand deck, imported PPTX, screenshot,
  design system, or bundled theme before claiming brand fidelity.

brand_template_manifest:
  deck_id: ""
  generated_at: ""
  source_reference:
    type: "imported_pptx | brand_deck | screenshot | design_system | bundled_theme"
    path_or_url: ""
    license_or_usage_note: ""
    confidence: "high | medium | low"
  visual_dna:
    summary: ""
    non_color_traits:
      - ""
    must_preserve:
      - ""
    must_avoid:
      - ""
  token_map:
    colors:
      background: ""
      surface: ""
      surface_alt: ""
      text: ""
      muted_text: ""
      accent: ""
      border: ""
      positive: ""
      negative: ""
      warning: ""
    typography:
      heading_family: ""
      body_family: ""
      mono_family: ""
      title_px: 0
      body_px: 0
      min_px: 0
      weights: []
    spacing:
      canvas: "16:9"
      grid_columns: 12
      margin_px: 0
      gutter_px: 0
      section_gap_px: 0
    shape_language:
      corner_radius_px: 0
      stroke_px: 0
      shadow_policy: "none | subtle | strong"
      surface_policy: ""
    chart_palette:
      primary: []
      neutral: ""
      grid: ""
      highlight: ""
  layout_families:
    - id: ""
      role: ""
      use_when:
        - ""
      avoid_when:
        - ""
      density: "low | medium | high"
      slots:
        - id: ""
          role: ""
          bounds_hint: ""
  component_patterns:
    - id: ""
      role: ""
      visual_rules:
        - ""
      reuse_for_slide_functions:
        - ""
  chart_language:
    chart_types_allowed: []
    label_policy: ""
    axis_policy: ""
    annotation_policy: ""
  media_language:
    image_treatment: ""
    crop_policy: ""
    icon_policy: ""
    product_or_evidence_media_policy: ""
  anti_patterns:
    - id: "identity_as_skin"
      description: "Using only logo/colors while ignoring layout, type, density, and component behavior."
    - id: "generic_stock_visual"
      description: "Using atmospheric images that do not prove, demonstrate, or clarify the slide claim."
  evidence:
    inspected_assets:
      - path: ""
        observed_rule: ""
    unresolved_questions:
      - ""

validation:
  block_if:
    - source_reference_missing
    - token_map_missing
    - typography_or_grid_missing
    - no_non_color_traits
    - no_component_patterns
    - no_anti_patterns
  warn_if:
    - confidence_low
    - chart_language_empty
    - media_language_empty
```


## Referência: references/source/templates/visual/chart-data-contracts.yaml

```yaml
version: 1
source_principle: >
  Chart selection is not enough. The chart data shape must be explicit so a
  renderer, editor, or QA script can validate it before a slide is called ready.
absorbed_from:
  - ../../../../../../bench/presentation-ai/src/components/notebook/presentation/charts/chart-data-editor/types.ts
  - ../../../../../../bench/presentation-ai/src/components/notebook/presentation/charts/chart-data-editor/use-chart-editor.ts

chart_data_modes:
  - id: label-value
    editor_mode: xy
    row_shape:
      required: [label, value]
      numeric: [value]
    best_for: [pie, donut, bar, rank, kpi_distribution]
  - id: xy
    editor_mode: xy
    row_shape:
      required: [x, y]
      numeric: [y]
    best_for: [line, scatter, trend]
  - id: xyz
    editor_mode: xy
    row_shape:
      required: [x, y, z]
      numeric: [y, z]
    best_for: [bubble, 3d_scatter]
  - id: multi-series
    editor_mode: multi-series
    row_shape:
      required: [label]
      dynamic_numeric_series: true
    best_for: [grouped_bar, stacked_bar, multi_line, area]
    default_series_chart_types: [bar, line, area]
  - id: range
    editor_mode: xy
    row_shape:
      required: [category, low, high]
      numeric: [low, high]
      constraints:
        - high_greater_or_equal_low
    best_for: [range_bar, confidence_interval, variance_band]
  - id: waterfall
    editor_mode: xy
    row_shape:
      required: [category, amount]
      numeric: [amount]
    best_for: [revenue_bridge, margin_bridge, before_after_delta]
  - id: ohlc
    editor_mode: multi-series
    row_shape:
      required: [date, open, high, low, close]
      numeric: [open, high, low, close]
      constraints:
        - high_must_cover_open_low_close
        - low_must_cover_open_high_close
    best_for: [financial_market, stock_price, volatility]
  - id: box-plot
    editor_mode: multi-series
    row_shape:
      required: [category, min, q1, median, q3, max]
      numeric: [min, q1, median, q3, max]
      constraints:
        - ordered_min_q1_median_q3_max
    best_for: [distribution, benchmark_spread, cohort_variance]
  - id: hierarchical
    editor_mode: multi-series
    row_shape:
      required: [name]
      optional: [value, children]
      recursive_children: true
    best_for: [treemap, sunburst, org_tree]
  - id: flow
    editor_mode: multi-series
    row_shape:
      required: [from, to, size]
      numeric: [size]
    best_for: [sankey, dependency_flow, source_to_destination]
  - id: funnel
    editor_mode: xy
    row_shape:
      required: [label, value]
      numeric: [value]
    best_for: [conversion_funnel, qualification_pipeline]
  - id: heatmap
    editor_mode: multi-series
    row_shape:
      required: [x, y, value]
      numeric: [value]
    best_for: [coverage_matrix, calendar_heatmap, risk_heatmap]
  - id: histogram
    editor_mode: xy
    row_shape:
      required: [value]
      numeric: [value]
    best_for: [frequency_distribution]
  - id: gauge
    editor_mode: xy
    row_shape:
      required: [value]
      numeric: [value]
    best_for: [single_metric_progress, readiness_score]

chart_dataset_contract:
  chart_dataset:
    id: ""
    mode: "label-value"
    title: ""
    source: ""
    unit: ""
    rows: []
    notes:
      assumptions: []
      caveats: []

selection_rules:
  - Validate data mode before selecting visual style.
  - A chart with invented or unsourced numbers must be labeled as illustrative or blocked.
  - Multi-series charts require series names that survive export to PPTX and speaker notes.
  - Use heatmap for large matrix coverage, but move cell rationale to a side panel or evidence ledger.
  - Use gauge only for a single metric with known denominator and threshold.
  - Use waterfall only when the sequence has a real start, signed changes, and end.

qa_blockers:
  - missing_required_fields
  - non_numeric_numeric_fields
  - invalid_range_order
  - invalid_box_plot_order
  - invalid_ohlc_bounds
  - unlabeled_unit
  - no_source_for_factual_chart
```


## Referência: references/source/templates/visual/charts-and-diagrams.yaml

```yaml
version: 1
source_principle: "Selection rules follow ppt-master grammar: Pick for content shape. Skip if another visual fits better."
visual_templates:
  - id: kpi_cards
    category: chart
    pick_when: ["4-8 standalone numeric metrics need an executive overview."]
    skip_when: ["Metrics have explicit targets; use bullet_chart.", "Only one hero metric exists; use gauge_chart."]
    data_shape: {metrics: "4-8", series: 1, target_required: false}
    constraints: {max_cards: 8, require_unit: true, require_delta_label: true}
    compatible_slide_functions: [executive_summary, proof, answer_first]
    absorbed_from: [ppt-master]
  - id: horizontal_bar_chart
    category: chart
    pick_when: ["Rank 5-12 items, especially with long labels."]
    skip_when: ["Few short labels; use bar_chart.", "Target versus actual; use bullet_chart."]
    data_shape: {items: "5-12", label_length: "medium-long"}
    constraints: {sort: descending, max_items: 12}
    compatible_slide_functions: [comparison, proof, prioritization]
    absorbed_from: [ppt-master]
  - id: line_chart
    category: chart
    pick_when: ["1-3 time series show direction over time."]
    skip_when: ["Different units; use dual_axis_line_chart.", "Composition matters; use stacked_area_chart."]
    data_shape: {series: "1-3", x_axis: time}
    constraints: {max_series: 3, annotate_inflections: true}
    compatible_slide_functions: [proof, trend, financial_update]
    absorbed_from: [ppt-master]
  - id: waterfall_chart
    category: chart
    pick_when: ["Explain additive/subtractive movement from starting value to ending value."]
    skip_when: ["No running total exists; use bar_chart."]
    data_shape: {start: 1, changes: "3-8", end: 1}
    constraints: {require_start_end: true, show_running_total: true}
    compatible_slide_functions: [explanation, financial_variance, proof]
    absorbed_from: [ppt-master]
  - id: bullet_chart
    category: chart
    pick_when: ["3-7 KPIs each have target and actual."]
    skip_when: ["No target baseline; use progress_bar_chart."]
    data_shape: {items: "3-7", target: true, actual: true}
    constraints: {max_items: 7, target_marker_required: true}
    compatible_slide_functions: [board_update, executive_summary, proof]
    absorbed_from: [ppt-master]
  - id: matrix_2x2
    category: strategic_framework
    pick_when: ["Prioritize items across two axes such as impact and effort."]
    skip_when: ["Quadrants hold text blocks; use quadrant_text_bullets.", "Bubble size matters; use quadrant_bubble_scatter."]
    data_shape: {axes: 2, items: "4-20"}
    constraints: {axis_labels_required: true, max_items: 20}
    compatible_slide_functions: [decision, prioritization, risk]
    absorbed_from: [ppt-master]
  - id: quadrant_text_bullets
    category: strategic_framework
    pick_when: ["A named 2x2 framework needs titled bullet content in each quadrant."]
    skip_when: ["Items are plotted as points; use matrix_2x2."]
    data_shape: {quadrants: 4, bullets_per_quadrant: "2-5"}
    constraints: {max_bullets_per_quadrant: 5}
    compatible_slide_functions: [segmentation, comparison, nuance]
    absorbed_from: [ppt-master]
  - id: harvey_balls_table
    category: matrix
    pick_when: ["Qualitative score grid uses 0-100% coverage or maturity."]
    skip_when: ["Binary checkmarks; use feature_matrix_table.", "Raw numbers; use basic_table."]
    data_shape: {rows: "4-40", columns: "3-12", score_type: qualitative}
    constraints: {avoid_repeated_cell_copy: true, side_panel_for_detail: true}
    compatible_slide_functions: [comparison, benchmark_matrix, capability_map]
    absorbed_from: [ppt-master, presentation-ai]
  - id: feature_matrix_table
    category: matrix
    pick_when: ["Products or plans are compared by feature availability."]
    skip_when: ["Qualitative scores; use harvey_balls_table."]
    data_shape: {rows: "5-30", columns: "2-8", value_type: boolean}
    constraints: {group_rows: true, sticky_header_recommended: true}
    compatible_slide_functions: [comparison, product_analysis]
    absorbed_from: [ppt-master]
  - id: process_flow
    category: diagram
    pick_when: ["3-8 sequential steps connected by simple arrows."]
    skip_when: ["Cycle repeats; use circular_stages.", "Stages produce named outputs; use pipeline_with_stages."]
    data_shape: {steps: "3-8", branching: false}
    constraints: {max_steps: 8, arrow_labels_optional: true}
    compatible_slide_functions: [method, plan, explanation]
    absorbed_from: [ppt-master, presentation-ai]
  - id: pipeline_with_stages
    category: diagram
    pick_when: ["Each stage has an output artifact."]
    skip_when: ["No output artifact per stage; use process_flow."]
    data_shape: {stages: "3-5", output_required: true}
    constraints: {max_stages: 5, output_label_required: true}
    compatible_slide_functions: [implementation, mechanism, runtime]
    absorbed_from: [ppt-master]
  - id: layered_architecture
    category: diagram
    pick_when: ["3-4 horizontal system layers contain modules with short descriptions."]
    skip_when: ["No per-module description; use icon_grid.", "Not a layered system; use module_composition."]
    data_shape: {layers: "3-4", modules_per_layer: "2-4"}
    constraints: {description_required: true, max_layers: 4}
    compatible_slide_functions: [mechanism, architecture, product_strategy]
    absorbed_from: [ppt-master, Presenton]
  - id: module_composition
    category: diagram
    pick_when: ["One parent system contains multiple child modules with descriptions."]
    skip_when: ["Only labels exist; use icon_grid or numbered_steps."]
    data_shape: {parent: 1, modules: "3-9"}
    constraints: {module_description_required: true}
    compatible_slide_functions: [mechanism, product_overview, offer]
    absorbed_from: [ppt-master, Presenton]
  - id: hub_spoke
    category: diagram
    pick_when: ["One core capability radiates into 4-8 surrounding capabilities."]
    skip_when: ["Forces point inward; use hub_inward_arrows."]
    data_shape: {center: 1, spokes: "4-8"}
    constraints: {center_label_required: true, max_spokes: 8}
    compatible_slide_functions: [mechanism, ecosystem, positioning]
    absorbed_from: [ppt-master]
  - id: journey_map
    category: experience
    pick_when: ["Customer experience needs phases, actions, emotion, and pain points."]
    skip_when: ["Simple conversion funnel; use funnel_chart."]
    data_shape: {phases: "4-7", lanes: "3-5"}
    constraints: {emotion_lane_required: true, pain_lane_required: true}
    compatible_slide_functions: [diagnosis, customer_gap, product_strategy]
    absorbed_from: [ppt-master]
  - id: before_after
    category: proof
    pick_when: ["A concrete state change is the message."]
    skip_when: ["Many items change over time; use dumbbell_chart or line_chart."]
    data_shape: {states: 2}
    constraints: {same_metric_or_view_required: true}
    compatible_slide_functions: [proof, demo, transformation]
    absorbed_from: [banana-slides, slide-deck-ai]
  - id: offer_stack
    category: conversion
    pick_when: ["Offer components, bonuses, value, and next step need one legible slide."]
    skip_when: ["No commercial CTA exists."]
    data_shape: {components: "3-8", cta: true}
    constraints: {cta_required: true, outcome_label_required: true}
    compatible_slide_functions: [conversion, cta, sales]
    absorbed_from: [presentation-ai, banana-slides]
  - id: decision_card
    category: decision
    pick_when: ["A recommendation must be clear and defended by tradeoffs."]
    skip_when: ["Audience only needs a neutral comparison."]
    data_shape: {recommendation: 1, alternatives: "1-3"}
    constraints: {recommendation_required: true, tradeoff_required: true}
    compatible_slide_functions: [decision, executive_summary]
    absorbed_from: [powerpoint-skill, ppt-master]

  - id: comparison_columns
    category: comparison
    pick_when: ["Two or three alternatives need direct narrative contrast."]
    skip_when: ["More than three alternatives or many criteria; use feature_matrix_table."]
    data_shape: {columns: "2-3", rows: "3-6"}
    constraints: {max_columns: 3, require_point_of_view: true}
    compatible_slide_functions: [reframe, decision, commercial]
    absorbed_from: [ppt-master, presentation-ai]
  - id: pros_cons_chart
    category: comparison
    pick_when: ["One option needs balanced benefits and risks before a recommendation."]
    skip_when: ["There is no recommendation; use comparison_columns."]
    data_shape: {pros: "2-5", cons: "2-5"}
    constraints: {recommendation_required: true, max_items_per_side: 5}
    compatible_slide_functions: [decision, objection_handling, tradeoff]
    absorbed_from: [ppt-master]
  - id: basic_table
    category: table
    pick_when: ["Precise values, source rows, assumptions, or appendix data need compact tabular form."]
    skip_when: ["The table is primarily a feature comparison; use feature_matrix_table."]
    data_shape: {rows: "3-30", columns: "2-6"}
    constraints: {right_align_numbers: true, max_columns: 6, totals_distinct: true}
    compatible_slide_functions: [appendix, evidence, financial_update]
    absorbed_from: [powerpoint-skill, PPTAgent]
  - id: vertical_list
    category: synthesis
    pick_when: ["A ranked or grouped list is the clearest synthesis."]
    skip_when: ["Items have numeric values; use horizontal_bar_chart."]
    data_shape: {items: "3-9", groups: "0-3"}
    constraints: {max_items: 9, group_labels_optional: true}
    compatible_slide_functions: [synthesis, findings, executive_summary]
    absorbed_from: [slide-deck-ai, presentation-ai]
  - id: numbered_steps
    category: process
    pick_when: ["A method, plan, or workflow has an ordered sequence."]
    skip_when: ["Steps run in parallel lanes; use swimlane_process."]
    data_shape: {steps: "3-8", strict_order: true}
    constraints: {max_steps: 8, verb_first_labels: true}
    compatible_slide_functions: [teaching, plan, implementation]
    absorbed_from: [ppt-master, slide-deck-ai]
  - id: timeline
    category: process
    pick_when: ["Milestones or changes occur across dates or periods."]
    skip_when: ["Durations and dependencies matter; use gantt_chart."]
    data_shape: {milestones: "3-8", time_axis: true}
    constraints: {date_labels_required: true, max_milestones: 8}
    compatible_slide_functions: [update, proof, roadmap]
    absorbed_from: [ppt-master]
  - id: checklist
    category: qa
    pick_when: ["Completion, readiness, or compliance needs pass/fail visibility."]
    skip_when: ["Items need scores or maturity; use harvey_balls_table."]
    data_shape: {items: "4-12", status: boolean}
    constraints: {max_items: 12, status_required: true}
    compatible_slide_functions: [qa, readiness, implementation]
    absorbed_from: [powerpoint-skill]
  - id: stacked_bar_chart
    category: chart
    pick_when: ["Composition across categories must be compared."]
    skip_when: ["Only total ranking matters; use horizontal_bar_chart."]
    data_shape: {categories: "3-8", segments: "2-5"}
    constraints: {max_segments: 5, show_totals: true}
    compatible_slide_functions: [comparison, financial_update, segmentation]
    absorbed_from: [ppt-master]
  - id: gantt_chart
    category: chart
    pick_when: ["Workstreams have durations, dependencies, and dates."]
    skip_when: ["Only phase order matters; use roadmap_vertical or timeline."]
    data_shape: {tasks: "4-16", time_axis: true, duration: true}
    constraints: {max_tasks: 16, dependency_labels_optional: true}
    compatible_slide_functions: [plan, implementation, roadmap]
    absorbed_from: [ppt-master]
  - id: gauge_chart
    category: chart
    pick_when: ["One headline metric needs status versus a clear target."]
    skip_when: ["Multiple KPIs need comparison; use bullet_chart or kpi_cards."]
    data_shape: {metric: 1, target: true}
    constraints: {single_metric_only: true, target_required: true}
    compatible_slide_functions: [executive_summary, proof, status]
    absorbed_from: [ppt-master]
  - id: progress_bar_chart
    category: chart
    pick_when: ["Progress toward completion is the point."]
    skip_when: ["Progress has multiple thresholds; use bullet_chart."]
    data_shape: {items: "1-8", percent: true}
    constraints: {max_items: 8, percent_label_required: true}
    compatible_slide_functions: [status, implementation, qa]
    absorbed_from: [ppt-master]
  - id: dumbbell_chart
    category: chart
    pick_when: ["Before/after or two-period comparison across multiple items."]
    skip_when: ["Only one before/after pair exists; use before_after."]
    data_shape: {items: "3-10", points_per_item: 2}
    constraints: {max_items: 10, delta_label_required: true}
    compatible_slide_functions: [proof, comparison, transformation]
    absorbed_from: [ppt-master]
  - id: funnel_chart
    category: chart
    pick_when: ["Conversion stages shrink from a starting audience to an outcome."]
    skip_when: ["The experience has emotional and behavioral lanes; use journey_map."]
    data_shape: {stages: "3-7", values: true}
    constraints: {max_stages: 7, show_conversion_rate: true}
    compatible_slide_functions: [diagnosis, growth, conversion]
    absorbed_from: [ppt-master, presentation-ai]
  - id: executive_snapshot
    category: executive
    pick_when: ["A single slide must combine answer, KPIs, status, and next decision."]
    skip_when: ["The deck needs a pure metric page; use kpi_cards."]
    data_shape: {headline: 1, metrics: "3-6", decision: "0-1"}
    constraints: {answer_first_required: true, max_metrics: 6}
    compatible_slide_functions: [answer_first, executive_summary, board_update]
    absorbed_from: [ppt-master, powerpoint-skill]
  - id: evidence_cards
    category: proof
    pick_when: ["3-6 proof points with source labels need equal visual weight."]
    skip_when: ["Proof is numeric trend; use line_chart."]
    data_shape: {cards: "3-6", source_label: true}
    constraints: {max_cards: 6, source_required: true}
    compatible_slide_functions: [credibility, proof, research_synthesis]
    absorbed_from: [PPTAgent, slide-deck-ai]
  - id: source_panel
    category: evidence
    pick_when: ["The slide needs transparent source, assumption, or confidence metadata."]
    skip_when: ["Sources are the main content; use basic_table."]
    data_shape: {claim: 1, sources: "1-6", confidence: "low-medium-high"}
    constraints: {claim_source_mapping_required: true}
    compatible_slide_functions: [appendix, credibility, benchmark_matrix]
    absorbed_from: [PPTAgent, powerpoint-skill]
  - id: risk_heatmap
    category: risk
    pick_when: ["Risks need likelihood versus impact and mitigation priority."]
    skip_when: ["Risks are binary blockers; use checklist."]
    data_shape: {items: "4-20", axes: [likelihood, impact]}
    constraints: {axis_labels_required: true, mitigation_required: true}
    compatible_slide_functions: [risk, decision, board_update]
    absorbed_from: [ppt-master, powerpoint-skill]
  - id: swimlane_process
    category: process
    pick_when: ["Multiple roles, systems, or teams act across the same workflow."]
    skip_when: ["One linear owner exists; use process_flow."]
    data_shape: {lanes: "2-6", steps: "4-12"}
    constraints: {lane_labels_required: true, max_lanes: 6}
    compatible_slide_functions: [operating_model, implementation, architecture]
    absorbed_from: [ppt-master]
  - id: system_flow
    category: architecture
    pick_when: ["Components exchange data, events, or control across boundaries."]
    skip_when: ["The system is best described by layers; use layered_architecture."]
    data_shape: {components: "3-10", flows: "3-12"}
    constraints: {arrow_labels_required: true, boundary_required: true}
    compatible_slide_functions: [architecture, mechanism, technical_review]
    absorbed_from: [ppt-master, PPTAgent]
  - id: client_server_flow
    category: architecture
    pick_when: ["A product flow crosses client, API, worker, database, or external provider layers."]
    skip_when: ["No technical boundary matters; use process_flow."]
    data_shape: {layers: "3-6", messages: "3-10"}
    constraints: {boundary_labels_required: true, secret_paths_hidden: true}
    compatible_slide_functions: [architecture, demo_setup, implementation]
    absorbed_from: [PPTAgent, powerpoint-skill]
  - id: pricing_table
    category: commercial
    pick_when: ["Offer tiers, plan fit, inclusions, and tradeoffs need comparison."]
    skip_when: ["There is one offer only; use offer_stack."]
    data_shape: {tiers: "2-4", rows: "4-12"}
    constraints: {recommended_tier_required: true, max_tiers: 4}
    compatible_slide_functions: [commercial, decision, sales]
    absorbed_from: [presentation-ai, ppt-master]
  - id: market_map
    category: positioning
    pick_when: ["Players or segments need spatial positioning across two strategic axes."]
    skip_when: ["Scores across many dimensions matter; use harvey_balls_table."]
    data_shape: {axes: 2, entities: "4-20"}
    constraints: {axis_labels_required: true, positioning_rationale_required: true}
    compatible_slide_functions: [positioning, comparison, strategy]
    absorbed_from: [ppt-master, Presenton]
  - id: stakeholder_map
    category: strategy
    pick_when: ["Stakeholders differ by influence, need, resistance, or buying role."]
    skip_when: ["The content is a customer journey; use journey_map."]
    data_shape: {stakeholders: "4-12", attributes: "2-4"}
    constraints: {role_labels_required: true, action_required: true}
    compatible_slide_functions: [customer_gap, GTM, operating_model]
    absorbed_from: [ppt-master]
  - id: dashboard_grid
    category: dashboard
    pick_when: ["Multiple metric families need a compact command-center view."]
    skip_when: ["Only 4-8 standalone metrics exist; use kpi_cards."]
    data_shape: {panels: "4-9", metric_groups: "2-4"}
    constraints: {max_panels: 9, consistent_units_required: true}
    compatible_slide_functions: [executive_summary, board_update, operating_review]
    absorbed_from: [presentation-ai, ppt-master]
  - id: screen_sequence
    category: demo
    pick_when: ["A product or workflow demo needs 3-5 screenshots or states in order."]
    skip_when: ["There is one before/after state; use before_after."]
    data_shape: {screens: "3-5", annotations: true}
    constraints: {max_screens: 5, annotation_required: true}
    compatible_slide_functions: [demo_setup, proof, product_walkthrough]
    absorbed_from: [Presenton, PPTAgent]
  - id: myth_truth
    category: persuasion
    pick_when: ["A false belief must be neutralized with a sharper replacement belief."]
    skip_when: ["Both sides are valid tradeoffs; use pros_cons_chart."]
    data_shape: {myths: "1-4", truths: "1-4"}
    constraints: {truth_must_answer_myth: true, max_pairs: 4}
    compatible_slide_functions: [objection_handling, reframe, teaching]
    absorbed_from: [banana-slides, presentation-ai]
  - id: case_study_panel
    category: proof
    pick_when: ["A case needs baseline, intervention, result, and repeatable lesson in one view."]
    skip_when: ["The case is only a testimonial quote."]
    data_shape: {baseline: 1, intervention: 1, result: 1, lesson: "0-1"}
    constraints: {metric_or_artifact_required: true}
    compatible_slide_functions: [proof, case_study, sales]
    absorbed_from: [slide-deck-ai, ppt-master]
  - id: responsibility_matrix
    category: operating_model
    pick_when: ["Roles need accountability across decisions, inputs, and outputs."]
    skip_when: ["The work is sequential across lanes; use swimlane_process."]
    data_shape: {roles: "3-8", responsibilities: "4-12"}
    constraints: {owner_required_for_each_row: true, max_roles: 8}
    compatible_slide_functions: [operating_model, implementation, governance]
    absorbed_from: [ppt-master, powerpoint-skill]
  - id: cohort_retention
    category: chart
    pick_when: ["Retention, repeat usage, or customer health needs cohort-by-period visibility."]
    skip_when: ["Only one aggregate retention metric exists; use gauge_chart."]
    data_shape: {cohorts: "3-12", periods: "3-12", value_type: percent}
    constraints: {period_labels_required: true, cohort_definition_required: true}
    compatible_slide_functions: [diagnosis, operating_review, customer_health]
    absorbed_from: [ppt-master]
  - id: unit_economics_panel
    category: finance
    pick_when: ["CAC, LTV, margin, payback, ARPA, or contribution economics need one decision view."]
    skip_when: ["Variance drivers are additive; use waterfall_chart."]
    data_shape: {metrics: "4-8", drivers: "2-5"}
    constraints: {period_required: true, formula_labels_required: true}
    compatible_slide_functions: [financial_update, investor_pitch, commercial]
    absorbed_from: [ppt-master, powerpoint-skill]
  - id: competitive_landscape_table
    category: positioning
    pick_when: ["Players need comparison by category, wedge, audience, moat, or pricing."]
    skip_when: ["A scored absorption matrix is required; use harvey_balls_table."]
    data_shape: {players: "3-12", criteria: "3-7"}
    constraints: {category_grouping_required: true, point_of_view_required: true}
    compatible_slide_functions: [positioning, fundraising, benchmark_matrix]
    absorbed_from: [presentation-ai, ppt-master]
  - id: maturity_ladder
    category: capability
    pick_when: ["A capability progresses through named maturity stages."]
    skip_when: ["Items are independent priorities; use matrix_2x2."]
    data_shape: {stages: "3-6", capabilities: "1-8"}
    constraints: {stage_definitions_required: true, current_target_markers_required: true}
    compatible_slide_functions: [capability_map, roadmap, design_audit]
    absorbed_from: [ppt-master]
  - id: org_chart
    category: operating_model
    pick_when: ["Reporting, ownership, or governance hierarchy must be visible."]
    skip_when: ["Responsibilities are matrixed; use responsibility_matrix."]
    data_shape: {levels: "2-5", roles: "3-20"}
    constraints: {role_labels_required: true, avoid_personal_data: true}
    compatible_slide_functions: [governance, onboarding, operating_model]
    absorbed_from: [ppt-master]
  - id: value_chain
    category: strategy
    pick_when: ["End-to-end business value creation or service delivery needs stage-by-stage mapping."]
    skip_when: ["The flow is technical data movement; use data_lineage or system_flow."]
    data_shape: {stages: "4-9", value_outputs: true}
    constraints: {output_per_stage_required: true, max_stages: 9}
    compatible_slide_functions: [strategy, diagnosis, operating_model]
    absorbed_from: [ppt-master, Presenton]
  - id: dependency_map
    category: planning
    pick_when: ["Roadmap, migration, or delivery work depends on blockers and prerequisite tasks."]
    skip_when: ["Only durations matter; use gantt_chart."]
    data_shape: {nodes: "4-16", dependencies: "3-20"}
    constraints: {critical_path_required: true, owner_optional: true}
    compatible_slide_functions: [implementation, prioritization, roadmap]
    absorbed_from: [ppt-master, powerpoint-skill]
  - id: decision_tree
    category: decision
    pick_when: ["The recommendation depends on conditional criteria or branching paths."]
    skip_when: ["Options are independent; use decision_card or comparison_columns."]
    data_shape: {branches: "2-5", levels: "2-4"}
    constraints: {criterion_labels_required: true, terminal_actions_required: true}
    compatible_slide_functions: [decision, facilitation, triage]
    absorbed_from: [ppt-master]
  - id: data_lineage
    category: architecture
    pick_when: ["Data origin, transformation, storage, and consumption need traceability."]
    skip_when: ["The flow is user-facing product flow; use client_server_flow."]
    data_shape: {sources: "1-6", transforms: "1-8", outputs: "1-6"}
    constraints: {source_labels_required: true, PII_or_secret_boundary_required: false}
    compatible_slide_functions: [architecture, evidence, governance]
    absorbed_from: [PPTAgent, powerpoint-skill]
  - id: experiment_card_grid
    category: proof
    pick_when: ["Multiple experiments or pilots need hypothesis, result, and decision status."]
    skip_when: ["Only one experiment exists; use before_after or evidence_cards."]
    data_shape: {experiments: "2-6", fields: [hypothesis, result, decision]}
    constraints: {success_metric_required: true, max_cards: 6}
    compatible_slide_functions: [proof, product_strategy, growth]
    absorbed_from: [PPTAgent, ppt-master]
  - id: agenda_timeline
    category: facilitation
    pick_when: ["A live session or next-step plan needs timeboxes and outcome checkpoints."]
    skip_when: ["Dates matter across weeks/months; use timeline or gantt_chart."]
    data_shape: {blocks: "3-8", timebox: true}
    constraints: {outcome_per_block_required: true, max_blocks: 8}
    compatible_slide_functions: [facilitation, action, training]
    absorbed_from: [presentation-ai, banana-slides]
  - id: quote_evidence_panel
    category: evidence
    pick_when: ["A sourced quote, customer voice, or expert excerpt supports the argument."]
    skip_when: ["The quote is decorative or unsourced; use evidence_cards only with sources."]
    data_shape: {quote: 1, attribution: true, implication: true}
    constraints: {attribution_required: true, max_quote_words: 32}
    compatible_slide_functions: [proof, credibility, voice_of_customer]
    absorbed_from: [PPTAgent, slide-deck-ai]
  - id: workshop_canvas
    category: facilitation
    pick_when: ["Participants must fill sections and produce a visible artifact."]
    skip_when: ["The slide only explains a method; use numbered_steps."]
    data_shape: {sections: "3-8", output_required: true}
    constraints: {timebox_required: true, output_label_required: true}
    compatible_slide_functions: [practice, facilitation, workshop]
    absorbed_from: [presentation-ai]
  - id: launch_calendar
    category: planning
    pick_when: ["Launch work needs dates, channels, assets, owners, and readiness gates."]
    skip_when: ["Dependencies are more important than dates; use dependency_map."]
    data_shape: {milestones: "4-14", channels: "1-6", owners: true}
    constraints: {date_required: true, owner_required: true, readiness_gate_required: true}
    compatible_slide_functions: [plan, GTM, launch]
    absorbed_from: [Presenton, presentation-ai]
  - id: affinity_map
    category: facilitation
    pick_when: ["Workshop inputs need clustering into themes before decisions."]
    skip_when: ["Items are already scored; use matrix_2x2."]
    data_shape: {clusters: "3-8", notes: "8-40"}
    constraints: {cluster_labels_required: true, decision_bridge_required: true}
    compatible_slide_functions: [synthesis, facilitation, research]
    absorbed_from: [presentation-ai]
  - id: incident_timeline
    category: incident
    pick_when: ["An incident needs timestamped sequence, detection, mitigation, and resolution."]
    skip_when: ["The topic is planned roadmap; use timeline."]
    data_shape: {events: "4-12", timestamps: true}
    constraints: {timestamp_required: true, impact_marker_required: true}
    compatible_slide_functions: [diagnosis, proof, postmortem]
    absorbed_from: [powerpoint-skill, ppt-master]
  - id: corrective_action_table
    category: incident
    pick_when: ["Fixes need owner, due date, status, and prevention logic."]
    skip_when: ["Actions are only checklist pass/fail; use checklist."]
    data_shape: {actions: "3-12", fields: [owner, due_date, status, prevention]}
    constraints: {owner_required: true, due_date_required: true, status_required: true}
    compatible_slide_functions: [implementation, postmortem, governance]
    absorbed_from: [powerpoint-skill]
  - id: hiring_scorecard
    category: evaluation
    pick_when: ["A role or candidate needs criteria, evidence, and decision threshold."]
    skip_when: ["The audience needs org structure; use org_chart."]
    data_shape: {criteria: "4-10", levels: "3-5"}
    constraints: {behavioral_evidence_required: true, decision_rule_required: true}
    compatible_slide_functions: [evaluation, onboarding, hiring]
    absorbed_from: [ppt-master]
  - id: ramp_plan
    category: onboarding
    pick_when: ["A new hire, customer, or team needs first 30/60/90 day outcomes."]
    skip_when: ["The plan is a project roadmap; use gantt_chart."]
    data_shape: {phases: "3-4", outcomes: true, owners: "0-4"}
    constraints: {outcome_per_phase_required: true, success_metric_required: true}
    compatible_slide_functions: [plan, onboarding, implementation]
    absorbed_from: [ppt-master, presentation-ai]
  - id: section_divider
    category: narrative
    pick_when: ["A long deck needs a chapter transition with one clear claim."]
    skip_when: ["The section does not change audience state."]
    data_shape: {chapter_label: 1, claim: 1}
    constraints: {max_words: 18, no_bullets: true}
    compatible_slide_functions: [transition, hook]
    absorbed_from: [Presenton, presentation-ai]
  - id: scoring_rubric_table
    category: method
    pick_when: ["A score needs formula, bands, evidence confidence, and interpretation."]
    skip_when: ["The audience only needs final ranking; use horizontal_bar_chart."]
    data_shape: {bands: "3-7", criteria: "2-8", confidence_levels: "2-4"}
    constraints: {formula_required: true, band_definitions_required: true}
    compatible_slide_functions: [method, benchmark_matrix, transparency]
    absorbed_from: [ppt-master, powerpoint-skill]
  - id: scoring_band_ladder
    category: method
    pick_when: ["The difference between score ranges must be memorable and visually simple."]
    skip_when: ["Many criteria need row-level details; use scoring_rubric_table."]
    data_shape: {bands: "4-6", labels: true}
    constraints: {range_labels_required: true, example_per_band_recommended: true}
    compatible_slide_functions: [method, training, benchmark]
    absorbed_from: [ppt-master]
  - id: persona_fit_matrix
    category: decision
    pick_when: ["Different personas require different weights, winners, or recommendations."]
    skip_when: ["Only one persona exists; use decision_card."]
    data_shape: {personas: "3-8", criteria: "3-8", recommendations: true}
    constraints: {weights_required: true, recommendation_per_persona_required: true}
    compatible_slide_functions: [decision, segmentation, benchmark]
    absorbed_from: [presentation-ai, ppt-master]
  - id: radar_chart
    category: chart
    pick_when: ["3-6 entities need profile comparison across 5-8 dimensions."]
    skip_when: ["Precise ranking matters; use horizontal_bar_chart or harvey_balls_table."]
    data_shape: {entities: "2-6", dimensions: "5-8"}
    constraints: {max_entities: 6, normalized_scores_required: true}
    compatible_slide_functions: [comparison, persona_fit, capability_map]
    absorbed_from: [presentation-ai, ppt-master]
  - id: traceability_matrix
    category: governance
    pick_when: ["Requirements need mapping to source, evidence, owner, status, or acceptance criteria."]
    skip_when: ["Only pass/fail status matters; use checklist."]
    data_shape: {requirements: "4-30", fields: [source, owner, evidence, status]}
    constraints: {requirement_id_required: true, evidence_or_gap_required: true}
    compatible_slide_functions: [governance, QA, implementation]
    absorbed_from: [powerpoint-skill, PPTAgent]
  - id: compliance_grid
    category: risk
    pick_when: ["Controls, policies, evidence, and open gaps need audit-ready display."]
    skip_when: ["Risks are not compliance-related; use risk_heatmap."]
    data_shape: {controls: "4-20", evidence: true, gaps: "0-10"}
    constraints: {control_owner_required: true, evidence_required: true}
    compatible_slide_functions: [risk, governance, compliance]
    absorbed_from: [powerpoint-skill]
  - id: survey_result_panel
    category: research
    pick_when: ["Survey or poll results need sample context plus top responses."]
    skip_when: ["Results are raw qualitative quotes; use quote_evidence_panel."]
    data_shape: {question: 1, sample_size: true, responses: "3-8"}
    constraints: {sample_size_required: true, date_or_context_required: true}
    compatible_slide_functions: [insight, research_synthesis, voice_of_customer]
    absorbed_from: [ppt-master, presentation-ai]
  - id: roadmap_status_board
    category: planning
    pick_when: ["Initiatives need status, owner, blocker, and next checkpoint."]
    skip_when: ["Dependencies are the primary story; use dependency_map."]
    data_shape: {initiatives: "4-12", statuses: [on_track, at_risk, blocked, done]}
    constraints: {owner_required: true, next_checkpoint_required: true}
    compatible_slide_functions: [update, roadmap, operating_review]
    absorbed_from: [banana-slides, ppt-master]
  - id: portfolio_allocation
    category: prioritization
    pick_when: ["Budget, effort, roadmap capacity, or headcount is allocated across categories."]
    skip_when: ["The goal is categorical composition only; use stacked_bar_chart."]
    data_shape: {categories: "3-8", allocation: percent, tradeoffs: true}
    constraints: {sum_to_100_required: true, tradeoff_note_required: true}
    compatible_slide_functions: [prioritization, strategy, financial_update]
    absorbed_from: [ppt-master]
  - id: treemap_chart
    category: chart
    pick_when: ["Part-to-whole allocation has many uneven categories."]
    skip_when: ["Time or sequence matters; use stacked_bar_chart or waterfall_chart."]
    data_shape: {items: "5-30", value: numeric}
    constraints: {label_threshold_required: true, avoid_tiny_unlabeled_tiles: true}
    compatible_slide_functions: [portfolio_allocation, market_map, financial_update]
    absorbed_from: [presentation-ai, ppt-master]
  - id: brand_principle_cards
    category: brand
    pick_when: ["Brand rules need principles, examples, and anti-patterns."]
    skip_when: ["Only visual mood is needed; use moodboard_grid."]
    data_shape: {principles: "3-6", examples: true, anti_patterns: true}
    constraints: {anti_pattern_required: true, example_required: true}
    compatible_slide_functions: [creative_direction, design_audit, brand_strategy]
    absorbed_from: [aiox-brandbook, redpine-ds]
  - id: moodboard_grid
    category: brand
    pick_when: ["A visual direction needs images, motifs, palette, and typography references."]
    skip_when: ["The deck needs enforceable rules; use brand_principle_cards."]
    data_shape: {tiles: "6-12", labels: true}
    constraints: {label_each_tile: true, avoid_unsourced_reference_claims: true}
    compatible_slide_functions: [creative_direction, design_direction, brand_strategy]
    absorbed_from: [aiox-brandbook, Presenton]
  - id: logo_wall
    category: proof
    pick_when: ["Adoption or credibility is best shown by recognized customer/partner logos."]
    skip_when: ["Logos are not permitted or sourced; use quote_evidence_panel."]
    data_shape: {logos: "6-24", grouping: "0-4"}
    constraints: {permission_or_source_required: true, no_fake_logos: true}
    compatible_slide_functions: [credibility, sales, fundraising]
    absorbed_from: [Presenton, presentation-ai]
  - id: testimonial_grid
    category: proof
    pick_when: ["Several short testimonials need equal treatment with attribution."]
    skip_when: ["One quote is decisive; use quote_evidence_panel."]
    data_shape: {testimonials: "2-6", attribution: true}
    constraints: {attribution_required: true, max_quote_words: 28}
    compatible_slide_functions: [credibility, sales, case_study]
    absorbed_from: [presentation-ai, slide-deck-ai]
  - id: objection_matrix
    category: persuasion
    pick_when: ["Multiple objections need response, proof, and residual risk."]
    skip_when: ["Only one objection matters; use myth_truth."]
    data_shape: {objections: "3-8", fields: [response, proof, residual_risk]}
    constraints: {proof_required: true, tone_neutral_required: true}
    compatible_slide_functions: [objection_handling, sales, decision]
    absorbed_from: [banana-slides, ppt-master]
  - id: user_story_map
    category: product
    pick_when: ["User activities, tasks, and release slices need product planning visibility."]
    skip_when: ["Only timeline is needed; use roadmap_status_board."]
    data_shape: {activities: "3-8", stories: "6-40", releases: "1-4"}
    constraints: {user_activity_required: true, release_slice_required: true}
    compatible_slide_functions: [product_strategy, roadmap, workshop]
    absorbed_from: [ppt-master, presentation-ai]
  - id: architecture_tradeoff_table
    category: architecture
    pick_when: ["Technical options need evaluation by cost, risk, latency, complexity, and operability."]
    skip_when: ["The architecture is already chosen; use system_flow."]
    data_shape: {options: "2-5", criteria: "4-8"}
    constraints: {recommendation_required: true, operational_criteria_required: true}
    compatible_slide_functions: [decision, architecture, technical_review]
    absorbed_from: [PPTAgent, powerpoint-skill]
  - id: sankey_flow
    category: chart
    pick_when: ["Volume, money, users, or attention flows between stages or categories."]
    skip_when: ["The flow is sequential without volume; use process_flow."]
    data_shape: {nodes: "4-16", flows: "3-24", values: numeric}
    constraints: {value_labels_required: true, avoid_too_many_crossings: true}
    compatible_slide_functions: [financial_update, customer_journey, strategy]
    absorbed_from: [presentation-ai, ppt-master]
  - id: scatter_plot
    category: chart
    pick_when: ["Items need comparison across two numeric variables with clusters or outliers."]
    skip_when: ["Axes are qualitative; use matrix_2x2."]
    data_shape: {points: "8-80", x_numeric: true, y_numeric: true}
    constraints: {axis_units_required: true, annotate_outliers: true}
    compatible_slide_functions: [insight, prioritization, market_map]
    absorbed_from: [ppt-master]
  - id: hero_claim
    category: narrative
    pick_when: ["A slide needs one dominant claim with optional proof chip or subtitle."]
    skip_when: ["The slide needs evidence density, table, or multi-part comparison."]
    data_shape: {claim: 1, subtitle: "0-1", proof_chip: "0-1"}
    constraints: {max_words: 28, action_title_required: true, no_bullets: true}
    compatible_slide_functions: [hook, transition, answer_first]
    absorbed_from: [Presenton, presentation-ai]
  - id: full_bleed_image
    category: media
    pick_when: ["A product, place, person, artifact, or scene must carry the slide emotionally or visually."]
    skip_when: ["The image is decorative or unrelated to inspection."]
    data_shape: {image: 1, overlay_text: "1-3"}
    constraints: {image_must_be_relevant: true, text_contrast_required: true, avoid_stock_like_blur: true}
    compatible_slide_functions: [hook, transition, proof]
    absorbed_from: [Presenton, presentation-ai]
  - id: fishbone_diagram
    category: diagnosis
    pick_when: ["A visible symptom needs root-cause categories and contributing factors."]
    skip_when: ["The explanation is sequential; use process_flow."]
    data_shape: {symptom: 1, cause_categories: "3-6", causes: "6-18"}
    constraints: {symptom_required: true, max_categories: 6, avoid_blame_language: true}
    compatible_slide_functions: [diagnosis, postmortem, risk]
    absorbed_from: [ppt-master, powerpoint-skill]
  - id: heatmap_chart
    category: matrix
    pick_when: ["A grid of normalized values needs intensity, outliers, or pattern detection."]
    skip_when: ["The grid is qualitative maturity; use harvey_balls_table."]
    data_shape: {rows: "3-30", columns: "3-20", value_type: numeric}
    constraints: {legend_required: true, normalized_scale_required: true}
    compatible_slide_functions: [comparison, diagnosis, retention]
    absorbed_from: [presentation-ai, ppt-master]
  - id: roadmap_vertical
    category: planning
    pick_when: ["Phases, milestones, or releases need vertical sequence and outcome per phase."]
    skip_when: ["Dates and dependencies matter; use gantt_chart or dependency_map."]
    data_shape: {phases: "3-8", outcome_per_phase: true}
    constraints: {phase_order_required: true, max_phases: 8}
    compatible_slide_functions: [plan, prioritization, roadmap]
    absorbed_from: [ppt-master, banana-slides]
  - id: circular_stages
    category: process
    pick_when: ["A repeatable cycle or feedback loop is the point."]
    skip_when: ["The method has a clear start and end; use numbered_steps."]
    data_shape: {stages: "3-7", loop: true}
    constraints: {max_stages: 7, loop_label_required: true}
    compatible_slide_functions: [teaching, mechanism, operating_model]
    absorbed_from: [ppt-master, presentation-ai]
  - id: chevron_process
    category: process
    pick_when: ["A linear transformation needs compact labeled phases with forward momentum."]
    skip_when: ["Each stage has rich outputs; use pipeline_with_stages."]
    data_shape: {steps: "3-7", forward_sequence: true}
    constraints: {verb_first_labels: true, max_steps: 7}
    compatible_slide_functions: [teaching, plan, implementation]
    absorbed_from: [ppt-master]
  - id: contrast
    category: comparison
    pick_when: ["Old versus new, before versus after, or wrong versus right framing must be immediately legible."]
    skip_when: ["The comparison has many criteria; use comparison_table or feature_matrix_table."]
    data_shape: {left: 1, right: 1, bridge: "0-1"}
    constraints: {two_sides_only: true, point_of_view_required: true}
    compatible_slide_functions: [reframe, diagnosis, persuasion]
    absorbed_from: [presentation-ai, ppt-master]
  - id: comparison_table
    category: comparison
    pick_when: ["Alternatives need rows of comparable criteria and a visible recommendation."]
    skip_when: ["Values are binary features; use feature_matrix_table."]
    data_shape: {alternatives: "2-5", criteria: "3-10"}
    constraints: {recommendation_required: true, criteria_labels_required: true}
    compatible_slide_functions: [decision, objection_handling, commercial]
    absorbed_from: [ppt-master, powerpoint-skill]
  - id: decision
    category: decision
    pick_when: ["The audience needs a final recommended action, owner, or ask."]
    skip_when: ["The slide must remain neutral; use comparison_columns."]
    data_shape: {recommendation: 1, rationale: "1-3", next_step: "0-1"}
    constraints: {recommendation_required: true, rationale_required: true}
    compatible_slide_functions: [decision, action, executive_summary]
    absorbed_from: [powerpoint-skill, banana-slides]
  - id: api_request_response
    category: technical
    pick_when: ["API, webhook, MCP tool, or integration behavior needs request and response side by side."]
    skip_when: ["The audience only needs system flow; use client_server_flow."]
    data_shape: {request: 1, response: 1, behavior_note: true}
    constraints: {schema_or_example_required: true, sensitive_values_redacted: true}
    compatible_slide_functions: [technical_demo, architecture, demo_setup]
    absorbed_from: [Presenton, PPTAgent]
  - id: code_explanation_split
    category: technical
    pick_when: ["A code/config/CLI excerpt needs readable annotations."]
    skip_when: ["The code is too long for one slide; use appendix_source_table."]
    data_shape: {code_block: 1, annotations: "3-7"}
    constraints: {monospace_required: true, max_code_lines: 18, annotation_required: true}
    compatible_slide_functions: [technical_teaching, architecture, training]
    absorbed_from: [Presenton, powerpoint-skill]
  - id: mission_vision_panel
    category: alignment
    pick_when: ["Mission, vision, and principles need strategic alignment in one slide."]
    skip_when: ["Only brand style is being explained; use brand_principle_cards."]
    data_shape: {mission: 1, vision: 1, principles: "0-5"}
    constraints: {decision_implication_required: true}
    compatible_slide_functions: [alignment, brand_strategy, product_strategy]
    absorbed_from: [Presenton, aiox-brandbook]
  - id: business_challenges_grid
    category: diagnosis
    pick_when: ["3-6 business constraints need impact and solution bridge."]
    skip_when: ["The cause tree matters; use fishbone_diagram."]
    data_shape: {challenges: "3-6", impact: true}
    constraints: {business_impact_required: true, max_challenges: 6}
    compatible_slide_functions: [diagnosis, sales, product_overview]
    absorbed_from: [Presenton, banana-slides]
  - id: service_catalog_grid
    category: offer
    pick_when: ["Service lines, modules, deliverables, and scope boundaries need a clear catalog."]
    skip_when: ["The slide is pricing-first; use pricing_table."]
    data_shape: {services: "3-8", deliverables: true}
    constraints: {outcome_per_service_required: true, max_services: 8}
    compatible_slide_functions: [offer, commercial, proposal]
    absorbed_from: [Presenton, presentation-ai]
  - id: team_credentials_grid
    category: credibility
    pick_when: ["Team expertise and delivery relevance are part of the proof."]
    skip_when: ["The slide is about reporting structure; use org_chart."]
    data_shape: {members: "2-8", credentials: true}
    constraints: {relevance_note_required: true, avoid_long_bios: true}
    compatible_slide_functions: [credibility, sales, fundraising]
    absorbed_from: [Presenton, ppt-master]
  - id: table_of_contents
    category: navigation
    pick_when: ["A long deck needs chapter orientation and narrative flow."]
    skip_when: ["The deck should feel like one continuous argument."]
    data_shape: {sections: "4-8", optional_page_numbers: true}
    constraints: {section_titles_required: true, max_sections: 8}
    compatible_slide_functions: [navigation, facilitation]
    absorbed_from: [Presenton]
  - id: contact_footer
    category: action
    pick_when: ["A final slide needs contact details, QR/link, owner, and next action."]
    skip_when: ["The final slide is a decision ask; use decision_card."]
    data_shape: {contact_channels: "1-4", next_action: 1}
    constraints: {next_action_required: true, contact_required: true}
    compatible_slide_functions: [action, closing]
    absorbed_from: [Presenton, powerpoint-skill]
  - id: closing_card
    category: action
    pick_when: ["A deck needs a polished close with explicit ask or meeting path."]
    skip_when: ["Contact details are the main content; use contact_footer."]
    data_shape: {ask: 1, supporting_note: "0-1"}
    constraints: {ask_required: true, avoid_generic_thank_you: true}
    compatible_slide_functions: [action, conversion]
    absorbed_from: [Presenton, banana-slides]
  - id: social_proof_wall
    category: proof
    pick_when: ["Credibility needs a compact wall of logos, testimonials, adoption signals, or trust markers."]
    skip_when: ["The proof is a single sourced quote; use quote_evidence_panel."]
    data_shape: {proof_items: "4-24", source_note: true}
    constraints: {source_required: true, no_fake_logos: true, relevance_note_required: true}
    compatible_slide_functions: [credibility, sales, fundraising]
    absorbed_from: [Presenton, presentation-ai]
```


## Referência: references/source/templates/visual/composition-patterns.yaml

```yaml
version: 1
purpose: >
  Visual composition grammar for image-heavy and media-heavy slides. Image type
  describes what the visual is; composition pattern describes how it is placed,
  layered, annotated, and made safe for PPTX/HTML export.
absorbed_from:
  - ppt-master/image-layout-patterns
  - ppt-master/spec_lock resource-list pattern ids

composition_model:
  rule: "primary_structure + optional_modifier_layers + native_overlay_plan"
  block_if:
    - composition_pattern_missing_for_generated_hero_image
    - modifier_layer_used_without_export_fallback
    - native_text_embedded_in_generated_image_when_editability_required
    - visual_pattern_not_declared_in_render_lock

primary_structures:
  - id: full_bleed_canvas
    use_when:
      - Cover, section, or emotional reset slide needs one visual canvas.
    avoid_when:
      - Exact labels or inspectable UI detail are central.
    pptx_safety: medium
    native_overlay_required: true

  - id: split_visual_text
    use_when:
      - One visual proof or scene supports one argument.
    avoid_when:
      - Slide has more than one message or visual requires full width.
    pptx_safety: high
    native_overlay_required: false

  - id: evidence_panel
    use_when:
      - Screenshot, diagram, chart, or artifact is the proof.
    avoid_when:
      - Visual is decorative or low-confidence.
    pptx_safety: high
    native_overlay_required: true

  - id: side_by_side_comparison
    use_when:
      - Before/after, option A/B, competitor comparison, or two workflows matter.
    avoid_when:
      - Items are not symmetric or one side requires much more detail.
    pptx_safety: high
    native_overlay_required: true

  - id: image_as_canvas_annotation
    use_when:
      - A screenshot, workflow, or real artifact needs callouts.
    avoid_when:
      - Callouts would hide the evidence.
    pptx_safety: medium
    native_overlay_required: true

  - id: multi_asset_grid
    use_when:
      - Multiple examples or artifacts need scannable comparison.
    avoid_when:
      - Each asset requires large readable detail.
    pptx_safety: high
    native_overlay_required: true

modifier_layers:
  - id: annotation_cards
    use_when:
      - Explain evidence without baking text into the image.
    fallback_for_powerpoint: native_shapes_and_connectors

  - id: focus_crop
    use_when:
      - Source visual is real but too broad.
    fallback_for_powerpoint: image_crop_src_rect_or_pre_cropped_asset

  - id: dimmed_backdrop
    use_when:
      - Native title or key claim needs contrast over full-bleed image.
    fallback_for_powerpoint: translucent_native_rectangle

  - id: numbered_steps_overlay
    use_when:
      - Visual explains sequence or workflow.
    fallback_for_powerpoint: native_number_badges

  - id: magnified_detail
    use_when:
      - A small UI or data detail is the point.
    fallback_for_powerpoint: duplicated_cropped_image_region

composition_patterns:
  - id: C01
    name: Full bleed with native claim
    expression: "full_bleed_canvas + dimmed_backdrop"
    best_for: [cover, reframe, manifesto, section_break]
    native_overlay_plan: headline_and_caption
    forbidden_if_pptx_editable: []

  - id: C02
    name: Evidence panel with callouts
    expression: "evidence_panel + annotation_cards"
    best_for: [proof, demo_payoff, case_study, benchmark]
    native_overlay_plan: callout_cards_and_connectors
    forbidden_if_pptx_editable: []

  - id: C03
    name: Screenshot canvas with magnified detail
    expression: "image_as_canvas_annotation + magnified_detail"
    best_for: [product_demo, ux_audit, implementation_walkthrough]
    native_overlay_plan: zoom_region_native_labels
    forbidden_if_pptx_editable: []

  - id: C04
    name: Side-by-side option comparison
    expression: "side_by_side_comparison + annotation_cards"
    best_for: [before_after, competitor_comparison, choice_frame]
    native_overlay_plan: symmetric_labels_and_verdict
    forbidden_if_pptx_editable: []

  - id: C05
    name: Multi-example proof grid
    expression: "multi_asset_grid + numbered_steps_overlay"
    best_for: [proof_stack, portfolio_examples, evidence_wall]
    native_overlay_plan: numbered_captions
    forbidden_if_pptx_editable: []

selection_report_required_fields:
  - composition_pattern_id
  - expression
  - selected_reason
  - rejected_patterns
  - pptx_fallback
  - native_overlay_plan
```


## Referência: references/source/templates/visual/design-mastery-contract.yaml

```yaml
version: 1
name: design-mastery-contract
purpose: >
  Contract for pushing slide design from "good enough" to reference-level.
  Use when the deck must score 95-100 in design, brand fidelity, template
  replication, and rendered visual quality.

absorbed_from:
  ppt_master:
    - pptx_template_manifest_import
    - layout_indexing
    - spec_lock_vs_render_lock
    - rendered_roundtrip_inspection
  presentation_ai:
    - theme_runtime
    - serialized_template_examples
    - rich_visual_blocks
    - chart_editor_contracts
  banana_slides:
    - prompt_to_edit_visual_iteration
    - high_polish_visual_defaults
    - reversible_visual_history
  powerpoint_skill:
    - overlap_boundary_checks
    - text_fit
    - technical_visual_qa

score_target:
  design_category_target: 100
  minimum_operational_score: 95
  score_lenses:
    - id: template_manifest
      weight: 15
      reference_level: Imported or selected template is represented as tokens, layout roles, components, density, chart style, imagery, and anti-patterns.
    - id: brand_fidelity
      weight: 20
      reference_level: Deck matches the visual language of the reference system beyond colors and logo.
    - id: layout_intelligence
      weight: 20
      reference_level: Layouts are chosen by slide function and vary without becoming a collage.
    - id: rendered_quality
      weight: 20
      reference_level: Rendered key slides pass hierarchy, spacing, contrast, crop, scan-path, and emphasis checks.
    - id: theme_runtime
      weight: 15
      reference_level: Tokens are consistently applied across slides, charts, diagrams, callouts, and exports.
    - id: iteration_loop
      weight: 10
      reference_level: Visual critique produces scoped diffs and corrected key slides before final delivery.

required_outputs:
  - file: design-mastery-report.yaml
    root_key: design_mastery_report
  - file: brand-template-manifest.yaml
    root_key: brand_template_manifest
  - file: key-slide-render-review.yaml
    root_key: key_slide_render_review
  - file: visual-regression-checklist.yaml
    root_key: visual_regression_checklist

brand_template_manifest:
  required_fields:
    - source_reference
    - token_map
    - typography_system
    - grid_system
    - layout_families
    - component_patterns
    - chart_language
    - media_language
    - anti_patterns
  token_map:
    required:
      - colors
      - fonts
      - type_scale
      - spacing
      - radius
      - stroke
      - shadow
      - chart_palette
  component_patterns:
    examples:
      - title_block
      - evidence_card
      - metric_row
      - contrast_panel
      - quote_block
      - callout
      - timeline
      - comparison_table
      - architecture_node
      - footer_provenance

layout_intelligence:
  required_fields:
    - slide_function_to_layout_map
    - rejected_layout_runners_up
    - repetition_control
    - quiet_slide_ratio
    - density_budget
  rules:
    - No more than two consecutive slides may share the same layout family.
    - Every decisive slide must declare why its layout is the best fit for the audience movement.
    - Rejected runners-up must include deck-specific reasons, not generic preference.
    - Dense executive slides must move detail into appendix if they exceed the function budget.
    - Visual story slides must use media that proves, demonstrates, or clarifies the claim.

rendered_key_slide_review:
  required_slides:
    - cover
    - reframe
    - mechanism
    - proof_or_demo
    - cta_or_decision
  checks:
    - hierarchy
    - scan_path
    - whitespace
    - contrast
    - alignment
    - crop_and_media_relevance
    - title_claim_visibility
    - body_text_fit
    - chart_or_diagram_readability
    - brand_fidelity
  block_if:
    - any_decisive_slide_has_generic_stock_visual
    - any_action_title_is_not_visually_dominant
    - any_key_slide_has_unresolved_overlap_or_clipping
    - any_key_slide_has_low_contrast_text
    - rendered_output_differs_from_locked_design_direction_without_reason

theme_runtime:
  required_fields:
    - token_source
    - runtime_mapping
    - fallback_policy
    - export_policy
  runtime_mapping:
    required:
      - slide_background
      - text_styles
      - chart_styles
      - diagram_styles
      - shape_styles
      - table_styles
      - image_treatment
      - accent_usage
  block_if:
    - tokens_exist_but_charts_ignore_them
    - diagrams_use_unmapped_colors_or_fonts
    - fallback_font_changes_layout_without_review

iteration_loop:
  required_steps:
    - render_or_preview_key_slides
    - score_key_slides_against_design_lenses
    - produce_visual_patch_list
    - apply_only_scoped_visual_fixes
    - rerun_key_slide_review
  patch_types:
    - hierarchy_fix
    - density_fix
    - crop_fix
    - spacing_fix
    - contrast_fix
    - template_fidelity_fix
    - chart_readability_fix
    - layout_variation_fix

validation:
  block_if:
    - design_mastery_report_missing_for_premium_deck
    - brand_template_manifest_missing_when_reference_exists
    - key_slide_render_review_missing
    - template_selection_without_rejected_runners_up
    - theme_tokens_not_applied_to_charts_or_diagrams
    - final_design_score_below_95_when_user_requested_premium_or_reference_level
  warn_if:
    - design_score_between_90_and_94
    - no_imported_template_or_visual_reference
    - visual_direction_relies_on_single_palette_or_motif
    - no_before_after_visual_iteration
```


## Referência: references/source/templates/visual/design-mastery-report.yaml

```yaml
version: 1
name: design-mastery-report
purpose: >
  Score Design as an operational release gate. This report is required when
  the user asks for premium/reference-level design or Design 100.

design_mastery_report:
  deck_id: ""
  generated_at: ""
  target_score: 95
  verdict: "pass | warn | fail"
  source_artifacts:
    brand_template_manifest: "brand-template-manifest.yaml"
    design_direction: "design-direction.yaml"
    render_lock: "render-lock.yaml"
    template_selection_report: "template-selection-report.yaml"
    key_slide_render_review: "key-slide-render-review.yaml"
    visual_regression_checklist: "visual-regression-checklist.yaml"
  score_lenses:
    - id: template_manifest
      weight: 15
      score: 0
      evidence: ""
      blockers: []
    - id: brand_fidelity
      weight: 20
      score: 0
      evidence: ""
      blockers: []
    - id: layout_intelligence
      weight: 20
      score: 0
      evidence: ""
      blockers: []
    - id: rendered_quality
      weight: 20
      score: 0
      evidence: ""
      blockers: []
    - id: theme_runtime
      weight: 15
      score: 0
      evidence: ""
      blockers: []
    - id: iteration_loop
      weight: 10
      score: 0
      evidence: ""
      blockers: []
  calculated_score: 0
  microdimension_mapping:
    visual_layout_quality__layout_variety:
      evidence: ""
      target_met: false
    visual_layout_quality__visual_density_control:
      evidence: ""
      target_met: false
    visual_layout_quality__rendered_visual_quality:
      evidence: ""
      target_met: false
    template_import_replication__template_manifest:
      evidence: ""
      target_met: false
    template_import_replication__brand_fidelity:
      evidence: ""
      target_met: false
    template_import_replication__template_selection_logic:
      evidence: ""
      target_met: false
    theme_tokens_branding__token_schema:
      evidence: ""
      target_met: false
    theme_tokens_branding__theme_runtime:
      evidence: ""
      target_met: false
    theme_tokens_branding__brand_guardrails:
      evidence: ""
      target_met: false
  required_fixes:
    - slide_id: ""
      issue: ""
      patch_type: "hierarchy_fix | density_fix | crop_fix | spacing_fix | contrast_fix | template_fidelity_fix | chart_readability_fix | layout_variation_fix"
      owner: ""
      status: "open | fixed | accepted_risk"

validation:
  block_if:
    - calculated_score_below_target
    - any_score_lens_missing_evidence
    - brand_fidelity_below_90
    - rendered_quality_below_90
    - unresolved_blockers
```


## Referência: references/source/templates/visual/key-slide-render-review.yaml

```yaml
version: 1
name: key-slide-render-review
purpose: >
  Review decisive rendered slides before final delivery. Source specs are not
  enough for Design 100; visual quality must be observed in render or preview.

key_slide_render_review:
  deck_id: ""
  generated_at: ""
  render_source: "screenshot | pptx_preview | html_preview | pdf_export | manual_preview"
  reviewed_slides:
    - slide_id: "s01"
      required_role: "cover | reframe | mechanism | proof_or_demo | cta_or_decision"
      screenshot_or_preview_path: ""
      score:
        hierarchy: 0
        scan_path: 0
        whitespace: 0
        contrast: 0
        alignment: 0
        crop_and_media_relevance: 0
        title_claim_visibility: 0
        body_text_fit: 0
        chart_or_diagram_readability: 0
        brand_fidelity: 0
      average_score: 0
      blockers:
        - ""
      visual_patches:
        - patch_type: "hierarchy_fix | density_fix | crop_fix | spacing_fix | contrast_fix | template_fidelity_fix | chart_readability_fix | layout_variation_fix"
          instruction: ""
          status: "open | applied | accepted_risk"
  aggregate:
    average_score: 0
    lowest_slide_score: 0
    verdict: "pass | warn | fail"

validation:
  required_roles:
    - cover
    - reframe
    - mechanism
    - proof_or_demo
    - cta_or_decision
  block_if:
    - missing_required_role
    - aggregate_average_below_95
    - any_slide_below_90
    - unresolved_visual_blockers
    - preview_path_missing_for_rendered_review
```


## Referência: references/source/templates/visual/layout-families.yaml

```yaml
version: 1
layout_families:
  - id: executive_dense
    pick_when:
      - Board, finance, benchmark, or operating review with high information density.
    skip_when:
      - Marketing hero or emotional story opening.
    patterns: [kpi_cards, harvey_balls_table, financial_statement_table, bullet_chart]
    density: high
    constraints:
      min_font_px: 16
      max_visible_words: 120
      reserve_detail_for_appendix: true
    absorbed_from: [ppt-master, powerpoint-skill]

  - id: editorial_persuasive
    pick_when:
      - Sales, webinar, manifesto, pitch, or strategy deck where belief shift matters.
    skip_when:
      - Pure technical appendix or legal documentation.
    patterns: [hero_claim, contrast, before_after, mechanism_layer]
    density: medium
    constraints:
      max_visible_words: 55
      action_title_required: true
      no_generic_section_titles: true
    absorbed_from: [slide-deck-ai, presentation-ai, Presenton]

  - id: technical_system
    pick_when:
      - Architecture, API, agent workflow, runtime, or product system explanation.
    skip_when:
      - Simple customer journey with no system layers.
    patterns: [layered_architecture, pipeline_with_stages, client_server_flow, module_composition]
    density: medium_high
    constraints:
      label_every_arrow: true
      explain_module_role: true
      avoid_unlabeled_boxes: true
    absorbed_from: [ppt-master, Presenton, PPTAgent]

  - id: visual_story
    pick_when:
      - A demo, webinar, or product narrative benefits from visual scene, media, or transformation.
    skip_when:
      - Evidence is mostly numeric.
    patterns: [full_bleed_image, image_left_text_right, before_after, journey_map]
    density: low_medium
    constraints:
      image_must_carry_message: true
      no_purely_atmospheric_stock: true
      media_relevance_reason_required: true
    absorbed_from: [Presenton, PPTAgent, banana-slides]

  - id: academic_rigorous
    pick_when:
      - Research, thesis, training, or technical lecture needs rigorous hierarchy.
    skip_when:
      - Conversion-oriented sales or webinar deck.
    patterns: [claim_evidence, table, equation_diagram, method_flow]
    density: medium
    constraints:
      source_required: true
      define_terms_before_use: true
      worked_example_within_two_slides: true
    absorbed_from: [powerpoint-skill, ppt-master]
```


## Referência: references/source/templates/visual/media-layouts.yaml

```yaml
version: 1
media_layouts:
  - id: full_bleed_image
    pick_when:
      - The image is concrete, inspection-worthy, and carries the core message.
    skip_when:
      - The image is atmospheric, generic, dark, blurred, or unrelated.
    elements:
      - {name: main_image, type: image, required: true, role: evidence_or_scene}
      - {name: overlay_claim, type: text, required: true, max_chars: 90}
    constraints:
      image_relevance_reason_required: true
      overlay_contrast_required: true
      max_visible_words: 28
    absorbed_from: [Presenton, banana-slides]

  - id: image_left_text_right
    pick_when:
      - One image needs interpretation by a concise right-side text block.
    skip_when:
      - Text is longer than 90 words or image is decorative.
    elements:
      - {name: main_image, type: image, required: true}
      - {name: action_title, type: text, required: true, max_chars: 80}
      - {name: explanation, type: text, required: true, max_chars: 420}
    constraints:
      image_width_percent: 55
      text_width_percent: 35
      image_alt_required: true
    absorbed_from: [PPTAgent, Presenton]

  - id: centered_image_with_caption
    pick_when:
      - The image is the evidence and needs title plus caption.
    skip_when:
      - The slide needs multiple claims or process explanation.
    elements:
      - {name: action_title, type: text, required: true}
      - {name: main_image, type: image, required: true}
      - {name: caption, type: text, required: true, max_chars: 180}
    constraints:
      caption_must_interpret_not_describe: true
    absorbed_from: [PPTAgent]

  - id: video_demo_frame
    pick_when:
      - A product or workflow video is stronger than a static screenshot.
    skip_when:
      - The video is not directly tied to the slide claim.
    elements:
      - {name: video_frame, type: video_or_screenshot, required: true}
      - {name: action_title, type: text, required: true}
      - {name: callouts, type: list, required: false, max_chars: 180}
    constraints:
      fallback_static_frame_required: true
      callouts_max: 3
    absorbed_from: [PresentAgent-2, banana-slides]
```


## Referência: references/source/templates/visual/redpine-deep-patterns.yaml

```yaml
version: 1
historical_sources:
  - ../../../../apps/redpine-ds/src/design-system/tokens.json
  - ../../../../apps/redpine-ds/src/design-system/components.manifest.json
  - ../../../../apps/redpine-ds/src/design-system/components.map.json
  - ../../../../apps/redpine-ds/src/styles/foundations.css
  - ../../../../apps/redpine-ds/src/components/system/data.ts

patterns:
  - id: redpine_12_col_report_grid
    category: layout_system
    pick_when:
      - The slide/deck needs disciplined editorial report layout with body text max width.
    skip_when:
      - The slide is a cinematic hero or full-screen visual.
    structure:
      grid: 12_columns_desktop
      mobile_grid: 2_columns
      gutters:
        small: "16px"
        desktop: "32px"
      max_widths: [544, 704, 928, 1136, 1376]
      recommended_body_span: 7
    constraints:
      body_text_max_span: 7
      use_column_span_intentionally: true
      section_spacing_desktop_px: 64
    absorbed_from: [redpine_foundations_css]

  - id: redpine_palette_surface_stack
    category: theme_behavior
    pick_when:
      - The deck needs consistent light/dark surface transitions without inventing palettes.
    skip_when:
      - The requested brand requires colorful multi-accent surfaces.
    palettes:
      light: [snow, paper, bone]
      dark: [ink, ink_elevated, ink_hover]
    semantic_bindings:
      bg: surface
      fg: text
      fg_2: secondary_text
      fg_3: tertiary_text
      border: hairline
      accent: red
    constraints:
      components_consume_semantic_aliases: true
      dark_palettes_override_shadcn_slots: true
      do_not_add_glassmorphism: true
    absorbed_from: [redpine_foundations_css, redpine_tokens]

  - id: redpine_component_manifest_grid
    category: component_audit
    pick_when:
      - A deck needs to show component maturity, production readiness, variants, or accessibility.
    skip_when:
      - The goal is pure marketing positioning with no component detail.
    structure:
      component_card_slots:
        - name
        - status
        - file_or_import
        - variants
        - a11y_role
        - keyboard_contract
        - token_consumption
      status_legend: [ready, beta, experimental, deprecated]
    constraints:
      status_required: true
      accessibility_required: true
      token_mapping_required: true
      deprecated_components_must_be_marked: true
    absorbed_from: [redpine_components_manifest, redpine_components_map]

  - id: redpine_accessible_status_row
    category: operational_table
    pick_when:
      - Risk, incidents, QA findings, or production statuses must be communicated without color-only semantics.
    skip_when:
      - The content is qualitative narrative.
    structure:
      row_slots: [id, site_or_scope, type, owner, status, reported, severity, risk_score]
      status_values: [critical, review, open, resolved]
      severity_values: [Critical, High, Medium, Low]
    constraints:
      status_text_required: true
      severity_text_required: true
      color_not_only_channel: true
      sort_by_risk_desc: true
      risk_score_visible: true
    absorbed_from: [redpine_system_data, redpine_components_manifest]

  - id: redpine_callout_left_rule
    category: editorial_callout
    pick_when:
      - A report needs a restrained insight, benchmark note, warning, or decision rationale.
    skip_when:
      - The callout is a high-drama manifesto quote.
    variants:
      - info
      - success
      - warning
      - danger
      - decision
    structure:
      left_rule: semantic_color
      title: display_font
      body: concise_paragraph
      source_or_owner: optional
    constraints:
      left_rule_not_only_signal: true
      title_required: true
      max_visible_words: 75
      no_shadow_by_default: true
    absorbed_from: [redpine_alert_component, redpine_blockquote_component]

  - id: redpine_dialog_decision_panel
    category: decision_panel
    pick_when:
      - A slide needs a focused decision, ask, or modal-like interrupt inside a dense report.
    skip_when:
      - The whole slide is already a hero decision slide.
    structure:
      container: elevated_surface
      top_rule: red
      slots: [decision_title, context, options, recommended_action, consequence]
    constraints:
      top_rule_can_not_replace_title: true
      recommendation_required: true
      consequence_required: true
      shadow_allowed: "tokens.shadow.3 only"
    absorbed_from: [redpine_dialog_component]

  - id: redpine_tabs_appendix_nav
    category: navigation
    pick_when:
      - Appendix or dashboard-like deck needs switchable sections or segmented comparison.
    skip_when:
      - The presentation is linear and live-delivered.
    structure:
      tablist: categories
      active_indicator: red_bottom_rule
      panels: content_sections
    constraints:
      active_tab_text_required: true
      not_color_only: true
      use_for_appendix_or_dashboards_only: true
    absorbed_from: [redpine_tabs_component]

  - id: redpine_form_field_briefing_slide
    category: input_schema
    pick_when:
      - A deck needs to show required briefing inputs, survey fields, or implementation setup.
    skip_when:
      - The slide is not about process, form, intake, or configuration.
    structure:
      field_slots: [label, input_value, helper_text, error_or_disabled_state]
      form_states: [default, focus, invalid, disabled]
    constraints:
      label_required: true
      helper_text_for_complex_fields: true
      invalid_state_must_include_text: true
    absorbed_from: [redpine_form_field_component]
```


## Referência: references/source/templates/visual/visual-regression-checklist.yaml

```yaml
version: 1
name: visual-regression-checklist
purpose: >
  Prevent known bad deck patterns from returning after design improvements.

visual_regression_checklist:
  deck_id: ""
  generated_at: ""
  checks:
    - id: no_identity_as_skin
      question: "Does the deck use brand language beyond logo/colors?"
      status: "pass | fail | n/a"
      evidence: ""
    - id: no_generic_stock_visual
      question: "Does every meaningful image prove, demonstrate, or clarify a claim?"
      status: "pass | fail | n/a"
      evidence: ""
    - id: no_repeated_layout_monotony
      question: "Are there no more than two consecutive slides in the same layout family?"
      status: "pass | fail | n/a"
      evidence: ""
    - id: no_dense_bullet_wall
      question: "Are dense slides intentionally structured as tables, diagrams, or appendix?"
      status: "pass | fail | n/a"
      evidence: ""
    - id: no_unmapped_theme_usage
      question: "Do charts, diagrams, tables, and shapes use mapped theme tokens?"
      status: "pass | fail | n/a"
      evidence: ""
    - id: no_unrendered_key_slides
      question: "Were decisive slides reviewed in render or preview?"
      status: "pass | fail | n/a"
      evidence: ""
    - id: no_weak_action_title_hierarchy
      question: "Is the action title visually dominant on each decisive slide?"
      status: "pass | fail | n/a"
      evidence: ""
    - id: no_unresolved_overlap_clipping
      question: "Are overlap, clipping, and text-fit issues resolved?"
      status: "pass | fail | n/a"
      evidence: ""
  verdict: "pass | warn | fail"
  release_blockers:
    - ""

validation:
  block_if:
    - any_required_check_fails
    - verdict_fail
    - release_blockers_not_empty
```


## Referência: references/source/templates/wireframes/agenda-timeline.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Agenda Timeline</title><style>body{margin:0;background:#fffdf5;color:#1f2933;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:56px;display:grid;grid-template-rows:auto 1fr auto;gap:30px}h1{margin:0;font-size:44px}.timeline{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;align-items:stretch}.block{border:1px solid #e7e1d2;background:white;border-radius:8px;padding:22px}.time{color:#7c3aed;font-weight:900;font-size:22px}.title{font-size:24px;font-weight:850;margin-top:18px}.outcome{color:#6b7280;font-size:17px;line-height:1.4;margin-top:14px}.decision{border-left:5px solid #f59e0b;padding-left:18px;font-size:22px;font-weight:800}</style></head><body><main class="slide"><h1>{{session_goal}}</h1><section class="timeline"><article class="block"><div class="time">{{time_1}}</div><div class="title">{{block_1}}</div><div class="outcome">{{outcome_1}}</div></article><article class="block"><div class="time">{{time_2}}</div><div class="title">{{block_2}}</div><div class="outcome">{{outcome_2}}</div></article><article class="block"><div class="time">{{time_3}}</div><div class="title">{{block_3}}</div><div class="outcome">{{outcome_3}}</div></article><article class="block"><div class="time">{{time_4}}</div><div class="title">{{block_4}}</div><div class="outcome">{{outcome_4}}</div></article><article class="block"><div class="time">{{time_5}}</div><div class="title">{{block_5}}</div><div class="outcome">{{outcome_5}}</div></article></section><footer class="decision">{{decision_point}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/api-request-response.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>API Request Response</title><style>body{margin:0;background:#06070d;color:#f8fbff;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:#101322;border:1px solid #2b3147;border-radius:8px;padding:20px}.label{color:#7cff6b;font-size:12px;letter-spacing:.12em;text-transform:uppercase;font-weight:900}pre{white-space:pre-wrap;font:18px/1.4 'IBM Plex Mono',monospace;color:#eaf2ff}.note{border-left:5px solid #7cff6b;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{endpoint_or_tool}}</h1><section class="cols"><article class="panel"><div class="label">Request</div><pre>{{request}}</pre></article><article class="panel"><div class="label">Response</div><pre>{{response}}</pre></article></section><footer class="note">{{behavior_note}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/architecture-tradeoff-table.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Architecture Tradeoff Table</title><style>body{margin:0;background:#071018;color:#eaf6ff;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.table{display:grid;grid-template-columns:1.2fr repeat(4,1fr);border:1px solid #233747}.cell{padding:16px;border-right:1px solid #233747;border-bottom:1px solid #233747;background:#0e1b26}.head{background:#51d6ff;color:#071018;font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:900}.rec{border-left:5px solid #9bdb7b;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="table"><div class="cell head">Opção</div><div class="cell head">Custo</div><div class="cell head">Risco</div><div class="cell head">Complexidade</div><div class="cell head">Operação</div><div class="cell">{{option_1}}</div><div class="cell">{{o1_cost}}</div><div class="cell">{{o1_risk}}</div><div class="cell">{{o1_complexity}}</div><div class="cell">{{o1_ops}}</div><div class="cell">{{option_2}}</div><div class="cell">{{o2_cost}}</div><div class="cell">{{o2_risk}}</div><div class="cell">{{o2_complexity}}</div><div class="cell">{{o2_ops}}</div><div class="cell">{{option_3}}</div><div class="cell">{{o3_cost}}</div><div class="cell">{{o3_risk}}</div><div class="cell">{{o3_complexity}}</div><div class="cell">{{o3_ops}}</div></section><footer class="rec">{{recommendation}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/benchmark-matrix.html

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <title>Benchmark Matrix Wireframe</title>
    <style>
      body { margin: 0; background: #050505; color: #f5f5ef; font: 14px Inter, Arial, sans-serif; }
      .wrap { padding: 32px; display: grid; grid-template-columns: 1fr 300px; gap: 24px; }
      h1 { margin: 0 0 18px; font-size: 28px; }
      .matrix { display: grid; grid-template-columns: 210px repeat(4, minmax(120px, 1fr)); border: 1px solid #292929; overflow: hidden; }
      .cell { min-height: 86px; padding: 12px; border-right: 1px solid #292929; border-bottom: 1px solid #292929; background: #101010; }
      .head { background: #171717; font-weight: 800; }
      .score { font-size: 28px; font-weight: 900; }
      .bar { height: 6px; background: #333; margin-top: 8px; }
      .bar span { display: block; height: 100%; background: #f5f5ef; }
      .win { background: #d7ff3f; color: #111; }
      aside { border-left: 1px solid #292929; padding-left: 24px; color: #b8b8b0; }
      .mono { font: 11px "IBM Plex Mono", monospace; text-transform: uppercase; letter-spacing: .08em; color: #d7ff3f; }
    </style>
  </head>
  <body>
    <div class="wrap">
      <main>
        <div class="mono">benchmark matrix</div>
        <h1>Matriz mostra diferença real; comentário vive no painel.</h1>
        <section class="matrix">
          <div class="cell head">Dimensão</div><div class="cell head">Player A</div><div class="cell head">Player B</div><div class="cell head">Player C</div><div class="cell head">Player D</div>
          <div class="cell">Prompt para deck completo</div><div class="cell win"><div class="score">95</div><div class="bar"><span style="width:95%"></span></div></div><div class="cell"><div class="score">82</div><div class="bar"><span style="width:82%"></span></div></div><div class="cell"><div class="score">75</div><div class="bar"><span style="width:75%"></span></div></div><div class="cell"><div class="score">70</div><div class="bar"><span style="width:70%"></span></div></div>
          <div class="cell">Template importável</div><div class="cell"><div class="score">75</div><div class="bar"><span style="width:75%"></span></div></div><div class="cell win"><div class="score">96</div><div class="bar"><span style="width:96%"></span></div></div><div class="cell"><div class="score">70</div><div class="bar"><span style="width:70%"></span></div></div><div class="cell"><div class="score">40</div><div class="bar"><span style="width:40%"></span></div></div>
        </section>
      </main>
      <aside>
        <div class="mono">selected cell</div>
        <h2>Por que 95?</h2>
        <p>Detalhe com evidência, path de fonte, limitação e implicação. A matriz em si fica limpa.</p>
      </aside>
    </div>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/brand-principles.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Brand Principles</title><style>body{margin:0;background:#faf7f2;color:#17120f;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:26px}h1{margin:0;font-size:44px}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.card{background:white;border:1px solid #e5d8c8;border-radius:8px;padding:24px}.num{color:#d946ef;font-size:14px;letter-spacing:.14em;text-transform:uppercase;font-weight:900}.title{font-size:30px;font-weight:900;margin-top:18px}.rule{color:#756b61;line-height:1.4;margin-top:14px;font-size:18px}.avoid{border-top:1px solid #e5d8c8;margin-top:20px;padding-top:14px;color:#f97316;font-weight:800}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="cards"><article class="card"><div class="num">01</div><div class="title">{{principle_1}}</div><div class="rule">{{rule_1}}</div><div class="avoid">{{avoid_1}}</div></article><article class="card"><div class="num">02</div><div class="title">{{principle_2}}</div><div class="rule">{{rule_2}}</div><div class="avoid">{{avoid_2}}</div></article><article class="card"><div class="num">03</div><div class="title">{{principle_3}}</div><div class="rule">{{rule_3}}</div><div class="avoid">{{avoid_3}}</div></article></section></main></body></html>
```


## Referência: references/source/templates/wireframes/business-challenges.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Business Challenges</title><style>body{margin:0;background:#fbfaf5;color:#111315;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.card{background:white;border:1px solid #ddd8cd;border-radius:8px;padding:24px}.num{color:#e5484d;font-weight:900}.title{font-size:28px;font-weight:900;margin-top:12px}.impact{color:#67615a;margin-top:14px;line-height:1.4}.bridge{border-left:5px solid #e5484d;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="grid"><article class="card"><div class="num">01</div><div class="title">{{challenge_1}}</div><div class="impact">{{impact_1}}</div></article><article class="card"><div class="num">02</div><div class="title">{{challenge_2}}</div><div class="impact">{{impact_2}}</div></article><article class="card"><div class="num">03</div><div class="title">{{challenge_3}}</div><div class="impact">{{impact_3}}</div></article></section><footer class="bridge">{{solution_bridge}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/case-study-proof.html

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <title>Case Study Proof Wireframe</title>
    <style>
      :root { --bg:#fbfaf5; --panel:#fff; --ink:#111315; --muted:#67615a; --line:#ddd8cd; --accent:#e5484d; --teal:#1f9d8a; }
      body { margin:0; background:var(--bg); color:var(--ink); font-family:Inter, Arial, sans-serif; }
      .slide { width:1280px; height:720px; box-sizing:border-box; padding:52px; display:grid; grid-template-rows:auto 1fr auto; gap:24px; }
      h1 { margin:0; font-size:44px; line-height:1.05; max-width:920px; }
      .story { display:grid; grid-template-columns:1fr 1fr 1fr; gap:18px; }
      .card { background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:24px; display:grid; grid-template-rows:auto auto 1fr; gap:16px; }
      .eyebrow { color:var(--accent); font-size:12px; letter-spacing:.14em; text-transform:uppercase; font-weight:850; }
      h2 { margin:0; font-size:30px; line-height:1.1; }
      p { margin:0; color:var(--muted); font-size:19px; line-height:1.42; }
      .result { color:var(--teal); font-size:56px; font-weight:900; }
      footer { display:grid; grid-template-columns:2fr 1fr; gap:24px; border-top:1px solid var(--line); padding-top:18px; }
      .lesson { font-size:22px; font-weight:750; }
      .source { color:var(--muted); font-size:15px; text-align:right; align-self:end; }
    </style>
  </head>
  <body>
    <main class="slide">
      <h1>{{action_title}}</h1>
      <section class="story">
        <article class="card"><div class="eyebrow">Antes</div><h2>{{baseline_title}}</h2><p>{{baseline_detail}}</p></article>
        <article class="card"><div class="eyebrow">Intervenção</div><h2>{{intervention_title}}</h2><p>{{intervention_detail}}</p></article>
        <article class="card"><div class="eyebrow">Resultado</div><div class="result">{{result_metric}}</div><p>{{result_detail}}</p></article>
      </section>
      <footer><div class="lesson">{{repeatable_lesson}}</div><div class="source">{{source_note}}</div></footer>
    </main>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/code-explanation.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Code Explanation</title><style>body{margin:0;background:#071018;color:#eaf6ff;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-columns:1.2fr .8fr;gap:26px}.code{background:#0e1b26;border:1px solid #233747;border-radius:8px;padding:24px}pre{white-space:pre-wrap;font:18px/1.45 'IBM Plex Mono',monospace}.side h1{font-size:40px;margin:0 0 24px}.note{border-left:4px solid #51d6ff;padding-left:16px;margin:16px 0;color:#8ea5b6;font-size:19px}.take{font-size:22px;font-weight:850;color:#9bdb7b;margin-top:28px}</style></head><body><main class="slide"><section class="code"><pre>{{code_excerpt}}</pre></section><aside class="side"><h1>{{action_title}}</h1><div class="note">{{annotation_1}}</div><div class="note">{{annotation_2}}</div><div class="note">{{annotation_3}}</div><div class="take">{{consequence}}</div></aside></main></body></html>
```


## Referência: references/source/templates/wireframes/cohort-retention.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Cohort Retention</title><style>body{margin:0;background:#fff;color:#1a1d21;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:56px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.heat{display:grid;grid-template-columns:160px repeat(6,1fr);gap:8px}.cell{padding:14px;border-radius:6px;background:#f4f6f8;text-align:center;font-weight:800}.head{color:#626a73;text-transform:uppercase;letter-spacing:.1em;font-size:12px}.c1{background:#d8f3dc}.c2{background:#b7e4c7}.c3{background:#95d5b2}.c4{background:#74c69d}.c5{background:#52b788;color:white}.c6{background:#2d6a4f;color:white}.note{color:#626a73;font-size:18px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="heat"><div></div><div class="cell head">M0</div><div class="cell head">M1</div><div class="cell head">M2</div><div class="cell head">M3</div><div class="cell head">M4</div><div class="cell head">M5</div><div class="cell head">{{cohort_1}}</div><div class="cell c6">{{c1_m0}}</div><div class="cell c5">{{c1_m1}}</div><div class="cell c4">{{c1_m2}}</div><div class="cell c3">{{c1_m3}}</div><div class="cell c2">{{c1_m4}}</div><div class="cell c1">{{c1_m5}}</div><div class="cell head">{{cohort_2}}</div><div class="cell c6">{{c2_m0}}</div><div class="cell c5">{{c2_m1}}</div><div class="cell c4">{{c2_m2}}</div><div class="cell c3">{{c2_m3}}</div><div class="cell c2">{{c2_m4}}</div><div class="cell c1">{{c2_m5}}</div><div class="cell head">{{cohort_3}}</div><div class="cell c6">{{c3_m0}}</div><div class="cell c5">{{c3_m1}}</div><div class="cell c4">{{c3_m2}}</div><div class="cell c3">{{c3_m3}}</div><div class="cell c2">{{c3_m4}}</div><div class="cell c1">{{c3_m5}}</div></section><footer class="note">{{retention_pattern}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/competitive-landscape.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Competitive Landscape</title><style>body{margin:0;background:#f8fafc;color:#101828;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.table{display:grid;grid-template-columns:1.1fr repeat(4,1fr);border:1px solid #d0d5dd}.cell{background:white;padding:16px;border-right:1px solid #d0d5dd;border-bottom:1px solid #d0d5dd}.head{background:#155eef;color:white;font-size:12px;text-transform:uppercase;letter-spacing:.1em;font-weight:900}.win{font-weight:900;color:#155eef}.take{border-left:5px solid #155eef;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="table"><div class="cell head">Player</div><div class="cell head">{{criterion_1}}</div><div class="cell head">{{criterion_2}}</div><div class="cell head">{{criterion_3}}</div><div class="cell head">Wedge</div><div class="cell">{{player_1}}</div><div class="cell win">{{p1_c1}}</div><div class="cell">{{p1_c2}}</div><div class="cell">{{p1_c3}}</div><div class="cell">{{p1_wedge}}</div><div class="cell">{{player_2}}</div><div class="cell">{{p2_c1}}</div><div class="cell win">{{p2_c2}}</div><div class="cell">{{p2_c3}}</div><div class="cell">{{p2_wedge}}</div><div class="cell">{{player_3}}</div><div class="cell">{{p3_c1}}</div><div class="cell">{{p3_c2}}</div><div class="cell win">{{p3_c3}}</div><div class="cell">{{p3_wedge}}</div></section><footer class="take">{{strategic_takeaway}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/compliance-grid.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Compliance Grid</title><style>body{margin:0;background:#f9fafb;color:#111827;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.control{background:white;border:1px solid #d1d5db;border-radius:8px;padding:20px}.label{color:#1d4ed8;font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:900}.name{font-size:24px;font-weight:900;margin-top:14px}.evidence{color:#6b7280;margin-top:12px;line-height:1.35}.gap{color:#b45309;margin-top:14px;font-weight:800}.note{border-left:5px solid #1d4ed8;padding-left:18px;font-size:20px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="grid"><article class="control"><div class="label">{{control_1_status}}</div><div class="name">{{control_1}}</div><div class="evidence">{{evidence_1}}</div><div class="gap">{{gap_1}}</div></article><article class="control"><div class="label">{{control_2_status}}</div><div class="name">{{control_2}}</div><div class="evidence">{{evidence_2}}</div><div class="gap">{{gap_2}}</div></article><article class="control"><div class="label">{{control_3_status}}</div><div class="name">{{control_3}}</div><div class="evidence">{{evidence_3}}</div><div class="gap">{{gap_3}}</div></article><article class="control"><div class="label">{{control_4_status}}</div><div class="name">{{control_4}}</div><div class="evidence">{{evidence_4}}</div><div class="gap">{{gap_4}}</div></article></section><footer class="note">{{readiness_note}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/contact-next-step.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Contact Next Step</title><style>body{margin:0;background:#05070a;color:#eef6ff;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:64px;display:grid;grid-template-columns:1fr 360px;gap:54px;align-items:end}.ask{font-size:72px;line-height:1.02;font-weight:950}.side{background:#10151d;border:1px solid #263241;border-radius:8px;padding:28px}.label{color:#00e5a8;font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:900}.contact{font-size:24px;font-weight:850;margin-top:16px}.date{color:#9aabbc;margin-top:28px;font-size:20px}.qr{height:150px;background:#eef6ff;color:#05070a;display:grid;place-items:center;margin-top:24px;font-weight:900}</style></head><body><main class="slide"><section class="ask">{{next_action}}</section><aside class="side"><div class="label">Contato</div><div class="contact">{{contact_1}}</div><div class="contact">{{contact_2}}</div><div class="date">{{owner_or_date}}</div><div class="qr">{{qr_or_link}}</div></aside></main></body></html>
```


## Referência: references/source/templates/wireframes/dashboard-grid.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Dashboard Grid</title><style>body{margin:0;background:#f8fafc;color:#101828;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr;gap:22px}h1{margin:0;font-size:42px}.grid{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr);gap:16px}.panel{background:white;border:1px solid #d0d5dd;border-radius:8px;padding:22px}.label{color:#667085;font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:900}.value{font-size:46px;font-weight:900;margin-top:18px}.spark{height:36px;background:linear-gradient(90deg,#155eef 65%,#eaecf0 65%);margin-top:22px}.note{color:#667085;margin-top:12px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="grid"><article class="panel"><div class="label">{{m1_label}}</div><div class="value">{{m1_value}}</div><div class="spark"></div><div class="note">{{m1_note}}</div></article><article class="panel"><div class="label">{{m2_label}}</div><div class="value">{{m2_value}}</div><div class="spark"></div><div class="note">{{m2_note}}</div></article><article class="panel"><div class="label">{{m3_label}}</div><div class="value">{{m3_value}}</div><div class="spark"></div><div class="note">{{m3_note}}</div></article><article class="panel"><div class="label">{{m4_label}}</div><div class="value">{{m4_value}}</div><div class="spark"></div><div class="note">{{m4_note}}</div></article><article class="panel"><div class="label">{{m5_label}}</div><div class="value">{{m5_value}}</div><div class="spark"></div><div class="note">{{m5_note}}</div></article><article class="panel"><div class="label">{{m6_label}}</div><div class="value">{{m6_value}}</div><div class="spark"></div><div class="note">{{m6_note}}</div></article></section></main></body></html>
```


## Referência: references/source/templates/wireframes/data-lineage.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Data Lineage</title><style>body{margin:0;background:#071018;color:#eaf6ff;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.flow{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;align-items:stretch}.stage{border:1px solid #233747;background:#0e1b26;border-radius:8px;padding:20px}.label{color:#51d6ff;font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:900}.name{font-size:24px;font-weight:900;margin-top:14px}.meta{color:#8ea5b6;line-height:1.4;margin-top:12px}.guard{border-left:5px solid #f6c85f;padding-left:18px;font-size:20px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="flow"><article class="stage"><div class="label">Source</div><div class="name">{{source}}</div><div class="meta">{{source_note}}</div></article><article class="stage"><div class="label">Extract</div><div class="name">{{extract}}</div><div class="meta">{{extract_note}}</div></article><article class="stage"><div class="label">Transform</div><div class="name">{{transform}}</div><div class="meta">{{transform_note}}</div></article><article class="stage"><div class="label">Store</div><div class="name">{{store}}</div><div class="meta">{{store_note}}</div></article><article class="stage"><div class="label">Use</div><div class="name">{{use}}</div><div class="meta">{{use_note}}</div></article></section><footer class="guard">{{boundary_or_policy}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/decision-options.html

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <title>Decision Options Wireframe</title>
    <style>
      :root { --bg:#090a0b; --panel:#14161a; --ink:#f3f1e8; --muted:#a4a09a; --line:#2d3138; --accent:#b6f04a; --risk:#ff5e5b; }
      body { margin:0; background:var(--bg); color:var(--ink); font-family:Inter, Arial, sans-serif; }
      .slide { width:1280px; height:720px; box-sizing:border-box; padding:48px; display:grid; grid-template-rows:auto 1fr; gap:34px; }
      h1 { margin:0; font-size:46px; line-height:1.05; max-width:920px; }
      .deck { display:grid; grid-template-columns:repeat(3,1fr); gap:18px; }
      .option { border:1px solid var(--line); background:var(--panel); border-radius:8px; padding:24px; display:grid; grid-template-rows:auto auto 1fr auto; gap:18px; }
      .option.recommended { border-color:var(--accent); box-shadow:inset 0 0 0 2px var(--accent); }
      .eyebrow { color:var(--accent); font-size:12px; letter-spacing:.14em; text-transform:uppercase; font-weight:800; }
      h2 { margin:0; font-size:30px; line-height:1.08; }
      ul { margin:0; padding-left:20px; color:var(--muted); font-size:18px; line-height:1.45; }
      .score { display:flex; justify-content:space-between; border-top:1px solid var(--line); padding-top:16px; font-size:18px; }
      .score strong { color:var(--ink); font-size:30px; }
      .tradeoff { color:var(--risk); font-weight:700; }
    </style>
  </head>
  <body>
    <main class="slide">
      <h1>{{action_title}}</h1>
      <section class="deck">
        <article class="option"><div class="eyebrow">Opção A</div><h2>{{option_a_name}}</h2><ul><li>{{option_a_point_1}}</li><li>{{option_a_point_2}}</li><li>{{option_a_point_3}}</li></ul><div class="score"><span>{{option_a_fit}}</span><strong>{{option_a_score}}</strong></div></article>
        <article class="option recommended"><div class="eyebrow">Recomendado</div><h2>{{option_b_name}}</h2><ul><li>{{option_b_point_1}}</li><li>{{option_b_point_2}}</li><li>{{option_b_point_3}}</li></ul><div class="score"><span>{{option_b_fit}}</span><strong>{{option_b_score}}</strong></div></article>
        <article class="option"><div class="eyebrow">Opção C</div><h2>{{option_c_name}}</h2><ul><li>{{option_c_point_1}}</li><li>{{option_c_point_2}}</li><li>{{option_c_point_3}}</li></ul><div class="score"><span class="tradeoff">{{option_c_tradeoff}}</span><strong>{{option_c_score}}</strong></div></article>
      </section>
    </main>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/decision-tree.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Decision Tree</title><style>body{margin:0;background:#090a0b;color:#f3f1e8;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr;gap:28px}h1{margin:0;font-size:42px}.tree{display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px;align-items:center}.node{border:1px solid #2d3138;background:#14161a;border-radius:8px;padding:22px}.root{border-color:#b6f04a}.q{color:#b6f04a;font-size:12px;letter-spacing:.12em;text-transform:uppercase;font-weight:900}.txt{font-size:26px;font-weight:900;margin-top:12px}.act{color:#a4a09a;margin-top:12px;line-height:1.4}.branch{display:grid;gap:18px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="tree"><article class="node root"><div class="q">Critério inicial</div><div class="txt">{{root_question}}</div><div class="act">{{root_context}}</div></article><div class="branch"><article class="node"><div class="q">{{branch_1_label}}</div><div class="txt">{{branch_1_question}}</div><div class="act">{{branch_1_action}}</div></article><article class="node"><div class="q">{{branch_2_label}}</div><div class="txt">{{branch_2_question}}</div><div class="act">{{branch_2_action}}</div></article></div><div class="branch"><article class="node"><div class="q">Decisão A</div><div class="txt">{{decision_a}}</div><div class="act">{{decision_a_action}}</div></article><article class="node"><div class="q">Decisão B</div><div class="txt">{{decision_b}}</div><div class="act">{{decision_b_action}}</div></article></div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/dependency-map.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Dependency Map</title><style>body{margin:0;background:#fff;color:#151515;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:56px;display:grid;grid-template-rows:auto 1fr;gap:30px}h1{margin:0;font-size:42px}.map{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(2,1fr);gap:22px;position:relative}.node{background:#fff;border:2px solid #d9d9d2;border-radius:8px;padding:22px}.critical{border-color:#b42318}.label{color:#2347ff;font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:900}.title{font-size:24px;font-weight:900;margin-top:12px}.meta{color:#666;margin-top:10px}.arrow{position:absolute;color:#777;font-weight:900}.a1{left:260px;top:90px}.a2{left:570px;top:90px}.a3{left:880px;top:90px}.a4{left:570px;top:330px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="map"><article class="node"><div class="label">{{node_1_type}}</div><div class="title">{{node_1}}</div><div class="meta">{{node_1_owner}}</div></article><article class="node"><div class="label">{{node_2_type}}</div><div class="title">{{node_2}}</div><div class="meta">{{node_2_owner}}</div></article><article class="node critical"><div class="label">Critical</div><div class="title">{{node_3}}</div><div class="meta">{{node_3_owner}}</div></article><article class="node"><div class="label">{{node_4_type}}</div><div class="title">{{node_4}}</div><div class="meta">{{node_4_owner}}</div></article><article class="node"><div class="label">{{node_5_type}}</div><div class="title">{{node_5}}</div><div class="meta">{{node_5_owner}}</div></article><article class="node"><div class="label">{{node_6_type}}</div><div class="title">{{node_6}}</div><div class="meta">{{node_6_owner}}</div></article><div class="arrow a1">-></div><div class="arrow a2">-></div><div class="arrow a3">-></div><div class="arrow a4">-></div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/design-system-audit.html

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <title>Design System Audit Wireframe</title>
    <style>
      :root { --bg:#11100e; --panel:#1c1915; --ink:#f6f0e6; --muted:#b8aa99; --line:#39332b; --accent:#f2613f; --ok:#55c2a2; --warn:#f2cb57; }
      body { margin:0; background:var(--bg); color:var(--ink); font-family:Inter, Arial, sans-serif; }
      .slide { width:1280px; height:720px; box-sizing:border-box; padding:48px; display:grid; grid-template-rows:auto 1fr; gap:28px; }
      h1 { margin:0; font-size:44px; line-height:1.05; max-width:900px; }
      .audit { display:grid; grid-template-columns:1fr 1fr; gap:18px; }
      .panel { border:1px solid var(--line); background:var(--panel); border-radius:8px; padding:22px; }
      .panel h2 { margin:0 0 18px; font-size:24px; }
      .score-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }
      .score { border:1px solid var(--line); border-radius:7px; padding:16px; }
      .score .label { color:var(--muted); font-size:12px; letter-spacing:.12em; text-transform:uppercase; }
      .score .value { font-size:42px; font-weight:850; color:var(--accent); margin-top:12px; }
      .bars { display:grid; gap:14px; }
      .row { display:grid; grid-template-columns:180px 1fr 48px; gap:12px; align-items:center; }
      .track { height:10px; background:#0d0c0b; border:1px solid var(--line); }
      .fill { height:100%; background:var(--ok); }
      .risk { color:var(--warn); }
    </style>
  </head>
  <body>
    <main class="slide">
      <h1>{{action_title}}</h1>
      <section class="audit">
        <article class="panel"><h2>{{summary_title}}</h2><div class="score-grid"><div class="score"><div class="label">Tokens</div><div class="value">{{token_score}}</div></div><div class="score"><div class="label">Templates</div><div class="value">{{template_score}}</div></div><div class="score"><div class="label">QA</div><div class="value">{{qa_score}}</div></div></div></article>
        <article class="panel"><h2>{{gap_title}}</h2><div class="bars"><div class="row"><strong>{{gap_1}}</strong><div class="track"><div class="fill" style="width:{{gap_1_width}}%"></div></div><span>{{gap_1_score}}</span></div><div class="row"><strong>{{gap_2}}</strong><div class="track"><div class="fill" style="width:{{gap_2_width}}%"></div></div><span>{{gap_2_score}}</span></div><div class="row"><strong>{{gap_3}}</strong><div class="track"><div class="fill" style="width:{{gap_3_width}}%"></div></div><span>{{gap_3_score}}</span></div><div class="row risk"><strong>{{risk_label}}</strong><span>{{risk_note}}</span><span>{{risk_score}}</span></div></div></article>
      </section>
    </main>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/executive-summary.html

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <title>Executive Summary Wireframe</title>
    <style>
      :root { --bg:#f7f7f4; --ink:#171717; --muted:#666a70; --line:#d7d7d0; --accent:#2457d6; }
      body { margin:0; background:var(--bg); color:var(--ink); font-family:Inter, Arial, sans-serif; }
      .slide { width:1280px; height:720px; box-sizing:border-box; padding:56px; display:grid; grid-template-rows:auto 1fr auto; gap:28px; }
      header { display:grid; grid-template-columns:1fr auto; gap:32px; align-items:start; border-bottom:1px solid var(--line); padding-bottom:24px; }
      h1 { margin:0; font-size:48px; line-height:1.02; max-width:840px; }
      .status { color:var(--accent); font-weight:800; font-size:18px; letter-spacing:.08em; text-transform:uppercase; }
      .grid { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; }
      .card { background:white; border:1px solid var(--line); border-radius:8px; padding:22px; min-height:140px; }
      .label { color:var(--muted); font-size:13px; letter-spacing:.08em; text-transform:uppercase; }
      .metric { font-size:44px; font-weight:850; margin-top:18px; }
      .delta { color:var(--accent); font-weight:700; margin-top:10px; }
      footer { display:grid; grid-template-columns:2fr 1fr; gap:24px; font-size:22px; }
      .decision { border-left:4px solid var(--accent); padding-left:18px; font-weight:750; }
      .source { color:var(--muted); font-size:15px; align-self:end; text-align:right; }
    </style>
  </head>
  <body>
    <main class="slide">
      <header>
        <h1>{{headline_answer}}</h1>
        <div class="status">{{status_label}}</div>
      </header>
      <section class="grid">
        <article class="card"><div class="label">{{metric_1_label}}</div><div class="metric">{{metric_1_value}}</div><div class="delta">{{metric_1_delta}}</div></article>
        <article class="card"><div class="label">{{metric_2_label}}</div><div class="metric">{{metric_2_value}}</div><div class="delta">{{metric_2_delta}}</div></article>
        <article class="card"><div class="label">{{metric_3_label}}</div><div class="metric">{{metric_3_value}}</div><div class="delta">{{metric_3_delta}}</div></article>
        <article class="card"><div class="label">{{metric_4_label}}</div><div class="metric">{{metric_4_value}}</div><div class="delta">{{metric_4_delta}}</div></article>
      </section>
      <footer>
        <div class="decision">{{decision_signal}}</div>
        <div class="source">{{source_note}}</div>
      </footer>
    </main>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/experiment-grid.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Experiment Grid</title><style>body{margin:0;background:#08111f;color:#eaf2ff;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr;gap:24px}h1{margin:0;font-size:42px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.card{background:#111c2e;border:1px solid #26364f;border-radius:8px;padding:22px}.hyp{color:#38bdf8;font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:900}.title{font-size:24px;font-weight:900;margin-top:12px}.result{font-size:36px;font-weight:900;color:#34d399;margin-top:18px}.decision{color:#9bafcc;margin-top:12px;line-height:1.4}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="grid"><article class="card"><div class="hyp">Hipótese</div><div class="title">{{hypothesis_1}}</div><div class="result">{{result_1}}</div><div class="decision">{{decision_1}}</div></article><article class="card"><div class="hyp">Hipótese</div><div class="title">{{hypothesis_2}}</div><div class="result">{{result_2}}</div><div class="decision">{{decision_2}}</div></article><article class="card"><div class="hyp">Hipótese</div><div class="title">{{hypothesis_3}}</div><div class="result">{{result_3}}</div><div class="decision">{{decision_3}}</div></article></section></main></body></html>
```


## Referência: references/source/templates/wireframes/feature-matrix.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Feature Matrix</title><style>body{margin:0;background:#fff;color:#151515;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:24px}h1{margin:0;font-size:42px}.matrix{display:grid;grid-template-columns:1.5fr repeat(4,1fr);border:1px solid #d9d9d2}.cell{padding:16px;border-right:1px solid #d9d9d2;border-bottom:1px solid #d9d9d2;background:white;text-align:center}.feature{text-align:left}.head{background:#151515;color:white;font-size:12px;text-transform:uppercase;letter-spacing:.1em;font-weight:900}.yes{color:#168a4a;font-size:28px;font-weight:900}.no{color:#b42318;font-size:28px;font-weight:900}.partial{color:#f0b35a;font-size:28px;font-weight:900}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="matrix"><div class="cell head">Feature</div><div class="cell head">{{plan_1}}</div><div class="cell head">{{plan_2}}</div><div class="cell head">{{plan_3}}</div><div class="cell head">{{plan_4}}</div><div class="cell feature">{{feature_1}}</div><div class="cell yes">{{p1_f1}}</div><div class="cell yes">{{p2_f1}}</div><div class="cell no">{{p3_f1}}</div><div class="cell partial">{{p4_f1}}</div><div class="cell feature">{{feature_2}}</div><div class="cell no">{{p1_f2}}</div><div class="cell yes">{{p2_f2}}</div><div class="cell yes">{{p3_f2}}</div><div class="cell partial">{{p4_f2}}</div><div class="cell feature">{{feature_3}}</div><div class="cell partial">{{p1_f3}}</div><div class="cell yes">{{p2_f3}}</div><div class="cell yes">{{p3_f3}}</div><div class="cell yes">{{p4_f3}}</div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/financial-waterfall.html

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <title>Financial Waterfall Wireframe</title>
    <style>
      :root { --bg:#ffffff; --ink:#151515; --muted:#666; --line:#d9d9d2; --blue:#2347ff; --green:#168a4a; --red:#b42318; }
      body { margin:0; background:var(--bg); color:var(--ink); font-family:Inter, Arial, sans-serif; }
      .slide { width:1280px; height:720px; box-sizing:border-box; padding:56px; display:grid; grid-template-rows:auto 1fr auto; gap:28px; }
      header { display:grid; grid-template-columns:1fr 280px; gap:32px; }
      h1 { margin:0; font-size:44px; line-height:1.05; }
      .callout { border-left:4px solid var(--blue); padding-left:18px; color:var(--muted); font-size:19px; line-height:1.35; }
      .chart { display:grid; grid-template-columns:repeat(7,1fr); align-items:end; gap:18px; border-bottom:2px solid var(--line); padding-top:30px; }
      .bar-wrap { display:grid; gap:10px; align-items:end; height:360px; }
      .bar { width:100%; background:var(--blue); min-height:34px; }
      .bar.pos { background:var(--green); }
      .bar.neg { background:var(--red); }
      .value { font-weight:850; font-size:24px; }
      .label { color:var(--muted); font-size:14px; line-height:1.2; min-height:36px; }
      footer { display:grid; grid-template-columns:1fr auto; color:var(--muted); font-size:16px; }
    </style>
  </head>
  <body>
    <main class="slide">
      <header><h1>{{action_title}}</h1><div class="callout">{{variance_explanation}}</div></header>
      <section class="chart">
        <div class="bar-wrap"><div class="value">{{start_value}}</div><div class="bar" style="height:{{start_height}}px"></div><div class="label">{{start_label}}</div></div>
        <div class="bar-wrap"><div class="value">{{change_1_value}}</div><div class="bar pos" style="height:{{change_1_height}}px"></div><div class="label">{{change_1_label}}</div></div>
        <div class="bar-wrap"><div class="value">{{change_2_value}}</div><div class="bar neg" style="height:{{change_2_height}}px"></div><div class="label">{{change_2_label}}</div></div>
        <div class="bar-wrap"><div class="value">{{change_3_value}}</div><div class="bar pos" style="height:{{change_3_height}}px"></div><div class="label">{{change_3_label}}</div></div>
        <div class="bar-wrap"><div class="value">{{change_4_value}}</div><div class="bar neg" style="height:{{change_4_height}}px"></div><div class="label">{{change_4_label}}</div></div>
        <div class="bar-wrap"><div class="value">{{change_5_value}}</div><div class="bar pos" style="height:{{change_5_height}}px"></div><div class="label">{{change_5_label}}</div></div>
        <div class="bar-wrap"><div class="value">{{end_value}}</div><div class="bar" style="height:{{end_height}}px"></div><div class="label">{{end_label}}</div></div>
      </section>
      <footer><span>{{source_note}}</span><strong>{{decision_ask}}</strong></footer>
    </main>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/gallery.html

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <title>Slide Creator Wireframe Gallery</title>
    <style>
      body { margin: 0; background: #050505; color: #f5f5ef; font: 16px Inter, Arial, sans-serif; }
      main { padding: 32px; display: grid; gap: 24px; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); }
      .frame { aspect-ratio: 16 / 9; border: 1px solid #2a2a2a; background: #111; padding: 24px; display: grid; gap: 16px; }
      .title { font-size: 22px; font-weight: 800; }
      .muted { color: #aaa; font-size: 13px; }
      .bar { height: 14px; background: #d7ff3f; }
      .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
      .card { border: 1px solid #333; padding: 12px; background: #171717; }
      .matrix { display: grid; grid-template-columns: 110px repeat(3, 1fr); gap: 1px; background: #333; }
      .matrix div { background: #111; padding: 8px; min-height: 44px; }
      .accent { background: #d7ff3f !important; color: #111; font-weight: 800; }
      .flow { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; align-items: center; }
      .step { border: 1px solid #444; padding: 12px; min-height: 70px; }
    </style>
  </head>
  <body>
    <main>
      <section class="frame">
        <div class="muted">hook_hero_claim</div>
        <div class="title">A tese do deck precisa caber em uma frase defensável.</div>
        <div class="bar" style="width: 55%"></div>
      </section>
      <section class="frame">
        <div class="muted">comparison_matrix</div>
        <div class="matrix">
          <div></div><div>A</div><div>B</div><div>C</div>
          <div>Critério 1</div><div class="accent">95</div><div>72</div><div>61</div>
          <div>Critério 2</div><div>80</div><div class="accent">93</div><div>44</div>
          <div>Critério 3</div><div>65</div><div>71</div><div class="accent">88</div>
        </div>
        <div class="muted">Detalhe de célula vai em painel/appendix, não repetido dentro da matriz.</div>
      </section>
      <section class="frame">
        <div class="muted">mechanism_layered_system</div>
        <div class="grid">
          <div class="card">Camada 1<br><span class="muted">Entrada</span></div>
          <div class="card">Camada 2<br><span class="muted">Processamento</span></div>
          <div class="card">Camada 3<br><span class="muted">Decisão</span></div>
          <div class="card accent">Resultado<br><span>Por que funciona</span></div>
        </div>
      </section>
      <section class="frame">
        <div class="muted">pipeline_with_stages</div>
        <div class="flow">
          <div class="step">Briefing<br><span class="muted">input</span></div>
          <div class="step">Tese<br><span class="muted">claim</span></div>
          <div class="step">Slides<br><span class="muted">spec</span></div>
          <div class="step accent">QA<br><span>gate</span></div>
        </div>
      </section>
    </main>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/harvey-balls-table.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Harvey Balls Table</title><style>body{margin:0;background:#090a0b;color:#f3f1e8;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr;gap:24px}h1{margin:0;font-size:42px}.matrix{display:grid;grid-template-columns:1.5fr repeat(4,1fr);border:1px solid #2d3138}.cell{padding:16px;border-right:1px solid #2d3138;border-bottom:1px solid #2d3138;background:#14161a;text-align:center}.dim{text-align:left}.head{background:#b6f04a;color:#090a0b;font-size:12px;text-transform:uppercase;letter-spacing:.1em;font-weight:900}.ball{font-size:30px;color:#b6f04a}.muted{color:#a4a09a}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="matrix"><div class="cell head">Dimensão</div><div class="cell head">{{player_1}}</div><div class="cell head">{{player_2}}</div><div class="cell head">{{player_3}}</div><div class="cell head">{{player_4}}</div><div class="cell dim">{{dimension_1}}</div><div class="cell ball">{{p1_d1}}</div><div class="cell ball">{{p2_d1}}</div><div class="cell ball">{{p3_d1}}</div><div class="cell ball">{{p4_d1}}</div><div class="cell dim">{{dimension_2}}</div><div class="cell ball">{{p1_d2}}</div><div class="cell ball">{{p2_d2}}</div><div class="cell ball">{{p3_d2}}</div><div class="cell ball">{{p4_d2}}</div><div class="cell dim">{{dimension_3}}</div><div class="cell ball">{{p1_d3}}</div><div class="cell ball">{{p2_d3}}</div><div class="cell ball">{{p3_d3}}</div><div class="cell ball">{{p4_d3}}</div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/hiring-scorecard.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Hiring Scorecard</title><style>body{margin:0;background:#f8f9fb;color:#172033;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:26px}h1{margin:0;font-size:44px}.table{display:grid;grid-template-columns:1.2fr 1fr 1fr 120px;border:1px solid #d9dfea}.cell{padding:18px;border-right:1px solid #d9dfea;border-bottom:1px solid #d9dfea;background:white}.head{background:#172033;color:white;text-transform:uppercase;letter-spacing:.1em;font-size:12px;font-weight:900}.score{font-size:30px;font-weight:900;color:#1849a9}.evidence{color:#667085}</style></head><body><main class="slide"><h1>{{role_mission}}</h1><section class="table"><div class="cell head">Critério</div><div class="cell head">Evidência</div><div class="cell head">Sinal forte</div><div class="cell head">Score</div><div class="cell">{{criterion_1}}</div><div class="cell evidence">{{evidence_1}}</div><div class="cell">{{signal_1}}</div><div class="cell score">{{score_1}}</div><div class="cell">{{criterion_2}}</div><div class="cell evidence">{{evidence_2}}</div><div class="cell">{{signal_2}}</div><div class="cell score">{{score_2}}</div><div class="cell">{{criterion_3}}</div><div class="cell evidence">{{evidence_3}}</div><div class="cell">{{signal_3}}</div><div class="cell score">{{score_3}}</div><div class="cell">{{criterion_4}}</div><div class="cell evidence">{{evidence_4}}</div><div class="cell">{{signal_4}}</div><div class="cell score">{{score_4}}</div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/incident-timeline.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Incident Timeline</title><style>body{margin:0;background:#05070a;color:#eef6ff;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr auto;gap:28px}h1{margin:0;font-size:44px}.events{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;align-items:stretch}.event{border:1px solid #263241;background:#10151d;border-radius:8px;padding:20px}.time{color:#00e5a8;font-size:18px;font-weight:900}.title{font-size:24px;font-weight:900;margin-top:16px}.impact{color:#9aabbc;margin-top:14px;line-height:1.4}.fix{border-left:5px solid #00e5a8;padding-left:18px;font-weight:850;font-size:22px}</style></head><body><main class="slide"><h1>{{incident_summary}}</h1><section class="events"><article class="event"><div class="time">{{time_1}}</div><div class="title">{{event_1}}</div><div class="impact">{{impact_1}}</div></article><article class="event"><div class="time">{{time_2}}</div><div class="title">{{event_2}}</div><div class="impact">{{impact_2}}</div></article><article class="event"><div class="time">{{time_3}}</div><div class="title">{{event_3}}</div><div class="impact">{{impact_3}}</div></article><article class="event"><div class="time">{{time_4}}</div><div class="title">{{event_4}}</div><div class="impact">{{impact_4}}</div></article><article class="event"><div class="time">{{time_5}}</div><div class="title">{{event_5}}</div><div class="impact">{{impact_5}}</div></article></section><footer class="fix">{{corrective_action}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/launch-calendar.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Launch Calendar</title><style>body{margin:0;background:#0d0f14;color:#f8fafc;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr;gap:28px}h1{margin:0;font-size:44px}.calendar{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.week{border:1px solid #2b3140;background:#171a22;border-radius:8px;padding:20px}.date{color:#ff6b35;font-size:13px;letter-spacing:.12em;text-transform:uppercase;font-weight:900}.milestone{font-size:25px;font-weight:900;margin-top:14px}.asset{color:#aeb7c7;margin-top:14px;line-height:1.4}.owner{border-top:1px solid #2b3140;margin-top:18px;padding-top:14px;color:#00c2a8;font-weight:800}</style></head><body><main class="slide"><h1>{{launch_thesis}}</h1><section class="calendar"><article class="week"><div class="date">{{date_1}}</div><div class="milestone">{{milestone_1}}</div><div class="asset">{{asset_1}}</div><div class="owner">{{owner_1}}</div></article><article class="week"><div class="date">{{date_2}}</div><div class="milestone">{{milestone_2}}</div><div class="asset">{{asset_2}}</div><div class="owner">{{owner_2}}</div></article><article class="week"><div class="date">{{date_3}}</div><div class="milestone">{{milestone_3}}</div><div class="asset">{{asset_3}}</div><div class="owner">{{owner_3}}</div></article><article class="week"><div class="date">{{date_4}}</div><div class="milestone">{{milestone_4}}</div><div class="asset">{{asset_4}}</div><div class="owner">{{owner_4}}</div></article></section></main></body></html>
```


## Referência: references/source/templates/wireframes/maturity-ladder.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Maturity Ladder</title><style>body{margin:0;background:#f8fafc;color:#101828;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:30px}h1{margin:0;font-size:44px}.ladder{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;align-items:end}.stage{background:white;border:1px solid #d0d5dd;border-radius:8px;padding:20px}.stage:nth-child(1){height:210px}.stage:nth-child(2){height:250px}.stage:nth-child(3){height:290px;border-color:#155eef}.stage:nth-child(4){height:330px}.stage:nth-child(5){height:370px}.level{color:#155eef;font-weight:900}.title{font-size:24px;font-weight:900;margin-top:14px}.desc{color:#667085;margin-top:12px;line-height:1.4}.marker{margin-top:16px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="ladder"><article class="stage"><div class="level">L1</div><div class="title">{{stage_1}}</div><div class="desc">{{stage_1_desc}}</div><div class="marker">{{stage_1_marker}}</div></article><article class="stage"><div class="level">L2</div><div class="title">{{stage_2}}</div><div class="desc">{{stage_2_desc}}</div><div class="marker">{{stage_2_marker}}</div></article><article class="stage"><div class="level">L3</div><div class="title">{{stage_3}}</div><div class="desc">{{stage_3_desc}}</div><div class="marker">{{stage_3_marker}}</div></article><article class="stage"><div class="level">L4</div><div class="title">{{stage_4}}</div><div class="desc">{{stage_4_desc}}</div><div class="marker">{{stage_4_marker}}</div></article><article class="stage"><div class="level">L5</div><div class="title">{{stage_5}}</div><div class="desc">{{stage_5_desc}}</div><div class="marker">{{stage_5_marker}}</div></article></section></main></body></html>
```


## Referência: references/source/templates/wireframes/mechanism-map.html

```html
<!doctype html>
<html lang="pt-BR">
  <head><meta charset="utf-8"><title>Mechanism Map</title></head>
  <body style="margin:0;background:#050505;color:#f5f5ef;font-family:Inter,Arial,sans-serif">
    <section style="padding:48px">
      <p style="color:#d7ff3f;text-transform:uppercase;font:12px monospace">mechanism_layered_system</p>
      <h1 style="font-size:36px;max-width:900px">O slide de mecanismo explica por que o resultado acontece.</h1>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:34px">
        <div style="border:1px solid #333;padding:18px;background:#111">Entrada<br><span style="color:#999">material bruto</span></div>
        <div style="border:1px solid #333;padding:18px;background:#111">Decisão<br><span style="color:#999">template certo</span></div>
        <div style="border:1px solid #333;padding:18px;background:#111">Execução<br><span style="color:#999">slide spec</span></div>
        <div style="border:1px solid #d7ff3f;padding:18px;background:#d7ff3f;color:#111;font-weight:800">Resultado<br><span>deck melhor</span></div>
      </div>
    </section>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/mission-vision.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Mission Vision</title><style>body{margin:0;background:#faf7f2;color:#17120f;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:60px;display:grid;grid-template-rows:auto 1fr;gap:30px}h1{margin:0;font-size:42px}.cards{display:grid;grid-template-columns:1fr 1fr;gap:20px}.card{background:white;border:1px solid #e5d8c8;border-radius:8px;padding:34px}.label{color:#d946ef;font-size:13px;text-transform:uppercase;letter-spacing:.14em;font-weight:900}.statement{font-size:42px;font-weight:900;line-height:1.08;margin-top:18px}.principles{grid-column:1/3;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.principle{background:#17120f;color:#fff;border-radius:8px;padding:18px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="cards"><article class="card"><div class="label">Missão</div><div class="statement">{{mission}}</div></article><article class="card"><div class="label">Visão</div><div class="statement">{{vision}}</div></article><div class="principles"><div class="principle">{{principle_1}}</div><div class="principle">{{principle_2}}</div><div class="principle">{{principle_3}}</div></div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/moodboard-grid.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Moodboard Grid</title><style>body{margin:0;background:#faf7f2;color:#17120f;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr auto;gap:22px}h1{margin:0;font-size:42px}.grid{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(2,1fr);gap:12px}.tile{border:1px solid #e5d8c8;border-radius:8px;background:linear-gradient(135deg,#d946ef,#f97316);padding:16px;color:white;font-weight:900;display:flex;align-items:end}.t2{background:linear-gradient(135deg,#0ea5e9,#d946ef)}.t3{background:linear-gradient(135deg,#17120f,#756b61)}.t4{background:linear-gradient(135deg,#f97316,#facc15)}.rule{border-left:5px solid #d946ef;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{visual_direction}}</h1><section class="grid"><div class="tile">{{tile_1}}</div><div class="tile t2">{{tile_2}}</div><div class="tile t3">{{tile_3}}</div><div class="tile t4">{{tile_4}}</div><div class="tile t3">{{tile_5}}</div><div class="tile">{{tile_6}}</div><div class="tile t4">{{tile_7}}</div><div class="tile t2">{{tile_8}}</div></section><footer class="rule">{{design_rule}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/objection-matrix.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Objection Matrix</title><style>body{margin:0;background:#15110f;color:#fff7ed;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr;gap:24px}h1{margin:0;font-size:42px}.table{display:grid;grid-template-columns:1fr 1.2fr 1fr;border:1px solid #3a302a}.cell{padding:18px;border-right:1px solid #3a302a;border-bottom:1px solid #3a302a;background:#211b18}.head{background:#ff7a1a;color:#15110f;text-transform:uppercase;letter-spacing:.12em;font-size:12px;font-weight:900}.proof{color:#facc15;font-weight:800}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="table"><div class="cell head">Objeção</div><div class="cell head">Resposta</div><div class="cell head">Prova</div><div class="cell">{{objection_1}}</div><div class="cell">{{response_1}}</div><div class="cell proof">{{proof_1}}</div><div class="cell">{{objection_2}}</div><div class="cell">{{response_2}}</div><div class="cell proof">{{proof_2}}</div><div class="cell">{{objection_3}}</div><div class="cell">{{response_3}}</div><div class="cell proof">{{proof_3}}</div><div class="cell">{{objection_4}}</div><div class="cell">{{response_4}}</div><div class="cell proof">{{proof_4}}</div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/org-chart.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Org Chart</title><style>body{margin:0;background:#f8f9fb;color:#172033;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:26px}h1{margin:0;font-size:42px}.org{display:grid;grid-template-rows:120px 150px 150px;gap:18px;justify-items:center}.row{display:flex;gap:18px}.box{background:white;border:1px solid #d9dfea;border-radius:8px;padding:20px;min-width:210px;text-align:center}.role{font-size:24px;font-weight:900}.owner{color:#667085;margin-top:8px}.top{border-color:#1849a9;border-width:3px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="org"><div class="row"><div class="box top"><div class="role">{{leader_role}}</div><div class="owner">{{leader_owner}}</div></div></div><div class="row"><div class="box"><div class="role">{{role_1}}</div><div class="owner">{{owner_1}}</div></div><div class="box"><div class="role">{{role_2}}</div><div class="owner">{{owner_2}}</div></div><div class="box"><div class="role">{{role_3}}</div><div class="owner">{{owner_3}}</div></div></div><div class="row"><div class="box"><div class="role">{{role_4}}</div><div class="owner">{{owner_4}}</div></div><div class="box"><div class="role">{{role_5}}</div><div class="owner">{{owner_5}}</div></div></div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/persona-fit-matrix.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Persona Fit Matrix</title><style>body{margin:0;background:#f8fafc;color:#101828;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:26px}h1{margin:0;font-size:42px}.matrix{display:grid;grid-template-columns:220px repeat(4,1fr);border:1px solid #d0d5dd}.cell{padding:18px;border-right:1px solid #d0d5dd;border-bottom:1px solid #d0d5dd;background:white}.head{background:#155eef;color:white;font-weight:900;text-transform:uppercase;letter-spacing:.08em;font-size:12px}.winner{font-size:24px;font-weight:900;color:#155eef}.note{color:#667085;margin-top:8px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="matrix"><div class="cell head">Persona</div><div class="cell head">{{criterion_1}}</div><div class="cell head">{{criterion_2}}</div><div class="cell head">{{criterion_3}}</div><div class="cell head">Melhor escolha</div><div class="cell">{{persona_1}}</div><div class="cell">{{p1_c1}}</div><div class="cell">{{p1_c2}}</div><div class="cell">{{p1_c3}}</div><div class="cell"><div class="winner">{{p1_winner}}</div><div class="note">{{p1_reason}}</div></div><div class="cell">{{persona_2}}</div><div class="cell">{{p2_c1}}</div><div class="cell">{{p2_c2}}</div><div class="cell">{{p2_c3}}</div><div class="cell"><div class="winner">{{p2_winner}}</div><div class="note">{{p2_reason}}</div></div><div class="cell">{{persona_3}}</div><div class="cell">{{p3_c1}}</div><div class="cell">{{p3_c2}}</div><div class="cell">{{p3_c3}}</div><div class="cell"><div class="winner">{{p3_winner}}</div><div class="note">{{p3_reason}}</div></div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/portfolio-allocation.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Portfolio Allocation</title><style>body{margin:0;background:#fff;color:#151515;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:56px;display:grid;grid-template-rows:auto 1fr auto;gap:28px}h1{margin:0;font-size:42px}.split{display:grid;grid-template-columns:1.1fr .9fr;gap:30px}.bar{height:72px;display:flex;border:1px solid #d9d9d2}.seg{display:grid;place-items:center;color:white;font-weight:900}.list{display:grid;gap:14px}.item{display:grid;grid-template-columns:80px 1fr;gap:16px;align-items:start}.pct{font-size:32px;font-weight:900;color:#2347ff}.why{color:#666;line-height:1.35}.tradeoff{border-left:5px solid #b42318;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="split"><div><div class="bar"><div class="seg" style="width:{{pct_1}}%;background:#2347ff">{{pct_1}}%</div><div class="seg" style="width:{{pct_2}}%;background:#168a4a">{{pct_2}}%</div><div class="seg" style="width:{{pct_3}}%;background:#f0b35a">{{pct_3}}%</div><div class="seg" style="width:{{pct_4}}%;background:#777">{{pct_4}}%</div></div></div><div class="list"><div class="item"><div class="pct">{{pct_1}}%</div><div class="why">{{cat_1}} — {{why_1}}</div></div><div class="item"><div class="pct">{{pct_2}}%</div><div class="why">{{cat_2}} — {{why_2}}</div></div><div class="item"><div class="pct">{{pct_3}}%</div><div class="why">{{cat_3}} — {{why_3}}</div></div><div class="item"><div class="pct">{{pct_4}}%</div><div class="why">{{cat_4}} — {{why_4}}</div></div></div></section><footer class="tradeoff">{{tradeoff_note}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/pricing-table.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Pricing Table</title><style>body{margin:0;background:#f8f9fb;color:#172033;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:28px}h1{margin:0;font-size:44px}.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.tier{background:white;border:1px solid #d9dfea;border-radius:8px;padding:26px;display:grid;gap:18px}.tier.best{border:3px solid #1849a9}.label{color:#1849a9;font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:850}.price{font-size:52px;font-weight:900}.fit{color:#667085;font-size:18px}ul{margin:0;padding-left:20px;line-height:1.5;font-size:18px}.cta{border-top:1px solid #d9dfea;padding-top:16px;font-weight:800}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="tiers"><article class="tier"><div class="label">{{tier_1_label}}</div><div class="price">{{tier_1_price}}</div><div class="fit">{{tier_1_fit}}</div><ul><li>{{tier_1_item_1}}</li><li>{{tier_1_item_2}}</li><li>{{tier_1_item_3}}</li></ul><div class="cta">{{tier_1_cta}}</div></article><article class="tier best"><div class="label">Recomendado</div><div class="price">{{tier_2_price}}</div><div class="fit">{{tier_2_fit}}</div><ul><li>{{tier_2_item_1}}</li><li>{{tier_2_item_2}}</li><li>{{tier_2_item_3}}</li></ul><div class="cta">{{tier_2_cta}}</div></article><article class="tier"><div class="label">{{tier_3_label}}</div><div class="price">{{tier_3_price}}</div><div class="fit">{{tier_3_fit}}</div><ul><li>{{tier_3_item_1}}</li><li>{{tier_3_item_2}}</li><li>{{tier_3_item_3}}</li></ul><div class="cta">{{tier_3_cta}}</div></article></section></main></body></html>
```


## Referência: references/source/templates/wireframes/proof-stack.html

```html
<!doctype html>
<html lang="pt-BR">
  <head><meta charset="utf-8"><title>Proof Stack</title></head>
  <body style="margin:0;background:#fafaf7;color:#151515;font-family:Inter,Arial,sans-serif">
    <section style="padding:48px">
      <p style="font:12px monospace;text-transform:uppercase;color:#2347ff">proof_before_after</p>
      <h1 style="font-size:34px">Prova boa mostra mudança, fonte e implicação.</h1>
      <div style="display:grid;grid-template-columns:1fr 1fr 260px;gap:20px;margin-top:28px">
        <div style="border:1px solid #ddd;padding:20px;background:white"><b>Antes</b><p>Estado inicial observável.</p></div>
        <div style="border:1px solid #ddd;padding:20px;background:white"><b>Depois</b><p>Resultado mensurável.</p></div>
        <div style="border:1px solid #2347ff;padding:20px;background:#eef1ff"><b>Fonte</b><p>Artefato, caminho, demo ou premissa.</p></div>
      </div>
    </section>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/quote-evidence-panel.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Quote Evidence Panel</title><style>body{margin:0;background:#ffffff;color:#1a1d21;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:64px;display:grid;grid-template-columns:1fr 360px;gap:46px;align-items:center}.quote{font-family:Georgia,serif;font-size:58px;line-height:1.05}.quote:before{content:'“';color:#2f6fed}.side{border-left:4px solid #2f6fed;padding-left:24px}.label{color:#626a73;text-transform:uppercase;letter-spacing:.12em;font-size:12px;font-weight:900}.source{font-size:24px;font-weight:900;margin-top:18px}.implication{color:#626a73;font-size:20px;line-height:1.4;margin-top:26px}</style></head><body><main class="slide"><section class="quote">{{quote}}</section><aside class="side"><div class="label">Fonte</div><div class="source">{{attribution}}</div><div class="implication">{{implication}}</div></aside></main></body></html>
```


## Referência: references/source/templates/wireframes/responsibility-matrix.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Responsibility Matrix</title><style>body{margin:0;background:#f8f9fb;color:#172033;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:24px}h1{margin:0;font-size:42px}.matrix{display:grid;grid-template-columns:1.4fr repeat(4,1fr);border:1px solid #d9dfea}.cell{background:white;padding:18px;border-right:1px solid #d9dfea;border-bottom:1px solid #d9dfea;text-align:center}.task{text-align:left;font-weight:850}.head{background:#1849a9;color:white;font-size:12px;text-transform:uppercase;letter-spacing:.1em;font-weight:900}.r{font-size:26px;font-weight:900;color:#1849a9}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="matrix"><div class="cell head">Responsabilidade</div><div class="cell head">{{role_1}}</div><div class="cell head">{{role_2}}</div><div class="cell head">{{role_3}}</div><div class="cell head">{{role_4}}</div><div class="cell task">{{task_1}}</div><div class="cell r">{{r1_1}}</div><div class="cell r">{{r1_2}}</div><div class="cell r">{{r1_3}}</div><div class="cell r">{{r1_4}}</div><div class="cell task">{{task_2}}</div><div class="cell r">{{r2_1}}</div><div class="cell r">{{r2_2}}</div><div class="cell r">{{r2_3}}</div><div class="cell r">{{r2_4}}</div><div class="cell task">{{task_3}}</div><div class="cell r">{{r3_1}}</div><div class="cell r">{{r3_2}}</div><div class="cell r">{{r3_3}}</div><div class="cell r">{{r3_4}}</div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/risk-heatmap.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Risk Heatmap</title><style>body{margin:0;background:#090a0b;color:#f3f1e8;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr;gap:28px}h1{margin:0;font-size:44px}.grid{display:grid;grid-template-columns:170px repeat(3,1fr);grid-template-rows:repeat(4,1fr);gap:10px}.cell{border:1px solid #2d3138;background:#14161a;border-radius:8px;padding:16px}.axis{color:#a4a09a;text-transform:uppercase;letter-spacing:.12em;font-size:12px}.high{background:#421818}.mid{background:#403214}.low{background:#183426}.risk{font-weight:800;font-size:20px}.mitigation{color:#c9c3b7;margin-top:10px;font-size:15px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="grid"><div></div><div class="axis">Baixo impacto</div><div class="axis">Médio impacto</div><div class="axis">Alto impacto</div><div class="axis">Alta prob.</div><div class="cell mid"><div class="risk">{{risk_1}}</div><div class="mitigation">{{mitigation_1}}</div></div><div class="cell high"><div class="risk">{{risk_2}}</div><div class="mitigation">{{mitigation_2}}</div></div><div class="cell high"><div class="risk">{{risk_3}}</div><div class="mitigation">{{mitigation_3}}</div></div><div class="axis">Média prob.</div><div class="cell low"><div class="risk">{{risk_4}}</div><div class="mitigation">{{mitigation_4}}</div></div><div class="cell mid"><div class="risk">{{risk_5}}</div><div class="mitigation">{{mitigation_5}}</div></div><div class="cell high"><div class="risk">{{risk_6}}</div><div class="mitigation">{{mitigation_6}}</div></div><div class="axis">Baixa prob.</div><div class="cell low"><div class="risk">{{risk_7}}</div><div class="mitigation">{{mitigation_7}}</div></div><div class="cell low"><div class="risk">{{risk_8}}</div><div class="mitigation">{{mitigation_8}}</div></div><div class="cell mid"><div class="risk">{{risk_9}}</div><div class="mitigation">{{mitigation_9}}</div></div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/roadmap-decision.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Roadmap Decision</title><style>body{margin:0;background:#f8fafc;color:#101828;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.bets{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.bet{background:white;border:1px solid #d0d5dd;border-radius:8px;padding:20px}.chosen{border:3px solid #12b76a}.label{color:#155eef;font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:900}.title{font-size:24px;font-weight:900;margin-top:14px}.why{color:#667085;margin-top:12px;line-height:1.35}.defer{color:#d92d20;font-weight:850}.logic{border-left:5px solid #155eef;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="bets"><article class="bet chosen"><div class="label">Chosen</div><div class="title">{{bet_1}}</div><div class="why">{{why_1}}</div></article><article class="bet"><div class="label">Next</div><div class="title">{{bet_2}}</div><div class="why">{{why_2}}</div></article><article class="bet"><div class="label">Watch</div><div class="title">{{bet_3}}</div><div class="why">{{why_3}}</div></article><article class="bet"><div class="label defer">Deferred</div><div class="title">{{bet_4}}</div><div class="why">{{why_4}}</div></article></section><footer class="logic">{{sequencing_logic}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/roadmap-status.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Roadmap Status</title><style>body{margin:0;background:#f8fafc;color:#101828;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:24px}h1{margin:0;font-size:42px}.board{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.col{background:white;border:1px solid #d0d5dd;border-radius:8px;padding:18px}.head{font-size:13px;text-transform:uppercase;letter-spacing:.12em;font-weight:900;color:#155eef}.item{border-top:1px solid #eaecf0;padding-top:14px;margin-top:14px}.title{font-weight:900;font-size:20px}.meta{color:#667085;margin-top:8px}.blocked{color:#d92d20;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="board"><article class="col"><div class="head">On track</div><div class="item"><div class="title">{{on_track_1}}</div><div class="meta">{{on_track_1_owner}}</div></div><div class="item"><div class="title">{{on_track_2}}</div><div class="meta">{{on_track_2_owner}}</div></div></article><article class="col"><div class="head">At risk</div><div class="item"><div class="title">{{risk_1}}</div><div class="meta">{{risk_1_owner}}</div></div><div class="item"><div class="title">{{risk_2}}</div><div class="meta">{{risk_2_owner}}</div></div></article><article class="col"><div class="head">Blocked</div><div class="item"><div class="title blocked">{{blocked_1}}</div><div class="meta">{{blocked_1_reason}}</div></div><div class="item"><div class="title blocked">{{blocked_2}}</div><div class="meta">{{blocked_2_reason}}</div></div></article><article class="col"><div class="head">Done</div><div class="item"><div class="title">{{done_1}}</div><div class="meta">{{done_1_evidence}}</div></div><div class="item"><div class="title">{{done_2}}</div><div class="meta">{{done_2_evidence}}</div></div></article></section></main></body></html>
```


## Referência: references/source/templates/wireframes/sankey-flow.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Sankey Flow</title><style>body{margin:0;background:#f5f7fa;color:#121826;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:56px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.flow{display:grid;grid-template-columns:220px 1fr 220px;gap:20px;align-items:center}.node{background:white;border:1px solid #d8dee8;border-radius:8px;padding:20px;font-size:24px;font-weight:900}.streams{display:grid;gap:18px}.stream{height:42px;background:#0052cc;border-radius:999px;color:white;display:grid;place-items:center;font-weight:900}.s2{background:#00a76f;width:78%}.s3{background:#d92d20;width:48%}.note{border-left:5px solid #0052cc;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="flow"><div><div class="node">{{source_1}}</div><div class="node">{{source_2}}</div></div><div class="streams"><div class="stream">{{flow_1_value}}</div><div class="stream s2">{{flow_2_value}}</div><div class="stream s3">{{flow_3_value}}</div></div><div><div class="node">{{target_1}}</div><div class="node">{{target_2}}</div></div></section><footer class="note">{{flow_takeaway}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/scatter-plot.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Scatter Plot</title><style>body{margin:0;background:#fff;color:#151515;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:56px;display:grid;grid-template-rows:auto 1fr auto;gap:20px}h1{margin:0;font-size:42px}.plot{position:relative;border-left:2px solid #777;border-bottom:2px solid #777;background:linear-gradient(#eee 1px,transparent 1px),linear-gradient(90deg,#eee 1px,transparent 1px);background-size:120px 80px}.dot{position:absolute;width:20px;height:20px;border-radius:50%;background:#2347ff}.d1{left:18%;bottom:24%}.d2{left:42%;bottom:62%;background:#168a4a}.d3{left:72%;bottom:44%;background:#b42318}.d4{left:84%;bottom:78%;background:#f0b35a}.label{position:absolute;font-weight:900}.x{right:0;bottom:-34px}.y{left:-6px;top:-30px}.note{border-left:5px solid #2347ff;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="plot"><span class="dot d1"></span><span class="dot d2"></span><span class="dot d3"></span><span class="dot d4"></span><div class="label x">{{x_axis}}</div><div class="label y">{{y_axis}}</div></section><footer class="note">{{outlier_takeaway}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/scoring-rubric.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Scoring Rubric</title><style>body{margin:0;background:#090a0b;color:#f3f1e8;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.bands{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.band{border:1px solid #2d3138;background:#14161a;border-radius:8px;padding:18px}.range{color:#b6f04a;font-size:30px;font-weight:900}.label{font-size:22px;font-weight:850;margin-top:14px}.rule{color:#a4a09a;line-height:1.35;margin-top:12px}.formula{border-left:5px solid #b6f04a;padding-left:18px;font-size:20px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="bands"><article class="band"><div class="range">0-20</div><div class="label">{{band_1}}</div><div class="rule">{{rule_1}}</div></article><article class="band"><div class="range">21-49</div><div class="label">{{band_2}}</div><div class="rule">{{rule_2}}</div></article><article class="band"><div class="range">50-69</div><div class="label">{{band_3}}</div><div class="rule">{{rule_3}}</div></article><article class="band"><div class="range">70-84</div><div class="label">{{band_4}}</div><div class="rule">{{rule_4}}</div></article><article class="band"><div class="range">85-100</div><div class="label">{{band_5}}</div><div class="rule">{{rule_5}}</div></article></section><footer class="formula">{{score_formula}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/screen-sequence.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Screen Sequence</title><style>body{margin:0;background:#06070d;color:#f8fbff;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.screens{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.screen{border:1px solid #2b3147;background:#101322;border-radius:8px;padding:16px}.shot{height:250px;border:1px solid #2b3147;background:linear-gradient(135deg,#1b2240,#06070d);border-radius:6px;display:grid;place-items:center;color:#7cff6b;font-weight:900}.step{font-size:24px;font-weight:900;margin-top:16px}.note{color:#aab4c5;margin-top:8px}.proof{border-left:5px solid #7cff6b;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{demo_goal}}</h1><section class="screens"><article class="screen"><div class="shot">{{screen_1_label}}</div><div class="step">{{step_1}}</div><div class="note">{{note_1}}</div></article><article class="screen"><div class="shot">{{screen_2_label}}</div><div class="step">{{step_2}}</div><div class="note">{{note_2}}</div></article><article class="screen"><div class="shot">{{screen_3_label}}</div><div class="step">{{step_3}}</div><div class="note">{{note_3}}</div></article></section><footer class="proof">{{proof_moment}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/service-catalog.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Service Catalog</title><style>body{margin:0;background:#f8f9fb;color:#172033;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:24px}h1{margin:0;font-size:42px}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.service{background:white;border:1px solid #d9dfea;border-radius:8px;padding:22px}.label{color:#1849a9;font-size:12px;text-transform:uppercase;letter-spacing:.12em;font-weight:900}.name{font-size:24px;font-weight:900;margin-top:14px}.deliver{color:#667085;margin-top:12px;line-height:1.35}.fit{margin-top:18px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="grid"><article class="service"><div class="label">Serviço</div><div class="name">{{service_1}}</div><div class="deliver">{{deliverable_1}}</div><div class="fit">{{fit_1}}</div></article><article class="service"><div class="label">Serviço</div><div class="name">{{service_2}}</div><div class="deliver">{{deliverable_2}}</div><div class="fit">{{fit_2}}</div></article><article class="service"><div class="label">Serviço</div><div class="name">{{service_3}}</div><div class="deliver">{{deliverable_3}}</div><div class="fit">{{fit_3}}</div></article><article class="service"><div class="label">Serviço</div><div class="name">{{service_4}}</div><div class="deliver">{{deliverable_4}}</div><div class="fit">{{fit_4}}</div></article></section></main></body></html>
```


## Referência: references/source/templates/wireframes/social-proof-wall.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Social Proof Wall</title><style>body{margin:0;background:#fbfaf5;color:#111315;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.wall{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.logo{background:white;border:1px solid #ddd8cd;border-radius:8px;display:grid;place-items:center;font-size:28px;font-weight:900;color:#67615a;min-height:104px}.quote{border-left:5px solid #e5484d;padding-left:18px;font-size:22px;font-weight:850}.source{color:#67615a;font-size:15px}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="wall"><div class="logo">{{proof_1}}</div><div class="logo">{{proof_2}}</div><div class="logo">{{proof_3}}</div><div class="logo">{{proof_4}}</div><div class="logo">{{proof_5}}</div><div class="logo">{{proof_6}}</div><div class="logo">{{proof_7}}</div><div class="logo">{{proof_8}}</div></section><footer><div class="quote">{{relevance_note}}</div><div class="source">{{source_note}}</div></footer></main></body></html>
```


## Referência: references/source/templates/wireframes/survey-results.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Survey Results</title><style>body{margin:0;background:#08111f;color:#eaf2ff;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr auto;gap:26px}h1{margin:0;font-size:42px}.bars{display:grid;gap:14px}.row{display:grid;grid-template-columns:260px 1fr 80px;gap:18px;align-items:center}.track{height:28px;background:#111c2e;border:1px solid #26364f}.fill{height:100%;background:#38bdf8}.pct{font-size:28px;font-weight:900}.meta{color:#9bafcc}.insight{border-left:5px solid #38bdf8;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{question}}</h1><section class="bars"><div class="row"><strong>{{answer_1}}</strong><div class="track"><div class="fill" style="width:{{answer_1_pct}}%"></div></div><div class="pct">{{answer_1_pct}}%</div></div><div class="row"><strong>{{answer_2}}</strong><div class="track"><div class="fill" style="width:{{answer_2_pct}}%"></div></div><div class="pct">{{answer_2_pct}}%</div></div><div class="row"><strong>{{answer_3}}</strong><div class="track"><div class="fill" style="width:{{answer_3_pct}}%"></div></div><div class="pct">{{answer_3_pct}}%</div></div><div class="row"><strong>{{answer_4}}</strong><div class="track"><div class="fill" style="width:{{answer_4_pct}}%"></div></div><div class="pct">{{answer_4_pct}}%</div></div><div class="meta">{{sample_context}}</div></section><footer class="insight">{{interpretation}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/table-of-contents.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Table of Contents</title><style>body{margin:0;background:#090a0b;color:#f3f1e8;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:60px;display:grid;grid-template-columns:360px 1fr;gap:56px}.title{font-size:48px;font-weight:900}.flow{color:#a4a09a;font-size:20px;line-height:1.4;margin-top:22px}.toc{display:grid;gap:12px}.row{display:grid;grid-template-columns:70px 1fr;gap:20px;border-bottom:1px solid #2d3138;padding:18px 0}.num{color:#b6f04a;font-weight:900}.section{font-size:28px;font-weight:850}</style></head><body><main class="slide"><aside><div class="title">{{deck_title}}</div><div class="flow">{{flow_note}}</div></aside><section class="toc"><div class="row"><div class="num">01</div><div class="section">{{section_1}}</div></div><div class="row"><div class="num">02</div><div class="section">{{section_2}}</div></div><div class="row"><div class="num">03</div><div class="section">{{section_3}}</div></div><div class="row"><div class="num">04</div><div class="section">{{section_4}}</div></div><div class="row"><div class="num">05</div><div class="section">{{section_5}}</div></div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/team-credentials.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Team Credentials</title><style>body{margin:0;background:#f7f7f4;color:#171717;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr auto;gap:24px}h1{margin:0;font-size:42px}.team{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.member{background:white;border:1px solid #d7d7d0;border-radius:8px;padding:22px}.avatar{height:120px;background:#ecece7;border-radius:8px;display:grid;place-items:center;font-size:36px;font-weight:900;color:#2457d6}.name{font-size:24px;font-weight:900;margin-top:18px}.cred{color:#666a70;margin-top:10px;line-height:1.35}.why{border-left:5px solid #2457d6;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="team"><article class="member"><div class="avatar">{{initials_1}}</div><div class="name">{{member_1}}</div><div class="cred">{{credential_1}}</div></article><article class="member"><div class="avatar">{{initials_2}}</div><div class="name">{{member_2}}</div><div class="cred">{{credential_2}}</div></article><article class="member"><div class="avatar">{{initials_3}}</div><div class="name">{{member_3}}</div><div class="cred">{{credential_3}}</div></article><article class="member"><div class="avatar">{{initials_4}}</div><div class="name">{{member_4}}</div><div class="cred">{{credential_4}}</div></article></section><footer class="why">{{delivery_relevance}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/technical-architecture.html

```html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <title>Technical Architecture Wireframe</title>
    <style>
      :root { --bg:#071018; --panel:#0e1b26; --ink:#eaf6ff; --muted:#8ea5b6; --line:#233747; --accent:#51d6ff; --ok:#9bdb7b; }
      body { margin:0; background:var(--bg); color:var(--ink); font-family:Inter, Arial, sans-serif; }
      .slide { width:1280px; height:720px; box-sizing:border-box; padding:48px; display:grid; grid-template-rows:auto 1fr; gap:28px; }
      h1 { margin:0; font-size:42px; line-height:1.05; }
      .map { display:grid; grid-template-columns:260px 1fr 260px; gap:18px; align-items:stretch; }
      .lane { border:1px solid var(--line); background:var(--panel); border-radius:8px; padding:20px; display:grid; gap:16px; }
      .lane-title { color:var(--accent); letter-spacing:.12em; text-transform:uppercase; font-size:13px; font-weight:850; }
      .node { border:1px solid var(--line); border-radius:7px; padding:14px; background:#091722; }
      .node strong { display:block; font-size:18px; margin-bottom:6px; }
      .node span { color:var(--muted); font-size:14px; line-height:1.35; }
      .flow { display:grid; grid-template-rows:1fr auto 1fr; gap:20px; }
      .arrow { align-self:center; justify-self:center; color:var(--ok); font-size:18px; border-top:2px solid var(--ok); width:88%; text-align:center; padding-top:12px; }
      .decision { border-left:4px solid var(--accent); padding-left:16px; color:var(--ink); font-size:20px; line-height:1.3; }
    </style>
  </head>
  <body>
    <main class="slide">
      <h1>{{action_title}}</h1>
      <section class="map">
        <div class="lane"><div class="lane-title">{{left_boundary}}</div><div class="node"><strong>{{client_node}}</strong><span>{{client_note}}</span></div><div class="node"><strong>{{input_node}}</strong><span>{{input_note}}</span></div></div>
        <div class="flow"><div class="lane"><div class="lane-title">{{core_boundary}}</div><div class="node"><strong>{{core_node_1}}</strong><span>{{core_note_1}}</span></div><div class="node"><strong>{{core_node_2}}</strong><span>{{core_note_2}}</span></div></div><div class="arrow">{{critical_flow_label}}</div><div class="decision">{{architecture_decision}}</div></div>
        <div class="lane"><div class="lane-title">{{right_boundary}}</div><div class="node"><strong>{{provider_node}}</strong><span>{{provider_note}}</span></div><div class="node"><strong>{{storage_node}}</strong><span>{{storage_note}}</span></div></div>
      </section>
    </main>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/traceability-matrix.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Traceability Matrix</title><style>body{margin:0;background:#f9fafb;color:#111827;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:24px}h1{margin:0;font-size:42px}.table{display:grid;grid-template-columns:120px 1.4fr 1.2fr 1fr 120px;border:1px solid #d1d5db}.cell{background:white;padding:16px;border-right:1px solid #d1d5db;border-bottom:1px solid #d1d5db}.head{background:#1d4ed8;color:white;font-size:12px;text-transform:uppercase;letter-spacing:.1em;font-weight:900}.status{font-weight:900;color:#1d4ed8}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="table"><div class="cell head">ID</div><div class="cell head">Requisito</div><div class="cell head">Evidência</div><div class="cell head">Owner</div><div class="cell head">Status</div><div class="cell">{{id_1}}</div><div class="cell">{{req_1}}</div><div class="cell">{{evidence_1}}</div><div class="cell">{{owner_1}}</div><div class="cell status">{{status_1}}</div><div class="cell">{{id_2}}</div><div class="cell">{{req_2}}</div><div class="cell">{{evidence_2}}</div><div class="cell">{{owner_2}}</div><div class="cell status">{{status_2}}</div><div class="cell">{{id_3}}</div><div class="cell">{{req_3}}</div><div class="cell">{{evidence_3}}</div><div class="cell">{{owner_3}}</div><div class="cell status">{{status_3}}</div><div class="cell">{{id_4}}</div><div class="cell">{{req_4}}</div><div class="cell">{{evidence_4}}</div><div class="cell">{{owner_4}}</div><div class="cell status">{{status_4}}</div></section></main></body></html>
```


## Referência: references/source/templates/wireframes/unit-economics.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Unit Economics</title><style>body{margin:0;background:#f5f7fa;color:#121826;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:56px;display:grid;grid-template-rows:auto 1fr auto;gap:26px}h1{margin:0;font-size:44px}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.metric{background:white;border:1px solid #d8dee8;border-radius:8px;padding:22px}.label{color:#5d6678;text-transform:uppercase;letter-spacing:.12em;font-size:12px;font-weight:850}.value{font-size:48px;font-weight:900;margin-top:18px}.formula{color:#5d6678;margin-top:12px}.decision{border-left:5px solid #0052cc;padding-left:18px;font-size:24px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="grid"><article class="metric"><div class="label">CAC</div><div class="value">{{cac}}</div><div class="formula">{{cac_formula}}</div></article><article class="metric"><div class="label">LTV</div><div class="value">{{ltv}}</div><div class="formula">{{ltv_formula}}</div></article><article class="metric"><div class="label">Payback</div><div class="value">{{payback}}</div><div class="formula">{{payback_formula}}</div></article><article class="metric"><div class="label">Margin</div><div class="value">{{margin}}</div><div class="formula">{{margin_formula}}</div></article></section><footer class="decision">{{decision}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/user-story-map.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>User Story Map</title><style>body{margin:0;background:#f8fafc;color:#101828;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:48px;display:grid;grid-template-rows:auto 1fr auto;gap:22px}h1{margin:0;font-size:42px}.map{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.col{display:grid;grid-template-rows:auto repeat(3,1fr);gap:10px}.activity{background:#155eef;color:white;border-radius:8px;padding:16px;font-weight:900}.story{background:white;border:1px solid #d0d5dd;border-radius:8px;padding:14px;color:#667085}.slice{border-left:5px solid #12b76a;padding-left:18px;font-size:20px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="map"><div class="col"><div class="activity">{{activity_1}}</div><div class="story">{{story_1a}}</div><div class="story">{{story_1b}}</div><div class="story">{{story_1c}}</div></div><div class="col"><div class="activity">{{activity_2}}</div><div class="story">{{story_2a}}</div><div class="story">{{story_2b}}</div><div class="story">{{story_2c}}</div></div><div class="col"><div class="activity">{{activity_3}}</div><div class="story">{{story_3a}}</div><div class="story">{{story_3b}}</div><div class="story">{{story_3c}}</div></div><div class="col"><div class="activity">{{activity_4}}</div><div class="story">{{story_4a}}</div><div class="story">{{story_4b}}</div><div class="story">{{story_4c}}</div></div><div class="col"><div class="activity">{{activity_5}}</div><div class="story">{{story_5a}}</div><div class="story">{{story_5b}}</div><div class="story">{{story_5c}}</div></div></section><footer class="slice">{{release_slice}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/value-chain.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Value Chain</title><style>body{margin:0;background:#fafaf8;color:#1c1d1f;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:56px;display:grid;grid-template-rows:auto 1fr auto;gap:26px}h1{margin:0;font-size:42px}.chain{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}.stage{background:white;border:1px solid #dcddd8;border-radius:8px;padding:18px}.num{color:#2e7d5b;font-weight:900}.name{font-size:22px;font-weight:900;margin-top:12px}.output{color:#63666a;margin-top:12px;line-height:1.35}.note{border-left:5px solid #2e7d5b;padding-left:18px;font-size:22px;font-weight:850}</style></head><body><main class="slide"><h1>{{action_title}}</h1><section class="chain"><article class="stage"><div class="num">01</div><div class="name">{{stage_1}}</div><div class="output">{{output_1}}</div></article><article class="stage"><div class="num">02</div><div class="name">{{stage_2}}</div><div class="output">{{output_2}}</div></article><article class="stage"><div class="num">03</div><div class="name">{{stage_3}}</div><div class="output">{{output_3}}</div></article><article class="stage"><div class="num">04</div><div class="name">{{stage_4}}</div><div class="output">{{output_4}}</div></article><article class="stage"><div class="num">05</div><div class="name">{{stage_5}}</div><div class="output">{{output_5}}</div></article><article class="stage"><div class="num">06</div><div class="name">{{stage_6}}</div><div class="output">{{output_6}}</div></article></section><footer class="note">{{bottleneck_or_takeaway}}</footer></main></body></html>
```


## Referência: references/source/templates/wireframes/webinar-flow.html

```html
<!doctype html>
<html lang="pt-BR">
  <head><meta charset="utf-8"><title>Webinar Flow</title></head>
  <body style="margin:0;background:#101010;color:#f7f3ea;font-family:Inter,Arial,sans-serif">
    <section style="padding:44px">
      <p style="font:12px monospace;text-transform:uppercase;color:#ffb84d">webinar_conversion</p>
      <h1 style="font-size:34px">Webinar é uma sequência de mudança de crença, não uma aula genérica.</h1>
      <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:30px">
        <div style="border:1px solid #333;padding:16px">Promessa</div>
        <div style="border:1px solid #333;padding:16px">Erro</div>
        <div style="border:1px solid #333;padding:16px">Mecanismo</div>
        <div style="border:1px solid #333;padding:16px">Prova</div>
        <div style="border:1px solid #ffb84d;background:#ffb84d;color:#111;padding:16px;font-weight:800">Oferta</div>
      </div>
    </section>
  </body>
</html>
```


## Referência: references/source/templates/wireframes/workshop-canvas.html

```html
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Workshop Canvas</title><style>body{margin:0;background:#fffcf5;color:#1f2933;font-family:Inter,Arial,sans-serif}.slide{width:1280px;height:720px;box-sizing:border-box;padding:52px;display:grid;grid-template-rows:auto 1fr;gap:24px}h1{margin:0;font-size:42px}.canvas{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr);gap:14px}.box{border:2px dashed #d8cbb3;background:white;border-radius:8px;padding:22px}.label{color:#7c3aed;font-size:13px;letter-spacing:.12em;text-transform:uppercase;font-weight:900}.prompt{font-size:24px;font-weight:850;margin-top:14px}.hint{color:#6b7280;font-size:16px;line-height:1.4;margin-top:12px}</style></head><body><main class="slide"><h1>{{canvas_goal}}</h1><section class="canvas"><article class="box"><div class="label">{{field_1_label}}</div><div class="prompt">{{field_1_prompt}}</div><div class="hint">{{field_1_hint}}</div></article><article class="box"><div class="label">{{field_2_label}}</div><div class="prompt">{{field_2_prompt}}</div><div class="hint">{{field_2_hint}}</div></article><article class="box"><div class="label">{{field_3_label}}</div><div class="prompt">{{field_3_prompt}}</div><div class="hint">{{field_3_hint}}</div></article><article class="box"><div class="label">{{field_4_label}}</div><div class="prompt">{{field_4_prompt}}</div><div class="hint">{{field_4_hint}}</div></article><article class="box"><div class="label">{{field_5_label}}</div><div class="prompt">{{field_5_prompt}}</div><div class="hint">{{field_5_hint}}</div></article><article class="box"><div class="label">Output</div><div class="prompt">{{output_artifact}}</div><div class="hint">{{timebox}}</div></article></section></main></body></html>
```
