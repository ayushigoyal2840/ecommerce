

from django.urls import path
from . import views
from .views import View
from .views import Basic , Login , Cart , CheckOut , Orders

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="Contact"),
    path('tracker/', views.tracker, name="Trackingstatus"),
    path('search/', views.search, name="Search"),
    path('products/<int:myid>', views.productView, name="Product View"),
    # path('checkout/', views.checkout, name="Checkout"),
    path('login/', Login.as_view(), name="Login"),
    path('logout/', views.logout, name="Logout"),
    path('shop/', views.shop, name="Shop"),
    path('cart/', Cart.as_view(), name="Cart"),
    path('checkout/', CheckOut.as_view(), name="Checkout"),
    path('orders/', Orders.as_view(), name="Checkout"),
    path('blog/', views.blog, name="Blog"),
    path('blog-details/', views.blog_details, name="Blog Details"),
    path('confirmation/', views.confirmation, name="Confirmation"),
    path('product_details/', views.product_details, name="product_details"),
    path('test/', views.test, name="test"),
    path('basic/', Basic.as_view(), name="basic"),
    path('product/', views.product, name="product"),
    path('signup/', views.signup, name="signup"),
    path('login2/', views.login2, name="login2"),

        
    

]
