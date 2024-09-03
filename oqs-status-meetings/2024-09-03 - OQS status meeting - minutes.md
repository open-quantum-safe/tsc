# 2024-09-03 - OQS status meeting - minutes

## Next meetings:

- Tuesday September 10, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom
- Tuesday September 17, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom

## Attendees

- Alex, Basil, Nigel (IBM)
- Douglas, Pravek, Spencer (Waterloo)
- JP (QRL)
- Mark, Norm (Cisco)
- Pierre-Elisée Flory (Thales)
- Yarkin (NVIDIA)

## Agenda

1. liboqs 0.11.0 release
2. Status updates
3. [Looking for help on profiling](https://github.com/open-quantum-safe/www/issues/216)

## 1. liboqs 0.11.0 release

The only remaining blocker is the [Ubuntu CI upgrade](https://github.com/open-quantum-safe/liboqs/issues/1780).
Spencer expects to have ths ready for final review and merge by end of day, pending updates to Classic McEliece constant-time suppression files.

The [PR to add the CROSS signature scheme](https://github.com/open-quantum-safe/liboqs/1881) has enough approvals to merge but has merge conflicts with main.
Pravek is waiting for a response from the creator regarding usage of memset to zero out memory.
This is not viewed as a blocker, as memset is used similarly in other places in liboqs.
Pravek to sort out conflicts and add a note on the [existing issue](https://github.com/open-quantum-safe/liboqs/issues/1864) tracking memset usage throughout the codebase.

We will aim to have a 0.11.0 release candidate including these PRs ready by end of week.

## Welcome 
Welcome to first-time attendee Pierre-Élisée Flory from Thales.

## 2. Status updates

### OQS TSC

A TSC meeting will be held at this same time (10:00am US Eastern) on Tuesday, September 10.
Agenda items will include the [liboqs roadmap](https://github.com/orgs/open-quantum-safe/discussions/1892) and organization [permissions management](https://github.com/open-quantum-safe/tsc/issues/10#issuecomment-2314375179)

### liboqs

Per Basil, an upstream update to ML-DSA is coming soon.
NIST test vectors currently test only the internal ML-DSA API but will soon also test the public one.
It may be possible to test the internal ML-DSA API with a similar approach to that used for testing symmetric crypto.
Norm asks about testing these APIs from the provider for ACVP purposes.
More discussion required.

### OpenSSL 3 Provider

Norm has been working through static analysis issues identified by Coverity.
He has been unable to discern if Coverity could have found the recent [buffer overflow security issue](https://github.com/open-quantum-safe/oqs-provider/security/advisories/GHSA-pqvr-5cr8-v6fx), but suspects that it would have.
Norm to create issues and PRs to track and/or fix the issues he finds.

### BoringSSL

No updates.

### OpenSSH

Gerardo recently released a [snapshot](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2024-08) on the OQS-v9 branch.
Douglas to update the website to reference this.

### OQS-Demos

No updates.

### Profiling

Douglas mentions that [help is wanted with revitalizing the project](open-quantum-safe/www/issues/216).

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
