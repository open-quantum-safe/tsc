# 2026-06-16 - OQS status meeting - agenda

<span style="color: red;"> Tuesday June 16 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates & items seeking help

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
- [PR 2407](https://github.com/open-quantum-safe/liboqs/pull/2407): Update HQC implementation to 2025-08-22 version (liboqs)
- [PR 2431](https://github.com/open-quantum-safe/liboqs/pull/2431): Implement value barrier and apply to FrodoKEM (liboqs)

**Ready**
- [Issue 2405](https://github.com/open-quantum-safe/liboqs/issues/2405): Mention FrodoKEM algorithm change in 0.16.0 release notes (liboqs)

**Backlog**
- [Issue 2436](https://github.com/open-quantum-safe/liboqs/issues/2436): Investigate weekly build failures (liboqs)



## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **[OQS Technical Steering Committee](https://github.com/open-quantum-safe/tsc)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 298](https://github.com/open-quantum-safe/tsc/pull/298): Add summary for OQS Status Meeting 09/06/2026
		 - [PR 297](https://github.com/open-quantum-safe/tsc/pull/297): Add agenda for OQS status meeting 2026-06-09
	- Open PRs: None


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2465](https://github.com/open-quantum-safe/liboqs/issues/2465): Close
		 - [Issue 2461](https://github.com/open-quantum-safe/liboqs/issues/2461): Download Intel SDE from alternative source
		 - [Issue 2455](https://github.com/open-quantum-safe/liboqs/issues/2455): Support for external-mu signature variant in ML-DSA
	- Merges in the last 7 days:
		 - [PR 2463](https://github.com/open-quantum-safe/liboqs/pull/2463): Switch linux\_x86\_emulated to download Intel SDE from alternative source
		 - [PR 2460](https://github.com/open-quantum-safe/liboqs/pull/2460): Fix uninitialized encaps\_derand pointer dereference for NTRU KEMs
		 - [PR 2441](https://github.com/open-quantum-safe/liboqs/pull/2441): Add updated information regarding algorithm support
	- Open PRs:
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2457](https://github.com/open-quantum-safe/liboqs/pull/2457): Update Nixpkgs version to 26.05
		 - [PR 2456](https://github.com/open-quantum-safe/liboqs/pull/2456): Bump the github-actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 2451](https://github.com/open-quantum-safe/liboqs/pull/2451): liboqs 0.16.0 release candidate 1
		 - [PR 2450](https://github.com/open-quantum-safe/liboqs/pull/2450): SHA3 test improvements
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework
		 - [PR 2446](https://github.com/open-quantum-safe/liboqs/pull/2446): Add Markdown documentation linting
		 - [PR 2431](https://github.com/open-quantum-safe/liboqs/pull/2431): Implement value barrier and apply to FrodoKEM
		 - [PR 2417](https://github.com/open-quantum-safe/liboqs/pull/2417): Build script to build liboqs
		 - [PR 2415](https://github.com/open-quantum-safe/liboqs/pull/2415): ci: add CodeQL query to enforce OpenSSL return code handling (#1867)
		 - [PR 2407](https://github.com/open-quantum-safe/liboqs/pull/2407): Update HQC implementation to 2025-08-22 version  `needs review` `focus`
		 - [PR 2387](https://github.com/open-quantum-safe/liboqs/pull/2387): Adapt/Fix latest Wycheproof tests
		 - [PR 2386](https://github.com/open-quantum-safe/liboqs/pull/2386): Add missing ACVP tests [ML-KEM]
		 - [PR 2366](https://github.com/open-quantum-safe/liboqs/pull/2366): Add API support for External-MU Signature[ML-DSA]
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 784](https://github.com/open-quantum-safe/oqs-provider/issues/784): Modifying the `generate.yml` template not working as expected  `bug`
		 - [Issue 783](https://github.com/open-quantum-safe/oqs-provider/issues/783): Confusing information about SLH-DSA (and hybrids) in TLS  `bug`
	- Merges in the last 7 days:
		 - [PR 785](https://github.com/open-quantum-safe/oqs-provider/pull/785): Enhance DTLS1.3 support to handle the case when DTLS1.3 is disabled.
	- Open PRs:
		 - [PR 778](https://github.com/open-quantum-safe/oqs-provider/pull/778): oqsprov: avoid encoder hotpath in P-curve hybrid KEM keygen
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 194](https://github.com/open-quantum-safe/openssh/pull/194): Openssh 10.3p1 uplift


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 397](https://github.com/open-quantum-safe/oqs-demos/pull/397): Update OQS dependencies and fix segmentation faults on Alpine
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- Issues with activity in the last 7 days:
		 - [Issue 105](https://github.com/open-quantum-safe/ci-containers/issues/105): Creating an s390x and ppc64le ubuntu image.
	- Merges in the last 7 days:
		 - [PR 104](https://github.com/open-quantum-safe/ci-containers/pull/104): Include Intel Simplified Software License
		 - [PR 103](https://github.com/open-quantum-safe/ci-containers/pull/103): Add Intel SDE 9.53.0 (2025-03-16)
	- Open PRs: None


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 331](https://github.com/open-quantum-safe/www/pull/331): Revert "Host Intel SDE 9.53.0"
		 - [PR 330](https://github.com/open-quantum-safe/www/pull/330): Host Intel SDE 9.53.0
	- Open PRs:
		 - [PR 332](https://github.com/open-quantum-safe/www/pull/332): Bump \_includes/liboqs from `5a8d047` to `11681ba`  `dependencies` `submodules`
		 - [PR 329](https://github.com/open-quantum-safe/www/pull/329): Update webpage with Rodrigo's info


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
		 - [PR 135](https://github.com/open-quantum-safe/liboqs-python/pull/135): docs: add clear installation guide for Windows and Raspberry Pi
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline


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
