from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)

admin.site.register(Buyer)
admin.site.register(Buyer_info)
admin.site.register(Seller)
admin.site.register(Seller_info)
admin.site.register(Shipping_company)
admin.site.register(Shipping_company_info)
admin.site.register(Product)
#admin.site.register(Product_info)
admin.site.register(Order)
admin.site.register(Bank)
admin.site.register(Transaction)
admin.site.register(Shopping_basket)
admin.site.register(Order_product)
admin.site.register(Basket_product)