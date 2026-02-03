# 2026-02-03 - OQS status meeting - agenda

<span style="color: red;"> Tuesday February 03 at 12:30 PM </span> US Eastern Time on Zoom (https://pqca.org/calendar/)

## Agenda

Douglas (@dstebila) out-of-office. Bruce (@xuganyu96) to run through projects.

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

See project dashboard at: https://openquantumsafe.org/dashboard.html

1. **OQS Technical Steering Committee**

    Next OQS TSC meeting: Tuesday February 17

	- Merges in the last 7 days: None.
	- Open PRs:
       - PR 234: Guidelines on algorithm inclusion in OQS, still a draft


2. **liboqs**

	- Merges in the last 7 days:
        - PR 2350: test OQS_SIG_sign methods in vectors_sig
        - PR 2354: Cache ACVP test vectors
        - PR 2357: Avoid inlined exponentiation in CROSS-RSDPG-1
	- Open PRs:
        - PR 2298: plan to close due to mldsa-native replacing pqcrystals
        - PR 2339: SPHINCS+ can be safely removed since oqs-provider already removed support for SPHINCS+


3. **OQS-OpenSSL 3 provider**

    no updates


4. **OQS-BoringSSL**

    no updates

5. **OQS-OpenSSH**

	- Open PRs:
        - PR 187: Add release managers. This is ready to go.


6. **oqs-demos**

    no updates

7. **ci-containers**

    Discussed how Python packages are managed in Ubuntu images. Consider installing `python3-venv` so PyPI packages that are not available as Ubuntu system packages can be included.

8. **www.openquantumsafe.org**

    no updates

9. **liboqs-C++**

    no updates

10. **liboqs-Go**

    no updates


11. **liboqs-Java**

    no updates


12. **liboqs-Python**

    no updates


13. **liboqs-Rust**

    no updates