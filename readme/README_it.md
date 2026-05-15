# Heiman Home per HomeAssistant

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## Panoramica

Questa integrazione per Home Assistant consente l'utilizzo di dispositivi domestici intelligenti Heiman all'interno di un sistema di casa intelligente. Si connette all'API cloud Heiman e utilizza il protocollo MQTT per aggiornamenti dello stato del dispositivo in tempo reale.

Questa integrazione consente agli utenti di integrare facilmente i propri dispositivi Heiman in Home Assistant e di utilizzarli per varie automazioni e monitoraggi, inclusa la gestione del firmware e il controllo dei dispositivi figli.

### Lingue Disponibili

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

Se manca una lingua, faccelo sapere e faremo del nostro meglio per aggiungerla.

## Caratteristiche

- 🔌 **Supporto Multi-dispositivo**: Gateway, sensori, interruttori, allarmi e altro
- ☁️ **Integrazione Cloud**: Connettiti tramite account Heiman con autenticazione OAuth2
- 📡 **Aggiornamenti MQTT in Tempo Reale**: Aggiornamenti istantanei dello stato del dispositivo tramite push MQTT
- 🔄 **Gestione Firmware**: Verifica e installa aggiornamenti firmware direttamente da Home Assistant
- 👨‍👩‍👧‍👦 **Gestione Dispositivi Figli**: Aggiungi, rimuovi e gestisci sottodispositivi del gateway tramite MQTT
- 🏠 **Supporto Multi-casa**: Gestisci più case Heiman in modo indipendente
- 🎛️ **Entità Complete**: Sensori, interruttori, pulsanti, selettori, sensori binari ed entità di aggiornamento
- ⚙️ **Configurazione Web UI**: Configurazione facile senza configurazione YAML

<a name="installation"></a>
## Installazione


### Metodo 1: HACS (Consigliato)

#### Prima Installazione
1. Apri **HACS** → **Integrazioni**
2. Clicca su **+ ESPLORA E SCARICA REPOSITORY**
3. Cerca `Heiman Home` o clicca sui tre punti (⋮) → **Repository personalizzate**
4. Aggiungi repository: `https://github.com/hass-user/heiman-home` con categoria `Integration`
5. Clicca su **SCARICA QUESTA REPOSITORY**

#### Aggiorna Componente
1. Apri **HACS** → **Integrazioni**
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. Trova **Heiman Home**
   ![img.png](image/img.png)
3. Clicca su ****AGGIORNA** o **Scarica di nuovo****
   ![img_1.png](image/img_1.png)
### Metodo 2: Installazione Manuale tramite Samba/SFTP

1. Scarica l'ultima versione da [GitHub Releases](https://github.com/hass-user/heiman-home/releases)
2. Estrai la cartella `heiman_home`
3. Copia la cartella `heiman_home` nella tua directory `custom_components` di Home Assistant
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### Metodo 3: Shell One-Key tramite SSH/Terminal e SSH Add-on

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### Dopo l'Installazione

1. Riavvia Home Assistant
2. Vai a **Impostazioni** → **Dispositivi e Servizi**
3. Clicca su **+ Aggiungi Integrazione**
4. Cerca `Heiman Home`

<a name="configuration"></a>
## Configurazione

### Aggiungi Integrazione tramite Web UI

1. Apri l'interfaccia web di Home Assistant
2. Naviga su **Impostazioni** → **Dispositivi e Servizi**
3. Clicca su **Aggiungi Integrazione**
4. Cerca `Heiman Home` e selezionalo
5. Autorizza con il tuo account Heiman (OAuth2)
6. Seleziona la casa che desideri integrare
7. Completa la configurazione

### Autenticazione

L'integrazione utilizza OAuth2 per l'autenticazione sicura:
- Clicca su **Autorizza** per accedere al tuo account Heiman
- Concedi le autorizzazioni richieste
- Seleziona la casa che desideri integrare

### Più Case

Puoi aggiungere più case Heiman:
1. Ogni casa crea una voce di configurazione separata
2. Ogni casa ha una gestione dei dispositivi indipendente
3. Configura ogni casa separatamente in **Dispositivi e Servizi**

### Filtraggio Dispositivi

Puoi filtrare quali dispositivi integrare:
1. Apri le impostazioni dell'integrazione
2. Naviga su **Opzioni**
3. Abilita/disabilita dispositivi specifici
4. Salva le modifiche

<a name="supported-devices"></a>
## Dispositivi Supportati

### Gateway
-  Smart Gateway (WS3GW-R, ecc.)
- 🌐 Gateway Zigbee
- 🌐 Gateway WiFi

### Sensori
- 🌡️ Sensori di Temperatura e Umidità
- 🚪 Sensori Porta/Finestra
- 💧 Sensori Perdita Acqua
- 🔥 Rilevatori Fumo
- 💨 Sensori Gas
- 🏃 Sensori Movimento
- 🌞 Sensori Luminosità

### Allarmi e Sicurezza
- 🚨 Sistemi di Allarme
- 🔔 Controllo Suono Allarme
- 🚪 Controllo Accessi

### Interruttori e Controlli
- 🔌 Prese Intelligenti
- 💡 Interruttori Luce
- 🎛️ Controller Scena

### Altri Dispositivi
- ️ Termostati
- 💨 Monitor Qualità Aria
- 🔋 Dispositivi a Batteria

<a name="entities"></a>
## Tipi di Entità

### Entità Sensore
- Temperatura
- Umidità
- Livello Batteria
- Forza Segnale (RSSI)
- Luminosità
- Stato Dispositivo

### Entità Sensore Binario
- Porta/Finestra Aperta/Chiusa
- Movimento Rilevato
- Perdita Acqua
- Fumo Rilevato
- Stato Manomissione
- Avviso Batteria Scarica

### Entità Interruttore
- Dispositivo Acceso/Spento
- Luce Indicatore
- Controllo Buzzer
- Allarme Abilitato/Disabilitato

### Entità Pulsante
- Aggiorna Stato Dispositivo
- Controllo Remoto
- Localizzazione Remota
- Muto Remoto

### Entità Selettore
- Opzioni Suono Allarme (Beep Veloce, Beep Medio, Beep Lento)
- Unità Temperatura (°C / °F)
- Modalità Operativa
- Visualizzazione Livello Segnale

### Entità Numero
- Soglia Alta Temperatura
- Soglia Bassa Temperatura
- Soglia Alta Umidità
- Soglia Bassa Umidità
- Intervallo Comfort Temperatura
- Intervallo Comfort Umidità

### Entità Aggiornamento
- Versione Firmware
- Aggiornamenti Disponibili
- Progresso Installazione Firmware

<a name="firmware-management"></a>
## Gestione Firmware

### Cerca Aggiornamenti
- Gli aggiornamenti firmware vengono verificati automaticamente durante la sincronizzazione del dispositivo
- Le entità di aggiornamento mostrano le versioni firmware disponibili
- Confronta la versione installata con l'ultima versione disponibile

### Installa Aggiornamenti Firmware
1. Naviga al dispositivo in Home Assistant
2. Apri l'entità **Firmware**
3. Clicca sul pulsante **Installa**
4. Monitora il progresso dell'aggiornamento in tempo reale
5. Il dispositivo si riavvierà dopo il completamento dell'aggiornamento

### Funzioni di Aggiornamento
- ✅ Rilevamento automatico della versione
- ✅ Monitoraggio progresso (0-100%)
- ✅ Tracciamento stato aggiornamento
- ✅ Confronto versioni
- ✅ Verifica aggiornamenti batch

<a name="mqtt-integration"></a>
## Integrazione MQTT

### Aggiornamenti in Tempo Reale
L'integrazione utilizza MQTT per aggiornamenti istantanei dello stato del dispositivo:
- Nessun ritardo di polling
- Cambiamenti di stato immediati
- Minore utilizzo API
- Migliori prestazioni

### Configurazione MQTT
- Configurato automaticamente durante l'installazione
- Utilizza il broker MQTT Heiman
- Connessione sicura con TLS/SSL
- Nessuna configurazione manuale richiesta

### Funzioni MQTT Supportate
- Aggiornamenti proprietà dispositivo
- Stato online/offline
- Eventi allarme
- Letture sensore
- Gestione dispositivi figli (registrazione, deregistrazione, rilevamento)

<a name="child-device-management"></a>
## Gestione Dispositivi Figli

L'integrazione fornisce una gestione completa dei dispositivi figli tramite la libreria `heiman-connect`.
Tutta la logica di gestione dei dispositivi è implementata nell'SDK e l'integrazione Home Assistant fornisce un'API semplice per accedere a queste funzionalità.

### Utilizzo del Gestore Dispositivi Figli

```python
from heimanconnect import ChildDeviceManager

# Ottieni il gestore dispositivi figli dal client API
device_manager = await api_client.async_get_child_device_manager(
    user_id="your_user_id",
    devices=devices_dict,
    user_display_name="Your Name"
)

# Aggiungi un dispositivo figlio (metodo consigliato)
result = await device_manager.add_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    child_product_id="1734821218500292608",
    child_device_name="Door Sensor"
)

# Rimuovi un dispositivo figlio (metodo consigliato)
result = await device_manager.remove_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    product_id="1734821218500292608",
    device_name="01000053"
)
```

### Metodi Disponibili

Per documentazione dettagliata di tutti i metodi disponibili e i loro parametri, consulta la [documentazione della libreria heiman-connect](https://pypi.org/project/heiman-connect/).

<a name="advanced-configuration"></a>
## Configurazione Avanzata

### Configurazione Logger

Abilita il logging di debug per la risoluzione dei problemi:

```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.heiman_home: debug
    heimanconnect: debug
```

### Personalizza Entità

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

### Escludi Attributi

```yaml
# configuration.yaml
heiman_home:
  exclude_attributes:
    - raw_data
    - firmware_info
    - configuration
```

<a name="services"></a>
## Servizi

### `heiman_home.refresh_device`

Aggiorna manualmente lo stato di un dispositivo.

```yaml
service: heiman_home.refresh_device
data:
  device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

Aggiorna tutti i dispositivi nell'integrazione.

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## Debug

### Ottieni Attributi Stato Entità

1. Apri **Strumenti per Sviluppatori** → **Stati**
2. Cerca la tua entità (ad esempio, `sensor.heiman_temperature`)
3. Visualizza tutti gli attributi e lo stato corrente

### Ottieni Log di Debug

1. Abilita il logging di debug (vedi [Configurazione Logger](#advanced-configuration))
2. Apri **Impostazioni** → **Sistema** → **Log**
3. Cerca `heiman_home` o `heimanconnect`

### Problemi Comuni

#### Il Dispositivo Non Appare
- Controlla le impostazioni di filtraggio dei dispositivi
- Assicurati che il dispositivo sia online nell'app Heiman
- Riavvia l'integrazione

#### L'Aggiornamento Firmware Non Funziona
- Assicurati che il dispositivo sia online
- Verifica la compatibilità del dispositivo
- Assicurati che sia disponibile un aggiornamento firmware nell'app Heiman

#### Problemi di Connessione
- Verifica la connessione Internet
- Controlla le credenziali dell'account Heiman
- Controlla i log di Home Assistant per errori

#### MQTT Non Si Connette
- Assicurati che la rete consenta connessioni in uscita a `spmqtt.heiman.cn:1884`
- Controlla le impostazioni del firewall
- Riavvia Home Assistant

<a name="troubleshooting"></a>
## Risoluzione dei Problemi

### Autenticazione Fallita
1. Riautorizza l'integrazione
2. Controlla le credenziali dell'account Heiman
3. Assicurati che l'account abbia accesso alla casa selezionata

#### I Dispositivi Non Si Aggiornano
1. Controlla lo stato della connessione MQTT nei log
2. Assicurati che il dispositivo sia online
3. Prova un aggiornamento manuale tramite il servizio

#### Elevato Utilizzo del Database
- Escludi attributi non necessari (vedi [Escludi Attributi](#advanced-configuration))
- Disabilita entità non utilizzate
- Controlla entità con troppi cambiamenti di stato

#### Problemi di Prestazioni
- Riduci l'intervallo di aggiornamento se possibile
- Filtra i dispositivi non utilizzati
- Disabilita MQTT se non necessario (non consigliato)

<a name="development"></a>
## Sviluppo

### Struttura del Progetto
```
heiman_home/
├── __init__.py          # Inizializzazione integrazione
├── api.py               # Wrapper client API
├── config_flow.py       # Flusso di configurazione
├── const.py             # Costanti e configurazione
├── coordinator.py       # Coordinatore aggiornamento dati
├── sensor.py            # Piattaforma sensore
├── binary_sensor.py     # Piattaforma sensore binario
├── switch.py            # Piattaforma interruttore
├── button.py            # Piattaforma pulsante
├── select.py            # Piattaforma selettore
├── number.py            # Piattaforma numero
├── update.py            # Piattaforma aggiornamento (firmware)
├── manifest.json        # Metadati integrazione
└── strings.json         # Traduzioni
```

**Nota**: Tutta la logica di gestione dei dispositivi si trova nella libreria `heiman-connect`, non in questa integrazione.

### Dipendenze
- `heiman-connect`: Libreria Python per l'API Heiman
- `packaging`: Confronto versioni per aggiornamenti firmware

<a name="contributing"></a>
## Contribuire

I contributi sono benvenuti! Non esitare a inviare:
- Segnalazioni di bug
- Richieste di funzionalità
- Supporto dispositivi
- Traduzioni
- Miglioramenti della documentazione

<a name="license"></a>
## Licenza

Questo progetto è concesso in licenza sotto la Licenza MIT - vedi il file [LICENSE](LICENSE) per i dettagli.

<a name="acknowledgments"></a>
## Ringraziamenti

- [Heiman](www.heimantech.com) per aver fornito la piattaforma IoT
- Comunità [Home Assistant](https://www.home-assistant.io)
- [HACS](https://hacs.xyz) per il framework di integrazione
- Tutti i contributori e tester

<a name="support"></a>
## Supporto

- **GitHub Issues**: [Segnala bug o richiedi funzionalità](https://github.com/hass-user/heiman-home/issues)
- **Forum della Comunità Home Assistant**: [Discuti e ottieni aiuto](https://community.home-assistant.io/)
- **Documentazione**: [Documentazione completa](https://github.com/hass-user/heiman-home/wiki)

---

**Goditi la tua casa intelligente con Heiman e Home Assistant! 🏠✨**
