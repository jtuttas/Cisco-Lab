# Cisco Lab - Router-on-a-Stick VLAN Konfiguration

Dieses Repository enthält eine vollständige Lernsituation für die Konfiguration von VLANs mit Router-on-a-Stick Technik in Cisco Packet Tracer.

## Übersicht

Die Lernsituation behandelt die Einrichtung eines Unternehmensnetzwerks mit mehreren VLANs für verschiedene Abteilungen. Das Netzwerk verwendet die Router-on-a-Stick-Technik für Inter-VLAN-Routing über einen einzelnen Router-Port.

### Netzwerkkomponenten

- **1x Cisco 4331 Router** (R-Kiesel) - Router-on-a-Stick Konfiguration
- **3x Cisco Switches** (S1, S2, S3) - Core/Distribution und Access Layer
- **4x VLANs** mit unterschiedlichen Subnetzgrößen

### VLANs

| VLAN | Name       | Zweck                  | Netzwerk       | Hosts |
|------|------------|------------------------|----------------|-------|
| 10   | Management | IT/Netz-Admin          | 10.10.10.0/27  | 30    |
| 20   | Office     | Vertrieb/HR/Backoffice | 10.10.20.0/24  | 254   |
| 30   | Dev        | Entwicklung/Produktion | 10.10.30.0/25  | 126   |
| 40   | Guest      | Gäste/extern           | 10.10.40.0/26  | 62    |

## Inhalt des Repositories

### Lernsituation Ausgangsmaterial

- **`Lernsituation-IT.txt`** - Ursprüngliche textuelle Beschreibung der Topologie mit VLAN-Plan und Konfigurationen

### Generierte Lernmaterialien

Das Verzeichnis `out/vlan-router-on-stick/` enthält alle generierten Materialien:

#### 1. Topologie-Diagramme
- **`diagram.drawio`** - Draw.io/diagrams.net Quelldatei (editierbar)
- **`diagram.svg`** - SVG-Vektorgrafik der Topologie
- **`diagram.png`** - PNG-Export für Präsentationen

#### 2. Lab-Übung
- **`lab.md`** - Vollständige Cisco Lab Übung im Markdown-Format
  - Szenario und Lernziele
  - Topologie-Diagramm
  - Detaillierter Adressierungsplan
  - Schritt-für-Schritt Konfigurationsanleitungen
  - Verifikations- und Troubleshooting-Abschnitte
  - Optionale Erweiterungen
- **`lab.pdf`** - PDF-Export der Lab-Übung (druckfertig)

#### 3. Moodle-Quiz
- **`gift/quiz.gift`** - Testaufgaben im Moodle GIFT Format
  - 28 Fragen verschiedener Typen
  - Multiple Choice (Single/Multiple Answer)
  - True/False Fragen
  - Short Answer (Kurzantworten)
  - Matching (Zuordnungsaufgaben)
  - Numerical (Numerische Fragen)
  - Essay (Offene Fragen)

## Verwendung

### Für Lehrende

1. **Lab-Durchführung:**
   - Öffnen Sie `out/vlan-router-on-stick/lab.pdf` für die vollständige Übungsanleitung
   - Die Konfigurationsbefehle können direkt in Cisco Packet Tracer kopiert werden
   - Zeitplanung: ca. 75 Minuten

2. **Moodle-Integration:**
   - Importieren Sie `out/vlan-router-on-stick/gift/quiz.gift` in Moodle
   - Die Fragen sind kategorisiert und sofort einsatzbereit
   - Automatische Bewertung für die meisten Fragentypen

3. **Präsentationen:**
   - Nutzen Sie `diagram.png` oder `diagram.svg` für Präsentationen
   - Die Draw.io Datei kann nach Bedarf angepasst werden

### Für Lernende

1. **Vorbereitung:**
   - Installieren Sie Cisco Packet Tracer
   - Lesen Sie das Szenario in `lab.md` oder `lab.pdf`
   - Überprüfen Sie die Topologie im Diagramm

2. **Durchführung:**
   - Folgen Sie den Aufgaben 1-5 in der angegebenen Reihenfolge
   - Nutzen Sie die Verifikations-Befehle zur Selbstkontrolle
   - Konsultieren Sie den Troubleshooting-Abschnitt bei Problemen

3. **Selbsttest:**
   - Die GIFT-Fragen können zur Selbstüberprüfung verwendet werden
   - Kontrollieren Sie Ihr Verständnis der Konzepte

## Lernziele

Nach Abschluss dieser Übung können Sie:

- ✅ VLANs auf Cisco Switches erstellen und benennen
- ✅ Trunk-Ports zwischen Switches und Routern konfigurieren
- ✅ Access-Ports VLANs zuordnen
- ✅ Router-on-a-Stick mit Subinterfaces einrichten
- ✅ Inter-VLAN Routing implementieren
- ✅ VLAN-Konfigurationen mit show-Befehlen verifizieren
- ✅ Netzwerk-Konnektivität testen und Fehler beheben
- ✅ Unterschiedliche Subnetzgrößen effizient nutzen

## Voraussetzungen

### Software
- **Cisco Packet Tracer** (Version 7.3 oder höher)
- Optional: Moodle für das Quiz

### Kenntnisse
- Grundlagen der Cisco IOS CLI
- Grundverständnis von VLANs und Trunking
- IP-Adressierung und Subnetting
- Grundlagen des IP-Routing

## Technische Details

### Topologie-Architektur

```
                    R-Kiesel (Cisco 4331)
                    G0/0/0 (Trunk)
                           |
                    S1 (Core/Distribution)
                    Gi0/1, Fa0/1, Fa0/2
                      /          \
                     /            \
              S2 (Access)    S3 (Access)
              Etage 2        Etage 3
```

### Trunk-Verbindungen
- R-Kiesel G0/0/0 ↔ S1 Gi0/1 (VLAN 10,20,30,40)
- S1 Fa0/1 ↔ S2 Fa0/1 (VLAN 10,20,30,40)
- S1 Fa0/2 ↔ S3 Fa0/2 (VLAN 10,20,30,40)

### Router Subinterfaces
- G0/0/0.10: 10.10.10.1/27 (VLAN 10 Gateway)
- G0/0/0.20: 10.10.20.1/24 (VLAN 20 Gateway)
- G0/0/0.30: 10.10.30.1/25 (VLAN 30 Gateway)
- G0/0/0.40: 10.10.40.1/26 (VLAN 40 Gateway)

## Generierung der Materialien

Diese Lernmaterialien wurden gemäß der AGENT.md Spezifikation generiert:

1. **Parsing**: Extraktion der Topologie-Informationen aus `Lernsituation-IT.txt`
2. **Diagramm-Erzeugung**: Erstellung der Draw.io und SVG Dateien
3. **PNG Export**: Konvertierung mit Inkscape
4. **Lab-Generierung**: Erstellung der vollständigen Markdown-Übung
5. **PDF Export**: Konvertierung mit Pandoc und XeLaTeX
6. **GIFT Quiz**: Generierung der Testaufgaben basierend auf Lab-Inhalten

## Erweiterungsmöglichkeiten

Die Übung bietet optionale Erweiterungen für fortgeschrittene Lernende:

1. **Separates Native VLAN** (VLAN 99) - Best Practice
2. **DHCP-Server** auf dem Router für automatische IP-Zuweisung
3. **Port Security** auf Access-Ports
4. **Access Control Lists (ACLs)** zur Einschränkung des Guest-VLANs

## Bewertung

### Bewertungskriterien
- **40%** - Korrekte VLAN-Konfiguration auf allen Switches
- **30%** - Funktionierende Router-on-a-Stick Konfiguration
- **20%** - Erfolgreiche Inter-VLAN Kommunikation
- **10%** - Dokumentation und Verifikation

### Häufige Fehler
- Vergessen, das Hauptinterface G0/0/0 zu aktivieren
- Falsche VLAN-IDs bei der dot1Q Encapsulation
- Access-Ports versehentlich als Trunk konfiguriert
- Falsche Subnetzmasken bei PC-Konfiguration
- Gateway bei PCs nicht gesetzt

## Lizenz

Dieses Lernmaterial ist für Bildungszwecke frei verfügbar.

## Support und Feedback

Bei Fragen oder Verbesserungsvorschlägen bitte ein Issue im Repository erstellen.

---

**Dokumentversion:** 1.0  
**Letzte Aktualisierung:** 28. Dezember 2025  
**Erstellt mit:** Cisco Lab Generator (gemäß AGENT.md Spezifikation)  
**Zielplattform:** Cisco Packet Tracer
