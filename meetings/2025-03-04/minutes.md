# OQS Technical Steering – 2025-03-04 – Minutes


## Attendees
* Douglas Stebila (University of Waterloo)
* Michael Baentsch
* Akira Nagai (NTT)
* Spencer Wilson
* Pravek Sharma
* Basil Hess
* Christian Paquin (Microsoft Corporation)
* Brian Jarvis (Amazon Web Services, Inc.)
* Balaji Ethirajulu (The Linux Foundation)
* Hart Montgomery
* Kan Yasuda (NTT)
* Norman Ashley 

## Meeting Recording

- [Recording](https://zoom.us/rec/share/gADvQF0yH7_sNeSRE8IW_WbB7ZTjQEBTb2fIKA1-3zNvV6o_wDGJbRzkIXMgLMG_.q65ytllLWYsKpGGu)

## Agenda
(see [agenda](./agenda.md))

### 1. Chair's introduction

- Douglas opened the meeting, welcome

### 2. Approve agenda

- Reordered to accomodate Akira Nagai's time zone.

### 3. Appoint minute-taker

- Norman Ashley 

### 8. NTRU (Akira Nagai and Kan Yasuda, NTT Social Informatics Laboratories)

* Akira Nagai and Kan Yasuda, NTT proposed and gave rational for re-adding NTRU to libOQS
    * NTRU is used by NTT
    * Submitting to IETF standardization process
    * Industry adoption
    * Used for testing 
    * Alternative to ML-KEM
    * They are willing to contribute and maintain

- Questions raised 
    - How will liboqs be used? Direct via OQS API
    - Will OQSProvider be needed? No, not initially

* Resulting Action Item:

     - Douglas to create an issue to further discussions on the topic. 
     - Follow up with Akira and Kan.

### 4. Review action items from previous meeting

- [Security response team](https://github.com/open-quantum-safe/tsc/issues/60)
    * Spencer gave update on the security response doc. It has been approved by some but needs more reviewers especially those on the response teams. Douglas to tag TSC members / VMT members who haven't provided feedback, then merge.

- [OQS security response process](https://github.com/open-quantum-safe/tsc/pull/124): Once merged, a trial run will be done on a low-level issue or as simulated issue.

- [Binary distributions](https://github.com/orgs/open-quantum-safe/discussions/1625#discussioncomment-11751301): Would still be nice to have this. Douglas to ping Nigel.

- [Algorithm support levels](https://github.com/open-quantum-safe/liboqs/issues/2045): Still to dol.

- Feedback from OQCA Governing Board on maintainer community
    * Our desire to get additional resources: Project Mgmt, Contributors, Maintainers.
    * Planning to launch a survey to reach out to users and understand their usage.
    * Hart M. to raise project needs with indsutry participants to try to increase contributors, collaborators

- Getting new contributors for next round competition
	- Clarify pathways for getting started. Action item: Create an OQS issue to create a document about getting started.
	- Reach out to authors and others about contributing their schemes.

### 5. Reports

#### 5.a PQCA TAC (Spencer)

- Drafting PQCA 1 year blog post writing OQS achievement 
- Onramp signatures... call to action for more contributors
- Elections for reps
- Content review reps 
- Hart M.: Connections with LF Outreach community: They are marketing roles with the goal getting increasing contributor involvement 

#### 5.b PQ Code Package (Pravek)

- ML-DSA-native implementation in progress

### 6. Appointment of new TSC Chair

Upcoming nominations, election process 
Desire to grow leadership pool 
 
Micheal Baentsch created an [issue for this](https://github.com/open-quantum-safe/tsc/issues/151) post meeting.
       

### 7. Election of Technical Community Rep to PQCA Governing Board

* Election of a tech rep to the PQCA board. Qualifications:- PQC expertise, represents the broader community. Call for nomination, 2 week waiting period
* Balaji Ethirajulu (LF) to send details and process

### 9. Other business

- Next TSC meeting set 3 weeks from today (May be delayed a week)
- Hart Montgomery
    - TSC team members can submit speaking proposals in various LF events, where security 
       is always a most welcome topic. Events such as CNCF, LFN, LF EDGE, OSS, etc. Balaji Ethirajulu of LF can give guidance.
