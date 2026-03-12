# テスト用の部屋（名前空間）「test-ns」を作成
sudo ip netns add test-ns

# vethペア（仮想LANケーブル）を作成
sudo ip link add veth-ns type veth peer name veth-tap

# 片方を tap0 に接続し、もう片方を test-ns に入れる
sudo ip link set veth-tap master tap0
sudo ip link set veth-ns netns test-ns

# 両端を起動
sudo ip link set veth-tap up
sudo ip netns exec test-ns ip link set veth-ns up

# 【テスト】名前空間内でDHCPクライアントを動かしてIP取得
sudo ip netns exec test-ns dhclient veth-ns

# IPが割り当てられたか確認
sudo ip netns exec test-ns ip a