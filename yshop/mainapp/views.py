from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.urls import reverse_lazy


from django.template import loader
from .models  import Product  # importing the products


# importing necessary generic class-based views for CRUD operations
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView



# Create your views here.
def home(request):
    home=''
    context={

    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))



def product_list(request):
    products = Product.objects.all() # colecting all the records in the DB of entity type 'products'
    # i.e this transaltes to the DQL :-> SELECT * FROM PRODUCT;
    context = {
        'prods' :products # hte key 'prods' will now be available to use in the django template design
    }  # context
    # context dictionary fro passing data fro rendering
    template = loader.get_template('product.html') # creating a template object from the designed template html
    return HttpResponse(template.render(context, request)) # creates a respones object after rendering
    # the returned response has the html of completed webpage including required data

    #view function for redering individual product page
def product_details(request,id):
    product = Product.objects.get(id = id)#select *from products where id = <parameter_id>
    context = {
        'prod' : product
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context,request))

# CRUD
# 1. C - create
class AddProduct(CreateView):
    model = Product # specifing the shema to insert record into
    fields = [ # specifying the fields to be generated in the form
        'name',
        'price',
        'desc',
        'stock',
        'pic'
        ]

    template_name = 'addproduct.html'
    success_url = reverse_lazy('homepage')  # redirect to the products page after adding product


    # 2. R - read
class ProductsView(ListView):
    model = Product
    template_name = 'productView.html'
    ordering = ['-id'] 
    # to sort in descending order

    # 3. U - update
class EditProduct(UpdateView):
    model = product_details
    template_name = 'editProduct.html'
    success_url = reverse_lazy('homepage')


# 4. D - delete

class DelProduct(DeleteView):
    model = Product
    template_name = 'delProduct.html'
    success_url = reverse_lazy('homepage')



# ### search results

# def searchView(request):
#     query = request.GET.get('search_text')
#     # fetch the query text from GET request


#     results = Product.objects.filter(name_icontain = query)
#     # collect the product objects matching the name


#     context = {
#         'item' : 'results'
#         'query' : 
#     }

