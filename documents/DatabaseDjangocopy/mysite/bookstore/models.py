from django.db import models

# Create your models here.

class Customer(models.Model):
    login_name = models.CharField(max_length = 16, primary_key = True)
    pwd = models.CharField(max_length = 8)
    surname = models.CharField(max_length = 16)
    given_name = models.CharField(max_length = 64)
    creditcard = models.CharField(max_length = 16)
    address = models.CharField(max_length = 128)
    phoneno = models.IntegerField()
    
class Book(models.Model):
    frmt_types = (("hardcover", "Hardcover"), ("softcover", "Softcover"))
    
    isbn = models.CharField(max_length = 14, primary_key = True)
    title = models.CharField(max_length = 128)
    author = models.CharField(max_length = 128)
    frmt = models.CharField(max_length = 9, choices=frmt_types)
    publisher = models.CharField(max_length = 64)
    yr = models.IntegerField() ## Supposed to check that it's > 0
    sbj = models.CharField(max_length = 64)
    keywords = models.CharField(max_length = 128)
    price = models.FloatField()
    copies = models.IntegerField()
    
class Ord(models.Model):
    ## Implicit OID auto-generated
    customer = models.ForeignKey(Customer)
    timestmp = models.DateTimeField()
    stat = models.CharField(max_length = 16)

class ordBook(models.Model):
    #TODO: Figure out how to make PRIMARY KEY (oid, book)
    oid = models.ForeignKey(Ord)
    book = models.ForeignKey(Book)
    qty = models.IntegerField()
    
class Opinion(models.Model):
    #TODO: Figure out how to make PRIMARY KEY (customer, book)
    customer = models.ForeignKey(Customer)
    book = models.ForeignKey(Book)
    score = models.IntegerField() #need to check that it's 0 < x < 10
    txt = models.CharField(max_length = 256)
    
    