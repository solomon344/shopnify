from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('products',views.products,name="product"),
    path('testimonials',views.testimony,name="testimony"),
    path('whyus',views.why,name="why"),
    path('product/<str:id>',views.review_product,name="product_review"),
    path('register',views.signup,name="register"),
    path('login',views.Login,name="login"),
    path('logout',views.Logout,name="logout"),
    path('checkout',views.chekout,name="checkout"),
    path('profile',views.profile,name="profile"),
    path('pay',views.pay,name="pay"),
    path('getproduct/<str:id>',views.getSingleProduct,name="singleProduct")
]