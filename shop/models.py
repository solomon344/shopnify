from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.

class Profile(models.Model):
    picture = models.ImageField(upload_to="media")
    country = models.CharField(max_length=100)
    account_balance = models.PositiveBigIntegerField()
    is_verified = models.BooleanField(default=False)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    

class Image(models.Model):
    img = models.ImageField(upload_to='media')

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    img = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class sellProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

class cart(models.Model):
    by = models.OneToOneField(User, on_delete=models.CASCADE)
    num_of_products = models.PositiveIntegerField()
    products = models.ForeignKey(sellProduct, on_delete=models.CASCADE)

class Order(models.Model):
    CHOICES = (
        ('P','pending'),
        ('D','delivered'),
        ('C','cancelled'),
    )
    code = models.CharField(default=str(uuid4()).split("-")[-1],max_length=25)
    status = models.CharField(max_length=200, choices=CHOICES)
    cart = models.OneToOneField(cart, on_delete=models.CASCADE)
   
    def __str__(self) -> str:
        return self.by.username

class Orderhistory(models.Model):
    for_user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.for_user.username

class CustomerReview(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.TextField()