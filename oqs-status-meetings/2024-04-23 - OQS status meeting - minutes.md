# 2024-04-23 - OQS status meeting - minutes

### Next meeting: Tuesday April 30, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

<!--### Next meeting: Tuesday April 23, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

## Attendees

- Alex, Nigel (IBM)
- Christian (MSR)
- Douglas, Pravek, Spencer (Waterloo)
- Jason (SandboxAQ)
- Mark, Norm (Cisco)
- Michael (independent)
- Sara (Synopsys)
- Vlad (softwareQ)

## Agenda

1. Report from Open Source Summit
1. Status updates

## 1. Report from Open Source Summit

Last week there were 3 presentations on PQCA and OQS at the Linux Foundation's Open Source Summit in Seattle. Douglas introduced the PQCA and OQS in the main conference keynote. Hart and Max gave an overview of the PQCA, and Alex presented a demo of using OQS provider in HAProxy and curl.

## 2. Status updates

### OQS TSC

Minutes available from the TSC.

### liboqs

Stateful hash-based signatures: Spencer is resolving some comments from Jason. Any other feedback welcome.

Scorecard: Nigel has a PR with most of the scorecard functionality enabled; additional feedback welcome on [#1708](https://github.com/open-quantum-safe/liboqs/pull/1708).

libjade: Pravek is fixing up some clang issues. Pravek points out that the code coming from libjade is CC0.  Douglas to email the Formosa project to ask about the status of their relicensing of libjade to Apache 2.  

0.11.0: Michael asks about plans for 0.11.0. Douglas points to the [0.11.0 milestone](https://github.com/open-quantum-safe/liboqs/milestone/25).

### OpenSSL 3 Provider

Norm asks about the path for getting PQ code in OpenSSL.  Douglas explains that we have had some interactions with OpenSSL, but are blocked at the moment due to contributor license agreement complications.  Douglas has asked the LF lawyers if they can help with this, and will follow up again to try to get a reply.

### BoringSSL

No updates.

### OpenSSH and libssh

Christian notes that the NCCoE project is planning to do some SSH testing; Panos is taking the lead on this. What's the status of our SSH implementations?  Currently inactive; most recent comment was from Brian Jarvis saying he would see whether AWS can provide assistance in updating/maintaining these.

### OQS-Demos

Alex reports that he and Mariam plan to submit their [tutorials for HAProxy](https://developer.ibm.com/tutorials/awb-building-quantum-safe-web-applications/) to our demos repository eventually. Michael asks why not just make a Docker image? Alex says that the tutorial started out from an internal Docker image. Nigel notes that there can be value to readers from stepping through these things manually; so ultimate both a tutorial and a Docker image can be useful to different audiences.

### Profiling

Spencer looking for feedback on [discussion on what are we looking for in a benchmarking tool](https://github.com/open-quantum-safe/profiling/discussions/112).

Michael asks if we want to remove old data? Spencer says that the old data does include a version number, so it is not false, though it is not up to date. Michael says we could add a disclaimer to the website for the old data. Douglas to create an issue to track this.

### CI containers

Nigel looking at updating images.

Spencer notes that PQCA now has Github Enterprise status which should give us access to ARM runners; he will follow up on this.

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
Vlad monitoring some issues.

### CI Containers

No updates.

### Website

No updates.
