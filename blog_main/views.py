# modules
from django.shortcuts import render

#main work
def home(request):
    return render(request, 'home.html')