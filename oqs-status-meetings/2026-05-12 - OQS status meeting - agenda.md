# 2026-05-12 - OQS status meeting - agenda

<span style="color: red;"> Tuesday May 12 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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

**In review**
- [Issue 2045](https://github.com/open-quantum-safe/liboqs/issues/2045): Create a table of algorithm support levels (liboqs)
- [Issue 2404](https://github.com/open-quantum-safe/liboqs/issues/2404): Update GOVERNANCE.md file and codeownwers for algorithms (liboqs)
- [PR 2410](https://github.com/open-quantum-safe/liboqs/pull/2410): [vote] Update GOVERNANCE.md and CODEOWNERS (liboqs)
- [PR 2413](https://github.com/open-quantum-safe/liboqs/pull/2413): Create a table of algorithm support levels (liboqs)

**Ready**
- [Issue 2405](https://github.com/open-quantum-safe/liboqs/issues/2405): Mention FrodoKEM algorithm change in 0.16.0 release notes (liboqs)



## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **[OQS Technical Steering Committee](https://github.com/open-quantum-safe/tsc)**


	- Issues with activity in the last 7 days:
		 - [Issue 277](https://github.com/open-quantum-safe/tsc/issues/277): OQS presence at relevant conferences - Message  `discussion`
		 - [Issue 276](https://github.com/open-quantum-safe/tsc/issues/276): OQS presence at relevant conferences - Venues  `discussion`
		 - [Issue 275](https://github.com/open-quantum-safe/tsc/issues/275): OQS Health Report - March 2026  `discussion`
	- Merges in the last 7 days:
		 - [PR 279](https://github.com/open-quantum-safe/tsc/pull/279): Add summary for OQS Status Meeting 05/05/2026
	- Open PRs:
		 - [PR 269](https://github.com/open-quantum-safe/tsc/pull/269): Update liboqs permissions


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2418](https://github.com/open-quantum-safe/liboqs/issues/2418): cryptobox pqc support
		 - [Issue 2392](https://github.com/open-quantum-safe/liboqs/issues/2392): MAYO signing function returns `MAYO\_OK` after 256 failed `sample\_solution()` attempts
		 - [Issue 1989](https://github.com/open-quantum-safe/liboqs/issues/1989): Drop Kyber support  `future-work`
		 - [Issue 1842](https://github.com/open-quantum-safe/liboqs/issues/1842): Use OQS\_*\_set\_callbacks instead of C\_OR\_NI\_OR\_ARM macros  `refactor` `good first issue`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 2419](https://github.com/open-quantum-safe/liboqs/pull/2419): Bump the pip group across 2 directories with 1 update  `dependencies` `python`
		 - [PR 2417](https://github.com/open-quantum-safe/liboqs/pull/2417): Build script to build liboqs
		 - [PR 2416](https://github.com/open-quantum-safe/liboqs/pull/2416): LMS Enhancements
		 - [PR 2415](https://github.com/open-quantum-safe/liboqs/pull/2415): ci: add CodeQL query to enforce OpenSSL return code handling (#1867)
		 - [PR 2414](https://github.com/open-quantum-safe/liboqs/pull/2414): Update Python package in copy\_from\_upstream  `dependencies`
		 - [PR 2413](https://github.com/open-quantum-safe/liboqs/pull/2413): Create a table of algorithm support levels  `documentation`
		 - [PR 2410](https://github.com/open-quantum-safe/liboqs/pull/2410): [vote] Update GOVERNANCE.md and CODEOWNERS  `focus`
		 - [PR 2407](https://github.com/open-quantum-safe/liboqs/pull/2407): Update HQC implementation to 2025-08-22 version
		 - [PR 2387](https://github.com/open-quantum-safe/liboqs/pull/2387): Adapt/Fix latest Wycheproof tests
		 - [PR 2386](https://github.com/open-quantum-safe/liboqs/pull/2386): Add missing ACVP tests [ML-KEM]
		 - [PR 2382](https://github.com/open-quantum-safe/liboqs/pull/2382): Add common dependencies with include\_only
		 - [PR 2366](https://github.com/open-quantum-safe/liboqs/pull/2366): Add API support for External-MU Signature[ML-DSA]
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 777](https://github.com/open-quantum-safe/oqs-provider/issues/777): Adding MQOM to oqs-provider  `question`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 779](https://github.com/open-quantum-safe/oqs-provider/pull/779): Add the MQOM signature algorithm 
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
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 325](https://github.com/open-quantum-safe/www/pull/325): Bump \_includes/liboqs from `ef70dea` to `0e325cc`  `dependencies` `submodules`


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


	- Issues with activity in the last 7 days:
		 - [Issue 136](https://github.com/open-quantum-safe/liboqs-python/issues/136): export\_secret\_key from StatefulSignature: TypeError: LoadLibrary() argument 1 must be str, not None
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 135](https://github.com/open-quantum-safe/liboqs-python/pull/135): docs: add clear installation guide for Windows and Raspberry Pi
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
