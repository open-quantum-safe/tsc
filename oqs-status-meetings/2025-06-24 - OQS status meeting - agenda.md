# 2025-06-24 - OQS status meeting - agenda

<span style="color: red;"> Tuesday June 24 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Thank you, Pravek and Spencer
2. Status updates

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
		 - PR 188: Change OQS TSC meeting times for July and August
		 - PR 187: Add agenda for OQS status meeting 2025-06-17
	- Open PRs: None


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 2168: Benchmarking comments only on alerts
		 - PR 2148: Adding code coverage
		 - PR 2171: Zeroize memory in SHA3 implementation
		 - PR 2167: Add AVX512VL-Optimized SHA3/SHAKE Implementations
	- Open PRs:
		 - PR 2138: Adding poutine SAST
		 - PR 2172: update ACVP to 1.1.0.40
		 - PR 2174: Initial addition of sqisign.
		 - PR 2175: Integrate SLH-DSA-C Library


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days: None.
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


	- Merges in the last 7 days:
		 - PR 372: Update various demos
		 - PR 375: Update Wireshark Dockerfile dependencies
	- Open PRs: None


7. **ci-containers**


	- Merges in the last 7 days: None.
	- Open PRs: None


8. **www.openquantumsafe.org**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 280: Bump \_includes/liboqs from `8d9cfd7` to `50185c6`


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
		 - PR 110: Add PEP 561 type stubs (.pyi) for oqs package
		 - PR 111: Use OQS\_SIG\_supports\_ctx\_str for context support detection and fix CI build


13. **liboqs-Rust**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 260: feat: Auto-allocate stack in runtime
		 - PR 268: feat: update to liboqs 0.11.0 and various Rust changes
