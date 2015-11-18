# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=14, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    author = models.CharField(max_length=128, blank=True, null=True)
    frmt = models.CharField(max_length=9, blank=True, null=True)
    publisher = models.CharField(max_length=64, blank=True, null=True)
    yr = models.IntegerField(blank=True, null=True)
    sbj = models.CharField(max_length=64, blank=True, null=True)
    keywords = models.CharField(max_length=128, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    copies = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Book'


class Customer(models.Model):
    login_name = models.CharField(primary_key=True, max_length=16, blank=True, null=True)
    pwd = models.CharField(max_length=8, blank=True, null=True)
    surname = models.CharField(max_length=16, blank=True, null=True)
    given_name = models.CharField(max_length=64, blank=True, null=True)
    creditcard = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    phoneno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customer'


class Opinion(models.Model):
    customer = models.CharField(primary_key=True, max_length=16, blank=True, null=True)
    book = models.CharField(primary_key=True, max_length=14, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    txt = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Opinion'
        unique_together = (('customer', 'book'),)


class Ord(models.Model):
    oid = models.IntegerField(primary_key=True, blank=True, null=True)
    customer = models.CharField(max_length=16, blank=True, null=True)
    timestmp = models.DateTimeField(blank=True, null=True)
    stat = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ord'


class Rate(models.Model):
    rater = models.CharField(primary_key=True, max_length=16, blank=True, null=True)
    ratee = models.CharField(primary_key=True, max_length=16, blank=True, null=True)
    book = models.CharField(primary_key=True, max_length=14, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rate'
        unique_together = (('rater', 'ratee', 'book'),)


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ordbook(models.Model):
    oid = models.IntegerField(primary_key=True, blank=True, null=True)
    book = models.CharField(primary_key=True, max_length=14, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordBook'
        unique_together = (('oid', 'book'),)
