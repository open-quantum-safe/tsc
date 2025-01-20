# 2025-01-14 - OQS status meeting - minutes

## Next meetings

- Tuesday, January 21, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday, January 28, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Agenda

1. Status updates

## 1. Status updates

### OQS Technical Steering Committee

Ongoing discussions on [security response process](https://github.com/open-quantum-safe/tsc/pull/124) and [subproject support level](https://github.com/open-quantum-safe/tsc/issues/2).

### liboqs

A PR from NVIDIA to support implementations from their cuPQC library is up for review.

A recent bug report highlights that liboqs is not using OpenSSL allocation functions as expected.
Consensus is that there is no good way to add automated testing for this, at least not without significant effort.
Spencer will wait a couple of days before patching to allow the bug reporter to submit a PR if they wish.

Discussion ongoing (and solicited) on a proposed [liboqs threat model](https://github.com/open-quantum-safe/liboqs/pull/2033).

### OpenSSL 3 Provider

oqs-provider is currently incompatible with OpenSSL master branch due to recent OpenSSL work on integrating standardized PQC algorithms.
For background, see issues [#621](https://github.com/open-quantum-safe/oqs-provider/issues/621) and [#623](https://github.com/open-quantum-safe/oqs-provider/issues/623).
One solution would be to drop support for standardized algorithms: see [discussion #610](https://github.com/open-quantum-safe/oqs-provider/discussions/610).
Michael requests input and suggestions on possible approaches.

Norm mentions provider-related bugs that arise when using liboqs with OpenSSL >= 3.3 and FIPS provider 3.0.
liboqs uses SHA3 API calls that are only supported in newer versions of OpenSSL without checking which provider it is using.
Norm to file an issue and investigate a fix.

### BoringSSL

No updates.

### OpenSSH

No updates.

### OQS Demos

There is an open PR to update Dockerfiles.
Michael to respond to the author.

### Profiling

No updates.

### CI containers

No updates.

### Language wrappers

Vlad has released the C++ wrapper; Python and Go are up next.

John Gray from Entrust contributed a PR to update the Java wrapper.
Spencer to update the README and cut a release.

### www.openquantumsafe.org

No updates.
