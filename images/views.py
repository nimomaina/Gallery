from django.shortcuts import render
from .models import *

# Create your views here.
def pictures(request):
    locations = Location.objects.all()
    pics = Picture.objects.all()
    return render(request, 'gallery.html' ,{"pics":pics, "locations":locations})


def search_category(request):
    location = Location.objects.all()
    category = Category.objects.all()
    if 'Category' in request.GET and request.GET["Category"]:
        category = request.GET.get("Category")
        searched_image = Picture.search_by_category(category)
        message = f"{category}"

        return render(request,'category/searched.html', {"message":message,"Category":searched_image})

    else:
        message = "You haven't searched for anything"
        return render(request,'category/searched.html',{"message":message})


def filter_location(request):
    locations = Location.objects.all()
    location = request.GET.get("location")

    searched_image = Picture.filter_by_location(location)
    message = f"{location}"

    return render(request,'category/location.html', {"message":message,"location":searched_image, "locations":locations})



