
from django.http import HttpResponse
from django.shortcuts import render
from .models import Deck


def index(request):
    return HttpResponse("Hello, world. You're at the sarasss.")
    
def playing(request):
    return render(request,'Cardgame/playing.html')

def home(request):
    deck = Deck.objects.all()[0]
    print(deck)
    content = {
        deck : deck,
    }
    return render(request, 'Cardgame/home.html',context = content)
