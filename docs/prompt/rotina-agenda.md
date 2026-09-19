# rotina-agenda · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: rotina-agenda
description: "Define as regras de agendar, remarcar e confirmar sem duplicar horário nem gerar no-show: slots, confirmação D-1, política de remarcação. Use: \"organiza a agenda\", \"regras de agendamento\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [agenda, agendamento, pme, rotina]
    related_skills: [atendimento-triagem-whatsapp, rotina-follow-up]
---

# AGENDA · agendar, remarcar, confirmar

Define as regras de agendamento de um negócio — tamanho do slot, o que fazer com pedidos que não cabem na grade, como confirmar 1 dia antes e como tratar remarcação e no-show — para que agendar não dependa de decorar exceções.

## When to Use

- Diga: "organiza a agenda de [negócio]" ou "define as regras de agendamento".
- Use quando o agendamento hoje depende só da memória de quem atende, ou quando há duplicidade/no-show frequente.
- NÃO use para o roteiro de conversa que leva à agenda (`atendimento-triagem-whatsapp`, que encaminha para cá).

## Quick Reference

| procedimento | referência |
|---|---|
| como definir o tamanho do slot | `references/tamanho-de-slot.md` |
| política de confirmação e no-show | `references/confirmacao-noshow.md` |

| apoio | arquivo |
|---|---|
| template das regras de agenda | `templates/regras-agenda.md` |

## Procedure

1. **Defina o tamanho do slot** por tipo de serviço (`references/tamanho-de-slot.md`) — nem todo serviço cabe no mesmo tempo; agendar todos do mesmo jeito é a causa mais comum de atraso em cadeia.
2. **Escreva a regra de encaixe**: o que fazer quando alguém pede um horário que não existe na grade — lista de espera, próximo slot livre, ou recusa educada com alternativa.
3. **Defina a confirmação D-1**: mensagem automática 1 dia antes, com opção de confirmar ou remarcar em 1 clique/resposta.
4. **Escreva a política de remarcação e no-show** (`references/confirmacao-noshow.md`): quantas remarcações são aceitas sem custo, o que acontece após não comparecer sem avisar.
5. **Feche o loop**: toda remarcação ou cancelamento libera o slot imediatamente para outra pessoa — nunca fica "reservado" sem confirmação.
6. **Entregue** no formato `templates/regras-agenda.md`.

## Pitfalls

- Slot único para serviços de duração diferente gera atraso que se acumula ao longo do dia.
- Confirmação D-1 sem opção fácil de remarcar vira no-show silencioso (a pessoa esquece de avisar que não vai poder ir).
- Política de no-show sem consequência nenhuma não muda comportamento; sem consequência nenhuma proporcional, gera atrito. Ache o meio-termo do negócio.

## Verification

Passou se: existe 1 tamanho de slot por tipo de serviço (não um genérico para tudo); a mensagem de confirmação D-1 tem uma ação clara de confirmar/remarcar; a política de no-show está escrita e é a mesma para todo mundo; nenhuma regra depende de "perguntar para fulano".


## Referência: references/confirmacao-noshow.md

# Confirmação D-1 e política de no-show

**Confirmação:** mensagem automática 24h antes, com resposta de 1 toque ("Confirmar" / "Preciso remarcar"). Quem não responde até X horas antes recebe 1 lembrete adicional.

**Remarcação:** defina um número de remarcações gratuitas por período (ex.: 1 por mês) antes de cobrar ou exigir confirmação antecipada.

**No-show (faltou sem avisar):** defina a consequência com o dono do negócio — pode ser desde nada (aceitável para negócios com fila de espera) até exigir sinal para o próximo agendamento. Escreva a regra e aplique igual para todos.


## Referência: references/tamanho-de-slot.md

# Tamanho de slot por tipo de serviço

Pergunte, para cada tipo de serviço: "quanto tempo, do início ao fim, incluindo preparo e limpeza/troca?" — não só o tempo "de mãos na massa".

| serviço | duração real | slot recomendado (+ margem) |
|---|---|---|
| [ex.: corte simples] | 25 min | 30 min |
| [ex.: consulta de avaliação] | 45 min | 60 min |

Margem sugerida: 10-15% do tempo real, para absorver pequenos atrasos sem afetar o próximo horário.


## Referência: templates/regras-agenda.md

# Regras de agenda — [nome do negócio]

## Slots por serviço
| serviço | duração | slot |
|---|---|---|

## Encaixe
Quando não há horário: [lista de espera / próximo slot livre / recusa com alternativa]

## Confirmação D-1
[texto da mensagem automática]

## Remarcação e no-show
- Remarcações gratuitas por período: [n]
- Consequência de no-show: [regra]
