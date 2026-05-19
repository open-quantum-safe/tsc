# 2026-05-19 - OQS status meeting - agenda

<span style="color: red;"> Tuesday May 19 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

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


	- Issues with activity in the last 7 days:
		 - [Issue 283](https://github.com/open-quantum-safe/tsc/issues/283): PQCA License Scan
		 - [Issue 282](https://github.com/open-quantum-safe/tsc/issues/282): Add Rodrigo to security@openquantumsafe.org
		 - [Issue 276](https://github.com/open-quantum-safe/tsc/issues/276): OQS presence at relevant conferences - Venues  `discussion`
		 - [Issue 275](https://github.com/open-quantum-safe/tsc/issues/275): OQS Health Report - March 2026  `discussion`
	- Merges in the last 7 days:
		 - [PR 284](https://github.com/open-quantum-safe/tsc/pull/284): Add dstebila as a liboqs-python maintainer
		 - [PR 281](https://github.com/open-quantum-safe/tsc/pull/281): Add minutes for OQS status meeting 2026-05-12
		 - [PR 269](https://github.com/open-quantum-safe/tsc/pull/269): Update liboqs permissions  `High priority`
	- Open PRs: None


2. **[liboqs](https://github.com/open-quantum-safe/liboqs)**


	- Issues with activity in the last 7 days:
		 - [Issue 2436](https://github.com/open-quantum-safe/liboqs/issues/2436): Investigate weekly build failures  `bug` `focus`
		 - [Issue 2418](https://github.com/open-quantum-safe/liboqs/issues/2418): cryptobox pqc support
		 - [Issue 2380](https://github.com/open-quantum-safe/liboqs/issues/2380): Copy from upstream: add support for algorithm-dependent common dependencies
		 - [Issue 2282](https://github.com/open-quantum-safe/liboqs/issues/2282): Review and Apply Hardened Default Compiler Options  `enhancement`
		 - [Issue 2141](https://github.com/open-quantum-safe/liboqs/issues/2141): Is there a way to save the private key without signing  `question`
		 - [Issue 2098](https://github.com/open-quantum-safe/liboqs/issues/2098): Solicit more schemes from NIST signature on-ramp round 3  `enhancement` `wishlist`
		 - [Issue 2064](https://github.com/open-quantum-safe/liboqs/issues/2064): Compile a list of upstream contacts
		 - [Issue 2045](https://github.com/open-quantum-safe/liboqs/issues/2045): Create a table of algorithm support levels  `documentation`
		 - [Issue 2042](https://github.com/open-quantum-safe/liboqs/issues/2042): liboqs Fails Depending on the OpenSSL Provider Version Used
		 - [Issue 1991](https://github.com/open-quantum-safe/liboqs/issues/1991): Develop policy about algorithm deprecation
		 - [Issue 1989](https://github.com/open-quantum-safe/liboqs/issues/1989): Drop Kyber support  `future-work`
		 - [Issue 1896](https://github.com/open-quantum-safe/liboqs/issues/1896): Unused variable in Classic McEliece  `wontfix`
		 - [Issue 1829](https://github.com/open-quantum-safe/liboqs/issues/1829): scorecard: publish results & run weekly
		 - [Issue 1811](https://github.com/open-quantum-safe/liboqs/issues/1811): The library always links against libpthreads
		 - [Issue 1802](https://github.com/open-quantum-safe/liboqs/issues/1802): Recreate public key from private
	- Merges in the last 7 days:
		 - [PR 2434](https://github.com/open-quantum-safe/liboqs/pull/2434): Add OQS\_SIG\_STFL\_keygen\_and\_sign\_supported() for runtime detection  `enhancement`
		 - [PR 2433](https://github.com/open-quantum-safe/liboqs/pull/2433): Fall back when EVP\_DigestSqueeze is unavailable or unsupported
		 - [PR 2430](https://github.com/open-quantum-safe/liboqs/pull/2430): Fix latent warnings exposed by refreshed CI container images  `bug` `needs review` `focus`
		 - [PR 2428](https://github.com/open-quantum-safe/liboqs/pull/2428): Bump the pip group across 2 directories with 2 updates  `dependencies` `python`
		 - [PR 2424](https://github.com/open-quantum-safe/liboqs/pull/2424): Bump the pip group across 2 directories with 13 updates  `dependencies` `python`
		 - [PR 2422](https://github.com/open-quantum-safe/liboqs/pull/2422): Bump the github-actions group across 1 directory with 9 updates  `dependencies` `github_actions`
		 - [PR 2421](https://github.com/open-quantum-safe/liboqs/pull/2421): Add loganaden as codeowner for Kyber  `needs review`
		 - [PR 2420](https://github.com/open-quantum-safe/liboqs/pull/2420): Dependabot configuration and dependency updates  `dependencies`
		 - [PR 2416](https://github.com/open-quantum-safe/liboqs/pull/2416): LMS Enhancements
		 - [PR 2413](https://github.com/open-quantum-safe/liboqs/pull/2413): Create a table of algorithm support levels  `documentation` `focus`
		 - [PR 2382](https://github.com/open-quantum-safe/liboqs/pull/2382): Add common dependencies with include\_only  `ready for merge`
	- Open PRs:
		 - [PR 2435](https://github.com/open-quantum-safe/liboqs/pull/2435): Add NIST LMS Signature verify KATs
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
		 - [Issue 777](https://github.com/open-quantum-safe/oqs-provider/issues/777): Adding MQOM to oqs-provider  `question`
	- Merges in the last 7 days:
		 - [PR 779](https://github.com/open-quantum-safe/oqs-provider/pull/779): Add the MQOM signature algorithm 
	- Open PRs:
		 - [PR 778](https://github.com/open-quantum-safe/oqs-provider/pull/778): oqsprov: avoid encoder hotpath in P-curve hybrid KEM keygen
		 - [PR 641](https://github.com/open-quantum-safe/oqs-provider/pull/641): nit: Fix runtime dependent format issue in generate.sh and clean up python scripts


4. **[OQS-OpenSSH](https://github.com/open-quantum-safe/openssh)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs:
		 - [PR 194](https://github.com/open-quantum-safe/openssh/pull/194): Openssh 10.3p1 uplift


5. **[OQS-BoringSSL](https://github.com/open-quantum-safe/boringssl)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days: None.
	- Open PRs: None


6. **[oqs-demos](https://github.com/open-quantum-safe/oqs-demos)**


	- Issues with activity in the last 7 days:
		 - [Issue 395](https://github.com/open-quantum-safe/oqs-demos/issues/395): General review of base image versions and oqs version updates  `good first issue` `help wanted`
		 - [Issue 392](https://github.com/open-quantum-safe/oqs-demos/issues/392): CI tags not properly aligned  `good first issue` `help wanted`
		 - [Issue 388](https://github.com/open-quantum-safe/oqs-demos/issues/388): OID displayed instead of signature algorithm name (MLDSA) in custom Chromium build  `future work` `help wanted`
		 - [Issue 386](https://github.com/open-quantum-safe/oqs-demos/issues/386): epiphany hybrid kem support issue
		 - [Issue 374](https://github.com/open-quantum-safe/oqs-demos/issues/374): oqs-provider 0.9.0: update demos
	- Merges in the last 7 days:
		 - [PR 394](https://github.com/open-quantum-safe/oqs-demos/pull/394): Fix CI tags in README and disable unmaintained projects in build.yml
	- Open PRs:
		 - [PR 380](https://github.com/open-quantum-safe/oqs-demos/pull/380): Add plotly digital signatures visualization demo


7. **[ci-containers](https://github.com/open-quantum-safe/ci-containers)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 102](https://github.com/open-quantum-safe/ci-containers/pull/102): Update Alpine Linux container to newer version
	- Open PRs: None


8. **[www.openquantumsafe.org](https://github.com/open-quantum-safe/www)**


	- Issues with activity in the last 7 days: None.
	- Merges in the last 7 days:
		 - [PR 326](https://github.com/open-quantum-safe/www/pull/326): Bump \_includes/liboqs from `0e325cc` to `077e32a`  `dependencies` `submodules`
		 - [PR 325](https://github.com/open-quantum-safe/www/pull/325): Bump \_includes/liboqs from `ef70dea` to `0e325cc`  `dependencies` `submodules`
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
		 - [Issue 136](https://github.com/open-quantum-safe/liboqs-python/issues/136): export\_secret\_key from StatefulSignature: TypeError: LoadLibrary() argument 1 must be str, not None
		 - [Issue 134](https://github.com/open-quantum-safe/liboqs-python/issues/134): is 0.12.0 0.11.0?
		 - [Issue 133](https://github.com/open-quantum-safe/liboqs-python/issues/133): liboqs-python automaticaly installs liboqs v14 but v15 is available
		 - [Issue 131](https://github.com/open-quantum-safe/liboqs-python/issues/131): No Github Releases for Latest Package Versions
		 - [Issue 128](https://github.com/open-quantum-safe/liboqs-python/issues/128): Allow toggling for randomized seed/nonce for ML-DSA signatures
		 - [Issue 124](https://github.com/open-quantum-safe/liboqs-python/issues/124): GitHub actions run twice on PRs
		 - [Issue 122](https://github.com/open-quantum-safe/liboqs-python/issues/122): Fails to import package when liboqs is compiled with OQS\_DLOPEN\_OPENSSL=ON
		 - [Issue 121](https://github.com/open-quantum-safe/liboqs-python/issues/121): Stateful sigs segfault on macOS and Linux
		 - [Issue 120](https://github.com/open-quantum-safe/liboqs-python/issues/120): Official PyPi package?
		 - [Issue 96](https://github.com/open-quantum-safe/liboqs-python/issues/96): Validate build passes against python 3.12
		 - [Issue 91](https://github.com/open-quantum-safe/liboqs-python/issues/91): Failures on ACVP Vectors for ML-DSA-65 and ML-DSA-87
		 - [Issue 78](https://github.com/open-quantum-safe/liboqs-python/issues/78): Importing OpenSSL keys and certificates  `question`
		 - [Issue 74](https://github.com/open-quantum-safe/liboqs-python/issues/74): Kat-Vector-Falcon  `question`
		 - [Issue 14](https://github.com/open-quantum-safe/liboqs-python/issues/14): PyPI library entry  `enhancement`
	- Merges in the last 7 days:
		 - [PR 145](https://github.com/open-quantum-safe/liboqs-python/pull/145): Remove docker/ directory
		 - [PR 144](https://github.com/open-quantum-safe/liboqs-python/pull/144): Fix StatefulSignature segfault when liboqs lacks STFL keygen support
		 - [PR 143](https://github.com/open-quantum-safe/liboqs-python/pull/143): Update Python versions to 3.12-3.14
		 - [PR 142](https://github.com/open-quantum-safe/liboqs-python/pull/142): Update algorithm name used in test file
		 - [PR 141](https://github.com/open-quantum-safe/liboqs-python/pull/141): Fix StatefulSignature.export\_secret\_key TypeErrors on Windows  `bug`
		 - [PR 140](https://github.com/open-quantum-safe/liboqs-python/pull/140): Add PYOQS\_VERSION env var to override auto-installed liboqs version
		 - [PR 139](https://github.com/open-quantum-safe/liboqs-python/pull/139): Bump pyasn1 from 0.6.1 to 0.6.3 in the pip group across 1 directory  `dependencies` `python`
		 - [PR 138](https://github.com/open-quantum-safe/liboqs-python/pull/138): CI: only run push workflow on main (#124)
		 - [PR 137](https://github.com/open-quantum-safe/liboqs-python/pull/137): Bump version to 0.16.0-dev
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
