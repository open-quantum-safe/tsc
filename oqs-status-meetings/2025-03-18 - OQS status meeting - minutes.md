# 2025-03-18 - OQS status meeting - minutes

## Next meetings

- Tuesday, March 25, 2025 at 12:30pm US Eastern / 5:30pm Central European / 9:30am US Pacific on Zoom
- ~~Tuesday, April 1, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom~~
- Tuesday, April 8, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Basil (IBM)
- Douglas, Spencer (Waterloo)
- Hart (LF)
- Mark (Cisco)
- Vlad (softwareQ)

## Agenda

1. PQCA Technical Community Representative
2. PQCA Happy Hour in Sofia, Bulgaria on Tuesday March 25
3. Status updates
4. liboqs 0.13.0

## 1. PQCA Technical Community Representative

Nominations for the PQCA Technical Community Representative are now open.
[An email](https://lists.pqca.org/g/oqs-tsc/message/146) was sent out to the TSC mailing list with more details.
Feel free to reach out to Douglas or Hart with any questions.

## 2. PQCA Happy Hour in Sofia, Bulgaria on Tuesday March 25

PQCA is organizing a happy hour for attendees of Real World Crypto / Real World Post-Quantum Crypto.
Hart to send out an email once the venue and time are determined.

## 3. Status updates

### OQS Technical Steering Committee

The TSC meeting for March 25 will be rescheduled to avoid a conflict with RWC.
Douglas had rescheduled for April 8, but that date conflicts with ICMC.
Douglas to reschedule again for April 1; the OQS status call for that day will be cancelled.

Nominations are sought for the TSC chair and vice-chair.

### liboqs

[PR 2070](https://github.com/open-quantum-safe/liboqs/pull/2070) has three approvals and is ready for merge.
Interest has been expressed in a similar feature for ML-DSA; this will be deferred to future work.

Basil has created [PR 2095](https://github.com/open-quantum-safe/liboqs/pull/2095) for a one-line MAYO documentation fix.

A release candidate for 0.13.0 will be cut in the next couple of days.
Outstanding documentation items may land after the release candidate is created.

### OpenSSL 3 Provider

There are open PRs to update OIDs for new and updated signature algorithms.
Basil and Douglas to take a look.

### BoringSSL

No updates.

### OpenSSH

No updates.

### OQS Demos

No updates.

### Profiling

No updates.

### CI containers

No updates.

### openquantumsafe.org

No updates.

### Language wrappers

Vlad is working through the list of open issues.
Vlad has also been experimenting with the Zig language and may make a liboqs language wrapper for it.

Support for the new deterministic keypair API will need to be added to the language wrappers.
Spencer to handle Java and Rust, Vlad to handle C++, Go, and Python.

## Closing business

Douglas will be away at RWC next week, but the meeting will still run for anyone who wants to talk about OQS.

The [virtual thank-you card](https://www.groupgreeting.com/sign/03bfa7c2f2fcfb8) for Michael is still open and will be sent automatically in two days.
