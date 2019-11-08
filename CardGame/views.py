from flask import json 
from django.http import HttpResponse
from django.shortcuts import render 
from Cardgame.models import Deck
# from django.utils import simplejson

def index(request):
    return HttpResponse("Hello, world. You're at the sarasss.")
    
def playing(request):
    topic = Deck.objects.get(pk=1)
    total_card = list(topic.card_set.all())
    card_name = [i.card_name for i in total_card]
    print(card_name)
    # card_name = simplejson.dumps(card_name)
    # card_name = json.dumps(card_name)
    return render(request,'Cardgame/newplayingpage.html',{'topic':topic,'cards':card_name},
    )