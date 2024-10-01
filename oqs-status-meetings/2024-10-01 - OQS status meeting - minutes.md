# 2024-10-01 - OQS status meeting - minutes

## Next meetings:

- Tuesday October 8, 2024 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday October 15, 2024 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Alex B, Basil (IBM)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- Hart (LF)
- Jason (Sandbox)
- Mark, Norm (Cisco)
- Prem (AMD)

## Agenda

1. liboqs 0.11.0 release cycle - Provider, demos, ...
2. Status updates

## 1. liboqs 0.11.0 release cycle - Provider, demos, ...

Pravek is aiming to cut a release candidate for oqs-provider by end of week.
[PR #524](https://github.com/open-quantum-safe/oqs-provider/pull/524) needs review/approval before merge.

No action is required for demos, as they are still released from the `main` branches on a rolling basis.

## 2. Status updates

### OQS TSC

[PR #77](https://github.com/open-quantum-safe/tsc/pull/77) to update permissions across OQS subprojects has landed.
Please file an issue or email Douglas or Spencer if you believe your access level is incorrect.

### liboqs

liboqs 0.11.0 was released last week!

No updates on ML-DSA, either in upstream code or regarding test vectors for prehash versions.

Spencer is working with an external contributor on PRs addressing memory management and error handling in common code.

Douglas has made [PR #1943](https://github.com/open-quantum-safe/liboqs/pull/1943) to update the CODEOWNERS file.

### OpenSSL 3 Provider

[PR #524](https://github.com/open-quantum-safe/oqs-provider/pull/524) for keyshare reversal needs review.
There is no automated interop testing for this feature, as Cloudflare has not yet switched on support for ML-KEM.
We will move forward with the PR and add back in the Cloudflare tests when possible.

### BoringSSL

Spencer to cut a release and update the Chromium demo.

### OpenSSH

No updates.

### OQS-Demos

Per feedback from Michael, Alex's PR for Curl will expand to include the other demos as well.

### Profiling

An external user has offered to contribute a benchmarking tool based on Locust in [discussion #113](https://github.com/open-quantum-safe/profiling/discussions/113).

No follow-up yet from ATIS on scheduling a meeting.

### CI containers

No updates.

### Language wrappers

No updates.
