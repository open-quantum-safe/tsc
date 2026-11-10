# 2026-11-10 - OQS status meeting - agenda

<span style="color: red;"> Tuesday November 10 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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
		 - [Issue 360](https://github.com/open-quantum-safe/tsc/issues/360): Update READMEs
		 - [Issue 293](https://github.com/open-quantum-safe/tsc/issues/293): Remove security email list
	- Merges in the last 7 days:
		 - [PR 359](https://github.com/open-quantum-safe/tsc/pull/359): Minutes for OQS status meeting 2026-11-03
		 - [PR 358](https://github.com/open-quantum-safe/tsc/pull/358): Add agenda for OQS Status Meeting 03/11/2026
		 - [PR 353](https://github.com/open-quantum-safe/tsc/pull/353): Update response process and security guidelines to exclude email
	- Open PRs:
		 - [PR 333](https://github.com/open-quantum-safe/tsc/pull/333): [vote] Add caretaker formal procedure


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2687](https://github.com/open-quantum-safe/liboqs/issues/2687): Fuzz KEM encapsulation with mutated public keys
		 - [Issue 2686](https://github.com/open-quantum-safe/liboqs/issues/2686): Update SLH-DSA implementation
		 - [Issue 2684](https://github.com/open-quantum-safe/liboqs/issues/2684): HQC: imported code still has upstream HQC issue #31 (uint8\_t buffers passed as uint64\_t *)
		 - [Issue 2682](https://github.com/open-quantum-safe/liboqs/issues/2682): QRUOV secure\_zero calls explicit\_bzero on NetBSD
		 - [Issue 2679](https://github.com/open-quantum-safe/liboqs/issues/2679): Validate liboqs’s installed link interface and strengthen downstream integration coverage
		 - [Issue 2678](https://github.com/open-quantum-safe/liboqs/issues/2678): Review upstream maintenance status
		 - [Issue 2674](https://github.com/open-quantum-safe/liboqs/issues/2674): Should we use merge queues?  `enhancement`
		 - [Issue 2673](https://github.com/open-quantum-safe/liboqs/issues/2673): Upgrade `haswell` target to `skylake` in CT tests to include more implementations
		 - [Issue 2670](https://github.com/open-quantum-safe/liboqs/issues/2670): Update HQC to 2026-10-12 version
		 - [Issue 2662](https://github.com/open-quantum-safe/liboqs/issues/2662): Restrict admins overruling push limitations
		 - [Issue 2659](https://github.com/open-quantum-safe/liboqs/issues/2659): Drop OpenSSL 1.1.1 support in 0.17.0
		 - [Issue 2658](https://github.com/open-quantum-safe/liboqs/issues/2658): CI runtime regression (again)
		 - [Issue 2653](https://github.com/open-quantum-safe/liboqs/issues/2653): copy\_from\_upstream: handle implementations with empty source lists
		 - [Issue 2647](https://github.com/open-quantum-safe/liboqs/issues/2647): ML-KEM: OQS\_KEM\_encaps/decaps cannot do the FIPS 203 length (type) checks; please document it
		 - [Issue 2644](https://github.com/open-quantum-safe/liboqs/issues/2644): Inconsistência de tipo de parâmetro em função SHA-3 (XKCP) — liboqs 0.16.0
		 - [Issue 2638](https://github.com/open-quantum-safe/liboqs/issues/2638): QR-UOV: investigate deduplicating variant signature wrappers
		 - [Issue 2637](https://github.com/open-quantum-safe/liboqs/issues/2637): QR-UOV: track official upstream instead of personal fork
		 - [Issue 2636](https://github.com/open-quantum-safe/liboqs/issues/2636): QR-UOV: use liboqs common AES implementation
		 - [Issue 2619](https://github.com/open-quantum-safe/liboqs/issues/2619): SDitH: Allow option to re-use temporary/entropy space in signature wrapper
		 - [Issue 2598](https://github.com/open-quantum-safe/liboqs/issues/2598): QR-UOV opt/avx2 excessive stack usage on small worker-thread stacks
		 - [Issue 2516](https://github.com/open-quantum-safe/liboqs/issues/2516): SLH-DSA SHA2 parameter sets fail signature verification on Windows/MSVC build (SHAKE variants unaffected)
		 - [Issue 2481](https://github.com/open-quantum-safe/liboqs/issues/2481): Add x86-optimized HQC  `enhancement`
		 - [Issue 1946](https://github.com/open-quantum-safe/liboqs/issues/1946): [Feature request] SQIsign  `enhancement` `help wanted`
		 - [Issue 1842](https://github.com/open-quantum-safe/liboqs/issues/1842): Use OQS\_*\_set\_callbacks instead of C\_OR\_NI\_OR\_ARM macros  `refactor` `good first issue`
		 - [Issue 1619](https://github.com/open-quantum-safe/liboqs/issues/1619): Introduce constant time build variable  `enhancement`
	- Merges in the last 7 days:
		 - [PR 2688](https://github.com/open-quantum-safe/liboqs/pull/2688): doc(kem): document caller length check responsibilities for FIPS 203 (#2647)
		 - [PR 2683](https://github.com/open-quantum-safe/liboqs/pull/2683): qruov: use explicit\_memset on NetBSD in secure\_zero
		 - [PR 2677](https://github.com/open-quantum-safe/liboqs/pull/2677): Fix minor CT bugs in CI
		 - [PR 2676](https://github.com/open-quantum-safe/liboqs/pull/2676): Bump the github-actions group with 2 updates  `dependencies` `github_actions`
		 - [PR 2675](https://github.com/open-quantum-safe/liboqs/pull/2675): Bump pytest from 9.1.1 to 9.2.0 in /.github/workflows in the pip group across 1 directory  `dependencies` `python`
		 - [PR 2667](https://github.com/open-quantum-safe/liboqs/pull/2667): Optimize CI Runtime
		 - [PR 2654](https://github.com/open-quantum-safe/liboqs/pull/2654): fix(importer): skip empty SIG and KEM implementation targets
		 - [PR 2652](https://github.com/open-quantum-safe/liboqs/pull/2652): fix(sha3): align XKCP extraction parameters with dispatch header
		 - [PR 2643](https://github.com/open-quantum-safe/liboqs/pull/2643): refactor(qruov): deduplicate signature wrappers across implementations
		 - [PR 2642](https://github.com/open-quantum-safe/liboqs/pull/2642): refactor(qruov): use liboqs common AES backend
		 - [PR 2627](https://github.com/open-quantum-safe/liboqs/pull/2627): Fix out-of-bounds write in sha256 inc\_blocks on zero-block call
		 - [PR 2622](https://github.com/open-quantum-safe/liboqs/pull/2622): Replace relative link with absolute URL
		 - [PR 2621](https://github.com/open-quantum-safe/liboqs/pull/2621): lock secret key in xmss/xmssmt sigs\_remaining
		 - [PR 2593](https://github.com/open-quantum-safe/liboqs/pull/2593): Add SQIsign
		 - [PR 2449](https://github.com/open-quantum-safe/liboqs/pull/2449): Include constant-time analysis framework
	- Open PRs:
		 - [PR 2690](https://github.com/open-quantum-safe/liboqs/pull/2690): fix(sqisign) avoid POSIX ssize\_t to support Windows
		 - [PR 2689](https://github.com/open-quantum-safe/liboqs/pull/2689): Amend to #2536: Fix SHA3 first-use dispatch race
		 - [PR 2685](https://github.com/open-quantum-safe/liboqs/pull/2685): fix(qruov): migrate importer to official integration upstream
		 - [PR 2681](https://github.com/open-quantum-safe/liboqs/pull/2681): Add CI timing report workflow
		 - [PR 2680](https://github.com/open-quantum-safe/liboqs/pull/2680): CI: create issue for failed weekly tests
		 - [PR 2671](https://github.com/open-quantum-safe/liboqs/pull/2671): Document buffer requirements for OQS\_SIG\_STFL\_alg\_lms\_sign  `documentation`
		 - [PR 2666](https://github.com/open-quantum-safe/liboqs/pull/2666): CI: code coverage rework
		 - [PR 2665](https://github.com/open-quantum-safe/liboqs/pull/2665): Let ML-DSA Wycheproof verify vectors reach the library with wrong lengths
		 - [PR 2649](https://github.com/open-quantum-safe/liboqs/pull/2649): Switch astyle to clang-format for code formatting
		 - [PR 2633](https://github.com/open-quantum-safe/liboqs/pull/2633): Add test checking for  NULL guards after `OQS\_MEM\_malloc` calls
		 - [PR 2625](https://github.com/open-quantum-safe/liboqs/pull/2625): SLH-DSA SHA2: ~4–5× sign/verify speedup
		 - [PR 2624](https://github.com/open-quantum-safe/liboqs/pull/2624): Add RISC-V RVV (rv64gcv) implementation for ML-KEM
		 - [PR 2620](https://github.com/open-quantum-safe/liboqs/pull/2620): xmss: fail closed on partial lock tuple (like LMS)
		 - [PR 2616](https://github.com/open-quantum-safe/liboqs/pull/2616): Add a fuzz harness for the signature verification path
		 - [PR 2604](https://github.com/open-quantum-safe/liboqs/pull/2604): feat: Improve fuzzing build logic and LMS header lookup (#2602)
		 - [PR 2596](https://github.com/open-quantum-safe/liboqs/pull/2596): check signature length in xmssmt\_core\_sign\_open
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


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 867](https://github.com/open-quantum-safe/oqs-provider/issues/867): HQC-KEM TLS groups from draft-preussmattsson-tls-hqckem  `question`
		 - [Issue 797](https://github.com/open-quantum-safe/oqs-provider/issues/797): Release new oqs-provider version  `question`
		 - [Issue 514](https://github.com/open-quantum-safe/oqs-provider/issues/514): Static Analysis Issues   `bug` `help wanted`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 866](https://github.com/open-quantum-safe/oqs-provider/pull/866): Enforce buffer capacity checks in hybrid KEM encapsulation
		 - [PR 861](https://github.com/open-quantum-safe/oqs-provider/pull/861): Clear private key copies before freeing them
		 - [PR 855](https://github.com/open-quantum-safe/oqs-provider/pull/855): User-level hybrid algorithm disablement
		 - [PR 852](https://github.com/open-quantum-safe/oqs-provider/pull/852): Re-structure code points assignation
		 - [PR 819](https://github.com/open-quantum-safe/oqs-provider/pull/819): fix: resolve OpenSSL 4.1 ASN.1 APIs at runtime


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days:
		 - [Issue 205](https://github.com/open-quantum-safe/openssh/issues/205): CI rekey fails on liboqs main after Classic McEliece default-off (#2640)
		 - [Issue 199](https://github.com/open-quantum-safe/openssh/issues/199): Implement Hybrid OQS provider for side-by-side PQ expirmentation  `enhancement`
	- Merges in the last 7 days:
		 - [PR 207](https://github.com/open-quantum-safe/openssh/pull/207): sshhole exploit remediation
		 - [PR 206](https://github.com/open-quantum-safe/openssh/pull/206): kex: drop Classic McEliece to match liboqs default-off
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
		 - [PR 347](https://github.com/open-quantum-safe/www/pull/347): Language wrappers: add Kotlin - Android (liboqs-android)
	- Open PRs: None


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 29](https://github.com/open-quantum-safe/liboqs-cpp/pull/29): Make secret-key cleanup and replacement exception-safe


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 57](https://github.com/open-quantum-safe/liboqs-go/pull/57): Add GOVERNANCE.md file


11. **[liboqs-Java](https://github.com/open-quantum-safe/liboqs-java)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 38](https://github.com/open-quantum-safe/liboqs-java/pull/38): Make dispose idempotent and reject use after dispose
		 - [PR 37](https://github.com/open-quantum-safe/liboqs-java/pull/37): Handle null context and algorithm names without crashing the JVM
		 - [PR 36](https://github.com/open-quantum-safe/liboqs-java/pull/36): Sign a 64-byte mu in testAllSigs for ML-DSA-*-extmu
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
		 - [PR 318](https://github.com/open-quantum-safe/liboqs-rust/pull/318): fix: allow disabling the NTRU, MQOM and SNOVA algorithm families
		 - [PR 317](https://github.com/open-quantum-safe/liboqs-rust/pull/317): build(oqs-sys): add opt-in reproducible vendored builds
		 - [PR 316](https://github.com/open-quantum-safe/liboqs-rust/pull/316): fix: zeroize sensitive Rust-owned key material on drop
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
