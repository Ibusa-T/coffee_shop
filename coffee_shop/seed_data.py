## coffee_shop/seed_data.py
import os
import sys
import django
import random
from datetime import date, timedelta

# 1. プロジェクトルートをパスに追加
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

# 2. Django設定の読み込み
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gemini_mart.settings')
django.setup()

from coffee_shop.repositories import repositories


# 既存データの全削除（重複防止）
print("Cleaning up old data...")
Delivery.objects.all().delete()
Slip.objects.all().delete()
SalesInfo.objects.all().delete()
SalePeriod.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()
Consumer.objects.all().delete()

# 1. マスターデータの作成
print("Generating Master Data...")

# 商品区分：コードと名前を明示的に指定
type_data = [
    {"code": "T01", "name": "ブレンド"},
    {"code": "T02", "name": "シングルオリジン"},
    {"code": "T03", "name": "デカフェ"},
]

types = [ProductTypeFactory(type_code=d["code"], type_name=d["name"]) for d in type_data]

# 商品ラインナップ：コードも重複しないように追加したぜ
product_list = [
    {"code": "P001", "name": "ダーク・ロースト・ネブラ", "price": 1800},
    {"code": "P002", "name": "エチオピア・サンライズ", "price": 2100},
    {"code": "P003", "name": "コロンビア・マイルド", "price": 1650},
    {"code": "P004", "name": "デカフェ・ナイト", "price": 1900},
    {"code": "P005", "name": "マンデリン・ゴールド", "price": 2300},
    {"code": "P006", "name": "グアテマラ・アンティグア", "price": 1750},
]
# 2. セール対象商品（SalesInfo）の紐付け設定
# どのセールにどの商品を、何%引きで入れるかのロジック用ハッシュだ
sales_assignment = [
    # デカフェ・ナイトセールはデカフェ商品（P004）をガッツリ値引き
    {"sale_code": "S001", "product_code": "P004", "discount": 25},
    
    # シングルオリジン紀行は高級豆（P002, P005）を対象に
    {"sale_code": "S002", "product_code": "P002", "discount": 15},
    {"sale_code": "S002", "product_code": "P005", "discount": 10},
    {"sale_code": "S002", "product_code": "P006", "discount": 15},
    
    # ブラックフライデーは全品一律セールのイメージ
    {"sale_code": "S003", "product_code": "P001", "discount": 30},
    {"sale_code": "S003", "product_code": "P003", "discount": 30},
    
    # ブレンド祭は定番のブレンド（P001）を
    {"sale_code": "S004", "product_code": "P001", "discount": 20},
]
products = []
for data in product_list:
    # ProductFactoryを呼ぶ際、モデルのフィールド名と完全に一致する引数だけを渡す
    p = ProductFactory(
        product_code=data["code"],
        product_name=data["name"],
        price=data["price"],
        type_code=random.choice(types)
    )
    products.append(p)

# 2. セール情報の作成
print("Generating Sale Periods...")
active_sale = SalePeriodFactory(
    sale_title="スプリング・ネブラ・フェア",
    start_date=date.today() - timedelta(days=7),
    end_date=date.today() + timedelta(days=7)
)

for p in random.sample(products, 3):
    SalesInfoFactory(product_code=p, sales_code=active_sale, discount_rate=20)

# 3. 注文と配送データの作成
print("Generating Transaction Data...")
consumers = ConsumerFactory.create_batch(10)

# --- ここで D001 から D051 までのリストを自動生成するぜ ---
delivery_code_list = [f"D{i:03d}" for i in range(1, 52)]
for i in range(50):  # 50件のデータを作成
    target_product = random.choice(products)
    
    # 注文 (Slip) の作成
    order = SlipFactory(
        product_code=target_product,
        consumer_code=random.choice(consumers),
        price=target_product.price,
        sales_code=random.choice([active_sale, None]),
        order_date=date.today() - timedelta(days=random.randint(0, 30))
    )
    
    # 配送 (Delivery) の作成
    status = random.choice(["1", "2", "3"])
    finish = (order.order_date + timedelta(days=random.randint(1, 3))) if status == "3" else None
    
    DeliveryFactory(
        delivery_code=delivery_code_list[i], # リストから順番にコードを割り当て
        slip_code=order,
        delivery_date=order.order_date + timedelta(days=1),
        delivery_status=status,
        finish_date=finish
    )

print(f"--- 完了！Delivery {delivery_code_list[0]} から {delivery_code_list[49]} まで使用したぜ ---")