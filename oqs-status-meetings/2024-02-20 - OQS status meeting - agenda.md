# 2024-02-20 - OQS status meeting - agenda

<span style="color: red;"> Tuesday February 20 at 10:00 AM </span> US Eastern Time / 4:00 PM Central European / 7:00 AM US Pacific Time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

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
10. liboqs language wrappers: liboqs-C++, liboqs-.NET, liboqs-Go, liboqs-Java, liboqs-Python, liboqs-Rust
11. www.openquantumsafe.org

## Pre-meeting project reviews

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **OQS Technical Steering Committee**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 2: OQS sub projects: Which ones to drop for good
		 - Issue 1: OQS goal: non-committal research or production use?


2. **liboqs**


	- Merges in the last 7 days:
		 - PR 1697: Change XMSS License from `(Apache 2.0 AND MIT)` to `(Apache 2.0 OR MIT) AND CC0-1.0`
		 - PR 1696: Fix cross compilation and test in CI
		 - PR 1692: Update GitHub Actions workflows for stateful signatures
		 - PR 1701: update brew install instructions to use openssl@3 instead of openssl@1.1.1 [skip ci]
		 - PR 1626: Add ML-DSA-ipd and ML-KEM-ipd & NIST supplied test vectors
	- Open PRs:
		 - PR 1603: Make common algorithms implementation pluggable
		 - PR 1650: Add Stateful Signature (XMSS and LMS)
		 - PR 1694: Refactor OpenSSL Implementation of SHA3 SHAKE to use new Squeeze API
		 - PR 1699: Update liboqs readme to point to oqs-provider instead of deprecated openssl1.1.1 fork [skip-ci]
		 - PR 1700: change from ninja and custom cmake target `run\_test` to using cmake & ctest.
	- Open Issues:
		 - Issue 1691: Align platforms supported with OpenSSL
		 - Issue 1678: Investigate BIKE failures on x86
		 - Issue 1674: Expand weekly test runs to platforms other than x86\_64 / Linux
		 - Issue 1673: Clearly document KAT sources
		 - Issue 1639: CI tooling for variable-time operations on some platforms
		 - Issue 1630: Improve CI for macOS on Apple Silicon
		 - Issue 1623: Update PR approval requirements
		 - Issue 1619: Introduce constant time build variable
		 - Issue 1608: Support multiple Falcon signature formats
		 - Issue 1606: OQS\_SHA*\_sha***\_ API does not support arbitrary length updates
		 - Issue 1599: Make low-level crypto algorithms implementation switchable
		 - Issue 1596: Update HQC AVX2 implementation
		 - Issue 1564: Update README and other documentation to better describe algorithm status
		 - Issue 1561: Falcon-1024 KATs differ from upstream
		 - Issue 1540: Environment-specific Classic McEliece constant-time leaks
		 - Issue 1539: Update OpenSSL integration
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


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 294: Fix #272: check `c\_obj\_create` error code for `OBJ\_R\_OID\_EXISTS`.
		 - PR 301: Prepare 240 for merge
		 - PR 316: Generate code coverage using source-based LLVM code coverage.
		 - PR 317: Implementation of Composite Sig
		 - PR 344: first cut adding ML-*
		 - PR 348: first cut adding ML-*
	- Open Issues:
		 - Issue 339: .deb inside of oqsprovider-linux-x64.zip 0.5.3 does not work & prevents OpenSSL from loading
		 - Issue 338: oqsprovider-linux-aarch64.zip 0.5.3, the .deb incorrectly identifies as AMD64
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


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 155: Fix CI failure
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


6. **OQS-libssh**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 21: pkd\_hello test suite breaks on Ubuntu 22.04 host


7. **oqs-demos**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 220: Update unbound DNS for openssl 3.x.x
	- Open Issues:
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
		 - Issue 101: Handshake performance of "reference code" vs "performance code"
		 - Issue 97: Investigate performance drop in handshaking
		 - Issue 96: Investigate memory use changes in handshaking
		 - Issue 88: Change display logic 
		 - Issue 74: Investigate gcc-11/OpenSSL3 profiling results on M1


9. **ci-containers**


	- Merges in the last 7 days:
		 - PR 71: Install MinGW in Focal for cross-compilation
	- Open PRs: None
	- Open Issues: None


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
		 - Issue 25: Link liboqs statically


13. **liboqs-Java**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 20: Tag 0.1.1
		 - Issue 1: Enable build on Windows


14. **liboqs-Python**


	- Merges in the last 7 days: None.
	- Open PRs:
		 - PR 73: alpine:3.16 security upgrade
		 - PR 75: Remove support for NIST KAT RNG
	- Open Issues:
		 - Issue 74: Kat-Vector-Falcon
		 - Issue 57: Question: Worth while automating install?


15. **liboqs-Rust**


	- Merges in the last 7 days: None.
	- Open PRs: None
	- Open Issues:
		 - Issue 216: Don't recompile oqs everytime cargo build is invoked
		 - Issue 202: expose `OQS\_PERMIT\_UNSUPPORTED\_ARCHITECTURE`, for example as cargo feature
		 - Issue 137: Support RustCrypto KEM and Signature traits
		 - Issue 131: WASM compatibility
		 - Issue 127: ARMv8 compatibility: CI and cross-compiling?


16. **www.openquantumsafe.org** : No updates