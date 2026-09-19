# Tech Stack — Brain Squad

## Runtime

- Claude Code CLI (Agent Teams)
- AIOS Core 2.1.0+

## Agent Framework

- Claude Code Agent Teams com roteamento por modelo
- Haiku: geracao em escala (10x paralelo)
- Sonnet: filtragem e sintese
- Opus: orquestracao e facilitacao interativa

## Tools

- Bash: escrita de arquivos de contrato
- Read/Glob: leitura de arquivos de contrato
- Agent: lancamento de subagentes paralelos
- Write: criacao de relatorios finais

## Languages

- Markdown (documentos, relatorios)
- YAML (workflows, configuracao)
- JSON (contratos de dados: top10.json, top3.json, context-manifest)

## File System

- `.brainstorm-tmp/`: diretorio temporario para contratos entre agentes
- Cleanup automatico ao final do pipeline
