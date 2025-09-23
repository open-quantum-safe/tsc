# 2025-09-23 - OQS status meeting - agenda

<span style="color: red;"> Tuesday September 23 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates
2. [liboqs 0.15.0 release planning](https://github.com/open-quantum-safe/liboqs/milestone/29)
3. [liboqs .NET language wrapper proposal](https://github.com/orgs/open-quantum-safe/discussions/2278)

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
		 - PR 203: Add saitomst to CODEOWNERS for liboqs NTRU implementation
		 - PR 204: [vote] Allow contributions to OQS-OpenSSH using upstream license
	- Open PRs:
		 - PR 205: [vote draft] Voting procedure


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 2276: Moving continuous benchmarking to weekly tests
		 - PR 2269: Add guidance / questions on generative AI use
		 - PR 2261: add content:read permission to scorecard workflow
		 - PR 2273: Link to contribution wishlist from CONTRIBUTING.md [skip ci]
		 - PR 2275: Remove Dilithium
	- Open PRs:
		 - PR 2185: Add markdownlint to CI workflow to lint documentation
		 - PR 2207: Adding new hash variants to HSS/LMS
		 - PR 2245: Replace SLH-DSA single call hash APIs with shims
		 - PR 2264: Disable strict aliasing on SPHINCS+-SHAKE
		 - PR 2277: SQIsign integration
		 - PR 2281: Fix typo in test\_kem


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 641: nit: Fix runtime dependent format issue in generate.sh and clean up python scripts
		 - PR 655: oqsprovider: allow building as shared library again
		 - PR 703: Add Brainpool hybrid KEMs support


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
		 - PR 380: Add plotly digital signatures visualization demo


7. **ci-containers**


	- Merges in the last 7 days: None.
	- Open PRs: None


8. **www.openquantumsafe.org**


	- Merges in the last 7 days: None.
	- Open PRs: None


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
