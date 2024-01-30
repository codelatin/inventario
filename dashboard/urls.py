from django.urls import path
from . import views

urlpatterns =[
    path('dashboard', views.index, name='index'),
    path('personal/', views.personal, name='personal'),
    path('producto/', views.producto, name='productos'),
    path('pedido/', views.pedido, name='pedido'),


]