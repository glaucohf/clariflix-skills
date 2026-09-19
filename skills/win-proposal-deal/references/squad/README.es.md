# DealForge

### Propuestas que cierran. En minutos, no dias.

<br>

> _"Mientras armas propuestas en Google Docs, tu competencia ya envio una personalizada."_

<br>

Tu equipo comercial pierde deals por lentitud, pricing a ojo y propuestas genericas que no convencen a nadie. DealForge es un squad de 4 agentes IA que transforma datos brutos del prospect en una **propuesta comercial completa, persuasiva y con prediccion de tasa de cierre** — todo antes de que se enfrie tu cafe.

## Instalacion

```bash
npx squads add Renat0z/squads-sh-aios/proposal-engine
```

## Por que tu agencia pierde deals

| Sintoma | Consecuencia |
|---------|-------------|
| Las propuestas tardan **dias** | El prospect se enfria, la competencia llega primero |
| El pricing es **a ojo** | Cobras de mas y pierdes, o cobras de menos y desangras margen |
| Alcance **copy-paste** | Propuestas genericas que no hablan el idioma del prospect |
| Las objeciones te agarran **desprevenido** | "Muy caro", "necesito pensarlo" — y no tienes respuesta |
| **Cero visibilidad** de win-rate | No sabes si tienes 30% u 80% de chance antes de enviar |

## Como DealForge lo resuelve

```
Datos del prospect ──▶ [ DealForge ] ──▶ Propuesta lista + Win-Rate predicho
```

El pipeline pasa por **4 agentes especializados**, cada uno dueno de una etapa critica:

### 1. Radiografia del Prospect
**ProspectAnalyzer** se sumerge en los datos — empresa, sector, presupuesto, dolores, historial — y entrega un mapa completo de oportunidades y riesgos.

### 2. Alcance en 3 Versiones
**ScopeArchitect** disena tres opciones estrategicas — Esencial, Recomendado y Premium — con anclaje de precio que guia al prospect hacia la version ideal.

### 3. Pricing Inteligente
**PricingStrategist** calcula el precio optimo: margen saludable x maximo win-rate. Nada de "a ojo".

### 4. Propuesta Matadora
**ProposalComposer** junta todo en una propuesta persuasiva con copy personalizado, objeciones ya anticipadas y CTA estrategico.

**Resultado:** propuesta profesional en minutos, con prediccion de tasa de aprobacion.

## Squad

| | Agente | Arquetipo | Que hace |
|---|--------|-----------|---------|
| 🔍 | **ProspectAnalyzer** | Guardian | Analiza prospect, historial y mapea dolores/objeciones |
| 📐 | **ScopeArchitect** | Builder | Disena alcance en 3 versiones con timeline y hitos |
| 💰 | **PricingStrategist** | Balancer | Precifica con margen optimizado y win-rate predictivo |
| 📝 | **ProposalComposer** | Flow_Master | Compone propuesta persuasiva con manejo de objeciones |

## Workflows

### `proposal_generation_pipeline` — Pipeline completo
De cero a propuesta final en un comando.
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — Revision rapida
Ajusta propuesta existente segun feedback del prospect.
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## Uso

```bash
# Pipeline completo — del prospect a la propuesta final
/SQUADS:pe:prospect-analyzer

# O usa agentes individuales
/SQUADS:pe:prospect-analyzer     # Radiografia del prospect
/SQUADS:pe:scope-architect       # Diseno de alcance
/SQUADS:pe:pricing-strategist    # Pricing estrategico
/SQUADS:pe:proposal-composer     # Composicion de propuesta
```

## Tasks

| Task | Responsable | Capa |
|------|-------------|------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## Autor

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## Licencia

MIT
