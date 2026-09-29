# 2026-09-29 - OQS status meeting - agenda

<span style="color: red;"> Tuesday September 29 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Discussion with QR-UOV team
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
		 - [PR 345](https://github.com/open-quantum-safe/tsc/pull/345): chore: update jarvis-brian account name
		 - [PR 344](https://github.com/open-quantum-safe/tsc/pull/344): Add minutes for OQS status meeting 2026-09-22
		 - [PR 343](https://github.com/open-quantum-safe/tsc/pull/343): Add agenda for OQS Status Meeting 22/09/2026
	- Open PRs:
		 - [PR 333](https://github.com/open-quantum-safe/tsc/pull/333): [vote] Add caretaker formal procedure
		 - [PR 332](https://github.com/open-quantum-safe/tsc/pull/332): Add review guidelines


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2588](https://github.com/open-quantum-safe/liboqs/issues/2588): Address `-DOQS\_STRICT\_WARNINGS=ON` warnings for SDitH code
		 - [Issue 2583](https://github.com/open-quantum-safe/liboqs/issues/2583): CI family usage reports (automated)
		 - [Issue 2580](https://github.com/open-quantum-safe/liboqs/issues/2580): Interest in RISC-V (RVV) support for ML-KEM?
		 - [Issue 2579](https://github.com/open-quantum-safe/liboqs/issues/2579): ARMv8 aarch64 -march flag issues
		 - [Issue 2570](https://github.com/open-quantum-safe/liboqs/issues/2570): AES 192 Support  `enhancement`
		 - [Issue 2453](https://github.com/open-quantum-safe/liboqs/issues/2453): Adding SDitH  `enhancement` `help wanted`
		 - [Issue 2057](https://github.com/open-quantum-safe/liboqs/issues/2057): opensslconf.h not used  `bug` `help wanted`
		 - [Issue 1408](https://github.com/open-quantum-safe/liboqs/issues/1408): Test all scripts  `help wanted` `good first issue`
	- Merges in the last 7 days:
		 - [PR 2595](https://github.com/open-quantum-safe/liboqs/pull/2595): CI: faster scheduling for platform-tests
		 - [PR 2584](https://github.com/open-quantum-safe/liboqs/pull/2584): Do not mark the public API dllexport in Windows static builds
		 - [PR 2576](https://github.com/open-quantum-safe/liboqs/pull/2576): common: include opensslconf.h so OPENSSL\_NO\_STDIO is actually visible
		 - [PR 2571](https://github.com/open-quantum-safe/liboqs/pull/2571): Add AES 192 support.
	- Open PRs:
		 - [PR 2596](https://github.com/open-quantum-safe/liboqs/pull/2596): check signature length in xmssmt\_core\_sign\_open
		 - [PR 2594](https://github.com/open-quantum-safe/liboqs/pull/2594): Interleave four AES blocks in the AES-NI and ARMv8 ECB and CTR paths
		 - [PR 2593](https://github.com/open-quantum-safe/liboqs/pull/2593): Add SQIsign
		 - [PR 2592](https://github.com/open-quantum-safe/liboqs/pull/2592): Integrate FAEST.
		 - [PR 2591](https://github.com/open-quantum-safe/liboqs/pull/2591): Add tests for scripts/parse\_liboqs\_speed.py
		 - [PR 2590](https://github.com/open-quantum-safe/liboqs/pull/2590): Bump the github-actions group with 2 updates  `dependencies` `github_actions`
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
		 - [PR 2489](https://github.com/open-quantum-safe/liboqs/pull/2489): ci: fix downstream-basic trigger logic (#2474)
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI  `help wanted`
		 - [PR 2478](https://github.com/open-quantum-safe/liboqs/pull/2478): Add public-input fuzzing CI  `help wanted`
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 835](https://github.com/open-quantum-safe/oqs-provider/issues/835): oqsx\_gen ignores the selection, so a TLS 1.3 server generates a full KEM key pair on every handshake  `bug`
		 - [Issue 834](https://github.com/open-quantum-safe/oqs-provider/issues/834): oqsx\_gen ignores the selection, so a TLS 1.3 server generates a full KEM key pair on every handshake  `enhancement`
		 - [Issue 831](https://github.com/open-quantum-safe/oqs-provider/issues/831): Current "main" fails to compile  `bug`
		 - [Issue 821](https://github.com/open-quantum-safe/oqs-provider/issues/821): Remove support for standardized algorithms
		 - [Issue 667](https://github.com/open-quantum-safe/oqs-provider/issues/667): Standalone ml-kem and ml-dsa along with openssl-3.5.0  `enhancement` `futurework`
		 - [Issue 81](https://github.com/open-quantum-safe/oqs-provider/issues/81): Faster error-exit  `enhancement` `good first issue`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 837](https://github.com/open-quantum-safe/oqs-provider/pull/837): Make concurrent provider loads safe
		 - [PR 836](https://github.com/open-quantum-safe/oqs-provider/pull/836): Skip key generation in oqsx\_gen when no key pair is requested
		 - [PR 833](https://github.com/open-quantum-safe/oqs-provider/pull/833): 0.12.0 Release Candidate 2
		 - [PR 819](https://github.com/open-quantum-safe/oqs-provider/pull/819): fix: resolve OpenSSL 4.1 ASN.1 APIs at runtime
		 - [PR 812](https://github.com/open-quantum-safe/oqs-provider/pull/812): Support out-of-source builds and tests in the convenience scripts
		 - [PR 808](https://github.com/open-quantum-safe/oqs-provider/pull/808): fix: I use OpenSSL 4.1 ASN.1 string APIs


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days:
		 - [Issue 199](https://github.com/open-quantum-safe/openssh/issues/199): Implement Hybrid OQS provider for side-by-side PQ expirmentation  `enhancement`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 198](https://github.com/open-quantum-safe/openssh/pull/198): OpenSSH 10.4p1 uplift


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
		 - [PR 111](https://github.com/open-quantum-safe/ci-containers/pull/111): Upgrade ubuntu-jammy's pytest-xdist to v3.5.0.
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
	- Merges in the last 7 days:
		 - [PR 159](https://github.com/open-quantum-safe/liboqs-python/pull/159): Bump version to 0.16.1-dev
		 - [PR 158](https://github.com/open-quantum-safe/liboqs-python/pull/158): Bump pypa/gh-action-pypi-publish to v1.14.2
		 - [PR 157](https://github.com/open-quantum-safe/liboqs-python/pull/157): Prepare 0.16.0.1 release
		 - [PR 156](https://github.com/open-quantum-safe/liboqs-python/pull/156): Publish to PyPI on four-part version tags
	- Open PRs:
		 - [PR 160](https://github.com/open-quantum-safe/liboqs-python/pull/160): Fix StatefulSignature.free leaking the native OQS\_SIG\_STFL struct
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- Issues with activity in the last 7 days:
		 - [Issue 302](https://github.com/open-quantum-safe/liboqs-rust/issues/302): Reproducible builds ?
		 - [Issue 269](https://github.com/open-quantum-safe/liboqs-rust/issues/269): Zeroize mem / proj status re safe-oqs?
		 - [Issue 137](https://github.com/open-quantum-safe/liboqs-rust/issues/137): Support RustCrypto KEM and Signature traits  `enhancement` `help wanted` `good first issue`
	- Merges in the last 7 days:
		 - [PR 314](https://github.com/open-quantum-safe/liboqs-rust/pull/314): docs: explain signature generation exclusions
		 - [PR 310](https://github.com/open-quantum-safe/liboqs-rust/pull/310): feat: implement RustCrypto traits for signatures
		 - [PR 308](https://github.com/open-quantum-safe/liboqs-rust/pull/308): docs: add macOS OpenSSL setup for tests
		 - [PR 306](https://github.com/open-quantum-safe/liboqs-rust/pull/306): chore(ci): fix targeting
	- Open PRs:
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 299](https://github.com/open-quantum-safe/liboqs-rust/pull/299): feat: add Android CMake configuration patch
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 297](https://github.com/open-quantum-safe/liboqs-rust/pull/297): feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
