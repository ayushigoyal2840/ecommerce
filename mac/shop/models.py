from django.db import models
import datetime

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="./shop/images", default="")

    def __str__(self):
        return self.product_name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    message=models.CharField(max_length=5000, default="")
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50, default="")
    desc=models.CharField(max_length=5000, default="")
    phone=models.CharField(max_length=10, default="")
    

    def __str__(self):
        return self.name

class Customer(models.Model):
    name1=models.CharField(max_length=200)
    name2=models.CharField(max_length=200)
    phone=models.CharField(max_length=10, default="")
    email=models.CharField(max_length=50, default="")
    password=models.CharField(max_length=8)
    
    def register(self):
        self.save()



    

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    def __str__(self):
        return self.name1

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=500 , default='')
    phone_number=models.CharField(max_length=10,  default='')
    date=models.DateField(default=datetime.datetime.today)


    def __str__(self):
        return self.customer.name1


    def placeOrder(self):
        self.save()


    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id)