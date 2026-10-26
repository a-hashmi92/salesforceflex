import os
NAME="Your Name"; SITE="salesforceflex.com"; EMAIL="hello@salesforceflex.com"
PROJECTS=[
 dict(slug="sales-cloud-revamp",title="Sales Cloud revamp for a B2B manufacturer",tag="Sales Cloud",
  blurb="Rebuilt lead-to-opportunity flow and cut quote turnaround from days to hours.",
  problem="Reps tracked deals in spreadsheets alongside a half-configured Salesforce org, so pipeline reports could not be trusted.",
  solution="Redesigned the lead, opportunity and quote objects, added Flow-based approvals, and migrated 40k legacy records.",
  results=["Quote turnaround down 70%","Single source of truth for pipeline","Adoption above 90% in 8 weeks"],
  stack="Sales Cloud, Flow, CPQ, Data Loader"),
 dict(slug="service-cloud-automation",title="Service Cloud case automation",tag="Service Cloud",
  blurb="Omni-channel routing and Einstein-assisted triage for a support team.",
  problem="Cases landed in one shared queue and were triaged by hand, so urgent issues waited behind routine ones.",
  solution="Built skills-based routing, entitlement rules and a knowledge-backed case console.",
  results=["First response time down 45%","Fewer escalations","Agents resolve more on first contact"],
  stack="Service Cloud, Omni-Channel, Knowledge, Flow"),
 dict(slug="integration-architecture",title="Integration architecture with ERP",tag="Integration",
  blurb="Designed a reliable two-way sync between Salesforce and the finance system.",
  problem="Orders and invoices were re-keyed between systems, causing errors and delayed billing.",
  solution="Designed an event-driven integration with retries, monitoring and clear ownership of each field.",
  results=["Manual re-keying eliminated","Invoices issued same day","Documented, supportable design"],
  stack="MuleSoft, Platform Events, Apex, REST APIs"),
]
NAV=[("index.html","Home"),("about.html","About"),("what-i-do.html","What I do"),("projects.html","Projects"),("contact.html","Contact")]
def page(fn,title,body,depth=0,cur=None):
    p="../"*depth
    nav="".join(f'<a href="{p}{h}"{" aria-current=\"page\"" if h==cur else ""}>{t}</a>' for h,t in NAV)
    html=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {NAME}</title><meta name="description" content="Salesforce consulting: {title}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700;800&family=Instrument+Sans:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css"></head><body>
<header class="top"><a class="logo" href="{p}index.html">{NAME}</a><nav aria-label="Main">{nav}</nav></header>
<main>{body}</main>
<footer><p>© 2026 {NAME}. <a href="https://{SITE}">{SITE}</a></p></footer></body></html>'''
    os.makedirs(os.path.dirname(fn) or ".",exist_ok=True); open(fn,"w").write(html)
def card(pr,p=""):
    return f'<a class="card" href="{p}projects/{pr["slug"]}.html"><span class="chip">{pr["tag"]}</span><h3>{pr["title"]}</h3><p>{pr["blurb"]}</p><span class="more">Read summary</span></a>'
page("index.html","Home",f'''
<section class="hero"><div><h1>Salesforce that bends to your business, not the other way round.</h1>
<p class="lead">I design, build and fix Salesforce orgs so your teams spend less time on admin and more time selling and serving.</p>
<p><a class="btn" href="projects.html">See my projects</a> <a class="btn ghost" href="contact.html">Get in touch</a></p></div>
<aside class="record" aria-hidden="true"><b>Opportunity</b><dl><dt>Stage</dt><dd>Negotiation</dd><dt>Owner</dt><dd>{NAME}</dd><dt>Automation</dt><dd>3 flows active</dd><dt>Data quality</dt><dd>Clean</dd></dl></aside></section>
<section class="wrap"><h2>Recent projects</h2><div class="grid">{"".join(card(x) for x in PROJECTS)}</div></section>''',cur="index.html")
page("about.html","About",f'''<section class="wrap narrow"><h1>About me</h1>
<p>I'm {NAME}, a Salesforce consultant. Replace this paragraph with your story: how you got into Salesforce, years of experience and the kinds of teams you work with.</p>
<h2>Certifications</h2><ul><li>Salesforce Administrator</li><li>Platform App Builder</li><li>Add your certifications here</li></ul>
<h2>How I work</h2><p>I start with how your team actually works, then configure before I code, and document everything so you are never locked in.</p></section>''',cur="about.html")
svc=[("Implementation","Sales, Service and Experience Cloud set up around your process."),("Automation","Flows and Apex that remove repetitive manual work."),("Integration","Reliable connections between Salesforce and your other systems."),("Data and migration","Clean-up, deduplication and moves from legacy systems."),("Org health checks","A written review of your org with a prioritised fix list."),("Training and support","Hands-on sessions and ongoing admin help.")]
page("what-i-do.html","What I do",f'''<section class="wrap"><h1>What I do</h1><p class="lead">Six ways I can help with your Salesforce org.</p>
<div class="grid">{"".join(f'<div class="card static"><h3>{a}</h3><p>{b}</p></div>' for a,b in svc)}</div></section>''',cur="what-i-do.html")
page("projects.html","Projects",f'''<section class="wrap"><h1>Projects</h1><p class="lead">Select a project to read the summary and download the full case study.</p>
<div class="grid">{"".join(card(x) for x in PROJECTS)}</div></section>''',cur="projects.html")
page("contact.html","Contact",f'''<section class="wrap narrow"><h1>Contact</h1><p class="lead">Tell me what you're working on and I'll reply within two working days.</p>
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST"><label>Name<input name="name" required></label><label>Email<input type="email" name="email" required></label><label>Message<textarea name="message" rows="6" required></textarea></label><button class="btn" type="submit">Send message</button></form>
<p>Or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></section>''',cur="contact.html")
for pr in PROJECTS:
    page(f"projects/{pr['slug']}.html",pr["title"],f'''<article class="wrap narrow"><p><a href="../projects.html">Back to all projects</a></p><span class="chip">{pr["tag"]}</span><h1>{pr["title"]}</h1>
<h2>The problem</h2><p>{pr["problem"]}</p><h2>What I did</h2><p>{pr["solution"]}</p><h2>Results</h2><ul>{"".join(f"<li>{r}</li>" for r in pr["results"])}</ul>
<h2>Tools used</h2><p>{pr["stack"]}</p>
<p><a class="btn" href="../case-studies/{pr["slug"]}.pdf" download>Download case study (PDF)</a></p></article>''',depth=1,cur="projects.html")
os.makedirs("case-studies",exist_ok=True); open("case-studies/README.txt","w").write("Put each case study PDF here, named exactly like the project slug, e.g. sales-cloud-revamp.pdf\n")
open("CNAME","w").write(SITE+"\n"); open(".nojekyll","w").write("")
open("style.css","w").write('''
:root{--bg:#EEF3F8;--ink:#12263F;--muted:#4A5E78;--blue:#0A66E0;--sun:#FFB400;--card:#fff;--line:#CBD6E4}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:400 1.05rem/1.65 "Instrument Sans",system-ui,sans-serif}
h1,h2,h3,.logo{font-family:"Bricolage Grotesque",system-ui,sans-serif;line-height:1.1;letter-spacing:-.02em}
h1{font-size:clamp(2.2rem,5vw,3.8rem);font-weight:800;margin:.2em 0 .4em}h2{font-size:1.6rem;margin:1.6em 0 .4em}h3{margin:.4em 0}
a{color:var(--blue)}a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible{outline:3px solid var(--sun);outline-offset:2px}
.top{display:flex;flex-wrap:wrap;gap:1rem;justify-content:space-between;align-items:center;padding:1rem clamp(1rem,5vw,4rem);border-bottom:1px solid var(--line)}
.logo{font-weight:800;font-size:1.3rem;text-decoration:none;color:var(--ink)}
nav{display:flex;flex-wrap:wrap;gap:1.2rem}nav a{color:var(--ink);text-decoration:none;padding:.2rem 0;border-bottom:3px solid transparent}
nav a:hover,nav a[aria-current]{border-color:var(--sun)}
.wrap{max-width:1080px;margin:0 auto;padding:3rem clamp(1rem,5vw,2rem)}.narrow{max-width:720px}
.hero{max-width:1080px;margin:0 auto;padding:4rem clamp(1rem,5vw,2rem) 2rem;display:grid;grid-template-columns:1.6fr 1fr;gap:3rem;align-items:center}
.lead{font-size:1.25rem;color:var(--muted);max-width:60ch}
.btn{display:inline-block;background:var(--blue);color:#fff;padding:.8rem 1.4rem;border-radius:6px;text-decoration:none;font-weight:600;border:2px solid var(--blue);cursor:pointer;font-size:1rem}
.btn:hover{background:var(--ink);border-color:var(--ink)}.btn.ghost{background:transparent;color:var(--blue)}.btn.ghost:hover{color:#fff}
.record{background:var(--card);border:1px solid var(--line);border-top:6px solid var(--sun);border-radius:4px;padding:1.2rem 1.4rem;box-shadow:8px 8px 0 var(--ink);transform:rotate(1.5deg)}
.record dl{display:grid;grid-template-columns:auto 1fr;gap:.4rem 1rem;margin:.6rem 0 0}.record dt{color:var(--muted)}.record dd{margin:0;font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;margin-top:1.5rem}
.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:4px;padding:1.4rem;text-decoration:none;color:var(--ink)}
a.card:hover{border-color:var(--blue);box-shadow:0 0 0 2px var(--blue)}.card p{color:var(--muted);margin:.3rem 0 1rem}
.more{color:var(--blue);font-weight:600;text-decoration:underline}
.chip{display:inline-block;background:var(--ink);color:#fff;font-size:.85rem;padding:.1rem .6rem;border-radius:99px}
form{display:grid;gap:1rem;margin:1.5rem 0}label{display:grid;gap:.3rem;font-weight:600}
input,textarea{font:inherit;padding:.7rem;border:1px solid var(--muted);border-radius:4px;background:#fff}
footer{padding:2rem clamp(1rem,5vw,4rem);border-top:1px solid var(--line);color:var(--muted)}
@media(max-width:760px){.hero{grid-template-columns:1fr}.record{transform:none}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
''')
open("README.md","w").write(f"""# {SITE}
Static site. Deploy: push to GitHub, then Settings > Pages > Deploy from branch > main / root. The CNAME file points it at {SITE}.
Edit content in `build.py` (name, email, projects) and run `python3 build.py`, or edit the HTML directly.
Add case study PDFs to `case-studies/` named after each project slug.
Contact form: create a free Formspree form and replace YOUR_FORM_ID in contact.html.
""")
