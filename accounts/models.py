from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import reverse
# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=20,null=True)
    email=models.EmailField()
    date_created=models.DateTimeField(auto_now_add=True,null=True)





# Create your models here.
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.user_name


class Buyer_info(models.Model):
    phone_number = models.CharField(max_length=10)
    buyer_address = models.CharField(max_length=100)
    buyer_city = models.CharField(max_length=100)
    buyer = models.ForeignKey(Buyer, null=True, on_delete=models.SET_NULL)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.seller_name


class Seller_info(models.Model):
    seller_phone = models.CharField(max_length=10)
    seller_address = models.CharField(max_length=100)
    seller_city = models.CharField(max_length=100)
    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)


class Shipping_company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Shipping_company_info(models.Model):
    company_phone = models.CharField(max_length=10)
    company_address = models.CharField(max_length=100)
    company_city = models.CharField(max_length=100)
    shipping_company = models.ForeignKey(Shipping_company, null=True, on_delete=models.SET_NULL)


class Product(models.Model):
    CATEGORY = (
        ('Annuals', 'Annuals'),
        ('Bulbs', 'Bulbs'),
        ('Herbs', 'Herbs'),
        ('Climbers', 'Climbers'),
        ('Ferns', 'Ferns'),
        ('fruit', 'fruit'),
        ('conifers', 'conifers')
    )
    category_name = models.CharField(max_length=100, choices=CATEGORY)
    stock_amount = models.FloatField()
    product_price = models.FloatField()
    shipping_company = models.ForeignKey(Shipping_company, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="images", default="")
    product_description = models.TextField(blank=True,null=True)
    slug=models.SlugField()

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product',kwargs={'slug':self.slug})
    def get_add_to_card_url(self):
        return reverse('add-to-cart', kwargs={'slug': self.slug})


#class Product_info(models.Model):


class Order_product(models.Model):
    # order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=2)
    ordered=models.BooleanField(default=False)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=1)

    def get_total_item_price(self):
        return self.quantity*self.product.product_price



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    track_id = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    #order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=150, null=True, choices=STATUS)
    total_price = models.FloatField(null=True)
    transaction_id = models.CharField(max_length=100)
    shipping_company = models.ForeignKey(Shipping_company, null=True, on_delete=models.SET_NULL)
    ordered=models.BooleanField(default=False)
    products=models.ManyToManyField(Order_product)

    def __str__(self):
        return str(self.user.username)





    def __str__(self):
        return str(self.id)

    def get_total(self):
        total=0
        for prod in self.products.all():
            total+=prod.get_total_item_price()
        return total



class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    product_info = models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name


class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    User = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)


class Shopping_basket(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)

class Basket_product(models.Model):
    basket = models.ForeignKey(Shopping_basket, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)





