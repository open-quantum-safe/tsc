# 2024-03-05 - OQS status meeting - minutes

### Next meeting: Tuesday March 12, 2024 at 12:30pm US Eastern time / <span style="color: red;">5:30pm Central European (note change to Daylight Saving Time in North America)</span> / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

<!--### Next meeting: Tuesday February 27, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

<!--### Next meeting: Tuesday March 5 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

## Attendees

- Alex B, Basil, Max, Nigel (IBM)
- Brian (AWS)
- Christian (MSR)
- Douglas, Spencer (Waterloo)
- Jason, Thomas (SandboxAQ)
- Mark, Norm (Cisco)
- Michael
- Prem (AMD)
- Ry (Linux Foundation)
- Sara (Synopsys)

## Agenda

1. Welcome
1. Status updates
1. PQ Code Package virtual hack day

## 1. Welcome

Welcome to the new faces joining the call!

Ry reminds people that if they would like to join the PQCA Discord, it's at https://discord.gg/xyVnwzfg5R.

## 2. Status updates

### liboqs

Falcon: A few small things were left to deal with - naming conventions and a superfluous license
	- License issue: dealt with
	- Naming conventions: Spencer has a draft PR to fix this in PQClean; need reviews. Then can finalize Falcon updates in liboqs.

Stateful hash-based signatures:

- Spencer continuing to review.
- Norm will respond to questions from Spencer about files from upstream.
- Norm can help with XMSS feedback when it comes in.
- Christian attended NCCoE meeting on SHBS. NIST looking at comments from implementers about restrictions on state management and export.

alg_support.cmake: Basil and Michael have agreed on a path forward. Basil will update the PR.

OpenSSF scorecard: still some issues to address.

#### 0.10.0 release planning

Agreed to save SHBS for 0.11.0.

Michael things all other issues in the 0.10.0 milestone should be easily addressable and will work with Spencer to finalize them.  Spencer noticed some constant-time failure on SPHINCS+; will create issue.

Spencer and Michael will prepare the release notes and tag -rc1.

### OpenSSL 3 Provider

OIDs:

- Michael would like to see someone take leadership on list of OIDs -- too many places to check.
- Basil says IBM has OIDs for ML-DSA-ipd and the Bouncycastle has OIDs for ML-KEM-ipd.
- This discussion can be directed towards issue #351.

Thanks to Spencer for preparing the PR for Falcon-padded.  

Michael wants to know about the prospect of including composite sigs (#317) in the next release. Will continue discussion on pull request.

### BoringSSL

Some recent updates. Michael working with contributor pi-314159 to continue. Anticipate that BoringSSL will (still) not have as full support as oqs-provider, but will have some algorithm updates.

### OpenSSH and libssh

Brian will check with the AWS team to see if they have bandwidth to update OpenSSH. They will eventually want to interop with it when they get further along with ML-KEM internally

### OQS-Demos

Will need to be updated with ML-KEM and ML-DSA.  Volunteers welcome.

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

## 3. PQ Code Package virtual hack day

The PQ Code Package virtual hack day will take place on Tuesday March 12.  For more information, see https://hackathon.pqcodepackage.org/ or contact Nigel Jones (jonesn@Uk.ibm.com).
