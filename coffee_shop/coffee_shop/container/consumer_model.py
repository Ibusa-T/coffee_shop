# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from cofee_shop.container.abstract_model import AbstractModel
class Consumer(models.Model):
    consumer_code = models.CharField(db_column='CONSUMER_CODE', primary_key=True)  # Field name made lowercase.
    consumer_name = models.CharField(db_column='CONSUMER_NAME', unique=True)  # Field name made lowercase.
    mail_address = models.CharField(db_column='MAIL_ADDRESS')  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER')  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'CONSUMER'
