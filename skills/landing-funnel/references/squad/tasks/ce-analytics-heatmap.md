---
task: configureHeatmaps()
agent: ce-analytics-architect
description: "Configurar Hotjar ou Microsoft Clarity: heatmaps, session recordings, conversion funnels, scroll maps"
elicit: true
responsavel: "Lens"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: heatmapTool
    tipo: string
    obrigatorio: true
    descricao: "Ferramenta escolhida: Hotjar ou Microsoft Clarity"

Saida:
  - nome: heatmapSetup
    tipo: file
    obrigatorio: true
    descricao: "Heatmap configurado com gravações de sessão, scroll maps e funis de conversão"

Checklist:
  pre-conditions:
    - "[ ] Conta Hotjar ou Clarity criada"
  post-conditions:
    - "[ ] Script instalado via GTM"
    - "[ ] Heatmaps ativados"
    - "[ ] Gravações de sessão iniciando"
---

# Task: configureHeatmaps()

## Objetivo
Configurar ferramenta de heatmap e session recording para capturar o comportamento visual real dos visitantes na landing page. Heatmaps revelam onde os usuários clicam, onde param de rolar e quais elementos atraem atenção — dados impossíveis de obter apenas com analytics numérico.

## Inputs Necessários
- `scope.md` (analytics flag ativa)
- Ferramenta escolhida (Hotjar recomendado para recursos; Microsoft Clarity como gratuito)
- Domínio da LP para verificação de site
- `sections-design-spec.md` (estrutura da página para configuração de funis)
- `traffic-data-analysis.md` (volume esperado de sessões para escolha do plano)

## Processo
1. **Elicitação de configuração:**
   - Volume esperado de sessões/mês (define se Clarity gratuito é suficiente ou se precisa Hotjar pago)
   - Budget para ferramentas: Clarity (gratuito, Microsoft), Hotjar Observe (a partir de $39/mês), FullStory
   - Necessidades específicas: só heatmap? Também session recordings? Conversion funnels? Surveys?

2. **Recomendação por volume:**

   | Volume (sessões/mês) | Recomendação | Custo |
   |---------------------|-------------|-------|
   | < 5.000 | Microsoft Clarity | Gratuito |
   | 5.000 - 50.000 | Hotjar Observe Starter | $39/mês |
   | > 50.000 | Hotjar Business ou FullStory | $99+/mês |
   | Enterprise | FullStory ou Contentsquare | Custom |

3. **Setup Microsoft Clarity (se escolhido):**

   **Instalação via GTM:**
   ```javascript
   // Tag GTM: Microsoft Clarity
   // Tipo: Custom HTML
   (function(c,l,a,r,i,t,y){
     c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
     t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
     y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
   })(window, document, "clarity", "script", "{{Clarity Project ID}}");
   ```

   **Configurações no Clarity Dashboard:**
   - Ativar Session Recordings: sim
   - Masking: mascarar campos sensíveis (email, telefone, dados de cartão)
   - Filtros: excluir tráfego interno (por IP ou cookie)
   - Integração com GA4: vincular Clarity com propriedade GA4 para cruzamento de dados

4. **Setup Hotjar (se escolhido):**

   **Instalação via GTM:**
   ```javascript
   // Tag GTM: Hotjar
   (function(h,o,t,j,a,r){
     h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
     h._hjSettings={hjid:{{Hotjar Site ID}},hjsv:6};
     a=o.getElementsByTagName('head')[0];
     r=o.createElement('script');r.async=1;
     r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
     a.appendChild(r);
   })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
   ```

   **Configurações no Hotjar Dashboard:**
   - Heatmaps: criar para a URL da LP (página principal)
     - Click heatmap: onde usuários clicam
     - Move heatmap: movimento do mouse (proxy para onde olham em desktop)
     - Scroll heatmap: até onde usuários rolam
   - Session Recordings: ativar para 100% das sessões inicialmente, depois ajustar
   - Masking: configurar campos de formulário como masked (PII)

5. **Configuração de Funis de Conversão (Hotjar Funnels ou Clarity Funnels):**

   **Funil principal da LP:**
   - Passo 1: URL da LP carregada (100%)
   - Passo 2: Scroll até 50% da página
   - Passo 3: Clique em qualquer CTA
   - Passo 4: Início do preenchimento do formulário
   - Passo 5: Submissão bem-sucedida do formulário

   **Funil de VSL (se aplicável):**
   - Passo 1: VSL visível no viewport
   - Passo 2: Play clicado
   - Passo 3: 50% do vídeo assistido
   - Passo 4: 100% do vídeo assistido
   - Passo 5: CTA clicado após vídeo

6. **Identificação de usuários (pós-conversão):**
   ```typescript
   // Após submissão bem-sucedida do formulário
   // Hotjar:
   window.hj?.('identify', leadId, {
     email: lead.email,
     lead_source: lead.source,
   })

   // Clarity:
   window.clarity?.('identify', leadId, sessionId, pageId, lead.email)
   // ATENÇÃO: usar email hasheado se PII
   ```

7. **Configuração de Scroll Map detalhada** — Mapear pontos críticos da página com marcadores:
   - Posição do primeiro CTA (deve ter alta concentração de cliques)
   - Início da seção de depoimentos
   - Seção de pricing
   - CTA final
   Anotar porcentagem de scroll de cada elemento para cruzar com dados de scroll map.

8. **Agenda de análise** — Definir rotina de revisão:
   - Semana 1: Revisar sessões de usuários que chegaram ao formulário mas não converteram
   - Semana 2: Comparar heatmap de cliques com posição dos CTAs
   - Semana 3: Análise do funil — identificar maior ponto de abandono
   - Semana 4: Formular primeira hipótese de A/B test com base nos dados

## Veto Conditions
- Campos de formulário sem masking de dados sensíveis → configurar antes de ativar recordings (LGPD e GDPR)
- Ferramenta ativa mas sem rotina de análise definida → ferramenta sem uso não tem valor
- Tráfego interno não filtrado → dados contaminados pelo uso da equipe

## Output Esperado
- Ferramenta de heatmap instalada e funcionando
- Session recordings ativadas (com masking de PII)
- Heatmaps de click, move e scroll configurados
- Funil de conversão configurado
- Agenda de análise documentada
- Documento `heatmap-config.md` com IDs, configurações e agenda

## Completion Criteria
- [ ] Ferramenta escolhida com justificativa de volume/budget
- [ ] Script instalado via GTM e verificado
- [ ] Campos sensíveis com masking ativado (email, telefone)
- [ ] Tráfego interno filtrado
- [ ] 3 tipos de heatmap ativos (click, move, scroll)
- [ ] Session recordings ativadas
- [ ] Funil de conversão de 5 passos configurado
- [ ] Identificação de usuário pós-conversão implementada
- [ ] Agenda de análise semanal documentada
- [ ] Documento `heatmap-config.md` criado
