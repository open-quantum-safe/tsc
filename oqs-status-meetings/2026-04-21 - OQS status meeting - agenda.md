# 2026-04-21 - OQS status meeting - agenda

<span style="color: red;"> Tuesday April 21 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates & items seeking help
2. liboqs 0.16.0 release progress

## OQS subprojects

1. OQS Technical Steering Committee
2. liboqs
3. OQS-OpenSSL 3 provider
4. OQS-OpenSSH
5. OQS-BoringSSL
6. oqs-demos
7. ci-containers
8. www.openquantumsafe.org
9. liboqs language wrappers: liboqs-C++, liboqs-Go, liboqs-Java, liboqs-js, liboqs-Python, liboqs-Rust


## Project board: [0.16.0 prioritization](https://github.com/orgs/open-quantum-safe/projects/11)

**In progress**
- [Issue 2118](https://github.com/open-quantum-safe/liboqs/issues/2118): Update HQC implementation to 2025/02/19 version (liboqs)
- [Issue 2404](https://github.com/open-quantum-safe/liboqs/issues/2404): Update GOVERNANCE.md file and codeownwers for algorithms (liboqs)
- [PR 2407](https://github.com/open-quantum-safe/liboqs/pull/2407): Update HQC implementation to 2025-08-22 version (liboqs)

**Ready**
- [Issue 2045](https://github.com/open-quantum-safe/liboqs/issues/2045): Create a table of algorithm support levels (liboqs)
- [Issue 2405](https://github.com/open-quantum-safe/liboqs/issues/2405): Mention FrodoKEM algorithm change in 0.16.0 release notes (liboqs)

**In review**
- [PR 2361](https://github.com/open-quantum-safe/liboqs/pull/2361): Add MQOM (liboqs)
- [PR 2384](https://github.com/open-quantum-safe/liboqs/pull/2384): Fix Reading beyond buffer end (liboqs)



## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **[OQS Technical Steering Committee](https://github.com/open-quantum-safe/tsc)**


	- Issues with activity in the last 7 days:
		 - [Issue 246](https://github.com/open-quantum-safe/tsc/issues/246): New TSC chair
		 - [Issue 216](https://github.com/open-quantum-safe/tsc/issues/216): Project health and maturity metrics
	- Merges in the last 7 days:
		 - [PR 268](https://github.com/open-quantum-safe/tsc/pull/268): Add agenda for OQS status meeting 2026-04-21
		 - [PR 267](https://github.com/open-quantum-safe/tsc/pull/267): [vote] Add Rodrigo Martín as TSC co-chair / future chair  `vote`
		 - [PR 266](https://github.com/open-quantum-safe/tsc/pull/266): Add minutes from 2026-04-14 status meeting
		 - [PR 265](https://github.com/open-quantum-safe/tsc/pull/265): Add agenda for OQS status meeting 2026-04-14
		 - [PR 264](https://github.com/open-quantum-safe/tsc/pull/264): Add hartm to the security-managers team
	- Open PRs:
		 - [PR 269](https://github.com/open-quantum-safe/tsc/pull/269): Update liboqs permissions


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2409](https://github.com/open-quantum-safe/liboqs/issues/2409): Integer underflow in CROSS crypto\_sign\_open()  `dependencies`
		 - [Issue 2405](https://github.com/open-quantum-safe/liboqs/issues/2405): Mention FrodoKEM algorithm change in 0.16.0 release notes  `documentation`
		 - [Issue 2404](https://github.com/open-quantum-safe/liboqs/issues/2404): Update GOVERNANCE.md file and codeownwers for algorithms
		 - [Issue 2401](https://github.com/open-quantum-safe/liboqs/issues/2401): armhf tests failing (weekly tests)
		 - [Issue 2392](https://github.com/open-quantum-safe/liboqs/issues/2392): MAYO signing function returns `MAYO\_OK` after 256 failed `sample\_solution()` attempts
		 - [Issue 2388](https://github.com/open-quantum-safe/liboqs/issues/2388): Mismatched CUDA symbol names in ML-KEM keypair\_derand and encaps\_derand paths
	- Merges in the last 7 days:
		 - [PR 2408](https://github.com/open-quantum-safe/liboqs/pull/2408): Update pytest package version  `dependencies`
		 - [PR 2406](https://github.com/open-quantum-safe/liboqs/pull/2406): Demote armhf from a Tier 2 to Tier 3 supported platform and remove from weekly CI  `bug`
		 - [PR 2403](https://github.com/open-quantum-safe/liboqs/pull/2403): Pull MAYO update from upstream (fixing issue reported by @programsurf)
		 - [PR 2396](https://github.com/open-quantum-safe/liboqs/pull/2396): fix: correct cuPQC ML-KEM derand symbol names and #if/#elif chains
		 - [PR 2394](https://github.com/open-quantum-safe/liboqs/pull/2394): fix: build on windows clang
		 - [PR 2383](https://github.com/open-quantum-safe/liboqs/pull/2383): Move compiler optimization level to CMAKE\_BUILD\_TYPE  `enhancement` `ready for merge`
	- Open PRs:
		 - [PR 2410](https://github.com/open-quantum-safe/liboqs/pull/2410): [vote] Update GOVERNANCE.md and CODEOWNERS
		 - [PR 2407](https://github.com/open-quantum-safe/liboqs/pull/2407): Update HQC implementation to 2025-08-22 version
		 - [PR 2400](https://github.com/open-quantum-safe/liboqs/pull/2400): tests: add fuzz harness for XMSS stateful signature verification (#2399)
		 - [PR 2397](https://github.com/open-quantum-safe/liboqs/pull/2397): Fix: Limit pytest processes to prevent OOM on low-RAM systems
		 - [PR 2391](https://github.com/open-quantum-safe/liboqs/pull/2391): Update mldsa-native to v1.0.0-beta [full tests] [extended tests]
		 - [PR 2387](https://github.com/open-quantum-safe/liboqs/pull/2387): Adapt/Fix latest Wycheproof tests
		 - [PR 2386](https://github.com/open-quantum-safe/liboqs/pull/2386): Add missing ACVP tests [ML-KEM]
		 - [PR 2384](https://github.com/open-quantum-safe/liboqs/pull/2384): Fix Reading beyond buffer end  `focus`
		 - [PR 2382](https://github.com/open-quantum-safe/liboqs/pull/2382): Add common dependencies with include\_only
		 - [PR 2366](https://github.com/open-quantum-safe/liboqs/pull/2366): Add API support for External-MU Signature[ML-DSA]
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 772](https://github.com/open-quantum-safe/oqs-provider/issues/772): Re-activate HQC by default  `enhancement`
		 - [Issue 770](https://github.com/open-quantum-safe/oqs-provider/issues/770): Which of the following outputs represents the actual key material? How should I extract the keys for the traditional algorithm and the PQC algorithm separately in order to test them individually?  `question`
	- Merges in the last 7 days:
		 - [PR 769](https://github.com/open-quantum-safe/oqs-provider/pull/769): Add capacity to build oqsprovider with SHARED library type
	- Open PRs:
		 - [PR 752](https://github.com/open-quantum-safe/oqs-provider/pull/752): Preserve property string for KEMs.
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- Issues with activity in the last 7 days:
		 - [Issue 392](https://github.com/open-quantum-safe/oqs-demos/issues/392): CI tags not properly aligned  `good first issue` `help wanted`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 323](https://github.com/open-quantum-safe/www/pull/323): Bump \_includes/liboqs from `8f08fd8` to `3cb781f`  `dependencies` `submodules`
	- Open PRs: None


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


11. **[liboqs-Java](https://github.com/open-quantum-safe/liboqs-java)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


12. **[liboqs-js](https://github.com/open-quantum-safe/liboqs-js)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


13. **[liboqs-Python](https://github.com/open-quantum-safe/liboqs-python)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 132](https://github.com/open-quantum-safe/liboqs-python/pull/132): Update liboqs version to 0.15.0.
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline
		 - [PR 119](https://github.com/open-quantum-safe/liboqs-python/pull/119): Version 0.14
		 - [PR 94](https://github.com/open-quantum-safe/liboqs-python/pull/94): replacing openssl111 with openssl3


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 306](https://github.com/open-quantum-safe/liboqs-rust/pull/306): chore(ci): fix targeting
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 299](https://github.com/open-quantum-safe/liboqs-rust/pull/299): feat: add Android CMake configuration patch
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 297](https://github.com/open-quantum-safe/liboqs-rust/pull/297): feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - [PR 295](https://github.com/open-quantum-safe/liboqs-rust/pull/295): feat:  Implemented the RustCrypto traits for signatures and kems (#137)
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
