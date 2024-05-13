# 2024-01-30 - OQS status meeting - minutes

*Attendees: Alex, Mark, Norm (Cisco); Douglas, Pravek, Spencer (Waterloo); Eric (AWS); Jason (SandboxAQ); Michael*

<!--### Next meeting: Tuesday January 30, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

### Next meeting: Tuesday February 6 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

## Agenda

1. Status updates
2. Preparing for LF launch
3. FIPS certification and talking to OpenSSL

## 1. Status updates

### liboqs

Stateful hash-based signatures: Norm working through how to handle function pointers in `OQS_SIG` data structure when keygen and sign are not enabled.  Then will replace some code with macro-based generation for consistency/easy of updates.

Spencer has been doing some clean up of old issues and PRs.

PRs ready for review: #1680, #1679, #1677, #1653, #1560.

### OpenSSL 3 Provider

No updates.

### BoringSSL

Following discussion last week about whether to declare this project inactive, received a reply from @pi-314159 that they are willing to update boringssl every 2-3 months.


### OpenSSH and libssh

Michael marked these two projects as presently inactive.

### OQS-Demos

Michael deployed the 0.9.2 release demos to Docker Hub.

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
Douglas received an expression of interest from Premachandra Mallappa at AMD about getting involved in Rust programming in OQS.  Douglas to  introduce Prem, Jason, Vlad in a group email, who have all expressed interesting in taking over support of liboqs-rust.

### CI Containers

No updates.

### Website

Michael suggests downplaying unsupported sub-projects.  Douglas suggests highlighting OQS Provider but Michael doesn't think so.

## 2. Preparing for LF Launch

The Post-Quantum Cryptography Alliance will launch on February 6.

What needs to be done to prepare for launch?

- Checking over READMEs
- Creating an FAQ?
	- Michael create a USAGE.md file oqs-provider, might be useful in liboqs
	- Douglas to start an FAQ for the website:
		- What is PQ?
		- What is the status of PQ standardization?
		- What is OQS?
		- What does quantum-safe mean?
		- Do I need a quantum computer?
		- Is OQS safe to use?
		- How to get involved?
		- How to use PQ with OpenSSL?
		- How to use PQ in (my favourite programming language)?

## 3. Discussions with outside groups: FIPS certification, OpenSSL

### FIPS certification

Douglas received an email from a FIPS certification lab, KeyPair.us, inquiring about our interest in seeking FIPS certification for OQS eventually.  Douglas thought it might be interesting to get them to tell us more about the process in general.

Eric has observed that FIPS certification is on-going and time-consuming. It does open doors to new customers. PQ algorithms can't be certified yet since there are no final FIPS standards and no testing standards.

Michael notes that it's very early -- too early to start any of this.  Michael notes that OpenSSL FIPS certification was done at no cost.  A discussion with a lab could involve asking them what's feasible for a project like ours.

There is the suggestion that it would be better to hold off on this for a few months until things are clearer with NIST, as well as when the Kyber Code Package effort has developed more, since that group will also likely be interested.

### OpenSSL

Douglas notes that Nicola Tuveri will be visiting Waterloo in April to spend some time collaborating on research. He is also a member of the OpenSSL technical committee so this also seemed like a good opportunity to start discussing what interactions with OpenSSL may be possible. 

Added after the call: start of a discussion with OpenSSL on GitHub: https://github.com/openssl/project/issues/431

