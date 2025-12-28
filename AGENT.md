# AGENT.md — Topology2Drawio + Cisco-Lab + Moodle GIFT Generator

## Zweck
Dieser Agent nimmt **textuelle Beschreibungen einer Netzwerktopologie** entgegen und liefert pro Topologie:

1) eine **Draw.io / diagrams.net** Datei (`.drawio` bzw. `.xml`)  
2) einen **PNG-Export** der Zeichnung  
3) eine **Cisco-Lab-ähnliche Übung** als **Markdown** (`.md`)  
4) einen **PDF-Export** der Übung (`.pdf`)  
5) **Testaufgaben im Moodle GIFT Format** basierend auf der Lab-Beschreibung (`.gift`) in einem separaten Verzeichnis

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
- optional: `out/<name>/meta.json` (zusammengefasste Annahmen, Mapping, Checks)
- `out/<name>/gift/quiz.gift` (Moodle GIFT)
- optional aufgeteilt: `out/<name>/gift/questions_*.gift`

---

## Kernfähigkeiten

### 1) Topologie → Draw.io (Render)
Der Agent konvertiert Geräte & Links in eine **drawio XML** (diagrams.net) Datei.

**Layout-Regeln (Default, deterministisch):**
- Geräte werden nach Rolle gruppiert: Core / Distribution / Access / Edge / WAN / Hosts
- Links werden orthogonal geroutet, soweit möglich
- Interface-Labels: `Gig0/0 10.0.12.1/30` etc.
- VLAN- oder Subnet-Labels als Annotationen (Container/Swimlanes optional)

**Shape-Set:**
- Router/Switch/Firewall/Server/PC als Standard-Draw.io-Netzwerkshapes
- Wenn Cisco-spezifische Icons nicht verfügbar sind, fallback auf generische Netzwerk-Icons

**Validierung:**
- Jede Link-Referenz muss existierende Geräte/Interfaces referenzieren
- IP-Präfixe werden syntaktisch geprüft (CIDR)
- Unklare Angaben werden als Annahmen dokumentiert (siehe `meta.json`)

### 2) Draw.io → PNG (Export)
Der Agent exportiert die Draw.io Datei nach PNG via CLI.

**Bevorzugtes Tooling (in dieser Reihenfolge):**
1) `drawio` CLI (diagrams.net / draw.io Desktop)
2) `npx @drawio/drawio-export` (Headless Export)
3) Headless Chromium + diagrams.net export endpoint (nur wenn lokal verfügbar)

Export-Parameter:
- Hintergrund: weiß (oder transparent optional)
- Maßstab: 2x (Default)
- Rand: 20px

### 3) Cisco-Lab-Übung als Markdown (Generierung)
Der Agent erzeugt pro Topologie eine Übung im Stil eines Cisco-Labs mit:

- **Zielsetzung / Szenario**
- **Topologie** (Referenz auf PNG)
- **Adressierungsplan**
- **VLAN-/Trunk-/STP-Plan** (wenn Switches vorkommen)
- **Routing-Anforderungen** (Static/OSPF/EIGRP/BGP je nach Eingabe)
- **Security/Services** (ACL, NAT, DHCP, DNS optional)
- **Aufgaben** (Step-by-step)
- **Verifikation** (show commands, ping/traceroute)
- **Troubleshooting-Hinweise**
- **Lösungsskizze** (optional: „Instructor Notes“ Abschnitt)

**Regeln:**
- Keine erfundenen Geräte/Netze ohne Kennzeichnung.
- Wenn Informationen fehlen, wählt der Agent plausible Defaults (z. B. /30 auf P2P) und dokumentiert sie.
- Befehle sind IOS/IOSv-typisch, mit klarer Device-Prompt-Konvention.

### 4) Markdown → PDF (Export)
Der Agent exportiert die Übung als PDF.

**Bevorzugtes Tooling:**
1) `pandoc` + `xelatex` (oder `lualatex`)
2) `wkhtmltopdf` (HTML-Weg)
3) Python `reportlab` als Fallback (Layout einfacher)

**PDF-Layout:**
- Titel, Datum, Topologiename
- PNG wird eingebettet (skalieren auf Seitenbreite)
- Codeblöcke monospaced
- Seitenzahlen

### 5) Lab → Moodle GIFT (Quiz-Generierung)
Der Agent generiert auf Basis von `lab.md` ein Set von Testaufgaben im **Moodle GIFT Format** und legt diese unter `out/<name>/gift/` ab.

#### 5.1 Umfang & Mischung (Default)
Pro Topologie standardmäßig **10–20 Fragen**, verteilt auf:
- **Multiple Choice (Single Answer)**
- **Multiple Choice (Multiple Answers)**
- **True/False**
- **Short Answer** (kurze Kommandos / Begriffe)
- **Matching** (z. B. Interface ↔ IP / VLAN ↔ Zweck)
- Optional: **Numerical** (z. B. Hostanzahl/Subnetzmaske), wenn eindeutig ableitbar

#### 5.2 Ableitungslogik (Quellen)
Fragen werden nur aus Inhalten generiert, die in `lab.md` eindeutig vorkommen:
- IP-Netze, Interfaces, VLAN-IDs, Routing-Protokoll (Area/AS), NAT/ACL/DHCP etc.
- geforderte Verifikationskommandos (`show`, `ping`, `traceroute`)
- typische Fehlerbilder aus dem Troubleshooting-Abschnitt

Fehlende Informationen → keine „Ratespiele“:
- generische Konzepte sind erlaubt, **wenn** sie durch Lab-Inhalte getriggert sind (z. B. wenn `show ip route` im Lab vorkommt)
- keine erfundenen IPs/VLANs/Gerätenamen

#### 5.3 GIFT-Konventionen (Agent-Regeln)
- Jede Frage hat einen eindeutigen Titel:
  - `:: <name> - Q01 - OSPF Neighbor ::`
- Antworten:
  - richtig: `=`
  - falsch: `~`
- Optional kurzes Feedback:
  - `# ...`
- Escaping: `:` `~` `=` `{` `}` bei Bedarf mit `\` escapen
- Keine Markdown-Fences im GIFT (Moodle-Import kann das je nach Filter stören)

#### 5.4 Ausgabe-Dateien
- Standard: `out/<name>/gift/quiz.gift`
- Optional bei vielen Fragen: Split nach Typ:
  - `mcq.gift`, `tf.gift`, `short.gift`, `match.gift`

---

## Ablauf (Pipeline)

### Schritt 0 — Arbeitsverzeichnis
- Erstelle `out/<name>/`
- Schreibe Rohinput nach `out/<name>/input.txt` oder `input.yaml`

### Schritt 1 — Parsing & Normalisierung
- Extrahiere: Geräte, Rollen, Interfaces, IPs, Links, Anforderungen
- Normalisiere in ein internes Modell `TopologyModel`

### Schritt 2 — Diagramm-Erzeugung
- Mappe Geräte → Shapes
- Mappe Links → Connectors mit Labels
- Schreibe `diagram.drawio`

### Schritt 3 — PNG Export
- Exportiere `diagram.drawio` → `diagram.png`
- Wenn Export scheitert: Fehler + konkrete Installationshinweise ausgeben

### Schritt 4 — Lab Markdown
- Generiere `lab.md`
- Referenziere das PNG relativ: `![Topologie](diagram.png)`

### Schritt 5 — PDF Export
- Exportiere `lab.md` → `lab.pdf`
- Stelle sicher, dass eingebettete Bilder gefunden werden (Working Dir setzen)

### Schritt 6 — GIFT Quiz
- Parse `lab.md` (Abschnittsüberschriften, Tabellen, Listen)
- Extrahiere Fakten (Devices, IPs, VLANs, Protokolle, Tasks, Verify-Commands)
- Generiere Fragenpool + Lösungen
- Schreibe `out/<name>/gift/quiz.gift`

### Schritt 7 — Ergebnisbericht
- Gib Pfade aller Artefakte aus
- Liste Annahmen & Validierungswarnungen

---

## Installations- und Laufzeitvoraussetzungen

### Minimal
- Node.js (für `@drawio/drawio-export`) **oder** installierte draw.io/diagrams.net CLI
- Python 3.10+
- `pandoc` (für PDF-Export)

### Empfohlen
- `drawio` CLI im PATH
- `pandoc` + `texlive-xetex` (oder `texlive-full`)
- optional: `wkhtmltopdf` als PDF-Fallback

---

## CLI-Kommandos (Referenz)

### drawio → png (Beispiel)
```bash
drawio --export --format png --scale 2 --border 20   --output out/<name>/diagram.png out/<name>/diagram.drawio
```

### markdown → pdf (pandoc)
```bash
pandoc out/<name>/lab.md -o out/<name>/lab.pdf   --pdf-engine=xelatex   -V geometry:margin=1in
```

---

## Qualitätskriterien (Acceptance Criteria)

1) **Diagramm korrekt**: alle Geräte/Links aus der Beschreibung sind enthalten  
2) **PNG erzeugt**: Datei existiert und ist nicht leer  
3) **Lab vollständig**: enthält Ziele, Aufgaben, Verifikation, Adressplan  
4) **PDF erzeugt**: enthält eingebettete Topologie-Grafik und Codeblöcke  
5) **GIFT erzeugt**:
   - importierbar in Moodle (keine Syntaxfehler)
   - mindestens 10 Fragen (Default)
   - Antworten konsistent mit Lab-Inhalten  
6) **Nachvollziehbarkeit**: Annahmen sind dokumentiert (`meta.json` oder Abschnitt im Lab)

---

## Fehlerbehandlung

- **Unbekannte Geräte/Typen** → generischer „Network Device“-Shape + Warnung
- **Fehlende Interface-Namen** → automatische Zuweisung (`Gig0/0`, `Gig0/1`, …) + Warnung
- **Ungültige CIDR/IP** → als Textlabel übernehmen + Warnung, keine „Korrektur“ erfinden
- **Export-Tool fehlt** → klare Installationsanweisung + Abbruch (kein stilles Weiterlaufen)
- **GIFT-Parsing-Probleme** → Escaping anwenden, ggf. Fragenanzahl reduzieren + Warnung

---

## Inhaltsschablone für das Lab (Markdown)

- `# <Topologiename> — Cisco Lab`
- `## Szenario`
- `## Topologie`
  - Bild: `![Topologie](diagram.png)`
- `## Adressierungsplan`
- `## Anforderungen`
- `## Aufgaben`
  1. Basis-Konfiguration (Hostname, SSH, Passwörter)
  2. Interface-IPs
  3. Routing (z. B. OSPF)
  4. Optional: VLAN/Trunk/STP / ACL / NAT / DHCP
- `## Verifikation`
  - `show ip int brief`, `show ip route`, `show ip ospf neighbor`, `ping`, `traceroute`
- `## Troubleshooting`
- `## Lösungsskizze (optional)`

---

## GIFT-Beispiele (Mini)

### Multiple Choice (single)
```
::branch-hq-ospf - Q01 - Routing-Protokoll::
Welches Routing-Protokoll wird in dieser Übung verwendet? {
=OSPF #Richtig.
~EIGRP #Wird hier nicht verwendet.
~BGP #Wird hier nicht verwendet.
~Static Routing #Nicht gefordert.
}
```

### True/False
```
::branch-hq-ospf - Q02 - OSPF Area::
OSPF wird in Area 0 konfiguriert. {T}
```

### Matching
```
::branch-hq-ospf - Q03 - Interface-IP Matching::
Ordne Interface und IP-Adresse korrekt zu. {
=R1 Gig0/0 -> 10.0.12.1/30
=R2 Gig0/0 -> 10.0.12.2/30
=R1 Gig0/1 -> 192.168.10.1/24
=R2 Gig0/1 -> 192.168.20.1/24
}
```

---

## Sicherheits- und Scope-Grenzen
- Der Agent generiert **keine** exploit-orientierten Anleitungen.
- Keine echten Credentials; Beispielpasswörter nur als Platzhalter.
- Fokus: Training, Konfiguration, Verifikation, Troubleshooting.

---

**Abschließend wird das README.md ergänzt oder erstellt**

