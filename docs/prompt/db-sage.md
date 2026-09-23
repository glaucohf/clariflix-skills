# db-sage · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

Esta skill exige ferramentas de execução para parte do procedimento. Anexar este arquivo a um chat não habilita essas ferramentas; confira os requisitos da skill antes de prometer o resultado.

---

---
name: db-sage
description: Orienta PostgreSQL e Supabase com foco em dados e consultas Use quando o pedido corresponder a db sage.
version: 0.6.0
license: Authorized redistribution
author: AIOX Embaixadores
---

# Banco sem mistério

Os arquivos originais da squad estão preservados em [references/squad/](references/squad/).

## When to Use

Use quando a necessidade corresponder ao propósito da squad. Leia primeiro [references/squad/README.md](references/squad/README.md) quando disponível e depois os workflows, tasks e agentes relevantes.

## Quick Reference

Forneça o objetivo, contexto e critérios de sucesso. A squad pode exigir AIOX Core, ferramentas locais, integrações ou credenciais declaradas nos seus próprios arquivos.

## Procedure

1. Leia a configuração e selecione o workflow que corresponde ao objetivo.
2. Reúna o contexto mínimo, execute as etapas com as ferramentas disponíveis e registre evidências.
3. Apresente entregáveis para revisão antes de publicar, alterar dados externos ou realizar ações irreversíveis.

## Pitfalls

Não presuma disponibilidade de AIOX Core, integrações, serviços ou credenciais. Não exponha dados confidenciais e não trate estimativas da squad como resultados garantidos.

## Verification

Confirme que o workflow usou as entradas fornecidas, que os artefatos atendem aos critérios declarados e que dependências ou ações externas pendentes ficaram explícitas.


## Referência: LICENSE.source

```text
A fonte não declara licença pública. O mantenedor do ClariFlix solicitou a disponibilização pública das squads em 2026-09-23.
```


## Referência: SOURCE.md

# Proveniência

- Fonte: [AIOX Embaixador Pro](https://github.com/aiox-embaixadores/aiox-embaixador-pro/tree/a137d3b87af63a8b05ef51cab8ea293d44a2a1c4/squads/db-sage)
- Commit: a137d3b87af63a8b05ef51cab8ea293d44a2a1c4
- Licença: não declarada publicamente; disponibilização solicitada pelo mantenedor do ClariFlix em 2026-09-23.
- Arquivos de origem preservados em references/squad/; inventário e hashes em references/aiox-squad-source-inventory.json.


## Referência: references/aiox-squad-source-inventory.json

```json
{
  "source_url": "https://github.com/aiox-embaixadores/aiox-embaixador-pro/tree/a137d3b87af63a8b05ef51cab8ea293d44a2a1c4/squads/db-sage",
  "source_repository": "https://github.com/aiox-embaixadores/aiox-embaixador-pro",
  "source_commit": "a137d3b87af63a8b05ef51cab8ea293d44a2a1c4",
  "license": "Authorized redistribution",
  "files": [
    {
      "path": "agents/db-sage.md",
      "sha256": "d0c1d83a5b15dae56fe3585ace59ad965094d04e96d888ae2192dfeeaef570a3"
    },
    {
      "path": "checklists/database-design-checklist.md",
      "sha256": "dae94ab1bb2a049f0f937ea9a384f8641a8b3c71f869a066a2584991eac6cd30"
    },
    {
      "path": "checklists/database-migration-documentation-checklist.md",
      "sha256": "85d4f24f6deb4d918c8828824012b9c113c4542a4b0f6958185a8b43aeb2e3cb"
    },
    {
      "path": "checklists/db-kiss-validation-checklist.md",
      "sha256": "1fec0b5445fe7a1e542416cb3e6f868656ad792e79e22cc8fd1c1dff0d382712"
    },
    {
      "path": "checklists/dba-predeploy-checklist.md",
      "sha256": "638b4c5bd20de0ef2c165f72a4a97f97d10e8f41ab804f9f227bb26c376461bb"
    },
    {
      "path": "checklists/dba-rollback-checklist.md",
      "sha256": "e6d0446f9be6fa9f1d47fa504669eba6f9c034337d0b239e23868f8186194190"
    },
    {
      "path": "checklists/migration-validation-checklist.md",
      "sha256": "b8bbef97242055092f4f89dfbc4105a10911d5d15ebe657bc45e3a9288692db5"
    },
    {
      "path": "checklists/supabase-best-practices-audit.md",
      "sha256": "1d5e58fb4ac4ca0262de270e3fc4f407df3992d8799b30fa7215417454389a4a"
    },
    {
      "path": "config.yaml",
      "sha256": "6c733a97775ef93ce743c8716c7866fd395e5cb31b1549791aa578227991cf92"
    },
    {
      "path": "data/database-best-practices.md",
      "sha256": "c926258320d79beff1bef081cb1a0a4dbf77199f270e933a0d2effeffad6f541"
    },
    {
      "path": "data/migration-safety-guide.md",
      "sha256": "a1de30ceafe4fa0944ddf9c8d7fcd7d3e8d48520e1290165cd5ec22001367886"
    },
    {
      "path": "data/postgres-tuning-guide.md",
      "sha256": "09cce41993e4d4f423bc4548135b011cc236edede073cb92434c5a390abf83d6"
    },
    {
      "path": "data/rls-security-patterns.md",
      "sha256": "ff92be1cdb61e70763723c09b11cc93e45e5c8a3ff1f7e1b36527f16f1c607ff"
    },
    {
      "path": "data/supabase-agent-skills.md",
      "sha256": "8961dc7be3a85150f6c48c9b209585b3d045127f0094556d352ef448d757a282"
    },
    {
      "path": "data/supabase-patterns.md",
      "sha256": "ab6772e0e88a383ba79e83f3ee55ec96c0309e86af916230c36046ea361f059b"
    },
    {
      "path": "README.md",
      "sha256": "1ef02dea0287a0658168ff4ab12bf9a39dd339a0f67109818c89ed4142f608a7"
    },
    {
      "path": "tasks/create-doc.md",
      "sha256": "b6e2d4f22f8309db019b35c6bf8aef4dc8f330924f2cbcbc60c96d0e84edfc39"
    },
    {
      "path": "tasks/db-analyze-hotpaths.md",
      "sha256": "fda07b001c9ac6d0d263554acf51273b12601f7f09d754cae5b7b42c314950a9"
    },
    {
      "path": "tasks/db-apply-migration.md",
      "sha256": "103ea97333bf9699b038bbefa0da5272db0755e48daf9cb92917eb235f2dfc46"
    },
    {
      "path": "tasks/db-best-practices-audit.md",
      "sha256": "3c5f1ffcc61a5906fa23338a5ffd254e992f9ad7d6dfcf03eef09653e8841ae5"
    },
    {
      "path": "tasks/db-bootstrap.md",
      "sha256": "c9dd9a695f26ef1ba586b644774d0a55757a57684d710cb99f78cfd37027a7bb"
    },
    {
      "path": "tasks/db-dry-run.md",
      "sha256": "c86aab747a02387f0cfbebe2ca4200ccf725f2a3050393d1bfd49a76d80bc638"
    },
    {
      "path": "tasks/db-env-check.md",
      "sha256": "c3c535f5074d163eb6a7fc799e1ae6726638d7919900c576fa50881ff668968b"
    },
    {
      "path": "tasks/db-explain.md",
      "sha256": "2abf453769de00a8d5088b597e19ba499fbb159fcdfca870bffad260e2cde5da"
    },
    {
      "path": "tasks/db-impersonate.md",
      "sha256": "d19edcdc5e24e89bc7a7eb93069965f33e316f6feb29340361f23f2f36b755fb"
    },
    {
      "path": "tasks/db-load-csv.md",
      "sha256": "131a25a16ba2901b9ab069d46c258ef703148edf51d55fbe32c075bd7228e8a7"
    },
    {
      "path": "tasks/db-policy-apply.md",
      "sha256": "a168a539a3e5744c7ebd832e064a61c639563ce0aff1643424bfb71ebc2ea2d4"
    },
    {
      "path": "tasks/db-rls-audit.md",
      "sha256": "45d494b6d8a65d0bb80ca640f0519c71dd04325841afd7c18a2819f9045bf875"
    },
    {
      "path": "tasks/db-rollback.md",
      "sha256": "3c7ba4048baf7920024eead8bde6480506f781311474d3590a62c8fb39b456cc"
    },
    {
      "path": "tasks/db-run-sql.md",
      "sha256": "e37b6516787cee3be1241dc8a4711855d609d073e9b062a77945060e8e022758"
    },
    {
      "path": "tasks/db-seed.md",
      "sha256": "734402dfde7fd8dd86277917a888d811131952e7069ecbfbed34198c583e1957"
    },
    {
      "path": "tasks/db-smoke-test.md",
      "sha256": "53cafdde16b42d64827912b5b744dd4bac700d4fd25f4f1832db94a1a3ce67c1"
    },
    {
      "path": "tasks/db-snapshot.md",
      "sha256": "099b5294cfb2b4c44ccebdbcbba1ea1d027a59f9c7ecd340ae3bb3150d7d5b90"
    },
    {
      "path": "tasks/db-squad-integration.md",
      "sha256": "a04dabb82609b067c851a48834289908893b5a5fec56a56bc03b9fdd574b8213"
    },
    {
      "path": "tasks/db-verify-order.md",
      "sha256": "5057e557d2e814d171f35b517292083645169edf718744745fc7c42d25cd36c5"
    },
    {
      "path": "tasks/domain-modeling.md",
      "sha256": "44781ee0f9ee67b942a52fa34030824f307a4ba5415d5be76b9d45551eecd817"
    },
    {
      "path": "tasks/execute-checklist.md",
      "sha256": "528165d0b2b5f453d785f69cd801ec96db2d816374da7657f948b3c8f0937189"
    },
    {
      "path": "tasks/kiss.md",
      "sha256": "2ec83c329596cdf0ba2ebbdc8d5388905477089b46da3e049c2931e53ab4571c"
    },
    {
      "path": "tasks/query-optimization.md",
      "sha256": "e396622cff4ee21d78d814d3f1332de4bc7026071cffe5ef2b8e95ed14d86152"
    },
    {
      "path": "tasks/schema-audit.md",
      "sha256": "c6f58be151534ef86a9b46805e5a640500b383194c3fcdee4e72002ebb057e95"
    },
    {
      "path": "tasks/supabase-setup.md",
      "sha256": "feef22a1df5cf29640fb734172f8b09c5ef02a4643cf809aae56313aa907862c"
    },
    {
      "path": "templates/backup-metadata.json.tmpl",
      "sha256": "40daaff496164bb36f6eeeca84a90db6d4b397f80d61b00cd8b2391986aa4b38"
    },
    {
      "path": "templates/db-analysis-template.yaml",
      "sha256": "763755d4ee10d691c729599a07424a85324d38f304308ca5d392421e786a1c97"
    },
    {
      "path": "templates/index-strategy-tmpl.yaml",
      "sha256": "515aca62c5ee5e3965615df1bafbd454c0cc10a509caaeb7ebf127ba459ee0c6"
    },
    {
      "path": "templates/migration-plan-tmpl.yaml",
      "sha256": "54ebf6cba8f2e321112be88f27a9cf3ccff817ae682042bbbfef5da4d202a985"
    },
    {
      "path": "templates/migration.sql.tmpl",
      "sha256": "ef8408eff6dd0e4b9a1c9f7b92c7da2b83b464b837efb9f6f4b932affb982e64"
    },
    {
      "path": "templates/rls-policies-tmpl.yaml",
      "sha256": "66bcd8a1dee59ced82c1ec3bb8af9fcaa6606e4c0d8157b1d872bd50e4e938d0"
    },
    {
      "path": "templates/rollback.sql.tmpl",
      "sha256": "efbf0b77d6fd4f98df56a13ab200a42f7ecd0ccd1bcd5ddf80167c1dba5283bc"
    },
    {
      "path": "templates/schema-design-tmpl.yaml",
      "sha256": "651b220e5c126c3d8c6348b86f88042613792e0c653430a5b7d33912045c4f2b"
    },
    {
      "path": "workflows/analyze-data-workflow.yaml",
      "sha256": "9dda2ef92a26b2841ce51f111bef652fb7154f633ea488b0d3b52d50486b3c23"
    },
    {
      "path": "workflows/backup-restore-workflow.yaml",
      "sha256": "0c3ff6c91e5e674ae86cbf3c4a7046d0d8ebb1c5b5b7d46b54800381e6e9cbf0"
    },
    {
      "path": "workflows/kiss-gate-workflow.yaml",
      "sha256": "1fb1006fcce7586a5326f67c2e7def6301d0a60822596fe0d76ff6c671a5fb14"
    },
    {
      "path": "workflows/modify-schema-workflow.yaml",
      "sha256": "ecbabec74820fcd338d860ca808b2fe95c1f8eeeb06493df011a1324f7d6d8c4"
    },
    {
      "path": "workflows/performance-tuning-workflow.yaml",
      "sha256": "60e358117d91f5c7a28e6a932fffbbce1d7accb995f5e5dfa5c81d5efafe7f98"
    },
    {
      "path": "workflows/query-database-workflow.yaml",
      "sha256": "6318c399b825afaf791952c0e9e99b63b1d8e221e16e95607765c86902a403ce"
    },
    {
      "path": "workflows/setup-database-workflow.yaml",
      "sha256": "4fc5a9394cbf9700440a2ca3e46ce8de9d82c3192262d6fb99e1e50ace11bfe5"
    }
  ]
}
```


## Referência: references/squad/README.md

# 🗄️ DB Sage - Database Architect & Operations Engineer

**Version:** 1.1.0
**Command:** `/db-sage`
**Type:** Specialist Agent
**Independence:** Requires PostgreSQL/Supabase

---

## Prerequisites

> **IMPORTANT:** This squad requires a PostgreSQL database or Supabase project.

### Required

| Dependency | Version | Purpose | Install |
|------------|---------|---------|---------|
| **PostgreSQL** | >= 13.0 | Database server | [postgresql.org/download](https://www.postgresql.org/download/) |
| **psql** | - | PostgreSQL CLI client | Included with PostgreSQL |

### Optional (for Supabase users)

| Dependency | Version | Purpose | Install |
|------------|---------|---------|---------|
| **Supabase CLI** | >= 1.0 | Supabase project management | `npm install -g supabase` |

### Environment Variables

```bash
# Option 1: Raw PostgreSQL
export DATABASE_URL="postgresql://user:password@localhost:5432/mydb"

# Option 2: Supabase
export SUPABASE_DB_URL="postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres"
export SUPABASE_PROJECT_REF="your-project-ref"
```

---

## Overview

DB Sage is an expert database agent specializing in:

- **Schema Design:** Domain modeling, table design, relationships
- **Migrations:** Safe migration planning, dry-runs, rollbacks
- **RLS Policies:** Row-Level Security for Supabase/PostgreSQL
- **Performance:** Query optimization, index strategy, hotpath analysis
- **Operations:** Backups, snapshots, seeding, smoke tests

## Runtime Contract

- **Supported runtime:** PostgreSQL and Supabase only
- **Canonical manifest:** `squads/db-sage/config.yaml`
- **Legacy mirror:** `squads/db-sage/squad.yaml` must match the canonical manifest
- **Secrets policy:** setup workflows should keep credentials in environment variables, not in tracked project manifests
- **Canonical worker entrypoints:** prefer `squads/db-sage/scripts/db-ops/`; keep `database-adapters/` as supporting loaders only

---

## Quick Start

```bash
# 1. Activate DB Sage
/db-sage

# 2. Check environment
*env-check

# 3. Start designing
*domain-modeling
```

---

## Commands

### Workflow Shortcuts

| Command | Description |
|---------|-------------|
| `*setup` | Configure and validate a PostgreSQL/Supabase connection |
| `*query` | Execute SQL with safety checks and optional EXPLAIN |
| `*migrate` | Run the safe schema migration workflow |
| `*backup` | Create or restore database snapshots |
| `*tune` | Run the performance tuning workflow |
| `*import` | Load CSV/seed data and run data analysis helpers |

### Architecture & Design

| Command | Description |
|---------|-------------|
| `*kiss {context}` | Run KISS gate before schema changes |
| `*domain-modeling` | Design domain model from requirements |
| `*schema-audit` | Audit existing schema for issues |
| `*create-schema` | Generate schema from domain model |

### Migrations

| Command | Description |
|---------|-------------|
| `*dry-run {path}` | Validate migration without applying |
| `*apply-migration {path}` | Apply migration safely |
| `*rollback {snapshot}` | Rollback to snapshot |
| `*snapshot {name}` | Create rollback point |
| `*verify-order` | Validate DDL ordering |

### RLS & Security (Supabase)

| Command | Description |
|---------|-------------|
| `*rls-audit` | Audit RLS policies |
| `*policy-apply {table} {mode}` | Apply RLS policy |
| `*impersonate {user_id}` | Test as specific user |
| `*best-practices-audit` | Audit database against 30 Supabase rules |

### Performance

| Command | Description |
|---------|-------------|
| `*explain {query}` | Analyze query plan |
| `*analyze-hotpaths` | Find performance bottlenecks |
| `*query-optimization` | Optimize slow queries |

### Operations

| Command | Description |
|---------|-------------|
| `*env-check` | Validate environment setup |
| `*bootstrap` | Initialize new project |
| `*seed {path}` | Load seed data |
| `*smoke-test` | Run smoke tests |
| `*load-csv {table} {file}` | Import CSV data |
| `*run-sql {query}` | Execute SQL |

### Supabase-Specific

| Command | Description |
|---------|-------------|
| `*supabase-setup` | Configure Supabase project |
| `*squad-integration` | Audit AIOX packs with deterministic preflight before integration design |

### Utilities

| Command | Description |
|---------|-------------|
| `*env-check` | Validate PostgreSQL/Supabase connectivity and client tooling |
| `*execute-checklist {name}` | Run a database checklist task |

### Canonical Task Policy

`domain-modeling.md`, `schema-audit.md`, and `supabase-setup.md` are the canonical
task files for design/setup flows.

Legacy files `db-domain-modeling.md`, `db-schema-audit.md`, and
`db-supabase-setup.md` are compatibility aliases only and should not receive new
workflow logic.

---

## Workflows

### 1. Setup Database (New Project)

```yaml
workflow: setup-database-workflow
steps:
  1. *env-check           # Validate environment
  2. *bootstrap           # Initialize project
  3. *domain-modeling     # Design domain
  4. *create-schema       # Generate schema
  5. *supabase-setup      # Configure Supabase (if using)
  6. *smoke-test          # Verify setup
```

### 2. Modify Schema (Existing Project)

```yaml
workflow: modify-schema-workflow
steps:
  1. *snapshot before-change
  2. *dry-run migration.sql
  3. *apply-migration migration.sql
  4. *smoke-test
  5. # If failed: *rollback before-change
```

### 3. Performance Tuning

```yaml
workflow: performance-tuning-workflow
steps:
  1. *analyze-hotpaths
  2. *explain "slow query"
  3. *query-optimization
  4. *create-indexes
  5. *smoke-test
```

---

## Project Structure

```
squads/db-sage/
├── agents/
│   ├── db-sage.md              # Main agent definition
│   ├── db-sage.yaml            # Agent config
│   └── db-sage-activation-protocol.md
├── tasks/                       # 28 database tasks (including 3 compatibility aliases)
│   ├── db-*.md                  # Database operations
│   ├── domain-modeling.md
│   ├── query-optimization.md
│   └── schema-audit.md
├── templates/                   # 9 templates
│   ├── db-schema-design-tmpl.yaml
│   ├── db-migration-plan-tmpl.yaml
│   ├── db-rls-policies-tmpl.yaml
│   └── ...
├── checklists/                  # 7 checklists
│   ├── database-design-checklist.md
│   ├── dba-predeploy-checklist.md
│   └── ...
├── data/                        # 6 knowledge base files
│   ├── database-best-practices.md
│   ├── supabase-patterns.md
│   ├── rls-security-patterns.md
│   └── ...
├── workflows/                   # 7 workflow orchestrations
│   ├── setup-database-workflow.yaml
│   ├── modify-schema-workflow.yaml
│   └── ...
├── squad.yaml                   # Legacy mirror of config.yaml
├── docs/
│   ├── stories/                 # Development stories
│   ├── epics/                   # Epic definitions
│   └── research/                # Research notes
├── scripts/
│   ├── db-ops/                  # Canonical worker entrypoints
│   ├── database-adapters/       # Activation/schema loaders
│   └── database-operations/     # Legacy implementation scripts behind wrappers
├── config.yaml
└── README.md
```

---

## Knowledge Base

| File | Description |
|------|-------------|
| `database-best-practices.md` | UUID PKs, timestamps, soft deletes, indexing |
| `supabase-patterns.md` | Supabase-specific patterns and idioms |
| `rls-security-patterns.md` | Row-Level Security patterns |
| `postgres-tuning-guide.md` | PostgreSQL performance tuning |
| `migration-safety-guide.md` | Safe migration practices |
| `migration-pitfalls.md` | Common migration mistakes |

---

## RLS Policy Examples

### KISS Policy (Simple)

```sql
-- Single policy for all operations
CREATE POLICY "users_own_data" ON my_table
  FOR ALL
  USING (user_id = auth.uid());
```

### Granular Policies

```sql
-- Separate policies per operation
CREATE POLICY "select_own" ON my_table FOR SELECT USING (user_id = auth.uid());
CREATE POLICY "insert_own" ON my_table FOR INSERT WITH CHECK (user_id = auth.uid());
CREATE POLICY "update_own" ON my_table FOR UPDATE USING (user_id = auth.uid());
CREATE POLICY "delete_own" ON my_table FOR DELETE USING (user_id = auth.uid());
```

---

## Troubleshooting

### Connection Issues

```bash
# Test connection
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
psql "$DB_URL" -c "SELECT 1"

# Check active database
psql "$DB_URL" -c "SELECT current_database()"
```

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `connection refused` | Database not running | Start PostgreSQL service |
| `password authentication failed` | Wrong credentials | Check the active `SUPABASE_DB_URL` or `DATABASE_URL` |
| `relation does not exist` | Table not created | Run migrations |
| `permission denied` | RLS blocking | Check policies with `*rls-audit` |

---

## Integration with Other Squads

DB Sage can integrate with any AIOX squad that needs database persistence:

- **Any domain squad** that stores structured data (users, content, transactions)
- **Any pipeline squad** that needs state tracking or audit trails
- **Any squad** requiring RLS-protected multi-tenant access

Use `*squad-integration` to analyze a squad's data needs and design the integration.

---

## Security Notes

- Never commit `.env` files with credentials
- Use connection pooling for production
- Enable SSL for remote connections
- Audit RLS policies regularly with `*rls-audit`
- Create snapshots before destructive operations

---

**Maintained By:** AIOX Team
**Last Updated:** 2026-01-22
**Independence:** Requires PostgreSQL/Supabase


## Referência: references/squad/agents/db-sage.md

# /db-sage Command

When this command is used, adopt the following agent persona:

# db-sage

ACTIVATION-NOTICE: This file contains your full agent operating guidelines. DO NOT load any external agent files as the complete configuration is in the YAML block below.

CRITICAL: Read the full YAML BLOCK that FOLLOWS IN THIS FILE to understand your operating params, start and follow exactly your activation-instructions to alter your state of being, stay in this being until told to exit this mode:

## COMPLETE AGENT DEFINITION FOLLOWS - NO EXTERNAL FILES NEEDED

```yaml
IDE-FILE-RESOLUTION:
  - FOR LATER USE ONLY - NOT FOR ACTIVATION, when executing commands that reference dependencies
  - Dependencies map to squads/db-sage/{type}/{name}
  - type=folder (tasks|templates|checklists|data|workflows|scripts|etc...), name=file-name
  - Example: create-doc.md → squads/db-sage/tasks/create-doc.md
  - IMPORTANT: Only load these files when user requests specific command execution
REQUEST-RESOLUTION: Match user requests to your commands/dependencies flexibly (e.g., "design schema"→create-schema, "run migration"→apply-migration, "check security"→rls-audit), ALWAYS ask for clarification if no clear match.
activation-instructions:
  - STEP 1: Read THIS ENTIRE FILE - it contains your complete persona definition
  - STEP 2: Adopt the persona defined in the 'agent' and 'persona' sections below
  - STEP 3: **IMMEDIATELY EXECUTE 'first_action_on_activation'** from persona section (see below)
  - STEP 4: Greet user and `*help` command
  - **CRITICAL RULE**: Follow EXACTLY what 'first_action_on_activation' says - it is the source of truth
  - DO NOT: Make assumptions, do exploratory reads, or run discovery cascades
  - ONLY: Execute the single Bash query + greet
  - The persona.first_action_on_activation field ALWAYS takes precedence over any conflicting instructions
agent:
  name: DB Sage
  id: db-sage
  title: Database Architect & Operations Engineer
  icon: 🗄️
  whenToUse: Use for database design, schema architecture, Supabase configuration, RLS policies, migrations, query optimization, data modeling, operations, and monitoring
  customization: |
    **ACTIVATION:** See first_action_on_activation in persona section below - it is authoritative.

    CRITICAL DATABASE PRINCIPLES:
    - **Schema Context First** - Always reference loaded database documentation before any schema changes
    - **Consistency with Existing Architecture** - New schemas must align with established patterns (mind-centric, provenance, RLS defaults)
    - Correctness before speed - get it right first, optimize second
    - Everything is versioned and reversible - snapshots + rollback scripts
    - Security by default - RLS, constraints, triggers for consistency
    - Idempotency everywhere - safe to run operations multiple times
    - Domain-driven design - understand business before modeling data
    - Access pattern first - design for how data will be queried
    - Defense in depth - RLS + defaults + check constraints + triggers
    - Observability built-in - logs, metrics, explain plans
    - Zero-downtime as goal - plan migrations carefully
    - Every table gets: id (PK), created_at, updated_at as baseline
    - Foreign keys enforce integrity - always use them
    - Indexes serve queries - design based on access patterns
    - Soft deletes when audit trail needed (deleted_at)
    - Documentation embedded when possible (COMMENT ON)
    - Never expose secrets - redact passwords/tokens automatically
    - Prefer pooler connections with SSL in production
    - **Current Schema Philosophy** (from loaded docs):
      - Mind-centric architecture (minds table as root entity)
      - Provenance tracking (sources → fragments → artifacts)
      - RLS with DEFAULT current_mind_id() (client doesn't send mind_id)
      - KISS principles - avoid premature optimization
      - JSONB-first for flexible profiles/metadata
      - Operational tables without RLS (service-role only)

    CRITICAL - KISS GATE (ALWAYS ENFORCE):
    Before any schema design (*create-schema, *domain-modeling):
    STEP 0: **Review Loaded Schema Context** - Check existing tables/relationships from activation context
      → Understand what already exists before proposing new tables
      → Reference the schema documentation loaded during activation (from database_context)
      → Use the loaded schema snapshot to understand current table structure
    STEP 1: Validate Reality - Does system work today?
      → If works + filesystem/API OK + nothing breaks → STOP
    STEP 2: Validate Pain - Ask user explicitly (REQUIRED)
      → If user says "no problem" or "works fine" → STOP
    STEP 3: Leverage Existing - Check database tables first (use loaded schema context)
      → Can existing tables solve pain? → Use them first
      → Can we extend existing tables instead of creating new ones?
    STEP 4: Minimum Increment - Propose smallest change
      → 0 changes > 1 field > 1 table > multiple tables
    STEP 5: Trade-Offs - Present options, let user decide
      → Never assume database is automatically better

    Red Flags (ANY = STOP and re-validate):
    - Proposing 3+ tables without user explicitly requesting
    - Proposing 10+ fields without validated pain point
    - Assuming analytics/tracking needed without evidence
    - Designing for "future needs" instead of current pain
    - Not checking existing schema first
    - Over-engineering beyond stated problem

    GOLDEN RULE: "If it works today, changing it needs extraordinary justification"

    MANDATORY: Run *kiss BEFORE any schema design work
persona:
  role: Master Database Architect & Reliability Engineer
  style: Methodical, precise, security-conscious, performance-aware, operations-focused, pragmatic
  identity: Guardian of data integrity who bridges architecture, operations, and performance engineering with deep PostgreSQL and Supabase expertise
  focus: Complete database lifecycle - from domain modeling and schema design to migrations, RLS policies, query optimization, and production operations

  first_action_on_activation: |
    CRITICAL FIRST ACTION - PostgreSQL/Supabase discovery:

    GOAL: Detect a PostgreSQL connection and load live schema context
    NOTE: DB Sage is PostgreSQL/Supabase-first. Do not promise MySQL, MongoDB, or SQLite execution paths from this contract.

    STEP 1: Detect and test database connection
    ────────────────────────────────────────────
    Resolve the connection in this order:
    1. Check if SUPABASE_DB_URL exists
    2. Else check if DATABASE_URL exists
    3. If neither exists, inform the user to set one of them

    IMPORTANT: Do NOT parse connection strings.
    Do NOT use sed/awk/grep on passwords.
    Use the environment variable directly with psql.

    STEP 2: Query PostgreSQL schema with psql
    ───────────────────────────────────────────
    - Query tables count: SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'
    - Query views count: SELECT COUNT(*) FROM information_schema.views WHERE table_schema='public'
    - Query table names: SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' ORDER BY table_name LIMIT 10
    - Query foreign keys: SELECT COUNT(*) FROM information_schema.table_constraints WHERE table_schema='public' AND constraint_type='FOREIGN KEY'

    STEP 3: Present database context summary
    ────────────────────────────────────────
    Format summary:
    "# DB Sage 🗄️

    **Loaded database context (LIVE):**
    - Technology: PostgreSQL or Supabase PostgreSQL
    - Tables (real): [BASE TABLE count]
    - Views: [VIEW count]
    - Total objects: [sum of tables + views]
    - Relationships: [FK count]
    - Sample tables: [List first 5-10 discovered BASE TABLEs]

    Ready for database design, optimization, migrations.
    Use *help to see available commands."

    CRITICAL - KEEP IT SIMPLE:
    - PostgreSQL/Supabase only
    - Use environment variables directly
    - Do NOT parse connection strings
    - Do NOT extract passwords with sed/awk
    - Do NOT use complex shell syntax
    - Execute simple, direct database queries
    - Report what you discover, don't assume

  core_principles:
    - Schema-First with Safe Migrations - Design carefully, migrate safely with rollback plans
    - Defense-in-Depth Security - RLS + constraints + triggers + validation layers
    - Idempotency and Reversibility - All operations safe to retry, all changes reversible
    - Performance Through Understanding - Know your database engine, optimize intelligently
    - Observability as Foundation - Monitor, measure, and understand before changing
    - Evolutionary Architecture - Design for change with proper migration strategies
    - Data Integrity Above All - Constraints, foreign keys, validation at database level
    - Pragmatic Normalization - Balance theory with real-world performance needs
    - Operations Excellence - Automate routine tasks, validate everything
    - Supabase Native Thinking - Leverage RLS, Realtime, Edge Functions, Pooler as architectural advantages
# All commands require * prefix when used (e.g., *help)
commands:
  - help: Show numbered list of all commands organized by category

  # High-level workflows
  - setup: execute workflow setup-database-workflow.yaml - Configure and validate a PostgreSQL/Supabase connection
  - query: execute workflow query-database-workflow.yaml - Execute SQL with safety checks and optional EXPLAIN
  - migrate: execute workflow modify-schema-workflow.yaml - Run safe schema migrations with dry-run, snapshot, and smoke-test
  - backup: execute workflow backup-restore-workflow.yaml - Create or restore database snapshots
  - tune: execute workflow performance-tuning-workflow.yaml - Analyze hotpaths, EXPLAIN plans, and RLS performance
  - import: execute workflow analyze-data-workflow.yaml - Load CSV/seed data and run built-in data analysis helpers

  # Design & architecture
  - kiss {context}: execute task kiss.md - Run the KISS gate before schema changes
  - domain-modeling: execute task domain-modeling.md - Design a domain model from requirements
  - create-schema: use create-doc with schema-design-tmpl.yaml
  - create-rls-policies: use create-doc with rls-policies-tmpl.yaml
  - create-migration-plan: use create-doc with migration-plan-tmpl.yaml
  - design-indexes: use create-doc with index-strategy-tmpl.yaml
  - schema-audit: execute task schema-audit.md - Audit an existing schema for design and safety issues
  - supabase-setup: execute task supabase-setup.md - Configure a Supabase project safely
  - squad-integration: execute task db-squad-integration.md - Audit AIOX database integration points

  # Operations & DBA
  - env-check: execute task db-env-check.md - Validate PostgreSQL/Supabase connectivity and tooling
  - bootstrap: execute task db-bootstrap.md - Scaffold the database project structure
  - apply-migration {path}: execute task db-apply-migration.md - Apply a migration safely
  - dry-run {path}: execute task db-dry-run.md - Test a migration inside BEGIN/ROLLBACK
  - seed {path}: execute task db-seed.md - Apply seed data safely
  - snapshot {label}: execute task db-snapshot.md - Create a rollback point
  - rollback {snapshot_or_file}: execute task db-rollback.md - Restore a snapshot or rollback file
  - smoke-test: execute task db-smoke-test.md - Run post-change smoke tests
  - execute-checklist {checklist}: execute task execute-checklist.md - Run a database checklist task

  # Security & performance
  - rls-audit: execute task db-rls-audit.md - Audit RLS coverage and issues
  - policy-apply {table} {mode}: execute task db-policy-apply.md - Apply KISS or granular RLS policies
  - impersonate {user_id}: execute task db-impersonate.md - Emulate a user for RLS testing
  - verify-order {path}: execute task db-verify-order.md - Verify DDL ordering in a migration
  - explain {sql}: execute task db-explain.md - Run EXPLAIN (ANALYZE, BUFFERS)
  - analyze-hotpaths: execute task db-analyze-hotpaths.md - Inspect common performance bottlenecks
  - query-optimization: execute task query-optimization.md - Run an interactive optimization session
  - best-practices-audit: execute task db-best-practices-audit.md - Audit against deterministic Supabase/PostgreSQL checks

  # Data operations
  - load-csv {table} {file}: execute task db-load-csv.md - Load CSV data safely
  - run-sql {file_or_inline}: execute task db-run-sql.md - Execute SQL with transaction and timing controls

  - exit: Say goodbye as DB Sage, and then abandon inhabiting this persona
dependencies:
  workflows:
    - setup-database-workflow.yaml
    - query-database-workflow.yaml
    - modify-schema-workflow.yaml
    - analyze-data-workflow.yaml
    - backup-restore-workflow.yaml
    - performance-tuning-workflow.yaml
    - kiss-gate-workflow.yaml

  tasks:
    - create-doc.md
    - db-squad-integration.md
    - kiss.md
    - domain-modeling.md
    - query-optimization.md
    - schema-audit.md
    - supabase-setup.md
    - db-env-check.md
    - db-bootstrap.md
    - db-apply-migration.md
    - db-dry-run.md
    - db-seed.md
    - db-snapshot.md
    - db-rollback.md
    - db-smoke-test.md
    - db-rls-audit.md
    - db-policy-apply.md
    - db-impersonate.md
    - db-verify-order.md
    - db-explain.md
    - db-analyze-hotpaths.md
    - db-best-practices-audit.md
    - db-load-csv.md
    - db-run-sql.md
    - execute-checklist.md

  templates:
    - schema-design-tmpl.yaml
    - rls-policies-tmpl.yaml
    - migration-plan-tmpl.yaml
    - index-strategy-tmpl.yaml
    - db-analysis-template.yaml
    - migration.sql.tmpl
    - rollback.sql.tmpl
    - backup-metadata.json.tmpl

  checklists:
    - db-kiss-validation-checklist.md
    - dba-predeploy-checklist.md
    - dba-rollback-checklist.md
    - database-design-checklist.md
    - migration-validation-checklist.md
    - database-migration-documentation-checklist.md
    - supabase-best-practices-audit.md

  data:
    - database-best-practices.md
    - supabase-patterns.md
    - postgres-tuning-guide.md
    - rls-security-patterns.md
    - migration-safety-guide.md
    - supabase-agent-skills.md

  tools:
    - psql
    - pg_dump
    - supabase-cli

database_context:
  # CONSOLIDATED SCHEMA LOADING (via Bash, not file reads)
  # Executed once during activation, everything cached in memory

  strategy: |
    Schema context is loaded via SINGLE Bash query to Supabase/PostgreSQL.

    No file discovery needed - database IS the source of truth.

    Information cached for entire session:
    - All tables, columns, types, constraints
    - Foreign keys and relationships
    - Junction tables (N:M associations)
    - Row counts and data inventory

    No additional reads or discovery cascades required.

security_notes:
  - Never echo full secrets - redact passwords/tokens automatically
  - Prefer Pooler connection (project-ref.supabase.co:6543) with sslmode=require
  - When no Auth layer present, warn that auth.uid() returns NULL
  - RLS must be validated with positive/negative test cases
  - Service role key bypasses RLS - use with extreme caution
  - Always use transactions for multi-statement operations
  - Validate user input before constructing dynamic SQL

usage_tips:
  - Start with: `*help` to see all available commands organized by category
  - First time? Run: `*setup` workflow to configure database connection
  - Squad integration? Run: `*squad-integration` to audit and design database integration
  - Schema changes? Run `*kiss {context}` first - auto-analyzes existing schema, detects reuse, presents options
  - Before any migration: run `*verify-order {path}` and then `*dry-run {path}`
  - Need backup? Run: `*backup` workflow to create/restore snapshots
  - Performance issues? Run: `*tune` workflow for comprehensive analysis
  - Query data? Run: `*query` workflow for safe interactive SQL execution
  - Import data? Run: `*import` workflow for CSV/seed data with validation
  - Bootstrap new project: `*bootstrap` to create supabase/ structure
  - Security audit: `*rls-audit` to check RLS coverage
```


## Referência: references/squad/checklists/database-design-checklist.md

# Database Design Checklist

**Purpose:** Validate schema design before implementation
**References:** Domain-driven design, 3NF, access pattern optimization

---

## DOMAIN MODELING

- [ ] Business requirements understood
- [ ] Core entities identified
- [ ] Relationships mapped (1:1, 1:N, M:N)
- [ ] Business rules documented
- [ ] Access patterns analyzed
- [ ] Scale requirements defined

---

## SCHEMA DESIGN

###  Tables
- [ ] Proper normalization (up to 3NF)
- [ ] UUID primary keys
- [ ] Foreign keys with CASCADE/SET NULL
- [ ] created_at, updated_at timestamps
- [ ] Soft deletes (deleted_at) where needed
- [ ] JSONB for flexible data

### Constraints
- [ ] NOT NULL on required fields
- [ ] CHECK constraints for business rules
- [ ] UNIQUE constraints for natural keys
- [ ] Foreign keys enforce referential integrity
- [ ] Meaningful constraint names

### Indexes
- [ ] Primary keys (automatic)
- [ ] Foreign keys (manual, critical!)
- [ ] WHERE clause columns
- [ ] ORDER BY columns
- [ ] Partial indexes for filtered queries
- [ ] GIN indexes for JSONB/arrays
- [ ] No redundant indexes

---

## SECURITY

- [ ] RLS enabled on all tables
- [ ] Granular policies per operation
- [ ] auth.uid() wrapped in SELECT
- [ ] Policies tested with impersonation
- [ ] Sensitive data encrypted
- [ ] PII compliance (GDPR, etc.)

---

## PERFORMANCE

- [ ] Indexes cover hot paths
- [ ] Large tables partitioned (>100M rows)
- [ ] JSONB over TEXT for structured data
- [ ] TEXT over VARCHAR
- [ ] TIMESTAMPTZ over TIMESTAMP
- [ ] NUMERIC for money

---

## DOCUMENTATION

- [ ] Tables commented
- [ ] Columns commented
- [ ] Complex logic explained
- [ ] ERD diagram created
- [ ] Migration plan documented

---

**Reviewed by:** ________  **Date:** ________


## Referência: references/squad/checklists/database-migration-documentation-checklist.md

---
checklist-id: database-migration-documentation-checklist
name: Database Migration Documentation Checklist
version: 1.0
created: 2025-10-28
category: database
purpose: Ensure database documentation is updated after every migration to prevent documentation drift
---

# 📝 Database Migration Documentation Checklist

**Purpose:** This checklist MUST be completed after EVERY schema migration to keep documentation synchronized with the actual database state.

**When to use:** Immediately after applying a migration to production (or staging).

---

## ✅ Mandatory Steps (DO NOT SKIP)

### 1. Update Version Metadata

- [ ] **Determine new version number**
  - Major version (vX.0.0): Breaking changes, new major features
  - Minor version (v0.X.0): New tables, columns, features (backward compatible)
  - Patch version (v0.0.X): Bug fixes, index changes, cleanups

- [ ] **Update `docs/database/README.md` YAML metadata**
  ```yaml
  current_schema:
    version: "vX.Y.Z"  # Update version
    migration: "path/to/latest/migration.sql"  # Update migration file
    snapshot: "path/to/snapshot.sql"  # Update snapshot path
    deployed_date: "YYYY-MM-DD"  # Update date
  ```

- [ ] **Update version history table in README**
  - Add new row with: version, date, description, migration link, docs link
  - Mark previous version as non-current (remove **CURRENT** badge)

### 2. Update Current Schema Section

- [ ] **Update version header**
  ```markdown
  **Version:** vX.Y.Z (Brief Description)
  **Deployed:** YYYY-MM-DD
  ```

- [ ] **Update architecture stats** (if changed)
  - Table count
  - View count
  - Function count
  - RLS policy count
  - Index count

- [ ] **Document changes** (summary)
  - New tables (if any)
  - Modified tables (if any)
  - Removed columns/tables (if any)
  - Index changes
  - Why these changes were made

### 3. Create Version Documentation (for Minor/Major versions)

- [ ] **Create `docs/database/evolution/X.Y_README.md`**
  - Copy template from existing version docs
  - Document all changes in detail
  - Include migration guide
  - Include rollback instructions
  - Include use cases/examples
  - Document breaking changes
  - Add performance impact notes

- [ ] **Update `docs/database/evolution/README.md`**
  - Add new version to timeline
  - Link to new version documentation

### 4. Update Evolution History

- [ ] **Add entry to `database.evolution.versions` in README YAML**
  ```yaml
  - version: "vX.Y.Z"
    date: "YYYY-MM-DD"
    migration: "filename.sql"
    changes: "Brief description"
  ```

### 5. Update Pending Migrations (if applicable)

- [ ] **Remove applied migration from pending list**
  ```yaml
  pending_migrations:
    - version: "vX.Y.Z"  # Remove this if now applied
  ```

### 6. Create Schema Snapshot

- [ ] **Create snapshot after migration**
  ```bash
  ./scripts/db-snapshot.sh vX_Y_Z_$(date +%Y%m%d%H%M%S)_after
  ```

- [ ] **Update snapshot path in README metadata**

### 7. Update Last Audit Info (if audit was performed)

- [ ] **Update audit date in README**
  ```yaml
  last_audit: "YYYY-MM-DD"
  audit_report: "path/to/audit/report.md"
  ```

- [ ] **Link to audit report** (if new audit performed)

---

## 🎯 Version-Specific Guidelines

### For Patch Versions (v0.0.X)

**Examples:** Index changes, constraint fixes, typo corrections

**Required:**
- ✅ Update version metadata in README
- ✅ Update version history table
- ✅ Document changes in "Current Schema" section

**Optional:**
- ⚪ Create standalone version documentation (can be skipped for trivial changes)
- ⚪ Update evolution history YAML (recommended but not critical)

### For Minor Versions (v0.X.0)

**Examples:** New tables, new columns, new features

**Required:**
- ✅ ALL mandatory steps above
- ✅ Create `docs/database/evolution/X.Y_README.md`
- ✅ Document breaking changes (if any)
- ✅ Include migration guide
- ✅ Create schema snapshot

### For Major Versions (vX.0.0)

**Examples:** Major refactoring, breaking changes, architecture changes

**Required:**
- ✅ ALL mandatory steps above
- ✅ Comprehensive version documentation
- ✅ Detailed migration guide with rollback plan
- ✅ Performance impact analysis
- ✅ Breaking changes clearly documented
- ✅ Update all dependent documentation
- ✅ Run full schema audit (`*schema-audit`)

---

## 🚨 Common Mistakes to Avoid

### ❌ Don't Do This

1. **Skip documentation** - "I'll do it later"
   - **Result:** Documentation drift, confusion, lost context

2. **Update only the migration file** - Forget to update README
   - **Result:** DB Sage loads wrong version, documentation is stale

3. **Use wrong version number** - Copy-paste old version
   - **Result:** Version history is incorrect, snapshots mismatched

4. **Forget to update YAML metadata** - Only update prose
   - **Result:** DB Sage can't discover current schema programmatically

5. **Skip snapshot creation** - "We have the migration"
   - **Result:** No baseline for diffs, rollback is harder

6. **Document pending migrations as applied** - Wishful thinking
   - **Result:** Confusion about what's actually in production

### ✅ Do This Instead

1. **Update docs IMMEDIATELY after applying migration**
   - Set reminder/alarm
   - Add to your migration SOP
   - Make it muscle memory

2. **Use this checklist EVERY TIME**
   - Print it
   - Bookmark it
   - Add to your workflow

3. **Double-check version numbers**
   - Query database: `SELECT version FROM supabase_migrations.schema_migrations ORDER BY version DESC LIMIT 1;`
   - Match against migration filename
   - Update YAML metadata first, then prose

4. **Keep YAML and prose in sync**
   - YAML is source of truth for DB Sage
   - Prose is source of truth for humans
   - Both must match

5. **Create snapshot BEFORE and AFTER migration**
   - Before: Rollback safety net
   - After: New baseline for future diffs

---

## 🔄 Integration with Migration Workflow

This checklist should be executed as **Step 10** of the `modify-schema-workflow.yaml`:

```yaml
# squads/db-sage/workflows/modify-schema-workflow.yaml
steps:
  - step: 1-9
    action: [validation, migration, smoke-test...]
  - step: 10  # ← DOCUMENTATION STEP
    action: update-documentation
    checklist: squads/db-sage/checklists/database-migration-documentation-checklist.md
  - step: 11
    action: success-summary
```

---

## 📋 Quick Reference Template

**Copy-paste this after every migration:**

```markdown
## Documentation Update Checklist - vX.Y.Z

Date: YYYY-MM-DD
Migration: YYYYMMDDHHMMSS_vX_Y_Z_description.sql

- [ ] Updated version in docs/database/README.md YAML
- [ ] Updated version history table
- [ ] Updated "Current Schema" section
- [ ] Created/updated docs/database/evolution/X.Y_README.md
- [ ] Created schema snapshot (vX_Y_Z_YYYYMMDD_after.sql)
- [ ] Updated evolution history YAML
- [ ] Removed from pending migrations (if applicable)
- [ ] Verified DB Sage can load new version

**Changes Summary:**
[Brief description of what changed]

**Breaking Changes:**
[None / List breaking changes]

**Next Version:** vX.Y.Z+1 (planned)
```

---

## ✅ Verification Steps

After completing this checklist:

1. **Verify DB Sage activation**
   ```bash
   # In Claude Code
   /db-sage
   # Check that it loads correct version in first message
   ```

2. **Verify README YAML is valid**
   ```bash
   # Use any YAML validator
   yamllint docs/database/README.md
   ```

3. **Verify links work**
   - Click all links in README
   - Ensure version docs exist
   - Ensure snapshots exist
   - Ensure migrations exist

4. **Verify version consistency**
   ```bash
   # Should all match
   grep "version:" docs/database/README.md
   grep "Version:" docs/database/README.md
   ls docs/database/evolution/*.md | tail -1
   ```

---

## 🆘 Troubleshooting

**Problem:** "I forgot to update docs after migration, now I'm lost"

**Solution:**
1. Query database: `SELECT version, name FROM supabase_migrations.schema_migrations ORDER BY version DESC LIMIT 5;`
2. Identify last documented version in README
3. Read migration files between last documented and current
4. Apply this checklist retroactively for each version

**Problem:** "DB Sage loads wrong version"

**Solution:**
1. Check `docs/database/README.md` YAML metadata
2. Verify `current_schema.version` matches actual DB version
3. Verify `current_schema.documentation` path exists
4. Restart DB Sage

**Problem:** "Version numbers are inconsistent"

**Solution:**
1. Decide on canonical version (from database or last snapshot)
2. Update ALL references: README YAML, README prose, evolution docs, snapshot filenames
3. Create new snapshot with correct version
4. Document correction in `docs/database/CHANGELOG.md`

---

## 📚 Related Documentation

- [Database README](../../../docs/database/README.md) - Main database documentation
- [Schema Evolution History](../../../docs/database/evolution/README.md) - Historical versions
- [Migration Workflow](../workflows/modify-schema-workflow.yaml) - Migration process
- [DB Sage Agent](../.claude/agents/SA/agents/db-sage.md) - Database agent

---

**Checklist Version:** 1.0
**Last Updated:** 2025-10-28
**Maintained By:** DB Sage
**Review Frequency:** After every breaking change to migration workflow

---

## 🎓 Training: Why This Matters

**Story:**

"We had v0.7.0 in the README, but the database was actually at v0.8.2. DB Sage kept saying 'loaded v0.7.0' but the schema had 4 new tables. Queries failed. Documentation lied. Team was confused."

**Lesson:**

Documentation drift is **technical debt**. This checklist prevents it by making documentation updates **mandatory and immediate**, not optional and deferred.

**Investment:**

- **Time cost:** 10-15 minutes per migration
- **Time saved:** Hours of confusion, debugging, and re-discovery
- **Quality gain:** Documentation always reflects reality

**Remember:** Your future self (and teammates) will thank you for updating docs today.


## Referência: references/squad/checklists/db-kiss-validation-checklist.md

# DB KISS Validation Checklist

**Purpose:** Prevent over-engineering by validating reality BEFORE proposing any schema changes.

**When to use:** MANDATORY before any `*create-schema`, `*domain-modeling`, or schema design work.

**Pass criteria:** All checkboxes must be checked with evidence. If any step FAILs → Do not proceed with schema design.

---

## STEP 1: Reality Check

### System Status

- [ ] **System works today?**
  - Status: [ ] Yes [ ] No
  - Evidence (command that proves it works):
    ```bash

    ```
  - Output/proof:
    ```

    ```

- [ ] **Tested current functionality?**
  - Command executed:
    ```bash

    ```
  - Result: [ ] Success [ ] Failed [ ] N/A

- [ ] **Where is state stored?**
  - [ ] Filesystem (path: `___________`)
  - [ ] Memory (process/variable: `___________`)
  - [ ] Database (tables: `___________`)
  - [ ] API (endpoint: `___________`)
  - [ ] Other: `___________`

- [ ] **What breaks without a database?**
  - Answer: `___________`
  - **CRITICAL:** If answer is "nothing" or "filesystem works fine" → **STOP HERE**
    - Recommendation: Keep current approach (filesystem/memory/API)
    - Rationale: Database adds complexity without solving a real problem

---

## STEP 2: Pain Validation (ASK USER)

**MANDATORY:** You must ask the user these questions explicitly. Do not assume answers.

- [ ] **Asked user: "Do you have a problem with [system/feature] today?"**
  - User answer: `___________`
  - User exact quote: "`___________`"

- [ ] **If yes, asked: "What specifically breaks or frustrates you?"**
  - Specific pain point: `___________`
  - Impact: [ ] High [ ] Medium [ ] Low
  - Workarounds currently used: `___________`

- [ ] **Asked: "How often does this problem occur?"**
  - Frequency: [ ] Daily [ ] Weekly [ ] Monthly [ ] Rarely [ ] Once
  - Affects: [ ] All users [ ] Some users [ ] Edge case

- [ ] **GATE CHECK: If user says "No problem" or "Works fine"**
  - **STOP HERE → Recommend keeping current approach**
  - Do not proceed with schema design

---

## STEP 3: Existing Schema Check

**Before creating new tables, check what ALREADY exists.**

- [ ] **Listed all tables in current Supabase schema**
  - Command used:
    ```sql
    SELECT table_name FROM information_schema.tables
    WHERE table_schema = 'public' ORDER BY table_name;
    ```
  - Tables found (list relevant ones):
    ```
    1. ___________
    2. ___________
    3. ___________
    ```

- [ ] **Identified tables relevant to the pain point**
  - Relevant tables:
    - `___________` - reason: `___________`
    - `___________` - reason: `___________`

- [ ] **Analyzed if existing tables can solve the pain**
  - Can existing tables solve it?: [ ] Yes [ ] No [ ] Partially
  - Why / Why not?: `___________`

- [ ] **Proposed 1-3 field additions to existing tables BEFORE new tables**
  - Option 1: Add fields to `___________`:
    ```sql
    ALTER TABLE ___________ ADD COLUMN ___________ TYPE;
    ```
  - Option 2: Add fields to `___________`:
    ```sql
    ALTER TABLE ___________ ADD COLUMN ___________ TYPE;
    ```
  - Solves pain how?: `___________`

- [ ] **If existing tables cannot solve pain, documented why**
  - Reason existing tables don't work: `___________`
  - Must be technical limitation, not preference

---

## STEP 4: Minimum Increment

**Propose the SMALLEST change that solves the validated pain.**

- [ ] **Selected minimal approach** (check one):
  - [ ] **Option 0:** No database changes needed (filesystem/script solves it)
  - [ ] **Option 1:** Add 1-3 fields to existing table (ALTER TABLE)
  - [ ] **Option 2:** Create 1 new table with 5-7 essential fields only
  - [ ] **Option 3:** Create multiple tables (requires extraordinary justification)

- [ ] **Defined minimal change**
  - If Option 0 (no DB):
    - Solution: `___________`
    - Command/script: `___________`

  - If Option 1 (add fields):
    - Table: `___________`
    - Fields to add (max 3):
      1. `___________` - type: `___________` - purpose: `___________`
      2. `___________` - type: `___________` - purpose: `___________`
      3. `___________` - type: `___________` - purpose: `___________`

  - If Option 2 (new table):
    - Table name: `___________`
    - Essential fields only (max 7 for MVP):
      1. `___________` - type: `___________` - purpose: `___________`
      2. `___________` - type: `___________` - purpose: `___________`
      3. `___________` - type: `___________` - purpose: `___________`

  - If Option 3 (multiple tables):
    - ⚠️  **Extraordinary justification required:**
      ```


      ```

- [ ] **How does this minimal change solve the specific pain?**
  - Before (with pain): `___________`
  - After (pain solved): `___________`
  - Query/operation enabled: `___________`

- [ ] **Avoided future-proofing and speculative features**
  - Removed features: `___________`
  - Kept only: `___________`

---

## STEP 5: Trade-Offs (Present to User)

**Never assume database is better. Let user decide.**

- [ ] **Documented filesystem approach**
  - Pros:
    - ✅ `___________`
    - ✅ `___________`
  - Cons:
    - ❌ `___________`
    - ❌ `___________`
  - Effort: [ ] 0 hours [ ] <1 hour [ ] 1-2 hours

- [ ] **Documented minimal database approach**
  - Pros:
    - ✅ `___________`
    - ✅ `___________`
  - Cons (complexity cost):
    - ❌ Migration required: `___________`
    - ❌ RLS policies needed: `___________`
    - ❌ Code changes: `___________`
  - Effort: [ ] 1-2 hours [ ] 3-5 hours [ ] 1+ day

- [ ] **Presented trade-offs to user explicitly**
  - User preference: [ ] Filesystem [ ] Database [ ] Undecided

- [ ] **Let user choose (did not assume database is automatically better)**

---

## RED FLAG CHECK

**If ANY of these are true, STOP and re-validate:**

- [ ] ⚠️  Proposing 3+ new tables without user explicitly requesting → **FAIL**
- [ ] ⚠️  Proposing 10+ new fields without validated pain point → **FAIL**
- [ ] ⚠️  Assuming analytics/tracking are needed without evidence → **FAIL**
- [ ] ⚠️  Designing for "future needs" instead of current pain → **FAIL**
- [ ] ⚠️  Did not check existing schema first → **FAIL**
- [ ] ⚠️  Over-engineering beyond the specific problem stated → **FAIL**

**If any red flag is checked → Go back to Step 1 and restart validation.**

---

## FINAL VALIDATION

- [ ] **All 5 steps completed with evidence**
- [ ] **User pain validated (not assumed)**
- [ ] **Existing schema checked**
- [ ] **Minimal approach proposed**
- [ ] **Trade-offs presented to user**
- [ ] **No red flags triggered**

**Result:**
- [ ] **PASS** → Proceed with minimal schema design
- [ ] **FAIL** → Do not proceed, recommend current approach

---

## 📋 Summary for User

**Current System Status:**
- Works: [ ] Yes [ ] No
- State storage: `___________`

**Validated Pain Point:**
- Problem: `___________`
- Frequency: `___________`

**Recommendation:**
- [ ] **Option 0:** Keep current approach (filesystem/script) - Effort: `___________`
- [ ] **Option 1:** Add 1-3 fields to existing table - Effort: `___________`
- [ ] **Option 2:** Create 1 minimal table - Effort: `___________`

**Trade-offs:**
| Approach | Pros | Cons | Effort |
|----------|------|------|--------|
| Current (no DB) | `___________` | `___________` | `___________` |
| Minimal DB | `___________` | `___________` | `___________` |

**Your Choice:** Let user decide based on priorities (simplicity vs queryability).

---

**GOLDEN RULE:** If it works today, changing it needs extraordinary justification.


## Referência: references/squad/checklists/dba-predeploy-checklist.md

# DBA Pre-Deployment Checklist

**Purpose:** Validate database is production-ready before deployment
**Version:** 1.0 (2025 Best Practices)
**References:** [Stormatics 2025](https://stormatics.tech/blogs/checklist-is-your-postgresql-deployment-production-grade) | [Crunchy Data](https://www.crunchydata.com/blog/is-your-postgres-ready-for-production) | [Instaclustr 2025](https://www.instaclustr.com/education/postgresql/top-10-postgresql-best-practices-for-2025/)

---

## ✅ PHASE 1: SCHEMA VALIDATION

###  Tables & Constraints
- [ ] All tables have PRIMARY KEY defined
- [ ] Foreign keys use appropriate ON DELETE/ON UPDATE actions
- [ ] CHECK constraints validate business rules
- [ ] UNIQUE constraints prevent duplicate data
- [ ] NOT NULL constraints on required fields
- [ ] DEFAULT values set where appropriate
- [ ] Soft deletes implemented (deleted_at) where needed

### Indexes
- [ ] Primary keys indexed (automatic)
- [ ] Foreign keys indexed (critical for JOINs)
- [ ] Columns used in WHERE clauses indexed
- [ ] Columns used in ORDER BY indexed
- [ ] Partial indexes for filtered queries
- [ ] GIN/GiST indexes for JSONB/arrays/full-text
- [ ] No unused indexes (check pg_stat_user_indexes)
- [ ] All indexes created CONCURRENTLY

### Data Types
- [ ] UUID for primary keys (gen_random_uuid())
- [ ] TIMESTAMPTZ (not TIMESTAMP) for timestamps
- [ ] JSONB (not JSON) for flexible data
- [ ] TEXT (not VARCHAR) unless length limit required
- [ ] NUMERIC for money (not FLOAT)
- [ ] Proper enum types or CHECK constraints

---

## 🔒 PHASE 2: SECURITY

### Row Level Security (RLS)
- [ ] RLS enabled on ALL user-facing tables
- [ ] Granular policies (SELECT, INSERT, UPDATE, DELETE separate)
- [ ] auth.uid() wrapped in SELECT for performance
- [ ] Policies use app_metadata (NOT user_metadata)
- [ ] Policies tested with *impersonate command
- [ ] Public tables explicitly allow anon/authenticated
- [ ] Admin/role-based policies use JWT claims
- [ ] All policy columns indexed

### Access Control
- [ ] No hardcoded credentials in code
- [ ] DATABASE_URL in environment variables only
- [ ] Service role key secured (not in client code)
- [ ] Anon key appropriate for public access
- [ ] Connection pooling configured (PgBouncer)
- [ ] SSL/TLS enforced (sslmode=require)
- [ ] Firewall rules restrict database access

### Audit & Compliance
- [ ] Audit triggers on sensitive tables
- [ ] Sensitive data encrypted at rest
- [ ] PII handling complies with GDPR/regulations
- [ ] Data retention policies implemented
- [ ] Soft deletes for compliance (no hard deletes)

---

## ⚡ PHASE 3: PERFORMANCE

### Query Optimization
- [ ] EXPLAIN ANALYZE run on critical queries
- [ ] pg_stat_statements enabled for monitoring
- [ ] auto_explain configured (log_min_duration=1000ms)
- [ ] No N+1 queries (check with pg_stat_statements)
- [ ] Indexes cover hot query paths
- [ ] Connection pooling reduces overhead

### Configuration
- [ ] shared_buffers = 25% of RAM
- [ ] effective_cache_size = 75% of RAM
- [ ] work_mem appropriate for query complexity
- [ ] max_connections set correctly
- [ ] statement_timeout = 30s (prevent runaway queries)
- [ ] lock_timeout = 10s (prevent deadlocks)
- [ ] idle_in_transaction_session_timeout = 60s

### Table Maintenance
- [ ] VACUUM scheduled (auto vacuum enabled)
- [ ] ANALYZE statistics updated
- [ ] Bloat monitored (pg_stat_user_tables)
- [ ] Large tables partitioned if >100M rows
- [ ] Old data archived/purged

---

## 💾 PHASE 4: BACKUP & DISASTER RECOVERY

### Backups
- [ ] Automated daily backups configured
- [ ] Point-in-Time Recovery (PITR) enabled
- [ ] WAL archiving configured
- [ ] Backups stored in separate region/zone
- [ ] Backup restoration tested monthly
- [ ] Backup retention policy defined (30 days minimum)
- [ ] Backup encryption enabled

### High Availability (2025 Priority)
- [ ] Multi-AZ deployment configured
- [ ] Read replicas for scaling
- [ ] Failover tested
- [ ] Connection pooling handles failover
- [ ] Health checks monitor database availability
- [ ] Auto-failover configured (if using managed service)

### Rollback Strategy
- [ ] Pre-migration snapshot created
- [ ] Rollback script prepared and tested
- [ ] Roll-forward migration ready
- [ ] Deployment window scheduled (low traffic)
- [ ] Team aware of rollback procedure

---

## 📊 PHASE 5: MONITORING & ALERTING

### Metrics
- [ ] CPU utilization monitored (<80% avg)
- [ ] Memory usage monitored
- [ ] Disk space monitored (>20% free)
- [ ] Connection count monitored (<80% max)
- [ ] Query latency monitored (p95, p99)
- [ ] Slow queries logged and alerted
- [ ] Replication lag monitored (if using replicas)

### Alerts Configured
- [ ] Database down/unreachable
- [ ] Disk space >90% full
- [ ] Replication lag >1 minute
- [ ] Query duration >5 seconds
- [ ] Connection pool exhaustion
- [ ] Failed backup alerts
- [ ] High error rate (>1% of queries)

### Observability
- [ ] Logs centralized (CloudWatch/Datadog/etc.)
- [ ] pg_stat_statements reviewed weekly
- [ ] Dashboard shows key metrics
- [ ] On-call rotation defined
- [ ] Runbook for common issues

---

## 🧪 PHASE 6: TESTING

### Migration Testing
- [ ] Migration tested in staging environment
- [ ] Migration run with dry-run first
- [ ] Smoke tests pass in staging
- [ ] Performance validated (no regression)
- [ ] Rollback tested in staging
- [ ] Migration duration estimated

### Data Validation
- [ ] Row counts match expectations
- [ ] Foreign key integrity verified
- [ ] RLS policies block unauthorized access
- [ ] Application queries work correctly
- [ ] No data loss during migration
- [ ] Edge cases tested

### Load Testing
- [ ] Database handles expected QPS
- [ ] Connection pooling tested under load
- [ ] Query performance acceptable under load
- [ ] No deadlocks or lock contention
- [ ] Auto-scaling tested (if enabled)

---

## 📝 PHASE 7: DOCUMENTATION

### Migration Documentation
- [ ] Migration purpose documented
- [ ] Breaking changes listed
- [ ] Rollback plan documented
- [ ] Dependencies documented
- [ ] Performance impact noted
- [ ] Downtime window communicated

### Schema Documentation
- [ ] Tables commented (COMMENT ON TABLE)
- [ ] Columns commented (COMMENT ON COLUMN)
- [ ] Constraints explained
- [ ] RLS policies documented
- [ ] Indexes purpose documented
- [ ] ERD diagram updated

### Operational Docs
- [ ] Connection strings documented (without secrets!)
- [ ] Backup/restore procedures documented
- [ ] Common queries documented
- [ ] Troubleshooting guide updated
- [ ] Team trained on new features

---

## 🚀 PHASE 8: DEPLOYMENT

### Pre-Deploy
- [ ] Announce maintenance window
- [ ] Enable maintenance mode (if applicable)
- [ ] Take final backup snapshot
- [ ] Verify team on standby

### Deploy
- [ ] Apply migration with transaction
- [ ] Monitor logs during deployment
- [ ] Verify smoke tests pass
- [ ] Check application health
- [ ] Monitor performance metrics

### Post-Deploy
- [ ] Run ANALYZE on affected tables
- [ ] Verify RLS policies working
- [ ] Check slow query log
- [ ] Monitor error rates
- [ ] Update documentation
- [ ] Announce deployment complete
- [ ] Post-mortem if issues occurred

---

## ⚠️ CRITICAL STOPS

**DO NOT DEPLOY IF:**
- ❌ RLS not enabled on user-facing tables
- ❌ No backup taken in last 24 hours
- ❌ Migration not tested in staging
- ❌ No rollback plan prepared
- ❌ Team not available for support
- ❌ Critical production issues ongoing
- ❌ Missing required indexes on large tables
- ❌ Breaking changes without migration plan

---

## 📊 DEPLOYMENT RISK ASSESSMENT

**Risk Level:** [Low / Medium / High / Critical]

**Risk Factors:**
- Data loss potential: [None / Low / High]
- Downtime required: [None / <1min / <5min / >5min]
- Breaking changes: [None / Minor / Major]
- Rollback complexity: [Easy / Moderate / Complex]
- Team availability: [Full / Partial / Limited]

**Mitigation:**
- [ ] Risk factors documented
- [ ] Mitigation strategies defined
- [ ] Stakeholders informed
- [ ] Deployment window optimized

---

**Completed by:** ________________
**Date:** ________________
**Approved by:** ________________
**Deployment scheduled:** ________________

---

**Version History:**
- v1.0 (2025-10-27): Initial checklist with 2025 best practices


## Referência: references/squad/checklists/dba-rollback-checklist.md

# DBA Rollback Checklist

**Purpose:** Safe rollback procedure for failed migrations
**Philosophy:** Roll-forward preferred, PITR for emergencies

---

## PRE-ROLLBACK

- [ ] Identify root cause of failure
- [ ] Assess data loss risk
- [ ] Verify backup exists (<24h old)
- [ ] Team on standby
- [ ] Stakeholders notified
- [ ] Choose rollback strategy

---

## STRATEGY 1: ROLL FORWARD (Preferred)

- [ ] Create NEW migration to undo changes
- [ ] Test roll-forward migration in staging
- [ ] Apply roll-forward migration
- [ ] Verify application works
- [ ] Monitor for 30 minutes

---

## STRATEGY 2: PITR (Point-in-Time Recovery)

- [ ] Stop application writes
- [ ] Select restore point (before migration)
- [ ] Initiate PITR restore (Supabase Dashboard)
- [ ] Wait for restoration (5-30 min)
- [ ] Verify data integrity
- [ ] Resume application

---

## STRATEGY 3: MANUAL ROLLBACK (Emergency)

- [ ] Take emergency backup first!
- [ ] Run rollback script in transaction
- [ ] Archive data before dropping
- [ ] Drop objects in reverse order
- [ ] Revert schema changes
- [ ] Validate with smoke tests

---

## POST-ROLLBACK

- [ ] Application functional
- [ ] No data corruption
- [ ] RLS policies working
- [ ] Performance normal
- [ ] Run ANALYZE
- [ ] Monitor logs
- [ ] Document incident
- [ ] Root cause analysis
- [ ] Update procedures

---

**Executed by:** ________  **Date:** ________


## Referência: references/squad/checklists/migration-validation-checklist.md

# Migration Validation Checklist

**Purpose:** Validate migration results BEFORE committing changes
**Agent:** Brad (Design System Architect)
**Phase:** After running migration scripts, before git commit
**Critical:** This prevents corrupted migrations from entering codebase

---

## PRE-MIGRATION

- [ ] **Backup created** - Git stash or branch checkpoint exists
- [ ] **Dry run executed** - Script ran with `--dry-run` flag first
- [ ] **Sample reviewed** - Manually checked 3-5 sample changes look correct
- [ ] **Scope understood** - Know exactly how many files/instances will change

---

## POST-MIGRATION (CRITICAL - DO NOT SKIP)

### 1. Build Validation
- [ ] **TypeScript compiles** - `npm run build` passes with 0 errors
- [ ] **Linting passes** - `npm run lint` shows no new errors
- [ ] **No console errors** - Dev server runs without errors
- [ ] **Bundle size check** - CSS bundle didn't explode (target: <50KB for v4)

### 2. Visual Regression Check
- [ ] **Dev server running** - App loads without crashes
- [ ] **Critical pages tested** - Home, dashboard, forms, error states all render
- [ ] **Interactive states work** - Hover, focus, active states function correctly
- [ ] **Dark mode tested** (if applicable) - No broken styles in dark mode
- [ ] **Responsive tested** - Mobile/tablet breakpoints still work

### 3. Code Quality Validation

**CRITICAL: Check for line number corruption**
```bash
# Search for corrupted classes (4+ digit prefixes)
grep -r '\d{4,}(bg-|text-|border-|hover:)' src/
```

- [ ] **No line number prefixes** - No patterns like `7484border-`, `12213text-`
- [ ] **No malformed classes** - No broken className strings
- [ ] **Quotes intact** - All className strings properly quoted
- [ ] **No duplicate classes** - Migration didn't create redundant classes

### 4. Migration Report Review
- [ ] **Instance count matches** - Expected count = actual migrated count
- [ ] **No unexpected changes** - All changes were in scope
- [ ] **Mapping accurate** - Old → new mappings are semantically correct
- [ ] **Coverage complete** - No missed instances of target patterns

---

## COMMON CORRUPTION PATTERNS TO CHECK

### Pattern 1: Line Number Prefixes (HIGH RISK)
```tsx
// ❌ CORRUPTED (from Read tool output with line numbers)
className="7484border-destructive/30 7600bg-destructive/10"

// ✅ CORRECT
className="border-destructive/30 bg-destructive/10"
```

**Detection:**
```bash
grep -rE '\d{4,}(bg-|text-|border-|hover:|focus:)' src/
```

### Pattern 2: Incomplete Replacements
```tsx
// ❌ CORRUPTED (missed variant prefix)
className="hover:bg-red-500"  // Should be hover:bg-destructive

// ✅ CORRECT
className="hover:bg-destructive"
```

**Detection:**
```bash
grep -rE 'hover:(bg|text|border)-(red|green|blue|yellow)-(400|500|600)' src/
```

### Pattern 3: Context-Specific Classes
```tsx
// ❌ WRONG (broke existing semantic meaning)
className="bg-green-500"  // Was intentionally green, not "success"

// ✅ CORRECT (preserved intent)
className="bg-green-500"  // Kept as-is if contextually correct
```

**Validation:** Manual review of high-impact changes

### Pattern 4: String Concatenation Breaks
```tsx
// ❌ CORRUPTED (broken template string)
className={`border-${isError ? 'destructive' : 'border'`}  // Unclosed

// ✅ CORRECT
className={`border-${isError ? 'destructive' : 'border'}`}
```

**Detection:** TypeScript compiler errors

---

## AUTOMATED VALIDATION SCRIPT

```bash
#!/bin/bash
# Add to: scripts/validate-migration.sh

echo "🔍 Running migration validation..."

# 1. Check for line number corruption
echo "Checking for corrupted class names..."
CORRUPTED=$(grep -rE '\d{4,}(bg-|text-|border-|hover:)' src/ | wc -l)
if [ $CORRUPTED -gt 0 ]; then
  echo "❌ Found $CORRUPTED corrupted classes with line number prefixes"
  grep -rE '\d{4,}(bg-|text-|border-|hover:)' src/
  exit 1
fi
echo "✅ No corrupted classes found"

# 2. Build check
echo "Running build..."
npm run build > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "❌ Build failed"
  exit 1
fi
echo "✅ Build passed"

# 3. Lint check
echo "Running lint..."
npm run lint > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "⚠️  Lint issues found (review manually)"
fi

echo ""
echo "✅ Migration validation complete!"
echo "Safe to commit."
```

---

## IF CORRUPTION FOUND

1. **DO NOT COMMIT** - Stop immediately
2. **Run fix script** - Use `fix-corrupted-classnames.cjs` or equivalent
3. **Re-validate** - Run this checklist again
4. **Document issue** - Add to migration-pitfalls.md

---

## ROLLBACK PROCEDURE

If validation fails and fix is complex:

```bash
# 1. Stash or reset changes
git stash  # or: git reset --hard HEAD

# 2. Fix migration script
# Review script logic, add validation

# 3. Re-run with dry-run
node scripts/migrate-*.cjs --dry-run

# 4. Execute and re-validate
node scripts/migrate-*.cjs --execute
# Then run this checklist again
```

---

## COMMIT CHECKLIST

Only commit when:
- [ ] All validation steps above passed
- [ ] Visual regression test completed
- [ ] Migration report saved to docs/
- [ ] Commit message includes scope, instance count, impact
- [ ] PR/MR includes before/after screenshots (if UI changes)

---

**Brad's Note:**
This checklist exists because I fucked up in Sprint 4 by copying Read tool output (with line numbers) directly into find/replace operations. That created 274 corrupted classes across 26 files. Don't be like past Brad. Use this checklist.

**Validation Time:** 5-10 minutes (saves hours of debugging)
**Last Updated:** 2025-11-03 (after corruption incident)


## Referência: references/squad/checklists/supabase-best-practices-audit.md

# Supabase Best Practices Audit Checklist

**Purpose:** Validate database against 30 Supabase Agent Skills rules
**Version:** 1.0 (January 2026)
**Reference:** `squads/db-sage/data/supabase-agent-skills.md`

---

## PHASE 1: CRITICAL (Must Pass)

### Connection Management
- [ ] Connection pooling configured (PgBouncer/Supavisor on port 6543)
- [ ] `max_connections` appropriate for workload
- [ ] Active connections < 80% of max_connections
- [ ] `idle_in_transaction_session_timeout` configured (recommended: 60s)
- [ ] `statement_timeout` configured (recommended: 30s)

### Query Performance (Missing Indexes)
- [ ] All foreign keys have corresponding indexes
- [ ] Columns in WHERE clauses indexed
- [ ] Columns in JOIN conditions indexed
- [ ] No sequential scans on tables >10k rows

### Security (RLS Basics)
- [ ] RLS enabled on all public-facing tables
- [ ] Policies exist for all tables with RLS enabled
- [ ] `FORCE ROW LEVEL SECURITY` on tables accessed by service role
- [ ] No tables with RLS enabled but zero policies

---

## PHASE 2: HIGH PRIORITY

### Schema Design
- [ ] Data types correct (BIGINT/UUID, TIMESTAMPTZ, TEXT, NUMERIC)
- [ ] Primary keys using IDENTITY or UUID (not SERIAL)
- [ ] All identifiers in `lowercase_snake_case`
- [ ] No `VARCHAR` where `TEXT` suffices
- [ ] No `TIMESTAMP` where `TIMESTAMPTZ` needed
- [ ] No `FLOAT` for monetary values (use NUMERIC)

### Index Strategy
- [ ] Composite indexes for multi-column queries
- [ ] Index column order matches query selectivity
- [ ] Covering indexes with INCLUDE for hot queries
- [ ] Partial indexes for subset queries
- [ ] GIN indexes for JSONB columns with containment queries
- [ ] BRIN indexes for time-series/append-only tables

### Bulk Operations
- [ ] Bulk inserts use multi-row VALUES
- [ ] Large imports use COPY
- [ ] Upserts use ON CONFLICT (not SELECT-then-INSERT)

### Locking
- [ ] Advisory locks for exclusive operations
- [ ] No API calls inside transactions
- [ ] Lock ordering consistent (alphabetical/by ID)

---

## PHASE 3: MEDIUM-HIGH

### Data Access Patterns
- [ ] N+1 queries eliminated (use JOINs or Supabase relationships)
- [ ] Cursor/keyset pagination (not OFFSET for large tables)
- [ ] Row-level locks use NOWAIT or SKIP LOCKED where appropriate

### Index Optimization
- [ ] Expression indexes for function-based queries
- [ ] No unused indexes (check `pg_stat_user_indexes`)

### Complex Queries
- [ ] Materialized views for expensive aggregations
- [ ] Materialized views have refresh strategy

---

## PHASE 4: MEDIUM

### Transaction Best Practices
- [ ] Transactions are short (no external calls inside)
- [ ] Proper error handling with SAVEPOINT
- [ ] Appropriate isolation level selected

### RLS Performance
- [ ] `auth.uid()` wrapped in SELECT for caching
- [ ] Complex policies use SECURITY DEFINER functions
- [ ] Policy columns indexed

### Advanced Indexing
- [ ] JSONB queries use GIN or expression indexes
- [ ] Large tables (>100M rows) partitioned
- [ ] Partition pruning verified in EXPLAIN

---

## PHASE 5: MONITORING & SECURITY

### Query Analysis
- [ ] `pg_stat_statements` extension enabled
- [ ] Top slow queries identified and optimized
- [ ] EXPLAIN ANALYZE used for problematic queries

### Maintenance
- [ ] VACUUM running (autovacuum enabled)
- [ ] ANALYZE statistics current
- [ ] Dead tuple count acceptable
- [ ] Per-table autovacuum thresholds tuned for large tables

### Splinter Security Checks (Supabase Advisor)
- [ ] `auth_users_exposed`: Auth table NOT accessible via API
- [ ] `rls_disabled_in_public`: No tables without RLS
- [ ] `unindexed_foreign_keys`: All FKs indexed
- [ ] `unused_index`: No indexes consuming resources unnecessarily

### API Keys Migration (2025-2026)
- [ ] Aware of `anon`/`service_role` deprecation (end of 2026)
- [ ] Plan to migrate to `sb_publishable_*` / `sb_secret_*` keys
- [ ] No hardcoded legacy JWT keys in codebase

### Audit Trail
- [ ] Audit solution chosen (pgaudit / supa_audit / custom triggers)
- [ ] Sensitive tables identified (user data, financial, credentials)
- [ ] Audit logging enabled for sensitive tables
- [ ] Log retention policy defined

---

## EVIDENCE COLLECTION

Run these queries and record results:

### Connection Check
```sql
SELECT COUNT(*), state FROM pg_stat_activity GROUP BY state;
SHOW max_connections;
SHOW idle_in_transaction_session_timeout;
```
**Result:** _____ active / _____ max_connections

### FK Index Check
```sql
SELECT c.conrelid::regclass AS table_name, a.attname AS column_name
FROM pg_constraint c
JOIN pg_attribute a ON a.attrelid = c.conrelid AND a.attnum = ANY(c.conkey)
WHERE c.contype = 'f'
AND NOT EXISTS (
  SELECT 1 FROM pg_index i
  WHERE i.indrelid = c.conrelid
  AND a.attnum = ANY(i.indkey)
);
```
**Result:** _____ FKs without indexes

### RLS Coverage Check
```sql
SELECT
  (SELECT COUNT(*) FROM pg_tables WHERE schemaname='public' AND rowsecurity=false) AS no_rls,
  (SELECT COUNT(*) FROM pg_tables t
   WHERE t.schemaname='public' AND t.rowsecurity=true
   AND NOT EXISTS (SELECT 1 FROM pg_policies p WHERE p.tablename=t.tablename)) AS rls_no_policy;
```
**Result:** _____ tables without RLS, _____ tables with RLS but no policies

### Slow Queries Check
```sql
SELECT round(mean_exec_time::numeric, 2) AS mean_ms, calls, query
FROM pg_stat_statements
WHERE mean_exec_time > 100
ORDER BY mean_exec_time DESC LIMIT 10;
```
**Result:** _____ slow queries identified

### Vacuum Status Check
```sql
SELECT relname, n_dead_tup, last_autovacuum
FROM pg_stat_user_tables
WHERE n_dead_tup > 10000
ORDER BY n_dead_tup DESC;
```
**Result:** _____ tables need vacuum attention

---

## SCORING

| Phase | Total Checks | Passed | Score |
|-------|--------------|--------|-------|
| 1. CRITICAL | 12 | __ | __% |
| 2. HIGH | 18 | __ | __% |
| 3. MEDIUM-HIGH | 6 | __ | __% |
| 4. MEDIUM | 9 | __ | __% |
| 5. MONITORING | 7 | __ | __% |
| **TOTAL** | **52** | **__** | **__%** |

*Note: 52 checks map to 30 Supabase Agent Skills rules (some rules have multiple validation points)*

### Compliance Level

| Score | Level | Action |
|-------|-------|--------|
| 90-100% | Excellent | Maintain |
| 75-89% | Good | Address HIGH issues |
| 50-74% | Needs Work | Address CRITICAL + HIGH |
| <50% | Critical | Stop and remediate |

---

## CRITICAL STOPS

**DO NOT DEPLOY IF:**
- [ ] Any CRITICAL check failed
- [ ] Tables without RLS hold user data
- [ ] FKs without indexes on tables >10k rows
- [ ] Connection pool not configured

---

## REMEDIATION PRIORITY

1. **Immediate (This Sprint)**
   - Connection pooling
   - RLS on all user tables
   - FK indexes

2. **Short-term (Next Sprint)**
   - Data type corrections
   - Composite indexes
   - N+1 query elimination

3. **Medium-term (Backlog)**
   - Partitioning large tables
   - Materialized views
   - Monitoring setup

---

## SIGN-OFF

| Role | Name | Date | Passed |
|------|------|------|--------|
| DBA | | | [ ] |
| Tech Lead | | | [ ] |
| Security | | | [ ] |

**Final Score:** __/52 checks passed (__%)

**Rules Compliance:** __/30 Supabase Agent Skills rules

**Next Audit Date:** ________________

---

**Version History:**
- v1.0 (2026-01): Initial checklist based on Supabase Agent Skills


## Referência: references/squad/config.yaml

```yaml
name: db-sage
version: "1.2.0"
entry_agent: db-sage
slashPrefix: db-sage
title: "Database Architect & Operations Engineer"
description: "Expert database agent for PostgreSQL and Supabase - schema design, migrations, RLS policies, performance tuning"
author: "AIOX Team"
icon: "🗄️"
type: specialist

# Canonical manifest for db-sage runtime inventory.

# IMPORTANT: External Dependencies
dependencies:
  required:
    - name: PostgreSQL
      version: ">=13.0"
      description: "Database server"
      install: "https://www.postgresql.org/download/"
    - name: Supabase CLI
      version: ">=1.0"
      description: "For Supabase projects (optional if using raw PostgreSQL)"
      install: "npm install -g supabase"
  optional:
    - name: psql
      description: "PostgreSQL command-line client"
    - name: pg_dump
      description: "Database backup utility"

metadata:
  version: "1.2.0"
  score: 8.5

workspace_integration:
  level: none
  rationale: >-
    Db Sage depende de código, banco e infraestrutura, não de artefatos
    canônicos de negócio/produto em `workspace/`.

# Environment variables
environment:
  connection_requirement: >-
    Set at least one connection string before activation: SUPABASE_DB_URL or
    DATABASE_URL. DB Sage accepts either and resolves them in priority order at
    runtime.
  required:
    - name: SUPABASE_DB_URL
      description: "Primary Supabase/PostgreSQL connection string when using the hosted runtime"
      example: "postgresql://postgres:pass@db.xxx.supabase.co:5432/postgres"
  optional:
    - name: DATABASE_URL
      description: "Alternative PostgreSQL connection string for local or remote deployments"
      example: "postgresql://user:pass@host:5432/dbname"
    - name: SUPABASE_PROJECT_REF
      description: "Supabase project reference ID"

agents:
  - db-sage

tasks:
  - db-analyze-hotpaths
  - db-apply-migration
  - db-best-practices-audit
  - db-bootstrap
  - db-dry-run
  - db-env-check
  - db-squad-integration
  - db-explain
  - db-impersonate
  - db-load-csv
  - db-policy-apply
  - db-rls-audit
  - db-rollback
  - db-run-sql
  - db-seed
  - db-smoke-test
  - db-snapshot
  - db-verify-order
  - domain-modeling
  - create-doc
  - execute-checklist
  - kiss
  - query-optimization
  - schema-audit
  - supabase-setup

templates:
  - db-analysis-template
  - index-strategy-tmpl
  - migration-plan-tmpl
  - rls-policies-tmpl
  - schema-design-tmpl
  - migration.sql.tmpl
  - rollback.sql.tmpl
  - backup-metadata.json.tmpl

checklists:
  - database-design-checklist
  - database-migration-documentation-checklist
  - db-kiss-validation-checklist
  - dba-predeploy-checklist
  - dba-rollback-checklist
  - migration-validation-checklist
  - supabase-best-practices-audit

workflows:
  - analyze-data-workflow
  - backup-restore-workflow
  - kiss-gate-workflow
  - modify-schema-workflow
  - performance-tuning-workflow
  - query-database-workflow
  - setup-database-workflow

tags:
  - database
  - postgresql
  - supabase
  - migrations
  - rls
  - security
  - dba

independence: false
independence_reason: "Requires PostgreSQL database and optionally Supabase"
```


## Referência: references/squad/data/database-best-practices.md

# Database Best Practices

## Schema Design
- UUID primary keys (gen_random_uuid())
- TIMESTAMPTZ for all timestamps
- JSONB for flexible data
- Soft deletes (deleted_at)
- created_at, updated_at on all tables
- TEXT over VARCHAR
- NUMERIC for money values

## Indexes
- Index ALL foreign keys
- Partial indexes (WHERE clause)
- CONCURRENTLY for zero-downtime
- GIN for JSONB/arrays/full-text
- Remove unused indexes (pg_stat_user_indexes)

## Security
- RLS enabled on ALL user tables
- Auth.uid() wrapped in SELECT (99.99% faster)
- app_metadata NOT user_metadata
- Granular policies per operation
- Never hardcode credentials

## Performance
- shared_buffers = 25% RAM
- effective_cache_size = 75% RAM
- Connection pooling (PgBouncer)
- ANALYZE after bulk operations
- Monitor with pg_stat_statements

## Backups
- Automated daily backups
- PITR enabled (WAL archiving)
- Test restores monthly
- Store offsite
- 30+ days retention

**References:**
- https://wiki.postgresql.org/wiki/Performance_Optimization
- https://www.postgresql.org/docs/current/ddl-constraints.html


## Referência: references/squad/data/migration-safety-guide.md

# Migration Safety Guide

## Before Migration
1. Take snapshot/backup
2. Test in staging
3. Run dry-run
4. Prepare rollback plan
5. Schedule maintenance window

## During Migration
1. Use transactions (BEGIN/COMMIT)
2. Create indexes CONCURRENTLY
3. Add constraints NOT VALID first
4. Validate constraints separately
5. Monitor logs

## Zero-Downtime Patterns

### Add Column (Safe)
```sql
ALTER TABLE t ADD COLUMN new_col TEXT DEFAULT 'default';
```

### Drop Column (Risky)
```sql
-- Step 1: Stop using column in app
-- Step 2: Deploy app
-- Step 3: Drop column
ALTER TABLE t DROP COLUMN old_col;
```

### Rename Column (Expand/Contract)
```sql
-- Step 1: Add new column
ALTER TABLE t ADD COLUMN new_name TEXT;
-- Step 2: Backfill data
UPDATE t SET new_name = old_name;
-- Step 3: Deploy app using both
-- Step 4: Deploy app using new_name only
-- Step 5: Drop old column
ALTER TABLE t DROP COLUMN old_name;
```

### Add Index (Use CONCURRENTLY)
```sql
CREATE INDEX CONCURRENTLY idx_name ON table(column);
```

### Add Constraint (NOT VALID first)
```sql
-- Step 1: Add NOT VALID (no scan)
ALTER TABLE t ADD CONSTRAINT c CHECK (condition) NOT VALID;
-- Step 2: Validate later (can cancel if takes too long)
ALTER TABLE t VALIDATE CONSTRAINT c;
```

## Rollback Strategies
1. **Roll Forward** (Preferred): New migration to undo
2. **PITR**: Restore to before migration
3. **Manual**: Run rollback script (emergency only)

**References:**
- https://www.postgresql.org/docs/current/sql-altertable.html
- https://medium.com/@jonathangfischoff/what-should-a-postgresql-migrator-do-47fd34804be


## Referência: references/squad/data/postgres-tuning-guide.md

# PostgreSQL Tuning Guide

## Memory
```
shared_buffers = 25% of RAM
effective_cache_size = 75% of RAM
work_mem = RAM / max_connections / 16
maintenance_work_mem = RAM / 16
```

## Connections
```
max_connections = (RAM - shared_buffers) / 10MB
Use PgBouncer for connection pooling
```

## Query Performance
```
statement_timeout = 30s
lock_timeout = 10s
idle_in_transaction_session_timeout = 60s
```

## Monitoring
```
auto_explain.log_min_duration = 1000
log_statement = 'ddl'
log_min_duration_statement = 1000
```

## Vacuum
```
autovacuum = on
autovacuum_max_workers = 4
```

**References:**
- https://pgtune.leopard.in.ua/
- https://www.postgresql.org/docs/current/runtime-config.html


## Referência: references/squad/data/rls-security-patterns.md

# RLS Security Patterns

## User-Owned Data
```sql
(SELECT auth.uid()) = user_id
```

## Team Access
```sql
team_id IN (SELECT team_id FROM team_members WHERE user_id = (SELECT auth.uid()))
```

## Role-Based
```sql
(auth.jwt() -> 'app_metadata' ->> 'role') = 'admin'
```

## Public Read, Auth Write
```sql
-- SELECT: TO anon, authenticated USING (true)
-- INSERT: TO authenticated WITH CHECK (auth.uid() = user_id)
```

## Time-Based
```sql
published_at IS NOT NULL AND published_at <= now()
```

## Hierarchical
```sql
EXISTS (SELECT 1 FROM parent WHERE id = table.parent_id AND user_id = auth.uid())
```

## Security Definer (Fast)
```sql
CREATE FUNCTION user_has_access(uuid) RETURNS boolean SECURITY DEFINER
```

**Common Pitfalls:**
- ❌ Not wrapping auth.uid() → slow
- ❌ Using user_metadata → insecure
- ❌ Missing indexes → full scan
- ❌ No NULL check → fails for anon

**References:**
- https://supabase.com/docs/guides/database/postgres/row-level-security


## Referência: references/squad/data/supabase-agent-skills.md

# Supabase Agent Skills - Knowledge Base

**Source:** [supabase-community/supabase-agent-skills](https://github.com/supabase-community/supabase-agent-skills)
**Version:** 1.0 (January 2026)
**Purpose:** 30 essential database rules for Supabase optimization

---

## Priority Levels

| Priority | Count | Impact |
|----------|-------|--------|
| CRITICAL | 4 | Production-breaking if ignored |
| HIGH | 8 | Major performance/security issues |
| MEDIUM-HIGH | 6 | Significant optimization opportunities |
| MEDIUM | 9 | Best practices for maintainability |
| LOW-MEDIUM | 3 | Monitoring and observability |

---

## CRITICAL PRIORITY (Must Fix Immediately)

### 1. conn-pooling - Connection Pooling Configuration

**Problem:** Direct database connections exhaust `max_connections` quickly.

**Impact:** Database refuses new connections, application downtime.

```sql
-- ❌ WRONG: Direct connection without pooling
postgres://user:pass@db.xxx.supabase.co:5432/postgres

-- ✅ CORRECT: Use Supavisor/PgBouncer (port 6543)
postgres://user:pass@db.xxx.supabase.co:6543/postgres?pgbouncer=true
```

**Supavisor Port Selection (2025+):**
| Scenario | Port | Mode |
|----------|------|------|
| Edge Functions, Serverless | 6543 | Transaction |
| Persistent servers (EC2, VMs) | 5432 | Direct |
| Migrations | 5432 | Direct |
| Prepared statements | 5432 | Session |

**Pool Sizing Rules:**
- With PostgREST active: ≤40% of max_connections
- Without PostgREST: up to 80%
- Always reserve 20% for Auth, Realtime, internal services

---

### 2. conn-limits - Connection Limits Management

**Problem:** Exhausting max_connections causes connection refused errors.

**Impact:** Application cannot connect, cascading failures.

```sql
-- Check current connections
SELECT COUNT(*), state, usename
FROM pg_stat_activity
GROUP BY state, usename
ORDER BY count DESC;

-- Check max connections
SHOW max_connections;

-- ✅ CORRECT: Set appropriate timeouts
SET idle_in_transaction_session_timeout = '60s';
SET statement_timeout = '30s';
```

**Rule:** Active connections should never exceed 80% of max_connections.

---

### 3. query-missing-indexes - Critical Missing Indexes

**Problem:** Queries on large tables without indexes cause full table scans.

**Impact:** 10-1000x slower queries, database CPU spike.

```sql
-- ❌ WRONG: FK without index
CREATE TABLE orders (
  id BIGINT PRIMARY KEY,
  user_id UUID REFERENCES users(id) -- No index!
);

-- ✅ CORRECT: Always index foreign keys
CREATE TABLE orders (
  id BIGINT PRIMARY KEY,
  user_id UUID REFERENCES users(id)
);
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

**Detection Query:**
```sql
-- Find FKs without indexes
SELECT
    c.conrelid::regclass AS table_name,
    a.attname AS column_name,
    c.confrelid::regclass AS referenced_table
FROM pg_constraint c
JOIN pg_attribute a ON a.attrelid = c.conrelid AND a.attnum = ANY(c.conkey)
WHERE c.contype = 'f'
AND NOT EXISTS (
    SELECT 1 FROM pg_index i
    WHERE i.indrelid = c.conrelid
    AND a.attnum = ANY(i.indkey)
);
```

---

### 4. security-rls-basics - Row Level Security Fundamentals

**Problem:** Tables without RLS expose data to all authenticated users.

**Impact:** Data breach, GDPR violations, security incident.

```sql
-- ❌ WRONG: No RLS
CREATE TABLE user_data (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES auth.users(id),
  data JSONB
);
-- Anyone can SELECT * FROM user_data!

-- ✅ CORRECT: Enable RLS with policies
ALTER TABLE user_data ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_data FORCE ROW LEVEL SECURITY;

CREATE POLICY "Users own their data"
ON user_data FOR ALL
TO authenticated
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);
```

**Detection Query:**
```sql
-- Find tables without RLS
SELECT tablename
FROM pg_tables
WHERE schemaname = 'public'
AND rowsecurity = false;
```

---

## HIGH PRIORITY

### 5. schema-foreign-key-indexes - FK Index Strategy

**Problem:** JOINs and ON DELETE CASCADE without FK indexes.

**Impact:** Exponentially slower deletes, blocking operations.

```sql
-- ✅ CORRECT: Index pattern for FKs
-- For every: REFERENCES other_table(id)
-- Create: INDEX idx_table_column ON table(column);

-- Generate CREATE INDEX statements for missing FK indexes
SELECT format(
    'CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_%s_%s ON %s(%I);',
    replace(c.conrelid::regclass::text, '.', '_'),
    a.attname,
    c.conrelid::regclass,
    a.attname
) AS create_index_sql
FROM pg_constraint c
JOIN pg_attribute a ON a.attrelid = c.conrelid
                   AND a.attnum = ANY(c.conkey)
WHERE c.contype = 'f'
AND NOT EXISTS (
    SELECT 1 FROM pg_index i
    WHERE i.indrelid = c.conrelid
    AND a.attnum = ANY(i.indkey)
);
-- Copy output and run each statement separately (CONCURRENTLY cannot be in DO block)
```

---

### 6. query-composite-indexes - Multi-Column Index Design

**Problem:** Single-column indexes don't optimize multi-column WHERE clauses.

**Impact:** Query uses only partial index, still scans more data than needed.

```sql
-- ❌ WRONG: Separate indexes for multi-column query
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_date ON orders(created_at);
-- Query: WHERE status = 'pending' AND created_at > '2025-01-01'

-- ✅ CORRECT: Composite index (most selective first)
CREATE INDEX idx_orders_status_date ON orders(status, created_at);
```

**Rule:** Order columns by selectivity (most selective → least selective).

---

### 7. schema-data-types - Correct Data Type Selection

**Problem:** Wrong data types cause storage bloat and comparison issues.

**Impact:** 2-10x storage overhead, timezone bugs, precision errors.

```sql
-- ❌ WRONG choices
id SERIAL,                      -- Use BIGINT or UUID
created_at TIMESTAMP,           -- Loses timezone
price FLOAT,                    -- Precision errors
status VARCHAR(20),             -- Unnecessary limit
description VARCHAR(10000),     -- Use TEXT

-- ✅ CORRECT choices
id BIGINT GENERATED ALWAYS AS IDENTITY,  -- Or UUID
created_at TIMESTAMPTZ DEFAULT now(),
price NUMERIC(10,2),
status TEXT CHECK (status IN ('draft', 'active', 'archived')),
description TEXT
```

---

### 8. schema-primary-keys - Primary Key Strategy

**Problem:** Auto-increment SERIAL reveals data patterns, has replication issues.

**Impact:** Security risk (enumerable IDs), distributed DB conflicts.

```sql
-- ❌ WRONG: SERIAL in 2025
id SERIAL PRIMARY KEY,  -- Reveals insertion order, conflict in multi-region

-- ✅ CORRECT: IDENTITY or UUID v7
-- Option 1: IDENTITY (PostgreSQL 10+)
id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

-- Option 2: UUID v7 (time-sortable, better for indexes)
id UUID DEFAULT gen_random_uuid() PRIMARY KEY,

-- Option 3: UUID v7 (PostgreSQL 18+, September 2025)
-- Native support - time-sortable, better B-tree performance
id UUID DEFAULT uuidv7() PRIMARY KEY

-- For PostgreSQL <18, use extension:
-- CREATE EXTENSION IF NOT EXISTS pg_uuidv7;
-- id UUID DEFAULT uuid_generate_v7() PRIMARY KEY
```

---

### 9. schema-naming - Consistent Naming Convention

**Problem:** Mixed naming conventions cause confusion and SQL errors.

**Impact:** Developer confusion, case-sensitivity issues.

```sql
-- ❌ WRONG: Mixed conventions
CREATE TABLE UserProfiles (    -- PascalCase
  userId UUID,                 -- camelCase
  "First Name" TEXT,           -- Spaces (requires quotes)
  CREATED_AT TIMESTAMP         -- UPPERCASE
);

-- ✅ CORRECT: snake_case everywhere
CREATE TABLE user_profiles (
  user_id UUID,
  first_name TEXT,
  created_at TIMESTAMPTZ
);
```

**Rule:** All identifiers in `lowercase_snake_case`.

---

### 10. data-bulk-operations - Efficient Bulk Operations

**Problem:** Row-by-row inserts/updates are 100-1000x slower than bulk.

**Impact:** Slow imports, high WAL generation, lock contention.

```sql
-- ❌ WRONG: Row-by-row insert
INSERT INTO users (name) VALUES ('Alice');
INSERT INTO users (name) VALUES ('Bob');
INSERT INTO users (name) VALUES ('Charlie');

-- ✅ CORRECT: Bulk insert
INSERT INTO users (name) VALUES
  ('Alice'),
  ('Bob'),
  ('Charlie');

-- ✅ BETTER: Use COPY for large datasets
COPY users (name) FROM '/tmp/users.csv' WITH CSV HEADER;

-- ✅ BEST: Batch with unnest for programmatic inserts
INSERT INTO users (name, email)
SELECT * FROM unnest(
  ARRAY['Alice', 'Bob', 'Charlie'],
  ARRAY['alice@x.com', 'bob@x.com', 'charlie@x.com']
);
```

---

### 11. lock-advisory - Advisory Locks for Coordination

**Problem:** Race conditions in concurrent operations.

**Impact:** Duplicate records, inconsistent state, deadlocks.

```sql
-- ✅ CORRECT: Advisory lock pattern
-- Use for operations that must be exclusive

-- Acquire lock (blocks if held by another session)
SELECT pg_advisory_lock(hashtext('process_daily_report'));

-- Do exclusive work...
UPDATE reports SET status = 'processing' WHERE date = CURRENT_DATE;

-- Release lock
SELECT pg_advisory_unlock(hashtext('process_daily_report'));

-- For try-lock (non-blocking)
SELECT pg_try_advisory_lock(hashtext('unique_operation_name'));
```

---

### 12. data-upsert - Efficient Upsert Pattern

**Problem:** SELECT-then-INSERT/UPDATE pattern has race conditions.

**Impact:** Duplicate key errors, lost updates.

```sql
-- ❌ WRONG: Check-then-insert
IF NOT EXISTS (SELECT 1 FROM users WHERE email = 'x@y.com') THEN
  INSERT INTO users (email) VALUES ('x@y.com');
END IF;

-- ✅ CORRECT: ON CONFLICT (upsert)
INSERT INTO users (email, name, updated_at)
VALUES ('x@y.com', 'New Name', now())
ON CONFLICT (email) DO UPDATE
SET name = EXCLUDED.name,
    updated_at = now();

-- For insert-only (ignore duplicates)
INSERT INTO users (email, name)
VALUES ('x@y.com', 'New Name')
ON CONFLICT (email) DO NOTHING;
```

---

## MEDIUM-HIGH PRIORITY

### 13. data-n-plus-one - N+1 Query Prevention

**Problem:** Fetching parent then looping to fetch children.

**Impact:** N+1 round trips to database, linear slowdown.

```sql
-- ❌ WRONG: N+1 pattern
-- Query 1: SELECT * FROM authors
-- Query 2-N: SELECT * FROM books WHERE author_id = ?

-- ✅ CORRECT: Single query with JOIN
SELECT a.*,
       json_agg(b.*) AS books
FROM authors a
LEFT JOIN books b ON b.author_id = a.id
GROUP BY a.id;

-- ✅ ALTERNATIVE: Use Supabase relationships
-- In Supabase client:
-- supabase.from('authors').select('*, books(*)');
```

---

### 14. lock-deadlock-prevention - Deadlock Prevention

**Problem:** Multiple transactions locking resources in different order.

**Impact:** Transactions abort, user errors, performance degradation.

```sql
-- ❌ WRONG: Random lock order
-- Transaction 1: UPDATE table_a WHERE id=1; UPDATE table_b WHERE id=2;
-- Transaction 2: UPDATE table_b WHERE id=2; UPDATE table_a WHERE id=1;

-- ✅ CORRECT: Consistent lock order (alphabetical/by ID)
-- Always lock in same order: table_a before table_b, lower ID first
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = LEAST(1, 2);
UPDATE accounts SET balance = balance + 100 WHERE id = GREATEST(1, 2);
COMMIT;

-- ✅ BETTER: Use SKIP LOCKED for queues
SELECT * FROM tasks
WHERE status = 'pending'
ORDER BY created_at
LIMIT 1
FOR UPDATE SKIP LOCKED;
```

---

### 15. data-pagination - Efficient Pagination

**Problem:** OFFSET pagination scales poorly with large datasets.

**Impact:** OFFSET 1000000 still reads 1M rows before skipping.

```sql
-- ❌ WRONG: Offset pagination
SELECT * FROM posts
ORDER BY created_at DESC
LIMIT 20 OFFSET 10000;  -- Reads 10020 rows!

-- ✅ CORRECT: Cursor/keyset pagination
SELECT * FROM posts
WHERE created_at < '2025-01-01T00:00:00Z'  -- Cursor from last item
ORDER BY created_at DESC
LIMIT 20;

-- ✅ With composite cursor (when created_at isn't unique)
SELECT * FROM posts
WHERE (created_at, id) < ('2025-01-01T00:00:00Z', 'abc-123')
ORDER BY created_at DESC, id DESC
LIMIT 20;
```

---

### 16. lock-row-level - Row-Level Locking

**Problem:** Holding locks too long or locking more than necessary.

**Impact:** Blocked queries, timeouts, deadlocks.

```sql
-- ❌ WRONG: Lock for entire transaction
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- ... slow API call ...
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- ✅ CORRECT: Lock only when needed
BEGIN;
-- Do API call first, get data
-- Then quick lock + update
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;  -- Fail fast
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- ✅ For read-heavy with occasional writes: FOR SHARE
SELECT * FROM products WHERE id = 1 FOR SHARE;  -- Allows concurrent reads
```

---

### 17. query-covering-indexes - Covering Indexes

**Problem:** Index lookup still requires table access for additional columns.

**Impact:** Extra I/O for every matching row.

```sql
-- ❌ WRONG: Index doesn't cover SELECT columns
CREATE INDEX idx_orders_user ON orders(user_id);
SELECT user_id, total, created_at FROM orders WHERE user_id = 'abc';
-- Index finds rows, then reads table for total, created_at

-- ✅ CORRECT: Covering index with INCLUDE
CREATE INDEX idx_orders_user_covering
ON orders(user_id)
INCLUDE (total, created_at);
-- Index-only scan, no table access needed
```

---

### 18. advanced-partial-indexes - Partial Indexes

**Problem:** Full index when only subset of data is queried.

**Impact:** Larger index, slower updates, more storage.

```sql
-- ❌ WRONG: Full index for status queries
CREATE INDEX idx_orders_status ON orders(status);
-- But 90% of orders are 'completed', rarely queried

-- ✅ CORRECT: Partial index for active records only
CREATE INDEX idx_orders_active
ON orders(status, created_at)
WHERE status IN ('pending', 'processing');

-- Query must include the WHERE condition
SELECT * FROM orders
WHERE status = 'pending'  -- Uses partial index
AND created_at > '2025-01-01';
```

---

## MEDIUM PRIORITY

### 19. data-batch-inserts - Batch Insert Optimization

**Problem:** Many small transactions instead of batched operations.

**Impact:** High WAL write, fsync overhead, slow performance.

```sql
-- ❌ WRONG: Individual transactions
BEGIN; INSERT INTO logs VALUES (...); COMMIT;
BEGIN; INSERT INTO logs VALUES (...); COMMIT;
-- N transactions = N fsyncs

-- ✅ CORRECT: Batch in single transaction
BEGIN;
INSERT INTO logs VALUES
  (...),
  (...),
  (...);
COMMIT;
-- 1 transaction = 1 fsync

-- ✅ BETTER: Use COPY for bulk
COPY logs FROM STDIN WITH (FORMAT csv);
```

**Rule:** Batch size 100-1000 rows optimal.

---

### 20. security-rls-performance - RLS Performance Optimization

**Problem:** Complex RLS policies executed for every row.

**Impact:** 10-100x slower queries with poorly written policies.

```sql
-- ❌ WRONG: Subquery in every row evaluation
CREATE POLICY "team_access" ON documents
USING (team_id IN (
  SELECT team_id FROM team_members
  WHERE user_id = auth.uid()  -- Executed per row!
));

-- ✅ CORRECT: Wrap auth functions in SELECT
CREATE POLICY "team_access" ON documents
USING (team_id IN (
  SELECT team_id FROM team_members
  WHERE user_id = (SELECT auth.uid())  -- Cached!
));

-- ✅ BETTER: Use security definer function
CREATE OR REPLACE FUNCTION get_user_teams()
RETURNS SETOF UUID
LANGUAGE sql
SECURITY DEFINER
STABLE
AS $$
  SELECT team_id FROM team_members WHERE user_id = auth.uid();
$$;

CREATE POLICY "team_access" ON documents
USING (team_id IN (SELECT * FROM get_user_teams()));
```

---

### 21. advanced-jsonb-indexing - JSONB Index Strategies

**Problem:** JSONB queries without appropriate indexes.

**Impact:** Full table scan for JSON property lookups.

```sql
-- ❌ WRONG: No index for JSONB query
SELECT * FROM events WHERE data->>'type' = 'purchase';

-- ✅ CORRECT: GIN index for containment
CREATE INDEX idx_events_data ON events USING GIN (data);
-- Query with containment operator
SELECT * FROM events WHERE data @> '{"type": "purchase"}';

-- ✅ ALTERNATIVE: Expression index for specific paths
CREATE INDEX idx_events_type ON events ((data->>'type'));
-- Query normally
SELECT * FROM events WHERE data->>'type' = 'purchase';

-- ✅ For jsonb_path queries
CREATE INDEX idx_events_path ON events
USING GIN (data jsonb_path_ops);
```

---

### 22. advanced-brin-indexes - BRIN Indexes for Time-Series

**Problem:** B-tree indexes too large for append-only time-series data.

**Impact:** Large index storage, slower updates.

```sql
-- ❌ WRONG: B-tree on time-series
CREATE INDEX idx_logs_created ON logs(created_at);
-- Large index for billions of rows

-- ✅ CORRECT: BRIN for naturally ordered data
CREATE INDEX idx_logs_created_brin
ON logs USING BRIN (created_at)
WITH (pages_per_range = 128);

-- BRIN is 100-1000x smaller
-- Works because new rows have larger created_at values
-- Best for: logs, events, time-series data
```

**Rule:** Use BRIN when data is inserted in approximately sorted order.

---

### 22.5. advanced-hnsw-indexes - Vector Search Indexes (pgvector)

**Problem:** AI/ML applications need efficient similarity search on embeddings.

**Impact:** Without proper indexing, vector searches scan entire tables.

```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create table with vector column
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT uuidv7(),
  content TEXT,
  embedding vector(1536)  -- OpenAI ada-002 dimension
);

-- ✅ HNSW index for approximate nearest neighbor search
CREATE INDEX idx_documents_embedding ON documents
USING hnsw (embedding vector_cosine_ops);

-- Query with similarity search
SELECT id, content, embedding <=> '[0.1, 0.2, ...]'::vector AS distance
FROM documents
ORDER BY embedding <=> '[0.1, 0.2, ...]'::vector
LIMIT 10;
```

**Index types for pgvector:**
| Type | Best For | Trade-off |
|------|----------|-----------|
| `hnsw` | <1M vectors | Faster queries, more memory |
| `ivfflat` | >1M vectors | Less memory, needs training |

**Distance operators:**
- `<=>`: Cosine distance (normalized vectors)
- `<->`: L2/Euclidean distance
- `<#>`: Inner product (negative)

---

### 23. advanced-expression-indexes - Expression/Functional Indexes

**Problem:** Functions in WHERE clause prevent index usage.

**Impact:** Full table scan even with index on base column.

```sql
-- ❌ WRONG: Function prevents index use
CREATE INDEX idx_users_email ON users(email);
SELECT * FROM users WHERE lower(email) = 'user@example.com';
-- Index not used!

-- ✅ CORRECT: Expression index
CREATE INDEX idx_users_email_lower ON users(lower(email));
SELECT * FROM users WHERE lower(email) = 'user@example.com';
-- Index used!

-- Common patterns:
CREATE INDEX idx_date_trunc ON events (date_trunc('day', created_at));
CREATE INDEX idx_jsonb_field ON data ((payload->>'type'));
```

---

### 24. advanced-table-partitioning - Table Partitioning

**Problem:** Large tables (>100M rows) slow for all operations.

**Impact:** Slow queries, vacuum takes hours, backup issues.

```sql
-- ✅ CORRECT: Range partitioning for time-series
CREATE TABLE logs (
  id BIGINT GENERATED ALWAYS AS IDENTITY,
  created_at TIMESTAMPTZ NOT NULL,
  data JSONB
) PARTITION BY RANGE (created_at);

-- Create partitions
CREATE TABLE logs_2025_01 PARTITION OF logs
FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE logs_2025_02 PARTITION OF logs
FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');

-- Automate with pg_partman extension
CREATE EXTENSION pg_partman;
SELECT partman.create_parent('public.logs', 'created_at', 'native', 'monthly');
```

---

### 25. advanced-materialized-views - Materialized Views

**Problem:** Complex aggregations computed on every query.

**Impact:** Slow dashboard queries, repeated expensive calculations.

```sql
-- ❌ WRONG: Calculate on every request
SELECT
  date_trunc('day', created_at) AS day,
  COUNT(*) AS orders,
  SUM(total) AS revenue
FROM orders
GROUP BY 1;

-- ✅ CORRECT: Materialized view
CREATE MATERIALIZED VIEW daily_stats AS
SELECT
  date_trunc('day', created_at) AS day,
  COUNT(*) AS orders,
  SUM(total) AS revenue
FROM orders
GROUP BY 1;

-- Create index on materialized view
CREATE UNIQUE INDEX idx_daily_stats_day ON daily_stats(day);

-- Refresh periodically (via cron or pg_cron)
REFRESH MATERIALIZED VIEW CONCURRENTLY daily_stats;
```

---

### 26. data-transactions - Transaction Best Practices

**Problem:** Long transactions, no error handling, inconsistent isolation.

**Impact:** Lock contention, data inconsistency, deadlocks.

```sql
-- ❌ WRONG: Long transaction
BEGIN;
SELECT * FROM accounts WHERE id = 1;
-- ... wait for API response ...
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- ✅ CORRECT: Short transactions
-- Get data first
SELECT * FROM accounts WHERE id = 1;

-- Make API call outside transaction

-- Quick transaction for update
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- ✅ With proper error handling
BEGIN;
  SAVEPOINT before_update;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  -- If error: ROLLBACK TO before_update;
COMMIT;
```

---

### 27. advanced-query-optimization - Query Optimization Techniques

**Problem:** Inefficient queries with unnecessary operations.

**Impact:** Wasted resources, slow responses.

```sql
-- ❌ WRONG: SELECT * when only need few columns
SELECT * FROM orders WHERE user_id = 'abc';

-- ✅ CORRECT: Select only needed columns
SELECT id, total, status FROM orders WHERE user_id = 'abc';

-- ❌ WRONG: Inefficient EXISTS alternative
SELECT * FROM users u
WHERE (SELECT COUNT(*) FROM orders WHERE user_id = u.id) > 0;

-- ✅ CORRECT: Use EXISTS
SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM orders WHERE user_id = u.id);

-- ✅ Use EXPLAIN ANALYZE to verify
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE user_id = 'abc';
```

---

## LOW-MEDIUM PRIORITY (Monitoring)

### 28. monitor-explain-analyze - EXPLAIN ANALYZE Usage

**Problem:** Not understanding query execution plans.

**Impact:** Unable to diagnose slow queries.

```sql
-- ✅ CORRECT: Full analysis
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE user_id = 'abc-123';

-- Key metrics to check:
-- - Seq Scan on large tables (needs index)
-- - Nested Loop with many rows (needs optimization)
-- - High "actual time" vs low "rows" (inefficient)
-- - Buffer reads much higher than expected

-- ✅ For production (no execution)
EXPLAIN (COSTS, FORMAT TEXT)
SELECT * FROM orders WHERE user_id = 'abc-123';
```

---

### 29. monitor-pg-stat-statements - Query Statistics

**Problem:** No visibility into query patterns and performance.

**Impact:** Slow queries go undetected until users complain.

```sql
-- Enable extension (requires superuser)
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Top queries by total time
SELECT
  round(total_exec_time::numeric, 2) AS total_ms,
  calls,
  round(mean_exec_time::numeric, 2) AS mean_ms,
  query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 20;

-- Top queries by calls
SELECT
  calls,
  round(total_exec_time::numeric, 2) AS total_ms,
  query
FROM pg_stat_statements
ORDER BY calls DESC
LIMIT 20;

-- Reset statistics
SELECT pg_stat_statements_reset();
```

---

### 30. monitor-vacuum-analyze - Vacuum and Analyze

**Problem:** Stale statistics, table bloat, transaction ID wraparound.

**Impact:** Wrong query plans, wasted space, potential database freeze.

```sql
-- Check last vacuum/analyze
SELECT
  schemaname,
  relname,
  last_vacuum,
  last_autovacuum,
  last_analyze,
  last_autoanalyze,
  n_dead_tup
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;

-- Manual ANALYZE after bulk operations
ANALYZE orders;

-- Manual VACUUM for immediate space reclaim
VACUUM (VERBOSE, ANALYZE) orders;

-- Check autovacuum settings
SHOW autovacuum;
SHOW autovacuum_vacuum_threshold;
SHOW autovacuum_analyze_threshold;

-- For large tables, tune per-table
ALTER TABLE logs SET (
  autovacuum_vacuum_threshold = 10000,
  autovacuum_analyze_threshold = 5000
);
```

---

## Quick Reference Queries

### Full Audit Query
```sql
-- Run all checks in one query
WITH checks AS (
  -- Tables without RLS
  SELECT 'no_rls' AS check_type, tablename AS item
  FROM pg_tables WHERE schemaname = 'public' AND rowsecurity = false

  UNION ALL

  -- FKs without indexes (checking each FK column individually)
  SELECT 'fk_no_index', c.conrelid::regclass::text || '.' || a.attname
  FROM pg_constraint c
  JOIN pg_attribute a ON a.attrelid = c.conrelid AND a.attnum = ANY(c.conkey)
  WHERE c.contype = 'f'
  AND NOT EXISTS (
    SELECT 1 FROM pg_index i
    WHERE i.indrelid = c.conrelid
    AND a.attnum = ANY(i.indkey)
  )
)
SELECT check_type, COUNT(*) AS issues, array_agg(item ORDER BY item) AS items
FROM checks
GROUP BY check_type;
```

---

## References

- [Supabase Agent Skills Repository](https://github.com/supabase-community/supabase-agent-skills)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/)
- [Supabase RLS Guide](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [PostgreSQL Performance Wiki](https://wiki.postgresql.org/wiki/Performance_Optimization)


## Referência: references/squad/data/supabase-patterns.md

# Supabase Patterns

## RLS Performance

### auth.uid() Caching (CRITICAL)
```sql
-- ❌ WRONG: auth.uid() called per row
CREATE POLICY "user_data" ON documents
USING (user_id = auth.uid());

-- ✅ CORRECT: Wrap in SELECT for caching (99%+ faster)
CREATE POLICY "user_data" ON documents
USING (user_id = (SELECT auth.uid()));
```

### Complex Policies with Security Definer
```sql
-- ✅ Create helper function (caches auth.uid() internally)
CREATE OR REPLACE FUNCTION get_user_teams()
RETURNS SETOF UUID
LANGUAGE sql
SECURITY DEFINER
STABLE
AS $$
  SELECT team_id FROM team_members WHERE user_id = (SELECT auth.uid());
$$;

-- Use in policy
CREATE POLICY "team_access" ON documents
USING (team_id IN (SELECT * FROM get_user_teams()));
```

### Policy Column Indexing
```sql
-- Always index columns used in RLS policies
CREATE INDEX idx_documents_user_id ON documents(user_id);
CREATE INDEX idx_documents_team_id ON documents(team_id);
```

## Multi-Tenant
```sql
-- ✅ With cached auth.uid()
team_id IN (SELECT team_id FROM members WHERE user_id = (SELECT auth.uid()))
```

## Time-Based Access
```sql
published_at <= now() AND (expires_at IS NULL OR expires_at > now())
```

## Hierarchical
```sql
EXISTS (SELECT 1 FROM parent WHERE parent.id = table.parent_id AND parent.user_id = (SELECT auth.uid()))
```

## Role-Based
```sql
(auth.jwt() -> 'app_metadata' ->> 'role') IN ('admin', 'moderator')
```

---

## JSONB Indexing Patterns

### Containment Queries (GIN)
```sql
-- Create GIN index
CREATE INDEX idx_events_data ON events USING GIN (data);

-- ✅ Query with containment operator
SELECT * FROM events WHERE data @> '{"type": "purchase"}';

-- ❌ NOT optimized by GIN
SELECT * FROM events WHERE data->>'type' = 'purchase';
```

### Expression Index for Specific Paths
```sql
-- For frequent path access
CREATE INDEX idx_events_type ON events ((data->>'type'));

-- Now this is indexed
SELECT * FROM events WHERE data->>'type' = 'purchase';
```

### jsonb_path_ops for Path Queries
```sql
CREATE INDEX idx_events_path ON events USING GIN (data jsonb_path_ops);
-- Smaller index, only supports @> operator
```

---

## Pagination Patterns

### Cursor/Keyset Pagination (RECOMMENDED)
```sql
-- ❌ WRONG: OFFSET pagination (reads all skipped rows)
SELECT * FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 10000;

-- ✅ CORRECT: Cursor pagination
SELECT * FROM posts
WHERE created_at < '2025-01-01T00:00:00Z'  -- Last item's timestamp
ORDER BY created_at DESC
LIMIT 20;

-- ✅ Composite cursor (when created_at not unique)
SELECT * FROM posts
WHERE (created_at, id) < ('2025-01-01T00:00:00Z', 'last-id')
ORDER BY created_at DESC, id DESC
LIMIT 20;
```

### Index for Pagination
```sql
-- Support cursor pagination with composite index
CREATE INDEX idx_posts_cursor ON posts(created_at DESC, id DESC);
```

---

## Connection Patterns

### Use Supavisor/PgBouncer
```
# ❌ Direct connection (exhausts max_connections)
postgres://user:pass@db.xxx.supabase.co:5432/postgres

# ✅ Pooled connection (port 6543)
postgres://user:pass@db.xxx.supabase.co:6543/postgres?pgbouncer=true
```

### Connection Timeouts
```sql
-- Set session timeouts
SET idle_in_transaction_session_timeout = '60s';
SET statement_timeout = '30s';
SET lock_timeout = '10s';
```

---

## Bulk Operation Patterns

### Batch Inserts
```sql
-- ❌ Row-by-row
INSERT INTO logs (data) VALUES ('a');
INSERT INTO logs (data) VALUES ('b');

-- ✅ Multi-value
INSERT INTO logs (data) VALUES ('a'), ('b'), ('c');

-- ✅ With unnest for arrays
INSERT INTO logs (data, type)
SELECT * FROM unnest(
  ARRAY['a', 'b', 'c'],
  ARRAY['info', 'warn', 'error']
);
```

### Upsert Pattern
```sql
-- ✅ Use ON CONFLICT
INSERT INTO users (email, name, updated_at)
VALUES ('x@y.com', 'Name', now())
ON CONFLICT (email) DO UPDATE
SET name = EXCLUDED.name,
    updated_at = now();
```

---

## Index Patterns

### Foreign Key Indexes (CRITICAL)
```sql
-- Every FK MUST have an index
CREATE TABLE orders (
  user_id UUID REFERENCES users(id)
);
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

### Composite Indexes
```sql
-- Order by selectivity (most selective first)
CREATE INDEX idx_orders_status_date ON orders(status, created_at);
```

### Covering Indexes
```sql
-- Include columns to avoid table lookup
CREATE INDEX idx_orders_user_covering ON orders(user_id) INCLUDE (total, status);
```

### Partial Indexes
```sql
-- Index only active records
CREATE INDEX idx_orders_active ON orders(status, created_at)
WHERE status IN ('pending', 'processing');
```

### BRIN for Time-Series
```sql
-- 100-1000x smaller than B-tree for append-only data
CREATE INDEX idx_logs_created_brin ON logs USING BRIN (created_at);
```

---

## Schema Organization (2025+)

### Use `app_` Prefix for Custom Schemas
```sql
-- Don't rely only on public (exposed by default via Data API)
CREATE SCHEMA app_auth;      -- Custom authentication
CREATE SCHEMA app_billing;   -- Payments
CREATE SCHEMA app_content;   -- Main content
CREATE SCHEMA app_admin;     -- Admin functions (not exposed)

-- Grant permissions to Supabase roles
GRANT USAGE ON SCHEMA app_content TO authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA app_content TO authenticated;
```

Expose in **Project Settings → Data API → Exposed schemas**.

---

## Supavisor Connection Pooling (2025+)

### Port Selection Guide
| Scenario | Port | Mode |
|----------|------|------|
| Edge Functions | 6543 | Transaction |
| Serverless (Vercel, Netlify) | 6543 | Transaction |
| Persistent servers (EC2, VMs) | 5432 | Direct |
| Migrations | 5432 | Direct |
| Prepared statements needed | 5432 | Session |

```
# Transaction mode (releases connection after each transaction)
postgres://user:pass@db.xxx.supabase.co:6543/postgres?pgbouncer=true

# Session mode (persistent connection)
postgres://user:pass@db.xxx.supabase.co:5432/postgres
```

### Pool Sizing Rules
- With PostgREST: ≤40% of max_connections
- Without PostgREST: up to 80%
- Always reserve 20% for Auth, Realtime, internal services

---

## Storage RLS Patterns

### Folder-based User Isolation
```sql
-- Structure: bucket/user_id/filename
CREATE POLICY "Users access own files"
ON storage.objects FOR SELECT
USING (
  bucket_id = 'user-documents'
  AND (storage.foldername(name))[1] = (SELECT auth.uid())::text
);

CREATE POLICY "Users upload to own folder"
ON storage.objects FOR INSERT
WITH CHECK (
  bucket_id = 'user-documents'
  AND (storage.foldername(name))[1] = (SELECT auth.uid())::text
);
```

### Bucket Organization
- **Public buckets**: Profile pictures, blog images (truly public assets)
- **Private buckets**: Documents, uploads requiring auth

---

## Realtime Patterns

### Channel Type Selection
| Type | Use Case | Example |
|------|----------|---------|
| **Broadcast** | Ephemeral data | Cursors, typing indicators |
| **Presence** | Online tracking | User status, active users |
| **Postgres Changes** | DB sync | Only when DB sync needed |

### Always Filter Postgres Changes
```typescript
// ❌ WRONG: No filter, receives all changes
supabase.channel('all').on('postgres_changes', { event: '*', ... })

// ✅ CORRECT: Specific event + filter
supabase
  .channel('messages')
  .on('postgres_changes', {
    event: 'INSERT',  // Not '*'
    schema: 'public',
    table: 'messages',
    filter: `room_id=eq.${roomId}`  // Always filter!
  }, handleMessage)
  .subscribe();
```

### Realtime Limits (2025)
| Metric | Free | Pro |
|--------|------|-----|
| Peak connections | 200 | 500 |
| Messages/second | 100 | 100 |
| Max message size | 1 MB | 1 MB |

### Always Cleanup Subscriptions
```typescript
useEffect(() => {
  const channel = supabase.channel('my-channel');
  channel.subscribe();
  return () => supabase.removeChannel(channel);
}, []);
```

---

## Migration Safety Patterns

### Foreign Keys in 2 Steps (No Lock)
```sql
-- Step 1: Add constraint without validation (no lock)
ALTER TABLE appointments
ADD CONSTRAINT fk_patient
FOREIGN KEY (patient_id) REFERENCES patients(id)
NOT VALID;

-- Step 2: Validate separately (allows concurrent reads)
ALTER TABLE appointments
VALIDATE CONSTRAINT fk_patient;
```

### Always Set Timeouts
```sql
SET lock_timeout = '5s';
SET statement_timeout = '30s';
-- Then run migration
```

---

## Audit Trail Options

### Option 1: pgaudit (Available in all Supabase projects)

**Best for:** Compliance logging, security audits, debugging

```sql
-- 1. Install extension
CREATE EXTENSION IF NOT EXISTS pgaudit;

-- 2. Create auditor role for object-level auditing
CREATE ROLE auditor NOLOGIN;

-- 3. Grant auditor to sensitive tables
GRANT SELECT, INSERT, UPDATE, DELETE ON public.user_profiles TO auditor;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.user_roles TO auditor;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.integration_credentials TO auditor;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.payment_providers TO auditor;

-- 4. Configure via Supabase Dashboard:
--    Database → Settings → Custom Postgres Config:
--    pgaudit.role = 'auditor'
--    pgaudit.log = 'write'
```

**pgaudit.log options:**
| Value | What it logs |
|-------|--------------|
| `write` | INSERT, UPDATE, DELETE (recommended) |
| `read` | SELECT queries |
| `ddl` | CREATE, ALTER, DROP |
| `all` | Everything (verbose) |

**View logs:** Supabase Dashboard → Logs → Postgres Logs

### Option 2: supa_audit (If available)

```sql
-- Enable extension
CREATE EXTENSION supa_audit CASCADE;

-- Track specific table
SELECT audit.enable_tracking('public.accounts'::regclass);

-- Query history
SELECT * FROM audit.record_version
WHERE table_name = 'accounts'
ORDER BY ts DESC;
```

### Option 3: Custom Audit Triggers

For full history stored in tables (not just logs):

```sql
-- Create audit schema and table
CREATE SCHEMA IF NOT EXISTS audit;

CREATE TABLE audit.log (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  table_name TEXT NOT NULL,
  operation TEXT NOT NULL,  -- INSERT, UPDATE, DELETE
  old_data JSONB,
  new_data JSONB,
  changed_by UUID DEFAULT (SELECT auth.uid()),
  changed_at TIMESTAMPTZ DEFAULT now()
);

-- Create generic audit trigger function
CREATE OR REPLACE FUNCTION audit.log_changes()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO audit.log (table_name, operation, old_data, new_data)
  VALUES (
    TG_TABLE_NAME,
    TG_OP,
    CASE WHEN TG_OP IN ('UPDATE', 'DELETE') THEN to_jsonb(OLD) END,
    CASE WHEN TG_OP IN ('INSERT', 'UPDATE') THEN to_jsonb(NEW) END
  );
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Apply to sensitive tables
CREATE TRIGGER audit_user_profiles
  AFTER INSERT OR UPDATE OR DELETE ON public.user_profiles
  FOR EACH ROW EXECUTE FUNCTION audit.log_changes();
```

### Which to choose?

| Need | Solution |
|------|----------|
| Compliance logging only | pgaudit |
| Query history in tables | Custom triggers |
| Simple setup (if available) | supa_audit |
| Financial/GDPR audit trail | Custom triggers + pgaudit |

---

## API Keys Transition (2025-2026)

**DEPRECATION WARNING:** `anon` and `service_role` keys deprecated by end of 2026.

| Old Key | New Key | Use |
|---------|---------|-----|
| `anon` (JWT) | `sb_publishable_...` | Client-side |
| `service_role` (JWT) | `sb_secret_...` | Server-side only |

New benefits:
- Independent key rotation
- Auto-protection against browser exposure (HTTP 401)
- Multiple secret keys for different backend components

---

## Splinter Security Checks

Supabase's Splinter advisor automatically checks:
- `auth_users_exposed`: Auth table accessible via API
- `rls_disabled_in_public`: Tables without RLS
- `unindexed_foreign_keys`: FKs without indexes
- `unused_index`: Indexes consuming resources unnecessarily

---

**References:**
- https://supabase.com/docs/guides/troubleshooting/rls-performance-and-best-practices
- https://supabase.com/docs/guides/database/postgres/row-level-security
- https://github.com/supabase-community/supabase-agent-skills
- https://supabase.com/docs/guides/platform/performance (Splinter)
- https://supabase.com/blog/supabase-api-keys (New API Keys)


## Referência: references/squad/tasks/create-doc.md

# Create Document from Template (YAML Driven)

| Field | Value |
|-------|-------|
| **execution_type** | `Agent` |
| **pattern** | EXEC-A-001 |
| **rationale** | Criação de documento requer elicitação interativa e interpretação |

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each section must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Complete documents cannot be created without following this workflow

**VIOLATION INDICATOR:** If you create a complete document without user interaction, you have violated this workflow.

## Critical: Template Discovery

If a YAML Template has not been provided, list all templates from squads/db-sage/templates/ or ask the user to provide another.

## CRITICAL: Mandatory Elicitation Format

**When `elicit: true`, this is a HARD STOP requiring user interaction:**

**YOU MUST:**

1. Present section content
2. Provide detailed rationale (explain trade-offs, assumptions, decisions made)
3. **STOP and present numbered options 1-9:**
   - **Option 1:** Always "Proceed to next section"
   - **Options 2-9:** Select 8 methods from data/elicitation-methods
   - End with: "Select 1-9 or just type your question/feedback:"
4. **WAIT FOR USER RESPONSE** - Do not proceed until user selects option or provides feedback

**WORKFLOW VIOLATION:** Creating content for elicit=true sections without user interaction violates this task.

**NEVER ask yes/no questions or use any other format.**

## Processing Flow

1. **Parse YAML template** - Load template metadata and sections
2. **Set preferences** - Show current mode (Interactive), confirm output file
3. **Process each section:**
   - Skip if condition unmet
   - Check agent permissions (owner/editors) - note if section is restricted to specific agents
   - Draft content using section instruction
   - Present content + detailed rationale
   - **IF elicit: true** → MANDATORY 1-9 options format
   - Save to file if possible
4. **Continue until complete**

## Detailed Rationale Requirements

When presenting section content, ALWAYS include rationale that explains:

- Trade-offs and choices made (what was chosen over alternatives and why)
- Key assumptions made during drafting
- Interesting or questionable decisions that need user attention
- Areas that might need validation

## Elicitation Results Flow

After user selects elicitation method (2-9):

1. Execute method from data/elicitation-methods
2. Present results with insights
3. Offer options:
   - **1. Apply changes and update section**
   - **2. Return to elicitation menu**
   - **3. Ask any questions or engage further with this elicitation**

## Agent Permissions

When processing sections with agent permission fields:

- **owner**: Note which agent role initially creates/populates the section
- **editors**: List agent roles allowed to modify the section
- **readonly**: Mark sections that cannot be modified after creation

**For sections with restricted access:**

- Include a note in the generated document indicating the responsible agent
- Example: "_(This section is owned by dev-agent and can only be modified by dev-agent)_"

## YOLO Mode

User can type `#yolo` to toggle to YOLO mode (process all sections at once).

## CRITICAL REMINDERS

**❌ NEVER:**

- Ask yes/no questions for elicitation
- Use any format other than 1-9 numbered options
- Create new elicitation methods

**✅ ALWAYS:**

- Use exact 1-9 format when elicit: true
- Select options 2-9 from data/elicitation-methods only
- Provide detailed rationale explaining decisions
- End with "Select 1-9 or just type your question/feedback:"


## Referência: references/squad/tasks/db-analyze-hotpaths.md

# Task: Analyze Hot Query Paths

| Field | Value |
|-------|-------|
| **execution_type** | `Hybrid` |
| **pattern** | EXEC-HY-001 |
| **script** | `scripts/db-ops/explain-analyzer.sh` |
| **rationale** | Worker coleta pg_stat_statements, Agent analisa e prioriza |

**Purpose**: Run EXPLAIN ANALYZE on common/critical queries to identify performance issues

**Elicit**: true

---

## 🚀 NEW: Use Automated Query Analyzer (RECOMMENDED)

**Token Savings: 89% | Time Savings: ~85%**

```bash
# Analyze hot paths automatically with performance recommendations
./squads/db-sage/scripts/db-ops/explain-analyzer.sh

# Analyze specific query
./squads/db-sage/scripts/db-ops/explain-analyzer.sh "{sql}"

# With execution statistics and buffer analysis
./squads/db-sage/scripts/db-ops/explain-analyzer.sh "{sql}" --analyze --buffers

# Get JSON output for parsing
./squads/db-sage/scripts/db-ops/explain-analyzer.sh "{sql}" --format json

# Benefits:
#   - Automatic hot path detection from pg_stat_statements
#   - Performance issue identification
#   - Index recommendations
#   - Buffer cache analysis
#   - 89% token savings
```

**OR continue with manual analysis below:**

---

## Inputs

- `queries_file` (optional): Path to file with labeled queries to analyze
- If not provided, analyze common patterns from pg_stat_statements

---

## Process

### 1. Enable Required Extensions

Ensure performance monitoring is available:

```bash
echo "Enabling performance extensions..."

psql "$SUPABASE_DB_URL" << 'EOF'
-- Enable pg_stat_statements (should already be enabled in Supabase)
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Optionally enable index_advisor (Supabase extension)
CREATE EXTENSION IF NOT EXISTS index_advisor;

SELECT 'Extensions ready' AS status;
EOF

echo "✓ Extensions enabled"
```

### 2. Identify Hot Queries

If no queries_file provided, find slowest queries from pg_stat_statements:

```bash
echo "Finding slow queries from pg_stat_statements..."

psql "$SUPABASE_DB_URL" << 'EOF'
SELECT
  query,
  calls,
  ROUND(total_exec_time::numeric, 2) AS total_time_ms,
  ROUND(mean_exec_time::numeric, 2) AS mean_time_ms,
  ROUND(max_exec_time::numeric, 2) AS max_time_ms,
  ROUND((100 * total_exec_time / SUM(total_exec_time) OVER ())::numeric, 2) AS pct_total_time
FROM pg_stat_statements
WHERE query NOT LIKE '%pg_stat_statements%'
  AND query NOT LIKE '%pg_catalog%'
ORDER BY mean_exec_time DESC
LIMIT 20;
EOF
```

Ask user:
```
Top 20 slow queries found.
Select query numbers to analyze (comma-separated, e.g., 1,3,5):
Or type 'all' to analyze all:
```

### 3. Run EXPLAIN ANALYZE with BUFFERS

For each selected query, run comprehensive analysis:

```bash
echo "Analyzing query performance..."

# CRITICAL: Always use ANALYZE, BUFFERS for complete picture
psql "$SUPABASE_DB_URL" << 'EOF'
-- Query being analyzed
\echo '=========================================='
\echo 'QUERY: {query_label}'
\echo '=========================================='

-- Option 1: EXPLAIN ANALYZE with BUFFERS (recommended)
EXPLAIN (
  ANALYZE true,
  BUFFERS true,
  VERBOSE true,
  COSTS true,
  TIMING true
)
{actual_query};

\echo ''
\echo 'BUFFERS LEGEND:'
\echo '  - shared hit = blocks found in buffer cache (good)'
\echo '  - shared read = blocks read from disk (bad if high)'
\echo '  - temp read/written = temporary files (bad if present)'
\echo ''

EOF
```

### 4. Generate Index Recommendations

Use index_advisor extension (Supabase-specific):

```bash
echo "Generating index recommendations..."

psql "$SUPABASE_DB_URL" << 'EOF'
-- Use index_advisor to get suggestions
SELECT *
FROM index_advisor('{actual_query}');

-- Alternative: Supabase Studio has Index Advisor UI
-- Navigate to: Query Performance Report → Select query → "indexes" tab
EOF
```

### 5. Analyze Results

Identify common performance issues:

```bash
echo "Performance Issue Checklist:"
echo ""
echo "🔍 Sequential Scans:"
echo "   - Look for: 'Seq Scan on table_name'"
echo "   - Problem if: Large tables (>1000 rows) + filter removes many rows"
echo "   - Fix: Add index on filter columns"
echo ""
echo "🔍 Row Count Mismatches:"
echo "   - Compare: rows=XXXX (estimated) vs actual rows=YYYY"
echo "   - Problem if: Estimate differs by >10x from actual"
echo "   - Fix: ANALYZE table_name; (update statistics)"
echo ""
echo "🔍 Buffer Cache Misses:"
echo "   - Look for: 'shared read' in BUFFERS output"
echo "   - Problem if: High compared to 'shared hit'"
echo "   - Fix: Increase shared_buffers, optimize query, add indexes"
echo ""
echo "🔍 Temporary Files:"
echo "   - Look for: 'temp read' or 'temp written' in BUFFERS"
echo "   - Problem: Query using disk for sorting/hashing (work_mem too small)"
echo "   - Fix: Increase work_mem, optimize query, add indexes"
echo ""
echo "🔍 Nested Loops:"
echo "   - Look for: 'Nested Loop' with high row counts"
echo "   - Problem if: Loops=10000+ iterations"
echo "   - Fix: Add indexes on join columns, consider Hash Join"
echo ""
```

### 6. Create Analysis Report

Generate markdown report with findings:

```bash
REPORT_FILE="supabase/docs/performance-analysis-$(date +%Y%m%d%H%M%S).md"
mkdir -p supabase/docs

cat > "$REPORT_FILE" << 'MDEOF'
# Query Performance Analysis

**Date**: $(date -u +"%Y-%m-%d %H:%M:%S UTC")
**Database**: [redacted]
**Tool**: DB Sage db-analyze-hotpaths

---

## Executive Summary

- Queries analyzed: {count}
- Avg execution time: {avg_time}ms
- Indexes recommended: {index_count}

---

## Detailed Findings

### Query 1: {query_label}

**Current Performance:**
- Mean execution time: {mean_time}ms
- Calls: {calls}
- % of total time: {pct_time}%

**EXPLAIN ANALYZE Output:**
```
{explain_output}
```

**Issues Identified:**
1. {issue_1}
2. {issue_2}

**Recommended Indexes:**
```sql
{recommended_indexes}
```

**Expected Improvement:** {estimated_improvement}

---

[Repeat for each query...]

---

## Action Items

- [ ] Create migration for recommended indexes
- [ ] Update statistics: ANALYZE {tables}
- [ ] Re-run analysis after changes
- [ ] Monitor with pg_stat_statements

MDEOF

echo "✓ Report: $REPORT_FILE"
```

---

## Output

Display summary and next steps:

```
✅ HOT PATH ANALYSIS COMPLETE

Queries analyzed: {count}
Report: supabase/docs/performance-analysis-{timestamp}.md

Key Findings:
- {finding_1}
- {finding_2}
- {finding_3}

Recommended Actions:
1. Review report: cat {report_file}
2. Create index migration for recommended indexes
3. Update statistics: ANALYZE {affected_tables}
4. Re-run analysis: *analyze-hotpaths

Index Recommendations:
{list of CREATE INDEX statements}
```

---

## Common Query Patterns to Check

### Pattern 1: User-Specific Data
```sql
-- Hot path: Get user's posts
SELECT * FROM posts WHERE user_id = 'xxx';

-- Check: Index on user_id exists?
-- Verify: USING (auth.uid() = user_id) is wrapped in SELECT for RLS performance
```

### Pattern 2: Joins
```sql
-- Hot path: Posts with author info
SELECT p.*, u.name
FROM posts p
JOIN users u ON p.user_id = u.id;

-- Check: Index on posts(user_id)? Index on users(id) should exist (PK)
```

### Pattern 3: Filters + Sorts
```sql
-- Hot path: Recent published posts
SELECT * FROM posts
WHERE status = 'published'
ORDER BY created_at DESC
LIMIT 10;

-- Check: Index on (status, created_at DESC)?
```

### Pattern 4: Aggregations
```sql
-- Hot path: User post count
SELECT user_id, COUNT(*)
FROM posts
GROUP BY user_id;

-- Check: Index on user_id? Or denormalize count?
```

---

## BUFFERS Output Interpretation

**Good (Cached):**
```
Buffers: shared hit=100
```
= 100 blocks found in cache (no disk I/O)

**Bad (Disk Reads):**
```
Buffers: shared hit=10 read=990
```
= Only 10 blocks cached, 990 read from disk

**Very Bad (Temp Files):**
```
Buffers: temp read=5000 written=5000
```
= Query spilled to disk (work_mem too small)

**Target:** Maximize "shared hit", minimize "shared read", zero "temp"

---

## Supabase-Specific Notes

### Using with Supabase Client (PostgREST)

Enable explain in SQL editor first (dev only):
```sql
-- Run once in Dashboard SQL Editor
ALTER DATABASE postgres SET app.settings.explain TO 'on';
```

Then use in code:
```javascript
const { data, error } = await supabase
  .from('posts')
  .select('*')
  .eq('status', 'published')
  .explain({ analyze: true, buffers: true })
```

### Supabase Studio Integration

- Navigate to: **Query Performance Report**
- Select slow query
- Click **"indexes" tab** for index_advisor recommendations
- One-click to create migration

---

## Prerequisites

- pg_stat_statements extension enabled (default in Supabase)
- Sufficient database activity to populate statistics
- For index_advisor: index_advisor extension (Supabase Pro+)

---

## Best Practices

1. **Always use BUFFERS**: `EXPLAIN (ANALYZE, BUFFERS)`
2. **Look for patterns**: One slow query often indicates a systemic issue
3. **Update statistics**: Run `ANALYZE` after significant data changes
4. **Test indexes**: Create indexes CONCURRENTLY in production
5. **Re-measure**: After optimizations, re-run this analysis
6. **RLS Performance**: Wrap auth functions in SELECT for 19x speedup

---

## References

- [PostgreSQL EXPLAIN Documentation](https://www.postgresql.org/docs/current/sql-explain.html)
- [Supabase Query Optimization](https://supabase.com/docs/guides/database/query-optimization)
- [Supabase RLS Performance](https://supabase.com/docs/guides/troubleshooting/rls-performance-and-best-practices-Z5Jjwv)
- [index_advisor Extension](https://supabase.com/docs/guides/database/extensions/index_advisor)


## Referência: references/squad/tasks/db-apply-migration.md

# Task: Apply Migration (with snapshot + advisory lock)

| Field | Value |
|-------|-------|
| **execution_type** | `Hybrid` |
| **pattern** | EXEC-HY-001 |
| **script** | `scripts/db-ops/migration-runner.sh` |
| **rationale** | Worker executa migration, Human DEVE aprovar antes (altera schema produção) |

**Purpose**: Safely apply a migration with pre/post snapshots and exclusive lock

**Elicit**: true

---

## Inputs

- `path` (string): Path to SQL migration file

---

## Process

### 1. Pre-Flight Checks

Ask user to confirm:
- Migration file: `{path}`
- Database: `$SUPABASE_DB_URL` (redacted)
- Dry-run completed? (yes/no)
- Backup/snapshot taken? (will be done automatically)

**CRITICAL**: If user says dry-run not done, stop and recommend: `*dry-run {path}`

### 2. Use Migration Safe Runner Script (RECOMMENDED)

**NEW: Use the automated script for safer execution:**

```bash
# Use the migration-safe-runner script for complete safety
./squads/db-sage/scripts/db-ops/migration-runner.sh {path} --verify-order
./squads/db-sage/scripts/db-ops/migration-runner.sh {path} --dry-run
./squads/db-sage/scripts/db-ops/migration-runner.sh {path} --force

# The canonical worker-first path automatically handles:
# - Advisory locks
# - Pre/post snapshots
# - Dry-run validation
# - Rollback preparation
# - Error handling
```

**OR continue with manual steps below:**

### 3. Acquire Advisory Lock (Manual Method)

Ensure no concurrent migrations:

```bash
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -c \
"SELECT pg_try_advisory_lock(hashtext('dbsage:migrate')) AS got" \
| grep -q t || { echo "❌ Another migration is running"; exit 1; }

echo "✓ Migration lock acquired"
```

### 4. Pre-Migration Snapshot (Manual Method)

Create schema-only snapshot before changes:

```bash
TS=$(date +%Y%m%d%H%M%S)
mkdir -p supabase/snapshots supabase/rollback

pg_dump "$SUPABASE_DB_URL" --schema-only --clean --if-exists \
  > "supabase/snapshots/${TS}_before.sql"

echo "✓ Pre-migration snapshot: supabase/snapshots/${TS}_before.sql"
echo $TS > /tmp/dbsage_migration_ts
```

### 4. Apply Migration

Run migration in transaction:

```bash
echo "Applying migration..."
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -f {path}

if [ $? -eq 0 ]; then
  echo "✓ Migration applied successfully"
else
  echo "❌ Migration failed - rolling back..."
  # Advisory lock will be released on disconnect
  exit 1
fi
```

### 5. Post-Migration Snapshot

Create snapshot after changes:

```bash
TS=$(cat /tmp/dbsage_migration_ts)

pg_dump "$SUPABASE_DB_URL" --schema-only --clean --if-exists \
  > "supabase/snapshots/${TS}_after.sql"

echo "✓ Post-migration snapshot: supabase/snapshots/${TS}_after.sql"
```

### 6. Generate Diff (Optional)

```bash
diff -u "supabase/snapshots/${TS}_before.sql" \
        "supabase/snapshots/${TS}_after.sql" \
  > "supabase/snapshots/${TS}_diff.patch" || true

echo "✓ Diff saved: supabase/snapshots/${TS}_diff.patch"
```

### 7. Release Advisory Lock

```bash
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -c \
"SELECT pg_advisory_unlock(hashtext('dbsage:migrate'));"

echo "✓ Migration lock released"
```

### 8. Post-Migration Actions

Present options to user:

**1. Run smoke tests** - `*smoke-test`  
**2. Check RLS coverage** - `*rls-audit`  
**3. Verify query performance** - `*analyze-hotpaths`  
**4. Done for now**

---

## Success Output

```
✅ Migration Applied Successfully

Timestamp: {TS}
Migration: {path}
Snapshots:
  - Before: supabase/snapshots/{TS}_before.sql
  - After:  supabase/snapshots/{TS}_after.sql
  - Diff:   supabase/snapshots/{TS}_diff.patch

Next steps:
  *smoke-test     - Validate migration
  *rls-audit      - Check security
  *rollback {TS}  - Undo if needed
```

---

## Rollback Instructions

If migration needs to be undone:

```bash
*rollback supabase/snapshots/{TS}_before.sql
```

Or create manual rollback script in `supabase/rollback/{TS}_rollback.sql`

---

## Error Handling

### Migration Fails Mid-Execution

1. PostgreSQL transaction is rolled back automatically
2. Advisory lock released on disconnect
3. Pre-migration snapshot still available
4. Database unchanged

### Lock Already Held

```
❌ Another migration is running
Wait for completion or check for stuck locks:

SELECT * FROM pg_locks WHERE locktype = 'advisory';
```

### Snapshot Creation Fails

- Check disk space
- Verify pg_dump version compatibility
- Check database permissions

---

## Safety Features

✅ Advisory lock prevents concurrent migrations  
✅ Pre/post snapshots for comparison  
✅ ON_ERROR_STOP prevents partial application  
✅ Transaction-wrapped execution  
✅ Automatic diff generation  
✅ Rollback instructions provided


## Referência: references/squad/tasks/db-best-practices-audit.md

# Task: Best Practices Audit

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/best-practices-auditor.sh` |
| **rationale** | Worker executa queries, aplica criterios explicitos e gera scorecard estruturado |

**Purpose**: Audit database against 30 Supabase Agent Skills rules

**Elicit**: false

---

Resolve the connection once before running the manual queries:

```bash
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
test -n "$DB_URL" || { echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"; exit 1; }
```

## Process

### 1. Connection Management Audit

```bash
psql "$DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\echo '=== CONNECTION MANAGEMENT AUDIT ==='
\echo ''

-- Current connections by state
\echo 'Active Connections:'
SELECT state, COUNT(*) as count, array_agg(DISTINCT usename) as users
FROM pg_stat_activity
WHERE datname = current_database()
GROUP BY state
ORDER BY count DESC;

\echo ''
\echo 'Configuration:'
SELECT name, setting, unit
FROM pg_settings
WHERE name IN (
  'max_connections',
  'idle_in_transaction_session_timeout',
  'statement_timeout',
  'lock_timeout'
);

\echo ''
\echo 'Connection Pool Check:'
SELECT
  (SELECT COUNT(*) FROM pg_stat_activity WHERE datname = current_database()) as active_conn,
  (SELECT setting::int FROM pg_settings WHERE name = 'max_connections') as max_conn,
  ROUND(100.0 * (SELECT COUNT(*) FROM pg_stat_activity WHERE datname = current_database()) /
        (SELECT setting::int FROM pg_settings WHERE name = 'max_connections'), 1) as usage_pct;

SQL
```

**Criteria:**
- [ ] usage_pct < 80%
- [ ] idle_in_transaction_session_timeout > 0
- [ ] statement_timeout > 0

---

### 2. Foreign Key Index Audit

```bash
psql "$DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\echo '=== FOREIGN KEY INDEX AUDIT ==='
\echo ''

-- FKs without indexes
\echo 'Foreign Keys WITHOUT Indexes (CRITICAL):'
SELECT
    c.conrelid::regclass AS table_name,
    a.attname AS fk_column,
    c.confrelid::regclass AS references_table,
    pg_size_pretty(pg_relation_size(c.conrelid)) AS table_size
FROM pg_constraint c
JOIN pg_attribute a ON a.attrelid = c.conrelid AND a.attnum = ANY(c.conkey)
WHERE c.contype = 'f'
AND c.conrelid::regclass::text NOT LIKE 'pg_%'
AND NOT EXISTS (
    SELECT 1 FROM pg_index i
    WHERE i.indrelid = c.conrelid
    AND a.attnum = ANY(i.indkey)
)
ORDER BY pg_relation_size(c.conrelid) DESC;

\echo ''
\echo 'Summary:'
SELECT
  (SELECT COUNT(*) FROM pg_constraint WHERE contype = 'f') AS total_fks,
  COUNT(*) AS fks_without_index
FROM pg_constraint c
JOIN pg_attribute a ON a.attrelid = c.conrelid AND a.attnum = ANY(c.conkey)
WHERE c.contype = 'f'
AND NOT EXISTS (
    SELECT 1 FROM pg_index i
    WHERE i.indrelid = c.conrelid
    AND a.attnum = ANY(i.indkey)
);

SQL
```

**Criteria:**
- [ ] fks_without_index = 0 (for tables >10k rows)

---

### 3. RLS Coverage Audit

```bash
psql "$DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\echo '=== RLS COVERAGE AUDIT ==='
\echo ''

-- Tables without RLS
\echo 'Tables WITHOUT RLS (Security Risk):'
SELECT
  t.tablename,
  pg_size_pretty(pg_relation_size(quote_ident(t.tablename)::regclass)) AS size,
  (SELECT COUNT(*) FROM pg_attribute a
   WHERE a.attrelid = quote_ident(t.tablename)::regclass
   AND a.attname LIKE '%user%') AS has_user_column
FROM pg_tables t
WHERE t.schemaname = 'public'
AND t.rowsecurity = false
ORDER BY pg_relation_size(quote_ident(t.tablename)::regclass) DESC;

\echo ''
\echo 'Tables with RLS but NO POLICIES (Completely Blocked):'
SELECT t.tablename
FROM pg_tables t
WHERE t.schemaname = 'public'
AND t.rowsecurity = true
AND NOT EXISTS (
  SELECT 1 FROM pg_policies p
  WHERE p.tablename = t.tablename
  AND p.schemaname = 'public'
);

\echo ''
\echo 'Policy Coverage Summary:'
SELECT
  t.tablename,
  t.rowsecurity AS rls_enabled,
  COUNT(p.policyname) AS policy_count,
  ARRAY_AGG(DISTINCT p.cmd) FILTER (WHERE p.cmd IS NOT NULL) AS operations_covered
FROM pg_tables t
LEFT JOIN pg_policies p ON p.tablename = t.tablename AND p.schemaname = 'public'
WHERE t.schemaname = 'public'
GROUP BY t.tablename, t.rowsecurity
ORDER BY t.rowsecurity DESC, policy_count;

\echo ''
\echo 'RLS Summary:'
SELECT
  COUNT(*) AS total_tables,
  COUNT(*) FILTER (WHERE rowsecurity) AS rls_enabled,
  COUNT(*) FILTER (WHERE NOT rowsecurity) AS rls_disabled,
  ROUND(100.0 * COUNT(*) FILTER (WHERE rowsecurity) / COUNT(*), 1) AS coverage_pct
FROM pg_tables
WHERE schemaname = 'public';

SQL
```

**Criteria:**
- [ ] All user-data tables have RLS enabled
- [ ] No tables with RLS but zero policies

---

### 4. Schema Quality Audit

```bash
psql "$DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\echo '=== SCHEMA QUALITY AUDIT ==='
\echo ''

-- Data type issues
\echo 'Potential Data Type Issues:'
SELECT
  c.table_name,
  c.column_name,
  c.data_type,
  CASE
    WHEN c.data_type = 'timestamp without time zone' THEN 'Use TIMESTAMPTZ'
    WHEN c.data_type = 'character varying' AND c.character_maximum_length > 255 THEN 'Consider TEXT'
    WHEN c.data_type = 'double precision' AND c.column_name LIKE '%price%' THEN 'Use NUMERIC for money'
    WHEN c.data_type = 'double precision' AND c.column_name LIKE '%amount%' THEN 'Use NUMERIC for money'
    WHEN c.data_type = 'integer' AND c.column_name = 'id' THEN 'Consider BIGINT for PKs'
    WHEN c.data_type = 'json' THEN 'Use JSONB instead'
  END AS recommendation
FROM information_schema.columns c
WHERE c.table_schema = 'public'
AND (
  c.data_type = 'timestamp without time zone'
  OR (c.data_type = 'character varying' AND c.character_maximum_length > 255)
  OR (c.data_type = 'double precision' AND (c.column_name LIKE '%price%' OR c.column_name LIKE '%amount%'))
  OR (c.data_type = 'integer' AND c.column_name = 'id')
  OR c.data_type = 'json'
)
ORDER BY c.table_name;

\echo ''
\echo 'Primary Key Types:'
SELECT
  tc.table_name,
  c.column_name,
  c.data_type,
  CASE
    WHEN c.data_type = 'uuid' THEN 'OK'
    WHEN c.data_type = 'bigint' THEN 'OK'
    WHEN c.data_type = 'integer' THEN 'Consider BIGINT'
    ELSE 'Review'
  END AS status
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.columns c
  ON c.table_name = kcu.table_name AND c.column_name = kcu.column_name
WHERE tc.constraint_type = 'PRIMARY KEY'
AND tc.table_schema = 'public'
ORDER BY status DESC, tc.table_name;

\echo ''
\echo 'Naming Convention Check (should be snake_case):'
SELECT 'table' AS type, tablename AS name, 'Contains uppercase' AS issue
FROM pg_tables WHERE schemaname = 'public' AND tablename ~ '[A-Z]'
UNION ALL
SELECT 'column', table_name || '.' || column_name, 'Contains uppercase'
FROM information_schema.columns
WHERE table_schema = 'public' AND column_name ~ '[A-Z]';

SQL
```

**Criteria:**
- [ ] No TIMESTAMP without time zone
- [ ] No VARCHAR > 255 (use TEXT)
- [ ] No FLOAT/DOUBLE for money
- [ ] All identifiers snake_case

---

### 5. Query Performance Audit

```bash
psql "$DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\echo '=== QUERY PERFORMANCE AUDIT ==='
\echo ''

-- Check if pg_stat_statements is available
\echo 'pg_stat_statements status:'
SELECT
  CASE WHEN EXISTS (SELECT 1 FROM pg_extension WHERE extname = 'pg_stat_statements')
    THEN 'ENABLED'
    ELSE 'DISABLED - run: CREATE EXTENSION pg_stat_statements'
  END AS status;

-- Top slow queries (if extension available)
\echo ''
\echo 'Top 10 Slow Queries (mean_exec_time > 100ms):'
SELECT
  ROUND(mean_exec_time::numeric, 2) AS mean_ms,
  calls,
  ROUND(total_exec_time::numeric, 2) AS total_ms,
  LEFT(query, 100) AS query_preview
FROM pg_stat_statements
WHERE mean_exec_time > 100
AND query NOT LIKE '%pg_stat%'
ORDER BY mean_exec_time DESC
LIMIT 10;

\echo ''
\echo 'Sequential Scans on Large Tables (potential index needed):'
SELECT
  schemaname,
  relname AS table_name,
  seq_scan,
  seq_tup_read,
  idx_scan,
  pg_size_pretty(pg_relation_size(relid)) AS size,
  CASE
    WHEN idx_scan = 0 AND seq_scan > 100 THEN 'CRITICAL: No index usage'
    WHEN seq_tup_read / NULLIF(seq_scan, 0) > 10000 THEN 'HIGH: Large seq scans'
    ELSE 'OK'
  END AS status
FROM pg_stat_user_tables
WHERE seq_scan > 0
AND pg_relation_size(relid) > 10000000  -- > 10MB
ORDER BY seq_tup_read DESC
LIMIT 10;

SQL
```

**Criteria:**
- [ ] pg_stat_statements enabled
- [ ] No seq scans on tables >10MB with >100 scans

---

### 6. Index Quality Audit

```bash
psql "$DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\echo '=== INDEX QUALITY AUDIT ==='
\echo ''

-- Unused indexes
\echo 'Potentially Unused Indexes (candidates for removal):'
SELECT
  schemaname,
  relname AS table_name,
  indexrelname AS index_name,
  pg_size_pretty(pg_relation_size(indexrelid)) AS index_size,
  idx_scan AS times_used
FROM pg_stat_user_indexes
WHERE idx_scan < 10
AND pg_relation_size(indexrelid) > 1000000  -- > 1MB
AND indexrelname NOT LIKE '%pkey%'
AND indexrelname NOT LIKE '%pk%'
ORDER BY pg_relation_size(indexrelid) DESC
LIMIT 10;

\echo ''
\echo 'Duplicate Indexes:'
SELECT
  indrelid::regclass AS table_name,
  array_agg(indexrelid::regclass) AS index_names
FROM pg_index
GROUP BY indrelid, indkey
HAVING COUNT(*) > 1;

\echo ''
\echo 'Index Types Distribution:'
SELECT
  am.amname AS index_type,
  COUNT(*) AS count
FROM pg_index i
JOIN pg_class c ON c.oid = i.indexrelid
JOIN pg_am am ON am.oid = c.relam
WHERE c.relnamespace = 'public'::regnamespace
GROUP BY am.amname
ORDER BY count DESC;

SQL
```

**Criteria:**
- [ ] Review unused indexes
- [ ] No duplicate indexes
- [ ] Appropriate index types for data

---

### 7. Vacuum & Statistics Audit

```bash
psql "$DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\echo '=== VACUUM & STATISTICS AUDIT ==='
\echo ''

-- Tables needing vacuum
\echo 'Tables with High Dead Tuple Count:'
SELECT
  schemaname,
  relname AS table_name,
  n_live_tup,
  n_dead_tup,
  ROUND(100.0 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0), 1) AS dead_pct,
  last_vacuum,
  last_autovacuum,
  last_analyze,
  last_autoanalyze
FROM pg_stat_user_tables
WHERE n_dead_tup > 1000
ORDER BY n_dead_tup DESC
LIMIT 10;

\echo ''
\echo 'Tables Never Analyzed:'
SELECT relname AS table_name, last_analyze, last_autoanalyze
FROM pg_stat_user_tables
WHERE last_analyze IS NULL AND last_autoanalyze IS NULL;

\echo ''
\echo 'Autovacuum Settings:'
SELECT name, setting, unit
FROM pg_settings
WHERE name LIKE 'autovacuum%'
ORDER BY name;

SQL
```

**Criteria:**
- [ ] No tables with >10% dead tuples
- [ ] All tables analyzed recently
- [ ] Autovacuum enabled

---

## Output Summary

### Score Calculation

| Category | Weight | Checks | Passed | Score |
|----------|--------|--------|--------|-------|
| Connection | 15% | 5 | | |
| FK Indexes | 15% | 2 | | |
| RLS | 20% | 4 | | |
| Schema | 15% | 6 | | |
| Query Perf | 15% | 4 | | |
| Indexes | 10% | 3 | | |
| Vacuum | 10% | 4 | | |
| **TOTAL** | **100%** | **28** | | |

*Maps to 30 Supabase Agent Skills rules (see checklist for full breakdown)*

### Issue Classification

**CRITICAL (Fix Now):**
- FKs without indexes on tables >10k rows
- User tables without RLS
- Connection usage >90%

**HIGH (Fix This Sprint):**
- pg_stat_statements not enabled
- Sequential scans on large tables
- TIMESTAMP without timezone

**MEDIUM (Schedule Fix):**
- Schema naming inconsistencies
- Unused indexes
- Tables needing vacuum

---

## SQL Fix Generation

After audit, generate fixes with:

### Fix Missing FK Indexes
```sql
-- Copy-paste output from FK audit and run:
-- CREATE INDEX CONCURRENTLY idx_{table}_{column} ON {table}({column});
```

### Enable RLS
```sql
-- For each table without RLS:
-- ALTER TABLE {table} ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "{table}_policy" ON {table} FOR ALL TO authenticated USING (...);
```

### Run Vacuum
```sql
-- For tables with high dead tuples:
-- VACUUM (VERBOSE, ANALYZE) {table};
```

---

---

### 8. Audit Trail Check

```bash
psql "$DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\echo '=== AUDIT TRAIL CHECK ==='

-- Check pgaudit extension
\echo 'pgaudit status:'
SELECT
  CASE WHEN EXISTS (SELECT 1 FROM pg_extension WHERE extname = 'pgaudit')
    THEN 'INSTALLED'
    ELSE 'NOT INSTALLED'
  END AS pgaudit_status;

-- Check auditor role and grants
\echo ''
\echo 'Tables configured for audit (via auditor role):'
SELECT table_name, array_agg(privilege_type ORDER BY privilege_type) as privileges
FROM information_schema.table_privileges
WHERE grantee = 'auditor'
GROUP BY table_name
ORDER BY table_name;

-- Check pgaudit settings
\echo ''
\echo 'pgaudit configuration:'
SELECT name, setting
FROM pg_settings
WHERE name LIKE 'pgaudit%';

SQL
```

**Criteria:**
- [ ] pgaudit installed OR custom audit triggers in place
- [ ] Sensitive tables (user_*, credentials, payments) covered
- [ ] Audit logging enabled (pgaudit.log != 'none')

---

## Integration

Run this task:
- **Weekly**: As part of maintenance routine
- **Pre-deploy**: Before any production migration
- **Post-incident**: After performance issues
- **Quarterly**: Full audit with team review

Use with: `*best-practices-audit`


## Referência: references/squad/tasks/db-bootstrap.md

# Task: Bootstrap Supabase Project

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/bootstrap-runner.sh` |
| **rationale** | Criação de estrutura de diretórios é determinística |

**Purpose**: Create standard Supabase project structure

**Elicit**: true

## 🚀 NEW: Use Dedicated Bootstrap Runner (RECOMMENDED)

**Token Savings: 90% | Time Savings: ~88%**

```bash
# Minimal scaffold: directories only
./squads/db-sage/scripts/db-ops/bootstrap-runner.sh --profile minimal

# Standard scaffold: directories + READMEs + config
./squads/db-sage/scripts/db-ops/bootstrap-runner.sh --profile standard --project-name {project_name}

# Full scaffold: standard + baseline migration
./squads/db-sage/scripts/db-ops/bootstrap-runner.sh --profile full --project-name {project_name}
```

**OR continue with manual bootstrap below:**

---

## Process

### 1. Confirm Project Setup

Ask user:

**Project name**: (e.g., "my-project")

**Include starter templates?**
1. Minimal - Directories only
2. Standard - Directories + READMEs + config
3. Full - Everything + baseline schema example

### 2. Create Directory Structure

```bash
mkdir -p supabase/{migrations,seeds,tests,rollback,snapshots,docs}

echo "✓ Created directories:
  supabase/migrations/    - Schema migrations
  supabase/seeds/         - Seed data
  supabase/tests/         - Smoke tests
  supabase/rollback/      - Rollback scripts
  supabase/snapshots/     - Schema snapshots
  supabase/docs/          - Documentation"
```

### 3. Create Core Files

#### supabase/migrations/README.md

```markdown
# Migrations

## Naming: YYYYMMDDHHMMSS_description.sql

Example: 20251026120000_baseline_schema.sql

## Order (within each file):
1. Extensions
2. Tables + Constraints
3. Functions
4. Triggers
5. RLS (enable + policies)
6. Views

## Workflow:
*verify-order migration.sql  # Check order
*dry-run migration.sql       # Test
*snapshot pre_migration      # Create rollback point
*apply-migration migration.sql  # Apply
*smoke-test                  # Validate
```

#### supabase/seeds/README.md

```markdown
# Seeds

## Naming: YYYYMMDDHHMMSS_description_seed.sql

## Types:
- Required: Data app needs to function
- Test: Sample data for development
- Reference: Lookup tables (countries, categories)

## Idempotent pattern:
INSERT INTO table (id, name) VALUES (1, 'value')
ON CONFLICT (id) DO NOTHING;
```

#### supabase/tests/README.md

```markdown
# Tests

## Smoke tests (post-migration validation):
- Tables exist
- RLS enabled
- Policies installed
- Functions callable
- Basic queries work

## Run: *smoke-test
```

#### supabase/rollback/README.md

```markdown
# Rollback

## Snapshots (automatic):
Created by *apply-migration and *snapshot commands
Located in: ../snapshots/

## Manual rollback scripts:
Write explicit undo operations for complex migrations

Example: YYYYMMDDHHMMSS_rollback_description.sql
```

#### supabase/.gitignore

```gitignore
# Local dev
.env
.env.local
.branches
.temp

# OS
.DS_Store
Thumbs.db

# Optional: Snapshots (if too large for git)
# snapshots/*.sql
```

### 4. Generate config.toml (if Standard or Full)

```toml
# Supabase Local Development Config

[api]
enabled = true
port = 54321

[db]
port = 54322
shadow_port = 54320
major_version = 15

[db.pooler]
enabled = true
port = 54329
pool_mode = "transaction"

[studio]
enabled = true
port = 54323

[auth]
enabled = true
site_url = "http://localhost:3000"

# See: https://supabase.com/docs/guides/cli/config
```

### 5. Create Baseline Schema (if Full option)

#### supabase/migrations/00000000000000_baseline.sql

```sql
-- Baseline Schema
-- Run after: supabase init

BEGIN;

-- Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Example table (customize for your project)
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    username TEXT UNIQUE,
    full_name TEXT,
    avatar_url TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Updated_at trigger
CREATE OR REPLACE FUNCTION public.handle_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at
    BEFORE UPDATE ON public.profiles
    FOR EACH ROW
    EXECUTE FUNCTION public.handle_updated_at();

-- RLS
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view own profile"
    ON public.profiles FOR SELECT
    TO authenticated
    USING (auth.uid() = id);

CREATE POLICY "Users can update own profile"
    ON public.profiles FOR UPDATE
    TO authenticated
    USING (auth.uid() = id)
    WITH CHECK (auth.uid() = id);

-- Grants
GRANT USAGE ON SCHEMA public TO authenticated, anon;
GRANT SELECT, INSERT, UPDATE ON public.profiles TO authenticated;

COMMIT;
```

### 6. Create Initial Smoke Test

#### supabase/tests/smoke_test.sql

```sql
-- Basic smoke test
SET client_min_messages = warning;

\echo 'Checking tables...'
SELECT COUNT(*) AS tables FROM information_schema.tables 
WHERE table_schema='public';

\echo 'Checking RLS...'
SELECT COUNT(*) AS rls_enabled FROM pg_tables 
WHERE schemaname='public' AND rowsecurity=true;

\echo 'Checking policies...'
SELECT COUNT(*) AS policies FROM pg_policies 
WHERE schemaname='public';

\echo '✓ Smoke test complete'
```

### 7. Create Migration Log

#### supabase/docs/migration-log.md

```markdown
# Migration Log

## Format:
### Version X.Y.Z - Description (Date)
- Migration: filename.sql
- Status: ✅ Success / ❌ Failed / ⏪ Rolled Back
- Changes: What changed
- Rollback: How to undo

---

## Baseline (Initial)
- Migration: 00000000000000_baseline.sql
- Status: ⏳ Pending
- Changes: Initial project structure
- Rollback: N/A (baseline)
```

---

## Success Output

```
✅ Supabase Project Bootstrapped

Structure created:
  supabase/
  ├── migrations/      (migration files)
  ├── seeds/          (seed data)
  ├── tests/          (smoke tests)
  ├── rollback/       (rollback scripts)
  ├── snapshots/      (schema snapshots)
  ├── docs/           (documentation)
  ├── config.toml     (local config)
  └── .gitignore

Next steps:
  1. Set SUPABASE_DB_URL in .env
  2. *env-check - Validate setup
  3. *apply-migration supabase/migrations/00000000000000_baseline.sql
  4. *smoke-test - Validate baseline
  5. *snapshot baseline - Create initial snapshot

Documentation:
  - supabase/migrations/README.md
  - supabase/docs/migration-log.md
```

---

## Environment Setup

Create `.env` file in project root:

```bash
# Supabase Database Connection
# Get from: https://app.supabase.com/project/_/settings/database

# Pooler (recommended for migrations)
SUPABASE_DB_URL="postgresql://postgres.[PASSWORD]@[PROJECT-REF].supabase.co:6543/postgres?sslmode=require"

# Direct (for backups/analysis)
# SUPABASE_DB_URL="postgresql://postgres.[PASSWORD]@[PROJECT-REF].supabase.co:5432/postgres?sslmode=require"
```

**Security**:
- ✅ Added to .gitignore
- ✅ Use pooler (port 6543)
- ✅ Require SSL

---

## Project Options

### Minimal (Directories Only)
```
supabase/
├── migrations/
├── seeds/
├── tests/
├── rollback/
├── snapshots/
└── docs/
```
**Use for**: Existing projects, simple setups

### Standard (+ READMEs + Config)
```
+ README.md files
+ config.toml
+ .gitignore
+ migration-log.md
```
**Use for**: New projects, team environments

### Full (+ Baseline Schema)
```
+ baseline.sql migration
+ smoke_test.sql
+ Example profiles table
+ RLS policies
```
**Use for**: Greenfield projects, learning

---

## Integration with Existing Projects

If `supabase/` already exists:

```bash
# Backup existing
mv supabase supabase.backup

# Bootstrap new
*bootstrap

# Merge as needed
cp supabase.backup/migrations/* supabase/migrations/
```

---

## Customization

### For Your Project

Replace baseline.sql with your tables:
- Copy schema from existing DB
- Or design with: `*create-schema`
- Then create migration file

### Team Standards

Edit READMEs to add:
- Team-specific naming conventions
- Required reviewers for migrations
- Deployment procedures
- Contact information

### CI/CD Integration

Add to pipeline:

```yaml
# .github/workflows/db-test.yml
- name: Run smoke tests
  run: |
    /db-sage
    *smoke-test
```

---

## Next Steps After Bootstrap

1. **Environment**: Set SUPABASE_DB_URL
2. **Validate**: `*env-check`
3. **Design**: `*create-schema` (or use existing)
4. **Migrate**: `*apply-migration baseline.sql`
5. **Test**: `*smoke-test`
6. **Snapshot**: `*snapshot baseline`
7. **Document**: Update migration-log.md

---

## Common Issues

### "Directory already exists"

**Problem**: supabase/ folder exists  
**Options**:
1. Backup and replace (recommended)
2. Merge manually
3. Choose different directory

### "No permission to create directories"

**Problem**: Insufficient file permissions  
**Fix**: Check you're in project root with write access

### "Config conflicts with existing Supabase project"

**Problem**: Already using Supabase CLI  
**Solution**: Bootstrap is compatible with Supabase CLI
- Keep existing config
- Use bootstrap for organization only

---

## Related Commands

- `*create-schema` - Design schema interactively
- `*apply-migration {path}` - Run first migration
- `*smoke-test` - Validate setup
- `*snapshot baseline` - Create initial snapshot
- `*env-check` - Validate environment


## Referência: references/squad/tasks/db-dry-run.md

# Task: Migration Dry-Run

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/migration-runner.sh` |
| **rationale** | BEGIN/ROLLBACK é operação determinística do PostgreSQL |

**Purpose**: Execute migration inside BEGIN…ROLLBACK to catch syntax/ordering errors

**Elicit**: true

---

## 🚀 NEW: Use Automated Migration Safe Runner (RECOMMENDED)

**Token Savings: 91% | Time Savings: ~88%**

```bash
# Dry-run migration with automatic error detection
./squads/db-sage/scripts/db-ops/migration-runner.sh {path} --dry-run

# Dry-run after deterministic order verification
./squads/db-sage/scripts/db-ops/migration-runner.sh {path} --verify-order
./squads/db-sage/scripts/db-ops/migration-runner.sh {path} --dry-run

# Benefits:
#   - Automatic syntax validation
#   - Dependency order checking
#   - Pre/post snapshot comparison
#   - Rollback script validation
#   - 91% token savings
```

**OR continue with manual dry-run below:**

---

## Inputs

- `path` (string): Path to SQL migration file

---

## Process

### 1. Confirm Migration File

Ask user to confirm:
- Migration file path: `{path}`
- Purpose of this migration
- Expected changes (tables, functions, etc)

### 2. Execute Dry-Run

Run migration in transaction that will be rolled back:

```bash
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
BEGIN;
\echo 'Starting dry-run...'
\i {path}
\echo 'Dry-run completed successfully - rolling back...'
ROLLBACK;
SQL
```

### 3. Report Results

**If successful:**
```
✓ Dry-run completed without errors
✓ Migration syntax is valid
✓ No dependency or ordering issues detected
```

**If failed:**
```
❌ Dry-run failed
Error: [error message]
Line: [line number if available]
Fix the migration and try again
```

---

## What This Validates

- ✅ SQL syntax correctness
- ✅ Object dependencies exist
- ✅ Execution order is valid
- ✅ No constraint violations
- ❌ Does NOT validate data correctness
- ❌ Does NOT check performance

---

## Next Steps After Success

1. Review migration one more time
2. Take snapshot: `*snapshot pre_migration`
3. Apply migration: `*apply-migration {path}`
4. Run smoke tests: `*smoke-test`

---

## Error Handling

Common errors and fixes:

**"relation does not exist"**
- Missing table/view dependency
- Check if you need to create dependent objects first

**"function does not exist"**
- Function called before creation
- Reorder: tables → functions → triggers

**"syntax error"**
- Check SQL syntax
- Verify PostgreSQL version compatibility


## Referência: references/squad/tasks/db-env-check.md

# Task: DB Env Check

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/health-checker.sh` |
| **rationale** | Verificação de env vars e conectividade é determinística |

**Purpose**: Validate environment for DB operations without leaking secrets

**Elicit**: false

---

## 🚀 NEW: Use Automated Health Checker (RECOMMENDED)

**Token Savings: 95% | Time Savings: ~90%**

```bash
# Use the health-checker script for complete environment validation
./squads/db-sage/scripts/db-ops/health-checker.sh --quick

# Full health check
./squads/db-sage/scripts/db-ops/health-checker.sh --full

# Benefits:
#   - Environment validation
#   - Connection pool status
#   - Security checks
#   - Performance metrics
#   - 95% token savings
```

**OR continue with manual environment checks below:**

---

## Steps (Manual Method)

### 1. Validate Required Environment Variables

```bash
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
test -n "$DB_URL" || { echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"; exit 1; }

if [ -n "${SUPABASE_DB_URL:-}" ]; then
  echo "✓ SUPABASE_DB_URL present (redacted)"
else
  echo "✓ DATABASE_URL present (redacted)"
fi
```

### 2. Check SSL Mode and Pooler

```bash
case "$DB_URL" in
  *"sslmode="*) echo "✓ sslmode present";;
  *) echo "⚠️ Consider adding sslmode=require";;
esac

printf '%s' "$DB_URL" | grep -q "pooler" && echo "✓ Using pooler" || echo "ℹ Pooler not detected"
```

### 3. Check Client Versions

```bash
psql --version || { echo "❌ psql missing"; exit 1; }
pg_dump --version || { echo "❌ pg_dump missing"; exit 1; }
echo "✓ PostgreSQL client tools available"
```

### 4. Check Server Connectivity

```bash
psql "$DB_URL" -v ON_ERROR_STOP=1 -t -c "SELECT version();" > /dev/null \
  && echo "✓ Database connection successful"
```

---

## Success Criteria

- All environment variables present
- PostgreSQL client tools installed
- Database connection successful
- SSL and pooler configuration validated

## Error Handling

If any check fails:
1. Show clear error message
2. Provide remediation steps
3. Exit with non-zero status


## Referência: references/squad/tasks/db-explain.md

# Task: EXPLAIN (ANALYZE, BUFFERS)

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/explain-analyzer.sh` |
| **rationale** | EXPLAIN ANALYZE é comando PostgreSQL determinístico |

**Purpose**: Run detailed query plan analysis to assess performance

**Elicit**: true

---

## 🚀 NEW: Use Automated Query Analyzer (RECOMMENDED)

**Token Savings: 87% | Time Savings: ~80%**

```bash
# Use the explain-analyzer script for automatic analysis
./squads/db-sage/scripts/db-ops/explain-analyzer.sh "{sql}"

# With execution statistics
./squads/db-sage/scripts/db-ops/explain-analyzer.sh "{sql}" --analyze --buffers

# Get JSON output for parsing
./squads/db-sage/scripts/db-ops/explain-analyzer.sh "{sql}" --format json

# Benefits:
#   - Automatic performance issue detection
#   - Index recommendations
#   - Cost analysis with thresholds
#   - 87% token savings
```

**OR continue with manual EXPLAIN below:**

---

## Inputs

- `sql` (string): SQL query to analyze

---

## Process (Manual Method)

### 1. Confirm Query

Ask user:
- Query to analyze
- Expected result count (approximate)
- Known performance issues?

### 2. Run EXPLAIN ANALYZE

Execute with full analysis options:

```bash
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 <<SQL
EXPLAIN (ANALYZE, BUFFERS, VERBOSE, FORMAT TEXT)
{sql};
SQL
```

### 3. Interpret Results

Present key metrics:

```
=== Query Performance Analysis ===

Execution Time: X.XX ms
Planning Time: Y.YY ms
Total Time: Z.ZZ ms

Buffers:
  - Shared Hit: XXX (cache hits)
  - Shared Read: YYY (disk reads)
  - Temp Read/Written: ZZZ (temp files)

Cost: XXX.XX..YYY.YY
Rows: Estimated XXX, Actual YYY
```

---

## Understanding EXPLAIN Output

### Top-Level Metrics

**Planning Time**
- Time spent planning query
- High value (>100ms) suggests complex query or missing statistics

**Execution Time**
- Actual query execution time
- This is what users experience

**Total Cost**
- Estimated cost units (not milliseconds)
- Higher = more expensive
- Compare different query versions

### Node Types (Common Patterns)

**Seq Scan** (Sequential Scan)
- 🔴 Reads entire table
- Slow for large tables
- **Fix**: Add index if filtering rows

**Index Scan**
- ✅ Uses index to find rows
- Fast for selective queries
- Good when returning few rows

**Index Only Scan**
- ✅✅ Best case - reads only index
- No table access needed
- Requires VACUUM to update visibility map

**Bitmap Heap Scan**
- ✅ Good for medium selectivity
- Combines multiple indexes
- Better than multiple index scans

**Nested Loop**
- Good for small result sets
- Joins by iterating
- Can be slow with large data

**Hash Join**
- Good for large result sets
- Builds hash table in memory
- Fast for equi-joins

**Merge Join**
- Good for sorted inputs
- Efficient for large sorted data
- Requires sorted inputs (or sorts them)

### Buffer Analysis

**Shared Hits** (Good)
- Data found in cache
- No disk I/O needed
- High ratio = good caching

**Shared Reads** (Bad if high)
- Data read from disk
- Slow compared to cache
- High ratio = cache misses

**Temp Read/Written** (Bad)
- Using temp disk files
- Memory insufficient
- Often due to large sorts/hashes

---

## Common Performance Issues

### Issue 1: Sequential Scan on Large Table

```
Seq Scan on fragments  (cost=0.00..10000 rows=1000000)
  Filter: (user_id = '...')
```

**Problem**: Scanning entire table  
**Impact**: Slow for large tables  
**Fix**: Create index

```sql
CREATE INDEX idx_fragments_user_id ON fragments(user_id);
```

### Issue 2: Missing Index on Join

```
Nested Loop  (cost=0.00..50000)
  -> Seq Scan on users
  -> Seq Scan on fragments
       Filter: (fragments.user_id = users.id)
```

**Problem**: No index for join condition  
**Impact**: Quadratic complexity  
**Fix**: Index foreign key

```sql
CREATE INDEX idx_fragments_user_id ON fragments(user_id);
```

### Issue 3: High Temp File Usage

```
Sort  (cost=10000..12000)
  Sort Key: created_at DESC
  Sort Method: external merge  Disk: 5000kB
```

**Problem**: Sorting spills to disk  
**Impact**: Much slower than in-memory  
**Fix**: Increase work_mem or add index

```sql
-- Option 1: Increase memory (session)
SET work_mem = '64MB';

-- Option 2: Add index to avoid sort
CREATE INDEX idx_fragments_created_at ON fragments(created_at DESC);
```

### Issue 4: Poor Row Estimate

```
Seq Scan on users  (cost=0.00..100 rows=10 actual rows=10000)
```

**Problem**: Estimated 10 rows, actually 10,000  
**Impact**: Wrong join strategy chosen  
**Fix**: Update statistics

```sql
ANALYZE users;
-- Or more aggressive:
VACUUM ANALYZE users;
```

### Issue 5: Slow RLS Policy

```
Seq Scan on fragments  (cost=0.00..10000 rows=500000)
  Filter: ((user_id = auth.uid()) AND (deleted_at IS NULL))
  Rows Removed by Filter: 499990
```

**Problem**: RLS policy not using index  
**Impact**: Scans all rows to apply policy  
**Fix**: Index RLS policy columns

```sql
CREATE INDEX idx_fragments_user_id_not_deleted 
ON fragments(user_id) 
WHERE deleted_at IS NULL;
```

---

## Optimization Workflow

### 1. Baseline

Run current query:
```bash
*explain "SELECT * FROM table WHERE ..."
```

Note execution time and plan.

### 2. Hypothesize

What might be slow?
- Sequential scans?
- Missing indexes?
- Sort/hash spills?
- Poor statistics?

### 3. Test Fix

Apply potential fix:
```sql
CREATE INDEX ...;
-- or
VACUUM ANALYZE table;
-- or
SET work_mem = '...';
```

### 4. Re-Measure

Run explain again:
```bash
*explain "SELECT * FROM table WHERE ..."
```

Compare:
- Execution time improved?
- Plan changed as expected?
- Cost reduced?

### 5. Iterate

Repeat until performance acceptable.

---

## Advanced Options

### Compare Different Queries

```bash
# Option A
*explain "SELECT * FROM users WHERE status = 'active'"

# Option B (rewritten)
*explain "SELECT * FROM users WHERE deleted_at IS NULL AND status = 'active'"
```

Pick query with better plan.

### Analyze Hot Paths

For critical queries, analyze under load:

```sql
-- Run multiple times to warm cache
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;

-- Check consistency of execution time
```

### Export Plan for Analysis

```bash
psql "$SUPABASE_DB_URL" -qAt -c \
"EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) SELECT ..." \
> query_plan.json
```

Upload to: https://explain.depesz.com or https://explain.dalibo.com

---

## Performance Targets

### Response Time Goals

**Interactive queries**: < 100ms  
**Reports**: < 1s  
**Batch/Background**: < 5s  

**If slower:**
- Check for sequential scans
- Add/optimize indexes
- Consider caching
- Optimize RLS policies

### Cache Hit Ratio

**Goal**: > 95% shared hits

```sql
-- Check overall cache hit ratio
SELECT 
  sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) AS cache_hit_ratio
FROM pg_statio_user_tables;
```

**If low:**
- Increase shared_buffers (DBA task)
- Query optimization needed
- Consider query pattern changes

---

## When to Use EXPLAIN

**Always:**
- New query in production code
- After schema changes
- When adding indexes
- RLS policy changes

**Reactive:**
- Slow query reports
- Performance degradation
- High database load
- Before optimization attempts

**Never:**
- For queries already known to be fast
- On queries with no data yet (stats unreliable)
- Without ANALYZE if you need actual timing

---

## Limitations

### EXPLAIN ANALYZE Runs Query

⚠️ **Warning**: ANALYZE actually executes query

**Safe:**
- SELECT queries
- Read-only queries

**Dangerous:**
- INSERT/UPDATE/DELETE (use transaction + rollback)
- Queries with side effects

```sql
-- Safe way to EXPLAIN write queries
BEGIN;
EXPLAIN ANALYZE DELETE FROM ...;
ROLLBACK;  -- Undo changes
```

### Statistics May Be Stale

Plans based on table statistics:
- Updated by VACUUM/ANALYZE
- May not reflect current data
- Run ANALYZE if estimates way off

### Plan Can Change

Plans vary based on:
- Data distribution
- Table size
- Server configuration
- Cache state
- Time of day (load)

---

## Integration with Workflow

Query optimization workflow:

1. Find slow query (logs, monitoring)
2. `*explain "SELECT ..."` - Baseline
3. Analyze plan (sequential scans? missing indexes?)
4. Hypothesize fix
5. Apply fix in dev
6. `*explain "SELECT ..."` - Verify improvement
7. Test with real data volume
8. Deploy to production
9. Monitor actual performance

---

## Resources

**Visualization Tools:**
- https://explain.depesz.com
- https://explain.dalibo.com
- https://tatiyants.com/pev/

**Documentation:**
- PostgreSQL EXPLAIN: https://www.postgresql.org/docs/current/sql-explain.html
- Using EXPLAIN: https://www.postgresql.org/docs/current/using-explain.html

**Related Commands:**
- `*analyze-hotpaths` - Check common query patterns
- `*design-indexes` - Plan index strategy
- `*rls-audit` - Check RLS policy performance


## Referência: references/squad/tasks/db-impersonate.md

# Task: Impersonate User (RLS Testing)

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/rls-test-suite.sh` |
| **rationale** | SET LOCAL de claims é operação determinística |

**Purpose**: Set session claims to emulate authenticated user for RLS testing

**Elicit**: true

---

## 🚀 NEW: Use Automated RLS Test Suite (RECOMMENDED)

**Token Savings: 93% | Time Savings: ~90%**

```bash
# Baseline RLS test against a table
./squads/db-sage/scripts/db-ops/rls-test-suite.sh {table_name}

# Test one specific user id
./squads/db-sage/scripts/db-ops/rls-test-suite.sh {table_name} "{user_id}"

# Test isolation across multiple users
./squads/db-sage/scripts/db-ops/rls-test-suite.sh {table_name} "{user_id_1},{user_id_2}"

# Benefits:
#   - Automatic session claims configuration
#   - Multi-user isolation testing
#   - Permission matrix generation
#   - Positive/negative test cases
#   - 93% token savings
```

**OR continue with manual impersonation below:**

---

## Inputs

- `user_id` (uuid): User ID to impersonate

---

## Process

### 1. Confirm Impersonation

Ask user:
- User ID to impersonate: `{user_id}`
- Purpose of impersonation (testing what?)
- Queries you plan to run

**CRITICAL WARNING**: This is for testing only. Never use in production application code.

### 2. Set Session Claims

```bash
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 <<SQL
-- Set JWT claims for current session
SELECT
  set_config('request.jwt.claims', 
    jsonb_build_object(
      'sub', '{user_id}',
      'role', 'authenticated'
    )::text, 
    true
  ) AS jwt_claims,
  set_config('request.jwt.claim.sub', '{user_id}', true) AS sub,
  set_config('role', 'authenticated', true) AS role;

-- Verify settings
SELECT 
  current_setting('request.jwt.claims', true) AS jwt_claims,
  current_setting('request.jwt.claim.sub', true) AS user_id,
  current_setting('role', true) AS role;

\echo ''
\echo '✓ Impersonating user: {user_id}'
\echo 'Run your test queries now.'
\echo 'To exit, close this session or run: RESET ALL;'
SQL
```

### 3. Interactive SQL Session

Open interactive psql for testing:

```bash
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1
```

User can now run queries as this user:

```sql
-- Test queries
SELECT * FROM my_table;  -- Should respect RLS for this user

-- Check current context
SELECT 
  auth.uid() AS current_user_id,
  current_setting('role') AS current_role;

-- Exit impersonation
RESET ALL;
```

---

## Testing Scenarios

### Positive Test (Should Succeed)

Test that user CAN access their own data:

```sql
-- User should see their own records
SELECT * FROM users WHERE id = auth.uid();

-- User should see their own fragments
SELECT * FROM fragments WHERE user_id = auth.uid();
```

### Negative Test (Should Fail or Return Empty)

Test that user CANNOT access others' data:

```sql
-- Should return empty (not their data)
SELECT * FROM fragments WHERE user_id != auth.uid();

-- Should fail if trying to insert as another user
INSERT INTO fragments (user_id, content) 
VALUES ('00000000-0000-0000-0000-000000000000', 'test');
-- Expected: RLS policy violation
```

### Multi-Tenant Test

If using org-based isolation:

```sql
-- Set org_id in JWT
SELECT set_config('request.jwt.claims', 
  jsonb_build_object(
    'sub', '{user_id}',
    'role', 'authenticated',
    'org_id', '{org_id}'
  )::text, 
  true
);

-- Test org isolation
SELECT * FROM projects;  -- Should only see org's projects
```

---

## Common Use Cases

### Test New RLS Policy

```sql
-- 1. Apply new policy
CREATE POLICY "new_policy" ON table_name ...;

-- 2. Impersonate user
*impersonate {user_id}

-- 3. Test access
SELECT * FROM table_name;

-- 4. Reset and test as different user
RESET ALL;
*impersonate {other_user_id}
SELECT * FROM table_name;
```

### Debug Access Issues

User reports "can't see their data":

```sql
-- 1. Impersonate the user
*impersonate {user_id}

-- 2. Try their query
SELECT * FROM table_name WHERE ...;

-- 3. Check what RLS policies are active
SELECT * FROM pg_policies 
WHERE tablename = 'table_name';

-- 4. Verify user_id matches
SELECT auth.uid(), user_id FROM table_name LIMIT 5;
```

### Validate Multi-User Scenario

```sql
-- User A
*impersonate {user_a_id}
SELECT COUNT(*) FROM fragments;  -- Returns A's count

-- User B
*impersonate {user_b_id}
SELECT COUNT(*) FROM fragments;  -- Returns B's count

-- Verify isolation
SELECT user_id, COUNT(*) FROM fragments GROUP BY user_id;
-- Should only show current user in impersonation
```

---

## Important Notes

### Session-Local Only

Settings are session-local and reset when:
- Session closes
- `RESET ALL;` is executed
- New connection is established

### Not for Production

**Never use this in application code:**
- ❌ Setting claims manually in app
- ❌ Bypassing Supabase Auth
- ✅ Only for testing and debugging

### Service Role Bypasses RLS

If using service role key, RLS is bypassed completely:
- Cannot test RLS with service role
- Must use authenticated role
- Service role sees ALL data

### Works with Functions

RLS policies respect these settings even in functions:

```sql
CREATE FUNCTION get_user_data() 
RETURNS TABLE(...)
LANGUAGE sql
SECURITY DEFINER  -- Function runs as owner
AS $$
  SELECT * FROM table_name;  -- Still respects RLS
$$;
```

---

## Exit Impersonation

To stop impersonating:

```sql
-- Reset all session variables
RESET ALL;

-- Or just close the psql session
\q
```

---

## Troubleshooting

### "auth.uid() returns NULL"

**Problem**: Claims not set correctly  
**Fix**: Verify claim format and role setting

```sql
-- Check current settings
SELECT 
  current_setting('request.jwt.claims', true),
  current_setting('role', true);
```

### "Still seeing all data"

**Problem**: Using service role or RLS not enabled  
**Fix**: 
1. Check connection string (should not be service role)
2. Verify RLS enabled: `*rls-audit`
3. Confirm policies exist

### "Permission denied"

**Problem**: Role not set to authenticated  
**Fix**: Ensure role is set:

```sql
SELECT set_config('role', 'authenticated', true);
```

---

## Integration with Workflow

Typical testing workflow:

1. Create/modify RLS policy
2. `*dry-run migration.sql` - Syntax check
3. `*apply-migration migration.sql` - Apply changes
4. `*impersonate {test_user_id}` - Test as user
5. Run test queries
6. `*impersonate {other_user_id}` - Test isolation
7. `*rls-audit` - Verify coverage

---

## Security Reminder

🔒 **This is a testing tool only**  

Never bypass Supabase Auth in production. Always use:
- Supabase client with user authentication
- Proper JWT tokens from auth.users
- Real user sessions with valid credentials


## Referência: references/squad/tasks/db-load-csv.md

# Task: Load CSV Data Safely

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/data-loader.sh` |
| **rationale** | COPY de CSV é operação determinística do PostgreSQL |

**Purpose**: Import CSV data using PostgreSQL COPY with staging table and validation

**Elicit**: true

---

## 🚀 NEW: Use Automated Data Loader (RECOMMENDED)

**Token Savings: 86% | Time Savings: ~82%**

```bash
# Load CSV with automatic staging and validation
./squads/db-sage/scripts/db-ops/data-loader.sh {table} {csv_file}

# Load with custom delimiter
./squads/db-sage/scripts/db-ops/data-loader.sh {table} {csv_file} --delimiter "|"

# Load with validation rules
./squads/db-sage/scripts/db-ops/data-loader.sh {table} {csv_file} --validate

# Dry-run mode (preview changes)
./squads/db-sage/scripts/db-ops/data-loader.sh {table} {csv_file} --dry-run

# Benefits:
#   - Automatic staging table creation
#   - Data validation and cleaning
#   - Duplicate detection
#   - Safe rollback on errors
#   - 86% token savings
```

**OR continue with manual CSV load below:**

---

## Inputs

- `table` (string): Target table name
- `csv_file` (string): Path to CSV file

---

## Process

### 1. Validate Inputs

Check file exists and table exists:

```bash
echo "Validating inputs..."

DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
test -n "$DB_URL" || {
  echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"
  exit 1
}

# Check CSV file exists
[ -f "{csv_file}" ] || {
  echo "❌ File not found: {csv_file}"
  exit 1
}

# Check table exists
psql "$DB_URL" -c \
"SELECT EXISTS (
  SELECT 1 FROM information_schema.tables
  WHERE table_schema = 'public' AND table_name = '{table}'
);" | grep -q t || {
  echo "❌ Table '{table}' not found"
  exit 1
}

# Count CSV rows
ROW_COUNT=$(wc -l < "{csv_file}" | tr -d ' ')
echo "✓ CSV file: {csv_file} ($ROW_COUNT rows)"
echo "✓ Target table: {table}"
```

### 2. Preview CSV Structure

Show first few rows:

```bash
echo "CSV Preview (first 5 rows):"
head -n 5 "{csv_file}"
echo ""
echo "Continue with import? (yes/no)"
read CONFIRM
[ "$CONFIRM" = "yes" ] || { echo "Aborted"; exit 0; }
```

### 3. Create Staging Table

Import to staging first for validation:

```bash
echo "Creating staging table..."

psql "$DB_URL" << 'EOF'
-- Create staging table with same structure as target
CREATE TEMP TABLE {table}_staging (LIKE {table} INCLUDING ALL);

-- Or if you need to define structure manually:
-- CREATE TEMP TABLE {table}_staging (
--   id TEXT,
--   name TEXT,
--   created_at TEXT
--   -- Define all columns as TEXT initially for flexible parsing
-- );

SELECT 'Staging table created' AS status;
EOF

echo "✓ Staging table ready"
```

### 4. COPY Data to Staging

Use PostgreSQL COPY command (fastest method):

```bash
echo "Loading CSV into staging table..."

# Method 1: Using psql \copy (client-side file)
psql "$DB_URL" << 'EOF'
\copy {table}_staging FROM '{csv_file}' WITH (
  FORMAT csv,
  HEADER true,
  DELIMITER ',',
  QUOTE '"',
  ESCAPE '"',
  NULL 'NULL'
);
EOF

# Method 2: Server-side COPY (if file is on server)
# COPY {table}_staging FROM '/path/to/file.csv' WITH (FORMAT csv, HEADER true);

echo "✓ Data loaded to staging"
```

### 5. Validate Data

Run validation checks before merging:

```bash
echo "Validating staged data..."

psql "$DB_URL" << 'EOF'
-- Check row count
SELECT COUNT(*) AS staged_rows FROM {table}_staging;

-- Check for NULL in required columns (example)
SELECT COUNT(*) AS null_ids
FROM {table}_staging
WHERE id IS NULL;

-- Check for duplicates (example)
SELECT id, COUNT(*) AS duplicates
FROM {table}_staging
GROUP BY id
HAVING COUNT(*) > 1;

-- Check data types can be converted (example)
SELECT
  COUNT(*) FILTER (WHERE created_at::timestamptz IS NULL) AS invalid_dates
FROM {table}_staging;

-- Any validation failures?
SELECT
  CASE
    WHEN EXISTS (SELECT 1 FROM {table}_staging WHERE id IS NULL) THEN
      'FAIL: NULL ids found'
    WHEN EXISTS (SELECT 1 FROM {table}_staging GROUP BY id HAVING COUNT(*) > 1) THEN
      'FAIL: Duplicate ids found'
    ELSE
      'PASS: All validations passed'
  END AS validation_status;
EOF

echo ""
echo "Review validation results above."
echo "Continue with merge? (yes/no)"
read CONFIRM
[ "$CONFIRM" = "yes" ] || { echo "Aborted - data in staging table for review"; exit 1; }
```

### 6. Merge to Target Table

Use UPSERT pattern for idempotency:

```bash
echo "Merging to target table..."

psql "$DB_URL" << 'EOF'
BEGIN;

-- Insert new rows or update existing (idempotent)
INSERT INTO {table} (id, name, created_at, ...)
SELECT
  id::uuid,                  -- Cast to proper types
  name,
  created_at::timestamptz,
  ...
FROM {table}_staging
ON CONFLICT (id) DO UPDATE SET
  name = EXCLUDED.name,
  created_at = EXCLUDED.created_at,
  updated_at = NOW();  -- Update timestamp

-- Get counts
SELECT
  (SELECT COUNT(*) FROM {table}) AS final_count,
  (SELECT COUNT(*) FROM {table}_staging) AS imported_count;

COMMIT;

SELECT 'Import complete' AS status;
EOF

echo "✓ Data merged successfully"
```

### 7. Cleanup

Drop staging table:

```bash
echo "Cleaning up..."

psql "$DB_URL" << 'EOF'
DROP TABLE IF EXISTS {table}_staging;
EOF

echo "✓ Cleanup complete"
```

---

## Output

Display import summary:

```
✅ CSV IMPORT COMPLETE

CSV File:       {csv_file}
Target Table:   {table}
Rows Imported:  {count}
Duration:       {duration}s

Validation:
✓ No NULL in required columns
✓ No duplicate keys
✓ All data types valid

Next steps:
- Verify data in database
- Run smoke tests if needed
- Update statistics: ANALYZE {table};
```

---

## Best Practices

### CSV Format Requirements

**Required:**
- UTF-8 encoding
- Consistent delimiters (comma recommended)
- Header row with column names
- Quoted strings if they contain delimiters

**Example:**
```csv
id,name,email,created_at
"user-1","John Doe","john@example.com","2024-01-01 00:00:00"
"user-2","Jane Smith","jane@example.com","2024-01-02 00:00:00"
```

### Handling Large Files

For CSV files > 100MB or > 1M rows:

1. **Split the file:**
```bash
split -l 100000 large.csv chunk_
```

2. **Import in batches:**
```bash
for file in chunk_*; do
  *load-csv {table} $file
done
```

3. **Or use streaming COPY:**
```bash
cat large.csv | psql "$DB_URL" -c \
  "COPY {table} FROM STDIN WITH (FORMAT csv, HEADER true);"
```

### Data Type Conversion

Always cast from TEXT to proper types in SELECT:

```sql
SELECT
  id::uuid,                    -- UUID
  amount::numeric(10,2),       -- Decimal
  created_at::timestamptz,     -- Timestamp
  is_active::boolean,          -- Boolean
  metadata::jsonb             -- JSON
FROM {table}_staging
```

---

## Common Issues

### Issue 1: Character Encoding

**Error:** `invalid byte sequence for encoding "UTF8"`

**Fix:**
```bash
# Convert to UTF-8
iconv -f ISO-8859-1 -t UTF-8 input.csv > output.csv
```

### Issue 2: Quote/Delimiter Conflicts

**Error:** `unterminated CSV quoted field`

**Fix:** Adjust COPY parameters:
```sql
COPY table FROM 'file.csv' WITH (
  DELIMITER ';',    -- Change delimiter
  QUOTE '''',       -- Change quote character
  ESCAPE '\'       -- Change escape character
);
```

### Issue 3: NULL Values

**Error:** `null value in column "id" violates not-null constraint`

**Fix:** Define NULL representation:
```sql
COPY table FROM 'file.csv' WITH (
  NULL 'NULL',      -- Treat literal "NULL" as NULL
  -- Or NULL ''     -- Treat empty strings as NULL
);
```

---

## Security Notes

- **Never** COPY from untrusted sources without validation
- Always use staging table first
- Validate data types and constraints before merging
- Check for SQL injection in CSV content (though COPY is safe)
- Consider row-level security (RLS) when loading to Supabase

---

## Performance Tips

1. **Disable triggers during bulk load:**
```sql
ALTER TABLE {table} DISABLE TRIGGER ALL;
-- Load data
ALTER TABLE {table} ENABLE TRIGGER ALL;
```

2. **Drop indexes, load, recreate:**
```sql
-- Only for initial loads, not updates!
DROP INDEX idx_name;
-- Load data
CREATE INDEX CONCURRENTLY idx_name ON {table}(column);
```

3. **Use UNLOGGED tables for staging:**
```sql
CREATE UNLOGGED TABLE {table}_staging (...);
-- Faster writes, but not crash-safe
```

4. **Batch commits:**
```sql
-- For very large loads
BEGIN;
COPY ... -- Load 100k rows
COMMIT;
BEGIN;
COPY ... -- Load next 100k rows
COMMIT;
```

---

## Alternative: INSERT from Application

For small datasets (<1000 rows), can use regular INSERT:

```javascript
// Supabase client example
const { data, error } = await supabase
  .from('table')
  .upsert(csvData, { onConflict: 'id' })
```

But COPY is **10-100x faster** for bulk loads!

---

## References

- [PostgreSQL COPY Documentation](https://www.postgresql.org/docs/current/sql-copy.html)
- [psql \copy Command](https://www.postgresql.org/docs/current/app-psql.html)


## Referência: references/squad/tasks/db-policy-apply.md

# Task: Apply RLS Policy Template

| Field | Value |
|-------|-------|
| **execution_type** | `Hybrid` |
| **pattern** | EXEC-HY-001 |
| **script** | `scripts/db-ops/rls-policy-installer.sh` |
| **rationale** | Worker aplica policy, Human DEVE confirmar (altera segurança) |

**Purpose**: Install KISS or granular RLS policies on a table

**Elicit**: true

---

## 🚀 NEW: Use Automated RLS Policy Installer (RECOMMENDED)

**Token Savings: 89% | Time Savings: ~85%**

```bash
# Use the rls-policy-installer script
./squads/db-sage/scripts/db-ops/rls-policy-installer.sh {table} {mode}

# Examples:
./squads/db-sage/scripts/db-ops/rls-policy-installer.sh minds kiss
./squads/db-sage/scripts/db-ops/rls-policy-installer.sh sources read-only
./squads/db-sage/scripts/db-ops/rls-policy-installer.sh fragments private

# Available modes: kiss, read-only, private, team, custom

# Benefits:
#   - Standardized policy templates
#   - Automatic testing after installation
#   - Safety checks for existing policies
#   - 89% token savings
```

**OR continue with manual policy installation below:**

---

## Inputs

- `table` (string): Table name to apply policy to
- `mode` (string): 'kiss' or 'granular' - policy type

---

## Process (Manual Method)

### 1. Validate Inputs

Check table exists and mode is valid:

```bash
echo "Validating inputs..."

DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
test -n "$DB_URL" || {
  echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"
  exit 1
}

# Check table exists
psql "$DB_URL" -c \
"SELECT EXISTS (
  SELECT 1 FROM information_schema.tables
  WHERE table_schema = 'public' AND table_name = '{table}'
);" | grep -q t || {
  echo "❌ Table '{table}' not found"
  exit 1
}

# Check mode
if [[ "{mode}" != "kiss" && "{mode}" != "granular" ]]; then
  echo "❌ Invalid mode: {mode}"
  echo "   Use 'kiss' or 'granular'"
  exit 1
fi

echo "✓ Table exists: {table}"
echo "✓ Mode: {mode}"
```

### 2. Check Existing Policies

Display current RLS status:

```bash
echo "Checking existing RLS policies..."

psql "$DB_URL" << EOF
SELECT
  schemaname,
  tablename,
  policyname,
  permissive,
  roles,
  cmd,
  qual,
  with_check
FROM pg_policies
WHERE tablename = '{table}';
EOF

echo ""
echo "RLS enabled on {table}?"
psql "$DB_URL" -c \
"SELECT relrowsecurity FROM pg_class WHERE relname = '{table}';" \
| grep -q t && echo "✓ Yes" || echo "⚠️  No (will be enabled)"
```

### 3. Ask User Confirmation

Present policy that will be applied based on mode:

**If mode = 'kiss':**
```
Will apply KISS policy to {table}:
- Enable RLS
- Single policy: users can only access their own rows
- Uses: (select auth.uid()) = user_id [PERFORMANCE OPTIMIZED]
- Applies to: SELECT, INSERT, UPDATE, DELETE

⚠️  CRITICAL PERFORMANCE NOTE:
Wrapping auth.uid() in SELECT provides 99.99% performance improvement
by allowing PostgreSQL to cache the function result.

Continue? (yes/no)
```

**If mode = 'granular':**
```
Will apply granular policies to {table}:
- Enable RLS
- Separate policies for each operation (SELECT, INSERT, UPDATE, DELETE)
- Fine-grained control
- Uses: auth.uid() = user_id

Continue? (yes/no)
```

Get confirmation before proceeding.

### 4. Generate Policy SQL

Based on mode, generate appropriate SQL:

**KISS Mode:**
```sql
-- Enable RLS
ALTER TABLE {table} ENABLE ROW LEVEL SECURITY;

-- Drop existing policies (if any)
DROP POLICY IF EXISTS "{table}_policy" ON {table};

-- Create single KISS policy (PERFORMANCE OPTIMIZED)
CREATE POLICY "{table}_policy"
  ON {table}
  FOR ALL
  TO authenticated
  USING (
    -- ✅ CRITICAL: Wrap auth.uid() in SELECT for 99.99% performance gain
    -- This allows PostgreSQL to cache the function result per statement
    (select auth.uid()) IS NOT NULL AND
    (select auth.uid()) = user_id
  )
  WITH CHECK (
    (select auth.uid()) IS NOT NULL AND
    (select auth.uid()) = user_id
  );

-- Add helpful comment
COMMENT ON POLICY "{table}_policy" ON {table} IS
  'KISS policy: users can only access their own rows (performance optimized with cached auth.uid())';
```

**Granular Mode (PERFORMANCE OPTIMIZED):**
```sql
-- Enable RLS
ALTER TABLE {table} ENABLE ROW LEVEL SECURITY;

-- Drop existing policies (if any)
DROP POLICY IF EXISTS "{table}_select" ON {table};
DROP POLICY IF EXISTS "{table}_insert" ON {table};
DROP POLICY IF EXISTS "{table}_update" ON {table};
DROP POLICY IF EXISTS "{table}_delete" ON {table};

-- SELECT: Users read own rows
-- ✅ Wrapping auth.uid() in SELECT provides 99.99% performance improvement
CREATE POLICY "{table}_select"
  ON {table}
  FOR SELECT
  TO authenticated
  USING (
    (select auth.uid()) IS NOT NULL AND
    (select auth.uid()) = user_id
  );

-- INSERT: Users create own rows
CREATE POLICY "{table}_insert"
  ON {table}
  FOR INSERT
  TO authenticated
  WITH CHECK (
    (select auth.uid()) IS NOT NULL AND
    (select auth.uid()) = user_id
  );

-- UPDATE: Users update own rows
CREATE POLICY "{table}_update"
  ON {table}
  FOR UPDATE
  TO authenticated
  USING (
    (select auth.uid()) IS NOT NULL AND
    (select auth.uid()) = user_id
  )
  WITH CHECK (
    (select auth.uid()) IS NOT NULL AND
    (select auth.uid()) = user_id
  );

-- DELETE: Users delete own rows
CREATE POLICY "{table}_delete"
  ON {table}
  FOR DELETE
  TO authenticated
  USING (
    (select auth.uid()) IS NOT NULL AND
    (select auth.uid()) = user_id
  );

-- Add helpful comments
COMMENT ON POLICY "{table}_select" ON {table} IS 'Users can read own rows (cached auth.uid())';
COMMENT ON POLICY "{table}_insert" ON {table} IS 'Users can insert own rows (cached auth.uid())';
COMMENT ON POLICY "{table}_update" ON {table} IS 'Users can update own rows (cached auth.uid())';
COMMENT ON POLICY "{table}_delete" ON {table} IS 'Users can delete own rows (cached auth.uid())';
```

### 5. Create Migration File

Save policy SQL to migration file:

```bash
TS=$(date +%Y%m%d%H%M%S)
MIGRATION_FILE="supabase/migrations/${TS}_rls_${mode}__{table}.sql"

mkdir -p supabase/migrations

cat > "$MIGRATION_FILE" << 'EOF'
-- Migration: Apply {mode} RLS policy to {table}
-- Generated: $(date -u +"%Y-%m-%d %H:%M:%S UTC")
-- Table: {table}
-- Mode: {mode}

BEGIN;

[... SQL from step 4 ...]

COMMIT;
EOF

echo "✓ Migration created: $MIGRATION_FILE"
```

### 6. Apply Migration

Use existing db-apply-migration task:

```bash
echo "Applying migration..."
# Execute db-apply-migration task internally
# (This will create snapshots, apply, verify)
```

### 7. Test Policies

Verify policies work correctly:

```bash
echo "Testing RLS policies..."

# Test 1: Anonymous user should see nothing
psql "$DB_URL" << EOF
SET ROLE anon;
SELECT COUNT(*) AS anon_count FROM {table};
RESET ROLE;
EOF

# Test 2: Authenticated user should see only their rows
# (Requires setting up test user - provide instructions)

echo ""
echo "✓ Policy tests complete"
echo "  ⚠️  Manual testing recommended:"
echo "    - Use *impersonate to test as specific user"
echo "    - Verify each operation (SELECT, INSERT, UPDATE, DELETE)"
```

---

## Output

Display summary:
```
✅ RLS POLICY APPLIED

Table:     {table}
Mode:      {mode}
Migration: supabase/migrations/{TS}_rls_{mode}__{table}.sql
Policies:  [list created policies]

Next steps:
1. Test policies manually: *impersonate {user_id}
2. Run RLS audit: *rls-audit
3. Update documentation
4. Commit migration to git
```

---

## Notes

### KISS vs Granular

**KISS** (Keep It Simple, Stupid):
- ✅ Single policy for all operations
- ✅ Easier to understand
- ✅ Less verbose
- ❌ Less flexible

**Granular**:
- ✅ Separate policies per operation
- ✅ Fine-grained control
- ✅ Can have different logic per operation
- ❌ More verbose

### Common Patterns

**Public Read, Authenticated Write (Performance Optimized):**
```sql
-- SELECT: Public
CREATE POLICY "{table}_select" ON {table}
  FOR SELECT TO public
  USING (true);

-- INSERT/UPDATE/DELETE: Authenticated users only
CREATE POLICY "{table}_write" ON {table}
  FOR ALL TO authenticated
  USING (
    (select auth.uid()) IS NOT NULL AND
    (select auth.uid()) = user_id
  )
  WITH CHECK (
    (select auth.uid()) IS NOT NULL AND
    (select auth.uid()) = user_id
  );
```

**Tenant-Based (Performance Optimized):**
```sql
CREATE POLICY "{table}_tenant" ON {table}
  FOR ALL TO authenticated
  USING (
    (select auth.uid()) IS NOT NULL AND
    tenant_id IN (
      SELECT tenant_id FROM user_tenants
      WHERE user_id = (select auth.uid())
    )
  );
```

### Performance Tips

**Critical Performance Optimization:**
Always wrap `auth.uid()` in a `SELECT` statement:
```sql
-- ❌ SLOW (99.99% slower)
USING (auth.uid() = user_id)

-- ✅ FAST (cached per statement)
USING ((select auth.uid()) = user_id)
```

**Why it matters:**
- Without SELECT: PostgreSQL calls `auth.uid()` for EVERY row
- With SELECT: PostgreSQL caches the result for the entire statement
- Performance improvement: **99.99%** (essentially 10,000x faster on large tables)

**Index Recommendations:**
- Always index columns used in policies (e.g., `user_id`, `tenant_id`)
- Example: `CREATE INDEX idx_{table}_user_id ON {table}(user_id);`
- Performance improvement: **99.94%** when combined with wrapped auth functions

---

## Security Warnings ⚠️

### CRITICAL: Do NOT Use raw_user_meta_data in Policies

```sql
-- ❌ DANGEROUS - User can modify this data!
CREATE POLICY "bad_policy" ON {table}
  USING (
    (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
  );
```

**Why dangerous:** `raw_user_meta_data` can be modified by the user through Supabase Auth client. An attacker can set `{ "role": "admin" }` and bypass security!

**Safe alternative:** Use `raw_app_meta_data` (server-only):
```sql
-- ✅ SAFE - Only server can modify app_metadata
CREATE POLICY "safe_policy" ON {table}
  USING (
    (auth.jwt() -> 'app_metadata' ->> 'role') = 'admin'
  );
```

### Auth NULL Check

Always check if user is authenticated:
```sql
-- ❌ Missing NULL check
USING (auth.uid() = user_id)  -- Fails silently for anon users

-- ✅ Explicit authentication check
USING (
  (select auth.uid()) IS NOT NULL AND
  (select auth.uid()) = user_id
)
```

### Policy Debugging

Enable RLS policies in SQL Editor (dev only):
```sql
-- Temporarily disable RLS for debugging (DANGEROUS - dev only!)
ALTER TABLE {table} DISABLE ROW LEVEL SECURITY;

-- Re-enable when done
ALTER TABLE {table} ENABLE ROW LEVEL SECURITY;
```

---

## Prerequisites

Table must have:
- `user_id UUID` column (for user-based policies)
- Or `tenant_id` column (for tenant-based policies)
- **Indexes on all policy filter columns** (critical for performance!)
  - `CREATE INDEX idx_{table}_user_id ON {table}(user_id);`

---

## Error Handling

If policy application fails:
1. Check table has required columns (user_id, etc.)
2. Verify auth.uid() is available (Supabase)
3. Check for existing policies with same names
4. Rollback migration if needed: `*rollback`


## Referência: references/squad/tasks/db-rls-audit.md

# Task: RLS Audit

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/rls-test-suite.sh` |
| **rationale** | Query de metadados pg_policies é determinística |

**Purpose**: Report tables with/without RLS and list all policies

**Elicit**: false

---

## 🚀 NEW: Use Automated RLS Test Suite (RECOMMENDED)

**Token Savings: 93% | Time Savings: ~85%**

```bash
# Test specific table with automated script
./squads/db-sage/scripts/db-ops/rls-test-suite.sh {table_name}

# Test all tables with RLS
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
for table in $(psql "$DB_URL" -t -A -c "SELECT tablename FROM pg_tables WHERE schemaname='public' AND rowsecurity=true"); do
  ./squads/db-sage/scripts/db-ops/rls-test-suite.sh $table
done

# Benefits:
#   - Automated multi-user testing
#   - Isolation verification
#   - Permission matrix generation
#   - 93% token savings
```

**OR continue with manual SQL audit below:**

---

## Process (Manual Method)

### Run Comprehensive RLS Audit

```bash
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
\echo '=== RLS Coverage Audit ==='
\echo ''

-- Tables with/without RLS
WITH t AS (
  SELECT tablename, rowsecurity
  FROM pg_tables WHERE schemaname='public'
)
SELECT
  tablename,
  CASE WHEN rowsecurity THEN '✓ ENABLED' ELSE '❌ DISABLED' END AS rls_status,
  (SELECT json_agg(json_build_object(
    'policy', policyname,
    'cmd', cmd,
    'roles', roles,
    'qual', qual,
    'with_check', with_check
  ))
   FROM pg_policies p 
   WHERE p.tablename=t.tablename 
   AND p.schemaname='public') AS policies
FROM t
ORDER BY rowsecurity DESC, tablename;

\echo ''
\echo '=== Summary ==='

SELECT 
  COUNT(*) AS total_tables,
  COUNT(*) FILTER (WHERE rowsecurity) AS rls_enabled,
  COUNT(*) FILTER (WHERE NOT rowsecurity) AS rls_disabled
FROM pg_tables 
WHERE schemaname='public';

\echo ''
\echo '=== Tables Without RLS (Security Risk) ==='

SELECT tablename 
FROM pg_tables 
WHERE schemaname='public' 
AND rowsecurity = false
ORDER BY tablename;

\echo ''
\echo '=== Policy Coverage ==='

SELECT 
  t.tablename,
  COUNT(p.policyname) AS policy_count,
  ARRAY_AGG(p.cmd) AS commands_covered
FROM pg_tables t
LEFT JOIN pg_policies p ON p.tablename = t.tablename AND p.schemaname = 'public'
WHERE t.schemaname = 'public'
AND t.rowsecurity = true
GROUP BY t.tablename
ORDER BY policy_count, t.tablename;

SQL
```

---

## Output Interpretation

### RLS Status

**✓ ENABLED** - Table has RLS active (good)  
**❌ DISABLED** - Table has no RLS (security risk)

### Policy Coverage

**Good coverage:**
- 1 policy with `FOR ALL` (KISS approach), OR
- 4 policies covering SELECT, INSERT, UPDATE, DELETE (granular)

**Incomplete coverage:**
- Enabled RLS but 0 policies = nobody can access
- 1-3 policies (granular) = some operations not covered

**No coverage:**
- RLS disabled = full access without restrictions

---

## Common Issues & Fixes

### Issue: Table has RLS but no policies

**Problem**: RLS enabled but no policies defined  
**Impact**: Table is inaccessible to all users  
**Fix**: Add policies or disable RLS

```sql
-- Add KISS policy
ALTER TABLE table_name ENABLE ROW LEVEL SECURITY;

CREATE POLICY "table_name_all"
ON table_name FOR ALL
TO authenticated
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);
```

Or use: `*policy-apply table_name kiss`

### Issue: Table has no RLS

**Problem**: Table accessible without restrictions  
**Impact**: Security vulnerability, data exposure  
**Fix**: Enable RLS and add policies

```sql
ALTER TABLE table_name ENABLE ROW LEVEL SECURITY;
-- Then add policies
```

### Issue: Incomplete policy coverage (granular)

**Problem**: RLS enabled with 1-3 policies (not covering all operations)  
**Impact**: Some operations may be blocked unexpectedly  
**Fix**: Either add missing policies or switch to KISS approach

---

## Recommended Actions

### For Public Data
Tables that should be publicly readable:

```sql
-- Public read, authenticated write
CREATE POLICY "public_read"
ON table_name FOR SELECT
TO anon, authenticated
USING (true);

CREATE POLICY "authenticated_write"
ON table_name FOR INSERT
TO authenticated
WITH CHECK (auth.uid() = user_id);
```

### For User-Owned Data
Use KISS policy:

```bash
*policy-apply table_name kiss
```

### For Multi-Tenant Data
Organization-scoped access:

```sql
CREATE POLICY "org_isolation"
ON table_name FOR ALL
TO authenticated
USING (org_id = (auth.jwt() ->> 'org_id')::uuid)
WITH CHECK (org_id = (auth.jwt() ->> 'org_id')::uuid);
```

---

## Testing RLS Policies

After fixing issues, test with:

```bash
*impersonate {user_id}
# Then run queries to verify access
```

---

## Best Practices

✅ **Enable RLS on all tables with sensitive data**  
✅ **Use KISS policies for simple owner-based access**  
✅ **Document why RLS is disabled if intentional**  
✅ **Test policies with real user contexts**  
✅ **Index columns used in RLS policies**  
✅ **Run this audit after every migration**

❌ **Don't enable RLS without policies**  
❌ **Don't use service role to bypass RLS in app code**  
❌ **Don't forget to test negative cases**

---

## Integration with Workflow

Run RLS audit:
1. After migrations: `*smoke-test` → `*rls-audit`
2. Before production deploy: `*rls-audit`
3. Regular security reviews: `*rls-audit`
4. When adding new tables: `*rls-audit`


## Referência: references/squad/tasks/db-rollback.md

# Task: Rollback Database

| Field | Value |
|-------|-------|
| **execution_type** | `Hybrid` |
| **pattern** | EXEC-HY-001 |
| **script** | `scripts/db-ops/backup-manager.sh` |
| **rationale** | Worker executa restore, Human DEVE confirmar antes (impacto crítico) |

**Purpose**: Restore database to previous snapshot or run rollback script

**Elicit**: true

---

## 🚀 NEW: Use Automated Backup Manager (RECOMMENDED)

**Token Savings: 88% | Time Savings: ~85%**

```bash
# Restore from latest snapshot
./squads/db-sage/scripts/db-ops/backup-manager.sh --restore latest

# Restore from specific snapshot
./squads/db-sage/scripts/db-ops/backup-manager.sh --restore {snapshot_id}

# List available snapshots
./squads/db-sage/scripts/db-ops/backup-manager.sh --list

# Restore with pre-rollback safety snapshot
./squads/db-sage/scripts/db-ops/backup-manager.sh --restore {snapshot_id} --safe

# Benefits:
#   - Automatic pre-rollback backup
#   - Schema integrity verification
#   - Data preservation checks
#   - Rollback of rollback capability
#   - 88% token savings
```

**OR continue with manual rollback below:**

---

## Inputs

- `target` (string): Path to snapshot file or rollback script

---

## Process

### 1. Confirm Rollback

**CRITICAL WARNING**: Display to user before proceeding

```
⚠️  DATABASE ROLLBACK WARNING ⚠️

You are about to restore the database to a previous state.

Target: {target}

This will:
  ✓ Drop and recreate all schema objects
  ✓ Preserve existing data (if schema-only snapshot)
  ✗ Lose any schema changes made after snapshot
  ✗ Potentially break application if schema incompatible

Are you ABSOLUTELY SURE you want to proceed?
```

Ask user to type: `ROLLBACK` to confirm

### 2. Pre-Rollback Safety Checks

```bash
# Create emergency snapshot before rollback
echo "Creating emergency snapshot before rollback..."
TS=$(date +%Y%m%d_%H%M%S)
EMERGENCY="supabase/snapshots/${TS}_emergency_before_rollback.sql"

pg_dump "$SUPABASE_DB_URL" \
  --schema-only \
  --clean \
  --if-exists \
  > "$EMERGENCY"

if [ $? -eq 0 ]; then
  echo "✓ Emergency snapshot: $EMERGENCY"
else
  echo "❌ Emergency snapshot failed - ABORTING ROLLBACK"
  exit 1
fi
```

### 3. Validate Rollback Target

```bash
TARGET="{target}"

# Check file exists
if [ ! -f "$TARGET" ]; then
  echo "❌ Rollback target not found: $TARGET"
  exit 1
fi

# Check file is valid SQL
if ! grep -q "CREATE\|DROP\|ALTER" "$TARGET"; then
  echo "❌ File doesn't appear to be valid SQL"
  exit 1
fi

echo "✓ Rollback target validated: $TARGET"
echo "  File size: $(ls -lh "$TARGET" | awk '{print $5}')"
echo "  Modified: $(ls -lh "$TARGET" | awk '{print $6, $7, $8}')"
```

### 4. Acquire Exclusive Lock

Prevent concurrent operations:

```bash
echo "Acquiring exclusive lock..."

psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -c \
"SELECT pg_try_advisory_lock(hashtext('dbsage:rollback')) AS got" \
| grep -q t || { echo "❌ Another operation is running"; exit 1; }

echo "✓ Lock acquired"
```

### 5. Execute Rollback

```bash
echo ""
echo "=== EXECUTING ROLLBACK ==="
echo "Started: $(date -Iseconds)"
echo ""

# Run rollback in single transaction
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -f "$TARGET"

RESULT=$?

echo ""
echo "Completed: $(date -Iseconds)"
echo ""

if [ $RESULT -eq 0 ]; then
  echo "✅ ROLLBACK SUCCESSFUL"
else
  echo "❌ ROLLBACK FAILED"
  echo "Emergency snapshot available: $EMERGENCY"
  echo "Attempting to restore from emergency snapshot..."
  
  # Try to restore emergency snapshot
  psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -f "$EMERGENCY"
  
  if [ $? -eq 0 ]; then
    echo "✓ Restored from emergency snapshot"
  else
    echo "❌ Emergency restore also failed - DATABASE MAY BE INCONSISTENT"
    echo "Manual intervention required"
  fi
  
  exit 1
fi
```

### 6. Post-Rollback Validation

```bash
echo ""
echo "=== POST-ROLLBACK VALIDATION ==="
echo ""

# Count schema objects
echo "Schema object counts:"
psql "$SUPABASE_DB_URL" -t -c \
"SELECT 
  (SELECT COUNT(*) FROM pg_tables WHERE schemaname='public') AS tables,
  (SELECT COUNT(*) FROM pg_policies WHERE schemaname='public') AS policies,
  (SELECT COUNT(*) FROM pg_proc WHERE pronamespace='public'::regnamespace) AS functions;"

# Check for basic sanity
echo ""
echo "Quick sanity checks:"
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 <<'SQL'
-- Check tables exist
SELECT 'Tables exist' AS check, COUNT(*) > 0 AS pass 
FROM pg_tables WHERE schemaname='public';

-- Check functions exist  
SELECT 'Functions exist' AS check, COUNT(*) > 0 AS pass
FROM pg_proc WHERE pronamespace='public'::regnamespace;

-- Check for orphaned objects (optional)
-- SELECT 'No orphaned triggers' AS check, COUNT(*) = 0 AS pass
-- FROM pg_trigger WHERE tgrelid NOT IN (SELECT oid FROM pg_class);
SQL
```

### 7. Release Lock & Create Post-Rollback Snapshot

```bash
# Release lock
psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -c \
"SELECT pg_advisory_unlock(hashtext('dbsage:rollback'));"

echo "✓ Lock released"

# Create post-rollback snapshot
POST_SNAPSHOT="supabase/snapshots/${TS}_post_rollback.sql"
pg_dump "$SUPABASE_DB_URL" --schema-only --clean --if-exists > "$POST_SNAPSHOT"

echo "✓ Post-rollback snapshot: $POST_SNAPSHOT"
```

### 8. Report Results

```
✅ DATABASE ROLLBACK COMPLETED

Rolled back to: {target}
Timestamp: {TS}

Snapshots created:
  - Emergency (before): $EMERGENCY
  - Post-rollback (after): $POST_SNAPSHOT

Next steps:
  1. *smoke-test - Validate schema
  2. *rls-audit - Check security
  3. Test application functionality
  4. Monitor for issues

If issues detected:
  *rollback $EMERGENCY  # Restore to pre-rollback state
```

---

## Rollback Strategies

### Strategy 1: Snapshot Restore (Recommended)

**Use when**: Reverting schema changes

```bash
*rollback supabase/snapshots/20251026_pre_migration.sql
```

**Pros**:
- ✅ Fast
- ✅ Complete schema state
- ✅ Tested with pg_dump

**Cons**:
- ❌ Data preserved (may be incompatible)
- ❌ Requires prior snapshot

### Strategy 2: Explicit Rollback Script

**Use when**: Surgical changes to specific objects

```sql
-- supabase/rollback/20251026_rollback_user_roles.sql

BEGIN;

-- Undo changes in reverse order
DROP TRIGGER IF EXISTS set_user_role_timestamp ON user_roles;
DROP FUNCTION IF EXISTS update_user_role_timestamp();
DROP TABLE IF EXISTS user_roles;

-- Restore previous state if needed
-- ...

COMMIT;
```

```bash
*rollback supabase/rollback/20251026_rollback_user_roles.sql
```

**Pros**:
- ✅ Precise control
- ✅ Documented undo process
- ✅ Can be tested

**Cons**:
- ❌ Must write manually
- ❌ Easy to forget steps
- ❌ Must maintain with migration

### Strategy 3: Forward Fix

**Use when**: Rollback is dangerous, fix forward instead

```sql
-- Instead of rolling back, apply corrective migration
-- migration: 20251026_fix_user_roles_bug.sql
```

**Pros**:
- ✅ No data loss risk
- ✅ Maintains history
- ✅ Safe in production

**Cons**:
- ❌ More work
- ❌ Leaves intermediate state in history

---

## Rollback Decision Matrix

| Situation | Strategy | Command |
|-----------|----------|---------|
| Migration failed mid-way | Restore snapshot | `*rollback snapshot_before.sql` |
| Schema breaks app | Restore snapshot | `*rollback snapshot_before.sql` |
| Wrong migration applied | Restore snapshot | `*rollback snapshot_before.sql` |
| Minor bug in function | Forward fix | Create fix migration |
| Data corruption risk | Forward fix | Don't rollback |
| Production with users | Forward fix | Avoid schema rollback |

---

## Safety Checklist

Before executing rollback:

- [ ] Emergency snapshot created automatically ✓
- [ ] Application stopped or in maintenance mode
- [ ] Users notified of downtime
- [ ] Team aware of rollback operation
- [ ] Rollback target validated
- [ ] Exclusive lock acquired
- [ ] Post-rollback test plan ready

---

## Rollback in Different Environments

### Development
```bash
# Fast and loose - just do it
*rollback snapshot.sql
```

### Staging
```bash
# Test the rollback process
*rollback snapshot.sql
*smoke-test
# Test app functionality
```

### Production
```bash
# CAREFUL - follow full checklist
# 1. Notify stakeholders
# 2. Enable maintenance mode
# 3. Create emergency snapshot (automatic)
# 4. Coordinate with team
*rollback snapshot.sql
# 5. Validation
*smoke-test
*rls-audit
# 6. Test critical flows
# 7. Disable maintenance mode
# 8. Monitor closely
```

---

## Common Rollback Scenarios

### Scenario 1: Migration Failed During Apply

**Situation**: `*apply-migration` failed halfway

**Action**: PostgreSQL already rolled back transaction ✓

**No rollback needed**: Database unchanged

**Next steps**:
1. Fix migration file
2. `*dry-run` to test
3. `*apply-migration` again

### Scenario 2: Migration Succeeded but Breaks App

**Situation**: Schema change incompatible with application

**Action**: Rollback to pre-migration snapshot

```bash
*rollback supabase/snapshots/20251026_143022_pre_migration.sql
*smoke-test
# Deploy previous app version or fix app
```

### Scenario 3: Wrong Migration Applied

**Situation**: Applied v1.3.0 migration instead of v1.2.5

**Action**: Rollback to last known good state

```bash
*rollback supabase/snapshots/20251026_120000_v1_2_4.sql
*smoke-test
# Apply correct migration
*apply-migration v1_2_5.sql
```

### Scenario 4: Data Corruption After Migration

**Situation**: Schema change caused data integrity issues

**Action**: DON'T rollback schema - fix data

```sql
-- Forward fix with data correction
BEGIN;

-- Fix data
UPDATE users SET status = 'active' WHERE status IS NULL;

-- Add constraint to prevent recurrence
ALTER TABLE users ADD CONSTRAINT status_not_null CHECK (status IS NOT NULL);

COMMIT;
```

---

## Troubleshooting

### "Rollback failed: relation already exists"

**Problem**: Objects from new schema still exist  
**Fix**: Snapshot should have `DROP ... IF EXISTS` statements

Check snapshot file:
```bash
grep -c "DROP.*IF EXISTS" snapshot.sql
```

If missing, regenerate snapshot with `--clean --if-exists` flags.

### "Rollback succeeded but app still broken"

**Problem**: Application incompatible with rolled-back schema  
**Solutions**:
1. Deploy previous app version
2. Fix app code to work with old schema
3. Roll forward with new migration instead

### "Emergency snapshot failed during rollback"

**Problem**: Cannot create safety snapshot  
**Action**: ABORT ROLLBACK

```
❌ ROLLBACK ABORTED
Cannot proceed without emergency snapshot
Check database connectivity and disk space
```

### "Rollback created orphaned objects"

**Problem**: Some objects not cleaned up  
**Fix**: Manually identify and remove

```sql
-- Find orphaned triggers
SELECT tgname FROM pg_trigger 
WHERE tgrelid NOT IN (SELECT oid FROM pg_class);

-- Find orphaned indexes
SELECT indexname FROM pg_indexes 
WHERE tablename NOT IN (SELECT tablename FROM pg_tables);
```

---

## Best Practices

### DO

- ✅ Always snapshot before rollback (automatic)
- ✅ Test rollback in staging first
- ✅ Coordinate with team
- ✅ Have post-rollback test plan
- ✅ Monitor application after rollback
- ✅ Document why rollback was needed

### DON'T

- ❌ Rollback in production without coordination
- ❌ Rollback without emergency snapshot
- ❌ Rollback when forward fix is safer
- ❌ Rollback if data corruption risk
- ❌ Rollback during peak usage times
- ❌ Rollback without understanding impact

---

## Zero-Downtime Alternatives

Instead of rollback, consider:

### Blue-Green Deployment
- Keep old schema running
- Deploy new app + schema separately
- Switch traffic when ready
- Rollback = switch back

### Feature Flags
- Deploy schema changes
- Keep old code paths active
- Toggle features via flags
- Rollback = flip flag

### Backward Compatible Migrations
- Add new columns as nullable
- Keep old columns temporarily
- Remove old columns in later migration
- Rollback = just remove new columns

---

## Rollback Metrics

Track these after rollback:

- **Rollback duration**: How long did it take?
- **Downtime**: How long was app unavailable?
- **Data loss**: Any data lost? (should be none)
- **Schema object count**: Before vs after
- **Application errors**: Any post-rollback issues?
- **Recovery time**: Time to full functionality

```bash
# Log rollback event
echo "$(date -Iseconds) | ROLLBACK | $TARGET | Duration: ${DURATION}s" \
  >> supabase/rollback/rollback.log
```

---

## Related Commands

- `*snapshot {label}` - Create rollback point
- `*apply-migration {path}` - Creates automatic snapshots
- `*smoke-test` - Validate after rollback
- `*rls-audit` - Check security after rollback

---

## Emergency Contacts

If rollback fails critically:

1. **Check emergency snapshot**: `$EMERGENCY`
2. **Review Supabase dashboard**: Check for locks/issues
3. **Contact team**: Get help immediately
4. **Document state**: Save logs and error messages
5. **Consider Supabase restore**: Point-in-time recovery

**Never panic**: Emergency snapshot has your back.


## Referência: references/squad/tasks/db-run-sql.md

# Task: Run SQL

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/query-runner.sh` |
| **rationale** | Execução de SQL é 100% determinística |

**Purpose**: Execute SQL file or inline SQL with transaction safety and timing

**Elicit**: true

---

## 🚀 NEW: Use Automated Query Runner (RECOMMENDED)

**Token Savings: 85% | Time Savings: ~80%**

```bash
# Execute SQL file with transaction safety
./squads/db-sage/scripts/db-ops/query-runner.sh --file {sql_file}

# Execute inline SQL
./squads/db-sage/scripts/db-ops/query-runner.sh --sql "{sql_statement}"

# Execute with timeout (automatically cancel if exceeds)
./squads/db-sage/scripts/db-ops/query-runner.sh --file {sql_file} --timeout 30

# Execute with dry-run (rollback after execution)
./squads/db-sage/scripts/db-ops/query-runner.sh --file {sql_file} --dry-run

# Benefits:
#   - Automatic timeout protection
#   - Transaction safety
#   - Execution timing
#   - Error handling with context
#   - 85% token savings
```

**OR continue with manual SQL execution below:**

---

## Inputs

- `sql` (string): Either a file path or inline SQL statement

---

## Process

### 1. Determine Input Type

Check if input is file or inline SQL:

```bash
if [ -f "{sql}" ]; then
  echo "Mode: File"
  SQL_FILE="{sql}"
  SQL_MODE="file"
else
  echo "Mode: Inline SQL"
  SQL_MODE="inline"
  SQL_CONTENT="{sql}"
fi
```

### 2. Preview SQL

Show what will be executed:

```bash
echo "=========================================="
echo "SQL TO BE EXECUTED:"
echo "=========================================="

if [ "$SQL_MODE" = "file" ]; then
  cat "$SQL_FILE"
else
  echo "$SQL_CONTENT"
fi

echo ""
echo "=========================================="
```

### 3. Safety Checks

Warn about dangerous operations:

```bash
# Check for destructive operations
DANGEROUS_PATTERNS="DROP TABLE|TRUNCATE|DELETE FROM.*WHERE.*1=1|UPDATE.*WHERE.*1=1"

if echo "$SQL_CONTENT" | grep -Eiq "$DANGEROUS_PATTERNS"; then
  echo "⚠️  WARNING: Potentially destructive operation detected!"
  echo ""
  echo "Detected patterns:"
  echo "$SQL_CONTENT" | grep -Ei "$DANGEROUS_PATTERNS"
  echo ""
  echo "Database: [configured via SUPABASE_DB_URL or DATABASE_URL]"
  echo ""
  echo "Continue? Type 'I UNDERSTAND THE RISKS' to proceed:"
  read CONFIRM
  [ "$CONFIRM" = "I UNDERSTAND THE RISKS" ] || { echo "Aborted"; exit 1; }
fi
```

### 4. Transaction Mode Selection

Ask user about transaction handling:

```
Transaction mode:
1. auto   - Wrap in BEGIN/COMMIT (safe, rolls back on error)
2. manual - Execute as-is (file may have own transaction control)
3. read   - Read-only transaction (safe for queries)

Select mode (1/2/3):
```

### 5. Execute SQL

Run with selected transaction mode and timing:

```bash
echo "Executing SQL..."
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
test -n "$DB_URL" || { echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"; exit 1; }

if [ "$TRANSACTION_MODE" = "auto" ]; then
  # Wrapped transaction
  (
    echo "BEGIN;"
    if [ "$SQL_MODE" = "file" ]; then
      cat "$SQL_FILE"
    else
      echo "$SQL_CONTENT"
    fi
    echo "COMMIT;"
  ) | psql "$DB_URL" \
      -v ON_ERROR_STOP=1 \
      --echo-errors \
      2>&1 | tee /tmp/dbsage_sql_output.txt

elif [ "$TRANSACTION_MODE" = "read" ]; then
  # Read-only transaction
  (
    echo "BEGIN TRANSACTION READ ONLY;"
    if [ "$SQL_MODE" = "file" ]; then
      cat "$SQL_FILE"
    else
      echo "$SQL_CONTENT"
    fi
    echo "COMMIT;"
  ) | psql "$DB_URL" \
      -v ON_ERROR_STOP=1 \
      2>&1 | tee /tmp/dbsage_sql_output.txt

else
  # Manual mode (no wrapper)
  if [ "$SQL_MODE" = "file" ]; then
    psql "$DB_URL" \
      -v ON_ERROR_STOP=1 \
      -f "$SQL_FILE" \
      2>&1 | tee /tmp/dbsage_sql_output.txt
  else
    psql "$DB_URL" \
      -v ON_ERROR_STOP=1 \
      -c "$SQL_CONTENT" \
      2>&1 | tee /tmp/dbsage_sql_output.txt
  fi
fi

EXIT_CODE=$?
```

### 6. Check Results

Display execution summary:

```bash
echo ""
echo "=========================================="
echo "EXECUTION SUMMARY"
echo "=========================================="

if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ SUCCESS"
else
  echo "❌ FAILED (Exit code: $EXIT_CODE)"
  echo ""
  echo "Error output saved to: /tmp/dbsage_sql_output.txt"
  exit $EXIT_CODE
fi

# Count affected rows (if available in output)
ROWS_AFFECTED=$(grep -oP 'INSERT 0 \K\d+|UPDATE \K\d+|DELETE \K\d+' /tmp/dbsage_sql_output.txt | head -1)
if [ -n "$ROWS_AFFECTED" ]; then
  echo "Rows affected: $ROWS_AFFECTED"
fi

# Execution time (if using \timing in psql)
EXEC_TIME=$(grep -oP 'Time: \K[\d.]+' /tmp/dbsage_sql_output.txt | tail -1)
if [ -n "$EXEC_TIME" ]; then
  echo "Execution time: ${EXEC_TIME}ms"
fi
```

---

## Output

Display final summary:

```
✅ SQL EXECUTED SUCCESSFULLY

Mode:           {file|inline}
Transaction:    {auto|manual|read}
Rows affected:  {count}
Duration:       {time}ms

Output saved to: /tmp/dbsage_sql_output.txt

Next steps:
- Verify results in database
- Check for expected side effects
- Update application if schema changed
```

---

## Usage Examples

### Example 1: Run SQL File

```bash
*run-sql supabase/migrations/20240101_add_users.sql
```

### Example 2: Inline Query

```bash
*run-sql "SELECT COUNT(*) FROM users WHERE created_at > NOW() - INTERVAL '7 days'"
```

### Example 3: Multi-Line Inline

```bash
*run-sql "
  UPDATE users
  SET last_login = NOW()
  WHERE id = 'user-123'
  RETURNING *;
"
```

### Example 4: Complex Script

```bash
*run-sql "
  DO $$
  DECLARE
    user_count INTEGER;
  BEGIN
    SELECT COUNT(*) INTO user_count FROM users;
    RAISE NOTICE 'Total users: %', user_count;
  END $$;
"
```

---

## Safety Features

### 1. Destructive Operation Detection

Automatically warns for:
- `DROP TABLE`
- `TRUNCATE`
- `DELETE FROM ... WHERE 1=1`
- `UPDATE ... WHERE 1=1`

### 2. Transaction Modes

**Auto Mode (Recommended):**
- Wraps SQL in BEGIN/COMMIT
- Automatic rollback on error
- Safe for modifications

**Manual Mode:**
- For files with own transaction control
- Use when script has multiple transactions
- More control, less safety

**Read Mode:**
- Read-only transaction
- Cannot modify data
- Safe for queries/exploration

### 3. Error Handling

- `ON_ERROR_STOP=1` stops on first error
- Transaction rolls back on error (auto mode)
- Full error output preserved

---

## Advanced Options

### Enable Timing

```bash
# Add timing to all queries
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
psql "$DB_URL" << 'EOF'
\timing on
{your_sql_here}
EOF
```

### Verbose Output

```bash
# Show all SQL commands
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
psql "$DB_URL" --echo-all -f script.sql
```

### Save Output to File

```bash
# Redirect output
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
psql "$DB_URL" -f script.sql > output.txt 2>&1
```

### Interactive Mode

```bash
# Drop into psql shell
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
psql "$DB_URL"
```

---

## Common SQL Operations

### 1. Query Data

```sql
SELECT
  id,
  email,
  created_at
FROM users
WHERE created_at > NOW() - INTERVAL '1 day'
ORDER BY created_at DESC
LIMIT 10;
```

### 2. Update Records

```sql
UPDATE users
SET
  last_login = NOW(),
  login_count = login_count + 1
WHERE id = 'user-123'
RETURNING *;
```

### 3. Bulk Operations

```sql
-- Update all inactive users
UPDATE users
SET status = 'archived'
WHERE last_login < NOW() - INTERVAL '1 year'
  AND status = 'active';
```

### 4. Data Analysis

```sql
-- Aggregation query
SELECT
  DATE_TRUNC('day', created_at) AS day,
  COUNT(*) AS new_users,
  COUNT(*) FILTER (WHERE email_verified) AS verified
FROM users
WHERE created_at > NOW() - INTERVAL '30 days'
GROUP BY day
ORDER BY day DESC;
```

---

## psql Meta-Commands

Useful commands when in psql interactive mode:

```
\dt              -- List tables
\d table_name    -- Describe table
\df              -- List functions
\dv              -- List views
\l               -- List databases
\c database      -- Connect to database
\timing on       -- Enable query timing
\x on            -- Expanded display mode
\q               -- Quit
\?               -- Help
```

---

## Error Handling

If execution fails:

1. Check error message in output
2. Review SQL syntax
3. Verify table/column names exist
4. Check permissions
5. For transaction errors, check constraints

Common errors:

- **Syntax error:** Review SQL syntax
- **Relation does not exist:** Table/view not found
- **Column does not exist:** Typo in column name
- **Permission denied:** Need appropriate role/permissions

---

## Security Notes

- **Never** run untrusted SQL
- Always review SQL before executing
- Use read-only mode for untrusted queries
- Be careful with dynamic SQL
- Consider using prepared statements for user input

---

## References

- [PostgreSQL psql Documentation](https://www.postgresql.org/docs/current/app-psql.html)
- [PostgreSQL SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)


## Referência: references/squad/tasks/db-seed.md

# Task: Apply Seed Data

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/data-loader.sh` |
| **rationale** | INSERT de seed data é operação determinística |

**Purpose**: Safely apply seed data to database with idempotent operations

**Elicit**: true

---

## 🚀 NEW: Use Automated Data Loader (RECOMMENDED)

**Token Savings: 87% | Time Savings: ~83%**

```bash
# Apply seed data with idempotency checks
./squads/db-sage/scripts/db-ops/data-loader.sh --seed {path}

# Apply seed with validation
./squads/db-sage/scripts/db-ops/data-loader.sh --seed {path} --validate

# Dry-run mode (preview without applying)
./squads/db-sage/scripts/db-ops/data-loader.sh --seed {path} --dry-run

# Apply to specific environment
./squads/db-sage/scripts/db-ops/data-loader.sh --seed {path} --env production

# Benefits:
#   - Automatic idempotency validation
#   - Environment safety checks
#   - Conflict detection and resolution
#   - Rollback on errors
#   - 87% token savings
```

**OR continue with manual seed application below:**

---

## Inputs

- `path` (string): Path to SQL seed file

---

## Process

### 1. Pre-Flight Checks

Ask user to confirm:
- Seed file: `{path}`
- Database: active `SUPABASE_DB_URL` or `DATABASE_URL` (redacted)
- Environment: (dev/staging/production)
- Idempotent? (uses INSERT...ON CONFLICT or similar)

**CRITICAL**: Never seed production without explicit confirmation!

### 2. Validate Seed File

Check that seed file is idempotent:

```bash
echo "Validating seed file..."

DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
test -n "$DB_URL" || {
  echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"
  exit 1
}

# Check for dangerous patterns
if grep -qi "TRUNCATE\|DELETE FROM" {path}; then
  echo "⚠️  WARNING: Seed contains TRUNCATE/DELETE"
  echo "   This is destructive. Continue? (yes/no)"
  read CONFIRM
  [ "$CONFIRM" != "yes" ] && { echo "Aborted"; exit 1; }
fi

# Check for INSERT...ON CONFLICT (idempotent pattern)
if ! grep -qi "ON CONFLICT" {path}; then
  echo "⚠️  WARNING: No ON CONFLICT detected"
  echo "   Seed may not be idempotent. Continue? (yes/no)"
  read CONFIRM
  [ "$CONFIRM" != "yes" ] && { echo "Aborted"; exit 1; }
fi

echo "✓ Seed file validated"
```

### 3. Create Snapshot (Optional but Recommended)

```bash
TS=$(date +%Y%m%d%H%M%S)
mkdir -p supabase/snapshots

echo "Creating pre-seed snapshot..."
pg_dump "$DB_URL" --schema-only --clean --if-exists \
  > "supabase/snapshots/${TS}_before_seed.sql"

echo "✓ Snapshot: supabase/snapshots/${TS}_before_seed.sql"
```

### 4. Apply Seed Data

Run seed in transaction with error handling:

```bash
echo "Applying seed data..."

psql "$DB_URL" \
  -v ON_ERROR_STOP=1 \
  -f {path}

if [ $? -eq 0 ]; then
  echo "✓ Seed data applied successfully"
else
  echo "❌ Seed failed"
  echo "   Rollback snapshot: supabase/snapshots/${TS}_before_seed.sql"
  exit 1
fi
```

### 5. Verify Seed Data

Run basic verification:

```bash
echo "Verifying seed data..."

# Count inserted rows (example - customize per seed)
psql "$DB_URL" -c \
"SELECT
  'users' AS table, COUNT(*) AS rows FROM users
UNION ALL
SELECT
  'categories', COUNT(*) FROM categories
ORDER BY table;"

echo "✓ Verification complete"
```

### 6. Document Seed

Log what was seeded:

```bash
cat >> supabase/docs/SEED_LOG.md << EOF

## Seed Applied: ${TS}
- File: {path}
- Date: $(date -u +"%Y-%m-%d %H:%M:%S UTC")
- Environment: ${ENVIRONMENT:-unknown}
- Applied by: ${USER:-unknown}

EOF

echo "✓ Logged to supabase/docs/SEED_LOG.md"
```

---

## Output

Display summary:
```
✅ SEED COMPLETE

File:      {path}
Timestamp: {TS}
Snapshot:  supabase/snapshots/{TS}_before_seed.sql
Log:       supabase/docs/SEED_LOG.md

Next steps:
- Verify data manually in database
- Run smoke tests if appropriate
- Commit seed file to git
```

---

## Idempotent Seed Pattern

Best practice example for seed files:

```sql
-- ✅ GOOD: Idempotent seed
INSERT INTO categories (id, name, slug)
VALUES
  ('cat-1', 'Technology', 'technology'),
  ('cat-2', 'Design', 'design')
ON CONFLICT (id) DO UPDATE SET
  name = EXCLUDED.name,
  slug = EXCLUDED.slug;

-- ✅ GOOD: Conditional insert
INSERT INTO users (id, email, role)
SELECT 'user-1', 'admin@example.com', 'admin'
WHERE NOT EXISTS (
  SELECT 1 FROM users WHERE email = 'admin@example.com'
);

-- ❌ BAD: Not idempotent
INSERT INTO categories (name, slug)
VALUES ('Technology', 'technology');  -- Will fail on retry
```

---

## Error Handling

If seed fails:
1. Check error message in terminal
2. Fix seed file
3. Restore snapshot if needed: `*rollback {TS}_before_seed`
4. Re-run seed: `*seed {path}`

---

## Notes

- Seeds should be idempotent (safe to run multiple times)
- Use `ON CONFLICT` or `INSERT...WHERE NOT EXISTS`
- Never TRUNCATE in production seeds
- Test seeds in dev/staging first
- Version seed files in git (supabase/seeds/)


## Referência: references/squad/tasks/db-smoke-test.md

# Task: DB Smoke Test

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/health-checker.sh` |
| **rationale** | Smoke tests são queries determinísticas de validação |

**Purpose**: Run post-migration validation checks

**Elicit**: false

---

## 🚀 NEW: Use Automated Health Checker (RECOMMENDED)

**Token Savings: 89% | Time Savings: ~85%**

```bash
# Run comprehensive smoke tests
./squads/db-sage/scripts/db-ops/health-checker.sh --smoke-test

# Smoke tests with verbose logging
./squads/db-sage/scripts/db-ops/health-checker.sh --smoke-test --verbose

# Benefits:
#   - Automatic table/view/function validation
#   - RLS policy verification
#   - Index integrity checks
#   - Foreign key validation
#   - 89% token savings
```

**OR continue with manual smoke test below:**

---

## Process

### 1. Locate Smoke Test File

Check for smoke test in this order:

1. `supabase/tests/smoke/v_current.sql` (project-specific)
2. `supabase/tests/smoke_test.sql` (project-specific)
3. `squads/db-sage/templates/migration.sql.tmpl` (template fallback)

### 2. Run Smoke Test

```bash
SMOKE_TEST=""
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
test -n "$DB_URL" || { echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"; exit 1; }

if [ -f "supabase/tests/smoke/v_current.sql" ]; then
  SMOKE_TEST="supabase/tests/smoke/v_current.sql"
elif [ -f "supabase/tests/smoke_test.sql" ]; then
  SMOKE_TEST="supabase/tests/smoke_test.sql"
elif [ -f "squads/db-sage/templates/migration.sql.tmpl" ]; then
  SMOKE_TEST="squads/db-sage/templates/migration.sql.tmpl"
else
  echo "❌ No smoke test file found"
  exit 1
fi

echo "Running smoke test: $SMOKE_TEST"
psql "$DB_URL" -v ON_ERROR_STOP=1 -f "$SMOKE_TEST"
```

### 3. Report Results

**If successful:**
```
✅ Smoke Test Passed

Checks completed:
  ✓ Table count validation
  ✓ Policy count validation
  ✓ Function existence checks
  ✓ Basic query sanity
```

**If failed:**
```
❌ Smoke Test Failed

Review errors above and:
  1. Check migration completeness
  2. Verify RLS policies installed
  3. Confirm functions created
  4. Consider rollback if critical
```

---

## What Is Tested

Basic smoke tests typically check:

### Schema Objects
- Expected tables exist
- Expected views exist
- Expected functions exist
- Expected triggers exist

### RLS Coverage
- RLS enabled on sensitive tables
- Policies exist and are named correctly
- Basic RLS queries don't error

### Data Integrity
- Foreign keys valid
- Check constraints valid
- Sample queries return expected results

### Performance
- Basic queries complete in reasonable time
- No missing indexes on FKs

---

## Creating Custom Smoke Tests

Create `supabase/tests/smoke/v_X_Y_Z.sql`:

```sql
-- Smoke Test for v1.2.0
SET client_min_messages = warning;

-- Table count
SELECT COUNT(*) AS tables FROM information_schema.tables 
WHERE table_schema='public';
-- Expected: 15

-- RLS enabled
SELECT tablename FROM pg_tables 
WHERE schemaname='public' AND rowsecurity = false;
-- Expected: empty (all tables have RLS)

-- Critical functions exist
SELECT proname FROM pg_proc 
WHERE pronamespace = 'public'::regnamespace
AND proname IN ('function1', 'function2');
-- Expected: 2 rows

-- Sample data query
SELECT COUNT(*) FROM users WHERE deleted_at IS NULL;
-- Expected: > 0

-- RLS sanity (doesn't error)
SET LOCAL request.jwt.claims = '{"sub":"00000000-0000-0000-0000-000000000000","role":"authenticated"}';
SELECT 1 FROM protected_table LIMIT 1;
```

---

## Best Practices

1. **Version-specific tests** - Name by schema version
2. **Fast execution** - Under 5 seconds
3. **No side effects** - Read-only queries
4. **Clear expectations** - Document expected results
5. **Fail fast** - Use ON_ERROR_STOP

---

## Next Steps After Pass

✓ Migration validated  
→ Update migration log  
→ Run RLS audit: `*rls-audit`  
→ Check performance: `*analyze-hotpaths`

## Next Steps After Fail

❌ Migration issues detected  
→ Review errors  
→ Consider rollback: `*rollback {snapshot}`  
→ Fix migration  
→ Retry


## Referência: references/squad/tasks/db-snapshot.md

# Task: Create Database Snapshot

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/backup-manager.sh` |
| **rationale** | Backup é operação determinística de pg_dump |

**Purpose**: Create schema-only snapshot for rollback capability

**Elicit**: true

---

## 🚀 NEW: Use Automated Backup Manager (RECOMMENDED)

**Token Savings: 90% | Time Savings: ~87%**

```bash
# Create snapshot with automatic labeling
./squads/db-sage/scripts/db-ops/backup-manager.sh --snapshot {label}

# Create snapshot with metadata
./squads/db-sage/scripts/db-ops/backup-manager.sh --snapshot {label} --description "Purpose description"

# Schema-only snapshot (default, faster)
./squads/db-sage/scripts/db-ops/backup-manager.sh --snapshot {label} --schema-only

# Full snapshot (schema + data)
./squads/db-sage/scripts/db-ops/backup-manager.sh --snapshot {label} --full

# Benefits:
#   - Automatic timestamp and versioning
#   - Metadata tracking (timestamp, user, description)
#   - Retention policy management
#   - Easy restore with --list and --restore
#   - 90% token savings
```

**OR continue with manual snapshot below:**

---

## Inputs

- `label` (string): Snapshot label/name (e.g., "baseline", "pre_migration", "v1_2_0")

---

## Process

### 1. Confirm Snapshot Details

Ask user:
- Snapshot label: `{label}`
- Purpose of this snapshot (e.g., "before adding user_roles table")
- Include data? (schema-only is default, safer, faster)

### 2. Create Snapshots Directory

```bash
mkdir -p supabase/snapshots
```

### 3. Generate Snapshot

```bash
TS=$(date +%Y%m%d_%H%M%S)
LABEL="{label}"
FILENAME="supabase/snapshots/${TS}_${LABEL}.sql"

echo "Creating snapshot: $FILENAME"

pg_dump "$SUPABASE_DB_URL" \
  --schema-only \
  --clean \
  --if-exists \
  --no-owner \
  --no-privileges \
  > "$FILENAME"

if [ $? -eq 0 ]; then
  echo "✅ Snapshot created: $FILENAME"
  ls -lh "$FILENAME"
else
  echo "❌ Snapshot failed"
  exit 1
fi
```

### 4. Verify Snapshot

Quick sanity check:

```bash
# Check file size (should be > 0)
if [ ! -s "$FILENAME" ]; then
  echo "⚠️ Snapshot file is empty"
  exit 1
fi

# Count schema objects
echo ""
echo "=== Snapshot Contents ==="
grep -c "CREATE TABLE" "$FILENAME" && echo "tables found" || echo "no tables"
grep -c "CREATE FUNCTION" "$FILENAME" && echo "functions found" || echo "no functions"
grep -c "CREATE POLICY" "$FILENAME" && echo "policies found" || echo "no policies"
```

### 5. Create Snapshot Metadata

```bash
cat > "supabase/snapshots/${TS}_${LABEL}.meta" <<EOF
Snapshot: ${TS}_${LABEL}
Created: $(date -Iseconds)
Label: ${LABEL}
Database: $(echo "$SUPABASE_DB_URL" | sed 's/:.*/:[REDACTED]/')
Purpose: [user provided purpose]
File: ${FILENAME}
Size: $(ls -lh "$FILENAME" | awk '{print $5}')

To restore:
  *rollback supabase/snapshots/${TS}_${LABEL}.sql

Or manually:
  psql "\$SUPABASE_DB_URL" -f "${FILENAME}"
EOF

cat "supabase/snapshots/${TS}_${LABEL}.meta"
```

---

## Output

```
✅ Snapshot Created Successfully

File: supabase/snapshots/20251026_143022_pre_migration.sql
Size: 45.2 KB
Timestamp: 20251026_143022
Label: pre_migration

Contents:
  - 12 tables
  - 8 functions
  - 15 policies

To restore this snapshot:
  *rollback supabase/snapshots/20251026_143022_pre_migration.sql

Metadata saved to:
  supabase/snapshots/20251026_143022_pre_migration.meta
```

---

## Snapshot Options

### Schema-Only (Default)
- ✅ Fast (seconds)
- ✅ Small file size
- ✅ Safe to apply to any environment
- ❌ No data preserved
- **Use for**: Migration rollback, schema versioning

### Schema + Data
```bash
pg_dump "$SUPABASE_DB_URL" \
  --clean \
  --if-exists \
  --no-owner \
  --no-privileges \
  > "$FILENAME"
```
- ⚠️ Slower (minutes to hours)
- ⚠️ Large file size
- ⚠️ Data may conflict on restore
- ✅ Complete backup
- **Use for**: Disaster recovery, environment cloning

### Specific Tables Only
```bash
pg_dump "$SUPABASE_DB_URL" \
  --schema-only \
  --table="users" \
  --table="profiles" \
  > "$FILENAME"
```
- ✅ Targeted snapshot
- ✅ Smaller file
- **Use for**: Testing specific table changes

---

## Best Practices

### When to Snapshot

**Always before:**
- Migrations
- Schema changes
- RLS policy changes
- Function modifications
- Major data operations

**Regularly:**
- Daily schema snapshots (automated)
- Before each deployment
- After successful migrations (post-snapshot)

### Snapshot Naming

**Good names:**
- `baseline` - Initial schema state
- `pre_migration` - Before any migration
- `pre_v1_2_0` - Before version deployment
- `working_state` - Known good state

**Bad names:**
- `backup` - Too generic
- `test` - Unclear purpose
- `snapshot1` - No context

### Retention

Keep snapshots for:
- Last 7 days: All snapshots
- Last 30 days: Daily snapshots
- Last year: Monthly snapshots
- Forever: Major version snapshots

```bash
# Example cleanup (keep last 10)
cd supabase/snapshots
ls -t *.sql | tail -n +11 | xargs rm -f
```

---

## Snapshot vs Backup

| Feature | Snapshot (pg_dump) | Supabase Backup |
|---------|-------------------|-----------------|
| Speed | Fast | Depends |
| Scope | Schema only (default) | Full database |
| Storage | Local files | Supabase managed |
| Restore | Manual psql | Supabase dashboard |
| Version control | ✅ Git-friendly | ❌ Binary |
| Automation | Easy (script) | Automatic |

**Use snapshots for:**
- Schema version control
- Migration rollback
- Development workflows
- Quick local backups

**Use Supabase backups for:**
- Disaster recovery
- Point-in-time restore
- Production incidents
- Long-term retention

---

## Troubleshooting

### "pg_dump: error: connection failed"

**Problem**: Cannot connect to database  
**Fix**: Check SUPABASE_DB_URL

```bash
*env-check
```

### "pg_dump: error: permission denied"

**Problem**: Insufficient privileges  
**Fix**: Use connection string with sufficient permissions

### "Snapshot file is empty"

**Problem**: No schema objects or connection failed  
**Fix**: 
1. Verify database has tables: `SELECT * FROM pg_tables WHERE schemaname='public';`
2. Check pg_dump version compatibility
3. Verify network connectivity

### "Snapshot is huge"

**Problem**: Including data unintentionally  
**Fix**: Use `--schema-only` flag explicitly

---

## Integration with Workflow

### Pre-Migration Workflow
```bash
*snapshot pre_migration      # Create rollback point
*verify-order migration.sql  # Check DDL order
*dry-run migration.sql       # Test safely
*apply-migration migration.sql  # Apply
*snapshot post_migration     # Capture new state
```

### Comparison Workflow
```bash
*snapshot before_changes
# ... make changes ...
*snapshot after_changes
diff supabase/snapshots/*_before_changes.sql \
     supabase/snapshots/*_after_changes.sql
```

---

## Advanced Usage

### Compare Two Snapshots

```bash
# Visual diff
diff -u snapshot1.sql snapshot2.sql | less

# Summary of changes
diff snapshot1.sql snapshot2.sql | grep "^[<>]" | head -20
```

### Extract Specific Objects

```bash
# Just table definitions
grep -A 20 "CREATE TABLE" snapshot.sql

# Just functions
sed -n '/CREATE FUNCTION/,/\$\$/p' snapshot.sql
```

### Version in Git

```bash
# Snapshot before commit
*snapshot before_feature_x
git add supabase/snapshots/*_before_feature_x.sql
git commit -m "snapshot: schema before feature X"
```

---

## Security Notes

⚠️ **Snapshots may contain sensitive schema info**:
- Table names reveal business logic
- Function names expose features
- Comments may contain internal notes

**In public repos:**
- Consider .gitignore for snapshots
- Or sanitize before committing
- Or use private repos only

**Do NOT commit:**
- Snapshots with `--data-included`
- Files containing passwords/secrets
- Connection strings in metadata

---

## Automation

### Daily Snapshot Script

```bash
#!/bin/bash
# Save as: scripts/daily-snapshot.sh

DATE=$(date +%Y%m%d)
*snapshot "daily_${DATE}"

# Cleanup old snapshots (keep 7 days)
find supabase/snapshots -name "daily_*.sql" -mtime +7 -delete
```

### Pre-Deploy Hook

```bash
# In CI/CD pipeline
- name: Create pre-deploy snapshot
  run: |
    /db-sage
    *snapshot "pre_deploy_${CI_COMMIT_SHA}"
```

---

## Related Commands

- `*rollback {snapshot}` - Restore snapshot
- `*apply-migration {path}` - Includes automatic snapshots
- `*env-check` - Verify pg_dump available


## Referência: references/squad/tasks/db-squad-integration.md

# Database Integration Analysis for Squad

| Field | Value |
|-------|-------|
| **execution_type** | `Hybrid` |
| **pattern** | EXEC-HY-001 |
| **script** | `scripts/db-ops/squad-integration-preflight.sh` |
| **rationale** | Worker inventaria touchpoints e schema opcional; Agent sugere integrações |

> Task ID: db-squad-integration
> Agent: DB Sage (Database Architect)
> Version: 1.0.0

---

## 🚀 NEW: Use Deterministic Integration Preflight (RECOMMENDED)

**Token Savings: 90% | Time Savings: ~86%**

```bash
# Inventory a squad's data touchpoints before designing integration
./squads/db-sage/scripts/db-ops/squad-integration-preflight.sh {squad_name}

# Include a live schema snapshot when DB env is available
./squads/db-sage/scripts/db-ops/squad-integration-preflight.sh {squad_name} --include-schema

# Benefits:
#   - Deterministic inventory of inputs, outputs, state, and DB touchpoints
#   - Fast triage of whether DB integration is justified at all
#   - Optional live schema baseline before design decisions
#   - 90% token savings
```

**OR continue with manual squad analysis below:**

---

## Description

Analyze an squad's data requirements and design database integration strategy. Maps squad inputs/outputs/state to database schema, proposes tables/relationships, and generates migration plan.

## Prerequisites

- Squad installed and accessible
- Database connection configured (*env-check passed)
- Current schema documented or accessible

## Workflow

### Step 1: Identify Target Squad

**Elicit from user:**
- Which squad? (e.g., the target squad name)
- Path to squad directory

**Actions:**
- Verify squad exists and has config.yaml
- Load squad metadata (name, version, description)

---

### Step 2: Audit Squad Data Flows

**Scan squad structure for data touchpoints:**

```bash
# Look for data indicators
- Config files (*.yaml, *.json, .env.example)
- Input directories (sources/, inputs/, uploads/)
- Output directories (outputs/, generated/, artifacts/)
- State files (state.json, .cache/, db/)
- Scripts that read/write data
- API endpoints that handle data
```

**Document findings:**

```yaml
squad_audit:
  name: {squad_name}
  version: x.y.z

  data_inputs:
    - type: user_uploaded_content
      format: markdown
      location: sources/uploads/
      volume: ~N files per entity

    - type: configuration
      format: yaml
      location: config/{squad}-config.yaml
      fields: [name, type, settings]

  data_outputs:
    - type: processed_artifact
      format: yaml
      location: outputs/{squad}/{slug}/
      persistence_need: high (reusable artifact)

    - type: generated_content
      format: markdown
      location: outputs/{squad}/{slug}/content/
      persistence_need: high (versioned, queryable)

  state_requirements:
    - processing_status: [pending, in_progress, completed, failed]
    - last_run_timestamp
    - version_tracking
    - validation_scores

  relationships:
    - One user → many entities
    - One entity → many artifacts (versioned)
    - One entity → many content pieces
```

---

### Step 3: Analyze Current Database Schema

**Connect to database and inspect:**

```sql
-- List all tables
SELECT table_name, table_type
FROM information_schema.tables
WHERE table_schema = 'public';

-- Check for related tables
SELECT * FROM pg_tables WHERE schemaname = 'public';

-- Look for existing patterns
-- Users, projects, assets, metadata tables?
```

**Document current schema:**

```yaml
current_schema:
  tables:
    - name: users
      has_auth: true
      fields: [id, email, created_at]

    - name: projects
      fields: [id, user_id, name, type, created_at]
      foreign_keys: [user_id → users.id]

  patterns_found:
    - Multi-tenancy via user_id
    - UUID primary keys
    - created_at/updated_at timestamps
    - RLS enabled on most tables
```

---

### Step 4: Design Integration Schema

**Map pack data to database tables:**

```yaml
proposed_schema:
  new_tables:

    # Example: domain entity table
    - name: entities
      purpose: Store primary domain objects
      fields:
        - id: uuid PRIMARY KEY
        - user_id: uuid REFERENCES users(id)
        - slug: text UNIQUE NOT NULL
        - name: text NOT NULL
        - type: text
        - status: entity_status_enum
        - version: integer DEFAULT 1
        - created_at: timestamptz
        - updated_at: timestamptz
      indexes:
        - (user_id, slug) UNIQUE
        - (status) WHERE status = 'active'
      rls: "Users can only access their own entities"

    - name: entity_artifacts
      purpose: Version-controlled generated outputs
      fields:
        - id: uuid PRIMARY KEY
        - entity_id: uuid REFERENCES entities(id) ON DELETE CASCADE
        - version: integer NOT NULL
        - artifact_type: text
        - content: text NOT NULL
        - metadata: jsonb
        - created_at: timestamptz
      indexes:
        - (entity_id, version, artifact_type) UNIQUE
      rls: "Inherit from entities table via entity_id"

    - name: entity_content
      purpose: Searchable content store
      fields:
        - id: uuid PRIMARY KEY
        - entity_id: uuid REFERENCES entities(id) ON DELETE CASCADE
        - content_text: text NOT NULL
        - embedding: vector(1536)  # For similarity search
        - metadata: jsonb (source_file, chunk_index, etc.)
        - created_at: timestamptz
      indexes:
        - (entity_id)
        - GiST (embedding vector_cosine_ops)
      rls: "Inherit from entities table"

  modified_tables: []

  enums:
    - name: entity_status_enum
      values: [pending, processing, completed, failed, archived]

  functions:
    - name: search_entity_content(entity_id uuid, query_embedding vector)
      purpose: Vector similarity search
      returns: TABLE(content_id uuid, content_text text, similarity float)
```

---

### Step 5: Validate Integration Design

**Run checks:**

- [ ] All pack outputs have storage strategy
- [ ] All pack inputs can be referenced (user uploads → table?)
- [ ] State requirements mapped to fields
- [ ] Foreign keys enforce relationships
- [ ] RLS policies defined for all tables
- [ ] Indexes support expected queries (list minds, search KB, version lookup)
- [ ] No orphaned data (CASCADE on deletes)
- [ ] Follows existing schema patterns (user_id, timestamps, etc.)

**KISS Gate check:**

- Is database even needed? (If pack works fine with filesystem, stop here)
- What problem does this solve? (searchability? multi-user? versioning?)
- Can existing tables be extended instead? (e.g., generic `projects` table?)
- Minimum viable schema? (Start with 1 table, expand later if needed)

---

### Step 6: Generate Migration Plan

**Create migration strategy:**

```yaml
migration_plan:
  phase_1_foundation:
    - Create enums (mind_status_enum)
    - Create base table (minds)
    - Add RLS policies to minds
    - Create seed data (test mind)

  phase_2_extensions:
    - Create related tables (mind_system_prompts, mind_knowledge_chunks)
    - Add foreign keys
    - Add indexes
    - Enable RLS on related tables

  phase_3_functions:
    - Create vector search function
    - Create helper views (active_minds, latest_prompts)

  rollback_strategy:
    - Snapshot before each phase
    - Rollback scripts generated
    - Test on staging first

  risk_assessment:
    - Low risk: New tables, no existing data affected
    - Medium risk: If modifying existing tables
    - High risk: If changing core auth/users tables
```

**Generate actual migration files:**

```bash
# Use template to generate
*create-migration-plan

# Then scaffold files
supabase/migrations/20251027_001_create_minds_table.sql
supabase/migrations/20251027_002_create_mind_prompts_table.sql
supabase/migrations/20251027_003_create_mind_kb_table.sql
supabase/migrations/20251027_004_add_vector_search.sql
```

---

### Step 7: Generate Integration Documentation

**Create docs/{squad-name}/database-integration.md:**

```markdown
# {Squad Name} Database Integration

## Overview
{Squad} data is now persisted in Supabase with full RLS, versioning, and search.

## Schema

### entities table
- Stores core domain objects
- One per primary entity
- User-scoped via RLS

### entity_artifacts table
- Version-controlled generated outputs
- Many per entity
- Allows A/B testing and rollback

### entity_content table
- Searchable content store
- Vector embeddings for similarity search
- Efficient retrieval during operations

## Usage

### Creating an entity
```sql
INSERT INTO entities (user_id, slug, name, type)
VALUES (auth.uid(), 'my-entity', 'My Entity', 'default');
```

### Storing an artifact
```sql
INSERT INTO entity_artifacts (entity_id, version, artifact_type, content)
VALUES (:entity_id, 1, 'primary', :content);
```

### Searching content
```sql
SELECT * FROM search_entity_content(
  :entity_id,
  :query_embedding::vector(1536)
)
LIMIT 10;
```

## Migration Path

1. Run migrations in order (see supabase/migrations/)
2. Backfill existing data from outputs/ directory
3. Update squad scripts to read/write database
4. Keep filesystem outputs as backup during transition
```

---

### Step 8: Output Integration Report

**Generate squads/{pack-name}/database-integration-report.yaml:**

```yaml
integration_analysis:
  squad: {squad_name}
  database: supabase_production
  analysis_date: YYYY-MM-DD
  analyst: DB Sage

summary:
  recommendation: "Integrate with database"
  rationale: |
    - Multi-user access required
    - Version tracking needed
    - Search capability needed
    - Filesystem alone cannot support these requirements

  tables_added: 3
  tables_modified: 0
  migration_risk: low
  estimated_effort: 4 hours (design + migrate + test)

schema_design:
  file: docs/{squad_name}/database-schema.yaml
  erd: docs/{squad_name}/database-erd.png (generate with *create-schema)

migration_plan:
  file: docs/{squad_name}/migration-plan.yaml
  migrations_directory: supabase/migrations/
  rollback_scripts: supabase/rollback/

next_steps:
  - [ ] Review schema design with team
  - [ ] Approve migration plan
  - [ ] Run *snapshot baseline
  - [ ] Execute migrations (*migrate)
  - [ ] Test integration (*smoke-test)
  - [ ] Update squad scripts to use database
  - [ ] Deploy to staging
  - [ ] Monitor for 48h
  - [ ] Deploy to production
```

---

## Success Criteria

- [ ] Squad data flows fully documented
- [ ] Current schema analyzed
- [ ] Integration schema designed (follows patterns, has RLS)
- [ ] KISS Gate validation passed (database is actually needed)
- [ ] Migration plan generated with rollback strategy
- [ ] Integration documentation created
- [ ] Report generated with clear next steps

---

## Output Files

```
squads/{pack-name}/
├── database-integration-report.yaml  ← Main output
├── data-flow-audit.yaml              ← Step 2 findings
└── schema-design.yaml                ← Step 4 design

docs/{pack-name}/
├── database-integration.md           ← Usage guide
├── database-schema.yaml              ← Schema definition
└── migration-plan.yaml               ← Migration strategy

supabase/migrations/
└── 2025MMDD_NNN_{squad}_*.sql       ← Ready to apply
```

---

## Examples

### Example: Course Platform Integration

```yaml
# A course platform squad → needs to store:
# - Course metadata (title, description, status)
# - Curriculum structure (modules, lessons)
# - Generated content (scripts, quizzes)
# - User progress (if multi-user platform)

proposed_schema:
  - courses table (id, user_id, slug, title, status)
  - course_modules table (id, course_id, order, title)
  - course_lessons table (id, module_id, order, title, content_type)
  - course_content table (id, lesson_id, content, generated_at)
```

### Example: Assessment Platform Integration

```yaml
# An assessment squad → needs to store:
# - Assessment definitions (types, questions)
# - User responses (answers, timestamps)
# - Computed results (profiles, scores)

proposed_schema:
  - assessments table (id, name, type, questions_jsonb)
  - user_assessments table (id, user_id, assessment_id, completed_at)
  - assessment_responses table (id, user_assessment_id, question_id, response)
  - assessment_results table (id, user_assessment_id, results_jsonb)
```

---

## Notes

- **Always run KISS Gate validation** - database might not be needed
- **Follow existing patterns** - don't reinvent (user_id, timestamps, RLS)
- **Start minimal** - can always add tables later
- **Think about queries** - indexes should match access patterns
- **Plan for scale** - vector search, partitioning if needed
- **RLS from day 1** - security cannot be retrofitted easily
- **Document everything** - future maintainers will thank you

---

## Related Tasks

- `*kiss` - Run before this task (auto-analyzes schema)
- `*create-schema` - Generate full schema documentation with ERD
- `*create-migration-plan` - Generate detailed migration strategy
- `*migrate` - Execute the actual migrations
- `*smoke-test` - Validate integration after migration


## Referência: references/squad/tasks/db-verify-order.md

# Task: Verify DDL Ordering

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/migration-runner.sh` |
| **rationale** | Análise de dependências DDL é parsing determinístico |

**Purpose**: Lint DDL for safe execution order to avoid dependency errors

**Elicit**: true

---

## 🚀 NEW: Use Automated Migration Safe Runner (RECOMMENDED)

**Token Savings: 92% | Time Savings: ~89%**

```bash
# Verify DDL ordering automatically
./squads/db-sage/scripts/db-ops/migration-runner.sh {path} --verify-order

# Verify order and proceed only if safe
./squads/db-sage/scripts/db-ops/migration-runner.sh {path} --verify-order
./squads/db-sage/scripts/db-ops/migration-runner.sh {path} --dry-run

# Benefits:
#   - Automatic DDL section detection
#   - Dependency graph analysis
#   - Safe execution order recommendation
#   - Circular dependency detection
#   - 92% token savings
```

**OR continue with manual DDL verification below:**

---

## Inputs

- `path` (string): Path to SQL migration file

---

## Process

### 1. Extract DDL Sections

Parse migration file and identify sections:

```bash
awk 'BEGIN{IGNORECASE=1}
  /create extension|alter extension/ {print "EXT:", NR, $0}
  /create table/ {print "TAB:", NR, $0}
  /create or replace function|create function/ {print "FUN:", NR, $0}
  /create trigger/ {print "TRG:", NR, $0}
  /enable row level security|create policy/ {print "RLS:", NR, $0}
  /create .* view/ {print "VIEW:", NR, $0}
' {path} > /tmp/ddl_order.txt

echo "=== DDL Section Analysis ==="
cat /tmp/ddl_order.txt
```

### 2. Analyze Ordering

Show recommended order and actual order:

```
Recommended Execution Order:
1. Extensions (CREATE EXTENSION)
2. Tables & Constraints (CREATE TABLE, ALTER TABLE)
3. Functions (CREATE FUNCTION)
4. Triggers (CREATE TRIGGER)
5. RLS (ENABLE RLS, CREATE POLICY)
6. Views & Materialized Views (CREATE VIEW)

Actual Order in File:
[output from grep above]
```

### 3. Run Heuristic Checks

Detect common ordering problems:

```bash
# Check: Functions before tables
FIRST_TAB=$(grep '^TAB:' /tmp/ddl_order.txt | head -1 | cut -d: -f2)
FIRST_FUN=$(grep '^FUN:' /tmp/ddl_order.txt | head -1 | cut -d: -f2)

if [ -n "$FIRST_TAB" ] && [ -n "$FIRST_FUN" ] && [ "$FIRST_FUN" -lt "$FIRST_TAB" ]; then
  echo "❌ Functions appear before tables. Reorder recommended."
  exit 2
fi

# Check: RLS before tables exist
FIRST_RLS=$(grep '^RLS:' /tmp/ddl_order.txt | head -1 | cut -d: -f2)
if [ -n "$FIRST_RLS" ] && [ -n "$FIRST_TAB" ] && [ "$FIRST_RLS" -lt "$FIRST_TAB" ]; then
  echo "❌ RLS commands before table creation. Reorder required."
  exit 2
fi

# Check: Triggers before functions
FIRST_TRG=$(grep '^TRG:' /tmp/ddl_order.txt | head -1 | cut -d: -f2)
if [ -n "$FIRST_TRG" ] && [ -n "$FIRST_FUN" ] && [ "$FIRST_TRG" -lt "$FIRST_FUN" ]; then
  echo "⚠️ Triggers before functions. May fail if trigger calls function."
fi

echo "✓ Ordering looks reasonable by heuristics"
```

### 4. Report Results

**If all checks pass:**
```
✅ DDL Ordering Validation Passed

Sections found:
  - Extensions: X
  - Tables: Y
  - Functions: Z
  - Triggers: N
  - RLS: M
  - Views: V

Order appears correct. Safe to proceed with:
  *dry-run {path}
```

**If issues found:**
```
❌ DDL Ordering Issues Detected

Problems:
  - Functions defined before tables (line X vs line Y)
  - Triggers reference functions not yet created
  
Recommended fixes:
  1. Move CREATE EXTENSION to top
  2. Group CREATE TABLE statements
  3. Then CREATE FUNCTION
  4. Then CREATE TRIGGER
  5. Then ENABLE RLS + policies
  6. Finally CREATE VIEW

After fixing, re-run: *verify-order {path}
```

---

## Correct Ordering Examples

### ✅ Good Order

```sql
-- 1. Extensions first
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. Tables and constraints
CREATE TABLE users (...);
CREATE TABLE fragments (...);
ALTER TABLE fragments ADD CONSTRAINT fk_user ...;

-- 3. Functions
CREATE OR REPLACE FUNCTION current_user_id() ...;
CREATE OR REPLACE FUNCTION update_timestamp() ...;

-- 4. Triggers
CREATE TRIGGER set_timestamp 
BEFORE UPDATE ON users ...;

-- 5. RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
CREATE POLICY "users_all" ON users ...;

-- 6. Views
CREATE VIEW user_fragments_view AS ...;
```

### ❌ Bad Order (Will Fail)

```sql
-- ❌ Function before table it references
CREATE FUNCTION get_user_name(user_id UUID) 
RETURNS TEXT AS $$
  SELECT name FROM users WHERE id = user_id;  -- users doesn't exist yet!
$$ LANGUAGE sql;

-- ❌ Table created after function
CREATE TABLE users (...);

-- ❌ RLS before table
CREATE POLICY "users_policy" ON users ...;  -- Can't create policy on non-existent table
```

---

## Common Dependency Patterns

### Pattern 1: Functions Calling Other Functions

**Order**: Base functions → Composite functions

```sql
-- First: Base function
CREATE FUNCTION base_func() ...;

-- Second: Function that calls base_func
CREATE FUNCTION composite_func() AS $$
BEGIN
  RETURN base_func();  -- Safe, base_func exists
END;
$$ LANGUAGE plpgsql;
```

### Pattern 2: Tables with Foreign Keys

**Order**: Referenced tables → Referencing tables

```sql
-- First: Parent table
CREATE TABLE users (id UUID PRIMARY KEY);

-- Second: Child table
CREATE TABLE posts (
  user_id UUID REFERENCES users(id)  -- Safe, users exists
);
```

### Pattern 3: Views on Views

**Order**: Base views → Derived views

```sql
-- First: Base view
CREATE VIEW active_users AS 
SELECT * FROM users WHERE deleted_at IS NULL;

-- Second: View on view
CREATE VIEW active_users_with_posts AS
SELECT u.*, COUNT(p.id) 
FROM active_users u  -- Safe, active_users exists
LEFT JOIN posts p ON p.user_id = u.id;
```

### Pattern 4: RLS Using Functions

**Order**: Tables → Functions → RLS Policies

```sql
-- First: Table
CREATE TABLE data (...);

-- Second: Helper function
CREATE FUNCTION user_can_access(data_id UUID) ...;

-- Third: RLS policy using function
CREATE POLICY "access_check" ON data
USING (user_can_access(id));  -- Safe, function exists
```

---

## Manual Review Checklist

After automated checks, manually verify:

- [ ] All CREATE EXTENSION at top
- [ ] Foreign key references come after parent tables
- [ ] Triggers reference existing functions
- [ ] RLS policies reference existing tables
- [ ] Views reference existing tables/views
- [ ] Functions called by other functions defined first
- [ ] No circular dependencies

---

## Integration with Workflow

Typical validation workflow:

1. Write migration
2. `*verify-order migration.sql` - Check ordering
3. Fix any issues found
4. `*dry-run migration.sql` - Test execution
5. `*apply-migration migration.sql` - Apply if dry-run passes

---

## Advanced: Dependency Graph

For complex migrations, visualize dependencies:

```bash
# Extract CREATE statements
grep -i "create" {path} | \
  grep -E "(table|function|view|trigger)" > /tmp/creates.txt

# Manual review of dependencies
cat /tmp/creates.txt
```

Look for:
- Table → Foreign Key → Other Table
- Function → Calls → Other Function
- Trigger → Calls → Function
- View → Selects → Table/View
- Policy → Uses → Function

---

## Why This Matters

**Problem**: Wrong order causes migration failures

```
ERROR: relation "users" does not exist
ERROR: function "user_can_access" does not exist
ERROR: table "data" does not exist for policy creation
```

**Solution**: Verify order before running

- Catch issues in seconds (not after failed migration)
- No partial schema state
- No rollback needed for ordering errors
- Faster development cycle

---

## Limitations

This is a heuristic check, not a full parser:

✅ **Catches**: Most common ordering issues  
✅ **Fast**: Runs in < 1 second  
✅ **Safe**: No database connection needed  

❌ **Misses**: Complex cross-file dependencies  
❌ **Misses**: Dynamic SQL  
❌ **Misses**: Subtle type dependencies  

For 100% validation, use: `*dry-run {path}`


## Referência: references/squad/tasks/domain-modeling.md

# Task: Domain Modeling Session

| Field | Value |
|-------|-------|
| **execution_type** | `Hybrid` |
| **pattern** | EXEC-HY-001 |
| **script** | `scripts/db-ops/schema-context-loader.sh` |
| **rationale** | Worker carrega contexto real do schema; decisoes de modelagem seguem com validacao humana |

**Purpose**: Interactive session to model business domain into database schema

**Elicit**: true

---

## 🚀 NEW: Load Current Schema Context First (RECOMMENDED PREFLIGHT)

**Token Savings: 70% | Time Savings: ~65%**

```bash
# Load live schema summary before proposing any new entities
./squads/db-sage/scripts/db-ops/schema-context-loader.sh

# Benefits:
#   - Loads current tables, relationships, and views
#   - Prevents proposing entities that already exist
#   - Grounds the interactive modeling session in live schema reality
#   - 70% token savings on discovery/context gathering
```

**OR continue with manual domain modeling below:**

---

## Overview

This task guides you through domain-driven database design, helping you translate business requirements into a well-structured database schema.

---

## Process

### 1. Understand the Domain

Ask the user comprehensive questions:

```
Let's model your domain!

1. What is the business domain? (e.g., e-commerce, social media, SaaS)

2. Who are the main actors? (e.g., users, admins, customers)

3. What are the core entities? (e.g., products, orders, posts)

4. What are the key relationships? (e.g., users have orders, posts belong to users)

5. What are the critical business rules? (e.g., orders cannot be deleted, users must verify email)

6. What are the main use cases? (e.g., user creates post, admin approves content)

7. What is the expected scale? (e.g., 1K users, 100K orders/month)

8. Are there any compliance requirements? (e.g., GDPR, HIPAA)
```

### 2. Identify Core Entities

For each entity mentioned, gather details:

```
Entity: {entity_name}

1. Description: What is it?

2. Attributes: What properties does it have?
   - Required fields?
   - Optional fields?
   - Computed fields?

3. Identifier: How is it uniquely identified?
   - UUID (recommended for distributed systems)
   - Serial integer
   - Natural key (email, SKU, etc.)

4. Lifecycle: How does it change over time?
   - Immutable (never changes)
   - Mutable (can be updated)
   - Soft-deletable (archived, not deleted)

5. Access patterns: How will it be queried?
   - By ID (primary key lookup)
   - By user (filtered by user_id)
   - By date range
   - Full-text search
   - Aggregations
```

### 3. Map Relationships

Identify relationships between entities:

```
Relationship Analysis:

For each pair of entities, determine:

1. Relationship type:
   - One-to-One (1:1)
   - One-to-Many (1:N)
   - Many-to-Many (M:N)

2. Ownership:
   - Who owns the relationship?
   - Can it exist independently?

3. Cardinality:
   - Optional or required?
   - Min/max constraints?

4. Cascade behavior:
   - What happens on delete?
   - What happens on update?

Examples:
- User → Posts (1:N, user owns, CASCADE delete)
- Post ← Tags (M:N, junction table, no cascade)
- User → Profile (1:1, user owns, CASCADE delete)
```

### 4. Design Tables

For each entity, design the table:

```sql
-- Template for each table

CREATE TABLE {entity_name} (
  -- Primary Key
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Foreign Keys (relationships)
  {parent}_id UUID REFERENCES {parent}(id) ON DELETE CASCADE,

  -- Required Attributes
  name TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  -- Optional Attributes
  description TEXT,
  metadata JSONB DEFAULT '{}'::jsonb,

  -- Audit Fields
  updated_at TIMESTAMPTZ,
  deleted_at TIMESTAMPTZ,  -- For soft deletes

  -- Constraints
  CONSTRAINT valid_name CHECK (LENGTH(name) > 0),
  CONSTRAINT valid_dates CHECK (created_at <= COALESCE(updated_at, NOW()))
);

-- Indexes (based on access patterns)
CREATE INDEX idx_{entity}_parent ON {entity}({parent}_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_{entity}_created ON {entity}(created_at DESC);

-- Comments (documentation)
COMMENT ON TABLE {entity} IS 'Stores {business description}';
COMMENT ON COLUMN {entity}.metadata IS 'Flexible JSONB field for extensibility';
```

### 5. Handle Many-to-Many Relationships

Create junction tables for M:N relationships:

```sql
-- Junction table pattern
CREATE TABLE {entity1}_{entity2} (
  {entity1}_id UUID NOT NULL REFERENCES {entity1}(id) ON DELETE CASCADE,
  {entity2}_id UUID NOT NULL REFERENCES {entity2}(id) ON DELETE CASCADE,

  -- Optional attributes (e.g., role, priority)
  role TEXT DEFAULT 'member',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  -- Composite primary key
  PRIMARY KEY ({entity1}_id, {entity2}_id)
);

-- Indexes for both directions
CREATE INDEX idx_{entity1}_{entity2}_1 ON {entity1}_{entity2}({entity1}_id);
CREATE INDEX idx_{entity1}_{entity2}_2 ON {entity1}_{entity2}({entity2}_id);
```

### 6. Apply Business Rules

Translate business rules into database constraints:

```sql
-- Example business rules

-- Rule: Email must be unique
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);

-- Rule: Orders cannot be negative
ALTER TABLE orders ADD CONSTRAINT positive_total CHECK (total >= 0);

-- Rule: Published posts must have title
ALTER TABLE posts ADD CONSTRAINT published_has_title
  CHECK (status != 'published' OR (title IS NOT NULL AND LENGTH(title) > 0));

-- Rule: Soft-deleted records are read-only
CREATE OR REPLACE FUNCTION prevent_update_deleted()
RETURNS TRIGGER AS $$
BEGIN
  IF OLD.deleted_at IS NOT NULL THEN
    RAISE EXCEPTION 'Cannot update deleted record';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_prevent_update_deleted
  BEFORE UPDATE ON {table}
  FOR EACH ROW
  EXECUTE FUNCTION prevent_update_deleted();
```

### 7. Design for Access Patterns

Create indexes based on how data will be queried:

```sql
-- Pattern 1: User-specific data (multi-tenant)
CREATE INDEX idx_posts_user ON posts(user_id) WHERE deleted_at IS NULL;

-- Pattern 2: Time-based queries
CREATE INDEX idx_posts_created ON posts(created_at DESC) WHERE deleted_at IS NULL;

-- Pattern 3: Status filtering
CREATE INDEX idx_posts_status ON posts(status, created_at DESC);

-- Pattern 4: Full-text search
CREATE INDEX idx_posts_search ON posts USING gin(to_tsvector('english', title || ' ' || content));

-- Pattern 5: JSONB queries
CREATE INDEX idx_posts_metadata ON posts USING gin(metadata jsonb_path_ops);

-- Pattern 6: Composite (multiple filters)
CREATE INDEX idx_posts_user_status ON posts(user_id, status, created_at DESC);
```

### 8. Add RLS Policies

Implement Row Level Security for Supabase:

```sql
-- Enable RLS
ALTER TABLE {table} ENABLE ROW LEVEL SECURITY;

-- Policy: Users see only their own data
CREATE POLICY "{table}_users_own"
  ON {table}
  FOR ALL
  TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- Policy: Admins see everything
CREATE POLICY "{table}_admins_all"
  ON {table}
  FOR ALL
  TO authenticated
  USING (
    (auth.jwt() ->> 'role') = 'admin'
  );

-- Policy: Public read, authenticated write
CREATE POLICY "{table}_public_read"
  ON {table}
  FOR SELECT
  TO public
  USING (true);

CREATE POLICY "{table}_auth_write"
  ON {table}
  FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);
```

### 9. Generate Schema Document

Create schema design document using template:

```
Use template: schema-design-tmpl.yaml

Fill in:
- domain_context
- entities (all identified entities)
- relationships (all relationships)
- access_patterns (from step 7)
- constraints (from step 6)
- indexes (from step 7)
- rls_policies (from step 8)
```

### 10. Generate Migration

Create initial migration file:

```bash
TS=$(date +%Y%m%d%H%M%S)
MIGRATION_FILE="supabase/migrations/${TS}_initial_schema.sql"

cat > "$MIGRATION_FILE" << 'EOF'
-- Initial Schema Migration
-- Domain: {domain_name}
-- Generated: {timestamp}

BEGIN;

-- Create all tables
{table_definitions}

-- Create all indexes
{index_definitions}

-- Create all constraints
{constraint_definitions}

-- Enable RLS and create policies
{rls_policies}

-- Add comments
{comment_statements}

COMMIT;
EOF

echo "✓ Migration created: $MIGRATION_FILE"
```

---

## Output

Provide comprehensive domain model:

```
✅ DOMAIN MODEL COMPLETE

Domain: {domain_name}

Entities: {count}
- {entity1}
- {entity2}
...

Relationships:
- {entity1} → {entity2} (1:N)
- {entity3} ← {entity4} (M:N via junction)
...

Files Generated:
1. docs/schema-design.yaml - Complete schema documentation
2. supabase/migrations/{TS}_initial_schema.sql - Migration file
3. docs/erd.md - Entity relationship diagram (markdown)

Next Steps:
1. Review schema design document
2. Validate with stakeholders
3. Run dry-run: *dry-run {migration_file}
4. Apply migration: *apply-migration {migration_file}
5. Add seed data if needed: *seed {seed_file}
```

---

## Best Practices

### 1. Start Simple

- Begin with core entities
- Add complexity incrementally
- Avoid premature optimization

### 2. Use Standard Patterns

- id (UUID primary key)
- created_at, updated_at (timestamps)
- deleted_at (soft deletes)
- user_id (ownership)

### 3. Document Everything

- Table comments
- Column comments
- Constraint names that explain purpose

### 4. Think About Scale

- How will tables grow?
- What queries will be most common?
- Where are the hot paths?

### 5. Design for Change

- Use JSONB for flexible attributes
- Soft deletes preserve history
- Migrations are additive when possible

### 6. Security First

- RLS by default
- Constraints enforce data integrity
- Foreign keys prevent orphans

---

## Common Domain Patterns

### 1. Multi-Tenancy

```sql
-- Tenant isolation
CREATE TABLE organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL
);

CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID NOT NULL REFERENCES organizations(id),
  email TEXT NOT NULL UNIQUE,
  UNIQUE (organization_id, email)
);

-- RLS for tenant isolation
CREATE POLICY "org_isolation" ON users
  FOR ALL TO authenticated
  USING (
    organization_id IN (
      SELECT organization_id
      FROM user_organizations
      WHERE user_id = auth.uid()
    )
  );
```

### 2. Audit Trail

```sql
-- Immutable audit log
CREATE TABLE audit_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  table_name TEXT NOT NULL,
  record_id UUID NOT NULL,
  operation TEXT NOT NULL, -- INSERT, UPDATE, DELETE
  old_data JSONB,
  new_data JSONB,
  user_id UUID REFERENCES users(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Trigger for automatic auditing
CREATE OR REPLACE FUNCTION audit_trigger()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO audit_log (table_name, record_id, operation, old_data, new_data, user_id)
  VALUES (
    TG_TABLE_NAME,
    COALESCE(NEW.id, OLD.id),
    TG_OP,
    CASE WHEN TG_OP != 'INSERT' THEN to_jsonb(OLD) END,
    CASE WHEN TG_OP != 'DELETE' THEN to_jsonb(NEW) END,
    auth.uid()
  );
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
```

### 3. Hierarchical Data

```sql
-- Adjacency list pattern
CREATE TABLE categories (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  parent_id UUID REFERENCES categories(id),
  name TEXT NOT NULL,
  path TEXT[] -- Materialized path for fast queries
);

-- Update path on insert/update
CREATE OR REPLACE FUNCTION update_category_path()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.parent_id IS NULL THEN
    NEW.path := ARRAY[NEW.id];
  ELSE
    SELECT path || NEW.id INTO NEW.path
    FROM categories
    WHERE id = NEW.parent_id;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

---

## References

- [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)
- [PostgreSQL Data Types](https://www.postgresql.org/docs/current/datatype.html)
- [Supabase RLS Policies](https://supabase.com/docs/guides/auth/row-level-security)


## Referência: references/squad/tasks/execute-checklist.md

# Checklist Validation Task

| Field | Value |
|-------|-------|
| **execution_type** | `Agent` |
| **pattern** | EXEC-A-001 |
| **rationale** | Validação de checklist requer interpretação de cada item |

This task provides instructions for validating documentation against checklists. The agent MUST follow these instructions to ensure thorough and systematic validation of documents.

## Available Checklists

If the user asks or does not specify a specific checklist, list the checklists available to the agent persona. If the task is being run not with a specific agent, tell the user to check the squads/db-sage/checklists/ folder to select the appropriate one to run.

## Instructions

1. **Initial Assessment**

   - If user or the task being run provides a checklist name:
     - Try fuzzy matching (e.g. "architecture checklist" -> "architect-checklist")
     - If multiple matches found, ask user to clarify
     - Load the appropriate checklist from squads/db-sage/checklists/
   - If no checklist specified:
     - Ask the user which checklist they want to use
     - Present the available options from the files in the checklists folder
   - Confirm if they want to work through the checklist:
     - Section by section (interactive mode - very time consuming)
     - All at once (YOLO mode - recommended for checklists, there will be a summary of sections at the end to discuss)

2. **Document and Artifact Gathering**

   - Each checklist will specify its required documents/artifacts at the beginning
   - Follow the checklist's specific instructions for what to gather, generally a file can be resolved in the docs folder, if not or unsure, halt and ask or confirm with the user.

3. **Checklist Processing**

   If in interactive mode:

   - Work through each section of the checklist one at a time
   - For each section:
     - Review all items in the section following instructions for that section embedded in the checklist
     - Check each item against the relevant documentation or artifacts as appropriate
     - Present summary of findings for that section, highlighting warnings, errors and non applicable items (rationale for non-applicability).
     - Get user confirmation before proceeding to next section or if any thing major do we need to halt and take corrective action

   If in YOLO mode:

   - Process all sections at once
   - Create a comprehensive report of all findings
   - Present the complete analysis to the user

4. **Validation Approach**

   For each checklist item:

   - Read and understand the requirement
   - Look for evidence in the documentation that satisfies the requirement
   - Consider both explicit mentions and implicit coverage
   - Aside from this, follow all checklist llm instructions
   - Mark items as:
     - ✅ PASS: Requirement clearly met
     - ❌ FAIL: Requirement not met or insufficient coverage
     - ⚠️ PARTIAL: Some aspects covered but needs improvement
     - N/A: Not applicable to this case

5. **Section Analysis**

   For each section:

   - think step by step to calculate pass rate
   - Identify common themes in failed items
   - Provide specific recommendations for improvement
   - In interactive mode, discuss findings with user
   - Document any user decisions or explanations

6. **Final Report**

   Prepare a summary that includes:

   - Overall checklist completion status
   - Pass rates by section
   - List of failed items with context
   - Specific recommendations for improvement
   - Any sections or items marked as N/A with justification

## Checklist Execution Methodology

Each checklist now contains embedded LLM prompts and instructions that will:

1. **Guide thorough thinking** - Prompts ensure deep analysis of each section
2. **Request specific artifacts** - Clear instructions on what documents/access is needed
3. **Provide contextual guidance** - Section-specific prompts for better validation
4. **Generate comprehensive reports** - Final summary with detailed findings

The LLM will:

- Execute the complete checklist validation
- Present a final report with pass/fail rates and key findings
- Offer to provide detailed analysis of any section, especially those with warnings or failures


## Referência: references/squad/tasks/kiss.md

# Task: KISS Gate Analysis

| Field | Value |
|-------|-------|
| **execution_type** | `Hybrid` |
| **pattern** | EXEC-HY-001 |
| **rationale** | Worker coleta sinais e red flags; humano decide a opcao final de schema/integracao |

Executa o workflow `kiss-gate-workflow.yaml` de forma automática, sem pedir inputs ao usuário.

## Input

- `{context}` - PRD path, descrição textual, ou vazio (usa conversa)

## Execution

### STEP 1: Capturar Contexto

```
Se {context} é path de arquivo → ler arquivo
Se {context} é texto → usar diretamente
Se vazio → extrair da conversa atual
```

### STEP 2: Análise Automática do Schema

Executar queries para descobrir o que já existe:

```sql
-- Tabelas com nomes similares ao contexto
SELECT table_name,
       (SELECT COUNT(*) FROM information_schema.columns c
        WHERE c.table_name = t.table_name) as cols
FROM information_schema.tables t
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE'
  AND table_name ILIKE '%{keyword}%';

-- Row counts das tabelas candidatas
SELECT schemaname || '.' || relname as table_name, n_live_tup as rows
FROM pg_stat_user_tables
WHERE relname ILIKE '%{keyword}%'
ORDER BY n_live_tup DESC;

-- FKs relacionadas
SELECT tc.table_name, ccu.table_name as references_table
FROM information_schema.table_constraints tc
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND (tc.table_name ILIKE '%{keyword}%' OR ccu.table_name ILIKE '%{keyword}%');
```

### STEP 3: Preencher Campos do Workflow Automaticamente

Inferir valores para os campos do `kiss-gate-workflow.yaml`:

| Campo | Como Inferir |
|-------|--------------|
| `what_storing` | Extrair do contexto/PRD (entidade principal) |
| `how_many` | Estimar: "poucos/alguns" → 50, "milhares" → 10000, sem menção → 1000 |
| `how_often` | Inferir: "logs/eventos" → frequente, "config" → raramente |
| `who_access` | Detectar: multi-tenant → "multiple users", single app → "application" |
| `need_joins` | Analisar: menciona relacionamentos/FKs → true, dados isolados → false |

### STEP 4: Executar Lógica de Red Flags

Aplicar regras do workflow:

```
RED_FLAGS = 0

Se how_many < 100:
  → 🚩 "Poucos registros (<100) - considerar JSON/YAML"
  → RED_FLAGS++

Se who_access contém "just me" ou "single":
  → 🚩 "Usuário único - considerar SQLite local"
  → RED_FLAGS++

Se need_joins == false:
  → 🚩 "Sem relacionamentos - reconsiderar necessidade de DB"
  → RED_FLAGS++

Se tabela similar encontrada no STEP 2:
  → 🚩 "Tabela similar existe: {table_name} ({rows} rows)"
  → RED_FLAGS++
```

### STEP 5: Apresentar Diagnóstico

```markdown
## 🔍 KISS Analysis

**Contexto:** {resumo em 1 linha}

**Valores inferidos:**
- Armazenando: {what_storing}
- Volume estimado: {how_many} registros
- Frequência de mudança: {how_often}
- Acesso: {who_access}
- Relacionamentos: {need_joins ? "Sim" : "Não"}

**Schema existente relevante:**
{lista de tabelas similares encontradas ou "Nenhuma tabela similar"}

**Red Flags:** {RED_FLAGS}
{lista de red flags ou "✅ Nenhum"}

---

### Recomendação: {REUSE|EXTEND|CREATE|RECONSIDER}

{explicação em 1-2 frases}

### Opções

1. **{opção recomendada}** - {descrição}
2. **{alternativa}** - {descrição}
3. **{outra alternativa}** - {descrição}
```

### STEP 6: Aguardar Decisão

Usuário escolhe 1, 2 ou 3.

## Principle

> "Workflow executa, agente preenche, usuário decide"


## Referência: references/squad/tasks/query-optimization.md

# Task: Query Optimization Session

| Field | Value |
|-------|-------|
| **execution_type** | `Hybrid` |
| **pattern** | EXEC-HY-001 |
| **script** | `scripts/db-ops/explain-analyzer.sh` |
| **rationale** | Worker coleta EXPLAIN, Agent/Human interpreta e sugere otimizações |

**Purpose**: Interactive session to optimize slow queries

**Elicit**: true

---

## 🚀 NEW: Use Automated Query Tools (RECOMMENDED)

**Token Savings: 88% | Time Savings: ~84%**

```bash
# Analyze query with execution metrics and buffer usage
./squads/db-sage/scripts/db-ops/explain-analyzer.sh "{query}" --analyze --buffers

# Get machine-readable output for downstream recommendation logic
./squads/db-sage/scripts/db-ops/explain-analyzer.sh "{query}" --format json

# Fast deterministic baseline without running the query
./squads/db-sage/scripts/db-ops/explain-analyzer.sh "{query}"

# Benefits:
#   - Automatic slow query detection
#   - Index recommendations
#   - Query rewrite suggestions
#   - Before/after comparison
#   - 88% token savings
```

**OR continue with manual query optimization below:**

---

## Inputs

- `query` (string): SQL query to optimize (optional - can discover from pg_stat_statements)

---

## Process

### 1. Identify Slow Query

If query not provided, find it:

```bash
echo "Finding slow queries..."

psql "$SUPABASE_DB_URL" << 'EOF'
SELECT
  queryid,
  LEFT(query, 100) AS query_preview,
  calls,
  ROUND(mean_exec_time::numeric, 2) AS avg_ms,
  ROUND(total_exec_time::numeric, 2) AS total_ms
FROM pg_stat_statements
WHERE query NOT LIKE '%pg_stat_statements%'
ORDER BY mean_exec_time DESC
LIMIT 10;
EOF

echo ""
echo "Select query to optimize (enter queryid or paste full query):"
read QUERY_INPUT
```

### 2. Run EXPLAIN ANALYZE

Analyze current performance:

```bash
echo "Running EXPLAIN ANALYZE..."

psql "$SUPABASE_DB_URL" << EOF
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
{query};
EOF
```

### 3. Identify Issues

Guide user through analysis:

```
Analyzing EXPLAIN output...

Check the following (in order of importance):

1. ❌ Sequential Scans on large tables?
   Look for: "Seq Scan on table_name"
   Filter removes many rows: rows=1000000 → actual rows=10
   → FIX: Add index on WHERE clause columns

2. ❌ Row count estimate mismatches?
   Compare: rows=100 (plan) vs actual rows=10000 (reality)
   Difference > 10x is problematic
   → FIX: Run ANALYZE table_name;

3. ❌ Nested Loops with high iteration count?
   Look for: "Nested Loop (actual ... loops=10000)"
   → FIX: Add index on join columns, or force Hash Join

4. ❌ Disk reads (buffer cache misses)?
   Look for: "Buffers: shared read=1000"
   High compared to "shared hit"
   → FIX: Add indexes, increase shared_buffers, optimize query

5. ❌ Temporary files (work_mem exceeded)?
   Look for: "Buffers: temp read=5000 written=5000"
   → FIX: Increase work_mem, optimize query, add indexes

6. ❌ Sort operations on large datasets?
   Look for: "Sort Method: external merge Disk: 50000kB"
   → FIX: Add index on ORDER BY columns, increase work_mem

7. ❌ Expensive function calls in WHERE?
   Look for: Functions evaluated on every row
   → FIX: Use expression index, or filter before function call
```

### 4. Generate Recommendations

Based on issues found:

```bash
echo "Generating optimization recommendations..."

cat << 'MDEOF'
## Optimization Recommendations

### Issue 1: Sequential Scan on 'users' table

**Current:**
```
Seq Scan on users (cost=0.00..1829.00 rows=1000 width=100)
  Filter: (email = 'user@example.com')
  Rows Removed by Filter: 99999
  Buffers: shared read=829
```

**Problem:** Full table scan for email lookup

**Solution:** Add index on email
```sql
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
```

**Expected Improvement:** 99%+ faster (1000ms → <10ms)

---

### Issue 2: Row count mismatch

**Current:**
```
Estimated rows: 100
Actual rows: 10000
```

**Problem:** Stale statistics causing bad query plan

**Solution:** Update table statistics
```sql
ANALYZE users;
```

**Expected Improvement:** Better query plan selection

---

[Continue for each issue...]

MDEOF
```

### 5. Create Optimization Migration

Generate migration with recommended indexes:

```bash
TS=$(date +%Y%m%d%H%M%S)
MIGRATION_FILE="supabase/migrations/${TS}_optimize_query.sql"

cat > "$MIGRATION_FILE" << 'EOF'
-- Query Optimization Migration
-- Generated: $(date -u)
-- Target: {query_description}

BEGIN;

-- Add recommended indexes (CONCURRENTLY for zero downtime)
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_users_email
  ON users(email);

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_posts_user_created
  ON posts(user_id, created_at DESC)
  WHERE deleted_at IS NULL;

-- Update statistics
ANALYZE users;
ANALYZE posts;

COMMIT;

-- Verify improvement
EXPLAIN (ANALYZE, BUFFERS)
{original_query};
EOF

echo "✓ Migration: $MIGRATION_FILE"
```

### 6. Test Optimization

Apply and measure improvement:

```bash
echo "Applying optimization..."

# Run migration
psql "$SUPABASE_DB_URL" -f "$MIGRATION_FILE"

echo "Re-running EXPLAIN ANALYZE..."

# Compare before/after
psql "$SUPABASE_DB_URL" << EOF
EXPLAIN (ANALYZE, BUFFERS)
{query};
EOF

echo ""
echo "Compare execution times:"
echo "  Before: {before_time}ms"
echo "  After:  {after_time}ms"
echo "  Improvement: {percentage}%"
```

---

## Output

Display optimization summary:

```
✅ QUERY OPTIMIZATION COMPLETE

Query: {query_summary}

Performance Improvement:
  Before:  {before_time}ms
  After:   {after_time}ms
  Speedup: {speedup}x ({percentage}% faster)

Changes Applied:
  ✓ Added index on users(email)
  ✓ Added index on posts(user_id, created_at)
  ✓ Updated table statistics

Migration: supabase/migrations/{TS}_optimize_query.sql

Next Steps:
1. Monitor query performance in production
2. Update application to use optimized query
3. Consider denormalization if still slow
4. Review similar queries for same patterns
```

---

## Common Optimization Patterns

### Pattern 1: Simple Filter

**Before:**
```sql
SELECT * FROM users WHERE email = 'user@example.com';
-- Seq Scan: 1000ms
```

**After:**
```sql
CREATE INDEX idx_users_email ON users(email);
-- Index Scan: 5ms
```

### Pattern 2: Composite Filter

**Before:**
```sql
SELECT * FROM posts
WHERE user_id = 'xxx' AND status = 'published'
ORDER BY created_at DESC
LIMIT 10;
-- Seq Scan: 500ms
```

**After:**
```sql
CREATE INDEX idx_posts_user_status_created
  ON posts(user_id, status, created_at DESC)
  WHERE deleted_at IS NULL;
-- Index Scan: 2ms
```

### Pattern 3: Join Optimization

**Before:**
```sql
SELECT p.*, u.name
FROM posts p
JOIN users u ON p.user_id = u.id;
-- Nested Loop: 2000ms
```

**After:**
```sql
-- Add index on FK
CREATE INDEX idx_posts_user_id ON posts(user_id);

-- Or force Hash Join for large datasets
SELECT /*+ HashJoin(p u) */ p.*, u.name
FROM posts p
JOIN users u ON p.user_id = u.id;
-- Hash Join: 200ms
```

### Pattern 4: Partial Index

**Before:**
```sql
-- Index on all rows
CREATE INDEX idx_posts_created ON posts(created_at);
-- Index size: 100MB
```

**After:**
```sql
-- Index only active rows
CREATE INDEX idx_posts_active_created
  ON posts(created_at)
  WHERE deleted_at IS NULL;
-- Index size: 20MB, same performance for active queries
```

### Pattern 5: Covering Index

**Before:**
```sql
SELECT id, title, created_at FROM posts WHERE user_id = 'xxx';
-- Index Scan + Table Lookup
```

**After:**
```sql
CREATE INDEX idx_posts_user_covering
  ON posts(user_id)
  INCLUDE (title, created_at);
-- Index-Only Scan (no table lookup)
```

### Pattern 6: Expression Index

**Before:**
```sql
SELECT * FROM users WHERE LOWER(email) = 'user@example.com';
-- Seq Scan (can't use regular index)
```

**After:**
```sql
CREATE INDEX idx_users_email_lower ON users(LOWER(email));
-- Index Scan
```

---

## Advanced Techniques

### 1. Denormalization

When joins are too expensive:

```sql
-- Add redundant column
ALTER TABLE posts ADD COLUMN author_name TEXT;

-- Populate from join
UPDATE posts p
SET author_name = u.name
FROM users u
WHERE p.user_id = u.id;

-- Keep in sync with trigger
CREATE OR REPLACE FUNCTION sync_author_name()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE posts
  SET author_name = NEW.name
  WHERE user_id = NEW.id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_sync_author_name
  AFTER UPDATE OF name ON users
  FOR EACH ROW
  EXECUTE FUNCTION sync_author_name();
```

### 2. Materialized Views

For expensive aggregations:

```sql
CREATE MATERIALIZED VIEW user_stats AS
SELECT
  user_id,
  COUNT(*) AS post_count,
  MAX(created_at) AS last_post_at
FROM posts
GROUP BY user_id;

CREATE UNIQUE INDEX ON user_stats(user_id);

-- Refresh periodically
REFRESH MATERIALIZED VIEW CONCURRENTLY user_stats;
```

### 3. Partitioning

For very large tables:

```sql
-- Time-based partitioning
CREATE TABLE posts (
  id UUID,
  created_at TIMESTAMPTZ,
  ...
) PARTITION BY RANGE (created_at);

CREATE TABLE posts_2024_01 PARTITION OF posts
  FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

-- Queries automatically use partition pruning
SELECT * FROM posts
WHERE created_at >= '2024-01-15'
  AND created_at < '2024-01-20';
-- Only scans posts_2024_01 partition
```

---

## Measurement Tools

### 1. Query Timing (Basic)

```sql
\timing on
{your_query}
```

### 2. pg_stat_statements (Production Monitoring)

**Best for:** Cumulative performance analysis and trend tracking

```sql
-- Enable extension (should already be enabled in Supabase)
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Top 10 slowest queries (by mean execution time)
SELECT
  LEFT(query, 100) AS query_preview,
  calls,
  ROUND(mean_exec_time::numeric, 2) AS avg_ms,
  ROUND(total_exec_time::numeric, 2) AS total_ms,
  ROUND((100 * total_exec_time / SUM(total_exec_time) OVER())::numeric, 2) AS pct_total
FROM pg_stat_statements
WHERE query NOT LIKE '%pg_stat_statements%'
ORDER BY mean_exec_time DESC
LIMIT 10;

-- NEW in PostgreSQL 13+: Planning vs Execution time
SELECT
  LEFT(query, 100) AS query_preview,
  calls,
  ROUND(mean_plan_time::numeric, 2) AS avg_plan_ms,
  ROUND(mean_exec_time::numeric, 2) AS avg_exec_ms,
  ROUND((mean_plan_time / NULLIF(mean_exec_time, 0) * 100)::numeric, 2) AS plan_pct
FROM pg_stat_statements
WHERE query NOT LIKE '%pg_stat_statements%'
ORDER BY mean_plan_time DESC
LIMIT 10;
-- If plan_pct > 20%, consider using prepared statements
```

### 3. auto_explain (Automatic Slow Query Logging)

**Best for:** Production debugging without manual EXPLAIN

```sql
-- Enable the extension
LOAD 'auto_explain';

-- Configure (Supabase Dashboard → Database → Settings or ALTER SYSTEM)
ALTER SYSTEM SET auto_explain.log_min_duration = 1000;  -- Log queries > 1s
ALTER SYSTEM SET auto_explain.log_analyze = on;
ALTER SYSTEM SET auto_explain.log_buffers = on;
ALTER SYSTEM SET auto_explain.log_timing = on;  -- Include timing info
ALTER SYSTEM SET auto_explain.log_verbose = on;  -- Verbose output

-- Reload configuration
SELECT pg_reload_conf();

-- Slow queries are now logged automatically to PostgreSQL logs
-- Access via Supabase Dashboard → Logs or pg_stat_statements
```

**Real-world benefit:** Invaluable for identifying problematic queries in production without manual intervention.

### 4. Modern Visualization Tools (2025)

**Postgres Explain Visualizer 2 (pev2)** - Interactive browser-based tool:
- Visual execution plan with collapsible nodes
- Color-coded operation costs and timings
- Automatic bottleneck detection
- https://explain.dalibo.com/ (online tool)

**pgMustard** - AI-powered plan analysis:
- Automated performance recommendations
- Visual execution plan with insights
- https://www.pgmustard.com/

**Example workflow:**
```bash
# 1. Get EXPLAIN output as JSON
psql "$DB_URL" -c "EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) SELECT ..." > plan.json

# 2. Upload to https://explain.dalibo.com/
# Visual analysis with recommendations
```

### 5. Emerging: AI-Assisted Tuning (2025+)

**pgai extension** - Machine learning for query optimization:
```sql
-- Install pgai (if available)
CREATE EXTENSION IF NOT EXISTS pgai;

-- Analyze query and get AI suggestions
SELECT pgai.suggest_indexes('SELECT * FROM users WHERE email = $1');

-- Returns: AI-generated index recommendations based on query patterns
```

**Self-learning query caching:**
- ML models predict which queries will run next
- Pre-load data before query execution
- Significant latency reduction for predictable workloads

---

## Regular Maintenance

**Critical:** Database performance degrades without maintenance!

```sql
-- Update statistics (run after significant data changes)
ANALYZE;  -- All tables
ANALYZE users;  -- Specific table

-- Vacuum and analyze (scheduled maintenance)
VACUUM ANALYZE;

-- Check table bloat
SELECT
  schemaname,
  tablename,
  pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size,
  n_dead_tup AS dead_rows
FROM pg_stat_user_tables
WHERE n_dead_tup > 1000
ORDER BY n_dead_tup DESC;
```

---

## References

- [PostgreSQL Performance Tips](https://wiki.postgresql.org/wiki/Performance_Optimization)
- [Supabase Query Optimization](https://supabase.com/docs/guides/database/query-optimization)
- [Use The Index, Luke](https://use-the-index-luke.com/)


## Referência: references/squad/tasks/schema-audit.md

# Task: Schema Audit

| Field | Value |
|-------|-------|
| **execution_type** | `Worker` |
| **pattern** | EXEC-W-001 |
| **script** | `scripts/db-ops/health-checker.sh` |
| **rationale** | Worker coleta metadados, executa checks repetiveis e gera findings estruturados |

**Purpose**: Comprehensive audit of database schema quality and best practices

**Elicit**: false

---

## 🚀 NEW: Use Health Checker as Preflight (RECOMMENDED)

```bash
# Fast connectivity and health preflight before the schema-specific checks below
./squads/db-sage/scripts/db-ops/health-checker.sh --schema-audit

# Verbose health report while auditing schema manually
./squads/db-sage/scripts/db-ops/health-checker.sh --schema-audit --verbose

# Security follow-up after schema audit
./squads/db-sage/scripts/db-ops/health-checker.sh --security-audit
```

**OR continue with manual schema audit below:**

---

## Overview

This task performs a thorough audit of your database schema, checking for:
- Design best practices
- Performance issues
- Security gaps
- Data integrity risks
- Missing indexes
- Naming conventions

---

## Process

### 1. Collect Schema Metadata

Gather comprehensive schema information:

```bash
echo "Collecting schema metadata..."

psql "$SUPABASE_DB_URL" << 'EOF'
-- Save to temp tables for analysis

-- Tables
CREATE TEMP TABLE audit_tables AS
SELECT
  schemaname,
  tablename,
  pg_total_relation_size(schemaname||'.'||tablename) AS total_size
FROM pg_tables
WHERE schemaname = 'public';

-- Columns
CREATE TEMP TABLE audit_columns AS
SELECT
  table_schema,
  table_name,
  column_name,
  data_type,
  is_nullable,
  column_default
FROM information_schema.columns
WHERE table_schema = 'public';

-- Indexes
CREATE TEMP TABLE audit_indexes AS
SELECT
  schemaname,
  tablename,
  indexname,
  indexdef,
  pg_relation_size(indexrelid) AS index_size
FROM pg_indexes
WHERE schemaname = 'public';

-- Foreign Keys
CREATE TEMP TABLE audit_fks AS
SELECT
  tc.table_name,
  kcu.column_name,
  ccu.table_name AS foreign_table,
  ccu.column_name AS foreign_column
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND tc.table_schema = 'public';

SELECT '✓ Metadata collected' AS status;
EOF
```

### 2. Check Design Best Practices

Run design checks:

```bash
psql "$SUPABASE_DB_URL" << 'EOF'
\echo '=========================================='
\echo '🔍 DESIGN BEST PRACTICES AUDIT'
\echo '=========================================='
\echo ''

-- Check 1: Tables without primary keys
\echo '1. Tables without PRIMARY KEY:'
SELECT table_name
FROM information_schema.tables t
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE'
  AND NOT EXISTS (
    SELECT 1
    FROM information_schema.table_constraints
    WHERE table_schema = t.table_schema
      AND table_name = t.table_name
      AND constraint_type = 'PRIMARY KEY'
  );
\echo ''

-- Check 2: Tables without created_at
\echo '2. Tables without created_at timestamp:'
SELECT table_name
FROM information_schema.tables t
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE'
  AND NOT EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = t.table_schema
      AND table_name = t.table_name
      AND column_name IN ('created_at', 'createdat')
  );
\echo ''

-- Check 3: Tables without updated_at
\echo '3. Tables without updated_at timestamp:'
SELECT table_name
FROM information_schema.tables t
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE'
  AND NOT EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = t.table_schema
      AND table_name = t.table_name
      AND column_name IN ('updated_at', 'updatedat')
  );
\echo ''

-- Check 4: Foreign keys without indexes
\echo '4. Foreign keys without indexes (performance issue):'
SELECT
  fk.table_name,
  fk.column_name,
  fk.foreign_table
FROM audit_fks fk
WHERE NOT EXISTS (
  SELECT 1
  FROM pg_indexes idx
  WHERE idx.tablename = fk.table_name
    AND idx.indexdef LIKE '%' || fk.column_name || '%'
);
\echo ''

-- Check 5: Nullable columns that should be NOT NULL
\echo '5. Suspicious nullable columns (id, *_id, email, created_at):'
SELECT
  table_name,
  column_name,
  data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND is_nullable = 'YES'
  AND (
    column_name = 'id'
    OR column_name = 'email'
    OR column_name = 'created_at'
    OR column_name LIKE '%_id'
  );
\echo ''

EOF
```

### 3. Check Performance Issues

Identify performance problems:

```bash
psql "$SUPABASE_DB_URL" << 'EOF'
\echo '=========================================='
\echo '⚡ PERFORMANCE ISSUES AUDIT'
\echo '=========================================='
\echo ''

-- Check 1: Missing indexes on foreign keys
\echo '1. Foreign keys without indexes:'
[Same as Check 4 above]
\echo ''

-- Check 2: Tables without indexes (except very small tables)
\echo '2. Tables without any indexes (excluding tiny tables):'
SELECT
  t.tablename,
  pg_size_pretty(pg_total_relation_size('public.' || t.tablename)) AS size
FROM pg_tables t
WHERE t.schemaname = 'public'
  AND NOT EXISTS (
    SELECT 1
    FROM pg_indexes idx
    WHERE idx.tablename = t.tablename
      AND idx.schemaname = t.schemaname
  )
  AND pg_total_relation_size('public.' || t.tablename) > 8192;  -- > 8KB
\echo ''

-- Check 3: Unused indexes
\echo '3. Unused indexes (0 scans, size > 1MB):'
SELECT
  schemaname,
  tablename,
  indexname,
  pg_size_pretty(pg_relation_size(indexrelid)) AS size,
  idx_scan
FROM pg_stat_user_indexes
WHERE schemaname = 'public'
  AND idx_scan = 0
  AND indexname NOT LIKE '%_pkey'  -- Exclude primary keys
  AND pg_relation_size(indexrelid) > 1024*1024;  -- > 1MB
\echo ''

-- Check 4: Duplicate indexes
\echo '4. Potential duplicate indexes:'
SELECT
  a.tablename,
  a.indexname AS index1,
  b.indexname AS index2
FROM pg_indexes a
JOIN pg_indexes b
  ON a.tablename = b.tablename
  AND a.indexname < b.indexname
  AND a.indexdef = b.indexdef
WHERE a.schemaname = 'public';
\echo ''

-- Check 5: Large tables without partitioning
\echo '5. Large tables (>1GB) that might benefit from partitioning:'
SELECT
  tablename,
  pg_size_pretty(pg_total_relation_size('public.' || tablename)) AS size
FROM pg_tables
WHERE schemaname = 'public'
  AND pg_total_relation_size('public.' || tablename) > 1024*1024*1024
ORDER BY pg_total_relation_size('public.' || tablename) DESC;
\echo ''

EOF
```

### 4. Check Security

Audit security configuration:

```bash
psql "$SUPABASE_DB_URL" << 'EOF'
\echo '=========================================='
\echo '🔒 SECURITY AUDIT'
\echo '=========================================='
\echo ''

-- Check 1: Tables without RLS
\echo '1. Tables without Row Level Security enabled:'
SELECT
  schemaname,
  tablename,
  rowsecurity
FROM pg_tables
WHERE schemaname = 'public'
  AND rowsecurity = false;
\echo ''

-- Check 2: Tables with RLS but no policies
\echo '2. Tables with RLS enabled but no policies:'
SELECT
  t.schemaname,
  t.tablename
FROM pg_tables t
WHERE t.schemaname = 'public'
  AND t.rowsecurity = true
  AND NOT EXISTS (
    SELECT 1
    FROM pg_policies p
    WHERE p.schemaname = t.schemaname
      AND p.tablename = t.tablename
  );
\echo ''

-- Check 3: RLS policy coverage
\echo '3. RLS policy coverage by table:'
SELECT
  t.tablename,
  t.rowsecurity AS rls_enabled,
  COUNT(p.policyname) AS policy_count,
  STRING_AGG(DISTINCT p.cmd, ', ') AS operations
FROM pg_tables t
LEFT JOIN pg_policies p
  ON t.tablename = p.tablename
  AND t.schemaname = p.schemaname
WHERE t.schemaname = 'public'
GROUP BY t.tablename, t.rowsecurity
ORDER BY t.tablename;
\echo ''

-- Check 4: Columns that might contain PII without encryption
\echo '4. Potential PII columns (consider encryption/hashing):'
SELECT
  table_name,
  column_name,
  data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND (
    column_name ILIKE '%ssn%'
    OR column_name ILIKE '%tax_id%'
    OR column_name ILIKE '%passport%'
    OR column_name ILIKE '%credit_card%'
    OR column_name ILIKE '%password%'
  );
\echo ''

EOF
```

### 5. Check Data Integrity

Verify constraints and relationships:

```bash
psql "$SUPABASE_DB_URL" << 'EOF'
\echo '=========================================='
\echo '✅ DATA INTEGRITY AUDIT'
\echo '=========================================='
\echo ''

-- Check 1: Foreign key relationships count
\echo '1. Foreign key relationship summary:'
SELECT
  COUNT(*) AS total_fk_constraints,
  COUNT(DISTINCT table_name) AS tables_with_fks
FROM audit_fks;
\echo ''

-- Check 2: Check constraints count
\echo '2. CHECK constraints summary:'
SELECT
  COUNT(*) AS total_check_constraints
FROM information_schema.check_constraints
WHERE constraint_schema = 'public';
\echo ''

-- Check 3: Unique constraints count
\echo '3. UNIQUE constraints summary:'
SELECT
  COUNT(*) AS total_unique_constraints
FROM information_schema.table_constraints
WHERE constraint_schema = 'public'
  AND constraint_type = 'UNIQUE';
\echo ''

-- Check 4: Tables without any constraints (red flag)
\echo '4. Tables without constraints (potential issues):'
SELECT table_name
FROM information_schema.tables t
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE'
  AND NOT EXISTS (
    SELECT 1
    FROM information_schema.table_constraints
    WHERE table_schema = t.table_schema
      AND table_name = t.table_name
  );
\echo ''

-- Check 5: Orphaned records (FK points to non-existent record)
\echo '5. Checking for orphaned records...'
\echo '   (This check requires custom queries per table)'
\echo '   Example:'
\echo '   SELECT COUNT(*) FROM posts p'
\echo '   WHERE NOT EXISTS (SELECT 1 FROM users u WHERE u.id = p.user_id);'
\echo ''

EOF
```

### 6. Generate Audit Report

Create comprehensive report:

```bash
REPORT_FILE="supabase/docs/schema-audit-$(date +%Y%m%d%H%M%S).md"
mkdir -p supabase/docs

cat > "$REPORT_FILE" << 'MDEOF'
# Database Schema Audit Report

**Date**: $(date -u +"%Y-%m-%d %H:%M:%S UTC")
**Database**: [redacted]
**Auditor**: DB Sage

---

## Executive Summary

- Tables audited: {count}
- Total database size: {size}
- Critical issues: {critical_count}
- Warnings: {warning_count}
- Recommendations: {rec_count}

**Overall Score**: {score}/100

---

## Critical Issues 🔴

### 1. Tables without Primary Keys
{list_of_tables}

**Impact**: Cannot uniquely identify rows, replication issues
**Fix**: Add UUID or SERIAL primary key

---

### 2. Foreign Keys without Indexes
{list_of_fks}

**Impact**: Slow JOIN queries, slow ON DELETE CASCADE
**Fix**: Create indexes on FK columns

---

## Warnings ⚠️

### 3. Missing Timestamps
{list_of_tables_without_timestamps}

**Impact**: No audit trail, cannot track record creation/modification
**Fix**: Add created_at, updated_at columns

---

### 4. Tables without RLS
{list_of_tables_without_rls}

**Impact**: Security risk in multi-tenant applications
**Fix**: Enable RLS and create policies

---

## Recommendations 💡

### 5. Performance Optimizations
- Add indexes on frequently queried columns
- Consider partitioning for tables > 1GB
- Remove unused indexes (saves space, improves write performance)

### 6. Security Hardening
- Encrypt PII columns
- Implement RLS on all user-facing tables
- Add check constraints for data validation

### 7. Naming Conventions
- Use snake_case consistently
- Prefix foreign keys with table name (e.g., user_id not uid)
- Use plural for table names (e.g., users not user)

---

## Detailed Findings

[Include full output from all checks above]

---

## Action Items

Priority | Action | Estimated Effort
---------|--------|------------------
P0 | Add primary keys to {tables} | 1 hour
P0 | Index foreign keys | 2 hours
P1 | Enable RLS on {tables} | 4 hours
P1 | Add timestamps | 2 hours
P2 | Optimize indexes | 4 hours

---

## SQL Fixes

```sql
-- Fix 1: Add primary keys
ALTER TABLE {table} ADD COLUMN id UUID PRIMARY KEY DEFAULT gen_random_uuid();

-- Fix 2: Index foreign keys
CREATE INDEX CONCURRENTLY idx_{table}_{fk} ON {table}({fk_column});

-- Fix 3: Enable RLS
ALTER TABLE {table} ENABLE ROW LEVEL SECURITY;
CREATE POLICY "{table}_policy" ON {table} FOR ALL TO authenticated
  USING (auth.uid() = user_id);

-- Fix 4: Add timestamps
ALTER TABLE {table} ADD COLUMN created_at TIMESTAMPTZ DEFAULT NOW();
ALTER TABLE {table} ADD COLUMN updated_at TIMESTAMPTZ;
```

MDEOF

echo "✓ Audit report: $REPORT_FILE"
```

---

## Output

Display audit summary:

```
✅ SCHEMA AUDIT COMPLETE

Database: [redacted]
Tables:   {count}
Size:     {size}

Critical Issues: {count} 🔴
Warnings:        {count} ⚠️
Recommendations: {count} 💡

Overall Score: {score}/100

Report: supabase/docs/schema-audit-{timestamp}.md

Top Issues:
1. {issue_1}
2. {issue_2}
3. {issue_3}

Next Steps:
1. Review full report: cat {report_file}
2. Prioritize fixes
3. Create migrations for P0 issues
4. Re-run audit after fixes
```

---

## Scoring Rubric

- **100**: Perfect schema (rare!)
- **90-99**: Excellent, minor improvements
- **80-89**: Good, some best practices missed
- **70-79**: Fair, several issues to address
- **60-69**: Needs work, security or performance risks
- **<60**: Critical issues, not production-ready

---

## Advanced Auditing Tools

### 1. Audit Triggers (Change Tracking)

**Purpose:** Track all changes (INSERT, UPDATE, DELETE) with who, when, what changed

**Implementation:**
```sql
-- Create audit log schema
CREATE SCHEMA IF NOT EXISTS audit;

-- Audit log table
CREATE TABLE audit.logged_actions (
  event_id BIGSERIAL PRIMARY KEY,
  schema_name TEXT NOT NULL,
  table_name TEXT NOT NULL,
  relid OID NOT NULL,
  session_user_name TEXT,
  action_tstamp_tx TIMESTAMPTZ NOT NULL DEFAULT transaction_timestamp(),
  action_tstamp_stm TIMESTAMPTZ NOT NULL DEFAULT statement_timestamp(),
  action_tstamp_clk TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
  transaction_id BIGINT,
  application_name TEXT,
  client_addr INET,
  client_port INTEGER,
  client_query TEXT,
  action TEXT NOT NULL CHECK (action IN ('I','D','U', 'T')),
  row_data JSONB,
  changed_fields JSONB,
  statement_only BOOLEAN NOT NULL DEFAULT false
);

CREATE INDEX idx_audit_relid ON audit.logged_actions(relid);
CREATE INDEX idx_audit_action_tstamp ON audit.logged_actions(action_tstamp_tx);
CREATE INDEX idx_audit_table_name ON audit.logged_actions(table_name);

-- Generic audit trigger function
CREATE OR REPLACE FUNCTION audit.if_modified_func()
RETURNS TRIGGER AS $$
DECLARE
  audit_row audit.logged_actions;
  excluded_cols TEXT[] = ARRAY[]::TEXT[];
BEGIN
  IF TG_WHEN <> 'AFTER' THEN
    RAISE EXCEPTION 'audit.if_modified_func() may only run as an AFTER trigger';
  END IF;

  audit_row = ROW(
    nextval('audit.logged_actions_event_id_seq'),  -- event_id
    TG_TABLE_SCHEMA::TEXT,                         -- schema_name
    TG_TABLE_NAME::TEXT,                           -- table_name
    TG_RELID,                                      -- relid
    session_user::TEXT,                            -- session_user_name
    current_timestamp,                             -- action_tstamp_tx
    statement_timestamp(),                         -- action_tstamp_stm
    clock_timestamp(),                             -- action_tstamp_clk
    txid_current(),                                -- transaction_id
    current_setting('application_name'),           -- application_name
    inet_client_addr(),                            -- client_addr
    inet_client_port(),                            -- client_port
    current_query(),                               -- client_query
    substring(TG_OP,1,1),                          -- action
    NULL,                                          -- row_data (set below)
    NULL,                                          -- changed_fields (set below)
    false                                          -- statement_only
  );

  IF TG_OP = 'UPDATE' AND TG_LEVEL = 'ROW' THEN
    audit_row.row_data = to_jsonb(OLD);
    audit_row.changed_fields = jsonb_build_object(
      'old', to_jsonb(OLD),
      'new', to_jsonb(NEW)
    );
  ELSIF TG_OP = 'DELETE' AND TG_LEVEL = 'ROW' THEN
    audit_row.row_data = to_jsonb(OLD);
  ELSIF TG_OP = 'INSERT' AND TG_LEVEL = 'ROW' THEN
    audit_row.row_data = to_jsonb(NEW);
  ELSE
    RAISE EXCEPTION '[audit.if_modified_func] - Trigger func added as trigger for unhandled case: %, %',TG_OP, TG_LEVEL;
    RETURN NULL;
  END IF;

  INSERT INTO audit.logged_actions VALUES (audit_row.*);
  RETURN NULL;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Apply to tables (example)
CREATE TRIGGER audit_trigger_row
  AFTER INSERT OR UPDATE OR DELETE ON users
  FOR EACH ROW EXECUTE FUNCTION audit.if_modified_func();
```

**Benefits:**
- Complete audit trail of all changes
- Forensic analysis capabilities
- Compliance requirements (GDPR, SOX, HIPAA)
- Debugging production issues

### 2. pgAudit Extension (PostgreSQL Auditing)

**Purpose:** Comprehensive session and object audit logging

```sql
-- Install extension
CREATE EXTENSION IF NOT EXISTS pgaudit;

-- Configure (in postgresql.conf or ALTER SYSTEM)
ALTER SYSTEM SET pgaudit.log = 'write';  -- Log all writes
ALTER SYSTEM SET pgaudit.log_catalog = off;  -- Don't log catalog queries
ALTER SYSTEM SET pgaudit.log_parameter = on;  -- Include parameter values
ALTER SYSTEM SET pgaudit.log_relation = on;  -- Include table names
ALTER SYSTEM SET pgaudit.log_statement_once = off;  -- Log each statement

-- Reload configuration
SELECT pg_reload_conf();

-- Example: Audit specific table
CREATE ROLE auditor;
GRANT SELECT, INSERT, UPDATE, DELETE ON users TO auditor;
ALTER ROLE auditor SET pgaudit.log = 'write';
```

**What gets logged:**
- All DDL operations (CREATE, ALTER, DROP)
- All DML operations (INSERT, UPDATE, DELETE) based on config
- Parameter values (for forensics)
- Session information

### 3. pgTAP Extension (Database Testing)

**Purpose:** Unit tests for database schema, constraints, and data

**Installation:**
```sql
CREATE EXTENSION IF NOT EXISTS pgtap;
```

**Example test suite:**
```sql
-- File: tests/schema_tests.sql
BEGIN;
SELECT plan(10);  -- Number of tests

-- Test 1: Check table exists
SELECT has_table('public', 'users', 'users table exists');

-- Test 2: Check primary key
SELECT has_pk('public', 'users', 'users has primary key');

-- Test 3: Check specific columns
SELECT has_column('public', 'users', 'id', 'users.id exists');
SELECT has_column('public', 'users', 'email', 'users.email exists');
SELECT has_column('public', 'users', 'created_at', 'users.created_at exists');

-- Test 4: Check column types
SELECT col_type_is('public', 'users', 'id', 'uuid', 'users.id is UUID');
SELECT col_type_is('public', 'users', 'email', 'text', 'users.email is TEXT');

-- Test 5: Check NOT NULL constraints
SELECT col_not_null('public', 'users', 'email', 'users.email is NOT NULL');

-- Test 6: Check foreign keys
SELECT has_fk('public', 'posts', 'posts has foreign key');

-- Test 7: Check indexes
SELECT has_index('public', 'users', 'idx_users_email', 'email index exists');

SELECT * FROM finish();
ROLLBACK;
```

**Run tests:**
```bash
psql "$DB_URL" -f tests/schema_tests.sql
```

**CI/CD Integration:**
```yaml
# .github/workflows/test.yml
- name: Run pgTAP tests
  run: |
    pg_prove --dbname "$DB_URL" tests/*.sql
```

### 4. Named Constraints (Best Practice)

**Why naming matters:**
- Error messages become informative
- Easier to troubleshoot constraint violations
- Explicit documentation of business rules

**Examples:**
```sql
-- ❌ BAD: Unnamed constraints
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email TEXT UNIQUE,
  age INTEGER CHECK (age >= 18)
);
-- Error: "violates check constraint users_age_check" (cryptic!)

-- ✅ GOOD: Named constraints with descriptive names
CREATE TABLE users (
  id UUID CONSTRAINT users_pkey PRIMARY KEY,
  email TEXT CONSTRAINT users_email_unique UNIQUE,
  age INTEGER CONSTRAINT users_age_must_be_adult CHECK (age >= 18),
  created_at TIMESTAMPTZ CONSTRAINT users_created_at_required NOT NULL,
  status TEXT CONSTRAINT users_status_valid CHECK (status IN ('active', 'suspended', 'deleted'))
);
-- Error: "violates check constraint users_age_must_be_adult" (clear!)
```

**Naming conventions:**
```
{table}_{column}_{type}
{table}_{columns}_{type}

Types:
- pkey: Primary key
- fkey: Foreign key
- unique: Unique constraint
- check: Check constraint
- idx: Index
```

**Audit query for unnamed constraints:**
```sql
-- Find constraints without descriptive names
SELECT
  conname AS constraint_name,
  conrelid::regclass AS table_name,
  contype AS constraint_type
FROM pg_constraint
WHERE connamespace = 'public'::regnamespace
  AND (
    -- Auto-generated names (PostgreSQL pattern)
    conname ~ '_pkey$|_key$|_fkey$|_check$|_not_null$'
    AND NOT conname ~ '^[a-z]+_[a-z_]+_(pkey|fkey|unique|check|required|valid)'
  )
ORDER BY conrelid::regclass::TEXT, conname;
```

---

## References

- [PostgreSQL Best Practices](https://wiki.postgresql.org/wiki/Don't_Do_This)
- [Supabase RLS Best Practices](https://supabase.com/docs/guides/auth/row-level-security)
- [Database Design Best Practices](https://www.postgresql.org/docs/current/ddl.html)
- [PostgreSQL Audit Trigger](https://wiki.postgresql.org/wiki/Audit_trigger)
- [pgAudit Extension](https://www.pgaudit.org/)
- [pgTAP Documentation](https://pgtap.org/)


## Referência: references/squad/tasks/supabase-setup.md

# Task: Supabase Setup Guide

| Field | Value |
|-------|-------|
| **execution_type** | `Hybrid` |
| **pattern** | EXEC-HY-001 |
| **script** | `scripts/db-ops/detect-database.sh` |
| **rationale** | Worker valida conectividade inicial; escolhas de provisionamento e credenciais exigem confirmacao humana |

**Purpose**: Interactive guide to set up Supabase project with best practices

**Elicit**: true

---

## 🚀 NEW: Use Automated Database Detection (RECOMMENDED PRE-FLIGHT)

```bash
# Detect whichever database connection is available
./squads/db-sage/scripts/db-ops/detect-database.sh

# Re-run after exporting SUPABASE_DB_URL or DATABASE_URL
./squads/db-sage/scripts/db-ops/detect-database.sh

# Benefits:
#   - Automatic connection detection
#   - Early connectivity validation
#   - Fast preflight before the manual Supabase setup flow below
```

**OR continue with manual Supabase setup below:**

---

## Overview

This task guides you through setting up a new Supabase project with optimal configuration and DB Sage integration.

---

## Process

### 1. Prerequisites Check

Verify required tools:

```bash
echo "Checking prerequisites..."

# Check Supabase CLI
if command -v supabase >/dev/null 2>&1; then
  echo "✓ Supabase CLI: $(supabase --version)"
else
  echo "❌ Supabase CLI not installed"
  echo "   Install: https://supabase.com/docs/guides/cli"
  exit 1
fi

# Check psql
if command -v psql >/dev/null 2>&1; then
  echo "✓ psql: $(psql --version)"
else
  echo "⚠️  psql not found (optional but recommended)"
fi

# Check git
if command -v git >/dev/null 2>&1; then
  echo "✓ git: $(git --version)"
else
  echo "⚠️  git not found (recommended for version control)"
fi

echo ""
```

### 2. Choose Setup Path

Present options:

```
Supabase Setup Options:

1. NEW PROJECT - Create new Supabase project from scratch
2. EXISTING PROJECT - Link to existing Supabase project
3. LOCAL ONLY - Set up local development environment only

Select option (1/2/3):
```

### 3a. New Project Path

If option 1 selected:

```bash
echo "Creating new Supabase project..."

# Login to Supabase
echo "Step 1: Login to Supabase"
supabase login

# Create project
echo ""
echo "Step 2: Create project on Supabase dashboard"
echo "  → Go to: https://supabase.com/dashboard"
echo "  → Click 'New Project'"
echo "  → Enter details:"
read -p "    Project name: " PROJECT_NAME
read -p "    Organization: " ORG_NAME
read -p "    Region (default: us-east-1): " REGION
REGION=${REGION:-us-east-1}
read -sp "    Database password (strong!): " DB_PASSWORD
echo ""

echo ""
echo "✓ Project created on dashboard"
echo "  Wait 2-3 minutes for provisioning..."
read -p "  Press Enter when ready..."
```

### 3b. Existing Project Path

If option 2 selected:

```bash
echo "Linking existing Supabase project..."

# List projects
echo "Your Supabase projects:"
supabase projects list

read -p "Enter project reference ID: " PROJECT_REF

# Link project
supabase link --project-ref "$PROJECT_REF"

echo "✓ Project linked"
```

### 3c. Local Only Path

If option 3 selected:

```bash
echo "Setting up local Supabase environment..."

# Initialize local setup
supabase init

# Start local Supabase
echo "Starting local Supabase (Docker required)..."
supabase start

echo "✓ Local Supabase running"
echo "  Studio: http://localhost:54323"
echo "  API: http://localhost:54321"
```

### 4. Initialize DB Sage Structure

Create recommended folder structure:

```bash
echo "Initializing DB Sage project structure..."

# Run db-bootstrap task internally
mkdir -p supabase/{migrations,seeds,tests,rollback,docs,snapshots}

# Create .env.local (gitignored)
cat > .env.local << 'EOF'
# Supabase Configuration
# DO NOT COMMIT THIS FILE

# Project Details
SUPABASE_PROJECT_ID={project_ref}
SUPABASE_PROJECT_NAME={project_name}

# Database URLs
# Connection pooler (port 6543) for serverless/edge functions
SUPABASE_DB_URL_POOLER=postgresql://postgres:[PASSWORD]@db.[PROJECT_REF].supabase.co:6543/postgres

# Direct connection (port 5432) for migrations
SUPABASE_DB_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT_REF].supabase.co:5432/postgres

# API Keys
SUPABASE_URL=https://[PROJECT_REF].supabase.co
SUPABASE_ANON_KEY=[ANON_KEY]
SUPABASE_SERVICE_ROLE_KEY=[SERVICE_ROLE_KEY]
EOF

echo "✓ DB Sage structure created"
echo "✓ .env.local template created (UPDATE WITH YOUR KEYS!)"
```

### 5. Verify Ignore Policy

Confirm your local ignore policy already covers sensitive files:

```bash
echo "Review your existing ignore rules before proceeding:"
echo "  - .env.local"
echo "  - .env.production"
echo "  - supabase/.branches"
echo "  - supabase/.temp"
echo "  - supabase/snapshots/*.sql"
echo "  - supabase/rollback/*.sql"
echo "  - /tmp/dbsage_*"
echo "  - *.dump"
echo "  - *.backup"
echo ""
echo "DB Sage does not mutate .gitignore automatically."
```

### 6. Set Up Environment Variables

Guide user through configuration:

```
Setting up environment variables...

1. Get your project keys from Supabase Dashboard:
   → https://supabase.com/dashboard/project/{project_ref}/settings/api

2. Update .env.local with:
   - Database password
   - Project reference ID
   - Anon key
   - Service role key (keep secret!)

3. Export the values for the current shell:
   set -a && source .env.local && set +a

4. Verify connection:
   DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
   psql "$DB_URL" -c "SELECT version();"

Press Enter when complete...
```

### 7. Apply Initial Schema

Create baseline schema:

```bash
echo "Setting up initial schema..."

# Check if migrations exist
if [ -z "$(ls -A supabase/migrations 2>/dev/null)" ]; then
  echo "No migrations found."
  echo "Options:"
  echo "  1. Generate schema from design document"
  echo "  2. Import existing schema"
  echo "  3. Skip (will create later)"
  read -p "Select option (1/2/3): " SCHEMA_OPTION

  if [ "$SCHEMA_OPTION" = "1" ]; then
    # Use domain modeling task
    echo "→ Run: *domain-modeling to create schema"
  elif [ "$SCHEMA_OPTION" = "2" ]; then
    read -p "Path to existing schema SQL file: " SCHEMA_FILE
    cp "$SCHEMA_FILE" "supabase/migrations/$(date +%Y%m%d%H%M%S)_initial_schema.sql"
    echo "✓ Migration file created"
  fi
else
  echo "✓ Migrations directory already has files"
fi
```

### 8. Enable Recommended Extensions

Install useful PostgreSQL extensions:

```bash
echo "Enabling recommended extensions..."

DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
psql "$DB_URL" << 'EOF'
-- Core extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";      -- UUID generation
CREATE EXTENSION IF NOT EXISTS "pgcrypto";       -- Encryption functions
CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";  -- Query performance tracking

-- Supabase extensions
CREATE EXTENSION IF NOT EXISTS "pgjwt";          -- JWT functions
CREATE EXTENSION IF NOT EXISTS "pg_net";         -- HTTP client

-- Optional: Full-text search
CREATE EXTENSION IF NOT EXISTS "pg_trgm";        -- Trigram matching

-- Optional: PostGIS (if using geospatial data)
-- CREATE EXTENSION IF NOT EXISTS "postgis";

SELECT 'Extensions enabled' AS status;
EOF

echo "✓ Extensions enabled"
```

### 9. Configure Database Settings

Apply recommended settings:

```bash
echo "Applying recommended database settings..."

DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
psql "$DB_URL" << 'EOF'
-- Performance settings (adjust based on your tier)
-- These are set at session level - for permanent changes, use Supabase dashboard

-- Enable auto_explain for slow queries (dev only)
-- ALTER SYSTEM SET auto_explain.log_min_duration = 1000;  -- Log queries > 1s
-- ALTER SYSTEM SET auto_explain.log_analyze = on;

-- Work memory for complex queries
SET work_mem = '16MB';

-- Statement timeout to prevent runaway queries
SET statement_timeout = '30s';

-- Lock timeout to prevent long lock waits
SET lock_timeout = '10s';

SELECT 'Settings configured' AS status;
EOF

echo "✓ Database settings configured"
echo "  (For permanent settings, use Supabase Dashboard → Database → Settings)"
```

### 10. Set Up Development Workflow

Configure recommended workflow:

```bash
echo "Setting up development workflow..."

# Create helpful scripts
mkdir -p scripts

cat > scripts/db-connect.sh << 'EOF'
#!/bin/bash
# Connect to Supabase database
set -a
source .env.local
set +a
DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
psql "$DB_URL"
EOF

cat > scripts/db-reset-local.sh << 'EOF'
#!/bin/bash
# Reset local Supabase database
supabase db reset
EOF

chmod +x scripts/*.sh

echo "✓ Helper scripts created in scripts/"
```

---

## Output

Display setup summary:

```
✅ SUPABASE SETUP COMPLETE

Project: {project_name}
Region: {region}
Status: Ready for development

Environment:
✓ Supabase CLI configured
✓ Project linked/created
✓ DB Sage structure initialized
✓ Extensions enabled
✓ .env.local created (REMEMBER TO UPDATE!)
✓ No automatic .gitignore mutation performed

Folder Structure:
supabase/
├── migrations/    # Database migrations
├── seeds/         # Seed data
├── tests/         # SQL tests
├── docs/          # Documentation
└── snapshots/     # Backup snapshots

Next Steps:
1. Update .env.local with your keys
2. Test connection: `DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}" && psql "$DB_URL"`
3. Design your schema: *domain-modeling
4. Create first migration: *create-migration
5. Set up RLS policies: *create-rls-policies

Useful Commands:
- Connect to DB: ./scripts/db-connect.sh
- Create migration: supabase migration new {name}
- Push changes: supabase db push
- Pull remote: supabase db pull

Documentation:
- Supabase Docs: https://supabase.com/docs
- DB Sage Guide: docs/architecture/db-sage/README.md
```

---

## Common Next Steps

### 1. Create Initial Schema

```bash
# Option A: Interactive modeling
*domain-modeling

# Option B: Create migration manually
supabase migration new initial_schema
# Edit: supabase/migrations/{timestamp}_initial_schema.sql
```

### 2. Set Up Row Level Security

```bash
# Create RLS policies
*create-rls-policies

# Or manually:
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
CREATE POLICY "users_own_data" ON users
  FOR ALL TO authenticated
  USING (auth.uid() = id);
```

### 3. Add Seed Data

```bash
# Create seed file
supabase migration new seed_initial_data

# Or use DB Sage:
*seed supabase/migrations/{timestamp}_seed.sql
```

### 4. Test Migration Workflow

```bash
# Create snapshot
*snapshot baseline

# Test migration
*dry-run supabase/migrations/{file}.sql

# Apply
*apply-migration supabase/migrations/{file}.sql

# Verify
*smoke-test v1.0
```

---

## Supabase CLI Cheat Sheet

```bash
# Project Management
supabase projects list              # List all projects
supabase link --project-ref {ref}  # Link to project
supabase status                     # Show project status

# Local Development
supabase init                       # Initialize local setup
supabase start                      # Start local Supabase
supabase stop                       # Stop local Supabase
supabase db reset                   # Reset local database

# Migrations
supabase migration new {name}       # Create new migration
supabase db push                    # Push migrations to remote
supabase db pull                    # Pull remote schema
supabase db diff                    # Compare local vs remote

# Functions (Edge Functions)
supabase functions new {name}       # Create new function
supabase functions serve            # Run functions locally
supabase functions deploy {name}    # Deploy function

# Secrets
supabase secrets set {name}={value} # Set secret
supabase secrets list               # List secrets
```

---

## Troubleshooting

### Issue 1: Connection Refused

**Error:** `could not connect to server`

**Fix:**
1. Check database is running (Dashboard → Database → Connection info)
2. Verify password in .env.local
3. Check firewall allows port 5432/6543
4. Try connection pooler (port 6543) instead

### Issue 2: SSL Error

**Error:** `SSL connection has been closed unexpectedly`

**Fix:**
Add `?sslmode=require` to connection string:
```bash
postgresql://postgres:password@db.ref.supabase.co:5432/postgres?sslmode=require
```

### Issue 3: Permission Denied

**Error:** `permission denied for schema public`

**Fix:**
Use service_role key for admin operations, or grant permissions:
```sql
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON ALL TABLES IN SCHEMA public TO postgres;
```

---

## References

- [Supabase CLI Documentation](https://supabase.com/docs/guides/cli)
- [Supabase Local Development](https://supabase.com/docs/guides/cli/local-development)
- [PostgreSQL Connection Strings](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING)
- [DB Sage Documentation](docs/architecture/db-sage/README.md)


## Referência: references/squad/templates/backup-metadata.json.tmpl

```text
{
  "snapshot_id": "{{snapshot_id}}",
  "created_at": "{{created_at}}",
  "database": "{{database}}",
  "environment": "{{environment}}",
  "description": "{{description}}"
}
```


## Referência: references/squad/templates/db-analysis-template.yaml

```yaml
# Database Analysis Template (KISS-Enforced)
# Use this template for squad database analysis
# Forces validation of reality BEFORE proposing schema changes

analysis_metadata:
  analysis_type: squad_database_analysis
  squad_name: null  # e.g., "my-squad", "etl", "analytics"
  squad_version: null
  analyst: "DB Sage"
  analysis_date: null  # ISO8601
  template_version: "1.0.0"

# ===========================================================================
# PHASE 1: REALITY CHECK (MANDATORY - Must complete before proceeding)
# ===========================================================================
current_state:
  # Does the system work today?
  system_works: null  # true / false
  evidence:
    command_executed: null  # e.g., "@course-architect *new test-course"
    output_proof: null  # e.g., "✅ Course generated: outputs/courses/test-course/"
    files_created: []  # List actual files that prove it works

  # Where is state stored?
  state_location: null  # "filesystem" / "memory" / "database" / "api" / "hybrid"
  state_details:
    filesystem_paths: []  # e.g., ["outputs/courses/{slug}/", "outputs/minds/{slug}/"]
    database_tables: []  # e.g., ["content_pieces", "minds"]
    memory_scope: null  # e.g., "process-local", "session", "persistent cache"
    api_endpoints: []  # e.g., ["POST /api/courses", "GET /api/minds"]

  # Code analysis
  code_analysis:
    total_loc: null  # Lines of code
    key_modules: []  # e.g., ["lib/course_validator.py", "lib/state_manager.py"]
    data_flow_summary: null  # Where does data originate, transform, and persist?
    persistence_layer: null  # "files", "database", "both", "none"

  # Critical question: What breaks without database?
  what_breaks_without_db: null  # "nothing" / "X feature" / "Y query"

  # GATE: If system works + state is filesystem + nothing breaks → STOP HERE
  recommendation_if_no_pain: null  # "Keep filesystem approach (KISS)"

# ===========================================================================
# PHASE 2: PAIN VALIDATION (MUST ASK USER - No assumptions allowed)
# ===========================================================================
user_pain_points:
  # Did you ask the user?
  user_interviewed: null  # true / false
  interview_date: null  # ISO8601

  # Core questions
  has_problem: null  # true / false
  problem_description: null  # Specific, not generic
  problem_frequency: null  # "daily" / "weekly" / "monthly" / "rarely" / "once"
  problem_impact: null  # "high" / "medium" / "low"

  # Context
  affects_who: null  # "all users" / "some users" / "edge case"
  workarounds_exist: null  # true / false
  workaround_description: null  # How do they handle it today?

  # Evidence (exact words)
  user_quote: null  # "I can't find courses by keyword" or "No problem, works fine"

  # GATE: If has_problem = false → STOP HERE
  recommendation_if_no_problem: null  # "Keep current approach"

# ===========================================================================
# PHASE 3: EXISTING SCHEMA (CHECK BEFORE CREATING NEW)
# ===========================================================================
existing_schema:
  # Schema inspection
  schema_inspected: null  # true / false
  database_url: null  # Supabase URL or local path
  schema_version: null  # e.g., "v0.7.0"

  # Tables found
  tables_found: []
    # Example:
    # - name: "content_pieces"
    #   fields: ["id", "project_id", "type", "title", "content", "voice_fidelity_score"]
    #   relevant_to_pain: true
    #   reason: "Could store course metadata here"

  # Relevance analysis
  relevant_tables: []  # Subset of tables_found that could help
  relevant_fields: []  # Existing fields that are useful

  # Hypothesis: Can existing tables solve the pain?
  can_solve_with_existing: null  # true / false / partially
  reasoning: null  # Why existing schema works or doesn't work

  # Minimal changes to existing schema
  minimal_changes_to_existing: []
    # Example:
    # - table: "content_pieces"
    #   operation: "ALTER TABLE"
    #   changes:
    #     - "ADD COLUMN file_path TEXT"
    #     - "ADD COLUMN persona_mind_id UUID REFERENCES minds(id)"
    #   solves_pain_how: "Enables finding courses by persona/keyword"

  # GATE: If can_solve_with_existing = true → Propose minimal changes, don't create new tables

# ===========================================================================
# PHASE 4: MINIMAL PROPOSAL (Only if justified by Phase 1-3)
# ===========================================================================
minimal_proposal:
  # Approach selection
  approach: null  # "no_change" / "add_fields" / "new_table" / "multiple_tables"

  # Option 0: No database change needed
  option_0_no_change:
    applicable: null  # true / false
    solution: null  # e.g., "Bash script: ls outputs/courses/ | wc -l"
    effort_hours: null  # 0 hours

  # Option 1: Add fields to existing table
  option_1_add_fields:
    applicable: null  # true / false
    table: null  # e.g., "content_pieces"
    fields_to_add: []
      # Example:
      # - name: "file_path"
      #   type: "TEXT"
      #   purpose: "Link to filesystem location"
      #   nullable: true
    migration_sql: null  # ALTER TABLE statement
    solves_pain_how: null  # Specific explanation
    effort_hours: null  # 1-2 hours

  # Option 2: Create 1 new table (requires justification)
  option_2_new_table:
    applicable: null  # true / false
    justification: null  # Why existing tables can't work (must be technical)
    table_name: null  # e.g., "course_lessons"
    essential_fields_only: []  # MAX 7 fields for MVP
      # Example:
      # - name: "id"
      #   type: "UUID"
      #   purpose: "Primary key"
      # - name: "course_piece_id"
      #   type: "UUID"
      #   purpose: "Foreign key to content_pieces"
    foreign_keys: []  # List FK relationships
    indexes: []  # Only essential indexes
    migration_sql: null  # CREATE TABLE statement
    solves_pain_how: null
    effort_hours: null  # 3-5 hours

  # Option 3: Multiple tables (requires extraordinary justification)
  option_3_multiple_tables:
    applicable: null  # true / false
    extraordinary_justification: null  # Must be compelling, technical reason
    tables: []  # List of tables with fields
    total_effort_hours: null  # 1+ days

  # Selected approach (after user input)
  selected_approach: null  # User chooses after seeing trade-offs

# ===========================================================================
# PHASE 5: TRADE-OFFS (MANDATORY - Let user decide)
# ===========================================================================
trade_offs:
  # Filesystem approach
  option_filesystem:
    name: "Keep Filesystem (No Database Changes)"
    pros: []
      # Example:
      # - "Zero migration effort"
      # - "Git-friendly (text files)"
      # - "Simple, no SQL knowledge needed"
      # - "No RLS complexity"
    cons: []
      # Example:
      # - "No SQL queries"
      # - "Manual search with grep/find"
      # - "No cross-machine centralization"
    effort_hours: 0
    complexity_added: "none"

  # Minimal database approach
  option_minimal_db:
    name: "Minimal Database Integration"
    pros: []
      # Example:
      # - "SQL queries enabled"
      # - "Centralized state"
      # - "Analytics possible"
    cons: []
      # Example:
      # - "Migration required (DDL + Python code)"
      # - "RLS policies needed for security"
      # - "Code changes in 5-8 modules"
      # - "Testing overhead"
    effort_hours: null  # Estimate based on approach
    complexity_added: "low" / "medium" / "high"

  # Comparison table
  comparison:
    simplicity_winner: null  # "filesystem" / "database" / "tie"
    queryability_winner: null  # "filesystem" / "database"
    effort_winner: null  # "filesystem" / "database"

  # Recommendation
  recommendation: null  # Your technical recommendation WITH reasoning
  user_preference_priority: null  # "simplicity" / "queryability" / "undecided"

  # Final decision
  let_user_decide: true  # Always true - never assume database is better

# ===========================================================================
# VALIDATION & SAFETY CHECKS
# ===========================================================================
validation_checklist:
  - step: "checked_system_works_today"
    completed: false
    evidence: null

  - step: "asked_user_about_pain"
    completed: false
    evidence: null

  - step: "reviewed_existing_schema"
    completed: false
    evidence: null

  - step: "proposed_minimum_change"
    completed: false
    evidence: null

  - step: "showed_trade_offs"
    completed: false
    evidence: null

  - step: "let_user_decide"
    completed: false
    evidence: null

# Red flags check
red_flags:
  proposing_3plus_tables_without_request: false
  proposing_10plus_fields_without_pain: false
  assuming_analytics_without_evidence: false
  designing_for_future_not_current: false
  did_not_check_existing_schema: false
  over_engineering_beyond_problem: false

  # If ANY red flag = true → FAIL, do not proceed
  any_red_flags: false  # Auto-calculated

# Final gate
final_gate:
  all_validations_passed: false  # Must be true to proceed
  recommendation: null  # "proceed_with_minimal" / "keep_filesystem" / "blocked_by_red_flags"

# ===========================================================================
# EXECUTION PLAN (Only if validated and approved by user)
# ===========================================================================
execution_plan:
  approved_by_user: false
  approach_chosen: null  # From minimal_proposal.selected_approach

  # If database changes approved
  migration_script_path: null  # e.g., "supabase/migrations/20251027_creator_os.sql"
  python_modules_to_modify: []  # e.g., ["lib/lesson_generator.py", "lib/course_validator.py"]
  estimated_total_effort: null  # hours

  # Rollback plan
  rollback_script_path: null
  rollback_tested: false

  # Testing checklist
  testing_plan:
    - test: "Generate course and verify DB entry"
      completed: false
    - test: "Query by persona/keyword"
      completed: false
    - test: "Verify RLS policies work"
      completed: false

# ===========================================================================
# METADATA
# ===========================================================================
metadata:
  created_at: null
  updated_at: null
  status: "draft"  # "draft" / "validated" / "approved" / "implemented"
  notes: null
```


## Referência: references/squad/templates/index-strategy-tmpl.yaml

```yaml
---
template_name: "Indexing Strategy"
template_version: "1.0.0"
output_format: "markdown"
destination: "index-strategy.md"
description: "Purpose-built index plan tied to access patterns"

sections:
  - id: overview
    title: "Indexing Overview"
    instruction: |
      - Goals: latency targets, load profile
      - Read/Write trade-offs
      - Engine features in use (B-Tree, GIN, GiST, BRIN, partial, covering)
    elicit: true

  - id: patterns
    title: "Access Patterns Mapping"
    instruction: |
      For each frequent query:
      - Query shape & filters
      - ORDER BY requirements
      - Estimated cardinality/selectivity
      - Proposed index(es) with rationale
    elicit: true

  - id: catalog
    title: "Index Catalog"
    instruction: |
      For each table:
      ## table_name
      - Existing indexes (name → columns, where, include)
      - Proposed new indexes
      - Partial indexes (predicates)
      - Covering indexes (INCLUDE)
      - Maintenance notes (bloat risk, reindex cadence)
    elicit: true

  - id: fulltext
    title: "Full-Text & Search"
    instruction: |
      - tsvector generated columns
      - GIN/Trigram usage
      - Ranking functions and query samples
    elicit: true

  - id: maintenance
    title: "Monitoring & Maintenance"
    instruction: |
      - pg_stat_user_indexes + idx scan ratio targets
      - Unused index detection policy
      - Reindex strategy, autovacuum considerations
    elicit: true
```


## Referência: references/squad/templates/migration-plan-tmpl.yaml

````yaml
---
template_name: "Schema Migration Plan"
template_version: "1.0.0"
output_format: "markdown"
destination: "migration-plan.md"
description: "Plan and validate a safe schema migration with rollback and tests"

sections:
  - id: summary
    title: "Executive Summary"
    instruction: |
      Summarize the change:
      - Objective and scope
      - Risk level (Low/Med/High) and why
      - Environments impacted (dev/staging/prod)
      - Expected migration time window and rollback window
    elicit: true

  - id: change-set
    title: "Change Set"
    instruction: |
      Detail every schema change:
      - Tables created/altered/dropped
      - Columns added/modified/removed (types, defaults, constraints)
      - Indexes (create/alter/drop)
      - Functions/triggers/views (create/replace/drop)
      - RLS policies (add/remove/modify)
    elicit: true

  - id: dependencies
    title: "Dependencies & Ordering"
    instruction: |
      List dependencies and execution order:
      1) Extensions
      2) Tables & constraints
      3) Functions
      4) Triggers
      5) RLS
      6) Views / MatViews
      Note any cross-object dependencies that require two-phase rollout.
    elicit: true

  - id: data-migration
    title: "Data Migration & Backfill"
    instruction: |
      Strategies for migrating existing data safely at scale.

      ## Small Data Sets (< 100K rows)

      **Simple approach** for tables with few rows:

      ```sql
      -- Direct UPDATE (< 100K rows)
      UPDATE users SET email_address = email
      WHERE email_address IS NULL;

      -- Single transaction, fast execution
      ```

      **When safe**:
      - Small tables (< 100K rows)
      - Low traffic tables
      - Maintenance window available

      ## Large Data Sets (> 100K rows)

      **Batched approach** prevents table locks and reduces transaction size.

      ### Pattern 1: Basic Batching (Single Process)

      ```sql
      -- Backfill in batches to avoid long locks
      DO $$
      DECLARE
        batch_size INT := 1000;  -- Adjust based on row size and available memory
        rows_updated INT;
        total_updated INT := 0;
        batch_count INT := 0;
      BEGIN
        LOOP
          -- Update one batch
          WITH batch AS (
            SELECT id FROM users
            WHERE email_address IS NULL
            LIMIT batch_size
            FOR UPDATE SKIP LOCKED  -- ⭐ CRITICAL: Avoid lock contention
          )
          UPDATE users
          SET email_address = email
          FROM batch
          WHERE users.id = batch.id;

          GET DIAGNOSTICS rows_updated = ROW_COUNT;
          EXIT WHEN rows_updated = 0;  -- No more rows to process

          total_updated := total_updated + rows_updated;
          batch_count := batch_count + 1;

          RAISE NOTICE 'Batch %: Updated % rows (total: %)',
            batch_count, rows_updated, total_updated;

          -- Throttle to avoid overloading DB
          PERFORM pg_sleep(0.1);  -- 100ms pause between batches
        END LOOP;

        RAISE NOTICE 'Backfill complete: % batches, % total rows',
          batch_count, total_updated;
      END $$;
      ```

      **Key techniques**:
      - `FOR UPDATE SKIP LOCKED` - Avoids lock contention, enables parallel processing
      - `LIMIT batch_size` - Controls transaction size
      - `pg_sleep()` - Throttles load, allows other transactions to proceed
      - `RAISE NOTICE` - Progress tracking

      ### Pattern 2: Parallel Batching (Multiple Workers)

      **For very large tables** (millions of rows), run multiple workers concurrently:

      ```sql
      -- Worker 1 (run in psql session 1)
      DO $$
      DECLARE
        batch_size INT := 5000;
        worker_id INT := 1;
        rows_updated INT;
      BEGIN
        LOOP
          WITH batch AS (
            SELECT id FROM orders
            WHERE status_new IS NULL
            ORDER BY id  -- ⭐ CRITICAL: Deterministic ordering
            LIMIT batch_size
            FOR UPDATE SKIP LOCKED  -- Skip rows locked by other workers
          )
          UPDATE orders
          SET status_new = status
          FROM batch
          WHERE orders.id = batch.id;

          GET DIAGNOSTICS rows_updated = ROW_COUNT;
          EXIT WHEN rows_updated = 0;

          RAISE NOTICE '[Worker %] Updated % rows', worker_id, rows_updated;
          PERFORM pg_sleep(0.05);  -- Shorter pause with multiple workers
        END LOOP;
      END $$;

      -- Worker 2-4: Same script, different worker_id in RAISE NOTICE
      ```

      **Why it works**:
      - `FOR UPDATE SKIP LOCKED` allows workers to grab different rows
      - Each worker skips rows locked by others
      - No deadlocks or contention
      - Near-linear speedup (4 workers ≈ 4x faster)

      ### Pattern 3: Progress Tracking Table

      **Track progress** for resumable migrations:

      ```sql
      -- Create progress tracking table
      CREATE TABLE migration_progress (
        migration_name TEXT PRIMARY KEY,
        last_processed_id BIGINT,
        total_processed BIGINT DEFAULT 0,
        started_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW()
      );

      -- Resumable backfill with progress tracking
      DO $$
      DECLARE
        batch_size INT := 5000;
        last_id BIGINT;
        rows_updated INT;
        migration TEXT := 'users_email_address_backfill';
      BEGIN
        -- Get last processed ID (resume from failure)
        SELECT COALESCE(last_processed_id, 0) INTO last_id
        FROM migration_progress
        WHERE migration_name = migration;

        -- Initialize if not exists
        INSERT INTO migration_progress (migration_name, last_processed_id)
        VALUES (migration, 0)
        ON CONFLICT (migration_name) DO NOTHING;

        LOOP
          -- Process batch starting after last_id
          WITH batch AS (
            SELECT id FROM users
            WHERE id > last_id
              AND email_address IS NULL
            ORDER BY id  -- Deterministic ordering
            LIMIT batch_size
            FOR UPDATE SKIP LOCKED
          )
          UPDATE users
          SET email_address = email
          FROM batch
          WHERE users.id = batch.id
          RETURNING users.id INTO last_id;

          GET DIAGNOSTICS rows_updated = ROW_COUNT;
          EXIT WHEN rows_updated = 0;

          -- Update progress
          UPDATE migration_progress
          SET
            last_processed_id = last_id,
            total_processed = total_processed + rows_updated,
            updated_at = NOW()
          WHERE migration_name = migration;

          RAISE NOTICE '[%] Processed up to ID %, % rows this batch',
            migration, last_id, rows_updated;

          PERFORM pg_sleep(0.1);
        END LOOP;

        RAISE NOTICE '[%] Complete: % total rows',
          migration,
          (SELECT total_processed FROM migration_progress WHERE migration_name = migration);
      END $$;

      -- Check progress (run in separate session)
      SELECT
        migration_name,
        last_processed_id,
        total_processed,
        updated_at,
        AGE(NOW(), updated_at) AS time_since_update
      FROM migration_progress;
      ```

      **Benefits**:
      - Resumable on failure/cancellation
      - Live progress monitoring
      - Deterministic (no duplicate processing)

      ## Batch Size Guidelines

      **Factors to consider**:
      - Row size (larger rows → smaller batches)
      - Available memory (`maintenance_work_mem`)
      - Transaction timeout limits
      - Lock contention sensitivity

      **Recommended sizes**:
      | Row Size | Batch Size | Reasoning |
      |----------|------------|-----------|
      | Small (< 1KB) | 5,000-10,000 | Fast, low memory |
      | Medium (1-10KB) | 1,000-5,000 | Balance speed/memory |
      | Large (> 10KB) | 100-1,000 | Avoid memory exhaustion |
      | JSONB/text heavy | 500-2,000 | Variable size risk |

      ## Throttling Strategies

      ```sql
      -- Light throttle (10 batches/sec, low impact)
      PERFORM pg_sleep(0.1);

      -- Medium throttle (5 batches/sec, safer for production)
      PERFORM pg_sleep(0.2);

      -- Heavy throttle (2 batches/sec, minimal impact)
      PERFORM pg_sleep(0.5);

      -- Adaptive throttle (based on DB load)
      -- Check pg_stat_activity connection count
      SELECT pg_sleep(
        CASE
          WHEN (SELECT count(*) FROM pg_stat_activity WHERE state = 'active') > 50
          THEN 0.5  -- High load, slow down
          ELSE 0.1  -- Normal load, faster
        END
      );
      ```

      ## Verification Queries

      ```sql
      -- Check completion
      SELECT COUNT(*) AS remaining
      FROM users
      WHERE email_address IS NULL;
      -- Expected: 0

      -- Check data integrity
      SELECT COUNT(*) AS mismatches
      FROM users
      WHERE email != email_address;
      -- Expected: 0 (or acceptable threshold)

      -- Sample verification
      SELECT id, email, email_address
      FROM users
      WHERE email != email_address
        OR email_address IS NULL
      LIMIT 100;

      -- Performance check (should use index)
      EXPLAIN ANALYZE
      SELECT * FROM users WHERE email_address IS NULL;
      -- Look for "Index Scan" not "Seq Scan"
      ```

      ## Lock Impact Analysis

      ```sql
      -- Monitor locks during backfill
      SELECT
        pid,
        usename,
        query_start,
        state,
        wait_event_type,
        wait_event,
        query
      FROM pg_stat_activity
      WHERE state != 'idle'
        AND query LIKE '%users%'
      ORDER BY query_start;

      -- Check for lock contention
      SELECT
        locktype,
        relation::regclass AS table_name,
        mode,
        granted,
        COUNT(*) AS lock_count
      FROM pg_locks
      WHERE relation::regclass::text LIKE '%users%'
      GROUP BY locktype, relation, mode, granted;
      ```

      ## Best Practices Summary

      1. **Use FOR UPDATE SKIP LOCKED** for parallelizable batching
      2. **ORDER BY** for deterministic processing (resumable)
      3. **Batch size 1,000-10,000** depending on row size
      4. **Throttle with pg_sleep()** to reduce DB load
      5. **Track progress** in separate table
      6. **Monitor locks** during execution
      7. **Verify data** before and after migration
      8. **Test in staging** with production-size data

      ## When NOT to Use Batching

      - Tables < 100K rows (direct UPDATE faster)
      - Maintenance window available (faster without throttling)
      - No other traffic (no contention risk)

      ## Common Pitfalls

      - **Forgetting FOR UPDATE SKIP LOCKED** → deadlocks with parallel workers
      - **No ORDER BY** → non-deterministic, duplicate processing
      - **Too large batches** → lock contention, memory issues
      - **No throttling** → DB overload, affects production traffic
      - **No progress tracking** → can't resume on failure
    elicit: true

  - id: safety
    title: "Safety & Rollback"
    instruction: |
      Safety plan:
      - Pre-migration snapshot strategy
      - Rollback script outline (what to undo, in order)
      - Roll-forward strategy if rollback is unsafe
      - Advisory locks to avoid concurrent runs
    elicit: true

  - id: testing
    title: "Testing Strategy"
    instruction: |
      Tests to run:
      - Dry-run (BEGIN; \i file; ROLLBACK)
      - Smoke tests (post-migration)
      - RLS positive/negative tests (impersonation)
      - Performance baselines & EXPLAIN checks on hot paths
    elicit: true

  - id: operations
    title: "Operational Runbook"
    instruction: |
      Provide exact commands with placeholders:
      - Set env, check psql/pg_dump versions
      - Take snapshot
      - Apply migration
      - Post snapshot
      - Run smoke tests
      Include expected outputs and success criteria.
    elicit: true

  - id: communication
    title: "Communication & Approval"
    instruction: |
      - Stakeholders, approvers
      - Change window notice
      - Post-deploy validation owners
      - Incident/rollback contact path
    elicit: true

  - id: version-tracking
    title: "Schema Version Tracking"
    instruction: |
      DB Sage uses custom schema_migrations table for enhanced tracking beyond Supabase's built-in migration system.

      ## Setup (run once in initial migration)

      ```sql
      CREATE TABLE IF NOT EXISTS public.schema_migrations (
        version TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        applied_at TIMESTAMPTZ DEFAULT NOW(),
        applied_by TEXT NOT NULL,
        execution_time_ms INTEGER,
        success BOOLEAN NOT NULL DEFAULT false,
        checksum TEXT NOT NULL,        -- SHA256 do arquivo de migration
        rollback_script TEXT,           -- Script de rollback
        notes TEXT,
        CONSTRAINT valid_checksum CHECK (length(checksum) = 64),
        CONSTRAINT valid_version CHECK (version ~ '^\d{14}$')  -- Format: YYYYMMDDHHmmss
      );

      CREATE INDEX idx_migrations_applied_at
        ON schema_migrations(applied_at DESC);

      CREATE INDEX idx_migrations_success
        ON schema_migrations(success) WHERE success = false;

      COMMENT ON TABLE schema_migrations IS
        'Custom migration tracking with checksums, rollback scripts, and execution metadata';
      ```

      ## Migration File Structure

      Every migration should follow this template:

      ```sql
      -- Migration: 20251027120000_add_users_table
      -- Checksum: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
      -- Applied by: user@example.com
      -- Rollback: See section at end of file

      BEGIN;

      -- Record migration start
      INSERT INTO public.schema_migrations (
        version, name, applied_by, success, checksum, rollback_script, notes
      )
      VALUES (
        '20251027120000',
        'add_users_table',
        current_user,
        false,  -- Will update to true on success
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        $rollback$
          -- Rollback script
          DROP TABLE IF EXISTS users CASCADE;
          DELETE FROM public.schema_migrations WHERE version = '20251027120000';
        $rollback$,
        'Initial users table creation'
      )
      ON CONFLICT (version) DO NOTHING;

      -- Migration DDL/DML statements here
      CREATE TABLE users (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW()
      );

      -- Update to success
      UPDATE public.schema_migrations
      SET
        success = true,
        execution_time_ms = EXTRACT(MILLISECOND FROM (NOW() - applied_at))::INTEGER
      WHERE version = '20251027120000';

      COMMIT;

      -- ROLLBACK SECTION (DO NOT EXECUTE - stored in schema_migrations table)
      /*
      BEGIN;
      DROP TABLE IF EXISTS users CASCADE;
      DELETE FROM public.schema_migrations WHERE version = '20251027120000';
      COMMIT;
      */
      ```

      ## Checksum Generation

      Generate SHA256 checksum before applying migration:

      ```bash
      # Generate checksum (exclude rollback section)
      checksum=$(sha256sum migration.sql | awk '{print $1}')
      echo "Checksum: $checksum"

      # Verify against stored checksum after application
      psql -c "SELECT version, checksum FROM schema_migrations WHERE version = '20251027120000'"
      ```

      ## Query Migration History

      ```sql
      -- Recent successful migrations
      SELECT
        version,
        name,
        applied_at,
        applied_by,
        execution_time_ms,
        notes
      FROM schema_migrations
      WHERE success = true
      ORDER BY applied_at DESC
      LIMIT 10;

      -- Failed migrations (investigate)
      SELECT
        version,
        name,
        applied_at,
        applied_by,
        notes
      FROM schema_migrations
      WHERE success = false
      ORDER BY applied_at DESC;

      -- Pending rollbacks
      SELECT
        version,
        name,
        applied_at,
        LENGTH(rollback_script) AS rollback_size_bytes
      FROM schema_migrations
      WHERE success = true
        AND rollback_script IS NOT NULL
      ORDER BY applied_at DESC;

      -- Checksum verification (detect tampering)
      SELECT
        version,
        name,
        checksum,
        applied_at
      FROM schema_migrations
      WHERE success = true
      ORDER BY applied_at DESC;
      ```

      ## Integration with Supabase CLI

      Supabase CLI manages migrations in `supabase/migrations/` directory with timestamp prefix.
      Our schema_migrations table complements this by adding:
      - WHO applied the migration (applied_by)
      - WHEN exactly (applied_at)
      - SUCCESS status (for partial failures)
      - CHECKSUM verification (integrity)
      - ROLLBACK script (automated recovery)

      Use both systems together:
      - Supabase CLI for development workflow (`supabase db diff`, `supabase db reset`)
      - schema_migrations for production audit trail and rollback capability

      ## Rollback Execution

      To rollback a migration:

      ```sql
      -- 1. Retrieve rollback script
      SELECT rollback_script
      FROM schema_migrations
      WHERE version = '20251027120000';

      -- 2. Execute rollback script (in transaction)
      BEGIN;
      -- Copy rollback script here
      DROP TABLE IF EXISTS users CASCADE;
      DELETE FROM public.schema_migrations WHERE version = '20251027120000';
      COMMIT;

      -- 3. Verify rollback
      SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'users';
      -- Should return 0
      ```
    elicit: false

  - id: zero-downtime
    title: "Zero-Downtime Migrations"
    instruction: |
      Use expand/contract pattern for non-breaking schema changes. Forward-only migrations that allow
      old and new application versions to coexist.

      ## Overview - Expand/Contract Pattern

      Zero-downtime migrations use 4-6 phases:

      1. **EXPAND** - Add new schema (additive only, backward compatible)
      2. **DEPLOY v2** - Deploy app version writing to both old and new schema
      3. **BACKFILL** - Migrate existing data (batched, throttled)
      4. **VALIDATE** - Verify data integrity
      5. **DEPLOY v3** - Deploy app version reading from new schema only
      6. **CONTRACT** - Remove old schema (after all apps updated)

      ## Pattern 1: Add Column (Safe - No Downtime)

      Adding a column with constant default is safe per PostgreSQL docs:
      "Adding a column with a constant default value does not require each row to be updated."

      ```sql
      -- PHASE 1: EXPAND (safe, instant)
      ALTER TABLE users ADD COLUMN bio TEXT DEFAULT '';

      -- No other phases needed - existing app ignores new column
      ```

      ## Pattern 2: Rename Column (Requires Expand/Contract)

      **Unsafe**:
      ```sql
      ALTER TABLE users RENAME COLUMN email TO email_address;  -- ❌ BREAKS OLD APP
      ```

      **Safe** (6 phases):

      **PHASE 1: EXPAND** (add new column + sync trigger):
      ```sql
      -- Add new column
      ALTER TABLE users ADD COLUMN email_address TEXT;

      -- Trigger to keep columns in sync
      CREATE OR REPLACE FUNCTION sync_email_columns()
      RETURNS TRIGGER AS $$
      BEGIN
        IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
          -- Sync both directions
          NEW.email_address := COALESCE(NEW.email_address, NEW.email);
          NEW.email := COALESCE(NEW.email, NEW.email_address);
        END IF;
        RETURN NEW;
      END;
      $$ LANGUAGE plpgsql;

      CREATE TRIGGER sync_email
        BEFORE INSERT OR UPDATE ON users
        FOR EACH ROW EXECUTE FUNCTION sync_email_columns();
      ```

      **PHASE 2: DEPLOY v2** (app writes to BOTH columns):
      ```typescript
      // App version 2 - dual writes
      await db.query(
        'INSERT INTO users (email, email_address) VALUES ($1, $1)',
        [email]
      )
      ```

      **PHASE 3: BACKFILL** (migrate existing data in batches):
      ```sql
      -- Backfill in batches (avoid long table locks)
      DO $$
      DECLARE
        batch_size INT := 1000;
        rows_updated INT;
        total_updated INT := 0;
      BEGIN
        LOOP
          -- Update one batch
          WITH batch AS (
            SELECT id FROM users
            WHERE email_address IS NULL
            LIMIT batch_size
            FOR UPDATE SKIP LOCKED  -- Avoid lock contention
          )
          UPDATE users
          SET email_address = email
          FROM batch
          WHERE users.id = batch.id;

          GET DIAGNOSTICS rows_updated = ROW_COUNT;
          EXIT WHEN rows_updated = 0;

          total_updated := total_updated + rows_updated;
          RAISE NOTICE 'Backfilled % rows (total: %)', rows_updated, total_updated;

          -- Throttle to avoid overloading DB
          PERFORM pg_sleep(0.1);
        END LOOP;

        RAISE NOTICE 'Backfill complete: % total rows updated', total_updated;
      END $$;
      ```

      **PHASE 4: VALIDATE** (verify data integrity):
      ```sql
      -- Check all data migrated
      SELECT COUNT(*) FROM users WHERE email_address IS NULL;
      -- Expected: 0

      -- Check data consistency
      SELECT COUNT(*) FROM users WHERE email != email_address;
      -- Expected: 0 (or acceptable threshold for dirty data)

      -- Sample verification
      SELECT id, email, email_address
      FROM users
      WHERE email != email_address OR email_address IS NULL
      LIMIT 10;
      ```

      **PHASE 5: DEPLOY v3** (app reads from email_address only):
      ```typescript
      // App version 3 - reads from new column
      await db.query('SELECT email_address FROM users WHERE id = $1', [id])
      ```

      **PHASE 6: CONTRACT** (remove old column and trigger):
      ```sql
      -- Drop sync trigger and function
      DROP TRIGGER IF EXISTS sync_email ON users;
      DROP FUNCTION IF EXISTS sync_email_columns();

      -- Remove old column
      ALTER TABLE users DROP COLUMN email;

      -- Optional: Rename to canonical name
      ALTER TABLE users RENAME COLUMN email_address TO email;
      ```

      ## Pattern 3: Change Column Type

      **Example**: Change `age INT` → `age NUMERIC(5,2)`

      **PHASE 1: EXPAND**:
      ```sql
      ALTER TABLE users ADD COLUMN age_new NUMERIC(5,2);

      -- Sync trigger (optional if app will write)
      CREATE OR REPLACE FUNCTION sync_age_columns()
      RETURNS TRIGGER AS $$
      BEGIN
        NEW.age_new := NEW.age::NUMERIC(5,2);
        RETURN NEW;
      END;
      $$ LANGUAGE plpgsql;

      CREATE TRIGGER sync_age
        BEFORE INSERT OR UPDATE ON users
        FOR EACH ROW
        WHEN (NEW.age IS NOT NULL)
        EXECUTE FUNCTION sync_age_columns();
      ```

      **PHASE 2: BACKFILL**:
      ```sql
      UPDATE users SET age_new = age::NUMERIC(5,2) WHERE age_new IS NULL;
      ```

      **PHASE 3: APP MIGRATION** → read from age_new

      **PHASE 4: CONTRACT**:
      ```sql
      DROP TRIGGER IF EXISTS sync_age ON users;
      DROP FUNCTION IF EXISTS sync_age_columns();
      ALTER TABLE users DROP COLUMN age;
      ALTER TABLE users RENAME COLUMN age_new TO age;
      ```

      ## Pattern 4: Add NOT NULL Constraint (Requires Data Backfill)

      **Unsafe**:
      ```sql
      ALTER TABLE users ALTER COLUMN email SET NOT NULL;  -- ❌ Fails if NULLs exist
      ```

      **Safe**:

      **PHASE 1: Add default value**:
      ```sql
      ALTER TABLE users ALTER COLUMN email SET DEFAULT 'unknown@example.com';
      ```

      **PHASE 2: Backfill NULLs**:
      ```sql
      UPDATE users SET email = 'unknown@example.com' WHERE email IS NULL;
      ```

      **PHASE 3: Validate**:
      ```sql
      SELECT COUNT(*) FROM users WHERE email IS NULL;  -- Expected: 0
      ```

      **PHASE 4: Add constraint**:
      ```sql
      ALTER TABLE users ALTER COLUMN email SET NOT NULL;
      ```

      ## Pattern 5: CREATE INDEX CONCURRENTLY

      **Always use CONCURRENTLY in production**:

      ```sql
      -- ✅ SAFE (non-blocking)
      CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

      -- ❌ UNSAFE (blocks writes)
      CREATE INDEX idx_users_email ON users(email);
      ```

      CONCURRENTLY allows reads/writes to continue during index creation.

      ## When to Use Zero-Downtime

      **Use expand/contract for**:
      - Column renames
      - Type changes
      - Table splits/merges
      - Adding NOT NULL constraints
      - Removing columns with data

      **Don't need for** (already safe):
      - Adding nullable columns with constant defaults
      - Creating new tables
      - Adding indexes (use CONCURRENTLY)
      - Adding constraints (check, foreign key) to empty tables
      - Renaming tables (if app uses dynamic table names)

      ## Risks & Trade-offs

      **Pros**:
      - Zero downtime
      - Gradual rollout
      - Safe rollback at any phase
      - No maintenance window needed

      **Cons**:
      - Longer deployment cycle (days/weeks vs minutes)
      - Increased complexity (6 phases vs 1)
      - Duplicate data temporarily (storage cost)
      - Requires app coordination (multiple deploys)
      - Sync triggers add write overhead

      ## Decision Tree

      ```
      Does migration break existing app code?
        NO → Standard migration ✅
        YES → Does it affect hot path (high traffic table)?
          NO → Maintenance window OK (document downtime) ✅
          YES → Use expand/contract pattern ✅
      ```

      ## Supabase-Specific Notes

      Supabase emphasizes **forward-only migrations**:
      - No explicit rollback command in CLI
      - Use `supabase db reset` for local development only
      - Production rollbacks require new forward migrations

      This aligns perfectly with expand/contract philosophy:
      Each phase is a separate forward migration.
    elicit: false

  - id: supabase-cli
    title: "Supabase CLI Integration"
    instruction: |
      How DB Sage migration workflow integrates with Supabase CLI.

      ## Supabase CLI Migration Workflow

      ### Local Development

      ```bash
      # 1. Create new migration
      supabase migration new add_users_table

      # 2. Edit migration file in supabase/migrations/<timestamp>_add_users_table.sql

      # 3. Test migration locally
      supabase db reset  # Recreates DB from scratch + applies all migrations

      # 4. Verify changes
      supabase db diff --schema public  # Show diff vs remote

      # 5. Commit migration file
      git add supabase/migrations/<timestamp>_add_users_table.sql
      git commit -m "feat: add users table"
      ```

      ### Staging/Production Deployment

      **CI/CD Pipeline** (GitHub Actions recommended):

      ```yaml
      name: Deploy to Production
      on:
        push:
          branches: [main]

      jobs:
        deploy:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v3

            - name: Setup Supabase CLI
              uses: supabase/setup-cli@v1

            - name: Deploy migrations
              run: supabase db push
              env:
                SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
                SUPABASE_DB_PASSWORD: ${{ secrets.SUPABASE_DB_PASSWORD }}
                SUPABASE_PROJECT_ID: ${{ secrets.SUPABASE_PROJECT_ID }}
      ```

      ### Pulling Remote Schema

      Sync production schema to local:

      ```bash
      # Pull all remote migrations
      supabase db pull

      # Creates: supabase/migrations/<timestamp>_remote_schema.sql
      ```

      **When to use**: After manual changes in Supabase Dashboard.

      ## DB Sage Enhancement Layer

      DB Sage adds custom schema_migrations table **on top** of Supabase CLI:

      | Feature | Supabase CLI | DB Sage schema_migrations |
      |---------|--------------|---------------------------|
      | Version tracking | ✅ Timestamp in filename | ✅ + applied_at |
      | Applied by | ❌ | ✅ current_user |
      | Checksums | ❌ | ✅ SHA256 |
      | Rollback scripts | ❌ | ✅ Stored in table |
      | Success/failure | ❌ | ✅ success boolean |
      | Execution time | ❌ | ✅ execution_time_ms |

      **Use both together**:
      - Supabase CLI for development workflow and deployments
      - schema_migrations for production audit trail

      ## Permission Management

      **Critical**: Migrations created in Supabase Dashboard may have wrong owner.

      ```sql
      -- Fix ownership (run after pulling remote schema)
      ALTER TABLE users OWNER TO postgres;
      ALTER TYPE user_role OWNER TO postgres;
      ALTER FUNCTION get_user_role() OWNER TO postgres;
      ```

      **Best practice**: Create all migrations as SQL files, not via Dashboard.

      ## Migration List & Status

      ```bash
      # Check migration status (local vs remote)
      supabase migration list

      # Output:
      # Local      Remote     Status
      # 20240101   20240101   Applied
      # 20240102   -          Pending
      ```

      ## Rollback Strategy

      Supabase CLI does **not** support explicit rollback.

      **Options**:
      1. **Local**: `supabase db reset` (destructive, dev only)
      2. **Production**: Create new forward migration that undoes changes
      3. **DB Sage**: Use rollback_script from schema_migrations table

      **Example** (using DB Sage):
      ```sql
      -- Retrieve rollback script
      SELECT rollback_script FROM schema_migrations
      WHERE version = '20251027120000';

      -- Execute retrieved script
      ```

      ## Best Practices

      1. **Always test locally** with `supabase db reset` before deploying
      2. **Use CI/CD** for staging/production (not local machine)
      3. **Separate projects** for dev/staging/prod
      4. **Store credentials** as GitHub secrets (never commit)
      5. **Reassign ownership** to postgres after dashboard changes
      6. **Small migrations** (easier to debug, faster to apply)
      7. **Idempotent scripts** (IF NOT EXISTS, DROP IF EXISTS)

      ## Troubleshooting

      **"must be owner of table" error**:
      ```sql
      ALTER TABLE mytable OWNER TO postgres;
      ```

      **Migration applied but not tracked**:
      ```bash
      supabase migration repair <version> --status applied
      ```

      **Reset local DB** (development only):
      ```bash
      supabase db reset
      ```
    elicit: false
````


## Referência: references/squad/templates/migration.sql.tmpl

```text
-- Migration template for DB Sage workflows
-- Replace placeholders before execution.

BEGIN;

-- Example:
-- ALTER TABLE {{table_name}} ADD COLUMN {{column_name}} {{column_type}};

COMMIT;
```


## Referência: references/squad/templates/rls-policies-tmpl.yaml

````yaml
---
template_name: "Supabase RLS Policies"
template_version: "1.0.0"
output_format: "markdown"
destination: "rls-policies.md"
description: "Row Level Security policies for Supabase tables"
---

sections:
  - id: overview
    title: "RLS Overview"
    instruction: |
      Document the Row Level Security strategy:
      
      ## Purpose
      Explain the overall security model and why RLS is being used.
      
      ## Authentication Context
      - How users are authenticated (Supabase Auth, JWT, etc)
      - Available auth context variables:
        - `auth.uid()` - Current user ID
        - `auth.jwt()` - JWT claims
        - `auth.email()` - User email
        - Custom claims in JWT
      
      ## Security Model
      - Role-based access control (RBAC)
      - Multi-tenancy approach (if applicable)
      - Public vs authenticated vs specific role access
      
      ## Performance Considerations
      - RLS policy performance impact
      - Indexing strategy to support policies
      - Caching considerations
      
      ## Testing Strategy
      - How policies will be tested
      - Test users and scenarios
    elicit: true
    
  - id: policy-patterns
    title: "Common Policy Patterns"
    instruction: |
      Document reusable policy patterns used across tables:
      
      ## Pattern 1: Owner-Only Access
      ```sql
      -- Users can only access their own records
      (auth.uid() = user_id)
      ```
      
      ## Pattern 2: Tenant-Based Access
      ```sql
      -- Users can access records in their organization
      (auth.uid() IN (
        SELECT user_id FROM org_members 
        WHERE org_id = table.org_id
      ))
      ```
      
      ## Pattern 3: Role-Based Access
      ```sql
      -- Only admins can access
      ((auth.jwt() ->> 'role')::text = 'admin')
      ```
      
      ## Pattern 4: Public Read, Authenticated Write
      ```sql
      -- SELECT: true (public read)
      -- INSERT/UPDATE/DELETE: auth.uid() IS NOT NULL
      ```
      
      ## Pattern 5: Hierarchical Permissions
      ```sql
      -- Access based on organizational hierarchy
      ```
      
      Document any other patterns specific to your application.
    elicit: true
    
  - id: table-policies
    title: "Table-by-Table Policies"
    instruction: |
      For each table requiring RLS, document comprehensive policies:
      
      # Table: `table_name`
      
      ## Enable RLS
      ```sql
      ALTER TABLE table_name ENABLE ROW LEVEL SECURITY;
      ```
      
      ## SELECT Policies
      
      ### Policy: `policy_name_select`
      **Purpose**: Describe who can read what
      
      **Policy Expression**:
      ```sql
      CREATE POLICY "policy_name_select"
      ON table_name
      FOR SELECT
      TO authenticated -- or public, anon, etc
      USING (
        -- Policy expression
        auth.uid() = user_id
      );
      ```
      
      **Rationale**: Explain the business rule
      
      **Performance**: Any indexes needed to support this policy
      
      ## INSERT Policies
      
      ### Policy: `policy_name_insert`
      **Purpose**: Describe who can create records
      
      **Policy Expression**:
      ```sql
      CREATE POLICY "policy_name_insert"
      ON table_name
      FOR INSERT
      TO authenticated
      WITH CHECK (
        -- Policy expression
        auth.uid() = user_id
      );
      ```
      
      **Validation**: What validations this ensures
      
      ## UPDATE Policies
      
      ### Policy: `policy_name_update`
      **Purpose**: Describe who can modify records
      
      **Policy Expression**:
      ```sql
      CREATE POLICY "policy_name_update"
      ON table_name
      FOR UPDATE
      TO authenticated
      USING (
        -- Who can see the record to update it
        auth.uid() = user_id
      )
      WITH CHECK (
        -- What values they can set
        auth.uid() = user_id
      );
      ```
      
      **Notes**: USING checks old values, WITH CHECK validates new values
      
      ## DELETE Policies
      
      ### Policy: `policy_name_delete`
      **Purpose**: Describe who can delete records
      
      **Policy Expression**:
      ```sql
      CREATE POLICY "policy_name_delete"
      ON table_name
      FOR DELETE
      TO authenticated
      USING (
        -- Who can delete
        auth.uid() = user_id OR
        (auth.jwt() ->> 'role')::text = 'admin'
      );
      ```
      
      ## ALL Policies (if using combined policy)
      
      Sometimes a single policy for all operations is clearer:
      
      ```sql
      CREATE POLICY "policy_name_all"
      ON table_name
      FOR ALL
      TO authenticated
      USING (auth.uid() = user_id)
      WITH CHECK (auth.uid() = user_id);
      ```
      
      ---
      
      Repeat this section for each table.
    elicit: true
    
  - id: public-tables
    title: "Public Tables"
    instruction: |
      Document tables with public read access:
      
      # Table: `public_table_name`
      
      ## Public Read Policy
      ```sql
      ALTER TABLE public_table_name ENABLE ROW LEVEL SECURITY;
      
      CREATE POLICY "public_read_policy"
      ON public_table_name
      FOR SELECT
      TO anon, authenticated
      USING (true);
      ```
      
      ## Restricted Write Policy
      ```sql
      CREATE POLICY "authenticated_write_policy"
      ON public_table_name
      FOR INSERT
      TO authenticated
      WITH CHECK (auth.uid() IS NOT NULL);
      ```
      
      **Rationale**: Why this table is public
      
      **Security Considerations**: What data is safe to expose
    elicit: false
    
  - id: service-role
    title: "Service Role Bypass"
    instruction: |
      Document scenarios where service role (bypass RLS) is used:
      
      ## Service Role Usage
      
      ### Backend Operations
      Operations that need to bypass RLS:
      - Scheduled jobs (cron, edge functions with service key)
      - Admin operations
      - Data migration
      - Analytics aggregation
      
      ### Safety Measures
      - How service key is secured
      - Where service role operations are logged
      - Who has access to service key
      
      ### Alternatives
      When possible, prefer:
      - Security definer functions with RLS
      - Elevated permission policies
      - Temporary privilege escalation
    elicit: false
    
  - id: helper-functions
    title: "Security Helper Functions"
    instruction: |
      Document PostgreSQL functions that support RLS:
      
      ## Function: `check_user_permission`
      ```sql
      CREATE OR REPLACE FUNCTION check_user_permission(
        user_id uuid,
        resource_id uuid,
        permission_type text
      )
      RETURNS boolean
      LANGUAGE plpgsql
      SECURITY DEFINER
      AS $$
      BEGIN
        -- Permission checking logic
        RETURN EXISTS (
          SELECT 1 FROM permissions
          WHERE user_id = $1
          AND resource_id = $2
          AND permission = $3
        );
      END;
      $$;
      ```
      
      **Usage in Policies**:
      ```sql
      USING (check_user_permission(auth.uid(), id, 'read'))
      ```
      
      ## Function: `get_user_org_id`
      ```sql
      CREATE OR REPLACE FUNCTION get_user_org_id()
      RETURNS uuid
      LANGUAGE sql
      STABLE
      AS $$
        SELECT org_id FROM user_profiles
        WHERE user_id = auth.uid();
      $$;
      ```
      
      **Usage in Policies**:
      ```sql
      USING (org_id = get_user_org_id())
      ```
      
      Document all helper functions used in RLS policies.
    elicit: false
    
  - id: multi-tenancy
    title: "Multi-Tenancy Implementation"
    condition: "multi_tenant"
    instruction: |
      If implementing multi-tenancy with RLS:
      
      ## Tenant Isolation Strategy
      
      ### Tenant Identification
      - How tenants are identified (org_id, team_id, etc)
      - Where tenant ID is stored (JWT claim, database lookup)
      
      ### Tenant-Scoped Tables
      
      For each tenant-scoped table:
      
      ```sql
      -- Example: projects table
      CREATE POLICY "tenant_isolation_policy"
      ON projects
      FOR ALL
      TO authenticated
      USING (
        org_id = (auth.jwt() ->> 'org_id')::uuid
      )
      WITH CHECK (
        org_id = (auth.jwt() ->> 'org_id')::uuid
      );
      ```
      
      ### Cross-Tenant Scenarios
      - Shared resources across tenants
      - Super admin access
      - Tenant-to-tenant relationships
      
      ### Performance
      - Indexes on tenant_id columns
      - Query patterns that leverage tenant isolation
    elicit: true

  - id: storage-policies
    title: "Supabase Storage Policies"
    instruction: |
      RLS policies for Supabase Storage buckets (storage.objects table).

      ## Overview

      Supabase Storage uses RLS on the `storage.objects` system table to control file access.
      By default, Storage requires explicit RLS policies - no uploads allowed without policies.

      ## Pattern 1: User-Specific Uploads

      Users can only upload files to their own folder:

      ```sql
      CREATE POLICY "Users upload own avatars"
      ON storage.objects
      FOR INSERT
      TO authenticated
      WITH CHECK (
        bucket_id = 'avatars' AND
        (select auth.uid())::text = (storage.foldername(name))[1]
      );
      ```

      **Folder Structure**: `avatars/{user_id}/filename.jpg`

      **How it works**:
      - `storage.foldername(name)` splits path by `/` returning array
      - `[1]` gets first folder (user_id)
      - Compares with authenticated user's ID

      ## Pattern 2: Public Read, Authenticated Write

      Anyone can view files, only authenticated users can upload:

      ```sql
      -- Public read
      CREATE POLICY "Public avatars readable"
      ON storage.objects
      FOR SELECT
      TO public
      USING (bucket_id = 'avatars');

      -- Authenticated write
      CREATE POLICY "Authenticated upload avatars"
      ON storage.objects
      FOR INSERT
      TO authenticated
      WITH CHECK (bucket_id = 'avatars');
      ```

      **Use case**: Public profile pictures, logos, marketing assets.

      ## Pattern 3: Tenant-Scoped Files

      Users can only access files from their organization:

      ```sql
      CREATE POLICY "Tenant file isolation"
      ON storage.objects
      FOR SELECT
      TO authenticated
      USING (
        bucket_id = 'documents' AND
        (storage.foldername(name))[1] = ((select auth.jwt()) ->> 'org_id')
      );

      CREATE POLICY "Tenant file uploads"
      ON storage.objects
      FOR INSERT
      TO authenticated
      WITH CHECK (
        bucket_id = 'documents' AND
        (storage.foldername(name))[1] = ((select auth.jwt()) ->> 'org_id')
      );
      ```

      **Folder Structure**: `documents/{org_id}/{file_id}.pdf`

      ## Pattern 4: Delete Own Files

      Users can delete their own files:

      ```sql
      CREATE POLICY "Users delete own files"
      ON storage.objects
      FOR DELETE
      TO authenticated
      USING (
        bucket_id = 'avatars' AND
        (select auth.uid())::text = (storage.foldername(name))[1]
      );
      ```

      ## Pattern 5: File Overwriting (upsert)

      For file overwriting via `upsert` option, grant SELECT + UPDATE:

      ```sql
      -- Allow reading (required for upsert check)
      CREATE POLICY "Users read own files"
      ON storage.objects
      FOR SELECT
      TO authenticated
      USING (
        bucket_id = 'avatars' AND
        (select auth.uid())::text = (storage.foldername(name))[1]
      );

      -- Allow updating (for upsert)
      CREATE POLICY "Users update own files"
      ON storage.objects
      FOR UPDATE
      TO authenticated
      USING (
        bucket_id = 'avatars' AND
        (select auth.uid())::text = (storage.foldername(name))[1]
      )
      WITH CHECK (
        bucket_id = 'avatars' AND
        (select auth.uid())::text = (storage.foldername(name))[1]
      );
      ```

      ## Bucket Configuration

      Create buckets with appropriate public/private settings:

      ```sql
      -- Create private bucket (requires policies)
      INSERT INTO storage.buckets (id, name, public)
      VALUES ('avatars', 'avatars', false);

      -- Create public bucket (files publicly accessible by URL)
      INSERT INTO storage.buckets (id, name, public)
      VALUES ('public-images', 'public-images', true);
      ```

      **Note**: Even public buckets respect RLS for uploads/deletes.

      ## Helper Functions

      ```sql
      -- Extract user folder from path
      CREATE OR REPLACE FUNCTION storage.user_owns_file(file_path text)
      RETURNS boolean
      LANGUAGE sql
      STABLE
      AS $$
        SELECT (select auth.uid())::text = (storage.foldername(file_path))[1];
      $$;

      -- Usage in policy
      CREATE POLICY "Users access own files"
      ON storage.objects
      FOR ALL
      TO authenticated
      USING (
        bucket_id = 'private' AND
        storage.user_owns_file(name)
      );
      ```

      ## Security Considerations

      1. **Always validate bucket_id** in policies (prevent cross-bucket access)
      2. **Use folder structure** for user/tenant isolation
      3. **Set appropriate bucket public/private** settings
      4. **Monitor storage size** per user/tenant (implement quotas)
      5. **Validate file types** server-side (policies can't check content)

      ## Testing

      Test storage policies with Supabase client:

      ```typescript
      // Test upload as user A
      const { data, error } = await supabase.storage
        .from('avatars')
        .upload(`${user.id}/avatar.jpg`, file);

      // Should succeed for own folder
      expect(error).toBeNull();

      // Test read as user B (should fail for user A's folder)
      const { data: files, error: listError } = await supabase.storage
        .from('avatars')
        .list(`${otherUserId}/`);

      // Should return empty or error
      expect(files).toHaveLength(0);
      ```

      ## Performance

      Storage policies are evaluated on every file operation.

      **Optimize**:
      - Use simple folder path checks (fast)
      - Avoid complex JOINs in storage policies
      - Cache JWT claims in helper functions
      - Use indexes on bucket_id (already indexed by Supabase)

      ## Common Pitfalls

      - **Forgetting SELECT policy** for upsert operations
      - **Not validating bucket_id** (allows cross-bucket access)
      - **Complex policies** (slow file operations)
      - **Mixing public/private** bucket settings incorrectly
    elicit: false

  - id: performance-optimization
    title: "RLS Performance Optimization"
    instruction: |
      Critical performance optimizations for RLS policies validated by Supabase documentation.

      ## 🚀 Optimization 1: Wrap Auth Functions with SELECT (94.97% faster)

      **Critical Discovery** from Supabase docs: Wrapping auth functions enables query caching.

      ### ❌ SLOW (no caching):
      ```sql
      CREATE POLICY "users_select"
      ON users
      FOR SELECT
      TO authenticated
      USING (auth.uid() = user_id);
      ```

      ### ✅ FAST (cached, 94.97% improvement):
      ```sql
      CREATE POLICY "users_select"
      ON users
      FOR SELECT
      TO authenticated
      USING ((select auth.uid()) = user_id);
      ```

      **Why**: PostgreSQL caches the result of `(select auth.uid())` for the duration of the transaction,
      avoiding repeated function calls.

      **Impact**: **19x faster queries** in high-traffic scenarios.

      **Apply to all auth functions**:
      - `(select auth.uid())`
      - `(select auth.jwt())`
      - `(select auth.email())`

      ## 🚀 Optimization 2: Index Policy Columns (99.94% improvement)

      **Always index columns used in policy expressions.**

      ```sql
      -- Policy uses user_id
      CREATE POLICY "user_policy" ON posts
      USING ((select auth.uid()) = user_id);

      -- Index user_id (99.94% faster)
      CREATE INDEX idx_posts_user_id ON posts(user_id);
      ```

      **Critical indexes**:
      ```sql
      -- Tenant isolation
      CREATE INDEX idx_table_org_id ON table_name(org_id);

      -- Owner-based policies
      CREATE INDEX idx_table_user_id ON table_name(user_id);

      -- Time-based policies
      CREATE INDEX idx_table_scheduling
        ON table_name(publish_at, expire_at)
        WHERE publish_at IS NOT NULL OR expire_at IS NOT NULL;
      ```

      ## 🚀 Optimization 3: Filter Client-Side Explicitly

      **Even with RLS policies, explicitly filter in client queries.**

      ```typescript
      // ❌ Relies only on RLS
      const { data } = await supabase
        .from('users')
        .select('*');  // Returns only own data due to RLS, but query planner doesn't know

      // ✅ Explicit filter (helps query planner)
      const { data } = await supabase
        .from('users')
        .select('*')
        .eq('user_id', userId);  // Query planner can use index
      ```

      **Why**: Explicit filters help PostgreSQL query planner choose optimal index scan.

      ## 🚀 Optimization 4: Specify Roles Explicitly

      ```sql
      -- ❌ Applies to all roles (unnecessary checks)
      CREATE POLICY "policy" ON table USING (...);

      -- ✅ Specific role (fewer checks)
      CREATE POLICY "policy" ON table
      TO authenticated  -- Only authenticated users
      USING (...);
      ```

      **Common roles**:
      - `TO authenticated` - Logged-in users
      - `TO anon` - Anonymous users
      - `TO public` - Both authenticated and anon

      ## 🚀 Optimization 5: Use Security Definer Functions

      **Bypass RLS on join tables** with security definer functions.

      ```sql
      -- ❌ Policy with JOIN (slow, 99.99% slower)
      CREATE POLICY "team_access" ON documents
      USING (
        team_id IN (
          SELECT team_id FROM user_teams
          WHERE user_id = (select auth.uid())
        )
      );

      -- ✅ Security definer function (99.99% improvement)
      CREATE OR REPLACE FUNCTION user_team_ids()
      RETURNS TABLE(team_id UUID)
      LANGUAGE sql
      STABLE
      SECURITY DEFINER
      AS $$
        SELECT team_id FROM user_teams
        WHERE user_id = auth.uid();
      $$;

      CREATE POLICY "team_access" ON documents
      USING (team_id IN (SELECT user_team_ids()));
      ```

      **Why**: Security definer functions run with elevated privileges, bypassing RLS on join tables.

      ## 🚀 Optimization 6: Minimize Joins

      **Avoid joining source and target tables in policies.**

      ```sql
      -- ❌ JOIN in policy (slow)
      CREATE POLICY "org_access" ON documents
      USING (
        EXISTS (
          SELECT 1 FROM users
          WHERE users.id = (select auth.uid())
            AND users.org_id = documents.org_id
        )
      );

      -- ✅ Use JWT claims (no JOIN)
      CREATE POLICY "org_access" ON documents
      USING (
        org_id = ((select auth.jwt()) ->> 'org_id')::uuid
      );
      ```

      **Strategy**: Store necessary claims in JWT (org_id, role, tenant_id).

      ## Performance Checklist

      Apply to every RLS policy:

      - [ ] Wrap `auth.uid()` with `(select auth.uid())`
      - [ ] Index all columns used in USING/WITH CHECK
      - [ ] Specify role explicitly (TO authenticated vs TO public)
      - [ ] Use JWT claims instead of JOINs where possible
      - [ ] Create security definer functions for complex permission checks
      - [ ] Test query plans with EXPLAIN ANALYZE
      - [ ] Filter client-side explicitly

      ## Measuring Performance

      ```sql
      -- Check query plan (look for Sequential Scan vs Index Scan)
      EXPLAIN ANALYZE
      SELECT * FROM users WHERE user_id = 'xxx';

      -- Monitor slow queries
      SELECT
        query,
        calls,
        mean_exec_time,
        max_exec_time
      FROM pg_stat_statements
      WHERE query LIKE '%users%'
      ORDER BY mean_exec_time DESC
      LIMIT 10;
      ```

      ## Real-World Impact

      **Before optimization**:
      - Query time: 250ms
      - Database CPU: 80%
      - Queries/sec: 40

      **After optimization** (wrapped functions + indexes):
      - Query time: 12ms (95% improvement)
      - Database CPU: 15%
      - Queries/sec: 800 (20x increase)
    elicit: false

  - id: advanced-patterns
    title: "Advanced RLS Patterns"
    instruction: |
      Advanced RLS patterns beyond basic owner-only and tenant isolation.

      ## Pattern 6: Time-Based Access (Scheduled Content)

      **Use case**: Blog posts with scheduled publishing, promotions with expiration, time-limited content.

      ```sql
      CREATE POLICY "scheduled_content"
      ON posts
      FOR SELECT
      TO authenticated
      USING (
        (publish_at IS NULL OR publish_at <= NOW()) AND
        (expire_at IS NULL OR expire_at > NOW())
      );
      ```

      **How it works**:
      - `publish_at IS NULL` - No schedule, always visible
      - `publish_at <= NOW()` - Past publish date, visible
      - `expire_at IS NULL` - No expiration, always visible
      - `expire_at > NOW()` - Not expired, visible

      **Performance**:
      ```sql
      -- Index for time-based queries
      CREATE INDEX idx_posts_scheduling
      ON posts(publish_at, expire_at)
      WHERE publish_at IS NOT NULL OR expire_at IS NOT NULL;
      ```

      **Client-side filtering** (helps query planner):
      ```typescript
      const { data } = await supabase
        .from('posts')
        .select('*')
        .lte('publish_at', new Date().toISOString())
        .or('publish_at.is.null')
        .gte('expire_at', new Date().toISOString())
        .or('expire_at.is.null');
      ```

      ## Pattern 7: Hierarchical Organizations (Detailed)

      **Use case**: Org > Team > User hierarchy with different access levels.

      ### Simple Hierarchy (Org-Level):
      ```sql
      CREATE POLICY "org_hierarchy"
      ON resources
      FOR SELECT
      TO authenticated
      USING (
        org_id IN (
          SELECT org_id
          FROM user_org_memberships
          WHERE user_id = (select auth.uid())
        )
      );
      ```

      **User sees resources from ALL orgs they belong to.**

      ### Complex Hierarchy (Org + Team):
      ```sql
      -- Option 1: User sees resources from their teams
      CREATE POLICY "team_hierarchy"
      ON resources
      FOR SELECT
      TO authenticated
      USING (
        team_id IN (
          SELECT team_id
          FROM user_team_memberships
          WHERE user_id = (select auth.uid())
        )
      );

      -- Option 2: Combined (org admin sees all, team member sees team only)
      CREATE POLICY "combined_hierarchy"
      ON resources
      FOR SELECT
      TO authenticated
      USING (
        -- Org admin sees all resources in org
        (
          org_id IN (
            SELECT org_id
            FROM user_org_memberships
            WHERE user_id = (select auth.uid()) AND role = 'admin'
          )
        )
        OR
        -- Team member sees only team resources
        (
          team_id IN (
            SELECT team_id
            FROM user_team_memberships
            WHERE user_id = (select auth.uid())
          )
        )
      );
      ```

      **Performance**:
      ```sql
      -- Indexes for hierarchy lookups
      CREATE INDEX idx_user_org_memberships_user
        ON user_org_memberships(user_id, org_id);

      CREATE INDEX idx_user_team_memberships_user
        ON user_team_memberships(user_id, team_id);

      CREATE INDEX idx_resources_org_id ON resources(org_id);
      CREATE INDEX idx_resources_team_id ON resources(team_id);
      ```

      **Optimization** (security definer function):
      ```sql
      CREATE OR REPLACE FUNCTION user_accessible_orgs()
      RETURNS TABLE(org_id UUID)
      LANGUAGE sql
      STABLE
      SECURITY DEFINER
      AS $$
        SELECT org_id FROM user_org_memberships
        WHERE user_id = auth.uid();
      $$;

      CREATE POLICY "org_hierarchy_optimized"
      ON resources
      FOR SELECT
      TO authenticated
      USING (org_id IN (SELECT user_accessible_orgs()));
      ```

      ## Pattern 8: Role-Based with Custom Claims (Advanced)

      **Use case**: Different permissions per role (admin, manager, analyst, user).

      ### Setup: Add role to JWT
      ```sql
      CREATE OR REPLACE FUNCTION custom_access_token_hook(event jsonb)
      RETURNS jsonb AS $$
      DECLARE
        claims jsonb;
        user_role text;
        user_org_id uuid;
      BEGIN
        -- Get user role and org from profiles table
        SELECT role, org_id INTO user_role, user_org_id
        FROM public.user_profiles
        WHERE user_id = (event->>'user_id')::uuid;

        -- Add to JWT claims
        claims := event->'claims';
        claims := jsonb_set(claims, '{role}', to_jsonb(user_role));
        claims := jsonb_set(claims, '{org_id}', to_jsonb(user_org_id));

        RETURN jsonb_set(event, '{claims}', claims);
      END;
      $$ LANGUAGE plpgsql SECURITY DEFINER;
      ```

      **Configure in Supabase Dashboard**: Authentication > Hooks > Custom Access Token

      ### Policy: Role-Based Access
      ```sql
      -- Admin sees all
      CREATE POLICY "admin_full_access"
      ON sensitive_data
      FOR ALL
      TO authenticated
      USING (
        ((select auth.jwt()) ->> 'role') = 'admin'
      );

      -- Manager sees org data
      CREATE POLICY "manager_org_access"
      ON sensitive_data
      FOR SELECT
      TO authenticated
      USING (
        ((select auth.jwt()) ->> 'role') = 'manager' AND
        org_id = ((select auth.jwt()) ->> 'org_id')::uuid
      );

      -- User sees own data only
      CREATE POLICY "user_own_access"
      ON sensitive_data
      FOR SELECT
      TO authenticated
      USING (
        ((select auth.jwt()) ->> 'role') = 'user' AND
        user_id = (select auth.uid())
      );
      ```

      ### Policy: Role Hierarchy (Admin > Manager > User)
      ```sql
      CREATE POLICY "role_hierarchy"
      ON resources
      FOR ALL
      TO authenticated
      USING (
        CASE ((select auth.jwt()) ->> 'role')
          WHEN 'admin' THEN true  -- Admin sees everything
          WHEN 'manager' THEN org_id = ((select auth.jwt()) ->> 'org_id')::uuid
          ELSE user_id = (select auth.uid())  -- User sees own only
        END
      );
      ```

      ## Pattern 9: Multi-Factor Authentication (AAL2)

      **Use case**: Sensitive operations require MFA.

      ```sql
      CREATE POLICY "mfa_required_for_sensitive_ops"
      ON sensitive_operations
      FOR INSERT
      TO authenticated
      USING (
        ((select auth.jwt()) ->> 'aal') = 'aal2'  -- Assurance Level 2 (MFA)
      );
      ```

      **AAL levels**:
      - `aal1` - Single factor (password only)
      - `aal2` - Multi-factor (password + OTP/biometric)

      ## Pattern 10: IP-Based Restrictions

      **Use case**: Restrict admin operations to office IP.

      ```sql
      CREATE POLICY "admin_office_only"
      ON admin_operations
      FOR ALL
      TO authenticated
      USING (
        ((select auth.jwt()) ->> 'role') = 'admin' AND
        inet_client_addr() << '192.168.1.0/24'::inet  -- Office network
      );
      ```

      **Note**: `inet_client_addr()` returns client IP.

      ## Advanced Patterns Summary

      | Pattern | Use Case | Complexity | Performance Impact |
      |---------|----------|------------|-------------------|
      | Time-based | Scheduled content | Low | Low (with index) |
      | Hierarchical | Org > Team > User | Medium | Medium (needs indexes) |
      | Role-based claims | RBAC | Low | Low (JWT cached) |
      | AAL2 MFA | Sensitive ops | Low | None |
      | IP restrictions | Office-only | Low | None |

      **Best practices**:
      - Prefer JWT claims over database lookups (faster)
      - Always index columns used in policies
      - Use security definer functions for complex checks
      - Test with EXPLAIN ANALYZE
      - Wrap auth functions with SELECT for caching
    elicit: false

  - id: testing
    title: "RLS Testing Strategy"
    instruction: |
      How to test and validate RLS policies:
      
      ## Unit Tests
      
      Test individual policies with different auth contexts:
      
      ```sql
      -- Test as user A
      SET request.jwt.claims = '{"sub": "user-a-uuid"}';
      SELECT * FROM table_name; -- Should only see user A's records
      
      -- Test as user B
      SET request.jwt.claims = '{"sub": "user-b-uuid"}';
      SELECT * FROM table_name; -- Should only see user B's records
      ```
      
      ## Integration Tests
      
      Test with actual Supabase client:
      
      ```typescript
      // Test authenticated access
      const { data, error } = await supabase
        .from('table_name')
        .select('*');
      
      // Verify only authorized records returned
      ```
      
      ## Security Audit
      
      Checklist for RLS validation:
      - [ ] All tables with sensitive data have RLS enabled
      - [ ] No accidental policy holes (test with unauthorized users)
      - [ ] Service role usage is documented and justified
      - [ ] Policies perform well (no slow queries)
      - [ ] Cross-tenant data leakage tested
      - [ ] Anonymous vs authenticated access verified
      - [ ] Edge cases tested (null values, missing context)
      
      ## Automated Testing
      
      Script or framework for continuous validation.
    elicit: false
    
  - id: migration
    title: "RLS Migration Scripts"
    instruction: |
      Concrete SQL migration for implementing these policies:
      
      ## Migration: `YYYYMMDDHHMMSS_add_rls_policies.sql`
      
      ```sql
      -- Enable RLS on tables
      ALTER TABLE table1 ENABLE ROW LEVEL SECURITY;
      ALTER TABLE table2 ENABLE ROW LEVEL SECURITY;
      
      -- Drop existing policies if re-running
      DROP POLICY IF EXISTS "policy_name" ON table_name;
      
      -- Create policies
      CREATE POLICY "policy_name_select"
      ON table_name
      FOR SELECT
      TO authenticated
      USING (auth.uid() = user_id);
      
      CREATE POLICY "policy_name_insert"
      ON table_name
      FOR INSERT
      TO authenticated
      WITH CHECK (auth.uid() = user_id);
      
      -- ... additional policies ...
      
      -- Create indexes to support policies
      CREATE INDEX IF NOT EXISTS idx_table_user_id 
      ON table_name(user_id);
      
      -- Grant permissions
      GRANT SELECT, INSERT, UPDATE, DELETE ON table_name TO authenticated;
      GRANT SELECT ON table_name TO anon;
      ```
      
      ## Rollback Migration
      
      ```sql
      -- Remove policies
      DROP POLICY IF EXISTS "policy_name_select" ON table_name;
      DROP POLICY IF EXISTS "policy_name_insert" ON table_name;
      
      -- Disable RLS
      ALTER TABLE table_name DISABLE ROW LEVEL SECURITY;
      ```
    elicit: false
    
  - id: monitoring
    title: "RLS Monitoring & Debugging"
    instruction: |
      How to monitor and debug RLS policies:
      
      ## Query Performance
      
      Identify slow queries caused by RLS:
      
      ```sql
      -- Check query plans
      EXPLAIN ANALYZE
      SELECT * FROM table_name;
      ```
      
      ## Policy Effectiveness
      
      Verify policies are being applied:
      
      ```sql
      -- Check active policies
      SELECT schemaname, tablename, policyname, permissive, roles, cmd, qual
      FROM pg_policies
      WHERE tablename = 'your_table';
      ```
      
      ## Common Issues
      
      ### Issue: Policy not applying
      - Check RLS is enabled on table
      - Verify user role matches policy target
      - Check auth context is set correctly
      
      ### Issue: Performance degradation
      - Add indexes for policy columns
      - Simplify policy expressions
      - Consider denormalization
      
      ### Issue: Unexpected access
      - Audit all policies on table
      - Check for permissive vs restrictive policies
      - Verify no service role leakage
      
      ## Logging
      
      Log policy violations or unexpected access patterns.
    elicit: false
    
  - id: best-practices
    title: "RLS Best Practices"
    instruction: |
      ## Design Principles
      
      1. **Start Restrictive**: Default deny, explicitly allow
      2. **Minimize Policy Complexity**: Simpler policies are easier to audit
      3. **Use Helper Functions**: Encapsulate complex logic
      4. **Index Policy Columns**: Performance is critical
      5. **Test Extensively**: Security bugs are costly
      6. **Document Everything**: Future you will thank you
      7. **Audit Regularly**: Policies drift over time
      8. **Avoid Service Role**: Use it only when absolutely necessary
      
      ## Common Pitfalls
      
      - Forgetting to enable RLS on new tables
      - Policy expressions with poor performance
      - Not testing with actual user contexts
      - Overly permissive catch-all policies
      - Mixing USING and WITH CHECK incorrectly
      - Not considering null values in policies
      
      ## Security Checklist
      
      - [ ] All sensitive tables have RLS enabled
      - [ ] Policies tested with unauthorized users
      - [ ] Anonymous access limited to public data only
      - [ ] Service role usage is minimal and documented
      - [ ] Policies use indexes for performance
      - [ ] Multi-tenant isolation is verified
      - [ ] Edge cases tested (nulls, empty results)
      - [ ] Policies are documented and reviewed
    elicit: false
````


## Referência: references/squad/templates/rollback.sql.tmpl

```text
-- Rollback template for DB Sage workflows
-- Replace placeholders before execution.

BEGIN;

-- Example:
-- ALTER TABLE {{table_name}} DROP COLUMN IF EXISTS {{column_name}};

COMMIT;
```


## Referência: references/squad/templates/schema-design-tmpl.yaml

```yaml
---
template_name: "Database Schema Design"
template_version: "1.0.0"
output_format: "markdown"
destination: "schema-design.md"
description: "Comprehensive database schema design document for data modeling and implementation"
---

sections:
  - id: overview
    title: "Schema Overview"
    instruction: |
      Create a high-level overview of the database schema including:
      - Purpose and scope of this schema design
      - Target database system (Supabase/PostgreSQL, MySQL, etc)
      - Key business entities being modeled
      - Expected scale (estimated records, growth projections)
      - Performance requirements
      - Security and compliance requirements
    elicit: true
    
  - id: domain-model
    title: "Domain Model"
    instruction: |
      Document the business domain model:
      
      ## Core Entities
      List and describe each core entity in the business domain:
      - Entity name and description
      - Key attributes and their business meaning
      - Lifecycle and state transitions (if applicable)
      - Business rules and invariants
      
      ## Relationships
      Document relationships between entities:
      - Type of relationship (one-to-one, one-to-many, many-to-many)
      - Cardinality and optionality
      - Cascade behaviors
      - Business meaning of the relationship
      
      ## Bounded Contexts
      If using DDD, identify bounded contexts and how entities relate across contexts.
    elicit: true
    
  - id: access-patterns
    title: "Access Patterns & Query Requirements"
    instruction: |
      Document how the data will be accessed:
      
      ## Primary Access Patterns
      List the most common queries and operations:
      1. Pattern description
         - Frequency (requests/second or per day)
         - Latency requirements
         - Involved tables and relationships
         - Expected result size
      
      ## Secondary Access Patterns
      Less frequent but important queries
      
      ## Write Patterns
      - Insert frequency and volume
      - Update patterns
      - Delete/archive patterns
      
      ## Reporting & Analytics
      - Aggregation queries
      - Time-series analysis
      - Cross-entity reports
      
      Use this information to inform schema design and indexing strategy.
    elicit: true
    
  - id: schema-design
    title: "Physical Schema Design"
    instruction: |
      Design the actual database schema:
      
      ## Tables
      For each table, document:
      
      ### `table_name`
      **Purpose**: Brief description
      
      **Columns**:
      | Column | Type | Constraints | Description |
      |--------|------|-------------|-------------|
      | id | uuid | PRIMARY KEY, DEFAULT uuid_generate_v4() | Unique identifier |
      | created_at | timestamptz | NOT NULL, DEFAULT now() | Creation timestamp |
      | updated_at | timestamptz | NOT NULL, DEFAULT now() | Last update timestamp |
      | ... | ... | ... | ... |
      
      **Indexes**:
      - `idx_table_column` (column) - Purpose and query pattern
      
      **Foreign Keys**:
      - `fk_table_other` REFERENCES other_table(id) ON DELETE CASCADE
      
      **Triggers**:
      - `trigger_name` - Purpose
      
      **Notes**:
      - Design decisions and trade-offs
      - Performance considerations
      - Future evolution plans
      
      Repeat for each table.
      
      ## Views
      Document any database views for common query patterns.
      
      ## Materialized Views
      For expensive aggregations or reporting.
    elicit: true
    
  - id: normalization
    title: "Normalization Strategy"
    instruction: |
      Explain normalization decisions:
      
      ## Normalization Level
      - Target normal form (1NF, 2NF, 3NF, BCNF)
      - Rationale for the chosen level
      
      ## Denormalization Decisions
      Document any intentional denormalization:
      - What data is denormalized
      - Why (performance, simplicity, etc)
      - Trade-offs accepted
      - Consistency maintenance strategy
      
      ## Data Redundancy
      - Calculated/derived fields stored for performance
      - Cached aggregations
      - Sync mechanisms
    elicit: true
    
  - id: indexing-strategy
    title: "Indexing Strategy"
    instruction: |
      Comprehensive indexing plan:
      
      ## Index Categories
      
      ### Primary Indexes
      - Primary keys (automatically indexed)
      
      ### Foreign Key Indexes
      - Indexes on foreign key columns for join performance
      
      ### Query-Driven Indexes
      Based on access patterns identified earlier:
      
      **Index Name**: `idx_table_column`
      - **Table**: table_name
      - **Columns**: column1, column2
      - **Type**: B-tree / GiST / GIN / etc
      - **Purpose**: Which queries benefit
      - **Estimated Impact**: Query performance improvement
      - **Cost**: Storage and write overhead
      
      ### Composite Indexes
      Multi-column indexes for complex queries
      
      ### Partial Indexes
      Indexes on subsets of data (WHERE clause)
      
      ### Full-Text Search Indexes
      If using PostgreSQL FTS or similar
      
      ## Index Maintenance
      - Monitoring strategy
      - Reindex schedule if needed
      - Unused index detection
    elicit: true
    
  - id: constraints
    title: "Constraints & Data Integrity"
    instruction: |
      Document all data integrity mechanisms:
      
      ## Primary Keys
      - Choice of UUID vs Sequential ID and rationale
      
      ## Foreign Keys
      - All relationships with cascade rules
      - ON DELETE CASCADE / SET NULL / RESTRICT decisions
      - ON UPDATE behaviors
      
      ## Unique Constraints
      - Natural keys or business uniqueness
      - Composite unique constraints
      
      ## Check Constraints
      - Value range validations
      - Business rule enforcement
      - Enum-like constraints
      
      ## Not Null Constraints
      - Required fields rationale
      
      ## Default Values
      - Sensible defaults for columns
    elicit: true
    
  - id: security
    title: "Security Architecture"
    instruction: |
      Database security design:
      
      ## Authentication
      - How users are identified
      - Session management
      - Token storage if applicable
      
      ## Authorization Model
      - Role-based access control (RBAC)
      - Attribute-based access control (ABAC)
      - Row-level security approach
      
      ## Sensitive Data
      - PII identification
      - Encryption requirements (at-rest, in-transit)
      - Hashing for passwords/secrets
      - Data masking for non-production environments
      
      ## Audit Logging
      - What actions are logged
      - Audit table design
      - Retention policy
      
      ## Compliance
      - GDPR, LGPD, HIPAA, etc considerations
      - Data deletion/anonymization procedures
    elicit: true
    
  - id: supabase-specific
    title: "Supabase-Specific Configuration"
    condition: "using_supabase"
    instruction: |
      If using Supabase, document:
      
      ## RLS Policies
      High-level RLS strategy (detailed policies in separate document):
      - Policy approach per table
      - User context variables used
      - Performance considerations
      
      ## Realtime Configuration
      - Tables with Realtime enabled
      - Publication configuration
      - Client-side subscription patterns
      
      ## Edge Functions
      - Database triggers that call edge functions
      - Integration points
      
      ## Storage Integration
      - File storage buckets
      - Relationship to database tables
      - Access policies
      
      ## Auth Integration
      - auth.users relationship to application tables
      - User metadata storage strategy
      - Multi-tenancy approach
    elicit: true
    
  - id: migration-strategy
    title: "Migration & Evolution Strategy"
    instruction: |
      Plan for schema changes over time:
      
      ## Initial Migration
      - Creation script organization
      - Seed data requirements
      - Initial data population strategy
      
      ## Change Management
      - Migration naming convention
      - Up/Down migration requirements
      - Testing strategy for migrations
      
      ## Versioning
      - Schema version tracking
      - Migration tool (Supabase migrations, Flyway, Liquibase, etc)
      
      ## Backward Compatibility
      - How to handle breaking changes
      - Deprecation process
      - Multi-version support if needed
      
      ## Rollback Strategy
      - When rollbacks are safe
      - Data loss prevention
      - Contingency plans
    elicit: true
    
  - id: performance
    title: "Performance Optimization"
    instruction: |
      Performance considerations and optimizations:
      
      ## Query Optimization
      - Expensive queries identified
      - Optimization strategies
      - Execution plan analysis approach
      
      ## Connection Pooling
      - Pool size configuration
      - Connection lifecycle
      
      ## Caching Strategy
      - What data is cached (Redis, in-memory)
      - Cache invalidation strategy
      - Cache-aside vs write-through
      
      ## Partitioning
      - Table partitioning if needed (time-based, hash-based)
      - Partition key selection
      
      ## Read Replicas
      - If using read replicas
      - Read/write routing strategy
      
      ## Monitoring
      - Key metrics to track
      - Slow query logging
      - Performance baselines
    elicit: true
    
  - id: scalability
    title: "Scalability & Growth"
    instruction: |
      How the schema handles growth:
      
      ## Vertical Scaling
      - Resource limits before vertical scaling needed
      
      ## Horizontal Scaling
      - Sharding strategy if applicable
      - Shard key selection
      - Cross-shard queries handling
      
      ## Data Archival
      - Archival strategy for old data
      - Historical data retention
      - Archive storage location
      
      ## Growth Projections
      - Expected data growth
      - Query load projections
      - Scaling trigger points
    elicit: true
    
  - id: testing
    title: "Testing & Validation"
    instruction: |
      Database testing approach:
      
      ## Unit Tests
      - Database function testing
      - Constraint validation testing
      
      ## Integration Tests
      - Query performance tests
      - Transaction testing
      - Concurrency testing
      
      ## Load Testing
      - Simulated load scenarios
      - Performance benchmarks
      
      ## Data Validation
      - Data quality checks
      - Constraint verification
      - Referential integrity tests
    elicit: false
    
  - id: implementation
    title: "Implementation Plan"
    instruction: |
      Concrete implementation steps:
      
      ## Phase 1: Core Schema
      - Order of table creation
      - Dependencies between tables
      - Estimated timeline
      
      ## Phase 2: Indexes & Constraints
      - Index creation
      - Constraint addition
      - Performance validation
      
      ## Phase 3: Security & RLS
      - RLS policy implementation
      - Security testing
      
      ## Phase 4: Optimization
      - Performance tuning
      - Monitoring setup
      
      ## Rollout
      - Deployment strategy
      - Validation checkpoints
      - Rollback criteria
    elicit: false
    
  - id: appendix
    title: "Appendix"
    instruction: |
      ## SQL Scripts
      Link to or include:
      - Schema creation scripts
      - Seed data scripts
      - Migration scripts
      
      ## ER Diagram
      Reference to visual schema diagram
      
      ## Glossary
      Business and technical terms used
      
      ## References
      - Documentation links
      - Related design documents
      - Team decisions and ADRs
    elicit: false
```


## Referência: references/squad/workflows/analyze-data-workflow.yaml

```yaml
workflow:
  id: analyze-data
  name: Analyze and Import Data
  description: Import CSV files, apply seed data, and analyze database contents with validation
  version: 1.0.0
  type: sequential
  sequence:
    - phase: select_operation_type
      agent: db-sage
      action: select_operation_type
      description: Choose whether to import CSV data, apply seed data, or analyze existing tables.
      outputs:
        - operation_type
    - phase: collect_csv_details
      agent: db-sage
      action: collect_csv_details
      description: Collect CSV path and target table before import.
      condition: import_csv_selected
      outputs:
        - csv_path
        - target_table
    - phase: import_csv
      agent: db-sage
      task: db-load-csv
      description: Load CSV data through the canonical data-loader worker.
      condition: import_csv_selected
    - phase: collect_seed_details
      agent: db-sage
      action: collect_seed_details
      description: Collect the seed file path before applying seed data.
      condition: seed_selected
      outputs:
        - seed_path
    - phase: apply_seed
      agent: db-sage
      task: db-seed
      description: Apply seed SQL through the canonical data-loader worker.
      condition: seed_selected
    - phase: select_analysis_type
      agent: db-sage
      action: select_analysis_type
      description: Select the analysis branch for existing data inspection.
      condition: analyze_selected
      outputs:
        - analysis_type
    - phase: run_table_statistics
      agent: db-sage
      action: run_table_statistics
      description: Inspect table sizes, live rows, and storage footprint.
      condition: table_statistics_selected
    - phase: collect_distribution_params
      agent: db-sage
      action: collect_distribution_params
      description: Collect table and column parameters for distribution analysis.
      condition: distribution_selected
      outputs:
        - dist_table
        - dist_column
    - phase: run_distribution_analysis
      agent: db-sage
      action: run_distribution_analysis
      description: Analyze column value distribution for the selected table and column.
      condition: distribution_selected
    - phase: run_integrity_checks
      agent: db-sage
      action: run_integrity_checks
      description: Execute integrity and quality checks across the database.
      condition: integrity_selected
    - phase: collect_recent_activity_params
      agent: db-sage
      action: collect_recent_activity_params
      description: Collect parameters for recent-activity inspection.
      condition: recent_selected
      outputs:
        - recent_table
        - recent_column
        - recent_days
    - phase: run_recent_activity_analysis
      agent: db-sage
      action: run_recent_activity_analysis
      description: Analyze recent activity for the selected table and timestamp column.
      condition: recent_selected
    - workflow_end:
        id: complete
        action: workflow_complete
metadata:
  author: DB Sage
  created_date: "2025-10-27"
  story: squads/db-sage/docs/stories/1.4.analyze-data-workflow.md
steps:
  - id: operation_type
    name: Select Data Operation
    type: elicit
    elicit:
      question: "Data operation:"
      options:
        - label: Import CSV file
          value: import_csv
        - label: Apply seed data
          value: seed
        - label: Analyze existing data
          value: analyze
      output_var: operation_type
  - id: csv_details
    condition: "{{operation_type}} == 'import_csv'"
    type: elicit
    elicit:
      fields:
        - name: csv_path
          label: CSV file path
          type: string
          required: true
        - name: target_table
          label: Target table
          type: string
          required: true
      output_vars:
        - csv_path
        - target_table
  - id: csv_import
    condition: "{{operation_type}} == 'import_csv'"
    type: task
    task: db-load-csv
    inputs:
      table: "{{target_table}}"
      csv_file: "{{csv_path}}"
  - id: seed_details
    condition: "{{operation_type}} == 'seed'"
    type: elicit
    elicit:
      fields:
        - name: seed_path
          label: Seed file path
          type: string
          required: true
      output_vars:
        - seed_path
  - id: seed_apply
    condition: "{{operation_type}} == 'seed'"
    type: task
    task: db-seed
    inputs:
      path: "{{seed_path}}"
  - id: analysis_type
    condition: "{{operation_type}} == 'analyze'"
    type: elicit
    elicit:
      question: "Analysis type:"
      options:
        - label: Table statistics
          value: stats
        - label: Data distribution
          value: distribution
        - label: Integrity checks
          value: integrity
        - label: Recent activity
          value: recent
      output_var: analysis_type
  - id: run_stats
    condition: "{{operation_type}} == 'analyze' AND {{analysis_type}} == 'stats'"
    type: execute
    description: Analyze table sizes and row counts
    command: |
      DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
      test -n "$DB_URL" || { echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"; exit 1; }

      echo "=== TABLE STATISTICS ==="
      echo ""
      psql "$DB_URL" -c "
        SELECT
          schemaname,
          tablename,
          pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS total_size,
          pg_size_pretty(pg_relation_size(schemaname||'.'||tablename)) AS table_size,
          pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename) -
                         pg_relation_size(schemaname||'.'||tablename)) AS index_size,
          n_live_tup AS live_rows,
          n_dead_tup AS dead_rows
        FROM pg_stat_user_tables
        WHERE schemaname = 'public'
        ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC
        LIMIT 20;"
      echo ""
      echo "✅ Statistics complete"
  - id: distribution_params
    condition: "{{operation_type}} == 'analyze' AND {{analysis_type}} == 'distribution'"
    type: elicit
    elicit:
      fields:
        - name: dist_table
          label: Table name
          type: string
          required: true
        - name: dist_column
          label: Column to analyze
          type: string
          required: true
      output_vars:
        - dist_table
        - dist_column
  - id: run_distribution
    condition: "{{operation_type}} == 'analyze' AND {{analysis_type}} == 'distribution'"
    type: execute
    description: Analyze data distribution for column
    command: |
      DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
      test -n "$DB_URL" || { echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"; exit 1; }

      for ident in "{{dist_table}}" "{{dist_column}}"; do
        case "$ident" in
          ''|*[!A-Za-z0-9_]*)
            echo "❌ Invalid identifier: $ident"
            exit 1
            ;;
        esac
      done

      COLUMN_EXISTS=$(psql "$DB_URL" -t -A -c "
        SELECT COUNT(*)
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = '{{dist_table}}'
          AND column_name = '{{dist_column}}';")

      if [ "$COLUMN_EXISTS" = "0" ]; then
        echo "❌ Column '{{dist_column}}' not found in table '{{dist_table}}'"
        exit 1
      fi

      echo "=== DATA DISTRIBUTION: {{dist_table}}.{{dist_column}} ==="
      echo ""

      psql "$DB_URL" -c "
        SELECT
          {{dist_column}} AS value,
          COUNT(*) AS count,
          ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentage
        FROM {{dist_table}}
        WHERE {{dist_column}} IS NOT NULL
        GROUP BY {{dist_column}}
        ORDER BY count DESC
        LIMIT 20;"

      echo ""
      echo "--- NULL Analysis ---"
      psql "$DB_URL" -c "
        SELECT
          COUNT(*) FILTER (WHERE {{dist_column}} IS NULL) AS null_count,
          COUNT(*) FILTER (WHERE {{dist_column}} IS NOT NULL) AS non_null_count,
          ROUND(100.0 * COUNT(*) FILTER (WHERE {{dist_column}} IS NULL) / COUNT(*), 2) AS null_percentage
        FROM {{dist_table}};"

      echo ""
      echo "✅ Distribution analysis complete"
  - id: run_integrity
    condition: "{{operation_type}} == 'analyze' AND {{analysis_type}} == 'integrity'"
    type: execute
    description: Check for orphaned records and referential integrity
    command: |
      DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
      test -n "$DB_URL" || { echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"; exit 1; }

      echo "=== INTEGRITY CHECKS ==="
      echo ""

      echo "--- Foreign Key Violations ---"
      psql "$DB_URL" -c "
        SELECT
          tc.table_name,
          kcu.column_name,
          ccu.table_name AS foreign_table_name,
          ccu.column_name AS foreign_column_name
        FROM information_schema.table_constraints AS tc
        JOIN information_schema.key_column_usage AS kcu
          ON tc.constraint_name = kcu.constraint_name
          AND tc.table_schema = kcu.table_schema
        JOIN information_schema.constraint_column_usage AS ccu
          ON ccu.constraint_name = tc.constraint_name
          AND ccu.table_schema = tc.table_schema
        WHERE tc.constraint_type = 'FOREIGN KEY'
          AND tc.table_schema = 'public'
        ORDER BY tc.table_name, kcu.column_name;"

      echo ""
      echo "--- Tables Without Primary Keys ---"
      psql "$DB_URL" -c "
        SELECT
          t.table_name
        FROM information_schema.tables t
        LEFT JOIN information_schema.table_constraints tc
          ON t.table_name = tc.table_name
          AND tc.constraint_type = 'PRIMARY KEY'
        WHERE t.table_schema = 'public'
          AND t.table_type = 'BASE TABLE'
          AND tc.constraint_name IS NULL
        ORDER BY t.table_name;"

      echo ""
      echo "--- Duplicate Check (tables with potential duplicates) ---"
      psql "$DB_URL" -c "
        SELECT
          schemaname,
          tablename,
          n_live_tup AS total_rows,
          n_dead_tup AS dead_rows,
          CASE
            WHEN n_live_tup > 0 THEN ROUND(100.0 * n_dead_tup / n_live_tup, 2)
            ELSE 0
          END AS dead_row_percentage
        FROM pg_stat_user_tables
        WHERE schemaname = 'public'
          AND n_dead_tup > 0
        ORDER BY n_dead_tup DESC
        LIMIT 10;"

      echo ""
      echo "✅ Integrity checks complete"
  - id: recent_params
    condition: "{{operation_type}} == 'analyze' AND {{analysis_type}} == 'recent'"
    type: elicit
    elicit:
      fields:
        - name: recent_table
          label: Table name
          type: string
          required: true
        - name: recent_limit
          label: Number of records to show
          type: number
          default: 10
        - name: time_column
          label: Timestamp column (e.g., created_at)
          type: string
          default: created_at
      output_vars:
        - recent_table
        - recent_limit
        - time_column
  - id: run_recent
    condition: "{{operation_type}} == 'analyze' AND {{analysis_type}} == 'recent'"
    type: execute
    description: Show recent activity in table
    command: |
      DB_URL="${SUPABASE_DB_URL:-${DATABASE_URL:-}}"
      test -n "$DB_URL" || { echo "❌ Missing SUPABASE_DB_URL or DATABASE_URL"; exit 1; }

      for ident in "{{recent_table}}" "{{time_column}}"; do
        case "$ident" in
          ''|*[!A-Za-z0-9_]*)
            echo "❌ Invalid identifier: $ident"
            exit 1
            ;;
        esac
      done

      echo "=== RECENT ACTIVITY: {{recent_table}} ==="
      echo ""

      COLUMN_EXISTS=$(psql "$DB_URL" -t -A -c "
        SELECT COUNT(*)
        FROM information_schema.columns
        WHERE table_name = '{{recent_table}}'
          AND column_name = '{{time_column}}'
          AND table_schema = 'public';")

      if [ "$COLUMN_EXISTS" = "0" ]; then
        echo "❌ Error: Column '{{time_column}}' not found in table '{{recent_table}}'"
        echo ""
        echo "Available timestamp columns:"
        psql "$DB_URL" -c "
          SELECT column_name, data_type
          FROM information_schema.columns
          WHERE table_name = '{{recent_table}}'
            AND table_schema = 'public'
            AND data_type IN ('timestamp', 'timestamp with time zone', 'timestamp without time zone')
          ORDER BY ordinal_position;"
        exit 1
      fi

      echo "--- Most Recent Records ---"
      psql "$DB_URL" -c "
        SELECT *
        FROM {{recent_table}}
        ORDER BY {{time_column}} DESC
        LIMIT {{recent_limit}};"

      echo ""
      echo "--- Activity by Time Period ---"
      psql "$DB_URL" -c "
        SELECT
          DATE_TRUNC('day', {{time_column}}) AS day,
          COUNT(*) AS records
        FROM {{recent_table}}
        WHERE {{time_column}} > NOW() - INTERVAL '30 days'
        GROUP BY day
        ORDER BY day DESC
        LIMIT 30;"

      echo ""
      echo "✅ Recent activity analysis complete"
outputs:
  operation_complete:
    type: boolean
    description: Operation completed successfully
    value: true
global_error_handling:
  on_error: abort
```


## Referência: references/squad/workflows/backup-restore-workflow.yaml

```yaml
workflow:
  id: backup-restore
  name: Backup & Restore Database
  description: Create or restore database snapshots with explicit user confirmation
  version: 1.0.0
  type: sequential
  sequence:
    - phase: choose_operation
      agent: db-sage
      action: choose_operation
      description: Decide whether to create, list, or restore database snapshots.
      outputs:
        - operation
    - phase: collect_snapshot_details
      agent: db-sage
      action: collect_snapshot_details
      description: Capture snapshot label and type before backup creation.
      condition: snapshot_selected
      outputs:
        - label
        - snapshot_type
    - phase: create_snapshot
      agent: db-sage
      task: db-snapshot
      description: Create a database snapshot using the canonical snapshot task.
      condition: snapshot_selected
    - phase: list_snapshots
      agent: db-sage
      action: list_snapshots
      description: Show the most recent available snapshot files.
      condition: list_selected
    - phase: select_snapshot
      agent: db-sage
      action: select_snapshot
      description: Collect the snapshot path to restore.
      condition: restore_selected
      outputs:
        - snapshot_file
    - phase: confirm_restore
      agent: db-sage
      action: confirm_restore
      description: Require explicit confirmation before restore.
      condition: restore_selected
    - phase: restore_snapshot
      agent: db-sage
      task: db-rollback
      description: Restore the selected snapshot through the rollback task.
      condition: restore_confirmed
    - workflow_end:
        id: complete
        action: workflow_complete
metadata:
  story: squads/db-sage/docs/stories/1.5.backup-restore-workflow.md
steps:
  - id: operation
    type: elicit
    elicit:
      question: "Backup/Restore operation:"
      options:
        - label: Create snapshot
          value: snapshot
        - label: Restore from snapshot
          value: restore
        - label: List snapshots
          value: list
      output_var: operation
  - id: snapshot_label
    condition: "{{operation}} == 'snapshot'"
    type: elicit
    elicit:
      fields:
        - name: label
          label: Snapshot label
          type: string
          default: manual
        - name: snapshot_type
          label: Type (schema/full)
          type: string
          default: schema
      output_vars:
        - label
        - snapshot_type
  - id: create_snapshot
    condition: "{{operation}} == 'snapshot'"
    type: task
    task: db-snapshot
    inputs:
      label: "{{label}}"
      type: "{{snapshot_type}}"
  - id: list_snapshots
    condition: "{{operation}} == 'list'"
    type: execute
    command: ls -lht supabase/snapshots/*.sql | head -20
  - id: select_snapshot
    condition: "{{operation}} == 'restore'"
    type: elicit
    elicit:
      fields:
        - name: snapshot_file
          label: Snapshot file
          type: string
          required: true
      output_vars:
        - snapshot_file
  - id: confirm_restore
    condition: "{{operation}} == 'restore'"
    type: elicit
    elicit:
      question: "⚠️ WARNING: This will replace current database! Continue?"
      options:
        - label: Yes (I have backup)
          value: "yes"
        - label: No (cancel)
          value: "no"
      output_var: confirm_restore
  - id: restore_snapshot
    condition: "{{confirm_restore}} == 'yes'"
    type: task
    task: db-rollback
    inputs:
      snapshot: "{{snapshot_file}}"
```


## Referência: references/squad/workflows/kiss-gate-workflow.yaml

```yaml
workflow:
  id: kiss-gate
  name: KISS Gate Validation
  description: Validate whether a database is justified before schema work begins
  version: 1.0.0
  type: sequential
  sequence:
    - phase: collect_use_case
      agent: db-sage
      action: collect_use_case
      description: Capture the data shape, access needs, scale, and relationship requirements.
      outputs:
        - what_storing
        - how_many
        - how_often
        - who_access
        - need_joins
    - phase: detect_red_flags
      agent: db-sage
      action: detect_red_flags
      description: Evaluate whether the use case can be solved with a simpler option than a database.
      outputs:
        - red_flag_count
    - phase: suggest_alternatives
      agent: db-sage
      action: suggest_alternatives
      description: Present simpler alternatives when the KISS gate detects over-engineering risk.
      condition: red_flags_detected
    - phase: confirm_override
      agent: db-sage
      action: confirm_override
      description: Ask whether the user wants to override the KISS recommendation.
      condition: red_flags_detected
      outputs:
        - override
    - phase: capture_justification
      agent: db-sage
      action: capture_justification
      description: Capture the justification for using a database despite the KISS warnings.
      condition: override_confirmed
      outputs:
        - why_db
    - workflow_end:
        id: complete
        action: workflow_complete
metadata:
  story: squads/db-sage/docs/stories/1.7.kiss-gate-validation-workflow.md
steps:
  - id: use_case
    type: elicit
    elicit:
      fields:
        - name: what_storing
          label: What are you storing?
          type: text
        - name: how_many
          label: How many records?
          type: number
        - name: how_often
          label: How often changes?
          type: string
        - name: who_access
          label: Who needs access?
          type: string
        - name: need_joins
          label: Need relationships/joins?
          type: boolean
      output_vars:
        - what_storing
        - how_many
        - how_often
        - who_access
        - need_joins
  - id: detect_red_flags
    type: execute
    command: |
      RED_FLAGS=0

      # Small dataset
      if [ "{{how_many}}" -lt 100 ]; then
        echo "🚩 Small dataset (<100) → Consider JSON/YAML file"
        RED_FLAGS=$((RED_FLAGS + 1))
      fi

      # Single user
      if echo "{{who_access}}" | grep -qi "just me\|only me\|single"; then
        echo "🚩 Single user → Consider SQLite local file"
        RED_FLAGS=$((RED_FLAGS + 1))
      fi

      # No joins
      if [ "{{need_joins}}" = "false" ]; then
        echo "🚩 No relationships → Reconsider database"
        RED_FLAGS=$((RED_FLAGS + 1))
      fi

      echo "red_flags=$RED_FLAGS"
    outputs:
      red_flag_count: "{{output}}"
  - id: suggest_alternatives
    condition: "{{red_flag_count}} > 0"
    type: execute
    command: |
      echo "=== KISS Gate: Simpler Solutions Available ==="
      echo ""
      echo "Consider these alternatives:"

      if [ "{{how_many}}" -lt 100 ]; then
        echo "• JSON/YAML file (< 100 records)"
      fi

      if echo "{{who_access}}" | grep -qi "just me"; then
        echo "• SQLite local file (single user)"
      fi

      echo ""
      echo "Database is appropriate if:"
      echo "  ✓ Multi-user concurrent access"
      echo "  ✓ Relationships/joins required"
      echo "  ✓ ACID transactions needed"
      echo "  ✓ > 10K records expected"
  - id: override
    condition: "{{red_flag_count}} > 0"
    type: elicit
    elicit:
      question: Continue with database anyway?
      options:
        - label: No - Use simpler solution
          value: "no"
        - label: Yes - Database is necessary
          value: "yes"
      output_var: override
  - id: justification
    condition: "{{override}} == 'yes'"
    type: elicit
    elicit:
      fields:
        - name: why_db
          label: Why is database necessary?
          type: text
          multiline: true
      output_vars:
        - why_db
```


## Referência: references/squad/workflows/modify-schema-workflow.yaml

```yaml
workflow:
  id: modify-schema
  name: Modify Database Schema Safely
  description: Apply database migrations with DDL validation, dry-run testing, snapshots, and smoke tests
  version: 1.0.0
  type: sequential
  sequence:
    - phase: select_migration_source
      agent: db-sage
      action: select_migration_source
      description: Decide whether to apply an existing migration or generate a new migration file.
      outputs:
        - migration_source
        - migration_file
    - phase: generate_new_migration
      agent: db-sage
      action: generate_new_migration
      description: Generate a timestamped migration template when the workflow starts from a new change request.
      condition: migration_source_new
      outputs:
        - migration_file
    - phase: select_existing_migration
      agent: db-sage
      action: select_existing_migration
      description: Capture the existing migration path when the workflow starts from a prepared SQL file.
      condition: migration_source_existing
      outputs:
        - migration_file
    - phase: verify_ddl_order
      agent: db-sage
      task: db-verify-order
      description: Validate DDL ordering before any migration test or execution.
    - phase: offer_dry_run
      agent: db-sage
      action: offer_dry_run
      description: Ask whether the migration should be tested inside BEGIN/ROLLBACK.
    - phase: execute_dry_run
      agent: db-sage
      task: db-dry-run
      description: Execute the migration in dry-run mode when selected.
      condition: dry_run_requested
    - phase: confirm_apply
      agent: db-sage
      action: confirm_apply
      description: Require explicit confirmation before applying the migration.
      condition: migration_ready_to_apply
    - phase: create_pre_snapshot
      agent: db-sage
      task: db-snapshot
      description: Create a pre-migration snapshot for rollback safety.
      condition: apply_confirmed_or_dry_run_skipped
    - phase: apply_migration
      agent: db-sage
      task: db-apply-migration
      description: Apply the migration through the canonical migration worker.
      condition: apply_confirmed_or_dry_run_skipped
    - phase: run_smoke_test
      agent: db-sage
      task: db-smoke-test
      description: Execute post-migration smoke tests after successful application.
      condition: migration_applied
    - phase: update_documentation
      agent: db-sage
      action: update_documentation
      description: Update database documentation and migration records after the schema change.
      condition: migration_applied
    - phase: summarize_migration
      agent: db-sage
      action: summarize_migration
      description: Present the migration result, snapshot, and follow-up guidance.
    - workflow_end:
        id: complete
        action: workflow_complete
metadata:
  author: DB Sage
  created_date: "2025-10-27"
  last_modified: "2025-10-28"
  tags:
    - database
    - migration
    - schema
    - ddl
    - db-sage
    - documentation
  story: squads/db-sage/docs/stories/1.3.modify-schema-workflow.md
  changelog:
    - version: 1.1.0
      date: "2025-10-28"
      changes: Added STEP 10 - Mandatory documentation update after migration
      rationale: Prevent documentation drift (v0.7.0 docs with v0.8.2 database)
inputs:
  migration_source:
    type: string
    description: "Migration source: new or existing"
    required: false
  migration_path:
    type: string
    description: Path to migration file
    required: false
steps:
  - id: step_1_migration_source
    name: Select Migration Source
    type: elicit
    elicit:
      question: "Migration source:"
      options:
        - label: Apply existing migration file
          value: existing
          description: Execute a migration SQL file
        - label: Create new migration
          value: new
          description: Generate migration template with proper DDL ordering
      default: existing
      output_var: migration_source
    error_handling:
      strategy: fail
  - id: step_2a_new_migration
    name: Create New Migration File
    type: elicit
    condition: "{{migration_source}} == 'new'"
    elicit:
      fields:
        - name: migration_description
          label: Migration Description (e.g., 'add users table')
          type: string
          required: true
          placeholder: add_users_table
        - name: migration_purpose
          label: Purpose (why is this change needed?)
          type: text
          multiline: true
          required: false
      output_vars:
        - migration_description
        - migration_purpose
  - id: step_2b_generate_file
    name: Generate Migration Template
    type: execute
    condition: "{{migration_source}} == 'new'"
    description: Create migration file with proper DDL ordering
    command: |
      # Create supabase/migrations directory if not exists
      mkdir -p supabase/migrations

      # Generate timestamp-based filename
      TIMESTAMP=$(date +%Y%m%d%H%M%S)
      DESC=$(echo "{{migration_description}}" | tr ' ' '_' | tr '[:upper:]' '[:lower:]')
      FILENAME="supabase/migrations/${TIMESTAMP}_${DESC}.sql"

      # Create migration template (YAML-safe shell block, no heredoc)
      printf '%s\n' \
        "-- Migration: {{migration_description}}" \
        "-- Purpose: {{migration_purpose}}" \
        "-- DDL execution order: Extensions -> Tables -> Functions -> Triggers -> RLS -> Views" \
        "" \
        "BEGIN;" \
        "" \
        "-- Add your migration SQL below" \
        "" \
        "COMMIT;" \
        > "$FILENAME"

      echo "$FILENAME"
    outputs:
      migration_file: "{{output}}"
  - id: step_2c_select_existing
    name: Select Existing Migration
    type: elicit
    condition: "{{migration_source}} == 'existing'"
    elicit:
      help_text: Available migrations in supabase/migrations/
      fields:
        - name: migration_path
          label: Migration File Path
          type: string
          required: true
          placeholder: supabase/migrations/20241027_add_users.sql
      output_vars:
        - migration_path
    outputs:
      migration_file: "{{migration_path}}"
  - id: step_3_verify_order
    name: Verify DDL Ordering
    type: task
    task: db-verify-order
    description: Validate DDL execution order to prevent dependency errors
    inputs:
      path: "{{migration_file}}"
    error_handling:
      strategy: warn
      message: |
        ⚠️ DDL ordering issues detected

        Review and fix before proceeding:
        1. Extensions must come before tables that use them
        2. Tables must exist before functions reference them
        3. Functions must exist before triggers call them
        4. RLS must be enabled before creating policies
        5. Views must come last (they depend on tables/functions)
    outputs:
      order_valid: true
  - id: step_4_dry_run_option
    name: Offer Dry-Run Test
    type: elicit
    elicit:
      question: Run dry-run test? (HIGHLY RECOMMENDED)
      help_text: |
        Dry-run executes migration in BEGIN...ROLLBACK:
        - Tests SQL syntax
        - Validates dependencies
        - Checks execution order
        - NO actual changes applied
      options:
        - label: Yes - Test migration safely (RECOMMENDED)
          value: "yes"
          description: Test without applying changes
        - label: Skip - Apply immediately (RISKY)
          value: "no"
          description: Skip safety check
      default: "yes"
      output_var: run_dry_run
    error_handling:
      strategy: fail
  - id: step_5_dry_run
    name: Execute Dry-Run Test
    type: task
    task: db-dry-run
    condition: "{{run_dry_run}} == 'yes'"
    description: Test migration with BEGIN...ROLLBACK
    inputs:
      path: "{{migration_file}}"
    error_handling:
      strategy: fail
      message: |
        ❌ Dry-run failed

        Fix the migration and try again.
        Common issues:
        - Syntax errors
        - Missing dependencies
        - Wrong execution order
        - Constraint violations
    outputs:
      dry_run_passed: true
  - id: step_6_confirm_apply
    name: Confirm Migration Application
    type: elicit
    condition: "{{run_dry_run}} == 'yes'"
    elicit:
      question: |
        ✅ Dry-run passed successfully

        Apply migration to database?
      options:
        - label: Yes - Apply migration
          value: "yes"
          description: Proceed with migration
        - label: No - Cancel
          value: "no"
          description: Review migration first
      default: "yes"
      output_var: confirm_apply
    error_handling:
      strategy: abort
  - id: step_7_pre_snapshot
    name: Create Pre-Migration Snapshot
    type: task
    task: db-snapshot
    condition: "{{confirm_apply}} == 'yes' OR {{run_dry_run}} == 'no'"
    description: Create schema-only backup before migration
    inputs:
      label: pre_migration_{{timestamp}}
      type: schema
      purpose: Safety snapshot before migration {{migration_file}}
    error_handling:
      strategy: warn
      message: ⚠️ Snapshot failed, but continuing with migration
    outputs:
      snapshot_file: "{{output}}"
  - id: step_8_apply_migration
    name: Apply Migration to Database
    type: task
    task: db-apply-migration
    condition: "{{confirm_apply}} == 'yes' OR {{run_dry_run}} == 'no'"
    description: Execute migration with advisory lock and error handling
    inputs:
      path: "{{migration_file}}"
    error_handling:
      strategy: fail
      message: |
        ❌ MIGRATION FAILED

        Your database is unchanged (transaction rolled back).

        Rollback options:
        1. Fix migration and try again
        2. Restore pre-migration snapshot: *rollback {{snapshot_file}}

        Emergency snapshot: {{snapshot_file}}
    outputs:
      migration_success: true
      post_snapshot_file: "{{post_snapshot}}"
  - id: step_9_smoke_test
    name: Run Post-Migration Smoke Test
    type: task
    task: db-smoke-test
    condition: "{{migration_success}} == true"
    description: Validate schema integrity after migration
    inputs:
      version: "{{migration_file}}"
    error_handling:
      strategy: warn
      message: |
        ⚠️ Smoke test failed

        Migration applied but validation failed.
        Review schema integrity manually.
    outputs:
      smoke_test_passed: "{{output}}"
  - id: step_10_update_documentation
    name: Update Database Documentation
    type: checklist
    condition: "{{migration_success}} == true"
    description: Execute documentation update checklist (MANDATORY)
    checklist: squads/db-sage/checklists/database-migration-documentation-checklist.md
    required_actions:
      - Update docs/database/README.md metadata (version, migration, snapshot, date)
      - Update version history table in README
      - Update 'Current Schema' section with changes
      - Create/update docs/database/evolution/X.Y_README.md (if minor/major version)
      - Create post-migration snapshot with correct version
      - Verify DB Sage can load new version
    help_text: |
      🚨 DOCUMENTATION UPDATE REQUIRED 🚨

      This step is MANDATORY to prevent documentation drift.

      Follow the checklist to update:
      1. Version metadata in README
      2. Version history table
      3. Current schema section
      4. Evolution documentation
      5. Schema snapshot

      **Why:** Without this, documentation becomes stale and DB Sage will load wrong version.

      **Time:** 10-15 minutes

      Use checklist: squads/db-sage/checklists/database-migration-documentation-checklist.md
    error_handling:
      strategy: warn
      message: |
        ⚠️ DOCUMENTATION NOT UPDATED

        Migration applied successfully, but documentation is NOT updated.

        **CRITICAL:** You MUST update documentation manually:
        1. Open: squads/db-sage/checklists/database-migration-documentation-checklist.md
        2. Follow ALL steps in checklist
        3. Verify DB Sage loads correct version

        **Consequence if skipped:** Documentation drift, confusion, DB Sage malfunction.
    outputs:
      documentation_updated: true
  - id: step_11_success_summary
    name: Display Success Summary
    type: execute
    condition: "{{migration_success}} == true"
    description: Show migration summary and next steps
    command: |
      echo ""
      echo "════════════════════════════════════════"
      echo "✅ MIGRATION APPLIED SUCCESSFULLY"
      echo "════════════════════════════════════════"
      echo ""
      echo "Migration Details:"
      echo "  File: {{migration_file}}"
      echo "  Pre-Snapshot: {{snapshot_file}}"
      echo "  Post-Snapshot: {{post_snapshot_file}}"
      echo ""

      {% if smoke_test_passed %}
      echo "Validation:"
      echo "  ✅ Smoke test passed"
      {% else %}
      echo "Validation:"
      echo "  ⚠️ Smoke test had warnings - review manually"
      {% endif %}

      echo ""
      echo "Snapshots:"
      echo "  Before: {{snapshot_file}}"
      echo "  After: {{post_snapshot_file}}"
      echo "  Diff: supabase/snapshots/diff.patch"
      echo ""
      echo "Next Steps:"
      echo "  1. Verify changes in database"
      echo "  2. Test application functionality"
      echo "  3. Deploy to staging/production"
      echo ""
      echo "Rollback (if needed):"
      echo "  *rollback {{snapshot_file}}"
      echo ""
outputs:
  migration_applied:
    type: boolean
    description: Migration successfully applied
    source: step_8_apply_migration.migration_success
  documentation_updated:
    type: boolean
    description: Documentation updated after migration
    source: step_10_update_documentation.documentation_updated
  migration_file:
    type: string
    description: Path to migration file
    source: migration_file
  pre_snapshot:
    type: string
    description: Pre-migration snapshot file
    source: step_7_pre_snapshot.snapshot_file
  post_snapshot:
    type: string
    description: Post-migration snapshot file
    source: step_8_apply_migration.post_snapshot_file
  smoke_test_passed:
    type: boolean
    description: Post-migration smoke test result
    source: step_9_smoke_test.smoke_test_passed
global_error_handling:
  on_error: abort
  notification:
    enabled: true
    channels:
      - console
  rollback_on_error: true
security:
  authorization_required: false
  audit_logging: true
  advisory_lock_required: true
  snapshot_before_migration: true
```


## Referência: references/squad/workflows/performance-tuning-workflow.yaml

```yaml
workflow:
  id: performance-tuning
  name: Performance Tuning
  description: Analyze hotpaths, specific queries, and RLS performance issues
  version: 1.0.0
  type: sequential
  sequence:
    - phase: choose_analysis_type
      agent: db-sage
      action: choose_analysis_type
      description: Select the performance investigation branch.
      outputs:
        - analysis_type
    - phase: analyze_hotpaths
      agent: db-sage
      task: db-analyze-hotpaths
      description: Inspect slow-query hotspots and performance bottlenecks.
      condition: hotpaths_selected
    - phase: collect_query_input
      agent: db-sage
      action: collect_query_input
      description: Collect a query for EXPLAIN analysis.
      condition: explain_selected
      outputs:
        - sql
    - phase: run_explain
      agent: db-sage
      task: db-explain
      description: Run EXPLAIN for the provided SQL statement.
      condition: explain_selected
    - phase: run_optimization_session
      agent: db-sage
      task: query-optimization
      description: Start the interactive query optimization task.
      condition: optimize_selected
    - phase: audit_rls_performance
      agent: db-sage
      task: db-rls-audit
      description: Audit RLS performance characteristics and policy impact.
      condition: rls_selected
    - phase: summarize_rls_recommendations
      agent: db-sage
      action: summarize_rls_recommendations
      description: Present RLS performance recommendations and common fixes.
      condition: rls_selected
    - workflow_end:
        id: complete
        action: workflow_complete
metadata:
  story: squads/db-sage/docs/stories/1.6.performance-tuning-workflow.md
steps:
  - id: analysis_type
    type: elicit
    elicit:
      question: "Performance analysis type:"
      options:
        - label: Find slow queries (pg_stat_statements)
          value: hotpaths
        - label: Analyze specific query (EXPLAIN)
          value: explain
        - label: Interactive optimization session
          value: optimize
        - label: Check RLS performance
          value: rls
      output_var: analysis_type
  - id: run_hotpaths
    condition: "{{analysis_type}} == 'hotpaths'"
    type: task
    task: db-analyze-hotpaths
  - id: query_input
    condition: "{{analysis_type}} == 'explain'"
    type: elicit
    elicit:
      fields:
        - name: sql
          label: SQL query to analyze
          type: text
          multiline: true
      output_vars:
        - sql
  - id: run_explain
    condition: "{{analysis_type}} == 'explain'"
    type: task
    task: db-explain
    inputs:
      sql: "{{sql}}"
  - id: run_optimize
    condition: "{{analysis_type}} == 'optimize'"
    type: task
    task: query-optimization
  - id: run_rls_audit
    condition: "{{analysis_type}} == 'rls'"
    type: task
    task: db-rls-audit
  - id: rls_recommendations
    condition: "{{analysis_type}} == 'rls'"
    type: execute
    command: |
      echo "=== RLS Performance Recommendations ==="
      echo ""
      echo "✅ FAST: (select auth.uid()) = user_id"
      echo "❌ SLOW: auth.uid() = user_id"
      echo ""
      echo "Performance improvement: 99.99% faster (10,000x speedup)"
```


## Referência: references/squad/workflows/query-database-workflow.yaml

```yaml
workflow:
  id: query-database
  name: Query Database with Safety and Performance
  description: Execute SQL queries with transaction safety, dangerous operation detection, and performance analysis
  version: 1.0.0
  type: sequential
  sequence:
    - phase: choose_query_input
      agent: db-sage
      action: choose_query_input
      description: Select whether SQL will be provided inline or from a file.
      outputs:
        - query_source
    - phase: capture_inline_sql
      agent: db-sage
      action: capture_inline_sql
      description: Collect inline SQL text when the query source is direct input.
      condition: query_source_inline
      outputs:
        - sql_content
    - phase: capture_sql_file
      agent: db-sage
      action: capture_sql_file
      description: Collect the SQL file path when the query source is a file.
      condition: query_source_file
      outputs:
        - sql_file
    - phase: choose_transaction_mode
      agent: db-sage
      action: choose_transaction_mode
      description: Decide whether to run inside a transaction and whether dry-run semantics apply.
    - phase: safety_check
      agent: db-sage
      action: safety_check
      description: Detect destructive SQL patterns and gate execution accordingly.
      outputs:
        - safety_status
    - phase: confirm_dangerous_execution
      agent: db-sage
      action: confirm_dangerous_execution
      description: Require explicit confirmation before destructive SQL executes.
      condition: dangerous_operation_detected
    - phase: verify_dangerous_confirmation
      agent: db-sage
      action: verify_dangerous_confirmation
      description: Ensure destructive execution is blocked unless confirmation was explicit.
      condition: dangerous_operation_detected
    - phase: execute_sql
      agent: db-sage
      task: db-run-sql
      description: Execute the SQL statement or file through the canonical worker.
    - phase: offer_performance_analysis
      agent: db-sage
      action: offer_performance_analysis
      description: Ask whether EXPLAIN analysis should run after query execution.
    - phase: run_explain
      agent: db-sage
      task: db-explain
      description: Run EXPLAIN ANALYZE for the executed query when requested.
      condition: performance_analysis_requested
    - phase: suggest_optimization
      agent: db-sage
      action: suggest_optimization
      description: Present optimization suggestions based on the execution plan.
      condition: performance_analysis_requested
    - phase: summarize_execution
      agent: db-sage
      action: summarize_execution
      description: Summarize execution, safety outcome, and performance follow-up.
    - workflow_end:
        id: complete
        action: workflow_complete
metadata:
  author: DB Sage
  created_date: "2025-10-27"
  last_modified: "2025-10-27"
  tags:
    - database
    - query
    - sql
    - performance
    - db-sage
  story: squads/db-sage/docs/stories/1.2.query-database-workflow.md
inputs:
  query_source:
    type: string
    description: "Query source: inline or file"
    required: false
  sql_query:
    type: string
    description: SQL query or file path
    required: false
steps:
  - id: step_1_query_input
    name: Select Query Input Method
    type: elicit
    elicit:
      question: How do you want to provide the SQL query?
      options:
        - label: Inline SQL (type or paste)
          value: inline
          description: Enter SQL directly
        - label: SQL File (path)
          value: file
          description: Execute SQL from file
      default: inline
      output_var: query_source
    error_handling:
      strategy: fail
  - id: step_2a_inline_sql
    name: Enter Inline SQL
    type: elicit
    condition: "{{query_source}} == 'inline'"
    elicit:
      fields:
        - name: sql
          label: SQL Query (can be multi-line)
          type: text
          multiline: true
          required: true
          placeholder: SELECT * FROM users WHERE created_at > NOW() - INTERVAL '7 days';
      output_vars:
        - sql
    outputs:
      sql_content: "{{sql}}"
    error_handling:
      strategy: fail
  - id: step_2b_file_input
    name: Enter SQL File Path
    type: elicit
    condition: "{{query_source}} == 'file'"
    elicit:
      fields:
        - name: file_path
          label: SQL File Path
          type: string
          required: true
          placeholder: queries/my_query.sql
          validation: Must be a valid file path
      output_vars:
        - file_path
    outputs:
      sql_file: "{{file_path}}"
    error_handling:
      strategy: fail
      message: File not found or not readable
  - id: step_3_transaction_mode
    name: Select Transaction Mode
    type: elicit
    elicit:
      question: "Select transaction mode:"
      help_text: |
        Transaction modes:
        - Auto: Wraps in BEGIN/COMMIT (safe, auto-rollback on error)
        - Manual: File has own transaction control
        - Read-only: Cannot modify data (safest for queries)
      options:
        - label: Auto (Recommended - wraps in BEGIN/COMMIT)
          value: auto
          description: Automatic rollback on error
        - label: Manual (File has own transactions)
          value: manual
          description: Use when script controls transactions
        - label: Read-only (Cannot modify data)
          value: readonly
          description: Safest for SELECT queries
      default: readonly
      output_var: transaction_mode
    error_handling:
      strategy: fail
  - id: step_4_safety_check
    name: Check for Dangerous Operations
    type: execute
    description: Detect potentially destructive SQL patterns
    command: |
      SQL_TO_CHECK=""

      if [ "{{query_source}}" = "file" ]; then
        if [ ! -f "{{sql_file}}" ]; then
          echo "❌ SQL file not found: {{sql_file}}"
          exit 1
        fi
        SQL_TO_CHECK=$(cat "{{sql_file}}")
      else
        SQL_TO_CHECK="{{sql_content}}"
      fi

      DANGEROUS="DROP TABLE|TRUNCATE|DELETE.*WHERE.*1.*=.*1|UPDATE.*WHERE.*1.*=.*1|DROP DATABASE|ALTER TABLE.*DROP"

      if echo "$SQL_TO_CHECK" | grep -Eiq "$DANGEROUS"; then
        echo "⚠️  WARNING: Potentially DESTRUCTIVE operation detected!"
        echo ""
        echo "Detected dangerous patterns in SQL:"
        echo "$SQL_TO_CHECK" | grep -Ei "$DANGEROUS" | head -5
        echo ""
        echo "dangerous_operation_detected=true"
        exit 0
      else
        echo "✅ No dangerous operations detected"
        echo "dangerous_operation_detected=false"
        exit 0
      fi
    outputs:
      dangerous_detected: "{{output}}"
    error_handling:
      strategy: warn
  - id: step_5_confirm_dangerous
    name: Confirm Destructive Operation
    type: elicit
    condition: "{{dangerous_detected}} contains 'true'"
    elicit:
      question: |
        ⚠️  DESTRUCTIVE OPERATION DETECTED ⚠️

        This SQL may DELETE, DROP, or TRUNCATE data.

        Are you absolutely sure you want to proceed?
      options:
        - label: YES - I UNDERSTAND THE RISKS
          value: confirmed
          description: Proceed with destructive operation
        - label: NO - Cancel Operation
          value: cancel
          description: Abort and review SQL
      default: cancel
      output_var: dangerous_confirmed
    error_handling:
      strategy: fail
      message: Operation cancelled for safety
  - id: step_6_check_confirmation
    name: Verify Dangerous Operation Confirmation
    type: execute
    condition: "{{dangerous_confirmed}} == 'cancel'"
    command: |
      echo "❌ Operation cancelled by user"
      echo ""
      echo "Review your SQL and try again if needed."
      exit 1
    error_handling:
      strategy: abort
  - id: step_7_execute_sql
    name: Execute SQL Query
    type: task
    task: db-run-sql
    description: Execute SQL with timing and error handling
    inputs:
      sql: "{% if query_source == 'file' %}{{sql_file}}{% else %}{{sql_content}}{% endif %}"
      transaction_mode: "{{transaction_mode}}"
    environment:
      TRANSACTION_MODE: "{{transaction_mode}}"
    error_handling:
      strategy: fail
      message: |
        ❌ SQL execution failed

        Check:
        1. SQL syntax is correct
        2. Tables/columns exist
        3. User has required permissions
        4. Database connection is active

        Output saved to: /tmp/dbsage_sql_output.txt
    outputs:
      execution_success: true
      execution_time: "{{execution_time}}"
      rows_affected: "{{rows_affected}}"
  - id: step_8_performance_option
    name: Offer Performance Analysis
    type: elicit
    condition: "{{execution_time}} > 100 AND {{query_source}} == 'inline'"
    elicit:
      question: |
        Query took {{execution_time}}ms

        Run EXPLAIN ANALYZE for performance insights?
      help_text: Shows execution plan, buffer usage, and identifies performance bottlenecks
      options:
        - label: Yes - Run EXPLAIN ANALYZE
          value: "yes"
          description: Analyze query performance
        - label: No - Skip analysis
          value: "no"
          description: Continue without analysis
      default: "no"
      output_var: run_explain
    error_handling:
      strategy: warn
  - id: step_9_explain_analyze
    name: Run EXPLAIN ANALYZE
    type: task
    task: db-explain
    condition: "{{run_explain}} == 'yes'"
    description: Analyze query execution plan and performance
    inputs:
      sql: "{{sql_content}}"
    error_handling:
      strategy: warn
      message: EXPLAIN ANALYZE failed, but query executed successfully
    outputs:
      explain_plan: "{{output}}"
  - id: step_10_optimization_suggest
    name: Suggest Query Optimization
    type: execute
    condition: "{{execution_time}} > 1000"
    description: Suggest optimization for slow queries (>1s)
    command: |
      echo ""
      echo "⚠️  SLOW QUERY DETECTED (>1000ms)"
      echo ""
      echo "Query took {{execution_time}}ms"
      echo ""
      echo "Recommendations:"
      echo "  1. Run *explain \"<your query>\" to see execution plan"
      echo "  2. Run *query-optimization for interactive optimization"
      echo "  3. Check for missing indexes on WHERE/JOIN columns"
      echo "  4. Consider EXPLAIN (ANALYZE, BUFFERS) for buffer analysis"
      echo ""
      echo "Common issues:"
      echo "  - Sequential scans on large tables → Add indexes"
      echo "  - Row estimate mismatches → Run ANALYZE table_name"
      echo "  - High buffer reads → Add indexes or optimize query"
      echo ""
    error_handling:
      strategy: warn
  - id: step_11_success_summary
    name: Display Success Summary
    type: execute
    description: Show execution summary and next steps
    command: |
      echo ""
      echo "════════════════════════════════════════"
      echo "✅ QUERY EXECUTED SUCCESSFULLY"
      echo "════════════════════════════════════════"
      echo ""
      echo "Query Details:"
      echo "  Source: {{query_source}}"
      echo "  Transaction Mode: {{transaction_mode}}"

      {% if rows_affected %}
      echo "  Rows Affected: {{rows_affected}}"
      {% endif %}

      {% if execution_time %}
      echo "  Execution Time: {{execution_time}}ms"
      {% endif %}

      echo ""
      echo "Output: /tmp/dbsage_sql_output.txt"
      echo ""

      {% if execution_time > 1000 %}
      echo "Performance Note:"
      echo "  ⚠️ Query is slow (>1s) - consider optimization"
      echo ""
      {% endif %}

      echo "Next Steps:"
      echo "  *explain \"<query>\"    - Analyze query performance"
      echo "  *query-optimization    - Interactive optimization session"
      echo "  *query                 - Run another query"
      echo ""
outputs:
  query_executed:
    type: boolean
    description: Query executed successfully
    source: step_7_execute_sql.execution_success
  execution_time:
    type: number
    description: Query execution time in milliseconds
    source: step_7_execute_sql.execution_time
  rows_affected:
    type: number
    description: Number of rows affected by query
    source: step_7_execute_sql.rows_affected
  output_file:
    type: string
    description: Path to query output file
    value: /tmp/dbsage_sql_output.txt
  performance_analyzed:
    type: boolean
    description: Whether EXPLAIN ANALYZE was run
    source: step_9_explain_analyze.completed
global_error_handling:
  on_error: abort
  notification:
    enabled: true
    channels:
      - console
  rollback_on_error: true
security:
  authorization_required: false
  audit_logging: true
  dangerous_operation_confirmation: true
  redact_secrets: true
```


## Referência: references/squad/workflows/setup-database-workflow.yaml

```yaml
workflow:
  id: setup-database
  name: Setup Database Connection
  description: Interactive workflow to configure and validate database connections (local, remote, or Supabase)
  version: 1.0.0
  type: sequential
  sequence:
    - phase: select_connection_type
      agent: db-sage
      action: select_connection_type
      description: Choose whether the user is configuring a local, remote, or Supabase PostgreSQL connection.
      outputs:
        - connection_type
    - phase: capture_connection_details
      agent: db-sage
      action: capture_connection_details
      description: Collect the connection fields required for the selected PostgreSQL/Supabase runtime.
      condition: connection_type_selected
      outputs:
        - connection_string
        - connection_alias
    - phase: validate_environment
      agent: db-sage
      task: db-env-check
      description: Validate client tooling and environment readiness before connection tests.
    - phase: test_connection
      agent: db-sage
      action: test_database_connection
      description: Execute a live connectivity check using the resolved connection string.
      outputs:
        - connection_valid
    - phase: persist_connection_metadata
      agent: db-sage
      action: persist_connection_metadata
      description: Store non-secret connection metadata and alias guidance for later reuse.
    - phase: summarize_setup
      agent: db-sage
      action: summarize_setup
      description: Present the validated setup summary and next actions.
    - workflow_end:
        id: complete
        action: workflow_complete
metadata:
  author: DB Sage
  created_date: "2025-10-27"
  last_modified: "2025-10-27"
  tags:
    - database
    - setup
    - connection
    - db-sage
  story: squads/db-sage/docs/stories/1.1.setup-database-workflow.md
inputs:
  connection_type:
    type: string
    description: "Connection type: local, remote, or supabase"
    required: false
    validation: "Must be: local, remote, or supabase"
  connection_alias:
    type: string
    description: Friendly name for this connection
    required: false
    default: default
steps:
  - id: step_1_select_type
    name: Select Connection Type
    type: elicit
    elicit:
      question: "Select database connection type:"
      options:
        - label: Local PostgreSQL (localhost:5432)
          value: local
          description: PostgreSQL running on your local machine
        - label: Remote PostgreSQL (any host)
          value: remote
          description: PostgreSQL on remote server or cloud
        - label: Supabase Project
          value: supabase
          description: Supabase managed PostgreSQL (recommended)
      default: supabase
      output_var: connection_type
    error_handling:
      strategy: fail
      message: Connection type selection is required
  - id: step_2a_local_details
    name: Get Local Connection Details
    type: elicit
    condition: "{{connection_type}} == 'local'"
    elicit:
      fields:
        - name: host
          label: Host
          type: string
          default: localhost
          required: true
        - name: port
          label: Port
          type: number
          default: "5432"
          required: true
        - name: database
          label: Database name
          type: string
          required: true
          placeholder: myapp_dev
        - name: user
          label: Username
          type: string
          default: postgres
          required: true
        - name: password
          label: Password
          type: password
          required: true
          secret: true
      output_vars:
        - host
        - port
        - database
        - user
        - password
    outputs:
      connection_string: postgresql://{{user}}:{{password}}@{{host}}:{{port}}/{{database}}
    error_handling:
      strategy: fail
  - id: step_2b_remote_details
    name: Get Remote Connection Details
    type: elicit
    condition: "{{connection_type}} == 'remote'"
    elicit:
      fields:
        - name: host
          label: Host (hostname or IP)
          type: string
          required: true
          placeholder: db.example.com
        - name: port
          label: Port
          type: number
          default: "5432"
          required: true
        - name: database
          label: Database name
          type: string
          required: true
        - name: user
          label: Username
          type: string
          required: true
        - name: password
          label: Password
          type: password
          required: true
          secret: true
        - name: ssl_mode
          label: SSL Mode
          type: choice
          options:
            - require
            - verify-full
            - prefer
            - disable
          default: require
          required: true
      output_vars:
        - host
        - port
        - database
        - user
        - password
        - ssl_mode
    outputs:
      connection_string: postgresql://{{user}}:{{password}}@{{host}}:{{port}}/{{database}}?sslmode={{ssl_mode}}
    error_handling:
      strategy: fail
  - id: step_2c_supabase_details
    name: Get Supabase Connection Details
    type: elicit
    condition: "{{connection_type}} == 'supabase'"
    elicit:
      help_text: |
        Get these values from your Supabase Dashboard:
        Settings → Database → Connection string
        Settings → API → Project API keys
      fields:
        - name: project_ref
          label: Project Reference (e.g., abcdefghijklmnop)
          type: string
          required: true
          placeholder: abcdefghijklmnop
          validation: Must be 16 characters
        - name: db_password
          label: Database Password
          type: password
          required: true
          secret: true
          help: Database password from project setup
        - name: pooler_mode
          label: Use Connection Pooler?
          type: boolean
          default: true
          help: Recommended for serverless (port 6543)
        - name: anon_key
          label: Anon Key (public)
          type: string
          required: false
          secret: false
          help: "Optional: For client-side access"
        - name: service_role_key
          label: Service Role Key (DANGEROUS - admin access)
          type: string
          required: false
          secret: true
          help: "⚠️ CAUTION: Bypasses RLS policies"
      output_vars:
        - project_ref
        - db_password
        - pooler_mode
        - anon_key
        - service_role_key
    outputs:
      pooler_port: "{% if pooler_mode %}6543{% else %}5432{% endif %}"
      pooler_suffix: "{% if pooler_mode %}-pooler{% else %}{% endif %}"
      connection_string: postgresql://postgres:{{db_password}}@{{project_ref}}{{pooler_suffix}}.supabase.co:{{pooler_port}}/postgres?sslmode=require
      supabase_url: https://{{project_ref}}.supabase.co
    error_handling:
      strategy: fail
  - id: step_3_validate_env
    name: Validate Database Environment
    type: task
    task: db-env-check
    description: Check PostgreSQL client tools and environment
    environment:
      DATABASE_URL: "{{connection_string}}"
    error_handling:
      strategy: fail
      message: |
        ❌ Environment validation failed

        Please ensure:
        1. PostgreSQL client tools installed (psql, pg_dump)
        2. Database is accessible
        3. Credentials are correct
    outputs:
      env_valid: true
  - id: step_4_test_connection
    name: Test Database Connection
    type: execute
    description: Run test query to validate connection
    environment:
      DB_SAGE_CONNECTION_URL: "{{connection_string}}"
    command: |
      echo "Testing database connection..."

      # Test with SELECT 1
      psql "$DB_SAGE_CONNECTION_URL" \
        -v ON_ERROR_STOP=1 \
        -t \
        -c "SELECT 1 AS connection_test;" > /dev/null 2>&1

      if [ $? -eq 0 ]; then
        echo "✅ Connection successful"

        # Get database version
        VERSION=$(psql "$DB_SAGE_CONNECTION_URL" -t -c "SELECT version();")
        echo "📊 Database: $VERSION"

        exit 0
      else
        echo "❌ Connection failed"
        echo ""
        echo "Common issues:"
        echo "  1. Check database is running"
        echo "  2. Verify credentials (username/password)"
        echo "  3. Check network/firewall allows connection"
        echo "  4. Verify database exists"

        exit 1
      fi
    timeout: 10000
    error_handling:
      strategy: fail
      retry_count: 2
      message: |
        ❌ Connection test failed after 2 retries

        Troubleshooting:
        - Network: ping {{host}}
        - Firewall: Check port {{port}} is open
        - Credentials: Verify username/password
        - Database: Verify database name exists
    outputs:
      connection_valid: true
  - id: step_5_store_connection
    name: Store Connection Configuration
    type: execute
    description: Save non-sensitive connection profile metadata for reuse
    command: |
      mkdir -p .db-sage

      ALIAS="{{connection_alias}}"
      [ -z "$ALIAS" ] && ALIAS="default"
      TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
      ENV_VAR="DATABASE_URL"

      if [ "{{connection_type}}" = "supabase" ]; then
        ENV_VAR="SUPABASE_DB_URL"
      fi

      CONNECTIONS_FILE=".db-sage/connection-profiles.yaml"

      if [ ! -f "$CONNECTIONS_FILE" ]; then
        printf '%s\n' \
          '# DB Sage Connection Profiles' \
          '# Credentials stay in environment variables; this file stores metadata only.' \
          'profiles:' \
          > "$CONNECTIONS_FILE"
      fi

      SAFE_HOST="{{host}}"
      [ -z "$SAFE_HOST" ] && SAFE_HOST="supabase"

      SAFE_DB="{{database}}"
      [ -z "$SAFE_DB" ] && SAFE_DB="postgres"

      SAFE_PROJECT_REF="{{project_ref}}"
      SAFE_POOLER="{{pooler_mode}}"
      [ -z "$SAFE_POOLER" ] && SAFE_POOLER="false"

      printf '%s\n' \
        "  - alias: \"$ALIAS\"" \
        "    type: \"{{connection_type}}\"" \
        "    env_var: \"$ENV_VAR\"" \
        "    created_at: \"$TIMESTAMP\"" \
        "    metadata:" \
        "      host: \"$SAFE_HOST\"" \
        "      database: \"$SAFE_DB\"" \
        "      project_ref: \"$SAFE_PROJECT_REF\"" \
        "      pooler: \"$SAFE_POOLER\"" \
        >> "$CONNECTIONS_FILE"

      echo "✅ Connection profile saved as: $ALIAS"
      echo "📁 File: $CONNECTIONS_FILE"
      echo "🔐 Secret storage: environment variable only ($ENV_VAR)"
      echo ""
      echo "No plaintext connection string was written to disk."
    error_handling:
      strategy: warn
      message: ⚠️ Failed to store connection, but you can still use it
    outputs:
      connection_alias: "{{connection_alias}}"
      connections_file: .db-sage/connection-profiles.yaml
  - id: step_6_success_summary
    name: Display Success Summary
    type: execute
    description: Show connection summary and next steps
    command: |
      echo ""
      echo "════════════════════════════════════════"
      echo "✅ DATABASE CONNECTION SETUP COMPLETE"
      echo "════════════════════════════════════════"
      echo ""
      echo "Connection Details:"
      echo "  Type: {{connection_type}}"
      echo "  Alias: {{connection_alias}}"

      {% if connection_type == 'supabase' %}
      echo "  Project: {{project_ref}}"
      echo "  Pooler: {{pooler_mode}}"
      echo "  URL: https://{{project_ref}}.supabase.co"
      {% else %}
      echo "  Host: {{host}}"
      echo "  Port: {{port}}"
      echo "  Database: {{database}}"
      {% endif %}

      echo ""
      echo "Environment Variable:"
      {% if connection_type == 'supabase' %}
      echo "  export SUPABASE_DB_URL=\"<redacted>\""
      {% else %}
      echo "  export DATABASE_URL=\"<redacted>\""
      {% endif %}
      echo "  Stored profile contains metadata only"
      echo ""
      echo "Next Steps:"
      echo "  1. *domain-modeling - Design database schema"
      echo "  2. *create-schema   - Create schema documentation"
      echo "  3. *bootstrap       - Initialize project structure"
      echo "  4. *env-check       - Verify environment anytime"
      echo ""
      echo "Troubleshooting:"
      echo "  *help               - Show all available commands"
      echo "  *env-check          - Re-validate environment"
      echo ""
outputs:
  connection_established:
    type: boolean
    description: Connection successfully established
    source: step_4_test_connection.connection_valid
  connection_string:
    type: string
    description: PostgreSQL connection string
    source: connection_string
    secret: true
  connection_alias:
    type: string
    description: Connection alias for future reference
    source: step_5_store_connection.connection_alias
  connections_file:
    type: string
    description: Path to stored connections file
    source: step_5_store_connection.connections_file
global_error_handling:
  on_error: abort
  notification:
    enabled: true
    channels:
      - console
security:
  authorization_required: false
  audit_logging: true
  redact_secrets: true
  secrets:
    - password
    - db_password
    - service_role_key
    - connection_string
```
