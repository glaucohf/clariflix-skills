# ROTEIRO: Devlog — Tirei meu jogo do papel com AIOX

**Duração estimada:** 9-10 min
**Formato:** Hybrid (Facecam + Screencast + B-Roll)
**Estilo:** Devlog pessoal — casual, honesto, mostrando o processo real
**Requisitos:** #DesafioAIOX | Mostrar AIOX na tela | Mínimo 5 min | 16:9

---

## METADATA

### Opções de Título
1. `Tirei meu jogo do papel com AIOX (depois de 6 anos)` ← recomendado
2. `6 anos engavetado. 1 sessão com AIOX. Olha no que deu.`
3. `Devlog #0 — Como a IA me deu o time que eu nunca tive`
4. `Eu tinha um jogo na gaveta. O AIOX tirou ele de lá.`
5. `De GDD parado a protótipo jogável — com AIOX | #DesafioAIOX`

### Thumbnail (Conceito)
- **Lado esquerdo:** Print do GDD no Obsidian (bagunçado, cheio de texto)
- **Lado direito:** Tela do jogo/conceito visual (pixel art, atmosfera)
- **Centro:** Rosto do Sid com expressão de "mano, funcionou"
- **Texto:** "6 ANOS → 1 DIA" (grande, contraste alto)
- **Seta:** Do GDD pro jogo

### Descrição do Vídeo
```
Eu tinha um jogo engavetado desde 2020. Uma história sobre bullying,
investigação e horror psicológico que começou como peça de teatro
e virou um GDD de 700 linhas... que nunca saiu do papel.

Até eu usar o AIOX.

Nesse devlog, mostro como usei squads de agentes de IA pra transformar
um documento parado em design refinado, narrativa expandida e um protótipo
real. Tudo em uma sessão.

Se você tem um projeto engavetado, comenta aqui embaixo qual é.
Vamos tirar do papel juntos.

⏱️ Timestamps:
0:00 — O jogo que eu nunca fiz
1:30 — O que é AIOX (e por que é diferente)
3:00 — Organizando o caos (GDD)
4:30 — Expandindo a narrativa com agentes
6:00 — Do design ao protótipo
7:30 — O resultado final
8:30 — O que aprendi

🔗 AIOX: [link]
🔗 Academia Lendária: [link]

#DesafioAIOX #GameDev #AIOX #IndieDev #Devlog
```

---

## ROTEIRO COMPLETO

═══════════════════════════════════════════════════════════════
### [00:00 — 00:10] COLD OPEN — Hook Visual
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Tela escura. Texto aparece letra por letra, estilo terminal:
```
> 14 anos atrás, um garoto com leucemia foi espancado pelos colegas.
> A escola encobriu tudo.
> Dois adolescentes morreram.
> Ninguém foi punido.
```
Som ambiente: chuva leve, teclas digitando.
Último texto aparece com delay: `> Essa história tá na minha cabeça desde 2020.`

🎙️ **ÁUDIO:** [Silêncio. Só o som ambiente. Sem narração.]

💡 **NOTA:** Esse hook é 100% visual. A ausência de voz cria tensão. O viewer precisa LER. Isso prende atenção.

═══════════════════════════════════════════════════════════════
### [00:10 — 00:25] TRANSIÇÃO — Facecam
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Corta pra facecam. Sid no setup, iluminação natural/ring light. Enquadramento médio (peito pra cima). Ambiente de dev — monitor atrás com código/Obsidian desfocado.

🎙️ **ÁUDIO:**
"Fala. Isso que você acabou de ler é a premissa de um jogo que eu quero fazer desde... 2020. Seis anos. Começou como uma peça de teatro na escola, virou um livro, e em algum momento eu pensei: 'isso precisa virar um jogo.' O problema é que eu nunca consegui tirar do papel."

💡 **NOTA:** Tom honesto, sem vergonha. Devlog = vulnerabilidade real.

═══════════════════════════════════════════════════════════════
### [00:25 — 01:30] BLOCO 1 — O Jogo Engavetado
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Screencast — abrir Obsidian mostrando o vault do jogo. Scroll pelo GDD. Zoom em seções: elevator pitch, personagens, mapa da casa do Samuel. Mostrar que é DENSO — 700+ linhas de design.

🎙️ **ÁUDIO:**
"O jogo se chama The Days After You. É um jogo de investigação e horror psicológico, estilo top-down, tipo Stardew Valley mas... sombrio. Você joga como Samuel, um investigador que reabre um caso de bullying fatal de 14 anos atrás. Duas mortes. Escola que encobriu tudo. Sobreviventes destruídos."

*(pausa, muda o tom)*

"E eu tenho TUDO documentado. Olha isso."

*(scroll pelo GDD)*

"Mecânicas, personagens, level design, paleta de cores, sistema de lanterna, sistema de intenções que substitui o quest log... 700 linhas de Game Design Document. Tá tudo aqui."

*(para o scroll, olha pra câmera)*

"Mas é isso. Tá aqui. Parado. Porque eu sou uma pessoa só e tirar um jogo do papel sozinho é... é difícil, mano."

💡 **NOTA:** Mostrar o GDD no Obsidian real. O scroll rápido mostra VOLUME. Os zooms mostram QUALIDADE. O viewer precisa pensar "caramba, esse cara planejou tudo e mesmo assim não fez".

---

**🔄 PATTERN INTERRUPT — 01:30**

═══════════════════════════════════════════════════════════════
### [01:30 — 03:00] BLOCO 2 — O que é AIOX (Apresentação Natural)
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Facecam → transição pra screencast do AIOX. Mostrar a interface — dashboard, squads, agentes. Abrir o terminal/Claude Code com AIOX rodando.

🎙️ **ÁUDIO:**
"Aí entra o AIOX. Pra quem não conhece: o AIOX é um framework de squads de agentes de IA. Em vez de ter uma IA genérica que faz tudo mais ou menos, você monta times especializados. Tipo... um arquiteto de software, um dev, um QA, um analista. Cada um com sua função, trabalhando junto."

*(mostra na tela os agentes)*

"E a sacada é: esses agentes não são chatbots. Eles têm contexto do seu projeto, seguem regras que você define, e trabalham em cima dos seus arquivos reais. Não é 'me dá uma ideia de jogo'. É 'aqui tem 700 linhas de GDD, me ajuda a tirar isso do papel'."

*(mostra abrindo o projeto no AIOX)*

"Eu sou professor de AIOX na Academia Lendária, então eu conheço a ferramenta. Mas até eu fiquei surpreso com o que saiu quando apontei pros meus arquivos do jogo."

💡 **NOTA:** Essa é a parte "educacional" mas no tom devlog. Não é tutorial — é "deixa eu te mostrar o que EU uso". Mostrar interface REAL do AIOX na tela. Tempo na tela: ~60% screencast, 40% facecam.

---

**🔄 PATTERN INTERRUPT — 03:00** (zoom no terminal, som de "boot")

═══════════════════════════════════════════════════════════════
### [03:00 — 04:30] BLOCO 3 — Organizando o Caos (GDD + Arquitetura)
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Screencast — sessão real com AIOX. Mostrar o agente @architect ou equivalente analisando o GDD. Output aparecendo em tempo real. Highlight nas partes mais relevantes.

🎙️ **ÁUDIO:**
"Primeira coisa que eu fiz: joguei o GDD inteiro pro AIOX e pedi pra ele analisar a arquitetura do jogo. O que tá sólido, o que tem buraco, o que falta."

*(mostra o output na tela, vai apontando)*

"E olha... ele pegou coisas que eu não tinha visto. Tipo: o sistema de intenções — que é uma das mecânicas mais originais do jogo — tava descrito como conceito mas não tinha especificação técnica de como implementar. State machine? Event queue? Nada. Tava no ar."

*(mostra sugestão do AIOX)*

"O agente sugeriu usar um padrão Command combinado com Observer pro sistema de intenções. E... faz sentido. As intenções se acumulam como comandos numa fila, e o sistema atmosférico reage como observer. Isso tá no GDD agora."

"Ele também organizou a priorização do MVP de um jeito que eu não tinha pensado. Separou o que é MUST do que é SHOULD com uma lógica de dependência que... é tipo ter um game designer senior do lado."

💡 **NOTA:** Mostrar output REAL. Se possível, acelerar partes lentas (2x) mas manter os momentos de "uau". Texto na tela destacando os insights mais fortes.

---

**🔄 PATTERN INTERRUPT — 04:30** (corte seco pra facecam, close-up)

═══════════════════════════════════════════════════════════════
### [04:30 — 06:00] BLOCO 4 — Narrativa Expandida (a parte que arrepia)
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Facecam (close) → screencast mostrando diálogos e narrativa gerada. Mostrar trechos de diálogo do Samuel, mensagens do celular in-game, storylets QBN.

🎙️ **ÁUDIO:**
"Agora a parte que me pegou de verdade. Eu pedi pro AIOX expandir a narrativa. Não inventar — expandir. Porque o lore já existe, veio de uma peça e um livro que eu escrevi. Mas faltava transformar em gameplay."

*(mostra diálogos gerados)*

"Ele gerou diálogos pro prólogo inteiro. Samuel acordando, checando o celular, fazendo café — e em cada momento plantando informação do caso. Tipo: enquanto o café tá passando, o Ícaro manda mensagem perguntando se ele viu a notícia da exumação. É natural. É como a gente recebe informação na vida real."

*(mostra exemplo de mensagem in-game)*

"E essa frase aqui..."

*(zoom na tela: "Você sente isso?")*

"Essa frase é de um NPC relatando sensações estranhas perto da escola. Pode ser sobrenatural. Pode ser trauma coletivo. O jogo nunca confirma. E o AIOX respeitou essa regra. Eu coloquei no contexto que a ambiguidade sobrenatural é inegociável, e ele manteve."

*(volta pra facecam, mais emocional)*

"Mano... essa história é muito pessoal pra mim. Nasceu na adolescência. E ver ela ganhando vida assim, com diálogos que soam como eu escreveria... é diferente."

💡 **NOTA:** Esse é o bloco EMOCIONAL do vídeo. O tom muda. Mais lento, mais próximo. O viewer precisa sentir que isso importa pro Sid. A frase "Você sente isso?" pode virar momento de thumbnail/shorts.

---

**🔄 PATTERN INTERRUPT — 06:00** (música muda, tela com montagem rápida de código)

═══════════════════════════════════════════════════════════════
### [06:00 — 07:30] BLOCO 5 — Do Design ao Protótipo
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Screencast — AIOX gerando código/estrutura. Mostrar: estrutura de projeto, código de movimentação, sistema de lanterna, UI do celular. Se possível, mostrar rodando numa engine (Godot/protótipo web).

🎙️ **ÁUDIO:**
"Ok, narrativa refinada, arquitetura sólida. Mas o teste real é: sai código disso?"

*(mostra gerando código)*

"Pedi pro AIOX gerar a estrutura base do projeto. Movimentação top-down 8 direções, sistema de interação, e o começo do sistema de lanterna com bateria que drena."

*(mostra código na tela, highlight nas partes mais interessantes)*

"O sistema da lanterna ficou... olha. Ela tem bateria limitada, drena mais rápido em locais 'carregados' emocionalmente, e nos horários significativos — 6h e 18h no jogo — ela pode falhar mesmo com bateria cheia. É uma metáfora de recurso mental. Tava no GDD e o AIOX implementou."

*(mostra protótipo rodando se possível, ou mockup/wireframe)*

"Não vou mentir: não é um jogo pronto. É um protótipo. Mas é um protótipo que tem as mecânicas core funcionando. Movimentação, lanterna, intenções acumulando. Semana passada isso era um PDF. Agora roda."

💡 **NOTA:** Se tiver protótipo rodando, é o MONEY SHOT do vídeo. Se não, mostrar código + mockups + wireframes já é forte. O importante é o contraste: antes (documento) → depois (algo funcional).

---

**🔄 PATTERN INTERRUPT — 07:30** (corte, tela split: GDD esquerda ↔ resultado direita)

═══════════════════════════════════════════════════════════════
### [07:30 — 08:30] BLOCO 6 — O Resultado (Antes vs Depois)
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Tela dividida:
- **Esquerda:** GDD no Obsidian (estático, texto puro)
- **Direita:** Tudo que foi gerado (código, diálogos, arte conceitual, protótipo)

Depois: facecam, enquadramento médio, tom reflexivo.

🎙️ **ÁUDIO:**
"Deixa eu recapitular o que aconteceu aqui."

*(tela split aparece)*

"Lado esquerdo: o que eu tinha. 700 linhas de GDD. Ideias. Ambição. E seis anos de 'um dia eu faço'."

"Lado direito: o que o AIOX me ajudou a gerar. Arquitetura técnica real. Narrativa expandida com diálogos jogáveis. Código funcional das mecânicas core. Tudo conectado ao meu material original."

*(volta pra facecam)*

"O AIOX não fez o jogo por mim. Ele não inventou a história, não criou os personagens, não decidiu o tom. Isso tudo já existia. O que ele fez foi me dar algo que eu nunca tive pra esse projeto..."

*(pausa)*

"Um time."

💡 **NOTA:** A frase "um time" é o payoff emocional do vídeo inteiro. Pausa antes, entrega com peso. Pode ter um leve zoom in na facecam.

═══════════════════════════════════════════════════════════════
### [08:30 — 09:15] BLOCO 7 — Reflexão + O que vem depois
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Facecam, mais relaxado. Pode estar com café na mão. Tela ao fundo mostrando o jogo/GDD.

🎙️ **ÁUDIO:**
"Se você é dev indie, ou criativo, ou qualquer pessoa que tem um projeto na gaveta... eu sei como é. Você sabe exatamente o que quer fazer, consegue descrever nos mínimos detalhes, mas na hora de executar sozinho... trava."

"O que eu aprendi com essa sessão é que o AIOX não substitui a sua visão. Ele acelera a execução. A diferença entre ter uma ideia e ter um protótipo é enorme. E quando você vê a sua ideia rodando pela primeira vez..."

*(olha pro lado, pro monitor com o jogo)*

"...é diferente."

"Esse devlog é o zero. O começo. The Days After You ainda tem um caminho longo. Mas pela primeira vez em seis anos... ele tá andando."

💡 **NOTA:** Tom de encerramento de devlog clássico — honesto, olhando pra frente, sem prometer demais.

═══════════════════════════════════════════════════════════════
### [09:15 — 09:45] CTA + ENCERRAMENTO
═══════════════════════════════════════════════════════════════

🎥 **VISUAL:** Facecam. Sorriso. Ao final, tela com:
- Nome do jogo: "The Days After You"
- #DesafioAIOX
- "Devlog #0"
- Link AIOX + Academia Lendária

🎙️ **ÁUDIO:**
"Se você tem um projeto engavetado — jogo, app, livro, qualquer coisa — comenta aqui embaixo qual é. Eu quero saber. E se esse vídeo te inspirou a tirar alguma coisa do papel, deixa o like que isso me ajuda demais."

*(tom mais leve)*

"Valeu por assistir. Nos vemos no devlog um... se tudo der certo."

*(pisca, sorriso, corta)*

💡 **NOTA:** CTA pede COMENTÁRIO (engagement) + LIKE. A pergunta "qual é seu projeto engavetado?" gera respostas longas = algoritmo adora. O "devlog um... se tudo der certo" planta expectativa sem prometer.

💡 **END SCREEN:** Últimos 20s com card de inscrição + sugestão de vídeo (se tiver).

---

## CHECKLIST DE GRAVAÇÃO

### Antes de gravar
- [ ] Obsidian aberto com o GDD do The Days After You
- [ ] AIOX/Claude Code aberto e configurado com o projeto
- [ ] OBS configurado (cenas: facecam, screencast, hybrid, tela escura)
- [ ] Mic testado (gravar 10s e ouvir)
- [ ] Iluminação ok (ring light ou janela lateral)
- [ ] Café na mão (prop real + referência ao jogo)
- [ ] Notificações do Windows desligadas
- [ ] Gravar as sessões com AIOX ANTES — o vídeo usa os melhores trechos

### Cenas do OBS
1. **[FACECAM]** — Câmera centralizada, fundo com setup
2. **[SCREENCAST]** — Tela cheia capturando monitor principal
3. **[HYBRID]** — Screencast + facecam pequena no canto inferior direito
4. **[DARK]** — Tela preta pra texto/transições

### Material a gravar
- [ ] Sessão AIOX analisando o GDD (~30-60 min de gravação bruta)
- [ ] Sessão AIOX gerando narrativa/diálogos (~30 min)
- [ ] Sessão AIOX gerando código/protótipo (~30-60 min)
- [ ] Facecam: blocos de narração (seguir o roteiro)
- [ ] B-Roll: scroll pelo GDD, close no código, tela do jogo

### Pós-produção (Capcut)
- [ ] Cortar sessões AIOX pros melhores momentos (acelelar partes lentas 2x-4x)
- [ ] Adicionar texto na tela nos momentos-chave
- [ ] Música ambiente (lo-fi/ambient, sem copyright — sugiro: Epidemic Sound free ou YouTube Audio Library)
- [ ] Color grading leve (warm nos blocos pessoais, cool nos blocos de código)
- [ ] Zoom ins pra enfatizar (frases importantes, código, "Você sente isso?")
- [ ] Exportar 1920x1080, 30fps mínimo

### Upload
- [ ] Título com #DesafioAIOX
- [ ] Descrição com timestamps + hashtag + links
- [ ] Thumbnail pronta (Canva ou Capcut)
- [ ] Tags: AIOX, GameDev, Devlog, IndieDev, DesafioAIOX, AI, AcademiaLendaria
- [ ] Vídeo PÚBLICO (não unlisted)
- [ ] Submeter formulário: tally.so/r/ODzkGK

---

## SHORTS DE APOIO (postar antes e depois do vídeo principal)

### Short 1 — Teaser (postar 2 dias antes)
```
[00:00] Texto na tela: "6 anos engavetado."
[00:02] Scroll rápido pelo GDD no Obsidian
[00:04] Texto: "1 sessão com AIOX."
[00:06] Tela do protótipo/resultado
[00:08] Facecam: "Vídeo completo saindo [data]. Fica ligado."
[00:10] Tela final com #DesafioAIOX
```

### Short 2 — "Você sente isso?" (postar junto com o vídeo)
```
[00:00] Tela escura, texto aparece: "Você sente isso?"
[00:03] Facecam: "Essa é a frase mais importante do meu jogo."
[00:05] Mostra o contexto no GDD — horror psicológico, ambiguidade sobrenatural
[00:12] "Quer saber a história completa? Link na bio."
[00:15] #DesafioAIOX #GameDev
```

### Short 3 — Resultado (postar 1 dia depois)
```
[00:00] Split screen: GDD (esquerda) vs resultado (direita)
[00:03] Facecam: "Lado esquerdo: 6 anos de planejamento. Lado direito: 1 sessão com AIOX."
[00:08] "E isso é só o devlog zero."
[00:10] #DesafioAIOX
```

---

*Roteiro v1.0 — Gerado por Cena (Scriptwriter) em 2026-03-16*
*Projeto: Desafio AIOX — "Tirei meu jogo do papel com AIOX"*
*Referências: GDD The Days After You (v0.1) + writing-style.md (Sid DNA)*
