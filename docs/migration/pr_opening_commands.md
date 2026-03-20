# PR Opening Commands

Run from the repository root:

```bash
git checkout chore/repo-fusion-plan
git status
git push -u origin chore/repo-fusion-plan
```

If using GitHub CLI:

```bash
gh pr create \
  --base main \
  --head chore/repo-fusion-plan \
  --title "docs: add first-phase fusion layer from industrial-copilot-template" \
  --body-file docs/migration/pr_draft_fusion_phase1.md
```

Optional review helpers:

```bash
git log --oneline main..chore/repo-fusion-plan
git diff --stat main..chore/repo-fusion-plan
```
