# 作業手順書

## 1. 作業手順

### ステップ1：Windows側の設定 (物理ネットワークの共有)

1.  **Hyper-V 仮想スイッチの作成:**
    *   `Hyper-V マネージャー` を開く。
    *   右側のペインから `仮想スイッチ マネージャー` を選択。
    *   `新しい仮想ネットワーク スイッチ` で `外部` を選択し、`仮想スイッチの作成` をクリック。
    *   **名前:** `任意の名前` (例: `WSLBridgeSwitch`) を設定。
    *   **外部ネットワーク:** インターネットに接続している物理ネットワークアダプター (通常は `Wi-Fi` や `イーサネット`) を選択。
    *   `適用` → `OK` をクリックして保存。

2.  **.wslconfig の編集:**
    *   `C:\Users\&lt;ユーザー名&gt;\.wslconfig` ファイルをテキストエディタで開く (なければ新規作成)。
    *   以下の内容を記述・保存する。`vmSwitch` には先ほど作成したスイッチ名を指定する。
        ```ini
        [wsl2]
        networkingMode=bridged
        vmSwitch=任意の名前
        ```
    *   **注意:** ファイルの拡張子が `.txt` にならないようにする。
    *   設定を反映させるため、管理者権限の PowerShell でWSLを完全に再起動する。
        ```powershell
        wsl --shutdown
        ```

### ステップ2：Linux側の設定 (Kali Linuxのルーター化)

WSLを再起動後、Kali Linuxターミナルで以下のコマンドを実行する。

1.  **仮想LANポート (`tap0`) の作成:**
    *   Linuxルーター内に「私設のLANポート」を増設する。
    ```bash
    # 仮想デバイス tap0 を作成
    sudo ip tuntap add dev tap0 mode tap
    
    # tap0 を有効化
    sudo ip link set tap0 up
    
    # tap0 に内部ネットワークのゲートウェイIPアドレスを割り当て
    sudo ip addr add 10.0.0.1/24 dev tap0
    ```

2.  **NAT (IPマスカレード) の有効化:**
    *   `tap0` に接続されたデバイスが `eth0` を通じてインターネットへアクセスできるように設定する。
    ```bash
    # 1. カーネルでIPv4パケット転送を有効化
    sudo sysctl -w net.ipv4.ip_forward=1
    
    # 2. iptables を使って、eth0 から出ていく通信の送信元IPアドレスを書き換える (MASQUERADE)
    sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    ```
    *   **確認コマンド:**
        ```bash
        # tap0 インターフェースが存在することを確認
        ip a show tap0
        
        # NATルールが追加されたことを確認
        sudo iptables -t nat -L POSTROUTING -n -v
        ```

### ステップ3：DHCPサーバーの構築 (`dnsmasq`)

`tap0` に接続してくるターゲットデバイスに対し、IPアドレスやゲートウェイ情報を自動配布するサーバーを構築する。

1.  **dnsmasq のインストール:**
    ```bash
    sudo apt update && sudo apt install dnsmasq -y
    ```

2.  **dnsmasq の設定:**
    *   メイン設定ファイル (`/etc/dnsmasq.conf`) を編集する。
        ```bash
        sudo nano /etc/dnsmasq.conf
        ```
    *   以下の行がコメントアウトされている場合は解除し、追記する。
        ```ini
        # 別のディレクトリにある詳細設定を読み込む
        conf-dir=/etc/dnsmasq.d/,*.conf
        # DNSのループを防ぐ
        domain-needed
        bogus-priv
        ```
    *   次に、DHCP用の詳細設定ファイル (`/etc/dnsmasq.d/hacking_lab.conf`) を新規作成・編集する。
        ```bash
        sudo nano /etc/dnsmasq.d/hacking_lab.conf
        ```
    *   以下の設定を記述する。
        ```ini
        # ===================================================
        # ハッキング実験用 DHCPサーバ設定 (dnsmasq)
        # ===================================================

        # 1. DHCP機能を有効にするインターフェースを指定 (tap0のみ)
        interface=tap0

        # 2. 貸し出すIPアドレスの範囲とリース時間 (10.0.0.10～10.0.0.50を12時間)
        dhcp-range=10.0.0.10,10.0.0.50,12h

        # 3. デフォルトゲートウェイを指定 (Kali自身のtap0アドレス)
        # これによりターゲットの通信がすべてKaliを経由する
        dhcp-option=3,10.0.0.1

        # 4. 配布するDNSサーバーを指定 (Google Public DNS)
        dhcp-option=6,8.8.8.8

        # 5. DHCPの動作ログを有効化
        log-dhcp
        ```

3.  **サービスの再起動とテスト:**
    ```bash
    # 設定を反映させるためにdnsmasqを再起動
    sudo systemctl restart dnsmasq
    
    # 設定ファイルの構文チェック
    dnsmasq --test 
    # "dnsmasq: syntax check OK." と表示されれば成功
    ```

---

## 2. 設定の永続化 (自動化スクリプト)

WSL2を再起動するとLinux側のネットワーク設定（`tap`デバイス、IPアドレス、`iptables`ルールなど）はリセットされる。以下のスクリプトを `setup_network.sh` などの名前で保存し、WSL起動時に実行することで設定を復元できる。

```bash
#!/bin/bash

echo "===== WSL2ネットワーク環境を構築します ====="

# 1. 仮想LANポート(tap0)を作成・設定
echo "[+] Creating and configuring tap0 interface..."
sudo ip tuntap add dev tap0 mode tap
sudo ip link set tap0 up
sudo ip addr add 10.0.0.1/24 dev tap0

# 2. IPフォワーディングとNATを有効化
echo "[+] Enabling IP forwarding and MASQUERADE..."
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# br0（iPad側）へのルートを明確にする
sudo ip route add 10.0.0.0/24 dev br0
# パケットの転送ルールを強制許可
sudo iptables -I FORWARD -j ACCEPT


# 3. DHCPサーバー(dnsmasq)を再起動
echo "[+] Restarting dnsmasq service..."
sudo systemctl restart dnsmasq

echo "===== 構築が完了しました ====="

# 状態確認
echo "
[INFO] Current interface status:"
ip a | grep -E "eth0|tap0"

echo "
[INFO] Current NAT rules:"
sudo iptables -t nat -L POSTROUTING -n -v
```
**実行方法:** `bash setup_network.sh`

---

# ブリッジデバイス(br0)を作成
sudo ip link add br0 type bridge
# tap0 をブリッジに所属させる
sudo ip link set tap0 master br0
# 両方を起動
sudo ip link set dev br0 up
sudo ip link set dev tap0 up
