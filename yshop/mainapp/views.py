from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.urls import reverse_lazy


from django.template import loader
from .models  import Product  


from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView




def home(request):
    home=''
    context={

    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))



def product_list(request):
    products = Product.objects.all() 
    context = {
        'prods' :products 
    }  
    
    template = loader.get_template('product.html') 
    return HttpResponse(template.render(context, request)) 
    
def product_details(request,id):
    product = Product.objects.get(id = id)
    context = {
        'prod' : product
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context,request))

# CRUD
# 1. C - create
class AddProduct(CreateView):
    model = Product 
    fields = [ 
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
    
    # 3. U - update
class EditProduct(UpdateView):
    model = Product
    template_name = 'editProduct.html'
    fields = '__all__'
    success_url = reverse_lazy('homepage')


# 4. D - delete

class DelProduct(DeleteView):
    model = Product
    fields = '__all__'
    template_name = 'delProduct.html'
    success_url = reverse_lazy('homepage')




