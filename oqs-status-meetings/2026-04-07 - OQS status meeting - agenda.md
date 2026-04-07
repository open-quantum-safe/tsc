# 2026-04-07 - OQS status meeting - agenda

<span style="color: red;"> Tuesday April 07 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates & items seeking help
2. liboqs 0.16.0 release planning

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


	- Issues with activity in the last 7 days:
		 - [Issue 246](https://github.com/open-quantum-safe/tsc/issues/246): New TSC chair
		 - [Issue 240](https://github.com/open-quantum-safe/tsc/issues/240): Propose PQCA mentorships for Summer 2026  `discussion` `High priority`
	- Merges in the last 7 days:
		 - [PR 261](https://github.com/open-quantum-safe/tsc/pull/261): 2026-03-31 OQS Status Meeting agenda
		 - [PR 260](https://github.com/open-quantum-safe/tsc/pull/260): add Rodrigo as oqsprovider maintainer
	- Open PRs: None


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2399](https://github.com/open-quantum-safe/liboqs/issues/2399): XMSS Signature Verification Fuzzing  `help wanted` `future-work` `good first issue`
		 - [Issue 2398](https://github.com/open-quantum-safe/liboqs/issues/2398): LMS Signature Verification Fuzzing  `help wanted` `good first issue`
	- Merges in the last 7 days:
		 - [PR 2393](https://github.com/open-quantum-safe/liboqs/pull/2393): Pin Wycheproof test vectors to last good commit
	- Open PRs:
		 - [PR 2397](https://github.com/open-quantum-safe/liboqs/pull/2397): Fix: Limit pytest processes to prevent OOM on low-RAM systems
		 - [PR 2396](https://github.com/open-quantum-safe/liboqs/pull/2396): fix: correct cuPQC ML-KEM derand symbol names and #if/#elif chains
		 - [PR 2394](https://github.com/open-quantum-safe/liboqs/pull/2394): fix: build on windows clang
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


	- Issues with activity in the last 7 days:
		 - [Issue 761](https://github.com/open-quantum-safe/oqs-provider/issues/761): TLS startup failed.  `question`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 752](https://github.com/open-quantum-safe/oqs-provider/pull/752): Preserve property string for KEMs.
		 - [PR 655](https://github.com/open-quantum-safe/oqs-provider/pull/655): oqsprovider: allow building as shared library again
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days:
		 - [Issue 193](https://github.com/open-quantum-safe/openssh/issues/193): Change documentation (missing ssh- reference for hybrid keyterm chosen)
	- Merges in the last 7 days: None.
	- Open PRs: None


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
	- Open PRs:
		 - [PR 101](https://github.com/open-quantum-safe/ci-containers/pull/101): Add python3-requests to bullseye dependencies


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 321](https://github.com/open-quantum-safe/www/pull/321): Bump \_includes/liboqs from `e8b2e77` to `8f08fd8`  `dependencies` `submodules`
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


	- Issues with activity in the last 7 days:
		 - [Issue 35](https://github.com/open-quantum-safe/liboqs-java/issues/35): Interface design for pluggable PQ verification backends (ML-DSA path)
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
