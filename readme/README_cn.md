# Heiman Home 用于 HomeAssistant

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## 概述

此 Home Assistant 集成允许在智能家居系统中使用 Heiman 智能家居设备。它连接到 Heiman 云 API 并使用 MQTT 协议进行实时设备状态更新。

此集成使用户能够轻松地将他们的 Heiman 设备集成到 Home Assistant 中，并用于各种自动化和监控，包括固件管理和子设备控制。

### 可用语言

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

如果缺少某种语言，请告诉我们，我们将尽力添加。

## 功能特性

- 🔌 **多设备支持**：网关、传感器、开关、警报等
- ☁️ **云集成**：通过 Heiman 账户连接，使用 OAuth2 认证
- 📡 **MQTT 实时更新**：通过 MQTT 推送即时设备状态更新
- 🔄 **固件管理**：直接从 Home Assistant 检查和安装固件更新
- 👨‍👩‍👧‍👦 **子设备管理**：通过 MQTT 添加、删除和管理网管子设备
- 🏠 **多家庭支持**：独立管理多个 Heiman 家庭
- 🎛️ **全面的实体**：传感器、开关、按钮、选择器、二进制传感器和更新实体
- ⚙️ **Web UI 配置**：无需 YAML 配置的简单设置

<a name="installation"></a>
## 安装


### 方法 1：HACS（推荐）

#### 首次安装
1. 打开 **HACS** → **集成**
2. 点击 **+ 探索和下载存储库**
3. 搜索 `Heiman Home` 或点击三个点 (⋮) → **自定义存储库**
4. 添加存储库：`https://github.com/hass-user/heiman-home`，类别为 `Integration`
5. 点击 **下载此存储库**

#### 更新组件
1. 打开 **HACS** → **集成**
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. 找到 **Heiman Home**
   ![img.png](image/img.png)
3. 点击 ****更新** 或 **重新下载****
   ![img_1.png](image/img_1.png)
### 方法 2：通过 Samba/SFTP 手动安装

1. 从 [GitHub Releases](https://github.com/hass-user/heiman-home/releases) 下载最新版本
2. 解压 `heiman_home` 文件夹
3. 将 `heiman_home` 文件夹复制到您的 Home Assistant `custom_components` 目录
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### 方法 3：通过 SSH/Terminal 和 SSH Add-on 一键 Shell

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### 安装后

1. 重启 Home Assistant
2. 前往 **设置** → **设备与服务**
3. 点击 **+ 添加集成**
4. 搜索 `Heiman Home`

<a name="configuration"></a>
## 配置

### 通过 Web UI 添加集成

1. 打开 Home Assistant Web UI
2. 导航到 **设置** → **设备与服务**
3. 点击 **添加集成**
4. 搜索 `Heiman Home` 并选择它
5. 使用您的 Heiman 账户授权（OAuth2）
6. 选择您要集成的家庭
7. 完成设置

### 认证

集成使用 OAuth2 进行安全认证：
- 点击 **授权** 登录您的 Heiman 账户
- 授予必要的权限
- 选择您要集成的家庭

### 多个家庭

您可以添加多个 Heiman 家庭：
1. 每个家庭创建单独的配置条目
2. 每个家庭有独立的设备管理
3. 在 **设备与服务** 中分别配置每个家庭

### 设备过滤

您可以过滤要集成的设备：
1. 打开集成设置
2. 导航到 **选项**
3. 启用/禁用特定设备
4. 保存更改

<a name="supported-devices"></a>
## 支持的设备

### 网关
-  智能网关（WS3GW-R 等）
- 🌐 Zigbee 网关
- 🌐 WiFi 网关

### 传感器
- 🌡️ 温湿度传感器
- 🚪 门/窗传感器
- 💧 水浸传感器
- 🔥 烟雾传感器
- 💨 气体传感器
- 🏃 运动传感器
- 🌞 光照传感器

### 警报与安全
- 🚨 警报系统
- 🔔 警报声音控制
- 🚪 门禁控制

### 开关与控制
- 🔌 智能插座
- 💡 灯光开关
- 🎛️ 场景控制器

### 其他设备
- ️ 恒温器
- 💨 空气质量监测器
- 🔋 电池供电设备

<a name="entities"></a>
## 实体类型

### 传感器实体
- 温度
- 湿度
- 电池电量
- 信号强度（RSSI）
- 光照度
- 设备状态

### 二进制传感器实体
- 门/窗开/关
- 检测到运动
- 水浸
- 检测到烟雾
- 防拆状态
- 低电量警告

### 开关实体
- 设备开/关
- 指示灯
- 蜂鸣器控制
- 警报启用/禁用

### 按钮实体
- 刷新设备状态
- 远程检查
- 远程定位
- 远程静音

### 选择器实体
- 警报声音选项（快速蜂鸣、中速蜂鸣、慢速蜂鸣）
- 温度单位（°C / °F）
- 操作模式
- 信号电平显示

### 数值实体
- 温度高阈值
- 温度低阈值
- 湿度高阈值
- 湿度低阈值
- 温度舒适范围
- 湿度舒适范围

### 更新实体
- 固件版本
- 可用更新
- 固件安装进度

<a name="firmware-management"></a>
## 固件管理

### 检查更新
- 在设备同步期间自动检查固件更新
- 更新实体显示可用的固件版本
- 比较已安装版本与最新可用版本

### 安装固件更新
1. 在 Home Assistant 中导航到设备
2. 打开 **固件** 实体
3. 点击 **安装** 按钮
4. 实时监控更新进度
5. 更新完成后设备将重启

### 更新功能
- ✅ 自动版本检测
- ✅ 进度监控（0-100%）
- ✅ 更新状态跟踪
- ✅ 版本比较
- ✅ 批量更新检查

<a name="mqtt-integration"></a>
## MQTT 集成

### 实时更新
集成使用 MQTT 进行即时设备状态更新：
- 无轮询延迟
- 即时状态变化
- 更低的 API 使用量
- 更好的性能

### MQTT 配置
- 在设置期间自动配置
- 使用 Heiman MQTT 代理
- 使用 TLS/SSL 的安全连接
- 无需手动配置

### 支持的 MQTT 功能
- 设备属性更新
- 在线/离线状态
- 警报事件
- 传感器读数
- 子设备管理（注册、注销、发现）

<a name="child-device-management"></a>
## 子设备管理

集成通过 `heiman-connect` 库提供全面的子设备管理。
所有设备管理逻辑都在 SDK 中实现，Home Assistant 集成提供了简单的 API 来访问这些功能。

### 使用子设备管理器

```python
from heimanconnect import ChildDeviceManager

# 从 API 客户端获取子设备管理器
device_manager = await api_client.async_get_child_device_manager(
    user_id="your_user_id",
    devices=devices_dict,
    user_display_name="Your Name"
)

# 添加子设备（推荐方法）
result = await device_manager.add_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    child_product_id="1734821218500292608",
    child_device_name="Door Sensor"
)

# 移除子设备（推荐方法）
result = await device_manager.remove_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    product_id="1734821218500292608",
    device_name="01000053"
)
```

### 可用方法

有关所有可用方法及其参数的详细文档，请参阅 [heiman-connect 库文档](https://pypi.org/project/heiman-connect/)。

<a name="advanced-configuration"></a>
## 高级配置

### 日志配置

启用调试日志以进行故障排除：

```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.heiman_home: debug
    heimanconnect: debug
```

### 自定义实体

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

### 排除属性

```yaml
# configuration.yaml
heiman_home:
  exclude_attributes:
    - raw_data
    - firmware_info
    - configuration
```

<a name="services"></a>
## 服务

### `heiman_home.refresh_device`

手动刷新设备状态。

```yaml
service: heiman_home.refresh_device
data:
  device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

刷新集成中的所有设备。

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## 调试

### 获取实体状态属性

1. 打开 **开发者工具** → **状态**
2. 搜索您的实体（例如，`sensor.heiman_temperature`）
3. 查看所有属性和当前状态

### 获取调试日志

1. 启用调试日志（参见 [日志配置](#advanced-configuration)）
2. 打开 **设置** → **系统** → **日志**
3. 搜索 `heiman_home` 或 `heimanconnect`

### 常见问题

#### 设备未显示
- 检查设备过滤设置
- 验证设备在 Heiman 应用中是否在线
- 重启集成

#### 固件更新不起作用
- 确保设备在线
- 检查设备兼容性
- 验证 Heiman 应用中是否有固件更新可用

#### 连接问题
- 检查互联网连接
- 验证 Heiman 账户凭据
- 检查 Home Assistant 日志中的错误

#### MQTT 未连接
- 验证网络允许出站连接到 `spmqtt.heiman.cn:1884`
- 检查防火墙设置
- 重启 Home Assistant

<a name="troubleshooting"></a>
## 故障排除

### 认证失败
1. 重新授权集成
2. 验证 Heiman 账户凭据
3. 检查账户是否有访问所选家庭的权限

### 设备未更新
1. 检查日志中的 MQTT 连接状态
2. 验证设备是否在线
3. 尝试通过服务手动刷新

### 高数据库使用率
- 排除不必要的属性（参见 [排除属性](#advanced-configuration)）
- 禁用未使用的实体
- 检查状态变化过多的实体

### 性能问题
- 如果可能，减少更新间隔
- 过滤掉未使用的设备
- 如果不需要，禁用 MQTT（不推荐）

<a name="development"></a>
## 开发

### 项目结构
```
heiman_home/
├── __init__.py          # 集成初始化
├── api.py               # API 客户端包装器
├── config_flow.py       # 配置流程
├── const.py             # 常量和配置
├── coordinator.py       # 数据更新协调器
├── sensor.py            # 传感器平台
├── binary_sensor.py     # 二进制传感器平台
├── switch.py            # 开关平台
├── button.py            # 按钮平台
├── select.py            # 选择器平台
├── number.py            # 数值平台
├── update.py            # 更新平台（固件）
├── manifest.json        # 集成元数据
└── strings.json         # 翻译
```

**注意**：所有设备管理逻辑都在 `heiman-connect` 库中，而不是在此集成中。

### 依赖项
- `heiman-connect`：用于 Heiman API 的 Python 库
- `packaging`：用于固件更新的版本比较

<a name="contributing"></a>
## 贡献

欢迎贡献！请随时提交：
- 错误报告
- 功能请求
- 设备支持
- 翻译
- 文档改进

<a name="license"></a>
## 许可证

本项目根据 MIT 许可证授权 - 有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

<a name="acknowledgments"></a>
## 致谢

- [Heiman](www.heimantech.com) 提供 IoT 平台
- [Home Assistant](https://www.home-assistant.io) 社区
- [HACS](https://hacs.xyz) 提供集成框架
- 所有贡献者和测试者

<a name="support"></a>
## 支持

- **GitHub Issues**：[报告错误或请求功能](https://github.com/hass-user/heiman-home/issues)
- **Home Assistant 社区论坛**：[讨论和获取帮助](https://community.home-assistant.io/)
- **文档**：[完整文档](https://github.com/hass-user/heiman-home/wiki)

---

**享受使用 Heiman 和 Home Assistant 的智能家居！🏠✨**
