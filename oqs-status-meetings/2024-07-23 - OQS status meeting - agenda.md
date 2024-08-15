# 2024-07-23 - OQS status meeting - agenda

<span style="color: red;"> Tuesday July 23 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Agenda

1. Trail of Bits audit
2. Issue triaging / prioritization
3. Status updates
4. liboqs 0.11.0 release planning
5. CBOM news

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

1. **OQS Technical Steering Committee**


	- Merges in the last 7 days:
		 - PR 54: Add @ajbozarth to triage members
		 - PR 53: Add agenda for 2024-07-16 status meeting
		 - PR 55: Add 2024-07-16 status meeting minutes
	- Open PRs:
		 - PR 46: Minutes for June 27, 2024 meeting
	- Open Issues:
		 - Issue 49: Switch open-quantum-safe/openssl to read-only
		 - Issue 45: Roles of maintainers & contributors
		 - Issue 29: Create project for tracking issues across repositories
		 - Issue 28: Automated dependency management
		 - Issue 27: Rollout scorecards across more repos
		 - Issue 24: Decide procedure(s) to handle CI failures
		 - Issue 12: Create a voting procedure for the OQS TSC
		 - Issue 11: Confirm mailing list openness and retention
		 - Issue 10: Update config.yaml
		 - Issue 5: CI in OQS: guidelines for responsible use
		 - Issue 2: OQS sub projects: Which ones to drop for good
		 - Issue 1: OQS goal: non-committal research or production use?


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 1836: Bump zipp from 3.4.0 to 3.19.1 in /scripts/copy\_from\_upstream in the pip group
		 - PR 1848: Use `cmake -LA -N` instead of `cmake -LA` in CI
		 - PR 1852: Fix passes.json entries for MAYO
		 - PR 1844: Update and fix CI status badges
	- Open PRs:
		 - PR 1700: change from ninja and custom cmake target `run\_test` to using cmake & ctest.
		 - PR 1717: Proposed build wrapper script for static libs macOS / iOS / Android platforms
		 - PR 1745: Integrate Kyber from libjade 
		 - PR 1816: CMakeLists: add ppc case to known archs
		 - PR 1834: Update CBOM format to upstream v1.6
		 - PR 1839: Decode FORS indices similarly to WOTS
		 - PR 1849: Move from CircleCI to GitHub Actions
	- Open Issues:
		 - Issue 1851: Add diagrams for minimal examples in wiki and liboqs documentation
		 - Issue 1850: Latest updates to ML-DSA are not implemented yet
		 - Issue 1847: Running `cmake -LA` changes library configuration
		 - Issue 1843: Update CODEOWNERS
		 - Issue 1842: Use OQS\_*\_set\_callbacks instead of C\_OR\_NI\_OR\_ARM macros
		 - Issue 1841: Document public / internal API split
		 - Issue 1840: Define threat model for liboqs
		 - Issue 1838: Decode FORS indices similarly to WOTS
		 - Issue 1831: Update CBOM to CycloneDX 1.6 format
		 - Issue 1830: scorecard: update to version 5
		 - Issue 1829: scorecard: publish results & run weekly
		 - Issue 1827: Update CI status report
		 - Issue 1824: huge stack usage
		 - Issue 1823: Replace malloc/free with OPENSSL\_malloc/OpenSSL\_free
		 - Issue 1811: The library always links against libpthreads
		 - Issue 1807: Extend constant-time testing
		 - Issue 1804: CI: macOS build failures
		 - Issue 1802: Recreate public key from private
		 - Issue 1795: Move from CCI to GH CI
		 - Issue 1788: Enable data independent timing on Apple Silicon
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
		 - Issue 1083: Enabling more compiler warnings
		 - Issue 910: Establish interop with Circl
		 - Issue 167: Code coverage


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 294: Fix #272: check `c\_obj\_create` error code for `OBJ\_R\_OID\_EXISTS`.
		 - PR 316: Generate code coverage using source-based LLVM code coverage.
		 - PR 363: Updates for clean builds across iOS / macOS / Android (all platforms)
		 - PR 367: improve static build testing
		 - PR 412: MSVC C2059 error when no signature is enabled
		 - PR 413: Add MAYO
	- Open Issues:
		 - Issue 451: Do project self-assessment
		 - Issue 450: Generate a Kyber Certificate
		 - Issue 447: Support deterministic key generation
		 - Issue 430: Too many agruments to function 'mkdir' on Windows
		 - Issue 399: Too many advertised sig algs cause TLS server hang-up
		 - Issue 375: Refactor code
		 - Issue 372: How to separate the post-quantum algorithmic key and the classical key in the generated pkey
		 - Issue 354: Adapt oqsprovider to liboqs version during build
		 - Issue 353: Make CI using downstream integrations optional
		 - Issue 351: Document & curate (O)IDs
		 - Issue 331: Supporting Stateful Signatures
		 - Issue 293: Document platforms supported
		 - Issue 289: Enable CI runs for specific upstream tags
		 - Issue 272: Race condition with `c\_obj\_create`.
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
		 - Issue 108: Review project status
		 - Issue 96: Add OpenSSL interop testing
		 - Issue 81: Introduce TLS\_DEFAULT\_GROUPS env var
		 - Issue 77: Automate hybrid strength assignment
		 - Issue 60: Add some OQS tests to x509/x509\_test.cc and evp/evp\_test.cc


5. **OQS-OpenSSH**


	- Merges in the last 7 days:
		 - PR 160: Apply upstream refactor to sshkey.c
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
	- Open PRs: None
	- Open Issues:
		 - Issue 287: Curl throwing cipher error
		 - Issue 284: Automate and streamline docker image generation
		 - Issue 283: Faling in Building nginx server with pqc certificate
		 - Issue 277: Build failures in CI
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


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 81: Update Container build CI
		 - Issue 78: Track container usage
		 - Issue 74: Refresh ci-debian-buster container image used for build


10. **liboqs-C++**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 20: Compile error


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
		 - Issue 25: Optimize pom.xml & Some fixes
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
		 - PR 259: feat: update liboqs, add ml-kem / ml-dsa
		 - PR 260: feat: Auto-allocate stack in runtime
		 - PR 261: chore(ci): bump KyleMayes/install-llvm-action from 1.9.0 to 2.0.3 in the actions group
	- Open Issues:
		 - Issue 263: MacOS build fails (as linking against OpenSSL1 instead of 3)
		 - Issue 262: Please document how to build against the system copy of liboqs
		 - Issue 216: Don't recompile oqs everytime cargo build is invoked
		 - Issue 202: expose `OQS\_PERMIT\_UNSUPPORTED\_ARCHITECTURE`, for example as cargo feature
		 - Issue 137: Support RustCrypto KEM and Signature traits
		 - Issue 131: WASM compatibility
		 - Issue 127: ARMv8 compatibility: CI and cross-compiling?


16. **www.openquantumsafe.org** : No updates
