from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(reauest):
    return render(reauest, 'products/products.html')