from django.shortcuts import render,redirect
from .models import Product,Image,Order
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
import time
from string import digits,ascii_letters
from random import choices
from django.http import JsonResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from .order_handler import CreateCart
from .auth_creds import email,token
from email.message import EmailMessage
import smtplib
import os


#from django_email_center.views.email_center import EmailCenter

# Create your views here.


def home(request):
    prod = Product.objects.all()
    context = {"products":prod}
    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')


def products(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request,'product.html',context)
    

def testimony(request):
    return render(request,'testimonial.html')



def why(request):
    return render(request,'why.html')


def review_product(request,id):
    single_prod = Product.objects.get(pk=id)
    context = {"product":single_prod}
    return render(request,'product_view.html', context)


def signup(request):
    if request.method.lower() =='post':

        first = request.POST.get("first")
        last = request.POST.get("last")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("confirm")
        username = f"{first}{''.join(choices([str(i) for i in digits],k=3))}"
        if password == password2:
            user = User.objects.create(
                first_name=first,
                last_name=last,
                email = email,
                password = password,
                username=username
                )
            user.save()
            messages.add_message(request,200,"successfully registered")
            return redirect('login')
        else:
            messages.add_message(request,403,"please correct your password")
            return redirect("register")
    else:
        return render(request,'signup.html')


def Login(request):
    if request.user.is_authenticated:
         return redirect("home")
          
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            get_user = User.objects.filter(email=email)[0]
            user = authenticate(request,username=get_user.username,password=password)
            if user is not None:
                login(request,user)
                messages.add_message(request,200,"login successful!")
                return redirect("home")
            else:
                messages.add_message(request,403,"There is no user with this email")
                return redirect("login")
        else:
            return render(request,"login.html")
       
        
def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
    else:
        return Http404("Page not found")

def chekout(request,*args,**kwargs):
    return render(request,'order.html')

@login_required(redirect_field_name="next",login_url="login")
def profile(request):
    return render(request,'profile.html',context={'user':request.user})

@login_required(redirect_field_name="next",login_url="login")
def pay(request):
    return render(request,'pay.html')

def getSingleProduct(request,id):
    product = Product.objects.filter(id=id)
    img = Image.objects.filter(pk = id)
    
    p1 = product.values()[0]
    p1["img"]=img[0].img.url
    print(img[0].img.url)
    return JsonResponse(p1,safe=False)

@login_required(redirect_field_name="next",login_url='login')
def allert(request):
    return render(request,'allert.html')

def Cart_Order(request):
    CreateCart(request=request)
    return redirect('/')



@receiver(post_save,sender=Order)
def send_order_mail(sender,instance,created,**kwargs):
    
    if created:

        subject = "Order placed"
        message_body = f"Thank you for ordering at Shopnify, your orders will be delivered soon. \n \n Your order Code is {instance.code} \n \n your order status is {instance.status} \n \n \n \n The Shopnify Team"
        
        
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = instance.by.email 
        msg.set_content(message_body)
        print(os.environ.get("EMAIL_PASSWORD"))
        # for key,item in os.environ.items():
        #     print(key,item)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email,os.environ.get("EMAIL_PASSWORD")) 
            smtp.send_message(msg)