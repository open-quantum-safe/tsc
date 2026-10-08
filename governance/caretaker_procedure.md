# Caretaker Process

## When this applies

A sub project moves to `INACTIVE`/`UNMAINTAINED` status in either of these cases:

- it loses its last Committer, or
- it still has a listed Committer, but that person is not actually
  fulfilling the Committer responsibilities defined in GOVERNANCE.md
  (e.g. unresponsive to PRs and issues over a sustained period).

Once this happens, the TSC will have the capacity to appoint an interim caretaker
for that subproject. Any TSC member, at a TSC meeting or via a TSC repository issue,
may raise that a sub project has reached either of these states.

## Default timeline

When a sub project reaches this state:

1. It is flagged: a tracking issue is opened in the TSC repository and a
   "maintenance at risk" line is added to the sub project's README.
2. It is archived (read-only) after one TSC meeting cycle, unless within
   that window someone volunteers as Caretaker, or the TSC votes for
   something else.

## Nomination

- The TSC chair nominates a candidate Caretaker, either self-nominated or
  proposed by another TSC member or the community.
- There is no requirement that a Caretaker be a subject-matter expert in
  the sub project; willingness and basic GitHub/CI literacy are
  sufficient, since the role's responsibilities are deliberately narrow
  (see the sub project's GOVERNANCE.md).
- If no one volunteers within the window of the default timeline, the
  sub project is archived.

## Appointment

- The nomination is confirmed by a TSC vote, following the TSC's standard
  voting procedures.
- Once confirmed:
  - The sub project's GOVERNANCE.md is updated to name the Caretaker
    under the Caretaker entry.
  - The `INACTIVE`/`UNMAINTAINED` status is set in the two places
    established by the existing openssh precedent: the GitHub repository
    description ("project overview"), and a prominent line near the top
    of the README, e.g. "PROJECT INACTIVE. CONTRIBUTORS WANTED."
  - The Caretaker is granted the GitHub permissions needed to approve
    and merge PRs on that repository — no more.
- Appointment is per sub project. A Caretaker for one sub project has no
  standing role in any other.

## Grooming Contributors into Committers

A key responsibility of the Caretaker is to groom Contributors into
Committers: to help willing Contributors grow, teach them the project's
code base and processes, and ensure the takeover runs smoothly once they
are ready. Soliciting interest is not enough. The Caretaker identifies
candidates, mentors them, and puts them forward to the TSC for a vote.

## TSC oversight

- The TSC periodically reviews open Caretaker appointments to confirm the
  appointment is still needed and still working, and that grooming is
  making progress.
- The TSC is the escalation point if a Caretaker's merges are disputed,
  or if the Caretaker is not keeping to the narrow scope defined in
  GOVERNANCE.md.
- While a project is under Caretaker status, the TSC assumes the
  governance decisions a Maintainer/Committer would normally make unilaterally.
  This includes not only voting on a replacement Maintainer/Committer, but also
  confirming any Contributor who wants to become a Committer on that
  project.

## Relief of duty

The Caretaker role for a sub project ends in any of these ways:

1. **A Committer or Maintainer is voted in.** A Contributor groomed by
   the Caretaker, or otherwise willing to take on real maintenance,
   presents themselves at a TSC meeting and is voted on as usual, per
   existing process. Once confirmed and the handover is complete, the
   Caretaker role for that sub project ends, the GOVERNANCE.md Caretaker
   entry is removed, and the `INACTIVE`/`UNMAINTAINED` status is lifted.
2. **The Caretaker steps down.** A Caretaker may resign at any time,
   without needing to justify it, by notifying the TSC chair. The TSC
   then either nominates a replacement or the default timeline above
   applies from the date of the resignation.
3. **The TSC removes a Caretaker.** If a Caretaker is not fulfilling even
   the narrow scope of the role (e.g. unresponsive, or acting outside
   the documented responsibilities), any TSC member may raise this at a
   TSC meeting, and the TSC may vote to end the appointment, following
   the same voting procedure used to confirm it.

In all cases, if a Caretaker appointment ends without a new Committer or
Maintainer in place, the default timeline above applies: the sub project
is archived after one TSC meeting cycle unless a new Caretaker volunteers
or the TSC votes for something else.