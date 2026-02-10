# OQS Technical Steering Committee meeting – 2026-01-13 – minutes

## Attendees

TSC members

- [x] [Norman Ashley (Cisco)](https://github.com/ashman-p)
- [x] [Michael Baentsch (independent contributor)](https://github.com/baentsch)
- [ ] [Thomas Bailleux (independent contributor)](https://github.com/zadlg)
- [ ] [Vlad Gheorghiu (softwareQ Inc.)](https://github.com/vsoftco)
- [x] [Basil Hess (IBM Research)](https://github.com/bhess)
- [x] [Christian Paquin (Microsoft Research)](https://github.com/christianpaquin)
- [x] [Douglas Stebila (University of Waterloo)](https://github.com/dstebila)

Other attendees

- Ganyu (Bruce) Xu [(University of Waterloo)](https://github.com/xuganyu96)
- Hart Montgomery (LF)

**Date and time:** Tuesday, January 13, 2026, [17:30-18:30 UTC / 9:30-10:30 US Pacific / 12:30-13:30 US Eastern / 18:30-19:30 Central European](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20260113T1230&p1=1203)

**Location:** [Zoom](https://zoom-lfx.platform.linuxfoundation.org/meetings/pqca?view=week&occurrence=1768325400)

Information about the TSC (members, roles and responsibilities, charter) is available on Github at [https://github.com/open-quantum-safe/tsc](https://github.com/open-quantum-safe/tsc)

## Agenda

1. Chair's introduction
2. Approve agenda
3. Appoint minute-taker
4. Review [action items from previous meeting](https://github.com/open-quantum-safe/tsc/blob/main/meetings/2025-11-25/minutes.md)
5. Reports
6. Governance positions
7. CI usage
8. [Impact of wind-down of PQClean](https://github.com/open-quantum-safe/liboqs/issues/2341)
9. [Soliciting more schemes from NIST signature on-ramp round 2](https://github.com/open-quantum-safe/liboqs/issues/2098)
10. Other business

## Chair's introduction

Douglas welcomes attendees.

## Approve agenda

Approved.

## Appoint minute-taker

Basil will take notes.

## Review action items from previous meeting

### Feedback on proposed liboqs-node subproject

Hart found JavaScript expert willing to review project; feedback expected next week.

Michael raised whether we have defined requirements for subprojects. 
Discussion on criteria:
- Contributors should identify maintainers and understand maintainer role
- Basic criteria: documented active contributor, documented usage information
- Should state "fit" - how it complements OQS capabilities or research/production focus

Douglas will write down basic subproject requirements.

## Reports

### PQCA TAC (Norm)

Last meeting mid-December 2025. Discussions on training, mentorship, and CI costs. PQCP CI is biggest cost contributor; OQS relatively small. Mentorship opportunities available; finding mentors is bottleneck.

### PQ Code Package

MLDSA-native PR to liboqs open. PQCP team planning next release soon.

### PQCA general / Outreach and Education committee (Hart)

Upcoming events:
- RWPQC announcement and speaker list coming soon
- European workshop at Cisco offices (Zurich, Munich, Copenhagen) - hybrid, open to public, PQ migration focus

## Governance positions

### PQ Code Package liaison

Basil offered to take role given existing contact with maintainers and experience with reference code.

Basil will serve as PQ Code Package liaison.

### TSC chair

Douglas offers to hand off chair role by March (two-year anniversary). Will continue participating. Looking for TSC members to consider chair/vice-chair roles.

## CI usage

Basil's draft guidelines ready to finalize. Agreed to place in "guidelines" directory in TSC repository (enables PRs and version control).

- Basil will create PR for CI guidelines
- To create implementation issues for liboqs and oqs-provider after guidelines land

## Impact of wind-down of PQClean

PQClean archiving over next few months. OQS relies on it for some algorithms (issue [#2341](https://github.com/open-quantum-safe/liboqs/issues/2341)). Options: replace, maintain via patches, or remove.

Christian raised broader question about OQS's long-term role as algorithms mature. Douglas noted lack of documented algorithm policy. Michael agreed - some algorithms favored, others neglected. Suggested documenting policy and considering dropping algorithms treated [stiefmüttelich](https://dict.leo.org/german-english/stiefmütterlich).

Douglas to draft algorithm policy and circulate for feedback.

## Soliciting more schemes from NIST signature on-ramp round 2

Limited traction (issue [#2098](https://github.com/open-quantum-safe/liboqs/issues/2098)). Bruce reported copy-from-upstream not a blocker. Douglas suggested focusing on 1-2 algorithms with OQS point persons. FAEST identified as candidate (issue [#2101](https://github.com/open-quantum-safe/liboqs/issues/2101)). Basil to contact a FAEST co-author.

## Other business

### Kyber support

Michael asked whether ML-KEM native could be patched to support Kyber, allowing OQS to drop PQ-crystals. Basil prefers sunsetting Kyber if not further used. Most ML-KEM/Kyber internals same, so patching theoretically possible, but PQCP maintainers likely wouldn't support it. Michael argued back-patch might be less work than maintaining full PQ-crystals without support.

Douglas suggested establishing timeline for dropping Kyber to inform investment needed.

Once algorithm policy written, determine timelines for dropping algorithms including Kyber.

## Next meeting

February 17, 2026, 10 a.m. Eastern. OQS status calls continue in between.