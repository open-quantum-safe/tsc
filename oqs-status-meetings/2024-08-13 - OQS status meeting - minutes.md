# 2024-08-13 - OQS status meeting - minutes

## Next meetings:

- Tuesday August 22, 2024, at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom
- Tuesday August 29, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom

<span style="color: red;">Note that we will be switching the Zoom platform hosted by the Linux Foundation. Meeting links are still being set up, but should appear shortly on the <a href="https://pqca.org/calendar/">PQCA Public Calendar</a>. No LF account is required to be able to join the meetings.</span>

## Attendees

- Alex, Basil, Nigel (IBM)
- Andrés
- Douglas, Pravek, Spencer (Waterloo)
- Gerardo (AWS)
- Hugo (independent)
- Kenny (Linux Foundation)
- Mark, Norm (Cisco)
- Yarkin (Nvidia)

## Agenda

1. Welcomes
2. Status updates

## 1. Welcomes

Wecome to new attendees: Hugo Landau and Kenny Paul.

## 2. Status updates

### OQS TSC

No updates.

### liboqs

**Release of FIPS standards for ML-KEM, ML-DSA, SLH-DSA.** Basil has created issue [#1891](https://github.com/open-quantum-safe/liboqs/issues/1891) to track updating liboqs to the final versions. PQ Crystals is planning to update in the next few weeks and then it will be available to us. Test vectors are available from AVCP but may not yet match the standard. 

**Production-oriented.** Andrés asks about when we plan to remove the language around not being for production use. We will need to [revive that discussion](https://github.com/open-quantum-safe/tsc/issues/1) and establish criteria for that.

**Deterministic keypair API.** Spencer looking for feedback on [#1877](https://github.com/open-quantum-safe/liboqs/pull/1877). 

**CROSS signature scheme.** [Initial PR](https://github.com/open-quantum-safe/liboqs/pull/1881) looks promising. Some CI issues needed to be addressed.

### OpenSSL 3 Provider

Norm starting to run OQS Provider through some internal static analysis tools and is aiming to submit issues arising from that. Spencer offers to help with scripting. Douglas asks if the static analysis tools would have detected [our recent CVE](https://github.com/open-quantum-safe/oqs-provider/security/advisories/GHSA-pqvr-5cr8-v6fx); Norm to try running the tools before/after to check.

### BoringSSL

No updates.

### OpenSSH and libssh

Gerardo would like to land [#161 Implement Hybrid SSH keys](https://github.com/open-quantum-safe/openssh/pull/161) to unblock future work. In a previous meeting Christian said he had some feedback but it hasn't come yet; Gerardo is going to land #161 now but can incorporate any further feedback afterwards. After this there will be PRs coming for hybrid X25519, Streamlined NTRU interop, and more.

### OQS-Demos

There's a [new nginx QUIC demo](https://github.com/open-quantum-safe/oqs-demos/pull/291) under review.

Alex says that discussion within IBM about HAProxy demo being contributed is ongoing.

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
No updates.

**liboqs-rust.**
No updates.

### Website

No updates.
