# 2026-09-01 - OQS status meeting - agenda

<span style="color: red;"> Tuesday September 01 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Discussion with Falcon / FN-DSA team
2. Status updates & items seeking help

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


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 333](https://github.com/open-quantum-safe/tsc/pull/333): [vote] Add caretaker formal procedure
		 - [PR 332](https://github.com/open-quantum-safe/tsc/pull/332): Add review guidelines


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2540](https://github.com/open-quantum-safe/liboqs/issues/2540): Is there a list of FOSS systems that can use liboqs?
		 - [Issue 2518](https://github.com/open-quantum-safe/liboqs/issues/2518): Update mldsa-native to v2.0.0
		 - [Issue 2454](https://github.com/open-quantum-safe/liboqs/issues/2454): Adding QR-UOV  `enhancement` `help wanted`
	- Merges in the last 7 days:
		 - [PR 2541](https://github.com/open-quantum-safe/liboqs/pull/2541): Rename shadowed test\_sig to test\_sig\_stfl in tests/test\_speed.py
		 - [PR 2522](https://github.com/open-quantum-safe/liboqs/pull/2522): Update mldsa-native to v2.0.0 [full tests] [extended tests]
	- Open PRs:
		 - [PR 2542](https://github.com/open-quantum-safe/liboqs/pull/2542): Fixed msg len for ML-DSA extmu speed test  `bug`
		 - [PR 2539](https://github.com/open-quantum-safe/liboqs/pull/2539): Vary the signature length in the stateful-signature fuzz harnesses
		 - [PR 2537](https://github.com/open-quantum-safe/liboqs/pull/2537): Documentation: link independent ML-KEM ACVP reproducibility study using liboqs 0.16.0
		 - [PR 2536](https://github.com/open-quantum-safe/liboqs/pull/2536): Fix SHA3 first-use dispatch race
		 - [PR 2535](https://github.com/open-quantum-safe/liboqs/pull/2535): Enable reduced-RAM ML-DSA under OQS\_MEMOPT\_BUILD
		 - [PR 2531](https://github.com/open-quantum-safe/liboqs/pull/2531): Bump gitpython from 3.1.58 to 3.1.59 in /scripts/copy\_from\_upstream in the pip group across 1 directory  `dependencies` `python`
		 - [PR 2526](https://github.com/open-quantum-safe/liboqs/pull/2526): Bump the github-actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 2524](https://github.com/open-quantum-safe/liboqs/pull/2524): build(cmake): allow CMAKE\_POSITION\_INDEPENDENT\_CODE to be overridden
		 - [PR 2521](https://github.com/open-quantum-safe/liboqs/pull/2521): Update mlkem-native to v2.0.0 [full tests] [extended tests]
		 - [PR 2520](https://github.com/open-quantum-safe/liboqs/pull/2520): Fix oqs\_sig\_stfl\_lms\_sign overflow on cross-parameter-set secret key
		 - [PR 2515](https://github.com/open-quantum-safe/liboqs/pull/2515): Fix undersized allocation in oqs\_aes128\_load\_schedule\_no\_bitslice
		 - [PR 2511](https://github.com/open-quantum-safe/liboqs/pull/2511): Fix out-of-bounds access in xmss\_core\_sign on secret key OID mismatch
		 - [PR 2509](https://github.com/open-quantum-safe/liboqs/pull/2509): further CI optimizations
		 - [PR 2507](https://github.com/open-quantum-safe/liboqs/pull/2507): Fix out-of-bounds read in hss\_validate\_signature\_init
		 - [PR 2494](https://github.com/open-quantum-safe/liboqs/pull/2494): release triggering for supported and ready downstreams and fix CI on forks
		 - [PR 2493](https://github.com/open-quantum-safe/liboqs/pull/2493): Add CI runtime report generator
		 - [PR 2489](https://github.com/open-quantum-safe/liboqs/pull/2489): ci: fix downstream-basic trigger logic (#2474)
		 - [PR 2488](https://github.com/open-quantum-safe/liboqs/pull/2488): Fix comment and string handling in the memory-function check
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI  `help wanted`
		 - [PR 2478](https://github.com/open-quantum-safe/liboqs/pull/2478): Add public-input fuzzing CI  `help wanted`
		 - [PR 2477](https://github.com/open-quantum-safe/liboqs/pull/2477): Add security research guidance and threat model
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)
		 - [PR 2469](https://github.com/open-quantum-safe/liboqs/pull/2469): Document imported implementation status contract
		 - [PR 2466](https://github.com/open-quantum-safe/liboqs/pull/2466): Fix genkatdict.py bug and add tests for scripts (#1408)
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 804](https://github.com/open-quantum-safe/oqs-provider/issues/804): Build deprecation warnings OpenSSL 4.1.0  `bug` `good first issue`
		 - [Issue 729](https://github.com/open-quantum-safe/oqs-provider/issues/729): Performance anomaly observed in hybrid KEM operations with oqs-provider  `question`
	- Merges in the last 7 days:
		 - [PR 815](https://github.com/open-quantum-safe/oqs-provider/pull/815): Fix component selection in hybrid KEM TEXT encoding
	- Open PRs:
		 - [PR 819](https://github.com/open-quantum-safe/oqs-provider/pull/819): fix: resolve OpenSSL 4.1 ASN.1 APIs at runtime
		 - [PR 818](https://github.com/open-quantum-safe/oqs-provider/pull/818): test: constant-time key comparison, no key-material dump on mismatch
		 - [PR 814](https://github.com/open-quantum-safe/oqs-provider/pull/814): Reject inconsistent classical lengths in hybrid KEM public keys
		 - [PR 812](https://github.com/open-quantum-safe/oqs-provider/pull/812): Support out-of-source builds and tests in the convenience scripts
		 - [PR 808](https://github.com/open-quantum-safe/oqs-provider/pull/808): fix: I use OpenSSL 4.1 ASN.1 string APIs


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 198](https://github.com/open-quantum-safe/openssh/pull/198): OpenSSH 10.4p1 uplift


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- Issues with activity in the last 7 days:
		 - [Issue 401](https://github.com/open-quantum-safe/oqs-demos/issues/401): New demo: Apache Kafka PQC TLS integration
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 397](https://github.com/open-quantum-safe/oqs-demos/pull/397): Update OQS dependencies and fix segmentation faults on Alpine
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 110](https://github.com/open-quantum-safe/ci-containers/pull/110): Add pre-build checks and drive CI from an images.yml manifest
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
		 - [PR 57](https://github.com/open-quantum-safe/liboqs-go/pull/57): Add GOVERNANCE.md file


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
