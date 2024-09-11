# 2024-09-10 - OQS status meeting - minutes

## Next meetings:

- Tuesday September 17, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom
- Tuesday September 24, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom

## Attendees

- Alex B, Basil, Max, Nigel (IBM)
- Alex H, Mark, Norm (Cisco)
- Douglas, Pravek, Spencer (Waterloo)
- JP (QRL)
- Michael (independent)
- Yarkin (NVIDIA)

## Agenda

1. liboqs 0.11.0 release planning
2. Status updates

## 1. liboqs 0.11.0 release planning

The remaining blockers (Ubuntu and ML-KEM) from last week have been resolved and merged.
However, ML-DSA final is now available in pq-crystals.
Do we want to hold 0.11.0 and include ML-DSA?

Basil is working on a draft PR for ML-DSA, but raises some points related to integrating the new code:
- The NIST ACVP vectors only test the "internal" API, which is not included upstream, although Gregor (from pq-crystals) has stated an intent to add it;
- NIST intends to publish test vectors against the external API in/around October; and
- We should also consider the "pre-hash" variants of ML-DSA.

The pre-hash variants have their own OIDs.
Basil expects that they will need to be implemented in liboqs as opposed to only in oqs-provider.

Douglas suggests that we wait until development and testing around the ML-DSA APIs stabilizes before releasing it.
Spencer proposes releasing 0.11.0 with ML-KEM (also MAYO and CROSS) and without ML-DSA; Norm voices support.
Douglas and Spencer to discuss cutting a release candidate tomorrow, with the goal of having it available for feedback by end of week.

## 2. Status updates

### OQS TSC

The TSC met earlier today.
Minutes will be circulated.

### liboqs

A major refactor to CI landed yesterday.
Developers are advised to rebase branches / sync forks to sort out conflicts.

There is a substantial backlog of open issues and PRs to go through.

### OpenSSL 3 Provider

Reviews are required on PRs for ML-KEM and CROSS integration.

The [CROSS PR](https://github.com/open-quantum-safe/oqs-provider/pull/461) is pending work on the TSC config.yaml file around codeowners and permissions (see https://github.com/open-quantum-safe/tsc/issues/10).

The [ML-KEM PR](https://github.com/open-quantum-safe/oqs-provider/pull/511) does not include "share reversal" for the x25519 / ML-KEM-768 hybrid (see https://github.com/open-quantum-safe/oqs-provider/issues/503).
Basil to work on that in a separate PR.

Norm has filed issue [#514](https://github.com/open-quantum-safe/oqs-provider/issues/514) to track some static analysis issues.
Also in that issue, Michael has linked to related discussions with LF folks and suggested that there could be room for collaboration.
Norm is using an internal Cisco static analysis pipeline using Coverity.
It's unlikely that this tooling can be shared directly with OQS, but Norm intends to contribute back any fixes.
Douglas notes that in principle we could get Coverity running ourselves as an open-source project.

### BoringSSL

No updates.

### OpenSSH

No updates.

### OQS-Demos

Alex has issues/PRs incoming related to pinning version numbers.
Michael mentions that using a non-pinned master/main has benefits as well.
Alex intends to allow CI to run both.

### Profiling

No updates.

### CI Containers

No updates.

### Language wrappers

**liboqs-cpp.**
No updates.

**liboqs-dotnet.** 
No updates.

**liboqs-go.** 
No updates.

**liboqs-java.**
No updates.

**liboqs-python.** 
No updates.

**liboqs-rust.**
No updates.

### Website

No updates.

## Closing notes

There are two upcoming PQCA events:
- a TAC meeting happening tomorrow (see PQCA calendar) and
- a get-together at ICMC next week.
