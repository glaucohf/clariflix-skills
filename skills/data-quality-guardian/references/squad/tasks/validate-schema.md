---
name: "Validate Schema"
description: "Validação de schema conduzida pelo schema-validator: infere ou carrega o schema esperado, valida tipos campo a campo, verifica constraints (not null, unique, check), checa integridade referencial entre entidades, detecta breaking changes vs a versão anterior, avalia compatibilidade backward/forward e gera o schema-validation-report.md com o impacto downstream de cada breaking change."

inputs:
  - name: dataset
    type: string
    description: "Dataset para validação — do usuário ou da task fullDataQualityAudit()"
    required: true
  - name: expectedSchema
    type: json
    description: "Schema esperado (JSON Schema, Avro, DDL); inferido se omitido"
    required: false
  - name: references
    type: array
    description: "Tabelas/entidades de referência para checagem de integridade referencial"
    required: false

outputs:
  - name: schemaReport
    type: file
    description: "schema-validation-report.md com breaking changes e violações, enviado a data-quality-reporter e remediation-suggester"
    required: true
  - name: breakingChanges
    type: array
    description: "Lista estruturada de breaking changes detectadas (breaking-changes.json)"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "100% dos campos validados contra schema esperado"
  - blocker: true
    criteria: "Breaking changes listadas com impacto downstream"
  - blocker: false
    criteria: "Integridade referencial verificada entre entidades"
---

# Validate Schema

## Flow

```
1. Receber dataset e schema esperado
2. Inferir ou carregar schema esperado
3. Validar tipos de dados campo a campo
4. Verificar constraints (not null, unique, check)
5. Checar integridade referencial entre tabelas/entidades
6. Detectar breaking changes vs versão anterior do schema
7. Avaliar compatibilidade backward/forward
8. Gerar schema-validation-report.md
9. Enviar para @data-quality-reporter
```

## Elicitation

- "Qual o dataset para validação de schema?"
- "Há um schema esperado documentado? (JSON Schema, Avro, DDL)"
- "Quais tabelas/entidades devem ser verificadas para integridade referencial?"
- "Qual a versão anterior do schema para detecção de breaking changes?"

## Performance

- **Duração esperada:** 5-10 minutos
- **Custo estimado:** ~0 (validação local)
- **Cacheável:** sim
- **Paralelizável:** sim

## Error Handling

- **Estratégia:** retry (máx. 3 tentativas, backoff exponencial base=5s, max=30s)
- **Fallback:** se o schema esperado não estiver disponível, inferir o schema do dataset e reportá-lo como baseline
- **Notificação:** data-quality-reporter
