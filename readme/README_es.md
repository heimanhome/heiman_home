# Heiman Home para HomeAssistant

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## Descripción General

Esta integración para Home Assistant permite el uso de dispositivos domésticos inteligentes Heiman dentro de un sistema de hogar inteligente. Se conecta a la API en la nube de Heiman y utiliza el protocolo MQTT para actualizaciones de estado del dispositivo en tiempo real.

Esta integración permite a los usuarios integrar fácilmente sus dispositivos Heiman en Home Assistant y utilizarlos para diversas automatizaciones y monitoreo, incluida la gestión de firmware y el control de dispositivos secundarios.

### Idiomas Disponibles

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

Si falta un idioma, háganoslo saber y haremos todo lo posible para agregarlo.

## Características

- 🔌 **Soporte Multi-dispositivo**: Puertas de enlace, sensores, interruptores, alarmas y más
- ☁️ **Integración en la Nube**: Conéctese a través de la cuenta Heiman con autenticación OAuth2
- 📡 **Actualizaciones MQTT en Tiempo Real**: Actualizaciones instantáneas del estado del dispositivo mediante push MQTT
- 🔄 **Gestión de Firmware**: Verifique e instale actualizaciones de firmware directamente desde Home Assistant
- 👨‍👩‍👧‍👦 **Gestión de Dispositivos Secundarios**: Agregue, elimine y administre subdispositivos de puerta de enlace a través de MQTT
- 🏠 **Soporte Multi-hogar**: Administre múltiples hogares Heiman de forma independiente
- 🎛️ **Entidades Completas**: Sensores, interruptores, botones, selectores, sensores binarios y entidades de actualización
- ⚙️ **Configuración Web UI**: Configuración fácil sin configuración YAML

<a name="installation"></a>
## Instalación


### Método 1: HACS (Recomendado)

#### Primera Instalación
1. Abra **HACS** → **Integraciones**
2. Haga clic en **+ EXPLORAR Y DESCARGAR REPOSITORIOS**
3. Busque `Heiman Home` o haga clic en los tres puntos (⋮) → **Repositorios personalizados**
4. Agregar repositorio: `https://github.com/hass-user/heiman-home` con categoría `Integration`
5. Haga clic en **DESCARGAR ESTE REPOSITORIO**

#### Actualizar Componente
1. Abra **HACS** → **Integraciones**
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. Encuentre **Heiman Home**
   ![img.png](image/img.png)
3. Haga clic en ****ACTUALIZAR** o **Volver a descargar****
   ![img_1.png](image/img_1.png)
### Método 2: Instalación Manual vía Samba/SFTP

1. Descargue la última versión desde [GitHub Releases](https://github.com/hass-user/heiman-home/releases)
2. Extraiga la carpeta `heiman_home`
3. Copie la carpeta `heiman_home` a su directorio `custom_components` de Home Assistant
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### Método 3: Shell de un clic vía SSH/Terminal y SSH Add-on

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### Después de la Instalación

1. Reinicie Home Assistant
2. Vaya a **Configuración** → **Dispositivos y Servicios**
3. Haga clic en **+ Agregar Integración**
4. Busque `Heiman Home`

<a name="configuration"></a>
## Configuración

### Agregar Integración vía Web UI

1. Abra la interfaz web de Home Assistant
2. Navegue a **Configuración** → **Dispositivos y Servicios**
3. Haga clic en **Agregar Integración**
4. Busque `Heiman Home` y selecciónelo
5. Autorice con su cuenta Heiman (OAuth2)
6. Seleccione el hogar que desea integrar
7. Complete la configuración

### Autenticación

La integración utiliza OAuth2 para autenticación segura:
- Haga clic en **Autorizar** para iniciar sesión en su cuenta Heiman
- Otorgue los permisos necesarios
- Seleccione el hogar que desea integrar

### Múltiples Hogares

Puede agregar múltiples hogares Heiman:
1. Cada hogar crea una entrada de configuración separada
2. Cada hogar tiene gestión de dispositivos independiente
3. Configure cada hogar por separado en **Dispositivos y Servicios**

### Filtrado de Dispositivos

Puede filtrar qué dispositivos integrar:
1. Abra la configuración de la integración
2. Navegue a **Opciones**
3. Habilite/deshabilite dispositivos específicos
4. Guarde los cambios

<a name="supported-devices"></a>
## Dispositivos Soportados

### Puertas de Enlace
-  Puerta de Enlace Inteligente (WS3GW-R, etc.)
- 🌐 Puerta de Enlace Zigbee
- 🌐 Puerta de Enlace WiFi

### Sensores
- 🌡️ Sensores de Temperatura y Humedad
- 🚪 Sensores de Puerta/Ventana
- 💧 Sensores de Fuga de Agua
- 🔥 Sensores de Humo
- 💨 Sensores de Gas
- 🏃 Sensores de Movimiento
- 🌞 Sensores de Iluminación

### Alarmas y Seguridad
- 🚨 Sistemas de Alarma
- 🔔 Control de Sonido de Alarma
- 🚪 Control de Acceso

### Interruptores y Controles
- 🔌 Enchufes Inteligentes
- 💡 Interruptores de Luz
- 🎛️ Controladores de Escena

### Otros Dispositivos
- ️ Termostatos
- 💨 Monitores de Calidad del Aire
- 🔋 Dispositivos Alimentados por Batería

<a name="entities"></a>
## Tipos de Entidades

### Entidades de Sensor
- Temperatura
- Humedad
- Nivel de Batería
- Fuerza de Señal (RSSI)
- Iluminación
- Estado del Dispositivo

### Entidades de Sensor Binario
- Puerta/Ventana Abierta/Cerrada
- Movimiento Detectado
- Fuga de Agua
- Humo Detectado
- Estado de Manipulación
- Advertencia de Batería Baja

### Entidades de Interruptor
- Dispositivo Encendido/Apagado
- Luz Indicadora
- Control de Zumbador
- Alarma Habilitada/Deshabilitada

### Entidades de Botón
- Actualizar Estado del Dispositivo
- Verificación Remota
- Localización Remota
- Silencio Remoto

### Entidades de Selector
- Opciones de Sonido de Alarma (Pitido Rápido, Pitido Medio, Pitido Lento)
- Unidad de Temperatura (°C / °F)
- Modo de Operación
- Visualización de Nivel de Señal

### Entidades de Número
- Umbral Alto de Temperatura
- Umbral Bajo de Temperatura
- Umbral Alto de Humedad
- Umbral Bajo de Humedad
- Rango de Confort de Temperatura
- Rango de Confort de Humedad

### Entidades de Actualización
- Versión de Firmware
- Actualizaciones Disponibles
- Progreso de Instalación de Firmware

<a name="firmware-management"></a>
## Gestión de Firmware

### Buscar Actualizaciones
- Las actualizaciones de firmware se verifican automáticamente durante la sincronización del dispositivo
- Las entidades de actualización muestran las versiones de firmware disponibles
- Compare la versión instalada con la última versión disponible

### Instalar Actualizaciones de Firmware
1. Navegue al dispositivo en Home Assistant
2. Abra la entidad **Firmware**
3. Haga clic en el botón **Instalar**
4. Monitoree el progreso de la actualización en tiempo real
5. El dispositivo se reiniciará después de completar la actualización

### Funciones de Actualización
- ✅ Detección automática de versión
- ✅ Monitoreo de progreso (0-100%)
- ✅ Seguimiento del estado de actualización
- ✅ Comparación de versiones
- ✅ Verificación de actualizaciones por lotes

<a name="mqtt-integration"></a>
## Integración MQTT

### Actualizaciones en Tiempo Real
La integración utiliza MQTT para actualizaciones instantáneas del estado del dispositivo:
- Sin retraso de sondeo
- Cambios de estado instantáneos
- Menor uso de API
- Mejor rendimiento

### Configuración MQTT
- Se configura automáticamente durante la configuración
- Utiliza el broker MQTT de Heiman
- Conexión segura con TLS/SSL
- No se requiere configuración manual

### Funciones MQTT Soportadas
- Actualizaciones de propiedades del dispositivo
- Estado en línea/fuera de línea
- Eventos de alarma
- Lecturas de sensores
- Gestión de dispositivos secundarios (registro, cancelación de registro, descubrimiento)

<a name="child-device-management"></a>
## Gestión de Dispositivos Secundarios

La integración proporciona una gestión completa de dispositivos secundarios a través de la biblioteca `heiman-connect`.
Toda la lógica de gestión de dispositivos está implementada en el SDK, y la integración de Home Assistant proporciona una API simple para acceder a estas funciones.

### Uso del Administrador de Dispositivos Secundarios

```python
from heimanconnect import ChildDeviceManager

# Obtener el administrador de dispositivos secundarios del cliente API
device_manager = await api_client.async_get_child_device_manager(
    user_id="your_user_id",
    devices=devices_dict,
    user_display_name="Your Name"
)

# Agregar un dispositivo secundario (método recomendado)
result = await device_manager.add_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    child_product_id="1734821218500292608",
    child_device_name="Door Sensor"
)

# Eliminar un dispositivo secundario (método recomendado)
result = await device_manager.remove_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    product_id="1734821218500292608",
    device_name="01000053"
)
```

### Métodos Disponibles

Para documentación detallada de todos los métodos disponibles y sus parámetros, consulte la [documentación de la biblioteca heiman-connect](https://pypi.org/project/heiman-connect/).

<a name="advanced-configuration"></a>
## Configuración Avanzada

### Configuración de Logger

Habilite el registro de depuración para la solución de problemas:

```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.heiman_home: debug
    heimanconnect: debug
```

### Personalizar Entidades

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

### Excluir Atributos

```yaml
# configuration.yaml
heiman_home:
  exclude_attributes:
    - raw_data
    - firmware_info
    - configuration
```

<a name="services"></a>
## Servicios

### `heiman_home.refresh_device`

Actualizar manualmente el estado de un dispositivo.

```yaml
service: heiman_home.refresh_device
data:
  device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

Actualizar todos los dispositivos en la integración.

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## Depuración

### Obtener Atributos de Estado de Entidad

1. Abra **Herramientas para Desarrolladores** → **Estados**
2. Busque su entidad (por ejemplo, `sensor.heiman_temperature`)
3. Vea todos los atributos y el estado actual

### Obtener Registros de Depuración

1. Habilite el registro de depuración (ver [Configuración de Logger](#advanced-configuration))
2. Abra **Configuración** → **Sistema** → **Registros**
3. Busque `heiman_home` o `heimanconnect`

### Problemas Comunes

#### El Dispositivo No Aparece
- Verifique la configuración de filtrado de dispositivos
- Verifique que el dispositivo esté en línea en la aplicación Heiman
- Reinicie la integración

#### La Actualización de Firmware No Funciona
- Asegúrese de que el dispositivo esté en línea
- Verifique la compatibilidad del dispositivo
- Verifique que haya una actualización de firmware disponible en la aplicación Heiman

#### Problemas de Conexión
- Verifique la conexión a Internet
- Verifique las credenciales de la cuenta Heiman
- Verifique los registros de Home Assistant en busca de errores

#### MQTT No Se Conecta
- Verifique que la red permita conexiones salientes a `spmqtt.heiman.cn:1884`
- Verifique la configuración del firewall
- Reinicie Home Assistant

<a name="troubleshooting"></a>
## Solución de Problemas

### Autenticación Fallida
1. Vuelva a autorizar la integración
2. Verifique las credenciales de la cuenta Heiman
3. Verifique si la cuenta tiene acceso al hogar seleccionado

### Los Dispositivos No Se Actualizan
1. Verifique el estado de la conexión MQTT en los registros
2. Verifique que el dispositivo esté en línea
3. Intente actualizar manualmente a través del servicio

### Alto Uso de Base de Datos
- Excluya atributos innecesarios (ver [Excluir Atributos](#advanced-configuration))
- Deshabilite entidades no utilizadas
- Verifique entidades con demasiados cambios de estado

### Problemas de Rendimiento
- Reduzca el intervalo de actualización si es posible
- Filtre los dispositivos no utilizados
- Deshabilite MQTT si no es necesario (no recomendado)

<a name="development"></a>
## Desarrollo

### Estructura del Proyecto
```
heiman_home/
├── __init__.py          # Inicialización de la integración
├── api.py               # Wrapper del cliente API
├── config_flow.py       # Flujo de configuración
├── const.py             # Constantes y configuración
├── coordinator.py       # Coordinador de actualización de datos
├── sensor.py            # Plataforma de sensor
├── binary_sensor.py     # Plataforma de sensor binario
├── switch.py            # Plataforma de interruptor
├── button.py            # Plataforma de botón
├── select.py            # Plataforma de selector
├── number.py            # Plataforma de número
├── update.py            # Plataforma de actualización (firmware)
├── manifest.json        # Metadatos de la integración
└── strings.json         # Traducciones
```

**Nota**: Toda la lógica de gestión de dispositivos está en la biblioteca `heiman-connect`, no en esta integración.

### Dependencias
- `heiman-connect`: Biblioteca Python para la API de Heiman
- `packaging`: Comparación de versiones para actualizaciones de firmware

<a name="contributing"></a>
## Contribuir

¡Las contribuciones son bienvenidas! No dude en enviar:
- Informes de errores
- Solicitudes de funciones
- Soporte de dispositivos
- Traducciones
- Mejoras de documentación

<a name="license"></a>
## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulte el archivo [LICENSE](LICENSE) para más detalles.

<a name="acknowledgments"></a>
## Agradecimientos

- [Heiman](www.heimantech.com) por proporcionar la plataforma IoT
- Comunidad de [Home Assistant](https://www.home-assistant.io)
- [HACS](https://hacs.xyz) por el framework de integración
- Todos los contribuyentes y probadores

<a name="support"></a>
## Soporte

- **GitHub Issues**: [Informar errores o solicitar funciones](https://github.com/hass-user/heiman-home/issues)
- **Foro de la Comunidad Home Assistant**: [Discutir y obtener ayuda](https://community.home-assistant.io/)
- **Documentación**: [Documentación completa](https://github.com/hass-user/heiman-home/wiki)

---

**¡Disfrute de su hogar inteligente con Heiman y Home Assistant! 🏠✨**
