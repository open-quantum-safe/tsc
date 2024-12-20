# OQS Technical Steering – 2024-12-10 – minutes

## Attendees

* Douglas Stebila (U Waterloo)
* Spencer Wilson (U Waterloo)
* Michael Baentsch (Intependent)
* Brian Jarvis (Amazon)
* Christian Paquin (Microsoft)
* Norman Ashley (Cisco)
* Alex Bozarth (IBM)
* Basil Hess (IBM)

## Agenda

1. Chair's introduction

- Introduction by Douglas.

2. Approve agenda

- No changes requested.

3. Appoint minute-taker

- Basil Hess

4. Review action items from previous meeting

- [Security response team](https://github.com/open-quantum-safe/tsc/issues/60)

- Setup GitHub/email alias: Pending.
- Dry run pending security response policy. Spencer and Douglas to discuss.
- Spencer: Awaiting wet run of HQC incident; will draft process document (PR forthcoming).
- Douglas: Solicit feedback, expecially from people with prior experience.
- Michael: Suggests documenting guidelines on how to interact with upstream projects. Responsiveness from upstreams is a concern; to identify key contacts at upstreams.

5. Reports (PQCA TAC, PQ Code Package) - Spencer

- TAC discussion around supporting context strings in ML-KEM. Google's Tink library doesn't expose context string features, alghough Tink aims at providing higher-level API compared to liboqs.
- PQCP mlkem-native version 1.0-alpha has been released, with Pravek and Basil working on its integration with OQS.


6. [SLH-DSA and which upstream code bases to rely on](https://github.com/open-quantum-safe/liboqs/issues/1894)

- Options presented are: Develop an independent implementation. Await availability from an upstream source. Utilize OpenSSL’s upcoming implementation. Exclude SLH-DSA entirely.
- Michael shared that OpenSSL is developing its own SLH-DSA implementation from scratch, alongside including other PQ standard implementations. The SLH-DSA implementation won't be formally verified.
- Christian raises question on the role of OQS once crypto libraries include own implementations of PQ standards.
- Douglas outlines potential value propositions of liboqs: availability of a wide set of algorithms and formally verified implementations. The team brings up other propositions: performance-optimized (assembly) versions, and diversity of implementations. Brian notes that PQCP's ML-KEM implementation is formally verified.
- Spencer notes that if including OpenSSL’s SLH-DSA implementation, the algorithms would not be able available to users disabling OpenSSL in the liboqs build. Questions on the sense of incorporating OpenSSL's implementation in oqs-provider were raised, circular dependencies might be another concerns. It might still be valuable to include for enabling constructions like composites.
- Norm and Duc expressed interest in contributing to SLH-DSA implementation, potentially leveraging other upstream resources.
- Michael emphasized considering the option to drop SLH-DSA support entirely, also for (CI) resources concerns.
- Douglas will reach out to upstream providers such as SPHINCS+ and pqclean and drafting an approach for approaching upstreams, likely in the security policy discussion thread.

7. [Binary distributions](https://github.com/orgs/open-quantum-safe/discussions/1625)

- Ubuntu has expressed interest in including liboqs/oqs-provider but only with no plain PQ algorithms. This raises implications for configuration.
- Action: Create a wiki/markdown page documenting binary distributions shipped.
- Suggestion: Ensure GitHub contacts for communication are accessible.

8. Other business

- Agreement to set the ops-openssl 1.1.1 fork and liboqs-dotnet repositories to read-only status (archive).
- Spencer to update the website with links to archived repositories, providing interested parties the ability to revive them if needed.
- libssh to also be archived following consensus.
- Question raised by Alex if the arm64 runner used in OQS is a self-hosted runner. Clarification provided that the project currently uses the GitHub-hosted beta runner, which may resemble a self-hosted instance. Alex will open a PR in the TSC repository to address this.
