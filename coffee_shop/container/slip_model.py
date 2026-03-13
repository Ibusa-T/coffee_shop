# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# coffee_shop/container/slip_model.py
from coffee_shop.container.abstract_model import AbstractModel
from .product_model import Product   # 外部キー参照用
from .consumer_model import Consumer # 外部キー参照用
from .sale_period_model import SalePeriod # 外部キー参照用

class Slip(AbstractModel):
    slip_code = AbstractModel.AbstractCharField(db_column='SLIP_CODE', primary_key=True, max_length=10)
    product_code = AbstractModel.AbstractForeignKey(Product, AbstractModel.PROTECT, db_column='PRODUCT_CODE')
    consumer_code = AbstractModel.AbstractForeignKey(Consumer, AbstractModel.PROTECT, db_column='CONSUMER_CODE')
    sales_code = AbstractModel.AbstractForeignKey(
        SalePeriod, 
        AbstractModel.PROTECT, 
        db_column='SALES_CODE', 
        blank=True, 
        null=True
    )
    order_date = AbstractModel.AbstractDateField(db_column='ORDER_DATE')
    price = AbstractModel.AbstractIntegerField(db_column='PRICE')
    quantity = AbstractModel.AbstractIntegerField(db_column='QUANTITY')

    class Meta:
        managed = True
        db_table = 'SLIP'