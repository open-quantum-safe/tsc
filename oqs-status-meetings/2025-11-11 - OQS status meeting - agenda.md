# 2025-11-11 - OQS status meeting - agenda

<span style="color: red;"> Tuesday November 11 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (<https://pqca.org/calendar/>)

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

See project dashboard at: <https://openquantumsafe.org/dashboard.html>

1. **OQS Technical Steering Committee**

	- Merges in the last 7 days:
	  - PR 219: Add OQS status meeting agenda 2025-11-04
	  - PR 220: Add AI meeting summary for OQS status meeting 2025-11-04
	- Open PRs:
	  - PR 205: [vote draft] Voting procedure
	  - PR 222: config cleanup

2. **liboqs**

	- Merges in the last 7 days:
	  - PR 2315: OQS Builder: an attempt "copy from upstream 2.0"
	  - PR 2308: Alpine Linux is distinct from Ubuntu/Debian because Alpine's standard…
	  - PR 2310: Add missing LMS macros. Correct typo.
	- Open PRs:
	  - PR 2185: Add markdownlint to CI workflow to lint documentation
	  - PR 2277: SQIsign integration
	  - PR 2284: [DRAFT] mldsa-native integration
	  - PR 2298: Add build option for randomized ML-DSA signing
	  - PR 2303: Remove ACVP test vectors from repository
	  - PR 2312: Add the path to the binary include dir
	  - PR 2317: liboqs 0.15.0 release candidate 2
	- Issues/PRs to draw attention to:
	  - Issue 2192: Include both variants FrodoKEM
	  - Issue 2314: Sporadic errors in FrodoKEM on PPC
	  - PR 2303: Remove ACVP test vectors from repository

3. **OQS-OpenSSL 3 provider**

	- Merges in the last 7 days:
	  - PR 713: updating committers due to (in)activity [skip ci]
	- Open PRs:
	  - PR 641: nit: Fix runtime dependent format issue in generate.sh and clean up python scripts
	  - PR 655: oqsprovider: allow building as shared library again
	  - PR 715: Updating Governance
	  - PR 716: Change remaining 'printf' to 'fprint(stderr'

4. **OQS-BoringSSL**

	- Merges in the last 7 days: None.
	- Open PRs:
	  - PR 137: Various Updates
	- Issues/PRs to draw attention to:
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

	- Merges in the last 7 days:
	  - PR 299: Bump \_includes/liboqs from `52169a1` to `46e2719`
	- Open PRs:
	  - PR 300: Bump \_includes/liboqs from `46e2719` to `08d56e9`

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
