from django.db import models

# Create your models here.
class category(models.Model):
    category_img = models.FileField(upload_to="category_images/",max_length=250,null=True,default=None)
    category_title = models.CharField(max_length=50)

class Grocery(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

class Product(models.Model):
    product_img = models.FileField(upload_to="product_images/",max_length=250,null=True,default=None)
    product_title = models.CharField(max_length=50)
    product_price = models.CharField(max_length=50)

