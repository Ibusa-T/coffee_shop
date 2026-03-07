# cafee_shop
🚀 Geminiマート：品質保証・データ出力モデル構築プロジェクト
1. プロジェクト概要本プロジェクトは、設計済みの高度な分析SQL（ビュー）を Django アプリケーションに統合し、データの正確な出力とモデルへのマッピングを保証することを目的とする。

2. システム構成（使用技術）レイヤー技術選定備考環境管理uvPython環境・パッケージ管理の高速化言語Python

3. 3.12+最新の型ヒントを活用WebフレームワークDjango 5.0+ORMによるモデル管理とテスト機能の活用データベースSQLite (開発・検証用)Django内蔵。将来的なPostgreSQL移行を視野に設計デプロイ先Renderrender.yaml によるインフラ管理 (Blueprints)

4. 3. 実装要件3.1 データベース・モデル物理テーブル定義: CONSUMER, PRODUCT, SLIP, PRODUCT_TYPE の Django モデル実装。仮想ビューの統合: 以前設計した SQL ビュー（VISIT, DAILY_SALES, GENDER_SALES 等）を Django の Managed = False モデルとして定義し、分析データをオブジェクトとして扱えるようにする。3.2 出力機能分析用API/エンドポイント: ビューから取得したリピーター数や売上データを、JSON形式で正確に出力する機能。管理画面 (Django Admin): 各種データを確認・操作できるデバッグ用インターフェース。

4. 4. テスト要件 (STE ミッション)
  4.1 単体テスト (Unit Testing)pytest-django を使用したテストスイートの構築。データ整合性チェック: 意図的に「同日複数購入」や「性別不明」などのデータを投入し、ビューの計算結果（DENSE_RANK 等）が期待値と一致するかを検証。
  4.2 統合テスト (Integration Testing)モデルマッピング検証: SQL ビューの実行結果が Django モデルの各フィールドに正しく格納されていか。空データ検証: テーブルが空の状態でビューを叩いた際に、システムがクラッシュせず 0 や空リストを返すか。

5. デプロイ要件 (Render)render.yaml の作成（WebサービスおよびDB設定）。静的ファイル (WhiteNoise) および環境変数の設定。デプロイ後のスモークテスト環境の構築。

6. プロジェクト・ディレクトリ構成案

gemini-mart/
├── .python-version
├── pyproject.toml      # uv で管理
├── render.yaml         # Render デプロイ設定
├── src/
│   ├── manage.py
│   ├── core/           # プロジェクト設定
│   ├── sales/          # 売上・顧客管理アプリ
│   │   ├── models.py   # 物理テーブル + SQLビューモデル
│   │   ├── views.py
│   │   └── migrations/ # カスタムSQL(ビュー作成)を含む
│   └── tests/          # STEの主戦場
│       ├── test_models.py
│       └── test_views.py
└── data/               # テスト用初期データ(fixtures)
