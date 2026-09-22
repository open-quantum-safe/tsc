# 2026-09-22 - OQS status meeting - agenda

<span style="color: red;"> Tuesday September 22 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 342](https://github.com/open-quantum-safe/tsc/pull/342): Add minutes for 2026-09-15 TSC meeting
		 - [PR 341](https://github.com/open-quantum-safe/tsc/pull/341): Add (draft) agenda for OQS TSC Meeting 15/09/2026
	- Open PRs:
		 - [PR 333](https://github.com/open-quantum-safe/tsc/pull/333): [vote] Add caretaker formal procedure
		 - [PR 332](https://github.com/open-quantum-safe/tsc/pull/332): Add review guidelines


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2583](https://github.com/open-quantum-safe/liboqs/issues/2583): CI family usage reports (automated)
		 - [Issue 2580](https://github.com/open-quantum-safe/liboqs/issues/2580): Interest in RISC-V (RVV) support for ML-KEM?
		 - [Issue 2579](https://github.com/open-quantum-safe/liboqs/issues/2579): ARMv8 aarch64 -march flag issues
		 - [Issue 2570](https://github.com/open-quantum-safe/liboqs/issues/2570): AES 192 Support  `enhancement`
		 - [Issue 2559](https://github.com/open-quantum-safe/liboqs/issues/2559): Update SNOVA to the Round 3 version
		 - [Issue 2545](https://github.com/open-quantum-safe/liboqs/issues/2545): pip install --require-hashes -r requirements.txt fails: charset\_normalizer not pinned
		 - [Issue 2454](https://github.com/open-quantum-safe/liboqs/issues/2454): Adding QR-UOV  `enhancement` `help wanted`
		 - [Issue 2453](https://github.com/open-quantum-safe/liboqs/issues/2453): Adding SDitH  `enhancement` `help wanted`
		 - [Issue 2160](https://github.com/open-quantum-safe/liboqs/issues/2160): Update speed tests to measure GPU performance for cuPQC code  `help wanted` `platform-specific`
		 - [Issue 1882](https://github.com/open-quantum-safe/liboqs/issues/1882): CMAKE\_POSITION\_INDEPENDENT\_CODE should be optional  `enhancement`
		 - [Issue 1408](https://github.com/open-quantum-safe/liboqs/issues/1408): Test all scripts  `help wanted` `good first issue`
	- Merges in the last 7 days:
		 - [PR 2578](https://github.com/open-quantum-safe/liboqs/pull/2578): Pin charset-normalizer in requirements.txt
		 - [PR 2577](https://github.com/open-quantum-safe/liboqs/pull/2577): Fixed XMSS Code Scan Issues
		 - [PR 2573](https://github.com/open-quantum-safe/liboqs/pull/2573): Bump the github-actions group with 3 updates  `dependencies` `github_actions`
		 - [PR 2572](https://github.com/open-quantum-safe/liboqs/pull/2572): Bump gitpython from 3.1.61 to 3.1.62 in /scripts/copy\_from\_upstream in the pip group across 1 directory  `dependencies` `python`
		 - [PR 2567](https://github.com/open-quantum-safe/liboqs/pull/2567): Fix AND separator in ARM64 required\_flags CMake guard
		 - [PR 2562](https://github.com/open-quantum-safe/liboqs/pull/2562): Update SNOVA to Round 3
		 - [PR 2524](https://github.com/open-quantum-safe/liboqs/pull/2524): build(cmake): allow CMAKE\_POSITION\_INDEPENDENT\_CODE to be overridden
		 - [PR 2515](https://github.com/open-quantum-safe/liboqs/pull/2515): Fix undersized allocation in oqs\_aes128\_load\_schedule\_no\_bitslice
		 - [PR 2511](https://github.com/open-quantum-safe/liboqs/pull/2511): Fix out-of-bounds access in xmss\_core\_sign on secret key OID mismatch
		 - [PR 2493](https://github.com/open-quantum-safe/liboqs/pull/2493): Add CI runtime report generator
	- Open PRs:
		 - [PR 2584](https://github.com/open-quantum-safe/liboqs/pull/2584): Do not mark the public API dllexport in Windows static builds
		 - [PR 2582](https://github.com/open-quantum-safe/liboqs/pull/2582): Add QR-UOV signature schemes
		 - [PR 2576](https://github.com/open-quantum-safe/liboqs/pull/2576): common: include opensslconf.h so OPENSSL\_NO\_STDIO is actually visible
		 - [PR 2571](https://github.com/open-quantum-safe/liboqs/pull/2571): Add AES 192 support.
		 - [PR 2569](https://github.com/open-quantum-safe/liboqs/pull/2569): Bind LMS verify to the variant the caller invoked
		 - [PR 2566](https://github.com/open-quantum-safe/liboqs/pull/2566): slh\_dsa: guard memcpy against NULL message in sha2\_{256,512}\_update
		 - [PR 2565](https://github.com/open-quantum-safe/liboqs/pull/2565): scripts: map upstream Arm AES CPU flags
		 - [PR 2539](https://github.com/open-quantum-safe/liboqs/pull/2539): Vary the signature length in the stateful-signature fuzz harnesses
		 - [PR 2536](https://github.com/open-quantum-safe/liboqs/pull/2536): Fix SHA3 first-use dispatch race
		 - [PR 2535](https://github.com/open-quantum-safe/liboqs/pull/2535): Enable reduced-RAM ML-DSA under OQS\_MEMOPT\_BUILD
		 - [PR 2520](https://github.com/open-quantum-safe/liboqs/pull/2520): Fix oqs\_sig\_stfl\_lms\_sign overflow on cross-parameter-set secret key
		 - [PR 2489](https://github.com/open-quantum-safe/liboqs/pull/2489): ci: fix downstream-basic trigger logic (#2474)
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI  `help wanted`
		 - [PR 2478](https://github.com/open-quantum-safe/liboqs/pull/2478): Add public-input fuzzing CI  `help wanted`
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 831](https://github.com/open-quantum-safe/oqs-provider/issues/831): Current "main" fails to compile  `bug`
		 - [Issue 826](https://github.com/open-quantum-safe/oqs-provider/issues/826): Update SNOVA parameter set (Round 3)  `question`
	- Merges in the last 7 days:
		 - [PR 830](https://github.com/open-quantum-safe/oqs-provider/pull/830): Update MAYO/MQOM/SNOVA to round-3
	- Open PRs:
		 - [PR 833](https://github.com/open-quantum-safe/oqs-provider/pull/833): 0.12.0 Release Candidate 2
		 - [PR 819](https://github.com/open-quantum-safe/oqs-provider/pull/819): fix: resolve OpenSSL 4.1 ASN.1 APIs at runtime
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
		 - [Issue 400](https://github.com/open-quantum-safe/oqs-demos/issues/400): New demo proposal: DICOM (DCMTK) over PQC-hybrid TLS 1.3
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


	- Issues with activity in the last 7 days:
		 - [Issue 155](https://github.com/open-quantum-safe/liboqs-python/issues/155): [Security Advisory] Please set a new Security Policy on the "Security and quality" tab so i can privately disclose a high severity vulnerability
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 313](https://github.com/open-quantum-safe/liboqs-rust/pull/313): refactor: generate signature algorithm metadata from liboqs
	- Open PRs:
		 - [PR 314](https://github.com/open-quantum-safe/liboqs-rust/pull/314): docs: explain signature generation exclusions
		 - [PR 310](https://github.com/open-quantum-safe/liboqs-rust/pull/310): feat: implement RustCrypto traits for signatures
		 - [PR 308](https://github.com/open-quantum-safe/liboqs-rust/pull/308): docs: add macOS OpenSSL setup for tests
		 - [PR 306](https://github.com/open-quantum-safe/liboqs-rust/pull/306): chore(ci): fix targeting
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 299](https://github.com/open-quantum-safe/liboqs-rust/pull/299): feat: add Android CMake configuration patch
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 297](https://github.com/open-quantum-safe/liboqs-rust/pull/297): feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - [PR 295](https://github.com/open-quantum-safe/liboqs-rust/pull/295): feat:  Implemented the RustCrypto traits for signatures and kems (#137)
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
