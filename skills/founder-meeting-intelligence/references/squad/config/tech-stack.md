# Tech stack (integrações da especificação)

- Google Meet / Zoom / Microsoft Teams (captura de gravações automática via webhooks ou API — intake direto de reuniões gravadas)
- Google Calendar / Outlook Calendar (enriquecimento de metadados — participantes, recorrência, tipo de reunião; trigger automático por evento de calendário com gravação)
- ClickUp (criação de tasks com owner, deadline, prioridade e contexto — core output do squad; leitura de tasks existentes para deduplicação e follow-up)
- Notion (KB institucional — armazenamento permanente de Decision Records, Knowledge Snippets e Meeting Intelligence Reports; busca semântica via Vector DB)
- Slack (intake de reuniões via upload/link no canal #meetings-intel + entrega de sumários + notificações de action items + alertas de deadline + confirmações HITL)
- HubSpot (atualização de deals e contatos quando reunião envolve cliente/prospect — next steps, mudança de stage, notas de reunião)
- Claude Agent SDK + LangGraph (orquestração stateful do pipeline multi-agente — gerencia sequência Vox→Pulse→Quill→Vector→Argos→Hermes e estado da sessão por reunião)
- Langfuse (observabilidade OTEL — tracing completo por reunião, custo por agente/token, eval de qualidade de extração, dashboard de KPIs do squad)
- Whisper API / AssemblyAI (transcrição de áudio com diarização de alta qualidade — Vox usa como motor de transcrição com fallback entre providers)
- Vector DB — Pinecone ou Qdrant (armazenamento e busca semântica de decisões históricas, sumários e conhecimento tácito do founder)
- Gmail / Email SMTP (notificações de action items para participantes externos; envio de Meeting Intelligence Report para stakeholders aprovados)
- MCP Servers (camada de integração universal — ClickUp MCP, Notion MCP, Slack MCP, Google Calendar MCP expostos como tools para os agents)

Nível de autonomia por agente: L0/L1 = worker (determinístico/autônomo), L2 = orquestra/decide, L3 = exige aprovação humana. CRITIC verifica toda saída antes de entrega externa.
