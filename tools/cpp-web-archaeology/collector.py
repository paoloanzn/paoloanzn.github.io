#!/usr/bin/env python3
import argparse, hashlib, itertools, json, os, re, time
from pathlib import Path
from urllib.parse import urlparse, urlsplit, urlunsplit, parse_qsl, urlencode
import requests
from bs4 import BeautifulSoup

YEARS=list(range(2000,2011))
LANGS=["C","C++"]
TOPICS=["Win32","MFC","Winsock","DirectX 8","DirectX 9","Direct3D 8","Direct3D 9","OpenGL","GLUT","SDL 1.2","Allegro","ncurses","sockets","HTTP server","FTP client","Unix shell","ray tracer","rasterizer","image processing","game engine","tile engine","particle engine","compiler","interpreter","operating system","kernel","filesystem","threads","pthreads","network server","OpenAL","FMOD"]
MARKERS=["Visual C++ 6.0","VC6",".dsp",".dsw","Visual Studio .NET 2003","Dev-C++","Borland C++","DJGPP","RHIDE","Windows 2000","Windows XP","Fedora Core 3","gcc 3","CVS","SourceForge"]
SITES=["site:edu","site:ac.uk","site:edu.au","site:sourceforge.net","site:codeproject.com","site:gamedev.net","site:flipcode.com","site:geocities.ws"]
REJECT={"github.com","gitlab.com","medium.com","dev.to","reddit.com","web.archive.org","archive.org"}
UA="CppWebArchaeology/1.0 (+https://paoloanzn.github.io/cpp-web-archaeology/)"

def q(s): return f'"{s}"' if (" " in s or "." in s) else s
def queries():
    out=[]; seen=set()
    def add(x,f):
        x=" ".join(x.split())
        if x not in seen: seen.add(x); out.append({"query":x,"family":f})
    for y,l,t in itertools.product(YEARS,LANGS,["tutorial","project","programming assignment","lab"]):
        add(f'{q(l)} {q(t)} "{y}"',"date+intent")
        add(f'{q(l)} {q(t)} "last updated" {y}',"last-updated")
    for y,l,t in itertools.product(YEARS,LANGS,TOPICS):
        add(f'inurl:{y} {q(l)} {q(t)} project',"year-url")
        add(f'site:edu inurl:{y} {q(l)} {q(t)} assignment',"university-year-url")
    for m,l,t in itertools.product(MARKERS,LANGS,TOPICS):
        add(f'{q(m)} {q(l)} {q(t)} tutorial',"toolchain")
        add(f'{q(m)} {q(l)} {q(t)} project',"toolchain-project")
    for s,l,t in itertools.product(SITES,LANGS,TOPICS):
        add(f'{s} {q(l)} {q(t)} tutorial',"site-family")
    return out

def search(query,count,provider):
    if provider=="brave":
        r=requests.get("https://api.search.brave.com/res/v1/web/search",params={"q":query,"count":count},headers={"Accept":"application/json","X-Subscription-Token":os.environ["BRAVE_SEARCH_API_KEY"],"User-Agent":UA},timeout=20)
        r.raise_for_status()
        return [{"title":x.get("title",""),"url":x.get("url",""),"snippet":x.get("description","")} for x in r.json().get("web",{}).get("results",[])]
    r=requests.post("https://google.serper.dev/search",json={"q":query,"num":count},headers={"X-API-KEY":os.environ["SERPER_API_KEY"],"Content-Type":"application/json"},timeout=20)
    r.raise_for_status()
    return [{"title":x.get("title",""),"url":x.get("link",""),"snippet":x.get("snippet","")} for x in r.json().get("organic",[])]

def fetch(url):
    try:
        r=requests.get(url,headers={"User-Agent":UA},timeout=20,allow_redirects=True)
        if r.status_code>=400 or "text/html" not in r.headers.get("content-type","").lower(): return None
        soup=BeautifulSoup(r.text,"html.parser")
        for t in soup(["script","style","noscript"]): t.decompose()
        return r.url,(soup.title.get_text(" ",strip=True) if soup.title else ""),soup.get_text(" ",strip=True)[:180000]
    except requests.RequestException: return None

def score(url,text):
    s=0; ev=[]; corpus=text.lower()
    years=[int(x) for x in re.findall(r'\b(20(?:0\d|10))\b',corpus+" "+url)]
    if years: s+=18; ev.append(f"period year evidence: {min(years)}")
    if re.search(r'/(?:200[0-9]|2010)(?:/|\b)|(?:spring|fall|winter|summer)[-_]?(?:0[0-9]|10)',url.lower()):
        s+=12; ev.append("period-coded URL")
    host=urlparse(url).hostname or ""
    if host.endswith(".edu") or host.endswith(".ac.uk"): s+=5; ev.append("academic host")
    tests=[(r'visual c\+\+ 6\.0|\bvc6\b|\.dsp\b|\.dsw\b',12),(r'dev-c\+\+|borland c\+\+|djgpp|rhide',8),(r'sdl\s*1\.2|allegro\s*4|directx\s*[789]|opengl\s*[12]\.|glut',7),(r'win32|mfc|winsock|ncurses|pthread',5),(r'\b(project|assignment|lab|tutorial|source code|starter code|skeleton code)\b',5),(r'\b(ray trac|shell|http server|ftp client|game engine|rasterizer|filesystem|kernel)\b',5)]
    for pat,pts in tests:
        if re.search(pat,corpus,re.I): s+=pts; ev.append(pat)
    if re.search(r'c\+\+\s*(11|14|17|20|23|26)|visual studio code|\bvscode\b',corpus,re.I): s-=18
    if re.search(r'\b(write|build|implement|create|develop)\b.{0,45}\b(program|application|server|client|shell|game|engine|ray tracer|operating system)\b',corpus,re.I|re.S):
        s+=9; ev.append("project-build language")
    return max(0,min(100,s)),ev,(min(years) if years else None)

def canon(u):
    s=urlsplit(u); q=urlencode([(k,v) for k,v in parse_qsl(s.query,keep_blank_values=True) if not k.lower().startswith("utm_")])
    return urlunsplit((s.scheme.lower(),s.netloc.lower().removeprefix("www."),re.sub(r'/+$','',s.path) or "/",q,""))

def classify(text):
    t=text.lower()
    rules=[("Operating Systems / Kernels",["kernel","operating system","filesystem"]),("Networking / Sockets",["socket","winsock","http server","ftp","tcp","udp"]),("Graphics / Ray Tracing",["ray trac"]),("Graphics / OpenGL",["opengl","glut","glsl"]),("Games / SDL",["sdl"]),("Games / Allegro",["allegro"]),("Windows / Win32",["win32","visual c++","mfc"]),("Unix / Systems",["shell","ncurses","pthread","unix"]),("Compilers / Languages",["compiler","parser","interpreter"])]
    for c,keys in rules:
        if any(k in t for k in keys): return c
    return "C/C++ Projects"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--provider",choices=["brave","serper"],required=True)
    ap.add_argument("--queries",type=int,default=750)
    ap.add_argument("--offset",type=int,default=0)
    ap.add_argument("--results",type=int,default=10)
    ap.add_argument("--seed",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    qs=queries(); chosen=[qs[(a.offset+i)%len(qs)] for i in range(min(a.queries,len(qs)))]
    seed=json.loads(Path(a.seed).read_text()); known={canon(x["url"]) for x in seed}; seen=set(); added=0
    for qi,row in enumerate(chosen,1):
        try: hits=search(row["query"],a.results,a.provider)
        except Exception as e: print("search error",qi,e); continue
        for hit in hits:
            url=hit["url"].split("#")[0]; host=(urlparse(url).hostname or "").lower().removeprefix("www.")
            if host in REJECT or not url.startswith(("http://","https://")): continue
            h=hashlib.sha1(url.encode()).hexdigest()
            if h in seen: continue
            seen.add(h); page=fetch(url)
            if not page: continue
            final,title,body=page; s,ev,year=score(final,hit.get("snippet","")+"\n"+body)
            if s<82 or year is None or not 2000<=year<=2010 or "project-build language" not in ev: continue
            cu=canon(final)
            if cu in known: continue
            txt=(title+" "+hit.get("snippet","")+" "+row["query"]).lower()
            langs=["C++"] if "c++" in txt else ["C"]
            seed.append({"title":title or hit["title"],"url":cu,"year":year,"year_label":str(year),"language":langs,"category":classify(txt),"kind":"auto-discovered project/tutorial","site":urlsplit(cu).netloc,"score":s,"evidence":ev[:4],"tags":[],"notes":hit.get("snippet","")[:360],"provenance":"automated-harvest","query_family":row["family"]})
            known.add(cu); added+=1
        print(f"{qi}/{len(chosen)} queries, {added} new")
        time.sleep(.6)
    seed.sort(key=lambda x:(-int(x.get("score",0)),int(x.get("year") or 9999),x.get("title","").lower()))
    Path(a.out).write_text(json.dumps(seed,ensure_ascii=False,indent=2)+"\n")
    print("generated_queries",len(qs),"added",added,"total",len(seed))
if __name__=="__main__": main()
