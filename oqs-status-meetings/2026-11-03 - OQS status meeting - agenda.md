# 2026-11-03 - OQS status meeting - agenda

<span style="color: red;"> Tuesday November 03 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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
		 - [Issue 293](https://github.com/open-quantum-safe/tsc/issues/293): Remove security email list
	- Merges in the last 7 days:
		 - [PR 357](https://github.com/open-quantum-safe/tsc/pull/357): Minutes for OQS status meeting 2026-10-27
		 - [PR 356](https://github.com/open-quantum-safe/tsc/pull/356): Add agenda for OQS Status Meeting 27/10/2026
		 - [PR 353](https://github.com/open-quantum-safe/tsc/pull/353): Update response process and security guidelines to exclude email
	- Open PRs:
		 - [PR 333](https://github.com/open-quantum-safe/tsc/pull/333): [vote] Add caretaker formal procedure


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2669](https://github.com/open-quantum-safe/liboqs/issues/2669): Add `docs/algorithms` datasheets to doxygen
		 - [Issue 2662](https://github.com/open-quantum-safe/liboqs/issues/2662): Restrict admins overruling push limitations
		 - [Issue 2659](https://github.com/open-quantum-safe/liboqs/issues/2659): Drop OpenSSL 1.1.1 support in 0.17.0
		 - [Issue 2658](https://github.com/open-quantum-safe/liboqs/issues/2658): CI runtime regression (again)
		 - [Issue 2657](https://github.com/open-quantum-safe/liboqs/issues/2657): Code coverage measures only the default-enabled algorithm set — define it and add a real weekly measurement
		 - [Issue 2653](https://github.com/open-quantum-safe/liboqs/issues/2653): copy\_from\_upstream: handle implementations with empty source lists
		 - [Issue 2644](https://github.com/open-quantum-safe/liboqs/issues/2644): Inconsistência de tipo de parâmetro em função SHA-3 (XKCP) — liboqs 0.16.0
		 - [Issue 2636](https://github.com/open-quantum-safe/liboqs/issues/2636): QR-UOV: use liboqs common AES implementation
		 - [Issue 2619](https://github.com/open-quantum-safe/liboqs/issues/2619): SDitH: Allow option to re-use temporary/entropy space in signature wrapper
		 - [Issue 2618](https://github.com/open-quantum-safe/liboqs/issues/2618): SDitH: Extend platform support (msvc/32-bit/big-endian)
		 - [Issue 2609](https://github.com/open-quantum-safe/liboqs/issues/2609): SDitH: Verify `test\_constant\_time` suppressions
		 - [Issue 2588](https://github.com/open-quantum-safe/liboqs/issues/2588): SDitH: Address `-DOQS\_STRICT\_WARNINGS=ON` warnings
		 - [Issue 2583](https://github.com/open-quantum-safe/liboqs/issues/2583): CI family usage reports (automated)
		 - [Issue 2490](https://github.com/open-quantum-safe/liboqs/issues/2490): Classic Mceliece status
		 - [Issue 2483](https://github.com/open-quantum-safe/liboqs/issues/2483): Add memory-optimized mldsa-native variants under OQS\_MEMOPT\_BUILD  `enhancement`
		 - [Issue 2482](https://github.com/open-quantum-safe/liboqs/issues/2482): Investigate Keccak\_Dispatch race condition  `bug`
		 - [Issue 2453](https://github.com/open-quantum-safe/liboqs/issues/2453): Adding SDitH  `enhancement` `help wanted`
		 - [Issue 2411](https://github.com/open-quantum-safe/liboqs/issues/2411): Include additional SLH-DSA-reduced parametrizations (SP 800-230)  `enhancement`
		 - [Issue 2291](https://github.com/open-quantum-safe/liboqs/issues/2291): Avoid duplicate CI runs in pull requests (push+PR tests)  `focus`
		 - [Issue 1867](https://github.com/open-quantum-safe/liboqs/issues/1867): Add CodeQL query to enforce OpenSSL return code handling  `enhancement` `good first issue`
	- Merges in the last 7 days:
		 - [PR 2668](https://github.com/open-quantum-safe/liboqs/pull/2668): Add repository rulesets as JSON for import
		 - [PR 2667](https://github.com/open-quantum-safe/liboqs/pull/2667): Optimize CI Runtime
		 - [PR 2664](https://github.com/open-quantum-safe/liboqs/pull/2664): Link libm via bare "m" flag for portable static/cross linking
		 - [PR 2663](https://github.com/open-quantum-safe/liboqs/pull/2663): remove retired macos-14 runners
		 - [PR 2661](https://github.com/open-quantum-safe/liboqs/pull/2661): Drop OpenSSL 1.1.1 Support
		 - [PR 2660](https://github.com/open-quantum-safe/liboqs/pull/2660): Build mldsa-native with MLD\_CONFIG\_REDUCE\_RAM if OQS\_MEMOPT\_BUILD  `enhancement`
		 - [PR 2656](https://github.com/open-quantum-safe/liboqs/pull/2656): Bump the github-actions group with 4 updates  `dependencies` `github_actions`
		 - [PR 2655](https://github.com/open-quantum-safe/liboqs/pull/2655): Bump the pip group across 1 directory with 2 updates  `dependencies` `python`
		 - [PR 2650](https://github.com/open-quantum-safe/liboqs/pull/2650): Bump certifi from 2025.8.3 to 2026.10.18 in /scripts/copy\_from\_upstream  `dependencies` `python`
		 - [PR 2648](https://github.com/open-quantum-safe/liboqs/pull/2648): Bump gitpython from 3.2.0 to 3.2.1 in /scripts/copy\_from\_upstream  `dependencies` `python`
		 - [PR 2646](https://github.com/open-quantum-safe/liboqs/pull/2646): Bump certifi from 2025.6.15 to 2026.10.19 in /.github/workflows  `dependencies` `python`
		 - [PR 2645](https://github.com/open-quantum-safe/liboqs/pull/2645): Bump certifi from 2025.6.15 to 2026.10.19 in the pip group across 1 directory  `dependencies` `python`
		 - [PR 2641](https://github.com/open-quantum-safe/liboqs/pull/2641): Bump the pip group across 1 directory with 2 updates  `dependencies` `python`
		 - [PR 2640](https://github.com/open-quantum-safe/liboqs/pull/2640): Disable Classic McEliece by default
		 - [PR 2634](https://github.com/open-quantum-safe/liboqs/pull/2634): Revived #2415: [CI] add CodeQL query to enforce OpenSSL return code handling (#1867)
		 - [PR 2630](https://github.com/open-quantum-safe/liboqs/pull/2630): Bump the github-actions group across 1 directory with 4 updates  `dependencies` `github_actions`
		 - [PR 2594](https://github.com/open-quantum-safe/liboqs/pull/2594): Interleave four AES blocks in the AES-NI and ARMv8 ECB and CTR paths
		 - [PR 2586](https://github.com/open-quantum-safe/liboqs/pull/2586): SDitH Integration
	- Open PRs:
		 - [PR 2666](https://github.com/open-quantum-safe/liboqs/pull/2666): CI: code coverage rework
		 - [PR 2665](https://github.com/open-quantum-safe/liboqs/pull/2665): Let ML-DSA Wycheproof verify vectors reach the library with wrong lengths
		 - [PR 2654](https://github.com/open-quantum-safe/liboqs/pull/2654): fix(importer): skip empty SIG and KEM implementation targets
		 - [PR 2652](https://github.com/open-quantum-safe/liboqs/pull/2652): fix(sha3): align XKCP extraction parameters with dispatch header
		 - [PR 2649](https://github.com/open-quantum-safe/liboqs/pull/2649): Switch astyle to clang-format for code formatting
		 - [PR 2643](https://github.com/open-quantum-safe/liboqs/pull/2643): refactor(qruov): deduplicate signature wrappers across implementations
		 - [PR 2642](https://github.com/open-quantum-safe/liboqs/pull/2642): refactor(qruov): use liboqs common AES backend
		 - [PR 2633](https://github.com/open-quantum-safe/liboqs/pull/2633): Add test checking for  NULL guards after `OQS\_MEM\_malloc` calls
		 - [PR 2627](https://github.com/open-quantum-safe/liboqs/pull/2627): Fix out-of-bounds write in sha256 inc\_blocks on zero-block call
		 - [PR 2625](https://github.com/open-quantum-safe/liboqs/pull/2625): SLH-DSA SHA2: ~4–5× sign/verify speedup
		 - [PR 2624](https://github.com/open-quantum-safe/liboqs/pull/2624): Add RISC-V RVV (rv64gcv) implementation for ML-KEM
		 - [PR 2622](https://github.com/open-quantum-safe/liboqs/pull/2622): Replace relative link with absolute URL
		 - [PR 2621](https://github.com/open-quantum-safe/liboqs/pull/2621): lock secret key in xmss/xmssmt sigs\_remaining
		 - [PR 2620](https://github.com/open-quantum-safe/liboqs/pull/2620): xmss: fail closed on partial lock tuple (like LMS)
		 - [PR 2616](https://github.com/open-quantum-safe/liboqs/pull/2616): Add a fuzz harness for the signature verification path
		 - [PR 2604](https://github.com/open-quantum-safe/liboqs/pull/2604): feat: Improve fuzzing build logic and LMS header lookup (#2602)
		 - [PR 2596](https://github.com/open-quantum-safe/liboqs/pull/2596): check signature length in xmssmt\_core\_sign\_open
		 - [PR 2593](https://github.com/open-quantum-safe/liboqs/pull/2593): Add SQIsign
		 - [PR 2592](https://github.com/open-quantum-safe/liboqs/pull/2592): Integrate FAEST.
		 - [PR 2591](https://github.com/open-quantum-safe/liboqs/pull/2591): Add tests for scripts/parse\_liboqs\_speed.py
		 - [PR 2587](https://github.com/open-quantum-safe/liboqs/pull/2587): Fix out-of-bounds read in slh\_dsa verify on short signature
		 - [PR 2566](https://github.com/open-quantum-safe/liboqs/pull/2566): slh\_dsa: guard memcpy against NULL message in sha2\_{256,512}\_update
		 - [PR 2565](https://github.com/open-quantum-safe/liboqs/pull/2565): scripts: map upstream Arm AES CPU flags
		 - [PR 2539](https://github.com/open-quantum-safe/liboqs/pull/2539): Vary the signature length in the stateful-signature fuzz harnesses
		 - [PR 2536](https://github.com/open-quantum-safe/liboqs/pull/2536): Fix SHA3 first-use dispatch race
		 - [PR 2479](https://github.com/open-quantum-safe/liboqs/pull/2479): Add public API mutation testing CI  `help wanted`
		 - [PR 2476](https://github.com/open-quantum-safe/liboqs/pull/2476): feat(sig): add derandomized keypair generation for ML-DSA (OQS\_SIG\_keypair\_derand)
		 - [PR 2464](https://github.com/open-quantum-safe/liboqs/pull/2464): Adds ppc64le support & draft pull of new mlkem-native ppc64le backend
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 864](https://github.com/open-quantum-safe/oqs-provider/issues/864): CI: aarch64 cross build fails linking oqs\_test\_signatures (undefined reference to log2 / SDitH)
		 - [Issue 807](https://github.com/open-quantum-safe/oqs-provider/issues/807): Homogenize CI jobs between platforms  `good first issue` `help wanted`
		 - [Issue 590](https://github.com/open-quantum-safe/oqs-provider/issues/590): Add static build CI  `good first issue` `help wanted`
		 - [Issue 485](https://github.com/open-quantum-safe/oqs-provider/issues/485): Document & test the new/3.4.0 encap/decap feature  `good first issue`
	- Merges in the last 7 days:
		 - [PR 865](https://github.com/open-quantum-safe/oqs-provider/pull/865): Resolve relative OPENSSL\_MODULES to absolute in runtests.sh
		 - [PR 863](https://github.com/open-quantum-safe/oqs-provider/pull/863): Fix crash CI tests
		 - [PR 862](https://github.com/open-quantum-safe/oqs-provider/pull/862): ci: run full ctest suite for static oqsprovider builds
		 - [PR 860](https://github.com/open-quantum-safe/oqs-provider/pull/860): tests: exercise pkeyutl -encap/-decap on OpenSSL >= 3.4
		 - [PR 857](https://github.com/open-quantum-safe/oqs-provider/pull/857): fix: resolve context string reuse failure and memory leak in signature ops
		 - [PR 844](https://github.com/open-quantum-safe/oqs-provider/pull/844): ci: homogenize platform testing 
	- Open PRs:
		 - [PR 866](https://github.com/open-quantum-safe/oqs-provider/pull/866): Enforce buffer capacity checks in hybrid KEM encapsulation
		 - [PR 861](https://github.com/open-quantum-safe/oqs-provider/pull/861): Clear private key copies before freeing them
		 - [PR 855](https://github.com/open-quantum-safe/oqs-provider/pull/855): User-level hybrid algorithm disablement
		 - [PR 852](https://github.com/open-quantum-safe/oqs-provider/pull/852): Re-structure code points assignation
		 - [PR 849](https://github.com/open-quantum-safe/oqs-provider/pull/849): Add QR-UOV to oqs-provider
		 - [PR 819](https://github.com/open-quantum-safe/oqs-provider/pull/819): fix: resolve OpenSSL 4.1 ASN.1 APIs at runtime


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days:
		 - [Issue 205](https://github.com/open-quantum-safe/openssh/issues/205): CI rekey fails on liboqs main after Classic McEliece default-off (#2640)
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 204](https://github.com/open-quantum-safe/openssh/pull/204): Teach sshkey\_check\_sigtype about OQS hybrid framing
		 - [PR 203](https://github.com/open-quantum-safe/openssh/pull/203): Fix memory leaks in OQS hybrid ECDH KEX path


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
	- Merges in the last 7 days:
		 - [PR 346](https://github.com/open-quantum-safe/www/pull/346): CI: bump setup-ruby and Ruby for Ubuntu 26.04 runners
		 - [PR 345](https://github.com/open-quantum-safe/www/pull/345): External users: add Qanum
	- Open PRs: None


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 28](https://github.com/open-quantum-safe/liboqs-cpp/pull/28): Fix SIGABRT crash in test suite by catching unhandled std::runtime\_error in threads
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
		 - [PR 163](https://github.com/open-quantum-safe/liboqs-python/pull/163): Bump version to 0.16.1-dev
		 - [PR 162](https://github.com/open-quantum-safe/liboqs-python/pull/162): Prepare 0.16.0.2 release
		 - [PR 161](https://github.com/open-quantum-safe/liboqs-python/pull/161): Validate key and ciphertext lengths before passing them to liboqs
		 - [PR 160](https://github.com/open-quantum-safe/liboqs-python/pull/160): Fix StatefulSignature.free leaking the native OQS\_SIG\_STFL struct
	- Open PRs:
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- Issues with activity in the last 7 days: None.
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
