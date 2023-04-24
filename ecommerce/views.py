from django.shortcuts import render
from .models import Product
from .form import ProductForm
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    homes = Product.objects.all()
    if request.method == "POST":
        forms = ProductForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponse("Product has been created successfully")
        else:
            forms = ProductForm()   
            homes = Product.objects.all()

    forms = ProductForm()
    context = {
        "homes": homes,
        "forms": forms
    }
    return render(request, "home_page.html", context)

def product_detail_page(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        "my_product": product
    }
    return render(request, "detail.html", context)