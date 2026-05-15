# Heiman Home ホームアシスタント用

---
![logo@2x.png](custom_components/heiman_home/brand/logo%402x.png)
## 概要

このHome Assistant統合は、スマートホームシステム内でHeimanスマートホームデバイスの使用を可能にします。HeimanクラウドAPIに接続し、リアルタイムのデバイスステータス更新のためにMQTTプロトコルを使用します。

この統合により、ユーザーはHeimanデバイスをHome Assistantに簡単に統合し、ファームウェア管理や子デバイス制御を含むさまざまな自動化と監視に使用できます。

### 利用可能な言語

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

言語が不足している場合は、お知らせください。追加できるよう最善を尽くします。

## 機能

- 🔌 **マルチデバイスサポート**: ゲートウェイ、センサー、スイッチ、アラームなど
- ☁️ **クラウド統合**: OAuth2認証を使用してHeimanアカウント経由で接続
- 📡 **MQTTリアルタイム更新**: MQTTプッシュによる即時デバイスステータス更新
- 🔄 **ファームウェア管理**: Home Assistantから直接ファームウェア更新を確認・インストール
- 👨‍👩‍👧‍👦 **子デバイス管理**: MQTTを介してゲートウェイサブデバイスを追加、削除、管理
- 🏠 **マルチホームサポート**: 複数のHeimanホームを独立して管理
- 🎛️ **包括的なエンティティ**: センサー、スイッチ、ボタン、セレクター、バイナリセンサー、更新エンティティ
- ⚙️ **Web UI設定**: YAML設定なしで簡単なセットアップ

<a name="installation"></a>
## インストール


### 方法1: HACS（推奨）

#### 初回インストール
1. **HACS** → **インテグレーション**を開く
2. **+ リポジトリを探索してダウンロード**をクリック
3. `Heiman Home`を検索するか、三点リーダー（⋮）→ **カスタムリポジトリ**をクリック
4. リポジトリを追加: `https://github.com/hass-user/heiman-home` カテゴリ `Integration`
5. **このリポジトリをダウンロード**をクリック

#### コンポーネントを更新
1. **HACS** → **インテグレーション**を開く
   ![Download (1)](https://github.com/Elwinmage/ha-xsense-component/assets/15807572/3220c686-f53f-4766-9523-e3272a6ff104)
2. **Heiman Home**を見つける
   ![img.png](image/img.png)
3. ****更新**または**再ダウンロード**をクリック**
   ![img_1.png](image/img_1.png)
### 方法2: Samba/SFTP経由の手動インストール

1. [GitHub Releases](https://github.com/hass-user/heiman-home/releases)から最新バージョンをダウンロード
2. `heiman_home`フォルダを抽出
3. `heiman_home`フォルダをHome Assistantの`custom_components`ディレクトリにコピー
   ```
   /config/custom_components/heiman_home/
   ```
![img_2.png](image/img_2.png)
![img_3.png](image/img_3.png)
### 方法3: SSH/TerminalおよびSSH Add-on経由のワンキーシェル

```shell
wget -O - https://raw.githubusercontent.com/hass-user/heiman-home/main/install.sh | bash -
```

### インストール後

1. Home Assistantを再起動
2. **設定** → **デバイスとサービス**に移動
3. **+ インテグレーションを追加**をクリック
4. `Heiman Home`を検索

<a name="configuration"></a>
## 設定

### Web UI経由でインテグレーションを追加

1. Home Assistant Webインターフェースを開く
2. **設定** → **デバイスとサービス**に移動
3. **インテグレーションを追加**をクリック
4. `Heiman Home`を検索して選択
5. Heimanアカウント（OAuth2）で承認
6. 統合したいホームを選択
7. 設定を完了

### 認証

インテグレーションは安全な認証のためにOAuth2を使用します：
- Heimanアカウントにログインするには**承認**をクリック
- 必要な権限を付与
- 統合したいホームを選択

### 複数のホーム

複数のHeimanホームを追加できます：
1. 各ホームが個別の設定エントリを作成
2. 各ホームが独立したデバイス管理を持つ
3. **デバイスとサービス**で各ホームを個別に設定

### デバイスフィルタリング

統合するデバイスをフィルタリングできます：
1. インテグレーション設定を開く
2. **オプション**に移動
3. 特定のデバイスを有効/無効
4. 変更を保存

<a name="supported-devices"></a>
## サポートされているデバイス

### ゲートウェイ
-  スマートゲートウェイ（WS3GW-Rなど）
- 🌐 Zigbeeゲートウェイ
- 🌐 WiFiゲートウェイ

### センサー
- 🌡️ 温度・湿度センサー
- 🚪 ドア/窓センサー
- 💧 水漏れセンサー
- 🔥 煙探知器
- 💨 ガスセンサー
- 🏃 動作センサー
- 🌞 照度センサー

### アラームとセキュリティ
- 🚨 アラームシステム
- 🔔 アラームサウンド制御
- 🚪 アクセス制御

### スイッチとコントロール
- 🔌 スマートプラグ
- 💡 ライトスイッチ
- 🎛️ シーンコントローラー

### その他のデバイス
- ️ サーモスタット
- 💨 空気質モニター
- 🔋 バッテリー駆動デバイス

<a name="entities"></a>
## エンティティタイプ

### センサーエンティティ
- 温度
- 湿度
- バッテリーレベル
- 信号強度（RSSI）
- 照度
- デバイスステータス

### バイナリセンサーエンティティ
- ドア/窓 開/閉
- 動作検知
- 水漏れ
- 煙検知
- タンパーステータス
- 低バッテリー警告

### スイッチエンティティ
- デバイス オン/オフ
- インジケーターライト
- ブザー制御
- アラーム 有効/無効

### ボタンエンティティ
- デバイスステータスを更新
- リモートチェック
- リモートローカライゼーション
- リモートミュート

### セレクターエンティティ
- アラームサウンドオプション（高速ビープ、中速ビープ、低速ビープ）
- 温度単位（°C / °F）
- 操作モード
- 信号レベル表示

### 数値エンティティ
- 高温閾値
- 低温閾値
- 高湿度閾値
- 低湿度閾値
- 温度快適範囲
- 湿度快適範囲

### 更新エンティティ
- ファームウェアバージョン
- 利用可能な更新
- ファームウェアインストール進捗

<a name="firmware-management"></a>
## ファームウェア管理

### 更新を確認
- デバイス同期中にファームウェア更新が自動的に確認されます
- 更新エンティティが利用可能なファームウェアバージョンを表示
- インストール済みバージョンと最新の利用可能バージョンを比較

### ファームウェア更新をインストール
1. Home Assistantでデバイスに移動
2. **ファームウェア**エンティティを開く
3. **インストール**ボタンをクリック
4. リアルタイムで更新進捗を監視
5. 更新完了後、デバイスが再起動

### 更新機能
- ✅ 自動バージョン検出
- ✅ 進捗監視（0-100%）
- ✅ 更新状態追跡
- ✅ バージョン比較
- ✅ バッチ更新チェック

<a name="mqtt-integration"></a>
## MQTT統合

### リアルタイム更新
インテグレーションは即時デバイスステータス更新のためにMQTTを使用します：
- ポーリング遅延なし
- 即時ステータス変更
- API使用量削減
- より良いパフォーマンス

### MQTT設定
- セットアップ中に自動的に構成
- Heiman MQTTブローカーを使用
- TLS/SSLによる安全な接続
- 手動設定不要

### サポートされているMQTT機能
- デバイスプロパティ更新
- オンライン/オフラインステータス
- アラームイベント
- センサー読み取り
- 子デバイス管理（登録、登録解除、検出）

<a name="child-device-management"></a>
## 子デバイス管理

インテグレーションは`heiman-connect`ライブラリを通じて包括的な子デバイス管理を提供します。
すべてのデバイス管理ロジックはSDKに実装されており、Home Assistantインテグレーションはこれらの機能にアクセスするためのシンプルなAPIを提供します。

### 子デバイスマネージャーの使用

```python
from heimanconnect import ChildDeviceManager

# APIクライアントから子デバイスマネージャーを取得
device_manager = await api_client.async_get_child_device_manager(
    user_id="your_user_id",
    devices=devices_dict,
    user_display_name="Your Name"
)

# 子デバイスを追加（推奨方法）
result = await device_manager.add_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    child_product_id="1734821218500292608",
    child_device_name="Door Sensor"
)

# 子デバイスを削除（推奨方法）
result = await device_manager.remove_and_sync_device(
    gateway_product_id="1733421468953686016",
    gateway_device_id="1760910156165971969",
    child_device_id="1768080341172985856",
    product_id="1734821218500292608",
    device_name="01000053"
)
```

### 利用可能なメソッド

利用可能なすべてのメソッドとそのパラメーターの詳細なドキュメントについては、[heiman-connectライブラリドキュメント](https://pypi.org/project/heiman-connect/)を参照してください。

<a name="advanced-configuration"></a>
## 高度な設定

### ロガー設定

トラブルシューティングのためにデバッグログを有効にする：

```yaml
# configuration.yaml
logger:
  default: warning
  logs:
    custom_components.heiman_home: debug
    heimanconnect: debug
```

### エンティティをカスタマイズ

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

### 属性を除外

```yaml
# configuration.yaml
heiman_home:
  exclude_attributes:
    - raw_data
    - firmware_info
    - configuration
```

<a name="services"></a>
## サービス

### `heiman_home.refresh_device`

デバイスのステータスを手動で更新。

```yaml
service: heiman_home.refresh_device
data:
  device_id: "1972646416676724736"
```

### `heiman_home.refresh_all_devices`

インテグレーション内のすべてのデバイスを更新。

```yaml
service: heiman_home.refresh_all_devices
```

<a name="debugging"></a>
## デバッグ

### エンティティステータス属性を取得

1. **開発者ツール** → **状態**を開く
2. エンティティを検索（例：`sensor.heiman_temperature`）
3. すべての属性と現在の状態を表示

### デバッグログを取得

1. デバッグログを有効にする（[ロガー設定](#advanced-configuration)を参照）
2. **設定** → **システム** → **ログ**を開く
3. `heiman_home`または`heimanconnect`を検索

### 一般的な問題

#### デバイスが表示されない
- デバイスフィルタ設定を確認
- Heimanアプリでデバイスがオンラインであることを確認
- インテグレーションを再起動

#### ファームウェア更新が機能しない
- デバイスがオンラインであることを確認
- デバイスの互換性を確認
- Heimanアプリでファームウェア更新が利用可能であることを確認

#### 接続問題
- インターネット接続を確認
- Heimanアカウントの認証情報を確認
- Home Assistantログでエラーを確認

#### MQTTが接続しない
- ネットワークが`spmqtt.heiman.cn:1884`へのアウトバウンド接続を許可していることを確認
- ファイアウォール設定を確認
- Home Assistantを再起動

<a name="troubleshooting"></a>
## トラブルシューティング

### 認証に失敗
1. インテグレーションを再承認
2. Heimanアカウントの認証情報を確認
3. アカウントが選択したホームにアクセスできることを確認

### デバイスが更新されない
1. ログでMQTT接続状態を確認
2. デバイスがオンラインであることを確認
3. サービス経由で手動更新を試みる

### 高いデータベース使用量
- 不要な属性を除外（[属性を除外](#advanced-configuration)を参照）
- 未使用のエンティティを無効化
- ステータス変更が多すぎるエンティティを確認

### パフォーマンス問題
- 可能であれば更新間隔を短縮
- 未使用のデバイスをフィルタリング
- 必要でない場合はMQTTを無効化（非推奨）

<a name="development"></a>
## 開発

### プロジェクト構造
```
heiman_home/
├── __init__.py          # インテグレーション初期化
├── api.py               # APIクライアントラッパー
├── config_flow.py       # 設定フロー
├── const.py             # 定数と設定
├── coordinator.py       # データ更新コーディネーター
├── sensor.py            # センサープラットフォーム
├── binary_sensor.py     # バイナリセンサープラットフォーム
├── switch.py            # スイッチプラットフォーム
├── button.py            # ボタンプラットフォーム
├── select.py            # セレクタープラットフォーム
├── number.py            # 数値プラットフォーム
├── update.py            # 更新プラットフォーム（ファームウェア）
├── manifest.json        # インテグレーションメタデータ
└── strings.json         # 翻訳
```

**注**: すべてのデバイス管理ロジックは`heiman-connect`ライブラリにあり、このインテグレーションにはありません。

### 依存関係
- `heiman-connect`: Heiman API用のPythonライブラリ
- `packaging`: ファームウェア更新のバージョン比較

<a name="contributing"></a>
## 貢献

貢献を歓迎します！お気軽にご提出ください：
- バグ報告
- 機能リクエスト
- デバイスサポート
- 翻訳
- ドキュメント改善

<a name="license"></a>
## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細については[LICENSE](LICENSE)ファイルを参照してください。

<a name="acknowledgments"></a>
## 謝辞

- IoTプラットフォームを提供してくれた[Heiman](www.heimantech.com)
- [Home Assistant](https://www.home-assistant.io)コミュニティ
- インテグレーションフレームワークのための[HACS](https://hacs.xyz)
- すべての貢献者とテスター

<a name="support"></a>
## サポート

- **GitHub Issues**: [バグを報告または機能をリクエスト](https://github.com/hass-user/heiman-home/issues)
- **Home Assistantコミュニティフォーラム**: [議論してヘルプを取得](https://community.home-assistant.io/)
- **ドキュメント**: [完全なドキュメント](https://github.com/hass-user/heiman-home/wiki)

---

**HeimanとHome Assistantでスマートホームをお楽しみください！ 🏠✨**
