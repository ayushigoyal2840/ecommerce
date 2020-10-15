

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="Contact"),
    path('tracker/', views.tracker, name="Trackingstatus"),
    path('search/', views.search, name="Search"),
    path('productview/', views.productView, name="Search"),
    path('checkout/', views.checkout, name="Checkout"),
    path('login/', views.login, name="Login"),
    path('shop/', views.shop, name="Shop"),
    path('cart/', views.cart, name="Cart"),
    path('checkout/', views.checkout, name="Checkout"),
    path('blog/', views.blog, name="Blog"),
    path('blog-details/', views.blog_details, name="Blog Details"),
    path('confirmation/', views.confirmation, name="Confirmation"),
    path('product_details/', views.product_details, name="product_details"),
    path('test/', views.test, name="test"),
    path('basic/', views.basic, name="basic"),
    # path('product/', views.product, name="product"),

        
    

]
