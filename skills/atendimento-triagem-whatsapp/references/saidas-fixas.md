# As 4 saídas fixas

Toda conversa de triagem termina em uma destas — nunca em silêncio, nunca em loop.

1. **Agendar** — a pessoa quer marcar algo que o negócio já sabe agendar. Encaminha para a skill/rotina de agenda (`rotina-agenda`) ou pede os dados mínimos (nome, serviço, dia preferido) e confirma.
2. **Orçar** — a pessoa quer saber quanto custa algo que depende de tabela ou avaliação. Se há tabela fixa fornecida pelo dono, responde com ela. Se depende de avaliação, marca uma saída "agendar avaliação", nunca chuta valor.
3. **Encaminhar para humano** — urgência, reclamação, pedido fora do escopo do roteiro, ou a pessoa pediu explicitamente para falar com alguém. Mensagem de handoff: confirma que foi entendido, avisa que um humano vai responder, e dá prazo realista (ex.: "em até 2h no horário comercial").
4. **Encerrar educadamente** — a pessoa só queria uma informação simples que já foi respondida (horário, endereço), ou não teve interesse real. Encerra com uma frase curta e a porta aberta ("Qualquer coisa, é só chamar por aqui").
