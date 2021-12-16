from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Discount

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products':products})
   

def new_view(request):
    return HttpResponse('New Products')


