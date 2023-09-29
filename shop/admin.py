from django.contrib import admin
from .models import (Product,Profile,Order,Image,cart)
# Register your models here.

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(cart)