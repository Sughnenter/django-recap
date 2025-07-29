from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello world, Locked in.")

def about(request):
    return HttpResponse("My about page")