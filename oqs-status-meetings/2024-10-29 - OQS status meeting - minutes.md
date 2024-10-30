# 2024-10-22 - OQS status meeting - minutes

## Next meetings:

- Tuesday November 5, 2024 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday November 12, 2024 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Alex B, Basil, Max, Nigel (IBM)
- Norm (Cisco)
- Christian (Microsoft)
- Douglas, Spencer (Waterloo)
- Hart (LF)
- Jason (Sandbox)
- Thomas (independent)
- Yarkin (NVIDIA)

## Agenda

1. Status updates
2. liboqs security issues

## 1. Status updates

### OQS Technical Steering Committee

The next OQS TSC meeting is scheduled for November 5 at 10:00 AM US Eastern / 4:00 PM Central European time.
A [first draft of the agenda](https://github.com/open-quantum-safe/tsc/blob/07bb0775c9b9dc14e4470859419bbf35a8f7dcad/meetings/2024-11-05/agenda.md) is posted in the tsc repo.
Items on the agenda include appointing the TSC TAC rep, discuss security response process, and setting up a meeting schedule.

Hart shares that LF has been working with OpenSSL folks on issues related to the OpenSSL CLA, with the goal of being able to contribute PQCA code to OpenSSL.
OpenSSL is most interested in C implementations at this point.

### liboqs

Jason mentions that [PR #1963](https://github.com/open-quantum-safe/liboqs/pull/1963), adding a C++ linking test to CI, needs another review.
Pravek and Spencer are meeting with the contributor tomorrow and will see it through then.

Basil's PR to the ML-DSA upstream is still open.
He expects that it will be another week or two before it is merged and the liboqs PR is ready for review.

Norm is waiting for reviews on [PR #1959](https://github.com/open-quantum-safe/liboqs/pull/1959) (OpenSSL-related memory leak) and will take a look at [issue #1966](https://github.com/open-quantum-safe/liboqs/issues/1966) (related to stateful signatures).

### OpenSSL 3 Provider

No updates.
 
### BoringSSL

No updates.

### OpenSSH

No updates.

### OQS Demos

Alex requests feedback on [PR #298](https://github.com/open-quantum-safe/oqs-demos/pull/298), which is now "done?", as well as paths forward.
The epiphany demo needs to be tested on a system that supports X11; Spencer volunteers to help with this.
Jason suggests that the deprecated demos be preserved somehow on GitHub; Alex proposes adding a directory for them in the repository.
This directory will be added in a separate PR.

### Profiling

Spencer is arranging a meeting with ATIS / AT&T, contact him if you are interested in attending.

### Language wrappers

No updates.

## 2. liboqs security issues

A number of security reports had gone unseen due to issues with GitHub configuration.

Basil is looking at a report for a Rowhammer attack on MAYO (although it would affect multiple algorithms).
The response will depend on the liboqs threat model.

Douglas is preparing a response to a report about input size checks, which we consider a non-issue.

Spencer is looking at a report about HQC, which seems to identify a legitimate bug in the reference implementation.

All of these reports indicate a need for a security response process, which will be discussed in the next TSC meeting.

## Closing notes

North America goes through a time change this weekend, so the meeting time will once again shift for Europe next week.
