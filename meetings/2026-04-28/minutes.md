# OQS Technical Steering Committee meeting – 2026-04-28 – minutes

## Attendees

TSC members

- [x] [Norman Ashley (Cisco)](https://github.com/ashman-p)
- [x] [Michael Baentsch (independent contributor)](https://github.com/baentsch)
- [ ] [Vlad Gheorghiu (softwareQ Inc.)](https://github.com/vsoftco)
- [x] [Basil Hess (IBM Research)](https://github.com/bhess)
- [x] [Rodrigo Martín (Indra)](https://github.com/bheRodriM11ss)
- [x] [Christian Paquin (Microsoft Research)](https://github.com/christianpaquin)
- [x] [Douglas Stebila (University of Waterloo)](https://github.com/dstebila)

Other attendees

- Hart Montgomery (LF)
- Kamal Tufekcic
- Bruce Xu (University of Waterloo)

**Date and time:** Tuesday, April 28, 2026, 14:00-15:00 UTC / 7:00-8:00 US Pacific / 10:00-11:00 US Eastern / 16:00-17:00 Central European

**Location:** Zoom

Information about the TSC (members, roles and responsibilities, charter) is available on Github at [https://github.com/open-quantum-safe/tsc](https://github.com/open-quantum-safe/tsc)

## Agenda

1. Introduction
2. Approve agenda
3. Review [action items from previous meeting](https://github.com/open-quantum-safe/tsc/blob/main/meetings/2026-03-24/minutes.md)
    - [Update CODEOWNERS in liboqs to establish a responsible maintainer for each algorithm and update GOVERNANCE file with current maintainers/committers](https://github.com/open-quantum-safe/liboqs/pull/2410)
    - [PQCA mentorship program deadline was April 17, 2026](https://github.com/open-quantum-safe/tsc/issues/240)
    - Hart: Gauge interest and potentially organize a PQCA social event at Eurocrypt
4. Reports
    - PQCA TAC (Norm)
    - PQ Code Package (Basil)
    - PQCA general / Outreach and Education committee (Hart)
5. Project health report
6. TSC vice chair role starting September 2026
7. OQS presentations at appropriate conferences
8. Other business

## Introduction and approve agenda

Agenda approved without changes.

## Review action items from previous meeting

### CODEOWNERS and GOVERNANCE update

Douglas noted that he has opened [PR #2410](https://github.com/open-quantum-safe/liboqs/pull/2410) on liboqs, which updates `GOVERNANCE.md` and `CODEOWNERS` to reflect the current state of the contributor base. The PR moves several existing contributors and maintainers to emeritus status based on recent engagement, and proposes adding Bruce (@xuganyu96) as a maintainer and Norm (@ashman-p), Matthias (@mkannwischer), and Rodrigo (@RodriM11) as committers. A matching PR on `tsc/config.yaml` will accompany it. Douglas asked members to review and provide feedback, noting that under GOVERNANCE.md the additions/promotions and removals require a majority/supermajority vote of active committers and maintainers.

> [!IMPORTANT]
> **Action (all):** Review and vote on [liboqs PR #2410](https://github.com/open-quantum-safe/liboqs/pull/2410) (GOVERNANCE.md and CODEOWNERS update).

### PQCA mentorship program

The deadline for project proposals (April 17, 2026) has passed, but Hart noted that mentorship projects can still be submitted — there is budget available for them. Hitting the typical summer timeline may be tight at this point, but overall mentorship project timelines are flexible and can be adjusted (e.g., half-time over six months instead of three). Michael asked how the program works in practice; Hart explained that mentors create proposals, mentees apply, and mentors select the mentee they prefer to work with. Project listings appear on the LF mentorship dashboards.

> [!IMPORTANT]
> **Action (all):** [Continue to consider proposing a project for the PQCA mentorship program](https://github.com/open-quantum-safe/tsc/issues/240); proposals are still welcome.

### Eurocrypt social event

Hart reported that polling indicated very few PQCA folks are attending Eurocrypt this year, so there is not enough momentum for a dedicated event. He noted that LF can help arrange happy hours at other events (e.g., Crypto) if there is sufficient interest. Discussion of conference engagement was deferred to the conference agenda item later in the meeting.

## Reports

### PQCA TAC (Norm)

Norm reported that the most significant item from the last TAC meeting was a new working group proposal from Amazon to create a repository / inventory of cryptographic libraries and applications using PQC algorithms (and beyond). Discussion is focused on synergies with other sub-working projects, whether data would be self-reported, and how to verify it. The [proposal is still under discussion](https://github.com/PQCA/TAC/issues/139); nothing has been decided.

### PQ Code Package (Basil)

**mldsa-native:** A beta release was made about a month ago (previously in alpha). The plan is to release improved versions every 2–3 months toward a final release this year. The major outstanding milestone before the final release is formal verification of the assembly code (the C code is already formally verified for memory safety and undefined behavior). The beta includes a reduced-memory version of ML-DSA, which could be valuable for memory-constrained users of liboqs. The upstream project is interested in opening regular pull requests against liboqs to keep it in sync with new releases (one such draft PR by Matthias already exists). Basil is in favor of accepting these regular updates given the upstream is proactive. Other consumers of mldsa-native include Amazon's libcrypto (where liboqs already uses the alpha) and OpenTitan.

**mlkem-native:** liboqs already includes the latest release. New developments include a RISC-V optimized version (not yet imported into liboqs) and an in-progress PowerPC optimization with GitHub Actions CI; Basil is helping to land the latter.

**slhdsa-c:** Rodrigo asked whether this project is also part of the regular update cadence. Basil noted it is at a relatively early stage and has not yet had a release.

Discussion: Michael agreed that accepting upstream pull requests is a no-brainer, but raised the broader question of how to determine which platforms (e.g., RISC-V, PowerPC) liboqs users actually want supported. Rodrigo agreed and suggested using upcoming conference engagement to poll users about their needs. Hart noted in chat that an OQS user poll was conducted in the past and could be repeated. Kamal clarified that liboqs already runs on RISC-V (he has tested it on RISC-V hardware); the open question is specifically whether to integrate the assembly/SIMD-optimized RISC-V code. Rodrigo noted that as new architectures are added, CI coverage for those architectures should be a prerequisite.

> [!IMPORTANT]
> **Action (Basil):** Coordinate with upstream mldsa-native maintainers on regular synchronization PRs into liboqs.

### PQCA general / Outreach and Education committee (Hart)

The main update is the ongoing webinar series on PQ migration. Stefan from Google delivered a webinar on migration that was well received (lots of questions, good content for sharing with people who are less familiar with the topic). Upcoming sessions include one from AWS and another from Sophie at Google on prioritizing PQ migrations. Hart encouraged members to tune in or share the recordings with others.

## Project health report

Rodrigo presented slides summarizing [Michael's project health report](https://github.com/user-attachments/files/26002281/oqs_health_report.docx), which was generated with the help of Claude with a focus on the last 18 months of GitHub activity for liboqs and oqs-provider.

Key findings highlighted:

- **liboqs:** Overall score 6.7/10. Activity peaked in June 2025 and has since trended downward. Retention of contributors is roughly 22%. Bus factor and concentration of contributions among a small core (~18 people) are concerns, though some metrics will improve once the governance/maintainer changes in PR #2410 are merged.
- **oqs-provider:** Overall score 4.3/10. Bus factor of effectively one (Michael accounts for ~50% of activity; top three account for ~60%). Strong year-over-year decline (~50%). Approximately 60% of contributions are one-time. Activity peaked in September 2025 and has trended down since.
- **Cross-project:** 81 unique contributors across both projects, but most are one-time contributors; the effective core is about 18 people.
- **Review culture:** ~40% of changes on liboqs and ~36% on oqs-provider are approved, with only ~4% formally requesting changes — suggesting reviewers may not always be using the formal "request changes" mechanism even when they have substantive comments.

Discussion points:

- Douglas noted the report captured many things that were intuitively known but not articulated, and welcomed recommendations around cultivating reviewers, mentoring high-potential contributors, and revisiting project health on a regular basis. He suggested using AI-assisted tools to help triage and review code.
- Rodrigo proposed generating an updated project health report on a quarterly basis so the TSC can track progress.
- Michael said many of the findings and recommendations surprised him as well; he was particularly struck by the review-culture finding (PRs being approved without comment) and emphasized the need to invest more effort in thorough review even if it means reviewing fewer PRs.
- Hart noted that several LF projects have PR review guidelines (some informal, some strict) that the TSC could look at as examples.
- Douglas and Rodrigo agreed that formal review rules might discourage participation at this stage; informal guidelines or helper tooling would be preferable.
- Norm suggested that better issue grooming — clear definition-of-done and scope per issue — would help reviewers know what to look for. He also asked whether the report could track the project's positioning between "research-focused" and "production-grade" maturity, and noted that the long-standing practice of redirecting users from oqs-provider to OpenSSL may dampen enthusiasm and contributions to oqs-provider.
- Michael responded that oqs-provider was never intended to compete with OpenSSL on production-grade implementations of standardized algorithms, but rather to be a research vehicle and a bridge for non-standardized / experimental work.
- Christian echoed Michael's view and added that OQS overall lacks clear "exit criteria" for sub-projects: a success story is being able to retire a sub-project once its target integration environment is taking it on (similar to the situation with Open SSH). He suggested this reflection should apply across all OQS sub-projects.

Time ran short during this discussion; Rodrigo committed to opening issues to continue the conversation on project mission, scope, and review culture before the next TSC meeting.

> [!IMPORTANT]
> **Action (Rodrigo):** Open issue(s) to continue discussion of OQS project mission/scope, oqs-provider's role relative to OpenSSL, and review culture / guidelines.

> [!IMPORTANT]
> **Action (Rodrigo):** Generate an updated project health report on a quarterly cadence and bring it to the TSC for discussion.

## TSC vice chair role starting September 2026

Deferred to the next meeting due to time constraints.

> [!IMPORTANT]
> **Action (Douglas):** Bring TSC vice chair discussion to the next meeting.

## OQS presentations at appropriate conferences

Rodrigo proposed re-establishing OQS presence at relevant conferences to (a) communicate that OQS is active and that its core mission — research, new algorithms, new primitives, hybrid constructions — remains very much relevant despite the standardization of the first PQC algorithms, (b) gather feedback from users about what they want from the project, and (c) attract new contributors.

Identified target venues:

- [OpenSSL Conference](https://openssl-conference.org/call-for-papers/) — submissions due May 31, 2026; event October 13–15, Prague.
- [PKI Consortium](https://pkic.org/wg/pqc/conferences/) — submissions open; event December 1–3, Amsterdam.
- RWPQC (March 2027).
- ICMC (April 2027).

Hart noted that the [Open Source Summit](https://events.linuxfoundation.org/) takes place in Prague at roughly the same time as the OpenSSL Conference and that the two could potentially be combined into a single trip.

Rodrigo offered to draft submission proposals (as part of the TSC chair role) and circulate them via GitHub issues for feedback before submission. Douglas suggested resolving the OpenSSL Conference and PKI Consortium submissions over GitHub in the coming weeks since both deadlines fall before the next TSC meeting.

> [!IMPORTANT]
> **Action (Rodrigo):** Open GitHub issues to draft and review submission proposals for the OpenSSL Conference and the PKI Consortium event.

> [!IMPORTANT]
> **Action (all):** Suggest other relevant conferences worth attending via the issues opened by Rodrigo.

## Other business

None — meeting ran slightly over time and was wrapped up.
