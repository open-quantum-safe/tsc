# 2024-02-20 - OQS status meeting - minutes

*Attendees: Basil (IBM); Brian (AWS); Christian (MSR); Douglas, Pravek, Spencer (Waterloo); Jason (SandboxAQ); Mark (Cisco); Sara (Synopsys)*

### Next meeting: Tuesday February 27, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

<!--### Next meeting: Tuesday February 20 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)-->

## Agenda

1. Status updates

## 1. Status updates

### liboqs

ML-KEM and ML-DSA: Have landed on main.

0.10.0 release: What else do we want to include a 0.10.0 release?

- Stateful hash-based signatures
- Falcon: Spencer notes that this is blocked on PQClean

Jason looking at home to remove Ninja and rely solely on CMake for builds. Douglas asks if we would lose Visual Studio project generation?  Jason to investigate and discuss with Michael. Jason asks about switching tests from Pytest to CMake tests.  Douglas suggests holding off on this for now, and focusing just on the Ninja -> CMake build switch.  Jason to add discussion to an issue on this.

Basil looking at adding the Mayo signature scheme from the on-ramp with C and AVX2 implementation.  Basil also thinks there's interest in adding SQIsign, although that is a larger code base and has some external dependencies.

### OpenSSL 3 Provider

ML-KEM and ML-DSA: Need to resolve how OIDs are going to work, then will be ready to merge.

Pravek to ping Entrust about reviving #312 once ML-KEM and ML-DSA land.

### BoringSSL

No updates.

### OpenSSH and libssh

Brian asks is there a plan to update SSH to ML-KEM. Douglas says no plan at this point.  Brian says that AWS will eventually be updating their SSH tools to support ML-KEM and would like to be able to interop with one of the OQS SSH implementations; will raise the issue again once they get to the work on their side.

### OQS-Demos

No updates.

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

