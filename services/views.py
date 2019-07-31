from django.shortcuts import render
# Create your views here.


def services(request):

    context = {
        'services' : services ,

    }

    return render(request , 'services/services.html' , context)