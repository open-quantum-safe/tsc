# 2025-03-04 - OQS status meeting - minutes

## Next meetings

- Tuesday, March 11, 2025 at 12:30pm US Eastern / 5:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday, March 18, 2025 at 10:00am US Eastern / 3:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Angel Camacho
- Basil (IBM)
- Douglas, Pravek, Spencer (Waterloo)
- Mark, Norm (Cisco)
- Hart (LF)
- JP (QRL)
- Leonardo K Shikida
- Prem (AMD)
- Yarkin (NVIDIA)

## Agenda

1. Status updates
2. liboqs 0.13.0 release planning

## 1. Status updates

### OQS Technical Steering Committee

Meeting later today at 12:30 Eastern.

### liboqs

[PR #2009](https://github.com/open-quantum-safe/liboqs/pull/2009), adding key checks to the ML-KEM tests, has landed.

The [DeriveKeyPair PR](https://github.com/open-quantum-safe/liboqs/pull/2070) is passing tests and ready for review.
Spencer is looking for consensus on the API design.

Basil is working on [updating MAYO](https://github.com/open-quantum-safe/liboqs/issues/2091), PR expected tomorrow.

There is an [open PR](https://github.com/open-quantum-safe/liboqs/pull/2092) to update the mlkem-native implementation.
The update includes a couple of features related to liboqs issues.

There is also [ongoing work](https://github.com/open-quantum-safe/liboqs/issues/2028#issuecomment-2697862072) to integrate the UOV signature scheme.

### OpenSSL 3 Provider

No updates.

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

### Language wrappers

No updates.

## Introductions

Angel is joining the OQS status call for the first time after listening in on the PQCA TAC calls.

## 2. liboqs 0.13.0 release planning

Contributors are invited to pick up issues from the [0.13.0 release milestone](https://github.com/open-quantum-safe/liboqs/milestone/27) or add things that they would like to include.
The MAYO update has been added alongside the CROSS update and the addition of UOV.
