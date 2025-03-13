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

## Agenda
(see [agenda](./agenda.md))
### 1. Chair's introduction
- Douglas opened the meeting, welcome

### 2. Approve agenda

- Reordered to accomodate Akira Nagai's time zone.
### 3. Appoint minute-taker

- Norman Ashley 
### 8. NTRU (Akira Nagai and Kan Yasuda, NTT Social Informatics Laboratories)
-------------------------------------------------------------------------
    * Akira Nagai and Kan Yasuda, NTT proposed and gave rational for re-adding NTRU to libOQS
        * NTRU is used by NTT
        * IETF involved standardization process
        * Industry adoption
        * Used for testing 
        * Alternative to MLKEM
        * They are willing to contribute and maintain

    - Questions raised 
        - How will liboqs be used? Direct via OQS API
        - will OQSProvider be needed? No, not initially

* Resulting Action Item:
     - Douglas to create an issue to further discussions on the topic. 
     - Follow up with Akira and Kan.

### 4. Review action items from previous meeting
	- [Security response team](https://github.com/open-quantum-safe/tsc/issues/60)
    * Spencer gave upon the security response doc. It has been approved by some but needs 
              more reviewers especially those on the response teams.
              OQS security response process
              https://github.com/open-quantum-safe/tsc/pull/124
              Once merged, a trial run will be done on a low-level issue or as simulated issue.
	- [Binary distributions](https://github.com/orgs/open-quantum-safe/discussions/1625#discussioncomment-11751301)
    Table of binary distributions

	- [Algorithm support levels](https://github.com/open-quantum-safe/liboqs/issues/2045)
     Table of support levels (see agenda)
        https://github.com/open-quantum-safe/liboqs/issues/2045

	- Feedback from OQCA Governing Board on maintainer community
      * Desire to get additional resources 
                     Project Mgmt
                     Contributors
                     Maintainers

                Planning to launch a survey to reach out users
                Hart M. to looking into getting LF people geared to increase contributors, collaborators

                Getting new contributors for next round competition

    Resulting Actin Items:
    ----------------------
                Email pathways to get started on contribution 
                Create a OQS issue on how to contribute

	- Strategy for NIST On-Ramp Signatures
    * Investigations concerning NIST onramp for signature scheme 
           Reaching out to authors
           Hart M. reaching out to others

### 5. Reports
** PQCA TAC
    Spencer:- 
          Drafting PQCA 1 year blog post writing OQS achievement 

          Onramp signatures... call to action for more contributors

          Elections for reps
          Content review reps 

          Hart M.:- connections with LF Outreach community 
                 They are marketing roles with the goal getting increasing contributor involvement
                 Content community

    Pravek:- 
       PQ Code Package
          PQ Code package MLKEM, API
          MLDSA native implementation in progress

### 6. Appointment of new TSC Chair
       Upcoming nominations, election process 
       Desire to grow leadership pool 
 
       Election of a tech rep to the PQCA board. Qualifications:- PQC expertise, represents the broader community.
       Call for nomination, 2 week waiting period

       Balaji Ethirajulu (LF) to send details and process

       Micheal Baentsch Created an issue post meeting ...
            https://github.com/open-quantum-safe/tsc/issues/151

### 7. Election of Technical Community Rep to PQCA Governing Board
* Election of a tech rep to the PQCA board. Qualifications:- PQC expertise, represents the broader community.
       Call for nomination, 2 week waiting period
* Balaji Ethirajulu (LF) to send details and process

### 9. Other business
- Next TSC meeting set 3 weeks from today (May be delayed a week)
- Hart Montgomery
    - TSC team members can submit speaking proposals in various LF events, where security 
       is always a most welcome topic. Events such as CNCF, LFN, LF EDGE, OSS, etc. Balaji Ethirajulu of LF can give guidance.
- Meeting Recording
    - [Recording](https://zoom.us/rec/share/gADvQF0yH7_sNeSRE8IW_WbB7ZTjQEBTb2fIKA1-3zNvV6o_wDGJbRzkIXMgLMG_.q65ytllLWYsKpGGu)