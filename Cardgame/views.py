
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import logout



def index(request):
    return render(request, 'Cardgame/index.html')
    
def views_logout(request):
    logout(request)
    return redirect("index")



def playing(request):
    return render(request,'Cardgame/playing.html')