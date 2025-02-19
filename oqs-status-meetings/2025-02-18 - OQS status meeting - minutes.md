# 2025-02-18 - OQS status meeting – minutes

## Next meeting

- Tuesday, February 25, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Basil (IBM)
- Mark, Norm (Cisco)
- Rafael (Meta)
- Yarkin (Nvidia)

## Agenda
1. Status updates

## 1. Status updates

### OQS Technical Steering Committee

TSC meeting is postponed to Tuesday March 4 at the same time (12:30pm US Eastern time).

### liboqs

First PR for updating PQC-DSS schemes to round 2 received (CROSS).
Basil to update the MAYO code once NIST publishes the round 2 submissions.

Rafael is interested in a new release using the updated ML-KEM implementations and is interested in any performance improvements/regressions.
He welcomes the addition of the arm64 optimized implementation.
Basil notes that the updated generic implementation from PQCP is faster than the previous implementation.
The Intel AVX2 implementation from PQCP is slower than the previous implementation, mainly due to the additional key checks required by FIPS 203 before encaps/decaps.
(up to 5% slower KEM encaps / up to 30% slower KEM decaps).

### OpenSSL 3 Provider

Rafael says that Meta uses their own fork of OpenSSL for integrating PQC. He offers to share their experiences with the integration: will reach out to Michael.
 
### BoringSSL

No updates.

### OpenSSH

No updates.

### OQS Demos

Test server is updated to send HSTS headers no longer for the landing page. It was reported to cause issues because the ports for testing the PQC algorithms use a different root CA than the landing page.

### Profiling

No updates.

### CI containers

No updates.

### Language wrappers

No updates.
