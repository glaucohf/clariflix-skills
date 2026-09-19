# Checklist do critic ARGUS — Objection Handling e Q&A em Tempo Real

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

ARGUS — O Verificador de Factualidade e Tom — Critic/Verifier que audita cada resposta gerada pelos workers antes da entrega ao vendedor. Verifica em < 2 segundos (para manter o SLA de tempo real): (1) Factualidade — a resposta contém dado específico (preço, prazo, ROI, feature de produto)? Se sim, o dado está na base de conhecimento verificada ou é inferência? Dados não verificados são substituídos por linguagem qualitativa ou flaggados com 'confirmar antes de usar'; (2) Tom — a resposta ataca o concorrente diretamente? Faz promessa que a empresa não pode cumprir? Usa linguagem agressiva ou desesperada que denota pressão de fechamento? (3) Completude — a resposta tem as três camadas (resposta principal + argumento + pergunta de redirecionamento)? (4) Adequação ao canal — resposta para call tem max 2 linhas? Resposta para WhatsApp está bem formatada? Emite veredicto APROVADO / APROVADO COM RESSALVA (entrega com nota ao vendedor) / REJEITADO (re-roteia para worker com instrução de correção específica).

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Verificador de Factualidade e Tom
- [ ] **C02** — Critic/Verifier que audita cada resposta gerada pelos workers antes da entrega ao vendedor
- [ ] **C03** — Verifica em < 2 segundos (para manter o SLA de tempo real): (1) Factualidade
- [ ] **C04** — a resposta contém dado específico (preço, prazo, ROI, feature de produto)? Se sim, o dado está na base de conhecimento verificada ou é inferência? Dados não verificados são substituídos por linguagem qualitativa ou flaggados com 'confirmar antes de usar'
- [ ] **C05** — a resposta ataca o concorrente diretamente? Faz promessa que a empresa não pode cumprir? Usa linguagem agressiva ou desesperada que denota pressão de fechamento? (3) Completude
- [ ] **C06** — a resposta tem as três camadas (resposta principal + argumento + pergunta de redirecionamento)? (4) Adequação ao canal
- [ ] **C07** — resposta para call tem max 2 linhas? Resposta para WhatsApp está bem formatada? Emite veredicto APROVADO / APROVADO COM RESSALVA (entrega com nota ao vendedor) / REJEITADO (re-roteia para worker com instrução de correção específica)

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Qualquer resposta que envolva promessa de desconto acima do nível autorizado para o vendedor: MAESTRO pausa, notifica supervisor ou gerente de vendas via Slack/WhatsApp, que aprova ou rejeita em tempo real antes da resposta chegar ao vendedor
- [ ] **L3** — Qualquer resposta a dúvida técnica que envolva prazo de implementação customizado, SLA não padrão, ou integração não documentada na base: TÉCNICO flag como HITL, vendedor recebe instrução 'vou confirmar com a equipe técnica e te retorno em X horas' em vez de uma promessa não verificada
- [ ] **L3** — Escrita de resultados de call e atualização de stage no CRM pelo ARQUIVO: vendedor confirma o resultado via formulário rápido (1 click) antes de qualquer persistência em CRM de produção
- [ ] **L2** — Quando ARGUS emite REJEITADO por factualidade: MAESTRO notifica o vendedor que a resposta está sendo verificada e entrega uma resposta genérica segura enquanto o worker corrige — o vendedor decide se usa a genérica ou aguarda a corrigida
- [ ] **L1** — Objecão nova não catalogada (aparece pela primeira vez): ARQUIVO sinaliza ao líder de vendas ou product owner que uma nova objecão foi detectada e sugere draft de resposta para validação antes de entrar na base — o líder aprova, edita ou rejeita o draft

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
