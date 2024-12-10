# 2024-12-10 - OQS status meeting - minutes

## Next meetings:

- Tuesday, December 17, 2024 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday, January 7, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Alex B, Basil, Nigel (IBM)
- Alex H, Mark, Norm (Cisco)
- Douglas, Pravek, Spencer (Waterloo)
- JP (QRL)
- Michael (independent)
- Vlad (softwareQ)
- Yarkin (NVIDIA)

## Agenda

1. Status updates
  - including discussion of releases of downstream projects

## 1. Status updates

### OQS Technical Steering Committee

TSC meeting today at unused OQS status meeting time (12:30 Eastern).

### liboqs

The 0.12.0 release is done and Douglas has merged some work that had been pending.
We can now drop Kyber support.
A number of downstreams need to be updated first as they rely on Kyber being available.

HQC security advisory and patch released, Spencer submitting patch upstream to PQClean.

### OpenSSL 3 Provider

OpenSSL is using oqs-provider to test their implementation of dTLS 1.3; everything is working so far.
There is an open PR ([#586](https://github.com/open-quantum-safe/oqs-provider/pull/586)) for dTLS 1.3 support in oqs-provider.

ML-DSA interop with other providers (from the IETF hackathon) is inconsistent.
Pravek is investigating the failing ones, Basil to help.
Pravek to open issue for discussion and to share results.
Interop with BouncyCastle is working, which is the most significant one.
Since interop with BouncyCastle is working, the failures will not block the release.

An external contributor has opened a PR to add an SBOM entry to oqs-provider.
They may do the same for liboqs.

### BoringSSL

Douglas to ping @pi-314159 about updating to liboqs 0.12.0.
 
### OpenSSH

Anyone interested in working with the OpenSSH fork is welcome to update it to liboqs 0.12.0.

Michael notes that somebody had asked on GitHub about using OpenSSL / oqs-provider in OpenSSH.
This approach may be a way to streamline the fork and/or contribute back to the upstream.

### OQS Demos

Alex's work is progressing with Michael's input; more reviewer eyes requested.

### Profiling

No updates.

### CI containers

No updates.

### Language wrappers

Vlad is working on updating language wrappers to include the new context string API.
Entrust has offered to contribute their updates for the new API to liboqs-java.

## NVIDIA update

NVIDIA cuPQC has been released to the public, and a PR for integration with liboqs is coming soon.
Development up to this point has taken place in a private repo.
The integration will enable acceleration of ML-KEM and ML-DSA in liboqs via cuPQC.

## Closing notes

No meetings on December 24 or December 31.
