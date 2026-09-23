# Task: Migrate Workflows -- Archive + Cleanup

**Task ID:** migrate-workflows-archive
**Parent Task:** `migrate-workflows-to-yaml.md`
**Purpose:** Archive original .md files, update cross-references, verify no broken links
**Execution Type:** Worker
**Model:** `Haiku`
**Haiku Eligible:** YES

---

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Migrate Workflows -- Archive + Cleanup |
| **status** | `active` |
| **responsible_executor** | @squad-chief |
| **execution_type** | Worker |
| **input** | Validated .yaml files + original .md files |
| **output** | Archived .md files + updated references |
| **action_items** | 3 steps |
| **acceptance_criteria** | Originals archived, references updated, no broken links |

---

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-MWY-002 | Originals must be archived before deletion | Verify _archive/ exists and originals copied | VETO - BLOCK |
| VETO-MWY-003 | Cross-references must be identified before archiving | Grep for .md filenames across tasks, workflows, config | VETO - BLOCK |

---

## Workflow

### Step 1: Identify Cross-References

```bash
# Find all references to the source .md filenames
grep -r "{workflow-name}.md" squads/{squad}/tasks/ squads/{squad}/workflows/ squads/{squad}/config.yaml
```

Record all files that reference the original .md workflow files.

### Step 2: Archive Originals

- [ ] Create `workflows/_archive/` directory if it does not exist
- [ ] Copy each original .md file to `_archive/`
- [ ] Verify copies exist in _archive/

### Step 3: Update References and Clean

- [ ] Update all cross-references to point to new .yaml files
- [ ] Remove original .md files from workflows/ (they are now in _archive/)
- [ ] Verify `ls workflows/*.md` returns empty (except _archive/)

---

## Error Handling

### Broken References

- **Trigger:** Another file references the old .md name
- **Detection:** Grep for .md filename in dependencies
- **Recovery:** Update reference to new .yaml path
- **Prevention:** Search references before archiving

---

## Output Contract

```yaml
archive_results:
  archived_files:
    - original: "{path}"
      archive: "{_archive/path}"
  references_updated:
    - file: "{path}"
      old_ref: "{old.md}"
      new_ref: "{new.yaml}"
  broken_references: []
  cleanup_complete: true|false
```

---

## Handoff Checklist

Before handoff, verify:

- [ ] All workflows migrated pass validation
- [ ] No broken references to .md files
- [ ] _archive/ contains backups
- [ ] workflows/ contains only .yaml files (except _archive/)

---

## Completion Criteria

- [ ] _archive/ directory created with all original .md files
- [ ] All cross-references updated to .yaml paths
- [ ] No .md workflow files remain in workflows/ root
- [ ] No broken references detected

---

_Task Version: 1.0.0_
_Pattern: Atomic sub-task of migrate-workflows-to-yaml.md_

## Acceptance Criteria

- [ ] Originals archived
- [ ] references updated
- [ ] no broken links
