# OQS Technical Steering Committee meeting – 2026-03-24 – minutes

## Attendees

TSC members

- [ ] [Norman Ashley (Cisco)](https://github.com/ashman-p)
- [x] [Michael Baentsch (independent contributor)](https://github.com/baentsch)
- [ ] [Vlad Gheorghiu (softwareQ Inc.)](https://github.com/vsoftco)
- [x] [Basil Hess (IBM Research)](https://github.com/bhess)
- [ ] [Christian Paquin (Microsoft Research)](https://github.com/christianpaquin)
- [ ] [Douglas Stebila (University of Waterloo)](https://github.com/dstebila)

Other attendees

- Hart Montgomery (LF)
- Kamal Tufekcic
- Rodrigo Martín (Indra)
- Ganyu (Bruce) Xu [(University of Waterloo)](https://github.com/xuganyu96)

**Date and time:** Tuesday, March 24, 2026, 16:30-17:30 UTC / 9:30-10:30 US Pacific / 12:30-13:30 US Eastern / 17:30-18:30 Central European

**Location:** Zoom

Information about the TSC (members, roles and responsibilities, charter) is available on Github at [https://github.com/open-quantum-safe/tsc](https://github.com/open-quantum-safe/tsc)

## Agenda

1. Introduction
2. Approve agenda
3. Appoint minute-taker
4. Review [action items from previous meeting](https://github.com/open-quantum-safe/tsc/blob/main/meetings/2026-02-17/minutes.md)
    - [Guidelines on algorithm inclusion](https://github.com/open-quantum-safe/tsc/pull/234)
    - [Follow-up: timeline for discontinuing Kyber support](https://github.com/open-quantum-safe/liboqs/issues/1989)
    - [Track release of mlkem-native 1.1.0](https://github.com/open-quantum-safe/liboqs/issues/2365)
5. Reports
    - PQCA TAC (Norm)
    - PQ Code Package (Basil)
    - PQCA general / Outreach and Education committee (Hart)
6. [Selection of new TSC chair](https://github.com/open-quantum-safe/tsc/issues/246)
7. [PQCA mentorships for summer 2026 (deadline for proposals extended)](https://github.com/open-quantum-safe/tsc/issues/240)
8. Project governance and onboarding (review) [[1]](https://github.com/open-quantum-safe/oqs-provider/pull/764),[[2]](https://github.com/user-attachments/files/26002281/oqs_health_report.docx)
9. Other business

## Introduction

Douglas is absent; Basil chairs the meeting on his behalf. Basil notes that quorum is not reached (2 of 6 TSC members present), but the meeting will proceed with discussion since there are no votes to be held.

## Approve agenda

Approved without changes.

## Appoint minute-taker

Minutes compiled from AI-assisted transcript by Basil.

## Review action items from previous meeting

### Guidelines on algorithm inclusion

The algorithm inclusion guidelines (PR [#234](https://github.com/open-quantum-safe/tsc/pull/234)) have been approved and merged since the last meeting. Michael noted for the record that the guidelines ended up being high-level, with the understanding that they will be reviewed on a case-by-case basis for each algorithm. No further comments.

### Timeline for discontinuing Kyber support

Basil summarized the situation: liboqs still ships Kyber alongside the standardized ML-KEM. Kyber was deprecated in a recent release with the plan to remove it in the next release. However, at least one downstream open-source project (Rosenpass, deployed in Linux distributions) still depends on Kyber and has indicated a migration timeline of several years.

Discussion points:
- Rodrigo noted that from a research perspective there is negligible interest in Kyber, and OQS is not formally a production library, so there is no strong reason to continue support beyond legacy users.
- Michael expressed concern about maintaining an unsupported algorithm with no upstream, and noted that only one user (Rosenpass) has spoken up.
- Basil suggested asking Rosenpass whether they would be willing to maintain Kyber themselves, similar to the model used for NTRU (which was reintroduced and is maintained by its interested parties).
- Hart agreed that asking the downstream user to maintain the code is the right approach.

Michael raised a related topic: establishing a lead maintainer or responsible party for every algorithm in liboqs. This would provide a clear contact for security issues and support questions. Hart noted this aligns with standard open-source security practices. Basil suggested the existing CODEOWNERS mechanism could be reviewed and updated to address this.

> [!IMPORTANT]
> **Action (Basil):** Follow up on the Kyber deprecation issue, stating limitations of continued support and asking if downstream users are willing to maintain Kyber themselves.

> [!IMPORTANT]
> **Action (Basil):** Create issue to review and update CODEOWNERS in liboqs to establish a responsible maintainer for each algorithm.

### Track release of mlkem-native 1.1.0

The mlkem-native 1.1.0 release is available and a pull request to update it in liboqs has been approved. It is expected to land soon.

## Reports

### PQCA TAC (Norm)

Norm is not present. Hart noted the TAC meeting was skipped two weeks ago (due to Real World PQC), so there is nothing new to report.

### PQ Code Package (Basil)

Basil attended the PQ Code Package TSC meeting and shared the following updates:

**mlkem-native:** The 1.1.0 release has been finalized. A key feature is that formal proofs for both the x86 and ARM assembly backends are now complete, covering correctness, memory safety, and constant-time properties. Presentations were given at Real World Crypto.

**mldsa-native:** Still in alpha. The plan is to complete formal proofs of the assembly implementations and produce a stable release this year.

**New project proposal:** A C++ library implementing ML-DSA and ML-KEM has requested onboarding into PQ Code Package. Discussion is ongoing about whether to include it. A decision is expected soon. Implications for integration into liboqs (e.g., via the C++ bindings) to be discussed.

### PQCA general / Outreach and Education committee (Hart)

- The Outreach and Education committee is developing a developer-targeted PQC course in collaboration with the LF Training and Education team, aiming to produce initial content soon.
- Google will deliver a series of two webinars: the first (April 14) on crypto agility and PQ migration by Stefan, the second on PQ migration prioritization by Sophie. Additional webinars are planned, including an AWS session on migrating Ubuntu on EC2 to use ML-KEM with OpenSSH, and a potential Trail of Bits session on lessons learned and common pitfalls in migration.


## Selection of new TSC chair

Basil reviewed the status of the chair selection discussion (issue [#246](https://github.com/open-quantum-safe/tsc/issues/246)). Douglas has outlined suggested responsibilities for the TSC chair and options for a single chair versus co-chairs are outlined.

Michael observed that participation in the discussion has been limited and urged all TSC members and the broader community to contribute. Key open questions include: what responsibilities should the chair carry, how much time is involved, and who is willing to step up.

Kamal and Rodrigo both expressed interest in understanding the concrete responsibilities and time commitment before considering involvement. Rodrigo suggested a mentorship-style co-chair transition could help onboard newer members who lack background on the LF relationship.

Hart clarified that the charter defines the chair's role as presiding over TSC meetings and serving as the primary communication contact for the PQCA, with the possibility of delegating tasks. The current PQCA TAC liaison role is already handled by Norm.

Basil noted that the PQ Code Package TSC has a one-year term for its chair. Hart confirmed the OQS charter leaves the term open-ended.

> [!IMPORTANT]
> **Action (all):** [Continue discussing TSC chair selection, responsibilities](https://github.com/open-quantum-safe/tsc/issues/246).

## PQCA mentorships for summer 2026

The deadline for project proposals has been extended to **April 17, 2026**. Basil encouraged anyone with project ideas or interest in mentoring to propose via issue [#240](https://github.com/open-quantum-safe/tsc/issues/240). Basil noted he has prior mentorship experience and is available to answer questions.

> [!IMPORTANT]
> **Action (all):** [Consider proposing a project for the PQCA mentorship program](https://github.com/open-quantum-safe/tsc/issues/240) by April 17, 2026.

## Project governance and onboarding

Michael prepared a project health report for OQS (generated with AI assistance from analyzing GitHub activity). Key findings and actions discussed:

- **oqs-provider:** Rodrigo has been approved as a maintainer, addressing the critical finding that only one active maintainer was in place. Michael also streamlined the requirements for committers and maintainers in the oqs-provider governance documents.
- **liboqs:** The governance file is outdated — it does not reflect current active contributors (e.g., Bruce is missing) and lists some inactive contributors. The report recommends updating governance across all OQS repositories to accurately represent current project health.
- Michael emphasized the importance of both promoting active contributors and removing inactive ones, to present an honest picture of the project's state.
- Rodrigo encouraged all attendees to read the full report, noting that the metrics (e.g., ~70% of contributions coming from 3–4 people) highlight areas of concern beyond just governance.

> [!IMPORTANT]
> **Action (Basil):** Create an issue in liboqs to track updating the governance file with current maintainers, committers, and contributors.

## Other business

Rodrigo asked about plans for an in-person meetup at Eurocrypt. Hart said a happy hour was held at Real World Crypto (approximately 20–30 attendees) and that a similar event could be organized for Eurocrypt if enough community members are attending. Basil confirmed he will attend Eurocrypt; Kamal and Rodrigo also expressed interest.

> [!IMPORTANT]
> **Action (Hart):** Gauge interest and potentially organize a PQCA social event at Eurocrypt.
