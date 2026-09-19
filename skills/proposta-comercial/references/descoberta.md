# Descoberta — protocolo pré-geração

Este protocolo roda **antes** de qualquer proposta ser gerada. O objetivo é preencher os
6 blocos de informação abaixo com o mínimo de fricção: primeiro **extrair** de materiais
que o usuário já forneceu, depois **perguntar** apenas o que faltar, e por fim
**confirmar** o brief consolidado antes de passar à geração.

---

## Regra de ouro

> **NUNCA invente preços, prazos, features, nomes de produtos, nomes de pessoas ou
> promessas.** Tudo que aparece na proposta vem do usuário ou dos materiais dele.
> Se uma informação necessária não existir, **pergunte** — não preencha com suposição,
> não use "valores típicos de mercado", não complete listas de features por conta própria.
> Placeholder só existe dentro do template; na proposta entregue, zero invenção.

---

## Ordem de operação

1. **Inventariar materiais fornecidos** (mensagens, arquivos anexados, URLs citadas).
2. **Extrair automaticamente** tudo que der (seção "Extração automática" abaixo).
3. **Marcar cada bloco A–F** como: `completo`, `parcial` ou `vazio`.
4. **Entrevistar** só sobre o que está `parcial`/`vazio` — máximo de 3–4 perguntas por
   mensagem. Comece pelo que bloqueia a geração (ver tabela "Mínimo viável").
5. **Consolidar e confirmar** o brief com o usuário antes de gerar qualquer HTML.

---

## Extração automática (SEMPRE antes de perguntar)

Perguntar algo que o material já responde queima a confiança do usuário. Por isso:

### Site do usuário (ou do cliente dele)
- Se o usuário citou uma URL, use **WebFetch** para ler o site.
- Extrair: nome/marca como escrita oficialmente, o que a empresa faz, tom de voz
  (formal? direto? técnico?), produtos/serviços listados, cores predominantes se
  descritas, claims e frases de posicionamento reutilizáveis.
- Preenche principalmente os **blocos A e B**.

### PDFs e arquivos (brief, brand guide, apresentação institucional)
- Use **Read** em cada arquivo fornecido (`.pdf`, `.md`, `.txt`, `.docx` convertido).
- De um **brand guide**: cores exatas (hex), fontes, regras de uso do logo, caminho do
  arquivo de logo — alimenta a fase de brand-config.
- De um **brief**: qualquer campo dos blocos A–F que estiver escrito. Copiar valores
  literalmente (preços, prazos, nomes) — nunca "arredondar" nem parafrasear números.

### Transcrições de calls de vendas
- Fonte mais valiosa de todas. Ler por inteiro e extrair:
  - **Dores literais do cliente**, nas palavras dele ("a gente perde lead no fim de
    semana", "meu time não dá conta do pós-venda"). Guardar as citações — elas viram
    o texto da página de contexto e dos parágrafos de entregáveis, porque proposta
    que ecoa as palavras do cliente fecha mais.
  - O que foi **efetivamente prometido/combinado** na call: escopo, prazos mencionados,
    valores discutidos, objeções e como foram respondidas.
  - Nomes das pessoas (decisor, contato) e como o cliente chama o próprio negócio.
- Atenção: transcrição contém especulação e negociação. Só entra na proposta o que foi
  **acordado ou confirmado pelo usuário** — na dúvida, listar e perguntar
  "isso ficou fechado ou ainda está em aberto?".

---

## Os 6 blocos de informação

Para cada bloco: as perguntas abaixo são o roteiro de entrevista. Faça apenas as que a
extração automática não respondeu, em grupos de **no máximo 3–4 perguntas por mensagem**.

### Bloco A — Quem vende (o usuário da skill)

| Campo | Obrigatório? |
|---|---|
| Nome/marca (grafia exata) | Sim |
| O que a empresa faz (1 frase) | Sim |
| Logo (arquivo SVG/PNG) ou aceitar monograma tipográfico | Não |
| Site, cores da marca, tom de voz | Não |

Perguntas:
1. Qual o nome da sua empresa/marca, exatamente como deve aparecer na proposta?
2. Em uma frase: o que vocês fazem e para quem?
3. Você tem logo em SVG ou PNG e um site que eu possa analisar? Se sim, me passe o
   caminho/URL.

### Bloco B — Para quem (o cliente da proposta)

| Campo | Obrigatório? |
|---|---|
| Nome da empresa cliente (grafia exata) | Sim |
| Setor/contexto do negócio | Recomendado |
| Nome do contato/decisor | Não |
| Dor ou motivação principal | Recomendado |

Perguntas:
1. Para qual empresa é esta proposta? Confirme a grafia exata do nome.
2. Qual o principal problema ou objetivo que levou esse cliente até você?
3. Tem alguma call, e-mail ou anotação dessa negociação que eu possa ler? (Se tiver,
   eu uso as palavras do próprio cliente no texto.)

### Bloco C — Oferta (produtos/serviços)

| Campo | Obrigatório? |
|---|---|
| Lista de produtos/serviços com nome de cada um | Sim (mínimo 1) |
| Features por produto (ideal 6–8; mínimo 3) | Sim |
| Opcionais/upsells (ex.: consultoria mensal) | Não |

Perguntas:
1. Quais produtos ou serviços entram nesta proposta? Liste os nomes.
2. Para cada um: quais são as entregas/features concretas? (O ideal são 6 a 8 por
   produto — se me der menos, eu pergunto, nunca completo sozinho.)
3. Existe algum item opcional/upsell que deva aparecer como "(Opcional)"?

### Bloco D — Execução (cronograma e prazo)

| Campo | Obrigatório? |
|---|---|
| Prazo total do projeto | Sim |
| Fases/sprints com nome, duração e atividades | Recomendado |
| Observações (ex.: possibilidade de entrega antecipada) | Não |

Perguntas:
1. Qual o prazo total do projeto?
2. Como você divide a execução em fases ou sprints? (Nome de cada fase, duração e
   2–4 atividades por fase.)
3. Alguma observação sobre prazo que valha registrar (ex.: "pode sair antes")?

### Bloco E — Comercial (preços e condições)

| Campo | Obrigatório? |
|---|---|
| Preço por item OU preço total fechado | Sim (total é obrigatório) |
| Condições de pagamento (à vista, parcelado, entrada) | Sim |
| Valor de opcionais/mensalidades | Se houver opcional |

Perguntas:
1. Qual o valor total do investimento?
2. Quanto custa cada item individualmente? (A tabela da proposta lista item a item —
   a soma precisa bater com o total.)
3. Quais as condições de pagamento (à vista, parcelas, entrada + parcelas)?
4. Se houver opcionais: qual o valor e a recorrência de cada um (ex.: R$ X/mês)?

Cuidado com multiplicadores: se o usuário disser "3x R$ 40.000", confirmar se é
**3 unidades** de R$ 40.000 (soma R$ 120.000) ou **3 parcelas** (soma R$ 40.000 ou
R$ 120.000 dependendo do combinado). Nunca decidir sozinho.

### Bloco F — Extras (opcional)

| Campo | Obrigatório? |
|---|---|
| Depoimentos/cases | Não |
| Garantias | Não |
| Outros anexos (equipe, metodologia) | Não |

Pergunta única (fazer só se os blocos A–E já estiverem resolvidos):
1. Quer incluir páginas extras — depoimentos, cases, garantias? Se sim, me passe o
   conteúdo exato (nunca vou redigir um depoimento ou uma garantia por conta própria).

---

## Mínimo viável vs. ideal

| Campo | Mínimo viável para gerar | Ideal |
|---|---|---|
| Quem vende | Nome/marca | + logo, site, cores, tom de voz |
| Cliente | Nome da empresa | + setor, contato, dor nas palavras do cliente |
| Oferta | 1 produto com **3+ features** | 2–4 produtos com 6–8 features cada + opcional |
| Execução | Prazo total | + 4–8 sprints nomeados com atividades |
| Comercial | **Preço total** | + preço por item, condições, opcionais mensais |
| Extras | — (nada) | Depoimentos, cases, garantias |

- **Abaixo do mínimo viável: não gerar.** Explique ao usuário exatamente o que falta e
  pergunte.
- **No mínimo viável (mas sem o ideal): pode gerar**, avisando quais páginas ficarão de
  fora (ex.: sem sprints detalhados, o deck sai sem as páginas de timeline — só a página
  de prazo).

---

## Confirmação do brief (obrigatória)

Antes de passar para a geração, mostrar ao usuário o **brief consolidado** em resumo
estruturado, neste formato:

```
BRIEF DA PROPOSTA — confirme antes de eu gerar

Quem vende:   <nome> — <o que faz> — logo: <arquivo/monograma>
Cliente:      <empresa> — <setor> — contato: <nome ou "não informado">
Dor/contexto: <resumo em 1–2 frases, com citações da call se houver>

Oferta:
  1. <Produto A> — <n> features: <lista curta>
  2. <Produto B> — ...
  Opcional: <item> — <valor/recorrência>

Execução:     <prazo total> — <n> sprints: <nomes>
Comercial:    Total <R$ X> — condições: <à vista/parcelado> 
              Itens: <item = valor, ...> (soma conferida: <R$ X>)
Extras:       <depoimentos/cases/garantias ou "nenhum">

Páginas previstas: <n> (<lista dos tipos de página>)
```

Perguntar explicitamente: **"Está tudo correto? Posso gerar a proposta com base nisso?"**

- Só avançar para a geração após o "sim" do usuário.
- Se o usuário corrigir algo, atualizar o brief, reexibir o resumo e confirmar de novo.
- Registrar no resumo a soma dos itens comerciais já conferida — se a soma dos itens não
  bater com o total informado, resolver **aqui**, nunca na página de investimento.
