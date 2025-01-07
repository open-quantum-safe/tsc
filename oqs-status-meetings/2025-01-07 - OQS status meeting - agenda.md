# 2025-01-07 - OQS status meeting - agenda

<span style="color: red;"> Tuesday January 07 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://pqca.org/calendar/)

## Agenda

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
10. www.openquantumsafe.org
11. liboqs language wrappers: liboqs-C++, liboqs-.NET, liboqs-Go, liboqs-Java, liboqs-Python, liboqs-Rust

## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **OQS Technical Steering Committee**


	- Merges in the last 7 days:
		 - PR 125: Add oqs-maintainers to openssl 1.1.1 repository
	- Open PRs:
		 - PR 100: Draft minutes from 2024-09-10 TSC meetings
		 - PR 123: Add TSC 2024-12-10 minutes
		 - PR 124: Draft: OQS security response process
	- Open Issues:
		 - Issue 120: OpenSSF best practices badge
		 - Issue 60: Decide security (issue) report handling team and procedure
		 - Issue 49: Switch open-quantum-safe/openssl to read-only
		 - Issue 45: Roles of maintainers & contributors
		 - Issue 28: Automated dependency management
		 - Issue 27: Rollout scorecards across more repos
		 - Issue 24: Decide procedure(s) to handle CI failures
		 - Issue 12: Create a voting procedure for the OQS TSC
		 - Issue 11: Confirm mailing list openness and retention
		 - Issue 5: CI in OQS: guidelines for responsible use
		 - Issue 2: OQS sub projects: Which ones to drop for good
		 - Issue 1: OQS goal: non-committal research or production use?


2. **liboqs**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 1876: CPU extension detection for arm64 on NetBSD.
		 - PR 1877: Add DeriveKeyPair API
		 - PR 1934: Adds sha3 to arm compile options which is needed for ios compilation.
		 - PR 1970: Add Nix flake
		 - PR 1994: Use seed as private key format for ML-KEM
		 - PR 2009: Add checks for ML-KEM keys
		 - PR 2022: Add faces of contributors to README
		 - PR 2031: extended api for allow use fixed seed for generate key pair and generate public key from private key in Signature schemes
		 - PR 2033: Add threat model
	- Open Issues:
		 - Issue 2034: Use of non-default OSSL\_LIB\_CTX* within OpenSSL construction
		 - Issue 2032: Supporting "seed" private key format
		 - Issue 2030: Signatures: derive keypair from seed or public key from private key
		 - Issue 2029: liboqs is not ready for cross-compilation
		 - Issue 2028: Add UOV sig alg
		 - Issue 2024: Add Wycheproof test vectors
		 - Issue 2016: Update Doxygen documentation
		 - Issue 2001: Deprecate signature API without context string?
		 - Issue 1999: Strengthen signature verification failure tests 
		 - Issue 1995: CROSS broken sigs validate 
		 - Issue 1991: Develop policy about algorithm deprecation
		 - Issue 1989: Drop Kyber support
		 - Issue 1986: 9 tests fail: No such file or directory: 'build/tests/vectors\_kem'
		 - Issue 1973: Build liboqs for MacOS M1 (arm64)
		 - Issue 1958: Verification error in CROSS-RDSDPG-128-small
		 - Issue 1951: ML-KEM doesn't perform encapsulation key check
		 - Issue 1946: [Feature request] SQIsign
		 - Issue 1945: Correct openssl init functions to take build params into account
		 - Issue 1933: Compilation error: <instantiation>:16:5: error: instruction requires: sha3
		 - Issue 1931: NIST CAVP validation of liboqs ML-DSA algorithm
		 - Issue 1928: Improve documentation about algorithm implementation sources
		 - Issue 1918: Release Builds Location?
		 - Issue 1915: Remove unsupported Kyber upstreams
		 - Issue 1912: Automatically trigger CI based on git diff
		 - Issue 1904: Explicitly testing generic and non-generic code variants
		 - Issue 1896: Unused variable in Classic McEliece
		 - Issue 1894: SLH-DSA: integrate final standard
		 - Issue 1882: CMAKE\_POSITION\_INDEPENDENT\_CODE should be optional
		 - Issue 1868: Add CodeQL query to check for memset calls
		 - Issue 1867: Add CodeQL query to enforce OpenSSL return code handling
		 - Issue 1864: memset used instead of OQS\_MEM\_CLEANSE
		 - Issue 1856: Add GitHub Actions to automate project board management 
		 - Issue 1851: Add diagrams for minimal examples in wiki and liboqs documentation
		 - Issue 1842: Use OQS\_*\_set\_callbacks instead of C\_OR\_NI\_OR\_ARM macros
		 - Issue 1841: Document public / internal API split
		 - Issue 1840: Define threat model for liboqs
		 - Issue 1829: scorecard: publish results & run weekly
		 - Issue 1824: huge stack usage
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
		 - Issue 1514: Review & automate license management
		 - Issue 1494: Use modern CMake syntax
		 - Issue 1474: Multithreading tests
		 - Issue 1456: Add telltale error handling in void functions
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
		 - Issue 910: Establish interop with Circl and other implementations
		 - Issue 167: Code coverage


3. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days:
		 - PR 607: Allow overriding OPENSSL\_MODULES\_PATH from the command line
		 - PR 606: change code point and name for mlkem1024 hybrid
		 - PR 611: limit testing to oqsprovider
		 - PR 614: Include use of loaded 'libctx' context in KEM and SIG procedures (#557)
	- Open PRs:
		 - PR 367: improve static build testing
		 - PR 597: Add key-type specific en- / decoder
		 - PR 616: add more complete KEM ENCODERS testing in recent openssl versions
	- Open Issues:
		 - Issue 613: ML-KEM private keys not compatible with draft-ietf-lamps-kyber-certificates-06 (seed as private key)
		 - Issue 612: Add cross-provider interop tests
		 - Issue 600: Addition of Brainpool curves to KEM procedures
		 - Issue 594: output debug messages to standard error stream
		 - Issue 590: Add static build CI
		 - Issue 571: use only public part to test key encapsulation
		 - Issue 569: cannot "print" either public or private key
		 - Issue 566: Build oqs-provider with only kyber tls key exchange functionality
		 - Issue 562: i2d\_PublicKey() fails with -1 for DILITHIUM2 key while using OQS provider with OpenSSL 3.2.1
		 - Issue 561: Re-assign all code points
		 - Issue 560: Multiple names for an algorithm
		 - Issue 553: Error handling in TLS is incorrect or missing
		 - Issue 545: Add test for out-of-source builds and tests
		 - Issue 539: Issue with Loading oqsprovider.so on Android using OSSL\_PROVIDER\_load
		 - Issue 526: SonarQube Static Analysis of oqsprovider 
		 - Issue 514: Static Analysis Issues 
		 - Issue 509: How can we get the part of the elliptic curve from the PKEY and use it as the public key of a digital certificat
		 - Issue 490: Add code coverage testing
		 - Issue 488: Testing in openssl 3.1/3.0
		 - Issue 485: Document & test the new/3.4.0 encap/decap feature
		 - Issue 483: Reliability
		 - Issue 482: Windows: Build fails when using OQS\_MINIMAL\_BUILD
		 - Issue 481: Handshake Failures with Post-Quantum Certificates on SCTP & DTLS 1.2
		 - Issue 473: CI upgrade breaks clang formatting and asan testing
		 - Issue 466: The privateKey encoding for pure ml-dsa differs from the privateKey encoding for the ml-dsa part in composite ml-dsa-xxxx
		 - Issue 464: tlssig test takes huge amount of time
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


	- Merges in the last 7 days: None.
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
		 - Issue 172: Snapshot release matching liboqs 0.12.0
		 - Issue 164: Add support for XMSS SSH Keys and Certificates
		 - Issue 150: Memory leaks in oqs ecdh path
		 - Issue 90: OpenSSH 8.4: Figure out if the regression suite can be augmented
		 - Issue 89: Figure out why certain tests are failing.
		 - Issue 24: Enable PQ certs


6. **OQS-libssh**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 25: Update README prior to archiving
		 - Issue 24: Deprecated Function Errors - Correct OpenSSL Version?
		 - Issue 21: pkd\_hello test suite breaks on Ubuntu 22.04 host


7. **oqs-demos**


	- Merges in the last 7 days:
		 - PR 337: Bump cURL version to 8.11.1
	- Open PRs:
		 - PR 338: Comprehensive Updates and Optimizations to Docker Files
	- Open Issues:
		 - Issue 332: Update CI to use GitHub-hosted runner
		 - Issue 328: Utilize LLM to Review Documentation
		 - Issue 308: Remove docker hub references
		 - Issue 301: Scanning of container images
		 - Issue 300: Consider use of opencontainers spec metadata in container images
		 - Issue 270: Dont get Server Temp Key in openssl s\_client when testing
		 - Issue 266: oqs-epiphany not working / maintainer sought
		 - Issue 255: Wireshark Docker Build Fails with WolfSSL Due to Undeclared 'QSC\_SIG\_CPS' Variable
		 - Issue 216: add into edk2 openssllib
		 - Issue 200: Path to a NodeJS demo


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


10. **www.openquantumsafe.org**


	- Merges in the last 7 days:
		 - PR 241: Add Meta to the list of external users of OQS
	- Open PRs:
		 - PR 242: Mark liboqs-dotnet as deprecated
	- Open Issues:
		 - Issue 216: Update benchmarking section
		 - Issue 215: Change integrations text
		 - Issue 197: Create CI


11. **liboqs-C++**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 21: Add API for signatures with context string


12. **liboqs-.NET**


	- Merges in the last 7 days:
		 - PR 32: Update README prior to archiving repository
	- Open PRs: None
	- Open Issues: None


13. **liboqs-Go**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 46: Version Incompatibility in Client-Server Communication Using liboqs and PQCrypto
		 - Issue 44: Add API for signatures with context string


14. **liboqs-Java**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 29: Add support for ML-DSA context
		 - Issue 28: Enable Build On Windows
		 - Issue 27: LibOQS-Java will need to support passing in the Context String into the Sign API
		 - Issue 26: Delivering liboqs-java as a JCE provider
		 - Issue 20: Tag 0.1.1
		 - Issue 1: Enable build on Windows


15. **liboqs-Python**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 94: replacing openssl111 with openssl3
		 - PR 95: provide an alternate way to set liboqs path
		 - PR 97: Beautify code
	- Open Issues:
		 - Issue 98: Add API for signatures with context string
		 - Issue 96: Validate build passes against python 3.12
		 - Issue 91: Failures on ACVP Vectors for ML-DSA-65 and ML-DSA-87
		 - Issue 78: Importing OpenSSL keys and certificates
		 - Issue 74: Kat-Vector-Falcon


16. **liboqs-Rust**


	- Merges in the last 7 days:
		 - PR 273: fix: run install target during build
	- Open PRs:
		 - PR 259: feat: update liboqs, add ml-kem / ml-dsa
		 - PR 260: feat: Auto-allocate stack in runtime
		 - PR 261: chore(ci): bump KyleMayes/install-llvm-action from 1.9.0 to 2.0.3 in the actions group
		 - PR 264: build: Update build script to enable cross compiling for Android
		 - PR 268: feat: update to liboqs 0.11.0 and various Rust changes
	- Open Issues:
		 - Issue 269: Zeroize mem / proj status re safe-oqs?
		 - Issue 266: failed to run custom build command for `oqs-sys v0.9.1+liboqs-0.9.0`
		 - Issue 265: Cross compilation results in size mismatch of `ssize\_t` and pointer size
		 - Issue 262: Please document how to build against the system copy of liboqs
		 - Issue 216: Don't recompile oqs everytime cargo build is invoked
		 - Issue 202: expose `OQS\_PERMIT\_UNSUPPORTED\_ARCHITECTURE`, for example as cargo feature
		 - Issue 137: Support RustCrypto KEM and Signature traits
		 - Issue 131: WASM compatibility
		 - Issue 127: ARMv8 compatibility: CI and cross-compiling?
