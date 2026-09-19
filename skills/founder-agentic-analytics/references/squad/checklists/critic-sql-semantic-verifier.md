# Checklist do critic SQL & Semantic Verifier — Ágentic Analytics

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Themis (SQL & Semantic Verifier) — Valida toda resposta antes de ser entregue ao founder. Verifica: (1) o SQL gerado esta correto e nao ha risco de retornar dado errado por join incorreto ou filtro invertido; (2) a metrica consultada esta sendo usada conforme sua definicao formal no schema semantico (sem reinterpretacao); (3) a interpretacao narrativa e consistente com os numeros apresentados; (4) nao ha alucinacao — todo numero na resposta e rastreavel a uma linha do resultado da query; (5) o nivel de confianca declarado e justo. Se encontrar problema, devolve para o worker responsavel com feedback especifico antes de liberar para o founder.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Themis (SQL & Semantic Verifier)
- [ ] **C02** — Valida toda resposta antes de ser entregue ao founder
- [ ] **C03** — Verifica: (1) o SQL gerado esta correto e nao ha risco de retornar dado errado por join incorreto ou filtro invertido
- [ ] **C04** — (2) a metrica consultada esta sendo usada conforme sua definicao formal no schema semantico (sem reinterpretacao)
- [ ] **C05** — (3) a interpretacao narrativa e consistente com os numeros apresentados
- [ ] **C06** — (4) nao ha alucinacao
- [ ] **C07** — todo numero na resposta e rastreavel a uma linha do resultado da query
- [ ] **C08** — (5) o nivel de confianca declarado e justo
- [ ] **C09** — Se encontrar problema, devolve para o worker responsavel com feedback especifico antes de liberar para o founder

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação de nova métrica na camada semântica (Ariadne propõe, founder ou data owner aprova antes de adicionar ao schema — L3, irreversível pois altera definições que afetam todas as queries futuras)
- [ ] **HITL** — Resolução de conflito de definição entre métricas (quando duas métricas existentes têm definições inconsistentes, founder decide qual é a oficial — L3)
- [ ] **HITL** — Configuração de thresholds de alerta para Cassandra (founder define o que é 'crítico' vs 'atenção' para cada métrica do seu negócio — L3 no setup inicial, L2 depois)
- [ ] **HITL** — Confirmação de decisão tomada com base em dados para o Clío registrar (founder confirma que vai agir — não é automático para evitar log de decisões não tomadas)
- [ ] **HITL** — Acesso a novas fontes de dados não mapeadas (conectar novo banco, nova planilha, nova API ao schema — L3 por impacto na governança)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
