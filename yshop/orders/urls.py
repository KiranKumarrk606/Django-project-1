
from django.urls import path
from . import views


urlpatterns = [
   
    path('create/', views.create_order, name='create_order'),
    
   
    path('orders/history/', views.order_history, name='order_history'),
    
    
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    
   
    path('address/add/', views.add_address, name='add_address'),
    
    
    path('address/select/<int:order_id>/', views.select_address_for_order, name='select_address_for_order'),
    

    path('update/<int:order_id>/', views.update_order, name='update_order'),
    
    path('order/cancel/<int:order_id>', views.cancel_order, name='cancel_order')
]
