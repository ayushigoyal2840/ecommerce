from django.contrib import admin

from . models import Product, Contact, Customer, Order

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Order)

