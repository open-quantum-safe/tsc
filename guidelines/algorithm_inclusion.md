# Guidelines on algorithm inclusion in OQS

Informed by [OQS's positioning](https://github.com/open-quantum-safe/tsc/blob/main/governance/project_lifecycle.md) as "Labs Stage" on the "Research Projects" track of the Post-Quantum Cryptography Alliance [Project Lifecycle Policy](https://pqca.github.io/TAC/Processes/Project_Lifecycle.html), this document outlines some principles on the inclusion of post-quantum algorithms in OQS.

## Types of algorithms

OQS currently supports key encapsulation mechanisms, (stateless) digital signature schemes, and stateful digital signature schemes. Other post-quantum public key primitives are currently out of scope, but could be considered. Symmetric key algorithms are out-of-scope, except to the extent that they are necessary to implement a supported public key algorithm.

## Inclusion criteria

A post-quantum algorithm is a candidate for inclusion in OQS if it meets one of the following criteria:

- Selected for standardization by a notable standards organization such as NIST, IETF, or ISO
- Currently under consideration for standardization by a notable standards organization
- Included in a notable application

An algorithm meeting the above criteria will not necessarily be automatically approved for inclusion. The following are additional factors in deciding to include an algorithm in OQS:

- Individuals / organizations willing to maintain and support the implementation
- Availability of reference and optimized implementations
- Interest from members of the OQS Technical Steering Committee and active contributors

Inclusion of an algorithm in liboqs does not necessarily imply that the algorithm will be included in an OQS subproject, as individual OQS subprojects have their own goals and constraints.

## Deprecation policy

Algorithms may be deprecated and marked for removal from OQS as their status changes. Examples of status changes that may lead to deprecation include:

- If an algorithm was included because it was under consideration for standardization by a standards organization, and then that standards organization decides to not standardize the algorithm
- Cryptanalysis or security vulnerability (see cryptanalysis section below)
- Lack of individuals / organizations willing to maintain and support the implementation
- Lack of interest in the algorithm from the community

Our algorithm deprecation process would normally be:

1. Raise an issue in liboqs proposing the deprecation and removal of the algorithm.
2. In the release notes for the next release of liboqs (say, 0.Y.0), announce that the algorithm is deprecated and will be removed in the subsequent release.
3. After the release of liboqs 0.Y.0, the code can be removed from main branch.

Subprojects will need to determine how to communicate and execute deprecation in a manner appropriate to their development and release cycle.

## Cryptanalysis

Included algorithms must be free from known cryptanalytic attacks. If an included algorithm is shown to be vulnerable to a cryptanalytic attack, then, depending on the severity of the attack, the algorithm may be removed immediately without following the above deprecation policy or temporarily deactivated pending a fix.
