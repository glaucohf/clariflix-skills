# conferencia-orcamento · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: conferencia-orcamento
description: "Monta uma proposta de orçamento a partir da tabela de preço, margens e descontos permitidos, com total que fecha exatamente com a tabela. Use: \"monta o orçamento para\", \"faz a proposta de preço\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [orcamento, precificacao, pme]
    related_skills: [conferencia-planilha]
---

# ORÇAMENTO · monta proposta a partir de tabela

Monta uma proposta de orçamento para um cliente a partir da tabela de preço vigente, aplicando apenas margens e descontos que o dono do negócio autorizou — nunca inventa valor.

## When to Use

- Diga: "monta o orçamento para [cliente/serviço]".
- Use quando já existe uma tabela de preço e regras de desconto definidas pelo dono.
- NÃO use se não houver tabela de preço confirmada — nesse caso, primeiro confirme os valores com o dono; não estime.

## Quick Reference

| procedimento | referência |
|---|---|
| regras de desconto por faixa | `references/regras-desconto.md` |

| apoio | arquivo |
|---|---|
| template de proposta | `templates/proposta.md` |

## Procedure

1. **Confirme a tabela de preço vigente** — peça a versão mais recente; nunca use uma tabela "de cabeça" sem confirmar a data.
2. **Liste os itens/serviços pedidos** com a quantidade e o valor unitário da tabela.
3. **Aplique desconto apenas se estiver nas regras autorizadas** (`references/regras-desconto.md`) — se o pedido de desconto for maior que o autorizado, sinalize para o dono decidir, não decida sozinho.
4. **Calcule o total** e confira que ele bate exatamente com tabela × quantidade × (1 - desconto aplicado) — sem arredondamento silencioso.
5. **Entregue a proposta** no formato `templates/proposta.md`, com a data de validade dos preços.

## Pitfalls

- Aplicar desconto "porque o cliente pediu" sem checar a regra autorizada corrói a margem sem o dono perceber.
- Usar tabela desatualizada gera orçamento errado que pode virar compromisso com o cliente.
- Arredondar o total "para ficar redondo" sem documentar o motivo quebra a rastreabilidade do orçamento.

## Verification

Passou se: todo item do orçamento tem origem rastreável na tabela vigente (com data); todo desconto aplicado está dentro da regra autorizada, ou foi escalado para decisão do dono; o total bate exatamente com o cálculo, sem arredondamento não documentado.


## Referência: references/regras-desconto.md

# Regras de desconto — perguntar ao dono antes de aplicar

| faixa | desconto máximo autorizado | quem aprova acima disso |
|---|---|---|
| [ex.: até R$500] | [ex.: 5%] | [ex.: o próprio atendente] |
| [ex.: acima de R$500] | [ex.: 10%] | [ex.: o dono] |

Nunca aplique desconto fora da tabela sem essa confirmação explícita — mesmo que o cliente insista ou pareça "razoável".


## Referência: templates/proposta.md

# Proposta de orçamento — [cliente]

**Tabela vigente de:** [data]

| item | quantidade | valor unitário | desconto | subtotal |
|---|---|---|---|---|

**Total:** [valor] · **Válido até:** [data]
