# 2024-01-16 - OQS status meeting - agenda

<span style="color: red;"> Tuesday January 16 at 12:30 PM </span> US Eastern Time / 6:30 PM Central European / 9:30 AM US Pacific Time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Agenda

1. Status updates
2. liboqs 0.9.2 release
3. Maintainer for liboqs-Rust
4. Safety of stateful hash-based signature API

## OQS subprojects

1. liboqs
2. OQS-OpenSSL 3 provider
3. OQS-BoringSSL
4. OQS-OpenSSH
5. OQS-libssh
6. oqs-demos
7. profiling
8. ci-containers
9. liboqs language wrappers: liboqs-C++, liboqs-.NET, liboqs-Go, liboqs-Java, liboqs-Python, liboqs-Rust
10. www.openquantumsafe.org

## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **liboqs**


	- Merges in the last 7 days:
		 - PR 1656: Address  stateful-sigs comments in #1650
		 - PR 1659: Bump gitpython from 3.1.37 to 3.1.41 in /scripts/copy\_from\_upstream
		 - PR 1655: Update `sig\_stfl.h` document for #1650
		 - PR 1658: Zephyr: fixes for platform support
		 - PR 1661: Bump jinja2 from 2.11.3 to 3.1.3 in /scripts/copy\_from\_upstream
		 - PR 1641: Riscv zephyr support
	- Open PRs:
		 - PR 1560: Test against all 100 KAT values
		 - PR 1603: Make common algorithms implementation pluggable
		 - PR 1626: Add ML-DSA-ipd and ML-KEM-ipd & NIST supplied test vectors
		 - PR 1650: Add Stateful Signature (XMSS and LMS)
		 - PR 1653: find\_package(Threads) regardless of BUILD\_ONLY\_LIB
		 - PR 1654: Run oqs-provider release tests in CI on release candidate branches
		 - PR 1664: Zephyr: CMake fixes
	- Open Issues:
		 - Issue 1663: Update documentation and license text.
		 - Issue 1662: Add Apache 2.0 and MIT License to XMSS
		 - Issue 1648: Better separate internal and public APIs
		 - Issue 1647: (Automated) downstream release testing
		 - Issue 1642: Objects of target "oqs" referenced but is not an OBJECT library.
		 - Issue 1639: CI tooling for variable-time operations on some platforms
		 - Issue 1630: Improve CI for macOS on Apple Silicon
		 - Issue 1623: Update PR approval requirements
		 - Issue 1619: Introduce constant time build variable
		 - Issue 1608: Support multiple Falcon signature formats
		 - Issue 1606: OQS\_SHA*\_sha***\_ API does not support arbitrary length updates
		 - Issue 1599: Make low-level crypto algorithms implementation switchable
		 - Issue 1596: Update HQC AVX2 implementation
		 - Issue 1591: Falcon variable length signatures 
		 - Issue 1573: ARM build fails with `-DOQS\_DIST\_BUILD=OFF` on CircleCI
		 - Issue 1564: Update README and other documentation to better describe algorithm status
		 - Issue 1561: Falcon-1024 KATs differ from upstream
		 - Issue 1540: Environment-specific Classic McEliece constant-time leaks
		 - Issue 1539: Update OpenSSL integration
		 - Issue 1521: Update Kyber and Dilithium to FIPS versions
		 - Issue 1514: Review & automate license management
		 - Issue 1494: Use modern CMake syntax
		 - Issue 1490: Add option to exclude the compilation of OQS\_randombytes\_system() when a custom algorithm is specified
		 - Issue 1474: Multithreading tests
		 - Issue 1466: Integrate Kyber implementation from libjade
		 - Issue 1456: Add telltale error handling in void functions
		 - Issue 1443: OQS\_ENABLE\_KEM\_BIKE forced to OFF for ARCH\_X86
		 - Issue 1437: CC0 license is an obstacle
		 - Issue 1418: Expand test coverage to all 100 NIST KAT values
		 - Issue 1416: RISC-V support
		 - Issue 1408: Test all scripts
		 - Issue 1366: Wrong flag passed to Clang when memory sanitizer build is requested.
		 - Issue 1233: Common code for s390x / ppc64le, Windows
		 - Issue 1215: Add fuzzing testing
		 - Issue 1206: Adding a DeriveKeyPair functionality
		 - Issue 1199: WASM compatibillity
		 - Issue 1185: Adding a build variable to specify armv8 version
		 - Issue 1138: Correct OQS\_MINIMAL\_BUILD logic when introducing new optimizations
		 - Issue 1098: Add stateful hash-based signatures
		 - Issue 1083: Enabling more compiler warnings
		 - Issue 1072: Android Buildscript problem with Cross Compilation
		 - Issue 910: Establish interop with Circl
		 - Issue 594: Add options for iOS and Android cross-compilation
		 - Issue 167: Code coverage


2. **OQS-OpenSSL 3 provider**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 294: Fix #272: check `c\_obj\_create` error code for `OBJ\_R\_OID\_EXISTS`.
		 - PR 301: Prepare 240 for merge
		 - PR 316: Generate code coverage using source-based LLVM code coverage.
		 - PR 317: Implementation of Composite Sig
		 - PR 334: Bump jinja2 from 3.0.3 to 3.1.3 in /oqs-template
	- Open Issues:
		 - Issue 331: Supporting Stateful Signatures
		 - Issue 328: Automate testing for backlevel liboqs variants
		 - Issue 319: how to integrate provider with openssl no-shared static build
		 - Issue 318: commit f205f116 broke tests
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


3. **OQS-BoringSSL**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 96: Add OpenSSL interop testing
		 - Issue 81: Introduce TLS\_DEFAULT\_GROUPS env var
		 - Issue 77: Automate hybrid strength assignment
		 - Issue 60: Add some OQS tests to x509/x509\_test.cc and evp/evp\_test.cc


4. **OQS-OpenSSH**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 154: OQS SSH Key Signing for PKI fails with quantum-resistant algorithms
		 - Issue 153: Fix version number
		 - Issue 152: Displayed version is not updated for 2023-10 release since 2022-08
		 - Issue 150: Memory leaks in oqs ecdh path
		 - Issue 149: Merge conflict markers in ssh\_config.5
		 - Issue 145: New "permanent temporary" P256+Kyber768 IANA codepoint support in OQS OpenSSH
		 - Issue 135: Migrate to OpenSSH 9.2
		 - Issue 90: OpenSSH 8.4: Figure out if the regression suite can be augmented
		 - Issue 89: Figure out why certain tests are failing.
		 - Issue 24: Enable PQ certs


5. **OQS-libssh**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 21: pkd\_hello test suite breaks on Ubuntu 22.04 host


6. **oqs-demos**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 220: Update unbound DNS for openssl 3.x.x
		 - PR 249: Renaming nginx/fulltest-provider -> nginx/fulltest & delete old fulltest dir.
	- Open Issues:
		 - Issue 255: Wireshark Docker Build Fails with WolfSSL Due to Undeclared 'QSC\_SIG\_CPS' Variable
		 - Issue 253: https://test.openquantumsafe.org:6000 does not accept `x25519\_kyber768`
		 - Issue 230: Fix integrations to specific commits?
		 - Issue 229: Cannot switch off OQS\_HAVE\_GETENTROPY, OQS\_HAVE\_EXPLICIT\_BZERO
		 - Issue 226: haproxy build failed on MacOS 
		 - Issue 216: add into edk2 openssllib
		 - Issue 213: Create cross-platform docker images in github
		 - Issue 200: Path to a NodeJS demo
		 - Issue 182: replace oqs-openssl111
		 - Issue 171: Create CI/docker push for unbound
		 - Issue 92: Add OQS to libnss (enabling loading quantum safe certificate into Chromium)


7. **profiling**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 101: Handshake performance of "reference code" vs "performance code"
		 - Issue 97: Investigate performance drop in handshaking
		 - Issue 96: Investigate memory use changes in handshaking
		 - Issue 88: Change display logic 
		 - Issue 74: Investigate gcc-11/OpenSSL3 profiling results on M1


8. **ci-containers**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues: None


9. **liboqs-C++**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues: None


10. **liboqs-.NET**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues: None


11. **liboqs-Go**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 34: How to use x509 Certificate Signer on golang
		 - Issue 25: Link liboqs statically


12. **liboqs-Java**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 20: Tag 0.1.1
		 - Issue 1: Enable build on Windows


13. **liboqs-Python**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 72: Criptomoneda
		 - Issue 57: Question: Worth while automating install?


14. **liboqs-Rust**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 216: Don't recompile oqs everytime cargo build is invoked
		 - Issue 202: expose `OQS\_PERMIT\_UNSUPPORTED\_ARCHITECTURE`, for example as cargo feature
		 - Issue 137: Support RustCrypto KEM and Signature traits
		 - Issue 131: WASM compatibility
		 - Issue 127: ARMv8 compatibility: CI and cross-compiling?


15. **www.openquantumsafe.org** : No updates
