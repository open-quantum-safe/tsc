# Coordinated vulnerability disclosure process

This document follows the framework and terminology from the OpenSSF's [`oss-vulnerability-guide`](https://github.com/ossf/oss-vulnerability-guide), with one additional step ("Feedback") added.

## Scope

This document applies to the following OQS subprojects:
- liboqs,
- liboqs-cpp,
- liboqs-go,
- liboqs-java,
- liboqs-python,
- liboqs-rust, and
- oqs-provider.

Other technical subprojects, such as the OQS fork of OpenSSH, are not considered to have security support.
Subprojects may be added to or removed from this list in the future.

## Vulnerability Management Team

The Vulnerability Management Team (VMT) is responsible for responding to reports of security vulnerabilities in OQS software.

### Members

- Michael Baentsch (@baentsch, info@baentsch.ch)
- Basil Hess (@bhess, BHE@zurich.ibm.com)
- Brian Jarvis (@brian-jarvis-aws, brianjar@amazon.com)
- Pravek Sharma (@praveksharma, pravek.sharma@uwaterloo.ca)
- Douglas Stebila (@dstebila, dstebila@uwaterloo.ca)
- Spencer Wilson (@SWilson4, spencer.wilson@uwaterloo.ca)

This team is codified as `security-managers` in the [config.yaml](../config.yaml) file.

### Coverage

Members of the VMT take it in turns to acknowledge and triage reports, rotating at each OQS Technical Steering Committee meeting, in the order listed here (which also happens to be alphabetical by last name).
The "on-call" member of the VMT shall be confirmed and communicated at each TSC meeting.
The above ordering is intended as an aid in staying organized but may be adjusted by the VMT as circumstances dictate---the important thing is to ensure coverage at all times.
Members of the VMT agree to be available to support each other on short notice if the need arises (e.g., because of overload).

When acknowledging a report, the on-call VMT member takes on the role of "[Quarterback](https://en.wikipedia.org/wiki/Quarterback)" for the issue.
They will be responsible for managing the OQS response to the vulnerability report, as described below.

## 1. Intake

This phase begins when a vulnerability report is received.
It ends when the report is acknowledged by a member of the VMT, who assumes the role of Quarterback for the issue.

### External reports

OQS provides reporters with three methods for reporting a vulnerability:
1. Email to security@openquantumsafe.org.
This email is an alias for the members of the VMT.
2. GitHub security advisories (for liboqs and oqs-provider).
These are submitted similarly to GitHub issues but are private.
3. Encrypted email to dstebila@uwaterloo.ca.

COMMENT:
We should confirm that all of the members of the VMT
(1) receive some sort of notification when a GitHub security advisory is filed on any OQS repo and (2) have the necessary permissions to view security advisories.

COMMENT:
Since liboqs-rust is published to crates.io, it should probably have security reporting switched on as well.

When a report is received via one of the first two methods, the "on call" member of the VMT is responsible for acknowledging it promptly (the OSSF recommends within 1-2 days).
- For email, this means responding to the reporter, cc'ing security@openquantumsafe.org.
- For a GitHub security advisory (which will be in the "Triage" state), this means leaving a comment on the security advisory.

No assessment of the report is necessary at this time.
The purpose of the acknowledgement is to let the reporter(s) and the rest of the VMT know that the issue is being looked at.

The responding VMT member assumes the role of Quarterback for the issue.

Reports received via encrypted email may be more sensitive and will be handled on a case-by-case basis.

> Example 1:
A vulnerability report is received via email.
Brian is on call.
He replies to the reporter(s) the next day, cc'ing security@openquantumsafe.org.
Brian is now the Quarterback for the report.

> Example 2:
A GitHub security advisory is received.
Pravek is on call.
He leaves a comment on the advisory the next day to acknowledge receipt of the report.
Pravek is now the Quarterback for the report.

COMMENT:
Do we want to commit to a reponse timeline?

### Internal reports

Vulnerabilities may also be discovered internally by members of the OQS development team or regular contributors.
For these reports, the Intake and Assessment phases may be streamlined at the discretion of the VMT.

> Example 3:
Michael receives an email from a former OQS developer advising him of a security issue in oqs-provider, including a patch.
Michael immediately recognizes the issue as a vulnerability.
Michael responds to the report, cc'ing security@openquantumsafe.org, and proceeds directly to the Patching phase.

### Reports from other channels

Reporters may not always follow instructions, and it is possible that security reports are received through other, non-endorsed channels (for example, email sent directly to a member of the VMT or a direct message on the PQCA discord).
Such a report should be funnelled into one of the provided channels as the member of the VMT who first becomes aware of it sees fit.
The focus should be on addressing the vulnerability report, not forcing the reporter(s) to resubmit via another channel.

## 2. Assessment

This phase begins when a vulnerability report is acknowledged by the VMT.
It ends when the VMT responds to the reporter(s) with an assessment of the report.

### Appointing a domain expert

The Quarterback identifies the person or people who are most qualified to assess the report and, if necessary, develop a fix.
The Quarterback provides them with all necessary information.
These domain experts may not be members of the VMT, but they should be people whom the VMT trusts to handle security-related information.
It is possible that the Quarterback will also be the team member who is most qualified to assess the issue.

### Assessing the report

The domain expert(s) assess the report and determine what action, if any, is required from OQS.
If more information from the reporter(s) is needed, the Quarterback facilitates communication.
The below table, indicating possible assessment outcomes, is copied from the [OSSF's vulnerability guide](https://github.com/ossf/oss-vulnerability-guide/blob/da8a22a1b09636c20a93fed58c1ba179557358d0/maintainer-guide.md), with the exception of the "Out of scope" lines, which are unique to OQS.

| Assessment          | Response                                                                                                                                                                                                                                                                                                                                                               |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Working as intended | Let the reporter know this is the intended behavior. If they think this behavior could be improved, they can file a feature request. Close the security issue. When responding with this assessment, you should explain why you arrived at this conclusion, in case the original report was unclear and the VMT has unintentionally misunderstood the original report. |
| Bug                 | Let the reporter know this is unwanted behavior but not a security issue, and ask them to refile this as a bug. Close the security issue.                                                                                                                                                                                                                              |
| Feature request     | Let the reporter know this is the intended behavior. If they think this behavior could be improved, they can file a feature request. Close the security issue.                                                                                                                                                                                                         |
| Vulnerability       | Let the reporter know that you have confirmed this unwanted behavior creates a security issue. Proceed with the process.                                                                                                                                                                                                                                               |
| Out of scope        | Let the reporter know that the issue is out of scope for OQS. If applicable, assist them in refiling the report upstream. See the following section for further actions.                                                                                                                                                                                                  |

#### "Out of scope" assessments

OQS packages cryptographic algorithm implementations from a variety of upstream sources.
These vary widely in level of support and software development expertise.
OQS assumes no obligation to fix vulnerabilities in upstream code, but it may choose to do so on a best-effort basis.

For all "out of scope" assessments, the vulnerability report should be passed on to the relevant upstream(s).
Depending on the nature of the issue, additional action may be required.

| "Out of scope" assessment | Description | Additional action |
|------------------|----------|-|
| Outside threat model | The issue lies outside the threat model of OQS. | Decide whether or not the severity of the issue warrants developing a patch irrespective of scope. |
| Unable to assess | Assessing the issue requires domain knowledge about the upstream beyond that of the OQS VMT. | Monitor the upstream for resolution. |
| Vulnerability: can patch  | The issue is indeed a vulnerability and can be simply and easily patched within OQS. | Decide whether or not to develop a patch. Coordinate disclosure with the upstream. |
| Vulnerability: can't patch | The issue is indeed a vulnerability but cannot be simply and easily patched within OQS. | Coordinate disclosure with the upstream. Monitor the upstream for resolution. Depending on severity, consider dropping the upstream. |

Decisions on whether or not to proceed with a possible patch should be made taking into account specifics of the upstream source.
These include responsiveness to vulnerability reports and ability of the upstream maintainers to develop a patch.
It is also important to consider the impact on end-users.
A longer response time can be tolerated for an experimental algorithm than for a standardized or standard-track algorithm.
For severe vulnerabilities which the upstream is unlikely to patch in a reasonable time frame, OQS may opt to drop support---temporarily or not---for algorithms affected by the vulnerability and publish a security advisory immediately.

COMMENT:
As a next step, we should compile a list of upstream contacts.

#### Determining affected subprojects

Part of the assessment should involve determining which subprojects are affected by the issue and how to fix the vulnerability throughout the OQS suite of [security-supported projects](#scope).
Issues within liboqs, in particular, will impact almost every subproject.
For every liboqs security advisory, advisories with the same CVE should be published on oqs-provider and the liboqs language wrappers instructing users to update the liboqs dependency.
Additionally, since the [oqs Rust crate](https://crates.io/crates/oqs) installs a specific version of liboqs as part of its build process, every liboqs security release should have a corresponding liboqs-rust security release.

### Responding to the reporter

Once the evaluation process is complete, the Quarterback responds to the reporter(s) with the OQS assessment of the vulnerability.
Regardless of the assessment outcome, the response should be courteous and thank the reporter(s) for filing the issue.
If a patch is to be made, the reporter(s) should be offered the opportunity to review and/or contribute to the fix.

### Assembling a response team

If the reported issue is assessed as a vulnerability to be patched, the Quarterback will assemble a team to develop the fix.
In addition to the patch developer(s), the team should involve at least two OQS developers with "write" permissions.
This corresponds to the minimum approval requirements for liboqs PR merge.
Additionally, the Quarterback should ensure that at least one person with GitHub admin privileges is aware of the issue and available, in order to resolve expediently any friction that may arise during the development process.

Assembling the team can be done concurrently with the other steps in the Assessment phase.

## 3. Patching

This phase after the VMT has responded to the reporter(s) with an assessment of the report.
It ends once a patch has been approved by the response team.

This document deliberately does not refer to specific GitHub UI features in order to stay current in the event of a redesign.
For these details, please see [GitHub's security advisory documentation](https://docs.github.com/en/code-security/security-advisories).

### Preparing the security advisory

The Quarterback creates a draft GitHub security advisory.
If the vulnerability report was filed as a GitHub security advisory, this will involve simply changing the state of the advisory from "Triage" to "Draft."
If the report was received via another source, a fresh security advisory will need to be created.
All members of the response team should be added to the advisory as collaborators.
The reporter(s) should also be added if they wish to be involved with patch development.

### Patch development

From the patch, the Quarterback creates a private fork specific to the security advisory.
All members of the response team should be added to the fork, as well as the reporter(s) if they wish to be involved.
From the private fork, the response team can create a pull request to fix the vulnerability.

Development on the private fork proceeds more or less as on public OQS GitHub repos, with one notable exception:
Due to current limitations on GitHub security advisories, the private fork will not have access to OQS CI.
Therefore, thorough testing of the patch should be performed offline.
The PR should be approved by
- at least two members of the response team with write permissions for the affected repo and
- if applicable, the reporter.

After approval, commits on the PR should be squashed into one, as the "squash and merge" option is not currently available for security advisories.

### Finalizing the security advisory

Concurrently with patch development, the domain expert appointed by the Quarterback should finalize the text of the security advisory.
This includes evaluating the vulnerability using the Common Vulnerability Scoring System.

## 4. CVE assignment

This phase begins when the patch is approved and ends when a CVE is assigned by GitHub.

Once the patch is ready for merge and the security advisory text is finalized, the Quarterback requests a CVE from GitHub.
This can be done from within the draft security advisory.

## 5. Public disclosure

This phase begins after a CVE has been assigned by GitHub and ends when the security advisory has been published.

Once a CVE has been assigned by GitHub, the following steps should be performed:
- Merge the security advisory.
Currently, this must be done by somebody with GitHub admin privileges.
It may be necessary to override branch protections.
- If necessary, prepare and publish a security release.
- Add specifics about the patch to the security advisory text (commit hash and version information).
- Publish the security advisory.

The security advisory should be published only after the patch has been merged and, if applicable, a security release has been published.
Whether or not a security release is required is left to the discretion of the VMT.

COMMENT:
Apart from publishing the security advisory, should we publicize the fix in any other way?

## 6. Feedback

This phase begins after the security advisory is published and ends when a security report is filed in the OQS TSC repository.

The Quarterback files a report for the issue following the [Vulnerability Response Report Template](reports/YYYYMMDD-template.md).
The report should highlight any friction or unexpected issues that arose in the response process.
This step is optional if the work did not proceed past the "Assessment" phase.
