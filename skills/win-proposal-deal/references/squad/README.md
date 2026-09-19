# DealForge

### Propostas que fecham. Em minutos, nao dias.

<br>

> _"Enquanto voce monta proposta no Google Docs, seu concorrente ja mandou uma personalizada."_

<br>

Seu time comercial perde deals por lentidao, pricing no feeling e propostas genericas que nao convencem ninguem. O DealForge e um squad de 4 agentes IA que transforma dados brutos do prospect em **proposta comercial completa, persuasiva e com previsao de taxa de aprovacao** — tudo antes do cafe esfriar.


## Por que sua agencia perde deals

| Sintoma | Consequencia |
|---------|-------------|
| Propostas demoram **dias** | Prospect esfria, concorrente chega primeiro |
| Pricing no **feeling** | Cobra demais e perde, ou cobra de menos e sangra margem |
| Escopo **copy-paste** | Proposta generica que nao fala a lingua do prospect |
| Objecoes pegam de **surpresa** | "Ta caro", "vou pensar" — e voce sem resposta |
| **Zero visibilidade** de win-rate | Nao sabe se tem 30% ou 80% de chance antes de enviar |

## Como o DealForge resolve

```
Dados do prospect ──▶ [ DealForge ] ──▶ Proposta pronta + Win-Rate previsto
```

O pipeline passa por **4 agentes especializados**, cada um dono de uma etapa critica:

### 1. Radiografia do Prospect
O **ProspectAnalyzer** mergulha nos dados — empresa, setor, budget, dores, historico — e entrega um mapa completo de oportunidades e riscos.

### 2. Escopo em 3 Versoes
O **ScopeArchitect** desenha tres opcoes estrategicas — Essencial, Recomendado e Premium — com ancoragem de preco que guia o prospect para a versao ideal.

### 3. Pricing Inteligente
O **PricingStrategist** calcula o preco otimo: margem saudavel x maximo win-rate. Nada de "chutometro".

### 4. Proposta Matadora
O **ProposalComposer** junta tudo em uma proposta persuasiva com copy personalizado, objecoes ja antecipadas e CTA estrategico.

**Resultado:** proposta profissional em minutos, com previsao de taxa de aprovacao.

## Squad

| | Agente | Archetype | O que faz |
|---|--------|-----------|-----------|
| 🔍 | **ProspectAnalyzer** | Guardian | Analisa prospect, historico e mapeia dores/objecoes |
| 📐 | **ScopeArchitect** | Builder | Desenha escopo em 3 versoes com timeline e marcos |
| 💰 | **PricingStrategist** | Balancer | Precifica com margem otimizada e win-rate preditivo |
| 📝 | **ProposalComposer** | Flow_Master | Compoe proposta persuasiva com objection handling |

## Workflows

### `proposal_generation_pipeline` — Pipeline completo
Do zero a proposta final em um comando.
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — Revisao rapida
Ajusta proposta existente com base em feedback do prospect.
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## Uso

```bash
# Pipeline completo — do prospect a proposta final
/SQUADS:pe:prospect-analyzer

# Ou use agentes individuais
/SQUADS:pe:prospect-analyzer     # Radiografia do prospect
/SQUADS:pe:scope-architect       # Design de escopo
/SQUADS:pe:pricing-strategist    # Pricing estrategico
/SQUADS:pe:proposal-composer     # Composicao da proposta
```

## Tasks

| Task | Responsavel | Camada |
|------|-------------|--------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## Autor

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## Licenca

MIT
