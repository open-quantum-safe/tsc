# 2025-04-08 - OQS status meeting - minutes

## Next meetings

- Tuesday, April 15, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday, April 22, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday, April 29, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Aditya (Coran Labs)
- Alex H (Cisco)
- Basil (IBM)
- Douglas, Pravek, Spencer (Waterloo)
- Mark (Cisco)
- Yarkin (NVIDIA)

## Agenda

1. [liboqs 0.13.0 release](https://github.com/open-quantum-safe/liboqs/pull/2119)
2. Technical Community Rep election
3. [Trail of Bits report released](https://github.com/trailofbits/publications/blob/master/reviews/2025-04-quantum-open-safe-liboqs-securityreview.pdf)
4. Status updates

## 1. liboqs 0.13.0 release

Any further feedback on the liboqs 0.13.0 release?  No further feedback, so plan is to go ahead.

Edit after meeting: new PR [#2122](https://github.com/open-quantum-safe/liboqs/pull/2122) to include in liboqs 0.13.0 to disable HQC in default build due to security vulnerability in IND-CCA2 security of HQC algorithm.

## 2. Technical Community Rep election

Reminder to eligible voters (OQS TSC members) vote in the election, it ends soon.

## 3. Trail of Bits report released

Trail of Bits has posted the public version of their report on last year's review of liboqs: https://github.com/trailofbits/publications/blob/master/reviews/2025-04-quantum-open-safe-liboqs-securityreview.pdf

## 4. Status updates

### liboqs

SNOVA pull request [#2109](https://github.com/open-quantum-safe/liboqs/pull/2109) is ready for review.

### oqs-provider

There are some fixes that need to made before release, including failures in the UOV handshake. To discuss with Pravek.

### BoringSSL

Review requested on [PR #134](https://github.com/open-quantum-safe/boringssl/pull/134).

### Demos

PR for NodeJS demo has been approved. Spencer would like to see an interop test between NodeJS and liboqs, but it can be a separate PR.

Basil will update the test server once liboqs 0.13.0 is released. It may have to move a new virtual server as the current one is at end-of-life.

### Profiling

Spencer met with a new contributor, Pablo, about updating profiling.

### Language wrappers

Some of these will need to be updated alongside the liboqs 0.13.0 release.
