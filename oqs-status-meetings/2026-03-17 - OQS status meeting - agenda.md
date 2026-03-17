# 2026-03-17 - OQS status meeting - agenda

<span style="color: red;"> Tuesday March 17 at 10:00 AM </span> US Eastern Time / 3:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates & items seeking help
2. 0.16.0 prioritization

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

**Ready**
- [Issue 2045](https://github.com/open-quantum-safe/liboqs/issues/2045): Create a table of algorithm support levels (liboqs)

**In progress**
- [Issue 2118](https://github.com/open-quantum-safe/liboqs/issues/2118): Update HQC implementation to 2025/02/19 version (liboqs)
- [PR 2328](https://github.com/open-quantum-safe/liboqs/pull/2328): Hqc update reference implementation  (liboqs)

**In review**
- [PR 2356](https://github.com/open-quantum-safe/liboqs/pull/2356): sntrup761: replace PQClean code with public domain OpenSSH code (liboqs); *Looking for feedback from Basil and Michael*
- [PR 2376](https://github.com/open-quantum-safe/liboqs/pull/2376): Update mlkem-native to v1.1.0 (liboqs)



## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **[OQS Technical Steering Committee](https://github.com/open-quantum-safe/tsc)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days:
		 - [PR 254](https://github.com/open-quantum-safe/tsc/pull/254): generated 2026-03-10 agenda; add Python gitignores
		 - [PR 253](https://github.com/open-quantum-safe/tsc/pull/253): Status meeting agenda for March 3, 2026
		 - [PR 248](https://github.com/open-quantum-safe/tsc/pull/248): Minutes of OQS TSC meeting 2026-02-17
	- Open PRs: None


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- New issues in the last 14 days:
		 - [Issue 2375](https://github.com/open-quantum-safe/liboqs/issues/2375): Limit runtime of regular CI runs in PRs
	- Merges in the last 7 days:
		 - [PR 2378](https://github.com/open-quantum-safe/liboqs/pull/2378): Add Wycheproof tests [ML-DSA]
		 - [PR 2377](https://github.com/open-quantum-safe/liboqs/pull/2377): Check for overflow in arguments passed to OQS\_MEM\_calloc  `needs review`
		 - [PR 2369](https://github.com/open-quantum-safe/liboqs/pull/2369): Update Zephyr CI tests to recent versions
	- Open PRs:
		 - [PR 2379](https://github.com/open-quantum-safe/liboqs/pull/2379): Fix mismatched macros in LMS variants
		 - [PR 2376](https://github.com/open-quantum-safe/liboqs/pull/2376): Update mlkem-native to v1.1.0
		 - [PR 2366](https://github.com/open-quantum-safe/liboqs/pull/2366): Add API support for External-MU Signature[ML-DSA]
		 - [PR 2361](https://github.com/open-quantum-safe/liboqs/pull/2361): Add MQOM  `needs review` *Looking for feedback from Basil*
		 - [PR 2356](https://github.com/open-quantum-safe/liboqs/pull/2356): sntrup761: replace PQClean code with public domain OpenSSH code  `needs review` `focus`
		 - [PR 2328](https://github.com/open-quantum-safe/liboqs/pull/2328): Hqc update reference implementation 
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- New issues in the last 14 days:
		 - [Issue 759](https://github.com/open-quantum-safe/oqs-provider/issues/759): Cannot generate a key using kyber512 algorithm  `question`
		 - [Issue 757](https://github.com/open-quantum-safe/oqs-provider/issues/757): Validate build on openssl master
		 - [Issue 756](https://github.com/open-quantum-safe/oqs-provider/issues/756): Implement PQC algorithm inside the Openssl core libraray  `question`
		 - [Issue 755](https://github.com/open-quantum-safe/oqs-provider/issues/755): The sigx\_cmp interface has crashed.  `bug`
	- Merges in the last 7 days:
		 - [PR 758](https://github.com/open-quantum-safe/oqs-provider/pull/758): OSSL4 fixup
	- Open PRs:
		 - [PR 752](https://github.com/open-quantum-safe/oqs-provider/pull/752): Preserve property string for KEMs.
		 - [PR 655](https://github.com/open-quantum-safe/oqs-provider/pull/655): oqsprovider: allow building as shared library again
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- New issues in the last 14 days:
		 - [Issue 191](https://github.com/open-quantum-safe/openssh/issues/191): Fix merge builds
	- Merges in the last 7 days:
		 - [PR 190](https://github.com/open-quantum-safe/openssh/pull/190): Address possible vulnerability in preauth lengths for hybrid KEM
		 - [PR 189](https://github.com/open-quantum-safe/openssh/pull/189): Updating Sphincs to SLH-DSA
	- Open PRs: None


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- New issues in the last 14 days:
		 - [Issue 316](https://github.com/open-quantum-safe/www/issues/316): Update external uses
	- Merges in the last 7 days:
		 - [PR 319](https://github.com/open-quantum-safe/www/pull/319): Bump \_includes/liboqs from `a2fb264` to `e8b2e77`  `dependencies` `submodules`
		 - [PR 317](https://github.com/open-quantum-safe/www/pull/317): Bump \_includes/liboqs from `6b390dd` to `a2fb264`  `dependencies` `submodules`
		 - [PR 315](https://github.com/open-quantum-safe/www/pull/315): meta-oqs : oqs support for embedded Linux
	- Open PRs:
		 - [PR 318](https://github.com/open-quantum-safe/www/pull/318): Deprecate former users of OQS


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days:
		 - [PR 50](https://github.com/open-quantum-safe/liboqs-go/pull/50): Fix for #49 and verification against liboqs 0.15.0
	- Open PRs: None


11. **[liboqs-Java](https://github.com/open-quantum-safe/liboqs-java)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


12. **[liboqs-js](https://github.com/open-quantum-safe/liboqs-js)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


13. **[liboqs-Python](https://github.com/open-quantum-safe/liboqs-python)**


	- New issues in the last 14 days:
		 - [Issue 134](https://github.com/open-quantum-safe/liboqs-python/issues/134): is 0.12.0 0.11.0?
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 132](https://github.com/open-quantum-safe/liboqs-python/pull/132): Update liboqs version to 0.15.0.
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline
		 - [PR 119](https://github.com/open-quantum-safe/liboqs-python/pull/119): Version 0.14
		 - [PR 94](https://github.com/open-quantum-safe/liboqs-python/pull/94): replacing openssl111 with openssl3


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- New issues in the last 14 days: None.
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
