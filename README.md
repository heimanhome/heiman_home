<p align="center">

![HACS](https://img.shields.io/badge/HACS-Default-blue)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.7%2B-41BDF5)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
</p>


---
<p align="left">
  <img src="custom_components/heiman_home/brand/logo@2x.png" width="640">
</p>


# Heiman Home
Official Home Assistant cloud integration for Heiman smart home devices.

> ⚠️ Worth to note:
>
> Currently this integration supports Heiman Cloud devices only, Local Zigbee device integration is not included at this time.


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
- Heat Alarms (Under Development)
- Carbon Monoxide Alarms (Planned)


### Environmental Sensors
- Temperature and Humidity Sensors (Planned)
- Water Leak Sensors

### Gateways
- Smart RF Hub (**SubG RF radio only**)
- Smart Zigbee Gatewat(Planned)


---

## Installation

### HACS (Recommended)
1. Click the icon and install Heiman Home:
[![Install Heiman Home](https://community-assets.home-assistant.io/original/4X/8/c/d/8cd1e59d88b00047b1b5ef5e19611794f3699618.png)](https://my.home-assistant.io/redirect/hacs_repository/?owner=heimanhome&repository=heiman_home&category=integration)

2. Restart Home Assistant

---


## Configuration

1. Open Home Assistant
2. Settings → Devices & Services
3. Add Integration
4. Search **Heiman Home**
5. Login using your Heiman account
6. Authorize Home Assistant
7. Select your Home
8. Finish setup

---


## Documentation 
[Heiman Home – How to Connect Heiman Home Integration](https://support.heimanhome.com/faq/?type=detail&id=1)

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
- Tamper/Mount Detection
- OTA Upgrade Support

More features will continue to be added through future updates.


---

## How to Ask Questions

If you have questions, feature requests, or need help with setup, please open a GitHub Issue.

Before opening an issue, please include as much information as possible:

- Home Assistant version
- Heiman Home integration version
- Installation method, for example HACS or manual installation
- Device model
- Problem description
- Error logs, if available
- Screenshots, if helpful

Please avoid sharing sensitive information such as passwords, tokens, or account credentials.


[GitHub Issues Page](https://github.com/heimanhome/heiman_home/issues)


---

## How to Contribute

Contributions are welcome.

You can help this project by:

- Reporting bugs
- Suggesting new features
- Improving documentation
- Testing new versions
- Submitting pull requests
- Sharing feedback from real Home Assistant usage

### Contributing Code

1. Fork this repository
2. Create a new branch
```bash
git checkout -b feature/your-feature-name
```

3. Make your changes
4. Test the integration locally
5. Commit your changes
6. git commit -m "Add your feature description"
7. Push your branch
```bash
git push origin feature/your-feature-name
```

8. Open a Pull Request

Please keep pull requests focused and describe clearly what has been changed.

---


## Support:
Email: support@heimanhome.com