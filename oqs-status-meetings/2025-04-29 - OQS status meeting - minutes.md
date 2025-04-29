# 2025-04-29 - OQS status meeting - minutes

## Next meetings

- Tuesday, May 6, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday, May 13, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Basil (IBM)
- Douglas, Pravek, Spencer (Waterloo)
- Hart (LF)
- Mark, Norm (Cisco)

## Agenda

1. Status updates
2. oqs-provider release

## 2. Status updates

### OQS Technical Steering Committee

There is a TSC meeting today at 12:30 Eastern Time.

### liboqs

Spencer expects to approve [PR #2109](https://github.com/open-quantum-safe/liboqs/pull/2109) for SNOVA today.
Basil to take a look as well.

A summer student from the University of Waterloo will be starting soon.
They will be working on integrating SLH-DSA into liboqs.

### oqs-provider

Pravek has made [PR #670](https://github.com/open-quantum-safe/oqs-provider/pull/670) to prepare for the 0.9.0 release.
It disables HQC and also disables TLS for some variants of UOV and CROSS due to excessive size.
Basil built the test server from the PR branch today.

Norm is looking at implementing seed handling for ML-KEM, focusing on pre-3.5.0, and asks if we are aiming to include it in this release or a future one.
We will wait for a future release.

[PR #644](https://github.com/open-quantum-safe/oqs-provider/pull/644) for IANA-compliant code point updates is open.
Pravek suggests to leave this and similar work for after the current release cycle.

Pravek to work on a milestone for a future 0.9.0 release.

### BoringSSL

No updates.

### OpenSSH

No updates.

### Demos

No updates.

### Profiling

Spencer shares Pablo's progress, which can be viewed at https://pablo-gf.github.io/liboqs/dev/bench.
Signature data and build information are now included.

### Language wrappers

Spencer has released liboqs-java and will make a liboqs-rust release this week.
Spencer to file a PR to update openquantumsafe.org with these releases.

## Closing business

Douglas will be away for the next couple of weeks.
