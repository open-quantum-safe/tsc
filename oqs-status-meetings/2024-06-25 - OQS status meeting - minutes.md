# 2024-06-25 - OQS status meeting - minutes

<!-- ### Next meeting: Tuesday June 25, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09) -->

### Next meeting: Tuesday July 2, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Attendees

- Alex B, Nigel (IBM)
- Mark, Norm (Cisco)
<!-- - Christian (MSR) -->
- Douglas, Pravek, Spencer (Waterloo)
- Gerardo (AWS)
<!-- - Jason (SandboxAQ) -->
<!-- - Ry (Linux Foundation) -->
<!--- JP (Quantum Resistant Ledger)-->
- Michael (independent)
<!-- - Sara (Synopsys) -->
<!-- - Vlad (softwareQ) -->
- Yarkin (NVIDIA)

## Agenda

1. Status updates
2. Next release of liboqs

## 1. Status updates

### OQS TSC

Thanks to those who responded to the poll for the next OQS TSC meeting. It will be held on Thrusday, June 27, from 12–1pm US Eastern time.

### liboqs

XMSS: PR 1819 is ready for review, this is the last of the XMSS additional parameter sets.

Scorecard: Dialogue still going on ont he issue with Nigel and Michael.

Kyber libjade: Still waiting for response from libjade team.

HQC: Spencer says that this will take longer than expected due to a memroy leak to be resolved upstream.

#1761 Valgrind: Unsure whether this is a bug in Valgrind/Massif or in liboqs. If anyone has expertise on ARM or Valgrind, help here would be appreciated.

### OpenSSL 3 Provider

MAYO: Still failures in the branch testing integration of MAYO into oqs-provider.  What's going on here?  May have to wait for Basil's return.

Gerardo asks if we know about OpenSSL's plans for post-quantum.  Douglas relays the basic story that we know.  Douglas to follow up with LF about discussions on OpenSSL CLA.

### BoringSSL

No updates.

### OpenSSH and libssh

Gerardo has created a PR with an initial draft of updating to OpenSSH v9.  It compiles, but tests fail.  More work to be done still.

### OQS-Demos

Call scheduled for Thursday June 27 at 1:30pm US Eastern time to discuss demos.  Alex's agenda: review the history of each demo, its current state, and then desires for update/overhaul.

### Profiling

No updates.

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

### CI Containers

No updates.

### Website

No updates.

## 2. Next release of liboqs

Items we'd marked for inclusion in the next liboqs release:

- stateful hash-based signatures: have landed
- MAYO: would merit a bump to 0.11.0
- Kyber libjade and HQC AVX2 optimizations: would only be a patch bump (e.g., could be 0.11.1)
- deterministic API
