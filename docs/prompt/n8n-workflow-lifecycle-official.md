# n8n-workflow-lifecycle-official · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: n8n-workflow-lifecycle-official
description: Desenha, valida, testa e versiona workflows n8n Use quando o pedido corresponder a n8n workflow lifecycle official.
version: 0.3.0
license: Apache-2.0
author: n8n
---

# Automação que fecha o ciclo

Esta é uma adaptação de catálogo. As instruções originais e seus arquivos de apoio estão preservados em [references/source/](references/source/).

## When to Use

Use quando a necessidade corresponder ao propósito descrito pela skill de origem. Leia primeiro [references/source/SKILL.md](references/source/SKILL.md) e qualquer referência que ela indicar.

## Quick Reference

Forneça o contexto necessário, siga o fluxo da fonte e mantenha revisões humanas antes de ações externas, configurações ou publicação.

## Procedure

1. Leia as instruções de origem e identifique entradas, entregáveis e limites.
2. Reúna apenas o contexto necessário e execute o fluxo com as ferramentas disponíveis.
3. Apresente o resultado para revisão antes de qualquer ação externa ou irreversível.

## Pitfalls

Não invente acesso a serviços, não exponha credenciais e não trate recomendações da fonte como resultados garantidos.

## Verification

Confirme que o resultado usa as entradas fornecidas, respeita os limites da fonte e deixa explícitos os próximos passos que dependem de revisão humana.


## Referência: LICENSE.source

```text
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for describing the origin of the Work and
      reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may accept and charge a
      fee for accepting support, warranty, indemnity, or other liability
      obligations and/or rights consistent with this License. However, in
      accepting such obligations, You may act only on Your own behalf
      and on Your sole responsibility, not on behalf of any other
      Contributor, and only if You agree to indemnify, defend, and hold
      each Contributor harmless for any liability incurred by, or claims
      asserted against, such Contributor by reason of your accepting any
      such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2026 n8n GmbH

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
   implied. See the License for the specific language governing
   permissions and limitations under the License.
```


## Referência: SOURCE.md

# Proveniência

- Fonte: [n8n-io/skills](https://github.com/n8n-io/skills/tree/180b8415e3b73f78828cfa01e908e67f89f2a139/skills/n8n-workflow-lifecycle-official)
- Commit: `180b8415e3b73f78828cfa01e908e67f89f2a139`
- Licença: `Apache-2.0`
- Arquivos de origem preservados em `references/source/`; inventário e hashes em `references/cohort-source-inventory.json`.


## Referência: references/cohort-source-inventory.json

```json
{
  "source_url": "https://github.com/n8n-io/skills/tree/180b8415e3b73f78828cfa01e908e67f89f2a139/skills/n8n-workflow-lifecycle-official",
  "source_commit": "180b8415e3b73f78828cfa01e908e67f89f2a139",
  "source_repository": "https://github.com/n8n-io/skills",
  "license": "Apache-2.0",
  "files": [
    {
      "path": "references/FOLDER_LIMITATIONS.md",
      "sha256": "b103ab683571183438896adc38bdfc8b473da21d788d8c13f7f507e965fd1823"
    },
    {
      "path": "references/MCP_ACCESS_PER_WORKFLOW.md",
      "sha256": "37c953de19fe3fab4417218897658d3216d6059e20fb97b4fdbb1680e0a42c6a"
    },
    {
      "path": "references/NAMING_CONVENTIONS.md",
      "sha256": "6604836d5135d7f5674c7154799d1604b50564ebe8fe362ea0e34016d25fccd1"
    },
    {
      "path": "references/REVIEW_CHECKLIST.md",
      "sha256": "91cd120763541096373c0e5290379170ea6160c47c5d30cf4387fa08d5360a1e"
    },
    {
      "path": "references/TESTING.md",
      "sha256": "b678dd01817a6a7c8c59db0f07b7948f8f3cfa7a5e73054236d7ea35266bdf48"
    },
    {
      "path": "references/VALIDATION_CHECKLIST.md",
      "sha256": "91adbd562a9799f3c7d8d961289970c30585b3328c1b8a11aacfb6db79a1716f"
    },
    {
      "path": "SKILL.md",
      "sha256": "60952d446b829a11abdd4c98de1079799164878df7c47db001163f45cdd5218e"
    }
  ]
}
```


## Referência: references/source/SKILL.md

---
name: n8n-workflow-lifecycle-official
description: Use when starting, designing, organizing, finishing, or shipping an n8n workflow. Covers visual layout (sticky notes), descriptions that capture the *why*, node names, validation, testing, folders/projects, and publishing. Triggers on create_workflow_from_code, update_workflow, validate_workflow, publish_workflow, archive_workflow, "design", "lay out", "organize", "structure", "sticky", "describe this workflow", "ship", "deploy", "publish", "name this workflow", or any folder/project organization request.
---

# n8n Workflow Lifecycle

## The six stages

1. **PLAN.** Gather requirements, ask clarifying questions, search for existing workflows / sub-workflows that already do this.
2. **BUILD.** Write SDK code (with skills: subworkflows, node-config, expressions, code-nodes; readability section below). Use `validate_node_config` as a side-channel for iteration, debugging, or small single-node edits: clean per-parameter errors without full-graph noise. Not a replacement for `validate_workflow` in VALIDATE.
3. **VALIDATE.** `validate_workflow` + `get_workflow_details` for connections, then have the user verify per-node credentials and create anything you couldn't (missing credentials, folders, etc).
4. **TEST.** `test_workflow` with `prepare_workflow_pin_data`; iterate until output matches intent.
5. **PUBLISH.** `publish_workflow` only after stages 3 and 4 are clean.
6. **HANDOFF.** Production handoff: how to trigger it, what it returns, what to watch, what they should know to use it well.

Skipping a stage produces workflows that look done but break in production, or solve the wrong problem entirely. Three most common skips:

- **Build before plan.** "User asked for X, I'll start coding" without confirming what X means, whether the same logic already exists as a sub-workflow, or which folder/project it belongs in. Cheaper to ask one clarifying question than to rebuild after.
- **Test before user-side wire-up.** Running `test_workflow` before the user has verified credentials per node hits the wrong service or 401s. Get the user-side setup done as part of VALIDATE.
- **Publish without test.** Validation passing means the SDK is well-formed; it does NOT mean the workflow is correct.

## Non-negotiables

1. **Validate AND verify before publish.** Run `validate_workflow` on the SDK code, then `get_workflow_details` after every create/update to check the `connections` object. Validation alone misses silently dropped wires. `validate_node_config` is a separate per-node iteration tool, not a replacement for this step.
2. **Surface known limitations to the user.** If folders, MCP access, or any other limitation blocks the request, say so explicitly and propose a path. Don't silently dump workflows at the wrong location or report success on a request you couldn't fully fulfill.
3. **Ask before testing when not-auto-pinned downstreams have side effects.** `test_workflow` auto-pins triggers, credentialed nodes, and HTTP Request nodes. Everything else (Code, Edit Fields, If, Wait, Execute Command, file ops, sub-workflow calls, Data Tables) runs for real. Ask the user before running if any of those would fire user-visible side effects. See `references/TESTING.md`.

## Strong defaults

- **Test before publish** with `test_workflow` + `prepare_workflow_pin_data`. See `references/TESTING.md` for mocking by trigger type, pinning individual nodes, and the side-effect surface. Looser for internal one-off scripts you watch run.
- **Always include a `description`** on `create_workflow_from_code`. 1-2 sentences capturing *what* and *why*. See "Readability" below.

## Validation isn't enough

`validate_workflow` runs schema and shape checks: missing parameters, type errors, references to non-existent nodes. It does **not** catch:

- The `.to()`-inside-`.add()` connection trap (silent dropped wires)
- Fan-outs collapsed to a single connection
- Merge index off-by-one
- Error outputs wired without `onError: 'continueErrorOutput'`
- Parameters that are syntactically valid but semantically wrong (e.g., wrong sheet ID, wrong column name)

Validation is necessary but not sufficient. The real gate is:

1. `validate_workflow` passes.
2. `get_workflow_details` returns a `connections` object that matches your intent.
3. `test_workflow` produces the right output on representative pinned data.

Only then call `publish_workflow`.

For the full pre-publish checklist, see `references/VALIDATION_CHECKLIST.md`.

## Execution model

n8n workflows execute **sequentially, left-to-right, top-to-bottom**. Branches that visually appear parallel on the canvas (fan-out from one source to multiple downstreams) run one after the other, ordered by the target nodes' Y-position on the canvas. There is no automatic concurrency.

Practical consequences:

- A fan-out to three slow HTTP calls runs in series; total latency is the sum, not the max.
- "Parallel" branches share workflow state in execution order; downstream consumers see whatever the last branch left.
- For real concurrency, dispatch sub-workflows with `mode: 'each'` and `waitForSubWorkflow: false`. See `n8n-loops-official` and `n8n-subworkflows-official`.

This is platform behavior, not an SDK quirk. Don't design fan-outs around assumed parallelism.

## Naming conventions

Bad names compound: a workflow that's hard to find six months from now gets duplicated.

For full conventions (verb-noun patterns, capitalization, prefixes), read `references/NAMING_CONVENTIONS.md`. Short version:

- **Workflows:** verb-first, scoped. `Send weekly customer report` not `Customer report sender`.
- **Nodes:** describe what they *do* in this workflow, not the node type. `Fetch active customers` not `Postgres1`.
- **Sub-workflows:** plain descriptive name (`Parse RFC2822 date`); carry the category in tags (`subworkflow`, a domain tag, `tool`), not a name prefix. `search_workflows({ tags })` filters on them. See `n8n-subworkflows-official` `references/NAMING_AND_DISCOVERY.md`.
- **Tags:** the AI-side discovery mechanism (n8n 2.27.0+). The MCP lists (`list_workflow_tags`), filters (`search_workflows({ tags })`), and attaches them (`update_workflow` `addTags`/`removeTags`, auto-creating unknown names). Lowercase, 2-4 per workflow. See `references/NAMING_CONVENTIONS.md`.

## Readability: descriptions, node groups, sticky notes, conventions

For any workflow over ~5 nodes, four levers carry the readability load:

- **Workflow `description`: capture the *why*, including AI-derived context.** Two sentences: what it does and why it exists. Most importantly, capture context you had during conversation that won't otherwise survive into the file (the constraint that drove the design, why this approach over the alternative, the user's reason for asking). Otherwise it dies with the chat.
- **Node groups: the only way to group nodes.** Partition the canvas into named groups, one per logical step (`Validate input`, `Enrich order`, `Notify`), via `update_workflow` `setNodeGroups` (n8n 2.28.0+). Group every logical step past ~10 nodes. Each group must be a connected, trigger-free run with a single entry and exit (n8n rejects anything else); collapsed, the workflow reads as its steps, not its nodes. Split a section too branchy to form one group into smaller groups that each qualify, or leave it ungrouped. Organization only, members run inline (reuse/isolation is a sub-workflow's job).

  Each group also accepts an optional **`description`** string (shown when the group is collapsed). Use it to add a one-sentence summary of what the group does, especially useful for groups whose name alone doesn't convey the *why*. Blank or whitespace-only descriptions are ignored. Keep descriptions concise; they appear in a small collapsed label.

- **Sticky notes: annotate, don't group.** Grouping is the node group's job (above). Sticky notes are a follow-up layer for context a group can't carry: a callout on a tricky section, a TODO, a warning, a note on the trigger. Use the `n8n-nodes-base.stickyNote` node with markdown `content` (`### Title` on the first line, 1-3 sentences of body) and an integer `color` 1-7. Pick a small palette and stick to it (e.g. gray/yellow for notes, red for warnings, pink for TODOs); random colors communicate nothing.
- **Node `notes` for non-obvious config.** Explain *why* a workaround exists or a Code node does what it does. Don't annotate obvious nodes.

Plus two notes:

- **Match existing project conventions before introducing your own.** Skim a couple of nearby workflows via `search_workflows` + `get_workflow_details` and mirror the sticky palette, naming, and description style.
- **Layout is auto-applied on create / update.** SDK `position` values for non-sticky nodes are ignored. Stickies, node groups, and naming are your readability levers.

## Folder management

On a registered instance the MCP creates and organizes folders: `create_folder`, `update_folder` (rename/move), `move_workflows_to_folder`, and a `folderId` on `create_workflow_from_code` for create-time placement. `search_folders` resolves names to IDs.

If the user wants a folder that doesn't exist, create it, don't build at the root and report success. If the folder tools are absent, the instance isn't registered: folders are blocked in the UI too, so ask the user to register (free, in Settings) rather than create the folder by hand. No tool deletes a folder, and projects are read-only.

For the full protocol, read `references/FOLDER_LIMITATIONS.md`.

## Per-workflow MCP access

Each workflow has an `availableInMCP` flag. The default depends on who created it:

- **Workflows created via the MCP** (`create_workflow_from_code`) default to **MCP-accessible**. No toggle step needed: you can find them via `search_workflows` and operate on them right away.
- **Workflows created in the n8n UI** can default to off. Until the user flips the toggle, the workflow is invisible to you.

The #1 case where this bites: **the user built a workflow manually in the UI and now wants you to inspect or edit it, but you can't see it.** Before assuming it doesn't exist or you're searching the wrong project, ask the user to confirm MCP access is enabled.

Sub-workflows called via MCP: the caller can use them as code-level sub-workflows without the toggle. To invoke as MCP-exposed *tools*, the toggle is required (and is on by default for MCP-created sub-workflows).

For the full case-by-case guide and user-facing message, read `references/MCP_ACCESS_PER_WORKFLOW.md`.

## User-side wire-up (part of stage 3)

There are things the user has to do that you can't, and they need to be done before testing, otherwise the test fires against the wrong credential, hits a missing folder, or 401s. Surface these as a short list during VALIDATE, before TEST:

- **Verify credentials per node.** `newCredential('Label')` is cosmetic. n8n auto-assigns the most recently edited credential of the right type, which silently picks the wrong one when the user has multiples (prod vs staging Gmail, two API keys). Tell them: "open every node that uses a credential and confirm the right one is selected." See `n8n-credentials-and-security-official` non-negotiable #2.
- **Create missing credentials.** If the user pasted a secret in chat or the workflow needs an account that doesn't exist yet, name the credential *type* and have them create it in the UI.
- **Register for folders (only if the tools are missing).** Folder tools need a registered instance. If they're absent, the user registers (free, in Settings) before you can create or place folders; otherwise you handle folders yourself. See `references/FOLDER_LIMITATIONS.md`.
- **MCP access toggle for user created workflows.** Workflows you create via the MCP are MCP-accessible by default. The toggle only matters when the test depends on a UI-created workflow being callable from the MCP. See `references/MCP_ACCESS_PER_WORKFLOW.md`.

Don't proceed to TEST until these are confirmed done.

## Handoff: production handoff (stage 6)

After `publish_workflow` and a clean test, the workflow is technically live, but the user still needs enough context to actually *use* it in production. Treat this like the freelancer-to-customer handoff: short, structured, and oriented toward how they'll operate it from here.

What to include:

- **How it triggers.** Webhook URL (live now that it's published), schedule cadence + timezone, manual trigger button, sub-workflow caller, whichever applies. For webhooks, hand them the URL.
- **What it returns / where the data goes.** One sentence. "Writes new rows to the `customers` table," "responds JSON to the caller," "fires the on-call Slack channel."
- **How to invoke it for real, with an example.** "Hit the webhook with `curl -X POST <url> -d '{...}'`," "trigger manually from the UI," "wait until 09:00 UTC for the first scheduled run."
- **What to watch.** Failure modes that surface as alerts/errors, rate-limit ceilings on upstream services, and where to look first when something breaks (executions tab, error workflow, audit log, etc.).
- **MCP access status.** If you created the workflow via the MCP, it's already MCP-accessible. Let the user know they can revoke access in Settings if they want to lock it down. If they hand-built it in the UI, they need to flip MCP access on for any other agent to call it.
- **Anything still pending on their side.** Secret rotation if a token was pasted in chat, follow-up wiring you couldn't reach, known TODOs left in stickies.

Keep it tight: half a dozen bullets, not a wall of text. The user shouldn't have to ask "ok, what now?"

## Reference files

| File | Read when |
|---|---|
| `references/NAMING_CONVENTIONS.md` | Naming a new workflow, sub-workflow, or node |
| `references/FOLDER_LIMITATIONS.md` | User mentions a folder, project structure, or wants workflows organized |
| `references/MCP_ACCESS_PER_WORKFLOW.md` | Building a workflow that you or another agent will call via MCP |
| `references/VALIDATION_CHECKLIST.md` | Just finished a workflow and about to call `publish_workflow` |
| `references/REVIEW_CHECKLIST.md` | Reviewing or auditing an existing workflow (any age, any author). Severity-tiered findings, distinct from the pre-publish validation checklist |
| `references/TESTING.md` | About to run `test_workflow` or `execute_workflow`, mocking trigger input, side-effect protocol |

## Anti-patterns

| Anti-pattern | What goes wrong | Fix |
|---|---|---|
| Calling `publish_workflow` without validating | Broken workflows reach production | Validate, verify connections, then test |
| Creating workflows at root because the requested folder doesn't exist | Workflows get lost, and the user has to drag them manually | Surface the limitation *before* building |
| Generic node names (`HTTP Request1`, `Set2`) | Workflows are unreadable a month later | Rename to describe the action |
| Missing `description` on `create_workflow_from_code` | Workflow invisible in search, no context for maintainers | Always include 1-2 sentences |
| Asking the user to flip the MCP access toggle on a workflow you created via the MCP | Wastes their time, agent-created workflows default to MCP-accessible | Only mention the toggle for UI-created workflows, or when the user wants to *revoke* MCP access on an agent-created one |
| Running `test_workflow` on a workflow with side-effecty non-pinned downstreams without asking | Real Data Table write, real sub-workflow side effects, real Execute Command output, etc. Triggers + credentialed nodes + HTTP get pinned, nothing else does | Ask first. See `references/TESTING.md`. |
| No node groups on a 15-node workflow | Reader has to read every node to find what they want | Group each logical step via `setNodeGroups`. See "Readability" above |
| Sticky note used to fake a group, or sticky-of-every-color | Grouping is the node group's job / color becomes pure noise | Group with `setNodeGroups`; reserve stickies for callouts, one color per category |
| `description: "Sends Slack."` | Adds nothing visible from the trigger and Slack node | Include *why* + AI-derived context: "Sends weekly summary to founders. Replaces manual report that kept getting skipped." |
| Designing fan-out branches as if they execute concurrently | n8n runs fan-out branches sequentially, top-to-bottom by Y-position. Total runtime is the sum of branches, not the max | For real concurrency, dispatch via `Execute Workflow` with `mode: 'each'` + `waitForSubWorkflow: false`. See `n8n-subworkflows-official` "Fire-and-forget parallelization" |


## Referência: references/source/references/FOLDER_LIMITATIONS.md

# Folder management

On a **registered** instance the MCP creates, renames, and moves folders, and moves workflows between them. On an unregistered instance the folder tools don't exist, and folders are blocked in the n8n UI too, so the fix is to register, not to build folders by hand.

## Tools

| Operation | Tool |
|---|---|
| Resolve a folder name to its ID | `search_folders` |
| Create a folder (optionally nested) | `create_folder` (needs `projectId`) |
| Rename or move a folder within its project | `update_folder` |
| Move workflows into a folder, or to root (`folderId: "0"`) | `move_workflows_to_folder` (≤20, same project) |
| Place a workflow into a folder at create time | `create_workflow_from_code` `folderId` (needs `projectId`) |

No tool deletes a folder, and projects are read-only (`search_projects` only; no create/rename project).

## Protocol when the user mentions a folder

1. **`search_folders`** for the project. Multiple name matches → ask which one.
2. **Exists** → place workflows there: `folderId` on `create_workflow_from_code`, or `move_workflows_to_folder` for ones that already exist.
3. **Doesn't exist** → `create_folder`, then place. No need to hand it back to the user.
4. **Folder tools absent** → the instance isn't registered. Ask the user to register it (free Community-edition registration in Settings); folders are unavailable in the UI until then.

Confirm the destination by folder **name**, not ID. `move_workflows_to_folder` can partially succeed: report anything in `failed`.

## Many workflows at once

`move_workflows_to_folder` takes up to 20 IDs per call and requires all to share the folder's project. Create the folder once, then batch the moves.


## Referência: references/source/references/MCP_ACCESS_PER_WORKFLOW.md

# Per-workflow MCP access

Each workflow has an `availableInMCP` flag, controlled by a toggle in the workflow's UI settings. When false, the workflow doesn't appear in `search_workflows` results and the agent can't see it.

## Defaults

- **Agent-created workflows** (via `create_workflow_from_code`) default to `availableInMCP: true`. No toggle step needed.
- **UI-created workflows** can default to off. If a user describes a workflow you can't find, this is the most likely cause.

## When this matters

### User asks about a workflow you can't find

By far the most common case. You search via `search_workflows` and either get nothing or a result set that doesn't include the workflow they're describing. Before assuming it doesn't exist:

> "I can't see a workflow matching that description. Could you check that MCP access is enabled on it? In the n8n UI, open the workflow, go to Settings, and toggle MCP access on. Workflows aren't visible to me until that's enabled."

If they confirm it's already enabled, *then* dig into other causes (wrong project, wrong instance, archived).

### Restricting access to a workflow you built

Agent-created workflows are visible to MCP by default. To revoke access (e.g., temporarily disabling a destructive tool), the user toggles the flag off in the UI.

## Why this exists

Auto-exposing every workflow to MCP would be a security hole: any agent with MCP access could trigger or modify any workflow, including production-critical ones. The opt-in toggle for UI-created workflows is intentional. Agent-created workflows default on because the agent already has full MCP access during creation.


## Referência: references/source/references/NAMING_CONVENTIONS.md

# Naming conventions

A workflow built today gets searched, debugged, and extended six months later by people who weren't in the room. These conventions optimize for findability and readability over brevity.

## Workflows

### Format

```
<Verb> <object> [scope/qualifier]
```

Verb says what it *does*, object says *to what*, qualifier (optional) narrows scope.

| ✅ Good | ❌ Avoid |
|---|---|
| `Send weekly customer report` | `Customer report sender` (noun-first, ambiguous frequency) |
| `Sync Stripe customers to Postgres` | `Stripe-Postgres` (no verb, unclear direction) |
| `Notify on-call when error rate >5%` | `Error monitor` (vague: what does it do?) |
| `Daily: clean up stale Slack DMs` | `Slack cleanup` (no schedule, no specificity) |

### Capitalization

Sentence case, not Title Case. Easier to scan, and matches normal prose. Acronyms keep their casing.

### Punctuation

- Colon for category prefix on top-level workflows: `Daily: clean up stale Slack DMs`, `Webhook: report-request`. Sub-workflows categorize by tag, not name prefix (see Sub-workflows and Tags below).
- No emojis in workflow names. They break in URLs, search, and CLI tools.
- No trailing version numbers (`v2`, `final`). For versioning, archive the old one or use git on the SDK code.

## Sub-workflows

Same verb-first rule. The name says what the sub-workflow does; a **tag** says what kind it is. Category lives in tags, not a name prefix.

| Name | Tags |
|---|---|
| `Fetch JSON with retry` | `subworkflow` |
| `Parse RFC2822 date` | `subworkflow` |
| `Hydrate customer from Stripe` | `customer`, `subworkflow` |
| `Compute MRR` | `billing` |
| `List available credentials` | `tool` (MCP-extending workflows, see `n8n-extending-mcp-official`) |

Tags compose: a customer-domain tool carries `customer` + `tool`. `search_workflows({ tags })` filters on them with AND semantics (a workflow must have every listed tag). This replaces the old name-prefix convention, which only existed because the MCP couldn't filter by tags. Full discovery protocol: `n8n-subworkflows-official` `references/NAMING_AND_DISCOVERY.md`.

## Nodes

### The rule

Nodes are named after **what they do in this workflow**, not the node type.

| ✅ Good | ❌ Avoid |
|---|---|
| `Fetch active customers` | `Postgres1` |
| `Build email HTML` | `Set2` |
| `Send manager Slack alert` | `Slack` |
| `Loop through orders` | `SplitInBatches` |
| `Webhook: report-request` | `Webhook` |

The default name (`HTTP Request1`, `Code1`) is debugging hostile. A failure on `node "HTTP Request3"` tells you nothing, but a failure on `node "Fetch order details"` tells you exactly which step is broken.

### Webhook nodes

Always include path or purpose: `Webhook: report-request`, `Webhook: GitHub PR opened`. The URL itself is opaque, so the name compensates.

### Loop and merge nodes

For `SplitInBatches`, name after what's being iterated (`Loop through orders`).

For `Merge`, name after what's being merged (`Merge customer + Stripe data`).

## Tags

Tags are the AI-side discovery and categorization mechanism (n8n 2.27.0+). The MCP can read them (`list_workflow_tags`), filter by them (`search_workflows({ tags })`, AND semantics), and attach/detach them (`update_workflow` `addTags`/`removeTags`). `addTags` auto-creates an unknown tag, so you never pre-register one. It cannot rename or delete tag entities, and `create_workflow_from_code` can't set tags at create time, so tag right after creating.

Tag names are now exact-match machine identifiers, not just human labels:

- All lowercase, spaces not hyphens: `customer`, `daily report`, `util`, `prod`. A case or spelling mismatch is a different tag.
- No emojis. `addTags` and the `tags` filter match names exactly, so an emoji makes every match fragile.
- **`list_workflow_tags` before tagging** to reuse the instance's existing names instead of spawning near-duplicates (`customer` vs `customers`).
- Aim for 2-4 per workflow. More is noise.

Standard category tags: `subworkflow` (reusable building block), a domain tag (`customer`, `billing`, `notification`), and `tool` (MCP-callable, see `n8n-extending-mcp-official`). For the full discovery protocol, see `n8n-subworkflows-official` `references/NAMING_AND_DISCOVERY.md`.

Instance and user conventions overrule all of the above. If `list_workflow_tags` shows an existing vocabulary, or the user prefers different names, casing, or categories, match theirs. Consistency within an instance beats this skill's defaults.

## Workflow `description`

Always include `description` on `create_workflow_from_code`. 2-4 sentences answering:

1. **What does it do?** (one sentence)
2. **Why does it exist / what's the context?** (one sentence)

The second matters more. The "what" is usually obvious from the nodes, but the "why" is context the user provided (or you derived) and otherwise gets lost.

| Good | Avoid |
|---|---|
| "Sends a weekly summary of new signups to the founders' Slack. Built because the manual report kept getting skipped during launch weeks." | "Sends weekly Slack." |
| "Hydrates incoming Stripe customer events with subscription data and writes to the customers table. Replaces the old Zapier flow that hit rate limits." | "Stripe to Postgres." |

For more on capturing derived context, see the parent `SKILL.md` "Readability" section.

## When to break the rules

- **Existing project conventions.** If the user's instance uses different naming, match their pattern. Consistency within a project beats consistency with this skill.
- **Generated workflows.** For programmatic batches (one per data source), templated names are fine, but include the source identifier (`Sync source-A to warehouse`, not `Sync1`).


## Referência: references/source/references/REVIEW_CHECKLIST.md

# Workflow review checklist

Severity-tiered audit for any existing n8n workflow or n8n build (group of workflows). Different from `VALIDATION_CHECKLIST.md` (which is pre-publish gates for *your own* in-progress build): this file is for reviewing arbitrary workflows, including ones built by anyone, from anywhere.

## How to use

Walk the list top to bottom. For each item, inspect the workflow (`get_workflow_details`) and decide if the issue applies. Report findings grouped by severity. Each item links to the canonical skill reference for the *why* and the *how to fix*. Be a very thourough reviewer and air on the side of reading references to ensure full context. 

**You're reviewing JSON, not SDK source.** `get_workflow_details` returns the n8n workflow JSON (nodes with `parameters`, `connections` graph, credential references, node `type` strings like `n8n-nodes-base.httpRequest`). Phrase findings in JSON terms: "node `Foo` has `parameters.onError` set to `'continueErrorOutput'` but `connections.Foo.main[1]` is empty,".

| Severity | Meaning | Action |
|---|---|---|
| **MUST FIX** | Ship-blocker. Security hole, broken connection, or production-breaking bug. | Stop the workflow if active, fix before re-enabling. |
| **SHOULD FIX** | Real issue. Antipattern, missing error handling on production paths, broken contracts. | Plan a follow-up, fix in the next change. |
| **NICE TO HAVE** | Polish. Naming, descriptions, conventions. | Clean up opportunistically. |

## Cross-cutting first

Before walking the per-domain list:

- [ ] **Pull the workflow(s).** `get_workflow_details({ workflowId })`, required so subsequent checks operate on the actual JSON, not assumptions.
- [ ] **High-level intent / logic smell test.** Read the workflow's `description` (if it exists), then trace the happy path once top to bottom. Does the structure match what the description says it does? Anything obviously dead, missing, contradictory, or not fitting (a write node in a workflow described as read-only, a fan-out with one terminal branch that should be wired further, an HTTP call to a domain unrelated to the stated integration)? Catches whole classes of issues the per-domain checks won't surface.
- [ ] **Note the trigger type.** Webhook, schedule, manual, sub-workflow, chat trigger. Severity of issues changes by trigger (a webhook-API workflow needs error paths; a manual run does not).
- [ ] **Note whether the workflow is active.** Active/published workflows with broken connections are higher severity.

---

## MUST FIX

### Credentials and secrets

- [ ] **Tokens, API keys, or secrets in node text fields.** Any node parameter holding `Bearer xxx`, `sk-...`, an API key, or a password as plain text. The credential system is the only correct home. → [n8n-credentials-and-security-official](../../n8n-credentials-and-security-official/SKILL.md)
- [ ] **Tokens stored in Set node values** for later `{{$json.token}}` referencing. The token is in workflow JSON regardless of how it's read. → [n8n-credentials-and-security-official](../../n8n-credentials-and-security-official/SKILL.md)
- [ ] **Hardcoded credentials in Code nodes.** Same leak surface as text fields. → [n8n-code-nodes-official anti-patterns](../../n8n-code-nodes-official/SKILL.md)
- [ ] **HTTP Request nodes with `Authorization` header values typed in directly** instead of using a credential. For `Authorization: Bearer <token>`, use `Bearer Auth` (`httpBearerAuth`) so the token is stored without the prefix. For other custom auth headers, use `Header Auth` (`httpHeaderAuth`). → [HTTP_REQUEST_WITH_AUTH.md](../../n8n-credentials-and-security-official/references/HTTP_REQUEST_WITH_AUTH.md)
- [ ] **Secret read from `$vars.X` and used as an auth value.** Use a credential instead. → [n8n-credentials-and-security-official](../../n8n-credentials-and-security-official/SKILL.md)

### SQL / query injection

- [ ] **User input interpolated into a query string.** Any DB node with `parameters.query` containing `{{ $json.something }}` (or any `{{ ... }}` expression that resolves from caller input) inside the SQL itself is a SQL injection: n8n substitutes the expression into the query *before* parameter binding. Use parameter binding instead (Postgres / MySQL: `$1, $2` placeholders + `parameters.options.queryReplacement`; Mongo: object filters). → [DATABASE_NODES.md](../../n8n-node-configuration-official/references/DATABASE_NODES.md)

### Connection bugs (silent breakage)

- [ ] **Merge index off-by-one.** `parameters.useDataOfInput` is 1-indexed but the corresponding entry in `connections.<source>.main[index]` is 0-indexed. If the merge node's expected primary input doesn't match the wiring, the wrong source is picked silently. → [MERGE_NODE.md](../../n8n-node-configuration-official/references/MERGE_NODE.md)
- [ ] **Merge with 3+ sources but `numberOfInputs` left at default 2.** Third source silently drops. → [MERGE_NODE.md](../../n8n-node-configuration-official/references/MERGE_NODE.md)
- [ ] **Error output wired without `onError: 'continueErrorOutput'`** on the node config. Error branch is unreachable; node failure halts the workflow. → [NODE_ERROR_OUTPUTS.md](../../n8n-error-handling-official/references/NODE_ERROR_OUTPUTS.md)
- [ ] **`onError: 'continueErrorOutput'` set but `main[1]` not wired.** Error path is enabled but goes nowhere. → [NODE_ERROR_OUTPUTS.md](../../n8n-error-handling-official/references/NODE_ERROR_OUTPUTS.md)

### Webhook API workflows (Webhook + Respond to Webhook)

- [ ] **Webhook performs a sensitive action with `parameters.authentication: 'none'`.** "Sensitive" = mutates state, sends external messages, hits production data, exposes private info, triggers paid actions. Anyone with the URL can fire it. Set `parameters.authentication` to `'basicAuth'` or `'headerAuth'` and use the matching credential. → [n8n-credentials-and-security-official](../../n8n-credentials-and-security-official/SKILL.md)

### Sub-workflow contracts

- [ ] **`Execute Workflow Trigger` set to `passthrough` when it shouldn't be.** Passthrough loses the typed-input contract that agent tools (`fromAi()`) and structured callers need. Only correct when (a) the sub-workflow specifically receives binary AND isn't an agent tool, or (b) the sub-workflow takes no inputs (Define Below requires at least one field). For (b), the body should open with a `Set` ("Keep Only Set", no fields) and the trigger should carry a sticky noting no inputs are expected. → [n8n-subworkflows-official non-negotiables](../../n8n-subworkflows-official/SKILL.md) and [SUBWORKFLOW_PATTERNS.md "Splitting by input shape"](../../n8n-subworkflows-official/references/SUBWORKFLOW_PATTERNS.md)

### Chat-triggered agents (Slack / Discord / Teams / Telegram)

- [ ] **Bot's own user ID not filtered out**, either via the trigger's own filter option (preferred: Slack's `options.userIds` exclusion list) or as the first node after the trigger. The bot's reply re-triggers the workflow → infinite loop. Watch out for surface-specific semantics: Telegram's `userIds` is an allowlist, not an exclusion list. → [CHAT_AGENT_PATTERNS.md](../../n8n-agents-official/references/CHAT_AGENT_PATTERNS.md)

---

## SHOULD FIX

### Naming

- [ ] **Generic node names** (`HTTP Request1`, `Set2`, `Postgres1`). Debugging-hostile: a failure on `node "HTTP Request3"` tells the operator nothing, but `node "Fetch order details"` localizes the break instantly. Rename every node to describe what it *does in this workflow*. → [NAMING_CONVENTIONS.md](NAMING_CONVENTIONS.md)

### Comms nodes (Slack, Gmail, Discord, SMTP, Telegram)

- [ ] **n8n attribution still appended** on Slack / Gmail / Email / Discord nodes. Most comms nodes have "Append n8n Attribution" enabled by default. Users typically want it removed in production. → [COMMS_NODES.md](../../n8n-node-configuration-official/references/COMMS_NODES.md)
- [ ] **Slack thread reply posting as top-level message.** `thread_ts` not set, or set in the wrong nested location. → [COMMS_NODES.md](../../n8n-node-configuration-official/references/COMMS_NODES.md)

### Set node antipattern

- [ ] **Set node feeding only 0 or 1 downstream consumer.** Most common antipattern in the pack. Delete + inline the expression at the consumer. → [n8n-expressions-official "The Set-node antipattern"](../../n8n-expressions-official/SKILL.md)
- [ ] **Set node before a Data Table Insert/Update mapping fields to schema.** Map directly in the Data Table node's per-column expression slots. → [n8n-data-tables-official strong defaults](../../n8n-data-tables-official/SKILL.md)
- [ ] **Set node building an email/Slack body.** Build the body inline in the comms node's body field with an expression. → [COMMS_NODES.md](../../n8n-node-configuration-official/references/COMMS_NODES.md)
- [ ] **Multiple consecutive Set nodes each defining one field.** Collapse, or eliminate. → [n8n-expressions-official](../../n8n-expressions-official/SKILL.md)

### Code node antipattern

- [ ] **Code node doing pure data shaping** (`.map`, `.filter`, `.find`, field rename, optional chaining). Use an expression or Edit Fields with arrow function. → [n8n-code-nodes-official decision tree](../../n8n-code-nodes-official/SKILL.md)
- [ ] **Code node using `crypto.createHash` / `crypto.createHmac`.** Use the native Crypto node (`n8n-nodes-base.crypto`). Recurring AI slip. → [n8n-code-nodes-official "Cryptographic operations"](../../n8n-code-nodes-official/SKILL.md)
- [ ] **Code node parsing XML / SOAP / RSS.** Use the native XML node + Edit Fields with arrow function for extraction. → [n8n-code-nodes-official "XML / SOAP / RSS parsing"](../../n8n-code-nodes-official/SKILL.md)
- [ ] **Code node + Set node combo** (Set builds inputs, Code transforms). One Edit Fields with arrow function does both. → [ARROW_FUNCTIONS_IN_EDIT_FIELDS.md](../../n8n-code-nodes-official/references/ARROW_FUNCTIONS_IN_EDIT_FIELDS.md)

### Expression discipline

- [ ] **`$json.x` references deep in workflows with branches/intermediates.** Switch to `$('Source Node').item.json.x` for refactor stability. → [n8n-expressions-official non-negotiable](../../n8n-expressions-official/SKILL.md)
- [ ] **DateTime nodes used for date math/formatting.** Use Luxon expressions (`DateTime.fromISO(...)`) inline. → [n8n-expressions-official strong defaults](../../n8n-expressions-official/SKILL.md)
- [ ] **`$env.X` referenced in any expression.** Doesn't work, throws at runtime. Replace with `$vars.X` (paid plans), a Data Table, or a credential for secrets. → [n8n-expressions-official anti-patterns](../../n8n-expressions-official/SKILL.md)
- [ ] **Aggregate node + per-item execution mismatch.** Expressions using `$input.all()` / `$('Node').all()` *without* combining with another node's `.item` should set `executeOnce: true` on the node. → [n8n-loops-official non-negotiable](../../n8n-loops-official/SKILL.md) and [n8n-expressions-official ".all().map() triggers an executeOnce question"](../../n8n-expressions-official/SKILL.md)

### Execution model

- [ ] **Workflow assumes fan-out branches execute in parallel.** They don't, n8n runs them sequentially top-to-bottom by Y-position. Real concurrency needs sub-workflow dispatch with `mode: 'each'` + `waitForSubWorkflow: false`. → [n8n-workflow-lifecycle-official "Execution model"](../SKILL.md)

### Loops

- [ ] **`Loop Over Items` added "to make it loop"** when default per-item iteration handles it. Default per-item iteration already waits for each item before the next, so a Loop Over Items added "to wait for all items" is unnecessary. → [n8n-loops-official "When NOT to reach for Loop Over Items"](../../n8n-loops-official/SKILL.md)
- [ ] **Custom pagination implementation** (Loop Over Items + `$pageCount`, hand-rolled `while` in a Code node, Set + IF cycle, etc.) instead of HTTP Request's built-in `Pagination` option. → [HTTP_PAGINATION.md](../../n8n-loops-official/references/HTTP_PAGINATION.md)
- [ ] **Reset-mode loop with no clear termination.** `reset: true` without an explicit stop condition + `$runIndex` ceiling = infinite loop, n8n eats memory until killed. → [LOOP_OVER_ITEMS.md "Reset mode"](../../n8n-loops-official/references/LOOP_OVER_ITEMS.md)
- [ ] **One `Loop Over Items` nested inside another in the same workflow.** Doesn't work; breaks at runtime. Move the inner loop into a sub-workflow called per outer iteration (`mode: 'each'`). → [LOOP_OVER_ITEMS.md "Nesting Loop Over Items"](../../n8n-loops-official/references/LOOP_OVER_ITEMS.md)

### Self-healing on transient failures

- [ ] **Network-calling nodes (HTTP, comms, DB, AI) without `retryOnFail` configured.** Transient 429s and upstream blips surface as 5xx, alerts fire on noise. → [n8n-error-handling-official "Self-healing on transient failures"](../../n8n-error-handling-official/SKILL.md)

### Switch nodes

- [ ] **Switch with no fallback output configured.** Unmatched items silently drop. Set `options.fallbackOutput: 'extra'` and `options.renameFallbackOutput: '<name>'`. → [SWITCH_FALLBACK.md](../../n8n-node-configuration-official/references/SWITCH_FALLBACK.md)
- [ ] **Switch outputs unnamed.** Set `renameOutput: true` + `outputKey: '<name>'` per rule for self-documenting branches. → [SWITCH_FALLBACK.md](../../n8n-node-configuration-official/references/SWITCH_FALLBACK.md)

### Sub-workflows

- [ ] **Duplicated logic across workflows** that would be a sub-workflow. → [n8n-subworkflows-official decision tree](../../n8n-subworkflows-official/SKILL.md)
- [ ] **Sub-workflow with no `description`.** Won't be found in future searches; nobody (or AI) knows what it does. → [n8n-subworkflows-official anti-patterns](../../n8n-subworkflows-official/SKILL.md)
- [ ] **Sub-workflow has hidden side effects.** The name and `description` describe pure logic (parse, validate, format, compute, transform), but the body contains write / send nodes (Data Table Insert/Update, Slack/Gmail/Discord send, HTTP POST, file write, audit log, etc.). Callers reasonably assume the sub-workflow is safe to retry; doing so creates duplicate writes or sends. Either declare the side effect (rename to e.g. `Audit:` or `<Domain>:`, document it in `description`, return a result the caller can branch on) or move the side effect out of this sub-workflow. → [n8n-subworkflows-official "Stateless vs stateful"](../../n8n-subworkflows-official/SKILL.md)
- [ ] **~30-node workflow with no extraction.** Extract logical sections into sub-workflows. → [n8n-subworkflows-official](../../n8n-subworkflows-official/SKILL.md)

### AI Agents and tools

- [ ] **`options.maxIterations` left at default 10 on a multi-tool agent.** Likely too low for modern agents with flexible tool sets; throws "Max iterations reached" workflow error. Raise to 30-50+. → [AI_NODES.md "Iteration cap"](../../n8n-node-configuration-official/references/AI_NODES.md)
- [ ] **Generic tool names (`doStuff`, `runQuery`).** Model can't tell which tool to pick, skips them or hallucinates parameters. Use verb-first specific names. → [TOOLS.md](../../n8n-agents-official/references/TOOLS.md)
- [ ] **Default, Empty, or one-line tool descriptions.** Model has no clue when to invoke. Tool descriptions are part of the prompt. → [TOOLS.md](../../n8n-agents-official/references/TOOLS.md)
- [ ] **`outputParserStructured` without `autoFix: true`.** One bad model output and the workflow fails. Set `autoFix: true` with a coding-capable fixer model. → [STRUCTURED_OUTPUT.md](../../n8n-agents-official/references/STRUCTURED_OUTPUT.md)
- [ ] **Tools with user-visible side effects (send, pay, refund) without human review.** Wrap with `slackHitlTool` / `discordHitlTool` / `telegramHitlTool` / `gmailHitlTool` / etc. → [HUMAN_REVIEW.md](../../n8n-agents-official/references/HUMAN_REVIEW.md)
- [ ] **Approval message via `fromAi()` instead of `$tool.parameters.<name>`.** Model paraphrases; you approve text not values. → [HUMAN_REVIEW.md](../../n8n-agents-official/references/HUMAN_REVIEW.md)
- [ ] **Hardcoded `sessionId: 'default'` or no sessionId** on memory. All conversations share one session or sessions won't be used properly. → [MEMORY.md](../../n8n-agents-official/references/MEMORY.md)
- [ ] **Image / audio / video generation wrapped in an Agent.** Binary doesn't flow through tools or the Agent's output formatter. Use the provider's native single-call node directly. → [n8n-agents-official anti-patterns](../../n8n-agents-official/SKILL.md)
- [ ] **Agent + Switch to route on natural-language input** when Text Classifier (`@n8n/n8n-nodes-langchain.textClassifier`) is one node with N built-in branches. → [n8n-agents-official](../../n8n-agents-official/SKILL.md)
- [ ] **Agent (or Basic LLM Chain + structured output parser) used to pull fields out of a blob of text** when Information Extractor (`@n8n/n8n-nodes-langchain.informationExtractor`) is one node with a typed schema, no tools, no system prompt. Use the Agent only when the extraction needs tool calls or multi-turn reasoning. → [n8n-agents-official](../../n8n-agents-official/SKILL.md)

### System prompts (AI Agents)

The system prompt is the load-bearing config of an agent. Severity ranges by how badly the issue degrades behavior.

- [ ] **Hardcoded date / missing date in the system prompt.** Stale immediately. Agents making time-sensitive decisions (deadlines, eligibility windows, "is X expired?") get wrong answers. Use `Current date: {{ $now }}`. → [SYSTEM_PROMPT.md "Always include the current date"](../../n8n-agents-official/references/SYSTEM_PROMPT.md)
- [ ] **Long system prompt with per-tool usage instructions buried inside.** Modular split violation. Brittle to edit, and tools become unreusable across agents. Move tool-specific instructions into each tool's description. → [SYSTEM_PROMPT.md "The modular split"](../../n8n-agents-official/references/SYSTEM_PROMPT.md) and [n8n-agents-official "What goes in the system prompt vs the tool description"](../../n8n-agents-official/SKILL.md)
- [ ] **"You are a helpful assistant" preamble with no role specifics.** Generic responses, agent has no identity. Replace with a specific role and scope. → [SYSTEM_PROMPT.md "What it's for"](../../n8n-agents-official/references/SYSTEM_PROMPT.md)
- [ ] **No refusal/safety boundary** when one is needed (the agent has tools that touch user-visible state, sends, payments). Define explicit boundaries: "only answer questions about X, redirect otherwise". → [SYSTEM_PROMPT.md](../../n8n-agents-official/references/SYSTEM_PROMPT.md)

### Data Tables

**System columns and identifiers**

- [ ] **Set node before Data Table Insert/Update.** Map directly in per-column slots. → [n8n-data-tables-official strong defaults](../../n8n-data-tables-official/SKILL.md)
- [ ] **`id`, `createdAt`, or `updatedAt` declared in `create_data_table`.** System-managed; declaring them errors or shadows. → [n8n-data-tables-official non-negotiable](../../n8n-data-tables-official/SKILL.md)
- [ ] **Auto-`id` used as a cross-system identifier.** Resets on table recreate / instance migration. Add a domain ID column (`arxivId`, `customerId`, `requestId`). → [SCHEMA_DESIGN.md "system-managed columns"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)

**`_object` postfix discipline (the most error-prone area)**

- [ ] **Column holds stringified JSON (array, object) without the `_object` postfix.** Readers have no contract telling them to parse. → [SCHEMA_DESIGN.md "the `_object` convention"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Column has `_object` postfix but is `string` type holding native (non-stringified) values.** Contract violation: postfix promises stringified content. → [SCHEMA_DESIGN.md](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Insert/Update writes to an `_object` column without `JSON.stringify(...)`.** A `[object Object]` literal lands in the row. → [SCHEMA_DESIGN.md](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Read from an `_object` column without `JSON.parse(...)`.** Downstream gets a string where it expects array/object; templates and tools choke. → [SCHEMA_DESIGN.md](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Sub-workflow returns `_object` columns as strings to callers.** Storage format leaking through the interface. Parse before returning so callers receive arrays as arrays and objects as objects. → [SCHEMA_DESIGN.md "Storage format ≠ interface format"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Sub-workflow's "fresh" path stringifies to "match" the cached path.** Wrong instinct. Parse the cached path so both branches return natural shapes. → [SCHEMA_DESIGN.md](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **`_object` column holds data that needs to be queried** (filter on `topics` content, find rows by tag). Strings can't be queried structurally. Refactor to a relational child table or move to a real DB. → [SCHEMA_DESIGN.md "When NOT to use `_object`"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)

**Schema design**

- [ ] **String column acting as boolean** (`'yes'/'no'`, `'true'/'false'`). Use the `boolean` type. → [SCHEMA_DESIGN.md "Picking column types"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Mixed casing within one table or query** (`createdAt` AND `arxiv_id` together). Match camelCase to the system columns. → [n8n-data-tables-official strong defaults](../../n8n-data-tables-official/SKILL.md)
- [ ] **Table named with snake_case, lowercase, or in singular for a set.** Title Case with spaces (`Papers`, `Recent Events`). Plural for sets, singular for one-row-per-global-thing only. → [SCHEMA_DESIGN.md "Naming"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Boolean column not named affirmatively** (`completed` instead of `isCompleted`). Affirmative names read better in filters and IFs. → [SCHEMA_DESIGN.md](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Table with more than ~17 columns.** Consider splitting; the table is probably trying to be multiple things. → [SCHEMA_DESIGN.md "A healthy table"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **User-declared `date` column duplicates `createdAt` / `updatedAt`.** Use the system columns where they fit; only add explicit `date` columns when the timestamp's meaning differs from "row created" or "row updated". → [SCHEMA_DESIGN.md](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)

**Relational design (when the data has shape)**

- [ ] **Genuine parent-child data crammed into one wide table** (papers + summaries in one `Papers` table, customers + orders in one `Customers` table). Split into parent + child tables, reference parent by `id` (`paperId`, `customerId`). → [SCHEMA_DESIGN.md "Designing relationally"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md) and [n8n-data-tables-official "Relational design"](../../n8n-data-tables-official/SKILL.md)
- [ ] **Child arrays stored in `_object` columns when they need to be queried or filtered individually.** Refactor to a relational child table. → [SCHEMA_DESIGN.md "When NOT to use `_object`"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Cascade strategy unclear** (no defined behavior on parent delete). Pick one per relationship: cascade-delete via a separate Delete on children, soft-delete (`archived` flag), or orphan. Mixed strategies cause silent bugs. → [SCHEMA_DESIGN.md "Enforce integrity in the workflow"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Multi-table write sequence (parent Insert + child Insert) without partial-failure handling.** No transactions exist; a child failure leaves the parent orphaned. Pick: compensating writes, idempotent retry with `upsert` + stable domain IDs, or soft state marker (`status: 'pending' → 'complete'`). → [SCHEMA_DESIGN.md "No transactions, plan for partial failure"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Child rows pointing at deleted parents** (orphan detection missing). Either soft-delete by default, or run a periodic cleanup workflow. → [SCHEMA_DESIGN.md "Watch for child without parent"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **3+ joined tables with transactional writes.** Past Data Tables' wheelhouse. Use a real SQL DB. → [SCHEMA_DESIGN.md "When Data Tables are the wrong tool"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)

**Operation gotchas**

- [ ] **Multi-column filter without explicit `matchType: 'allConditions'`.** Defaults to `anyCondition` (OR) in some versions; surprising when intent is AND. → [OPERATIONS.md "matchType"](../../n8n-data-tables-official/references/OPERATIONS.md)
- [ ] **`Get` without `alwaysOutputData: true` followed by an IF** that branches on result presence. No-match produces zero items, the IF doesn't fire at all. → [DEDUP_PATTERNS.md "Pattern 3: Get + IF"](../../n8n-data-tables-official/references/DEDUP_PATTERNS.md)
- [ ] **Get + IF branches produce different JSON shapes** (cached path vs. freshly-processed path). Downstream `$json.x` resolves to the wrong field depending on which fired. Insert a Set/NoOp anchor to normalize. → [n8n-expressions-official "Combine Inputs convergence"](../../n8n-expressions-official/SKILL.md)
- [ ] **`Update` with no match silently does nothing.** No error. Either follow with a `Get` to confirm, or use `upsert` for create-or-update. → [OPERATIONS.md "Update with no match"](../../n8n-data-tables-official/references/OPERATIONS.md)
- [ ] **`Insert` with no dedup in a workflow that can re-fire** (webhook retry, scheduled re-run). Creates duplicates. Use `upsert`, `rowNotExists` + Insert, or upstream dedup. → [DEDUP_PATTERNS.md](../../n8n-data-tables-official/references/DEDUP_PATTERNS.md)
- [ ] **`returnAll: false` without explicit `limit`.** Defaults to 50 in many versions; downstream may expect more and silently truncate. → [OPERATIONS.md "returnAll"](../../n8n-data-tables-official/references/OPERATIONS.md)
- [ ] **Plain "have I seen this value?" dedup using a Data Table.** The `Remove Duplicates` node ("items seen in previous executions" mode) handles this with no schema. Reach for Data Tables only when the dedup state needs to be queryable, has row-level logic, or has TTL/per-tenant scoping. → [DEDUP_PATTERNS.md](../../n8n-data-tables-official/references/DEDUP_PATTERNS.md)
- [ ] **Idempotency-key workflow without TTL cleanup.** Markers shouldn't live forever; run a daily cleanup. → [DEDUP_PATTERNS.md "Idempotency keys"](../../n8n-data-tables-official/references/DEDUP_PATTERNS.md)

**Mapping mode and evolution**

- [ ] **`autoMapInputData` mode without a stable 1:1 between upstream field names and column names.** Drift on either side silently breaks the mapping. Default to `defineBelow`. → [SCHEMA_DESIGN.md "Mapping mode"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Workflow attempts an in-place column type change.** Not supported. Add a new column, copy via workflow, drop the old, rename the new. → [SCHEMA_DESIGN.md "Schema evolution"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)

**Wrong tool for the job**

- [ ] **Cross-app shared data in Data Tables.** Awkward to query from outside n8n. Use a real DB. → [SCHEMA_DESIGN.md "When Data Tables are the wrong tool"](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)
- [ ] **Millions of rows or write-heavy volume in a Data Table.** Performance degrades; use a real DB. → [SCHEMA_DESIGN.md](../../n8n-data-tables-official/references/SCHEMA_DESIGN.md)

### Binary handling

- [ ] **Reading file content from `$json` instead of `$binary`.** → [BINARY_BASICS.md](../../n8n-binary-and-data-official/references/BINARY_BASICS.md)
- [ ] **Agent tool returning raw binary directly.** Tool output is JSON-only. Upload to storage, return key/URL in JSON. → [AGENT_TOOL_BINARY.md](../../n8n-binary-and-data-official/references/AGENT_TOOL_BINARY.md)
- [ ] **Uploaded chat files passed to a tool via `fromAi`.** `fromAi` doesn't carry binary. Pre-stage to storage, inject keys in the system prompt. → [AGENT_TOOL_BINARY.md](../../n8n-binary-and-data-official/references/AGENT_TOOL_BINARY.md)
- [ ] **Binary lost after a JSON transform.** Use Merge to combine the JSON output with the binary stream. → [MERGE_FOR_CONTEXT.md](../../n8n-binary-and-data-official/references/MERGE_FOR_CONTEXT.md)
- [ ] **Image sent to a chat surface from raw `$binary`.** Chat surfaces need a URL-referenced image (or platform-native file upload). → [CDN_REQUIREMENT.md](../../n8n-binary-and-data-official/references/CDN_REQUIREMENT.md)

### Public trigger auth

- [ ] **Webhook trigger with `parameters.authentication: 'none'`** even on read-only / lookup paths. The URL is publicly callable; no auth invites abuse (rate-limit exhaustion, scanning, scraping). Use Basic / Header / JWT auth unless the workflow is genuinely meant to be public. (If the action is sensitive, this is a MUST FIX, see above.) → [n8n-credentials-and-security-official](../../n8n-credentials-and-security-official/SKILL.md)
- [ ] **Form Trigger fronting a sensitive action with no auth gate.** Forms that create accounts, mutate data, send external messages, or trigger paid operations should require real auth at the trigger. An obscure URL is not auth. → [n8n-credentials-and-security-official](../../n8n-credentials-and-security-official/SKILL.md)

### Webhook / Respond to Webhook

- [ ] **Fallible nodes with no error path.** HTTP / DB / API / file nodes need `output(1)` wired to a 5xx Respond. Without it, the failure is unhandled: the workflow halts and the caller gets whatever n8n's generic error response is (no controlled status code, no useful body), and the operator only learns about it if a workflow-level error workflow is configured separately. → [n8n-error-handling-official non-negotiables](../../n8n-error-handling-official/SKILL.md) and [API_WORKFLOWS.md](../../n8n-error-handling-official/references/API_WORKFLOWS.md)
- [ ] **Error response returns 200.** Caller's HTTP client treats it as success; downstream error handling never fires. Always 4xx (caller error) or 5xx (server error). → [RESPONSE_SHAPES.md](../../n8n-error-handling-official/references/RESPONSE_SHAPES.md)
- [ ] **Generic 500 for every failure.** Validation errors should be 400, auth issues 401/403, conflicts 409, rate limits 429. Caller can't distinguish their bug from your outage. → [RESPONSE_SHAPES.md](../../n8n-error-handling-official/references/RESPONSE_SHAPES.md)
- [ ] **`respondWith: 'json'` body using `JSON.stringify(...)`** instead of an object literal (produces double-encoded body). → [WEBHOOK_NODES.md](../../n8n-node-configuration-official/references/WEBHOOK_NODES.md)

### HTTP Request

- [ ] **Headers set both via `headerParameters` and a credential's `httpHeaderAuth`.** They conflict. → [HTTP_NODES.md](../../n8n-node-configuration-official/references/HTTP_NODES.md)
- [ ] **Untrusted external API call without `options.timeout` set.** Runtime default is 5 minutes; a hung request stalls the workflow. → [HTTP_NODES.md](../../n8n-node-configuration-official/references/HTTP_NODES.md)

### Schedule trigger

- [ ] **Business-critical schedule with no explicit timezone** at the workflow level. DST and instance moves cause timing shifts. → [TRIGGER_NODES.md](../../n8n-node-configuration-official/references/TRIGGER_NODES.md)
- [ ] **Schedule-triggered workflow not idempotent** for missed-run scenarios. Restarts or downtime can miss runs. → [TRIGGER_NODES.md](../../n8n-node-configuration-official/references/TRIGGER_NODES.md)

---

## NICE TO HAVE

### Naming

- [ ] **Workflow name doesn't follow verb-first pattern** (`Send weekly customer report` vs. `Customer report sender`). → [NAMING_CONVENTIONS.md](NAMING_CONVENTIONS.md)
- [ ] **Untagged sub-workflow** (missing `subworkflow`, a domain tag, or `tool`). Tags are the discovery mechanism; an untagged sub-workflow won't surface under any `tags` filter. → [NAMING_AND_DISCOVERY.md](../../n8n-subworkflows-official/references/NAMING_AND_DISCOVERY.md)

### Readability

- [ ] **Workflow over ~10 nodes (n8n 2.28+) whose logical steps aren't grouped into node groups.** Grouping is the node group's job; collapsed groups make the canvas read as steps, not nodes. Skip on older instances, where node groups don't exist. → [SKILL.md "Readability"](../SKILL.md)
- [ ] **Sticky note used to fake a group instead of `setNodeGroups`.** Stickies annotate (callouts, TODOs, warnings); they don't group. → [SKILL.md "Readability"](../SKILL.md)
- [ ] **Sticky title re-states what's visible** (`Set, If, Set`). Title with the callout's point. → [SKILL.md "Readability"](../SKILL.md)
- [ ] **Sticky colors used inconsistently.** One color per category (processing / errors / TODOs); otherwise color is noise. → [SKILL.md "Readability"](../SKILL.md)
- [ ] **Workflow `description` is empty, one sentence, or doesn't capture the *why*.** Two sentences: what it does, why it exists. → [SKILL.md "Readability"](../SKILL.md)
- [ ] **Code node without a one-line note** explaining its purpose. → [SKILL.md "Readability"](../SKILL.md)
- [ ] **Workflow ignores existing house style** (sticky palette, naming convention used in nearby workflows). Match what's there. → [SKILL.md "Readability"](../SKILL.md)

### Sub-workflow conventions

- [ ] **Sub-workflow without a final `Return` Set / Edit Fields node** shaping the return contract. The legitimate exception to the Set-node antipattern. → [n8n-subworkflows-official "Other conventions"](../../n8n-subworkflows-official/SKILL.md)
- [ ] **Inputs / outputs not documented in the sub-workflow's `description`.** Field names, types, purpose. → [n8n-subworkflows-official "Sub-workflow inputs and outputs"](../../n8n-subworkflows-official/SKILL.md)

### Conventions

- [ ] **Per-execution context (user identity, files, current task) buried in a static system prompt** instead of injected via expressions or piecing. Hard to update. → [SYSTEM_PROMPT.md "Storing the prompt"](../../n8n-agents-official/references/SYSTEM_PROMPT.md)
- [ ] **Generic safety boilerplate language** in the system prompt for risks the model already handles. Reinforcement adds tokens without changing behavior. Reserve safety language for specific, named risks. → [SYSTEM_PROMPT.md anti-patterns](../../n8n-agents-official/references/SYSTEM_PROMPT.md)

---

## Reporting findings

When reporting, group by severity, then within severity by domain. For each finding include:

- The specific node(s) or section affected.
- A one-sentence description of the issue.
- The link to the canonical skill ref for the fix.

```
MUST FIX
  Security
  - Node `Send Webhook`: bearer token in headerParameters value field. → n8n-credentials-and-security-official
  - Node `Lookup user`: SQL string concat with $json.email. → DATABASE_NODES.md

  Connections
  - Node `Validate input`: `connections.Validate input.main[0]` has only 1 entry, but the workflow's logic expects fan-out to 3 downstreams. → check the SDK code (likely a missed `.add(...)` call)

SHOULD FIX
  ...
```

A review agent should not auto-fix MUST FIX items without user confirmation: security and connection fixes have blast radius and the user should know what's changing.


## Referência: references/source/references/TESTING.md

# Testing workflows

Two tools, used together. `prepare_workflow_pin_data` returns JSON Schemas (no actual data) for every node that needs pinning. You generate sample values matching the schemas and pass them to `test_workflow` as the `pinData` parameter. Inspect results via `get_workflow_execution`.

## What `test_workflow` actually pins

Three categories are pinned (return your supplied data instead of executing): **trigger nodes**, **nodes with credentials**, and **HTTP Request nodes**. Everything else runs.

| Node category | Behavior under `test_workflow` |
|---|---|
| Trigger node | Pinned, never fires |
| HTTP Request | Pinned, does NOT hit the URL |
| Slack / Gmail / Discord / SMTP / Telegram | Pinned (credentialed), does NOT send |
| Postgres / MySQL / Mongo / Supabase | Pinned (credentialed), does NOT read or write |
| LLM nodes (OpenAI, Anthropic, etc.) | Pinned (credentialed), no API call, no cost |
| Data Tables (built-in n8n storage) | Real reads AND writes (no credential, not pinned) |
| Code node | Executes as written |
| Edit Fields / Set / If / Switch / Merge / Filter | Execute normally |
| Wait node | Actually waits |
| Execute Workflow (sub-workflow call) | Runs the sub end-to-end, and the sub's pinning rules don't apply |

The auto-pin covers most of the obvious side-effect surface (sends, third-party writes, paid API calls). It does NOT cover:

- **Data Tables**, since they're n8n's built-in storage and have no credential. Insert / Update writes for real.
- **Execute Workflow** calling a sub. Test mode does not propagate into sub-workflows. The sub runs normally with all its credentialed nodes firing for real (it's its own execution).
- **Execute Command** and **File Read/Write** nodes, which are credential-free I/O.
- **Code nodes that touch external state** (filesystem, child processes, network via Node APIs on self-hosted Code nodes).

## Non-negotiable

**Ask the user before `test_workflow` if any of the not-auto-pinned categories would fire downstream.** A short message before the call:

> "This workflow writes to the `customers` Data Table and calls sub-workflow `process-payment` (which charges Stripe). Both will fire for real. Want me to run the test?"

Many users will say yes (sandbox table, test sub, trust the inputs). Some will pin or disable specific nodes first. The conversation costs nothing, but running an irreversible operation against the wrong account costs everything.

Skip the ask when EVERY non-pinned downstream is read-only or stateless: Get / Search / Lookup, pure compute (Set / If / Code shaping data), MCP-extension tools that only read.

If you're unsure whether a node has side effects, ask. False-positive asks waste a turn, but false-negative side effects waste real resources.

## Generating pin data

`prepare_workflow_pin_data` returns JSON Schemas describing the expected shape for each node that needs pinning. **It does not return actual data, you generate it.** Merge sample values into a single `pinData` object keyed by node name, with every item wrapped in `{ "json": { ... } }`:

```js
{
  "Webhook": [{ "json": { "headers": {...}, "body": {...} } }],
  "Postgres1": [{ "json": { "id": "123", "email": "a@b.com" } }],
  "OpenAI Chat": [{ "json": { "message": { "content": "..." } } }]
}
```

Pin every key the generator returns. Skipping a credentialed node leaves it without input data, and the test won't represent real behavior. For keys where the generator can't infer a schema (no past executions, no node-type hint), use an empty default or hand-build based on what the next node expects.

## Mocking trigger input by type

`prepare_workflow_pin_data` generates a representative trigger input. Hand-build when the generator's defaults don't match real callers.

| Trigger | Pin shape |
|---|---|
| Webhook | `{ headers, params, query, body, webhookUrl }` |
| Schedule | Empty or timestamp-shaped. Default usually fine. |
| Manual | Arbitrary, whatever the first downstream expects. |
| Chat (`chatTrigger`) | `{ chatInput, sessionId, files }`. Pin `files: []` unless testing file handling. |
| Execute Workflow Trigger | The typed inputs declared on the trigger node. |
| Polling | One item shaped like what polling normally yields. Polling logic is bypassed. |

For per-trigger config details, see `n8n-node-configuration-official` `references/TRIGGER_NODES.md`.

## Strategies when a non-pinned downstream isn't safe

In order of preference:

1. **Ask the user first** (the protocol above). Many concerns dissolve once the user explicitly OKs the test or names which nodes worry them.
2. **Pin individual node outputs.** Add the node to your `pinData` object even though it's not auto-pinned. The pinned response is returned and the node body never runs. Works on any node.
3. **Disable specific nodes** (`disabled: true`) for the test run. `test_workflow` skips disabled nodes. Useful when nothing meaningful would be pinned and you just want to skip the side effect.
4. **Sandbox credentials.** A separate credential pointing at staging (Stripe test mode, sandbox Slack workspace, dev DB). The user owns creating these, suggest, don't implement without permission.

Pinning and disabling are revertable. Sandbox credentials are infrastructure and persist.

## Inspection after testing

`test_workflow` returns an execution ID. `get_workflow_execution({ executionId, workflowId, includeData: true })` exposes per-node input/output. Walk through:

- Per-node output shape matches intent.
- Errors caught by error branches fired correctly, not silently.
- Webhook response shape (status, body, headers) matches the contract.

The full pre-publish checklist that includes testing is in `VALIDATION_CHECKLIST.md` §5.

<!-- TEMPORARY: n8n's execution viewer shows no visual indication that a node's output was pinned via test_workflow. May be fixed in a future n8n version. When fixed, this section can be removed. -->

## After test_workflow: announce what was pinned

Pin data passed to `test_workflow` is **per-execution only**. It is not written to the workflow definition, and the n8n execution viewer currently shows no visual indicator (no pin icon, no badge) on the nodes that were pinned. The only programmatic signals are:

- The `pinData` block in `get_workflow_execution`'s response, which lists the pinned node names.
- `executionTime: 0` on each pinned node.

Because the user has no canvas confirmation that a destructive-looking node was actually mocked, **always tell the user which nodes were pinned after the call.** Especially for nodes whose live execution would be destructive (Postgres `DELETE`, payment capture, file write, email send). A one-liner is enough:

> "Test ran. Pinned (did NOT execute): `Webhook`, `Delete inactive customers`. Ran for real: `Format report`, `Send summary`."

Without this, the user has to either trust the protocol or open the execution payload to verify. The reassurance costs one sentence, but the cost of the user assuming a destructive node fired (or of assuming it was pinned when it wasn't) is much higher.

## `test_workflow` vs `execute_workflow`

| Tool | Trigger | Credentialed / HTTP nodes | Other downstreams |
|---|---|---|---|
| `test_workflow` | Pinned via your data | Pinned via your data | Run for real |
| `execute_workflow` | Real (kicked off ad-hoc) | Run for real | Run for real |

`execute_workflow` is **not** a safer `test_workflow`. It's the opposite. `test_workflow` covers the credentialed surface automatically, but `execute_workflow` runs everything end-to-end with real auth and cost. "Run this once for me" means `execute_workflow`. "Test this" means `test_workflow` (and ask about the not-auto-pinned downstreams first).

Both want the same ask-before-running discipline when user-visible side effects are at stake.

## Re-test after iteration

After fixing something, re-run `test_workflow` on the SAME pin data before claiming the fix works. Same pin, same expected output, every iteration.

If a test passes but production fails, check whether the pin data covers the failing case. Usually it doesn't, and the pin needs updating to match the real-world shape that broke things.


## Referência: references/source/references/VALIDATION_CHECKLIST.md

# Pre-publish validation checklist

Run before every `publish_workflow`. The whole list. Skipping items is how broken workflows ship.

## The checklist

### 1. `validate_workflow` passed

Run `validate_workflow`. Schema and shape errors must be zero. If validation fails, fix and re-validate.

If a failure points at a single node's params, `validate_node_config` on that node alone returns per-parameter errors without full-graph noise. For tool subnodes, set `isToolNode: true`. Best used as a per-node spot-check during BUILD.

### 2. Antipattern scan (the build-time discipline check)

Walk the workflow with these questions in mind. These are patterns that recur across builds even when relevant skills are loaded, so making this explicit catches them.

**Set nodes:**
- For each Set node, count how many downstream nodes reference its output fields.
- If only 0 or 1 downstream consumer references each field, **delete the Set node and inline the expression at the consumer**. The most common antipattern (`n8n-expressions-official` non-negotiable #2).
- Common offender: a Set node right before a Data Table Insert / Update node, mapping fields to match schema. Map directly in the Insert/Update node's expression slots.
- Common offender: a Set node building a body before an Email/Slack node. Build the body in the body field with an expression.

**Code nodes:**
- For each Code node, ask: could this be an expression or arrow-function-in-Edit-Fields?
- If it's pure data shaping (`.map`, `.filter`, `.find`, field renaming, optional chaining), rewrite as expression or Edit Fields with arrow function. Code's bar is multi-source aggregation, external libraries, or stateful transforms (`n8n-code-nodes-official`).
- **For each operation the Code does, check separately for a native node.** A Code node doing 4 things probably has 4 native answers. Read its body and ask:
  - `this.helpers.httpRequest(...)` → use the **HTTP Request node**.
  - Manual pagination loop (`while (more) { start += page; ... }`) → use HTTP Request's **Pagination** option.
  - Regex parsing structured response (`/<id>...<\/id>/g`, etc.) → use the **XML node** for XML, `JSON.parse` for JSON.
  - `crypto.createHash(...)` or `crypto.createHmac(...)` → use the **Crypto node**.
  - Status-code retry logic (`if (status === 429) throw`) → HTTP Request's `retryOnFail` (retries on any error, no per-status filter, capped at 5 tries / 5000ms wait). For 429-only or 5xx-only retry, use the error output + IF on `$json.error.httpCode` instead.
- **Identity Code nodes** (`return $('Some Node').all();` or `return $input.all();`) are always wrong. They re-emit upstream data, which means the workflow shape is wrong: the downstream consumer should branch off the upstream directly, or the per-item-vs-aggregate context mismatch should be solved with fan-out, not a Code-node bridge.
- Common offender: flattening a single API response's nested structure. That's Edit Fields with arrow function, not Code.

**Merge nodes:**
- Count wires going in. Confirm `numberOfInputs` matches.
- For Merges using `useDataOfInput`, walk through the off-by-one rule (`n8n-node-configuration-official` `references/MERGE_NODE.md`).

**Fan-out branches:**
- If the design assumes branches run in parallel, it's wrong. n8n runs them sequentially top-to-bottom by Y-position. For real concurrency, dispatch via `Execute Workflow` with `mode: 'each'` + `waitForSubWorkflow: false`.

**DateTime nodes:**
- Replace with a Luxon expression (see `n8n-expressions-official`). DateTime nodes are almost always wrong.

**Sub-workflow triggers:**
- For each `Execute Workflow Trigger`, confirm **"Define Below"** mode with typed fields. Passthrough is only correct for (a) binary-receiving sub-workflows that won't be agent tools or (b) sub-workflows that genuinely take no inputs (Define Below requires at least one field). For (b), verify the body opens with a `Set` ("Keep Only Set", no fields) and a sticky noting no inputs are expected. See `n8n-subworkflows-official` non-negotiable #2.

**Data references:**
- Search for `$json.` in expressions. Replace with `$('Node Name').item.json.` unless the node is directly downstream of a single source with no intermediates (`n8n-expressions-official` non-negotiable #1).
- Search for `$env.` in expressions. Doesn't work, throws at runtime. Replace with `$vars.X` (paid plans), a Data Table, or a credential if it's a secret.

Skipping it is how build-time slips slip past validation.

### 3. Error handling is wired

For workflows that are webhook-triggered, production-bound, or otherwise user-facing, every fallible node should have its error path handled. This isn't about catching bugs. It's about returning a clean response when an upstream is down.

Invoke `n8n-error-handling-official` if any of these are true:

- Webhook trigger with a respond-to-webhook pair.
- Unattended (scheduled, cron, queue-driven).
- A failure would silently drop user-visible work.

For internal one-off scripts (manual trigger), error handling can be looser.

### 4. Credentials, not tokens in text fields

Walk every node config for tokens, API keys, or auth values pasted into text parameters. They should be referenced via the credential system.

If you find any, invoke `n8n-credentials-and-security-official` and migrate before publishing.

### 5. `test_workflow` produced expected output

Use `prepare_workflow_pin_data`, then `test_workflow`. Inspect outputs via `get_workflow_execution`.

**Before running:** `test_workflow` auto-pins triggers, credentialed nodes, and HTTP Request. Code, Edit Fields, If, Data Tables, Execute Command, file ops, and sub-workflow calls run for real. If any of those have user-visible side effects, ask the user before running. See `TESTING.md` for the side-effect protocol, mocking by trigger type, pinning individual nodes, and the post-run announce-what-was-pinned protocol.

Check:

- Output shape matches what consumers expect.
- No unexpected errors swallowed by error branches.
- Fan-outs all produced data, none collapsed to empty.
- For webhook responses, the shape is correct (status, body, headers).

Fix and re-test if anything's off.

### 6. Naming, descriptions, structure

Quick pass:

- Workflow name follows the verb-first pattern (`NAMING_CONVENTIONS.md`). Sub-workflows are tagged (`subworkflow`, a domain tag, `tool`) since that's how `search_workflows({ tags })` finds them.
- `description` is set and captures both *what* and *why*, with searchable keywords.
- Nodes are renamed from defaults.
- Workflows past ~10 nodes group their logical steps into node groups (`setNodeGroups`). Ungrouped still runs, but a large ungrouped canvas is hard to read and maintain, so take it seriously. See `SKILL.md` "Readability".

These don't block publish technically, but workflows without them rot faster.

### 7. Folder placement

If the user requested a specific folder, confirm via `search_folders` that the workflow ended up there. If the folder didn't exist, you should have surfaced that before building (`FOLDER_LIMITATIONS.md`). Don't silently dump at root.

### 8. MCP access (if applicable)

Workflows created via `create_workflow_from_code` default to MCP-accessible. No toggle step needed. Only ask the user to flip the toggle when:

- They built the workflow in the n8n UI and you need to operate on it.
- They want to *revoke* MCP access on an agent-created workflow (the toggle is on by default).

See `MCP_ACCESS_PER_WORKFLOW.md`.

## Order matters

Top-to-bottom. Items 1-4 are gates: failing any means the workflow shouldn't publish. Items 5-8 are quality checks: failing means the workflow ships and rots, but won't break immediately.

The most common skip is item 2 (the antipattern scan). It feels like polish, but it catches things `validate_workflow` doesn't.

## What to do if something fails after publish

> **Post-publish is high-stakes: run every operation through the user.** Once a workflow is published, it may be receiving real traffic, holding state, or being depended on by other systems. **Do not** take autonomous action: no `publish_workflow`, no `unpublish_workflow`, no `update_workflow`, no `archive_workflow`, no triggering executions to "see what happens." Surface the problem, propose the fix, and wait for explicit approval before each step. The guidance below is what to *recommend* to the user, not what to do without asking.

n8n keeps versions: `get_workflow_details` returns both `versionId` (the current draft) and `activeVersionId` (the version that's live). They diverge when you save changes via `update_workflow`. Those changes only go live on the next `publish_workflow` call. **Saving is not publishing.**

1. **Consider rolling back first.** `get_workflow_history` lists saved versions (newest first); `get_workflow_version` fetches a known-good one, and `restore_workflow_version` re-applies it as the draft (or pass its `versionId` to `publish_workflow` to go straight live). (n8n 2.29.0+.) Rollback no longer needs the user to copy a `versionId` from the UI, but per the guardrail above, recommend it and let the user approve before you restore.
2. **Recommend `unpublish_workflow` only if no rollback target exists** and the workflow is actively running and broken. A scheduled or webhook workflow with broken connections shouldn't keep firing. Surface the problem and the recommendation, let the user pull the trigger.
3. **Fix-forward path: `update_workflow` saves the draft, then `publish_workflow` makes it live.** Two separate steps: `update_workflow` does NOT auto-publish, the change sits as an unpublished draft until `publish_workflow` runs against it. Re-run this checklist before the publish step. Don't trust that "just one fix" doesn't ripple.

## A note on speed

The cost of skipping is higher than the cost of checking. Debugging a broken production workflow is much more time consuming, stressful, and can cause damage.
