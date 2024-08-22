# 2024-08-20 - OQS status meeting - minutes

## Next meetings:

- Tuesday August 27, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom
- Tuesday September 3, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom

## Attendees

- Basil, Max, Nigel (IBM)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- Gerardo (AWS)
- Ken (AGCO Corp)
- Mark, Norm (Cisco)
- Prem (AMD)
- Yarkin (NVIDIA)

## Agenda

1. Welcome
2. Status updates
3. Release planning

## 1. Welcome

Welcome to Ken from AGCO Corp, who is attending the status call for the first time.

## 2. Status updates

### OQS TSC

Douglas has sent out a poll to schedule the next TSC meeting: https://www.when2meet.com/?25945661-DWIRz.

### liboqs

**CI failures.**
The libjade PR (#1745) has landed on main.
Pravek observes that it introduced a CI failure due to an invalid configuration file.
Basil notes that Travis CI continues to fail, and his ticket with them is still pending.

**ML-KEM and ML-DSA.**
The upstream for ML-KEM has been updated, as have the NIST test vectors.
Basil is working on pulling the new code into liboqs and checking it against the test vectors; a draft PR is incoming.
For naming the new version of ML-KEM, Basil suggests simply dropping the "-ipd" suffix.
For now, OQS will continue to support the Round 3 version of Kyber, as it is used in TLS hybrid key exchange, and we have a formally verified implementation.
Douglas suggests stating intent in the 0.11.0 release to remove the IPD version of ML-KEM from the library, with the removal to occur in 0.12.0.
Gerardo shares that AWS has intentionally not deployed the IPD version of ML-KEM.
Basil has no updates on ML-DSA.
Norm asks about plans to update the TLS hybrid key exchange draft to use ML-KEM.
Douglas says that updated code points are in the works, and we would update oqs-provider when they arrive.

**Other notes.**
Norm has been running static analysis tools on liboqs and oqs-provider.
A PR to add the CROSS signature scheme (#1881) has one approval and could use more reviews.

### OpenSSL 3 Provider

No updates.

### BoringSSL

No updates.

### OpenSSH and libssh

Gerardo has merged [OpenSSH PR #161](https://github.com/open-quantum-safe/openssh/pull/161) to implement hybrid keys and has another PR ([#165](https://github.com/open-quantum-safe/openssh/pull/165)) up to support the latest algorithms and parameter sets.
CircleCI is failing due to a timeout, Gerardo to tag Spencer to look at moving to GitHub CI.
Gerardo is going on vacation in two weeks and would like to cut a release before then; more updates are on deck.
Gerardo shares that Damien Miller is starting to look at X25519/ML-KEM-768 in the upstream, so eventually we can do interop testing.

### OQS-Demos

No updates.

### Profiling

No updates.

### CI containers

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

## 3. Release planning

The only outstanding issue for a liboqs 0.11.0 release is updating Ubuntu support.
Spencer is working on this.
Depending on timeline, CROSS and/or ML-KEM might make it into 0.11.0.
As per the [roadmap discussion](https://github.com/orgs/open-quantum-safe/discussions/1892), the plan is to release 0.12.0, containing ML-KEM and ML-DSA, on the heels of 0.11.0.
Douglas suggests that an eventual 1.0.0 release should include the NIST standards and remove disclaimers around production use.
Douglas solicits feedback on the roadmap discussion.
Some potential criteria for a 1.0.0 release, including team size and incident response process, are discussed.

## Closing notes

A call with Trail of Bits to review their draft report is occurring directly after this meeting.
Douglas will share results with the team.
Pravek brings up an access control issue related to the new liboqs-cupqc repository.
