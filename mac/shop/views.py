from django.shortcuts import render
from django.http import HttpResponse
# from .models import Product
def index (request):
    return render(request, 'shop/index.html')
def about (request):
    return render(request, 'shop/about.html')
def contact (request):
    return render(request, 'shop/contact.html')
def tracker (request):
    return HttpResponse("We are tracker")
def search (request):
    return render(request, 'shop/search.html')
def productView (request):
    return render(request, 'shop/productView.html')
def checkout (request):
    return render(request, 'shop/checkout.html')
def login(request):
    return render(request, 'shop/login.html')
def shop(request):
    return render(request, 'shop/shop.html')
def cart(request):
    return render(request, 'shop/cart.html')
def blog(request):
    return render(request, 'shop/blog.html')
def blog_details(request):
    return render(request, 'shop/blog-details.html')
def confirmation(request):
    return render(request, 'shop/confirmation.html')
def product_details(request):
    return render(request, 'shop/product_details.html')
def test(request):
    return render(request, 'shop/test.html')
def basic(request):
    return render(request, 'shop/basic.html')


