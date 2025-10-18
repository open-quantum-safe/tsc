# OQS Technical Steering Committee meeting – 2025-09-16 – minutes

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

- Bruce (University of Waterloo) Hart (Linux Foundation)

**Date and time:** Tuesday, September 16, 2025, 16:30-17:30 UTC / 9:30-10:30 US Pacific / 12:30-13:30 US Eastern / 18:30-19:30 Central European

Information about the TSC (members, roles and responsibilities, charter) is available on Github at [https://github.com/open-quantum-safe/tsc](https://github.com/open-quantum-safe/tsc)

## Agenda

1. Chair's introduction
2. Approve agenda
3. Appoint minute-taker
4. Review [action items from previous meeting](https://github.com/open-quantum-safe/tsc/blob/main/meetings/2025-08-12/minutes.md)
5. Reports
    - PQCA TAC (Norm)
    - PQ Code Package
    - PQCA general / Outreach and Education committee (Hart)
6. [PR review procedure for liboqs](https://github.com/orgs/open-quantum-safe/discussions/2268)
7. Motion: [Allow contributions to OQS-OpenSSH using upstream licence](https://github.com/open-quantum-safe/tsc/pull/204)
8. Generative AI
    - Follow up from Christian's experiments and [discussion](https://github.com/orgs/open-quantum-safe/discussions/2253)
    - [Issue/PR template updates](https://github.com/open-quantum-safe/liboqs/pull/2269)
9. PQCA support of activities
    - Support for creation of webinar-type content
    - Do we want to have an in-person event supported by PQCA?
10. [OpenSSL conference (October 7–9)](https://openssl-conference.org/): Douglas, Michael, Norm presenting
11. Draft motion: [Voting procedure](https://github.com/open-quantum-safe/tsc/pull/205)
12. Other business

## 1. Chair's introduction

Douglas welcomes the attendees.

## 2. Approve agenda

The agenda is approved.

## 3. Appoint minute-taker

Douglas volunteers to take minutes.

## 4. Review Action items from previous meeting

- Basil and Douglas to draft some bullet points about liboqs wishlist. Done: see [liboqs wiki page "Contribution wishlist"](https://github.com/open-quantum-safe/liboqs/wiki/Contribution-wishlist)
- Norm and Pravek to draft some bullet points about OQS Provider wishlist after the next provider release. In progress; see [OQS Provider Wish List discussion](https://github.com/open-quantum-safe/oqs-provider/discussions/701)
- Tag issues with "good first issue" and "no math expertise required". No action taken.

## 5. Reports

- PQCA TAC (Norm): PQCA TAC has noted that OQS is categorized as Lab Stage on the Research Projects track. The TAC is doing its annual review of the lifecycle document and doing a retrospective on the year.
  Norm tasked with overall review of PQCA lifecycle documents in TAC. Will facilitate annual review.
- PQ Code Package:
  - Matthias gave a presentation on the PQ Code Package at the OPTIMIST workshop at the CHES conference recently. [Slides available](https://kannwischer.eu/talks/20250914_optimist.pdf).
  - mldsa-native: Still in progress.
  - mlkem-native: Optimized versions coming for RISC-V and PPC.
- PQCA general / Outreach and Education committee (Hart): Hart will be in touch with Basil about legal issues regarding the SQIsign pull request.

## 6. PR review procedure for liboqs

Discussion to allow PRs in liboqs to be merged with a single (hoepfully more thorough) review at the discretion of the maintainers. Any further feedback invited on https://github.com/orgs/open-quantum-safe/discussions/2268.

## 7. Motion: Allow contributions to OQS-OpenSSH using upstream licence

Already passed prior to meeting.

## 8. Generative AI

Christian provides an update on his experiments with Copilot, and notes that there can be helpful contributions coming from that approach.

There is general agreement to allow contributions generated using AI, as long as that information is fully disclosed e.g. via the issue & PR templates.

## 9. PQCA support of activities

Douglas mentions that we can propose to PQCA activities that we would like to see supported.

We could consider a meet-up co-located with another event that many of us expect to attend.

Observations: hard to run a solo event. Easier when colocated with a research or customer event. Key question is ensuring we have critical mass.

RWPQC might be an option, but is in Taipei in 2026 so maybe not as many people will be travelling there. Douglas suggests something associated to Eurocrypt 2026 in Rome.

To be revisited at a future meeting.

## 10. OpenSSL conference (October 7–9)

For information: Douglas (remotely), Michael, Norm presenting.

## 11. Draft motion: Voting procedure

Discussion going on regarding a clause to avoid deadlock.

Norm suggests language explicitly indicating that people can abstain.

ACTION: Add language to explicitly indicating that people can abstain.

## 12. Other business

None.
