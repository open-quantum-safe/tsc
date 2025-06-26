# OQS Vulnerability Response Report: 2025-06-26-hqc-branching

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

See https://github.com/open-quantum-safe/liboqs/security/advisories/GHSA-qq3m-rq9v-jfgm

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

Douglas and Pravek received an email from Matthias Kannwischer on May 15.
Matthias was forwarding a vulnerability report for PQClean from Zhenzhi Lai and Zhiyuan Zhang from the University of Melbourne and MPI-SP.
Pravek acknowledged the email from Matthias the same day.
The OQS security team was looped in via email on May 20.

Matthias forwarded a related report from the same researchers on June 9.
Spencer acknowledged this email the same day.


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

Spencer confirmed that the reported vulnerability was present in liboqs, imported from the reference implementation (https://pqc-hqc.org) via PQClean.
The HQC team had already been notified by the initial reporters.

liboqs and liboqs-rust were directly affected by including vulnerable code.

The UWaterloo team (Douglas, Pravek, and Spencer) decided to roll the security fix into a 0.14.0 release, which would include other unreleased features from the main branch.

### 3. Patching

<!--
Briefly summarize the patch development process.
Be sure to highlight any friction points.
-->

Spencer created a temporary private fork via the draft GitHub advisory and developed a PR with a fix and a regression test.
The fix was merged into liboqs main branch on June 23.

### 4. CVE assignment

<!--
Was a CVE assigned?
If not, provide rationale.
-->

GitHub assigned CVE-2025-52473.

### 5. Public disclosure

<!--
Provide details about public disclosures (e.g., release notes, emails) other than the GitHub Security Advisories already included in the "Information" section.
-->

### 6. Feedback

<!--
Highlight any friction points in the response process.
Feel free to provide suggestions to improve the process.
Additionally, mention any follow-up work related to the vulnerability.
-->

