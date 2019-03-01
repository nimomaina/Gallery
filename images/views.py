from django.shortcuts import render
from .models import *

# Create your views here.
def pictures(request):
    pics = Picture.objects.all()
    return render(request, 'gallery.html' ,{"pics":pics})
