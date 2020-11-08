from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Contact, Customer, Order
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from shop.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class Basic(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])

        return redirect('basic')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        # products=Product.objects.all()
        # print(products)
        # n=len(products)
        # nSlides=n//4 + ceil((n/4)-(n//4))
        allProds = []
        catprods = Product.objects.values('category', 'id', )
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])

        # params={'no_of_slides':nSlides , 'range': range(1,nSlides) , 'product':products}
        # allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
        params = {'allProds': allProds}
        return render(request, 'shop/basic.html', params)


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        phone = request.POST.get('phone', '')
        contact = Contact(message=message, name=name, email=email, desc=desc, phone=phone)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/productView.html', {'product': product[0]})


class Login(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                # request.session['email'] = customer.email
                return redirect('index')
            else:
                error = "Email or Password invalid !!!"
        else:
            error = "Email or Password invalid !!!"
        print(customer)
        print(email, password)
        return render(request, 'shop/login.html', {'error1': error})

    def get(self, request):
        return render(request, 'shop/login.html')


def logout(request):
    request.session.clear()
    return redirect("index")


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone_number=phone,
                          quantity=cart.get(str(product.id))
                          )
            order.save()
            request.session['cart'] = {}
        return redirect("index")


class Orders(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer=request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'shop/orders.html', {'orders':orders})


def shop(request):
    # print('you are= ', request.session.get('email'))
    return render(request, 'shop/shop.html')


def login2(request):
    return render(request, 'shop/login2.html')


class Cart(View):
    def get(self, request):
        ids = (list(request.session.get('cart')))
        products = Product.get_products_by_id(ids)
        # print(list(request.session.get('cart').keys()))
        # print(products)
        return render(request, 'shop/cart.html', {'products': products})


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


# def basic(request):

def product(request):
    return render(request, 'shop/product.html')


def validatecustomer(customer):
    error = None
    if not customer.name1:
        error = "First name required!!!"
    elif not customer.phone:
        error = "Phone number required !!!"
    elif len(customer.phone) < 10:
        error = "Phone number must be 10 digits!!!"

    elif len(customer.password) < 6:
        error = "Password must be 6 digits, characters or special symbol!!!"

    elif len(customer.email) < 6:
        error = "Enter valid email!!!"
    elif customer.isExists():
        error = "Email Already Registered!!!"

    return error


def registeruser(request):
    name1 = request.POST.get('name1')
    name2 = request.POST.get('name2')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    password = request.POST.get('password')
    value = {
        'name1': name1,
        'name2': name2,
        'phone': phone,
        'email': email
    }
    customer = Customer(name1=name1, name2=name2, phone=phone, email=email, password=password)
    error = validatecustomer(customer)

    if not error:
        customer.password = make_password(customer.password)
        customer.register()
        return render(request, 'shop/login.html')
    else:
        data = {
            'error1': error,
            'values': value
        }
        return render(request, 'shop/signup.html', data)


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        return render(request, 'shop/signup.html')
    else:
        return registeruser(request)
