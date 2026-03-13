from coffee_shop.repositories.abstractrepository import Baserepository
from coffee_shop.container.master_factory import MasterFactory

class ProductTypeRepository(Baserepository):
    
    def __init__(cls):
        cls.name = 'ProductType'
        cls.master_factory = MasterFactory

    @classmethod
    def insert(cls, **kwargs):
        # Factoryを使用してインスタンスを生成・保存
        model = cls.master_factory.create_for(cls.name, **kwargs)
        model.save()
    
    @classmethod
    def findByTypeName(cls,typeName):
        
        return cls.master_factory.get_model(cls.name).objects.get(typeName=typeName)
    
    @classmethod
    def findAll(cls):
        """引数なし。純粋に全件を返す"""
        return cls.master_factory.get_model(cls.name).objects.all()
    
    
    @classmethod 
    def delete(cls):
        cls.master_factory.get_model(cls.name).objects.all().delete()