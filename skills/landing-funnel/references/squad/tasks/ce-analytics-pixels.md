---
task: setupConversionPixels()
agent: ce-analytics-architect
description: "Setup de pixels: Meta Pixel + Conversions API, Google Ads conversion tracking, TikTok Pixel (se aplicável)"
elicit: true
responsavel: "Lens"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: pixelIds
    tipo: object
    obrigatorio: true
    descricao: "IDs dos pixels: Meta Pixel ID, Google Ads Conversion ID, TikTok Pixel ID"

Saida:
  - nome: pixelsSetup
    tipo: file
    obrigatorio: true
    descricao: "Pixels configurados via GTM: Meta Pixel + Conversions API, Google Ads, TikTok Pixel"

Checklist:
  pre-conditions:
    - "[ ] GTM instalado"
    - "[ ] IDs dos pixels disponíveis"
  post-conditions:
    - "[ ] Meta Pixel disparando"
    - "[ ] Conversions API conectada"
    - "[ ] Google Ads conversion tracking ativo"
---

# Task: setupConversionPixels()

## Objetivo
Configurar todos os pixels de conversão da landing page com arquitetura server-side + client-side (dual tracking) para máxima precisão de dados. O rastreamento impreciso resulta em otimização de campanhas baseada em dados incorretos — o que desperdiça budget e impede scaling.

## Inputs Necessários
- `scope.md` (plataformas de tráfego ativas)
- Meta Pixel ID e Access Token da Conversions API
- Google Ads Conversion ID e Conversion Label
- TikTok Pixel ID (se tráfego TikTok planejado)
- Backend com server-side tracking implementado (`setupEventTracking()` concluído)
- `gtm-config.md` (triggers disponíveis no GTM)

## Processo
1. **Elicitação de pixels necessários** — Confirmar com o cliente:
   - Meta Ads está sendo ou será usado? → Meta Pixel + CAPI
   - Google Ads está sendo ou será usado? → Google Ads Conversion Tracking
   - TikTok Ads está sendo ou será usado? → TikTok Pixel
   - Outros: LinkedIn, Twitter/X, Pinterest?

2. **Meta Pixel — Configuração completa:**

   **Client-side (via GTM):**
   ```javascript
   // Tag GTM: Meta Pixel Base
   // Tipo: Custom HTML
   !function(f,b,e,v,n,t,s){
   if(f.fbq)return;n=f.fbq=function(){n.callMethod?
   n.callMethod.apply(n,arguments):n.queue.push(arguments)};
   if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
   n.queue=[];t=b.createElement(e);t.async=!0;
   t.src=v;s=b.getElementsByTagName(e)[0];
   s.parentNode.insertBefore(t,s)}(window,document,'script',
   'https://connect.facebook.net/en_US/fbevents.js');
   fbq('init', '{{Meta Pixel ID}}');
   fbq('track', 'PageView');
   ```

   **Eventos Meta via GTM:**

   | Evento Meta | Trigger GTM | Event ID (para dedup) |
   |-------------|------------|----------------------|
   | `PageView` | All Pages | N/A |
   | `Lead` | Form Submit | `lead_{{DL - lead_id}}_{{timestamp}}` |
   | `InitiateCheckout` | Pricing CTA Click | N/A |
   | `Purchase` | Purchase Complete | `purchase_{{transaction_id}}` |
   | `ViewContent` | All Pages | N/A |

   **Implementação com event ID para deduplication:**
   ```javascript
   // Tag GTM: Meta Lead Event
   var eventID = 'lead_' + {{DL - lead_id}} + '_' + Date.now();
   fbq('track', 'Lead', {
     content_name: '{{Product Name}}',
     content_category: '{{Product Category}}',
   }, {eventID: eventID});
   // Enviar eventID ao backend para CAPI usar o mesmo ID
   ```

   **Server-side Meta CAPI** (já implementado no backend):
   - Verificar que backend está enviando o mesmo `event_id` client-side
   - Usar Meta Events Manager → Test Events para verificar

3. **Google Ads Conversion Tracking:**

   **Opção A — Via GTM (recomendado para simplicidade):**
   ```javascript
   // Tag GTM: Google Ads Conversion
   // Tipo: Google Ads Conversion Tracking
   // Conversion ID: AW-XXXXXXXXXX
   // Conversion Label: [Label]
   // Conversion Value: [Dinâmico ou fixo]
   // Currency: BRL
   // Trigger: Form Submit
   ```

   **Opção B — Via gtag.js diretamente:**
   ```typescript
   // src/lib/tracking.ts — adicionar ao trackConversion()
   window.gtag?.('event', 'conversion', {
     send_to: `${process.env.NEXT_PUBLIC_GADS_CONVERSION_ID}/${process.env.NEXT_PUBLIC_GADS_CONVERSION_LABEL}`,
     value: 0,
     currency: 'BRL',
     transaction_id: leadId,
   })
   ```

   **Enhanced Conversions (recomendado):**
   - Enviar dados hasheados do usuário para melhorar correspondência
   - No GTM: Google Ads Enhanced Conversions tag
   - Mapear campo de email do formulário

4. **TikTok Pixel (se aplicável):**

   **Client-side via GTM:**
   ```javascript
   // Tag GTM: TikTok Pixel Base
   !function (w, d, t) {
     w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];
     ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"];
     ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};
     for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);
     ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e};
     ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{};ttq._i[e]=[];ttq._i[e]._u=i;ttq._t=ttq._t||{};ttq._t[e]=+new Date;ttq._o=ttq._o||{};ttq._o[e]=n||{};var o=document.createElement("script");o.type="text/javascript";o.async=!0;o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};
     ttq.load('{{TikTok Pixel ID}}');
     ttq.page();
   }(window, document, 'ttq');
   ```

   **Evento Lead no TikTok:**
   ```javascript
   ttq.track('SubmitForm', {
     content_id: '{{Product ID}}',
     content_name: '{{Product Name}}',
   });
   ```

5. **Verificação de todos os pixels:**

   **Meta Pixel Helper (extensão Chrome):**
   - Verificar que Pixel dispara em page load (PageView)
   - Verificar que Lead event dispara no submit do form
   - Verificar que event_id está presente para deduplication

   **Google Tag Assistant:**
   - Verificar que Google Ads conversion tag está presente
   - Verificar que Enhanced Conversions está passando dados hasheados

   **Meta Events Manager — Test Events:**
   - Enviar evento de teste
   - Verificar que server-side (CAPI) e client-side chegam com mesmo event_id
   - Verificar que Meta deduplica corretamente (conta como 1, não 2)

6. **Documentação de pixels** — Criar registro de todos os pixels instalados:
   - Nome do pixel, ID, plataforma, eventos rastreados, deduplication implementada

## Veto Conditions
- Meta CAPI e client-side sem deduplication via event_id → implementar antes de ativar tráfego (dados duplicados inflam conversões)
- Enhanced Conversions do Google Ads não configurado → implementar para melhorar match rate
- Pixel instalado mas não verificado no Events Manager/Tag Assistant → verificar antes de lançar
- TikTok Pixel instalado sem flag de tráfego TikTok ativa → remover para reduzir peso de JS

## Output Esperado
- Meta Pixel instalado via GTM com todos os eventos configurados
- Meta CAPI verificado em Events Manager (deduplicado)
- Google Ads Conversion Tracking configurado com Enhanced Conversions
- TikTok Pixel instalado (se aplicável)
- Documento `pixels-config.md` com IDs, eventos e status de verificação

## Completion Criteria
- [ ] Meta Pixel PageView verificado em cada page load
- [ ] Meta Lead event disparando no form submit com event_id
- [ ] Meta CAPI enviando Lead event com mesmo event_id (deduplication verificada)
- [ ] Google Ads conversion tag disparando no form submit
- [ ] Enhanced Conversions passando email hasheado
- [ ] TikTok Pixel instalado e verificado (se aplicável)
- [ ] Todos os pixels verificados via extensões/debuggers
- [ ] Documento `pixels-config.md` com status de cada pixel
