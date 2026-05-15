# Heiman Home voor HomeAssistant

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## Overzicht

Deze Home Assistant-integratie maakt het gebruik van Heiman slimme huisapparaten in een smart home-systeem mogelijk. Het verbindt met de Heiman cloud API en gebruikt het MQTT-protocol voor realtime apparaatstatusupdates.

Met deze integratie kunnen gebruikers Heiman-apparaten eenvoudig integreren in Home Assistant en ze gebruiken voor verschillende automatiseringen en monitoring, inclusief firmwarebeheer en kindapparaatbesturing.

### Beschikbare talen

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

Als er een taal ontbreekt, laat het ons weten. We doen ons best om deze toe te voegen.

## Functies

- 🔌 **Multi-apparaatondersteuning**: Gateways, sensoren, schakelaars, alarmen en meer
- ☁️ **Cloud-integratie**: Verbind via Heiman-account met OAuth2-authenticatie
- 📡 **MQTT realtime-updates**: Onmiddellijke apparaatstatusupdates via MQTT-push
- 🔄 **Firmwarebeheer**: Controleer en installeer firmware-updates rechtstreeks vanuit Home Assistant
- 👨‍👩‍👧‍👦 **Kindapparaatbeheer**: Voeg gateway-subapparaten toe, verwijder en beheer ze via MQTT
- 🏠 **Multi-home ondersteuning**: Beheer meerdere Heiman-huizen onafhankelijk
- 🎛️ **Uitgebreide entiteiten**: Sensoren, schakelaars, knoppen, selectors, binaire sensoren en update-entiteiten
- ⚙️ **Web UI-configuratie**: Eenvoudige installatie zonder YAML-configuratie

<a name="installation"></a>
## Installatie


### Methode 1: HACS (Aanbevolen)

#### Eerste installatie
1. Open **HACS** → **Integraties**
2. Klik op **+ ONTDEK & DOWNLOAD REPOSITORIES**
3. Zoek naar `Heiman Home` of klik op de drie puntjes (⋮) → **Aangepaste repositories**
4. Repository toevoegen: `https://github.com/hass-user/heiman-home` met categorie `Integration`
5. Klik op **DOWNLOAD DEZE REPOSITORY**

#### Component bijwerken
1. Open **HACS** → **Integraties**
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. Zoek **Heiman Home**
   ![img.png](image/img.png)
3. **Klik op **BIJWERKEN** of **Opnieuw downloaden****
   ![img_1.png](image/img_1.png)
### Methode 2: Handmatige installatie via Samba/SFTP

1. Download de nieuwste versie van [GitHub Releases](https://github.com/hass-user/heiman-home/releases)
2. Pak de map `heiman_home` uit
3. Kopieer de map `heiman_home` naar je Home Assistant `custom_components` directory
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### Methode 3: One-Key-Shell via SSH/Terminal & SSH Add-on

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### Na de installatie

1. Start Home Assistant opnieuw op
2. Ga naar **Instellingen** → **Apparaten & services**
3. Klik op **+ Integratie toevoegen**
4. Zoek naar `Heiman Home`

<a name="configuration"></a>
## Configuratie

### Integratie toevoegen via Web UI

1. Open de Home Assistant webinterface
2. Navigeer naar **Instellingen** → **Apparaten & services**
3. Klik op **Integratie toevoegen**
4. Zoek naar `Heiman Home` en selecteer het
5. Autoriseer met je Heiman-account (OAuth2)
6. Selecteer het huis dat je wilt integreren
7. Voltooi de installatie

### Authenticatie

De integratie gebruikt OAuth2 voor veilige authenticatie:
- Klik op **Autoriseren** om in te loggen op je Heiman-account
- Verleen de vereiste machtigingen
- Selecteer het huis dat je wilt integreren

### Meerdere huizen

Je kunt meerdere Heiman-huizen toevoegen:
1. Elk huis maakt een aparte configuratie-entry
2. Elk huis heeft onafhankelijk apparaatbeheer
3. Configureer elk huis afzonderlijk in **Apparaten & services**

### Apparaatfiltering

Je kunt filteren welke apparaten geïntegreerd moeten worden:
1. Open de integratie-instellingen
2. Navigeer naar **Opties**
3. Schakel specifieke apparaten in/uit
4. Sla de wijzigingen op

<a name="supported-devices"></a>
## Ondersteunde apparaten

### Gateways
-  Slimme gateway (WS3GW-R, enz.)
- 🌐 Zigbee gateway
- 🌐 WiFi gateway

### Sensoren
- 🌡️ Temperatuur- & vochtigheidssensoren
- 🚪 Deur-/raamsensoren
- 💧 Waterleksensoren
- 🔥 Rookmelders
- 💨 Gassensoren
- 🏃 Bewegingsmelders
- 🌞 Lichtsterktesensoren

### Alarmen & beveiliging
- 🚨 Alarmsystemen
- 🔔 Alarmgeluidsbediening
- 🚪 Toegangscontrole

### Schakelaars & bedieningen
- 🔌 Slimme stekkers
- 💡 Lichtschakelaars
- 🎛️ Scènecontrollers

### Andere apparaten
- ️ Thermostaten
- 💨 Luchtkwaliteitsmonitors
- 🔋 Batterij-aangedreven apparaten

<a name="entities"></a>
## Entiteitstypen

### Sensor-entiteiten
- Temperatuur
- Vochtigheid
- Batterijniveau
- Signaalsterkte (RSSI)
- Lichtsterkte
- Apparaatstatus

### Binaire sensor-entiteiten
- Deur/raam open/gesloten
- Beweging gedetecteerd
- Waterlek
- Rook gedetecteerd
- Tamper-status
- Lage batterijwaarschuwing

### Schakelaar-entiteiten
- Apparaat aan/uit
- Indicatorlampje
- Zoemerbediening
- Alarm in-/uitschakelen

### Knop-entiteiten
- Apparaatstatus bijwerken
- Externe controle
- Externe lokalisatie
- Extern dempen

### Selector-entiteiten
- Alarmgeluidsopties (Snelle piep, Middelmatige piep, Langzame piep)
- Temperatuureenheid (°C / °F)
- Bedieningsmodus
- Signaalniveau-indicator

### Numerieke entiteiten
- Hoge temperatuurdrempel
- Lage temperatuurdrempel
- Hoge vochtigheidsdrempel
- Lage vochtigheidsdrempel
- Temperatuurcomfortbereik
- Vochtigheidscomfortbereik

### Update-entiteiten
- Firmware-versie
- Beschikbare updates
- Firmware-installatievoortgang

<a name="firmware-management"></a>
## Firmwarebeheer

### Controleren op updates
- Firmware-updates worden automatisch gecontroleerd tijdens apparaatsynchronisatie
- Update-entiteiten tonen beschikbare firmware-versies
- Vergelijk de geïnstalleerde versie met de nieuwste beschikbare versie

### Firmware-updates installeren
1. Navigeer naar het apparaat in Home Assistant
2. Open de **Firmware**-entiteit
3. Klik op de knop **Installeren**
4. Monitor de updatevoortgang in realtime
5. Het apparaat wordt opnieuw gestart nadat de update is voltooid

### Updatefuncties
- ✅ Automatische versiedetectie
- ✅ Voortgangsmonitoring (0-100%)
- ✅ Updatestatustracking
- ✅ Versievergelijking
- ✅ Batch-updatecontrole

<a name="mqtt-integration"></a>
## MQTT-integratie

### Realtime-updates
De integratie gebruikt MQTT voor onmiddellijke apparaatstatusupdates:
- Geen polling-vertraging
- Onmiddellijke statuswijzigingen
- Minder API-gebruik
- Betere prestaties

### MQTT-configuratie
- Wordt automatisch geconfigureerd tijdens installatie
- Gebruikt Heiman MQTT-broker
- Beveiligde verbinding met TLS/SSL
- Geen handmatige configuratie vereist

### Ondersteunde MQTT-functies
- Apparaateigenschap-updates
- Online/offline-status
- Alarmgebeurtenissen
- Sensorwaarden
- Kindapparaatbeheer (registratie, deregistratie, detectie)

<a name="child-device-management"></a>
## Kindapparaatbeheer

De integratie biedt uitgebreid kindapparaatbeheer via de `heiman-connect` bibliotheek.
Alle apparaatbeheerlogica is geïmplementeerd in de SDK, en de Home Assistant-integratie biedt een eenvoudige API om toegang te krijgen tot deze functies.

### De kindapparaatmanager gebruiken

```python
from heimanconnect import ChildDeviceManager

# Haal de kindapparaatmanager op van de API-client
device_manager = await api_client.async_get_child_device_manager(
    user_id="your_user_id",
    devices=devices_dict,
    user_display_name="Your Name"
)

# Kindapparaat toevoegen (aanbevolen methode)
result = await device_manager.add_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    child_product_id="1734821218500292608",
    child_device_name="Door Sensor"
)

# Kindapparaat verwijderen (aanbevolen methode)
result = await device_manager.remove_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    product_id="1734821218500292608",
    device_name="01000053"
)
```

### Beschikbare methoden

Voor gedetailleerde documentatie van alle beschikbare methoden en hun parameters, zie de [heiman-connect bibliotheekdocumentatie](https://pypi.org/project/heiman-connect/).

<a name="advanced-configuration"></a>
## Geavanceerde configuratie

### Logger-configuratie

Schakel debug-logboekregistratie in voor probleemoplossing:

```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.heiman_home: debug
    heimanconnect: debug
```

### Entiteiten aanpassen

```yaml
# configuration.yaml
homeassistant:
  customize: !include customize.yaml

# customize.yaml
sensor.heiman_temperature:
  friendly_name: "Living Room Temperature"
  device_class: temperature
  unit_of_measurement: "°C"

binary_sensor.heiman_door:
  friendly_name: "Front Door"
  device_class: door
```

### Attributen uitsluiten

```yaml
# configuration.yaml
heiman_home:
  exclude_attributes:
    - raw_data
    - firmware_info
    - configuration
```

<a name="services"></a>
## Services

### `heiman_home.refresh_device`

Handmatig de status van een apparaat bijwerken.

```yaml
service: heiman_home.refresh_device
data:
  device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

Alle apparaten in de integratie bijwerken.

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## Debuggen

### Entiteitstatusattributen ophalen

1. Open **Ontwikkelaarstools** → **Statussen**
2. Zoek naar je entiteit (bijv. `sensor.heiman_temperature`)
3. Bekijk alle attributen en de huidige status

### Debug-logs ophalen

1. Schakel debug-logboekregistratie in (zie [Logger-configuratie](#advanced-configuration))
2. Open **Instellingen** → **Systeem** → **Logboeken**
3. Zoek naar `heiman_home` of `heimanconnect`

### Veelvoorkomende problemen

#### Apparaat wordt niet weergegeven
- Controleer de apparaatfilterinstellingen
- Zorg ervoor dat het apparaat online is in de Heiman-app
- Start de integratie opnieuw op

#### Firmware-update werkt niet
- Zorg ervoor dat het apparaat online is
- Controleer de apparaatcompatibiliteit
- Zorg ervoor dat er een firmware-update beschikbaar is in de Heiman-app

#### Verbindingsproblemen
- Controleer de internetverbinding
- Controleer de Heiman-accountinloggegevens
- Controleer de Home Assistant-logboeken op fouten

#### MQTT maakt geen verbinding
- Zorg ervoor dat het netwerk uitgaande verbindingen naar `spmqtt.heiman.cn:1884` toestaat
- Controleer de firewall-instellingen
- Start Home Assistant opnieuw op

<a name="troubleshooting"></a>
## Probleemoplossing

### Authenticatie mislukt
1. Autoriseer de integratie opnieuw
2. Controleer de Heiman-accountinloggegevens
3. Zorg ervoor dat het account toegang heeft tot het geselecteerde huis

### Apparaten worden niet bijgewerkt
1. Controleer de MQTT-verbindingsstatus in de logboeken
2. Zorg ervoor dat het apparaat online is
3. Probeer handmatig bijwerken via de service

### Hoog databasegebruik
- Sluit onnodige attributen uit (zie [Attributen uitsluiten](#advanced-configuration))
- Schakel ongebruikte entiteiten uit
- Controleer entiteiten met te veel statuswijzigingen

### Prestatieproblemen
- Verminder het update-interval indien mogelijk
- Filter ongebruikte apparaten eruit
- Schakel MQTT uit als het niet nodig is (niet aanbevolen)

<a name="development"></a>
## Ontwikkeling

### Projectstructuur
```
heiman_home/
├── __init__.py          # Integratie-initialisatie
├── api.py               # API-client wrapper
├── config_flow.py       # Configuratiestroom
├── const.py             # Constanten en configuratie
├── coordinator.py       # Data-update coördinator
├── sensor.py            # Sensor-platform
├── binary_sensor.py     # Binaire sensor-platform
├── switch.py            # Schakelaar-platform
├── button.py            # Knop-platform
├── select.py            # Selector-platform
├── number.py            # Numeriek platform
├── update.py            # Update-platform (firmware)
├── manifest.json        # Integratiemetadata
└── strings.json         # Vertalingen
```

**Opmerking**: Alle apparaatbeheerlogica bevindt zich in de `heiman-connect` bibliotheek, niet in deze integratie.

### Afhankelijkheden
- `heiman-connect`: Python-bibliotheek voor Heiman API
- `packaging`: Versievergelijking voor firmware-updates

<a name="contributing"></a>
## Bijdragen

Bijdragen zijn welkom! Dien gerust in:
- Bugrapporten
- Functieverzoeken
- Apparaatondersteuning
- Vertalingen
- Documentatieverbeteringen

<a name="license"></a>
## Licentie

Dit project is gelicentieerd onder de MIT-licentie - zie het [LICENSE](LICENSE) bestand voor details.

<a name="acknowledgments"></a>
## Erkenningen

- [Heiman](www.heimantech.com) voor het bieden van het IoT-platform
- [Home Assistant](https://www.home-assistant.io) community
- [HACS](https://hacs.xyz) voor het integratieframework
- Alle bijdragers en testers

<a name="support"></a>
## Ondersteuning

- **GitHub Issues**: [Bugs melden of functies aanvragen](https://github.com/hass-user/heiman-home/issues)
- **Home Assistant Community Forum**: [Discussiëren en hulp krijgen](https://community.home-assistant.io/)
- **Documentatie**: [Volledige documentatie](https://github.com/hass-user/heiman-home/wiki)

---

**Geniet van je smart home met Heiman en Home Assistant! 🏠✨**
