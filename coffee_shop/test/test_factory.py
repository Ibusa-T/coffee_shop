import factory
from factory import fuzzy
from datetime import date, timedelta
from coffee_shop.container.consumer_model import Consumer
from coffee_shop.container.delivery_model import Delivery
from coffee_shop.container.product_model import Product
from coffee_shop.container.product_type_model import ProductType
from coffee_shop.container.sales_info_model import SalesInfo
from coffee_shop.container.sale_period_model import SalePeriod
from coffee_shop.container.slip_model import Slip


"""
from coffee_shop.tests.test_factory import (
    ProductTypeFactory, ProductFactory, ConsumerFactory, 
    SalePeriodFactory, SlipFactory, DeliveryFactory, SalesInfoFactory
)
"""

# 1. 商品区分
class ProductTypeFactory(factory.django.DjangoModelFactory):
    #Metaは物理データ
    class Meta:
        model = ProductType
    
    type_code = factory.Sequence(lambda n: f"T{n:09d}")
    type_name = fuzzy.FuzzyChoice(["ブレンド", "シングルオリジン", "デカフェ", "限定アイテム"])


# 2.商品
# coffee_shop/tests/factory.py

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    product_code = factory.Sequence(lambda n: f"P{n:09d}")
    type_code = factory.SubFactory(ProductTypeFactory)

 

# 3. 顧客
class ConsumerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Consumer
    
    consumer_code = factory.Sequence(lambda n: f"C{n:09d}")
    consumer_name = factory.Faker("name", locale="ja_JP")
    mail_address = factory.Faker("email")
    gender = fuzzy.FuzzyChoice(["1", "2"])
    age = fuzzy.FuzzyInteger(18, 80)
    address = factory.Faker("address", locale="ja_JP")

# 4. セール期間
class SalePeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SalePeriod
    
    sales_code = factory.Sequence(lambda n: f"S{n:09d}")
    sale_title = "スプリング・ネブラ・フェア"
    start_date = date.today() - timedelta(days=7)
    end_date = date.today() + timedelta(days=7)

# 5. 伝票
class SlipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Slip
    
    slip_code = factory.Sequence(lambda n: f"SL{n:08d}")
    order_date = factory.Faker("date_this_year")
    
    product_code = factory.SubFactory(ProductFactory)
    consumer_code = factory.SubFactory(ConsumerFactory)
    sales_code = factory.SubFactory(SalePeriodFactory)
    
    # 商品の価格を自動で伝票に反映
    price = factory.SelfAttribute('product_code.price')
    quantity = fuzzy.FuzzyInteger(1, 5)

# 6. セール詳細
class SalesInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SalesInfo
    
    product_code = factory.SubFactory(ProductFactory)
    sales_code = factory.SubFactory(SalePeriodFactory)
    discount_rate = 20  # デフォルト 20% OFF

# 7. 配送
class DeliveryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Delivery
    
    slip_code = factory.SubFactory(SlipFactory)
    delivery_status = fuzzy.FuzzyChoice(['OUT_STOCK', 'NOW_DELIVERY', 'FINISH']) # 1:受付, 2:配送中, 3:完了
    finish_date = None # status が 3 の時に日付を入れる運用を想定