# 2024-10-15 - OQS status meeting - minutes

## Next meetings:

- Tuesday October 22, 2024 at 12:30pm US Eastern / 6:30pm Central European / 9:30am US Pacific on Zoom
- Tuesday October 29, 2024 at 10:00am US Eastern / 3:00pm Central European / 7:00am US Pacific on Zoom

## Attendees

- Alex B, Nigel (IBM)
- Christian (Microsoft)
- Hart (LF)
- JP (QRL)
- Mark, Norm (Cisco)
- Pierre-Elisée (Thales)
- Pravek, Spencer (Waterloo)
- Yarkin (NVIDIA)

## Status updates

### OQS Technical Steering Committee

Spencer requests reviews on [PR #88](https://github.com/open-quantum-safe/tsc/pull/88), which updates the liboqs CODEOWNERS team.
Later in the meeting, Christian suggests mentioning people's names in the PR as well as GitHub handles.

### liboqs

Spencer requests another review on [PR #1926](https://github.com/open-quantum-safe/liboqs/pull/1926), which introduces the use of OpenSSL memory management functions.
**Note: in the meeting, the PR number was incorrectly stated as #1923.**

Norm is working on [PR #1942](https://github.com/open-quantum-safe/liboqs/pull/1942) to fix a memory leak that arises when using OpenSSL and threads.
He plans to follow it up with a PR making an API change so that applications can properly call the thread cleanup function.

### OpenSSL 3 Provider

The release notes from last week's release had a minor issue, which has been fixed.
Pravek is looking into automating some of the release process to avoid similar errors in the future.
 
### BoringSSL

A new snapshot was released last week.
The Chromium demo has also been updated accordingly.

### OpenSSH / libssh

Christian suggests that libssh is a historical project at this point.
It may be a good idea to archive it.

### OQS Demos

Alex has updated [PR #298](https://github.com/open-quantum-safe/oqs-demos/pull/298) to include the nginx and OpenSSL demos; Basil has tested the changes to the nginx demo.
Alex is now working on the httpd demo.
Once all of the demos are updated, he plans to migrate CI from CircleCI to GitHub Actions.

No update yet on the Locust contribution (see [profiling discussion #113](https://github.com/open-quantum-safe/profiling/discussions/113)).

### Profiling

No updates.

### CI containers

No updates.

### Language wrappers

No updates.
