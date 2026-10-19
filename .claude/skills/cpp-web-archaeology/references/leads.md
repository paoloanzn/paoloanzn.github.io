# Leads for future batches

Pages found in earlier batches (last updated after batch 2, October 2026) that were not added yet. Check them first when your domain matches.
Remove a lead from this file when it is added to the catalog or confirmed dead. Add new leads from each batch
(merge_batch.py prints them; its report JSON lists them under `leads`).

Status words: **candidate** = likely acceptable; **sibling** = another semester of a course already in the catalog (add only if clearly stronger or different); **check** = needs a date or language check.

## Carried over from batch 1 (re-checked October 2026)

- https://courses.cs.umbc.edu/undergraduate/421/spring02/burt/projects/project1.html — UMBC CMSC421, assigned 6 March 2002: add a system call to a Linux 2.4 kernel (ksyms.c, EXPORT_SYMBOL). Authentic but small; around score 88.
- https://courses.grainger.illinois.edu/ece511/Fa2003/homework/hw2.html — UIUC ECE412 Fall 2003 HW2: register renaming in a pipelined simulator (rename_stage.h). Tarballs are 404, so the language can't be confirmed.
- https://www.classes.cs.uchicago.edu/archive/2007/fall/51081-1/labs/LAB5/lab5.html — UChicago 51081 Fall 2007 System V IPC lab (message queues, shared memory, semaphores) in C. A sibling of the accepted LAB4.
- http://www.osdever.net/tutorials/view/multitasking-howto — Bona Fide Multitasking Howto (indexed Jul 2003): stack-based task switching with a C process struct and NASM ISR. Also Spinlocks I-III by Rieker.
- https://www.cs.princeton.edu/courses/archive/fall04/cos318/projects/5.html — Fall 2004 version of the COS318 VM project (Last-Modified 18 Nov 2004). The fall06 version was accepted instead.

## Language runtimes, GC, interpreters

- https://cs.unm.edu/~williams/cs491s06.html — UNM CS491/591 Spring 2006 (also cs491s04.html, cs491s02.html): every student writes a Scheme interpreter or compiler 'in a non-garbage-collected language (e.g., C)' with projects for reader, symbol table, evaluator and GC plus a best-GC contest. The project specs are not linked, so C is only suggested. Around 86.
- https://www.complang.tuwien.ac.at/anton/vmgen/ — Anton Ertl's Vmgen interpreter generator (makes C VM interpreters with threaded code and superinstructions); dir files dated March 2003, mentions Unladen Swallow 2009Q1. A tool page rather than a project. Around 87.
- https://www.complang.tuwien.ac.at/forth/threaded-code.html — Ertl's classic threaded-code explainer with GNU C 'goto **ip++' examples; latest reference 2003 but no page date.
- https://archive.gamedev.net/archive/reference/articles/article1633.html — GameDev 'Creating a Scripting System in C++' Parts I-IV (articles 1633/1686/1788/1803, c. 2002); Cloudflare challenge blocked curl, so it could not be verified.
- https://sfkaplan.people.amherst.edu/courses/2003/fall/cs12/labs/lab-9/index.html — Amherst CS12 Fall 2003 lab (Scott Kaplan, a GC researcher) on reference counting; the https cert has expired and http times out, so it could not be read.
- https://www.piumarta.com/software/cola/ — Piumarta COLA/idst snapshot idst-20070918 (late-bound object/lambda architecture in C). Large research system, but period-dated.
- https://zeus.cs.pacificu.edu/ryand/cs480/2007/interpreter.html — Pacific U CS480 Spring 2007 quad interpreter spec (fetch/decode/execute, activation records); language not stated. Better fit for the compilers agent.
- https://swtch.com/~rsc/regexp/regexp3.html — Russ Cox 'Regular Expression Matching in the Wild' (March 2010, RE2 in C++); third sibling of the series, so it was left out.

## Emulators, simulators, assemblers, linkers

- https://www.cs.unc.edu/~gb/Comp120Fall2004/Assignment10.html — UNC COMP 120 Fall 2004 cache simulator (assigned 2 Nov 2004) in C/C++/Java; small scope, about 85
- https://acg.cis.upenn.edu/milom/cis501-Fall05/homework/hwk2.pdf — UPenn CIS501 Fall 2005 cache-inference program and 2-way LRU cache module (my-cache.c) for SimpleScalar; sibling of accepted hwk4
- https://www.cs.virginia.edu/~skadron/cs654/assignments/pipe2.pdf — UVA CS654 pipeline exercise #2 (Oct 2003): adds bimodal predictor, caches and forwarding to sim-pipe.c; sibling of accepted pipe1
- https://courses.grainger.illinois.edu/ece511/Fa2006/homework/hw2.html — UIUC ECE 511 Fall 2006: gshare in ifetch.h of the same C++ simulator lineage (RedHat 9/Cygwin); hw1–hw5 listed
- https://pages.cs.wisc.edu/~david/courses/cs752/Fall2008/handouts/hw3.html — Wisconsin CS752 Fall 2008 hw3: modify SimpleScalar sim-fast.c to count load/store address conflicts; modest coding
- https://gavare.se/gxemul/gxemul-stable/doc/technical.html — GXemul C full-system emulator, 'mostly written in 2003-2005'; technical doc has 2004 dates, but the page is the current 0.7.0 release
- https://www.muppetlabs.com/~breadbox/software/elfkickers.html — ELF Kickers C object-file tools (elfls, elftoc, rebind, sstrip), changelog 1999-2001, but the current tarball is 2021
- https://piumarta.com/software/lib6502/ — lib6502/run6502 C 6502 emulator library; earliest dated changelog entry on the page is 2010-07-23 (v1.1)
- https://www.joachim-bauch.de/tutorials/loading-a-dll-from-memory/ — C PE loader tutorial (relocations, imports) for MemoryModule, originally c. 2004, but the page has no date beyond a '2003-2026' footer
- https://www.csd.uoc.gr/~hy425/2008s/projects/machine_assignment_1.pdf — Crete HY425 2008 (m,n) branch predictor model from a C template; sibling of accepted MA3

## Parallel and distributed systems

- https://classes.cs.uchicago.edu/archive/2000/fall/CS103-01/ — Fall 2000 Beowulf/MPI course (Tufo): Alpha Huxley cluster at Argonne HOWTO, mpihello.c, MPICH/LAM links. Very authentic, but assignment specs are not linked, only 'Assignment 1 - Solution 1'.
- https://userpages.cs.umbc.edu/motteler/teaching/parpro/06a/proj2/index.html — Spring 2006 version of the UMBC MPI N-body project (binary column-order format); sibling of the accepted 2001 page.
- https://cseweb.ucsd.edu/classes/wi08/cse260/ — UCSD CSE260 Winter 2008 (Baden) graduate parallel computation with HW A1-A4 and projects; not checked in detail.
- https://cseweb.ucsd.edu/classes/sp06/cse223b/labs.html — Spring 2006 CSE223B labs on a virtual cluster; may differ from the 2004 set (lab4.html linked).
- https://pages.cs.wisc.edu/~david/courses/cs758/Fall2009/includes/homeworks.html — Fall 2009 CS758 homework set; sibling of the accepted Fall 2007 page.
- https://sites.cc.gatech.edu/fac/hyesoon/spr10/lab4.html — Spring 2010 CUDA ray-tracer improvement lab (AntTweakBar, GLEW); lab3 is CUDA 2D convolution.
- https://sites.cc.gatech.edu/classes/AY2009/cs4210_fall/ — GT CS4210 Fall 2008 with projects/Project1-3.pdf (pthreads server, shared-memory proxy, RPC); sibling of the accepted Fall 2009 project.
- https://users.cs.utah.edu/~mhall/cs4961f09/CS4961-proj1.pdf — Utah CS4961 Fall 2009 project 1: rewrite t1.c..t5.c to vectorize with ICC on VS2008 (/Qvec-report:3). Small scope.
- https://bluehawk.monmouth.edu/~rclayton/web-pages/s04-537/proj2.html — Monmouth CS537 Spring 2004: write an sRPC stub generator (srpc-gen emits C++); host language is the student's choice of C++ or Java.
- https://webpages.charlotte.edu/abw/parallel/par_prog/index.htm — Wilkinson/Allen textbook site (2nd ed. 2004) with step-by-step MPI, PVM, pthreads and DSM tutorials in C; undated pages.

## Embedded systems and drivers

- https://course.ece.cmu.edu/~ee349/f-2008/ece349-fall08-html-files/projects.html — CMU 18-349 Fall 2008: Gumstix/XScale labs with U-Boot 1.1.4 standalone apps, the Gravel kernel, IRQs/timers and RMS/priority inheritance (Gravelv2). The page is live but every handout PDF and support tarball returns 404. The host is very slow.
- https://www.rose-hulman.edu/class/ee/hoover/ece331/old%20stuff/ECE331%20Spring%202008%20Labs/ — Rose-Hulman ECE331 Spring 2008: Apache index of 9S12C32 labs (.doc handouts plus .c files such as cointoss.c, an interrupt-driven combination lock and a tuner). Authentic but raw; score about 88.
- https://my.mech.utah.edu/~me3200/labs/F02Labs/F02_Handyboard_L5.pdf — Utah ME3200 Fall 2002 Handy Board / Interactive C intro lab; the directory has F01-F05 lab sets with 2000-2005 timestamps. Introductory level.
- https://www.linuxjournal.com/article/7136 — Greg KH 'I2C Drivers, Part I' (Dec 2003), C listings; Part II and other 'Driving Me Nuts' columns such as 8110 (2005) are also live. Held back to limit records from one site.
- https://users.ece.utexas.edu/~valvano/robot/Robot2006.htm — UT EE345M 2006 robot competition (6812 drivers, PWM, input capture); the page itself never mentions C.
- https://www.eecg.utoronto.ca/~pc/courses/edk/modules/ — Toronto Xilinx EDK tutorial modules for versions 6.1-8.2 (2004-2007), MicroBlaze. Mostly tool walkthroughs.
- https://www.ethernut.de/en/documents/ — Nut/OS (AVR/ARM RTOS) tutorial index; mixed dates (SuSE 9.3, RHEL4, July 2009 manual).
- https://www.cs.usfca.edu/~cruse/cs686f05/ — Cruse CS686 Fall 2005: Linux 2.6 VESA/vram drivers and four projects (project1-4.f05). Cruse quota used.

## Unix tools, compression, crypto

- https://www.cct.lsu.edu/~kosar/csc4304/projects/Project-1.pdf — LSU CSC4304 Fall 2010 (Kosar): implement ls with -a -C -d -l -L -p -r -R -S in C; Project-2 is the myhttpd web server. Fall 2010 is on the course page, not in the PDF. About 87.
- https://research.cs.umbc.edu/cisa/courses/cmsc/443/fall06/PROJECTS/project1sp2005.html — UMBC CMSC443 Spring 2005 crypto projects (mini DES, A5 key stream, hash, RSA text-to-integer); C/C++/Java allowed
- https://zlib.net/zlib_how.html — Mark Adler's annotated zpipe.c deflate/inflate example; version history from 30 Oct 2004, but the page was touched again in Feb 2026
- https://www.cs.princeton.edu/courses/archive/spr03/cs126/assignments/prefix.html — Same COS126 Spring 2003: decode prefix-code (Huffman tree) messages in C. Small sibling of the RSA entry.
- https://www.cs.princeton.edu/courses/archive/spr04/cos217/assignments.html — COS217 Spring 2004 to Spring 2009 assignments (decomment, symtable, heapmgr, buffer overrun, ish shell) are all live; better for a systems agent
- https://staff.um.edu.mt/csta1/courses/lectures/csa2060/ — Malta CSM210 C course index: assessed C projects for 1997, 2000, 2001 (x2), Jan 2002 and Jan 2004 (process scheduling simulator)
- https://users.csc.calpoly.edu/~pnico/class/ — Cal Poly CPE357 (Nico): mytar, Huffman hencode/hdecode, mush shell. The https chain is incomplete here (curl error 60), so it could not be verified.
- https://web.eecs.utk.edu/~jplank/plank/classes/cs360/360/labs/Lab-4-Fakemake/index.html — UTK CS360 Fakemake lab (make clone in C); TLS chain failed here, and Plank's pages are often undated
- https://web.cs.wpi.edu/~cs4513/b05/proj0.html — WPI CS4513 B-term 2005: install the WPI File System (Minix fs clone) into a Linux kernel; for the filesystems agent
- https://www.cs.columbia.edu/~smb/classes/f07/assignments.html — Bellovin W4187 Fall 2007 security architecture programming assignments (four, dated); not checked in detail

## Under-represented years (2000, 2008–2010)

- https://cseweb.ucsd.edu/classes/fa00/cse131a/parser.htm — UCSD CSE131A Fall 2000 Oberon compiler (lexer due Oct 15, 2000; parser 11/12/00; semantic analysis Dec 3, 2000) with yacc for C++ users or CUP for Java users. Left out because Java is also allowed and UCSD already has a fa00 entry. wi00 cse131a_A has the same course.
- https://www.cs.columbia.edu/~nieh/teaching/w4118_f10/homeworks/hmwk6.html — Columbia Fall 2010 W4118 (due 12/13/2010): ext2 work on the Android emulator/goldfish kernel 2.6.32; f10 HW4 is a SCHED_DBMC scheduler. Siblings of the accepted f09 pages.
- https://www.cs.columbia.edu/~nieh/teaching/w4118_f00/homeworks/hmwk5.html — Columbia Fall 2000 HW5: new Linux 2.2 page-replacement policy (kern4). Could stand alone if the sequence entry is not enough.
- https://www.cs.columbia.edu/~junfeng/10sp-w4118/hw/hw2.html — Columbia Spring 2010 W4118 (Junfeng Yang), Linux kernel homeworks on VMware; another Columbia offering, so skipped.
- https://www.cs.rochester.edu/~kshen/csc257-fall2009/assignments/assignment2.html — Same Fall 2009 course: distance-vector routing over UDP (any language). assignment1 is a threaded web proxy (C/C++ or Java).
- https://www.cs.utah.edu/~mflatt/past-courses/cs5460/hw7.html — Utah Fall 2009 HW7: distributed version of the threaded game simulation (dist-field.zip, rpc.zip, dsm.zip). hw3.html is a pthreads game simulation.
- https://www2.cs.uh.edu/~jsteach/cosc4377/ — UH COSC4377 archive with 2000fall, 2001spring/fall, 2002-2007 and 2009spring offerings; later semesters may have stronger socket projects.
- https://www.cs.hmc.edu/~geoff/classes/ — Kuenning's index of HMC class archives: cs105 spring09/spring10 (CS:APP labs), cs134 OS 2002/2003, cs70 C++ fall00/spring00.
- https://courses.engr.illinois.edu/cs241/sp2010/ — UIUC CS241 Spring 2010 sibling of the accepted Fall 2009 page; not checked in depth.

## Graphics, games, audio internals

- https://people.ece.cornell.edu/land/courses/ece4760/labs/s2005/lab2.html — ECE476 Spring 2005 cricket-call generator: amplitude-modulated DDS sine synthesis in C on a Mega32 (lab2.html dated 2005-02-21, ddsC.c 2004-11). Good audio/embedded lab, but the host already has 3 catalog entries.
- https://users.ece.utexas.edu/~bevans/courses/realtime/lectures/laboratory/c6713/lab3/index.html — UT EE345S TMS320C6713 FIR/IIR circular-buffer filters in C; only a 2008 book reference dates it
- https://graphics.stanford.edu/courses/cs248-04/proj3/index.html — CS248 2004 video game project resources; also cs248-02/03/05/06/07 offerings are live with the same paint/rasterizer/game sequence
- https://flipcode.com/archives/Advanced_Lightmapping.shtml — March 2001 lightmap generation article on flipcode; not checked in depth
- https://fabiensanglard.net/quakeSource/index.php — Fabien Sanglard's 2009 Quake engine code review; in-window article but a retrospective on 1996 code. Not loaded.

## Compilers (batch 3, October 2026)

- Not yet added on purpose (catalog review drops, could return if a slot opens): UDel CISC672 Spring 2005 Cool semantic analyzer (~90); Wisconsin CS701 Fall 2005 project 3; IIT Bombay CS715 2009-10; McGill COMP520 Fall 2004 (C or Java); Pacific CS480 2007 part 4bu.
- https://www.eecis.udel.edu/~pollock/672/s05/pa4.pdf — UDel CISC672 Spring 2005 Cool semantic analyzer (semant.cc, cool-tree.h, C++ default, due 18 Apr 2005), score ~90. UDel f06 is already in the catalog, so this is out of scope for this batch. It would be a valid 2nd semester covering the semantic-analysis phase, which the f06 records lack. Course schedule: https://www.eecis.udel.edu/~pollock/672/s05/sched.html
- https://theory.stanford.edu/~aiken/software/cool/cool.html — Aiken's Cool distribution page (Stanford host, not CS143 proper); cooldist/handouts are CS143 Fall 2009 copies, so skipped under the Stanford rule
- https://web.eecs.umich.edu/~weimerw/2009-4610/pa.html — Weimer UVA Cool PAs 2007-2010. Re-check if a fetcher can pass the host's TLS; probably multi-language, which would rule it out
- https://www.cs.utexas.edu/~novak/cs375.html — UT Austin CS375: students write a Pascal-subset compiler in C. Not Cool/Decaf; a lead for the general compilers agent
- https://www.cs.rutgers.edu/courses/415/ — Rutgers CS415 (ILOC, C) has older semesters under classes/. Not Cool/Decaf; a lead for the general compilers agent
- https://www.lrde.epita.fr/~tiger/tigdes_20010430_v11.pdf — EPITA Tiger project design doc in French, dated 30/04/2001, v1.1 (H. Delorme, W. De Denterghem): abstract syntax, visitors and frame modeling for the C++ Tiger compiler. Genuine period document, but it is design notes rather than an assignment. About 86.
- https://www.lrde.epita.fr/~tiger/sujet-libre-2003-tigerVM.pdf — EPITA 2003 optional student project spec: a VM that runs the textual Tiger IR, covering canonicalization, basic blocks and traces (the ancestor of HAVM). Implementation language not stated.
- https://www.lrde.epita.fr/~tiger/exams/ — EPITA Tiger/ccmp exams 2002-2007 with corrections (PDFs). Period material, but exams, not projects.
- https://homepage.iis.sinica.edu.tw/~tshsu/compiler2005/hwks/hwk5.txt — Sibling 2005 version (due June 16, 2005) of the accepted NTU lex/yacc Pascal-like-to-C-- assignment. The host often resets connections.
- https://st.ewi.tudelft.nl/koen/compilerbouw/resources.html — TU Delft master's compiler construction 2002 (Langendoen): LLgen/lex/yacc slides plus a link to 'assignments and reference compiler'. Not yet followed; the host resets curl, but WebFetch works.
- https://zeus.cs.pacificu.edu/ryand/cs480/2005/cs480.html — Spring 2005 offering of the accepted Pacific CS480 pcc compiler course. Use it only if the 2007 page ever goes down.
- https://pages.cs.wisc.edu/~fischer/cs701.f00/proj2.html — Wisconsin CS701 Fall 2000/2001/2003 directories hold the same Simple-SUIF register-allocation and optimization projects; only usable if the F05 records are dropped (sibling limit).
- https://pages.cs.wisc.edu/~fischer/cs701.f05/proj4.html — CS701 F05 Project 4: open research project (Appel/George coalescing, live-range splitting, rematerialization, scheduling) on the same C++ code generator; small sibling.
- https://web.eecs.umich.edu/~mahlke/courses/583f07/homeworks/583hw2.htm — EECS 583 Fall 2007 HW2: Trimaran hyperblocks over loops and SESE regions with a performance contest; a strong alternative to W06 if the semester mix changes. umich needs the InCommon RSA OV SSL CA 3 intermediate for curl.
- https://moss.csc.ncsu.edu/~mueller/codeopt/codeopt05/projects.html — NCSU CSC 791A Spring 2005 student project pages (VPO for Power, gprof via binary instrumentation, SUIF MPI); reports, not assignments.
- https://www.cs.unh.edu/~pjh/courses/cs912/ — UNH CS912 Advanced Compiler Design Fall 2000 (Hatcher): code selector from Hyperion IC to Alpha and a semester project. Language not stated (the java2c system is C).
- https://bellard.org/tcc/tccboot.html — TCCBOOT (Oct 2004): TinyCC boot loader that compiles and boots a Linux kernel from source. Strong period page, but Bellard TCC is already covered, so left out to avoid near-duplicates.
- http://www.fpgacpu.org/xsoc/cc.html — Jan Gray XSOC/xr16 (Circuit Cellar 2000), including an lcc 4.1 port to the xr16 RISC. Mostly FPGA hardware; the lcc retarget is one part.
- https://web.eecs.umich.edu/~mahlke/courses/583f07/homeworks.html — EECS 583 Fall 2007 homeworks on the Trimaran (C++) research compiler; dated Sep-Oct 2007. Out of LLVM/GCC scope but may suit a research-compiler batch.
- https://pages.cs.wisc.edu/~fischer/cs701.f07/ — Wisconsin CS701 F05-F07 directories hold SUIF/Mulhern-era back-end projects (proj2-4, asg2.mulhern.html); worth checking for C++ SUIF/MachSUIF assignments.
- https://www.cse.iitb.ac.in/grc/gcc-workshop-09/ — GCC Resource Center 2009 workshop with lab exercises and solutions pages (index.php?page=solution); may contain hands-on GCC 4.x pass and machine-description labs.
- https://www.antlr2.org/doc/cpp-runtime.html — ANTLR 2.7.x C++ target notes ('New as of ANTLR 2.7.2'); the doc index says ANTLR 2.7.5, January 28, 2005, but this page has no date of its own. About 87.
- https://cs.ecu.edu/abrahamsonk/4627/spr05/index.html — ECU CSCI 4627 Spring 2005 course index: five-part C- compiler in C (flex lexer, RD parser, table manager, type checker, abstract-machine codegen with C sources). Could be a sequence entry. The ECU WAF sometimes blocks repeated requests.
- https://www.ndsl.kaist.edu/~kyoungsoo/ee209_2010/assignment/regexp/ — KAIST EE209 2010 regexp assignment in C; host would not resolve from the sandbox
- https://www.boost.org/doc/libs/1_33_1/libs/wave/index.html — Boost.Wave 1.33.1 (2005): C++ preprocessor with re2c/Spirit lexers. Library docs; fits a lexing tile.
- https://www.usna.edu/Users/cs/wcbrown/courses/F09SI413/labs/L08/Lab.html — USNA SI413 Fall 2009 Lab 8: AST interpreter for SPL with flex/bison in C++; labs 3, 6 and 7 cover flex and LR conflicts
- https://www.gnu.org/s/dotgnu/libjit-doc/libjit_3.html — Original DotGNU libjit texinfo manual with tutorials (mul_add, gcd, Fibonacci) in C. gnu.org kept resetting through the proxy, so it was not verified. Check for texi2html dates (c. 2004–2008).
- https://pages.lip6.fr/vvm/projects_realizations/ccg/ccg-1.php — Ian Piumarta's ccg runtime-assembler docs (C preprocessor plus runtime assemblers), early 2000s; connection reset, so it could not be read.
- https://www.st.cs.uni-saarland.de/edu/interpreters08/ivm08.html — Saarland 'Interpreters and Virtual Machines' 2008 course; host blocked by the proxy. It may have C VM or JIT projects.
- https://bluishcoder.co.nz/2007/02/18/dynamic-code-generation-and-image/ — Chris Double, 18 Feb 2007: a C loader that mmaps and relocates generated x86/ARM machine-code images (cegcc, Windows Mobile 5). The assembler half is in JavaScript (Rhino), so around 86.
- https://psyco.sourceforge.net/ — Psyco specializing JIT for Python, written in C; SourceForge-era site with news from 2006–2012 and PEPM'04/ACCU 2004 docs. The reader writes Python, so around 85–86.
- https://harmony.apache.org/subcomponents/drlvm/gc-howto.html — 'How to Write DRL GC': a hands-on C++ tutorial for writing a garbage collector for DRLVM (c. 2006–2007). Belongs to the GC/runtime domain.
- https://harmony.apache.org/subcomponents/drlvm/encoder_library.html — DRLVM IA-32/Intel64 encoder library doc dated January 30, 2007 (C++). Sibling of the accepted Jitrino page.
- https://www.cs.utexas.edu/users/mckinley/380C/labs/labs.html — UT CS 380C Fall 2009 (McKinley): 3-address-to-C translator, dataflow, SSA and register allocation labs. Optimization domain; check the implementation language.
- https://www.cs.mcgill.ca/~nnaeem/520/ — McGill COMP 520 Fall 2005: 'Sept 27, 2005' note that all JOOS deliverables must use the C (A-) implementation; CVS/svn, Sun and FreeBSD machines. Good, but a third semester after c2's 2004 and this batch's 2008.
- https://st.ewi.tudelft.nl/~koen/compilerbouw/2003/practicum.html — TU Delft 2003 Asterix practicum (deadlines 14 April and 26 May 2003, flex/bison/LLgen). Only reachable with WebFetch; curl gets connection resets.
- https://dudka.cz/vyp08 — Kamil Dudka's 2008 VUT Brno VYP course project: a flex/bison compiler and interpreter in C++ with Boost, with source and docs online. Student source project; README says 2008 but it uses CMake. About 86.
- https://dudka.cz/ifj05 — VUT Brno IFJ 2005 team project: a compiler/interpreter for IFJ05 in C, with source browser and docs (Czech). Thin page.
- https://www.complang.tuwien.ac.at/ubvl/skriptum/ — Index of TU Wien Übersetzerbau skripta for every year 2000–2026 (skriptum00..skriptum10 are period). Other agents should not add more years.
- https://www.inf.ufrgs.br/~johann/comp/ — UFRGS Compiladores (Marcelo Johann) staged lex/yacc C compiler. The host resets connections; try again later.
- https://people.cs.nctu.edu.tw/~ypyou/courses/Compiler-s09/ — NCTU Compiler Design Spring 2009 lex/yacc project. The host returned 502; not verified.
- https://www.embecosm.com/appnotes/ean3/embecosm-howto-gdb-porting-ean3-issue-2.html — Embecosm EAN3 'Howto: Porting the GNU Debugger' (Issue 2, Nov 2008), OpenRISC GDB port in C; sibling of accepted EAN4. EAN2 (toolchain install, Nov 2008), EAN6 Verilator SystemC (Feb 2009), EAN1 TLM 2.0 (May 2010) and EAN8 DejaGnu (Apr 2010) are also live under /appnotes/eanN/html/index.html.
- https://dmitrybrant.com/?p=43 — Aug 2003 post: grammar-driven recursive-descent parser in C++ that emits assembly, with source download; small college assignment, about 86.
- http://moxielogic.org/blog/archives.html — Anthony Green's moxie dev blog: dated 2009-2010 posts on a new ISA with GCC/binutils/GDB/QEMU ports ('Moxie GCC port is upstream!', 9 June 2009). Re-rendered with Pelican, and https cert mismatch; short posts.
- https://www.cc65.org/doc/ — Frozen cc65 doc set (index 2005-8-6): internal.txt describes cc65's Small-C-derived code generation (undated), coding.html efficiency hints.
- https://www.boost.org/doc/libs/1_34_0/libs/spirit/index.html — Boost 1.34 (2007) Spirit 1.8 docs with calculator and parser examples in C++; library docs rather than a project.

## Lisp wing (batch 4, October 2026)

- Review drops that could return: Freiburg Informatik I 2008 exercise sheets; TKK Scheme course 2009; Let Over Lambda source file; Brown CS019 2009 seam carving; UT CS381K TMYCIN; UVa CS150 PS5; Sacha Chua BBDB posts; Northwestern EECS 322 Spring 2010 (any language allowed).
- https://websanity.objectcomputing.com — Mark Volkmann "Clojure - Functional Programming for the JVM" (March 2009) lives on this odd subdomain only; decide if acceptable.
- https://www.math.tau.ac.il/~haimk/mavo/ — Tel Aviv Univ 0368.1105 Extended Intro to CS Fall 2000/2001, SICP in Scheme; 10 homework PS files (dvips CreationDate Jan 2001) incl. streams and metacircular evaluator code, but each homework is a 2-page exercise sheet
- https://ocw.mit.edu/courses/6-090-building-programming-experience-a-lead-in-to-6-001-january-iap-2005/pages/assignments/ — MIT 6.090 IAP 2005 Scheme homework (nimrod.scm, advgame.scm); homework-sized
- https://science.slc.edu/jmarshall/courses/2006/spring/cs131/ — Pomona CS131 Spring 2006 Programming Languages via Scheme interpreters (EOPL style); now hosted at slc.edu, frames, Assignments.html not yet checked
- https://people.csail.mit.edu/meyer/6001/ — Albert Meyer 6.001 Spring 2000 directory: m-eval.scm, call-cc.scm, mycompile.ps dated 2000; directory listing only
- https://www.cs.brandeis.edu/~mairson/Courses/cs21b/ — Brandeis COSI 21b SICP course directory: mceval-required.scm (2004), marry.tex (2005), meta-compiler.tex (2005); mixed with 2014-2019 files, no dated project page
- https://www.cs.virginia.edu/~evans/cs200-spring2003/ — Sibling UVa semesters (cs200 Spring 2003/2004, cs150 Fall 2005) have the same SICP-style problem sets; skipped because of the 2-semester cap
- https://courses.cs.washington.edu/courses/cse341/10wi/assignments/scheme-interpreter.pdf — UW CSE341 Winter 2010 Scheme interpreter assignment; PL-course domain
- https://khoury.northeastern.edu/home/lieber/courses/csg111/f07/machprobs/ — Northeastern CSG 111 Fall 2007 (Lieberherr), EOPL3 machine problems with SLLGEN and Scheme interps, but roughly half the MPs are Java/DemeterF; maybe 88
- https://users.cs.utah.edu/~mflatt/past-courses/cs3520/public_html/schedule.html — Utah CS 3520 Fall 2005 PLAI schedule, strong; skipped only to limit Utah/Flatt to two entries. Also CS 6520 S00-S04 archives
- https://cs.brown.edu/courses/cs173/2005/Assignments/index.shtml — Brown CS173 Fall 2005 also live (Laziness, Prolog added); skipped due to 2-semester cap (2003, 2008 taken). 2004, 2007, 2010 also live
- https://www.cse.iitm.ac.in/~krishna/cs3100/a2.html — IIT Madras minischeme interpreter, lazy interpreter and type inference in Scheme; no on-page date
- https://webhome.cs.uvic.ca/~gtzan/csc330/Summer2004/assigns/Assignment3.pdf — UVic CSC330 Summer 2004 interpreters assignment mixing C, Scheme and ML
- https://users.cs.northwestern.edu/~robby/courses/395-495-2009-winter/ — Semantics Engineering with PLT Redex, Winter 2009, model papers in Redex; seminar style
- https://classes.cs.uchicago.edu/archive/2008/autumn/15100-1/ — UChicago classes archive currently serves an expired TLS certificate (and robots-blocks WebFetch); recheck 15100 2006–2010 later
- https://www.ccs.neu.edu/home/dvanhorn/csu211.2007.fa/Assignments/X1.html — Optional Set X1: extend meta-circular evaluator with cond and lazy evaluation (thunks), Fall 2007; same semester as accepted Tetris set
- https://www.ccs.neu.edu/home/dvanhorn/csu211.2007.fa/Assignments/7.html — Snake game with world.ss, Fall 2007, same semester as accepted Tetris set
- https://users.cs.utah.edu/~mflatt/past-courses/cs2010/public_html/f03/hw6.html — UFO shooting game with draw.ss teachpack, due Sept 30 2003; spec lives on an external HtDP page
- https://my.eng.utah.edu/~cs1410-20/f10/hw6.html — Simple Tetris from HtDP/2e with 2htdp/image, Oct 2010; very short page
- https://cs.brown.edu/courses/cs019/2009/assignments/circuits — Circuit-board connectivity analysis on images (circuit-teach.ss), Fall 2009; fourth CS019 2009 project
- https://cs.brown.edu/courses/cs019/2010/assignments — CS019 Fall 2010 (DrRacket) has same project set plus Oracle/Parallelism; a second semester if needed
- https://users.cs.northwestern.edu/~jesse/course/cs2500-sp10/ — Jesse Tov NEU CS 2500 Spring 2010 (PLT Scheme 4.2.3), moved from ccs.neu.edu to Northwestern; 12 assignments, not checked in depth
- https://www.ccs.neu.edu/home/jpalm/211-s05/ — CSU 211 Spring 2005 with Assignments/13.html and a DrScheme gallery project; third CSU 211 semester so held back
- https://users.cs.northwestern.edu/~robby/uc-courses/15100-2005-fall/ — Further Findler 15100 semesters 2003–2006 in the same archive
- https://courses.cs.umbc.edu/undergraduate/471/fall09/hw/hw4.html — UMBC 471 Fall 2009 WalkSAT in Lisp (stubs provided), out 10/15/09. Good, held back for 2-semester cap (Fall 2004 accepted).
- https://courses.cs.umbc.edu/undergraduate/471/fall02/hw/hw3.html — UMBC 471 Fall 2002 BFS/greedy/A* Romania search in CLISP. Third UMBC semester; cap.
- https://www.cs.utexas.edu/~mooney/cs351/hw4.html — Mooney CS 351 Spring 2000 HW4: extending Norvig's Prolog interpreter in Lisp (due April 25, 2000). Also hw3 Robosurfer heuristic web search, hw5 NL grammar.
- https://www.d.umn.edu/~rmaclin/cs5541/Programs/04.html — UMN Duluth CS 5541 Fall 2010 Program 4: reinforcement learning maze in Lisp (prog4.lisp); 01 minimax tic-tac-toe.
- https://www.cs.hmc.edu/courses/2000/spring/cs151/assignment3.html — HMC CS 151 Spring 2000 (Fleck) resolution theorem prover in Scheme; page title says 'Fall 1998' but index is Spring 2000; due 'Thursday, 2 March'. Score ~92.
- https://people.cs.georgetown.edu/~maloof/cosc387.f04/p2.html — Georgetown COSC 387 Fall 2004 Project 2: BFS/informed/A* on French city graph in Lisp (gcl/clisp/cmucl); p3 propositional resolution. Score ~92.
- https://www2.cs.sfu.ca/CourseCentral/310/pwfong/Assignments/ — SFU CMPT 310 (Fong) four cumulative Common Lisp assignments ending in a mechanical planner, Allegro CL 4.3/6.0; date only via outline URL 2001-1. Score ~90-91.
- https://userpages.cs.umbc.edu/ypeng/AICourseOld/project3.PDF — UMBC 471/671 Fall 2000 (Peng) resolution step with unification; 'Lisp is strongly recommended' but not required.
- https://people.eecs.berkeley.edu/~russell/classes/cs289/f04/assignments/a2.html — Berkeley CS 289 Fall 2004 SAT-based STRIPS planning; 'I recommend using LISP' with Lisp DPLL code; Lisp optional.
- https://www.eecis.udel.edu/~decker/courses/681s07/prog3-2007.pdf — Delaware CISC 481/681 Spring 2007 decision-tree learner; Lisp suggested but not required.
- http://landoflisp.com/source.html — Land of Lisp (2010) source listing: Wumpus, Orc Battle, Dice of Doom v1-v4, a web server, SVG DSL. No on-page date (only HTTP Last-Modified Nov 2010; the homepage links a /10/11/03/ Slashdot review). HTTPS cert is self-signed, so HTTP only. Would be about 89.
- https://nklein.com/2009/10/dsl-for-drawing-floor-plans/ — October 28th, 2009, Common Lisp floor-plan DSL on Vecto with code. Good, but the nklein.com cap of 2 was used up.
- https://www.newartisans.com/2007/11/a-quick-hunchentoot-primer/ — November 6, 2007, short Hunchentoot/CL-WHO define-easy-handler primer. Small companion to the accepted Apache post.
- https://paulgraham.com/rootsoflisp.html — "May 2001": McCarthy eval in Common Lisp. The HTML page is only an intro; the paper (PS) and jmc.lisp are now on a turbifycdn.com CDN.
- https://gsharp.common-lisp.dev/ — Gsharp score editor in CL/McCLIM, release 0.2 dated 2003-09-06, page signed 2010-03-27. Would be the 2nd common-lisp.dev record; note common-lisp.net now redirects to common-lisp.dev.
- https://frank-buss.de/lisp/aqueduct.html — Aqueduct puzzle game in LispWorks CAPI, news dated February-May 2005. Frank Buss cap reached; Sudoku solver (Feb 2006) and Functional Texture (Mar 2005) are also on that site.
- https://defmacro.org/ramblings/lisp.html — The Nature of Lisp, Monday, May 8, 2006. Conceptual essay (Ant/XML to Lisp), not a project.
- https://cliki.net/LispGameDesignChallenge-spring-2010 — Dated CLiki list of 2010 Lisp game jam entries. A directory to mine for more game projects.
- http://www.larcenists.org/twobit.html — Twobit compiler design notes (pass1..pass6, MacScheme machine page 'Last updated 27 October 2002'); index updated 2015, descriptive rather than a build project
- http://www-sop.inria.fr/indes/scheme2js/ — Scheme2Js Scheme-to-JavaScript compiler in Bigloo; ICFP 2006 / TFP 2007 / Scheme Workshop 2007 papers, but page last updated 2011
- https://www.iro.umontreal.ca/~feeley/cours/ift2030-old/ — Feeley IFT2030 Hiver 2006 PL course: TP1 functional drawing library in Scheme (02/02/06); TP2 is Prolog. For PL/intro domain
- https://users.cs.northwestern.edu/~robby/uc-courses/ — Robby Findler UChicago CMSC 15100 2003-2008 (HtDP intro) archives; 22001 Software Construction game projects
- https://www.cs.utah.edu/~mflatt/courses.html — Flatt CS 6510 S08 / CS 7963 S05 Practical Functional Programming (PLT Scheme games); CS 6520 S00-S04
- https://www.iro.umontreal.ca/~feeley/ — Feeley papers on PICOBIT (IFL 2009) and BIT (HOSC 2005) Scheme compilers for microcontrollers, PDFs only
- https://www.scheme.com/tspl4/ — The Scheme Programming Language 4th ed. (2009) online, for Tutorials & Books
- https://websanity.objectcomputing.com/resources/publications/sett/march-2009-clojure-functional-programming-for-the-jvm/ — Volkmann's 'Clojure - Functional Programming for the JVM' (March 2009) is live, but only on an odd 'websanity' subdomain; main objectcomputing.com path 404s. Strong content if the host is acceptable (~92).
- http://www.jefferypsanders.com/autolisptut.html — Jeffery P. Sanders AutoLisp tutorial and AutoLISP games (autolisp_games.html); behind a bot-verification loader for curl. Programs say 'tested in Release 14 thru 2004', footer 'Copyright 2002-2016'. Check in a browser.
- https://www.afralisp.net/visual-lisp/tutorials/reactors-part-1.php — AfraLISP Visual LISP reactors series, substantial but no on-page date; afralisp.net already used twice
- http://blog.fogus.me/2010/05/25/trammel-contracts-programming-for-clojure.html — Trammel design-by-contract library for Clojure, May 2010 (URL date); fogus has only one record so a second is allowed
- https://stuartsierra.com/2009/10/08/generating-clojure-from-an-ontology/ — Oct 2009 Clojure code generation post, not checked in depth
- https://data-sorcery.org/2009/08/30/processing-intro/ — Incanter.processing visualizations in Clojure, 30 Aug 2009; site cap reached
- https://rebelsky.cs.grinnell.edu/Courses/CS151/2007S/Projects/report.01.html — Grinnell CSC151 Spring 2007 Project One: random rhyming or story text generation in Scheme ("Assigned: Monday, March 5, 2007", "Due: Friday, March 16, 2007"). Solid at about 91 but left out to respect the two-semesters-per-course limit (2001S and 2007F accepted).
- https://www.cs.swarthmore.edu/~richardw/classes/cs37/s08/ — Swarthmore CS37 Spring 2008 SICP (Wicentowski), DrScheme. Probably has a similar interpreter project; not checked, and the course is already covered by S06.
- https://people.cs.aau.dk/~normark/prog3-03/html/notes/theme-index.html — Aalborg, Kurt Nørmark, 'Functional Programming in Scheme, With Web Programming Examples': a substantial online book (prog3-03 = 2003) but the page says 'Generated: Friday January 3, 2014'. Needs a check for an original 2003 date.
- https://proglang.informatik.uni-freiburg.de/teaching/info1/2009/uebungen.html — Freiburg Informatik I WS 2009/10: DrScheme sheets with world/turtle and priority-queue ADT tasks. Second semester of the same course as the accepted 2008 entry.
- https://www-ppti.ufr-info-p6.jussieu.fr/cederoms/VideoScm2005/ — UPMC LI101 2005–2006 CD-ROM, a near-duplicate of the accepted 2006 one. Also VideoScm2002/2001 (DEUG MIAS) on the same index.
- https://www.cs.hmc.edu/courses/2003/spring/cs131/assignments/5.pdf — HMC CS131 Spring 2003 PL assignment, seen in search results; language not checked.
- https://faculty.hampshire.edu/lspector/courses/cs263s01.html — Hampshire CS263 Spring 2001 Common Lisp AI ('last updated on January 29, 2001'): resource page with live Lisp code (genetic-salesman.lisp, grid2d.lisp) and a portfolio requirement but no concrete assignment handouts. Also rejected by the d4 agent, so not accepted.

## Known dead ends (as of October 2026)

Do not spend searches here unless something has changed:

- `cs.umd.edu/class/*/cmsc412` pages for 2004–2008 return 403 (the `~hollings` archive works).
- UNSW COMP3231 OS/161 pages 2004–2009 return 403.
- UW CSE451 / CSE461 and Berkeley `inst.eecs` CS162 / CS186 / EE122 sit behind logins.
- Harvard CS161: only recent offerings are live.
- Yale CS422 course site returns 403 (a mirror exists on homes.cs.washington.edu/~arvind).
- NYU Gottlieb linker labs: course indexes 2000–2009 load but every lab file is 404.
- CMU 18-349 Fall 2008 ARM labs: index loads, handouts are 404.
- CMU 15-441 Fall 2008 and UMD CMSC417 Spring 2010 return 403.
- Stanford CS346 RedBase: only 2013+ offerings survive (out of period).
- JamesM kernel tutorials (503) and BrokenThorn OS dev series (403) could not be verified.
- flipcode "Implementing A Scripting Engine" and "Network Game Programming" (1999): just before the window.
- KFUPM SIC/XE assembler and linking loader: dated 1998, out of range.
- epaperpress.com Lex & Yacc tutorial: PDF rebuilt in 2020.
- gamedev.net / archive.gamedev.net articles: Cloudflare 403 from the sandbox. drdobbs.com unreachable through the proxy.
- USC CS530/531, WPI CS4513 (Claypool), UW CSE490G/CSE303/CSE466, Calgary CPSC599.49: 401/403 or login.
- Berkeley CS267, UIUC ECE498AL / CS420, Cornell CS5220: no surviving 2000s assignment pages found.
- UIUC ECE391 old terms show a placeholder; CMU 18-348 and Georgia Tech ECE4180 only have modern versions.
- Cal Poly CPE357 and UTK CS360: TLS certificate errors through the proxy (unverified, not dead).
- Dipperstein compression pages gone; arturocampos.com is now spam; Charles Bloom source pages stop in 1999.
- Wisconsin CS640 Fall 2006 assignment PDFs: 404.
- University GC/VM courses in C are scarce: Rose-Hulman (Java), Brown (Scheme), Princeton/HMC (SML); Tufts, Arizona, KAIST gone.
- Compilers: UC Davis ECS142 2003/2005 folders 403; Berkeley CS164 2000–2006 CalNet; UIUC CS426 old terms redirect to current; UW CSE401 PL/0 login; Arizona CSc453, Dartmouth CS57, Calgary CPSC411 403; Alberta CMPUT415 404.
- Compilers: Rutgers 415, Rice COMP412/512, FSU, Alberta Pro64, Edinburgh 2000s archives dead; lcc site redirects to a Google login; pcc site 503; CodeProject articles now redirect to a placeholder.
- gnu.org / ftp.gnu.org (flex, bison, lightning, libjit manuals) and lip6.fr did not respond through the proxy in batch 3. Retry later.
- Appel "Modern Compiler Implementation in C" site is dated 1997 (out of range).
- Lisp: Berkeley CS61A Scheme-era pages need CalNet; Brian Harvey ~bh/61a-pages have no on-page dates (uploaded 2020); sicp.csail.mit.edu gone; web.mit.edu/6.001 stub.
- Lisp: Indiana C311/B521/P423 and Ghuloum pages redirect to the IU front page; Northeastern Wand/Felleisen course pages 404; Rice COMP 210 gone; Waterloo CS135 2008–2010 gone.
- Lisp: weitz.de library pages now redirect to edicl.github.io (fails original-site rule); Matt Might articles show no period date; Feeley 90-minute Scheme->C 404; Ikarus domain parked.
- Lisp: UChicago classes archive had an expired TLS certificate (Oct 2026); Grinnell and some hosts reset curl through the proxy but load in WebFetch.
