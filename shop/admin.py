from django.contrib import admin
from .models import (Product,Profile,sellProduct,Order,Orderhistory,Image)
# Register your models here.

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(sellProduct)
admin.site.register(Order)
admin.site.register(Orderhistory)