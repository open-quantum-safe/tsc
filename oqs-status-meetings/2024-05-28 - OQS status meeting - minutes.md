# 2024-05-28 - OQS status meeting - minutes

<!--### Next meeting: Tuesday May 14, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday June 4, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Attendees

- Alex, Basil, Max, Nigel (IBM)
- Christian (MSR)
- Douglas, Pravek, Spencer (Waterloo)
- Hart, Ry (Linux Foundation)
- Jason (SandboxAQ)
<!--- JP (Quantum Resistant Ledger)-->
- Mark (Cisco)
<!--- Michael (independent)-->
- Sara (Synopsys)
- Vlad (softwareQ)
<!--- Yarkin (NVIDIA)-->

## Agenda

1. Status updates

## 1. Status updates

### OQS project dashboard

oqs-demos CircleCI build failing. Pravek says that one of them is easy to fix.  Douglas to create an issue to track.

### OQS TSC

Douglas to poll for scheduling a TSC call for mid-June.

### liboqs

Stateful hash-based signatures: Spencer has updated build configuration variable name to include the word HAZARDOUS.  No other known outstanding issues.  This is the final call for reviews of [#1650](https://github.com/open-quantum-safe/liboqs/pull/1650) and will be merged on Friday if there is no objection before then.

MAYO: Basil has some changes locally that he will push. Will be omitting one variant from CI that has larger stack usage.

libjade: Pravek implementing some changes. Still waiting on Tiago for licence changes, he's had some other stuff pop up that has delayed this.

Scorecard: Nigel working to complete some documentation before merging the v4 scorecard. Some previews are available of the v5 scorecard.

PR#1799: Basil will merge.  Basil asks if we can create a new release since this is a bug that is affecting some users.  Douglas notes another issue coming early next week that we might want to also include in a release; more details to follow.

### OpenSSL 3 Provider

Douglas will work with Ry to draft the advisory to obtain a CVE.  Douglas to follow up with Michael to determine if we should tag a release of oqs-provider with the fix.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

No updates.

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

## 2. Other business

Nigel gives updates from PQ Code Package: the TSC met last week and included discussions on what "assured" means.  Input welcome.

Nigel gives updates from the PQCA TAC: the TAC received a presentation from OpenSSF; recording available for those who are interested.
