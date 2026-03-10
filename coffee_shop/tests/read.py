import sqlite3, os
db_path = 'db.sqlite3'
sql_path='../db/schema.sql'
try:
    with sqlite3.connect(db_path) as conn:
        with open(sql_path, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
    print('✅ DDLの反映が完了したぜ！設計通りのテーブルが作成されたぞ。')
except Exception as e:
    print(f'❌ エラー発生だ: {e}')

# run terminal
"""run sql"""
"""
uv run python -c "
>> import sqlite3, os
>> db_path = 'db.sqlite3'
>> sql_path = '../db/schema.sql'
>> try:
>>     with sqlite3.connect(db_path) as conn:
>>         with open(sql_path, 'r', encoding='utf-8') as f:
>>             conn.executescript(f.read())
>>     print('✅ DDLの反映が完了したぜ！設計通りのテーブルが作成されたぞ。')
>> except Exception as e:
>>     print(f'❌ エラー発生だ: {e}')
>> "
✅ DDLの反映が完了したぜ！設計通りのテーブルが作成されたぞ。
"""

