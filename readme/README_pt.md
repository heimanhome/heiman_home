# Heiman Home para HomeAssistant

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## Visão Geral

Esta integração do Home Assistant permite o uso de dispositivos domésticos inteligentes Heiman em um sistema de casa inteligente. Ela se conecta à API da nuvem Heiman e usa o protocolo MQTT para atualizações de status do dispositivo em tempo real.

Com esta integração, os usuários podem integrar facilmente dispositivos Heiman ao Home Assistant e usá-los para várias automações e monitoramento, incluindo gerenciamento de firmware e controle de dispositivos filhos.

### Idiomas disponíveis

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

Se algum idioma estiver faltando, avise-nos. Faremos o nosso melhor para adicioná-lo.

## Recursos

- 🔌 **Suporte a múltiplos dispositivos**: Gateways, sensores, interruptores, alarmes e mais
- ☁️ **Integração com nuvem**: Conecte via conta Heiman com autenticação OAuth2
- 📡 **Atualizações MQTT em tempo real**: Atualizações instantâneas de status do dispositivo via push MQTT
- 🔄 **Gerenciamento de firmware**: Verifique e instale atualizações de firmware diretamente do Home Assistant
- 👨‍👩‍👧‍👦 **Gerenciamento de dispositivos filhos**: Adicione, remova e gerencie subdispositivos do gateway via MQTT
- 🏠 **Suporte a múltiplas casas**: Gerencie várias casas Heiman independentemente
- 🎛️ **Entidades abrangentes**: Sensores, interruptores, botões, seletores, sensores binários e entidades de atualização
- ⚙️ **Configuração via interface web**: Configuração simples sem configuração YAML

<a name="installation"></a>
## Instalação


### Método 1: HACS (Recomendado)

#### Primeira instalação
1. Abra **HACS** → **Integrações**
2. Clique em **+ EXPLORAR E BAIXAR REPOSITÓRIOS**
3. Pesquise por `Heiman Home` ou clique nos três pontos (⋮) → **Repositórios personalizados**
4. Adicionar repositório: `https://github.com/hass-user/heiman-home` com categoria `Integration`
5. Clique em **BAIXAR ESTE REPOSITÓRIO**

#### Atualizar componente
1. Abra **HACS** → **Integrações**
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. Encontre **Heiman Home**
   ![img.png](image/img.png)
3. **Clique em **ATUALIZAR** ou **Baixar novamente****
   ![img_1.png](image/img_1.png)
### Método 2: Instalação manual via Samba/SFTP

1. Baixe a versão mais recente em [GitHub Releases](https://github.com/hass-user/heiman-home/releases)
2. Extraia a pasta `heiman_home`
3. Copie a pasta `heiman_home` para o diretório `custom_components` do Home Assistant
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### Método 3: One-Key-Shell via SSH/Terminal e SSH Add-on

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### Após a instalação

1. Reinicie o Home Assistant
2. Vá para **Configurações** → **Dispositivos e serviços**
3. Clique em **+ Adicionar integração**
4. Pesquise por `Heiman Home`

<a name="configuration"></a>
## Configuração

### Adicionar integração via interface web

1. Abra a interface web do Home Assistant
2. Navegue para **Configurações** → **Dispositivos e serviços**
3. Clique em **Adicionar integração**
4. Pesquise por `Heiman Home` e selecione-o
5. Autorize com sua conta Heiman (OAuth2)
6. Selecione a casa que deseja integrar
7. Conclua a configuração

### Autenticação

A integração usa OAuth2 para autenticação segura:
- Clique em **Autorizar** para fazer login na sua conta Heiman
- Conceda as permissões necessárias
- Selecione a casa que deseja integrar

### Múltiplas casas

Você pode adicionar várias casas Heiman:
1. Cada casa cria uma entrada de configuração separada
2. Cada casa tem gerenciamento de dispositivos independente
3. Configure cada casa separadamente em **Dispositivos e serviços**

### Filtragem de dispositivos

Você pode filtrar quais dispositivos devem ser integrados:
1. Abra as configurações da integração
2. Navegue para **Opções**
3. Ative/desative dispositivos específicos
4. Salve as alterações

<a name="supported-devices"></a>
## Dispositivos Suportados

### Gateways
-  Gateway inteligente (WS3GW-R, etc.)
- 🌐 Gateway Zigbee
- 🌐 Gateway WiFi

### Sensores
- 🌡️ Sensores de temperatura e umidade
- 🚪 Sensores de porta/janela
- 💧 Sensores de vazamento de água
- 🔥 Detectores de fumaça
- 💨 Sensores de gás
- 🏃 Sensores de movimento
- 🌞 Sensores de intensidade de luz

### Alarmes e segurança
- 🚨 Sistemas de alarme
- 🔔 Controle de som de alarme
- 🚪 Controle de acesso

### Interruptores e controles
- 🔌 Tomadas inteligentes
- 💡 Interruptores de luz
- 🎛️ Controladores de cena

### Outros dispositivos
- ️ Termostatos
- 💨 Monitores de qualidade do ar
- 🔋 Dispositivos alimentados por bateria

<a name="entities"></a>
## Tipos de Entidades

### Entidades de sensor
- Temperatura
- Umidade
- Nível da bateria
- Força do sinal (RSSI)
- Intensidade da luz
- Status do dispositivo

### Entidades de sensor binário
- Porta/janela aberta/fechada
- Movimento detectado
- Vazamento de água
- Fumaça detectada
- Status de violação
- Aviso de bateria fraca

### Entidades de interruptor
- Dispositivo ligado/desligado
- Luz indicadora
- Controle de buzina
- Alarme ativar/desativar

### Entidades de botão
- Atualizar status do dispositivo
- Verificação remota
- Localização remota
- Silenciamento remoto

### Entidades de seletor
- Opções de som de alarme (Bipe rápido, Bipe médio, Bipe lento)
- Unidade de temperatura (°C / °F)
- Modo de operação
- Indicador de nível de sinal

### Entidades numéricas
- Limite superior de temperatura
- Limite inferior de temperatura
- Limite superior de umidade
- Limite inferior de umidade
- Faixa de conforto de temperatura
- Faixa de conforto de umidade

### Entidades de atualização
- Versão do firmware
- Atualizações disponíveis
- Progresso da instalação do firmware

<a name="firmware-management"></a>
## Gerenciamento de Firmware

### Verificar atualizações
- As atualizações de firmware são verificadas automaticamente durante a sincronização do dispositivo
- As entidades de atualização mostram as versões de firmware disponíveis
- Compare a versão instalada com a versão mais recente disponível

### Instalar atualizações de firmware
1. Navegue até o dispositivo no Home Assistant
2. Abra a entidade **Firmware**
3. Clique no botão **Instalar**
4. Monitore o progresso da atualização em tempo real
5. O dispositivo será reiniciado após a conclusão da atualização

### Recursos de atualização
- ✅ Detecção automática de versão
- ✅ Monitoramento de progresso (0-100%)
- ✅ Rastreamento de status de atualização
- ✅ Comparação de versões
- ✅ Verificação de atualização em lote

<a name="mqtt-integration"></a>
## Integração MQTT

### Atualizações em tempo real
A integração usa MQTT para atualizações instantâneas de status do dispositivo:
- Sem atraso de polling
- Mudanças de status imediatas
- Menor uso da API
- Melhor desempenho

### Configuração MQTT
- Configurado automaticamente durante a instalação
- Usa o broker MQTT da Heiman
- Conexão segura com TLS/SSL
- Nenhuma configuração manual necessária

### Recursos MQTT suportados
- Atualizações de propriedades do dispositivo
- Status online/offline
- Eventos de alarme
- Leituras de sensor
- Gerenciamento de dispositivos filhos (registro, cancelamento de registro, detecção)

<a name="child-device-management"></a>
## Gerenciamento de Dispositivos Filhos

A integração oferece gerenciamento abrangente de dispositivos filhos através da biblioteca `heiman-connect`.
Toda a lógica de gerenciamento de dispositivos é implementada no SDK, e a integração do Home Assistant fornece uma API simples para acessar esses recursos.

### Usando o gerenciador de dispositivos filhos

```python
from heimanconnect import ChildDeviceManager

# Obter o gerenciador de dispositivos filhos do cliente API
device_manager = await api_client.async_get_child_device_manager(
    user_id="your_user_id",
    devices=devices_dict,
    user_display_name="Your Name"
)

# Adicionar dispositivo filho (método recomendado)
result = await device_manager.add_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    child_product_id="1734821218500292608",
    child_device_name="Door Sensor"
)

# Remover dispositivo filho (método recomendado)
result = await device_manager.remove_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    product_id="1734821218500292608",
    device_name="01000053"
)
```

### Métodos disponíveis

Para documentação detalhada de todos os métodos disponíveis e seus parâmetros, consulte a [documentação da biblioteca heiman-connect](https://pypi.org/project/heiman-connect/).

<a name="advanced-configuration"></a>
## Configuração Avançada

### Configuração do logger

Ative o log de depuração para solução de problemas:

```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.heiman_home: debug
    heimanconnect: debug
```

### Personalizar entidades

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

### Excluir atributos

```yaml
# configuration.yaml
heiman_home:
  exclude_attributes:
    - raw_data
    - firmware_info
    - configuration
```

<a name="services"></a>
## Serviços

### `heiman_home.refresh_device`

Atualize manualmente o status de um dispositivo.

```yaml
service: heiman_home.refresh_device
data:
  device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

Atualize todos os dispositivos na integração.

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## Depuração

### Obter atributos de status da entidade

1. Abra **Ferramentas do desenvolvedor** → **Estados**
2. Pesquise sua entidade (por exemplo, `sensor.heiman_temperature`)
3. Exiba todos os atributos e o estado atual

### Obter logs de depuração

1. Ative o log de depuração (veja [Configuração do logger](#advanced-configuration))
2. Abra **Configurações** → **Sistema** → **Logs**
3. Pesquise por `heiman_home` ou `heimanconnect`

### Problemas comuns

#### Dispositivo não aparece
- Verifique as configurações de filtro de dispositivos
- Certifique-se de que o dispositivo está online no aplicativo Heiman
- Reinicie a integração

#### Atualização de firmware não funciona
- Certifique-se de que o dispositivo está online
- Verifique a compatibilidade do dispositivo
- Certifique-se de que uma atualização de firmware está disponível no aplicativo Heiman

#### Problemas de conexão
- Verifique a conexão com a internet
- Verifique as credenciais da conta Heiman
- Verifique os logs do Home Assistant em busca de erros

#### MQTT não conecta
- Certifique-se de que a rede permite conexões de saída para `spmqtt.heiman.cn:1884`
- Verifique as configurações do firewall
- Reinicie o Home Assistant

<a name="troubleshooting"></a>
## Solução de problemas

### Autenticação falhou
1. Reautorize a integração
2. Verifique as credenciais da conta Heiman
3. Certifique-se de que a conta tem acesso à casa selecionada

### Dispositivos não estão sendo atualizados
1. Verifique o status da conexão MQTT nos logs
2. Certifique-se de que o dispositivo está online
3. Tente uma atualização manual através do serviço

### Alto uso do banco de dados
- Exclua atributos desnecessários (veja [Excluir atributos](#advanced-configuration))
- Desative entidades não utilizadas
- Verifique entidades com muitas mudanças de estado

### Problemas de desempenho
- Reduza o intervalo de atualização, se possível
- Filtre dispositivos não utilizados
- Desative o MQTT se não for necessário (não recomendado)

<a name="development"></a>
## Desenvolvimento

### Estrutura do projeto
```
heiman_home/
├── __init__.py          # Inicialização da integração
├── api.py               # Wrapper do cliente API
├── config_flow.py       # Fluxo de configuração
├── const.py             # Constantes e configuração
├── coordinator.py       # Coordenador de atualização de dados
├── sensor.py            # Plataforma de sensores
├── binary_sensor.py     # Plataforma de sensores binários
├── switch.py            # Plataforma de interruptores
├── button.py            # Plataforma de botões
├── select.py            # Plataforma de seletores
├── number.py            # Plataforma numérica
├── update.py            # Plataforma de atualização (firmware)
├── manifest.json        # Metadados da integração
└── strings.json         # Traduções
```

**Nota**: Toda a lógica de gerenciamento de dispositivos está na biblioteca `heiman-connect`, não nesta integração.

### Dependências
- `heiman-connect`: Biblioteca Python para API Heiman
- `packaging`: Comparação de versões para atualizações de firmware

<a name="contributing"></a>
## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar:
- Relatórios de bugs
- Solicitações de recursos
- Suporte a dispositivos
- Traduções
- Melhorias na documentação

<a name="license"></a>
## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

<a name="acknowledgments"></a>
## Agradecimentos

- [Heiman](www.heimantech.com) por fornecer a plataforma IoT
- Comunidade [Home Assistant](https://www.home-assistant.io)
- [HACS](https://hacs.xyz) pelo framework de integração
- Todos os contribuidores e testadores

<a name="support"></a>
## Suporte

- **GitHub Issues**: [Relatar bugs ou solicitar recursos](https://github.com/hass-user/heiman-home/issues)
- **Fórum da comunidade Home Assistant**: [Discutir e obter ajuda](https://community.home-assistant.io/)
- **Documentação**: [Documentação completa](https://github.com/hass-user/heiman-home/wiki)

---

**Aproveite sua casa inteligente com Heiman e Home Assistant! 🏠✨**
