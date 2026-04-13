# Vault File Templates

Use these templates when creating new vault files to ensure proper structure and wikilinks.

## Files

- `decision.md` — Strategic decisions (use when choosing between options)
- `bug.md` — Fixed bugs (use after resolving a production issue)
- `pattern.md` — Reusable technical patterns (use when discovering a solution)
- `session.md` — Work sessions (use at end of day or milestone)
- `assumption.md` — Hypotheses about market/product (use when making a claim without proof)

## Workflow

1. Copy appropriate template to destination (e.g., `founder/decisions/YYYY-MM-DD-title.md`)
2. Fill in all fields
3. Ensure `## Related` section has backlinks:
   - Parent MOC (e.g., `[[_system/MOC-decisions]]`)
   - Project MOC (e.g., `[[brantham/_MOC]]`)
   - Cross-links to related files
4. Run audit before saving:
   ```bash
   python3 _system/vault-linker.py
   ```
5. Verify no broken wikilinks in Obsidian Graph View

## Auto-Linking

After creating a file, run:
```bash
python3 _system/vault-linker.py fix
```

This will auto-add `## Related` sections to any file missing them.

