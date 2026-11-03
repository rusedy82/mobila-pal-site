# Site 2 (aceeași firmă): mobilă la comandă din PAL melaminat și MDF vopsit.
# Rulare: python3 build.py <folder-ieșire>
import os, sys, shutil, html

OUT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))

C = {
    "nume": "Mobilă PAL & MDF",                 # PROVIZORIU
    "sub": "Mobilă la comandă din PAL melaminat și MDF vopsit",
    "tel_afisat": "0759 324 006",
    "tel_link": "+40759324006",
    "whatsapp": "40759324006",
    "domeniu": "",                               # gol până avem domeniul
}
ORAS = "Arad"

def icon(name, size=26, color="currentColor"):
    p = {
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
        "ruler": '<path d="M3 17 17 3l4 4L7 21z"/><path d="m7 13 2 2M10 10l2 2M13 7l2 2"/>',
        "cube": '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
        "truck": '<path d="M1 4h14v12H1zM15 9h4l4 4v3h-8z"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>',
        "tool": '<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L4 12l8-8z"/>',
        "layers": '<path d="M12 3 2 8l10 5 10-5z"/><path d="m2 13 10 5 10-5"/>',
        "brush": '<path d="M9.06 11.9 18 3l3 3-8.94 8.94"/><path d="M7 14a3 3 0 0 0-3 3c0 1.5-1 2-2 3 2.5 1 6 .5 7-2a3 3 0 0 0-2-4z"/>',
        "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
        "arrow": '<path d="M4 12h16M14 6l6 6-6 6"/>',
        "menu": '<path d="M3 7h18M3 12h18M3 17h18"/>',
        "image": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 17-5-5-9 8"/>',
    }[name]
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>')

WA_ICON = '<svg width="22" height="22" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'

def kw(href, text): return f'<a class="kw" href="{href}.html">{text}</a>'
PAL = lambda t="PAL melaminat": kw("pal-melaminat", t)
MDF = lambda t="MDF vopsit": kw("mdf-vopsit", t)

# ---------- mostre de decor (desen) ----------
def swatches(kind):
    if kind == "pal":
        cols = [("Stejar natural", "linear-gradient(90deg,#C9A27A,#B98C61 40%,#CFA984 70%,#BE9268)"),
                ("Nuc închis", "linear-gradient(90deg,#5B3E2B,#4A3222 45%,#634532 75%,#4E3524)"),
                ("Alb mat", "#F4F2EE"), ("Gri antracit", "#3E4447"), ("Beton", "linear-gradient(135deg,#A9A9A4,#BDBCB6 50%,#9F9E99)"), ("Bej", "#D9C7A7")]
    else:
        cols = [("Alb", "#FAFAF8"), ("Verde salvie", "#9DAE98"), ("Albastru petrol", "#24485A"),
                ("Grej", "#B8AEA2"), ("Negru mat", "#1E1F21"), ("Teracotă", "#B66A4C")]
    return '<div class="sw">' + "".join(f'<div class="swi"><span style="background:{b}"></span><small>{n}</small></div>' for n, b in cols) + '</div>'

# ---------- comune ----------
def logo_mark(size=46):
    return f'''<svg class="logo-mark" width="{size}" height="{size}" viewBox="0 0 48 48" aria-hidden="true">
  <defs><linearGradient id="pgb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#25443C"/><stop offset="1" stop-color="#132723"/></linearGradient>
  <linearGradient id="pga" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9CF96"/><stop offset="1" stop-color="#C49A4C"/></linearGradient></defs>
  <rect width="48" height="48" rx="13" fill="url(#pgb)"/>
  <rect x="11" y="12" width="12" height="24" rx="2" fill="none" stroke="url(#pga)" stroke-width="3"/>
  <rect x="25" y="12" width="12" height="24" rx="2" fill="url(#pga)"/>
  <path d="M20 22v4M28 22v4" stroke="#132723" stroke-width="2" stroke-linecap="round"/>
  <path d="M20 22v4" stroke="#E9CF96" stroke-width="2" stroke-linecap="round"/>
</svg>'''

def logo(light=False):
    a, b = (C["nume"].split(" ", 1) + [""])[:2]
    return f'<span class="logo{" logo-light" if light else ""}">{logo_mark()}<span class="wm"><span class="wm1">{a} <i>{b}</i></span><small>{C["sub"]}</small></span></span>'

PAGES_NAV = [("index.html#pal", "PAL melaminat"), ("index.html#mdf", "MDF vopsit"), ("pal-melaminat-sau-mdf-vopsit.html", "PAL sau MDF?"),
             ("index.html#unde", "Ce facem"), ("index.html#oferta", "Cere ofertă")]

def header():
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in PAGES_NAV)
    return f'''<div class="live"><div class="wrap"><span class="dot"></span>Răspundem acum<span class="hide-m"> · Mostre de PAL melaminat și MDF vopsit la măsurători</span></div></div>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html" aria-label="{C["nume"]}, pagina principală">{logo()}</a>
  <nav class="menu nav-desktop" aria-label="Meniu principal"><div class="wrap">{nav}</div></nav>
  <a class="call-dot" href="tel:{C["tel_link"]}" aria-label="Sună la {C["tel_afisat"]}">{icon("phone", 24, "#fff")}</a>
  <button class="menu-btn" type="button" aria-label="Meniu" aria-expanded="false" id="menu-btn">{icon("menu", 26, "#17302A")}</button>
</div></header>'''

def footer():
    links = "".join(f'<li><a href="{s}.html">{t}</a></li>' for s, t in [
        ("pal-melaminat", "PAL melaminat"), ("mdf-vopsit", "MDF vopsit"), ("pal-melaminat-sau-mdf-vopsit", "PAL melaminat sau MDF vopsit"),
        ("bucatarii-pal-melaminat", "Bucătării din PAL melaminat"), ("bucatarii-mdf-vopsit", "Bucătării din MDF vopsit"), ("dressing-pal-melaminat", "Dressing din PAL melaminat")])
    return f'''<footer><div class="wrap">
  <div class="cols">
    <div><a href="index.html" class="f-logo" aria-label="{C["nume"]}">{logo(True)}</a><p style="margin-top:14px">Mobilă la comandă din PAL melaminat și MDF vopsit. Măsurători gratuite, proiect 3D, transport și montaj incluse.</p></div>
    <div><h4>Materiale și mobilă</h4><ul>{links}</ul></div>
    <div><h4>Contact</h4><ul><li><a href="tel:{C["tel_link"]}">{C["tel_afisat"]}</a></li><li><a href="https://wa.me/{C["whatsapp"]}">WhatsApp</a></li><li><a href="index.html#oferta">Cere ofertă</a></li></ul></div>
  </div>
  <p class="legal">© 2026 {C["nume"]} · <span class="loc">{ORAS}</span> · Toate drepturile rezervate.</p>
</div></footer>
<div class="sticky"><a href="tel:{C["tel_link"]}"><span class="ring">{icon("phone", 24, "#fff")}</span><span><small>Sună pentru o ofertă PAL sau MDF</small><b>{C["tel_afisat"]}</b></span></a></div>
<script>
(function(){{var b=document.getElementById("menu-btn"),m=document.querySelector("nav.menu");if(!b||!m)return;
b.addEventListener("click",function(){{var o=m.classList.toggle("open");b.setAttribute("aria-expanded",o)}});
m.addEventListener("click",function(e){{if(e.target.tagName==="A"){{m.classList.remove("open");b.setAttribute("aria-expanded","false")}}}});}})();
</script>'''

def page(title, desc, path, body):
    # Arad în titlu și descriere: acolo se uită Google pentru căutările locale
    if ORAS not in title: title = title.replace(" | ", f" în {ORAS} | ", 1)
    if ORAS not in desc: desc = desc.rstrip(".") + f". Lucrăm în {ORAS} și împrejurimi."
    ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness",'
          f'"name":"{C["nume"]}","description":"Mobilă la comandă din PAL melaminat și MDF vopsit","telephone":"{C["tel_link"]}",'
          f'"areaServed":{{"@type":"City","name":"{ORAS}"}},"address":{{"@type":"PostalAddress","addressLocality":"{ORAS}","addressCountry":"RO"}}'
          + (f',"url":"{C["domeniu"]}/"' if C["domeniu"] else "") + '}</script>\n') if path == "index.html" else ""
    canon = f'<link rel="canonical" href="{C["domeniu"]}/{"" if path == "index.html" else path}">\n' if C["domeniu"] else ""
    return f'''<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{canon}{ld}<meta name="theme-color" content="#17302A">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
{header()}
<main>
{body}
</main>
{footer()}
</body>
</html>
'''

def call_btn(label="Sună acum"):
    return f'<a class="btn" href="tel:{C["tel_link"]}">{icon("phone", 24, "#fff")}<span><small>{label}</small>{C["tel_afisat"]}</span></a>'
def faq_html(items): return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
def li(xs): return "".join(f"<li>{x}</li>" for x in xs)

def why_block():
    return f'''<div class="why">
  <h2>De ce să comanzi de la noi</h2>
  <ul class="checks">
    <li>Mobilă din {PAL()} și {MDF()}, făcută pe centimetru</li>
    <li>Măsurători gratuite, cu mostre de decoruri și culori</li>
    <li>Proiect 3D înainte de producție</li>
    <li>Transport și montaj incluse în preț</li>
    <li>Lucrăm în {ORAS} și împrejurimi</li>
  </ul>
  <a class="btn" href="tel:{C["tel_link"]}">{icon("phone", 22, "#fff")} Sună acum {C["tel_afisat"]}</a>
</div>'''

# ---------- formular pe WhatsApp ----------
def oferta_section():
    return f'''
<section id="oferta" class="order-sec"><div class="wrap">
  <div class="head"><span class="eyebrow pill">Cere ofertă</span><h2>Cere o ofertă pentru mobilă din PAL melaminat sau MDF vopsit</h2>
  <p>Completează câteva detalii și apasă butonul: cererea se deschide gata scrisă în WhatsApp, iar tu doar o trimiți.</p></div>
  <form id="of-form" class="order" novalidate>
    <fieldset class="fs">
      <legend><span class="n">{icon("user", 20, "#fff")}</span>Datele tale</legend>
      <div class="row2">
        <label>Numele tău <em>*</em><input name="Nume" required autocomplete="name"></label>
        <label>Telefonul tău <em>*</em><input name="Telefon" id="f-tel" type="tel" required autocomplete="tel" placeholder="+40 7xx xxx xxx"><span class="err-txt" id="tel-err" hidden>Scrie un număr de telefon valid, ca să te putem suna.</span></label>
      </div>
      <label>Orașul / localitatea <em>*</em><input name="Oraș" required autocomplete="address-level2"></label>
    </fieldset>
    <fieldset class="fs">
      <legend><span class="n">{icon("layers", 20, "#fff")}</span>Ce mobilă vrei</legend>
      <div class="row2">
        <label>Tip de mobilă <em>*</em><select name="Tip mobilă" required><option value="">Alege...</option><option>Bucătărie</option><option>Dressing / dulap</option><option>Dormitor</option><option>Living</option><option>Baie</option><option>Birou / firmă</option><option>Altceva</option></select></label>
        <label>Material<select name="Material"><option>PAL melaminat</option><option>MDF vopsit</option><option>PAL melaminat + fețe din MDF vopsit</option><option>Nu știu încă, vreau recomandare</option></select></label>
      </div>
      <label>Dimensiuni / descriere <small>(opțional)</small><textarea name="Descriere" rows="3" placeholder="de ex. bucătărie pe colț 3 m + 2 m, fețe albe mat"></textarea></label>
    </fieldset>
    <label class="agree"><input type="checkbox" required> Sunt de acord să fiu contactat telefonic sau pe WhatsApp pentru această cerere.</label>
    <button class="btn btn-wa" type="submit" id="of-submit">{WA_ICON} Trimite cererea pe WhatsApp</button>
  </form>
  <div id="of-ok" class="order-ok" tabindex="-1" hidden>
    <div class="ok-ic"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div>
    <h3>Vă mulțumim!</h3>
    <p class="ok-thanks">Cererea ta e gata în WhatsApp.</p>
    <p class="ok-next" style="margin-top:12px"><b>Ultimul pas:</b> în WhatsApp, apasă <b>Trimite</b>. Dacă WhatsApp nu s-a deschis, apasă butonul de mai jos.</p>
    <p style="margin-top:16px"><a class="btn btn-wa" id="wa-again" href="https://wa.me/{C["whatsapp"]}" target="_blank" rel="noopener">{WA_ICON} Deschide WhatsApp</a></p>
    <p class="ok-urgent">Sau sună-ne: <a href="tel:{C["tel_link"]}">{C["tel_afisat"]}</a></p>
  </div>
</div></section>
<script>
(function(){{
  var f=document.getElementById("of-form"); if(!f) return;
  var tel=document.getElementById("f-tel");
  tel.addEventListener("input",function(){{ tel.setCustomValidity(""); document.getElementById("tel-err").hidden=true; }});
  f.addEventListener("submit",function(e){{
    e.preventDefault();
    var cifre=(tel.value.match(/\\d/g)||[]).length;
    tel.setCustomValidity(cifre>=9 && cifre<=15 ? "" : "Scrie un număr de telefon valid.");
    document.getElementById("tel-err").hidden=tel.validity.valid;
    if(!f.checkValidity()){{ f.reportValidity(); return; }}
    var d={{}}; new FormData(f).forEach(function(v,k){{ d[k]=v; }});
    var txt="Bună ziua! Aș dori o ofertă pentru mobilă la comandă.\\n";
    ["Nume","Telefon","Oraș","Tip mobilă","Material","Descriere"].forEach(function(k){{ var v=(d[k]||"").trim(); if(v) txt+="\\n"+k+": "+v; }});
    var url="https://wa.me/{C["whatsapp"]}?text="+encodeURIComponent(txt);
    document.getElementById("wa-again").href=url;
    f.reset(); f.hidden=true; var ok=document.getElementById("of-ok"); ok.hidden=false; ok.scrollIntoView({{block:"center",behavior:"smooth"}});
    var w=window.open(url,"_blank"); if(!w) window.location.href=url;
  }});
}})();
</script>'''

# ---------- conținut ----------
PAL_PLUS = ["Preț bun: cea mai accesibilă variantă pentru mobilă la comandă", "Sute de decoruri: lemn, culori uni, piatră, beton",
            "Suprafață rezistentă la zgârieturi ușoare", "Se curăță ușor, cu o lavetă umedă"]
PAL_MINUS = ["Nu se poate revopsi", "Muchiile trebuie protejate de apă stătută", "Fețe drepte, fără frezări"]
MDF_PLUS = ["Orice culoare, cu finisaj mat, satinat sau lucios", "Se poate freza: profile clasice, caneluri, muchii rotunjite",
            "Aspect elegant, fără muchii vizibile", "Potrivit pentru fețe fără mânere"]
MDF_MINUS = ["Mai scump decât PAL-ul melaminat", "Finisajul lucios arată amprentele", "La lovituri puternice vopseaua se poate ciobi"]

def pm(plus, minus):
    return f'<div class="pm"><div class="pm-col pm-plus"><h3>Avantaje</h3><ul>{li(plus)}</ul></div><div class="pm-col pm-minus"><h3>De ținut cont</h3><ul>{li(minus)}</ul></div></div>'

COMPARE = [("Preț", "mai accesibil", "mai scump"), ("Culori", "sute de decoruri gata făcute", "orice culoare, vopsită la comandă"),
           ("Aspect", "decor de lemn, uni sau piatră", "fețe vopsite, mat sau lucios"), ("Frezări și profile", "nu", "da"),
           ("Reparații", "se schimbă fața", "se revopsește fața"), ("Potrivit pentru", "corpuri, dressinguri, dormitoare, bucătării", "fețe de bucătărie, living, dressing")]
def compare_table():
    rows = "".join(f"<tr><th>{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in COMPARE)
    return f'<div class="cmp-wrap"><table class="cmp"><thead><tr><th></th><th>{PAL()}</th><th>{MDF()}</th></tr></thead><tbody>{rows}</tbody></table></div>'

UNDE = [("bucatarii-pal-melaminat", "Bucătării din PAL melaminat", "Corpuri și fețe din PAL melaminat, în decor de lemn sau culori uni, cu blat asortat."),
        ("bucatarii-mdf-vopsit", "Bucătării din MDF vopsit", "Fețe din MDF vopsit mat sau lucios, pe corpuri din PAL melaminat."),
        ("dressing-pal-melaminat", "Dressing din PAL melaminat", "Dressinguri și dulapuri încastrate din PAL melaminat, cu uși glisante sau batante."),
        ("pal-melaminat-sau-mdf-vopsit", "PAL melaminat sau MDF vopsit?", "Comparația completă, ca să alegi materialul potrivit pentru bugetul tău.")]

FAQ = [
    ("Ce este PAL-ul melaminat?", f"{PAL('PAL-ul melaminat')} este o placă din particule de lemn presate, acoperită cu un strat melaminat decorativ. E cel mai folosit material pentru mobilă la comandă: accesibil, rezistent și disponibil în sute de decoruri."),
    ("Ce este MDF-ul vopsit?", f"{MDF('MDF-ul vopsit')} este o placă din fibre fine de lemn, densă, care se poate freza și vopsi în aproape orice culoare. Se folosește mai ales pentru fețele mobilei."),
    ("Ce e mai bun: PAL melaminat sau MDF vopsit?", f"Depinde de buget și de aspectul dorit. Multe bucătării au corpurile din PAL melaminat și fețele din MDF vopsit. Vezi {kw('pal-melaminat-sau-mdf-vopsit','comparația PAL melaminat sau MDF vopsit')}."),
    ("Cât costă mobila din PAL melaminat?", "Prețul depinde de dimensiuni, decor și feronerie. După măsurătorile gratuite primești proiectul 3D și prețul final, cu transport și montaj incluse."),
    ("Pot vedea mostre de PAL melaminat și MDF vopsit?", "Da. La măsurători aducem mostre de decoruri de PAL melaminat și de culori pentru MDF vopsit, ca să le vezi în lumina din casa ta."),
]

def index():
    unde = "".join(f'<div class="ucard"><h3>{kw(s, t)}</h3><p>{d}</p></div>' for s, t, d in UNDE)
    body = f'''
<div class="hx">
  <div class="hx-bg" aria-hidden="true"><img src="lucrari/alba-1.jpg" alt="" width="1600" height="1200" fetchpriority="high"></div>
  <div class="wrap hx-in">
    <span class="eyebrow pill pill-glass">Mobilă la comandă din PAL melaminat și MDF vopsit</span>
    <h1>Mobilă la comandă din <em>PAL melaminat</em> și <em>MDF vopsit</em></h1>
    <p class="lead">Facem mobilă pe centimetru din {PAL()} și {MDF()}: bucătării, dressinguri, dormitoare și living. Alegi decorul de {PAL()} sau culoarea de {MDF()}, iar noi venim la măsurători, facem proiectul 3D și montăm mobila. Lucrăm în {ORAS} și împrejurimi.</p>
    <div class="cta-row">{call_btn()}<a class="btn ghost ghost-light" href="#oferta">Cere ofertă</a></div>
    <p class="hx-cap">{icon("image", 16, "#E9CF96")} Lucrare realizată și montată de echipa noastră</p>
  </div>
</div>
<div class="wrap"><div class="trust">
  <div class="t-item"><span class="t-ic">{icon("ruler", 24, "#fff")}</span><div><b>Măsurători gratuite</b><span>cu mostre la tine acasă</span></div></div>
  <div class="t-item"><span class="t-ic">{icon("cube", 24, "#fff")}</span><div><b>Proiect 3D</b><span>vezi totul înainte</span></div></div>
  <div class="t-item"><span class="t-ic">{icon("truck", 24, "#fff")}</span><div><b>Transport inclus</b><span>în prețul ofertei</span></div></div>
  <div class="t-item"><span class="t-ic">{icon("tool", 24, "#fff")}</span><div><b>Montaj inclus</b><span>plecăm când e gata</span></div></div>
</div></div>

<section id="pal"><div class="wrap two-mat">
  <div>
    <div class="head"><span class="eyebrow pill">Material 1</span><h2>Mobilă din PAL melaminat</h2></div>
    <p>{PAL("PAL-ul melaminat")} este cel mai folosit material pentru mobila la comandă. Este o placă din particule de lemn, acoperită cu un strat melaminat rezistent, disponibil în sute de decoruri. Din {PAL()} facem corpurile pentru aproape orice mobilă, dar și fețe pentru bucătării, dressinguri și dormitoare.</p>
    <p style="margin-top:12px">Mobila din {PAL()} are un preț bun, se curăță ușor și arată bine mulți ani, dacă muchiile sunt protejate cu cant de calitate.</p>
    {pm(PAL_PLUS, PAL_MINUS)}
    <p style="margin-top:16px"><a class="more-l" href="pal-melaminat.html">Tot despre PAL melaminat →</a></p>
  </div>
  <div class="mat-card">
    <h3>Decoruri de PAL melaminat</h3><p>Câteva exemple. La măsurători îți aducem mostre reale.</p>
    {swatches("pal")}
  </div>
</div></section>

<section id="mdf" class="soft"><div class="wrap two-mat">
  <div>
    <div class="head"><span class="eyebrow pill">Material 2</span><h2>Mobilă din MDF vopsit</h2></div>
    <p>{MDF("MDF-ul vopsit")} se folosește pentru fețele mobilei: uși și sertare. Este o placă densă din fibre de lemn, care se poate freza și vopsi în aproape orice culoare, mat, satinat sau lucios. Fețele din {MDF()} dau mobilei un aspect elegant, fără muchii vizibile.</p>
    <p style="margin-top:12px">Cel mai des combinăm corpurile din {PAL()} cu fețele din {MDF()}: ai aspectul vopsit acolo unde se vede și un preț mai bun la structură.</p>
    {pm(MDF_PLUS, MDF_MINUS)}
    <p style="margin-top:16px"><a class="more-l" href="mdf-vopsit.html">Tot despre MDF vopsit →</a></p>
  </div>
  <div class="mat-card">
    <h3>Culori pentru MDF vopsit</h3><p>Câteva exemple. Putem vopsi și după codul de culoare dorit.</p>
    {swatches("mdf")}
  </div>
</div></section>

<section id="compara"><div class="wrap">
  <div class="head"><span class="eyebrow pill">Comparație</span><h2>PAL melaminat sau MDF vopsit?</h2><p>Pe scurt, diferențele dintre cele două materiale. Detalii în {kw("pal-melaminat-sau-mdf-vopsit","comparația completă")}.</p></div>
  {compare_table()}
</div></section>

<section id="unde" class="band"><div class="wrap">
  <div class="head"><span class="eyebrow pill pill-dark">Ce facem</span><h2>Mobilă din PAL melaminat și MDF vopsit, pentru fiecare cameră</h2></div>
  <div class="ugrid">{unde}</div>
</div></section>

{oferta_section()}

<section id="intrebari"><div class="wrap">
  <div class="head"><span class="eyebrow pill">Întrebări</span><h2>Întrebări despre PAL melaminat și MDF vopsit</h2></div>
  <div class="faq">{faq_html(FAQ)}</div>
</div></section>

<section class="final"><div class="wrap">
  <h2>Vrei mobilă din PAL melaminat sau MDF vopsit? Sună acum.</h2>
  <a class="phone-big" href="tel:{C["tel_link"]}">{C["tel_afisat"]}</a>
</div></section>
'''
    return page(f"Mobilă la comandă din PAL melaminat și MDF vopsit | {C['nume']}",
                "Mobilă la comandă din PAL melaminat și MDF vopsit: bucătării, dressinguri, dormitoare. Măsurători gratuite cu mostre, proiect 3D, transport și montaj incluse.",
                "index.html", body)

def inner(path, h1, lead, inner_html, title, desc):
    body = f'''
<div class="hero hero-k"><div class="wrap">
  <p class="crumbs"><a href="index.html">Acasă</a> / {h1.replace("<em>","").replace("</em>","")}</p>
  <h1 style="margin-top:14px">{h1}</h1>
  <p class="lead" style="margin-top:12px">{lead}</p>
  <div class="cta-row">{call_btn()}<a class="btn ghost" href="index.html#oferta">Cere ofertă</a></div>
</div></div>
<section><div class="wrap"><div class="two">
  <div class="prose">{inner_html}</div>
  {why_block()}
</div></div></section>'''
    return page(title, desc, path, body)

def pages():
    out = {}
    out["pal-melaminat.html"] = inner("pal-melaminat.html", "Mobilă din <em>PAL melaminat</em>",
        f"Tot ce trebuie să știi despre {PAL()}: ce este, ce decoruri există, avantaje, dezavantaje și unde se potrivește.",
        f'''<h2 style="margin-top:0">Ce este PAL-ul melaminat</h2>
<p>{PAL("PAL-ul melaminat")} este o placă din particule de lemn presate, acoperită pe ambele fețe cu un strat melaminat decorativ. La mobilă se folosește de obicei placa de 18 mm, iar muchiile se acoperă cu cant ABS.</p>
<h2>Decoruri de PAL melaminat</h2><p>{PAL()} există în sute de decoruri: imitație de lemn, culori uni, piatră sau beton.</p>{swatches("pal")}
{pm(PAL_PLUS, PAL_MINUS)}
<h2>Unde folosim PAL melaminat</h2><p>La corpurile pentru aproape orice mobilă și la fețe pentru {kw("bucatarii-pal-melaminat","bucătării din PAL melaminat")}, {kw("dressing-pal-melaminat","dressinguri din PAL melaminat")}, dormitoare și camere de copii.</p>
<h2>Întreținerea mobilei din PAL melaminat</h2><p>Se șterge cu o lavetă umedă și detergent delicat. Evită bureții abrazivi și șterge imediat apa vărsată, mai ales lângă chiuvetă.</p>
<h2>PAL melaminat sau MDF vopsit?</h2><p>Dacă vrei fețe vopsite sau frezate, alege {MDF()}. Vezi {kw("pal-melaminat-sau-mdf-vopsit","comparația completă")}.</p>''',
        f"PAL melaminat în {ORAS}: mobilă la comandă, decoruri, avantaje | {C['nume']}",
        "Mobilă la comandă din PAL melaminat: ce este, decoruri, avantaje și dezavantaje, unde se folosește. Măsurători gratuite cu mostre.")
    out["mdf-vopsit.html"] = inner("mdf-vopsit.html", "Mobilă din <em>MDF vopsit</em>",
        f"Tot ce trebuie să știi despre {MDF()}: ce este, ce culori și finisaje există, avantaje, dezavantaje și unde se potrivește.",
        f'''<h2 style="margin-top:0">Ce este MDF-ul vopsit</h2>
<p>{MDF("MDF-ul vopsit")} este o placă din fibre fine de lemn, densă și omogenă, vopsită în mai multe straturi. Se poate freza, așa că poți avea profile clasice, caneluri sau muchii rotunjite.</p>
<h2>Culori și finisaje pentru MDF vopsit</h2><p>{MDF()} se vopsește în aproape orice culoare, cu finisaj mat, satinat sau lucios.</p>{swatches("mdf")}
{pm(MDF_PLUS, MDF_MINUS)}
<h2>Unde folosim MDF vopsit</h2><p>Mai ales la fețe: {kw("bucatarii-mdf-vopsit","bucătării din MDF vopsit")}, uși de dressing și mobilă de living. Corpurile le facem de obicei din {PAL()}.</p>
<h2>Întreținerea mobilei din MDF vopsit</h2><p>Se curăță cu o lavetă moale din microfibră, umedă, fără produse abrazive sau pe bază de solvenți.</p>
<h2>MDF vopsit sau PAL melaminat?</h2><p>Dacă vrei un preț mai mic și decor de lemn, alege {PAL()}. Vezi {kw("pal-melaminat-sau-mdf-vopsit","comparația completă")}.</p>''',
        f"MDF vopsit în {ORAS}: mobilă la comandă, culori, avantaje | {C['nume']}",
        "Mobilă la comandă din MDF vopsit: ce este, culori și finisaje mat sau lucios, avantaje și dezavantaje. Măsurători gratuite cu mostre.")
    out["pal-melaminat-sau-mdf-vopsit.html"] = inner("pal-melaminat-sau-mdf-vopsit.html", "<em>PAL melaminat</em> sau <em>MDF vopsit</em>?",
        f"Comparația dintre {PAL()} și {MDF()}, ca să alegi materialul potrivit pentru mobila ta și pentru bugetul tău.",
        f'''<h2 style="margin-top:0">Pe scurt</h2>{compare_table()}
<h2>Când alegi PAL melaminat</h2><p>Alege {PAL()} dacă vrei un preț bun, decor de lemn sau culori uni și o mobilă ușor de întreținut. E alegerea potrivită pentru {kw("dressing-pal-melaminat","dressinguri")}, dormitoare și {kw("bucatarii-pal-melaminat","bucătării cu buget atent")}.</p>
<h2>Când alegi MDF vopsit</h2><p>Alege {MDF()} dacă vrei o culoare anume, fețe fără mânere sau profile clasice. Se potrivește la {kw("bucatarii-mdf-vopsit","bucătării moderne și clasice")} și la mobila de living.</p>
<h2>Varianta combinată</h2><p>Cel mai des facem corpurile din {PAL()} și fețele din {MDF()}. Ai aspectul vopsit acolo unde se vede și un preț mai bun la structură.</p>''',
        f"PAL melaminat sau MDF vopsit? Comparație pentru mobilă la comandă în {ORAS} | {C['nume']}",
        "PAL melaminat sau MDF vopsit: diferențe de preț, aspect, culori și întreținere. Cum alegi materialul potrivit pentru mobila la comandă.")
    out["bucatarii-pal-melaminat.html"] = inner("bucatarii-pal-melaminat.html", "Bucătării din <em>PAL melaminat</em>",
        f"Bucătării la comandă cu corpuri și fețe din {PAL()}, în decor de lemn sau culori uni, făcute pe centimetru.",
        f'''<h2 style="margin-top:0">De ce o bucătărie din PAL melaminat</h2><p>O bucătărie din {PAL()} are cel mai bun raport între preț și rezistență. Decorurile de lemn arată natural, iar culorile uni dau un aspect modern.</p>{swatches("pal")}
<h2>Ce putem face</h2><ul class="ticks-l">{li(["Bucătării drepte, pe colț sau în U", "Corpuri suspendate până la tavan", "Blat asortat cu decorul", "Feronerie cu închidere lină"])}</ul>
<h2>Vrei fețe vopsite?</h2><p>Putem păstra corpurile din {PAL()} și face fețele din {MDF()}. Vezi {kw("bucatarii-mdf-vopsit","bucătării din MDF vopsit")}.</p>''',
        f"Bucătării din PAL melaminat la comandă | {C['nume']}",
        "Bucătării la comandă din PAL melaminat: decoruri de lemn și culori uni, măsurători gratuite, proiect 3D, transport și montaj incluse.")
    out["bucatarii-mdf-vopsit.html"] = inner("bucatarii-mdf-vopsit.html", "Bucătării din <em>MDF vopsit</em>",
        f"Bucătării la comandă cu fețe din {MDF()}, mat sau lucios, în culoarea aleasă de tine.",
        f'''<h2 style="margin-top:0">De ce o bucătărie din MDF vopsit</h2><p>Fețele din {MDF()} se vopsesc în orice culoare și pot fi frezate, așa că bucătăria arată exact cum îți dorești: modernă, fără mânere, sau clasică, cu profile.</p>{swatches("mdf")}
<h2>Ce putem face</h2><ul class="ticks-l">{li(["Fețe mat, satinat sau lucios", "Fețe fără mânere, cu profil", "Profile clasice frezate", "Corpuri din PAL melaminat, pentru un preț mai bun"])}</ul>
<h2>Vrei un preț mai mic?</h2><p>Vezi {kw("bucatarii-pal-melaminat","bucătării din PAL melaminat")}, sau compară materialele în {kw("pal-melaminat-sau-mdf-vopsit","PAL melaminat sau MDF vopsit")}.</p>''',
        f"Bucătării din MDF vopsit la comandă | {C['nume']}",
        "Bucătării la comandă din MDF vopsit: orice culoare, mat sau lucios, fețe fără mânere sau clasice. Măsurători gratuite, montaj inclus.")
    out["dressing-pal-melaminat.html"] = inner("dressing-pal-melaminat.html", "Dressing din <em>PAL melaminat</em>",
        f"Dressinguri și dulapuri încastrate din {PAL()}, făcute pe măsura camerei, din podea până la tavan.",
        f'''<h2 style="margin-top:0">De ce un dressing din PAL melaminat</h2><p>{PAL()} e materialul ideal pentru dressinguri: rezistent, ușor de curățat și disponibil în decoruri care se potrivesc cu restul casei.</p>{swatches("pal")}
<h2>Ce putem face</h2><ul class="ticks-l">{li(["Dressing walk-in sau dulap încastrat", "Uși glisante sau batante", "Sertare, rafturi pentru pantofi, bare de haine", "Uși din MDF vopsit, dacă vrei o culoare anume"])}</ul>
<h2>Uși vopsite</h2><p>Pentru uși în culoarea dorită folosim {MDF()}. Vezi {kw("mdf-vopsit","mobilă din MDF vopsit")}.</p>''',
        f"Dressing din PAL melaminat la comandă | {C['nume']}",
        "Dressinguri și dulapuri încastrate din PAL melaminat, la comandă. Măsurători gratuite, proiect 3D, transport și montaj incluse.")
    return out

# ---------- scriere ----------
os.makedirs(OUT, exist_ok=True)
files = {"index.html": index(), **pages()}
for n, c in files.items():
    with open(os.path.join(OUT, n), "w", encoding="utf-8") as f: f.write(c)
shutil.copy(os.path.join(HERE, "style.css"), os.path.join(OUT, "style.css"))
shutil.copytree(os.path.join(HERE, "lucrari"), os.path.join(OUT, "lucrari"), dirs_exist_ok=True)
if C["domeniu"]:
    urls = "".join(f"  <url><loc>{C['domeniu']}/{'' if n == 'index.html' else n}</loc></url>\n" for n in files)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write("User-agent: *\nAllow: /\n" + (f"\nSitemap: {C['domeniu']}/sitemap.xml\n" if C["domeniu"] else ""))
with open(os.path.join(OUT, "favicon.svg"), "w") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="13" fill="#17302A"/><rect x="11" y="12" width="12" height="24" rx="2" fill="none" stroke="#E9CF96" stroke-width="3"/><rect x="25" y="12" width="12" height="24" rx="2" fill="#D9B46A"/></svg>')
print(len(files), "pagini")
