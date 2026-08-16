# Reviewing pull requests in OQS

The goal of this guideline is to describe what a good review looks like, so reviewers have a shared reference point. It is guidance, not a checklist — nothing here should be used to block a merge or discourage anyone, maintainer, committer, or first-time contributor, from reviewing.

## What a good review looks like

- **Avoid empty approvals.** When you approve, add a sentence or two on what you checked or why the change looks correct — "verified against RFC X §Y" or "matches the pattern used in the KEM adapter" tells the next person something; a bare approval doesn't, and is indistinguishable from a rubber stamp to anyone reading the history later.
- **Leave the comment where the thought happened.** If something is unclear, could break another algorithm, or just made you pause, say so inline, even briefly. You don't need to resolve it yourself — flagging it is the useful part.
- **Requesting changes is a normal outcome, not a verdict on the contributor.** If something needs fixing before merge, say so. Reviews that never request changes usually mean issues are being caught in earlier informal discussion (great) or not being caught at all (not great) — and from the outside those look identical, so it's worth being explicit either way.
- **Match the depth of your review to the depth of the change.** Typo fixes, version bumps, and similar trivial changes are fine with a plain approval and no further comment. But a change to constant-time arithmetic deserves real engagement — save the substance for where it matters, rather than either skipping it everywhere or adding ceremony everywhere.
- **Don't delete other people's contributions or comments.** If a comment or suggestion seems wrong, resolved, or off-base, reply or mark it resolved — don't remove it. The discussion trail is part of the record, including for people who weren't in the room.

If you're new to a subproject and unsure what to look for, saying so in the review is itself useful signal — it tells maintainers where reviewer bandwidth is thin.
