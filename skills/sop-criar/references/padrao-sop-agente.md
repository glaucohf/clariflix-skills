# Padrão do SOP para agente (YAML)

```yaml
processo: nome-do-processo
gatilho: evento que inicia
states:
  - id: estado_1
    acao: o que o agente faz
    ferramenta: nome do sistema/API usado
    proximo: estado_2
  - id: estado_2
    decisao:
      criterio: "valor > 500"
      se_verdadeiro: estado_escalar
      se_falso: estado_seguir
decisions:
  - id: escalar_ou_seguir
    criterio: "condição explícita, nunca 'depende'"
handoff_humano:
  gatilho: "condição que exige parar e chamar humano"
  para: "papel/pessoa"
```

Regra: toda `decisao` tem `criterio` em texto verificável (comparação, lista fechada de valores, ou regra numérica) — nunca um adjetivo vago ("caso complexo", "se fizer sentido").
