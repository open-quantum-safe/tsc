# OQS Technical Steering – 2024-04-10 – minutes

## Attendees

TSC members

- [X] [Norman Ashley (Cisco)](https://github.com/ashman-p)
- [X] [Michael Baentsch (independent contributor)](https://github.com/baentsch)
- [X] [Thomas Bailleux (SandboxAQ)](https://github.com/)
- [X] [Basil Hess (IBM Research)](https://github.com/bhess)
- [X] [Brian Jarvis (AWS)](https://github.com/brian-jarvis-aws)
- [X] [Christian Paquin (Microsoft Research)](https://github.com/christianpaquin)
- [X] [Douglas Stebila (University of Waterloo)](https://github.com/dstebila)

Other attendees

 - [x] [Nigel Jones (IBM)](https://github.com/planetf1)
 - [x] [Alex Bozarth (IBM)](https://github.com/ajbozarth)
 - [x] [Michael (Max)imilien, IBM](https://github.com/maximilien)
 - [x] [Ry Jones (Linux Foundation)](https://github.com/ryjones)
 - [x] [Hart Montgomery, Linux Foundation](https://github.com/hartm)


## 1. Chair's introduction
 - The chair thanks members for being patient as we get up and running
 - TSC aims to be consensus driven & friendly
 - TSC will discuss & make strategic decisions on technical matters. Developer call handlers regular operational matters

## 2. Approve agenda

 - Agreed

## 3. Appoint minute-taker

 - Nigel will take this week's notes. Agreed that we would ask at the beginning of each meeting & do in rotation.

## 4. Approval of minutes of last meeting

- Last meeting's notes are open as [PR #14](https://github.com/open-quantum-safe/tsc/pull/14). Comments/reviewers invited. TSC members asked to approve. 
- will use direct links to recordings in future minutes - portal not available to all (has been requested)

## 5. Voting procedure

- [Issue #12](https://github.com/open-quantum-safe/tsc/issues/12) open for discussion
- online/async voting to allow broadest engagement
- open votes for technical matters
- differing opinions on whether personal matters (including voting such as ranking) should be public or secret, or referred up to the board.
- noted that most decisions consensus driven in any case
- mechanism - git (simple), [gitvote](https://github.com/cncf/gitvote), [Helios](https://vote.heliosvoting.org/) are possible options
- discussion to continue in [issue 12](https://github.com/open-quantum-safe/tsc/issues/12)


## 6. Addition of Vlad Gheorghiu to TSC

- Vlad is maintainer of language wrappers 
- Intent had been he was in the TSC from launch
- Christan proposed, Basil seconded motion to add Vlad. Agreed by verbal vote of TSC members with no objections

## 7. Meeting cadence

- Monthly still seems appropriate - lots of topics
- Two suggestions:
  - in PQCA TAC timeslot (alt. weeks) in off-week
  - offline poll to accommodate most TSC members, and consider time rotation to handle differing timezones. This may require a higher frequency than monthly
- Agreed poll will be conducted

## 8. Report from TAC representative (Thomas)

- Project Lifecycle. 
  - [Early draft](https://docs.google.com/document/d/1NV-0vNgXWdc81oqT0jv0C-9Funb8dySS06u90ghF-X4/edit)
  - PQCA TAC suggests oqs tsc review and develop as most active project.
  - objective is clarity for consumers as to what state the code is in - production, experimental, how good is security, maintenance - don't want to set wrong expectations. 
  - Also covers adoption of new projects. Similar to apache incubation approach
  - may apply at sub-project or component level
  - should map existing oqs subprojects/components to proposal for validation
  - clear separation may require feature flags, restructuring of liboqs, additional projects etc
  - should delegate to OQS dev meeting to decide/discuss in github issues
  - Issue will be opened for followup
- Security
  - PQCA [setting up security workgroup](https://github.com/PQCA/TAC/issues/2)
  - Hoping to arrange presentation from [OSSF](https://openssf.org/) around [scorecard](https://securityscorecards.dev/) & other best practices. TSC members will be invited
  - Also Use of sigstore, CBOMs, SBOMs, vulnerability reporting process

## 9. Does OQS-BoringSSL repository require a license exemption?

- [Issue #13](https://github.com/open-quantum-safe/tsc/issues/13) has background
- Current project charter requires contributions under MIT license
- Discussed allowing Apache 2.0 as an exception for this work, or changing charter to allow generally
- [Issue #17](https://github.com/open-quantum-safe/tsc/pull/17) for TSC members to vote on exception

## 10. Sub-project lifecycle

No discussion beyond 8. above - timeout

## 11.  Discussing plan for level of code support and the production vs. research tracks

No discussion beyond 8. above - timeout

## 12. Other business

None

## Meeting Recording

A [transcript and recording of this meeting](https://zoom.us/rec/play/SSS-KDTuL7-MfCQaBoOH6NsJ2qRjPuc46X1hzaRizeJBeFsgRlTapONnlosGDbBGjAJI8dksmehEiF0I.s2Hw9yHdlBvJ0s-A?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2FoQXCKON8wrHgBsjAWgWQYZxOBfKB9eeiyw38CgqMbhVB9LqHnE0cPMhwdW3zZDYp.ID4HoVpw_jj0841b) is available
