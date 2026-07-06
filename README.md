# Heiman Home

Official Home Assistant cloud integration for Heiman smart home devices.

<p align="center">
  <img src="custom_components/heiman_home/brand/logo@2x.png" width="420">
</p>

<p align="center">

![HACS](https://img.shields.io/badge/HACS-Default-blue)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.7%2B-41BDF5)
![License](https://img.shields.io/badge/License-Apache%202.0-green)

</p>

---

## Overview

Heiman Home brings native integration between Home Assistant and Heiman smart home devices.

The integration provides secure OAuth2 authentication, automatic device discovery, MQTT real-time updates, firmware management, and seamless support for multiple Heiman homes.

### Key Features

- OAuth2 secure authentication
- MQTT real-time device updates
- Multi-home support
- Firmware update management
- Device diagnostics
- Battery monitoring
- Remote self-test
- Remote silence
- Home Assistant native entities
- HACS installation support

---

## Supported Devices

### Safety Devices

- Smoke Alarms
- Carbon Monoxide Alarms
- Heat Alarms
- Gas Sensors

### Environmental Sensors

- Temperature Sensors
- Humidity Sensors
- Water Leak Sensors
- Motion Sensors

### Gateways

- Zigbee Gateways
- Wi-Fi Gateways
- Smart Home Hubs

---

## Supported Entities

| Entity Type | Supported |
|------------|------------|
| Sensor | ✅ |
| Binary Sensor | ✅ |
| Switch | ✅ |
| Button | ✅ |
| Select | ✅ |
| Update | ✅ |

---

## Installation

### HACS (Recommended)

1. Open HACS
2. Navigate to Integrations
3. Add Custom Repository

```
https://github.com/heimanhome/heiman_home
```

4. Select category:

```
Integration
```

5. Install
6. Restart Home Assistant

---

## Configuration

1. Open Home Assistant
2. Settings → Devices & Services
3. Add Integration
4. Search:

```
Heiman Home
```

5. Login using your Heiman account
6. Authorize Home Assistant
7. Select your Home
8. Finish setup

---

## Home Assistant Support

Compatible with:

- Home Assistant OS
- Home Assistant Container
- Home Assistant Supervised
- Home Assistant Core

---

## Community Driven

Many features were developed directly from feedback provided by Home Assistant users.

Current supported advanced features include:

- Remote Silence
- Remote Self-Test
- Device Diagnostics
- Siren Control
- Battery Status
- Tamper Detection
- OTA Upgrade Support

More features will continue to be added through future updates.

---

## Documentation

https://leo2442926161.github.io/heiman-docs/

---

## License

Apache 2.0