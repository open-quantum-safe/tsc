# 2024-11-12 - OQS status meeting - minutes

## Next meetings:

- Tuesday November 19, 2024 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday November 26, 2024 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Alex B, Nigel (IBM)
- Alex H, Mark, Norm (Cisco)
- Douglas, Pravek, Spencer (Waterloo)
- Hart (LF)
- JP (QRL)
- Michael (independent)
- Yarkin (NVIDIA)

## Agenda

1. 0.12.0 release planning
2. Status updates

## 1. 0.12.0 release planning

ML-DSA would be the main milestone for this release.
A decision needs to be made regarding API changes: add a new function or modify an existing one.

Other features in the [0.12.0 milestone](https://github.com/open-quantum-safe/liboqs/milestone/26) include
- deterministic keygen API ([liboqs PR #1877](https://github.com/open-quantum-safe/liboqs/pull/1877))
- improved error handling
- expanded interop testing.

Also on the table is dropping support for Kyber, up for discussion in [liboqs issue #1989](https://github.com/open-quantum-safe/liboqs/issues/1989).

Related to deterministic keygen is recent discussion around a seed-only format for ML-KEM keys and related API changes.
See [liboqs issue #1985](https://github.com/open-quantum-safe/liboqs/issues/1985) and [PQ Code Package TSC issue #4](https://github.com/pq-code-package/tsc/issues/4).
Some back-and-forth with NIST may be involved before an API is settled on.
Consensus is to let the discussion unfold and not try to include this in 0.12.0.

Some interop testing is already in place in oqs-provider, which may be sufficient for the purpose of testing TLS implementations.

Decision is to focus the 0.12.0 release on ML-DSA, with a target of within two weeks.
Douglas to check with Basil on the feasibility of this timeline.

Leaning toward keeping Kyber in this release and dropping it in 0.13.0, with notice of this in the 0.12.0 release notes.
Similar approach for the oqs-provider update to move codepoints within the proper IANA space.

## 2. Status updates

### liboqs

[PR #1982](https://github.com/open-quantum-safe/liboqs/pull/1982) has two approvals but has not yet been merged.

### OpenSSL 3 Provider

It seems like confusion from packagers around the 0.7.0 / 0.7.1-dev version mixup has been sorted out.
There is no plan to do a release until the next liboqs release.
 
### BoringSSL

No updates.

### OpenSSH

No updates.

### OQS Demos

Alex is squashing commits and addressing review feedback on [PR #298](https://github.com/open-quantum-safe/oqs-demos/pull/298).
Hoping to merge in the next couple of days.
Next up is CI work.

### Profiling

Pravek, Christian, and Spencer met with ATIS last week.
It seems like their benchmarking tool is in a similar position to profiling, developed but not maintained.
Awaiting further information from them, including a demo video.

### Language wrappers

No updates.
