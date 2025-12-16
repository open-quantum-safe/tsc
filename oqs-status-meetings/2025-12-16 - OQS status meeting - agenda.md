# 2025-12-16 - OQS status meeting - agenda

<span style="color: red;"> Tuesday December 16 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates & items seeking help

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


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 222: config cleanup
		 - PR 228: Meeting minutes 25-11-25


2. **liboqs**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 2185: Add markdownlint to CI workflow to lint documentation
		 - PR 2277: SQIsign integration
		 - PR 2284: mldsa-native integration
		 - PR 2298: Add build option for randomized ML-DSA signing
		 - PR 2303: Remove ACVP test vectors from repository
		 - PR 2312: Add the path to the binary include dir
		 - PR 2323: Fix small README issues
		 - PR 2328: Hqc update reference implementation 
		 - PR 2330: Fix incorrect arg register update in avx512 Keccak
		 - PR 2331: Bump the pip group across 2 directories with 1 update


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days:
		 - PR 716: Change remaining 'printf' to 'fprint(stderr'
	- Open PRs:
		 - PR 641: nit: Fix runtime dependent format issue in generate.sh and clean up python scripts
		 - PR 655: oqsprovider: allow building as shared library again
		 - PR 715: Updating Governance
		 - PR 722: fix issue 628 and change oqs\_test\_evp\_pkey\_params.c to use TEST\_ASSERT()
		 - PR 730: Expand 'oqs\_test\_kem' to perform encapsulation from pubkey only


4. **OQS-BoringSSL**


	- Merges in the last 7 days:
		 - PR 137: Various Updates
	- Open PRs: None


5. **OQS-OpenSSH**


	- Merges in the last 7 days: None.
	- Open PRs: None


6. **oqs-demos**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 379: Update OQS Release Tags 
		 - PR 380: Add plotly digital signatures visualization demo


7. **ci-containers**


	- Merges in the last 7 days: None.
	- Open PRs: None


8. **www.openquantumsafe.org**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 303: Replace ad-hoc API doc entirely with Doxygen
		 - PR 304: Bump \_includes/liboqs from `97f6b86` to `39ea281`


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
