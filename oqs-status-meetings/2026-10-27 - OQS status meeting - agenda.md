# 2026-10-27 - OQS status meeting - agenda

<span style="color: red;"> Tuesday October 27 at 10:00 AM </span> US Eastern Time / 3:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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
		 - [Issue 310](https://github.com/open-quantum-safe/tsc/issues/310): Revise liboqs SECURITY.md
		 - [Issue 293](https://github.com/open-quantum-safe/tsc/issues/293): Remove security email list
	- Merges in the last 7 days:
		 - [PR 355](https://github.com/open-quantum-safe/tsc/pull/355): Minutes for OQS TSC meeting 2026-10-20
		 - [PR 354](https://github.com/open-quantum-safe/tsc/pull/354): Update meeting date in agenda for October 20, 2026
	- Open PRs:
		 - [PR 353](https://github.com/open-quantum-safe/tsc/pull/353): Update response process and security guidelines to exclude email
		 - [PR 333](https://github.com/open-quantum-safe/tsc/pull/333): [vote] Add caretaker formal procedure


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2647](https://github.com/open-quantum-safe/liboqs/issues/2647): ML-KEM: OQS\_KEM\_encaps/decaps cannot do the FIPS 203 length (type) checks; please document it
		 - [Issue 2644](https://github.com/open-quantum-safe/liboqs/issues/2644): Inconsistência de tipo de parâmetro em função SHA-3 (XKCP) — liboqs 0.16.0
		 - [Issue 2638](https://github.com/open-quantum-safe/liboqs/issues/2638): QR-UOV: investigate deduplicating variant signature wrappers
		 - [Issue 2637](https://github.com/open-quantum-safe/liboqs/issues/2637): QR-UOV: track official upstream instead of personal fork
		 - [Issue 2636](https://github.com/open-quantum-safe/liboqs/issues/2636): QR-UOV: use liboqs common AES implementation
		 - [Issue 2632](https://github.com/open-quantum-safe/liboqs/issues/2632): [0.16.0] `ninja run-tests` cannot pass, due to style issues?
		 - [Issue 2602](https://github.com/open-quantum-safe/liboqs/issues/2602): Improve public-input fuzzing and CI coverage  `enhancement` `help wanted`
		 - [Issue 2583](https://github.com/open-quantum-safe/liboqs/issues/2583): CI family usage reports (automated)
		 - [Issue 2483](https://github.com/open-quantum-safe/liboqs/issues/2483): Add memory-optimized mldsa-native variants under OQS\_MEMOPT\_BUILD  `enhancement`
		 - [Issue 2482](https://github.com/open-quantum-safe/liboqs/issues/2482): Investigate Keccak\_Dispatch race condition  `bug`
		 - [Issue 2454](https://github.com/open-quantum-safe/liboqs/issues/2454): Adding QR-UOV  `enhancement` `help wanted`
		 - [Issue 2160](https://github.com/open-quantum-safe/liboqs/issues/2160): Update speed tests to measure GPU performance for cuPQC code  `help wanted` `platform-specific`
		 - [Issue 1750](https://github.com/open-quantum-safe/liboqs/issues/1750): Return value from OQS\_randombytes
	- Merges in the last 7 days:
		 - [PR 2639](https://github.com/open-quantum-safe/liboqs/pull/2639): Expand SECURITY.md classification of vulnerabilities
		 - [PR 2582](https://github.com/open-quantum-safe/liboqs/pull/2582): Add QR-UOV signature schemes
	- Open PRs:
		 - [PR 2649](https://github.com/open-quantum-safe/liboqs/pull/2649): Switch astyle to clang-format for code formatting
		 - [PR 2648](https://github.com/open-quantum-safe/liboqs/pull/2648): Bump gitpython from 3.2.0 to 3.2.1 in /scripts/copy\_from\_upstream  `dependencies` `python`
		 - [PR 2646](https://github.com/open-quantum-safe/liboqs/pull/2646): Bump certifi from 2025.6.15 to 2026.10.19 in /.github/workflows  `dependencies` `python`
		 - [PR 2645](https://github.com/open-quantum-safe/liboqs/pull/2645): Bump certifi from 2025.6.15 to 2026.10.19 in the pip group across 1 directory  `dependencies` `python`
		 - [PR 2643](https://github.com/open-quantum-safe/liboqs/pull/2643): refactor(qruov): deduplicate signature wrappers across implementations
		 - [PR 2642](https://github.com/open-quantum-safe/liboqs/pull/2642): refactor(qruov): use liboqs common AES backend
		 - [PR 2641](https://github.com/open-quantum-safe/liboqs/pull/2641): Bump the pip group across 1 directory with 2 updates  `dependencies` `python`
		 - [PR 2640](https://github.com/open-quantum-safe/liboqs/pull/2640): Disable Classic McEliece by default
		 - [PR 2634](https://github.com/open-quantum-safe/liboqs/pull/2634): Revived #2415: [CI] add CodeQL query to enforce OpenSSL return code handling (#1867)
		 - [PR 2633](https://github.com/open-quantum-safe/liboqs/pull/2633): Add test checking for  NULL guards after `OQS\_MEM\_malloc` calls
		 - [PR 2630](https://github.com/open-quantum-safe/liboqs/pull/2630): Bump the github-actions group across 1 directory with 4 updates  `dependencies` `github_actions`
		 - [PR 2627](https://github.com/open-quantum-safe/liboqs/pull/2627): Fix out-of-bounds write in sha256 inc\_blocks on zero-block call
		 - [PR 2625](https://github.com/open-quantum-safe/liboqs/pull/2625): SLH-DSA SHA2: ~4–5× sign/verify speedup
		 - [PR 2624](https://github.com/open-quantum-safe/liboqs/pull/2624): Add RISC-V RVV (rv64gcv) implementation for ML-KEM
		 - [PR 2622](https://github.com/open-quantum-safe/liboqs/pull/2622): Replace relative link with absolute URL
		 - [PR 2621](https://github.com/open-quantum-safe/liboqs/pull/2621): lock secret key in xmss/xmssmt sigs\_remaining
		 - [PR 2620](https://github.com/open-quantum-safe/liboqs/pull/2620): xmss: fail closed on partial lock tuple (like LMS)
		 - [PR 2616](https://github.com/open-quantum-safe/liboqs/pull/2616): Add a fuzz harness for the signature verification path
		 - [PR 2604](https://github.com/open-quantum-safe/liboqs/pull/2604): feat: Improve fuzzing build logic and LMS header lookup (#2602)
		 - [PR 2603](https://github.com/open-quantum-safe/liboqs/pull/2603): improve OQS\_BUILD\_FUZZ\_TESTS build configuration
		 - [PR 2596](https://github.com/open-quantum-safe/liboqs/pull/2596): check signature length in xmssmt\_core\_sign\_open
		 - [PR 2594](https://github.com/open-quantum-safe/liboqs/pull/2594): Interleave four AES blocks in the AES-NI and ARMv8 ECB and CTR paths
		 - [PR 2593](https://github.com/open-quantum-safe/liboqs/pull/2593): Add SQIsign
		 - [PR 2592](https://github.com/open-quantum-safe/liboqs/pull/2592): Integrate FAEST.
		 - [PR 2591](https://github.com/open-quantum-safe/liboqs/pull/2591): Add tests for scripts/parse\_liboqs\_speed.py
		 - [PR 2587](https://github.com/open-quantum-safe/liboqs/pull/2587): Fix out-of-bounds read in slh\_dsa verify on short signature
		 - [PR 2586](https://github.com/open-quantum-safe/liboqs/pull/2586): SDitH Integration
		 - [PR 2566](https://github.com/open-quantum-safe/liboqs/pull/2566): slh\_dsa: guard memcpy against NULL message in sha2\_{256,512}\_update
		 - [PR 2565](https://github.com/open-quantum-safe/liboqs/pull/2565): scripts: map upstream Arm AES CPU flags
		 - [PR 2539](https://github.com/open-quantum-safe/liboqs/pull/2539): Vary the signature length in the stateful-signature fuzz harnesses
		 - [PR 2536](https://github.com/open-quantum-safe/liboqs/pull/2536): Fix SHA3 first-use dispatch race
		 - [PR 2535](https://github.com/open-quantum-safe/liboqs/pull/2535): Enable reduced-RAM ML-DSA under OQS\_MEMOPT\_BUILD
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI  `help wanted`
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 856](https://github.com/open-quantum-safe/oqs-provider/issues/856): complete 0.12.0 release cycle
		 - [Issue 854](https://github.com/open-quantum-safe/oqs-provider/issues/854): New Feature proposal: Automated TLS handshake performance benchmarking in CI  `won't fix` `question`
		 - [Issue 853](https://github.com/open-quantum-safe/oqs-provider/issues/853): Disable Classic McEliece by default  `question`
		 - [Issue 850](https://github.com/open-quantum-safe/oqs-provider/issues/850): BIKE-L1 silently TLS-disabled since #711; enable\_tls opt-in default is a KEM-side footgun
		 - [Issue 847](https://github.com/open-quantum-safe/oqs-provider/issues/847): Split out support for hybrid algorithms  `question`
		 - [Issue 807](https://github.com/open-quantum-safe/oqs-provider/issues/807): Homogenize CI jobs between platforms  `good first issue` `help wanted`
		 - [Issue 545](https://github.com/open-quantum-safe/oqs-provider/issues/545): Add test for out-of-source builds and tests  `good first issue` `help wanted`
		 - [Issue 272](https://github.com/open-quantum-safe/oqs-provider/issues/272): Race condition with `c\_obj\_create`.  `enhancement`
	- Merges in the last 7 days:
		 - [PR 848](https://github.com/open-quantum-safe/oqs-provider/pull/848): CI runtime optimization
		 - [PR 845](https://github.com/open-quantum-safe/oqs-provider/pull/845): Add advisory code-complexity CI (cyclomatic + cognitive)
		 - [PR 837](https://github.com/open-quantum-safe/oqs-provider/pull/837): Make concurrent provider loads safe
		 - [PR 812](https://github.com/open-quantum-safe/oqs-provider/pull/812): Support out-of-source builds and tests in the convenience scripts
	- Open PRs:
		 - [PR 855](https://github.com/open-quantum-safe/oqs-provider/pull/855): User-level hybrid algorithm disablement
		 - [PR 852](https://github.com/open-quantum-safe/oqs-provider/pull/852): Re-structure code points assignation
		 - [PR 849](https://github.com/open-quantum-safe/oqs-provider/pull/849): Add QR-UOV to oqs-provider
		 - [PR 844](https://github.com/open-quantum-safe/oqs-provider/pull/844): ci: homogenize platform testing 
		 - [PR 819](https://github.com/open-quantum-safe/oqs-provider/pull/819): fix: resolve OpenSSL 4.1 ASN.1 APIs at runtime


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days:
		 - [Issue 202](https://github.com/open-quantum-safe/openssh/issues/202): Add crypto library backing info to ssh -Q output  `enhancement`
	- Merges in the last 7 days:
		 - [PR 198](https://github.com/open-quantum-safe/openssh/pull/198): OpenSSH 10.4p1 uplift
	- Open PRs: None


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 402](https://github.com/open-quantum-safe/oqs-demos/pull/402): Update OQS Provider Tag
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
	- Open PRs:
		 - [PR 345](https://github.com/open-quantum-safe/www/pull/345): External users: add Qanum


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 28](https://github.com/open-quantum-safe/liboqs-cpp/pull/28): Fix SIGABRT crash in test suite by catching unhandled std::runtime\_error in threads


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
		 - [Issue 302](https://github.com/open-quantum-safe/liboqs-rust/issues/302): Reproducible builds ?
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 317](https://github.com/open-quantum-safe/liboqs-rust/pull/317): build(oqs-sys): add opt-in reproducible vendored builds
		 - [PR 316](https://github.com/open-quantum-safe/liboqs-rust/pull/316): fix: zeroize sensitive Rust-owned key material on drop
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 299](https://github.com/open-quantum-safe/liboqs-rust/pull/299): feat: add Android CMake configuration patch
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 297](https://github.com/open-quantum-safe/liboqs-rust/pull/297): feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
