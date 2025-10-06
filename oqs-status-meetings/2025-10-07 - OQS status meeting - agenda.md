# 2025-10-07 - OQS status meeting - agenda

<span style="color: red;"> Tuesday October 07 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates
2. 0.15.0 release planning

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


	- Merges in the last 7 days:
		 - PR 210: Add Pablo to config.yml
		 - PR 209: Add agenda for 2025-09-30 status meeting
	- Open PRs:
		 - PR 205: [vote draft] Voting procedure


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 2288: Fix/icicle ml kem 768
		 - PR 2293: Fix incorrect Actual signature length (0) in sig fullcycle speed test
		 - PR 2286: More readable algorithm support in README.md
		 - PR 2285: Fixes for Weekly Test Failures
		 - PR 2290: Replace SPHINCS+ with SLH-DSA for OQS\_ALGS\_ENABLED=STD
	- Open PRs:
		 - PR 2185: Add markdownlint to CI workflow to lint documentation
		 - PR 2207: Adding new hash variants to HSS/LMS
		 - PR 2277: SQIsign integration
		 - PR 2284: [DRAFT] mldsa-native integration
		 - PR 2294: update no-pass explanation for CT testing [skip ci]
		 - PR 2295: [WIP] 0.15.0 release candidate 1


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days:
		 - PR 707: follow upstream and fixup Composites removal
		 - PR 708: Add Brainpool hybrid KEM support
		 - PR 710: remove CircleCI support
	- Open PRs:
		 - PR 641: nit: Fix runtime dependent format issue in generate.sh and clean up python scripts
		 - PR 655: oqsprovider: allow building as shared library again
		 - PR 706: fix code point mismatch


4. **OQS-BoringSSL**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 137: Various Updates


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
		 - PR 295: Bump \_includes/liboqs from `dd942d4` to `9a61d90`


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
		 - PR 123: chore: publish to PyPi


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
