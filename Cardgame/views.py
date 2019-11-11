
from django.http import HttpResponse
from django.shortcuts import render 


def index(request):
    return HttpResponse("Hello, world. You're at the sarasss.")
    
def playing(request):
    return render(request,'Cardgame/playing.html')