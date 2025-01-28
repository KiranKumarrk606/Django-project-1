from django.urls import path
from . import views 


# path('', views.home, name='homepage')
urlpatterns =[
    path('', views.home, name='homepage'),
]