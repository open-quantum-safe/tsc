# 2024-03-12 - OQS status meeting - minutes

<!--### Next meeting: Tuesday March 12, 2024 at 12:30pm US Eastern time / <span style="color: red;">5:30pm Central European (note change to Daylight Saving Time in North America)</span> / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)
-->
<!--### Next meeting: Tuesday February 27, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday March 19 at 10:00am US Eastern time / <span style="color: red;">3:00pm Central European (note change to Daylight Saving Time in North America)</span> / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Attendees

- Alex B (IBM)
- Alex H, Norm (Cisco)
- Christian (MSR)
- Douglas, Pravek (Waterloo)
- Jason (SandboxAQ)

## Agenda

1. Status updates
1. Feedback on liboqs 0.10.0-rc1
2. Other business

## 1. Status updates

### OQS TSC

Douglas gave a recap of the OQS Technical Steering Committee meeting from Monday March 11.  

### liboqs

PR #1723: This can be merged and then Douglas will make a new 0.10.0 release candidates.

PR #1700: Jason will resume work on this soon, for inclusion in the next release after 0.10.0.

PR #1729: Pravek has created a draft PR for the libjade-based implementation of Kyber.

### OpenSSL 3 Provider

No updates.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

Will need to be updated with ML-KEM and ML-DSA.  Volunteers welcome.

### Profiling

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

## 2. Feedback on liboqs 0.10.0-rc1

No additional feedback received.  Douglas will tag -rc2 after #1723 lands.

## 3. Other business

Douglas will not be at the next two weekly meetings; Basil will chair them.

Douglas mentions that in April Nicola Tuveri, a PhD student from Finland who wants to do research on PQ implementations and who is also a member of the OpenSSL technical committee, will be visiting Waterloo for a few weeks.  Hope to have some discussions about how OQS and OpenSSL might be able to work together, and can meet with others who are interested.  Norm would like to be involved.

Alex B asks if the OQS status call will move over to the Linux Foundation Zoom platform.  On the one hand, there are some nice benefits, like it showing up in your meeting dashboard and recordings and transcripts being stored automatically.  On the other hand, it does require people to be signed into a Zoom account, a feature LF has turned on to help manage abuse across calls on LF projects.  What would people prefer?
