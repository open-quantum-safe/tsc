# 2024-09-24 - OQS status meeting - agenda

<span style="color: red;"> Tuesday September 24 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://zoom-lfx.platform.linuxfoundation.org/meetings/pqca?view=month)

## Agenda

1. liboqs 0.11.0 release
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

1. **OQS Technical Steering Committee**


	- Merges in the last 7 days:
		 - PR 79: Add OQS status meeting 2024-09-17 agenda
		 - PR 80: Add minutes for 2024-09-17 status call
	- Open PRs:
		 - PR 77: implementing #10
	- Open Issues:
		 - Issue 60: Decide security (issue) report handling team and procedure
		 - Issue 49: Switch open-quantum-safe/openssl to read-only
		 - Issue 45: Roles of maintainers & contributors
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


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 1700: change from ninja and custom cmake target `run\_test` to using cmake & ctest.
		 - PR 1834: Update CBOM format to upstream v1.6
		 - PR 1839: Decode FORS indices similarly to WOTS
		 - PR 1876: CPU extension detection for arm64 on NetBSD.
		 - PR 1877: Add DeriveKeyPair API
		 - PR 1890: #1830 update scorecard to v5 (gh action 2.4.0)
		 - PR 1905: Add a basic fuzz testing harness for Dilithium2
		 - PR 1919: Add ML-DSA / FIPS 204 final
		 - PR 1925: 0.11.0 release candidate 1
		 - PR 1926: [#1823] replace malloc/calloc/strdup/free with openssl allocator
		 - PR 1927: Change README links to be doxygen-friendly
		 - PR 1929: Improve Error Handling to Prevent Exit, Crashes and Memory Leaks
	- Open Issues:
		 - Issue 1931: NIST CAVP validation of liboqs ML-DSA algorithm
		 - Issue 1928: Improve documentation about algorithm implementation sources
		 - Issue 1921: Trouble building on Mac
		 - Issue 1918: Release Builds Location?
		 - Issue 1915: Remove unsupported Kyber upstreams
		 - Issue 1912: Automatically trigger CI based on git diff
		 - Issue 1904: Explicitly testing generic and non-generic code variants
		 - Issue 1897: Current "main" fails to gen\_docs
		 - Issue 1896: Unused variable in Classic McEliece
		 - Issue 1894: SLH-DSA: integrate final standard
		 - Issue 1891: ML-DSA: integrate final standard
		 - Issue 1888: Re-activate Travis CI for Tier-3 IBM platforms
		 - Issue 1882: CMAKE\_POSITION\_INDEPENDENT\_CODE should be optional
		 - Issue 1868: Add CodeQL query to check for memset calls
		 - Issue 1867: Add CodeQL query to enforce OpenSSL return code handling
		 - Issue 1866: Add CI workflow analysis tooling
		 - Issue 1864: memset used instead of OQS\_MEM\_CLEANSE
		 - Issue 1856: Add GitHub Actions to automate project board management 
		 - Issue 1851: Add diagrams for minimal examples in wiki and liboqs documentation
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
		 - Issue 1788: Enable data independent timing on Apple Silicon
		 - Issue 1786: Enhance test output
		 - Issue 1785: Add documentation Markdown linter to CI
		 - Issue 1770: Add C++ test to ci
		 - Issue 1768: dlfcn required for windows build
		 - Issue 1766: Overhauling OQS\_MEM functions
		 - Issue 1765: Automated dependency checks/updates
		 - Issue 1761: Valgrind Massif Tool Breaks During Verify Operation of Falcon Algorithms on Raspberry Pi
		 - Issue 1760: Document DCO utility and HOWTO
		 - Issue 1750: Return value from OQS\_randombytes
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
		 - Issue 1596: Update HQC AVX2 implementation
		 - Issue 1540: Environment-specific Classic McEliece constant-time leaks
		 - Issue 1514: Review & automate license management
		 - Issue 1494: Use modern CMake syntax
		 - Issue 1474: Multithreading tests
		 - Issue 1456: Add telltale error handling in void functions
		 - Issue 1437: CC0 license is an obstacle
		 - Issue 1426: OQS\_USE\_SHA3\_OPENSSL=ON makes running tests significantly slower
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


	- Merges in the last 7 days:
		 - PR 521: Address some Static Analysis Issues #519
	- Open PRs:
		 - PR 367: improve static build testing
		 - PR 412: MSVC C2059 error when no signature is enabled
		 - PR 461: Add CROSS
		 - PR 522: Remove unmanaged KEM OIDs
		 - PR 524: Reverse TLS hybrid keyshares for x25519/x448-mlkem hybrids
		 - PR 525: Only overwrite default library prefix for module library type build.
	- Open Issues:
		 - Issue 520: Mismatched hybrid default OIDs
		 - Issue 518: Create infrastructure to automate multiple releases with and without libjade code
		 - Issue 517: Add option to build against liboqs with OQS\_LIBJADE\_BUILD=ON
		 - Issue 514: Static Analysis Issues 
		 - Issue 509: How can we get the part of the elliptic curve from the PKEY and use it as the public key of a digital certificat
		 - Issue 503: Implement new ML-KEM hybrid key exchange in TLS
		 - Issue 502: Change default signature algorithms enabled
		 - Issue 494: Unknown certificate type
		 - Issue 490: Add code coverage testing
		 - Issue 488: Testing in openssl 3.1/3.0
		 - Issue 485: Document & test the new/3.4.0 encap/decap feature
		 - Issue 483: Reliability
		 - Issue 482: Windows: Build fails when using OQS\_MINIMAL\_BUILD
		 - Issue 481: Handshake Failures with Post-Quantum Certificates on SCTP & DTLS 1.2
		 - Issue 475: Missing Composite documentation
		 - Issue 473: CI upgrade breaks clang formatting and asan testing
		 - Issue 472: TLS sig tests failing when OQS\_KEM\_ENCODERS=ON
		 - Issue 466: The privateKey encoding for pure ml-dsa differs from the privateKey encoding for the ml-dsa part in composite ml-dsa-xxxx
		 - Issue 464: tlssig test takes huge amount of time
		 - Issue 451: Do project self-assessment
		 - Issue 447: Support deterministic key generation
		 - Issue 430: Too many agruments to function 'mkdir' on Windows
		 - Issue 399: Too many advertised sig algs cause TLS server hang-up
		 - Issue 375: Refactor code
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
		 - Issue 94: Make available binaries
		 - Issue 81: Faster error-exit
		 - Issue 17: Hybrid KEM: more combiners, more abstraction


4. **OQS-BoringSSL**


	- Merges in the last 7 days:
		 - PR 124: Sync algs with liboqs and oqs-provider
	- Open PRs: None
	- Open Issues:
		 - Issue 96: Add OpenSSL interop testing
		 - Issue 81: Introduce TLS\_DEFAULT\_GROUPS env var
		 - Issue 77: Automate hybrid strength assignment
		 - Issue 60: Add some OQS tests to x509/x509\_test.cc and evp/evp\_test.cc


5. **OQS-OpenSSH**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 164: Add support for XMSS SSH Keys and Certificates
		 - Issue 150: Memory leaks in oqs ecdh path
		 - Issue 90: OpenSSH 8.4: Figure out if the regression suite can be augmented
		 - Issue 89: Figure out why certain tests are failing.
		 - Issue 24: Enable PQ certs


6. **OQS-libssh**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 21: pkd\_hello test suite breaks on Ubuntu 22.04 host


7. **oqs-demos**


	- Merges in the last 7 days:
		 - PR 299: Update
	- Open PRs:
		 - PR 298: Pin libraries to current releases in curl demo
	- Open Issues:
		 - Issue 294: Switch off CircleCI
		 - Issue 284: Automate and streamline docker image generation
		 - Issue 273: HAProxy
		 - Issue 270: Dont get Server Temp Key in openssl s\_client when testing
		 - Issue 266: oqs-epiphany not working 
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
		 - Issue 78: Track container usage


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
	- Open Issues: None


13. **liboqs-Java**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 26: Delivering liboqs-java as a JCE provider
		 - Issue 20: Tag 0.1.1
		 - Issue 1: Enable build on Windows


14. **liboqs-Python**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 78: Importing OpenSSL keys and certificates
		 - Issue 74: Kat-Vector-Falcon


15. **liboqs-Rust**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 259: feat: update liboqs, add ml-kem / ml-dsa
		 - PR 260: feat: Auto-allocate stack in runtime
		 - PR 261: chore(ci): bump KyleMayes/install-llvm-action from 1.9.0 to 2.0.3 in the actions group
		 - PR 264: build: Update build script to enable cross compiling for Android
	- Open Issues:
		 - Issue 266: failed to run custom build command for `oqs-sys v0.9.1+liboqs-0.9.0`
		 - Issue 265: Cross compilation results in size mismatch of `ssize\_t` and pointer size
		 - Issue 263: MacOS build fails (as linking against OpenSSL1 instead of 3)
		 - Issue 262: Please document how to build against the system copy of liboqs
		 - Issue 216: Don't recompile oqs everytime cargo build is invoked
		 - Issue 202: expose `OQS\_PERMIT\_UNSUPPORTED\_ARCHITECTURE`, for example as cargo feature
		 - Issue 137: Support RustCrypto KEM and Signature traits
		 - Issue 131: WASM compatibility
		 - Issue 127: ARMv8 compatibility: CI and cross-compiling?


16. **www.openquantumsafe.org** : No updates
