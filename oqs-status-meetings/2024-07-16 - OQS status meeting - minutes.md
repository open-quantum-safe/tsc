# 2024-07-16 - OQS status meeting - minutes

### Next meeting: Tuesday July 23, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

<!-- ### Next meeting: Tuesday July 16, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09) -->

## Attendees

- Alex B, Max, Nigel (IBM)
- Alex H, Mark (Cisco)
- Andrés Vega
- Douglas, Pravek, Spencer (Waterloo)
- Gerardo (AWS)
- Hart (Linux Foundation)
- Jason (SandboxAQ)
- JP (Quantum Resistant Ledger)
- Michael (independent)
<!-- - Christian (MSR) -->
<!-- - Gerardo (AWS) -->
<!-- - Jason (SandboxAQ) -->
<!-- - Prem (AMD) -->
<!-- - Ry (Linux Foundation) -->
<!-- - Sara (Synopsys) -->
<!-- - Vlad (softwareQ) -->
<!-- - Yarkin (NVIDIA) -->

## Agenda

1. Status updates
2. Trail of Bits code review
3. liboqs 0.11.0 release planning

## 1. Status updates

### OQS TSC

No updates.

### liboqs

**libjade**: There's been a release upstream from Formosa that includes the license changes we need.  Pravek has pushed an update. Ran into some problems with gcc 13 on Mac; Nigel ran into the same problems a few weeks ago and made some changes; Spencer suggests it could be fixed by a rebase.

**Threat modelling**: Spencer and Pravek had a discussion with Nicola from OpenSSL; notes have been posted to issue #1840. Douglas to ping Yarkin to also post notes on #1840.  Feedback from others is welcome.

Jason reports that he did a project using the stateful hash-based signatures code in DNSSEC which he'll be presenting this week at IETF 120 in Vancouver.  See also the following blog posts:
- https://www.isc.org/blogs/2024-pqc-study/
- https://blog.powerdns.com/2024/07/15/more-pqc-in-powerdns-a-dnssec-field-study

**CBOM**: Max says that there may be a PR coming to generate our CBOM file using tooling.

**SPHINCS+**: Any feedback on the necessity of keeping both the Round 3 version and the updated NIST version (once it appears)?  Spencer adds that if we do not keep both versions, then we'll have to also decide when is the right time to rename the algorithm in liboqs to the NIST name.

### OpenSSL 3 Provider

Michael notes that Basil has a PR adding MAYO5, which brings us to 58 signature algorithms, close to the 64 that would start to cause problems in some TLS servers (due to server implementation bugs); see issue #399.  We're okay when MAYO lands, but any others added after that may require some consideration of defaults.

### BoringSSL

No updates.

### OpenSSH and libssh

Gerardo reports that the initial PR updating upstream to OpenSSH 9.7 has landed. A new PR #160 is up which does a refactor of sshkeys.c to reduce conflicts.  No hybrids yet; also fixes some CI issues.  #160 is ready for review.

Michael suggests interop testing with the v8 branch.

### OQS-Demos

Alex has proposal for OQS Demos revitalization in issue #288.  For each demo, there would be 3 phases:

1. Create project board
2. Execute project board
3. The future

Feedback on these is welcome on issue #288 as well as in meetings.  We'll have a discussion about demos at the next 2 status meetings to collect feedback.

Michael suggests adding some prioritization.  Max suggests voting to help identify priorities. Alex to create a comment for each demo and ask people to vote on which ones they think are important.

Andrés asks which are most compelling and most mature? He is willing to help on project management.

Alex notes that he doesn't have triage rights on OQS Demos; he'll make a PR on open-quantum-safe/tsc to get the appropriate rights.

Gerardo asks about PQ work on Strongswan.  Douglas has received some emails in the apst about Strongswan and will forward to Gerardo.

### Profiling

No updates.

### CI containers

Spencer notes that our Ubuntu Bionic i386 image worked on CircleCI but doesn't work on Github CI and would like help figure this out.  Michael notes that x86 Linux is not listed as supported at any tier in our liboqs PLATFORMS.md file, so perhaps this work is unnecessary.

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

### Website

Jason reminds that the [list of algorithms on the website](https://openquantumsafe.org/liboqs/algorithms/) needs to be updated now that MAYO has landed.

## 2. Trail of Bits code review

Douglas reports that the Trail of Bits code review is underway. They had some initial questions about whether we were using self-hosted runners, which Spencer has responded to.

Douglas mentions that anyone interested in participating in the Slack with Trail of Bits is welcome to do so; he will forward requests to be added.

## 3. liboqs 0.11.0 release planning

Not discussed to due time constraints.
