# Heiman Home HomeAssistant için

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## Genel Bakış

Bu Home Assistant entegrasyonu, akıllı ev sisteminde Heiman akıllı ev cihazlarının kullanımını mümkün kılar. Heiman bulut API'sine bağlanır ve cihaz durumunu gerçek zamanlı olarak güncellemek için MQTT protokolünü kullanır.

Bu entegrasyon ile kullanıcılar, Heiman cihazlarını kolayca Home Assistant'a entegre edebilir ve firmware yönetimi ve alt cihaz kontrolü dahil olmak üzere çeşitli otomasyonlar ve izleme için kullanabilirler.

### Mevcut Diller

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

Eksik bir dil varsa, lütfen bize bildirin. Eklemek için elimizden geleni yapacağız.

## Özellikler

- 🔌 **Çoklu Cihaz Desteği**: Ağ geçitleri, sensörler, anahtarlar, alarmlar ve daha fazlası
- ☁️ **Bulut Entegrasyonu**: OAuth2 kimlik doğrulama ile Heiman hesabı üzerinden bağlantı
- 📡 **MQTT Gerçek Zamanlı Güncellemeler**: MQTT push ile anlık cihaz durumu güncellemeleri
- 🔄 **Firmware Yönetimi**: Firmware güncellemelerini doğrudan Home Assistant'tan kontrol edin ve yükleyin
- 👨‍👩‍👧‍👦 **Alt Cihaz Yönetimi**: MQTT aracılığıyla ağ geçidi alt cihazlarını ekleyin, kaldırın ve yönetin
- 🏠 **Çoklu Ev Desteği**: Birden fazla Heiman evini bağımsız olarak yönetin
- 🎛️ **Kapsamlı Varlıklar**: Sensörler, anahtarlar, düğmeler, seçiciler, ikili sensörler ve güncelleme varlıkları
- ⚙️ **Web UI Yapılandırması**: YAML yapılandırması olmadan kolay kurulum

<a name="installation"></a>
## Kurulum


### Yöntem 1: HACS (Önerilen)

#### İlk Kurulum
1. **HACS** → **Entegrasyonlar**'ı açın
2. **+ DEPOLARI KEŞFET VE İNDİR**'e tıklayın
3. `Heiman Home` araması yapın veya üç noktaya (⋮) tıklayın → **Özel Depolar**
4. Depo ekle: `https://github.com/hass-user/heiman-home` kategori `Integration` ile
5. **BU DEPOYU İNDİR**'e tıklayın

#### Bileşeni Güncelleme
1. **HACS** → **Entegrasyonlar**'ı açın
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. **Heiman Home**'u bulun
   ![img.png](image/img.png)
3. **GÜNCELLE** veya **Tekrar indir**'e tıklayın**
   ![img_1.png](image/img_1.png)
### Yöntem 2: Samba/SFTP Üzerinden Manuel Kurulum

1. En son sürümü [GitHub Releases](https://github.com/hass-user/heiman-home/releases) adresinden indirin
2. `heiman_home` klasörünü çıkarın
3. `heiman_home` klasörünü Home Assistant `custom_components` dizinine kopyalayın
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### Yöntem 3: SSH/Terminal ve SSH Add-on Üzerinden One-Key-Shell

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### Kurulumdan Sonra

1. Home Assistant'ı yeniden başlatın
2. **Ayarlar** → **Cihazlar ve Hizmetler**'e gidin
3. **+ Entegrasyon ekle**'ye tıklayın
4. `Heiman Home` araması yapın

<a name="configuration"></a>
## Yapılandırma

### Web UI Üzerinden Entegrasyon Ekleme

1. Home Assistant web arayüzünü açın
2. **Ayarlar** → **Cihazlar ve Hizmetler**'e gidin
3. **Entegrasyon ekle**'ye tıklayın
4. `Heiman Home` araması yapın ve seçin
5. Heiman hesabınızla yetkilendirin (OAuth2)
6. Entegre etmek istediğiniz evi seçin
7. Kurulumu tamamlayın

### Kimlik Doğrulama

Entegrasyon, güvenli kimlik doğrulama için OAuth2 kullanır:
- Heiman hesabınıza giriş yapmak için **Yetkilendir**'e tıklayın
- Gerekli izinleri verin
- Entegre etmek istediğiniz evi seçin

### Birden Fazla Ev

Birden fazla Heiman evi ekleyebilirsiniz:
1. Her ev ayrı bir yapılandırma girişi oluşturur
2. Her ev bağımsız cihaz yönetimine sahiptir
3. **Cihazlar ve Hizmetler**'de her evi ayrı ayrı yapılandırın

### Cihaz Filtreleme

Hangi cihazların entegre edileceğini filtreleyebilirsiniz:
1. Entegrasyon ayarlarını açın
2. **Seçenekler**'e gidin
3. Belirli cihazları etkinleştirin/devre dışı bırakın
4. Değişiklikleri kaydedin

<a name="supported-devices"></a>
## Desteklenen Cihazlar

### Ağ Geçitleri
-  Akıllı Ağ Geçidi (WS3GW-R, vb.)
- 🌐 Zigbee Ağ Geçidi
- 🌐 WiFi Ağ Geçidi

### Sensörler
- 🌡️ Sıcaklık ve Nem Sensörleri
- 🚪 Kapı/Pencere Sensörleri
- 💧 Su Kaçak Sensörleri
- 🔥 Duman Dedektörleri
- 💨 Gaz Sensörleri
- 🏃 Hareket Sensörleri
- 🌞 Işık Şiddeti Sensörleri

### Alarmlar ve Güvenlik
- 🚨 Alarm Sistemleri
- 🔔 Alarm Sesi Kontrolü
- 🚪 Erişim Kontrolü

### Anahtarlar ve Kontroller
- 🔌 Akıllı Prizler
- 💡 Işık Anahtarları
- 🎛️ Sahne Kontrolleri

### Diğer Cihazlar
- ️ Termostatlar
- 💨 Hava Kalitesi Monitörleri
- 🔋 Pille Çalışan Cihazlar

<a name="entities"></a>
## Varlık Türleri

### Sensör Varlıkları
- Sıcaklık
- Nem
- Pil Seviyesi
- Sinyal Gücü (RSSI)
- Işık Şiddeti
- Cihaz Durumu

### İkili Sensör Varlıkları
- Kapı/Pencere Açık/Kapalı
- Hareket Algılandı
- Su Kaçağı
- Duman Algılandı
- Tahrifat Koruması Durumu
- Düşük Pil Uyarısı

### Anahtar Varlıkları
- Cihaz Açık/Kapalı
- Gösterge Lambası
- Zil Kontrolü
- Alarm Etkinleştir/Devre Dışı Bırak

### Düğme Varlıkları
- Cihaz Durumunu Güncelle
- Uzaktan Kontrol
- Uzaktan Konumlandırma
- Uzaktan Sessize Alma

### Seçici Varlıkları
- Alarm Sesi Seçenekleri (Hızlı Bip, Orta Bip, Yavaş Bip)
- Sıcaklık Birimi (°C / °F)
- Çalışma Modu
- Sinyal Seviyesi Göstergesi

### Sayısal Varlıklar
- Sıcaklık Üst Sınırı
- Sıcaklık Alt Sınırı
- Nem Üst Sınırı
- Nem Alt Sınırı
- Sıcaklık Konfor Aralığı
- Nem Konfor Aralığı

### Güncelleme Varlıkları
- Firmware Sürümü
- Mevcut Güncellemeler
- Firmware Kurulum İlerlemesi

<a name="firmware-management"></a>
## Firmware Yönetimi

### Güncellemeleri Kontrol Etme
- Firmware güncellemeleri cihaz senkronizasyonu sırasında otomatik olarak kontrol edilir
- Güncelleme varlıkları mevcut firmware sürümlerini gösterir
- Yüklü sürümü en son mevcut sürümle karşılaştırın

### Firmware Güncellemelerini Yükleme
1. Home Assistant'ta cihaza gidin
2. **Firmware** varlığını açın
3. **Yükle** düğmesine tıklayın
4. Güncelleme ilerlemesini gerçek zamanlı olarak izleyin
5. Güncelleme tamamlandıktan sonra cihaz yeniden başlatılır

### Güncelleme Özellikleri
- ✅ Otomatik sürüm algılama
- ✅ İlerleme izleme (0-100%)
- ✅ Güncelleme durumu takibi
- ✅ Sürüm karşılaştırması
- ✅ Toplu güncelleme kontrolü

<a name="mqtt-integration"></a>
## MQTT Entegrasyonu

### Gerçek Zamanlı Güncellemeler
Entegrasyon, anlık cihaz durumu güncellemeleri için MQTT kullanır:
- Anket gecikmesi yok
- Anında durum değişiklikleri
- Daha az API kullanımı
- Daha iyi performans

### MQTT Yapılandırması
- Kurulum sırasında otomatik olarak yapılandırılır
- Heiman MQTT Broker'ını kullanır
- TLS/SSL ile güvenli bağlantı
- Manuel yapılandırma gerekmez

### Desteklenen MQTT Özellikleri
- Cihaz özellik güncellemeleri
- Çevrimiçi/Çevrimdışı durumu
- Alarm olayları
- Sensör değerleri
- Alt cihaz yönetimi (kayıt, kayıt iptali, keşif)

<a name="child-device-management"></a>
## Alt Cihaz Yönetimi

Entegrasyon, `heiman-connect` kütüphanesi aracılığıyla kapsamlı alt cihaz yönetimi sunar.
Tüm cihaz yönetimi mantığı SDK'da uygulanmıştır ve Home Assistant entegrasyonu bu işlevlere erişim için basit bir API sağlar.

### Alt Cihaz Yöneticisini Kullanma

```python
from heimanconnect import ChildDeviceManager

# API istemcisinden alt cihaz yöneticisini alın
device_manager = await api_client.async_get_child_device_manager(
    user_id="your_user_id",
    devices=devices_dict,
    user_display_name="Your Name"
)

# Alt cihaz ekleme (önerilen yöntem)
result = await device_manager.add_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    child_product_id="1734821218500292608",
    child_device_name="Door Sensor"
)

# Alt cihaz kaldırma (önerilen yöntem)
result = await device_manager.remove_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    product_id="1734821218500292608",
    device_name="01000053"
)
```

### Mevcut Yöntemler

Mevcut tüm yöntemlerin ve parametrelerinin ayrıntılı belgelendirmesi için [heiman-connect kütüphane belgelerine](https://pypi.org/project/heiman-connect/) bakın.

<a name="advanced-configuration"></a>
## Gelişmiş Yapılandırma

### Logger Yapılandırması

Sorun giderme için hata ayıklama günlüğünü etkinleştirin:

```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.heiman_home: debug
    heimanconnect: debug
```

### Varlıkları Özelleştirme

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

### Öznitelikleri Hariç Tutma

```yaml
# configuration.yaml
heiman_home:
  exclude_attributes:
    - raw_data
    - firmware_info
    - configuration
```

<a name="services"></a>
## Hizmetler

### `heiman_home.refresh_device`

Bir cihazın durumunu manuel olarak güncelleyin.

```yaml
service: heiman_home.refresh_device
data:
  device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

Entegrasyondaki tüm cihazları güncelleyin.

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## Hata Ayıklama

### Varlık Durumu Özniteliklerini Alma

1. **Geliştirici Araçları** → **Durumlar**'ı açın
2. Varlığınızı arayın (örneğin, `sensor.heiman_temperature`)
3. Tüm öznitelikleri ve mevcut durumu görüntüleyin

### Hata Ayıklama Günlüklerini Alma

1. Hata ayıklama günlüğünü etkinleştirin (bkz. [Logger Yapılandırması](#advanced-configuration))
2. **Ayarlar** → **Sistem** → **Günlükler**'i açın
3. `heiman_home` veya `heimanconnect` araması yapın

### Yaygın Sorunlar

#### Cihaz Görünmüyor
- Cihaz filtreleme ayarlarını kontrol edin
- Cihazın Heiman uygulamasında çevrimiçi olduğundan emin olun
- Entegrasyonu yeniden başlatın

#### Firmware Güncellemesi Çalışmıyor
- Cihazın çevrimiçi olduğundan emin olun
- Cihaz uyumluluğunu kontrol edin
- Heiman uygulamasında firmware güncellemesinin mevcut olduğundan emin olun

#### Bağlantı Sorunları
- İnternet bağlantısını kontrol edin
- Heiman hesap kimlik bilgilerini kontrol edin
- Hatalar için Home Assistant günlüklerini kontrol edin

#### MQTT Bağlanmıyor
- Ağın `spmqtt.heiman.cn:1884` adresine giden bağlantılara izin verdiğinden emin olun
- Güvenlik duvarı ayarlarını kontrol edin
- Home Assistant'ı yeniden başlatın

<a name="troubleshooting"></a>
## Sorun Giderme

### Kimlik Doğrulama Başarısız Oldu
1. Entegrasyonu yeniden yetkilendirin
2. Heiman hesap kimlik bilgilerini kontrol edin
3. Hesabın seçili eve erişimi olduğundan emin olun

### Cihazlar Güncellenmiyor
1. Günlüklerde MQTT bağlantı durumunu kontrol edin
2. Cihazın çevrimiçi olduğundan emin olun
3. Hizmet aracılığıyla manuel güncelleme deneyin

### Yüksek Veritabanı Kullanımı
- Gereksiz öznitelikleri hariç tutun (bkz. [Öznitelikleri Hariç Tutma](#advanced-configuration))
- Kullanılmayan varlıkları devre dışı bırakın
- Çok fazla durum değişikliği olan varlıkları kontrol edin

### Performans Sorunları
- Mümkünse güncelleme aralığını azaltın
- Kullanılmayan cihazları filtreleyin
- Gerekmiyorsa MQTT'yi devre dışı bırakın (önerilmez)

<a name="development"></a>
## Geliştirme

### Proje Yapısı
```
heiman_home/
├── __init__.py          # Entegrasyon başlatma
├── api.py               # API istemci sarmalayıcı
├── config_flow.py       # Yapılandırma akışı
├── const.py             # Sabitler ve yapılandırma
├── coordinator.py       # Veri güncelleme koordinatörü
├── sensor.py            # Sensör platformu
├── binary_sensor.py     # İkili sensör platformu
├── switch.py            # Anahtar platformu
├── button.py            # Düğme platformu
├── select.py            # Seçici platformu
├── number.py            # Sayısal platform
├── update.py            # Güncelleme platformu (firmware)
├── manifest.json        # Entegrasyon meta verileri
└── strings.json         # Çeviriler
```

**Not**: Tüm cihaz yönetimi mantığı `heiman-connect` kütüphanesinde bulunur, bu entegrasyonda değil.

### Bağımlılıklar
- `heiman-connect`: Heiman API için Python kütüphanesi
- `packaging`: Firmware güncellemeleri için sürüm karşılaştırması

<a name="contributing"></a>
## Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Lütfen çekinmeyin:
- Hata raporları gönderin
- Özellik istekleri yapın
- Cihaz desteği ekleyin
- Çeviriler sağlayın
- Belgeleri iyileştirin

<a name="license"></a>
## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

<a name="acknowledgments"></a>
## Teşekkürler

- IoT platformunu sağladığı için [Heiman](www.heimantech.com)
- [Home Assistant](https://www.home-assistant.io) topluluğu
- Entegrasyon çerçevesi için [HACS](https://hacs.xyz)
- Tüm katkıda bulunanlar ve test edenler

<a name="support"></a>
## Destek

- **GitHub Issues**: [Hata bildirin veya özellik isteyin](https://github.com/hass-user/heiman-home/issues)
- **Home Assistant Topluluk Forumu**: [Tartışın ve yardım alın](https://community.home-assistant.io/)
- **Belgeler**: [Tam belgeler](https://github.com/hass-user/heiman-home/wiki)

---

**Heiman ve Home Assistant ile akıllı evinizin keyfini çıkarın! 🏠✨**
