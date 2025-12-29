# Cisco Network Labs

Willkommen zum Cisco Network Labs Repository! Dieses Repository enthält praxisorientierte Cisco Netzwerk-Übungen mit vollständiger Dokumentation, Diagrammen und Testaufgaben.

## 🌐 GitHub Pages

Die Labs sind auch online verfügbar: **[https://jtuttas.github.io/Cisco-Lab/](https://jtuttas.github.io/Cisco-Lab/)**

## 📚 Verfügbare Labs

<!-- LABS:START -->
### VLAN Router-on-a-Stick Konfiguration

**Beschreibung:** Eine umfassende Übung zur Implementierung von VLANs und Inter-VLAN Routing mit der Router-on-a-Stick Technik. Diese Übung deckt die Konfiguration von VLANs auf Cisco Switches, Trunk- und Access-Ports sowie 802.1Q Subinterfaces ab.

**Themen:**
- VLAN-Konfiguration auf Cisco Switches
- Trunk und Access Ports
- 802.1Q Subinterfaces auf Router
- Inter-VLAN Routing
- Netzwerk-Verifizierung und Troubleshooting

**Ressourcen:**
- 📖 [Lab-Anleitung (Online)](https://jtuttas.github.io/Cisco-Lab/docs/labs/vlan-router-on-stick/)
- 📄 [Lab-Anleitung (PDF)](out/vlan-router-on-stick/lab.pdf)
- 🎯 [Moodle GIFT Quiz](out/vlan-router-on-stick/gift/quiz.gift)
- 🖼️ [Netzwerk-Diagramm (PNG)](out/vlan-router-on-stick/diagram.png)
- 📐 [Netzwerk-Diagramm (Draw.io)](out/vlan-router-on-stick/diagram.drawio)

**Netzwerk-Topologie:**
- 1x Cisco 4331 Router (Router-on-a-Stick)
- 3x Switches (1x Core/Distribution, 2x Access)
- 4 VLANs (Management, Office, Dev, Guest)
- 6x PCs in verschiedenen VLANs

---

### VLAN Router-on-a-Stick - Erweiterte Konfiguration (R-Nova)

**Beschreibung:** Eine fortgeschrittene VLAN-Übung mit erweiterten Sicherheitsfeatures, Voice VLAN, und Best Practices. Diese Übung behandelt die Implementierung von separatem Native VLAN, Management VLAN, Voice VLAN mit QoS, und verschiedenen Subnetzgrößen.

**Themen:**
- Erweiterte VLAN-Konfiguration mit unterschiedlichen Subnetzgrößen
- Sicherheits-Best-Practices (separates Native VLAN, Passwort-Verschlüsselung)
- Voice VLAN mit QoS (Quality of Service)
- Management VLAN (SVI) für Switch-Administration
- Spanning Tree PortFast
- Port Security und ungenutzte Ports
- Umfassende Verifikation und Troubleshooting

**Ressourcen:**
- 📖 [Lab-Anleitung (Online)](https://jtuttas.github.io/Cisco-Lab/docs/labs/vlan-advanced-nova/)
- 📄 [Lab-Anleitung (PDF)](out/vlan-advanced-nova/lab.pdf)
- 🎯 [Moodle GIFT Quiz](out/vlan-advanced-nova/gift/quiz.gift)
- 🖼️ [Netzwerk-Diagramm (PNG)](out/vlan-advanced-nova/diagram.png)
- 📐 [Netzwerk-Diagramm (Draw.io)](out/vlan-advanced-nova/diagram.drawio)

**Netzwerk-Topologie:**
- 1x Cisco 4331 Router (R-Nova)
- 1x Cisco 2960 Switch
- 6 VLANs (Verwaltung, Entwicklung, Vertrieb, Voice, Native, Management)
- 6x PCs + 1x IP-Telefon
- Erweiterte Sicherheitsfeatures und QoS
<!-- LABS:END -->

## 🚀 Schnellstart

### Voraussetzungen

- **Cisco Packet Tracer** (empfohlen für Einsteiger)
- **Cisco VIRL/CML** (für fortgeschrittene Szenarien)
- Oder echte Cisco Hardware

### Repository klonen

```bash
git clone https://github.com/jtuttas/Cisco-Lab.git
cd Cisco-Lab
```

### Labs durcharbeiten

1. Wählen Sie ein Lab aus dem `out/` Verzeichnis
2. Öffnen Sie die Lab-Anleitung (PDF oder Markdown)
3. Folgen Sie den Schritt-für-Schritt-Anleitungen
4. Nutzen Sie die Diagrams zur Orientierung
5. Testen Sie Ihr Wissen mit den GIFT Quiz-Dateien

## 📁 Struktur

```
Cisco-Lab/
├── out/                           # Generierte Lab-Ausgaben
│   └── vlan-router-on-stick/      # VLAN Router-on-a-Stick Lab
│       ├── diagram.drawio         # Netzwerk-Diagramm (editierbar)
│       ├── diagram.png            # Netzwerk-Diagramm (Bild)
│       ├── lab.md                 # Lab-Anleitung (Markdown)
│       ├── lab.pdf                # Lab-Anleitung (PDF)
│       └── gift/
│           └── quiz.gift          # Moodle GIFT Testfragen
├── docs/                          # MkDocs Dokumentation
│   ├── index.md                   # Landing Page
│   └── labs/                      # Lab-Dokumentation
│       └── vlan-router-on-stick/
│           ├── index.md
│           ├── diagram.png
│           ├── lab.pdf
│           └── quiz.gift
├── mkdocs.yml                     # MkDocs Konfiguration
├── .github/
│   └── workflows/
│       └── pages.yml              # GitHub Pages Deployment
└── README.md                      # Diese Datei
```

## 🛠️ Dokumentation lokal anzeigen

### Mit MkDocs

```bash
# MkDocs installieren
pip install mkdocs mkdocs-material pymdown-extensions

# Lokalen Server starten
mkdocs serve

# Im Browser öffnen: http://127.0.0.1:8000
```

### Mit Packet Tracer

1. Öffnen Sie die `.pkt` Datei (falls vorhanden) in Cisco Packet Tracer
2. Oder erstellen Sie die Topologie manuell anhand des Diagramms
3. Kopieren Sie die Konfigurationsbefehle aus der Lab-Anleitung

## 📝 Lab-Komponenten

Jedes Lab enthält:

1. **Diagram.drawio** - Editierbares Netzwerk-Diagramm (diagrams.net)
2. **Diagram.png** - Hochauflösendes Topologie-Bild
3. **Lab.md** - Ausführliche Schritt-für-Schritt-Anleitung
4. **Lab.pdf** - Druckfreundliche PDF-Version
5. **Quiz.gift** - Moodle-importierbare Testfragen

## 🎓 Lernziele

Nach Abschluss dieser Labs können Sie:

- VLANs auf Cisco Switches konfigurieren
- Trunk- und Access-Ports einrichten
- Inter-VLAN Routing implementieren
- Router-on-a-Stick Konfigurationen durchführen
- Netzwerk-Konnektivität testen und verifizieren
- Typische Netzwerkprobleme diagnostizieren und beheben

## 🧪 Moodle GIFT Quiz

Die GIFT-Dateien können direkt in Moodle importiert werden:

1. In Moodle als Administrator/Trainer einloggen
2. Zu Ihrem Kurs navigieren
3. "Fragenkatalog" öffnen
4. "Import" wählen
5. Format "GIFT" auswählen
6. Die `.gift` Datei hochladen

## 📖 Best Practices

Die Labs folgen Cisco Best Practices:

- ✅ Strukturierte VLAN-Benennung
- ✅ Sinnvolle IP-Adressierung mit Subnetting
- ✅ Trunk-Port-Konfiguration mit allowed VLANs
- ✅ Systematische Verifizierung und Testing
- ✅ Dokumentierte Troubleshooting-Schritte

## 🤝 Beitragen

Verbesserungsvorschläge und Beiträge sind willkommen! Bitte öffnen Sie ein Issue oder Pull Request.

## 📄 Lizenz

Diese Übungen dienen ausschließlich zu Schulungszwecken. Die Konfigurationsbeispiele verwenden private IP-Adressen und Platzhalter-Hostnamen.

## 🔗 Links

- [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer)
- [Cisco Learning Network](https://learningnetwork.cisco.com/)
- [Draw.io / diagrams.net](https://www.diagrams.net/)
- [MkDocs](https://www.mkdocs.org/)
- [Moodle GIFT Format](https://docs.moodle.org/en/GIFT_format)

## 📞 Support

Bei Fragen oder Problemen öffnen Sie bitte ein Issue im GitHub Repository.

---

**Viel Erfolg beim Lernen! 🚀**
