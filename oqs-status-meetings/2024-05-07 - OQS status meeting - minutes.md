# 2024-05-07 - OQS status meeting - minutes

### Next meeting: Tuesday May 14, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

<!--### Next meeting: Tuesday May 7, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

## Attendees

- Alex, Mariam, Max, Nigel (IBM)
<!--- Christian (MSR)-->
- Douglas, Pravek, Spencer (Waterloo)
- Jason (SandboxAQ)
- JP (Quantum Resistant Ledger)
- Mark, Norm (Cisco)
- Michael (independent)
<!--- Sara (Synopsys)-->
<!--- Vlad (softwareQ)-->

## Agenda

1. Welcomes
1. Status updates

## 1. Welcomes

Welcome to new participants joining the call: Mariam from IBM and JP from Quantum Resistant Ledger.

## 2. Status updates

### OQS TSC

No updates.

### liboqs

Michael notes many build failures on the dashboard.

1784: Documentation fixed.

Scorecard: 

- Nigel will rebase the PR.
- Report highlights some missing checks that we should be doing, such as fuzzing.
- Nigel to create new (or lift up existing) issues highlighted by the scorecad
- Apparently this can be used to populate the Security tab on Github
	- Michael suggests fixing as many issues as possible first so that out profile looks good
- Who can help with tokens for triggering downstream builds? Ry?
- Michael asks about constant time checks and why they're not part of the scorecard. Douglas responds that constant-time checks are very specific to cryptographic code, the scorecard is meant to be security best practices for more general open source code.

Stateful hash-based signatures:

- Douglas will review this week.

Kyber from libjade:

- Thanks to Michael for review
- Licence changes have been applied to the tip of the libjade repository and will be propagated back by the end of the month
- Michael asks if these implementations will be available by default. If so, how will users know which implementations are being used. Pravek to make an issue in provider to discuss how to surface this information.
- Spencer asks about performance timing. Pravek doesn't have numbers available.

Markdown linter: Pravek asks if there is a Markdown spec we should be pinned against.

### OpenSSL 3 Provider

410: Needs review.

399: The problem is with another project, not our code.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

Mariam will start working on contributing changes / documentation for HAProxy.

### Profiling

No updates.

### CI containers

Ubuntu 22.04: 

- We should prioritize updating this.
- Pravek says we should document which subprojects use which containers.
- Spencer asks if this could be automated.
- Michael suggests Dependabot. Norm has has some experience with Dependabot and can take a look.


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
