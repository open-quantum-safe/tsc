# 2026-06-30 - OQS status meeting - agenda

<span style="color: red;"> Tuesday June 30 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates & items seeking help
2. liboqs 0.16.0 release

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

No non-Done items.


## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **[OQS Technical Steering Committee](https://github.com/open-quantum-safe/tsc)**


	- Issues with activity in the last 7 days:
		 - [Issue 303](https://github.com/open-quantum-safe/tsc/issues/303): Create private security-tracking repo
	- Merges in the last 7 days:
		 - [PR 304](https://github.com/open-quantum-safe/tsc/pull/304): Create overall tracking repo
		 - [PR 302](https://github.com/open-quantum-safe/tsc/pull/302): Add summary for OQS Status Meeting 23/06/2026
		 - [PR 301](https://github.com/open-quantum-safe/tsc/pull/301): Add agenda for OQS Status Meeting 23/06/2026
	- Open PRs: None


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2483](https://github.com/open-quantum-safe/liboqs/issues/2483): Add memory-optimized mldsa-native variants under OQS\_MEMOPT\_BUILD  `enhancement`
		 - [Issue 2482](https://github.com/open-quantum-safe/liboqs/issues/2482): Investigate Keccak\_Dispatch race condition  `bug`
		 - [Issue 2481](https://github.com/open-quantum-safe/liboqs/issues/2481): Add x86-optimized HQC  `enhancement`
		 - [Issue 2475](https://github.com/open-quantum-safe/liboqs/issues/2475): Feature request: expose deterministic/derandomized keygen for the SIG family (OQS\_SIG\_*\_keypair\_derand) — mirroring the existing OQS\_KEM derand API
		 - [Issue 2474](https://github.com/open-quantum-safe/liboqs/issues/2474): [basic-downstream / trigger-downstream-ci] CI job does not appear to handle failures correctly
		 - [Issue 2405](https://github.com/open-quantum-safe/liboqs/issues/2405): Mention FrodoKEM algorithm change in 0.16.0 release notes  `documentation`
		 - [Issue 2402](https://github.com/open-quantum-safe/liboqs/issues/2402): HQC-128 base\_mul: clang x86-cmov-converter introduces secret-dependent branch chain (all released clang 14–22)
		 - [Issue 2390](https://github.com/open-quantum-safe/liboqs/issues/2390): clang-21 compilation warning: implicit conversion loses integer precision
		 - [Issue 2311](https://github.com/open-quantum-safe/liboqs/issues/2311): Refactor SLH-DSA C integration  `refactor`
		 - [Issue 1785](https://github.com/open-quantum-safe/liboqs/issues/1785): Add documentation Markdown linter to CI  `enhancement` `good first issue`
	- Merges in the last 7 days:
		 - [PR 2470](https://github.com/open-quantum-safe/liboqs/pull/2470): Update mlkem-native to v1.2.0
		 - [PR 2451](https://github.com/open-quantum-safe/liboqs/pull/2451): liboqs 0.16.0 release candidate 1
	- Open PRs:
		 - [PR 2484](https://github.com/open-quantum-safe/liboqs/pull/2484): Fix undefined ERR\_clear\_error symbol in OQS\_DLOPEN\_OPENSSL builds
		 - [PR 2480](https://github.com/open-quantum-safe/liboqs/pull/2480): Add bounded CBMC proofs for liboqs-owned code
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI
		 - [PR 2478](https://github.com/open-quantum-safe/liboqs/pull/2478): Add public-input fuzzing CI
		 - [PR 2477](https://github.com/open-quantum-safe/liboqs/pull/2477): Add security research guidance and threat model
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)
		 - [PR 2473](https://github.com/open-quantum-safe/liboqs/pull/2473): tests: Mark rc as public via declassification
		 - [PR 2472](https://github.com/open-quantum-safe/liboqs/pull/2472): Bump the github-actions group across 1 directory with 4 updates  `dependencies` `github_actions`
		 - [PR 2471](https://github.com/open-quantum-safe/liboqs/pull/2471): Add parantheses around the use of sizeof operator
		 - [PR 2469](https://github.com/open-quantum-safe/liboqs/pull/2469): Normalize mlkem-native backend status returns
		 - [PR 2466](https://github.com/open-quantum-safe/liboqs/pull/2466): Fix genkatdict.py bug and add tests for scripts (#1408)
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2457](https://github.com/open-quantum-safe/liboqs/pull/2457): Update Nixpkgs version to 26.05
		 - [PR 2450](https://github.com/open-quantum-safe/liboqs/pull/2450): SHA3 test improvements
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework
		 - [PR 2446](https://github.com/open-quantum-safe/liboqs/pull/2446): Add Markdown documentation linting
		 - [PR 2417](https://github.com/open-quantum-safe/liboqs/pull/2417): Build script to build liboqs
		 - [PR 2415](https://github.com/open-quantum-safe/liboqs/pull/2415): ci: add CodeQL query to enforce OpenSSL return code handling (#1867)
		 - [PR 2387](https://github.com/open-quantum-safe/liboqs/pull/2387): Adapt/Fix latest Wycheproof tests
		 - [PR 2386](https://github.com/open-quantum-safe/liboqs/pull/2386): Add missing ACVP tests [ML-KEM]
		 - [PR 2366](https://github.com/open-quantum-safe/liboqs/pull/2366): Add API support for External-MU Signature[ML-DSA]
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 784](https://github.com/open-quantum-safe/oqs-provider/issues/784): Modifying the `generate.yml` template not working as expected  `bug`
		 - [Issue 783](https://github.com/open-quantum-safe/oqs-provider/issues/783): Confusing information about SLH-DSA (and hybrids) in TLS  `bug`
		 - [Issue 772](https://github.com/open-quantum-safe/oqs-provider/issues/772): Re-activate HQC by default  `bug` `enhancement`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 788](https://github.com/open-quantum-safe/oqs-provider/pull/788): Remove algs that cannot be used in TLS from `openssl list -tls-signature-algorithms`
		 - [PR 787](https://github.com/open-quantum-safe/oqs-provider/pull/787): Re-activate HQC version 2025-08-22
		 - [PR 786](https://github.com/open-quantum-safe/oqs-provider/pull/786): ci: Harden GitHub Actions workflows
		 - [PR 778](https://github.com/open-quantum-safe/oqs-provider/pull/778): oqsprov: avoid encoder hotpath in P-curve hybrid KEM keygen
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


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 399](https://github.com/open-quantum-safe/oqs-demos/pull/399): Add PostgreSQL PQC TLS demo
		 - [PR 397](https://github.com/open-quantum-safe/oqs-demos/pull/397): Update OQS dependencies and fix segmentation faults on Alpine
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- Issues with activity in the last 7 days:
		 - [Issue 105](https://github.com/open-quantum-safe/ci-containers/issues/105): Creating an s390x and ppc64le ubuntu image.
	- Merges in the last 7 days:
		 - [PR 106](https://github.com/open-quantum-safe/ci-containers/pull/106): Add kyberslash patches for valgrind-based constant-time testing
	- Open PRs: None


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 334](https://github.com/open-quantum-safe/www/pull/334): Bump \_includes/liboqs from `11681ba` to `aa294f5`  `dependencies` `submodules`


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- Issues with activity in the last 7 days:
		 - [Issue 53](https://github.com/open-quantum-safe/liboqs-go/issues/53): 0.15 not released
		 - [Issue 51](https://github.com/open-quantum-safe/liboqs-go/issues/51): build-windows failing in CI
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 52](https://github.com/open-quantum-safe/liboqs-go/pull/52): fix stack size on windows for heavy sigs


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
		 - [Issue 122](https://github.com/open-quantum-safe/liboqs-python/issues/122): Fails to import package when liboqs is compiled with OQS\_DLOPEN\_OPENSSL=ON
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
