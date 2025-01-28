# 2025-01-28 - OQS status meeting - minutes

## Next meetings

- Tuesday, February 4, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday, February 11, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Alex, Mark, Norm (Cisco)
- Basil, Nigel (IBM)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- JP (QRL)
- Ken (AGCO Corp)
- Michael (independent)
- Steve Derezinski
- Vlad (softwareQ)

## Agenda

1. Status updates

## 1. Status updates

### OQS Technical Steering Committee

[Proposed security response process](https://github.com/open-quantum-safe/tsc/pull/124) updated to include subproject scope and a time-based rotation of duty.
Feedback solicited, Spencer to move to "Ready for Review."

### liboqs

The NVIDIA cuPQC integration has landed.
Pravek is fixing a related CI failure due to a recent container update.

Basil has reviewed and approved a [PR to update ACVP vectors](https://github.com/open-quantum-safe/liboqs/pull/2051).
This adds tests for the ML-DSA external API.
One more review is required.

There has been discussion around performance tradeoffs due to input validation in the [ML-KEM from PQCP PR](https://github.com/open-quantum-safe/liboqs/pull/2041).
It seems that there is no way to eliminate redundant validations with the current OQS architecture.
A rebase and one more review are required before merge.

We have received a [report](https://github.com/open-quantum-safe/liboqs/issues/2047) of a significant performance degradation in HQC.
Michael to review noregress script.
Spencer to investigate HQC specifics further.

### OpenSSL 3 Provider

oqs-provider is still incompatible with OpenSSL master due to the merge in OpenSSL of OIDs for standardized PQC algorithms.
Michael plans to hold off on fixing this until OpenSSL PQC implementation feature branches are merged, in order to reduce duplicated effort.
OpenSSL's decision date for the feature branches is February 11.
Input solicited on [Michael's proposed design for a solution](https://github.com/open-quantum-safe/oqs-provider/discussions/625).

### BoringSSL

There is a new snapshot release available.

### OpenSSH

No updates.

### OQS Demos

No updates.

### Profiling

No updates.

### CI containers

The size of the OQS Ubuntu CI image has grown significantly after recent merges, leading to longer runtimes for lightweight tests.
Pravek is working on this alongside cuPQC-related changes.

### Language wrappers

Feedback is solicited on the security support status of language wrappers in the [proposed security response process](https://github.com/open-quantum-safe/tsc/pull/124).

#### liboqs-python
Vlad is reviewing a contribution for liboqs-python with a number of general improvements.

#### liboqs-go
There is confusion around a recent [liboqs-go issue](https://github.com/open-quantum-safe/liboqs-go/issues/46) that refers to "PQCrypto."
More information is required from the reporter.

#### liboqs-java
There is a new release of liboqs-java, which brings it up to date with liboqs and adds CI for Ubuntu 24 and macOS.

#### liboqs-rust
Spencer to review a recent PR [related to OpenSSL use in the build process](https://github.com/open-quantum-safe/liboqs-rust/pull/275).
