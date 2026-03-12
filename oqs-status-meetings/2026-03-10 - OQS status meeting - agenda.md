# 2026-03-10 - OQS status meeting - agenda

<span style="color: red;"> Tuesday March 10 at 12:30 PM </span> US Eastern Time / 5:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

1. Status updates & items seeking help

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

**Ready**
- [Issue 2291](https://github.com/open-quantum-safe/liboqs/issues/2291): Avoid duplicate CI runs in pull requests (push+PR tests) (liboqs)
- [Issue 2118](https://github.com/open-quantum-safe/liboqs/issues/2118): Update HQC implementation to 2025/02/19 version (liboqs)
- [Issue 2045](https://github.com/open-quantum-safe/liboqs/issues/2045): Create a table of algorithm support levels (liboqs)
- [Issue 2101](https://github.com/open-quantum-safe/liboqs/issues/2101): Adding FAEST (liboqs)
- [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration (liboqs)

**Backlog**
- [Issue 2334](https://github.com/open-quantum-safe/liboqs/issues/2334): Review performance regression tests (liboqs)
- [Issue 1788](https://github.com/open-quantum-safe/liboqs/issues/1788): Enable data independent timing on Apple Silicon (liboqs)
- [Issue 2282](https://github.com/open-quantum-safe/liboqs/issues/2282): Review and Apply Hardened Default Compiler Options (liboqs)
- [Issue 2329](https://github.com/open-quantum-safe/liboqs/issues/2329): Add support for Clang 22 \_\_builtin\_ct\_select (liboqs)
- [Issue 2098](https://github.com/open-quantum-safe/liboqs/issues/2098): Solicit more schemes from NIST signature on-ramp round 2 (liboqs)
- [Issue 2375](https://github.com/open-quantum-safe/liboqs/issues/2375): Limit runtime of regular CI runs in PRs (liboqs)

**In review**
- [PR 2356](https://github.com/open-quantum-safe/liboqs/pull/2356): sntrup761: replace PQClean code with public domain OpenSSH code (liboqs)



## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **[OQS Technical Steering Committee](https://github.com/open-quantum-safe/tsc)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 253](https://github.com/open-quantum-safe/tsc/pull/253): Status meeting agenda for March 3, 2026
		 - [PR 248](https://github.com/open-quantum-safe/tsc/pull/248): Minutes of OQS TSC meeting 2026-02-17


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- New issues in the last 14 days:
		 - [Issue 2375](https://github.com/open-quantum-safe/liboqs/issues/2375): Limit runtime of regular CI runs in PRs
		 - [Issue 2371](https://github.com/open-quantum-safe/liboqs/issues/2371): Memory-optimized build option
	- Merges in the last 7 days:
		 - [PR 2373](https://github.com/open-quantum-safe/liboqs/pull/2373): Add latest Wycheproof tests [ML-KEM]
		 - [PR 2367](https://github.com/open-quantum-safe/liboqs/pull/2367): Introduce OQS\_MEMOPT\_BUILD to enable memory‑optimized implementations  `needs review`
	- Open PRs:
		 - [PR 2369](https://github.com/open-quantum-safe/liboqs/pull/2369): Update Zephyr CI tests to recent versions
		 - [PR 2366](https://github.com/open-quantum-safe/liboqs/pull/2366): Add API support for External-MU Signature[ML-DSA]
		 - [PR 2361](https://github.com/open-quantum-safe/liboqs/pull/2361): Add MQOM  `needs review`
		 - [PR 2356](https://github.com/open-quantum-safe/liboqs/pull/2356): sntrup761: replace PQClean code with public domain OpenSSH code  `needs review` `focus`
		 - [PR 2328](https://github.com/open-quantum-safe/liboqs/pull/2328): Hqc update reference implementation   `focus`
		 - [PR 2298](https://github.com/open-quantum-safe/liboqs/pull/2298): Add build option for randomized ML-DSA signing
		 - [PR 2277](https://github.com/open-quantum-safe/liboqs/pull/2277): SQIsign integration


3. **[OQS-OpenSSL 3 provider](https://github.com/open-quantum-safe/oqs-provider)**


	- New issues in the last 14 days:
		 - [Issue 756](https://github.com/open-quantum-safe/oqs-provider/issues/756): Implement PQC algorithm inside the Openssl core libraray  `question`
		 - [Issue 755](https://github.com/open-quantum-safe/oqs-provider/issues/755): The sigx\_cmp interface has crashed.  `bug`
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 752](https://github.com/open-quantum-safe/oqs-provider/pull/752): Preserve property string for KEMs.
		 - [PR 655](https://github.com/open-quantum-safe/oqs-provider/pull/655): oqsprovider: allow building as shared library again
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 190](https://github.com/open-quantum-safe/openssh/pull/190): Bugfix/hybrid preauth length
		 - [PR 189](https://github.com/open-quantum-safe/openssh/pull/189): Updating Sphincs to SLH-DSA


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- New issues in the last 14 days:
		 - [Issue 316](https://github.com/open-quantum-safe/www/issues/316): Update external uses
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 317](https://github.com/open-quantum-safe/www/pull/317): Bump \_includes/liboqs from `6b390dd` to `a2fb264`  `dependencies` `submodules`
		 - [PR 315](https://github.com/open-quantum-safe/www/pull/315): meta-oqs : oqs support for embedded Linux


9. **[liboqs-C++](https://github.com/open-quantum-safe/liboqs-cpp)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


10. **[liboqs-Go](https://github.com/open-quantum-safe/liboqs-go)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days:
		 - [PR 50](https://github.com/open-quantum-safe/liboqs-go/pull/50): Fix for #49 and verification against liboqs 0.15.0
	- Open PRs: None


11. **[liboqs-Java](https://github.com/open-quantum-safe/liboqs-java)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


12. **[liboqs-js](https://github.com/open-quantum-safe/liboqs-js)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


13. **[liboqs-Python](https://github.com/open-quantum-safe/liboqs-python)**


	- New issues in the last 14 days:
		 - [Issue 133](https://github.com/open-quantum-safe/liboqs-python/issues/133): liboqs-python automaticaly installs liboqs v14 but v15 is available
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 132](https://github.com/open-quantum-safe/liboqs-python/pull/132): Update liboqs version to 0.15.0.
		 - [PR 130](https://github.com/open-quantum-safe/liboqs-python/pull/130): Update STFL pipeline
		 - [PR 119](https://github.com/open-quantum-safe/liboqs-python/pull/119): Version 0.14
		 - [PR 94](https://github.com/open-quantum-safe/liboqs-python/pull/94): replacing openssl111 with openssl3


14. **[liboqs-Rust](https://github.com/open-quantum-safe/liboqs-rust)**


	- New issues in the last 14 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 303](https://github.com/open-quantum-safe/liboqs-rust/pull/303): chore(ci): bump the actions group across 1 directory with 2 updates  `dependencies` `github_actions`
		 - [PR 300](https://github.com/open-quantum-safe/liboqs-rust/pull/300): CI on Windows arm64
		 - [PR 299](https://github.com/open-quantum-safe/liboqs-rust/pull/299): feat: add Android CMake configuration patch
		 - [PR 298](https://github.com/open-quantum-safe/liboqs-rust/pull/298): fix: support compiling on Windows ARM64
		 - [PR 297](https://github.com/open-quantum-safe/liboqs-rust/pull/297): feat: add conditional OpenSSL compilation support for iOS and embedded platforms
		 - [PR 295](https://github.com/open-quantum-safe/liboqs-rust/pull/295): feat:  Implemented the RustCrypto traits for signatures and kems (#137)
		 - [PR 260](https://github.com/open-quantum-safe/liboqs-rust/pull/260): feat: Auto-allocate stack in runtime
