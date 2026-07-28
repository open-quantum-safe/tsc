# 2026-07-28 - OQS status meeting - agenda

<span style="color: red;"> Tuesday July 28 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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
		 - [Issue 275](https://github.com/open-quantum-safe/tsc/issues/275): OQS Health Report - March 2026  `discussion`
	- Merges in the last 7 days:
		 - [PR 322](https://github.com/open-quantum-safe/tsc/pull/322): add jplomas to ci-containers committers
		 - [PR 320](https://github.com/open-quantum-safe/tsc/pull/320): Add summary for OQS Status Meeting 21/07/2026
		 - [PR 319](https://github.com/open-quantum-safe/tsc/pull/319): Add agenda for Status Meeting 21/07/26
	- Open PRs: None


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2506](https://github.com/open-quantum-safe/liboqs/issues/2506): macOS ARM64 CI build fails compiling sha2\_armv8.c without sha2 target feature
		 - [Issue 2504](https://github.com/open-quantum-safe/liboqs/issues/2504): Consider bounded CBMC proofs for liboqs-owned code  `help wanted` `future-work`
		 - [Issue 2498](https://github.com/open-quantum-safe/liboqs/issues/2498): CI re-design & review responsibility proposal
		 - [Issue 2497](https://github.com/open-quantum-safe/liboqs/issues/2497): Investigate and fix basic-checks CI runtime violation against CI runtime requirements (factor ~4x)
		 - [Issue 1842](https://github.com/open-quantum-safe/liboqs/issues/1842): Use OQS\_*\_set\_callbacks instead of C\_OR\_NI\_OR\_ARM macros  `refactor` `good first issue`
	- Merges in the last 7 days:
		 - [PR 2508](https://github.com/open-quantum-safe/liboqs/pull/2508): Fix ARM SHA2 build with AppleClang on macOS
		 - [PR 2503](https://github.com/open-quantum-safe/liboqs/pull/2503): Fix usage of XGETBV inline assembly in CPU extension detection
		 - [PR 2502](https://github.com/open-quantum-safe/liboqs/pull/2502): Bump the pip group across 2 directories with 3 updates  `dependencies` `python`
		 - [PR 2501](https://github.com/open-quantum-safe/liboqs/pull/2501): Add algorithm-integrator guidance to copy\_from\_upstream README
		 - [PR 2500](https://github.com/open-quantum-safe/liboqs/pull/2500): CI Workflow optimizer
		 - [PR 2471](https://github.com/open-quantum-safe/liboqs/pull/2471): Add parantheses around the use of sizeof operator
		 - [PR 2387](https://github.com/open-quantum-safe/liboqs/pull/2387): Adapt/Fix latest Wycheproof tests
		 - [PR 2386](https://github.com/open-quantum-safe/liboqs/pull/2386): Add missing ACVP tests [ML-KEM]
	- Open PRs:
		 - [PR 2510](https://github.com/open-quantum-safe/liboqs/pull/2510): Add requirements.txt for Python dependencies
		 - [PR 2509](https://github.com/open-quantum-safe/liboqs/pull/2509): further CI optimizations
		 - [PR 2507](https://github.com/open-quantum-safe/liboqs/pull/2507): Fix out-of-bounds read in hss\_validate\_signature\_init
		 - [PR 2505](https://github.com/open-quantum-safe/liboqs/pull/2505): Add another batch of declared algorithm support
		 - [PR 2494](https://github.com/open-quantum-safe/liboqs/pull/2494): release triggering for supported and ready downstreams and fix CI on forks
		 - [PR 2493](https://github.com/open-quantum-safe/liboqs/pull/2493): Add CI runtime report generator
		 - [PR 2489](https://github.com/open-quantum-safe/liboqs/pull/2489): ci: fix downstream-basic trigger logic (#2474)
		 - [PR 2488](https://github.com/open-quantum-safe/liboqs/pull/2488): Fix comment and string handling in the memory-function check
		 - [PR 2486](https://github.com/open-quantum-safe/liboqs/pull/2486): Bump the github-actions group across 1 directory with 5 updates  `dependencies` `github_actions`
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI  `help wanted`
		 - [PR 2478](https://github.com/open-quantum-safe/liboqs/pull/2478): Add public-input fuzzing CI  `help wanted`
		 - [PR 2477](https://github.com/open-quantum-safe/liboqs/pull/2477): Add security research guidance and threat model
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)
		 - [PR 2469](https://github.com/open-quantum-safe/liboqs/pull/2469): Document imported implementation status contract
		 - [PR 2466](https://github.com/open-quantum-safe/liboqs/pull/2466): Fix genkatdict.py bug and add tests for scripts (#1408)
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework
		 - [PR 2446](https://github.com/open-quantum-safe/liboqs/pull/2446): Add Markdown documentation linting
		 - [PR 2415](https://github.com/open-quantum-safe/liboqs/pull/2415): ci: add CodeQL query to enforce OpenSSL return code handling (#1867)
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 804](https://github.com/open-quantum-safe/oqs-provider/issues/804): Build deprecation warnings OpenSSL 4.1.0  `bug` `good first issue`
		 - [Issue 791](https://github.com/open-quantum-safe/oqs-provider/issues/791): Include CI testing again 'master' OpenSSL branch  `question`
	- Merges in the last 7 days:
		 - [PR 786](https://github.com/open-quantum-safe/oqs-provider/pull/786): ci: Harden GitHub Actions workflows
	- Open PRs:
		 - [PR 805](https://github.com/open-quantum-safe/oqs-provider/pull/805): Include back OpenSSL master testing onto CI
		 - [PR 803](https://github.com/open-quantum-safe/oqs-provider/pull/803): update SECURITY.md [skip ci]
		 - [PR 802](https://github.com/open-quantum-safe/oqs-provider/pull/802): Add IANA codepoints for hybrid SecP256r1MLKEM512 and MLKEM512X25519
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
		 - [PR 397](https://github.com/open-quantum-safe/oqs-demos/pull/397): Update OQS dependencies and fix segmentation faults on Alpine
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 108](https://github.com/open-quantum-safe/ci-containers/pull/108): size-reduce image for faster CI execution
	- Open PRs:
		 - [PR 109](https://github.com/open-quantum-safe/ci-containers/pull/109): Add monthly container usage tracker
		 - [PR 107](https://github.com/open-quantum-safe/ci-containers/pull/107): ci: notify consumers when a new image is pushed


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- Issues with activity in the last 7 days: None.
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


	- Issues with activity in the last 7 days:
		 - [Issue 151](https://github.com/open-quantum-safe/liboqs-python/issues/151): Support external-mu (extmu) ML-DSA variants in Signature wrapper and tests
		 - [Issue 149](https://github.com/open-quantum-safe/liboqs-python/issues/149): Bug: need a publishing workflow to publish to PyPi
		 - [Issue 14](https://github.com/open-quantum-safe/liboqs-python/issues/14): PyPI library entry  `enhancement`
	- Merges in the last 7 days:
		 - [PR 153](https://github.com/open-quantum-safe/liboqs-python/pull/153): Pin GitHub Actions to commit SHAs
		 - [PR 152](https://github.com/open-quantum-safe/liboqs-python/pull/152): Skip extmu ML-DSA variants in generic signature tests
		 - [PR 150](https://github.com/open-quantum-safe/liboqs-python/pull/150): Add PyPI trusted publishing workflow
		 - [PR 148](https://github.com/open-quantum-safe/liboqs-python/pull/148): Bump version to 0.16.1-dev
		 - [PR 147](https://github.com/open-quantum-safe/liboqs-python/pull/147): Bump pyasn1 from 0.6.3 to 0.6.4 in the pip group across 1 directory  `dependencies` `python`
		 - [PR 146](https://github.com/open-quantum-safe/liboqs-python/pull/146): Prepare 0.16.0 release
	- Open PRs:
		 - [PR 154](https://github.com/open-quantum-safe/liboqs-python/pull/154): Add external-mu (extmu) support to Signature wrapper and tests
		 - [PR 135](https://github.com/open-quantum-safe/liboqs-python/pull/135): docs: add clear installation guide for Windows and Raspberry Pi
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- Issues with activity in the last 7 days:
		 - [Issue 311](https://github.com/open-quantum-safe/liboqs-rust/issues/311): macOS ARM64 CI build fails compiling sha2\_armv8.c without sha2 target feature
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
