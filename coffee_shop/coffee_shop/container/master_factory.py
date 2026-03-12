#本番用ファクトリ
import factory

from coffee_shop.container.models import (
    Consumer, Delivery, Product, ProductType, 
    SalesInfo, SalePeriod, Slip
)


class MasterFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        abstract = True
    # インポートしたクラスリテラルをそのままリストに入れる
    MODELS = [Consumer, Delivery, Product, ProductType, SalesInfo, SalePeriod, Slip]
    # リストから「クラス名: クラスオブジェクト」のハッシュテーブルを自動生成！ 
    REGISTRY = {model.__name__: model for model in MODELS}
    
    @classmethod
    def get_model(cls, model_name):
        """インスタンスを作らず、モデルクラスそのものを返すぜ"""
        target_model = cls.REGISTRY.get(model_name)
        
        if not target_model:
            raise ValueError(f"Model {model_name} は登録されてません")
        return target_model
    
    
    @classmethod         #テーブル    項目
    def create_for(cls, model_name, **kwargs):
        
        target_model = cls.REGISTRY.get(model_name)
        if not target_model:
            raise ValueError(f"Model {model_name} は登録されてません")
        
        # 内部で一時的にMetaを書き換えて生成する
        cls._meta.model = target_model
        return super().build(**kwargs)
    
    