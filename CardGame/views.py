
from django.http import HttpResponse
from django.shortcuts import render 


def index(request):
    return HttpResponse("Hello, world. You're at the sarasss.")
    
def playing(request):
    return render(request,'Cardgame/playing.html')

def setting(request):
    return render(request,'Cardgame/setting.html')

def setting2(request):
    return render(request,'Cardgame/setting2.html')
