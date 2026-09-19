---
task: reviewConversionScore()
agent: ce-reviewer
description: "EXCLUSIVO: audit de conversão — above-fold CTA, friction points, social proof placement, urgência, garantias, mobile experience. Score: 0-100"
elicit: false
responsavel: "Audit"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: completePage
    tipo: file
    obrigatorio: true
    descricao: "Página completa com todos os elementos"

Saida:
  - nome: conversionScore
    tipo: file
    obrigatorio: true
    descricao: "Conversion score 0-100: above-fold CTA, friction points, social proof placement, urgência e mobile"

Checklist:
  pre-conditions:
    - "[ ] Página completa disponível"
  post-conditions:
    - "[ ] CTA acima da dobra confirmado"
    - "[ ] Friction points eliminados"
    - "[ ] Social proof posicionado estrategicamente"
---

# Task: reviewConversionScore()

## Objetivo
Realizar o audit de conversão mais crítico de todo o processo — uma avaliação independente e sistemática de todos os elementos que afetam diretamente a taxa de conversão da LP. Esta é a task EXCLUSIVA que determina se a LP está verdadeiramente pronta para converter visitantes em leads ou clientes.

## Inputs Necessários
- Landing page funcionando completamente (formulário, integrações, tracking)
- `cro-design-audit.md` (especificações originais de CRO)
- `intelligence-brief.md` (benchmarks de conversão do nicho)
- Dispositivo mobile real (ou BrowserStack) para teste genuíno
- `review-copy.md` e `review-design.md` (reviews anteriores)

## Processo
1. **Simulação de visita fria** — Abrir a LP em modo incógnito, sem scroll e sem leitura prévia:
   - Em 5 segundos: o que a página oferece está claro? (Clarity Test)
   - Em 10 segundos: para quem é esta oferta?
   - Em 30 segundos: qual é o próximo passo?
   Registrar percepções brutas antes de aplicar a rubrica.

2. **Rubrica de avaliação de conversão (100 pontos):**

   **Above-fold e primeira impressão (25 pontos):**
   - CTA visível sem scroll em mobile (375px) → 0 ou 8 pts (binário)
   - Proposta de valor clara em < 5 segundos → 0-8 pts
   - Design inspire confiança imediatamente (não parece spam/scam) → 0-5 pts
   - Social proof imediata (número de clientes, rating) abaixo do hero → 0-4 pts

   **Fluxo e friction (25 pontos):**
   - Número de campos do formulário ≤ 3 para lead magnet, ≤ 5 para lead qualificado → 0-8 pts
   - Sem links externos distrativos (sem nav, sem footer com links) → 0-5 pts
   - CTA repetido em pelo menos 3 pontos do scroll → 0-6 pts
   - Loading após submit < 3s (testar na rede real) → 0-3 pts
   - Mensagem de sucesso clara e positiva → 0-3 pts

   **Social proof e credibilidade (20 pontos):**
   - Mínimo 3 depoimentos com foto + resultado mensurável → 0-8 pts
   - Pelo menos 1 elemento de autoridade (mídia, certificação, número de clientes) → 0-4 pts
   - Rating/estrelas visíveis → 0-4 pts
   - Trust badges relevantes (garantia, segurança) posicionados corretamente → 0-4 pts

   **Urgência e motivação para agir (15 pontos):**
   - Existe razão legítima para agir AGORA (não "qualquer hora") → 0-8 pts
   - Garantia visível e clara próxima ao CTA → 0-4 pts
   - Risco percebido eliminado (garantia + social proof + segurança) → 0-3 pts

   **Mobile experience (15 pontos):**
   - Testado em dispositivo mobile real (não só DevTools) → 0 ou 15 pts se não testado
   - Formulário fácil de preencher com teclado mobile (campos corretos, autocomplete) → 0-5 pts
   - CTA no tamanho certo para toque (≥ 44px) → 0-3 pts
   - Imagens carregando rápido em mobile (< 3s na rede 4G) → 0-4 pts
   - Sem elementos que requerem hover para funcionar → 0-3 pts

3. **Teste funcional do formulário:**
   - Submeter formulário com dados válidos → verificar sucesso
   - Submeter formulário com email inválido → verificar validação
   - Submeter formulário vazio → verificar mensagens de erro
   - Verificar que lead aparece no backend (admin panel ou banco)
   - Verificar que email de confirmação chega (se configurado)
   - Verificar que WhatsApp dispara (se configurado)
   - Verificar que lead aparece no CRM (se configurado)

4. **Teste de velocidade de carregamento em condições reais:**
   - Usar WebPageTest.org com conexão "4G" e localização São Paulo
   - Registrar: LCP, CLS, TTI, tamanho total
   - LCP < 2.5s em 4G (bloqueante se > 4s)

5. **Verificação de tracking de conversão:**
   - Submeter lead de teste
   - Verificar evento `lead_submitted` no GA4 DebugView
   - Verificar evento `Lead` no Meta Events Manager Test Events
   - Verificar que conversion tracking do Google Ads disparou
   - Verificar que server-side tracking foi enviado (backend logs)

6. **Checklist de itens bloqueantes para GO/NO-GO:**
   - [ ] CTA visível acima da dobra em mobile 375px
   - [ ] Formulário funcional (submit → sucesso → lead criado no backend)
   - [ ] Página carregando em < 4s em conexão 4G real
   - [ ] Tracking de conversão funcionando (GA4 + Meta)
   - [ ] Nenhum erro de JavaScript no console (F12 → Console)
   - [ ] HTTPS ativo (não HTTP) → verificar cadeado no browser
   - [ ] Garantia visível próxima ao CTA principal

## Veto Conditions
- CTA não visível acima da dobra em mobile → GO/NO-GO = NO-GO (bloqueante)
- Formulário não funcionando → GO/NO-GO = NO-GO (bloqueante)
- Nenhum tracking de conversão funcionando → GO/NO-GO = NO-GO (bloqueante)
- Página com erro de JavaScript quebrando funcionalidade → NO-GO
- Score < 70 → retornar ao squad com lista prioritária antes do lançamento

## Output Esperado
Arquivo `review-conversion.md` contendo:
- Resultado do "Clarity Test" (primeiros 30 segundos)
- Score por critério (above-fold, friction, social proof, urgência, mobile)
- Resultado dos testes funcionais (formulário, tracking)
- Resultado do teste de velocidade (LCP, CLS, score real)
- Checklist GO/NO-GO com resultado por item
- Problemas bloqueantes vs melhorias opcionais
- Score total (0-100)
- Veredicto final: GO / NO-GO para lançamento

## Completion Criteria
- [ ] Clarity Test executado (5s, 10s, 30s documentados)
- [ ] Score calculado para todos os 5 critérios
- [ ] Formulário testado: válido + inválido + vazio
- [ ] Lead criado no backend verificado
- [ ] Email de confirmação recebido (se configurado)
- [ ] Tracking GA4 + Meta verificado em evento real
- [ ] Teste de velocidade via WebPageTest (LCP documentado)
- [ ] Teste em dispositivo mobile real (não só DevTools)
- [ ] Checklist GO/NO-GO preenchida
- [ ] Score total calculado (0-100)
- [ ] Veredicto GO ou NO-GO emitido com justificativa
- [ ] Arquivo `review-conversion.md` criado
