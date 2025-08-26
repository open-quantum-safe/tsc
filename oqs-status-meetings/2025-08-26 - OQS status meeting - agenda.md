# 2025-08-26 - OQS status meeting - agenda

<span style="color: red;"> Tuesday August 26 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Welcome Bruce
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


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 198: [vote] Proposal for OQS Project Lifecycle stage


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 2239: Avoid invalid compiler options for MSVC
		 - PR 2250: Update license info for ML-KEM
		 - PR 2214: Upgrade Jinja to 3.1.6
		 - PR 2248: Disable testing on Travis CI
	- Open PRs:
		 - PR 2174: Initial addition of sqisign.
		 - PR 2176: Add NTRU back
		 - PR 2185: Add markdownlint to CI workflow to lint documentation
		 - PR 2206: Fix #2057 and some OpenSSL 3.x compatibility related issues
		 - PR 2207: Adding new hash variants to HSS/LMS
		 - PR 2221: Include DeriveEncapsulation functionality (Issue #2135)
		 - PR 2225: Improve random number generator security
		 - PR 2236: Move linux\_arm\_emulated to extended tests
		 - PR 2237: SLHDSA ACVP tests
		 - PR 2245: Replace SLH-DSA single call hash APIs with shims
		 - PR 2246: Fix permissions for poutine\_analysis job
		 - PR 2247: Update CROSS to version 2.2
		 - PR 2252: Change 64 bit add to 32 bit add to wrap on 32 bit counter for AES-CTR…


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 597: Add key-type specific en- / decoder
		 - PR 641: nit: Fix runtime dependent format issue in generate.sh and clean up python scripts
		 - PR 655: oqsprovider: allow building as shared library again
		 - PR 694: Update CROSS to version 2.2


4. **OQS-BoringSSL**


	- Merges in the last 7 days: None.
	- Open PRs: None


5. **OQS-OpenSSH**


	- Merges in the last 7 days: None.
	- Open PRs: None


6. **oqs-demos**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 379: Update OQS Release Tags 


7. **ci-containers**


	- Merges in the last 7 days: None.
	- Open PRs: None


8. **www.openquantumsafe.org**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 287: Bump \_includes/liboqs from `16b8629` to `1698d86`


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
		 - PR 117: Fix Windows DLL lookup: search both oqs.dll and liboqs.dll (Issue #108)
		 - PR 119: Version 0.14


13. **liboqs-Rust**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 260: feat: Auto-allocate stack in runtime
		 - PR 268: feat: update to liboqs 0.11.0 and various Rust changes
		 - PR 292: feat: implement FromStr for Algorithm Enums
		 - PR 295: feat:  Implemented the RustCrypto traits for signatures and kems (#137)
