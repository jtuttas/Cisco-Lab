# Cisco Network Labs

Willkommen zu den Cisco Network Labs! Diese Sammlung enthält Lernsituationen und praktische Übungen für Cisco Netzwerktechnologien.

## Über diese Labs

Diese Labs sind entwickelt, um praktische Erfahrungen mit Cisco-Netzwerkgeräten zu sammeln. Jedes Lab enthält:

- **Detaillierte Topologie-Diagramme** - Visualisierung der Netzwerkstruktur
- **Schritt-für-Schritt Anleitungen** - Konfigurationsaufgaben mit vollständigen Befehlen
- **Adressierungspläne** - IP-Adress- und VLAN-Zuordnungen
- **Verifikationstests** - Methoden zur Überprüfung der Konfiguration
- **Troubleshooting-Tipps** - Hilfe bei häufigen Problemen
- **Quizfragen** - Testaufgaben im Moodle GIFT Format

## Verfügbare Labs

### [VLAN Router-on-a-Stick](labs/vlan-router-on-stick/index.md)

**Thema:** VLANs und Inter-VLAN Routing

**Beschreibung:** Konfiguration eines Netzwerks mit mehreren VLANs und Inter-VLAN Routing über einen Router (Router-on-a-Stick). Das Szenario simuliert eine typische Unternehmensumgebung mit getrennten Netzwerksegmenten für Management, Office, Entwicklung und Gäste.

**Lernziele:**
- VLANs auf Cisco Switches erstellen und konfigurieren
- Trunk-Ports zwischen Switches konfigurieren
- Router-on-a-Stick für Inter-VLAN Routing einrichten
- Subinterfaces mit 802.1Q Encapsulation konfigurieren
- Konnektivität innerhalb und zwischen VLANs testen

**Komponenten:**
- 1 Router (Cisco 4331)
- 1 Core/Distribution Switch
- 2 Access Switches
- 4 VLANs mit unterschiedlichen Subnetzgrößen

**Downloads:**
- [PDF Version](../out/vlan-router-on-stick/lab.pdf)
- [Moodle Quiz (GIFT)](../out/vlan-router-on-stick/gift/quiz.gift)

## Verwendung der Labs

### In Cisco Packet Tracer

1. Öffnen Sie Cisco Packet Tracer
2. Erstellen Sie die Topologie gemäß dem Lab-Diagramm
3. Folgen Sie den Konfigurationsschritten im Lab
4. Verwenden Sie die Verifikationsbefehle, um Ihre Konfiguration zu überprüfen

### Als Lernmaterial

- Lesen Sie das Lab-Dokument durch
- Studieren Sie die Topologie und den Adressierungsplan
- Versuchen Sie, die Konfiguration selbst zu erstellen
- Vergleichen Sie Ihre Lösung mit der bereitgestellten Konfiguration

### Für Kurse und Schulungen

- Importieren Sie die GIFT-Datei in Moodle für automatisierte Tests
- Verwenden Sie die PDF-Version für Handouts
- Nutzen Sie die Diagramme für Präsentationen

## Technologie-Stack

- **Cisco IOS** - Router und Switch Betriebssystem
- **VLANs** - Virtuelle LANs zur Netzwerksegmentierung
- **802.1Q** - VLAN Tagging Protokoll
- **Router-on-a-Stick** - Inter-VLAN Routing Methode
- **Subnetting** - Variable Length Subnet Masking (VLSM)

## Lizenz und Nutzung

Diese Labs sind für Bildungszwecke konzipiert. Verwenden Sie sie frei in Kursen, Schulungen und zum Selbststudium.

## Feedback und Beiträge

Haben Sie Verbesserungsvorschläge oder haben Sie Fehler gefunden? Bitte erstellen Sie ein Issue im [GitHub Repository](https://github.com/jtuttas/Cisco-Lab).

---

*Letzte Aktualisierung: Dezember 2025*
