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

# --- Git Hooks の自動セットアップ ---
# ファイルが存在しない場合のみ作成し、実行権限を付与します

if [ ! -f .git/hooks/post-checkout ]; then
    echo "🔧 Setting up post-checkout hook..."
    echo -e "#!/bin/sh\nuv sync" > .git/hooks/post-checkout
    chmod +x .git/hooks/post-checkout
fi

if [ ! -f .git/hooks/post-merge ]; then
    echo "🔧 Setting up post-merge hook..."
    echo -e "#!/bin/sh\nuv sync" > .git/hooks/post-merge
    chmod +x .git/hooks/post-merge
fi
echo -e "\n${GREEN}=========================================${NC}"
echo -e "${GREEN}   ✅ All Checks Passed! Ready to Push!  ${NC}"
echo -e "${GREEN}=========================================${NC}"