"""Plant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import loginPage,registerPage,logoutUser,HomeView,ProductDetailView,add_to_cart,OrderSummaryView,paymentPage,productPage
from django.conf import settings
from django.conf.urls.static import static
#from settings import staticfiles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='register'),
    path('login/',loginPage,name='login'),
    path('reg/',registerPage),
    path('logout/',logoutUser,name='logout'),
    path('home/',HomeView.as_view(),name='home'),
    path('product/<slug>',ProductDetailView.as_view(),name='product'),
    path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart'),
    path('order-summary/',OrderSummaryView.as_view(),name='order-summary'),
    path('payment/',paymentPage,name='payment'),
    path('products/',productPage,name='products'),


]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)