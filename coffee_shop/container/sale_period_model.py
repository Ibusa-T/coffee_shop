# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from cofee_shop.container.models import AbstractModel
class SalePeriod(models.Model):
    sales_code = models.CharField(db_column='SALES_CODE', primary_key=True)  # Field name made lowercase.
    sale_title = models.TextField(db_column='SALE_TITLE')  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE')  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SALE_PERIOD'
