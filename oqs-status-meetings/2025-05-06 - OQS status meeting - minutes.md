# 2025-05-06 - OQS status meeting - minutes

## Next meeting

- Tuesday, May 13, 2025 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Alex, Mark, Norman (Cisco)
- Spencer, Pravek, Hayden (Waterloo)
- Christian (Microsoft)
- Basil (IBM)

## Agenda

Status updates

### OQS Technical Steering Committee

TSC meeting took place last week. PR with minutes waiting for approval: https://github.com/open-quantum-safe/tsc/pull/177

### liboqs

SNOVA implementation landed. Next step is the provider integration.

### oqs-provider

Pravek has PRs https://github.com/open-quantum-safe/oqs-provider/pull/671 and https://github.com/open-quantum-safe/oqs-provider/pull/676 open towards a 0.9.0 release.

### BoringSSL

No updates.

### OpenSSH

PR from Alex https://github.com/open-quantum-safe/openssh/pull/176, which includes finalized code points for ML-KEM. Spencer plans to cut snapshot release.

### Demos

No updates.

### Profiling

Spencer shares that Pablo made a PR for the new profiling: https://github.com/open-quantum-safe/liboqs/pull/2134.
Another contribution is upcoming for benchmarking visualizations, which is integratable with the OQS Website.
Christian says it will be useful for the NIST NCCoE report.

### Language wrappers

Spencer has released liboqs-rust, based on liboqs 0.13.0.


## Closing business

Introducing and welcoming Hayden, summer student at University of Waterloo, working on SLH-DSA. The implementation will be based on M. Saarinen's implementaion sloth: https://github.com/slh-dsa/sloth
