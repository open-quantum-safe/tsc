# 2024-11-05 - OQS status meeting - minutes

## Next meetings:

- Tuesday November 12, 2024 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday November 19, 2024 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Alex B, Basil (IBM)
- Mark (Cisco)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- Elizabeth (AT&T)
- JP (QRL)
- Michael (independent)
- Sara (Synopsys)
- Yarkin (NVIDIA)

## Agenda

1. Status updates

## 1. Status updates

### OQS Technical Steering Committee

The TSC met earlier today. Among the agenda items were
- selecting a new OQS representative to the PQCA TAC (a vote is underway to appoint Spencer)
- handling security issues (five people volunteered to be on a security response team)

The TSC will now be meeting every five weeks in the unused OQS status meeting time.

### liboqs

Pravek participated in the IETF Hackathon this past weekend.
He shares that OQS is falling behind other providers there with regards to support for new standards (ML-DSA and SLH-DSA) and composite signatures.
Pravek suggests that we prioritize work on SLH-DSA.
Douglas highlights the need for a "champion" for the SLH-DSA effort.
Spencer suggests that the underlying algorithm might not need to change per the [appendix of FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf#appendix.A).

Basil is looking for feedback on the sign with context string API in the ML-DSA PR [#1919](https://github.com/open-quantum-safe/liboqs/pull/1919).
He needs to add a test for this API and then will mark it ready for review.
It will be missing NIST test vectors for the external API, but these are pending release.

PR [#1959](https://github.com/open-quantum-safe/liboqs/pull/1959) added a function to the public API.
No version update is required, although the SOVERSION will need to be bumped at release time.

### OpenSSL 3 Provider

The next release will include updated IANA codepoints.
More discussion next week as to timing of this release and the next liboqs release.
 
### BoringSSL

No updates.

### OpenSSH

No updates.

### OQS Demos

Alex requests final review on [PR #298](https://github.com/open-quantum-safe/oqs-demos/pull/298) and will be moving on to working on GitHub Actions.
CI is failing both due to access permissions on forks and DCO.
Michael to pull Alex's branch into the OQS repo to fix the permissions issue.
Alex to squash commits immediately before merge to fix the DCO issue.

### Profiling

Spencer and others are meeting with ATIS later today.

The Locust demo contributor has shared some thoughts on profiling in [discussion #112](https://github.com/open-quantum-safe/profiling/discussions/112).

### Language wrappers

No updates.
