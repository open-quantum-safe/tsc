# 2024-07-23 - OQS status meeting - minutes

<!--### Next meeting: Tuesday July 23, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

<!-- ### Next meeting: Tuesday July 30, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09) -->

## Attendees

- Alex B, Basil, Max (IBM)
- Douglas, Spencer (Waterloo)
- Mark, Norm (Cisco)
- Prem (AMD)
- Sara (Synopsys)
- Vlad (softwareQ)
- Yarkin (NVIDIA)

## Agenda

1. Trail of Bits audit
2. Issue triaging / prioritization
3. Status updates
4. liboqs 0.11.0 release planning
5. CBOM demo from Max

## 1. Trail of Bits audit

Douglas reports that Trail of Bits has given us a report based on their first week of activity, with a few small issues to resolve and some recommendations around CI.  There is a meeting scheduled immediately after this meeting with Trail of Bits to discuss the results with them; anyone who would like to join is welcome to attend.  Spencer will translate their findings into issues / pull requests for us to resolve.

## 2. Issue triaging / prioritization

We are starting to have a large number of issues piling up. Douglas asks if anyone has any recommendations around organizing these issues. Max and Alex suggest a project board with a "3 lane approach": an "icebox" containing all issues (set up Github to automatically add this), then columns for "prioritized" (committers can move issues to prioritized) and "assigned" (anyone can take a prioritized issue and move it to assign to indicate they're starting work on it).  Alex will look into setting up something.

## 3. Status updates

### OQS TSC

No updates.

### liboqs

\#1850: NIST has ML-DSA updates in the code running on their AVCP server that we haven't incorporated yet. Basil suggests waiting until the FIPS documents are released with the changes, at which point upstream will update; Basil to confirm with Gregor about PQ Crystals repository.  This change affects algorithmic interoperability. Douglas asks whether we will need to keep 3 versions (Dilithium Round 3, ML-DSA-idp, ML-DSA)?  To discuss.

### OpenSSL 3 Provider

No updates.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

Alex reminds that feedback continues to be welcome in the discussion on #288 about the plan for revitalizing demos, as well as upvotes on demos of interest.

Norm mentions that he is thinking of adding AVCP testing, and asks where the right place to do it is -- Demos, liboqs, a new repository?  Basil notes that we currently have code in liboqs that pulls test vectors from a NSIT server, this could be similar.  It is also noted that if we're testing common code (AES, SHA) or intermediate values against AVCP, then may need to do it in liboqs to access these non exported symbols in the library.

### Profiling

Spencer asks for thoughts on whether it would be worthwhile to restart what we had in profiling with the latest commits to provide benchmarks for ML-KEM and ML-DSA.  Douglas says it would depend on whether we are confident we're getting meaningful benchmark data.

### CI containers

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

### Website

No updates.

## 4. liboqs 0.11.0 release planning

Douglas to create a discussion in liboqs repository seeking feedback on any further elements people would like to include in liboqs 0.11.0.  It seems like we may be in a position to do a release in August.  See discussion here: https://github.com/orgs/open-quantum-safe/discussions/1858

## 5. CBOM demo from Max

Max gives a demo of a tool that can visualize the cryptographic components in a software package based on CBOMs:

- https://github.com/IBM/sonar-cryptography
- https://cbomdb-frontend-scanservice.openshift-cluster-d465a2b8669424cc1f37658bec09acda-0000.eu-de.containers.appdomain.cloud/

