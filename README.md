# Cisco Lab - Netzwerk Lernsituationen

Dieses Repository enthält vollständige Lernsituationen und praktische Übungen für Cisco Netzwerktechnologien. Jedes Lab umfasst Diagramme, detaillierte Konfigurationsanleitungen, Testaufgaben und Dokumentation.

## 🎯 Projektübersicht

Das Cisco Lab Projekt bietet:
- **Interaktive Netzwerktopologien** in Draw.io Format
- **Schritt-für-Schritt Lab-Anleitungen** als Markdown und PDF
- **Moodle GIFT Quizfragen** für automatisierte Tests
- **MkDocs Dokumentation** mit GitHub Pages Hosting
- **Praxisnahe Szenarien** für realistische Lernumgebungen

## 🚀 Quickstart

### Voraussetzungen

- Cisco Packet Tracer (für praktische Übungen)
- PDF-Reader (für Lab-Dokumente)
- Web-Browser (für Online-Dokumentation)
- Optional: Moodle-Installation (für Quiz-Import)

### Repository klonen

```bash
git clone https://github.com/jtuttas/Cisco-Lab.git
cd Cisco-Lab
```

### Dokumentation lokal anzeigen

```bash
# MkDocs installieren
pip install mkdocs mkdocs-material

# Lokalen Server starten
mkdocs serve

# Öffnen Sie http://127.0.0.1:8000 im Browser
```

## 📚 Verfügbare Labs

<!-- LABS:START -->
### VLAN Router-on-a-Stick

**Thema:** VLANs und Inter-VLAN Routing

**Beschreibung:** Konfiguration eines Netzwerks mit mehreren VLANs und Inter-VLAN Routing über einen Router (Router-on-a-Stick). Das Szenario simuliert eine typische Unternehmensumgebung mit getrennten Netzwerksegmenten für Management, Office, Entwicklung und Gäste.

**Ressourcen:**
- 📄 [Lab-Anleitung (Markdown)](docs/labs/vlan-router-on-stick/index.md)
- 📑 [Lab-Anleitung (PDF)](out/vlan-router-on-stick/lab.pdf)
- 🖼️ [Topologie-Diagramm](out/vlan-router-on-stick/diagram.png)
- 🎨 [Draw.io Diagramm](out/vlan-router-on-stick/diagram.drawio)
- 📝 [Moodle Quiz (GIFT)](out/vlan-router-on-stick/gift/quiz.gift)

**Lernziele:**
- VLANs erstellen und konfigurieren
- Trunk-Ports einrichten
- Router-on-a-Stick für Inter-VLAN Routing
- 802.1Q Encapsulation auf Subinterfaces
- Konnektivität testen und verifizieren

**Komponenten:**
- 1x Router (Cisco 4331)
- 1x Core/Distribution Switch (S1)
- 2x Access Switches (S2, S3)
- 4x VLANs (Management, Office, Dev, Guest)
<!-- LABS:END -->

## 📖 Online-Dokumentation

Die vollständige Dokumentation ist verfügbar unter:
**https://jtuttas.github.io/Cisco-Lab/**

Die Dokumentation wird automatisch über GitHub Pages bereitgestellt und bei jedem Push auf den `main` Branch aktualisiert.

## 🗂️ Projektstruktur

```
Cisco-Lab/
├── out/                          # Generierte Lab-Artefakte
│   └── vlan-router-on-stick/
│       ├── diagram.drawio        # Draw.io Diagramm
│       ├── diagram.png           # PNG Export
│       ├── lab.md                # Lab-Anleitung (Markdown)
│       ├── lab.pdf               # Lab-Anleitung (PDF)
│       └── gift/
│           └── quiz.gift         # Moodle Quiz
├── docs/                         # MkDocs Dokumentation
│   ├── index.md                  # Startseite
│   └── labs/
│       └── vlan-router-on-stick/
│           ├── index.md          # Lab-Dokumentation
│           └── diagram.png       # Diagramm
├── .github/
│   └── workflows/
│       └── pages.yml             # GitHub Pages Workflow
├── mkdocs.yml                    # MkDocs Konfiguration
├── AGENT.md                      # Agent-Spezifikation
└── README.md                     # Diese Datei
```

## 🛠️ Verwendung der Labs

### In Cisco Packet Tracer

1. Öffnen Sie das Lab-Dokument (PDF oder Markdown)
2. Studieren Sie das Topologie-Diagramm
3. Erstellen Sie die Topologie in Packet Tracer
4. Folgen Sie den Konfigurationsschritten
5. Führen Sie die Verifikationstests durch

### Moodle Quiz importieren

1. Loggen Sie sich in Moodle ein
2. Navigieren Sie zur Fragensammlung
3. Wählen Sie "Import" und Format "GIFT"
4. Laden Sie die `.gift` Datei hoch
5. Die Fragen werden automatisch importiert

### Für Kurse und Schulungen

- Verwenden Sie die PDF-Dateien als Handouts
- Zeigen Sie die Diagramme in Präsentationen
- Nutzen Sie die Online-Dokumentation als Referenz
- Importieren Sie die Quizfragen in Ihr LMS

## 🔧 Technologien

- **Draw.io** - Netzwerk-Diagramme
- **Markdown** - Dokumentation
- **MkDocs** - Statische Website-Generierung
- **ReportLab** - PDF-Generierung
- **Moodle GIFT** - Quiz-Format
- **GitHub Pages** - Hosting
- **Cisco IOS** - Router und Switch Konfiguration

## 📝 Lab-Inhalte

Jedes Lab enthält:

- **Szenario** - Realistische Geschäftsanforderungen
- **Zielsetzung** - Klare Lernziele
- **Topologie** - Visuelle Darstellung des Netzwerks
- **Adressierungsplan** - IP-Adressen und VLANs
- **Aufgaben** - Schritt-für-Schritt Konfigurationsanleitungen
- **Verifikation** - Tests zur Überprüfung der Konfiguration
- **Troubleshooting** - Hilfe bei häufigen Problemen
- **Erweiterte Aufgaben** - Optionale Herausforderungen
- **Quiz** - Testfragen im GIFT-Format

## 🤝 Beiträge

Beiträge sind willkommen! Wenn Sie:
- Fehler finden
- Verbesserungsvorschläge haben
- Neue Labs beitragen möchten

Erstellen Sie bitte ein Issue oder einen Pull Request.

## 📄 Lizenz

Dieses Projekt ist für Bildungszwecke konzipiert. Die Labs können frei in Kursen, Schulungen und zum Selbststudium verwendet werden.

## 👤 Autor

Entwickelt für die IT-Ausbildung und Netzwerk-Training.

## 🔗 Links

- [Online-Dokumentation](https://jtuttas.github.io/Cisco-Lab/)
- [GitHub Repository](https://github.com/jtuttas/Cisco-Lab)
- [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer)
- [MkDocs](https://www.mkdocs.org/)

---

*Generiert mit dem Cisco Lab Generator - Letzte Aktualisierung: Dezember 2025*
