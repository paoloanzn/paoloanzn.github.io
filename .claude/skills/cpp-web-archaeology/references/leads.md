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
