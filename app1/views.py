from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import *

def home(request):
    products = Product.objects.all().order_by("-date")
    context = {
        "products": products
    }


    return render(request,"app1/home.html",context=context)


def product_detail(request,id):
    get_product = Product.objects.get(id=id)
    context = {
        "product": get_product
    }
    return render(request,"app1/product_detail.html",context=context)
