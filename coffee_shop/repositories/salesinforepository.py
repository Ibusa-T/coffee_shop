from coffee_shop.repositories.abstractrepository import Baserepository

class SalesInfoRepository(Baserepository):
    @classmethod
    def insert(cls, **kwargs):
        # Factoryを使用してインスタンスを生成・保存
        model = cls.master_factory.create_for('SalesInfo', **kwargs)
        model.save()

    
    @classmethod
    def findAll(cls):
        """引数なし。純粋に全件を返す"""
        return cls.master_factory.get_model('SalesInfo').objects.all()
    
    
    @classmethod 
    def delete(cls):
        cls.master_factory.get_model('SalesInfo').objects.all().delete()
        