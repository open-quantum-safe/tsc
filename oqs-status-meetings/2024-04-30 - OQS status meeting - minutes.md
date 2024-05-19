# 2024-04-30 - OQS status meeting - minutes

<!--### Next meeting: Tuesday April 30, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday May 7, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Attendees

- Alex, Basil, Nigel (IBM)
<!--- Christian (MSR)-->
- Douglas, Pravek, Spencer (Waterloo)
- Jason (SandboxAQ)
- Mark, Norm (Cisco)
- Prem (AMD)
<!--- Michael (independent)-->
- Sara (Synopsys)
<!--- Vlad (softwareQ)-->

## Agenda

1. Status updates
2. PQ Code Package updates

## 1. Status updates

### OQS TSC

No updates.

### liboqs

Stateful hash-based signatures: Ready for final review with a goal of merging in the next week.

MAYO: Basil working on changes upstream so it can be imported without too many patches. Aiming for being ready for review next week.

libjade: Now Apache 2 licensed.  Pravek will update accordingly, then looking for more review/feedback. Q: Does the licensing change retroactively apply to past releases? 

Scorecard: Documentation and cleanup still to be done. Nigel mentions that there's a proposal for a PQCA security workgroup and another proposal around CBOM, see https://github.com/PQCA/TAC/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc

### OpenSSL 3 Provider

No updates.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

271 can be closed.

Douglas mentions 273 about HAProxy to Alex in case he's interested.

### Profiling

Spencer looking for feedback on [discussion on what are we looking for in a benchmarking tool](https://github.com/open-quantum-safe/profiling/discussions/112).

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

## 2. PQ Code Package

Nigel mentions that the PQ Code Package Technical Steering Committee will kick off next Thursday May 9, see https://github.com/pq-code-package/tsc/issues/44
