from django.shortcuts import render
from django.http import HttpResponse
def index (request):
    return render(request, 'shop/index.html')
def about (request):
    return render(request, 'shop/about.html')
def contact (request):
    return HttpResponse("We are contact")
def tracker (request):
    return HttpResponse("We are tracker")
def search (request):
    return render(request, 'shop/search.html')
def productView (request):
    return HttpResponse("We are view")
def checkout (request):
    return HttpResponse("We are out")
