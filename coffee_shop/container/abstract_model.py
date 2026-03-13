# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# coffee_shop/container/abstract_model.py
from django.db import models

class AbstractModel(models.Model):
    # フィールドクラスそのものをプロパティとして定義
    AbstractCharField = models.CharField
    AbstractIntegerField = models.IntegerField
    AbstractDateField = models.DateField
    AbstractTextField = models.TextField
    AbstractForeignKey = models.ForeignKey
    
    # 制約などの定数
    PROTECT = models.PROTECT

    class Meta:
        abstract = True
        managed = False