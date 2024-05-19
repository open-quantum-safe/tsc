# 2024-05-14 - OQS status meeting - agenda

<span style="color: red;"> Tuesday May 14 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Agenda

1. Security issue for oqs-provider
1. Call with Trail of Bits
1. Status updates

## OQS subprojects

1. OQS Technical Steering Committee
2. liboqs
3. OQS-OpenSSL 3 provider
4. OQS-BoringSSL
5. OQS-OpenSSH
6. OQS-libssh
7. oqs-demos
8. profiling
9. ci-containers
10. liboqs language wrappers: liboqs-C++, liboqs-.NET, liboqs-Go, liboqs-Java, liboqs-Python, liboqs-Rust
11. www.openquantumsafe.org

## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **<span style="color: red;">Build failures:<span style="color: red;">**

	- **<span style="color: red;">liboqs CircleCI<span style="color: red;">**
	- **<span style="color: red;">oqs-demos CircleCI<span style="color: red;">**
	- **<span style="color: red;">liboqs-java CircleCI<span style="color: red;">**

1. **OQS Technical Steering Committee**


	- Merges in the last 7 days:
		 - PR 22: Remove Amber Sprenkels from liboqs-rust
	- Open PRs:
		 - PR 14: Minutes from 2024-03-11 TSC meeting
		 - PR 18: Add 20240410 minutes
	- Open Issues:
		 - Issue 25: Obtain funding for ARM CI GH runners
		 - Issue 24: Decide procedure(s) to handle CI failures
		 - Issue 12: Create a voting procedure for the OQS TSC
		 - Issue 11: Confirm mailing list openness and retention
		 - Issue 10: Update config.yaml
		 - Issue 8: FYI: open-quantum-safe/rust team has crates.io push access
		 - Issue 5: CI in OQS: guidelines for responsible use
		 - Issue 2: OQS sub projects: Which ones to drop for good
		 - Issue 1: OQS goal: non-committal research or production use?


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 1782: Bump jinja2 from 3.1.3 to 3.1.4 in /scripts/copy\_from\_upstream
		 - PR 1784: Algorithm selection clarification
	- Open PRs:
		 - PR 1650: Add Stateful Signature (XMSS and LMS)
		 - PR 1700: change from ninja and custom cmake target `run\_test` to using cmake & ctest.
		 - PR 1707: Add MAYO signature scheme from NIST onramp
		 - PR 1708: Create scorecard.yml (OpenSSF)
		 - PR 1717: Proposed build wrapper script for static libs macOS / iOS / Android platforms
		 - PR 1745: Integrate Kyber from libjade 
		 - PR 1773: Use OPENSSL\_cleanse if OpenSSL is used
		 - PR 1774: Errors not printed out when OPENSSL\_NO\_STDIO is set
	- Open Issues:
		 - Issue 1790: Zeroing internal state memory on heap
		 - Issue 1789: Trigger downstream liboqs-python CI is failing
		 - Issue 1788: Enable data independent timing on Apple Silicon
		 - Issue 1787: Malformed generated `liboqs.pc` file
		 - Issue 1786: Enhance test output
		 - Issue 1785: Add documentation Markdown linter to CI
		 - Issue 1783: Remove unnecessary downstream CI
		 - Issue 1780: Update Ubuntu support to more current LTS version(s)
		 - Issue 1770: Add C++ test to ci
		 - Issue 1768: dlfcn required for windows build
		 - Issue 1766: Overhauling OQS\_MEM functions
		 - Issue 1765: Automated dependency checks/updates
		 - Issue 1761: Valgrind Massif Tool Breaks During Verify Operation of Falcon Algorithms on Raspberry Pi
		 - Issue 1760: Document DCO utility and HOWTO
		 - Issue 1753: Update CBOM to CycloneDX 1.6 specification
		 - Issue 1750: Return value from OQS\_randombytes
		 - Issue 1748: LibOQS CMake fails with cmake 3.28.3
		 - Issue 1740: Add more test vectors for ML-KEM
		 - Issue 1719: Improve algorithm versioning
		 - Issue 1706: Add OpenSSF scorecard
		 - Issue 1705: Handle out-of-memory errors gracefully
		 - Issue 1691: Align platforms supported with OpenSSL
		 - Issue 1678: Investigate BIKE failures on x86
		 - Issue 1674: Expand weekly test runs to platforms other than x86\_64 / Linux
		 - Issue 1673: Clearly document KAT sources
		 - Issue 1639: CI tooling for variable-time operations on some platforms
		 - Issue 1623: Update PR approval requirements
		 - Issue 1619: Introduce constant time build variable
		 - Issue 1606: OQS\_SHA*\_sha***\_ API does not support arbitrary length updates
		 - Issue 1596: Update HQC AVX2 implementation
		 - Issue 1540: Environment-specific Classic McEliece constant-time leaks
		 - Issue 1514: Review & automate license management
		 - Issue 1494: Use modern CMake syntax
		 - Issue 1474: Multithreading tests
		 - Issue 1466: Integrate Kyber implementation from libjade
		 - Issue 1456: Add telltale error handling in void functions
		 - Issue 1437: CC0 license is an obstacle
		 - Issue 1416: RISC-V support
		 - Issue 1408: Test all scripts
		 - Issue 1366: Run clang's MemorySanitizer in CI
		 - Issue 1233: Common code for s390x / ppc64le, Windows
		 - Issue 1215: Add fuzzing testing
		 - Issue 1206: Adding a DeriveKeyPair functionality
		 - Issue 1199: WASM compatibillity
		 - Issue 1185: Adding a build variable to specify armv8 version
		 - Issue 1138: Correct OQS\_MINIMAL\_BUILD logic when introducing new optimizations
		 - Issue 1098: Add stateful hash-based signatures
		 - Issue 1083: Enabling more compiler warnings
		 - Issue 910: Establish interop with Circl
		 - Issue 167: Code coverage


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days:
		 - PR 410: Fix CI (Add Ubuntu 24 support)
		 - PR 409: Bump jinja2 from 3.1.3 to 3.1.4 in /oqs-template
		 - PR 405: Extra parentheses removed
		 - PR 404: No unwanted error left in queue from OBJ\_create
	- Open PRs:
		 - PR 294: Fix #272: check `c\_obj\_create` error code for `OBJ\_R\_OID\_EXISTS`.
		 - PR 316: Generate code coverage using source-based LLVM code coverage.
		 - PR 363: Updates for clean builds across iOS / macOS / Android (all platforms)
		 - PR 367: improve static build testing
		 - PR 412: MSVC C2059 error when no signature is enabled
	- Open Issues:
		 - Issue 399: Too many advertised sig algs cause TLS server hang-up
		 - Issue 396: Update SPECIFICATIONS.md
		 - Issue 389: conduct 'Full stack' performance testing using standard client software like 'curl' and nginx as the Web Server
		 - Issue 375: Refactor code
		 - Issue 372: How to separate the post-quantum algorithmic key and the classical key in the generated pkey
		 - Issue 360: Getting message "too weak" when launching openssl server
		 - Issue 358: oqs\_tlssig fails against OpenSSL 3.2.1
		 - Issue 354: Adapt oqsprovider to liboqs version
		 - Issue 353: Make CI using downstream integrations optional
		 - Issue 351: Document & curate (O)IDs
		 - Issue 331: Supporting Stateful Signatures
		 - Issue 328: Automate testing for backlevel liboqs variants
		 - Issue 319: how to integrate provider with openssl no-shared static build
		 - Issue 293: Document platforms supported
		 - Issue 289: Enable CI runs for specific upstream tags
		 - Issue 279: Evaluate liboqs reference in dynamic linking situations
		 - Issue 272: Race condition with `c\_obj\_create`.
		 - Issue 269: What hybrid key concepts should be supported?
		 - Issue 251: Using PKCS#7 OpenSSL API
		 - Issue 248: Move off CircleCI
		 - Issue 239: Missing support for hash-n-sign
		 - Issue 228: Eliminate use of jinja2
		 - Issue 227: Create PR for brew when oqsprovider is notable enough
		 - Issue 162: Improve use of IDs in ERR\_raise()
		 - Issue 155: Improve (heap) memory consumption
		 - Issue 154: QSC encoder library build loses cross-compilation settings
		 - Issue 94: Make available binaries
		 - Issue 81: Faster error-exit
		 - Issue 17: Hybrid KEM: more combiners, more abstraction


4. **OQS-BoringSSL**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 115: Update to upstream 783ae72
		 - Issue 108: Review project status
		 - Issue 96: Add OpenSSL interop testing
		 - Issue 81: Introduce TLS\_DEFAULT\_GROUPS env var
		 - Issue 77: Automate hybrid strength assignment
		 - Issue 60: Add some OQS tests to x509/x509\_test.cc and evp/evp\_test.cc


5. **OQS-OpenSSH**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 153: Fix version number
		 - Issue 152: Displayed version is not updated for 2023-10 release since 2022-08
		 - Issue 150: Memory leaks in oqs ecdh path
		 - Issue 149: Merge conflict markers in ssh\_config.5
		 - Issue 145: New "permanent temporary" P256+Kyber768 IANA codepoint support in OQS OpenSSH
		 - Issue 135: Migrate to OpenSSH 9.2
		 - Issue 90: OpenSSH 8.4: Figure out if the regression suite can be augmented
		 - Issue 89: Figure out why certain tests are failing.
		 - Issue 24: Enable PQ certs


6. **OQS-libssh**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 21: pkd\_hello test suite breaks on Ubuntu 22.04 host


7. **oqs-demos**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 272: Update test server build script: liboqs-0.10.0 & oqs-provider-0.6.0-rc1
		 - PR 275: reduce further and document better support level of single integrations
	- Open Issues:
		 - Issue 273: HAProxy
		 - Issue 270: Dont get Server Temp Key in openssl s\_client when testing
		 - Issue 266: oqs-epiphany not working 
		 - Issue 265: Not able to get OQS-Chromium browser working - https://openquantumsafe.org/applications/tls.html#chromium
		 - Issue 261: Add QUIC support
		 - Issue 255: Wireshark Docker Build Fails with WolfSSL Due to Undeclared 'QSC\_SIG\_CPS' Variable
		 - Issue 230: Fix integrations to specific commits?
		 - Issue 229: Cannot switch off OQS\_HAVE\_GETENTROPY, OQS\_HAVE\_EXPLICIT\_BZERO
		 - Issue 226: haproxy build failed on MacOS 
		 - Issue 216: add into edk2 openssllib
		 - Issue 213: Create cross-platform docker images in github
		 - Issue 200: Path to a NodeJS demo
		 - Issue 182: replace oqs-openssl111
		 - Issue 171: Create CI/docker push for unbound
		 - Issue 92: Add OQS to libnss (enabling loading quantum safe certificate into Chromium)


8. **profiling**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 110: liboqs benchmarking still running 0.9.0-rc1


9. **ci-containers**


	- Merges in the last 7 days:
		 - PR 77: update go to 1.22.2
		 - PR 79: Update Go to 1.22.3 and fix errors
		 - PR 80: set env vars GOROOT and PATH explicitly
		 - PR 84: Adding Ubuntu latest
	- Open PRs: None
	- Open Issues:
		 - Issue 81: Update Container build CI
		 - Issue 78: Track container usage
		 - Issue 74: Refresh ci-debian-buster container image used for build


10. **liboqs-C++**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues: None


11. **liboqs-.NET**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 28: fix Classic McEliece stackoverflow issue by running unit tests with larger stack


12. **liboqs-Go**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 40: A pipeline to release container image on github?


13. **liboqs-Java**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 20: Tag 0.1.1
		 - Issue 1: Enable build on Windows


14. **liboqs-Python**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 86: Building for MacOS M1 (Arm)
		 - Issue 78: Importing OpenSSL keys and certificates
		 - Issue 74: Kat-Vector-Falcon


15. **liboqs-Rust**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 258: chore(ci): bump KyleMayes/install-llvm-action from 1.9.0 to 2.0.2 in the actions group
		 - PR 259: feat: update liboqs, add ml-kem / ml-dsa
	- Open Issues:
		 - Issue 216: Don't recompile oqs everytime cargo build is invoked
		 - Issue 202: expose `OQS\_PERMIT\_UNSUPPORTED\_ARCHITECTURE`, for example as cargo feature
		 - Issue 137: Support RustCrypto KEM and Signature traits
		 - Issue 131: WASM compatibility
		 - Issue 127: ARMv8 compatibility: CI and cross-compiling?


16. **www.openquantumsafe.org** : No updates
