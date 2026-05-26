# 2026-05-26 - OQS status meeting - agenda

<span style="color: red;"> Tuesday May 26 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Discussion with HQC team
2. Status updates & items seeking help

## OQS subprojects

1. OQS Technical Steering Committee
2. liboqs
3. OQS-OpenSSL 3 provider
4. OQS-OpenSSH
5. OQS-BoringSSL
6. oqs-demos
7. ci-containers
8. www.openquantumsafe.org
9. liboqs language wrappers: liboqs-C++, liboqs-Go, liboqs-Java, liboqs-js, liboqs-Python, liboqs-Rust


## Project board: [0.16.0 prioritization](https://github.com/orgs/open-quantum-safe/projects/11)

**In progress**
- [Issue 2118](https://github.com/open-quantum-safe/liboqs/issues/2118): Update HQC implementation to 2025/02/19 version (liboqs)
- [PR 2407](https://github.com/open-quantum-safe/liboqs/pull/2407): Update HQC implementation to 2025-08-22 version (liboqs)
- [PR 2431](https://github.com/open-quantum-safe/liboqs/pull/2431): Implement value barrier and apply to FrodoKEM (liboqs)

**Ready**
- [Issue 2405](https://github.com/open-quantum-safe/liboqs/issues/2405): Mention FrodoKEM algorithm change in 0.16.0 release notes (liboqs)

**Backlog**
- [Issue 2436](https://github.com/open-quantum-safe/liboqs/issues/2436): Investigate weekly build failures (liboqs)



## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **[OQS Technical Steering Committee](https://github.com/open-quantum-safe/tsc)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 287](https://github.com/open-quantum-safe/tsc/pull/287): Add agenda for TSC Meeting 02/06/2026
		 - [PR 286](https://github.com/open-quantum-safe/tsc/pull/286): Add summary for OQS status meeting 2026-05-19
		 - [PR 285](https://github.com/open-quantum-safe/tsc/pull/285): Add agenda for OQS Status Meeting 19/05/2026
	- Open PRs: None


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2437](https://github.com/open-quantum-safe/liboqs/issues/2437): API hygiene: OQS\_STATUS enum vs mlkem-native return values + accel branches missing on *\_derand variants
		 - [Issue 1785](https://github.com/open-quantum-safe/liboqs/issues/1785): Add documentation Markdown linter to CI  `enhancement` `good first issue`
	- Merges in the last 7 days:
		 - [PR 2444](https://github.com/open-quantum-safe/liboqs/pull/2444): Bump the pip group across 2 directories with 2 updates  `dependencies` `python`
		 - [PR 2443](https://github.com/open-quantum-safe/liboqs/pull/2443): Bump github/codeql-action from 4.35.4 to 4.35.5 in the github-actions group  `dependencies` `github_actions`
		 - [PR 2440](https://github.com/open-quantum-safe/liboqs/pull/2440): Bump idna from 3.10 to 3.15 in /.github/workflows  `dependencies` `python`
		 - [PR 2439](https://github.com/open-quantum-safe/liboqs/pull/2439): Bump idna from 3.10 to 3.15 in /scripts/copy\_from\_upstream  `dependencies` `python`
		 - [PR 2438](https://github.com/open-quantum-safe/liboqs/pull/2438): Fix comments in SHA3 AVX512VL assembly file  `documentation`
		 - [PR 2435](https://github.com/open-quantum-safe/liboqs/pull/2435): Add NIST LMS Signature verify KATs
	- Open PRs:
		 - [PR 2446](https://github.com/open-quantum-safe/liboqs/pull/2446): Add Markdown documentation linting
		 - [PR 2445](https://github.com/open-quantum-safe/liboqs/pull/2445): Update mldsa-native to v1.0.0-beta2
		 - [PR 2442](https://github.com/open-quantum-safe/liboqs/pull/2442): fix: incorrect incremental absorption in AVX512VL impl of SHA3-512
		 - [PR 2441](https://github.com/open-quantum-safe/liboqs/pull/2441): Add updated information regarding algorithm support
		 - [PR 2431](https://github.com/open-quantum-safe/liboqs/pull/2431): Implement value barrier and apply to FrodoKEM
		 - [PR 2417](https://github.com/open-quantum-safe/liboqs/pull/2417): Build script to build liboqs
		 - [PR 2415](https://github.com/open-quantum-safe/liboqs/pull/2415): ci: add CodeQL query to enforce OpenSSL return code handling (#1867)
		 - [PR 2407](https://github.com/open-quantum-safe/liboqs/pull/2407): Update HQC implementation to 2025-08-22 version  `needs review` `focus`
		 - [PR 2387](https://github.com/open-quantum-safe/liboqs/pull/2387): Adapt/Fix latest Wycheproof tests
		 - [PR 2386](https://github.com/open-quantum-safe/liboqs/pull/2386): Add missing ACVP tests [ML-KEM]
		 - [PR 2366](https://github.com/open-quantum-safe/liboqs/pull/2366): Add API support for External-MU Signature[ML-DSA]
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- Issues with activity in the last 7 days:
		 - [Issue 780](https://github.com/open-quantum-safe/oqs-provider/issues/780): API hygiene: implicit success encoding in oqs\_evp\_kem\_encaps\_keyslot
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 781](https://github.com/open-quantum-safe/oqs-provider/pull/781): Fix clang-formatting errors from PR #779
		 - [PR 778](https://github.com/open-quantum-safe/oqs-provider/pull/778): oqsprov: avoid encoder hotpath in P-curve hybrid KEM keygen
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 194](https://github.com/open-quantum-safe/openssh/pull/194): Openssh 10.3p1 uplift


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 142](https://github.com/open-quantum-safe/boringssl/pull/142): Update to upstream 956bac6
	- Open PRs:
		 - [PR 143](https://github.com/open-quantum-safe/boringssl/pull/143): bump versions of actions


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- Issues with activity in the last 7 days:
		 - [Issue 395](https://github.com/open-quantum-safe/oqs-demos/issues/395): General review of base image versions and oqs version updates  `good first issue` `help wanted`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 396](https://github.com/open-quantum-safe/oqs-demos/pull/396): Update QUIC
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 327](https://github.com/open-quantum-safe/www/pull/327): Bump \_includes/liboqs from `077e32a` to `5a8d047`  `dependencies` `submodules`
	- Open PRs: None


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


11. **[liboqs-Java](https://github.com/open-quantum-safe/liboqs-java)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


12. **[liboqs-js](https://github.com/open-quantum-safe/liboqs-js)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


13. **[liboqs-Python](https://github.com/open-quantum-safe/liboqs-python)**


	- Issues with activity in the last 7 days:
		 - [Issue 14](https://github.com/open-quantum-safe/liboqs-python/issues/14): PyPI library entry  `enhancement`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 135](https://github.com/open-quantum-safe/liboqs-python/pull/135): docs: add clear installation guide for Windows and Raspberry Pi
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 306](https://github.com/open-quantum-safe/liboqs-rust/pull/306): chore(ci): fix targeting
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 299](https://github.com/open-quantum-safe/liboqs-rust/pull/299): feat: add Android CMake configuration patch
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 297](https://github.com/open-quantum-safe/liboqs-rust/pull/297): feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - [PR 295](https://github.com/open-quantum-safe/liboqs-rust/pull/295): feat:  Implemented the RustCrypto traits for signatures and kems (#137)
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
