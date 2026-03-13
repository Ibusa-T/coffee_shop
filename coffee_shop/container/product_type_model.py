# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# coffee_shop/container/product_type_model.py
from coffee_shop.container.abstract_model import AbstractModel

class ProductType(AbstractModel):
    # AbstractModel.AbstractCharField を使用
    type_code = AbstractModel.AbstractCharField(db_column='TYPE_CODE', primary_key=True, max_length=10)
    type_name = AbstractModel.AbstractCharField(db_column='TYPE_NAME', max_length=100)

    class Meta:
        managed = True
        db_table = 'PRODUCT_TYPE'