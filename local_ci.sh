#manage.py runserver
#!/bin/bash

# --- 設定: エラーが発生したら即座にスクリプトを中断する ---
set -e

# --- 見栄えを良くするための色設定 (Git Bash用) ---
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}   🚀 Local CI/CD Pipeline Starting...   ${NC}"
echo -e "${GREEN}=========================================${NC}"

# 1. 依存関係のチェックと同期
# uv.lockとpyproject.tomlに基づいて、環境を最新に保ちます
echo -e "\n📦 Step 1: Syncing dependencies with uv..."
uv sync

# 2. Djangoのシステムチェック
# モデル定義のミスや、設定ファイルの不備を事前に検知します
echo -e "\n🔍 Step 2: Running Django system check..."
uv run python manage.py check

# 3. テストの実行
# ここで test_*.py がすべて走り、1つでも失敗すれば止まります
echo -e "\n🧪 Step 3: Running tests..."
uv run python manage.py test

# post-checkout (ブランチ切り替え後に実行)
echo "uv sync" > .git/hooks/post-checkout
chmod +x .git/hooks/post-checkout

# post-merge (merge や pull の後に実行)
echo "uv sync" > .git/hooks/post-merge
chmod +x .git/hooks/post-merge

echo -e "\n${GREEN}=========================================${NC}"
echo -e "${GREEN}   ✅ All Checks Passed! Ready to Push!  ${NC}"
echo -e "${GREEN}=========================================${NC}"