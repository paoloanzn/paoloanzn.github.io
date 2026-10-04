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
