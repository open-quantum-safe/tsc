# 2026-02-10 - OQS status meeting - agenda

<span style="color: red;"> Tuesday February 10 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates & items seeking help
2. [liboqs 0.16.0 prioritization](https://github.com/orgs/open-quantum-safe/projects/11/views/1)

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
		 - PR 237: Feb 3, 2026 OQS status meeting agenda
	- Open PRs:
		 - PR 234: Guidelines on algorithm inclusion in OQS
	- Open issues:
		- Issue 238: [vote] Accept liboqs-node as an OQS subproject


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 2359: Make fuzzers tolerant to disabled algorithms
		 - PR 2352: Add external-mu sign gen ACVP tests
		 - PR 2339: Remove SPHINCS+
	- Open PRs:
		 - PR 2277: SQIsign integration
		 - PR 2298: Add build option for randomized ML-DSA signing
		 - PR 2328: Hqc update reference implementation 
		 - PR 2342: Add both variants of frodokem
		 - PR 2356: sntrup761: replace PQClean code with public domain OpenSSH code
		 - PR 2361: Add MQOM
		 - PR 2362: Add support for ML-DSA pre-hash sign ACVP test vectors


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days:
		 - PR 742: Use accessors for ASN1\_STRING types
		 - PR 739: Add sign/verify message API from 3.4.0 onwards
	- Open PRs:
		 - PR 641: nit: Fix runtime dependent format issue in generate.sh and clean up python scripts
		 - PR 655: oqsprovider: allow building as shared library again
		 - PR 747: Add test for context strings in signatures


4. **OQS-BoringSSL**


	- Merges in the last 7 days: None.
	- Open PRs: None


5. **OQS-OpenSSH**


	- Merges in the last 7 days:
		 - PR 187: Update README.md and add GOVERNANCE.md
	- Open PRs: None


6. **oqs-demos**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 380: Add plotly digital signatures visualization demo


7. **ci-containers**


	- Merges in the last 7 days: None.
	- Open PRs: None


8. **www.openquantumsafe.org**


	- Merges in the last 7 days:
		 - PR 312: Bump \_includes/liboqs from `30edf7b` to `c58e93e`
	- Open PRs: None


9. **liboqs-C++**


	- Merges in the last 7 days: None.
	- Open PRs: None


10. **liboqs-Go**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 50: Fix for #49 and verification against liboqs 0.15.0


11. **liboqs-Java**


	- Merges in the last 7 days: None.
	- Open PRs: None


12. **liboqs-Python**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 94: replacing openssl111 with openssl3
		 - PR 119: Version 0.14
		 - PR 130: Update STFL pipeline
		 - PR 132: Update liboqs version to 0.15.0.


13. **liboqs-Rust**


	- Merges in the last 7 days:
		 - PR 305: chore: add contributor to readme and fix ci
	- Open PRs:
		 - PR 260: feat: Auto-allocate stack in runtime
		 - PR 295: feat:  Implemented the RustCrypto traits for signatures and kems (#137)
		 - PR 297: feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - PR 298: fix: support compiling on Windows ARM64
		 - PR 299: feat: add Android CMake configuration patch
		 - PR 300: CI on Windows arm64
		 - PR 303: chore(ci): bump the actions group across 1 directory with 2 updates
