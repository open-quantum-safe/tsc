# 2024-01-16 - OQS status meeting - minutes

*Attendees: Alex, Mark, Norm (Cisco); Christian (MSR); Douglas, Pravek, Spencer (UW); Eric (AWS); Jason (SandboxAQ); Michael; Sara (Synopsys); Vlad (softwareQ)*

<!--### Next meeting: Tuesday January 2, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday January 23 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Agenda

1. Status updates
2. liboqs 0.9.2 release
3. Maintainer for liboqs-Rust
4. Safety of stateful hash-based signature API

## 1. Status updates

### liboqs

No updates.

### OpenSSL 3 Provider

No updates.

### BoringSSL

No updates.

### OpenSSH and libssh

Should we label OpenSSH as less supported / deprecated? Christian does not have bandwidth to do major updates like in the past.  Michael notes that the falcosecurity organization on Github has some promising documents on denoting project lifecycle.

### OQS-Demos

Christian reports that in the NCCoE, Palo Alto Networks wants to start doing some VPN testing.  Do we have any IPsec demos?  No, only OpenVPN, which is TLS-based.

### Profiling

No updates.

### Language wrappers

**liboqs-cpp.**
No updates.

**liboqs-dotnet.** 
No updates.

**liboqs-go.** 
Vlad has a fix for issue #25.  Will release a version matching liboqs 0.9.2 later this week.  Regarding the X.509 issue #34, is this in scope of liboqs-go?  No, seems to be about higher level APIs in Go which are not part of the liboqs language wrapper.  Vlad to respond that it's out of scope then close.

**liboqs-java.**
No updates.

**liboqs-python.** 
Vlad has a fix coming for issue #57 which will install liboqs if it's not found.

**liboqs-rust.**
No updates.

### CI Containers

No updates.

### Website

No updates.

## 2. liboqs 0.9.2 release

Douglas asks for feedback on the 0.9.2 release candidate.  

Michael created a branch in oqs-provider testing 0.9.2 and everything was fine, so okay to go there.

Spencer ran the release test script for 0.9.2 and it ran fine.  Spencer also ran the constant time tests.  With extensions enabled, everything passed.  With extensions disabled, there were some failures but not in Kyber; Spencer will create an issue to track this but we won't hold the 0.9.2 release for it since it's not related.

Michael asks what else should be released as part of the 0.9.2 release cycle.

- Demos: Normally we do a release tag matching liboqs but the process for generating those builds off of liboqs main; would need to update to build off of a specific tag.  Michael to see how difficult this would be.
- Test server needs to be updated.  Douglas to create an issue and tag Basil.

Consensus: okay for 0.9.2 release. Douglas to release later today.

## 3. Maintainer for liboqs-Rust

After several years of excellent service, Thom is stepping down as maintainer of liboqs-rust.  Vlad has some Rust experience and offers to help maintain, Jason offers as well.  

## 4. Safety of stateful hash-based signature API

Comments were raised today on liboqs PR #1650 with concerns about whether it is safe to make available software-based implementation of stateful hash-based signature schemes.

- Jason thinks it's okay to include in an experimental library -- people want to do experiments. Could rip it out later once we move to production oriented.
- Michael suggests putting it into a separate repository especially since it uses a distinct API from normal signatures.
- Spencer suggests that configuration time flags could be used to turn on/off the key generation and signing. Norm had been considering adding configuration time flags later, but maybe we have to do it sooner rather than later.
- Douglas to think about who else we could ask for an opinion.  Norm notes that Scott Fluhrer has in the past been in agreement with NIST guidance and against having these operations in software.

Norm to look at what it would take to sequester signing and key generation at configuration time. 
