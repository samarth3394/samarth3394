import random, math

SANS = "'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', Consolas, 'Courier New', monospace"

# ───────────────────────── HEADER ─────────────────────────
random.seed(11)
W, H = 1200, 320
nodes = []
while len(nodes) < 40:
    x, y = random.randint(25, 1175), random.randint(20, 300)
    if 50 < x < 780 and 60 < y < 285:   # keep text area clean
        continue
    nodes.append((x, y))
edges = []
for i, a in enumerate(nodes):
    for j in range(i + 1, len(nodes)):
        b = nodes[j]
        if math.dist(a, b) < 150:
            edges.append((a, b))

net = ""
for k, (a, b) in enumerate(edges):
    net += (f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#7c83ff" stroke-width="1" '
            f'stroke-dasharray="3 7" opacity=".55"><animate attributeName="stroke-dashoffset" from="0" to="-40" '
            f'dur="{2+k%4}s" repeatCount="indefinite"/></line>\n')
for k, (x, y) in enumerate(nodes):
    col = ["#22d3ee", "#a78bfa", "#f472b6"][k % 3]
    net += (f'<circle cx="{x}" cy="{y}" r="3" fill="{col}"><animate attributeName="opacity" values=".25;1;.25" '
            f'dur="{2+(k%5)*.7:.1f}s" begin="{(k%7)*.3:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="r" values="2;4.5;2" dur="{2+(k%5)*.7:.1f}s" begin="{(k%7)*.3:.1f}s" repeatCount="indefinite"/></circle>\n')

header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Samarth Choudhar - GenAI Developer">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#070514"/><stop offset=".55" stop-color="#14103a"/><stop offset="1" stop-color="#06203a"/>
  </linearGradient>
  <linearGradient id="tg" gradientUnits="userSpaceOnUse" x1="70" y1="0" x2="670" y2="0" spreadMethod="reflect">
    <stop offset="0" stop-color="#a78bfa"/><stop offset=".5" stop-color="#22d3ee"/><stop offset="1" stop-color="#f472b6"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="1200 0" dur="8s" repeatCount="indefinite"/>
  </linearGradient>
  <radialGradient id="orb"><stop offset="0" stop-color="#22d3ee" stop-opacity=".95"/><stop offset=".6" stop-color="#7c3aed" stop-opacity=".6"/><stop offset="1" stop-color="#7c3aed" stop-opacity="0"/></radialGradient>
  <filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <clipPath id="rc"><rect width="{W}" height="{H}" rx="20"/></clipPath>
  <style>
    .f{{opacity:0;animation:fi 1s ease forwards}}
    .s{{opacity:0;transform:translateX(-40px);animation:si 1.1s cubic-bezier(.2,.8,.2,1) forwards}}
    @keyframes fi{{to{{opacity:1}}}}
    @keyframes si{{to{{opacity:1;transform:translateX(0)}}}}
  </style>
</defs>
<g clip-path="url(#rc)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<circle cx="150" cy="40" r="220" fill="#7c3aed" opacity=".12"><animate attributeName="cx" values="150;260;150" dur="12s" repeatCount="indefinite"/></circle>
<circle cx="1050" cy="300" r="260" fill="#06b6d4" opacity=".10"><animate attributeName="cy" values="300;230;300" dur="14s" repeatCount="indefinite"/></circle>
<g>{net}</g>
<g transform="translate(1010,160)">
  <circle r="120" fill="url(#orb)" opacity=".35"><animate attributeName="r" values="105;130;105" dur="4s" repeatCount="indefinite"/></circle>
  <g><circle r="95" fill="none" stroke="#22d3ee" stroke-width="1.5" stroke-dasharray="6 10" opacity=".8"/><circle cx="95" r="6" fill="#22d3ee" filter="url(#glow)"/>
    <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="14s" repeatCount="indefinite"/></g>
  <g><circle r="66" fill="none" stroke="#f472b6" stroke-width="1.5" stroke-dasharray="3 9" opacity=".8"/><circle cx="-66" r="5" fill="#f472b6" filter="url(#glow)"/>
    <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="9s" repeatCount="indefinite"/></g>
  <circle r="34" fill="#0b0820" stroke="#a78bfa" stroke-width="2" filter="url(#glow)"><animate attributeName="stroke-width" values="2;4;2" dur="2.5s" repeatCount="indefinite"/></circle>
  <text text-anchor="middle" y="9" font-family="{SANS}" font-size="26" font-weight="800" fill="url(#tg)">AI</text>
</g>
<text class="f" style="animation-delay:.2s" x="72" y="92" font-family="{MONO}" font-size="20" fill="#22d3ee">&lt;GenAI Developer /&gt;</text>
<text class="s" style="animation-delay:.5s" x="70" y="172" font-family="{SANS}" font-size="68" font-weight="800" fill="url(#tg)" filter="url(#glow)">Samarth Choudhar</text>
<text class="f" style="animation-delay:1.1s" x="73" y="218" font-family="{SANS}" font-size="25" fill="#cbd5e1">Data Scientist  •  AI &amp; ML Engineer</text>
<text class="f" style="animation-delay:1.6s" x="73" y="258" font-family="{MONO}" font-size="18" fill="#94a3b8">RAG  ·  LangChain  ·  LLM Apps  ·  Python  ·  Pune, IN</text>
<rect x="73" y="272" width="0" height="3" rx="2" fill="url(#tg)"><animate attributeName="width" from="0" to="420" dur="1.6s" begin="1.8s" fill="freeze"/></rect>
</g>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="20" fill="none" stroke="#a78bfa" stroke-opacity=".35" stroke-width="2"/>
</svg>'''
open("assets/header.svg", "w", encoding="utf-8").write(header)

# ───────────────────────── TERMINAL ─────────────────────────
FS, CW = 17, 17 * 0.6
entries = [
    ("cmd", "whoami"),
    ("out", "samarth :: GenAI Developer | Data Scientist"),
    ("cmd", "cat focus.txt"),
    ("out", "LLM apps · RAG pipelines · AI agents · ML systems"),
    ("cmd", "./build --ship --production"),
    ("out", "turning ideas into AI products that scale   [ OK ]"),
]
T = 18.0
t = 0.8
body = ""
defs = ""
y0, dy = 96, 34
for i, (kind, txt) in enumerate(entries):
    y = y0 + i * dy
    n = len(txt) + (2 if kind == "cmd" else 0)
    d = max(0.6, n * 0.055)
    full = n * CW + 6
    times = [0.0]
    vals = [0.0]
    for k in range(n + 1):
        times.append(round((t + k * d / n) / T, 5))
        vals.append(round(k * CW, 1))
    hold = round((T - 1.2) / T, 5)
    times.append(hold); vals.append(0)
    # ensure monotonic
    for z in range(1, len(times)):
        if times[z] < times[z-1]: times[z] = times[z-1]
    defs += (f'<clipPath id="c{i}"><rect x="30" y="{y-FS}" height="{FS+10}" width="0">'
             f'<animate attributeName="width" calcMode="discrete" dur="{T}s" repeatCount="indefinite" '
             f'keyTimes="{";".join(map(str,times))}" values="{";".join(map(str,vals))}"/></rect></clipPath>\n')
    if kind == "cmd":
        body += (f'<text x="30" y="{y}" font-family="{MONO}" font-size="{FS}" clip-path="url(#c{i})" xml:space="preserve">'
                 f'<tspan fill="#7ee787">$ </tspan><tspan fill="#e6edf3">{txt}</tspan></text>\n')
    else:
        body += (f'<text x="30" y="{y}" font-family="{MONO}" font-size="{FS}" fill="#79c0ff" clip-path="url(#c{i})">{txt}</text>\n')
    t += d + (0.5 if kind == "cmd" else 0.7)

yc = y0 + len(entries) * dy
appear = round(t / T, 5)
cursor = (f'<g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="{T}s" repeatCount="indefinite" '
          f'keyTimes="0;{appear};{hold};1" values="0;1;0;0"/>'
          f'<text x="30" y="{yc}" font-family="{MONO}" font-size="{FS}" fill="#7ee787">$ </text>'
          f'<rect x="{30+2*CW}" y="{yc-FS+2}" width="{CW}" height="{FS+2}" fill="#e6edf3"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect></g>')

terminal = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {yc+40}" width="900" role="img" aria-label="Animated terminal">
<defs>
<linearGradient id="tb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b2030"/><stop offset="1" stop-color="#151a27"/></linearGradient>
{defs}</defs>
<rect x="1" y="1" width="898" height="{yc+38}" rx="14" fill="#0d1117" stroke="#30363d" stroke-width="2"/>
<path d="M1 15a14 14 0 0 1 14-14h870a14 14 0 0 1 14 14v34H1z" fill="url(#tb)"/>
<circle cx="28" cy="25" r="7" fill="#ff5f56"/><circle cx="52" cy="25" r="7" fill="#ffbd2e"/><circle cx="76" cy="25" r="7" fill="#27c93f"/>
<text x="450" y="30" text-anchor="middle" font-family="{MONO}" font-size="14" fill="#8b949e">samarth@genai: ~/profile</text>
{body}{cursor}
</svg>'''
open("assets/terminal.svg", "w", encoding="utf-8").write(terminal)

# ───────────────────────── SKILLS MARQUEE ─────────────────────────
row1 = [("Python","#3776AB"),("LangChain","#1C9C6B"),("RAG","#a78bfa"),("LLMs","#f472b6"),("OpenAI API","#10a37f"),
        ("Hugging Face","#FFD21E"),("FastAPI","#009688"),("Flask","#e5e7eb"),("Django","#44B78B"),("spaCy","#09A3D5")]
row2 = [("PyTorch","#EE4C2C"),("TensorFlow","#FF6F00"),("scikit-learn","#F7931E"),("Vector DBs","#22d3ee"),("Docker","#2496ED"),
        ("Kubernetes","#326CE5"),("AWS","#FF9900"),("PostgreSQL","#4169E1"),("MongoDB","#47A248"),("Git","#F05032")]

def pills(items, y):
    x, out = 0, ""
    for name, col in items:
        w = int(len(name) * 9.4 + 52)
        out += (f'<g transform="translate({x},{y})"><rect width="{w}" height="42" rx="21" fill="#141a2b" stroke="{col}" stroke-opacity=".7" stroke-width="1.5"/>'
                f'<circle cx="22" cy="21" r="6" fill="{col}"><animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/></circle>'
                f'<text x="38" y="27" font-family="{SANS}" font-size="16" font-weight="600" fill="#e6edf3">{name}</text></g>')
        x += w + 16
    return out, x

def row(items, y, direction, dur):
    p, tw = pills(items, y)
    a, b = (0, -tw) if direction == "l" else (-tw, 0)
    return (f'<g><g>{p}</g><g transform="translate({tw},0)">{p}</g>'
            f'<animateTransform attributeName="transform" type="translate" from="{a} 0" to="{b} 0" dur="{dur}s" repeatCount="indefinite"/></g>')

skills = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 140" width="1200" role="img" aria-label="Tech stack marquee">
<defs>
<linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#000"/><stop offset=".08" stop-color="#fff"/><stop offset=".92" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
<mask id="m"><rect width="1200" height="140" fill="url(#fade)"/></mask>
</defs>
<g mask="url(#m)">{row(row1, 12, "l", 38)}{row(row2, 80, "r", 42)}</g>
</svg>'''
open("assets/skills.svg", "w", encoding="utf-8").write(skills)

# ───────────────────────── DIVIDER ─────────────────────────
divider = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 24" width="1200" role="presentation">
<defs>
<linearGradient id="d" x1="0" x2="1"><stop offset="0" stop-color="#7c3aed" stop-opacity="0"/><stop offset=".5" stop-color="#22d3ee"/><stop offset="1" stop-color="#f472b6" stop-opacity="0"/></linearGradient>
<filter id="g"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect x="0" y="11" width="1200" height="2" fill="url(#d)"/>
<circle cy="12" r="5" fill="#fff" filter="url(#g)"><animate attributeName="cx" values="0;1200" dur="4s" repeatCount="indefinite"/><animate attributeName="fill" values="#22d3ee;#f472b6;#a78bfa;#22d3ee" dur="4s" repeatCount="indefinite"/></circle>
</svg>'''
open("assets/divider.svg", "w", encoding="utf-8").write(divider)

# ───────────────────────── RAG PIPELINE ─────────────────────────
steps = [("Documents","PDF · Web · DB","#a78bfa"),("Chunk + Embed","LangChain","#22d3ee"),("Vector Store","FAISS · Chroma","#34d399"),
         ("Retriever","Hybrid search","#fbbf24"),("LLM","Reason + Generate","#f472b6"),("API / App","FastAPI · Docker","#60a5fa")]
boxes = ""
for i, (a, b, c) in enumerate(steps):
    x = i * 190
    boxes += (f'<g transform="translate({x},40)"><rect width="150" height="84" rx="14" fill="#10162a" stroke="{c}" stroke-width="2">'
              f'<animate attributeName="stroke-width" values="2;5;2;2" keyTimes="0;.06;.18;1" dur="6s" begin="{1.2*i:.1f}s" repeatCount="indefinite"/>'
              f'<animate attributeName="fill" values="#10162a;#1f2747;#10162a;#10162a" keyTimes="0;.06;.18;1" dur="6s" begin="{1.2*i:.1f}s" repeatCount="indefinite"/></rect>'
              f'<text x="75" y="38" text-anchor="middle" font-family="{SANS}" font-size="17" font-weight="700" fill="#f1f5f9">{a}</text>'
              f'<text x="75" y="62" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{c}">{b}</text></g>')
arrows = "".join(f'<path d="M{i*190+156} 82 L{i*190+184} 82" stroke="#475569" stroke-width="2" marker-end="url(#ah)"/>' for i in range(5))
rag = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 0 1180 170" width="1100" role="img" aria-label="Animated RAG pipeline">
<defs>
<marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0L8 4L0 8z" fill="#64748b"/></marker>
<filter id="g"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<path id="p" d="M75 82 L1025 82" stroke="#1e293b" stroke-width="2" stroke-dasharray="2 6"/>
{arrows}{boxes}
<circle r="7" fill="#22d3ee" filter="url(#g)"><animateMotion dur="6s" repeatCount="indefinite"><mpath href="#p"/></animateMotion></circle>
<circle r="5" fill="#f472b6" filter="url(#g)"><animateMotion dur="6s" begin="-3s" repeatCount="indefinite"><mpath href="#p"/></animateMotion></circle>
<text x="560" y="158" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#64748b">retrieve  →  augment  →  generate</text>
</svg>'''
open("assets/rag-pipeline.svg", "w", encoding="utf-8").write(rag)
print("ok")
