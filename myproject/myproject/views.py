from django.http import HttpResponse # this imports https response



# Created funtion for each page
def homepage(request):
    return HttpResponse("Hello Worl, This is your HOME") # Created the home page to request and respond )

def about(request):
    return HttpResponse("This is about Page and it is about you") #Created about page