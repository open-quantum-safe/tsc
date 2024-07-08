# 2024-07-02 - OQS status meeting - minutes

### Next meeting: Tuesday July 9, 2024 at 10:00am US Eastern time / 4:00pm Central European / 7:00am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09)

<!-- ### Next meeting: Tuesday July 2, 2024 at 12:30pm US Eastern time / 6:30pm Central European / 9:30am US Pacific time on Zoom (https://uwaterloo.zoom.us/j/98064335970?pwd=U0tTZk84blBZTnptTXh0YmlZd1dOQT09) -->

## Attendees

- Alex B, Max, Nigel (IBM)
<!-- - Mark, Norm (Cisco) -->
<!-- - Christian (MSR) -->
- Douglas, Pravek (Waterloo)
- Gerardo (AWS)
<!-- - Jason (SandboxAQ) -->
<!-- - Ry (Linux Foundation) -->
- JP (Quantum Resistant Ledger)
<!-- - Michael (independent) -->
<!-- - Sara (Synopsys) -->
<!-- - Vlad (softwareQ) -->
- Yarkin (NVIDIA)

## Agenda

1. Status updates

## 1. Status updates

### OQS TSC

The OQS TSC meeting was held on June 27, 2024.  A draft of the meeting minutes are available at https://github.com/open-quantum-safe/tsc/pull/46

### liboqs

**Scorecard**: Main scorecard PR has been merged. Nigel will create follow-on issues to update the scorecard to new version of the spec and to publish it properly on the OpenSSF dashboard, then add a badge to our README.

**CBOM**: Issue #1831 proposes to update CBOM to the new format. To be discussed with Basil on his return.  Max notes that there will be a presentation on CBOM at tomorrow's TAC meeting.

### OpenSSL 3 Provider

No updates.

### BoringSSL

No updates.

### OpenSSH and libssh

Gerardo looking for review on PR #159. Recommend reviewing the process described.  Gerardo encountered some challenges with git history (due to the use of squash commits previously) but has made some changes that should make it easier going forward.

### OQS-Demos

Alex created issue #286 which tracks notes from last week's meeting about updating Demos.  Alex will prepare a plan of attack and a project board for working going forward. 

### Profiling

No updates.

### CI containers

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


---

## AI-generated meeting summary from Zoom

### Quick recap

The team discussed their weekends, the upcoming holiday, and a hockey game before moving on to business matters. Nigel presented on the scorecard and issues with CBOM, while Gerardo presented a massive pull request aimed at updating the codebase. The team also discussed the complexities of merging different repositories of content and the development of a plan of attack for the Demos project.
Next steps

Nigel to update the CBOM for liboqs to version 1.6 and discuss with Basil when he returns from holiday.

Douglas to review Gerardo's large PR for updating SSH with upstream OpenSSH changes.

Alex to create and share a plan of attack for the OQS Demos project in the next 1-2 weeks.

### Summary

#### Casual Conversation and Holiday Plans

The team engaged in a casual conversation about their recent weekends and the upcoming holiday. max shared that he had a busy weekend and would be taking a short break starting from Thursday. There was also a brief discussion about a hockey game, with max mentioning that Florida won, and Alex and Nigel sharing their experiences and opinions about hockey.

#### Scorecard, CBOM

Douglas started with status updates and asked the team if there were any other topics to discuss. Nigel then presented on the scorecard, highlighting that it had been merged and needed to be published properly. He also mentioned issues with CBOM and suggested updating it to the current version. max announced a presentation on CBOM at the upcoming TAC meeting. There were no updates on Kyber and libjade, with Pravek waiting to hear back on an issue.

#### SSH Update

Gerardo presented a massive pull request (PR) aimed at updating the codebase with upstream OpenSSH and resolving merge conflicts. He was working on resolving a refactor upstream on the SSH piece. Douglas agreed to review the PR, and Gerardo advised him to focus on the process and how he handled merge conflicts. Nigel asked about the differences between the base SSH and the custom build supporting OQS, to which Gerardo explained that the main changes were the addition of new algorithms and the implementation of a templating system for security parameters. Gerardo also clarified that most of the PR was straightforward, with the refactor upstream on the SSH key being the most significant change.

Nigel, Gerardo, and Douglas discussed the complexities and potential solutions for merging different repositories of content. Nigel suggested creating a new repository with a clean history to avoid past mistakes. Gerardo agreed, stating that this new branch could make future work easier. The team also discussed the challenges of merging the latest open source with their existing content, with Gerardo noting that the evolving machinery under the hood made it not straightforward. They acknowledged that their previous use of squash merges had caused issues, and agreed to move forward with a new approach. Douglas thanked Gerardo for his work and encouraged others to review it to move forward with the next phase. 

#### Demos Project Plan and Sub-Project Updates

Alex then shared his plan to develop a plan of attack for the Demos project, aiming to have it ready by the next week's meeting. Douglas also briefly reviewed the status of other sub-projects and invited additional comments. The conversation ended with the announcement of the next week's meeting time and a holiday greeting.
