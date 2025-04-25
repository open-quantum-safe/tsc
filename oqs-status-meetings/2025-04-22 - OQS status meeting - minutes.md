# 2025-04-22 - OQS status meeting - minutes

## Next meetings

- Tuesday, April 29, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday, May 6, 2025 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Basil (IBM)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- Vlad (softwareQ)
- Yarkin (NVIDIA)

## Agenda

1. oqs-provider status and release
2. Profiling updates
3. Status updates

## 1. oqs-provider status and release

Some release tests are failing due to configuration issues with UOV and HQC.
Pravek has draft [PR #670](https://github.com/open-quantum-safe/oqs-provider/pull/670) to address this, waiting for CI to clear.
Basil to try building the test server with this branch.

Pravek to investigate which of the ML-KEM hybrids supported in provider are dynamically disabled with OpenSSL 3.5.0.

## 2. Profiling updates

Spencer has been working with a contributor from SandboxAQ / University of Málaga who has been working on revamping the profiling project.
He is combining some of the existing OQS profiling scripts with a GitHub Actions setup similar to that used by PQ Code Package for benchmarking.
Spencer showcased the [work to date](https://github.com/pablo-gf/liboqs/tree/bench) on the call and asked for feedback.

Do we want to prioritize presentation before publishing or just get data published?
Douglas says that it is better to get data out there sooner, as details around deployment and publication will come up regardless.
It will be important to ensure that the data is well documented.
OK to host it on one or more GitHub Pages for now and link to them from openquantumsafe.org.

## 2. Status updates

### OQS Technical Steering Committee

Norm has officially been added as a maintainer for oqs-provider.

Spencer asks for review on a PR to update his own permissions as a liboqs maintainer.

### liboqs

The 0.13.0 release is out!

The SNOVA PR is ready for final review and is passing all CI.

Aiden, a past contributor to liboqs, is reviving some work on code coverage.

Basil shares that some IBM colleagues will be submitting a PR with optimized common code for PowerPC.

### oqs-provider

No further updates.

### BoringSSL

No updates.

### OpenSSH

No updates.

### Demos

Douglas to review a PR that bumps versions.

### Profiling

No updates.

### Language wrappers

Vlad is reviewing [liboqs-python PR #94](https://github.com/open-quantum-safe/liboqs-python/pull/94).
It seems like it might be better suited for the OQS Demos repository.

## Closing business

There will be a TSC meeting at 12:30 Eastern Time next week.
