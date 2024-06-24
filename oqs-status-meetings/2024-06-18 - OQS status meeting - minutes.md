# 2024-06-18 - OQS status meeting - minutes

### Next meeting: Tuesday June 25, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

<!-- ### Next meeting: Tuesday June 4, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09) -->

## Attendees

- Alex B, Max, Nigel (IBM)
- Alex H, Mark, Norm (Cisco)
- Christian (MSR)
- Douglas, Pravek, Spencer (Waterloo)
- Gerardo (AWS)
- Jason (SandboxAQ)
- Ry (Linux Foundation)
<!--- JP (Quantum Resistant Ledger)-->
<!--- Michael (independent)-->
<!-- - Sara (Synopsys) -->
- Vlad (softwareQ)
- Yarkin (NVIDIA)

## Agenda

1. Welcomes
1. Status updates

## 1. Welcomes

Welcome to Gerardo Ravago from AWS who is interested in contributing to updating OQS-OpenSSH.

## 2. Status updates

### OQS TSC

Douglas to poll for scheduling a TSC call for next week.

### liboqs

Scorecard: All issues with the scorecard itself seem to have been addressed. Ready for review; Nigel would like to merge.  It's not currently being pushed to the OSSF scorecard repository, this can be done in a later PR.

libjade: On hold as Pravek waiting for Tiago to return from vacation; anticipating being able to finalize this later this month.

XMSS: New paramter sets from Duc. Ready for review; Spencer will review.

There's still the CVE-2024-31510 to deal with.

### OpenSSL 3 Provider

Release of oqs-provider 0.6.1.

### BoringSSL

No updates.

### OpenSSH and libssh

Gerardo asks about what's needed to update OQS-OpenSSH:

- update to latest upstream
- update hybrid key exchange to latest draft
- add support for ML-KEM-ipd and ML-DSA-ipd.

Christian offers some advice from past experience.  

Options for interop: AWS internal transfer tool; wolfSSH; OQS-OpenSSH; OpenSSH itself (Gerardo talking to Damien Miller).

### OQS-Demos

Alex would like to lead an effort to update demos. Would like to set up a call with those interested in updating demos or who have information / opinions about the current demos.  Alex will ping interested parties for a meeting time and then circulate.

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
Vlad unsure how to resovle issue #86.

**liboqs-rust.**
No updates.

### CI Containers

No updates.

### Website

No updates.
