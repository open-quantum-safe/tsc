# 2024-01-02 - OQS status meeting - minutes

*Attendees: Christian (MSR); Douglas, Eddy, Pravek, Spencer (UW); Eric (AWS); Mark (Cisco); Michael; Sara (Synopsys); Vlad (softwareQ)*

<!--### Next meeting: Tuesday January 2, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday January 9 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Agenda

1. Status updates
2. liboqs 0.9.2 release planning
3. API structure - internal / SHA-3

## 1. Status updates

### liboqs

Updated constant-time suppression files for Falcon and BIKE have landed.

PR #1643 needs review.

Michael notes a problem between liboqs 0.9.1 release and oqs-provider related to HQC; oqs-provider failed because stuff didn't get cherry-picked over properly and tests (oqs-provider release-test scripts) weren't run on the downstream oqs-provider before liboqs release.  Should be added to release process page on OQS wiki.

### OpenSSL 3 Provider

A 0.5.3 release is waiting to sync with 0.9.1.  Should it be released, or wait until 0.9.2?  Decision is to wait until 0.9.2.

There was an issue asking why we used SHA-384 in a hashing the hybrid signature between Dilithium2 and ecdsap256.  Douglas says he doesn't know why.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

No updates.

### Profiling

No updates.

### Language wrappers

**liboqs-cpp.**
No updates.

**liboqs-dotnet.** 
No updates.

**liboqs-go.** 
No updates.

**liboqs-java.**
No updates.

**liboqs-python.** 
No updates.

**liboqs-rust.**
No updates.

### CI Containers

No updates.

### Website

No updates.

## 2. liboqs 0.9.2 release

This would address additional Kyber potentially non-constant-time divisions.  

Spencer and Pravek will help pulling in the code updates needed.  Goal is to have a release candidate by end of week and then do the release early next week.

Douglas to create a branch for this security release.

Michael to highlight the commit needed to be cherry-picked over to avoid problems with oqs-provider.

## 3. API structure - internal / SHA-3

Spencer asks whether our API especially around SHA-3 is being exposed the way we intend.  He noticed that sha3.h is being installed in the include/oqs directory and that some functions are available in test programs.  Douglas says that for the header file, it could just be a mistake in the CMake configuration.

## 4. Other business

Christian reports that the NCCoE has released some reports for which they are seeking feedback:

https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms


