---
name: proposta-comercial
description: "Cria propostas comerciais em HTML e PDF: extrai o briefing, adapta a identidade visual, organiza escopo e investimento e valida o deck antes da entrega."
version: 0.2.0
author: "Máquina de Receita · Gabriel Marcondes / Academia Lendária; adaptação ClariFlix"
license: LicenseRef-MaquinaDeReceita
platforms: [linux, macos, windows]
---

# Proposta Comercial — deck premium HTML → PDF

## Visão geral

Esta skill produz uma **proposta comercial em formato de deck 2:1** (páginas de
1280×640, como slides widescreen estendidos): um único arquivo
`proposta-<cliente>.html` self-contained (CSS inline, fontes com fallback, zero
dependências obrigatórias), revisado com o usuário no navegador e depois exportado
para **PDF paginado com fidelidade exata** (1 section = 1 página).

O design segue um sistema visual validado — neo-suíço, flat, preto/branco/cinza com
acento pontual na cor da marca, espaço em branco radical, divisórias dramáticas de uma
palavra ("Entregáveis.", "Cronograma.", "Investimento."). O arco narrativo apresenta
valor antes do preço: abertura → oferta → execução → comercial → fechamento.

**Para quem**: qualquer empresa ou profissional que venda serviços/projetos e precise
enviar propostas com aparência de agência de design — sem ter uma. A skill descobre o
negócio, o cliente e a oferta, e a marca do usuário entra por re-branding de tokens.

Tudo em pt-BR, salvo pedido explícito do usuário.

## When to Use

Use quando o usuário pedir uma proposta comercial, orçamento de serviços ou deck de proposta em HTML/PDF. Extraia primeiro os dados dos materiais já fornecidos. Não invente preços, prazos, condições ou provas sociais.

## Quick Reference

| Etapa | Recurso |
|---|---|
| Briefing | `references/descoberta.md` |
| Marca e layouts | `references/design-system.md` |
| Sumário e copy | `references/estrutura-narrativa.md` |
| Base do deck | `assets/template.html` |
| Exportação | `scripts/html2pdf.py` |
| Validação | `references/qa-checklist.md` |

Resolva esses caminhos a partir da **pasta instalada desta skill**, não do diretório atual do projeto. Para HTML, use um ambiente que possa criar arquivos. Para PDF automático, verifique Python 3.8+ e Edge, Chrome ou Chromium; não instale dependências automaticamente. O script usa a biblioteca padrão, com `pypdf` opcional para contar páginas. Sem navegador automatizável, ofereça a impressão manual descrita abaixo.

## Procedure

### Fluxo em 5 fases

Execute as fases em ordem. Cada fase indica o arquivo de referência a ler **naquele
momento** — não carregue todos de uma vez (mapa de recursos ao final).

### FASE 1 — Descoberta

1. Leia `references/descoberta.md` e execute o protocolo dele integralmente.
2. Inventarie os materiais fornecidos (mensagens, arquivos, URLs, transcrições de
   call) e **extraia primeiro, pergunte depois** — perguntar o que o material já
   responde queima a confiança do usuário.
3. Preencha os blocos A–F (quem vende, cliente, oferta, execução, comercial, extras).
   Entreviste apenas o que faltar, em grupos de no máximo 3–4 perguntas por mensagem.
4. **Nunca invente dados.** Preço, prazo, feature, nome, depoimento ou garantia que
   não veio do usuário não existe. Faltou? Pergunte.
5. Consolide o brief no formato do protocolo (com a soma comercial já conferida) e
   obtenha o "sim" explícito do usuário antes de seguir.

### FASE 2 — Configuração de marca

1. Leia a seção **"Protocolo de Adaptação de Marca"** (seção 4) de
   `references/design-system.md`.
2. Extraia a marca dos materiais: site (ferramenta de navegação disponível), logo SVG/PNG, brand guide (o brand
   guide tem prioridade). Sem materiais: entrevista mínima ou default monocromático —
   um default limpo vale mais que um acento inventado.
3. Monte o **brand-config**: bloco de tokens CSS com a cor da marca aplicada **apenas
   aos papéis de acento** (`--verde-toggle`, `--badge-texto`, derivados
   `--verde-icone-bg` ~12–15% de luminosidade e `--badge-bg` ~90%, `--acento-quente`).
   Fundos permanecem preto/branco/cinza — o estilo suíço é o produto.
4. Valide contraste WCAG AA nos contextos onde o acento carrega informação; clareie
   sobre fundo escuro / escureça sobre fundo claro conforme a seção 4c.
5. Registre no brand-config: fonte escolhida (Google Fonts + fallback), logo (arquivo
   ou monograma tipográfico), modo claro/escuro (dark-first inverte o ritmo, não o
   sistema) e, se o usuário pediu fuga do estilo suíço, o aviso dado e a confirmação.

### FASE 3 — Arquitetura de conteúdo

1. Leia `references/estrutura-narrativa.md` (arco, variantes e regras de mapeamento).
2. Escolha a variante — compacto (8–10 p.), padrão (12–16 p.) ou extenso (16–20 p.) —
   pelo tamanho da oferta. Na dúvida, a menor.
3. Aplique as regras de mapeamento brief → páginas: 1 produto = 1 página (6–8
   features), sumário de toggles com 2+ produtos, 4 sprints por página de cronograma,
   opcional só se houver upsell (e aparecendo exatamente 2x), soma da tabela = total.
4. Monte o **sumário de páginas** (lista numerada: nº, tipo de layout, conteúdo) e
   **apresente ao usuário para aprovação ANTES de gerar qualquer HTML**. Só avance
   após o "sim"; se ele ajustar, reexiba e confirme de novo.
5. Escreva a copy seguindo as diretrizes da seção 4 (bold-em-muted com 1–2 bolds por
   parágrafo, números concretos, divisórias de uma palavra com ponto final, zero
   clichês, zero exclamações, zero emojis).

### FASE 4 — Geração

1. **Copie** `assets/template.html` para o diretório de trabalho como
   `proposta-<cliente>.html` (nome do cliente em minúsculas, sem espaços). **Nunca
   edite o template original da skill** — ele é a matriz de todos os decks futuros.
2. No arquivo copiado: substitua os tokens do `:root` pelo brand-config; troque o
   `<symbol>` do logo pelo SVG da marca (instruções no próprio symbol); reescreva as
   sections conforme o sumário aprovado — duplique/remova/reordene as
   `<section class="page" data-layout="...">` (10 variantes de layout disponíveis).
3. Elimine TODO o conteúdo de exemplo ("Studio Vetor", "Café Aurora"): a proposta
   entregue não pode conter um único texto do template.
4. Consulte as especificações de layout (seção 3 de `references/design-system.md`)
   ao ajustar qualquer página — cada layout tem blocos "NÃO MEXER".
5. Abra o preview no navegador disponível no ambiente e itere com o
   usuário até ele aprovar. Texto que estoura um card é problema de copy: encurte o
   texto ou crie outra página — nunca reduza a fonte.

### FASE 5 — Exportação e QA

1. Exporte com validação:
   `python "<raiz-da-skill>/scripts/html2pdf.py" "<caminho-do-projeto>/proposta-<cliente>.html" --check`
   (exit 0 = ok; 2 = aviso de divergência de páginas; 1 = erro — ver Resolução de
   problemas). Use `--dpi-scale 2` se o usuário pedir mais nitidez.
2. Leia `references/qa-checklist.md` e rode o checklist COMPLETO (Técnica, Visual,
   Comercial). Itens comerciais em dúvida **bloqueiam a entrega** até o usuário
   responder.
3. Quando possível, renderize 2–3 páginas do PDF (capa, uma página de produto, a de
   investimento) e confira visualmente contra o HTML antes de entregar.
4. Reporte o resultado do QA ao usuário no formato compacto do checklist e entregue
   os caminhos do HTML e do PDF finais.

## Regras inegociáveis

- **Tudo em pt-BR** — skill, perguntas, copy do deck e mensagens — salvo pedido
  explícito do usuário por outro idioma.
- **Nunca inventar preço, prazo, feature, nome, depoimento ou garantia.** Tudo que
  aparece na proposta é rastreável ao brief confirmado. Lacuna = pergunta.
- **Sumário de páginas aprovado pelo usuário ANTES de gerar o HTML.** Sem exceção.
- **QA completo antes de entregar** (os 3 blocos do checklist), com resultado
  reportado. Divergência comercial (soma, multiplicadores "3x", promessas) para tudo
  até o usuário confirmar.
- **O template original da skill permanece intacto.** Trabalhe sempre numa cópia no
  diretório de trabalho do usuário.
- Fundos não recebem a cor da marca; acento não vira cor de corpo de texto; se o
  usuário pedir fuga do estilo suíço, avise uma vez, obtenha confirmação e registre.

## Pitfalls

### Resolução de problemas

| Problema | O que fazer |
|---|---|
| **Navegador não encontrado** (`html2pdf.py` exit 1) | Tente `--browser "C:/caminho/para/msedge.exe"` (ou chrome.exe). Se não houver navegador automatizável, instrua o fallback manual: abrir o HTML, Ctrl+P → Salvar como PDF → Margens: **Nenhuma** → ativar **"Gráficos de fundo"**. Resultado idêntico ao do script. |
| **Fontes não carregam** (sem internet / Google Fonts bloqueado) | Comportamento esperado: o `@import` falha em silêncio e o stack cai para `'Helvetica Neue', Helvetica, Arial`. O layout não quebra. Se o usuário exigir a fonte exata offline, embuta-a como `@font-face` com fonte em base64. |
| **`--check` acusa divergência de páginas** (exit 2) | Uma section está vazando conteúdo e criando página extra (ou uma section a menos/a mais no HTML). Confira: cada `<section class="page">` com a altura exata do template, `overflow: hidden` presente, `@page { margin: 0 }` intacto. Ache a página que estourou comparando PDF × HTML página a página. |
| **Texto vazando de card, badge ou tabela** | Reduza o CONTEÚDO, nunca a fonte: encurte a copy (features em até 2 linhas, bullets de 1 linha, máx. 4 sprints por página) ou mova o excedente para outra página. Encolher fonte para "caber" é bug de design. |
| **Fundos pretos/cinzas saem brancos no PDF** | Confirme `print-color-adjust: exact` no CSS (o template já traz); na exportação manual, "Gráficos de fundo" precisa estar marcado. |
| **Soma da tabela não bate com o total** | Nunca ajuste um número por conta própria. Multiplicadores ("3x R$ 40.000") podem ser quantidade ou parcelamento — pergunte ao usuário e só então corrija. |

## Mapa de recursos (progressive disclosure)

Leia cada arquivo apenas na fase indicada — não carregue tudo de uma vez.

| Arquivo | Quando ler |
|---|---|
| `references/descoberta.md` | Início da FASE 1 — protocolo de entrevista/extração dos blocos A–F e confirmação do brief. |
| `references/design-system.md` | FASE 2 (seção 4, adaptação de marca) e FASE 4 (seções 1–3 e 5–6: tokens, gramática visual, especificações dos 10 layouts, tipografia, anti-padrões). |
| `references/estrutura-narrativa.md` | Início da FASE 3 — arco de páginas, variantes de deck, mapeamento brief→páginas e diretrizes de copy. |
| `assets/template.html` | FASE 4 — copiar como base do deck (nunca editar o original). Cabeçalho do arquivo traz instruções de uso, re-branding e troca de logo. |
| `scripts/html2pdf.py` | FASE 5 — conversão HTML→PDF via Edge/Chrome headless; `--check` valida nº de páginas; `--help` documenta opções e fallback. |
| `references/qa-checklist.md` | FASE 5 — checklist obrigatório (Técnica/Visual/Comercial) e formato do reporte ao usuário. |

## Verification

- O briefing, o sumário e as decisões comerciais foram confirmados conforme o procedimento.
- Não restam nomes ou ofertas de exemplo do template; valores, quantidades e condições são rastreáveis ao briefing.
- O HTML abre com a marca correta, sem cortes de conteúdo; o template instalado permanece intacto.
- Quando PDF foi solicitado, o arquivo existe e a quantidade de páginas corresponde às sections; execute `--check` e informe o resultado real.
- O checklist técnico, visual e comercial foi aplicado. Entregue links para os arquivos e identifique qualquer pendência; não declare exportação concluída se apenas gerou HTML.

Proveniência e condições de uso: [SOURCE.md](SOURCE.md) e [LICENSE](LICENSE).
