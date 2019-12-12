from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Product, DescribeProduct

# Create your views here.

def index(request):
    product = Product.objects.all()
    return render (request, 'onlineshop/index.html', {'products': product})

def input_product(request):
    return render(request, 'onlineshop/form.html',{})
    
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    dummy = DescribeProduct.objects.get(pk=product_id)
    list_desc = dummy.descipt.split(',')
    
    return render (request, 'onlineshop/detail.html', {'product': product, 'list_desc':list_desc})

def index_update(request):
    image_path          = request.POST['image_path']
    product_name        = request.POST['product_name']
    price               = request.POST['price']
    description         = request.POST['description']

    newproduct = Product(image_path=image_path, name=product_name, price=price)
    newproduct.save()
    newdesc = DescribeProduct(product=newproduct, descipt=description)
    newdesc.save()

    product = Product.objects.all()
    return render (request, 'onlineshop/index.html', {'products': product})
