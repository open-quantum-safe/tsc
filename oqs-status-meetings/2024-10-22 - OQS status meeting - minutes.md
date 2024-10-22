# 2024-10-22 - OQS status meeting - minutes

## Next meetings:

- Tuesday October 29, 2024 at 10:00am US Eastern / 3:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday November 5, 2024 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Alex B, Basil, Nigel (IBM)
- Alex H, Mark (Cisco)
- Christian (Microsoft)
- Douglas, Pravek, Spencer (Waterloo)
- Elizabeth (AT&T)

## Agenda

1. Status updates

## 1. Status updates

### OQS Technical Steering Committee

Douglas has sent out a poll to schedule the next TSC meeting (late October / early November).

### liboqs

External contributions to improve memory management and add fuzz testing have landed, with more work to come.

Basil has opened a PR to pq-crystals to add the internal API for NIST test vectors.
Once that lands, we can integrate the "pure" ML-DSA implementation into liboqs.

An additional API function allowing a context string to be passed to sign/verify was added to the standard.
Basil plans to add the new API function and retain the existing API for backwards compatibility.
The default version sets the context string to empty, so Basil believes we can still be standards-compliant without modifying the OQS API.

### OpenSSL 3 Provider

No updates.
 
### BoringSSL

No updates.

### OpenSSH

No updates.

### OQS Demos

Alex has added httpd to [PR #298](https://github.com/open-quantum-safe/oqs-demos/pull/298).
This means that all demos supported in CI are now in the PR.
One of Alex's coworkers at IBM has offered to start working up from the bottom of the list.

[PR #304](https://github.com/open-quantum-safe/oqs-demos/pull/304) has a new demo contribution.
Spencer asks that Alex take a look to make sure that it fits in with the ongoing work.

### Profiling

Spencer and Douglas to discuss tomorrow and follow up with ATIS.

### Language wrappers

No updates.

## Closing notes

Nigel shares that there is ongoing work in PQCP on ML-KEM implementations which can eventually be consumed by liboqs.

Keep an eye on Daylight Savings Time changes and how they affect the meeting schedule over the next couple of weeks.
