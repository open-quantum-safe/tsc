# OQS Vulnerability Response Report

<!--
Copy this template and rename the file following the format YYYYMMDD-vulnerability-name.md format.
The date should be the date that the report was created.

The intent of these reports is to help streamline the vulnerability response process.
No technical details about the vulnerability need to be provided here; those are contained in the security advisories.

For a completed example, see the report 20241220-hqc-decaps.md in this same directory.
-->

## Information

<!--
Provide links to any associated published GitHub Security Advisories.
If there are none, provide (or link to) information about the reported vulnerability.
-->

See https://github.com/open-quantum-safe/liboqs/security/advisories/GHSA-gpf4-vrrw-r8v7

## Process

### 1. Intake

<!--
Briefly summarize how the vulnerability report was received.
Be sure to include the following information:
- intake method (e.g., security@openquantumsafe.org, GitHub security report, internal meeting)
- date of report
- initial response time
- initial responder
-->

We received an initial report from Quarkslab researchers Célian Glénaz and Dahmun Goudarzi via GitHub on 17 September 2024.
Due to GitHub configuration issues, we were unaware of the report until 24 October, when the reporters left a follow-up comment.
We did not respond to the reporters until completing the Assessment phase.

### 2. Assessment

<!--
Briefly summarize the assessment process.
Technical details about the vulnerability are not necessary.
Instead, focus on which projects were impacted and 
Be sure to include the following information:
- OQS subprojects affected by the vulnerability
- upstream sources notified
- team members identified and assigned to work on a fix
-->

Douglas shared the report with Spencer, who was the team member most familiar with the affected code (the HQC implementation).
Spencer confirmed the report's findings and responded to the reporters on GitHub on 6 November.
The vulnerability was present in upstream code (https://pqc-hqc.org) and pulled into the library via PQClean.
Spencer notified the "main" and "backup" contacts listed on the upstream source's website after coordinating with the reporters.
The only subproject directly affected (by including vulnerable code) was liboqs.
It was believed that liboqs-rust was also affected; however, this turned out not to be the case.

Douglas and Spencer consulted and decided not to create a dedicated security release for two reasons:
1. The 0.12.0 release of liboqs was imminent, so a patch could be included there.
2. HQC was still an experimental algorithm.

### 3. Patching

<!--
Briefly summarize the patch development process.
Be sure to highlight any friction points.
-->
Spencer created a temporary private fork via the draft GitHub advisory and developed a PR with a fix using the `copy_from_upstream` patch mechanism.
One of the reporters reviewed and approved the PR.
The fix was merged into liboqs main branch on 21 November.
Due to liboqs GitHub settings, the PR from the private fork could not be merged directly.
It was necessary for an administrator (in this case, Ry Jones) to override these settings and commit to main.

### 4. CVE assignment

<!--
Was a CVE assigned?
If not, provide rationale.
-->
GitHub assigned CVE-2024-54137.

### 5. Public disclosure

<!--
Provide details about public disclosures (e.g., release notes, emails) other than the GitHub Security Advisories already included in the "Information" section.
-->
The security advisory was published on 6 December.
Version 0.12.0 of liboqs was released on 9 December, with a note about the vulnerability in its release notes: https://github.com/open-quantum-safe/liboqs/releases/tag/0.12.0

Spencer submitted the fix to PQClean (https://github.com/PQClean/PQClean/pull/578) on 10 December.
This led to a related security advisory being published for the pqcrypto Rust crate: https://github.com/PQClean/PQClean/security/advisories/GHSA-753p-wrj5-g8fj

### 6. Feedback

<!--
Highlight any friction points in the response process.
Feel free to provide suggestions to improve the process.
Additionally, mention any follow-up work related to the vulnerability.
-->

We observed the following obstacles throughout the process:
- Our initial response was very slow due to misconfiguration of GitHub notifications.
  This has hopefully been amended.
- Merging the patch required "admin"-level access on GitHub.
  Based on GitHub logs, this seems to be due to liboqs settings requiring a pull request for all commits.
  Apparently, a PR from a private fork does not count.
