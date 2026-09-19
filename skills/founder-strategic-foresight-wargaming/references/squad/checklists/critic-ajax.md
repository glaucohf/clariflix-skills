# Checklist do critic Ajax — Strategic Foresight & Wargaming

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Ajax — O Crítico de Guerra — Ajax é o agente critic/red-team do squad. Executa verificação adversarial em quatro camadas após os três workers (Cassandra, Brutus, Chisel) concluírem: (1) CONSISTÊNCIA CRUZADA — verifica se as reações dos adversários (Brutus) são coerentes com os cenários gerados (Cassandra) e com as premissas estressadas (Chisel); inconsistências são sinalizadas e retornam para retrabalho. (2) PRE-MORTEM ESTRUTURADO — assume que a decisão falhou em 12 meses e constrói a narrativa causal mais plausível com base nos outputs dos workers; força o squad a encarar a falha antes que ela aconteça. (3) COBERTURA DE PREMISSAS — verifica se todas as premissas críticas da Árvore receberam stress-test do Chisel; premissas não cobertas são retornadas como gap. (4) TESTE DE ROBUSTEZ — verifica se a recomendação de GO/NO-GO ainda se sustenta se as 2 premissas mais frágeis falharem simultaneamente. Se Pre-Mortem revelar caminho de falha com probabilidade > 30%, bloqueia recomendação de GO e escalona para HITL gate obrigatório.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Crítico de Guerra
- [ ] **C02** — Ajax é o agente critic/red-team do squad
- [ ] **C03** — Executa verificação adversarial em quatro camadas após os três workers (Cassandra, Brutus, Chisel) concluírem: (1) CONSISTÊNCIA CRUZADA
- [ ] **C04** — verifica se as reações dos adversários (Brutus) são coerentes com os cenários gerados (Cassandra) e com as premissas estressadas (Chisel)
- [ ] **C05** — inconsistências são sinalizadas e retornam para retrabalho
- [ ] **C06** — (2) PRE-MORTEM ESTRUTURADO
- [ ] **C07** — assume que a decisão falhou em 12 meses e constrói a narrativa causal mais plausível com base nos outputs dos workers
- [ ] **C08** — força o squad a encarar a falha antes que ela aconteça
- [ ] **C09** — (3) COBERTURA DE PREMISSAS
- [ ] **C10** — verifica se todas as premissas críticas da Árvore receberam stress-test do Chisel
- [ ] **C11** — premissas não cobertas são retornadas como gap
- [ ] **C12** — (4) TESTE DE ROBUSTEZ
- [ ] **C13** — verifica se a recomendação de GO/NO-GO ainda se sustenta se as 2 premissas mais frágeis falharem simultaneamente
- [ ] **C14** — Se Pre-Mortem revelar caminho de falha com probabilidade > 30%, bloqueia recomendação de GO e escalona para HITL gate obrigatório

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Premissas, classificação de stakes, estimativa de custo de tokens). Para decisões classificadas como Alto (R$100k-500k) ou Crítico (R$500k+), aprovação explícita do founder é obrigatória antes de disparar workers. Inclui confirmação do escopo, dos concorrentes a simular e do nível de profundidade desejado.
- [ ] **HITL** — PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o wargaming pausa e founder recebe notificação urgente com evidências contrárias. O founder deve decidir: (a) revisar a tese antes de prosseguir, (b) validar a premissa com dado adicional, ou (c) aceitar o risco explicitamente e autorizar o prosseguimento. Sem aprovação explícita, Atlas não gera recomendação de GO.
- [ ] **HITL** — PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de 30%, o squad bloqueia automaticamente a recomendação de GO e escalona para o founder. O relatório apresenta: narrativa do caminho de falha, premissas que o geram e opções de mitigação. O founder deve responder com ação concreta (mitigar, aceitar, desistir) antes de qualquer recomendação final.
- [ ] **HITL** — BOARD MEMO E ENVIO EXTERNO (L3): Memo nunca envia qualquer documento para audiência externa (board, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento gerado vai primeiro para Notion como draft. Somente após founder marcar como aprovado o envio é permitido. Este gate é inviolável e não pode ser desabilitado.
- [ ] **HITL** — WARGAMING DE CONCORRENTE ESPECÍFICO (L2): Quando Brutus simula um concorrente específico com dados sensíveis (ex: informações não-públicas sobre capacidades financeiras ou decisões internas), o output é marcado como confidencial e apresentado ao founder antes de ser incluído em qualquer documento compartilhável. Dados de origem não-verificada são explicitamente rotulados.
- [ ] **HITL** — DECISÃO DE MONITORAMENTO CONTÍNUO (L2): Após wargaming concluído, Atlas apresenta lista de tripwires sugeridos para aprovação do founder antes de ativar Tripwire. O founder pode ajustar thresholds, remover indicadores ou adicionar novos. Apenas após aprovação o monitoramento é ativado para evitar notificações não-desejadas.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
