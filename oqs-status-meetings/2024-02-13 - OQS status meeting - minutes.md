# 2024-02-13 - OQS status meeting - minutes

<!--*Attendees: Alex, Mark, Norm (Cisco); Douglas, Pravek, Spencer (Waterloo); Eric (AWS); Jason (SandboxAQ); Michael*-->

<!--### Next meeting: Tuesday January 30, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday February 20 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Agenda

1. Top-level discussions
1. Status updates

## 1. Top-level discussions

There are discussion posts in the top-level OQS GitHub organization discussions section on subproject status and other issues, please take a look.

## 2. Status updates

### liboqs

ML-KEM and ML-DSA: Ready for review.

Stateful hash-based signatures: ready for review.  Aim to merge next week.

Michael uncertain if trigger from liboqs to oqs-provider has been triggered. Spencer says the second last commit seems to have done this.

### OpenSSL 3 Provider

Code review from Radically Open Security is mostly done, so code freeze can be lifted.

ML-KEM and ML-DSA: Ready for review.  Michael to remove draft status once it's confirmed that CI triggers are okay.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

No updates.

### Profiling

Spencer wants to revisit M1 profiling and consider moving to GitHub Actions.  Douglas cautions that benchmarking via GitHub Actions may not be reliable.

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

