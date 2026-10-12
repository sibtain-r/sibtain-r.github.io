#!/usr/bin/env python3
"""Build the blog from Markdown files. No dependencies, Python 3.8+.

    python build.py                     rebuild blog/ and the Writing section of index.html
    python build.py new "Post title"    create posts/<slug>.md from the template

Every posts/*.md file becomes blog/<slug>.html. Name files YYYY-MM-DD-slug.md: the date is the post's
date (use a date from when you worked on the project) and the rest is the page address.
Files starting with "_" are ignored.
Edit blog/blog.css to change how posts look. Group names live in posts/groups.json.
"""
import datetime, html, json, math, os, re, sys, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(ROOT, "posts")
OUT = os.path.join(ROOT, "blog")
INDEX = os.path.join(ROOT, "index.html")

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900'
         '&family=Newsreader:ital,opsz,wght@0,6..72,300..700;1,6..72,300..700&display=swap" rel="stylesheet">')
FAVICON = ('<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 64 64\'%3E'
           '%3Crect width=\'64\' height=\'64\' fill=\'%2308122a\'/%3E%3Crect x=\'8\' y=\'8\' width=\'20\' height=\'20\' fill=\'%23b2b755\'/%3E'
           '%3Crect x=\'36\' y=\'8\' width=\'20\' height=\'20\' fill=\'%236b1826\'/%3E%3Crect x=\'8\' y=\'36\' width=\'20\' height=\'20\' fill=\'%236b1826\'/%3E'
           '%3Crect x=\'36\' y=\'36\' width=\'20\' height=\'20\' fill=\'%23b2b755\'/%3E%3C/svg%3E">')

BANDS = {"b-black", "b-olive", "b-maroon", "b-navy", "b-now"}
HIGHLIGHTS = {"olive", "maroon", "navy"}


# ------------------------------------------------------------------ markdown
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", r'<img src="\2" alt="\1" loading="lazy">', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               lambda m: '<a href="%s"%s>%s</a>' % (m.group(2), ' rel="noopener"' if m.group(2).startswith("http") else "", m.group(1)), t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


def render(body):
    out, para, lst, kind, quote = [], [], [], None, []
    lines = body.strip("\n").split("\n")
    i = 0

    def flush_p():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    def flush_l():
        nonlocal lst, kind
        if lst:
            tag = "ol" if kind == "ol" else "ul"
            out.append("<%s>" % tag + "".join("<li>%s</li>" % inline(x) for x in lst) + "</%s>" % tag)
            lst, kind = [], None

    def flush_q():
        nonlocal quote
        if quote:
            out.append("<blockquote><p>" + inline(" ".join(quote)) + "</p></blockquote>")
            quote = []

    def flush_all():
        flush_p(); flush_l(); flush_q()

    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("```"):
            flush_all()
            lang = s[3:].strip()
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            cls = ' class="language-%s"' % html.escape(lang) if lang else ""
            out.append("<pre><code%s>%s</code></pre>" % (cls, html.escape("\n".join(code))))
        elif not s:
            flush_all()
        elif s.startswith("### "):
            flush_all(); out.append("<h3>%s</h3>" % inline(s[4:]))
        elif s.startswith("## "):
            flush_all(); out.append("<h2>%s</h2>" % inline(s[3:]))
        elif s.startswith("> "):
            flush_p(); flush_l(); quote.append(s[2:])
        elif s.startswith("- "):
            flush_p(); flush_q()
            if kind not in (None, "ul"): flush_l()
            kind = "ul"; lst.append(s[2:])
        elif re.match(r"\d+\. ", s):
            flush_p(); flush_q()
            if kind not in (None, "ol"): flush_l()
            kind = "ol"; lst.append(re.sub(r"^\d+\. ", "", s))
        else:
            flush_l(); flush_q(); para.append(s)
        i += 1
    flush_all()
    return "\n".join(out)


def parse(path):
    raw = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    if not raw.startswith("---\n"):
        raise ValueError("missing front matter (the block between --- lines at the top)")
    head, _, body = raw[4:].partition("\n---")
    meta = {}
    for line in head.split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip()
    return meta, body.lstrip("\n")


def load_posts():
    groups = json.load(open(os.path.join(POSTS_DIR, "groups.json"), encoding="utf-8"))
    keys = [g["key"] for g in groups]
    if "more" not in keys:
        groups.append({"key": "more", "name": "More writing", "sub": ""})
    posts, problems = [], []
    for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
        name = os.path.basename(path)
        if name.startswith("_"):
            continue
        stem = name[:-3]
        dm = re.match(r"^(\d{4})-(\d{2})-(\d{2})-(.+)$", stem)
        slug, date = stem, None
        if dm:
            try:
                date = datetime.date(int(dm.group(1)), int(dm.group(2)), int(dm.group(3)))
                slug = dm.group(4)
            except ValueError:
                problems.append("%s: not a valid date in the file name" % name)
        try:
            meta, body = parse(path)
        except ValueError as e:
            problems.append("%s: %s" % (name, e)); continue
        if meta.get("date"):
            try:
                date = datetime.date.fromisoformat(meta["date"])
            except ValueError:
                problems.append("%s: 'date' must look like 2019-08-01" % name)
        if date is None:
            problems.append("%s: no date. Name it YYYY-MM-DD-slug.md (using today's date for now)" % name)
            date = datetime.date.today()
        for req in ("title", "dek"):
            if not meta.get(req):
                problems.append("%s: front matter needs a '%s' line" % (name, req))
        g = meta.get("group", "more")
        if g not in [x["key"] for x in groups]:
            problems.append("%s: unknown group '%s' (using 'more'). Known: %s" % (name, g, ", ".join(keys)))
            g = "more"
        band = meta.get("band", "b-navy")
        if band not in BANDS:
            problems.append("%s: band '%s' not one of %s (using b-navy)" % (name, band, ", ".join(sorted(BANDS))))
            band = "b-navy"
        hl = meta.get("highlight", "olive")
        if hl not in HIGHLIGHTS:
            hl = "olive"
        try:
            order = float(meta.get("order", "999"))
        except ValueError:
            order = 999
        posts.append(dict(
            slug=slug, date=date, title=meta.get("title", slug), dek=meta.get("dek", ""), group=g, order=order,
            band=band, hl=hl, org=meta.get("where", ""), when=meta.get("when", ""),
            stack=[s.strip() for s in meta.get("tools", "").split(",") if s.strip()],
            featured=meta.get("featured", "no").lower() in ("yes", "true", "1"), body=body))
    return groups, posts, problems


# ------------------------------------------------------------------ templates
def nav(current):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return '<li><a class="l" href="%s"%s>%s</a></li>' % (href, cur, label)
    return """<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap">
<a class="brand" href="../index.html">Sibtain Raza</a>
<button class="menu" id="menuBtn" aria-expanded="false" aria-controls="navLinks">Menu</button>
<ul id="navLinks">
%s
%s
%s
%s
%s
</ul></div></header>""" % (
        a("../index.html#journey", "Journey", "j"), a("../index.html#work", "Work", "w"),
        a("index.html", "Writing", "blog"), a("../index.html#toolbox", "Toolbox", "t"),
        a("../index.html#contact", "Contact", "c"))


NAVJS = """<script>
(function(){var b=document.getElementById('menuBtn'),l=document.getElementById('navLinks');
b.addEventListener('click',function(){var o=l.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');});
l.addEventListener('click',function(e){if(e.target.closest('a')){l.classList.remove('open');b.setAttribute('aria-expanded','false');}});})();
</script>"""

FOOT = """<footer class="foot"><div class="wrap">
<div class="row">
<a class="btn solid" href="../index.html">Back to the portfolio</a>
<a class="btn" href="index.html">All posts</a>
<a class="btn" href="https://www.linkedin.com/in/sibt-ain/" rel="noopener">LinkedIn</a>
<a class="btn" href="mailto:sibt.rj@gmail.com">Email me</a>
</div>
<p>Sibtain Raza, from Shakargarh, Punjab. Based in Islamabad, Pakistan.</p>
</div></footer>"""


def head(title, desc):
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#08122a">
%s
%s
<link rel="stylesheet" href="blog.css">
</head><body>""" % (html.escape(title), html.escape(desc, quote=True), FAVICON, FONTS)


def fmt(d):
    return d.strftime("%B %Y")


def build():
    groups, posts, problems = load_posts()
    gname = {g["key"]: g["name"] for g in groups}
    posts.sort(key=lambda p: (p["date"], p["title"].lower()), reverse=True)  # newest first
    os.makedirs(OUT, exist_ok=True)
    for old in glob.glob(os.path.join(OUT, "*.html")):
        os.remove(old)

    for i, p in enumerate(posts):
        words = len(re.sub(r"[#*`\-]", " ", p["body"]).split())
        mins = max(2, math.ceil(words / 210))
        prev = posts[i - 1] if i > 0 else None
        nxt = posts[i + 1] if i < len(posts) - 1 else None
        pn = ""
        if prev or nxt:
            pn = '<nav class="pn" aria-label="More posts"><div class="wrap">'
            pn += ('<a href="%s.html"><small>Newer post</small><span>%s</span></a>' % (prev["slug"], html.escape(prev["title"].split(":")[0])) if prev else "<div></div>")
            pn += ('<a href="%s.html"><small>Older post</small><span>%s</span></a>' % (nxt["slug"], html.escape(nxt["title"].split(":")[0])) if nxt else "<div></div>")
            pn += "</div></nav>"
        glance = "<dt>Date</dt><dd>%s</dd>" % fmt(p["date"])
        if p["group"] != "more": glance += "<dt>Topic</dt><dd>%s</dd>" % html.escape(gname[p["group"]])
        if p["org"]: glance += "<dt>Where</dt><dd>%s</dd>" % html.escape(p["org"])
        if p["when"]: glance += "<dt>When</dt><dd>%s</dd>" % html.escape(p["when"])
        if p["stack"]: glance += "<dt>Tools</dt><dd><ul>%s</ul></dd>" % "".join("<li>%s</li>" % html.escape(s) for s in p["stack"])
        glance += "<dt>Reading time</dt><dd>%d minutes</dd>" % mins
        page = head("%s | Sibtain Raza" % p["title"], p["dek"]) + nav("blog") + """
<main id="main">
<section class="phead %s"><div class="wrap">
<p class="metaline"><a class="crumb" href="index.html">Writing</a><time datetime="%s">%s</time></p>
<h1 class="disp">%s</h1>
<p class="dek">%s</p>
</div></section>
<article class="post h-%s"><div class="wrap grid">
<aside class="glance" aria-label="Project at a glance"><dl>%s</dl></aside>
<div class="prose">
%s
</div>
</div></article>
%s
</main>
%s
%s
</body></html>""" % (p["band"], p["date"].isoformat(), fmt(p["date"]), html.escape(p["title"]), html.escape(p["dek"]), p["hl"], glance, render(p["body"]), pn, FOOT, NAVJS)
        with open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(page)

    # blog index, grouped by year (newest first)
    gh = ""
    for y in sorted({p["date"].year for p in posts}, reverse=True):
        rows = "".join(
            '<a class="row-a" href="%s.html"><span class="t">%s</span><span class="d">%s</span><span class="y">%s</span></a>'
            % (p["slug"], html.escape(p["title"]), html.escape(p["dek"]), fmt(p["date"]))
            for p in posts if p["date"].year == y)
        gh += '<section class="grp"><h2>%d</h2>%s</section>' % (y, rows)
    idx = head("Writing | Sibtain Raza", "Write-ups of the projects behind my portfolio.") + nav("blog") + """
<main id="main">
<section class="phead b-navy"><div class="wrap">
<a class="crumb" href="../index.html">Portfolio</a>
<h1 class="disp">Writing</h1>
<p class="dek">%d write-ups, one for each project on my resume and LinkedIn. How things work, what I built, and what I would tell someone starting out.</p>
</div></section>
<div class="idx"><div class="wrap">%s</div></div>
</main>
%s
%s
</body></html>""" % (len(posts), gh, FOOT, NAVJS)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx)

    # Writing section on the portfolio home page
    feat = [p for p in posts if p["featured"]][:6] or posts[:6]
    rows = "".join(
        '<a class="row-a" href="blog/%s.html"><span class="t">%s</span><span class="d">%s</span><span class="y">%s</span></a>'
        % (p["slug"], html.escape(p["title"]), html.escape(p["dek"]), fmt(p["date"])) for p in feat)
    block = ('<p class="intro">%d write-ups, one for each project on my resume and LinkedIn. Here are %s to start with.</p>\n'
             '    <div class="wlist">%s</div>\n'
             '    <p class="all"><a class="btn solid" href="blog/index.html">Read all %d posts</a></p>'
             % (len(posts), {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}.get(len(feat), str(len(feat))), rows, len(posts)))
    s = open(INDEX, encoding="utf-8").read()
    pat = re.compile(r"(<!-- WRITING:START[^>]*-->)(.*?)(<!-- WRITING:END -->)", re.S)
    if pat.search(s):
        s = pat.sub(lambda m: m.group(1) + "\n    " + block + "\n    " + m.group(3), s)
        open(INDEX, "w", encoding="utf-8").write(s)
    else:
        problems.append("index.html has no WRITING:START / WRITING:END markers, so its Writing section was not updated")

    print("Built %d posts into blog/." % len(posts))
    for pr in problems:
        print("  note:", pr)


def slugify(t):
    s = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return s[:70].strip("-") or "new-post"


def new(title):
    slug = datetime.date.today().isoformat() + "-" + slugify(title)
    path = os.path.join(POSTS_DIR, slug + ".md")
    if os.path.exists(path):
        sys.exit("posts/%s.md already exists" % slug)
    tpl = open(os.path.join(POSTS_DIR, "_template.md"), encoding="utf-8").read()
    tpl = tpl.replace("title: Your post title", "title: " + title, 1)
    open(path, "w", encoding="utf-8").write(tpl)
    print("Created posts/%s.md. Rename its date prefix if the project is from earlier years, edit it, then run: python build.py" % slug)


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "new":
        new(" ".join(sys.argv[2:]))
    elif len(sys.argv) == 1:
        build()
    else:
        print(__doc__)
