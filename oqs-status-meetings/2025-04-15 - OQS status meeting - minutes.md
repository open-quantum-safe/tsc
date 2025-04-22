# 2025-04-15 - OQS status meeting - minutes

## Next meetings

- Tuesday, April 22, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday, April 29, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Basil (IBM)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- Hart (LF)
- Mark, Norm (Cisco)

## Agenda

1. [liboqs 0.13.0 release](https://github.com/open-quantum-safe/liboqs/pull/2119)
2. Status updates

## 0. ICMC 2025

Pravek and Spencer attended and presented at ICMC 2025 last week.
They had a chance to connect with Brian, Christian, Norm, Mike Ounsworth from Entrust and Nicola from OpenSSL.
Mike expressed a desire for better OQS interoperability for the IETF hackathon, including with HashML-DSA.
Nicola pointed us toward an open-source SLH-DSA implementation for possible integration into liboqs.

## 1. liboqs 0.13.0 release

The release was delayed due to a security flaw in the design of HQC.
The HQC team will fix the issue; for now, HQC has been switched off by default in liboqs.
Would anyone like a new release candidate for further testing?
If not, we will proceed with the 0.13.0 release.

Basil has compiled a version of the test server with the 0.13.0 release candidate and current oqs-provider.
Tests are OK except for a known OpenSSL and/or TLS issue with one of the UOV variants having large message sizes.
Pravek to look into this before the provider release.
Spencer suggests that CROSS might have had a similar issue in the past.

## 2. Status updates

### OQS Technical Steering Committee

Spencer to merge minutes from last meeting at end of day if there are no objections.

### liboqs

No further updates.

### oqs-provider

Norm and Pravek to set up a call to talk about seed handling.

The PR to add Norm as a Committer and Maintainer for oqs-provider needs further review from existing Committers.

### BoringSSL

No updates.

### OpenSSH

Spencer has a PR to disable HQC by default that he will merge at end of day if there are no objections.

### Demos

The NodeJS demo has been merged, including interop testing with OQS cURL.

### Profiling

No updates.

### Language wrappers

No updates.

## Closing business

Douglas to send out an email to the OQS developers list with a link to the OQS user survey.
Please get the word out about the survey.
