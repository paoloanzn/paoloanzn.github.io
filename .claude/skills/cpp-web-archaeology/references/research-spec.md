You are contributing to the **C/C++ Web Archaeology** project.

The goal is to discover and catalog period-authentic C and C++ programming projects, tutorials, university assignments, lab sequences, technical articles, and source-code projects from roughly **2000–2010** that are **still available on the live web today**.

The emphasis is on material that feels like programming on the web during that era: original university course archives, personal programming sites, old technical communities, SourceForge-era project pages, long-running tutorial domains, and similar sources.

Do not optimize for quantity. A smaller batch of genuinely period-authentic material is much more valuable than hundreds of weak search results.

## Repository and output location

The project lives in:

`paoloanzn/paoloanzn.github.io`

The public catalog is served from:

`/cpp-web-archaeology/`

The primary database is:

`cpp-web-archaeology/data/projects.json`

The website reads that JSON file directly.

When you finish a research batch:

1. Add only genuinely new records to `cpp-web-archaeology/data/projects.json`.
2. Do not rewrite or reorder existing records unnecessarily.
3. Deduplicate primarily by canonical URL.
4. Commit the changes to the `main` branch.
5. Use a descriptive commit message such as:

`Add 18 manually curated compiler and systems archive entries`

Do not modify unrelated files in the repository unless necessary.

## Core research criterion

The page must satisfy two separate conditions:

**A. The material itself must come from approximately 2000–2010.**

There should be credible evidence such as:

- explicit publication/update date
- course semester/year
- year embedded in the original URL
- original file timestamps
- assignment due dates
- contemporary compiler/toolchain references
- contemporaneous surrounding course material

**B. The site/page must still be directly available on the live web.**

Preferred:

`https://some-old-site.edu/course/2004/project1.html`

Not acceptable as the primary catalog URL:

`https://web.archive.org/...`

The Wayback Machine may be useful to investigate provenance, but this catalog is specifically about old material that survived on the live web.

Modern GitHub recreations, mirrors, reposts and retrospective articles should normally be rejected.

## What counts as a strong result

Prefer pages where the reader actually builds or implements something substantial.

Excellent examples include:

- operating system kernels
- schedulers
- user-level thread libraries
- filesystems
- shells
- memory allocators
- network servers
- TCP/UDP-like protocols
- routing protocols
- compilers
- interpreters
- virtual machines
- assemblers/linkers
- emulators
- database buffer managers
- B+ trees
- query engines
- compression tools
- text editors
- game engines
- graphics/rendering systems
- image-processing programs
- embedded systems
- substantial course project sequences

A project specification is acceptable even when it is not a step-by-step tutorial. Old university assignments are often some of the best material in the archive because they preserve the original environment, source skeletons and implementation requirements.

## Search methodology

Do not simply search:

`C++ tutorial 2004`

Use combinations of historical fingerprints, project terminology, old toolchains, university archives and URL structure.

### 1. Search by period toolchain fingerprints

Period-specific technologies are extremely valuable because they naturally surface old pages.

Useful queries include combinations of:

- `"Visual C++ 6.0"`
- `"VC6"`
- `".dsp"`
- `".dsw"`
- `"Visual Studio .NET 2003"`
- `"Borland C++"`
- `"Dev-C++"`
- `"DJGPP"`
- `"RHIDE"`
- `"Fedora Core 3"`
- `"Fedora Core 4"`
- `"gcc 3"`
- `"CVS"`
- `"Bochs"`
- `"Nachos"`
- `"Pintos"`
- `"Minithreads"`
- `"MINIBASE"`
- `"SDL 1.2"`
- `"Allegro"`
- `"OpenGL 1.4"`
- `"DirectX 8"`
- `"DirectX 9"`

Examples:

`"Visual C++ 6.0" filesystem C++ project`

`"CVS" "Makefile" operating systems project C`

`"Bochs" kernel project C 2003`

`"Fedora Core 4" compiler project C`

These toolchain references frequently provide stronger period evidence than a copyright footer.

### 2. Search university archives aggressively

University sites are one of the richest sources.

Use:

`site:edu`

plus terms such as:

- `project`
- `assignment`
- `lab`
- `programming assignment`
- `handout`
- `starter code`
- `skeleton code`
- `source code`
- `project 1`
- `project 2`

Combine them with technologies and years.

Examples:

`site:edu "filesystem" "project" C 2004`

`site:edu "compiler" C++ "Fall 2006"`

`site:edu "operating systems" "project 3" C`

`site:edu "buffer manager" C++ 2004`

`site:edu "user level threads" C project`

### 3. Exploit year-coded URL structures

Old university sites frequently keep semesters permanently under paths such as:

`/2004/`

`/fa04/`

`/fall2004/`

`/spring2003/`

`/archive/2006/winter/`

Search for these directly.

Examples:

`site:edu inurl:2004 filesystem C project`

`site:edu inurl:2006 compiler C++ assignment`

`site:edu inurl:fall05 operating systems`

`site:edu inurl:spring2002 sockets project C`

The URL itself can then become part of the provenance evidence.

### 4. Search for implementation language rather than topic names alone

Phrases such as these identify real project work:

- `"implement"`
- `"write"`
- `"build"`
- `"develop"`
- `"you will implement"`
- `"your task is"`
- `"starter code"`
- `"skeleton"`
- `"what to submit"`
- `"files to modify"`
- `"Makefile"`
- `"tar.gz"`
- `"turn in"`
- `"due"`

Example:

`site:edu "you will implement" filesystem C`

`site:edu compiler "files to modify" C++`

`site:edu "what to submit" shell C`

### 5. Search for old software architectures and canonical teaching systems

Some systems were widely used in period courses and lead to entire ecosystems of archived assignments.

Examples worth deliberately searching:

- GeekOS
- Nachos
- Pintos
- JOS
- Minithreads / PortOS
- Cool compiler
- MINIBASE / Minibase
- OpenImpact
- xv6 only when the page actually falls inside the desired period
- Bochs-based kernels

Once you find one course using such a system, inspect the surrounding course directory manually. Often there are four to six additional project pages nearby.

### 6. Follow directories, not just search results

This is one of the most important techniques.

When a strong result appears, inspect:

- its parent course page
- previous/next project pages
- assignments index
- project directory
- starter-code links
- sibling semesters
- instructor's older course archives

One good page frequently leads to ten better pages.

For example, discovering a 2003 Minithreads assignment should trigger exploration of:

`/projects/`

`project1/`

`project2/`

`project3/`

and adjacent semesters.

Treat old websites as directory trees to explore, rather than isolated search-engine results.

### 7. Search adjacent domains after finding a good source

If a department or professor maintained good historical material, search that host directly.

Examples:

`site:cs.cornell.edu/courses filesystem C`

`site:classes.cs.uchicago.edu/archive compiler`

`site:cs.umd.edu GeekOS`

The exact syntax supported by a search engine may vary, so also search the full hostname as a quoted or normal term.

## Provenance methodology

Every entry should answer:

**Why do we believe this material really comes from the period?**

Use concrete evidence.

Strong evidence:

- `"Due: May 2, 2002"`
- `"Fall 2004"`
- page says `"Last updated March 2004"`
- URL includes `/2003/`
- instructions mention Visual C++ 6.0
- source workspace uses `.dsp` / `.dsw`
- project requires CVS
- instructions target Windows NT/2000
- course uses Fedora Core 4
- compiler requirements mention GCC 3.x
- source release history dates to 2001

Weak evidence:

- current copyright footer says 2004–2026
- modern article claims something originated in 2002
- search snippet mentions 2005 with no confirmation
- modern GitHub README references old code

Always prefer primary evidence visible on the original page.

## Authenticity signals

Positive historical signals include:

- Visual C++ 6
- `.dsp` / `.dsw`
- CVS
- SourceForge
- Windows NT / 2000 / XP
- Fedora Core
- GCC 2.x / 3.x / early 4.x
- Bochs
- Solaris university machines
- tar/gzip submission instructions
- FTP submission
- email submission
- old Makefile assumptions
- pthreads
- raw BSD sockets
- fixed-function OpenGL
- SDL 1.2
- Allegro 4
- DirectX 7/8/9
- early MIPS/SPIM workflows

Negative or suspicious signals include:

- GitHub as the only source
- GitLab as the only source
- Medium
- Dev.to
- modern static-blog reposts
- VS Code
- C++17 / C++20 / C++23
- modern CMake-centric rewrites
- Docker
- modern package managers
- tutorial pages obviously redesigned/re-authored recently with no preserved original text

A modern-looking website is not automatically disqualifying if the original period content clearly remains intact. Judge the content and provenance.

## Research focus

The catalog already contains significant graphics, OpenGL and Win32 material.

New research should preferably explore underrepresented domains such as:

- operating systems
- filesystems
- concurrency
- compilers
- interpreters
- virtual machines
- assemblers
- linkers/loaders
- emulators
- networking protocols
- database internals
- storage engines
- compression
- Unix utilities
- embedded programming
- device drivers
- distributed systems
- language runtimes
- garbage collectors
- memory allocators

Do not avoid graphics completely, but only add more graphics material when it is unusually strong.

## Quality control

Before adding a page, manually inspect it.

Confirm:

1. The URL currently loads.
2. It is not merely a modern mirror.
3. C or C++ is actually involved.
4. The material is genuinely from 2000–2010.
5. It represents meaningful project/tutorial material.
6. It is not already present in `projects.json`.
7. The claimed year is supported by evidence.
8. The description accurately reflects what the reader implements.

Reject borderline results rather than weakening the catalog.

## Record schema

Add entries in approximately this structure:

```json
{
  "title": "Cornell CS414 — User-level threads and semaphores",
  "url": "https://...",
  "year": 2003,
  "year_label": "June 2003",
  "language": ["C"],
  "category": "Operating Systems / Concurrency",
  "kind": "project assignment",
  "site": "cs.cornell.edu",
  "score": 99,
  "evidence": [
    "Original 2003 assignment",
    "C source skeleton",
    "Windows NT Minithreads environment",
    "Implements TCBs, scheduler, queues and semaphores"
  ],
  "tags": [
    "threads",
    "semaphores",
    "scheduler",
    "Minithreads"
  ],
  "notes": "Build a non-preemptive user-level thread package, including queues, thread control blocks, a scheduler and synchronization primitives."
}
```

### Score guidance

The score is an archival-fit/confidence score rather than an evaluation of educational quality.

Use approximately:

**100**
Exceptionally strong provenance and project value. Original dated archive, concrete implementation project, strong C/C++ evidence.

**95–99**
Very strong period evidence and clearly relevant material.

**90–94**
Good material with somewhat weaker provenance or less substantial project scope.

**85–89**
Useful but borderline. Add sparingly.

Avoid adding entries below roughly 85 unless there is a compelling reason.

## Categories

Use descriptive categories. Existing examples include:

- `Operating Systems`
- `Operating Systems / Concurrency`
- `Operating Systems / IPC`
- `Filesystems`
- `Systems / Unix`
- `Systems / Memory`
- `Systems / Labs`
- `Networking`
- `Networking / Protocols`
- `Networking / Routing`
- `Compilers`
- `Compilers / Lexing`
- `Compilers / Semantic Analysis`
- `Compilers / Code Generation`
- `Compilers / Optimization`
- `Database Internals / Buffer Manager`
- `Database Internals / Indexing`
- `Database Internals / Query Processing`

Create new categories when they materially improve navigation, but avoid unnecessary one-entry microcategories.

## Project sequences versus individual assignments

It is acceptable to include both:

1. the overall course/project sequence, and
2. particularly strong individual projects from that sequence.

For example:

`Cornell CS414 — Minithreads OS project sequence`

and

`Cornell CS414 — Unix-like filesystem for Minithreads`

This is useful because one entry gives the reader the whole curriculum while the individual entry makes a specific project discoverable by category/search.

Do not index every trivial sub-page.

## PDFs

Period PDFs are acceptable and often excellent.

If a PDF contains the original assignment or tutorial, catalog the direct live PDF URL.

Verify:

- date
- language
- project requirements
- host provenance

Prefer the university's original PDF over copies hosted elsewhere.

## Research reporting

At the end of your batch, report:

- how many entries you investigated
- how many you accepted
- how many you rejected
- which problem domains you focused on
- the strongest discoveries
- the resulting catalog size
- the Git commit SHA

Also mention any interesting rejected/borderline sources that another agent may want to investigate later.

## Critical principle

This is an **internet archaeology project**, not a general list of C/C++ tutorials.

The most valuable discovery is a page where a programmer can open it today and encounter something very close to what a student or hobbyist would actually have seen in 2002, 2004 or 2007:

old toolchains,
old APIs,
old build systems,
old terminology,
old source skeletons,
old submission instructions,
and a real programming project.

Search for that feeling, then verify it with evidence.