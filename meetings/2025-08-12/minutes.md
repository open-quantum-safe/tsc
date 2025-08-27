# OQS Technical Steering Committee meeting – 2025-08-12 – minutes

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

- Alex, Andrew (Cisco)

**Date and time:** Tuesday, August 12, 2025, 16:30-17:30 UTC / 9:30-10:30 US Pacific / 12:30-13:30 US Eastern / 18:30-19:30 Central European

Information about the TSC (members, roles and responsibilities, charter) is available on Github at [https://github.com/open-quantum-safe/tsc](https://github.com/open-quantum-safe/tsc)

## Agenda

1. Chair's introduction
2. Approve agenda
3. Appoint minute-taker
4. Review [action items from previous meeting](https://github.com/open-quantum-safe/tsc/blob/main/meetings/2025-07-08/minutes.md)
    - ACTION: Norm and Pravek to draft some bullet points about OQS Provider wishlist after the next provider release.
    - ACTION: Basil and Douglas to draft some bullet points about liboqs wishlist.
    - ACTION: Hart and Douglas to connect about soliciting contributors based on PQCA membership and responses to the OQS survey.
    - ACTION: Tag issues with "good first issue" and "no math expertise required".
5. Reports
    - PQCA TAC (Norm)
    - PQ Code Package (Pravek)
    - PQCA general / Outreach and Education committee (Hart)
6. [Applying PQCA project lifecycle to OQS](https://github.com/orgs/open-quantum-safe/discussions/2191)
7. AI-generated contributions
    - Do we want to restrict completely? Create issue / PR forms/templates that ask about AI use?
8. Other business


## 1. Chair's introduction

Douglas welcomes the attendees.

## 2. Approve agenda

The agenda is approved.

## 3. Appoint minute-taker

Basil volunteers to take minutes.

## 4. Review Action items from previous meeting

Douglas and Basil identified a wishlist for liboqs. Douglas will upload them to wiki.
Purpose is to have an overview of bigger picture items, should be linked to Github issues.

Norm met Douglas on onboarding to OQS, he is about to document toghether with Pravek for oqs-provider.

Hart and Douglas had a call on a stragegy to solicit more contribution from PQCA corporate members. They will meet with some PQCA corporate members, Hart raising it with other LF members. Status is in progress.

"Good first issue" and "no math expertise required" tag: A few issues are already flagged with "good first issue". Douglas notes that "good first issue" will attract AI-generated content. Michael notes that most issues don't require math expertise.

## 5. Reports
    - PQCA TAC (Norm)
      Norm tasked with overall review of PQCA lifecycle documents in TAC. Will facilitate annual review.
    - PQ Code Package (Pravek)
      No update
    - PQCA general / Outreach and Education committee (Hart)
      No update
    - Mentorships:
      Looking for mentees for two projects, one in PQCP (mldsa-native), one in OQS.
      Douglas mentions the possibility for more mentorships.
      Basil presented the OQS mentorship project focused on improving constant-time detection tooling. The goal is to extend existing tooling to detect issues like Kyberslash and Clangover, with CI integration planned. A mentee has been selected and will begin in September for a 3-month term.

## 6. Applying PQCA project lifecycle to OQS

About deciding where OQS falls in the lifecycle: research/labs or production/growth track.

Douglas: not large enough contributor base for production track.
Michael: Outlined his thoughts in writing. Not enough participation for production track, should continue serving research community.
Christian: Agrees with research track.
Norm: Current state is research/lab track, but welcoming interest to move it to production track.

Douglas will leave discussion open and proposes a vote at the TSC repository.

## 7. AI-generated contributions

Douglas asks how should AI-generated content be handled? Options are: complete restriction, discouraged, disclosure of AI-generation, etc.
LF has no general policy on AI use, up to projects, with DCO it should be currently acceptable.

Points brought in the discussion: 
Trend is in using AI for coding, should be disclosed, but accepted if code is improveed. Might experient himself with using AI for oqs contribution (Christian)
Start with checkbox with disclosure, prefers to defer decision because of license unknowns, not accepting AI contributions in the meanwhile (Norm)
Disclosure is minimum, people should explain contribution, open if contributions improve OQS, but critical with hallucinating AI in security software, should require careful application of AI, if anything goes wrong, contributor is rejected (Michael)
Self-declaration/disclosure should be minimum, there will be various levels of AI use (Basil)

Current minimum consensus: disclosure of (careful) AI application, contributor reviews AI-generated content, ability to explain contributions
