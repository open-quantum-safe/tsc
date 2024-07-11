# 2024-07-09 - OQS status meeting - minutes

<!-- ### Next meeting: Tuesday July 9, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09) -->

### Next meeting: Tuesday July 16, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Attendees

- Alex B, Basil, Nigel (IBM)
- Alexandra Walker
- Douglas, Pravek, Spencer (Waterloo)
- Goutam
- Mark (Cisco)
- Prem (AMD)
<!-- - Christian (MSR) -->
<!-- - Gerardo (AWS) -->
<!-- - Jason (SandboxAQ) -->
<!-- - Ry (Linux Foundation) -->
<!-- - JP (Quantum Resistant Ledger) -->
<!-- - Michael (independent) -->
<!-- - Sara (Synopsys) -->
- Vlad (softwareQ)
- Yarkin (NVIDIA)

## Agenda

1. Status updates
2. Task force to support Trail of Bits audit

## 1. Status updates

### OQS TSC

No updates.

### liboqs

**MAYO**: Basil has made a small fix to some CI problems. He thinks the code is ready for a final review before merge.

**#1832 Callback API**: Some confusion over what's visible; Spencer will follow up on the PR.

**CVE-2024-31510**: Goutam asks about the status of CVE-2024-31510 (Rowhammer attack on Dilithium implementation). 

- Douglas says that we discussed this and whether it was inside our threat model; we should develop our threat model and then respond based on that. 
- Yarkin notes that an optioin is to have a re-verification ccountermeasure behind a compilation flag.  OpenSSL apparently declares such attacks out of scope; WolfSSL has countermeasures behind a compilation flag.
- Spencer: Suggests another option may be to use magic numbers that are checked after an operation.
- Yarkin will ask wolfSSL about their threat model.
- Douglas will create an issue for creation of a threat model. [Done in Issue #1840](https://github.com/open-quantum-safe/liboqs/issues/1840)

**CBOM**: Basil is working on updating the CBOM to use some new tooling.

### OpenSSL 3 Provider

No updates.

### BoringSSL

No updates.

### OpenSSH and libssh

PR #159 is ready for review.

### OQS-Demos

Alex aims to have a plan about OQS Demos ready for discussion on #286 next week.

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

## 2. Task force to support Trail of Bits audit

Jim from Trail of Bits emailed a few days ago that they will be ready to start work on review liboqs next week.  Douglas would like to have a few people available as a task force to respond to queries from Trail of Bits during the audit.  Basil, Pravel, and Spencer volunteer.
