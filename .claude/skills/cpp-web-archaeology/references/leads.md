# Leads for future batches

Pages found in earlier batches that were not added yet. Check them first when your domain matches.
Remove a lead from this file when it is added to the catalog or confirmed dead. Add new leads from each batch
(merge_batch.py prints them; its report JSON lists them under `leads`).

Status words: **candidate** = likely acceptable; **sibling** = another semester of a course already in the catalog (add only if clearly stronger or different); **check** = needs a date or language check.

## Operating system kernels

- https://users.cs.duke.edu/~chase/nachos-guide/guide/nachos.htm — Jeff Chase's Duke Nachos Project Guide (C++, Solaris SPARC, nachos-3.4); widely linked c. 2001-2005 but no explicit date on page
- https://courses.cs.vt.edu/~cs3204/fall2009/pintos-vt-local/projects.html — VT CS3204 Fall 2009 Pintos with dated deadlines; skipped as near-duplicate of covered spring2008
- https://www.cs.princeton.edu/courses/archive/fall06/cos318/projects/5.html — Princeton COS318 Fall 2006 Project 5 demand-paged VM on a USB disk; strong, could be added
- https://www.cs.cmu.edu/~410-s07/projects.html — CMU 15-410 Spring 2007 sibling semester; also ~410-f05, ~410-f08 load
- https://www.khoury.northeastern.edu/~amislove/teaching/cs5600/fall10 — Northeastern CS5600 Fall 2010 Pintos; at the end of the period
- https://www.cs.rochester.edu/~kshen/csc256-spring2007/assignments/xen-programming5.html — Rochester 2007 Xen/Linux kernel CPU scheduling track (Linux kernel C)
- https://classes.cs.uchicago.edu/archive/2001/winter/CS230/ — UChicago Yalnix Winter 2001 sibling offering
- https://student.cs.uwaterloo.ca/~cs350/common/nachos.html — Waterloo Nachos install/debug guides, undated

## Filesystems, concurrency, memory

- https://www.cs.cmu.edu/~410-f03/p2/ — 15-410 has live dirs for every term f03 to f10 (thr_lib.pdf, proj2.tar.gz, kernel specs, P3 kernel handouts). Other agents could catalog the P3 Pebbles kernel and P1 handouts.
- https://cseweb.ucsd.edu/classes/wi05/cse121/project2.html — UCSD Winter 2005 application-level file system over dread/dwrite with disk.h/disk.c/driver.c skeleton; strong sibling of the accepted P1
- https://people.cs.pitt.edu/~jmisurda/teaching/cs1550/2081/cs1550-2081-project2.htm — Pitt Fall 2007 pthreads flagperson/one-lane traffic synchronization project; the 2077-2111 dirs are all live (syscall semaphore and VM simulator projects too)
- https://www.cs.columbia.edu/~nieh/teaching/w4118_f07/homeworks/hmwk5.html — Fall 2007 Linux 2.6.18.8 modified-set tracking through page-table write protection; strong kernel memory project
- https://www.cs.columbia.edu/~nieh/teaching/w4118_f08/homeworks/hmwk3.html — Fall 2008 Linux 2.6.11 SThreads locking primitives with test_and_set
- https://www.cs.umd.edu/~hollings/cs412/s04/proj5/index.html — GeekOS GOSFS file system (Spring 2004, Bochs, due April 27 2004). Live, but the catalog already has hollings s02/s03 so it may be a near-duplicate
- https://pages.cs.wisc.edu/~remzi/Classes/537/Spring2010/Projects/p4.html — Spring 2010 spin locks with x86 xchg vs pthread locks, with concurrent counter/list/hash
- https://pages.cs.wisc.edu/~remzi/Classes/537/Fall2008/Projects/p5.html — Fall 2008 user-level thread library (userthread.h, locks/CVs). Near-duplicate of the accepted Fall 2005 P3
- https://courses.umbc.edu/undergraduate/421/spring06/Project3.pdf — UMBC CMSC421 Spring 2006 simulated file system in a Diskfile (C/C++, gcc/g++ -ansi on GL Linux)
- https://courses.cs.vt.edu/~cs3204/fall2006/gback/project0.html — VT CS3204 Fall 2006 Pintos Project 0 first-fit user-level allocator built on Pintos lists
- https://www.cse.unr.edu/~sushil/class/os/assignments/s04/as3/ — UNR Spring 2004 producer/consumer and readers/writers with pthreads/semaphores (Sun and Linux samples, last modified Feb 23 2004); small scope
- https://www.cs.montana.edu/courses/fall2005/418/assign2.pdf — Montana Fall 2005 pthreads producer/consumer on a protected doubly linked list; small scope
- https://imada.sdu.dk/u/daniel/DM510-2010/assignment2/assign-2010-2.html — SDU Spring 2010 Linux 2.6 char-device kernel module (scull-based, kernel 2.6.28/2.6.32)
- https://homes.cs.washington.edu/~arvind/cs422/assignments/as4.html — Yale CS422 Nachos FS assignment (due April 26, Monday); no year on page, but the weekday fits 2004
- https://www.cs.usfca.edu/~cruse/cs635/ — USF CS635 Fall 2007 advanced systems programming (Linux 2.6.22 modules, ext2, device drivers) with many .c/.cpp demos; course page rather than projects

## Compilers

- https://www.cs.utexas.edu/users/mckinley/380C/labs/lab4.html — UT CS380C Fall 2009 (McKinley): 3-addr-to-C translator, dataflow, SSA and PowerPC register allocation, with a C-subset compiler (csc, C source, 2007-2009 tarball). Students may use any language, so it was left out; strong otherwise.
- https://www.cs.cmu.edu/afs/cs/academic/class/15745-s07/www/assignments/0/assign0.html — CMU 15-745 Spring 2007 CASH compiler setup (RH 9 machines, CVS). Assignments 1-2 (CCP/ADCE on Pegasus, cluster scheduling) could be added as more entries.
- https://www.cs.cmu.edu/afs/cs/academic/class/15745-s02/www/suif.htm — CMU 15-745 Spring 2002 Machine SUIF environment page; assignment pages from that semester not checked yet.
- https://web.stanford.edu/class/archive/cs/cs143/cs143.1102/materials/handouts/PA4.pdf — Stanford CS143 Fall 2009 Cool code generator (C++, /usr/class/cs143). Not added to avoid too many Stanford entries; also cs143.1052 and cs143.1072 have full handout sets.
- https://www.cs.unh.edu/~pjh/courses/cs712/2005/ — UNH CS712 2004-2006 offerings: students design their own OO language and compile it to IA-32 with lex/yacc. Phase pages not checked yet.
- https://www.cs.csustan.edu/~mmartin/teaching/CS4300F07/CS4300_F07_Project.pdf — Same C++-subset project for Fall 2007; near-duplicate of the F06 entry.
- https://compilers.iecc.com/comparch/article/05-01-082 — Jan 2005 comp.compilers post announcing TinC, a C port of Crenshaw's Tiny (DJGPP/Red Hat 9). The home.comcast.net download link is dead.

## Interpreters, VMs, assemblers, simulators, emulators

- https://www.piumarta.com/software/lysp/ — Ian Piumarta's LYSP tiny Lisp interpreter + GC in C (Lisp's 50th anniversary, ~2008); server reset connections, so I could not confirm the date
- http://www.codeslinger.co.uk/pages/projects/chip8.html — C++ CHIP-8/Game Boy emulator tutorials, footer 'Copyright 2008', but the site was restored in 2014; https cert is broken
- https://courses.grainger.illinois.edu/ece511/Fa2003/homework/ece412-sim.html — UIUC ECE 412 Fall 2003 simulator tarball quickstart; need to confirm it is a C simulator students modify
- https://users.ece.utexas.edu/~patt/03s.360N/labs/lab4.html — UT EE360N Spring 2003 pipelined LC-3b lab (due 2 May 2003); 03f, 04f, 07s and 09s offerings are also live and could be added as sibling semesters
- https://www.iecc.com/linker/ — John Levine's Linkers and Loaders manuscript chapters (~1999-2000); reference text with no build project
- https://www.airs.com/blog/archives/38 — Ian Lance Taylor's 'Linkers' blog series, August 2007 (gold linker); essays, not a C project
- https://www.usenix.org/legacy/event/usenix05/tech/freenix/full_papers/bellard/bellard_html/index.html — QEMU dynamic translator paper, USENIX 2005; emulator internals, but a paper
- https://tinyscheme.sourceforge.net/home.html — TinyScheme SourceForge home page; no dates visible on the page
- https://www.cs.colostate.edu/~cs270/.Fall08/Programs/PA3.html — CSU CS270 Fall 2008 LC-3 simulator in C (PA3), sibling of the accepted PA4
- https://acg.cis.upenn.edu/milom/cse240-Fall06/handouts/hw8 — UPenn CSE240 Fall 2006 LC-3 disassembler in C (sibling of hw9)
- https://www.cs.cmu.edu/afs/cs/academic/class/15213-f02/www/labs.html — CMU 15-213 Fall 2002 lab index; not my domain, but the f02/s03/f03/s04 offerings are live for other agents

## Networking and distributed systems

- https://pdos.csail.mit.edu/6.824-2004/labs/tcpproxy.html — 2004 libasync TCP proxy in C++ (tcpproxy.C); header oddly says 'Fall 2004' but due Feb 26. Sibling labs webproxy2.html and fs-lab-1/2 are also live.
- https://pdos.csail.mit.edu/6.824-2007/labs/lab-7.html — Fall 2007 replicated state machine lab (C++, dated RCS header); strong if more 6.824 entries are wanted. 2005/2006/2007 lab indexes are all live.
- https://www.scs.stanford.edu/07wi-cs244b/lab1.html — Stanford CS244B Winter 2007 Sun RPC lab (rpcgen + g++ output shown, lab1.tar.gz); lab2 is an event-driven replicated file store. Dates only via URL and sibling pages.
- https://www.cl.cam.ac.uk/teaching/0910/P33/sw/dynamic-routing-pwospf/ — Cambridge P33 2009-10 PWOSPF on VNS/NetFPGA, last modified 2009-10-24; C files (sr_integration.c) named on the basic-router sibling page.
- https://sites.cc.gatech.edu/classes/AY2010/cs4210_fall/Project3.pdf — Georgia Tech CS4210 Fall 2009 distributed proxy server using Sun RPC (due 11/30/2009); Project1 is a pthreads web server and Project2 a shared-memory proxy.
- https://sites.cc.gatech.edu/fac/Russell.Clark/Classes/06/3251-spring/sockets2.html — Georgia Tech CS3251 Spring 2006 selective-repeat ARQ file transfer in C or C++ on Solaris/Linux (-lsocket -lnsl). Good candidate, around score 92.
- https://math.hws.edu/eck/cs441/f02/lab4.html — HWS CPSC441 Fall 2002 web server labs in C++ with an instructor Socket class (threaded_chat.cc in an open directory listing).
- https://www.cs.cornell.edu/courses/cs414/2005sp/cs415/project4.html — Cornell 2005sp minithreads reliable networking and ad-hoc routing (project5); not yet in catalog but close to existing cs414 entries.
- https://pages.cs.wisc.edu/~akella/CS640/F06/work.html — Wisconsin CS640 Fall 2006: mock name server, distance vector and e-CHIMP chat protocol (echimp-rfc.txt); directory listing dated 2006.
- https://www.cs.princeton.edu/courses/archive/spr08/cos461/simple_tcp.html — COS461 Spring 2008 STCP plus web_proxy (ANSI C) and router pages; spr07 and spr09 variants are also live.

## Database internals

- https://www.cs.cornell.edu/courses/cs432/2002fa/assignments/a6/description.htm — Fall 2002 rerun of the ARIES recovery assignment (deadline Dec 9); duplicate of the accepted 2001 page, so left out
- https://www.cs.cornell.edu/courses/cs432/2002fa/assignments/a1/description.htm — Fall 2002 Minibase buffer manager shipped as a Visual Studio .NET project; a3/a4 (B+ tree, joins) are at description.html
- https://www.dbai.tuwien.ac.at/staff/wei/teaching/ads0708/projects/project1/index.html — TU Wien WS 2007/08 PostgreSQL 8.0.3 CLOCK buffer manager in C, adapted from Berkeley CS186; good but derivative
- https://www.cs.iusb.edu/minidb/2_assignments/ — IU South Bend MiniDB C++ engine assignments (PDFs dated Aug 2010, tech report 2007); a Windows C++ teaching DB engine
- https://users.cs.northwestern.edu/~pdinda/db-f06/projectc.pdf — Fall 2006 and 2007 versions of the Northwestern BTree project also live (db-f07/projectc.pdf); host sometimes resets connections
- https://www.cs.ucdavis.edu/~green/courses/ecs165b-s10/indexManager.html — Individual DavisDB B+ tree part (due 5/2/2010) if separate component entries are wanted
- https://www.cs.cornell.edu/courses/cs432/2001fa/a1/index.htm — Fall 2001 Minibase buffer manager (bufmgr.cpp, Visual C++); buffer manager is already well covered

## Unix tools, compression, drivers, embedded

- https://www.cs.usfca.edu/~cruse/ — Allan Cruse's home page links dated course archives (cs210f03–s09, cs630s04/f06/f08, cs635s03/s05/f07, cs686f03/f05/s05/s07/s08). These hold bootloaders, a mini OS (os630.s), SVGA/Radeon programming, RTL8139 NIC drivers and VMX kernel modules. Most are x86 assembly or graphics, but more C driver projects could be catalogued.
- https://www.cs.usfca.edu/~cruse/cs635s05/proj2s05.635 — May 2005 'nicchat.cpp' over a custom RealTek 8139 character driver. Good for a networking/driver agent.
- https://people.ece.cornell.edu/land/courses/ece4760/labs/s2004/lab1.html — Every year from s1999 to s2012 holds an intact AVR lab set. Individual labs (DTMF/DDS synthesis, TV video game) could be added.
- https://forum.cone.informatik.uni-freiburg.de/teaching/labcourse/Adhocnetworks-w07/manet-assignment.html — Winter 2007/08 Gumstix ad-hoc networking lab with dated tasks (cross-compiling, U-Boot reflashing). Mostly written questions rather than a C build, but authentic Gumstix-era material.
- https://courses.cs.umbc.edu/undergraduate/421/spring02/burt/projects/project1.html — March 2002 UMBC CMSC421 project: add a system call to a Red Hat-era kernel (ksyms.c, EXPORT_SYMBOL). Better fit for the OS agent.
- https://courses.cs.duke.edu/fall01/cps100/assign/huff/ — Earlier Fall 2001 version of the Duke Huffman assignment. Only one semester accepted to avoid near-duplicates.
- https://www.classes.cs.uchicago.edu/archive/2007/fall/51081-1/labs/LAB2/lab2.html — Same Fall 2007 course: regex/grep/awk lab. LAB4 (fork/exec/pipes) and LAB5 (SysV IPC) are also intact.

## Hobbyist and community sites

- http://www.kegel.com/c10k.html — C10K survey; strong 1999–2003 content (select/poll/epoll/kqueue, sendfile) but continuously updated to 2018 and not a project
- http://www.codeslinger.co.uk/pages/projects/gameboy.html — C++ Game Boy emulator tutorial with source (Visual Studio/Code::Blocks); no date visible on page, likely ~2008–2010
- https://dunkels.com/adam/pt/ — Protothreads (C, 2005–2006) — subpages blocked by WAF (466), date not visible on main page
- http://www.osdever.net/tutorials/ — Bona Fide index, all dated Jul 2003: Spinlocks I–III (Rieker), Implementing Basic Paging, Multitasking Howto, Software Task Switching, Writing a Kernel in C (Robinson)
- https://www.hboehm.info/gc/gcdescr.html — Boehm conservative GC algorithm overview (C); strong topic but no explicit in-window date on page
- https://flipcode.com/archives/Network_Game_Programming-Issue_01_Things_that_make_you_go_hmm.shtml — Winsock C++ network game series, June–Aug 1999 — just before window

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
