**OQS Status Meeting Summary - October 7, 2025**

**liboqs 0.15 Release Progress:**

- Several pull requests merged including documentation updates and weekly test fixes
- Bruce is working through the release checklist and preparing release notes
- Goal: Release candidate out this week, collect feedback next week
- After 0.15, focus will shift to 0.16

**Constant Time Work Update (Basil):**

- Pablo is researching available tooling and compiling reports
- Testing multiple tools: Valgrind with extended options, Memory Sanitizer (works on more platforms than Valgrind), and CT-Verifier for source code analysis
- Progress visible on [OQS project board](https://github.com/orgs/open-quantum-safe/projects/10/views/1)
- Memory Sanitizer may solve AVX512 compatibility issues encountered with Valgrind

**Provider Updates:**

- Recent PRs included composite cleanup, upstream algorithm updates, brainpool curve support for hybrid schemes, and CircleCI removal
- Will need to check if Provider needs any updates once liboqs release candidate is ready

**Community Engagement:**

- OQS Provider community call scheduled for Thursday, October 23rd at 11:30 AM Eastern
- Will be publicized through OQS website, release notes, and OpenSSL conference presentations

**Notable Milestone:**

- OQS has supported at least 33 different algorithm families over the years

**Next Meeting:** October 14th at 10 AM Eastern
