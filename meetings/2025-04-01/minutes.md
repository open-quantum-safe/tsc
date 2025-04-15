# OQS Technical Steering Committee meeting – 2025-04-01 – minutes

## Attendees

TSC members

- [x] [Norman Ashley (Cisco)](https://github.com/ashman-p)
- [ ] [Michael Baentsch (independent contributor)](https://github.com/baentsch)
- [ ] [Thomas Bailleux (independent contributor)](https://github.com/zadlg)
- [ ] [Vlad Gheorghiu (softwareQ Inc.)](https://github.com/vsoftco)
- [x] [Basil Hess (IBM Research)](https://github.com/bhess)
- [x] [Christian Paquin (Microsoft Research)](https://github.com/christianpaquin)
- [x] [Douglas Stebila (University of Waterloo)](https://github.com/dstebila)
- [x] [Spencer Wilson (University of Waterloo)](https://github.com/SWilson4)

Other attendees
- Balaji Ethirajulu
- Hart Montgomery
- JP Lomas
- Pablo Gutiérrez
- Pravek Sharma

## Agenda

1. Chair's introduction
2. Approve agenda
3. Appoint minute-taker
4. Review action items from previous meeting
    - Trial run of security response process
5. Reports
	- PQCA TAC (Spencer)
	- PQ Code Package (Pravek)
6. [Appointment of new TSC chair](https://github.com/open-quantum-safe/tsc/issues/151)
7. Election of Technical Community Rep to PQCA Governing Board
8. Additional maintainers in liboqs and oqs-provider
9. Other business

## 1. Chair's introduction

Douglas welcomes the attendees and thanks them for accommodating the meeting change due to Real World Crypto last week.

## 2. Approve agenda

The agenda is approved.

## 3. Appoint minute-taker

Spencer volunteers to take minutes.

## 4. Review action items from previous meeting

### Trial run of security response process

There is an outstanding low-level security issue related to clearing seeds that can be used for a trial run.
Douglas to review the response process and send out an email to kick it off.

## 5. Reports

### PQCA TAC (Spencer)

Brian Jarvis has been elected as the new TAC chair.
The vice chair election process is ongoing, with Aditya Koranga from Coran Labs as the only nominee.

The election process for the Technical Community Representative (TCR) to the Governing Board is also ongoing, with Matthias Kannwischer as the only nominee.
TSC members will vote on this.

The year-in-review blog draft is completed and will be distributed for review.

The TAC will be holding a retrospective meeting later this month.
TSC members are encouraged to attend and provide feedback or send Spencer feedback to raise at the meeting.
Spencer will let the TSC know when the retrospective is scheduled.

### PQ Code Package (Pravek)

The upcoming liboqs 0.13.0 release will be the first one with mlkem-native.
The mlkem-native code will also be integrated into Amazon's aws-lc library.

libjade has finished formal verification of their portable C and AVX2 ML-KEM implementations.
These implementations will be exported into PQCP.

Work is ongoing on the mldsa-native implementation.

### Outreach committee

Douglas suggests that the outreach committee should also provide updates.
Hart offers to provide updates going forward.

## 6. [Appointment of new TSC chair](https://github.com/open-quantum-safe/tsc/issues/151)

Douglas would like to somebody to step up either as TSC chair or liboqs maintainer.
Responsibility could be divided between co-chairs or chair and vice chair.

Norm asks about the term and suggests that people might not want to feel stuck in the position.
Douglas suggests a one-year term, and that a new vice chair could potentially ease into a larger role.

Basil (the current vice chair) is unsure if he can effectively fill the chair role this year and does not wish to be a candidate.

Douglas to do some canvassing privately after the meeting.

## 7. Election of Technical Community Rep to PQCA Governing Board

As mentioned before, there is one nominee, Matthias Kannwischer.
TSC members should be able to vote in their [Linux Foundation portal](https://openprofile.dev).

## 8. Additional maintainers in liboqs and oqs-provider

With Michael stepping away, there are no active mainters for oqs-provider and only one (Douglas) for liboqs.

Somebody is needed to step up for oqs-provider, and it would be good to have more leadership for liboqs.
Reach out to Douglas initially; the formal process will be via PR to the appropriate GOVERNANCE file.

Spencer volunteers to step up as liboqs maintainer; Douglas and Spencer to discuss in a meeting tomorrow.

## 9. Other business

The [liboqs 0.13.0 release candidate](https://github.com/open-quantum-safe/liboqs/pull/2107) is up for review.
Douglas asks everyone take a look and wrap up loose ends over the next day or so.

The regular schedule of OQS status meetings will resume next Tuesday.
The next TSC meeting will be Tuesday, April 29, at 12:30 Eastern Time.

## Meeting recording

https://zoom.us/rec/play/9G8p_ohLn-CpbqiYgPbhYdtHSWlz49Y_Ifl1AVXtmidPbcpDIJBwr2ThpJln35fV0pi1MDdoJLO0x9-j.9-wsnABt1JvWCV0K
