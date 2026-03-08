# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Delivery(models.Model):
    delivery_code = models.CharField(db_column='DELIVERY_CODE', primary_key=True)  # Field name made lowercase.
    slip_code = models.ForeignKey('Slip', models.PROTECT, db_column='SLIP_CODE')  # Field name made lowercase.
    delivery_date = models.DateField(db_column='DELIVERY_DATE')  # Field name made lowercase.
    delivery_status = models.CharField(db_column='DELIVERY_STATUS')  # Field name made lowercase.
    finish_date = models.DateField(db_column='FINISH_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DELIVERY'


class Product(models.Model):
    product_code = models.CharField(db_column='PRODUCT_CODE', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME')  # Field name made lowercase.
    type_code = models.ForeignKey('ProductType', models.PROTECT, db_column='TYPE_CODE')  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PRODUCT'


class ProductType(models.Model):
    type_code = models.CharField(db_column='TYPE_CODE', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='TYPE_NAME')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PRODUCT_TYPE'


class SalesInfo(models.Model):
    sales_code = models.ForeignKey('SalePeriod', models.PROTECT, db_column='SALES_CODE')  # Field name made lowercase.
    product_code = models.ForeignKey(Product, models.PROTECT, db_column='PRODUCT_CODE')  # Field name made lowercase.
    discount_rate = models.IntegerField(db_column='DISCOUNT_RATE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SALES_INFO'


class SalePeriod(models.Model):
    sales_code = models.CharField(db_column='SALES_CODE', primary_key=True)  # Field name made lowercase.
    sale_title = models.TextField(db_column='SALE_TITLE')  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE')  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SALE_PERIOD'


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
