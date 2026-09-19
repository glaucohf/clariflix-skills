---
task: setupGTM()
agent: ce-analytics-architect
description: "Setup completo de Google Tag Manager: container, variáveis, triggers, tags base"
elicit: false
responsavel: "Lens"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: gtmContainerId
    tipo: string
    obrigatorio: true
    descricao: "ID do container GTM"

Saida:
  - nome: gtmSetup
    tipo: file
    obrigatorio: true
    descricao: "GTM configurado: container, variáveis, triggers e tags base com dataLayer tipado"

Checklist:
  pre-conditions:
    - "[ ] Conta GTM criada"
    - "[ ] Container ID disponível"
  post-conditions:
    - "[ ] GTM snippet instalado"
    - "[ ] dataLayer configurado"
    - "[ ] Preview mode testado"
---

# Task: setupGTM()

## Objetivo
Configurar o Google Tag Manager como hub central de todas as tags da landing page, criando a arquitetura correta de variáveis, triggers e tags que permitirá rastrear cada interação relevante do visitante sem modificar o código do site a cada nova necessidade de tracking.

## Inputs Necessários
- `scope.md` (flags de analytics, pixels ativos)
- `product-brief.md` (produto, domínio)
- Acesso ao Google Tag Manager (conta e container criados)
- `sections-design-spec.md` (nomes e IDs dos elementos interativos)
- GA4 Measurement ID
- Meta Pixel ID
- Outros pixels ativos (TikTok, Google Ads)

## Processo
1. **Criação e configuração do container** — Verificar ou criar:
   - Container do tipo Web
   - Container ID no formato GTM-XXXXXXX
   - Snippet de instalação adicionado ao Next.js:

   ```tsx
   // src/components/providers/GTMProvider.tsx
   import Script from 'next/script'

   export function GTMProvider({ gtmId }: { gtmId: string }) {
     return (
       <>
         {/* GTM Script — no <head> */}
         <Script
           id="gtm-script"
           strategy="afterInteractive"
           dangerouslySetInnerHTML={{
             __html: `(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
             new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
             j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
             'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
             })(window,document,'script','dataLayer','${gtmId}');`,
           }}
         />
         {/* GTM noscript — no início do <body> */}
         <noscript>
           <iframe
             src={`https://www.googletagmanager.com/ns.html?id=${gtmId}`}
             height="0" width="0"
             style={{ display: 'none', visibility: 'hidden' }}
           />
         </noscript>
       </>
     )
   }
   ```

2. **Configuração do dataLayer** — Estrutura padronizada de eventos:
   ```typescript
   // src/lib/datalayer.ts
   export function pushToDataLayer(event: DataLayerEvent) {
     window.dataLayer = window.dataLayer || []
     window.dataLayer.push(event)
   }

   export type DataLayerEvent =
     | { event: 'page_view'; page_title: string; page_path: string }
     | { event: 'cta_click'; cta_text: string; cta_location: string; cta_type: string }
     | { event: 'form_start'; form_name: string }
     | { event: 'form_submit'; form_name: string; lead_id?: string }
     | { event: 'scroll_depth'; percent: 25 | 50 | 75 | 90 }
     | { event: 'video_play'; video_title: string; video_provider: string }
     | { event: 'video_complete'; video_title: string; duration: number }
   ```

3. **Variáveis GTM** — Criar as seguintes variáveis no container:

   **Variáveis de URL:**
   - `utm_source` — Query param UTM source
   - `utm_medium` — Query param UTM medium
   - `utm_campaign` — Query param UTM campaign
   - `utm_content` — Query param UTM content
   - `utm_term` — Query param UTM term
   - `page_path` — URL path atual
   - `page_url` — URL completa

   **Variáveis de dataLayer:**
   - `DL - cta_text` — dataLayer variable
   - `DL - cta_location` — dataLayer variable
   - `DL - form_name` — dataLayer variable
   - `DL - scroll_depth_percent` — dataLayer variable
   - `DL - lead_id` — dataLayer variable

   **Variáveis de cookies:**
   - `_ga` — Cookie GA4 (client ID)
   - `_fbp` — Cookie Meta Pixel
   - `_gcl_aw` — Cookie Google Ads click

   **Constantes:**
   - `GA4 Measurement ID` — Constante com o ID GA4
   - `Meta Pixel ID` — Constante com o Pixel ID

4. **Triggers GTM** — Criar os seguintes gatilhos:

   | Trigger | Tipo | Condição |
   |---------|------|----------|
   | `All Pages` | Page View | Todas as páginas |
   | `CTA Click` | Custom Event | event = 'cta_click' |
   | `Form Start` | Custom Event | event = 'form_start' |
   | `Form Submit` | Custom Event | event = 'form_submit' |
   | `Scroll 25%` | Custom Event | event = 'scroll_depth', percent = 25 |
   | `Scroll 50%` | Custom Event | event = 'scroll_depth', percent = 50 |
   | `Scroll 75%` | Custom Event | event = 'scroll_depth', percent = 75 |
   | `Scroll 90%` | Custom Event | event = 'scroll_depth', percent = 90 |
   | `Video Play` | Custom Event | event = 'video_play' |
   | `Video Complete` | Custom Event | event = 'video_complete' |

5. **Tags GTM base** — Criar tags para GA4:

   **GA4 Configuration Tag:**
   - Tipo: Google Analytics GA4 Configuration
   - Measurement ID: `{{GA4 Measurement ID}}`
   - Parâmetros adicionais: `user_properties` com `utm_source`, `utm_medium`, `utm_campaign`
   - Trigger: All Pages

   **GA4 Event — Page View:**
   - Tipo: Google Analytics GA4 Event
   - Event Name: `page_view`
   - Trigger: All Pages (após configuration tag)

   **GA4 Event — CTA Click:**
   - Event Name: `cta_clicked`
   - Parameters: `cta_text: {{DL - cta_text}}`, `cta_location: {{DL - cta_location}}`
   - Trigger: CTA Click

   **GA4 Event — Form:**
   - Form Start event + Form Submit event com parameters

   **GA4 Event — Scroll Depth:**
   - 4 tags separadas (25/50/75/90%) OU 1 tag com variable de percent

6. **Publicação e verificação:**
   - Usar GTM Preview Mode para testar cada trigger
   - Verificar no GA4 DebugView que eventos chegam
   - Publicar container com versão nomeada: "Versão inicial - [data]"

## Veto Conditions
- Container GTM instalado sem verificação de funcionamento → testar Preview Mode antes de publicar
- Tags disparando em todos os eventos (trigger too broad) → refinar triggers
- Variáveis de dataLayer sem typagem correspondente no código → sincronizar
- Publicação sem versão nomeada → sempre nomear versões

## Output Esperado
- Container GTM publicado e funcionando
- GTMProvider implementado no Next.js
- Arquivo `gtm-config.md` documentando todas as variáveis, triggers e tags criadas
- `src/lib/datalayer.ts` com tipos TypeScript

## Completion Criteria
- [ ] Container GTM criado e snippet instalado no Next.js (head + noscript body)
- [ ] dataLayer tipado em TypeScript
- [ ] Mínimo 12 variáveis criadas (UTM, dataLayer, cookies, constantes)
- [ ] Mínimo 10 triggers criados (page view + 9 eventos customizados)
- [ ] Tag GA4 Configuration com Measurement ID configurada
- [ ] Tags de eventos GA4 criadas (page_view, cta_click, form_start, form_submit, scroll)
- [ ] Container testado via Preview Mode (todos os triggers disparando corretamente)
- [ ] Container publicado com versão nomeada
- [ ] Documentação `gtm-config.md` criada
