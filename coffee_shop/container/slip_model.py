# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from cofee_shop.container.abstract_model import AbstractModel
class Slip(models.Model):
    slip_code = models.CharField(db_column='SLIP_CODE', primary_key=True)  # Field name made lowercase.
    product_code = models.ForeignKey(Product, models.PROTECT, db_column='PRODUCT_CODE')  # Field name made lowercase.
    consumer_code = models.ForeignKey(Consumer, models.PROTECT, db_column='CONSUMER_CODE')  # Field name made lowercase.
    sales_code = models.ForeignKey(SalePeriod, models.PROTECT, db_column='SALES_CODE', blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateField(db_column='ORDER_DATE')  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SLIP'
