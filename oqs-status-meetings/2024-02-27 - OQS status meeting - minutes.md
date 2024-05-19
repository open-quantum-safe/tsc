# 2024-02-27 - OQS status meeting - minutes

*Attendees: Alex (Cisco); Eric (AWS); Douglas, Pravek, Spencer (Waterloo); Jason (SandboxAQ); Michael; Sara (Synopsys)*

<!--### Next meeting: Tuesday February 27, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday March 5 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Agenda

1. TSC meeting
1. Status updates

### 1. TSC meeting

Douglas needs to schedule a OQS TSC meeting.

## 2. Status updates

### liboqs

Stateful hash-based signatures: review continues.

Falcon: Ready for review in PQClean and then can merge into OQS.

0.10.0:

- Falcon should be straightforward and a quick review.
- Stateful hash-based signatures could be further out since it's such a big PR.
- Michael would prefer an earlier 0.10.0 release to land ML-KEM-ipd and ML-DSA-ipd soon, and then can hold SHBS for 0.11.0.
- We will target a release candidate by next week.

### OpenSSL 3 Provider

KEM OIDs: Pravek to investigate what the IETF Interop is using.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

Will need to be updated with ML-KEM and ML-DSA.

### Profiling

Will need to be updated with ML-KEM and ML-DSA.

Noting that profiling is in a deteriorated state.  Spencer would like to redo profiling.  Should have some discussions about our intended use case for profiling.

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

