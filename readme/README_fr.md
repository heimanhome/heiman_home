# Heiman Home pour HomeAssistant

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## Aperçu

Cette intégration pour Home Assistant permet l'utilisation d'appareils domestiques intelligents Heiman au sein d'un système de maison intelligente. Elle se connecte à l'API cloud Heiman et utilise le protocole MQTT pour des mises à jour d'état d'appareil en temps réel.

Cette intégration permet aux utilisateurs d'intégrer facilement leurs appareils Heiman dans Home Assistant et de les utiliser pour diverses automatisations et surveillances, y compris la gestion du firmware et le contrôle des appareils enfants.

### Langues Disponibles

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

Si une langue manque, faites-le nous savoir et nous ferons de notre mieux pour l'ajouter.

## Fonctionnalités

- 🔌 **Support Multi-appareils**: Passerelles, capteurs, interrupteurs, alarmes et plus
- ☁️ **Intégration Cloud**: Connexion via compte Heiman avec authentification OAuth2
- 📡 **Mises à Jour MQTT en Temps Réel**: Mises à jour instantanées de l'état de l'appareil via push MQTT
- 🔄 **Gestion du Firmware**: Vérifiez et installez les mises à jour du firmware directement depuis Home Assistant
- 👨‍👩‍👧‍👦 **Gestion des Appareils Enfants**: Ajoutez, supprimez et gérez les sous-appareils de passerelle via MQTT
- 🏠 **Support Multi-maisons**: Gérez plusieurs maisons Heiman indépendamment
- 🎛️ **Entités Complètes**: Capteurs, interrupteurs, boutons, sélecteurs, capteurs binaires et entités de mise à jour
- ⚙️ **Configuration Web UI**: Configuration facile sans configuration YAML

<a name="installation"></a>
## Installation


### Méthode 1: HACS (Recommandé)

#### Première Installation
1. Ouvrez **HACS** → **Intégrations**
2. Cliquez sur **+ EXPLORER ET TÉLÉCHARGER DES DÉPÔTS**
3. Recherchez `Heiman Home` ou cliquez sur les trois points (⋮) → **Dépôts personnalisés**
4. Ajouter un dépôt: `https://github.com/hass-user/heiman-home` avec catégorie `Integration`
5. Cliquez sur **TÉLÉCHARGER CE DÉPÔT**

#### Mettre à Jour le Composant
1. Ouvrez **HACS** → **Intégrations**
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. Trouvez **Heiman Home**
   ![img.png](image/img.png)
3. Cliquez sur ****METTRE À JOUR** ou **Retélécharger****
   ![img_1.png](image/img_1.png)
### Méthode 2: Installation Manuelle via Samba/SFTP

1. Téléchargez la dernière version depuis [GitHub Releases](https://github.com/hass-user/heiman-home/releases)
2. Extrayez le dossier `heiman_home`
3. Copiez le dossier `heiman_home` dans votre répertoire `custom_components` de Home Assistant
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### Méthode 3: Shell One-Key via SSH/Terminal et SSH Add-on

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### Après l'Installation

1. Redémarrez Home Assistant
2. Allez dans **Paramètres** → **Appareils et Services**
3. Cliquez sur **+ Ajouter une Intégration**
4. Recherchez `Heiman Home`

<a name="configuration"></a>
## Configuration

### Ajouter une Intégration via Web UI

1. Ouvrez l'interface web de Home Assistant
2. Naviguez vers **Paramètres** → **Appareils et Services**
3. Cliquez sur **Ajouter une Intégration**
4. Recherchez `Heiman Home` et sélectionnez-le
5. Autorisez avec votre compte Heiman (OAuth2)
6. Sélectionnez la maison que vous souhaitez intégrer
7. Terminez la configuration

### Authentification

L'intégration utilise OAuth2 pour une authentification sécurisée:
- Cliquez sur **Autoriser** pour vous connecter à votre compte Heiman
- Accordez les autorisations requises
- Sélectionnez la maison que vous souhaitez intégrer

### Plusieurs Maisons

Vous pouvez ajouter plusieurs maisons Heiman:
1. Chaque maison crée une entrée de configuration séparée
2. Chaque maison a une gestion d'appareils indépendante
3. Configurez chaque maison séparément dans **Appareils et Services**

### Filtrage des Appareils

Vous pouvez filtrer quels appareils intégrer:
1. Ouvrez les paramètres d'intégration
2. Naviguez vers **Options**
3. Activez/désactivez des appareils spécifiques
4. Enregistrez les modifications

<a name="supported-devices"></a>
## Appareils Pris en Charge

### Passerelles
-  Passerelle Intelligente (WS3GW-R, etc.)
- 🌐 Passerelle Zigbee
- 🌐 Passerelle WiFi

### Capteurs
- 🌡️ Capteurs de Température et d'Humidité
- 🚪 Capteurs de Porte/Fenêtre
- 💧 Capteurs de Fuite d'Eau
- 🔥 Détecteurs de Fumée
- 💨 Capteurs de Gaz
- 🏃 Capteurs de Mouvement
- 🌞 Capteurs de Luminosité

### Alarmes et Sécurité
- 🚨 Systèmes d'Alarme
- 🔔 Contrôle du Son d'Alarme
- 🚪 Contrôle d'Accès

### Interrupteurs et Contrôles
- 🔌 Prises Intelligentes
- 💡 Interrupteurs d'Éclairage
- 🎛️ Contrôleurs de Scène

### Autres Appareils
- ️ Thermostats
- 💨 Moniteurs de Qualité de l'Air
- 🔋 Appareils Fonctionnant sur Batterie

<a name="entities"></a>
## Types d'Entités

### Entités de Capteur
- Température
- Humidité
- Niveau de Batterie
- Force du Signal (RSSI)
- Luminosité
- État de l'Appareil

### Entités de Capteur Binaire
- Porte/Fenêtre Ouverte/Fermée
- Mouvement Détecté
- Fuite d'Eau
- Fumée Détectée
- État de Sabotage
- Avertissement de Batterie Faible

### Entités d'Interrupteur
- Appareil Activé/Désactivé
- Voyant Lumineux
- Contrôle du Buzzer
- Alarme Activée/Désactivée

### Entités de Bouton
- Actualiser l'État de l'Appareil
- Vérification à Distance
- Localisation à Distance
- Mise en Sourde à Distance

### Entités de Sélecteur
- Options de Son d'Alarme (Bip Rapide, Bip Moyen, Bip Lent)
- Unité de Température (°C / °F)
- Mode de Fonctionnement
- Affichage du Niveau de Signal

### Entités de Nombre
- Seuil Haut de Température
- Seuil Bas de Température
- Seuil Haut d'Humidité
- Seuil Bas d'Humidité
- Plage de Confort de Température
- Plage de Confort d'Humidité

### Entités de Mise à Jour
- Version du Firmware
- Mises à Jour Disponibles
- Progression de l'Installation du Firmware

<a name="firmware-management"></a>
## Gestion du Firmware

### Rechercher des Mises à Jour
- Les mises à jour du firmware sont vérifiées automatiquement pendant la synchronisation de l'appareil
- Les entités de mise à jour affichent les versions de firmware disponibles
- Comparez la version installée avec la dernière version disponible

### Installer les Mises à Jour du Firmware
1. Naviguez vers l'appareil dans Home Assistant
2. Ouvrez l'entité **Firmware**
3. Cliquez sur le bouton **Installer**
4. Surveillez la progression de la mise à jour en temps réel
5. L'appareil redémarrera après avoir terminé la mise à jour

### Fonctionnalités de Mise à Jour
- ✅ Détection automatique de la version
- ✅ Surveillance de la progression (0-100%)
- ✅ Suivi de l'état de la mise à jour
- ✅ Comparaison des versions
- ✅ Vérification des mises à jour par lots

<a name="mqtt-integration"></a>
## Intégration MQTT

### Mises à Jour en Temps Réel
L'intégration utilise MQTT pour des mises à jour instantanées de l'état de l'appareil:
- Aucun délai de sondage
- Changements d'état instantanés
- Utilisation réduite de l'API
- Meilleures performances

### Configuration MQTT
- Configuré automatiquement pendant la configuration
- Utilise le broker MQTT Heiman
- Connexion sécurisée avec TLS/SSL
- Aucune configuration manuelle requise

### Fonctionnalités MQTT Prises en Charge
- Mises à jour des propriétés de l'appareil
- État en ligne/hors ligne
- Événements d'alarme
- Lectures de capteur
- Gestion des appareils enfants (enregistrement, désenregistrement, découverte)

<a name="child-device-management"></a>
## Gestion des Appareils Enfants

L'intégration fournit une gestion complète des appareils enfants via la bibliothèque `heiman-connect`.
Toute la logique de gestion des appareils est implémentée dans le SDK, et l'intégration Home Assistant fournit une API simple pour accéder à ces fonctionnalités.

### Utilisation du Gestionnaire d'Appareils Enfants

```python
from heimanconnect import ChildDeviceManager

# Obtenir le gestionnaire d'appareils enfants du client API
device_manager = await api_client.async_get_child_device_manager(
    user_id="your_user_id",
    devices=devices_dict,
    user_display_name="Your Name"
)

# Ajouter un appareil enfant (méthode recommandée)
result = await device_manager.add_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    child_product_id="1734821218500292608",
    child_device_name="Door Sensor"
)

# Supprimer un appareil enfant (méthode recommandée)
result = await device_manager.remove_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    product_id="1734821218500292608",
    device_name="01000053"
)
```

### Méthodes Disponibles

Pour une documentation détaillée de toutes les méthodes disponibles et leurs paramètres, consultez la [documentation de la bibliothèque heiman-connect](https://pypi.org/project/heiman-connect/).

<a name="advanced-configuration"></a>
## Configuration Avancée

### Configuration du Logger

Activez la journalisation de débogage pour le dépannage:

```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.heiman_home: debug
    heimanconnect: debug
```

### Personnaliser les Entités

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

### Exclure des Attributs

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

Actualiser manuellement l'état d'un appareil.

```yaml
service: heiman_home.refresh_device
data:
  device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

Actualiser tous les appareils dans l'intégration.

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## Débogage

### Obtenir les Attributs d'État de l'Entité

1. Ouvrez **Outils de Développement** → **États**
2. Recherchez votre entité (par exemple, `sensor.heiman_temperature`)
3. Affichez tous les attributs et l'état actuel

### Obtenir les Journaux de Débogage

1. Activez la journalisation de débogage (voir [Configuration du Logger](#advanced-configuration))
2. Ouvrez **Paramètres** → **Système** → **Journaux**
3. Recherchez `heiman_home` ou `heimanconnect`

### Problèmes Courants

#### L'Appareil N'apparaît Pas
- Vérifiez les paramètres de filtrage des appareils
- Assurez-vous que l'appareil est en ligne dans l'application Heiman
- Redémarrez l'intégration

#### La Mise à Jour du Firmware Ne Fonctionne Pas
- Assurez-vous que l'appareil est en ligne
- Vérifiez la compatibilité de l'appareil
- Assurez-vous qu'une mise à jour du firmware est disponible dans l'application Heiman

#### Problèmes de Connexion
- Vérifiez la connexion Internet
- Vérifiez les identifiants du compte Heiman
- Vérifiez les journaux de Home Assistant pour les erreurs

#### MQTT Ne Se Connecte Pas
- Assurez-vous que le réseau autorise les connexions sortantes vers `spmqtt.heiman.cn:1884`
- Vérifiez les paramètres du pare-feu
- Redémarrez Home Assistant

<a name="troubleshooting"></a>
## Dépannage

### Échec de l'Authentification
1. Réautorisez l'intégration
2. Vérifiez les identifiants du compte Heiman
3. Assurez-vous que le compte a accès à la maison sélectionnée

### Les Appareils Ne Sont Pas Mis à Jour
1. Vérifiez l'état de la connexion MQTT dans les journaux
2. Assurez-vous que l'appareil est en ligne
3. Essayez une actualisation manuelle via le service

### Utilisation Élevée de la Base de Données
- Excluez les attributs inutiles (voir [Exclure des Attributs](#advanced-configuration))
- Désactivez les entités inutilisées
- Vérifiez les entités avec trop de changements d'état

### Problèmes de Performance
- Réduisez l'intervalle de mise à jour si possible
- Filtrez les appareils inutilisés
- Désactivez MQTT si non nécessaire (non recommandé)

<a name="development"></a>
## Développement

### Structure du Projet
```
heiman_home/
├── __init__.py          # Initialisation de l'intégration
├── api.py               # Wrapper du client API
├── config_flow.py       # Flux de configuration
├── const.py             # Constantes et configuration
├── coordinator.py       # Coordinateur de mise à jour des données
├── sensor.py            # Plateforme de capteur
├── binary_sensor.py     # Plateforme de capteur binaire
├── switch.py            # Plateforme d'interrupteur
├── button.py            # Plateforme de bouton
├── select.py            # Plateforme de sélecteur
├── number.py            # Plateforme de nombre
├── update.py            # Plateforme de mise à jour (firmware)
├── manifest.json        # Métadonnées de l'intégration
└── strings.json         # Traductions
```

**Note**: Toute la logique de gestion des appareils se trouve dans la bibliothèque `heiman-connect`, pas dans cette intégration.

### Dépendances
- `heiman-connect`: Bibliothèque Python pour l'API Heiman
- `packaging`: Comparaison de versions pour les mises à jour du firmware

<a name="contributing"></a>
## Contribuer

Les contributions sont les bienvenues! N'hésitez pas à soumettre:
- Rapports de bogues
- Demandes de fonctionnalités
- Support d'appareils
- Traductions
- Améliorations de la documentation

<a name="license"></a>
## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

<a name="acknowledgments"></a>
## Remerciements

- [Heiman](www.heimantech.com) pour avoir fourni la plateforme IoT
- Communauté [Home Assistant](https://www.home-assistant.io)
- [HACS](https://hacs.xyz) pour le framework d'intégration
- Tous les contributeurs et testeurs

<a name="support"></a>
## Support

- **GitHub Issues**: [Signaler des bogues ou demander des fonctionnalités](https://github.com/hass-user/heiman-home/issues)
- **Forum de la Communauté Home Assistant**: [Discuter et obtenir de l'aide](https://community.home-assistant.io/)
- **Documentation**: [Documentation complète](https://github.com/hass-user/heiman-home/wiki)

---

**Profitez de votre maison intelligente avec Heiman et Home Assistant! 🏠✨**
