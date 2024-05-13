# 2024-04-09 - OQS status meeting - minutes

### Next meeting: Tuesday April 16, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

<!--### Next meeting: Tuesday April 16, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

## Attendees

- Alex, Max (IBM)
- Douglas, Pravek, Spencer (Waterloo)
- Jason, Thomas (SandboxAQ)
- Mark, Norm (Cisco)
- Michael (independent)
- Sara (Synopsys)
- Vlad (softwareQ)

## Agenda

1. Status updates

## 1. Status updates

### OQS TSC

Next OQS TSC meeting is tomorrow, April 10.

### liboqs

libjade integration: Pravek not sure what information to enter for the libjade implementation of Kyber in the CBOM. Pravek can ask Basil.

Stateful hash-based signatures: Spencer has a call with Norm, Mark, Duc to finalize things before merge.  OpenSSL had a discussion about adding SHBS and we should talk to Nicola about this.

What could be included in the next release?

- stateful hash-based signatures
- libjade implementation of Kyber
- HQC AVX2 implementation update
- Mayo

Douglas to create milestone for 0.11.0.

Eddy working on deterministic MLKEM key generation.

### OpenSSL 3 Provider

Michael has prepared a release candidate for oqs-provider 0.6.0.  Please take a look and provide feedback before a release at the end of the week.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

Spencer mentions that a student from Singapore expressed interest in nginx.

Max asks about the status of various demos.  Douglas notes that we are overstretched on demos and many don't have someone interested in updating them.

### Profiling

Discussion about revamping profiling platform. It is shutdown at the moment.  Spencer prefers to do a major update to profiling rather than restart with a small bump to enable 0.10.0.  Michael highlights the need to identify goals of profiling.  Spencer to create some issues to discuss.  If it remains off, will need to disable it on www.

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
Vlad to respond to issues.

**liboqs-rust.**
No updates.

### CI Containers

No updates.

### Website

No updates.

## 2. Other business

Next week there will be presentations on OQS & PQCA at the Linux Foundation Open Source Summit in Seattle: Douglas, Max & Hart, and Alex & Max.
