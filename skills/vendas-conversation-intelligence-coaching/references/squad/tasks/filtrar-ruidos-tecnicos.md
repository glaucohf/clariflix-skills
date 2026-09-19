---
task: babel()
responsavel: "Babel"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Arquivo de áudio/vídeo da call (MP3, MP4, WAV, WebM) OU URL de gravação (Zoom, Google Meet, Vapi, Retell)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Metadados da call: ID do deal no CRM, nome do vendedor, nome do prospect, data/hora, duração esperada"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Mínimo de 3 minutos de duração para processamento"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Transcript Object estruturado em JSON: {call_id, deal_id, vendedor_id, prospect_id, duracao_total_seg, turnos_de_fala: [{speaker: 'vendedor'|'prospect', inicio_seg, fim_seg, texto, confianca_pct}], silencias_relevantes: [{inicio_seg, duracao_seg, contexto}], talk_ratio: {vendedor_pct, prospect_pct}, palavras_por_minuto_vendedor, qualidade_audio_score}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Arquivo de transcricao em texto plano para uso pelo Analisador"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Armazenado no Supabase com link de referencia"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook POST de plataforma de voz/vídeo indicando call encerrada com gravação disponível. Evento call_recorded no event bus. Upload manual de arquivo de áudio via interface do gestor. Job de verifica…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Calibrador antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL-1 (L3): Deal Risk Alert de nível ALTO ou CRÍTICO gerado pelo Vigilante — gestor recebe alerta no WhatsApp e deve confirmar qual ação tomar (ligar agora, escalar para diretor, ajustar proposta, aceitar perda) antes de qualquer comunicação automatizada com o prospect. SLA de resposta: 4h em dias úteis."
    - "[ ] HITL: HITL-2 (L3): Objeção de tipo não mapeado detectada pela primeira vez — o Analisador sinaliza objeção nova fora da biblioteca existente. Humano (gestor ou especialista de produto) deve validar a classificação e criar o counter-script antes que o sistema use-o em coachings futuros. Evita ensinar o time a responder errado."
    - "[ ] HITL: HITL-3 (L2): Score da call abaixo de 40/100 (call catastrófica) — além do coaching card automático, o Orchestrator notifica o gestor para que ele decida se faz uma sessão 1:1 urgente com o vendedor ou se o deal precisar de intervenção direta do gestor. Vendedor não é notificado do score crítico sem acompanhamento humano."
    - "[ ] HITL: HITL-4 (L2): Transcrição com qualidade de áudio abaixo de 75% de confiança — a Babel sinaliza e o gestor decide se envia para transcrição manual, descarta a call da análise ou aceita os resultados com baixa confiança. Garante que coaching baseado em transcrição ruim não chegue ao vendedor."
    - "[ ] HITL: HITL-5 (L2): Calibração quinzenal da Rubrica de Avaliação — o gestor revisa um sample de 5 calls para verificar se os scores do Juiz estão alinhados com sua percepção. Ajusta pesos de dimensões se necessário. Previne drift do modelo de scoring ao longo do tempo."
---

# Filtrar Ruídos técnicos

**Task ID:** `babel()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Conversation Intelligence e Coaching

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Filtrar Ruídos técnicos |
| **status** | `pending` |
| **responsible_executor** | Babel (Transcritora de Calls (Babel)) |
| **execution_type** | `Worker` |
| **input** | 3 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de transcrição e diarização. Recebe o arquivo de áudio/vídeo da call (ou URL de gravação), executa STT (Speech-to-Text) com diarização de speakers — identificando quem é o vendedor e quem é o prospect — e normaliza a transcrição em formato estruturado com timestamps por turno de fala, labels de speaker e marcadores de silêncio. Detecta e filtra ruídos técnicos (chamada caindo, eco, sobreposição de fala). Reconhece termos técnicos e nomes próprios frequentes do segmento do cliente para reduzir erros de transcrição.

## Input

- Arquivo de áudio/vídeo da call (MP3, MP4, WAV, WebM) OU URL de gravação (Zoom, Google Meet, Vapi, Retell)
- Metadados da call: ID do deal no CRM, nome do vendedor, nome do prospect, data/hora, duração esperada
- Mínimo de 3 minutos de duração para processamento

## Output

- Transcript Object estruturado em JSON: {call_id, deal_id, vendedor_id, prospect_id, duracao_total_seg, turnos_de_fala: [{speaker: 'vendedor'|'prospect', inicio_seg, fim_seg, texto, confianca_pct}], silencias_relevantes: [{inicio_seg, duracao_seg, contexto}], talk_ratio: {vendedor_pct, prospect_pct}, palavras_por_minuto_vendedor, qualidade_audio_score}
- Arquivo de transcricao em texto plano para uso pelo Analisador
- Armazenado no Supabase com link de referencia

## Trigger

Webhook POST de plataforma de voz/vídeo indicando call encerrada com gravação disponível. Evento call_recorded no event bus. Upload manual de arquivo de áudio via interface do gestor. Job de verificação diário às 06h para calls das últimas 24h sem transcrição.

## Knowledge base (o que o executor consulta)

- Credenciais de API do provedor STT configurado (Deepgram ou AssemblyAI
- Deepgram preferido por latencia < 1min/hora de audio)
- Dicionario de termos customizado por segmento do cliente (ex: imobiliaria: VGV, permuta, habite-se, escritura
- agencia: CPL, ROAS, media paga, briefing)
- Regras de identificacao de speaker: o vendedor normalmente e quem inicia a call e faz mais perguntas nos primeiros 5 minutos
- Threshold de confianca minima de transcricao: 75%
- abaixo disso sinaliza para revisao humana

## Action Items

1. Confirmar o gatilho e carregar a entrada (Arquivo de áudio/vídeo da call (MP3, MP4, WAV, WebM) OU URL de gravação (Zoom, Google Meet, Vapi, Retell)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Transcript Object estruturado em JSON: {call_id, deal_id, vendedor_id, prospect_id, duracao_total_seg, turnos_de_fala:…) e persistir no artefato do squad.
4. Entregar ao critic Calibrador; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Transcript Object estruturado em JSON: {call_id, deal_id, vendedor_id, prospect_id, duracao_total_seg, turnos_de_fala: [{speaker: 'vendedor'|'prospect', inicio…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Calibrador registrado
- [ ] Gate HITL respeitado: HITL-1 (L3): Deal Risk Alert de nível ALTO ou CRÍTICO gerado pelo Vigilante — gestor recebe alerta no WhatsApp e deve confirmar qual ação t…
- [ ] Gate HITL respeitado: HITL-2 (L3): Objeção de tipo não mapeado detectada pela primeira vez — o Analisador sinaliza objeção nova fora da biblioteca existente. Hum…
- [ ] Gate HITL respeitado: HITL-3 (L2): Score da call abaixo de 40/100 (call catastrófica) — além do coaching card automático, o Orchestrator notifica o gestor para q…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL-1 (L3): Deal Risk Alert de nível ALTO ou CRÍTICO gerado pelo Vigilante — gestor recebe alerta no WhatsApp e deve confirmar qual ação tomar (ligar agora, e… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL-2 (L3): Objeção de tipo não mapeado detectada pela primeira vez — o Analisador sinaliza objeção nova fora da biblioteca existente. Humano (gestor ou espec… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL-3 (L2): Score da call abaixo de 40/100 (call catastrófica) — além do coaching card automático, o Orchestrator notifica o gestor para que ele decida se faz… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL-4 (L2): Transcrição com qualidade de áudio abaixo de 75% de confiança — a Babel sinaliza e o gestor decide se envia para transcrição manual, descarta a ca… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL-5 (L2): Calibração quinzenal da Rubrica de Avaliação — o gestor revisa um sample de 5 calls para verificar se os scores do Juiz estão alinhados com sua pe… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL-6 (L1): Aprovação do Plano de Role-Play semanal gerado pelo Radar do Time — gestor revisa as objeções priorizadas e o script de simulação antes de compart… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Calibrador | BLOQUEIA entrega |

## Handoff

- **to:** Sherlock da Call
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
