# TAPデバイスを作成
sudo ip tuntap add dev tap0 mode tap

# 自身のインターフェースにゲートウェイとなるIPを付与（例: 192.168.50.1）
sudo ip addr add 192.168.50.1/24 dev tap0

# インターフェースを起動
sudo ip link set tap0 up


sudo apt update && sudo apt install dnsmasq -y


sudo nano /etc/dnsmasq.d/host-only.conf


# tap0 インターフェースに対してのみ動作させる
interface=tap0
bind-interfaces

# 割り当てるIPアドレスの範囲とリース期間（12時間）
dhcp-range=192.168.50.10,192.168.50.100,12h

# デフォルトゲートウェイ（自分自身）を指定
dhcp-option=option:router,192.168.50.1



sudo systemctl restart dnsmasq