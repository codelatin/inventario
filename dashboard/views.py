from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Producto
# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, "dashboard/index.html")

@login_required
def personal(request):
    return render(request, "dashboard/personal.html")

@login_required
def producto(request):
    return render(request, "dashboard/producto.html")

@login_required
def pedido(request):
    return render(request, "dashboard/pedido.html")

