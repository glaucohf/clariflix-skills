# Validar e Onboardar Novo Embaixador

**Task ID:** `validate-onboard-ambassador`
**Pattern:** HO-TP-010
**Version:** 1.0.0
**Responsible executor:** Hub Chief (orquestra) → Hub Members (acolhimento) + Hub Content (mensagens)

## Overview

Conduzir um candidato a Embaixador Lendário do recebimento da candidatura (Tally) até o
onboarding completo, passando pela call de alinhamento e pela aprovação oficial.

Cobre o ciclo de ponta a ponta: **triagem → call de alinhamento → aceite → aprovação no app →
acesso ao painel → entrada nos grupos → All-Hands → tag no Circle**.

Esta task NÃO substitui o app `hub.lendario.ai` (onde a aprovação formal acontece). Ela
**orquestra a jornada**, prepara as mensagens e mantém o mapa de status de cada candidato,
para Rodrigo não perder nenhuma etapa nem nenhum candidato.

> **Quando usar:** sempre que houver candidaturas pendentes de marcar a primeira reunião,
> ou ao iniciar uma nova turma/lote de embaixadores.

---

## Atores

- **Rodrigo** — operador, avaliador e decisor único do fluxo (aprova, faz a call, dá acesso)
- **Candidato** — pessoa que se candidatou via Tally
- **Hub Chief** — orquestra a jornada, mantém o mapa de status
- **Hub Members / Hub Content** — geram mensagens de cada etapa

---

## Inputs

| Input | Obrigatório | Fonte |
|-------|-------------|-------|
| `tally_link` | sim (fonte da verdade) | `https://tally.so/forms/3yR2J6/submissions` (ver `data/sources-of-truth.yaml`) |
| `csv_app_export` | opcional (reconciliação) | CSV exportado do app do Claus (candidaturas pendentes) |
| `lote_id` | opcional | rótulo da turma (ex.: `2026-06`) |

## Outputs

- Lista de candidaturas a avaliar (triagem)
- Relatório de reconciliação Tally × app (quais não sincronizaram)
- Mensagens prontas por etapa (aprovação prévia + convite call, boas-vindas, apresentação)
- Mapa de status por candidato (alimenta o fluxograma `docs/ambassador-onboarding-flow.html`)

---

## As 9 etapas da jornada

> Estado real do sistema anotado em cada etapa (`✅` roda no app · `🟡` parcial/manual no app ·
> `⚪` manual externo · `🔴` ainda sem suporte no app). Fonte: análise verificada do código/banco
> do `hub-lendario` (2026-06-16).

| # | Etapa | Fase | Onde acontece | Estado |
|---|-------|------|---------------|--------|
| 0 | Candidato lê a página e se candidata | entrada | landing `/embaixadores` → form Tally | ⚪ Tally externo |
| 1 | **Triagem da candidatura** | validação | app admin (`triar_candidatura`) + esta task | ✅ / aqui orquestrado |
| 2 | **Call de alinhamento** (grupo ou individual) | validação | WhatsApp + call | ⚪ manual — *disparada pela mensagem de aprovação prévia* |
| 3 | **Aceite oficial na call + próximos passos** | validação | call | ⚪ manual |
| 4 | **Aprovar candidatura no app** | aprovação | `hub.lendario.ai/admin` | 🔴 status `aprovada` ainda sem botão no app — hoje é decisão manual |
| 5 | **Acesso ao painel** (e-mail + senha) | onboarding | `criarAcessoEmbaixador` (painel admin) | 🟡 funciona, mas e-mail digitado à mão; senha via tela Supabase |
| 6 | **Grupo WhatsApp + boas-vindas** | onboarding | WhatsApp | ⚪ manual |
| 7 | **Apresentação oficial no grupo do hub** | onboarding | WhatsApp do hub local | ⚪ manual |
| 8 | **Adicionar e-mail ao convite do All-Hands** | onboarding | Calendar/convite | ⚪ manual |
| 9 | **Tag no Circle que libera espaços** | onboarding | Circle | ⚪ manual |

---

## Action Items

### Fase A — Triagem (etapa 1)

1. **Carregar candidaturas da fonte da verdade (Tally).**
   - Tentar via `tally` MCP (form `3yR2J6`). Se o MCP não estiver autorizado, pedir a Rodrigo
     o link de autorização OU o CSV exportado.
2. **Reconciliar Tally × app (se CSV fornecido).**
   - Comparar por e-mail. Apontar candidaturas que estão no Tally mas **não** no CSV do app
     (sintoma da dessincronia Tally→app do Claus, em conserto). Sinalizar para Rodrigo não
     perder ninguém, já que ele acompanha pelo app.
   - Marcar também candidaturas sem `Data Candidatura` (possível sintoma de migração incompleta).
3. **Listar as candidaturas a avaliar** (sem ranquear, salvo pedido): Nome · Hub · Score IA ·
   Aprovado IA · status de sincronia.
4. **Perguntar a Rodrigo quais seguem** para a call. Não decidir por ele.
   - Detectar e sinalizar **hubs duplicados** (2+ candidatos na mesma cidade) antes de seguir.

### Fase B — Call e aprovação (etapas 2–4)

5. **Gerar a mensagem de aprovação prévia + convite para call** usando
   `templates/ambassador-approval-message-tmpl.md` (versões: individual, enxuta, grupo).
   - Personalizar com nome, cidade/hub e, se possível, um elogio concreto da candidatura.
   - Voz do Rodrigo: tratamento **você/seu** (nunca tu/tua). Tom caloroso-Lendário.
6. **Registrar o aceite** após a call (atualizar status do candidato no mapa).
7. **Lembrar Rodrigo de aprovar no app** (`hub.lendario.ai/admin`) — etapa 4. Anotar que o
   status `aprovada` ainda não tem botão no app (gap conhecido) → confirmar manualmente.

### Fase C — Onboarding (etapas 5–9)

8. **Conceder acesso ao painel** — orientar Rodrigo a usar o painel "Acesso de Embaixadores"
   (`criarAcessoEmbaixador`) com o e-mail do candidato.
9. **Gerar as mensagens de onboarding** (boas-vindas no grupo de embaixadores, apresentação no
   grupo do hub local) via Hub Content / `templates/`.
10. **Checklist final dos combinados mínimos** confirmados com o embaixador:
    - 🎯 1 objetivo único do hub agora
    - 🤝 ≥ 1 encontro presencial/mês
    - 📋 envio do formulário de relatório mensal
    - 📣 participação no All-Hands mensal
11. **Atualizar o fluxograma** (`docs/ambassador-onboarding-flow.html`) com o bloco de status
    de cada embaixador da jornada.

---

## Acceptance Criteria

- Toda candidatura do Tally foi considerada (nenhuma perdida na dessincronia com o app).
- Hubs duplicados foram sinalizados antes da call.
- Rodrigo decidiu quais candidatos seguem — a task nunca aprova/recusa por ele.
- Cada candidato que segue tem mensagem de aprovação prévia + convite de call pronta na voz dele.
- Os 4 combinados mínimos foram comunicados antes do candidato assumir o hub.
- O mapa de status (fluxograma) reflete a etapa atual de cada embaixador.

## Veto Conditions

- Não seguir se a candidatura não puder ser confirmada na fonte da verdade (Tally).
- Não marcar candidato como "aprovado" sem o aceite na call (etapa 3) registrado.
- Não prometer benefício automático — todos os incentivos são avaliados caso a caso.

## Anti-Patterns

- Aprovar pela planilha sem a call de alinhamento.
- Mensagem fria/burocrática ou com tratamento "tu/tua" (quebra a voz do Rodrigo).
- Confiar só no app do Claus quando há dessincronia conhecida com o Tally.
- Dois embaixadores na mesma cidade sem decisão consciente (co-embaixador é caso a caso).

## Dependencies

- `templates/ambassador-approval-message-tmpl.md`
- `templates/onboarding-message-tmpl.md`
- `data/sources-of-truth.yaml`
- `docs/ambassador-onboarding-flow.html`
- Tasks vizinhas: `onboard-hub-member.md` (membro ≠ embaixador), `create-hub-post.md`
