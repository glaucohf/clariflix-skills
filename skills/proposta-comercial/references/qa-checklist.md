# QA Checklist — controle de qualidade pré-entrega

**Rode este checklist SEMPRE antes de entregar a proposta ao usuário** — tanto na primeira
versão quanto após qualquer rodada de ajustes. Nenhuma proposta é considerada pronta sem
os três blocos verificados (Técnica, Visual, Comercial).

Ao terminar, **reporte o resultado ao usuário** em formato compacto:

```
QA da proposta — resultado
Tecnica:   X/Y ok
Visual:    X/Y ok
Comercial: X/Y ok
Pendencias: <lista do que falhou e o que foi feito, ou "nenhuma">
```

Itens que falharem devem ser corrigidos e re-verificados antes da entrega. Itens do bloco
COMERCIAL que dependam de confirmação do usuário (valores, promessas) **bloqueiam a
entrega** até a resposta dele.

---

## 1. TÉCNICA

Verificações sobre o arquivo HTML e o PDF exportado.

- [ ] **HTML abre sem erros**: abrir o arquivo no navegador (`start <arquivo>.html`) e
      conferir que renderiza; sem erros no console (F12) que afetem o layout.
- [ ] **Proporção das sections**: todas as `<section class="page">` têm a proporção 2:1
      (1280×640 base) — nenhuma página esticada, cortada ou com altura diferente das demais.
- [ ] **Contagem de páginas na impressão**: o PDF gerado tem **exatamente N páginas**,
      onde N = número de `<section>` no HTML. Sem páginas em branco extras no meio ou no
      fim (causa comum: margem/overflow empurrando conteúdo — corrigir com
      `page-break-after` e `@page { margin: 0 }`). Usar `scripts/html2pdf.py --check`.
- [ ] **Cores de fundo na impressão**: fundos pretos/cinzas aparecem no PDF
      (`-webkit-print-color-adjust: exact` / `print-color-adjust: exact` presentes; se a
      exportação for manual, "Gráficos de fundo" marcado).
- [ ] **Fontes**: a fonte principal carrega; se a Google Font falhar (sem internet), o
      fallback do stack (`Helvetica Neue, Helvetica, Arial, sans-serif`) mantém o deck
      legível e sem quebra de layout.
- [ ] **Zero texto vazando**: nenhum texto escapa de card, tabela, badge ou section —
      conferir especialmente nomes longos de produto nos cards de feature, valores na
      tabela de investimento e títulos gigantes das divisórias.
- [ ] **PDF final conferido página a página**: abrir o PDF exportado e passar por TODAS as
      páginas, uma a uma, comparando com o HTML. Não entregar PDF que não foi aberto.

## 2. VISUAL

Fidelidade ao design system (ver `design-system.md`) e ao brand-config do usuário.

- [ ] **Tokens respeitados**: cores usadas são exatamente as do brand-config/tokens
      (fundos, muted, acentos) — nenhuma cor "aproximada" inventada durante a geração.
- [ ] **Rodapé em todas as páginas exceto o fechamento**: 4 colunas
      ("Proposta Comercial" | marca do usuário | "©" | ano), low-contrast, presente em
      todas as sections menos a última (fechamento com logo centralizado).
- [ ] **Ênfase bold com parcimônia**: parágrafos em cinza muted com apenas trechos-chave
      em bold — se mais da metade de um parágrafo está em bold, a ênfase morreu; reescrever.
- [ ] **Nenhum placeholder esquecido**: buscar no HTML por `{{`, `}}`, "LOREM", "TODO",
      "Studio Vetor", "Café Aurora" (conteúdo de exemplo do template) — zero ocorrências.
- [ ] **Logo correto**: logo do usuário (ou monograma acordado) nas páginas de conteúdo,
      no tamanho/posição do padrão (topo-direito); nunca o logo de exemplo do template.
- [ ] **Ano correto**: capa e rodapé exibem o ano atual (ou o ano informado pelo usuário)
      — não o ano do template.
- [ ] **Ritmo de fundos respeitado**: a alternância claro → escuro → respiro → claro →
      pontuação escura segue o arco definido em `estrutura-narrativa.md`; divisórias de
      uma palavra com ponto final ("Entregáveis.", "Cronograma.", "Investimento.");
      nenhuma sequência longa de páginas iguais que quebre o drama do deck.

## 3. COMERCIAL

O bloco mais crítico: erro aqui custa dinheiro ou credibilidade do usuário.

- [ ] **Valores conferidos com o usuário**: todos os preços exibidos foram informados ou
      confirmados por ele — nenhum valor estimado ou "completado".
- [ ] **Soma da tabela bate com o total**: somar linha a linha a tabela de investimento e
      conferir contra o "Investimento Total". Atenção a multiplicadores ("3x R$ 40.000"):
      confirmar com o usuário se é quantidade (entra 120.000 na soma) ou parcelamento —
      se a soma não bater, **parar e perguntar**, nunca ajustar um número por conta própria.
- [ ] **Nomes grafados corretamente em TODAS as ocorrências**: nome da empresa cliente e
      nome/marca do usuário — capa, contexto, rodapés, tabela, texto corrido. Buscar cada
      variação de grafia no HTML para garantir consistência (ex.: "XFlow" vs "Xflow").
- [ ] **Features correspondem ao que foi vendido**: cada card de feature veio do brief
      confirmado — nenhuma feature adicionada, renomeada ou "melhorada" na geração.
- [ ] **Prazo consistente**: a soma/duração dos sprints do cronograma é compatível com o
      prazo total da página de prazo (ex.: sprints somando 90 dias ↔ "prazo de 90 dias").
      Datas ou faixas de dias sem contradição entre páginas.
- [ ] **Condições de pagamento explícitas**: a página de investimento diz claramente como
      se paga (à vista, parcelas, entrada) e o que está incluído; opcionais marcados como
      opcionais, com valor e recorrência ("R$ X/mês") corretos.
- [ ] **Nenhuma promessa que o usuário não fez**: varrer o texto por garantias, prazos de
      resposta, SLAs, resultados prometidos ("aumento de X%", "sem custos adicionais") —
      cada afirmação dessas precisa existir no brief confirmado; o que não veio dele, sai.

---

## Regra final

Se qualquer item comercial estiver em dúvida, a resposta certa nunca é "provavelmente está
certo" — é perguntar ao usuário. Uma proposta atrasada em cinco minutos é melhor que uma
proposta entregue com o preço errado.
