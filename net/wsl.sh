database=postgresql
datasource.url=jdbc:postgresql://localhost:5432/shop?ssl=false
datasource.username=postgres
datasource.password=passward

ssh -i  Django-Training-User.pem  django-training-user@3.23.244.11 -p 52002


sudo apt install php
sudo apt install php-fpm

ip情報
ip a
ローカルのip確認
hostname -I

//
#システムの起動。停止。再起動
# sudo systemctl start postgresql@17-main
# sudo systemctl start postgresql
# sudo systemctl stop postgresql@17-main
# sudo systemctl restart postgresql@17-main
# sudo systemctl status postgresql
postgreでログイン
# sudo -i -u postgres
#sudo -u postgres psql
#systemctl list-units --type=service | grep postgres
#sudo systemctl status postgresql@17-main
#sudo systemctl start mariadb
#sudo systemctl enable mariadb
#ps aux | grep ssh

#SSH起動も忘れずに
# sudo systemctl start ssh
#sudo systemctl stop ssh
#SSHを貼る
#ssh -L 9000:localhost:5432 sou@172.26.43.86
#SSH張られている確認
#動いているプロセス
#ps aux | grep ssh
# sudo apt install openssh-client -y
#ローカルホストをsshにフォワーディング
# ssh sou@localhost
# ALTER ROLE user01 LOGIN;
# ALTER ROLE postgres WITH PASSWORD 'postgres';
# ALTER ROLE user01 WITH PASSWORD 'newpassword';

ALTER ROLE postgres WITH PASSWORD 'root';





export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"

sucddo apt update
sudo apt install build-essential git postgresql-server-dev-17

git clone https://github.com/pgvector/pgvector.git
cd pgvector
make
sudo make install

Java＊COBOL/金融向けシステム開発(No.K260161352)/パーソルクロステクノロジーのお仕事[E0257217453]
