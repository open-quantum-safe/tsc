# OQS Technical Steering – 2024-06-27 – minutes

## Attendees

TSC members

- [ ] [Norman Ashley (Cisco)](https://github.com/ashman-p)
- [X] [Michael Baentsch (independent contributor)](https://github.com/baentsch)
- [ ] [Thomas Bailleux (SandboxAQ)](https://github.com/)
- [ ] [Basil Hess (IBM Research)](https://github.com/bhess)
- [X] [Brian Jarvis (AWS)](https://github.com/brian-jarvis-aws)
- [ ] [Christian Paquin (Microsoft Research)](https://github.com/christianpaquin)
- [X] [Douglas Stebila (University of Waterloo)](https://github.com/dstebila)

Other attendees

 - [x] [Nigel Jones (IBM)](https://github.com/planetf1)
 - [x] [Alex Bozarth (IBM)](https://github.com/ajbozarth)
 - [x] [Michael (Max)imilien, IBM](https://github.com/maximilien)
 - [x] [Ry Jones (Linux Foundation)](https://github.com/ryjones)


## 1. Chair's introduction

## 2. Approve agenda

No changes requested

## 3. Appoint minute taker

@baentsch volunteers

## 4. Report from TAC representative

@maximilien reporting for @thb-sb:
- @brian-jarvis-aws highlighted as TAC vice chair
- reminder to comment on PQCA lifecycle document as that should govern all PQCA projects; invitation to comment online and at TAC meeting(s)
  brief discussion and agreement that feedback comments in Google docs should not be silently deleted
- mention of different work groups being formed around security and CBOM
- requests for publication reviewers

## 5. Planning for Trail of Bits audit

@dstebila reiterated [meeting](https://github.com/open-quantum-safe/tsc/blob/main/meetings/2024-06-27/notes-trail-of-bits.md) and solicited discussion as to what Trail of Bits should be asked to do for OQS within the suggested 4 person weeks
- a discussion on the benefits of code audits at this time ensued and no clear agreement was achieved regarding benefits of such audit at this time; @ryjones and @baentsch emphasized the need to follow strict security practices (e.g., SDLC, Common Criteria) as and when such audits are done; further discussion seemed to be required to agree on which parts of OQS should be subject to code audit (also pertaining to https://github.com/open-quantum-safe/tsc/issues/1 and https://github.com/open-quantum-safe/tsc/issues/2. 
- a wider agreement seemed to exist around the benefits of Trail of Bits contributing to the OQS CI pipeline such as to persist their know-how for a longer period of time within the OQS code space(s)
- the particular benefit for QEMU-based testing was highlighted for the embedded OQS user community (knowing CPU cycle and memory requirements) as early as possible to plan for long-term embedded HW deployments

## 6. European Cyber week

@dstebila mentioned an invitation to present at this event and asked whether anyone would be willing to do so. No responses.

## 7. Other business

The observation was raised that the TSC github repo has many open issues and that progress on those is necessary. @dstebila suggested to make progress on those in core team meetings & agreement was reached that everyone should tag the issues of particular interest to them with "High", "Medium", "Low" importance. The tags have now been created and everyone is invited to give such feedback to prioritize the discussions.

The meeting closes after 45 minutes with no items un-discussed.
