# AGENT.md — Topology2Drawio + Cisco-Lab + Moodle GIFT + MkDocs/GitHub Pages Generator

## Zweck
Dieser Agent nimmt **textuelle Beschreibungen einer Netzwerktopologie** entgegen und liefert pro Topologie:

1) eine **Draw.io / diagrams.net** Datei (`.drawio` bzw. `.xml`)  
2) einen **PNG-Export** der Zeichnung  
3) eine **Cisco-Lab-ähnliche Übung** als **Markdown** (`.md`)  
4) einen **PDF-Export** der Übung (`.pdf`)  
5) **Testaufgaben im Moodle GIFT Format** basierend auf der Lab-Beschreibung (`.gift`)  
6) **Aktualisierung der Projekt-Dokumentation** (`README.md`)  
7) **MkDocs-Rendering** der Labs und **Deployment über GitHub Pages**

Der Agent arbeitet reproduzierbar, dateibasiert und ohne manuelle UI-Schritte.

---

## Ein- und Ausgabeformate

### Eingabe (Topologie-Beschreibung)
Der Agent akzeptiert eine von zwei Formen:

**A) Freitext (robust, ggf. mit dokumentierten Annahmen)**  
- Geräte, Rollen, IPs, VLANs, Links, Routing-Protokolle, Anforderungen

**B) Strukturierte Topologie (bevorzugt)**  
YAML/JSON in Markdown-Codeblock, z. B.:
```yaml
name: "branch-hq-ospf"
devices:
  - id: R1
    type: router
    vendor: cisco
    model: "IOSv"
    role: edge
    interfaces:
      - name: Gig0/0
        ip: 10.0.12.1/30
      - name: Gig0/1
        ip: 192.168.10.1/24
  - id: R2
    type: router
    vendor: cisco
    model: "IOSv"
    role: edge
    interfaces:
      - name: Gig0/0
        ip: 10.0.12.2/30
      - name: Gig0/1
        ip: 192.168.20.1/24
links:
  - a: R1:Gig0/0
    b: R2:Gig0/0
notes:
  routing: "OSPF area 0"
requirements:
  - "End-to-End Reachability zwischen 192.168.10.0/24 und 192.168.20.0/24"
  - "OSPF Single Area, keine Default Route"
```

### Ausgabe (pro Topologie)
Für jede Topologie mit `name` erzeugt der Agent:

- `out/<name>/diagram.drawio`
- `out/<name>/diagram.png`
- `out/<name>/lab.md`
- `out/<name>/lab.pdf`
- optional: `out/<name>/meta.json` (Annahmen, Mapping, Checks)
- `out/<name>/gift/quiz.gift` (Moodle GIFT)

Zusätzlich für die Dokumentations-Site:
- `docs/index.md`
- `docs/labs/<name>/index.md`
- `mkdocs.yml`
- `.github/workflows/pages.yml`
- Aktualisierung von `README.md`

---

## Kernfähigkeiten

### 1) Topologie → Draw.io (Render)
Der Agent konvertiert Geräte & Links in eine **drawio XML** (diagrams.net) Datei. Dabei sollen stets dir offiziellen *CISCO* Shapes / Symbole verwendet werden ! 

**Layout-Regeln (Default, deterministisch):**
- Rollenbasiertes Placement (Core / Distribution / Access / Edge / WAN / Hosts)
- Orthogonale Connectoren
- Interface-Labels: `Gig0/0 10.0.12.1/30`
- VLAN-/Subnetz-Annotationen als Notes/Container

**Validierung:**
- Link-Referenzen müssen existierende Geräte/Interfaces referenzieren
- IP/CIDR syntaktisch prüfen
- Annahmen dokumentieren (`meta.json`)

### 2) Draw.io → PNG (Export)
**Tooling (Reihenfolge):**
1) `drawio` CLI
2) `npx @drawio/drawio-export`
3) Headless Chromium Export (Fallback)

Parameter: Hintergrund weiß, Scale 2, Border 20.

### 3) Cisco-Lab-Übung als Markdown
Das Lab enthält:
- Zielsetzung/Szenario
- Topologie (PNG)
- Adressierungsplan
- Anforderungen
- Aufgaben (Step-by-step)
- Verifikation (show/ping/traceroute)
- Troubleshooting
- optional Lösung

### 4) Markdown → PDF
**Tooling:**
1) `pandoc` + `xelatex`/`lualatex`
2) `wkhtmltopdf`
3) `reportlab` (Fallback)

### 5) Lab → Moodle GIFT
Der Agent generiert auf Basis von `lab.md` ein Moodle-importierbares `quiz.gift`.

**Default:** 10–20 Fragen, Mix aus MCQ, TF, Matching, Short Answer.

---

## README.md stets aktualisieren

### Ziel
Nach jeder Topologie-Generierung wird **README.md** aktualisiert, sodass das Repo als „Landing Page“ stets aktuell ist.

### Inhalt (Konvention)
README enthält mindestens:
- Projektbeschreibung
- Quickstart (Requirements + Commands)
- Index der verfügbaren Labs (automatisch gepflegt)
- Link zur GitHub Pages Site (falls konfiguriert)
- Strukturübersicht (`out/`, `docs/`)

### Aktualisierungslogik
- Der Agent scannt `docs/labs/*/index.md` (oder `out/*/lab.md`) und erzeugt eine Liste:
  - Name
  - Kurzbeschreibung (aus Lab-„Szenario“-Abschnitt, falls vorhanden)
  - Links (Docs/PDF/GIFT)
- Änderungen erfolgen idempotent über Markerblock:
  - `<!-- LABS:START -->` … `<!-- LABS:END -->`
  - Nur dieser Block wird ersetzt.

Beispiel:
```md
<!-- LABS:START -->
- **branch-hq-ospf** — OSPF Single Area, 2 LANs  
  - Docs: docs/labs/branch-hq-ospf/
  - PDF: out/branch-hq-ospf/lab.pdf
  - Quiz: out/branch-hq-ospf/gift/quiz.gift
<!-- LABS:END -->
```

---

## MkDocs Rendering + GitHub Pages Präsentation

### Ziel
Labs werden als Website mit **MkDocs** gerendert und via **GitHub Pages** veröffentlicht.

### MkDocs Setup (Agent verwaltet)
- `mkdocs.yml`
- `docs/index.md`
- `docs/labs/<name>/index.md` pro Lab
- Kopie der Artefakte nach `docs/labs/<name>/`:
  - `diagram.png`
  - optional `lab.pdf`
  - optional `quiz.gift` (oder nur Link)

**Empfehlung:**
- Theme: `material` (oder Standardtheme)
- Extensions: `admonition`, `toc`, `tables`, `fenced_code`

Minimalbeispiel `mkdocs.yml`:
```yaml
site_name: Network Labs
nav:
  - Home: index.md
  - Labs:
      - branch-hq-ospf: labs/branch-hq-ospf/index.md
theme:
  name: material
markdown_extensions:
  - admonition
  - toc:
      permalink: true
  - tables
  - fenced_code
```

### Rendering-Regeln (Lab → docs)
- `out/<name>/lab.md` wird nach `docs/labs/<name>/index.md` kopiert/transformiert
- Bildreferenzen werden so angepasst, dass `diagram.png` lokal im gleichen Ordner liegt
- Optional: Download-Sektion (PDF/GIFT)

### GitHub Pages Deployment (Agent legt Workflow an)
Pfad: `.github/workflows/pages.yml`

Beispiel-Workflow:
```yaml
name: Deploy MkDocs to GitHub Pages
on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - run: pip install mkdocs mkdocs-material
      - run: mkdocs gh-deploy --force
```

### Ergebnis
Nach Push auf `main` ist die Site verfügbar unter:
- `https://<user>.github.io/<repo>/`

README verlinkt diese URL (falls Repo-Name/User bekannt, sonst Platzhalter).

---

## Pipeline (End-to-End)

1. Input erfassen → `out/<name>/input.*`
2. Parsing/Normalisierung → `TopologyModel` + `meta.json`
3. Draw.io generieren → `diagram.drawio`
4. PNG exportieren → `diagram.png`
5. Lab erstellen → `lab.md`
6. PDF exportieren → `lab.pdf`
7. GIFT generieren → `gift/quiz.gift`
8. Docs aktualisieren:
   - `docs/labs/<name>/index.md` + Assets
   - `mkdocs.yml` Navigation idempotent erweitern
9. README aktualisieren (Markerblock)
10. Optional: Commit/Push (falls Agent in Repo/CI läuft)

---

## Qualitätskriterien (Acceptance Criteria)
- Diagramm/PNG/Lab/PDF/GIFT erzeugt und konsistent
- README enthält aktuellen Labs-Index (Markerblock)
- MkDocs baut erfolgreich (`mkdocs build` ohne Fehler)
- GitHub Pages Workflow vorhanden und lauffähig

---

## Sicherheits- und Scope-Grenzen
- Keine exploit-orientierten Anleitungen
- Keine echten Credentials; Platzhalter verwenden
- Fokus: Training, Konfiguration, Verifikation, Troubleshooting
