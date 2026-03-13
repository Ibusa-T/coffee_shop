# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from coffee_shop.container.abstract_model import AbstractModel

class Delivery(AbstractModel):
    delivery_code = AbstractModel.AbstractCharField(db_column='DELIVERY_CODE', primary_key=True, max_length=10)
    slip_code = AbstractModel.AbstractForeignKey('Slip', AbstractModel.PROTECT, db_column='SLIP_CODE')
    delivery_date = AbstractModel.AbstractDateField(db_column='DELIVERY_DATE')
    delivery_status = AbstractModel.AbstractCharField(db_column='DELIVERY_STATUS', max_length=20)
    finish_date = AbstractModel.AbstractDateField(db_column='FINISH_DATE', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DELIVERY'