# 2025-02-11 - OQS status meeting - minutes

## Next meetings

- Tuesday, February 18, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday, February 25, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Christian (Microsoft)
- Mark, Norm (Cisco)
- Michael (independent)
- Pravek, Spencer (Waterloo)
- Yarkin (NVIDIA)

## Agenda

1. Status updates

## 1. Status updates

### OQS Technical Steering Committee

Michael OK with [security response process](https://github.com/open-quantum-safe/tsc/pull/124) as-is if its scope includes only liboqs, not provider.
Spencer to update the PR accordingly and move toward merge.

There is a TSC meeting next week at 12:30 Eastern Time.

### liboqs

Spencer has [rebased](https://github.com/open-quantum-safe/liboqs/pull/2070) [Eddy's PR #1877](https://github.com/open-quantum-safe/liboqs/pull/1877) to add a "DeriveKeyPair" (i.e., expand from seed) function for ML-KEM.
Need to make design/API decisions around supporting seed format.
Michael suggests determining which standards or standards bodies OQS wants to support.

### OpenSSL 3 Provider

Tomorrow (Feb. 12) OpenSSL should decide which algorithms will land in master.
This will hopefully unblock work on the provider.

### BoringSSL

No updates.

### OpenSSH

Pravek to cut a new release this week.

### OQS Demos

[PR #347](https://github.com/open-quantum-safe/oqs-demos/pull/347) needs to land in order to update the OpenSSL 3 Docker image.
This will resolve an issue reported by Entrust where the image does not support ML-DSA.

### Profiling

No updates.

### CI containers

No updates.

### Language wrappers

No updates.

## Other business

Douglas, Pravek, and Spencer will be at an event next week and will be unable to run the status meeting.
People are still welcome to use the time slot if they would like to meet.
