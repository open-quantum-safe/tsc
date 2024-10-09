# 2024-10-08 - OQS status meeting - minutes

## Next meetings:

- Tuesday October 15, 2024 at 10:00am US Eastern / 4:00pm Central European / 7:00am US Pacific on Zoom
- Tuesday October 22, 2024 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom

## Attendees

- Alex H, Mark (Cisco)
- Bill Trost, Elizabeth Wood (AT&T)
- Gerardo (AWS)
- Ian Deakin (ATIS)
- Max (IBM)
- Pravek, Spencer (Waterloo)
- Yarkin (NVIDIA)

## 1. liboqs 0.11.0 release cycle - Provider, demos, ...

oqs-provider 0.7.0 has been released; the demos still need to be tagged.

## 2. Status updates

### liboqs

Norm observed a memory leak related to OpenSSL and threading usage (see [issue #1941](https://github.com/open-quantum-safe/liboqs/issues/1941)).
The leak only manifests in our test programs.
Norm is working on a fix (see [PR #1942](https://github.com/open-quantum-safe/liboqs/pull/1942)).

### OpenSSL 3 Provider

No further updates.
 
### BoringSSL

No further updates.

### OpenSSH

No updates.

### OQS-Demos / Profiling

Spencer has suggested that the Locust integration be contributed as a new demo (see [discussion #113](https://github.com/open-quantum-safe/profiling/discussions/113)).

Pravek to tag Docker images for the new releases today or tomorrow.

### CI containers

No updates.

### Language wrappers

No updates.

## 3. OQS representative to the TAC

As part of the TAC calls, a representative from OQS gives a project update and carries updates from the TAC to OQS.
The current representative to the TAC (Thomas Bailleux) may not be able to continue in this role.
Pravek volunteers to cover the TAC meeting tomorrow (October 9), with the TAC representative to be chosen more formally in a future process.
Max suggests Yarkin as Yarkin typically attends both TAC and OQS meetings.

## 4. ATIS / AT&T introductions

Ian Deakin from ATIS and Bill Trost and Elizabeth Wood from AT&T are attending the status meeting for the first time.
They are working on a test/performance framework using OQS and hope to contribute to the community.
They plan on continuing to attend status calls.

Spencer to set up a separate call to discuss collaboration on profiling/benchmarking.
