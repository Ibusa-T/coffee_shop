# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# coffee_shop/container/consumer_model.py
from coffee_shop.container.abstract_model import AbstractModel

class Consumer(AbstractModel):
    consumer_code = AbstractModel.AbstractCharField(db_column='CONSUMER_CODE', primary_key=True, max_length=10)
    consumer_name = AbstractModel.AbstractCharField(db_column='CONSUMER_NAME', unique=True, max_length=100)
    mail_address = AbstractModel.AbstractCharField(db_column='MAIL_ADDRESS', max_length=255)
    gender = AbstractModel.AbstractCharField(db_column='GENDER', max_length=1)
    age = AbstractModel.AbstractIntegerField(db_column='AGE')
    address = AbstractModel.AbstractCharField(db_column='ADDRESS', max_length=255)

    class Meta:
        managed = True
        db_table = 'CONSUMER'