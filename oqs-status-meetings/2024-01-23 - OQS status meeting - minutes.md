# 2024-01-23 - OQS status meeting - minutes

*Attendees: Basil (IBM); Brian (AWS); Christian (MSR); Douglas, Pravek, Spencer (Waterloo); Mark (Cisco); Michael*

### Next meeting: Tuesday January 30, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

<!--### Next meeting: Tuesday January 23 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

## Agenda

1. Status updates
2. liboqs 0.10.0 release planning
3. Linux Foundation update

## 1. Status updates

### liboqs

PR #1560 and #1677 are ready for review.

PR #1676 will have discussion on the PR.

ML-KEM and ML-DSA updates: There's a draft PR but still a few open points to do. Basil hopes to come back to it in a couple of weeks.

AppVeyor is failing on liboqs.  It seems to be an OpenSSL linking failure.  Spencer to investigate.  But this raises some bigger questions:

- Why aren't these included in the CI checks in GitHub?
- Do we even need these?  If we can switch to covering all our Windows CI needs via GitHub Actions, that would simplify things
- Spencer to investigate
- Also need to update the dashboard

### OpenSSL 3 Provider

No updates.

### BoringSSL

Should we mark this is as obsolete or looking for help?  Discussion follows.  Consensus: clearly mark as "looking for help, not actively maintained".  Also update OQS www accordingly.  Michael can do PRs about this.

### OpenSSH and libssh

Should we mark this is as obsolete or looking for help?  Discussion follows.  Consensus: clearly mark as "looking for help, not actively maintained".  Also update OQS www accordingly.  Michael can do PRs about this.

### OQS-Demos

PR #262 ready for review.  Doesn't do tagging of Docker in CI so that will have to be manually done.

### Profiling

No updates.

### Language wrappers

**liboqs-cpp.**
No updates.

**liboqs-dotnet.** 
No updates.

**liboqs-go.** 
Vlad has a fix for issue #25.  Will release a version matching liboqs 0.9.2 later this week.  Regarding the X.509 issue #34, is this in scope of liboqs-go?  No, seems to be about higher level APIs in Go which are not part of the liboqs language wrapper.  Vlad to respond that it's out of scope then close.

**liboqs-java.**
No updates.

**liboqs-python.** 
Vlad has a fix coming for issue #57 which will install liboqs if it's not found.

**liboqs-rust.**
No updates.

### CI Containers

No updates.

### Website

Michael suggests downplaying unsupported sub-projects.  Douglas suggests highlighting OQS Provider but Michael doesn't think so.

## 2. liboqs 0.10.0 release planning

What should be included?

- ML-KEM and ML-DSA are the most important
- Falcon and stateful hash-based signatures are nice-to-have, if they are ready at that time

## 3. Linux Foundation update

OQS has completed its move into the LF.  The Post-Quantum Cryptography Alliance will launch on February 6.

What needs to be done to prepare for launch?

- Look at old issues at clean up (Spencer will start)
- An FAQ
- Checking over READMEs
- Checking over website
- Update dashboard and cleaning up failed builds
