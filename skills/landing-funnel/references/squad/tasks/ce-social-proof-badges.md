---
task: designTrustBadges()
agent: ce-social-proof
description: "Definir e posicionar trust badges: certificações, mídia citada, número de clientes, garantias, parceiros"
elicit: false
responsavel: "Trust"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: credentials
    tipo: object
    obrigatorio: true
    descricao: "Certificações, parcerias, menções na mídia e números de clientes"

Saida:
  - nome: trustBadges
    tipo: file
    obrigatorio: true
    descricao: "Trust badges definidos e posicionados: certificações, mídia, número de clientes e garantias"

Checklist:
  pre-conditions:
    - "[ ] Credenciais verificadas"
  post-conditions:
    - "[ ] Badges posicionados acima da dobra"
    - "[ ] Garantias com destaque visual"
    - "[ ] Logos de clientes/parceiros incluídos"
---

# Task: designTrustBadges()

## Objetivo
Definir, criar e posicionar estrategicamente os trust badges da landing page — elementos visuais que constroem credibilidade instantânea sem requerer que o visitante leia texto. Trust badges bem posicionados reduzem ansiedade de compra e eliminam objeções de credibilidade nos segundos críticos antes da conversão.

## Inputs Necessários
- `social-proof-audit.md` (certificações, parceiros, mídia disponíveis)
- `product-brief.md` (garantia oferecida, número de clientes, certificações)
- `cro-design-audit.md` (Cialdini — onde posicionar cada badge)
- `sections-design-spec.md` (seções onde badges serão inseridos)
- `design-system-decision.md` (paleta e estilo visual)

## Processo
1. **Inventário de trust assets** — Catalogar todos os elementos disponíveis:

   **Autoridade e credibilidade:**
   - Certificações profissionais ou de produto
   - Prêmios e reconhecimentos do setor
   - Anos de mercado / fundação
   - Número de clientes atendidos (se > 100)
   - Parceiros e integrações reconhecidas
   - Aparições em mídia (Exame, G1, Valor Econômico, podcasts relevantes)

   **Segurança de transação:**
   - SSL/HTTPS (verificar que site usa HTTPS)
   - Métodos de pagamento aceitos (Visa, Mastercard, Pix, etc.)
   - Proteção de dados (LGPD compliance)
   - Garantia (dias + condições)

   **Prova social numérica:**
   - "X+ clientes atendidos"
   - "X projetos entregues"
   - "X anos de experiência"
   - "Avaliação X/5 com X reviews"
   - "X% de satisfação"

2. **Design de cada badge** — Para cada elemento, definir:

   **Badge de Garantia** (mais importante):
   - Formato: Círculo ou shield com texto interno
   - Conteúdo: "Garantia de [X] dias" + "Devolução integral" ou condição específica
   - Posição recomendada: Próximo ao CTA principal e próximo ao preço
   - Estilo: SVG com ícone de shield (Lucide: `ShieldCheck`) + texto
   - Variantes: Light e dark mode

   ```tsx
   // Componente de exemplo
   <div className="flex items-center gap-2 text-sm text-muted-foreground">
     <ShieldCheck className="h-5 w-5 text-green-500" />
     <span>Garantia de <strong>30 dias</strong> — devolução total sem perguntas</span>
   </div>
   ```

   **Badge de Número de Clientes:**
   - Formato: Inline com ícone de pessoas
   - Conteúdo: "[N]+ empresas confiam em nós"
   - Posição: Hero (abaixo do CTA) ou barra de social proof
   - Estilo: Avatares empilhados (3-4 avatares genéricos) + contador

   **Badge de Mídia Citada ("Como visto em"):**
   - Formato: Logos em fundo neutro com header "Como visto em"
   - Logos em escala de cinza (mais profissional, menos distração)
   - Posição: Logo abaixo do hero ou na seção de autoridade
   - Tamanho: 80-120px de largura, altura consistente (32-40px)

   **Badge de Segurança de Pagamento:**
   - Logos de métodos de pagamento (Visa, Mastercard, Pix, Boleto se aplicável)
   - Ícone de cadeado/SSL
   - Posição: Próximo ao formulário de checkout ou CTA de compra
   - Tamanho: Pequeno e discreto (não deve competir com o CTA)

   **Rating Badge:**
   - Stars SVG animadas + "X.X/5.0 baseado em [N] avaliações"
   - Posição: Abaixo do hero (social proof bar) ou na seção de depoimentos

3. **Posicionamento estratégico de cada badge na LP** — Baseado nos princípios de Cialdini:

   | Badge | Princípio | Posição na LP | Razão |
   |-------|-----------|--------------|-------|
   | Número de clientes | Prova Social | Hero (social proof bar) | Reduz ansiedade imediata |
   | Rating/Estrelas | Prova Social | Hero + Depoimentos | Valida credibilidade cedo |
   | Garantia | Redução de Risco | Próximo ao CTA + Próximo ao preço | Elimina objeção de risco no ponto de decisão |
   | Como visto em | Autoridade | Logo abaixo do hero | Transfere credibilidade da mídia |
   | Certificações | Autoridade | Seção de credibilidade | Valida competência |
   | Segurança de pagamento | Confiança | Próximo ao checkout | Elimina medo de segurança |
   | Anos de mercado | Autoridade | Hero ou bio do fundador | Sugere estabilidade |

4. **Implementação como componentes** — Criar componentes reutilizáveis:

   ```tsx
   // src/components/atoms/TrustBadge.tsx
   interface TrustBadgeProps {
     type: 'guarantee' | 'clients' | 'rating' | 'security' | 'media' | 'certification'
     value?: string | number
     label?: string
     size?: 'sm' | 'md' | 'lg'
   }
   ```

   ```tsx
   // src/components/molecules/SocialProofBar.tsx
   // Barra compacta com: "X+ clientes" | Rating stars | "Como visto em [logos]"
   ```

5. **Regras de uso de badges:**
   - Usar apenas badges com evidência real (número verificável, logo real, certificação existente)
   - Não criar badges falsos ("Prêmio XYZ" que não existe)
   - Manter atualizado: se número de clientes cresce, atualizar badge
   - Limitar a 3-4 badges por área (excesso reduz impacto individual)
   - Badges de segurança devem estar mais próximos do momento de conversão

## Veto Conditions
- Badge com informação falsa ou exagerada → remover
- Mais de 5 badges na mesma área → consolidar e priorizar
- Badge de segurança de pagamento em LP de captura de lead (sem pagamento) → remover (incongruente)
- Logos de mídia sem evidência real de menção → remover (ilegal)

## Output Esperado
- Especificação de cada badge (tipo, conteúdo, posição, tamanho)
- Componentes React implementados (TrustBadge, SocialProofBar)
- SVGs criados para badges que não têm ícone Lucide adequado
- Mapa de posicionamento: qual badge vai em qual seção
- Arquivo `trust-badges-spec.md` com especificações completas

## Completion Criteria
- [ ] Inventário de trust assets completado
- [ ] Badge de garantia especificado e implementado (obrigatório)
- [ ] Badge de número de clientes especificado (se N > 100)
- [ ] Badge "Como visto em" com logos reais verificados (se há menções na mídia)
- [ ] Badge de segurança de pagamento (se há checkout)
- [ ] Rating badge (se há avaliações verificáveis)
- [ ] Posicionamento estratégico definido para cada badge
- [ ] Componentes React implementados e funcionando em dark/light mode
- [ ] Arquivo `trust-badges-spec.md` criado
