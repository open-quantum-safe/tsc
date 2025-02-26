# 2025-02-25 - OQS status meeting - minutes

## Next meetings

- Tuesday, March 4, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday, March 11, 2025 at 12:30pm US Eastern / 5:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Alex, Mark, Norm (Cisco)
- Christian (Microsoft)
- JP (QRL)
- Michael (independent)
- Douglas, Spencer (Waterloo)
- Vlad (softwareQ)
- Yarkin (NVIDIA)

## Agenda

1. Status updates
2. liboqs release planning

## 1. Status updates

### OQS Technical Steering Committee

Meeting next Tuesday, March 4 at 12:30pm Eastern Time.
Douglas to circulate agenda within the next couple of days.

### liboqs

CROSS has recently been updated to version 2.0.

Spencer has an open draft PR (#2070) for [code coverage testing](https://github.com/open-quantum-safe/liboqs/pull/2072) that requires more work.
Part of the remaining work is to determine which subset of the codebase should be built and tested for coverage.

Spencer is also addressing CI failures on [the ML-KEM DeriveKeypair PR](https://github.com/open-quantum-safe/liboqs/pull/2070) and will solicit feedback when it is passing.
One open question to resolve is naming conventions (internal/derand/seed/coins etc).

[PR #2031](https://github.com/open-quantum-safe/liboqs/pull/2031) from an external contributor proposes similar keypair derivation functions for signature schemes.
Douglas to follow up asking for the intended use case.

[PR #2009](https://github.com/open-quantum-safe/liboqs/pull/2009) is pending resolution of comments from Basil.

[PR #2072](https://github.com/open-quantum-safe/liboqs/pull/2072) is a proposal to support a seed format for ML-KEM keys.
Douglas to ask if this is obviated by #2070, including a link to the [draft spec for ML-KEM in HPKE](https://www.ietf.org/archive/id/draft-connolly-cfrg-hpke-mlkem-04.html#name-decapsulation).

[PR #1970](https://github.com/open-quantum-safe/liboqs/pull/1970) for a Nix flake is low priority.
Douglas to comment and see if Aiden, the contributor, plans to resolve outstanding issues on the PR.

Michael has bumped [PR #1934](https://github.com/open-quantum-safe/liboqs/pull/1934) to check on the contributor's plans.

### OpenSSL 3 Provider

oqs-provider once again builds successfully against OpenSSL master with standardized algorithms disabled dynamically.

Michael to look at [PR #644](https://github.com/open-quantum-safe/oqs-provider/pull/644) and close [PR #597](https://github.com/open-quantum-safe/oqs-provider/pull/597).

### BoringSSL

No updates.

### OpenSSH

Alex plans to submit a PR to add final code points for ML-KEM.

### OQS Demos

Spencer to redo the proposed CODEOWNERS file to include only Michael and himself.
This is to ensure that reviews are requested on all new PRs.

### Profiling

No updates.

### CI containers

No updates.

### Language wrappers

Vlad has updated liboqs-python and liboqs-cpp so that a warning will be issued if the language wrapper major or minor version differs from the underlying liboqs major or minor version.
Previously the warning had been raised for any version mismatch.
Vlad isn't aware of a way to do this for liboqs-go.

## 2. liboqs release planning

Douglas has created [a milestone for the 0.13.0 release](https://github.com/open-quantum-safe/liboqs/milestone/27).
Please weigh in on PRs and issues for inclusion.
The aim is to have a release sometime in March.
