from django.db import models
from django.contrib.auth.models import User
from string import digits, ascii_letters
from random import choices
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
    
#class cart(models.Model):
#     num_of_products = models.PositiveIntegerField()
#     products = models.ManyToManyField(to=Product)
    

    

class cart(models.Model):
    num_of_products = models.PositiveIntegerField()
    products = models.ManyToManyField(to=Product)
    quantity = models.PositiveIntegerField(default=0)

class Order(models.Model):
   
    code = models.CharField(default= ''.join(choices(digits+ascii_letters,k=10)),max_length=25)
    status = models.CharField(default="Pending",max_length=200,)
    cart = models.OneToOneField(cart, on_delete=models.CASCADE)
    by = models.ForeignKey(User,on_delete=models.CASCADE)
   
    def __str__(self) -> str:
        return self.by.username


class CustomerReview(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.TextField()