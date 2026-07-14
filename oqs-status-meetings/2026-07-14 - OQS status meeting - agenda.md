# 2026-07-14 - OQS status meeting - agenda

<span style="color: red;"> Tuesday July 14 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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


## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **[OQS Technical Steering Committee](https://github.com/open-quantum-safe/tsc)**


	- Issues with activity in the last 7 days:
		 - [Issue 316](https://github.com/open-quantum-safe/tsc/issues/316): Regularly review maintenance status of sub projects
		 - [Issue 312](https://github.com/open-quantum-safe/tsc/issues/312): Revise www security instructions
		 - [Issue 311](https://github.com/open-quantum-safe/tsc/issues/311): Revise oqs-provider SECURITY.md
		 - [Issue 310](https://github.com/open-quantum-safe/tsc/issues/310): Revise liboqs SECURITY.md
		 - [Issue 295](https://github.com/open-quantum-safe/tsc/issues/295): TSC Vice-chair selection
		 - [Issue 293](https://github.com/open-quantum-safe/tsc/issues/293): Remove security email list
	- Merges in the last 7 days:
		 - [PR 315](https://github.com/open-quantum-safe/tsc/pull/315): [vote] Add Douglas as future TSC vice chair
		 - [PR 314](https://github.com/open-quantum-safe/tsc/pull/314): Minutes for TSC meeting 2026-07-07
		 - [PR 313](https://github.com/open-quantum-safe/tsc/pull/313): Add TSC team to security-tracking repository
	- Open PRs: None


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 2491](https://github.com/open-quantum-safe/liboqs/pull/2491): [skip ci] remove release candidate suffix from 0.16.0-rc1
	- Open PRs:
		 - [PR 2489](https://github.com/open-quantum-safe/liboqs/pull/2489): ci: fix downstream-basic trigger logic (#2474)
		 - [PR 2488](https://github.com/open-quantum-safe/liboqs/pull/2488): Fix comment and string handling in the memory-function check
		 - [PR 2487](https://github.com/open-quantum-safe/liboqs/pull/2487): Add script inventory coverage tests
		 - [PR 2486](https://github.com/open-quantum-safe/liboqs/pull/2486): Bump the github-actions group across 1 directory with 5 updates  `dependencies` `github_actions`
		 - [PR 2485](https://github.com/open-quantum-safe/liboqs/pull/2485): Update Kyber algorithm status from Community to Supported
		 - [PR 2480](https://github.com/open-quantum-safe/liboqs/pull/2480): Add bounded CBMC proofs for liboqs-owned code
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI
		 - [PR 2478](https://github.com/open-quantum-safe/liboqs/pull/2478): Add public-input fuzzing CI
		 - [PR 2477](https://github.com/open-quantum-safe/liboqs/pull/2477): Add security research guidance and threat model
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)
		 - [PR 2473](https://github.com/open-quantum-safe/liboqs/pull/2473): tests: Mark rc as public via declassification
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
		 - [Issue 798](https://github.com/open-quantum-safe/oqs-provider/issues/798): Create test to ensure no alg overlap exists with openssl default provider
		 - [Issue 797](https://github.com/open-quantum-safe/oqs-provider/issues/797): Release new oqs-provider version  `question`
		 - [Issue 783](https://github.com/open-quantum-safe/oqs-provider/issues/783): Confusing information about SLH-DSA (and hybrids) in TLS  `bug`
	- Merges in the last 7 days:
		 - [PR 790](https://github.com/open-quantum-safe/oqs-provider/pull/790): Clarify standardized PQ algorithms on OpenSSL >= 3.5
		 - [PR 778](https://github.com/open-quantum-safe/oqs-provider/pull/778): oqsprov: avoid encoder hotpath in P-curve hybrid KEM keygen
	- Open PRs:
		 - [PR 799](https://github.com/open-quantum-safe/oqs-provider/pull/799): Add test algs overlap
		 - [PR 795](https://github.com/open-quantum-safe/oqs-provider/pull/795): Add weekly CI
		 - [PR 786](https://github.com/open-quantum-safe/oqs-provider/pull/786): ci: Harden GitHub Actions workflows
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 196](https://github.com/open-quantum-safe/openssh/pull/196): Add security fixes


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
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 107](https://github.com/open-quantum-safe/ci-containers/pull/107): ci: notify consumers when a new image is pushed


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days:
		 - [Issue 337](https://github.com/open-quantum-safe/www/issues/337): External-user listing request: BlackCoin v30.1.0 uses liboqs ML-DSA-44
		 - [Issue 215](https://github.com/open-quantum-safe/www/issues/215): Change integrations text
	- Merges in the last 7 days:
		 - [PR 340](https://github.com/open-quantum-safe/www/pull/340): External users: add subtlepq under VESvault
		 - [PR 339](https://github.com/open-quantum-safe/www/pull/339): Updates for liboqs 0.16.0 release
		 - [PR 338](https://github.com/open-quantum-safe/www/pull/338): Bump \_includes/liboqs from `aa294f5` to `5a1a854`  `dependencies` `submodules`
		 - [PR 336](https://github.com/open-quantum-safe/www/pull/336): Add VESvault / libVES to external users of OQS
		 - [PR 335](https://github.com/open-quantum-safe/www/pull/335): Remove email security alias and list from website security information
		 - [PR 334](https://github.com/open-quantum-safe/www/pull/334): Bump \_includes/liboqs from `11681ba` to `aa294f5`  `dependencies` `submodules`
	- Open PRs: None


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- Issues with activity in the last 7 days:
		 - [Issue 51](https://github.com/open-quantum-safe/liboqs-go/issues/51): build-windows failing in CI
	- Merges in the last 7 days:
		 - [PR 52](https://github.com/open-quantum-safe/liboqs-go/pull/52): fix stack size on windows for heavy sigs
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


	- Issues with activity in the last 7 days:
		 - [Issue 262](https://github.com/open-quantum-safe/liboqs-rust/issues/262): Please document how to build against the system copy of liboqs
		 - [Issue 137](https://github.com/open-quantum-safe/liboqs-rust/issues/137): Support RustCrypto KEM and Signature traits  `enhancement` `help wanted` `good first issue`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 310](https://github.com/open-quantum-safe/liboqs-rust/pull/310): feat: implement RustCrypto traits for signatures and KEMs
		 - [PR 309](https://github.com/open-quantum-safe/liboqs-rust/pull/309): fix: update wrapper for latest liboqs algorithm names
		 - [PR 308](https://github.com/open-quantum-safe/liboqs-rust/pull/308): docs: add macOS OpenSSL setup for tests
		 - [PR 306](https://github.com/open-quantum-safe/liboqs-rust/pull/306): chore(ci): fix targeting
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 299](https://github.com/open-quantum-safe/liboqs-rust/pull/299): feat: add Android CMake configuration patch
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 297](https://github.com/open-quantum-safe/liboqs-rust/pull/297): feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - [PR 295](https://github.com/open-quantum-safe/liboqs-rust/pull/295): feat:  Implemented the RustCrypto traits for signatures and kems (#137)
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
