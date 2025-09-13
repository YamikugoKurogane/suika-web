from django.shortcuts import render
from .models import *


# Create your views here.
from .models import Servicio, BlogPost

def home(request):
    servicios = Servicio.objects.all().order_by('orden')
    blogs = BlogPost.objects.all().order_by('orden')
    return render(request, 'index.html', {'servicios': servicios, 'blogs': blogs})
