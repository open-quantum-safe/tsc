# Voting procedure

## Voting requirements from OQS Technical Charter

Section 3 of the [Technical Charter for the Open Quantum Safe project](https://github.com/open-quantum-safe/tsc/blob/main/charter/charter-2024-01-03.pdf) lays out requirements for votes of the OQS Technical Steering Committee.

> TSC Voting
> 
> a) While the Project aims to operate as a consensus-based community, if any TSC decision requires a vote to move the Project forward, the voting members of the TSC will vote on a one vote per voting member basis.
> 
> b. Quorum for TSC meetings requires at least fifty percent of all voting members of the TSC to be present. The TSC may continue to meet if quorum is not met but will be prevented from making any decisions at the meeting. Any TSC member that misses three (3) consecutive meetings shall be automatically suspended from eligibility to vote and shall not constitute a voting representative for purposes of determining quorum until having attended two meetings consecutively. For avoidance of doubt, the suspended TSC member shall be eligible to vote in the second consecutive meeting.
> 
> c. Except as provided in Section 7.c. and 8.a, decisions by vote at a meeting require a majority vote of those in attendance, provided quorum is met. Decisions made by electronic vote without a meeting require a majority vote of all voting members of the TSC.
> 
> d. No organization or company or group of related companies will be allowed more than 20% of eligible votes, or 2 votes, whichever is higher. If more than that number of eligible votes are affiliated with an organization or company, they must decide who will cast votes. Affiliations must be publicly stated or acknowledged when a person is associated with or employed by an organization or company.
> 
> e. In the event a vote cannot be resolved by the TSC, any voting member of the TSC may refer the matter to the Series Manager for assistance in reaching a resolution.

## Implementation

1. Votes of the OQS TSC will be public ballots.
2. Motions can be discussed in TSC meetings, but additional discussion and voting will take place asynchronously via Github.
3. Motions will be submitted as a pull request on the OQS TSC Github repository, with `[vote]` in the PR title.
  - The outcome of the vote should have some effect on the contents of the TSC repository, such as editing an existing file or adding a new file to record or implement the policy decision being made.
4. Motions may be submitted as a draft PR to solicit discussion or feedback or changes, and then converted into a full PR once the motion is ready for a vote.
5. When the motion is ready for a vote, the TSC chair will request PR reviews from all voting TSC members. Members can vote in favour by approving the pull request or leaving a comment indicating their approval; members can vote opposed or explicitly abstain by leaving a comment to that effect.
6. The motion will be considered passed once either of the following occurs:
  1. a majority of TSC members have voted in favour; or
  2. the motion has been open for votes for at least 3 weeks, and a majority of TSC members who cast a vote have voted in favour.
7. The chair is allowed to vote.
8.  Once the motion is passed, the TSC chair will merge the pull request.
