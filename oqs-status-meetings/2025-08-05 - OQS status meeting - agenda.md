# 2025-08-05 - OQS status meeting - agenda

<span style="color: red;"> Tuesday August 05 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates

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
		 - PR 195: Update agenda
		 - PR 194: Add status call agendas
		 - PR 192: Add TSC minutes from 2025-07-08
	- Open PRs: None


2. **liboqs**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 2174: Initial addition of sqisign.
		 - PR 2175: Integrate SLH-DSA-C Library
		 - PR 2176: Add NTRU back
		 - PR 2185: Add markdownlint to CI workflow to lint documentation
		 - PR 2200: feat: implement automatic CI triggering based on git diff
		 - PR 2206: Fix #2057 and some OpenSSL 3.x compatibility related issues
		 - PR 2207: Adding new hash variants to HSS/LMS
		 - PR 2212: Change Nix install action to verified
		 - PR 2214: Upgrade Jinja to 3.1.6
		 - PR 2216: Icicle-pqc integration
		 - PR 2217: Fix code scanning workflow
		 - PR 2218: Add Classic McEliece sanitization patch 
		 - PR 2221: Include DeriveEncapsulation functionality (Issue #2135)
		 - PR 2222: Test mldsa-native integration
		 - PR 2223: Added dilithium3 derand keypair from seed
		 - PR 2225: Improve random number generator security


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days:
		 - PR 689: Release Candidate 0.10.0
		 - PR 691: Update RELEASE.md
		 - PR 693: Update CMakeLists.txt
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
	- Open PRs:
		 - PR 379: Update OQS Release Tags 


7. **ci-containers**


	- Merges in the last 7 days: None.
	- Open PRs: None


8. **www.openquantumsafe.org**


	- Merges in the last 7 days:
		 - PR 283: Bump \_includes/liboqs from `94b421e` to `78e2389`
		 - PR 284: Update OQS-Provider 0.10.0
	- Open PRs:
		 - PR 285: Bump \_includes/liboqs from `78e2389` to `01de36c`


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
		 - PR 115: Fix 'No such file or directory' when ctu.find\_library don't find anything
		 - PR 116: UpdateV14
		 - PR 117: Fix Windows DLL lookup: search both oqs.dll and liboqs.dll (Issue #108)


13. **liboqs-Rust**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 260: feat: Auto-allocate stack in runtime
		 - PR 268: feat: update to liboqs 0.11.0 and various Rust changes
		 - PR 292: feat: implement FromStr for Algorithm Enums
