# 2025-02-04 - OQS status meeting - minutes

## Next meetings

- Tuesday, February 11, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday, February 18, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Basil (IBM)
- Christian (Microsoft)
- Mark, Norm (Cisco)
- Hart (LF)
- JP (QRL)
- Douglas, Pravek, Spencer (Waterloo)
- Vlad (softwareQ)
- Yarkin (NVIDIA)

## Agenda

1. Status updates

## 1. Status updates

### OQS Technical Steering Committee

The [security response process](https://github.com/open-quantum-safe/tsc/pull/124) has been marked as ready for review and is awaiting approval.
Input/approval is requested from the security response team and Vlad (as a maintainer of some of the included subprojects).

### liboqs

Basil to merge the [mlkem-native integration PR](https://github.com/open-quantum-safe/liboqs/pull/2041) now that it has two approvals.
This implementation has the additional key checks from FIPS 203.
[liboqs PR #2009](https://github.com/open-quantum-safe/liboqs/pull/2041) to add key checks in tests is stil relevant, both to check the new CUDA implementation of ML-KEM and to test the checks in the mlkem-native implementation.
Douglas to tag Yarkin on #2009 to see if integration with CUDA code/wrappers is needed.

The [threat model PR](https://github.com/open-quantum-safe/liboqs/pull/2033) has been updated and is close to being ready for merge.

Pravek is working on the cuPQC CI build failure; he believes that it's an issue with [environment variables in the CI setup](https://github.com/open-quantum-safe/ci-containers/blob/656ab3b2bcc6539f1bf8622eecd3378ec072436c/ubuntu-latest/Dockerfile#L92).

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

Vlad asks for feedback on when to print a warning that a language wrapper version is out of sync with the installed liboqs version.
Consensus is to check the minor version only and ignore the patch.

Spencer has released a new version of liboqs-rust, which was prepared by an external contributor.

## PQCA Updates (Hart)

A PQCA governing board position, the Technical Community Representative, is open for nomination.

The Linux Foundation mentorship program provides stipends for mentees to work with a mentor on a project over the course of about three months.
PQCA can support up to five positions, and most are expected to go to OQS.
Project proposals from potential mentors would be required.
Douglas expresses a desire for mentors to come from industry, as Waterloo already has a similar program.
