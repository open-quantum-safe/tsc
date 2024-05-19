# 2024-05-14 - OQS status meeting - minutes

<!--### Next meeting: Tuesday May 14, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday May 21, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Attendees

- Alex, Basil, Mariam (IBM)
<!--- Christian (MSR)-->
- Douglas, Pravek, Spencer (Waterloo)
- Hart, Ry (Linux Foundation)
<!--- Jason (SandboxAQ)-->
<!--- JP (Quantum Resistant Ledger)-->
- Mark, Norm (Cisco)
<!--- Michael (independent)-->
<!--- Sara (Synopsys)-->
<!--- Vlad (softwareQ)-->
- Yarkin (NVIDIA)

## Agenda

1. Welcomes
1. Security issue for oqs-provider
1. Call with Trail of Bits
1. Status updates

## 1. Welcomes

Welcome to new participants joining the call: Yarkin from NVIDIA.

## 2. Security issue for oqs-provider

Douglas reports that a security issue for oqs-provider has been received by email with a proposed patch; Douglas has looped in Michael. Ry notes that Github has a feature to allow for receiving security issues and that this can be used to create private repositories for dealing with the issue as well as issuing an advisory. If the original reporters re-file using this mechanism, then they can get credit as well as a CVE if desired.

## 3. Call with Trail of Bits

Last week, members of the TSC had a call with Trail of Bits, a company that does crypto software audits. They are offering to do some review of the OQS codebase this summer when they have some availability.

## 4. Status updates

### OQS project dashboard

Ry working on debugging personal access tokens, which would help us resolve some current build failures. Also working on ARM runners.

Spencer reports that liboqs-java's build failures are due to API changes, which he will make a PR to fix. Spencer notes that this highlights that liboqs-java hasn't been kept in sync with ongoing development.

### OQS TSC

Douglas has added OQS status call meeting agenda and minutes to the TSC repository under https://github.com/open-quantum-safe/tsc/tree/main/oqs-status-meetings.

### liboqs

MAYO: Basil has a PR ready for review. Failing CI is due to the problem with the downstream trigger; Basil says he has run the tests locally.

Stateful hash-based signatures: Duc has a PR to address the secure free issues.  Spencer going through old unresolved comments and will make a PR.

### OpenSSL 3 Provider

No updates.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

No updates.

### Profiling

Spencer reminds that the discussion on the future of profiling is still open, and has not received much feedback.

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
