from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader
from .models  import Product  # importing the products

# Create your views here.

def home(request):
    products = Product.objects.all() # colecting all the records in the DB of entity type 'products'
    # i.e this transaltes to the DQL :-> SELECT * FROM PRODUCT;
    context = {
        'prods' :products # hte key 'prods' will now be available to use in the django template design
    }  # context
    context = {} # context dictionary fro passing data fro rendering
    template = loader.get_template('home.html') # creating a template object from the designed template html
    return HttpResponse(template.render(context, request)) # creates a respones object after rendering
    # the returned response has the html of completed webpage including required data