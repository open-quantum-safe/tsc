# 2024-08-27 - OQS status meeting - minutes

## Next meetings:

- Tuesday September 3, 2024, at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom
- Tuesday September 10, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom

## Attendees

- Alex B, Basil, Max, Nigel (IBM)
- Andrés
- Alex H, Mark, Norm (Cisco)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- Gerardo (AWS)
- Jason (SandboxAQ)
- Michael
- Vlad (softwareQ)
- Yarkin (Nvidia)

## Agenda

1. [liboqs 0.11.0 release planning](https://github.com/open-quantum-safe/liboqs/milestone/25)
2. TSC meeting: Tuesday September 10, 4pm Central European / 10am US Eastern / 7am US Pacific
3. Status updates
4. [Checking in on CI status and stability](https://github.com/open-quantum-safe/liboqs/pull/1745#issuecomment-2303989757)

## 1. [liboqs 0.11.0 release planning](https://github.com/open-quantum-safe/liboqs/milestone/25)

### [Ubuntu upgrade](https://github.com/open-quantum-safe/liboqs/issues/1780)

Spencer has an [open PR in ci-containers](https://github.com/open-quantum-safe/ci-containers/pull/85) to update the Ubuntu CI images and will create a draft PR shortly in liboqs using the new images.
Michael requests that the draft PR be created by tomorrow to allow time to review before travelling.

### [ML-KEM update](https://github.com/open-quantum-safe/liboqs/pull/1899)

Basil's PR is ready to go; it includes checks against NIST-provided test vectors.
Code 
What to do about the "IPD" version of ML-KEM?
Spencer notes that an industry contact is only supporting IPD for interop with liboqs.
Per Gerardo, AWS is removing IPD now that the final version is available.
By consensus, IPD support will be dropped in 0.11.0.

### [CROSS](https://github.com/open-quantum-safe/liboqs/pull/1881)

Spencer asks how closely the algorithm source code should be reviewed.
Douglas, Michael, Basil: no deep cryptographic analysis required.
Michael voices support for including CROSS in the next release.
Douglas asks for a second pair of eyes on the PR over the next few days.

### Release candidate

With the above issues addressed, Douglas thinks we can cut a release candidate next week.
Michael asks that the extended constant-time tests be run in advance of the release so that issues do not have to be dealt with at the last minute.

## 2. TSC meeting

Scheduled for Tuesday September 10, 4pm Central European / 10am US Eastern / 7am US Pacific.

Douglas leaves to catch the bus; Michael takes over as MC.

## 3. Status updates

### OQS TSC

Spencer has created [a PR](https://github.com/open-quantum-safe/tsc/pull/71) to grant himself write access to push meeting minutes.
Michael to approve.

### liboqs

Pravek asks about CI coverage and refactoring, specifically regarding the usage of GitHub matrices.
Spencer hopes to address this as a follow-up to the Ubuntu CI update, probably after the release.
Michael suggests clearly documenting our CI test coverage.
Spencer to take notes on CI while doing the update.

Also on the topic of CI, Michael additionally suggests that the team agree to not override the [CI workflow linting](https://github.com/open-quantum-safe/liboqs/pull/1880) check which is under development.
Pravek suggests updating documentation to this effect.

### OpenSSL 3 Provider

The [CROSS integration](https://github.com/open-quantum-safe/oqs-provider/pull/461) is looking good here pending merge into liboqs.

Norm asks about support in provider for the final version of ML-KEM.
No naming update is required, only new OIDs and codepoints.
Discussion of updating hybrid KEMs to use ML-KEM over Kyber (particularly regarding algorithm order) is deferred until Douglas is available.

### BoringSSL

New features include hybrid signatures and GitHub Actions CI (moved from CircleCI).

### OpenSSH

Gerardo to cut a release this week before going on vacation.
Damien Miller has made a branch upstream to support interop testing with ML-KEM, which currently fails to liboqs still using the IPD version.
Gerardo will try to follow the existing release documentation and will update it if things fail.
Michael asks about future support for OpenSSH; Gerardo is unsure about his post-vacation priorities.

### OQS-Demos

Michael has [an open PR](https://github.com/open-quantum-safe/oqs-demos/pull/296) to upgrade a package, requests reviews.

### Profiling

Michael asks about plans for this project.
Spencer will probably get to it after the liboqs CI refactor is done.

### CI containers

No updates beyond what was already mentioned.

### Language wrappers

Vlad has been cleaning up some open issues.

### Website

No updates.

## 4. CI status and stability

Already discussed.

## Closing Notes

Michael has observed that a number of issues and discussions are going unanswered. 
Michael suggests that participating in these questions and bug reports would not only help the people reporting them but also be a good way to get one's feet wet with the project.
