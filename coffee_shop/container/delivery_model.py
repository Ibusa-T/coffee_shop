# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from cofee_shop.container.abstract_model import AbstractModel

class Delivery(models.Model):
    delivery_code = models.CharField(db_column='DELIVERY_CODE', primary_key=True)  # Field name made lowercase.
    slip_code = models.ForeignKey('Slip', models.PROTECT, db_column='SLIP_CODE')  # Field name made lowercase.
    delivery_date = models.DateField(db_column='DELIVERY_DATE')  # Field name made lowercase.
    delivery_status = models.CharField(db_column='DELIVERY_STATUS')  # Field name made lowercase.
    finish_date = models.DateField(db_column='FINISH_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DELIVERY'