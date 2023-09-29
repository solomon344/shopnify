from .models import User,Order,Product,cart as Cart
import json

def CreateCart(request):\

    data = json.loads(request.POST.get("items"))

    new_cart = Cart.objects.create(
                                   num_of_products=len(data.get("data")),
                                   quantity = len(data.get("data"))
                                   )
    new_cart.save()

    for i in data.get("data"):
        prod = Product.objects.get(pk=int(i['id']))
        new_cart.products.add(prod)
    
    order = Order.objects.create(cart=new_cart,by=request.user)
    order.save()

    

