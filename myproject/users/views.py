from django.shortcuts import render

def user(request):
    return render(request, 'users/register.html')

# Create your views here.
