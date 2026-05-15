# Heiman Home dla HomeAssistant

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## Przegląd

Ta integracja Home Assistant umożliwia korzystanie z urządzeń inteligentnego domu Heiman w systemie smart home. Łączy się z API chmury Heiman i wykorzystuje protokół MQTT do aktualizacji statusu urządzeń w czasie rzeczywistym.

Dzięki tej integracji użytkownicy mogą łatwo integrować urządzenia Heiman z Home Assistant i używać ich do różnych automatyzacji i monitorowania, w tym zarządzania firmware'm i kontrolowania urządzeń podrzędnych.

### Dostępne języki

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

Jeśli brakuje jakiegoś języka, daj nam znać. Dołożymy wszelkich starań, aby go dodać.

## Funkcje

- 🔌 **Obsługa wielu urządzeń**: Bramy, czujniki, przełączniki, alarmy i więcej
- ☁️ **Integracja z chmurą**: Połączenie przez konto Heiman z uwierzytelnianiem OAuth2
- 📡 **Aktualizacje MQTT w czasie rzeczywistym**: Natychmiastowe aktualizacje statusu urządzeń przez push MQTT
- 🔄 **Zarządzanie firmware'm**: Sprawdzaj i instaluj aktualizacje firmware'u bezpośrednio z Home Assistant
- 👨‍👩‍👧‍👦 **Zarządzanie urządzeniami podrzędnymi**: Dodawaj, usuwaj i zarządzaj urządzeniami podrzędnymi bramki przez MQTT
- 🏠 **Obsługa wielu domów**: Niezależne zarządzanie wieloma domami Heiman
- 🎛️ **Kompleksowe encje**: Czujniki, przełączniki, przyciski, selektory, czujniki binarne i encje aktualizacji
- ⚙️ **Konfiguracja przez interfejs webowy**: Prosta konfiguracja bez YAML

<a name="installation"></a>
## Instalacja


### Metoda 1: HACS (Zalecane)

#### Pierwsza instalacja
1. Otwórz **HACS** → **Integracje**
2. Kliknij **+ ODKRYWAJ I POBIERAJ REPOZYTORIA**
3. Wyszukaj `Heiman Home` lub kliknij trzy kropki (⋮) → **Niestandardowe repozytoria**
4. Dodaj repozytorium: `https://github.com/hass-user/heiman-home` z kategorią `Integration`
5. Kliknij **POBIERZ TO REPOZYTORIUM**

#### Aktualizacja komponentu
1. Otwórz **HACS** → **Integracje**
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. Znajdź **Heiman Home**
   ![img.png](image/img.png)
3. **Kliknij **AKTUALIZUJ** lub **Pobierz ponownie****
   ![img_1.png](image/img_1.png)
### Metoda 2: Ręczna instalacja przez Samba/SFTP

1. Pobierz najnowszą wersję z [GitHub Releases](https://github.com/hass-user/heiman-home/releases)
2. Rozpakuj folder `heiman_home`
3. Skopiuj folder `heiman_home` do katalogu `custom_components` Home Assistant
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### Metoda 3: One-Key-Shell przez SSH/Terminal i SSH Add-on

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### Po instalacji

1. Uruchom ponownie Home Assistant
2. Przejdź do **Ustawienia** → **Urządzenia i usługi**
3. Kliknij **+ Dodaj integrację**
4. Wyszukaj `Heiman Home`

<a name="configuration"></a>
## Konfiguracja

### Dodawanie integracji przez interfejs webowy

1. Otwórz interfejs webowy Home Assistant
2. Przejdź do **Ustawienia** → **Urządzenia i usługi**
3. Kliknij **Dodaj integrację**
4. Wyszukaj `Heiman Home` i wybierz je
5. Autoryzuj za pomocą konta Heiman (OAuth2)
6. Wybierz dom, który chcesz zintegrować
7. Zakończ konfigurację

### Uwierzytelnianie

Integracja używa OAuth2 do bezpiecznego uwierzytelniania:
- Kliknij **Autoryzuj**, aby zalogować się na konto Heiman
- Udziel wymaganych uprawnień
- Wybierz dom, który chcesz zintegrować

### Wiele domów

Możesz dodać wiele domów Heiman:
1. Każdy dom tworzy osobny wpis konfiguracyjny
2. Każdy dom ma niezależne zarządzanie urządzeniami
3. Skonfiguruj każdy dom osobno w **Urządzenia i usługi**

### Filtrowanie urządzeń

Możesz filtrować, które urządzenia mają być zintegrowane:
1. Otwórz ustawienia integracji
2. Przejdź do **Opcje**
3. Włącz/wyłącz określone urządzenia
4. Zapisz zmiany

<a name="supported-devices"></a>
## Obsługiwane urządzenia

### Bramy
-  Inteligentna brama (WS3GW-R, itp.)
- 🌐 Brama Zigbee
- 🌐 Brama WiFi

### Czujniki
- 🌡️ Czujniki temperatury i wilgotności
- 🚪 Czujniki drzwi/okien
- 💧 Czujniki wycieku wody
- 🔥 Detektory dymu
- 💨 Czujniki gazu
- 🏃 Czujniki ruchu
- 🌞 Czujniki natężenia światła

### Alarmy i bezpieczeństwo
- 🚨 Systemy alarmowe
- 🔔 Sterowanie dźwiękiem alarmu
- 🚪 Kontrola dostępu

### Przełączniki i sterowania
- 🔌 Inteligentne gniazdka
- 💡 Przełączniki światła
- 🎛️ Kontrolery scen

### Inne urządzenia
- ️ Termostaty
- 💨 Monitory jakości powietrza
- 🔋 Urządzenia zasilane bateryjnie

<a name="entities"></a>
## Typy encji

### Encje czujników
- Temperatura
- Wilgotność
- Poziom baterii
- Siła sygnału (RSSI)
- Natężenie światła
- Status urządzenia

### Encje czujników binarnych
- Drzwi/okno otwarte/zamknięte
- Wykryto ruch
- Wyciek wody
- Wykryto dym
- Status sabotażu
- Ostrzeżenie o niskim poziomie baterii

### Encje przełączników
- Urządzenie włącz/wyłącz
- Lampka kontrolna
- Sterowanie brzęczykiem
- Alarm włącz/wyłącz

### Encje przycisków
- Aktualizuj status urządzenia
- Zdalne sprawdzanie
- Zdalna lokalizacja
- Zdalne wyciszanie

### Encje selektorów
- Opcje dźwięku alarmu (Szybki beep, Średni beep, Wolny beep)
- Jednostka temperatury (°C / °F)
- Tryb pracy
- Wskaźnik poziomu sygnału

### Encje numeryczne
- Górny próg temperatury
- Dolny próg temperatury
- Górny próg wilgotności
- Dolny próg wilgotności
- Zakres komfortu temperaturowego
- Zakres komfortu wilgotności

### Encje aktualizacji
- Wersja firmware'u
- Dostępne aktualizacje
- Postęp instalacji firmware'u

<a name="firmware-management"></a>
## Zarządzanie firmware'm

### Sprawdzanie aktualizacji
- Aktualizacje firmware'u są automatycznie sprawdzane podczas synchronizacji urządzeń
- Encje aktualizacji pokazują dostępne wersje firmware'u
- Porównaj zainstalowaną wersję z najnowszą dostępną wersją

### Instalowanie aktualizacji firmware'u
1. Przejdź do urządzenia w Home Assistant
2. Otwórz encję **Firmware**
3. Kliknij przycisk **Zainstaluj**
4. Monitoruj postęp aktualizacji w czasie rzeczywistym
5. Urządzenie zostanie ponownie uruchomione po zakończeniu aktualizacji

### Funkcje aktualizacji
- ✅ Automatyczne wykrywanie wersji
- ✅ Monitorowanie postępu (0-100%)
- ✅ Śledzenie statusu aktualizacji
- ✅ Porównywanie wersji
- ✅ Sprawdzanie aktualizacji wsadowych

<a name="mqtt-integration"></a>
## Integracja MQTT

### Aktualizacje w czasie rzeczywistym
Integracja używa MQTT do natychmiastowych aktualizacji statusu urządzeń:
- Brak opóźnień pollingowych
- Natychmiastowe zmiany statusu
- Mniejsze użycie API
- Lepsza wydajność

### Konfiguracja MQTT
- Automatycznie konfigurowana podczas instalacji
- Używa brokera MQTT Heiman
- Bezpieczne połączenie z TLS/SSL
- Nie wymaga ręcznej konfiguracji

### Obsługiwane funkcje MQTT
- Aktualizacje właściwości urządzeń
- Status online/offline
- Zdarzenia alarmowe
- Odczyty czujników
- Zarządzanie urządzeniami podrzędnymi (rejestracja, wyrejestrowanie, wykrywanie)

<a name="child-device-management"></a>
## Zarządzanie urządzeniami podrzędnymi

Integracja oferuje kompleksowe zarządzanie urządzeniami podrzędnymi poprzez bibliotekę `heiman-connect`.
Cała logika zarządzania urządzeniami jest zaimplementowana w SDK, a integracja Home Assistant zapewnia prosty API do uzyskiwania dostępu do tych funkcji.

### Korzystanie z menedżera urządzeń podrzędnych

```python
from heimanconnect import ChildDeviceManager

# Pobierz menedżer urządzeń podrzędnych z klienta API
device_manager = await api_client.async_get_child_device_manager(
    user_id="your_user_id",
    devices=devices_dict,
    user_display_name="Your Name"
)

# Dodaj urządzenie podrzędne (zalecana metoda)
result = await device_manager.add_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    child_product_id="1734821218500292608",
    child_device_name="Door Sensor"
)

# Usuń urządzenie podrzędne (zalecana metoda)
result = await device_manager.remove_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    product_id="1734821218500292608",
    device_name="01000053"
)
```

### Dostępne metody

Aby uzyskać szczegółową dokumentację wszystkich dostępnych metod i ich parametrów, zobacz [dokumentację biblioteki heiman-connect](https://pypi.org/project/heiman-connect/).

<a name="advanced-configuration"></a>
## Zaawansowana konfiguracja

### Konfiguracja loggera

Włącz logowanie debugowania do rozwiązywania problemów:

```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.heiman_home: debug
    heimanconnect: debug
```

### Dostosowywanie encji

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

### Wykluczanie atrybutów

```yaml
# configuration.yaml
heiman_home:
  exclude_attributes:
    - raw_data
    - firmware_info
    - configuration
```

<a name="services"></a>
## Usługi

### `heiman_home.refresh_device`

Ręcznie zaktualizuj status urządzenia.

```yaml
service: heiman_home.refresh_device
data:
  device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

Zaktualizuj wszystkie urządzenia w integracji.

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## Debugowanie

### Pobieranie atrybutów statusu encji

1. Otwórz **Narzędzia deweloperskie** → **Stany**
2. Wyszukaj swoją encję (np. `sensor.heiman_temperature`)
3. Wyświetl wszystkie atrybuty i bieżący stan

### Pobieranie logów debugowania

1. Włącz logowanie debugowania (zobacz [Konfiguracja loggera](#advanced-configuration))
2. Otwórz **Ustawienia** → **System** → **Logi**
3. Wyszukaj `heiman_home` lub `heimanconnect`

### Częste problemy

#### Urządzenie nie jest wyświetlane
- Sprawdź ustawienia filtrowania urządzeń
- Upewnij się, że urządzenie jest online w aplikacji Heiman
- Uruchom ponownie integrację

#### Aktualizacja firmware'u nie działa
- Upewnij się, że urządzenie jest online
- Sprawdź kompatybilność urządzenia
- Upewnij się, że aktualizacja firmware'u jest dostępna w aplikacji Heiman

#### Problemy z połączeniem
- Sprawdź połączenie internetowe
- Sprawdź dane logowania do konta Heiman
- Sprawdź logi Home Assistant pod kątem błędów

#### MQTT nie łączy się
- Upewnij się, że sieć zezwala na połączenia wychodzące do `spmqtt.heiman.cn:1884`
- Sprawdź ustawienia zapory sieciowej
- Uruchom ponownie Home Assistant

<a name="troubleshooting"></a>
## Rozwiązywanie problemów

### Uwierzytelnianie nie powiodło się
1. Ponownie autoryzuj integrację
2. Sprawdź dane logowania do konta Heiman
3. Upewnij się, że konto ma dostęp do wybranego domu

#### Urządzenia nie są aktualizowane
1. Sprawdź status połączenia MQTT w logach
2. Upewnij się, że urządzenie jest online
3. Spróbuj ręcznej aktualizacji przez usługę

### Wysokie użycie bazy danych
- Wyklucz niepotrzebne atrybuty (zobacz [Wykluczanie atrybutów](#advanced-configuration))
- Wyłącz nieużywane encje
- Sprawdź encje ze zbyt wieloma zmianami stanu

### Problemy z wydajnością
- Zmniejsz interwał aktualizacji, jeśli to możliwe
- Filtruj nieużywane urządzenia
- Wyłącz MQTT, jeśli nie jest potrzebne (niezalecane)

<a name="development"></a>
## Rozwój

### Struktura projektu
```
heiman_home/
├── __init__.py          # Inicjalizacja integracji
├── api.py               # Wrapper klienta API
├── config_flow.py       # Przepływ konfiguracji
├── const.py             # Stałe i konfiguracja
├── coordinator.py       # Koordynator aktualizacji danych
├── sensor.py            # Platforma czujników
├── binary_sensor.py     # Platforma czujników binarnych
├── switch.py            # Platforma przełączników
├── button.py            # Platforma przycisków
├── select.py            # Platforma selektorów
├── number.py            # Platforma numeryczna
├── update.py            # Platforma aktualizacji (firmware)
├── manifest.json        # Metadane integracji
└── strings.json         # Tłumaczenia
```

**Uwaga**: Cała logika zarządzania urządzeniami znajduje się w bibliotece `heiman-connect`, a nie w tej integracji.

### Zależności
- `heiman-connect`: Biblioteka Python dla API Heiman
- `packaging`: Porównywanie wersji dla aktualizacji firmware'u

<a name="contributing"></a>
## Współtworzenie

Wkład jest mile widziany! Śmiało przesyłaj:
- Raporty błędów
- Prośby o funkcje
- Obsługę urządzeń
- Tłumaczenia
- Ulepszenia dokumentacji

<a name="license"></a>
## Licencja

Ten projekt jest objęty licencją MIT - zobacz plik [LICENSE](LICENSE) po szczegóły.

<a name="acknowledgments"></a>
## Podziękowania

- [Heiman](www.heimantech.com) za udostępnienie platformy IoT
- Społeczność [Home Assistant](https://www.home-assistant.io)
- [HACS](https://hacs.xyz) za framework integracji
- Wszystkim współtwórcom i testerom

<a name="support"></a>
## Wsparcie

- **GitHub Issues**: [Zgłaszanie błędów lub żądanie funkcji](https://github.com/hass-user/heiman-home/issues)
- **Forum społeczności Home Assistant**: [Dyskusje i uzyskiwanie pomocy](https://community.home-assistant.io/)
- **Dokumentacja**: [Pełna dokumentacja](https://github.com/hass-user/heiman-home/wiki)

---

**Ciesz się swoim inteligentnym domem z Heiman i Home Assistant! 🏠✨**
