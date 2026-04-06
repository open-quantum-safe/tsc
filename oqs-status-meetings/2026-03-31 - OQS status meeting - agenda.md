# 2026-03-31 - OQS status meeting - agenda

<span style="color: red;"> Tuesday March 31 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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

**Ready**
- [Issue 2291](https://github.com/open-quantum-safe/liboqs/issues/2291): Avoid duplicate CI runs in pull requests (push+PR tests) (liboqs)
- [Issue 2045](https://github.com/open-quantum-safe/liboqs/issues/2045): Create a table of algorithm support levels (liboqs)
- [Issue 2101](https://github.com/open-quantum-safe/liboqs/issues/2101): Adding FAEST (liboqs)

**Backlog**
- [Issue 2334](https://github.com/open-quantum-safe/liboqs/issues/2334): Review performance regression tests (liboqs)
- [Issue 1788](https://github.com/open-quantum-safe/liboqs/issues/1788): Enable data independent timing on Apple Silicon (liboqs)
- [Issue 2282](https://github.com/open-quantum-safe/liboqs/issues/2282): Review and Apply Hardened Default Compiler Options (liboqs)
- [Issue 2329](https://github.com/open-quantum-safe/liboqs/issues/2329): Add support for Clang 22 \_\_builtin\_ct\_select (liboqs)
- [Issue 2098](https://github.com/open-quantum-safe/liboqs/issues/2098): Solicit more schemes from NIST signature on-ramp round 2 (liboqs)
- [Issue 2375](https://github.com/open-quantum-safe/liboqs/issues/2375): Limit runtime of regular CI runs in PRs (liboqs)
- [Issue 2341](https://github.com/open-quantum-safe/liboqs/issues/2341): Discuss impact of PQClean wind-down (liboqs)

**In progress**
- [Issue 2118](https://github.com/open-quantum-safe/liboqs/issues/2118): Update HQC implementation to 2025/02/19 version (liboqs)
- [PR 2328](https://github.com/open-quantum-safe/liboqs/pull/2328): Hqc update reference implementation  (liboqs)

**In review**
- [PR 2356](https://github.com/open-quantum-safe/liboqs/pull/2356): sntrup761: replace PQClean code with public domain OpenSSH code (liboqs)
- [PR 2376](https://github.com/open-quantum-safe/liboqs/pull/2376): Update mlkem-native to v1.1.0 (liboqs)
- [PR 2361](https://github.com/open-quantum-safe/liboqs/pull/2361): Add MQOM (liboqs)



## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **[OQS Technical Steering Committee](https://github.com/open-quantum-safe/tsc)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days:
		 - [PR 259](https://github.com/open-quantum-safe/tsc/pull/259): 2026-03-24 TSC meeting minutes
		 - [PR 258](https://github.com/open-quantum-safe/tsc/pull/258): Add 2026-03-24 TSC meeting agenda
	- Open PRs:
		 - [PR 260](https://github.com/open-quantum-safe/tsc/pull/260): add Rodrigo as oqsprovider maintainer


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- New issues in the last 14 days:
		 - [Issue 2392](https://github.com/open-quantum-safe/liboqs/issues/2392): MAYO signing function returns `MAYO\_OK` after 256 failed `sample\_solution()` attempts
		 - [Issue 2390](https://github.com/open-quantum-safe/liboqs/issues/2390): clang-21 compilation warning: implicit conversion loses integer precision
		 - [Issue 2388](https://github.com/open-quantum-safe/liboqs/issues/2388): Mismatched CUDA symbol names in ML-KEM keypair\_derand and encaps\_derand paths
		 - [Issue 2381](https://github.com/open-quantum-safe/liboqs/issues/2381): BIKE secret key indices leaked on stack due to sizeof(*array) vs sizeof(array) bug in secure\_clean()
		 - [Issue 2380](https://github.com/open-quantum-safe/liboqs/issues/2380): Copy from upstream: add support for algorithm-dependent common dependencies
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 2391](https://github.com/open-quantum-safe/liboqs/pull/2391): Update mldsa-native to v1.0.0-beta [full tests] [extended tests]
		 - [PR 2389](https://github.com/open-quantum-safe/liboqs/pull/2389): Bump the pip group across 2 directories with 1 update  `dependencies` `python`
		 - [PR 2387](https://github.com/open-quantum-safe/liboqs/pull/2387): Adapt/Fix latest Wycheproof tests
		 - [PR 2386](https://github.com/open-quantum-safe/liboqs/pull/2386): Add missing ACVP tests [ML-KEM]
		 - [PR 2385](https://github.com/open-quantum-safe/liboqs/pull/2385): Add MQOM to liboqs
		 - [PR 2384](https://github.com/open-quantum-safe/liboqs/pull/2384): Fix Reading beyond buffer end
		 - [PR 2383](https://github.com/open-quantum-safe/liboqs/pull/2383): Move compiler optimization level to CMAKE\_BUILD\_TYPE  `enhancement`
		 - [PR 2382](https://github.com/open-quantum-safe/liboqs/pull/2382): Add common dependencies with include\_only
		 - [PR 2379](https://github.com/open-quantum-safe/liboqs/pull/2379): Fix mismatched macros in LMS variants
		 - [PR 2376](https://github.com/open-quantum-safe/liboqs/pull/2376): Update mlkem-native to v1.1.0
		 - [PR 2366](https://github.com/open-quantum-safe/liboqs/pull/2366): Add API support for External-MU Signature[ML-DSA]
		 - [PR 2356](https://github.com/open-quantum-safe/liboqs/pull/2356): sntrup761: replace PQClean code with public domain OpenSSH code  `needs review` `focus`
		 - [PR 2328](https://github.com/open-quantum-safe/liboqs/pull/2328): Hqc update reference implementation 
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- New issues in the last 14 days:
		 - [Issue 761](https://github.com/open-quantum-safe/oqs-provider/issues/761): TLS startup failed.  `question`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 752](https://github.com/open-quantum-safe/oqs-provider/pull/752): Preserve property string for KEMs.
		 - [PR 655](https://github.com/open-quantum-safe/oqs-provider/pull/655): oqsprovider: allow building as shared library again
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- New issues in the last 14 days:
		 - [Issue 192](https://github.com/open-quantum-safe/openssh/issues/192): Not possible to create cert for quantum-safe algorithm | error "invalid argument"
	- Merges in the last 7 days: None.
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
	- Open PRs:
		 - [PR 101](https://github.com/open-quantum-safe/ci-containers/pull/101): Add python3-requests to bullseye dependencies


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 320](https://github.com/open-quantum-safe/www/pull/320): Bump \_includes/liboqs from `e8b2e77` to `ab0e07c`  `dependencies` `submodules`


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
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


	- New issues in the last 14 days: None.
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
