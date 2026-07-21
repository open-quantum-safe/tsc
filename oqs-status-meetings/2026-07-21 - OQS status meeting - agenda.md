# 2026-07-21 - OQS status meeting - agenda

<span style="color: red;"> Tuesday July 21 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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
	- Merges in the last 7 days:
		 - [PR 318](https://github.com/open-quantum-safe/tsc/pull/318): Add meeting summary from 2026-07-14 status meeting
		 - [PR 317](https://github.com/open-quantum-safe/tsc/pull/317): Add agenda for OQS status meeting 2026-07-14
	- Open PRs: None


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2498](https://github.com/open-quantum-safe/liboqs/issues/2498): CI re-design & review responsibility proposal
		 - [Issue 2497](https://github.com/open-quantum-safe/liboqs/issues/2497): Investigate and fix basic-checks CI runtime violation against CI runtime requirements (factor ~4x)
		 - [Issue 2495](https://github.com/open-quantum-safe/liboqs/issues/2495): Make Wycheproof CI (network) failure resistant  `help wanted`
		 - [Issue 2490](https://github.com/open-quantum-safe/liboqs/issues/2490): Classic Mceliece status
		 - [Issue 2454](https://github.com/open-quantum-safe/liboqs/issues/2454): Adding QR-UOV  `enhancement` `help wanted`
		 - [Issue 1842](https://github.com/open-quantum-safe/liboqs/issues/1842): Use OQS\_*\_set\_callbacks instead of C\_OR\_NI\_OR\_ARM macros  `refactor` `good first issue`
	- Merges in the last 7 days:
		 - [PR 2492](https://github.com/open-quantum-safe/liboqs/pull/2492): Fix integer overflow in OQS\_MEM\_aligned\_alloc size calculation
		 - [PR 2473](https://github.com/open-quantum-safe/liboqs/pull/2473): tests: Mark rc as public via declassification
		 - [PR 2457](https://github.com/open-quantum-safe/liboqs/pull/2457): Update Nixpkgs version to 26.05
		 - [PR 2450](https://github.com/open-quantum-safe/liboqs/pull/2450): SHA3 test improvements
		 - [PR 2366](https://github.com/open-quantum-safe/liboqs/pull/2366): Add API support for External-MU Signature[ML-DSA]
	- Open PRs:
		 - [PR 2496](https://github.com/open-quantum-safe/liboqs/pull/2496): Additional CI profiling and sig\_stfl CI bug fixes
		 - [PR 2494](https://github.com/open-quantum-safe/liboqs/pull/2494): release triggering for supported and ready downstreams and fix CI on forks
		 - [PR 2493](https://github.com/open-quantum-safe/liboqs/pull/2493): Add CI runtime report generator
		 - [PR 2489](https://github.com/open-quantum-safe/liboqs/pull/2489): ci: fix downstream-basic trigger logic (#2474)
		 - [PR 2488](https://github.com/open-quantum-safe/liboqs/pull/2488): Fix comment and string handling in the memory-function check
		 - [PR 2487](https://github.com/open-quantum-safe/liboqs/pull/2487): Add script inventory coverage tests
		 - [PR 2486](https://github.com/open-quantum-safe/liboqs/pull/2486): Bump the github-actions group across 1 directory with 5 updates  `dependencies` `github_actions`
		 - [PR 2480](https://github.com/open-quantum-safe/liboqs/pull/2480): Add bounded CBMC proofs for liboqs-owned code
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI
		 - [PR 2478](https://github.com/open-quantum-safe/liboqs/pull/2478): Add public-input fuzzing CI
		 - [PR 2477](https://github.com/open-quantum-safe/liboqs/pull/2477): Add security research guidance and threat model
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)  `focus`
		 - [PR 2471](https://github.com/open-quantum-safe/liboqs/pull/2471): Add parantheses around the use of sizeof operator
		 - [PR 2469](https://github.com/open-quantum-safe/liboqs/pull/2469): Document imported implementation status contract
		 - [PR 2466](https://github.com/open-quantum-safe/liboqs/pull/2466): Fix genkatdict.py bug and add tests for scripts (#1408)
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework
		 - [PR 2446](https://github.com/open-quantum-safe/liboqs/pull/2446): Add Markdown documentation linting
		 - [PR 2417](https://github.com/open-quantum-safe/liboqs/pull/2417): Build script to build liboqs
		 - [PR 2415](https://github.com/open-quantum-safe/liboqs/pull/2415): ci: add CodeQL query to enforce OpenSSL return code handling (#1867)
		 - [PR 2387](https://github.com/open-quantum-safe/liboqs/pull/2387): Adapt/Fix latest Wycheproof tests
		 - [PR 2386](https://github.com/open-quantum-safe/liboqs/pull/2386): Add missing ACVP tests [ML-KEM]
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 801](https://github.com/open-quantum-safe/oqs-provider/issues/801): IANA codepoints for ML-KEM-512 hybrids  `question`
		 - [Issue 800](https://github.com/open-quantum-safe/oqs-provider/issues/800): BIKE-L1 disable in PR #790 contradicts stated policy  `question`
		 - [Issue 798](https://github.com/open-quantum-safe/oqs-provider/issues/798): Create test to ensure no alg overlap exists with openssl default provider
		 - [Issue 792](https://github.com/open-quantum-safe/oqs-provider/issues/792): Handling of "caching" behavior in `oqsprovider\_query`  `question`
		 - [Issue 791](https://github.com/open-quantum-safe/oqs-provider/issues/791): Include CI testing again 'master' OpenSSL branch  `question`
		 - [Issue 729](https://github.com/open-quantum-safe/oqs-provider/issues/729): Performance anomaly observed in hybrid KEM operations with oqs-provider  `question`
		 - [Issue 727](https://github.com/open-quantum-safe/oqs-provider/issues/727): Key generation performance of EC-P hybrids drops significantly when OQS\_KEM\_ENCODERS is set to ON  `help wanted`
	- Merges in the last 7 days:
		 - [PR 799](https://github.com/open-quantum-safe/oqs-provider/pull/799): Add test algs overlap
	- Open PRs:
		 - [PR 803](https://github.com/open-quantum-safe/oqs-provider/pull/803): update SECURITY.md [skip ci]
		 - [PR 802](https://github.com/open-quantum-safe/oqs-provider/pull/802): Add IANA codepoints for hybrid SecP256r1MLKEM512 and MLKEM512X25519
		 - [PR 795](https://github.com/open-quantum-safe/oqs-provider/pull/795): Add weekly CI
		 - [PR 786](https://github.com/open-quantum-safe/oqs-provider/pull/786): ci: Harden GitHub Actions workflows
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 196](https://github.com/open-quantum-safe/openssh/pull/196): Add security fixes
	- Open PRs: None


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 399](https://github.com/open-quantum-safe/oqs-demos/pull/399): Add PostgreSQL PQC TLS demo
	- Open PRs:
		 - [PR 397](https://github.com/open-quantum-safe/oqs-demos/pull/397): Update OQS dependencies and fix segmentation faults on Alpine
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 107](https://github.com/open-quantum-safe/ci-containers/pull/107): ci: notify consumers when a new image is pushed


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days:
		 - [Issue 337](https://github.com/open-quantum-safe/www/issues/337): External-user listing request: BlackCoin v30.1.0 uses liboqs ML-DSA-44
	- Merges in the last 7 days:
		 - [PR 340](https://github.com/open-quantum-safe/www/pull/340): External users: add subtlepq under VESvault
	- Open PRs: None


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- Issues with activity in the last 7 days:
		 - [Issue 54](https://github.com/open-quantum-safe/liboqs-go/issues/54): CI failures: ML-DSA extmu in liboqs:main
		 - [Issue 53](https://github.com/open-quantum-safe/liboqs-go/issues/53): 0.15 not released
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 55](https://github.com/open-quantum-safe/liboqs-go/pull/55): liboqs 0.16.0 parity and CI enhancements


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
		 - [PR 146](https://github.com/open-quantum-safe/liboqs-python/pull/146): Prepare 0.16.0 release
		 - [PR 135](https://github.com/open-quantum-safe/liboqs-python/pull/135): docs: add clear installation guide for Windows and Raspberry Pi
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 310](https://github.com/open-quantum-safe/liboqs-rust/pull/310): feat: implement RustCrypto traits for signatures and KEMs
		 - [PR 309](https://github.com/open-quantum-safe/liboqs-rust/pull/309): fix: update wrapper for latest liboqs algorithm names  `focus`
		 - [PR 308](https://github.com/open-quantum-safe/liboqs-rust/pull/308): docs: add macOS OpenSSL setup for tests
		 - [PR 306](https://github.com/open-quantum-safe/liboqs-rust/pull/306): chore(ci): fix targeting
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 299](https://github.com/open-quantum-safe/liboqs-rust/pull/299): feat: add Android CMake configuration patch
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 297](https://github.com/open-quantum-safe/liboqs-rust/pull/297): feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - [PR 295](https://github.com/open-quantum-safe/liboqs-rust/pull/295): feat:  Implemented the RustCrypto traits for signatures and kems (#137)
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
