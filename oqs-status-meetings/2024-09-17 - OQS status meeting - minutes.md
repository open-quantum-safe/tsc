# 2024-09-17 - OQS status meeting - minutes

## Next meetings:

- Tuesday September 24, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom
- Tuesday October 1, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom

## Attendees

- Alex (IBM)
- Christian (Microsoft)
- Douglas, Spencer (Waterloo)
- Jolene, Mingtao, Rafael (Meta)
- JP (QRL)
- Mark (Cisco)
- Michael, Thomas (independent)
- Prem (AMD)

## Agenda

1. Welcome
2. liboqs 0.11.0 release
3. Meta bug discussion
4. News from Michael
5. Status updates

## 1. Welcome

Jolene, Mingtao, and Rafael are joining for the first time.

## 2. liboqs 0.11.0 release

[A release candidate](https://github.com/open-quantum-safe/liboqs/pull/1925) has been posted.
Feedback and testing are solicited.
If there are no concerns, we will aim to cut a release for end of this week or early next week.

## 3. Meta bug discussion

Meta uses liboqs quite a bit for internal traffic.
They discovered a bug in Kyber on Arm and filed a fix (https://github.com/open-quantum-safe/liboqs/pull/1914).
Pravek adapted the fix to work with copy_from_upstream and merged (https://github.com/open-quantum-safe/liboqs/pull/1922).
The fix is in the 0.11.0 release.

Jolene asks about how upstreams are monitored for maintenance.
Douglas says that we historically pulled implementations from wherever we could find them.
The PQ Code Package will hopefully help with this in the future by providing a single source for ML-KEM and other standards-track algorithms.

Michael suggests having clear documentation regarding upstreams, their maintenance statuses, and where bug reports should be filed.
This would also aid in deciding when to stop supporting an algorithm (for example, Kyber).
We currently track upstream sources in yaml files, but this is not straightforward to find and does not include information about maintenance.
Douglas suggests to audit the status of our upstreams to record this information and then find a better way to surface it.

Meta plans to switch from Kyber Round 3 to ML-KEM after the 0.11.0 release is available.
More discussion is needed about when to deprecate Kyber (possibly in the 0.12.0 release).

JP suggests using GitHub Actions to monitor upstream dependencies for potentially impactful issues and will take a look at what can be done in this regard.

Spencer asks if Meta can contribute the test setup that detected the Kyber Arm bug.
Mingtao says that the bug was a one-off finding and they don't have any external tests for OQS.

## 4. News from Michael

[Michael is now a member of the OpenSSL team!](https://openssl-library.org/post/2024-09-17-post-quantum/)
He will be working on bringing post-quantum crypto into OpenSSL.
Michael doesn't expect this to impact his involvement with OQS, although he will have to maintain a "split personality" between the two projects.

## 5. Status updates

### OQS TSC

Michael has [created a PR](https://github.com/open-quantum-safe/tsc/pull/77) to help with permissions management issues.
The config.yml file still needs to be updated; Michael solicits help with this and Spencer and Alex volunteer.

### liboqs

[PRs 1905](https://github.com/open-quantum-safe/liboqs/pull/1905) and [1890](https://github.com/open-quantum-safe/liboqs/pull/1890), for fuzzing and scorecard updates are in need of review.

### OpenSSL 3 Provider

Michael has an open [PR to address logic issues around OIDs](https://github.com/open-quantum-safe/oqs-provider/pull/522).
The fix is to set unassigned OIDs to null.
This will result in OpenSSL errors when KEMs without assigned OIDs are used and KEM encoding is activated (which is not a default setting).

A [PR from Norm](https://github.com/open-quantum-safe/oqs-provider/pull/521) is ready to merge, but he is away this week.

### BoringSSL

The latest BoringSSL update includes Google's implementation of ML-KEM.
This raises the question of which implementation should take precedence in our fork: OQS or Google?
Both approaches could have their own merits.

### OpenSSH

No updates.

### OQS-Demos

A PR from Alex is coming soon.

### Profiling

No updates.

### CI Containers

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

### Website

No updates.

## Closing questions

Mingtao asks if liboqs would be receptive to a PR to reduce code duplication.
This would help to reduce the size of the library.
Consensus is that such a PR would be very welcome.

Jolene asks if 0.11.0 will include an Arm implementation of ML-KEM.
Douglas says that there will be a generic C implementation, but the only optimized version will be AVX2.
