# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# coffee_shop/container/product_model.py
from coffee_shop.container.abstract_model import AbstractModel

class Product(AbstractModel):
    product_code = AbstractModel.AbstractCharField(db_column='PRODUCT_CODE', primary_key=True, max_length=10)
    product_name = AbstractModel.AbstractCharField(db_column='PRODUCT_NAME', max_length=100)
    # 外部キーも AbstractModel 経由で定義
    type_code = AbstractModel.AbstractForeignKey(
        'ProductType', 
        AbstractModel.PROTECT, 
        db_column='TYPE_CODE'
    )
    price = AbstractModel.AbstractIntegerField(db_column='PRICE')

    class Meta:
        managed = True
        db_table = 'PRODUCT'