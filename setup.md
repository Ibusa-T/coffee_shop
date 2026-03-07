🚀 Geminiマート：プロジェクトセットアップガイド
1. 事前準備（Windows環境）
まずは、Python本体と高速なパッケージ管理ツール uv をWindowsにインストールする。

Python のインストール
Python公式サイト から最新版（3.12以上推奨）をダウンロード。

インストーラー実行時、必ず「Add Python.exe to PATH」にチェックを入れること。

uv のインストール
PowerShellを開き、以下のコマンドを実行する。

PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
完了後、ターミナルを再起動して uv --version が動くことを確認。

2. プロジェクト初期化コマンド
ディレクトリの作成から、Djangoアプリの作成までを一気に uv で実行する。

PowerShell
# プロジェクトフォルダ作成と移動
mkdir gemini_mart_project
cd gemini_mart_project

# プロジェクト初期化
uv init

# 必要なパッケージの追加
uv add django whitenoise
uv add --dev pytest pytest-django

# Djangoプロジェクト(gemini_mart)の作成
uv run django-admin startproject gemini_mart .

# アプリケーション(cofee_shop)の作成
uv run python manage.py startapp cofee_shop

# pytest設定ファイルの作成
echo "[pytest]\nDJANGO_SETTINGS_MODULE = gemini_mart.settings\npython_files = tests.py test_*.py *_tests.py" > pytest.ini
3. WhiteNoise & 静的ファイル設定 (settings.py)
gemini_mart/settings.py を開き、以下の箇所を修正・追記する。

MIDDLEWARE の修正
SecurityMiddleware の直後に WhiteNoise を追加する。

Python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ←ここを追加
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... 他のミドルウェア
]
静的ファイル設定の追記
ファイルの末尾（STATIC_URL 付近）に以下の設定を記述する。

Python
import os

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise ストレージ設定（圧縮とキャッシュを有効化）
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
4. 起動確認
環境が正しく構築されたか、以下のコマンドでテストする。

PowerShell
# データベースの初期化（SQLite）
uv run python manage.py migrate

# 開発サーバーの起動
uv run python manage.py runserver
ブラウザで http://127.0.0.1:8000/ にアクセスし、Djangoのロケットが表示されれば成功だ。

5. STE（テストエンジニア）の次のステップ
セットアップが完了したら、いよいよ本題の「テストと実装」だ。

モデル定義: cofee_shop/models.py に物理テーブル（SLIP, CONSUMER等）を定義する。

ビュー作成: 設計したSQLをマイグレーションファイルとして書き出し、SQLite上にVIEWを構築する。

テスト記述: tests/ ディレクトリを作成し、データの整合性テストを開始する。
