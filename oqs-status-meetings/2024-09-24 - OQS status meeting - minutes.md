# 2024-09-24 - OQS status meeting - minutes

## Next meetings:

- Tuesday October 1, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom
- Tuesday October 8, 2024 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Alex H, Mark (Cisco)
- Alex B, Max, Nigel (IBM)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- Jason (Sandbox)
- JP (QRL)
- Ken (AGCO Corp)
- Michael (independent)
- Yarkin (NVIDIA)

## Agenda

## Agenda

1. liboqs 0.11.0 release
2. Status updates

## 1. liboqs 0.11.0 release

The [release](https://github.com/open-quantum-safe/liboqs/pull/1925) was held pending interop testing with Google and/or Cloudflare.
Some interop testing has been done manually (see oqs-provider [PR #524](https://github.com/open-quantum-safe/oqs-provider/pull/524)).
Do we want to prepare releases for downstream projects before actually releasing liboqs 0.11.0?
Douglas and Spencer to evaluate and prioritize downstream releases over the next couple of days.
Michael suggests codifying external interop testing as part of the release process.

Pravek to handle the oqs-provider release process.
[CROSS](https://github.com/open-quantum-safe/oqs-provider/pull/461) is a priority for inclusion in an oqs-provider release but requires a permissions fix in the TSC repo to land.
Other PRs for inclusion in a release are [#522](https://github.com/open-quantum-safe/oqs-provider/pull/522) and [#524](https://github.com/open-quantum-safe/oqs-provider/pull/524).
Pravek to add tests for oqs-provider with libjade code.

Douglas solicits input on a PQCA blog post to accompany the 0.11.0 release.
Michael suggests having interop test results which can be pointed to in the post.

## 2. Status updates

### OQS TSC

Spencer to push an update this afternoon [to PR #77](https://github.com/open-quantum-safe/tsc/pull/77) addressing permissions issues.

### liboqs

No further updates.

### OpenSSL 3 Provider

Further external static analysis reports are available in [issue #526](https://github.com/open-quantum-safe/oqs-provider/issues/526).

As an aside, the final Trail of Bits audit report for liboqs is expected this week, pending further work by ToB.

### BoringSSL

Douglas asks if the [ML-KEM / x25519 keyshare reversal issue](https://github.com/open-quantum-safe/oqs-provider/issues/503) has been fixed here.
Spencer believes that it has, since the latest updates to the fork default to Google's implementation of ML-KEM.
Michael points out that this makes it a good candidate for interop testing.
Douglas to ask pi-314159 if the BoringSSL fork is ready for release.

### OpenSSH

Do we want to release a snapshot to accompany liboqs 0.11.0?
Unclear who would handle this.
Douglas to create an issue summarizing what needs to be done for a release.

### OQS-Demos

Alex has [created PR #298](https://github.com/open-quantum-safe/oqs-demos/pull/298) to implement version pinning in the curl demo.
Discussions regarding versioning to continue in [issue #284](https://github.com/open-quantum-safe/oqs-demos/issues/284).

### Language wrappers

Douglas requests that people with interests in specific languages take a look at the wrappers and see if work needs to be done to bring them up to date.
Spencer volunteers to look at Java.
Michael suggests that Python and Rust should be prioritized.
Douglas is emailing someone who is interested in working on the Rust wrapper.
Christian suggests that Entrust might be interested in Java and proposes deprecating the .NET wrapper.

### Profiling

Christian has been in touch with ATIS regarding OQS benchmarking.
Spencer to set up a call with them.
