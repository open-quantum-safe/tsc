# 2026-11-17 - OQS status meeting - agenda

<span style="color: red;"> Tuesday November 17 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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
		 - [PR 363](https://github.com/open-quantum-safe/tsc/pull/363): Add summary for OQS Status Meeting 10/11/2026
		 - [PR 361](https://github.com/open-quantum-safe/tsc/pull/361): Add agenda for OQS Status Meeting 10/11/2026
		 - [PR 333](https://github.com/open-quantum-safe/tsc/pull/333): [vote] Add caretaker formal procedure
	- Open PRs:
		 - [PR 364](https://github.com/open-quantum-safe/tsc/pull/364): Add agenda for TSC Meeting 24/11/2026
		 - [PR 362](https://github.com/open-quantum-safe/tsc/pull/362): Add Orlando as liboqs-rust Maintainer [vote]


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2702](https://github.com/open-quantum-safe/liboqs/issues/2702): ds\_benchmark.h RDTSC Bug in x86\_64
		 - [Issue 2701](https://github.com/open-quantum-safe/liboqs/issues/2701): Investigate MAYO signing slowdown with `OQS\_HARDENED\_COMPILE\_OPTS`
		 - [Issue 2700](https://github.com/open-quantum-safe/liboqs/issues/2700): Re-enable warnings as errors for exempted upstream code
		 - [Issue 2698](https://github.com/open-quantum-safe/liboqs/issues/2698): Test CI on the two most recent Ubuntu LTS releases
		 - [Issue 2697](https://github.com/open-quantum-safe/liboqs/issues/2697): libjade upstream repo change
		 - [Issue 2691](https://github.com/open-quantum-safe/liboqs/issues/2691): Triage  and analyze CT warnings
		 - [Issue 2687](https://github.com/open-quantum-safe/liboqs/issues/2687): Fuzz KEM encapsulation with mutated public keys
		 - [Issue 2662](https://github.com/open-quantum-safe/liboqs/issues/2662): Restrict admins overruling push limitations
		 - [Issue 2644](https://github.com/open-quantum-safe/liboqs/issues/2644): Inconsistência de tipo de parâmetro em função SHA-3 (XKCP) — liboqs 0.16.0
		 - [Issue 2619](https://github.com/open-quantum-safe/liboqs/issues/2619): SDitH: Allow option to re-use temporary/entropy space in signature wrapper
		 - [Issue 2143](https://github.com/open-quantum-safe/liboqs/issues/2143): Missing support for parameter sets that use SHA256/192 hashes from draft-fluhrer-lms-more-parm-sets  `help wanted`
		 - [Issue 1807](https://github.com/open-quantum-safe/liboqs/issues/1807): Extend constant-time testing  `wishlist`
	- Merges in the last 7 days:
		 - [PR 2705](https://github.com/open-quantum-safe/liboqs/pull/2705): Fix: add missing NULL guard in SQISign
		 - [PR 2696](https://github.com/open-quantum-safe/liboqs/pull/2696): SDitH: Remove the buffer reuse TODO
		 - [PR 2695](https://github.com/open-quantum-safe/liboqs/pull/2695): Bump the github-actions group across 1 directory with 3 updates  `dependencies` `github_actions`
		 - [PR 2693](https://github.com/open-quantum-safe/liboqs/pull/2693): CI: select test suites per platform and stage, and run a lighter scope on PRs
		 - [PR 2690](https://github.com/open-quantum-safe/liboqs/pull/2690): fix(sqisign) avoid POSIX ssize\_t to support Windows
		 - [PR 2652](https://github.com/open-quantum-safe/liboqs/pull/2652): fix(sha3): align XKCP extraction parameters with dispatch header
		 - [PR 2633](https://github.com/open-quantum-safe/liboqs/pull/2633): Add test checking for  NULL guards after `OQS\_MEM\_malloc` calls
	- Open PRs:
		 - [PR 2710](https://github.com/open-quantum-safe/liboqs/pull/2710): Fuzz KEM encapsulation with mutated public keys
		 - [PR 2709](https://github.com/open-quantum-safe/liboqs/pull/2709): Feat: update SLH-DSA to latest upstream (2026-11-04)
		 - [PR 2708](https://github.com/open-quantum-safe/liboqs/pull/2708): Fix: RDTSC Bug in x86\_64
		 - [PR 2707](https://github.com/open-quantum-safe/liboqs/pull/2707): vectors\_sig: run sigVer\_ext for SLH-DSA in builds without ML-DSA
		 - [PR 2706](https://github.com/open-quantum-safe/liboqs/pull/2706): Run SLH-DSA ACVP vectors for SHA2-512/224 and SHA2-512/256 pre-hash
		 - [PR 2704](https://github.com/open-quantum-safe/liboqs/pull/2704): Fix two CMP warnings in CMake >= 4.1 and 4.4
		 - [PR 2703](https://github.com/open-quantum-safe/liboqs/pull/2703): Fix strdup deprecated in MSVC CRT
		 - [PR 2699](https://github.com/open-quantum-safe/liboqs/pull/2699): Apply Hardened Default Compiler Options
		 - [PR 2694](https://github.com/open-quantum-safe/liboqs/pull/2694): Refactor OQS\_*\_set\_callbacks instead of C\_OR\_NI\_OR\_ARM macros
		 - [PR 2692](https://github.com/open-quantum-safe/liboqs/pull/2692): Update HQC to v5.1.0  `enhancement`
		 - [PR 2689](https://github.com/open-quantum-safe/liboqs/pull/2689): Amend to #2536: Fix SHA3 first-use dispatch race
		 - [PR 2685](https://github.com/open-quantum-safe/liboqs/pull/2685): fix(qruov): migrate importer to official integration upstream
		 - [PR 2681](https://github.com/open-quantum-safe/liboqs/pull/2681): Add CI timing report workflow
		 - [PR 2680](https://github.com/open-quantum-safe/liboqs/pull/2680): CI: create issue for failed weekly tests
		 - [PR 2671](https://github.com/open-quantum-safe/liboqs/pull/2671): Document buffer requirements for OQS\_SIG\_STFL\_alg\_lms\_sign  `documentation`
		 - [PR 2666](https://github.com/open-quantum-safe/liboqs/pull/2666): CI: code coverage rework
		 - [PR 2665](https://github.com/open-quantum-safe/liboqs/pull/2665): Let ML-DSA Wycheproof verify vectors reach the library with wrong lengths
		 - [PR 2649](https://github.com/open-quantum-safe/liboqs/pull/2649): Switch astyle to clang-format for code formatting
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
		 - [Issue 879](https://github.com/open-quantum-safe/oqs-provider/issues/879): CI: Remove support for unsupported OpenSSL versions
		 - [Issue 876](https://github.com/open-quantum-safe/oqs-provider/issues/876): CI: flag changes to the registered algorithm, TLS group and sigalg lists between releases
		 - [Issue 875](https://github.com/open-quantum-safe/oqs-provider/issues/875): Align BC/OQS (O)IDs
		 - [Issue 874](https://github.com/open-quantum-safe/oqs-provider/issues/874): Test 11 (multi-thread) fails on OpenSSL-4  `bug`
		 - [Issue 871](https://github.com/open-quantum-safe/oqs-provider/issues/871): OpenSSL >= 3.5: the runtime filter turns off method caching for all oqsprovider algorithms, and there is no opt-in to keep the liboqs ML-DSA/ML-KEM
		 - [Issue 867](https://github.com/open-quantum-safe/oqs-provider/issues/867): HQC-KEM TLS groups from draft-preussmattsson-tls-hqckem  `question`
		 - [Issue 856](https://github.com/open-quantum-safe/oqs-provider/issues/856): complete 0.12.0 release cycle
		 - [Issue 847](https://github.com/open-quantum-safe/oqs-provider/issues/847): Split out support for hybrid algorithms  `question`
		 - [Issue 821](https://github.com/open-quantum-safe/oqs-provider/issues/821): Remove support for standardized algorithms
		 - [Issue 792](https://github.com/open-quantum-safe/oqs-provider/issues/792): Handling of "caching" behavior in `oqsprovider\_query`  `question`
		 - [Issue 675](https://github.com/open-quantum-safe/oqs-provider/issues/675): Use of a 'seed' parameter for deterministic key pair generation  `enhancement` `won't fix`
		 - [Issue 613](https://github.com/open-quantum-safe/oqs-provider/issues/613): ML-KEM private keys not compatible with draft-ietf-lamps-kyber-certificates-06 (seed as private key)  `enhancement`
		 - [Issue 612](https://github.com/open-quantum-safe/oqs-provider/issues/612): Add cross-provider interop tests  `help wanted` `futurework`
		 - [Issue 561](https://github.com/open-quantum-safe/oqs-provider/issues/561): Re-assign all code points  `help wanted`
		 - [Issue 560](https://github.com/open-quantum-safe/oqs-provider/issues/560): Multiple names for an algorithm  `enhancement` `good first issue`
		 - [Issue 488](https://github.com/open-quantum-safe/oqs-provider/issues/488): Testing in openssl 3.1/3.0  `good first issue` `help wanted`
	- Merges in the last 7 days:
		 - [PR 872](https://github.com/open-quantum-safe/oqs-provider/pull/872): oqsprov: let the core cache the algorithm tables on OpenSSL >= 3.5
		 - [PR 869](https://github.com/open-quantum-safe/oqs-provider/pull/869): complete 0.12.0 release cycle
		 - [PR 852](https://github.com/open-quantum-safe/oqs-provider/pull/852): Re-structure code points assignation
	- Open PRs:
		 - [PR 878](https://github.com/open-quantum-safe/oqs-provider/pull/878): drop wrong mlkem hybrid OIDs
		 - [PR 877](https://github.com/open-quantum-safe/oqs-provider/pull/877): updating UOV & integrating SDitH, FAEST, SQIsign, SNOVA
		 - [PR 870](https://github.com/open-quantum-safe/oqs-provider/pull/870): std alg deprecation notice (821) [skip ci]
		 - [PR 866](https://github.com/open-quantum-safe/oqs-provider/pull/866): Enforce buffer capacity checks in hybrid KEM encapsulation and decapsulation
		 - [PR 861](https://github.com/open-quantum-safe/oqs-provider/pull/861): Clear private key copies before freeing them
		 - [PR 855](https://github.com/open-quantum-safe/oqs-provider/pull/855): User-level hybrid algorithm disablement
		 - [PR 819](https://github.com/open-quantum-safe/oqs-provider/pull/819): fix: resolve OpenSSL 4.1 ASN.1 APIs at runtime


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days:
		 - [Issue 211](https://github.com/open-quantum-safe/openssh/issues/211): OQS-v10: kexgen.c fails with GCC 14: kex\_reset\_keys has no prototype in kex.h
		 - [Issue 210](https://github.com/open-quantum-safe/openssh/issues/210): OQS-v10: ssh-oqs.c fails with GCC 14: implicit declaration of sshkey\_clear\_pkey
		 - [Issue 208](https://github.com/open-quantum-safe/openssh/issues/208): CI VM: `dragonflybsd-6.4.2` dies before build (`sudo` needs `libcrypto.so.17`)
		 - [Issue 201](https://github.com/open-quantum-safe/openssh/issues/201): Hybrid signatures bypass sshkey\_check\_sigtype post-sign validation
		 - [Issue 150](https://github.com/open-quantum-safe/openssh/issues/150): Memory leaks in oqs ecdh path
	- Merges in the last 7 days:
		 - [PR 204](https://github.com/open-quantum-safe/openssh/pull/204): Teach sshkey\_check\_sigtype about OQS hybrid framing
		 - [PR 203](https://github.com/open-quantum-safe/openssh/pull/203): Fix memory leaks in OQS hybrid ECDH KEX path
	- Open PRs:
		 - [PR 209](https://github.com/open-quantum-safe/openssh/pull/209): ci: fix DragonFly after Avalon openssl 3.5 `libcrypto` SONAME bump


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- Issues with activity in the last 7 days:
		 - [Issue 406](https://github.com/open-quantum-safe/oqs-demos/issues/406): Create automation to inform upstream about integration problems unearthed
	- Merges in the last 7 days:
		 - [PR 405](https://github.com/open-quantum-safe/oqs-demos/pull/405): move curl to experimental algs still supported by oqsprovider
		 - [PR 403](https://github.com/open-quantum-safe/oqs-demos/pull/403): Update H2load to Latest OQS Releases
	- Open PRs:
		 - [PR 407](https://github.com/open-quantum-safe/oqs-demos/pull/407): CI: report upstream integration failures
		 - [PR 404](https://github.com/open-quantum-safe/oqs-demos/pull/404): Fix build\_main flag so scheduled CI builds against liboqs/oqs-provider main
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
	- Open PRs: None


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 30](https://github.com/open-quantum-safe/liboqs-cpp/pull/30): Add GOVERNANCE file
		 - [PR 29](https://github.com/open-quantum-safe/liboqs-cpp/pull/29): Make secret-key cleanup and replacement exception-safe


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
	- Open PRs:
		 - [PR 1](https://github.com/open-quantum-safe/liboqs-js/pull/1): Add GOVERNANCE file


13. **[liboqs-Python](https://github.com/open-quantum-safe/liboqs-python)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 164](https://github.com/open-quantum-safe/liboqs-python/pull/164): Add GOVERNANCE file
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
