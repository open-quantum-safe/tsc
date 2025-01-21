# 2025-01-21 - OQS status meeting - minutes

## Next meetings

- Tuesday, January 28, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday, February 4, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Basil (IBM)
- Douglas, Spencer (Waterloo)
- Hart (Linux Foundation)
- Mark (Cisco)
- Morgan
- Sara (Synopsys)
- Vlad (softwareQ)
- Yarkin (NVIDIA)

## Agenda

1. Status updates

## 1. Status updates

### OQS Technical Steering Committee

Ongoing discussion on [security response process](https://github.com/open-quantum-safe/tsc/pull/124).
Spencer is working to update the doc to reflect consensus in open comment threads.

### liboqs

The [NVIDIA cuPQC integration PR](https://github.com/open-quantum-safe/liboqs/pull/2044) is up for review.
Pravek is looking at a CI build.

A [draft PR](https://github.com/open-quantum-safe/liboqs/pull/2041) to source ML-KEM from the PQ Code Package is up.
Basil is working through some TODOs before marking as ready for review.

### OpenSSL 3 Provider

No updates.

### BoringSSL

Recently updated to sync with the upstream and update a hybrid name/OID.
Douglas to ask about plans for a snapshot release.

### OpenSSH

No updates.

### OQS Demos

No updates.

### Profiling

No updates.

### CI containers

No updates.

### Language wrappers

The C++, Python, and Go wrappers have all been updated to support the new signature API and released.
Vlad is working through some open issues on liboqs-python, including one involving pip packaging.

Spencer to release liboqs-java.

### www.openquantumsafe.org

No updates.

## Closing notes

Discussion is encouraged on the [liboqs threat model](https://github.com/open-quantum-safe/liboqs/pull/2033).
