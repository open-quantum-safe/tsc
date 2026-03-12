# OQS Technical Steering Committee meeting – 2026-02-17 – minutes

## Attendees

TSC members

- [ ] [Norman Ashley (Cisco)](https://github.com/ashman-p)
- [ ] [Michael Baentsch (independent contributor)](https://github.com/baentsch)
- [ ] [Vlad Gheorghiu (softwareQ Inc.)](https://github.com/vsoftco)
- [x] [Basil Hess (IBM Research)](https://github.com/bhess)
- [x] [Christian Paquin (Microsoft Research)](https://github.com/christianpaquin)
- [x] [Douglas Stebila (University of Waterloo)](https://github.com/dstebila)

Other attendees

- Mark Albert (Cisco)
- Hart Montgomery (LF)
- Ganyu (Bruce) Xu [(University of Waterloo)](https://github.com/xuganyu96)

**Date and time:** Tuesday, February 17, 2026, 14:00-15:00 UTC / 7:00-8:00 US Pacific / 10:00-11:00 US Eastern / 16:00-17:00 Central European

**Location:** Zoom

Information about the TSC (members, roles and responsibilities, charter) is available on Github at [https://github.com/open-quantum-safe/tsc](https://github.com/open-quantum-safe/tsc)

## Agenda

1. Chair's introduction
2. Approve agenda
3. Appoint minute-taker
4. Review [action items from previous meeting](https://github.com/open-quantum-safe/tsc/blob/main/meetings/2026-01-13/minutes.md)
    - [Guidelines on algorithm inclusion](https://github.com/open-quantum-safe/tsc/pull/234)
    - Follow-up: timeline for discontinuing Kyber support
5. Reports
    - PQCA TAC (Norm)
    - PQ Code Package (Basil)
    - PQCA general / Outreach and Education committee (Hart)
6. [Selection of new TSC chair](https://github.com/open-quantum-safe/tsc/issues/246)
7. [PQCA mentorships for summer 2026](https://github.com/open-quantum-safe/tsc/issues/240)
8. Other business

## Chair's introduction

Douglas welcomes attendees. Douglas apologizes for the mixup in the time listed in the distributed agenda. Douglas notes that we do not have quorum, but will continue with discussion today since there are no votes to be held during the meeting.

## Approve agenda

Approved.

## Appoint minute-taker

Douglas will take notes.

## Review action items from previous meeting

### Guidelines on algorithm inclusion

Douglas wrote up the algorithm inclusion guidelines (PR [#234](https://github.com/open-quantum-safe/tsc/pull/234)), incorporated feedback from reviewers, and made revisions. Several approving reviews are already in place. Douglas will formally put it to a vote and then land it.

> [!IMPORTANT]
> **Action (Douglas):** Convert to issue to vote for resolution.

### Timeline for discontinuing Kyber support

Now that the algorithm inclusion guidelines are nearly finalized, Douglas will revive the Kyber timeline discussion to establish a concrete deprecation timeline.

> [!IMPORTANT]
> **Action (Douglas):** Revive the Kyber deprecation timeline discussion.

## Reports

### PQCA TAC (Norm)

Norm is not present. No other attendees had news to share from the TAC.

### PQ Code Package (Basil)

**mlkem-native:** A talk on PQ Code Package will be given at Real World Crypto (in a few weeks) by Matthias. The team plans to finalize a new release around that time, with a major feature being formal proofs for the x86 assembly implementation. The version currently in OQS is outdated relative to development head but remains the official release; OQS can import the new release once it is tagged.

> [!IMPORTANT]
> **Action (Douglas):** Open an issue in liboqs to track updating mlkem-native once the new PQ Code Package release is available.

**mldsa-native:** Currently an alpha release in PQ Code Package (not yet an official release). More work is ongoing. A forthcoming feature is a reduced-RAM/memory-footprint build option, which could be useful for constrained environments.

Discussion of how OQS might support memory-constrained build profiles. Bruce noted in chat that there is an existing embedded build flag, though Basil noted it currently only affects random number generation. The existing machinery for selecting implementation variants (e.g., the Jasmine formally-verified variant for Kyber) may be relevant for future memory-optimized variant support.

### PQCA general / Outreach and Education committee (Hart)

- Encourages all TSC members to participate in the PQCA mentorship program.
- The hybrid event hosted at Cisco (European workshop) had strong attendance: approximately 130–140 online and an estimated 50–60 in person. Hart hopes to do more such events; TSC members interested in hosting similar events should reach out.
- OQS and PQCA stickers have been produced. Hart will bring them to Real World Crypto in Taiwan. Douglas and Basil will also attend and can take packs back to distribute to colleagues.

## Selection of new TSC chair

March 2026 marks the two-year anniversary of the OQS TSC under the Linux Foundation. Douglas would like to hand off the chair responsibilities and build broader leadership within the project. Basil has served as vice chair over the past two years.

Norm nominated Basil for chair; Basil declined but suggested a co-chair structure to distribute responsibilities. Douglas agreed this is a good idea. Options discussed:
- Two new co-chairs step up together.
- Douglas stays on as co-chair with one other person, alternating meeting facilitation.

The discussion will continue in issue [#246](https://github.com/open-quantum-safe/tsc/issues/246), with the goal of reaching a resolution before the next TSC meeting.

> [!IMPORTANT]
> **Action (all):** [Discuss options for new TSC chair](https://github.com/open-quantum-safe/tsc/issues/246).

## PQCA mentorships for summer 2026

Key dates for the [PQCA summer 2026 mentorship program](https://github.com/open-quantum-safe/tsc/issues/240):
- **Feb 2 – Mar 13:** Committee members submit project proposals.
- **Second half of March:** TAC reviews proposals.
- **End of March:** Selected projects posted; mentee applications open until **May 8**.
- **Late May:** Mentee interview and selection.
- **June – August:** Mentorship program runs (some schedule flexibility available).

Basil shared his experience mentoring a fall-term project on constant-time analysis:

- Received approximately 100 applications; conducted short conversations with 3–4 candidates before selecting one (a PhD student).
- Structured the engagement in phases: project orientation, then implementation work.
- Held weekly 30–60 minute sync calls; mentor time commitment was roughly 2–3 hours per week.
- Work was conducted in a fork of liboqs that set up constant-time tooling and then ran it across all liboqs algorithms, generating a large dataset. Interesting characteristics emerged across different compiler versions and optimization levels.
- Next steps for that project: analyze results in detail for at least one algorithm (distinguishing false positives from true positives), then gradually integrate into the main liboqs repository.
- The mentee (a PhD student) is interested in writing a publication; the Linux Foundation also encourages a blog post at the end of the mentorship.
- Overall assessment: the program has some mentor time commitment but is very worthwhile for bringing contributors into the project and potentially retaining them beyond the mentorship period.

A potential follow-up mentorship project was discussed: adding constant-time primitives to liboqs common code and patching existing implementations to use them.

Douglas encouraged TSC members and industry contributors to consider proposing projects by **March 13**. Scope can be broadly PQC-related: directly in liboqs, in OQS sub-projects, or even new work (e.g., post-quantum oblivious PRFs, threshold signatures) that could eventually find a home in PQCA.

> [!IMPORTANT]
> **Action (all):** [Consider proposing a project for the PQCA mentorship program](https://github.com/open-quantum-safe/tsc/issues/240) by March 13, 2026.

## Other business

Douglas is in an email exchange with Michael on maintainer and committer guidelines. A draft is expected to appear within the next week or so.

## Next meeting

Next week is an OQS status call at the later time slot (12:30 Eastern). The following TSC meeting will be in approximately one month. Several members (Douglas, Basil) will attend Real World PQC and Real World Crypto in Taiwan in the coming weeks.
