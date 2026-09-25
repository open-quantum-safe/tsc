# Caretaker Process

## When this applies

A sub project moves to `INACTIVE`/`UNMAINTAINED` status in either of these cases:

- it loses its last Maintainer and no Committer is ready to step up and
  be listed as Maintainer in their place, or
- it still has a listed Maintainer, but that person is not actually
  fulfilling the Maintainer responsibilities defined in GOVERNANCE.md
  (e.g. unresponsive to PRs and issues over a sustained period).

Once this happens, the TSC will have the capacity to appoint an interim caretaker 
for that subproject. Any TSC member, at a TSC meeting or via a TSC repository issue, 
may raise that a sub project has reached either of these states.

## Nomination

- The TSC chair nominates a candidate Caretaker, either self-nominated or
  proposed by another TSC member or the community.
- There is no requirement that a Caretaker be a subject-matter expert in
  the sub project; willingness and basic GitHub/CI literacy are
  sufficient, since the role's responsibilities are deliberately narrow
  (see the sub project's GOVERNANCE.md).
- If no one is willing to be named as an individual Caretaker, the TSC
  may instead grant the `oqs-maintainers` GitHub team the ability to
  approve and merge PRs on the sub project, as a fallback that does not
  require naming a person.

## Appointment

- The nomination is confirmed by a TSC vote, following the TSC's standard
  voting procedures.
- Once confirmed:
  - The sub project's GOVERNANCE.md is updated to name the Caretaker (or
    the `oqs-maintainers` team) under the Caretaker entry.
  - The `INACTIVE`/`UNMAINTAINED` status is set in the two places
    established by the existing openssh precedent: the GitHub repository
    description ("project overview"), and a prominent line near the top
    of the README, e.g. "PROJECT INACTIVE. CONTRIBUTORS WANTED."
  - The Caretaker (or the `oqs-maintainers` team) is granted the GitHub
    permissions needed to approve and merge PRs on that repository —
    no more.
- Appointment is per sub project. A Caretaker for one sub project has no
  standing role in any other.

## TSC oversight

- The TSC periodically reviews open Caretaker appointments to confirm the
  appointment is still needed and still working, and to actively solicit
  Contributors willing to grow into a true Maintainer.
- The TSC is the escalation point if a Caretaker's merges are disputed,
  or if the Caretaker is not keeping to the narrow scope defined in
  GOVERNANCE.md.
- While a project is under Caretaker status, the TSC assumes the
  governance decisions a Maintainer would normally make unilaterally.
  This includes not only voting on a replacement Maintainer, but also
  confirming any Contributor who wants to become a Committer on that
  project.

## Relief of duty

The Caretaker role for a sub project ends in any of these ways:

1. **A Maintainer is voted in.** A Contributor who wants to take on real
   maintenance presents themselves at a TSC meeting and is voted on as
   usual, per existing process. Once confirmed, the Caretaker role for
   that sub project ends immediately, the GOVERNANCE.md Caretaker entry
   is removed, and the `INACTIVE`/`UNMAINTAINED` status is lifted.
2. **The Caretaker steps down.** A Caretaker may resign at any time,
   without needing to justify it, by notifying the TSC chair. The TSC
   then either nominates a replacement or falls back to
   `oqs-maintainers` team rights per the nomination process above.
3. **The TSC removes a Caretaker.** If a Caretaker is not fulfilling even
   the narrow scope of the role (e.g. unresponsive, or acting outside
   the documented responsibilities), any TSC member may raise this at a
   TSC meeting, and the TSC may vote to end the appointment, following
   the same voting procedure used to confirm it.

In all cases, ending a Caretaker appointment without a new Maintainer in
place reverts the sub project to fallback `oqs-maintainers` team rights
until a new Caretaker is nominated.
