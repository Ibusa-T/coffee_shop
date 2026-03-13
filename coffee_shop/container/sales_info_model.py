# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# coffee_shop/container/sales_info_model.py
from coffee_shop.container.abstract_model import AbstractModel
from .product_model import Product  # 外部キー参照用

class SalesInfo(AbstractModel):
    # 文字列での指定、またはインポートしたクラスリテラルでの指定どちらも可能です
    sales_code = AbstractModel.AbstractForeignKey('SalePeriod', AbstractModel.PROTECT, db_column='SALES_CODE')
    product_code = AbstractModel.AbstractForeignKey(Product, AbstractModel.PROTECT, db_column='PRODUCT_CODE')
    discount_rate = AbstractModel.AbstractIntegerField(db_column='DISCOUNT_RATE')

    class Meta:
        managed = True
        db_table = 'SALES_INFO'