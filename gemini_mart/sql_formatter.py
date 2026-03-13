
import logging
import sqlparse
from django.utils.termcolors import make_style

class SQLFormatter(logging.Formatter):
    def format(self, record):
        # SQL文を取得
        sql = record.getMessage()
        
        # 1. 予約語を大文字に変換し、綺麗に整形 (reindent=True)
        formatted_sql = sqlparse.format(
            sql, 
            keyword_case='upper', 
            reindent=True, 
            indent_width=4
        )
        
        # 2. コンソール出力用の色付け設定（予約語を太字の青にする例）
        # Djangoの標準機能を使って色を付けます
        bold_blue = make_style(fg='blue', opts=('bold',))
        
        # 簡易的な色付け（sqlparse自体に色付け機能もありますが、ターミナル制御文字を扱います）
        # ここでは予約語を大文字化した上で、全体を読みやすく整形しています
        
        record.msg = formatted_sql
        return super().format(record)