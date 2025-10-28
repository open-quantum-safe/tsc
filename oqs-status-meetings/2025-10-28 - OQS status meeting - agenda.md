# 2025-10-28 - OQS status meeting - agenda

<span style="color: red;"> Tuesday October 28 at 10:00 AM </span> US Eastern Time / 3:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates
2. liboqs 0.15.0 release

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
		 - PR 217: meeting minutes  2025-10-21
		 - PR 214: Minutes from OQS TSC meeting 2025-09-16
	- Open PRs:
		 - PR 205: [vote draft] Voting procedure


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 2295: 0.15.0 release candidate 1
	- Open PRs:
		 - PR 2185: Add markdownlint to CI workflow to lint documentation
		 - PR 2207: Adding new hash variants to HSS/LMS
		 - PR 2277: SQIsign integration
		 - PR 2284: [DRAFT] mldsa-native integration
		 - PR 2298: Add build option for randomized ML-DSA signing
		 - PR 2303: Remove ACVP test vectors from repository
		 - PR 2306: Make pull request hyperlink format consistent


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 641: nit: Fix runtime dependent format issue in generate.sh and clean up python scripts
		 - PR 655: oqsprovider: allow building as shared library again
		 - PR 706: fix code point mismatch
		 - PR 711: Fix 'enable\_tls' SIG algorithm mismatch


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


	- Merges in the last 7 days:
		 - PR 97: Add Python requests to alpine and ubuntu-jammy Dockerfile
		 - PR 98: Automate building Alpine Linux CI image in GitHub Action
	- Open PRs: None


8. **www.openquantumsafe.org**


	- Merges in the last 7 days:
		 - PR 297: Bump \_includes/liboqs from `b02d0c9` to `52169a1`
	- Open PRs:
		 - PR 298: Bump \_includes/liboqs from `52169a1` to `ed5c2cc`


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
		 - PR 301: chore(ci): bump KyleMayes/install-llvm-action from 2.0.7 to 2.0.8 in the actions group
