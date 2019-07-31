from django.shortcuts import render
from .models import AboutUs , Why_Choose_Us , Director

# Create your views here.


def aboutus_list(request):
    about = AboutUs.objects.last()
    why_choose_us = Why_Choose_Us.objects.last()
    director = Director.objects.last()

    context = {
        'about' : about , 
        'why_choose_us' : why_choose_us ,
        'director' : director
    }

    return render(request , 'aboutus/about.html' , context)