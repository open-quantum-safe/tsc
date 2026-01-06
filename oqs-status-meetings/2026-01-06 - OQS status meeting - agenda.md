# 2026-01-06 - OQS status meeting - agenda

<span style="color: red;"> Tuesday January 06 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

0. Happy new year!
1. Status updates & items seeking help
2. [Priority setting for liboqs 0.16.0](https://github.com/orgs/open-quantum-safe/discussions/2309)

## OQS subprojects

1. OQS Technical Steering Committee
2. liboqs
3. OQS-OpenSSL 3 provider
4. OQS-BoringSSL
5. OQS-OpenSSH
6. oqs-demos
7. ci-containers
8. www.openquantumsafe.org
9. liboqs language wrappers: liboqs-C++, liboqs-Go, liboqs-Java, liboqs-Python, liboqs-Rust

## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **OQS Technical Steering Committee**

   Next OQS TSC meeting: Tuesday January 13

	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 222: config cleanup
		 - PR 230: Add Andrew Younkers and Alex Harrison as release managers on OpenSSH fork


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 2333: Docs: List all optimized implementations
		 - PR 2331: Update Python modules
		 - PR 2330: Fix incorrect arg register update in avx512 Keccak
	- Open PRs:
		 - PR 2277: SQIsign integration
		 - PR 2284: mldsa-native integration
		 - PR 2298: Add build option for randomized ML-DSA signing
		 - PR 2303: Remove ACVP test vectors from repository
		 - PR 2312: Add the path to the binary include dir
		 - PR 2328: Hqc update reference implementation 


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 641: nit: Fix runtime dependent format issue in generate.sh and clean up python scripts
		 - PR 655: oqsprovider: allow building as shared library again
		 - PR 715: Updating Governance
		 - PR 730: Expand 'oqs\_test\_kem' to perform encapsulation from pubkey only
		 - PR 731: Add 'sign/verify\_message' interface
		 - PR 732: Add "Pure" Stateless Hash-Based Algorithms (SLH-DSA-*) Support
		 - PR 735: oqs\_provider. Enable Algo Fetch Cache mechanism only for OpenSSL v3.5.0 or newer.


4. **OQS-BoringSSL**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 139: Add "Pure" Stateless Hash-Based Algorithms (SLH-DSA-*) Support


5. **OQS-OpenSSH**


	- Merges in the last 7 days:
		 - PR 184: Fix NULL pointer crash in OQS KEM encaps/decaps error handling
	- Open PRs:
		 - PR 186: Uplift OQS-SSH to OpenSSH 10\_2\_P1


6. **oqs-demos**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 379: Update OQS Release Tags 
		 - PR 380: Add plotly digital signatures visualization demo


7. **ci-containers**


	- Merges in the last 7 days: None.
	- Open PRs: None


8. **www.openquantumsafe.org**


	- Merges in the last 7 days:
		 - PR 307: Bump just-the-docs from 0.10.1 to 0.11.1
		 - PR 306: Bump \_includes/liboqs from `97f6b86` to `589731b`
		 - PR 305: Add Dart wrapper to third-party language wrappers
	- Open PRs:
		 - PR 303: Replace ad-hoc API doc entirely with Doxygen


9. **liboqs-C++**


	- Merges in the last 7 days: None.
	- Open PRs: None


10. **liboqs-Go**


	- Merges in the last 7 days: None.
	- Open PRs: None


11. **liboqs-Java**


	- Merges in the last 7 days: None.
	- Open PRs: None


12. **liboqs-Python**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 94: replacing openssl111 with openssl3
		 - PR 119: Version 0.14
		 - PR 130: Update STFL pipeline


13. **liboqs-Rust**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 260: feat: Auto-allocate stack in runtime
		 - PR 268: feat: update to liboqs 0.11.0 and various Rust changes
		 - PR 295: feat:  Implemented the RustCrypto traits for signatures and kems (#137)
		 - PR 297: feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - PR 298: fix: support compiling on Windows ARM64
		 - PR 299: feat: add Android CMake configuration patch
		 - PR 300: CI on Windows arm64
		 - PR 303: chore(ci): bump the actions group across 1 directory with 2 updates
