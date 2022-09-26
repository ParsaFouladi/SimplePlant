from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Product,Order,Order_product
from django.views.generic import ListView,DetailView,View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Sum, Max, Min




# Create your views here.
def registerPage(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account is created successfully " + user + "!")
    context={'form':form,"login":"0"}
    return render(request, './account.html', context)

def loginPage(request):


    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'User or Password is incorrect!')

    context = {"login":"1"}
    return render(request, './account.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


class HomeView(ListView):
    model = Product
    template_name = 'index.html'

'''
def homePage(request):

    context={'items':Product.objects.all()}
    #return HttpResponse("<h1>Hello World</h1>") #string of HTML code
    return render(request,"./index.html",context)
'''

class ProductDetailView(DetailView):
    model = Product
    template_name = "product-details.html"

def add_to_cart(request,slug):
    product=get_object_or_404(Product,slug=slug)
    order_item,created=Order_product.objects.get_or_create(product=product,user=request.user,ordered=False)
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
        #check if the order item is in the order
        if order.products.filter(product__slug=product.slug):
            order_item.quantity+=1
            order_item.save()
        else:
            order.products.add(order_item)
    else:
        order=Order.objects.create(user=request.user)
        order.products.add(order_item)

    return redirect("product",slug=slug)

class OrderSummaryView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        try:
            order=Order.objects.get(user=self.request.user,ordered=False)
            context={'object':order}
            return render(self.request, 'cart.html',context)
        except:
            messages.error(self.request,"You don't have an active order")
            return redirect("/home")

def paymentPage(request):
    context = {}
    return render(request, './payment.html', context)

def productPage(request):
    context = {}
    return render(request, './products.html', context)
