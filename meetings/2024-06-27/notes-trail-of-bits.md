# Douglas's notes from OQS meeting with Trail of Bits (2024-05-10)

## Attendees

- Filipe Casal, Jim Miller (Trail of Bits)
- Christian (MSR)
- Douglas, Pravek, Spencer (Waterloo)
- Hart (Linux Foundation)
- Jason (SandboxAQ)
- Michael (independent)

## Notes

Trail of Bits has some time in their schedule that they can contribute to work on an open source project -- approximately a month (2 engineers for 2 weeks).  Probably late June / July.

Typically starts with a kick-off call, similar to an onboarding process for a new team member. They have a script of questions to run through. They'll ask about our security concerns, what we think needs attention, what our test suite is.  

During the review they like to have a Slack channel with the client to confirm details and ask questions. They have a variety of tooling they use in their analysis. They'll do a weekly status report call: what they've found, how to fix it, what the plan is for the next week.  

After delivery, we digest their report, and try to fix any issues they've raised.  They'll review the fixes to see if it solves the problem, and then add a "fix report" to the appendix.  They can provide us with some example reports.

- Publications page of public reports: https://github.com/trailofbits/publications?tab=readme-ov-file#security-reviews
- Open source audits on cURL: https://github.com/trailofbits/publications/blob/master/reviews/2023-12-curl-http3-securityreview.pdf
- A cryptographic audit on the “Sweet B” library- shows some of the approaches to low-level cryptographic C https://github.com/trailofbits/publications/blob/master/reviews/SweetB.pdf

Have to deicde what we want them to focus on.  They can do a code review, which is usually better for more mature code.  They can do advisory work: better CI/CD, improvements to testing, etc.  Could be narrowly focused on specific cryptographic primitives or a broader review.  Can choose whether upstream dependencies are in scope or not.

Filipe's ideas for starting points:

1. Define the scope of algorithms: ML-KEM, ML-DSA, ...? Common code: symmetric crypto, OpenSSL links? 
2. Static analysis: [CodeQL](https://codeql.github.com/) (e.g., [as applied to OpenSSL](https://blog.trailofbits.com/2023/12/22/catching-openssl-misuse-using-codeql/)), fuzzing, compiler flags, sanitizers. They have standard rulesets which are easy to apply, and can develop custom rulesets.
3. Test coverage: identify potential test gaps. They can write tests but that's not necessarily the most effective use of their time.
4. Differential fuzzing of different implementations of each algorithm, e.g., AVX2 versus reference versus libjade.
5. Constant time analysis using QEMU (https://github.com/trailofbits/qemu-tracer); evaluating our current suppression files.

### Feedback from Michael after the meeting: One proposal for how to proceed:

1. Ask TrailOfBits to add their baseline tooling to OQS CI via PRs with the following priorities:
   1. Test coverage
   2. Static analysis (missing NULL pointer/retval checks etc)
   3. Fuzzing
   4. Differential fuzzing (initially targeting the different Kyber algs)
2. Ask them for (ideally github/wiki based) documentation as to how to read and act upon errors highlighted and what to do to keep the new tests up-to-date (should they decide to not keep contributing to OQS)
3. Resource/time permitting, ask them to propose specific tests for these tools targeting "areas of interest" they undoubtedly uncover when running the tests.
