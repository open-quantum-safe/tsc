# 2026-10-06 - OQS status meeting - agenda

<span style="color: red;"> Tuesday October 06 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Discussion with FAEST team
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
	- Merges in the last 7 days:
		 - [PR 347](https://github.com/open-quantum-safe/tsc/pull/347): Minutes for OQS status meeting 2026-09-29
		 - [PR 346](https://github.com/open-quantum-safe/tsc/pull/346): Add agenda for Status Meeting 29/09/2026
		 - [PR 332](https://github.com/open-quantum-safe/tsc/pull/332): Add review guidelines
	- Open PRs:
		 - [PR 333](https://github.com/open-quantum-safe/tsc/pull/333): [vote] Add caretaker formal procedure


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2605](https://github.com/open-quantum-safe/liboqs/issues/2605): Fix minimal-build filtering for STFL fuzz targets and LMS generated-header lookup
		 - [Issue 2602](https://github.com/open-quantum-safe/liboqs/issues/2602): Improve public-input fuzzing and CI coverage  `enhancement` `help wanted`
		 - [Issue 2599](https://github.com/open-quantum-safe/liboqs/issues/2599): Falcon and Valgrind-Varlat crash due to floating-point use
		 - [Issue 2598](https://github.com/open-quantum-safe/liboqs/issues/2598): QR-UOV opt/avx2 excessive stack usage on small worker-thread stacks
		 - [Issue 2583](https://github.com/open-quantum-safe/liboqs/issues/2583): CI family usage reports (automated)
		 - [Issue 2579](https://github.com/open-quantum-safe/liboqs/issues/2579): ARMv8 aarch64 -march flag issues
		 - [Issue 2495](https://github.com/open-quantum-safe/liboqs/issues/2495): Make Wycheproof CI (network) failure resistant  `help wanted`
		 - [Issue 2490](https://github.com/open-quantum-safe/liboqs/issues/2490): Classic Mceliece status
		 - [Issue 2101](https://github.com/open-quantum-safe/liboqs/issues/2101): Adding FAEST  `enhancement` `help wanted`
	- Merges in the last 7 days:
		 - [PR 2597](https://github.com/open-quantum-safe/liboqs/pull/2597): Fix ARMv8 (sha3) handling in sig and kem families.
	- Open PRs:
		 - [PR 2607](https://github.com/open-quantum-safe/liboqs/pull/2607): Bump urllib3 from 2.7.0 to 2.8.0 in /.github/workflows  `dependencies` `python`
		 - [PR 2606](https://github.com/open-quantum-safe/liboqs/pull/2606): Bump urllib3 from 2.7.0 to 2.8.0 in /scripts/copy\_from\_upstream  `dependencies` `python`
		 - [PR 2604](https://github.com/open-quantum-safe/liboqs/pull/2604): feat: Improve fuzzing build logic and LMS header lookup (#2602)
		 - [PR 2603](https://github.com/open-quantum-safe/liboqs/pull/2603): improve OQS\_BUILD\_FUZZ\_TESTS build configuration
		 - [PR 2601](https://github.com/open-quantum-safe/liboqs/pull/2601): fix uninitialised length read in OQS\_SIG\_STFL\_alg\_lms\_sign
		 - [PR 2596](https://github.com/open-quantum-safe/liboqs/pull/2596): check signature length in xmssmt\_core\_sign\_open
		 - [PR 2594](https://github.com/open-quantum-safe/liboqs/pull/2594): Interleave four AES blocks in the AES-NI and ARMv8 ECB and CTR paths
		 - [PR 2593](https://github.com/open-quantum-safe/liboqs/pull/2593): Add SQIsign
		 - [PR 2592](https://github.com/open-quantum-safe/liboqs/pull/2592): Integrate FAEST.
		 - [PR 2591](https://github.com/open-quantum-safe/liboqs/pull/2591): Add tests for scripts/parse\_liboqs\_speed.py
		 - [PR 2590](https://github.com/open-quantum-safe/liboqs/pull/2590): Bump the github-actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 2587](https://github.com/open-quantum-safe/liboqs/pull/2587): Fix out-of-bounds read in slh\_dsa verify on short signature
		 - [PR 2586](https://github.com/open-quantum-safe/liboqs/pull/2586): SDitH3 Integration
		 - [PR 2582](https://github.com/open-quantum-safe/liboqs/pull/2582): Add QR-UOV signature schemes
		 - [PR 2569](https://github.com/open-quantum-safe/liboqs/pull/2569): Bind LMS verify to the variant the caller invoked
		 - [PR 2566](https://github.com/open-quantum-safe/liboqs/pull/2566): slh\_dsa: guard memcpy against NULL message in sha2\_{256,512}\_update
		 - [PR 2565](https://github.com/open-quantum-safe/liboqs/pull/2565): scripts: map upstream Arm AES CPU flags
		 - [PR 2539](https://github.com/open-quantum-safe/liboqs/pull/2539): Vary the signature length in the stateful-signature fuzz harnesses
		 - [PR 2536](https://github.com/open-quantum-safe/liboqs/pull/2536): Fix SHA3 first-use dispatch race
		 - [PR 2535](https://github.com/open-quantum-safe/liboqs/pull/2535): Enable reduced-RAM ML-DSA under OQS\_MEMOPT\_BUILD
		 - [PR 2520](https://github.com/open-quantum-safe/liboqs/pull/2520): Fix oqs\_sig\_stfl\_lms\_sign overflow on cross-parameter-set secret key
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI  `help wanted`
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 838](https://github.com/open-quantum-safe/oqs-provider/issues/838): CI failure with OpenSSL master  `bug`
		 - [Issue 834](https://github.com/open-quantum-safe/oqs-provider/issues/834): oqsx\_gen ignores the selection, so a TLS 1.3 server generates a full KEM key pair on every handshake  `enhancement`
		 - [Issue 821](https://github.com/open-quantum-safe/oqs-provider/issues/821): Remove support for standardized algorithms
		 - [Issue 81](https://github.com/open-quantum-safe/oqs-provider/issues/81): Faster error-exit  `enhancement` `good first issue`
	- Merges in the last 7 days:
		 - [PR 840](https://github.com/open-quantum-safe/oqs-provider/pull/840): Drop support for SecP256r1MLKEM512 from OpenSSL 4.0.0 onwards
		 - [PR 839](https://github.com/open-quantum-safe/oqs-provider/pull/839): Check unchecked allocation results in provider init and keygen
		 - [PR 836](https://github.com/open-quantum-safe/oqs-provider/pull/836): Skip key generation in oqsx\_gen when no key pair is requested
	- Open PRs:
		 - [PR 837](https://github.com/open-quantum-safe/oqs-provider/pull/837): Make concurrent provider loads safe
		 - [PR 833](https://github.com/open-quantum-safe/oqs-provider/pull/833): 0.12.0 Release Candidate 2
		 - [PR 819](https://github.com/open-quantum-safe/oqs-provider/pull/819): fix: resolve OpenSSL 4.1 ASN.1 APIs at runtime
		 - [PR 812](https://github.com/open-quantum-safe/oqs-provider/pull/812): Support out-of-source builds and tests in the convenience scripts


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
	- Merges in the last 7 days:
		 - [PR 342](https://github.com/open-quantum-safe/www/pull/342): Bump jekyll-feed from 0.17.0 to 0.18.0  `dependencies` `ruby`
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
		 - [PR 160](https://github.com/open-quantum-safe/liboqs-python/pull/160): Fix StatefulSignature.free leaking the native OQS\_SIG\_STFL struct
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- Issues with activity in the last 7 days:
		 - [Issue 315](https://github.com/open-quantum-safe/liboqs-rust/issues/315): Proposal: expose liboqs accelerator backends through oqs-sys Cargo features
		 - [Issue 302](https://github.com/open-quantum-safe/liboqs-rust/issues/302): Reproducible builds ?
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 299](https://github.com/open-quantum-safe/liboqs-rust/pull/299): feat: add Android CMake configuration patch
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 297](https://github.com/open-quantum-safe/liboqs-rust/pull/297): feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
