# Design System — Proposta Comercial

> Especificação visual canônica da skill `proposta-comercial`. Baseada na análise
> página-a-página da proposta de referência (Proposta_XFlow, 16 páginas, proporção 2:1).
> Este arquivo garante que QUALQUER proposta gerada — com qualquer marca — mantenha a
> qualidade do design de referência: suíço, tipográfico, flat, com espaço em branco radical.

**Convenção de medidas**: todas as medidas são RELATIVAS à largura da página
(base de referência: 1280×640px, proporção 2:1). Ex.: "5% da largura" = 64px na base.
Use `clamp()`/unidades relativas no CSS para que o deck escale sem quebrar.
Nunca use medidas absolutas que não derivem da largura da página.

---

## 1. Design Tokens

Declare TODOS os tokens como CSS custom properties no `:root` do HTML gerado.
O re-branding acontece SOMENTE trocando valores de tokens — nunca editando CSS espalhado.

| CSS var | Valor default | Papel | O que muda no re-branding |
|---|---|---|---|
| `--pagina-branca` | `#ffffff` | Fundo das páginas claras (capa, cronograma, investimento, fechamento) | NADA. Fundos permanecem neutros. |
| `--pagina-cinza` | `#f8f8f8` | Variação sutil para páginas de contexto (quebra a monotonia do branco puro) | NADA. |
| `--pagina-preta` | `#000000` | Fundo do bloco escuro (entregáveis, páginas de produto, prazo) | NADA (exceção: modo dark-first pode trocar por um "quase-preto" da marca, ex. `#0a0a0c`, se o brand guide o definir). |
| `--pagina-cinza-med` | `#b8b8b8` | Fundo das divisórias cinza e da página de opcional/upsell — título branco sobre ele | NADA, ou um cinza neutro equivalente (luminância similar). Nunca uma cor saturada. |
| `--card-escuro` | `#161616` | Fundo dos cards sobre página preta (borda: `rgba(255,255,255,0.08)`) | NADA. Card escuro é sempre "um degrau acima" do fundo preto. |
| `--texto-primario` | `#000000` (claro) / `#ffffff` (escuro) | Títulos, trechos em bold, texto de ênfase | NADA. Texto primário é sempre preto-ou-branco. |
| `--texto-muted` | `#a5a5a5` | Bullets, parágrafos secundários, a "voz baixa" do deck | NADA (ajuste fino de contraste permitido, ver seção 4c). |
| `--texto-fantasma` | `#ececec` | Elementos gigantes decorativos (ano na capa, "©" central, logo do fechamento) | NADA. Deve ser quase invisível — é textura, não informação. |
| `--verde-toggle` | `#2fd157` | Toggle iOS "ligado" nos cards de entregáveis; ícones de check nas features | SIM — recebe a cor de acento da marca (validada, ver seção 4c). |
| `--verde-icone-bg` | `#132315` | Fundo do quadrado atrás do ícone de check (versão escurecida do acento) | SIM — recalcular: mesma matiz do acento, ~12-15% de luminosidade (mistura do acento com o preto a ~85%). |
| `--badge-bg` | `#e4e6ff` | Pill do sprint no cronograma (versão pastel do acento frio) | SIM — versão pastel/clareada da cor de acento (~90% de luminosidade, mesma matiz). |
| `--badge-texto` | `#0079ff` | Texto dentro do pill do sprint | SIM — a cor de acento da marca (ou versão escurecida dela que passe AA sobre `--badge-bg`). |
| `--acento-quente` | `#ff8770` | Rótulo "Opcional )" na página de investimento — o ÚNICO ponto quente do deck | SIM — segunda cor da marca se existir; senão, derivar um tom quente análogo, ou reutilizar o acento principal. |

Tokens derivados recomendados (declarar também, para consistência):

```css
--card-borda:  rgba(255,255,255,0.08);  /* borda 1px dos cards escuros */
--linha-clara: #d9d9d9;                 /* linha do cronograma e divisores em páginas claras
                                           (equivale a rgba(0,0,0,0.15) sobre branco) */
--margem-x:    64px;                    /* margem lateral padrão (~5% da largura base 1280px) */
--fonte: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
```

Raio dos cards: 12–14px conforme o card (cards de toggle 14px; cards de feature e
mini-cards 12px) — sempre sutil, nunca "pílula".

---

## 2. Gramática Visual — as 9 regras e o porquê de cada uma

Estas regras NÃO são sugestões estéticas. São o mecanismo pelo qual a proposta comunica
competência e valor antes mesmo de o cliente ler uma linha. Violar uma regra barateia o deck.

**Regra 1 — Ritmo de cores.**
Capa clara → contexto claro → bloco escuro (entregáveis/produtos) → respiro cinza (opcional) →
bloco claro (cronograma) → pontuação escura (prazo) → divisória cinza → fechamento claro.
*Por quê:* a alternância claro/escuro cria capítulos perceptíveis — o leitor SENTE quando muda
de assunto sem precisar de numeração. O bloco escuro concentra a oferta (o "produto" fica em
palco escuro, como vitrine); as páginas claras dão respiro e credibilidade documental.
Divisórias de uma palavra só funcionam como respiração dramática entre atos.

**Regra 2 — Espaço em branco radical.**
Páginas com 60-80% de vazio são INTENCIONAIS. A capa é ~90% vazia. O contexto tem um único
parágrafo num quadrante.
*Por quê:* espaço em branco é o sinal visual mais barato e mais forte de percepção premium —
diz "não precisamos gritar". Encher a página comunica insegurança e barateia o preço pedido.
Se o conteúdo não cabe, a resposta é criar outra página, nunca comprimir.

**Regra 3 — Grid e margens.**
Margens laterais de ~5% da largura em todas as páginas; conteúdo alinhado a um grid implícito
de 12 colunas.
*Por quê:* o alinhamento invisível é o que faz 16 páginas diferentes parecerem UM documento.
Quando títulos, parágrafos e cards de páginas distintas caem nas mesmas colunas, o leitor
percebe rigor de execução — exatamente a promessa comercial da proposta.

**Regra 4 — Cards uniformes.**
Bordas de 1px sutis (`rgba(255,255,255,0.08)` no escuro), cantos arredondados ~12-16px,
preenchimento interno generoso, MESMA altura dentro de cada grid.
*Por quê:* uniformidade transmite sistema, não improviso. A borda sutil delimita sem pesar;
sombras e bordas grossas criariam ruído e quebrariam o flat suíço.

**Regra 5 — Toggles verdes = incluído.**
Cada entregável do sumário aparece num card com um toggle estilo iOS LIGADO na cor de acento.
*Por quê:* é uma metáfora universal ("está ativado para você") que transforma uma lista
burocrática em sensação de produto configurado e pronto. O acento aparece pouco no deck —
por isso, quando aparece, significa "isto está incluso".

**Regra 6 — Timeline com dots e alternância.**
Cronograma como linha horizontal central com pontos; conteúdo dos sprints alternando acima e
abaixo da linha (pares acima, ímpares abaixo).
*Por quê:* a alternância dobra a densidade sem parecer cheio, e a linha única comunica que o
projeto tem começo, meio e fim — sequência sob controle. Tabelas de cronograma parecem
burocracia; timelines parecem plano.

**Regra 7 — Fotografia disciplinada.**
Foto SOMENTE quando dramatiza (página do prazo/equipe). Sempre P&B/dessaturada, escurecida por
overlay preto de ~85%, texto branco por cima.
*Por quê:* foto colorida em página de proposta compete com o texto e introduz paleta fora dos
tokens. Escurecida a ~85%, ela vira textura emocional (gente trabalhando) sem quebrar o
monocromático. Uma única página com foto tem impacto; três teriam nenhum.

**Regra 8 — Rodapé fixo low-contrast.**
Todas as páginas de conteúdo levam o rodapé de 4 colunas:
`Proposta Comercial | {Marca do usuário} | © | {Ano}` — cinza discreto
(~`#b0b0b0` sobre claro; ~`#3a3a3a` sobre escuro), nunca chamando atenção.
*Por quê:* o rodapé é assinatura silenciosa e âncora de consistência — confirma em cada página
que o documento é um sistema. Low-contrast porque é metadado, não mensagem. Única página sem
rodapé: o fechamento (só o logo).

**Regra 9 — Flat, tipográfico, suíço.**
Nada de gradientes, sombras fortes, ilustrações 3D ou clip-art. A hierarquia nasce de tamanho,
peso e cor de texto — não de efeitos.
*Por quê:* efeitos datam rápido e sinalizam template genérico. Tipografia gigante bem colocada
sinaliza confiança de design. O estilo suíço é o produto: é ele que faz uma proposta de
R$ 200 mil parecer que vale R$ 200 mil.

---

## 3. Especificações por Layout (10 variantes)

Medidas em % da LARGURA da página, salvo indicação "da altura". Base: 1280×640.
Os valores com "~" são alvos aproximados; `assets/template.html` é a implementação
de referência — em caso de conflito numérico, o template prevalece.
O rodapé padrão (ver Regra 8) fica com baseline a ~92-93% da altura, texto ~1.1% da largura,
nas colunas: esquerda em 5%, centro-esquerda centrada em ~54%, "©" em ~76%, ano alinhado à
direita na margem de 95%.

### 3.1 `capa`
- Fundo: `--pagina-branca`. Sem logo no topo.
- Nome do cliente: bold, ~6.5-7% da largura (86px na base), tracking -0.02em, posicionado à
  esquerda (margem 5%), verticalmente centrado (~48-52% da altura). Sufixo "®" opcional em
  sobrescrito.
- "©" decorativo: `--texto-fantasma`, ~3% da largura, centrado horizontalmente (~62%), na
  mesma linha visual do nome.
- Ano: `--texto-fantasma`, MESMO tamanho do nome do cliente, alinhado à direita
  na margem de 95%, mesma baseline.
- Rodapé padrão presente.
- NÃO MEXER: no vazio. A capa é ~90% vazia por design. Nada de subtítulo, foto, tagline ou
  logo grande. Um elemento a mais aqui destrói a primeira impressão.

### 3.2 `contexto`
- Fundo: `--pagina-cinza` (#f8f8f8 — sutilmente diferente do branco da capa).
- Logo do usuário: line-art/monocromático, topo-direito (~2.5-3% de largura), margem 5%.
- Parágrafo único no quadrante inferior-direito: começa em ~50-55% da largura e ~55-60% da
  altura; largura de coluna ~35-40%; corpo ~1.6% da largura, line-height 1.55.
- Padrão de ênfase: texto base em `--texto-muted`, frases-chave em bold `--texto-primario`.
- Rodapé padrão presente.
- NÃO MEXER: na posição do parágrafo (inferior-direito) e no vazio dos outros 3 quadrantes.
  Não adicionar títulos — a página É o parágrafo.

### 3.3 `divisoria` (variantes dark / light / gray)
- Fundo: `--pagina-preta`, `--pagina-branca` ou `--pagina-cinza-med` conforme o ritmo.
- Uma ÚNICA palavra (ou expressão curtíssima) + ponto final: "Entregáveis.", "Cronograma.",
  "Investimento.".
- Título: ~9% da largura (112px na base), bold, tracking -0.02em, topo-esquerdo
  (margem 5%, topo ~8-12% da altura). Cor: branco sobre preto/cinza-med; preto sobre branco.
- Sem logo. Rodapé padrão presente (low-contrast adequado ao fundo).
- NÃO MEXER: uma palavra só, ponto final obrigatório, canto superior-esquerdo. Não centralizar,
  não adicionar subtítulo, não diminuir para "caber melhor" — se a palavra for longa demais,
  escolher palavra mais curta.

### 3.4 `sumario-toggles`
- Fundo: `--pagina-preta`. Logo topo-direito.
- Título da página (~5% da largura, bold, branco) no topo-esquerdo, margem 5%, topo ~8%.
- Parágrafo de apoio à direita: coluna de ~50% a ~84% da largura, topo alinhado ao título;
  corpo ~1.6%, ênfase seletiva (muted + bold branco).
- Cards de entregáveis: grid 2×2 (até 4 itens; com 5-6 itens usar 2×3), começando a
  ~56% da altura. Cada card: largura ~46% (duas colunas com gap ~2.5%), altura ~9.5-10% da
  altura da página, fundo `--card-escuro`, borda `--card-borda`, raio 14px.
- Dentro do card: toggle iOS ligado (`--verde-toggle`, largura ~2.2% da página) à esquerda +
  nome do entregável bold branco ~1.6%, alinhados verticalmente ao centro.
- Rodapé padrão presente.
- NÃO MEXER: no toggle (sempre LIGADO, sempre a cor de acento), na altura única dos cards,
  no espaço vazio entre o título e os cards.

### 3.5 `produto-features-grid`
- Fundo: `--pagina-preta`. Logo topo-direito.
- Título = nome do produto: ~5% da largura, bold branco, topo-esquerdo (margem 5%, topo ~7%).
- Grid de features: 4 colunas × 2 linhas (8 features — o ideal; aceitável 6 em grid 3×2).
  Cards: largura ~21.5% cada com gap ~2%, altura ~23% da altura da página;
  linha 1 a ~26% da altura, linha 2 a ~56%. Fundo `--card-escuro` (ou transparente com borda),
  borda 1px sutil, raio 12px.
- Dentro do card: quadrado do ícone (~3% da largura, raio ~10px, fundo `--verde-icone-bg`,
  ícone check circular em `--verde-toggle` com ~55% do quadrado) no topo; texto branco de
  2 linhas (~1.4-1.5% da largura, line-height 1.4) na base do card.
- Rodapé padrão presente.
- NÃO MEXER: máximo 8 cards; textos de NO MÁXIMO 2 linhas (cortar copy, não fonte); o mesmo
  ícone check em todos (a variação fica no texto, não no ícone).

### 3.6 `opcional-2col`
- Fundo: `--pagina-cinza-med` (#b8b8b8). Logo topo-direito (branco/line-art).
- Título branco em até 2 linhas, ~4.5% da largura, topo-esquerdo; rótulo "(Opcional)" logo
  abaixo em branco translúcido (`rgba(255,255,255,0.55)`), ~1.9%.
- Coluna central de texto (de ~46% a ~72% da largura): 2 blocos, cada um com título bold
  branco ~1.9% + corpo ~1.5% em branco translúcido; blocos separados por linha horizontal
  sutil (`rgba(255,255,255,0.3)`). Divisor vertical sutil entre coluna central e direita.
- Coluna direita (de ~75% a ~97%): título bold branco ~1.9% + pilha de até 5 mini-cards
  (altura ~9% da altura da página, borda 1px `rgba(255,255,255,0.35)`, raio ~12px), cada um
  com quadrado de ícone line-art branco (~2.4%) + texto bold branco ~1.3% em até 2 linhas.
- Rodapé padrão presente.
- NÃO MEXER: fundo cinza-médio com texto TODO branco (é o "respiro" do deck — não escurecer,
  não colorir); máximo 5 mini-cards.

### 3.7 `cronograma-timeline`
- Fundo: `--pagina-branca`. Logo topo-direito.
- Título "Cronograma." (COM ponto final) ~5.5% da largura, bold preto, topo-esquerdo —
  apenas na PRIMEIRA página de cronograma; páginas de continuação omitem o título.
- Linha do tempo: horizontal, y = ~50% da altura, cor `--linha-clara` (#d9d9d9), atravessando de
  0 a 100% da largura (pode iniciar em dashed antes do primeiro dot); dots (~0.55% de
  diâmetro, cinza `#c9c9c9`) marcando cada sprint.
- 4 sprints por página, alternando: ímpares ABAIXO da linha, pares ACIMA. Cada bloco de
  sprint ocupa coluna de ~25-30% da largura, alinhado ao seu dot.
- Badge pill: fundo `--badge-bg`, raio pill, padding ~0.6%/1%; texto "Sprint NN" bold +
  separador + "X-Y Dias", em `--badge-texto`, ~1.3% da largura.
- Título do sprint: bold preto, ~1.9%, logo abaixo (ou acima, nos blocos superiores) do badge.
- Bullets: até 5 por sprint, ~1.35%, `--texto-muted`, com ícone prefixo discreto (⊛ / ✳
  line-art cinza), line-height ~1.9.
- Rodapé padrão presente.
- NÃO MEXER: na alternância acima/abaixo (é ela que evita a cara de tabela); máximo
  4 sprints por página — 5 a 8 sprints = segunda página de cronograma, mesmo layout sem título.

### 3.8 `prazo-foto`
- Fundo: foto P&B (pessoas trabalhando/contexto do projeto), dessaturada, coberta por
  overlay preto de ~85% de opacidade (a foto deve ser percebida, não lida).
- Título ("O Prazo") branco bold, ~4.5% da largura, topo-esquerdo. Logo topo-direito.
- Parágrafo no quadrante inferior-direito: coluna de ~50% a ~84% da largura, iniciando a
  ~55% da altura; corpo ~1.6%, texto base em cinza-claro (`rgba(255,255,255,0.72)`) com
  ênfase bold branca nos números e compromissos ("prazo total de 90 dias").
- Segundo parágrafo opcional ("Obs.: ...") separado por linha em branco.
- Rodapé padrão presente (versão low-contrast clara).
- NÃO MEXER: overlay nunca abaixo de ~80% (texto precisa passar contraste AA sobre qualquer
  área da foto); foto sempre monocromática; sem créditos de foto visíveis.

### 3.9 `investimento-tabela`
- Fundo: `--pagina-branca` (ou `--pagina-cinza`). Logo topo-direito.
- Título ("Investimento") ~5.5% da largura, bold preto, topo-esquerdo.
- Coluna esquerda (margem 5% até ~45%), iniciando a ~50% da altura: frase principal ~1.9%
  com padrão de ênfase (muted + bold preto nos valores e condições); subtexto ~1.4% muted
  ("sem surpresas ou custos adicionais"); depois a linha do opcional: rótulo
  "Opcional )" em `--acento-quente` + texto muted ~1.4% descrevendo o recorrente mensal.
- Coluna direita (de ~50% a ~96.5%): tabela de linhas — cada linha com item bold preto
  ~1.9% à esquerda e preço bold preto alinhado à DIREITA; separadores `1px dashed`
  em cinza claro (#cccccc); altura de linha ~11% da altura da página.
- Linha final "Investimento Total": separada por borda SÓLIDA mais forte acima, item e valor
  em bold, mesmo corpo ou levemente maior.
- Rodapé padrão presente.
- NÃO MEXER: alinhamento dos preços à direita (escaneabilidade); dashed nas linhas comuns e
  sólida apenas antes do total; o acento quente aparece SÓ no rótulo do opcional — nunca nos
  valores.

### 3.10 `fechamento-logo`
- Fundo: `--pagina-branca`.
- Apenas o logo do usuário, centralizado (horizontal e vertical), em `--texto-fantasma` ou
  cinza-claro equivalente, com ~6-8% da largura.
- SEM rodapé. SEM texto. SEM CTA.
- NÃO MEXER: é a única página sem rodapé; a ausência de "chamada final" é intencional —
  o silêncio fecha a proposta com a mesma confiança da capa.

---

## 4. Protocolo de Adaptação de Marca

Executar ANTES de gerar o HTML. O resultado é um "brand-config" (mapa de tokens + fonte +
logo + modo claro/escuro) que parametriza o template.

### (a) Extrair a marca dos materiais do usuário

1. **Site (via WebFetch)**: buscar no HTML/CSS retornado: cores de fundo e de acento
   (procurar custom properties, cores de botões/links), família tipográfica declarada
   (`font-family` de headings e corpo), URL do logo (`<img>` no header, `og:image`,
   favicon SVG). Anotar se o site é dark-first (fundo global escuro).
2. **Logo (SVG/PNG fornecido)**: extrair a(s) cor(es) dominante(s) — em SVG, ler os `fill`;
   em PNG, perguntar ao usuário o hex se não for óbvio. Verificar se existe versão
   monocromática/line-art (ideal para o topo-direito das páginas). Se só houver logo colorido
   e pesado, preferir usar o NOME da marca tipografado (bold, na fonte do deck) ou um
   monograma tipográfico gerado.
3. **Brand guide (PDF)**: ler e extrair: paleta oficial (primária, secundária, neutros),
   tipografia oficial e usos, regras de logo (margens de proteção, versões). O brand guide
   TEM PRIORIDADE sobre o que for inferido de site/logo.
4. **Fonte**: se a fonte da marca existir no Google Fonts, usar com fallback no stack padrão
   (`'FonteDaMarca', 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif`). Se for
   proprietária sem equivalente, escolher a grotesca do Google Fonts mais próxima
   (Inter, Manrope, Archivo, Space Grotesk...) e AVISAR o usuário da substituição.
5. Sem materiais nenhum: entrevista mínima (3-6 perguntas) ou herdar o default monocromático
   integral (que é elegante por si só — melhor default limpo do que acento inventado).

### (b) Mapear a cor da marca APENAS para papéis de acento

- A cor primária da marca substitui: `--verde-toggle`, `--badge-texto` e os ícones de check.
- Derivar: `--verde-icone-bg` = acento a ~12-15% de luminosidade (mistura com preto ~85%);
  `--badge-bg` = acento a ~90% de luminosidade (versão pastel).
- `--acento-quente` recebe a cor secundária da marca, se houver; senão um análogo quente,
  ou o próprio acento principal.
- **Fundos NÃO mudam.** `--pagina-branca`, `--pagina-preta`, `--pagina-cinza`,
  `--pagina-cinza-med` e `--card-escuro` permanecem neutros. O estilo suíço monocromático
  com acento pontual É o produto — pintar fundos com a cor da marca transforma a proposta
  em panfleto. A marca aparece no acento, no logo e no rodapé; isso basta.

### (c) Validar contraste (WCAG AA)

- Textos: mínimo 4.5:1 contra o fundo (3:1 para texto grande, >= ~24px/19px bold).
- Testar o acento nos contextos onde ele carrega informação:
  - `--badge-texto` sobre `--badge-bg`;
  - ícone check sobre `--verde-icone-bg`;
  - `--acento-quente` sobre fundo claro.
- Se a cor de acento falhar sobre fundo ESCURO (ex.: azul-marinho da marca sobre `#000000`):
  CLAREAR a cor (aumentar luminosidade mantendo a matiz) até passar. O toggle e os ícones
  precisam "acender" sobre o preto.
- Se falhar sobre fundo CLARO (ex.: amarelo): escurecer para os usos sobre branco
  (`--badge-texto`, `--acento-quente`) mantendo a versão viva para os usos sobre preto.
  É legítimo ter duas variantes do acento (sobre-claro / sobre-escuro) — documentar ambas
  no brand-config.
- **NUNCA usar o acento como cor de corpo de texto.** Acento é para toggle, badge, ícone e
  rótulo curto. Parágrafos são sempre preto/branco/muted.
- `--texto-muted` (#a5a5a5) está no limite de AA para corpo pequeno: usar apenas em textos
  >= 1.4% da largura e nunca para informação crítica (preços, prazos ficam em bold primário).

### (d) Modo dark-first

Se a marca do usuário for dark-first (site escuro, brand guide dark), inverter o ritmo de
páginas: capa preta (nome do cliente em branco, ano em cinza-escuro fantasma ~`#1c1c1c`),
contexto quase-preto (`#0f0f0f` no papel do `--pagina-cinza`), bloco de produtos pode ir a
claro OU permanecer escuro com divisórias claras fazendo a pontuação invertida, cronograma
segue legível (se mantido escuro, badge pastel vira badge translúcido
`rgba(acento, 0.15)` com texto no acento clareado), fechamento preto com logo em
cinza-escuro. As REGRAS não mudam: continua havendo alternância de capítulos, espaço radical,
rodapé low-contrast (agora ~`#3a3a3a`), cards com borda sutil. Dark-first é espelhamento do
ritmo, não um design novo.

### (e) Quando o usuário pede para fugir do estilo suíço

Se o usuário pedir explicitamente algo fora do design system (fundos coloridos, gradientes,
estilo "vibrante", ilustrações): **obedecer** — a proposta é dele. Mas antes de gerar,
avisar em uma frase objetiva, por exemplo:

> "Posso fazer. Só registrando: isso sai do design system validado (estilo suíço da proposta
> de referência), então a garantia de consistência visual passa a ser menor. Confirma?"

Confirmado, gerar o que foi pedido mantendo o que ainda se aplicar (grid, margens, rodapé,
hierarquia tipográfica, contraste AA). Registrar no brand-config que o deck está em modo
"fora do padrão" para que iterações futuras não tentem "corrigir" de volta sem o usuário pedir.

---

## 5. Tipografia

**Stack**: `'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif` (grotesca neo-suíça,
Helvetica Now-like). Carregar Inter via Google Fonts com fallback graceful — o deck deve
continuar correto se a fonte não carregar. Pesos usados: 400 (corpo), 500 (apoios), 700
(títulos e ênfases). Nada de itálico, nada de light/thin.

**Escala (em % da largura da página; base 1280px entre parênteses):**

| Papel | Tamanho | Peso | Tracking | Observações |
|---|---|---|---|---|
| Título de divisória | ~9% (≈112px; reduza só se a palavra não couber) | 700 | -0.02em | SEMPRE com ponto final. Uma palavra. |
| Nome do cliente na capa / ano fantasma | ~6.5-7% (≈86px) | 700 | -0.02em | Ano em `--texto-fantasma`, MESMO tamanho do nome. |
| Título de página de conteúdo | ~5% (≈64px; até ~6.5% em páginas de 1 título) | 700 | -0.02em | Topo-esquerdo, margem 5%. |
| Título de seção interna (colunas, sprints) | ~1.9% (≈24px) | 700 | normal | |
| Corpo | 1.5-1.7% (≈19-22px) | 400 | normal | line-height 1.5-1.6. |
| Bullets / mini-cards / badge | ~1.3-1.4% (≈17-18px) | 400-700 | normal | badge em 700. |
| Rodapé | ~1.1% (≈14px) | 400 | normal | low-contrast sempre. |

**Regra do ponto final**: títulos de DIVISÓRIA terminam com ponto final ("Entregáveis.",
"Cronograma.", "Investimento.") — o ponto transforma a palavra em afirmação. Títulos de
páginas de conteúdo NÃO levam ponto ("Agente CS", "O Prazo", "Investimento" na página da
tabela). Não aplicar ponto final em nomes de produto nem em itens de card.
Exceção única (herdada da referência): a PRIMEIRA página de cronograma-timeline repete o
título "Cronograma." COM ponto final (ver 3.7); as páginas de continuação não têm título.

**Padrão de ênfase (assinatura tipográfica do deck)**: parágrafos em `--texto-muted` com os
trechos-chave em bold na cor primária (preto no claro, branco no escuro). O leitor apressado
deve conseguir ler SÓ os bolds e entender a proposta: promessa, prazo, preço. Ao escrever
copy, escolher os bolds deliberadamente (valores, entregas, compromissos) — nunca bold em
frase inteira, nunca mais de ~30% do parágrafo em bold.

**Alinhamento**: tudo alinhado à esquerda (exceto preços da tabela de investimento, à direita,
e o ano da capa/rodapé, à direita). Nunca centralizar parágrafos. Nunca justificar.

---

## 6. Anti-padrões Visuais (proibições)

Se qualquer item abaixo aparecer no HTML gerado, é bug de design — corrigir antes de mostrar:

1. **Gradientes chamativos** (fundos degradê, texto com gradiente, glassmorphism). O deck é
   flat. Único "gradiente" tolerado: overlay escuro uniforme sobre a foto do prazo.
2. **Sombras pesadas** (`box-shadow` visível, drop-shadows em cards ou títulos). Cards se
   separam do fundo por borda de 1px e diferença de tom — nunca por sombra.
3. **Clip-art, ilustrações 3D, stock icons coloridos**. Ícones são line-art monocromáticos
   ou o check no quadrado de acento. Fotografia só na página de prazo, P&B com overlay.
4. **Emojis como ícones** (em cards, bullets, títulos ou rodapé). Além de quebrarem a
   estética suíça, quebram a renderização consistente entre navegador e PDF.
5. **Mais de 1 cor de acento por papel**: um acento para "incluído/positivo"
   (toggle, checks, badges) e no máximo um acento quente para "opcional". Três ou mais cores
   vivas = panfleto. Se a marca tem 5 cores, escolher 1 (máximo 2) e ignorar o resto.
6. **Texto justificado** (`text-align: justify`) ou parágrafos centralizados. Alinhamento à
   esquerda, bandeira à direita, sempre.
7. **Mais de 8 cards por página** (ou mais de 4 sprints por página de cronograma, ou mais de
   5 mini-cards na coluna do opcional). Estourou? Cria-se outra página — nunca encolher
   cards ou fonte para caber.
8. Derivados diretos das regras (igualmente proibidos): encher o vazio das divisórias/capa
   com conteúdo; usar o acento em corpo de texto; colorir fundos com a cor da marca;
   rodapé em alto contraste; fotos coloridas ou sem overlay.
