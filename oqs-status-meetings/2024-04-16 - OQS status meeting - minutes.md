# 2024-04-16 - OQS status meeting - minutes

<!--### Next meeting: Tuesday April 16, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday April 23, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Attendees

- Basil (IBM)
- Douglas, Pravek, Spencer (Waterloo)
- Hart (Linux Foundation)
- Jason, Thomas (SandboxAQ)
- Mark, Norm (Cisco)
- Prem (AMD)
- Sara (Synopsys)
- Shubham Tatvamasi

## Agenda

1. Status updates

## 1. Status updates

### OQS TSC

Minutes available from the TSC.

### liboqs

Stateful hash-based signatures: 

- Jason would like to have an API to identify the algorithm from the public key. Norm notes that there are many variants of XMSS & LMS compared to other algorithms. Jason to introduce an issue to discuss.
- Norm/Spencer/Duc/Mark met last Friday to discuss. Getting very close. Spencer making some changes to CMake flag for enabling signatures. Spencer doing some cleanup on CI failures.  Concerned about CI time.  Hart mentions that Ry can help us think about our CI usage.
- Jason has a comment about SIG_free not releasing the right thing.

### OpenSSL 3 Provider

0.6.0 was released.

Thomas: There might be an issue with output artifacts -- the .so / .a files on Intel contain nothing.  See issue #395. Basil was able to reproduce and has a potential fix.

### BoringSSL

No updates.

### OpenSSH and libssh

No updates.

### OQS-Demos

The test server was updated to 0.10.0.  Note that some ports have changed, which are documented in the JSON file.

### Profiling

Spencer stated discussion #112 about the direction of profiling; please contribute.

### Language wrappers

**liboqs-cpp.**
No updates.

**liboqs-dotnet.** 
No updates.

**liboqs-go.** 
No updates.

**liboqs-java.**
Spencer asks if this is maintained. Douglas says that we don't have an active maintainer.

**liboqs-python.** 
No updates.

**liboqs-rust.**
No updates.

### CI Containers

No updates.

### Website

No updates.

## 2. Other business

Shubham is working on integrating a QRNG into one of the liboqs language wrappers and may be able to contribute it.

Norm asks if anyone is familiar with the [ATIS testing framework](https://www.atis.org/initiatives/quantum/qscii-open-source-pqc-test-framework/) and [Qujata](https://github.com/att/qujata/tree/main).  Hart had a discussion with them a few weeks ago to learn more about what they're doing and see if they are willing to contribute.
