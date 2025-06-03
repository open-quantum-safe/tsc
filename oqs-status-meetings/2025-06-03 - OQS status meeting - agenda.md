# 2025-06-03 - OQS status meeting - agenda

<span style="color: red;"> Tuesday June 03 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates
2. Mentorship project ideas
	- signature on-ramp
	- language wrappers
	- test vectors
	- Java JCE

## OQS subprojects

1. OQS Technical Steering Committee
2. liboqs
3. OQS-OpenSSL 3 provider
4. OQS-BoringSSL
5. OQS-OpenSSH
6. oqs-demos
7. profiling
8. ci-containers
9. www.openquantumsafe.org
10. liboqs language wrappers: liboqs-C++, liboqs-Go, liboqs-Java, liboqs-Python, liboqs-Rust

## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **OQS Technical Steering Committee**


	- Merges in the last 7 days: None.
	- Open PRs: None


2. **liboqs**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 2072: Add code coverage tests
		 - PR 2133: test: Add basic kem fuzz testing
		 - PR 2134: Continuous Benchmarking using Github Actions
		 - PR 2138: Adding poutine SAST
		 - PR 2145: Wycheproof
		 - PR 2146: Draft: Update mlkem-native to v1.0.0
		 - PR 2148: Adding code coverage
		 - PR 2149: test: Use secure free for freeing secret key objects
		 - PR 2151: Check for NULL dereference before using secure free
		 - PR 2152: tests: Remove unused variables
		 - PR 2153: tests: Check OQS\_STATUS of RNG and fstore functions


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days:
		 - PR 674: Add SNOVA signatures
		 - PR 681: 0.9.0 release
	- Open PRs:
		 - PR 597: Add key-type specific en- / decoder
		 - PR 641: nit: Fix runtime dependent format issue in generate.sh and clean up python scripts
		 - PR 655: oqsprovider: allow building as shared library again
		 - PR 672: Hide all symbols except for OSSL\_provider\_init entrypoint


4. **OQS-BoringSSL**


	- Merges in the last 7 days: None.
	- Open PRs: None


5. **OQS-OpenSSH**


	- Merges in the last 7 days: None.
	- Open PRs: None


6. **oqs-demos**


	- Merges in the last 7 days: None.
	- Open PRs: None


7. **profiling**


	- Merges in the last 7 days: None.
	- Open PRs: None


8. **ci-containers**


	- Merges in the last 7 days: None.
	- Open PRs: None


9. **www.openquantumsafe.org**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 275: Adding benchmarking page
		 - PR 276: Bump \_includes/liboqs from `b75bfb8` to `51bf0b6`


10. **liboqs-C++**


	- Merges in the last 7 days: None.
	- Open PRs: None


11. **liboqs-Go**


	- Merges in the last 7 days: None.
	- Open PRs: None


12. **liboqs-Java**


	- Merges in the last 7 days: None.
	- Open PRs: None


13. **liboqs-Python**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 94: replacing openssl111 with openssl3
		 - PR 110: Add PEP 561 type stubs (.pyi) for oqs package
		 - PR 111: Use OQS\_SIG\_supports\_ctx\_str for context support detection and fix CI build


14. **liboqs-Rust**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 260: feat: Auto-allocate stack in runtime
		 - PR 268: feat: update to liboqs 0.11.0 and various Rust changes
