# from django.http import HttpResponse # this imports https response
from django.shortcuts import render # imports render


# Created funtion for each page
def homepage(request):
    # return HttpResponse("Hello Worl, This is your HOME") # Created the home page to request and respond )
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("This is about Page and it is about you") #Created about page
    return render(request, 'about.html')