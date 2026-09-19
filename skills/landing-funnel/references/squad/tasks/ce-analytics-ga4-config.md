---
task: configureGA4()
agent: ce-analytics-architect
description: "Configurar GA4: propriedade, eventos customizados (lead_submitted, page_scroll_depth, cta_clicked, form_started), conversões"
elicit: false
responsavel: "Lens"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: ga4MeasurementId
    tipo: string
    obrigatorio: true
    descricao: "GA4 Measurement ID (G-XXXXXXXX)"
  - nome: gtmSetup
    tipo: file
    obrigatorio: true
    descricao: "GTM configurado"

Saida:
  - nome: ga4Config
    tipo: file
    obrigatorio: true
    descricao: "GA4 configurado com eventos customizados: lead_submitted, page_scroll_depth, cta_clicked, form_started"

Checklist:
  pre-conditions:
    - "[ ] GTM instalado"
    - "[ ] GA4 propriedade criada"
  post-conditions:
    - "[ ] Eventos customizados ativos"
    - "[ ] Conversões configuradas"
    - "[ ] Relatórios base criados"
---

# Task: configureGA4()

## Objetivo
Configurar o Google Analytics 4 de forma completa e profissional, indo além da configuração básica de page views. Implementar eventos customizados críticos para otimização de conversão, marcar conversões corretamente e configurar relatórios personalizados que entregam insights acionáveis ao cliente.

## Inputs Necessários
- Conta Google Analytics com permissão de Administrador
- GA4 Measurement ID (obtido na propriedade GA4)
- GA4 API Secret (para Measurement Protocol server-side)
- `gtm-config.md` (estrutura de eventos já configurada no GTM)
- `traffic-data-analysis.md` (benchmarks e métricas-alvo)
- `scope.md` (eventos relevantes para o produto)

## Processo
1. **Verificação e configuração da propriedade GA4:**

   **Configurações básicas:**
   - Fuso horário: America/Sao_Paulo
   - Moeda: BRL (Real brasileiro)
   - Setor: [Setor correto do produto]
   - Tamanho da empresa: adequado ao cliente

   **Configurações de coleta de dados:**
   - Google Signals: Ativar (para dados demográficos e cross-device)
   - Retenção de dados: 14 meses (máximo disponível no GA4 gratuito)
   - Filtros de IP interno: Adicionar IP do cliente e da agência

   **Vinculações:**
   - Vincular com Google Ads (se ativo)
   - Vincular com Search Console (se domínio tem orgânico)
   - Vincular com BigQuery (se volume justificar — análise avançada)

2. **Configuração de eventos customizados** — Criar e verificar no GA4:

   **Eventos críticos (rastrear obrigatoriamente):**

   | Evento | Trigger | Parâmetros | Marcar como conversão? |
   |--------|---------|------------|----------------------|
   | `lead_submitted` | Formulário enviado com sucesso | `lead_source`, `form_location`, `campaign` | SIM |
   | `cta_clicked` | Clique em qualquer CTA | `cta_text`, `cta_location`, `cta_type` | Não |
   | `form_started` | Usuário clicou no primeiro campo | `form_name`, `form_location` | Não |
   | `page_scroll_depth` | Usuário scrollou 25/50/75/90% | `percent_scrolled`, `page_title` | Não |
   | `video_started` | Play no VSL | `video_title`, `video_duration` | Não |
   | `video_completed` | VSL assistido até o fim | `video_title`, `watch_time` | Não |
   | `purchase` | Compra concluída (se payments ativo) | `value`, `currency`, `transaction_id` | SIM |

   **Implementação via dataLayer (coordenada com GTM):**
   ```typescript
   // Disparado no frontend no momento correto
   pushToDataLayer({
     event: 'form_submit',
     form_name: 'lead-hero',
     lead_id: responseData.id,
   })
   ```

3. **Marcação de conversões** — No GA4 Admin → Conversões:
   - `lead_submitted` → Marcar como conversão
   - `purchase` → Marcar como conversão (se payments ativo)
   - Verificar que conversões aparecem em Relatórios → Conversões

4. **Parâmetros de evento personalizados** — Registrar no GA4 (Admin → Definições de evento):

   Parâmetros a registrar como dimensões/métricas customizadas:
   - `cta_location` → Dimensão: "Local do CTA"
   - `form_location` → Dimensão: "Local do Formulário"
   - `lead_source` → Dimensão: "Fonte do Lead"
   - `percent_scrolled` → Métrica: "Profundidade de Scroll"
   - `campaign` → Dimensão: "Campanha UTM"

5. **Configuração de funil de conversão** — Admin → Explorações → Funil:

   Funil: "Jornada de conversão da LP"
   - Passo 1: `session_start` (chegada)
   - Passo 2: `page_scroll_depth` percent=50 (engajamento)
   - Passo 3: `form_started` (intenção)
   - Passo 4: `lead_submitted` (conversão)

   Este funil mostra onde os visitantes desistem — ouro para otimização.

6. **Relatórios personalizados** — Criar em Explorar:

   **Relatório "Performance de CTAs":**
   - Dimensões: `cta_location`, `cta_text`
   - Métricas: `event_count`, `sessions`, `taxa de conversão`
   - Filtro: evento = `cta_clicked`

   **Relatório "Análise de Scroll":**
   - Dimensões: `percent_scrolled`, `device_category`
   - Métricas: `event_count`, `sessions`
   - Ordenado por scroll crescente — mostra onde usuários param

   **Relatório "Fonte de Leads":**
   - Dimensões: `utm_source`, `utm_medium`, `utm_campaign`
   - Métricas: `conversions`, `sessions`, `taxa de conversão por sessão`

7. **Configuração de Audiences** — Para uso em remarketing:
   - "Visitantes da LP" — Todos que chegaram na página
   - "Leads Engajados" — Que scrollaram 75%+ mas não converteram
   - "Iniciaram formulário" — Que clicaram no form mas não submeteram
   - "Convertidos" — Que submeteram o formulário (excluir de remarketing de conversão)

8. **Verificação end-to-end** — Usar GA4 DebugView:
   - Abrir LP com `?debug_mode=1` na URL
   - Rolar a página e verificar eventos de scroll
   - Clicar em CTAs e verificar `cta_clicked`
   - Submeter formulário de teste e verificar `lead_submitted`
   - Confirmar que conversão é contabilizada

## Veto Conditions
- Conversão `lead_submitted` não marcada como conversão no GA4 → marcar obrigatoriamente
- Fuso horário incorreto (UTC em vez de Brasília) → corrigir antes de coletar dados
- Dados sem filtro de IP interno (dados da agência contaminando métricas) → adicionar filtro
- Evento sem parâmetros (apenas nome do evento) → adicionar parâmetros relevantes

## Output Esperado
- Propriedade GA4 configurada com todos os settings corretos
- Eventos customizados ativos e verificados no DebugView
- Conversões marcadas
- Dimensões e métricas customizadas registradas
- Funil de conversão configurado
- 3 relatórios personalizados criados
- Audiences de remarketing configuradas
- Documento `ga4-config.md` com ID, eventos e configurações

## Completion Criteria
- [ ] Fuso horário e moeda corretos configurados
- [ ] Retenção de dados em 14 meses
- [ ] Filtro de IP interno adicionado
- [ ] Google Signals ativado
- [ ] 7 eventos customizados verificados no DebugView
- [ ] `lead_submitted` marcado como conversão
- [ ] `purchase` marcado como conversão (se payments ativo)
- [ ] Dimensões customizadas registradas (mínimo 3)
- [ ] Funil de conversão de 4 etapas configurado
- [ ] 3 relatórios personalizados criados
- [ ] 4 audiences de remarketing criadas
- [ ] Documento `ga4-config.md` com toda a configuração documentada
