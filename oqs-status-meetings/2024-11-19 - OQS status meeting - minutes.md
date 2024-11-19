# 2024-11-19 - OQS status meeting - minutes

## Next meetings:

- Tuesday November 26, 2024 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday December 3, 2024 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Alex B (IBM)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- Hart (LF)
- Jason (Sandbox)
- JP (QRL)
- Mark, Norm (Cisco)
- Massimiliano Pala (OpenCA Labs)
- Yarkin (NVIDIA)

## Agenda

1. [liboqs 0.12.0 release planning](https://github.com/open-quantum-safe/liboqs/milestone/26)
2. Status updates

## 1. [liboqs 0.12.0 release planning](https://github.com/open-quantum-safe/liboqs/milestone/26)

Spencer has reviewed [PR #1919](https://github.com/open-quantum-safe/liboqs/pull/1919) and believes it is nearly ready to go.
More reviews encouraged; Douglas to try to take a look.

PRs [#1877](https://github.com/open-quantum-safe/liboqs/pull/1877) and [#1929](https://github.com/open-quantum-safe/liboqs/pull/1929) not to be included in this release.
Version macros still needed.

Spencer is hoping to include a fix for an HQC bug that is currently on a private fork (reported as a security issue).

Norm has a draft PR fixing [issue #1966](https://github.com/open-quantum-safe/liboqs/issues/1966), which would be nice to have as well.

The plan going forward is to check in on next week's call and subsequently create a release candidate.

## 2. Status updates

### OQS Technical Steering Committee

Recurring meetings have been added to the [PQCA calendar](https://pqca.org/calendar), with the next scheduled for December 10.

### liboqs

The ML-KEM seed format issue ([#1985](https://github.com/open-quantum-safe/liboqs/issues/1985)) is of interest to Cisco.
No consensus yet on a path forward.
Pravek notes that Peter Schwabe had planned to reach out to NIST.
Norm to follow up with Richard Barnes (the creator of issue #1985).

### OpenSSL 3 Provider

Massimiliano expresses an interest in having FIPS 204 in oqs-provider for interoperability testing.
Douglas suggests subscribing to [PR #568](https://github.com/open-quantum-safe/oqs-provider/pull/568) for updates.
 
### OpenSSH

No updates.

### OQS Demos

Alex has made progress on the CI work but will be off during the next couple of weeks.
Alex is unsure about merging [PR #298](https://github.com/open-quantum-safe/oqs-demos/pull/298) and will ping Michael.


### Profiling

No updates.

### Language wrappers

Updates will be needed across the board to support the new signature API.
