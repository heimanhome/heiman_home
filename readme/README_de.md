# Heiman Home für HomeAssistant

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## Übersicht

Diese Integration für Home Assistant ermöglicht die Verwendung von Heiman Smart-Home-Geräten in einem Smart-Home-System. Sie verbindet sich mit der Heiman Cloud API und verwendet das MQTT-Protokoll für Echtzeit-Gerätestatusaktualisierungen.

Diese Integration ermöglicht es Benutzern, ihre Heiman-Geräte einfach in Home Assistant zu integrieren und sie für verschiedene Automatisierungen und Überwachungen zu verwenden, einschließlich Firmware-Management und Kindgeräte-Steuerung.

### Verfügbare Sprachen

- [English (en)](README_en.md)
- [German (deutsch) (de)](README_de.md)
- [Dutch (nederlands) (nl)](README_nl.md)
- [Spanish (español) (es)](README_es.md)
- [French (français) (fr)](README_fr.md)
- [Italian (italiano) (it)](README_it.md)
- [Portuguese (português) (pt)](README_pt.md)
- [Russian (русский) (ru)](README_ru.md)
- [Simplified Chinese (中文) (cn)](README_cn.md)
- [Japanese (日本語) (ja)](README_ja.md)
- [Arabic (العربية) (ar)](README_ar.md)
- [Greek (Ελληνικά) (el)](README_el.md)
- [Hindi (हिन्दी) (hi)](README_hi.md)
- [Polish (polski) (pl)](README_pl.md)
- [Turkish (türkçe) (tr)](README_tr.md)

Wenn eine Sprache fehlt, teilen Sie uns dies bitte mit, und wir werden unser Bestes tun, um sie hinzuzufügen.

## Funktionen

- 🔌 **Multi-Geräte-Unterstützung**: Gateways, Sensoren, Schalter, Alarme und mehr
- ☁️ **Cloud-Integration**: Verbindung über Heiman-Konto mit OAuth2-Authentifizierung
- 📡 **MQTT-Echtzeit-Updates**: Sofortige Gerätestatusaktualisierungen über MQTT-Push
- 🔄 **Firmware-Management**: Firmware-Updates direkt aus Home Assistant prüfen und installieren
- 👨‍👩‍👧‍👦 **Kindgeräte-Management**: Gateway-Subgeräte über MQTT hinzufügen, entfernen und verwalten
- 🏠 **Multi-Home-Unterstützung**: Mehrere Heiman-Homes unabhängig verwalten
- 🎛️ **Umfassende Entitäten**: Sensoren, Schalter, Buttons, Auswahlen, Binärsensoren und Update-Entitäten
- ⚙️ **Web-UI-Konfiguration**: Einfache Einrichtung ohne YAML-Konfiguration

<a name="installation"></a>
## Installation


### Methode 1: HACS (Empfohlen)

#### Erste Installation
1. Öffnen Sie **HACS** → **Integrationen**
2. Klicken Sie auf **+ REPOSITORIES ERKUNDEN & HERUNTERLADEN**
3. Suchen Sie nach `Heiman Home` oder klicken Sie auf die drei Punkte (⋮) → **Benutzerdefinierte Repositories**
4. Repository hinzufügen: `https://github.com/hass-user/heiman-home` mit Kategorie `Integration`
5. Klicken Sie auf **DIESES REPOSITORY HERUNTERLADEN**

#### Komponente aktualisieren
1. Öffnen Sie **HACS** → **Integrationen**
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. Finden Sie **Heiman Home**
   ![img.png](image/img.png)
3. Klicken Sie auf ****AKTUALISIEREN** oder **Erneut herunterladen****
   ![img_1.png](image/img_1.png)
### Methode 2: Manuelle Installation über Samba/SFTP

1. Laden Sie die neueste Version von [GitHub Releases](https://github.com/hass-user/heiman-home/releases) herunter
2. Extrahieren Sie den Ordner `heiman_home`
3. Kopieren Sie den Ordner `heiman_home` in Ihr Home Assistant `custom_components` Verzeichnis
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### Methode 3: One-Key-Shell über SSH/Terminal & SSH-Add-on

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### Nach der Installation

1. Starten Sie Home Assistant neu
2. Gehen Sie zu **Einstellungen** → **Geräte & Dienste**
3. Klicken Sie auf **+ Integration hinzufügen**
4. Suchen Sie nach `Heiman Home`

<a name="configuration"></a>
## Konfiguration

### Integration über Web-UI hinzufügen

1. Öffnen Sie die Home Assistant Web-Oberfläche
2. Navigieren Sie zu **Einstellungen** → **Geräte & Dienste**
3. Klicken Sie auf **Integration hinzufügen**
4. Suchen Sie nach `Heiman Home` und wählen Sie es aus
5. Autorisieren Sie mit Ihrem Heiman-Konto (OAuth2)
6. Wählen Sie das Home aus, das Sie integrieren möchten
7. Schließen Sie die Einrichtung ab

### Authentifizierung

Die Integration verwendet OAuth2 für sichere Authentifizierung:
- Klicken Sie auf **Autorisieren**, um sich bei Ihrem Heiman-Konto anzumelden
- Gewähren Sie die erforderlichen Berechtigungen
- Wählen Sie das Home aus, das Sie integrieren möchten

### Mehrere Homes

Sie können mehrere Heiman-Homes hinzufügen:
1. Jedes Home erstellt einen separaten Konfigurationseintrag
2. Jedes Home hat eine unabhängige Geräteverwaltung
3. Konfigurieren Sie jedes Home separat in **Geräte & Dienste**

### Gerätefilterung

Sie können filtern, welche Geräte integriert werden sollen:
1. Öffnen Sie die Integrationseinstellungen
2. Navigieren Sie zu **Optionen**
3. Aktivieren/deaktivieren Sie bestimmte Geräte
4. Speichern Sie die Änderungen

<a name="supported-devices"></a>
## Unterstützte Geräte

### Gateways
-  Smart Gateway (WS3GW-R, usw.)
- 🌐 Zigbee Gateway
- 🌐 WiFi Gateway

### Sensoren
- 🌡️ Temperatur- & Feuchtigkeitssensoren
- 🚪 Tür-/Fenstersensoren
- 💧 Wasserlecksensoren
- 🔥 Rauchmelder
- 💨 Gassensoren
- 🏃 Bewegungsmelder
- 🌞 Beleuchtungsstärkesensoren

### Alarme & Sicherheit
- 🚨 Alarmsysteme
- 🔔 Alarmtonsteuerung
- 🚪 Zugangskontrolle

### Schalter & Steuerungen
- 🔌 Intelligente Steckdosen
- 💡 Lichtschalter
- 🎛️ Szenensteuerungen

### Andere Geräte
- ️ Thermostate
- 💨 Luftqualitätsmonitore
- 🔋 Batteriebetriebene Geräte

<a name="entities"></a>
## Entitätstypen

### Sensor-Entitäten
- Temperatur
- Feuchtigkeit
- Batteriestand
- Signalstärke (RSSI)
- Beleuchtungsstärke
- Gerätestatus

### Binärsensor-Entitäten
- Tür/Fenster Offen/Geschlossen
- Bewegung erkannt
- Wasserleck
- Rauch erkannt
- Manipulationsschutzstatus
- Niedrige Batteriewarnung

### Schalter-Entitäten
- Gerät Ein/Aus
- Kontrollleuchte
- Summersteuerung
- Alarm Aktivieren/Deaktivieren

### Button-Entitäten
- Gerätestatus aktualisieren
- Remote-Check
- Remote-Lokalisierung
- Remote-Stummschaltung

### Auswahl-Entitäten
- Alarmtonoptionen (Schnelles Piepen, Mittleres Piepen, Langsames Piepen)
- Temperatureinheit (°C / °F)
- Betriebsmodus
- Signalpegelanzeige

### Zahlen-Entitäten
- Temperaturobergrenze
- Temperaturuntergrenze
- Feuchtigkeits-Obergrenze
- Feuchtigkeits-Untergrenze
- Temperatur-Komfortbereich
- Feuchtigkeits-Komfortbereich

### Update-Entitäten
- Firmware-Version
- Verfügbare Updates
- Firmware-Installationsfortschritt

<a name="firmware-management"></a>
## Firmware-Management

### Nach Updates suchen
- Firmware-Updates werden automatisch während der Gerätesynchronisierung geprüft
- Update-Entitäten zeigen verfügbare Firmware-Versionen an
- Vergleichen Sie die installierte Version mit der neuesten verfügbaren Version

### Firmware-Updates installieren
1. Navigieren Sie zum Gerät in Home Assistant
2. Öffnen Sie die **Firmware**-Entität
3. Klicken Sie auf die Schaltfläche **Installieren**
4. Überwachen Sie den Update-Fortschritt in Echtzeit
5. Das Gerät wird nach Abschluss des Updates neu gestartet

### Update-Funktionen
- ✅ Automatische Versionserkennung
- ✅ Fortschrittsüberwachung (0-100%)
- ✅ Update-Statusverfolgung
- ✅ Versionsvergleich
- ✅ Batch-Update-Prüfung

<a name="mqtt-integration"></a>
## MQTT-Integration

### Echtzeit-Updates
Die Integration verwendet MQTT für sofortige Gerätestatusaktualisierungen:
- Keine Polling-Verzögerung
- Sofortige Statusänderungen
- Geringere API-Nutzung
- Bessere Leistung

### MQTT-Konfiguration
- Wird während der Einrichtung automatisch konfiguriert
- Verwendet Heiman MQTT-Broker
- Sichere Verbindung mit TLS/SSL
- Keine manuelle Konfiguration erforderlich

### Unterstützte MQTT-Funktionen
- Geräteproperty-Updates
- Online/Offline-Status
- Alarmereignisse
- Sensorwerte
- Kindgeräte-Management (Registrierung, Deregistrierung, Erkennung)

<a name="child-device-management"></a>
## Kindgeräte-Management

Die Integration bietet umfassendes Kindgeräte-Management durch die `heiman-connect` Bibliothek.
Alle Geräteverwaltungslogik ist im SDK implementiert, und die Home Assistant-Integration bietet eine einfache API für den Zugriff auf diese Funktionen.

### Verwendung des Kindgeräte-Managers

```python
from heimanconnect import ChildDeviceManager

# Kindgeräte-Manager vom API-Client abrufen
device_manager = await api_client.async_get_child_device_manager(
   user_id="ihre_benutzer_id",
   devices=geräte_dict,
   user_display_name="Ihr Name"
)

# Kindgerät hinzufügen (empfohlene Methode)
result = await device_manager.add_and_sync_device(
   gateway_product_id="1733421468953686016",
   gateway_device_id="1760910156165971969",
   child_device_id="1768080341172985856",
   child_product_id="1734821218500292608",
   child_device_name="Türsensor"
)

# Kindgerät entfernen (empfohlene Methode)
result = await device_manager.remove_and_sync_device(
   gateway_product_id="1733421468953686016",
   gateway_device_id="1760910156165971969",
   child_device_id="1768080341172985856",
   product_id="1734821218500292608",
   device_name="01000053"
)
```

### Verfügbare Methoden

Für detaillierte Dokumentation aller verfügbaren Methoden und ihrer Parameter siehe die [heiman-connect Bibliotheksdokumentation](https://pypi.org/project/heiman-connect/).

<a name="advanced-configuration"></a>
## Erweiterte Konfiguration

### Logger-Konfiguration

Debug-Logging für Fehlerbehebung aktivieren:

```yaml
# configuration.yaml
logger:
   default: warning
   logs:
      custom_components.heiman_home: debug
      heimanconnect: debug
```

### Entitäten anpassen

```yaml
# configuration.yaml
homeassistant:
   customize: !include customize.yaml

# customize.yaml
sensor.heiman_temperature:
   friendly_name: "Wohnzimmer Temperatur"
   device_class: temperature
   unit_of_measurement: "°C"

binary_sensor.heiman_door:
   friendly_name: "Eingangstür"
   device_class: door
```

### Attribute ausschließen

```yaml
# configuration.yaml
heiman_home:
   exclude_attributes:
      - raw_data
      - firmware_info
      - configuration
```

<a name="services"></a>
## Dienste

### `heiman_home.refresh_device`

Manuell den Status eines Geräts aktualisieren.

```yaml
service: heiman_home.refresh_device
data:
   device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

Alle Geräte in der Integration aktualisieren.

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## Fehlerbehebung

### Entitätsstatus-Attribute abrufen

1. Öffnen Sie **Entwicklertools** → **Zustände**
2. Suchen Sie nach Ihrer Entität (z.B. `sensor.heiman_temperature`)
3. Zeigen Sie alle Attribute und den aktuellen Zustand an

### Debug-Logs abrufen

1. Debug-Logging aktivieren (siehe [Logger-Konfiguration](#advanced-configuration))
2. Öffnen Sie **Einstellungen** → **System** → **Protokolle**
3. Suchen Sie nach `heiman_home` oder `heimanconnect`

### Häufige Probleme

#### Gerät wird nicht angezeigt
- Überprüfen Sie die Gerätefiltereinstellungen
- Stellen Sie sicher, dass das Gerät in der Heiman-App online ist
- Starten Sie die Integration neu

#### Firmware-Update funktioniert nicht
- Stellen Sie sicher, dass das Gerät online ist
- Überprüfen Sie die Gerätekompatibilität
- Stellen Sie sicher, dass ein Firmware-Update in der Heiman-App verfügbar ist

#### Verbindungsprobleme
- Überprüfen Sie die Internetverbindung
- Überprüfen Sie die Heiman-Konto-Anmeldeinformationen
- Überprüfen Sie die Home Assistant-Protokolle auf Fehler

#### MQTT verbindet sich nicht
- Stellen Sie sicher, dass das Netzwerk ausgehende Verbindungen zu `spmqtt.heiman.cn:1884` erlaubt
- Überprüfen Sie die Firewall-Einstellungen
- Starten Sie Home Assistant neu

<a name="troubleshooting"></a>
## Problemlösung

### Authentifizierung fehlgeschlagen
1. Autorisieren Sie die Integration erneut
2. Überprüfen Sie die Heiman-Konto-Anmeldeinformationen
3. Stellen Sie sicher, dass das Konto Zugriff auf das ausgewählte Home hat

### Geräte werden nicht aktualisiert
1. Überprüfen Sie den MQTT-Verbindungsstatus in den Protokollen
2. Stellen Sie sicher, dass das Gerät online ist
3. Versuchen Sie eine manuelle Aktualisierung über den Dienst

### Hohe Datenbanknutzung
- Schließen Sie unnötige Attribute aus (siehe [Attribute ausschließen](#advanced-configuration))
- Deaktivieren Sie nicht verwendete Entitäten
- Überprüfen Sie Entitäten mit zu vielen Zustandsänderungen

### Leistungsprobleme
- Reduzieren Sie das Update-Intervall, wenn möglich
- Filtern Sie nicht verwendete Geräte heraus
- Deaktivieren Sie MQTT, wenn nicht benötigt (nicht empfohlen)

<a name="development"></a>
## Entwicklung

### Projektstruktur
```
heiman_home/
├── __init__.py          # Integrationsinitialisierung
├── api.py               # API-Client-Wrapper
├── config_flow.py       # Konfigurationsfluss
├── const.py             # Konstanten und Konfiguration
├── coordinator.py       # Datenupdate-Koordinator
├── sensor.py            # Sensor-Plattform
├── binary_sensor.py     # Binärsensor-Plattform
├── switch.py            # Schalter-Plattform
├── button.py            # Button-Plattform
├── select.py            # Auswahl-Plattform
├── number.py            # Zahlen-Plattform
├── update.py            # Update-Plattform (Firmware)
├── manifest.json        # Integrationsmetadaten
└── strings.json         # Übersetzungen
```

**Hinweis**: Alle Geräteverwaltungslogik befindet sich in der `heiman-connect` Bibliothek, nicht in dieser Integration.

### Abhängigkeiten
- `heiman-connect`: Python-Bibliothek für Heiman API
- `packaging`: Versionsvergleich für Firmware-Updates

<a name="contributing"></a>
## Mitwirken

Beiträge sind willkommen! Bitte reichen Sie gerne ein:
- Fehlerberichte
- Funktionsanfragen
- Geräteunterstützung
- Übersetzungen
- Dokumentationsverbesserungen

<a name="license"></a>
## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

<a name="acknowledgments"></a>
## Danksagungen

- [Heiman](www.heimantech.com) für die Bereitstellung der IoT-Plattform
- [Home Assistant](https://www.home-assistant.io) Community
- [HACS](https://hacs.xyz) für das Integrationsframework
- Alle Mitwirkenden und Tester

<a name="support"></a>
## Support

- **GitHub Issues**: [Fehler melden oder Funktionen anfordern](https://github.com/hass-user/heiman-home/issues)
- **Home Assistant Community Forum**: [Diskutieren und Hilfe erhalten](https://community.home-assistant.io/)
- **Dokumentation**: [Vollständige Dokumentation](https://github.com/hass-user/heiman-home/wiki)

---

**Genießen Sie Ihr Smart Home mit Heiman und Home Assistant! 🏠✨**
