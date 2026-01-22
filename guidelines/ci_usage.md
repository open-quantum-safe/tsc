# CI Usage Guidelines
The OQS project aims to reduce redundant CI runs while maintaining good test quality, promoting efficient use of computational resources, minimizing environmental impact, and ensuring developers receive timely feedback from CI results.

## Contributor Guidelines

To help achieve this goal, contributors are asked to follow these practices:

- Use `[skip ci]` in commit messages for changes that do not affect program logic and do not require testing (e.g., documentation updates, formatting).
  - Example: `git commit -s -m "chore: correcting a typo in the documentation [skip ci]"`
- Prefer manual workflow triggers via GitHub Actions when selective testing is sufficient.
  - Workflows that have a "workflow_dispatch" trigger can be triggered manually. To trigger them, go to "Actions", select the workflow in the list on the left, then click on "Run workflow" and select the branch or the commit to be tested.
<img width="864" height="508" alt="Image" src="https://github.com/user-attachments/assets/c723823a-b948-4dbf-a7ec-55860a314718" />
- Cancel superseded workflows manually if a newer commit renders the current CI run obsolete.
  - To cancel a workflow, go to "Actions", select the workflow to be cancelled, and click "Cancel workflow"
  <img width="864" height="508" alt="Image" src="https://github.com/user-attachments/assets/102acc72-2b4d-473e-8939-7d75b9ff6c43" />

- Use `[full tests]` in commit messages only when the change requires testing across all supported platforms.
  - Example: `git commit -s -m "<your commit message> [full tests]"`
- Use `[extended tests]` only when the change affects features covered by extended tests (e.g., algorithm behavior changes requiring extended KAT or constant-time tests).
  - Example: `git commit -s -m "<your commit message> [extended tests]"`

## Reviewer Guidelines

- For pull requests requiring workflow approval, the approver should do a basic sanity check before approving the CI run.

## Project-Level CI Optimization Goals

To maximize CI efficiency and ensure effective use of resources, the OQS CI setup should aim to:

- Ensure basic workflows complete within 2 minutes.
- Gate resource-heavy tests behind successful completion of basic checks.
- Ensure that push tests without any tags (i.e., without `[full tests]` or `[extended tests]`) complete within 5 minutes.
- Ensure that PR tests without any tags (i.e., without `[full tests]` or `[extended tests]`) complete within 15 minutes.
- Ensure that full tests (tagged with `[full tests]`) complete within 30 minutes.
- Ensure that extended tests (tagged with `[extended tests]`) complete within 1 hour.
- Limit automatic test runs on non-main branches to a minimal set.
- Cancel in-progress jobs on double-pushes.
- Enable manual triggers for heavy or extended test workflows.
- Ensure regular CI runs in PRs do not exceed 1 hour until completion.

If the limits are exceeded, consider:

- Adding parallel jobs.
- Moving longer-running jobs to weekly workflows (up to 2 hours).
- Moving jobs running longer than 2 hours to tests only triggered manually.
- All workflows, including those only triggered manually, should be run before a release.