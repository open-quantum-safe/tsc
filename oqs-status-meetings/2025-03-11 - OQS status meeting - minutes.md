# 2025-03-11 - OQS status meeting - minutes

## Next meetings

- Tuesday, March 18, 2025 at 10:00am US Eastern / 3:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday, March 25, 2025 at 12:30pm US Eastern / 5:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Alex, Mark (Cisco)
- Douglas, Pravek, Spencer (Waterloo)
- Katarina Amrichova (Siemens Healthineers)
- Matvii Kistaiev (IntellectEU)

## Agenda

1. Status updates
2. liboqs 0.13.0

## Introductions

Welcome to Matvii from IntellectEU and Katarina from Siemens Healthineers, both of whom are joining for the first time.

## News

NIST has announced the end of Round 4. HQC was selected over BIKE and McEliece.

Michael Baentsch, a long-time OQS contributor, is stepping away for at least the next few months due to burnout.
Forward any technical questions for Michael to Douglas, who will address them with Michael in a follow-up email.
Please also feel free to sign [a virtual thank-you card for Michael](https://www.groupgreeting.com/sign/03bfa7c2f2fcfb8).

## 1. Status updates

### OQS Technical Steering Committee

The TSC met last week; meetings have been posted (pending approval).
The security response process document has landed.
Nominations (including self-nominations) are sought for TSC chair and vice-chair.

### liboqs

A MAYO version upgrade, an ML-KEM upstream update, and a brand new UOV integration have landed.

[PR 2070](https://github.com/open-quantum-safe/liboqs/pull/2070) for ML-KEM keypair derivation needs more reviews.
Pravek has followed up with Yarkin on related questions around the cuPQC API and is awaiting a response.

The aim is to cut a release candidate for 0.13.0 next week.

### OpenSSL 3 Provider

Need to grow contributor base (including a new maintainer) due to Michael stepping away.

A PR is needed to get UOV support in the provider.
Douglas to file an issue for this, tagging Basil and/or Mattias as possible implementers.

### BoringSSL

No updates.

### OpenSSH

No updates.

### OQS Demos

An external contributor has opened a PR for a PQ-enabled NodeJS.

Katarina inquires about contributing a PQ-enabled version of the DICOM protocol for medical records.
Douglas suggests opening an issue on OQS demos for discussion about the best path forward.

### Profiling

No updates.

### CI containers

No updates.

### openquantumsafe.org

Douglas to update website to point to new security response process.

### Language wrappers

No updates.
