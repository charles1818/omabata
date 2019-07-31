from django.shortcuts import render
from product.models import Product , Category

# Create your views here.


def home(request):

    product = Product.objects.all()
    product_list = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'product' : product ,
        'product_list' : product_list ,
        'categories' : categories ,
    }

    return render(request , 'home/index.html' , context)