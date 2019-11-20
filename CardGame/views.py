from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import logout
from .models import Deck



def index(request):
    return render(request, 'Cardgame/index.html')
    
def views_logout(request):
    logout(request)
    return redirect("index")


def playing(request):
    topic = Deck.objects.all()[0]
    total_card = list(topic.card_set.all())
    card_name = [i.card_name for i in total_card]
    print(card_name)
    # card_name = simplejson.dumps(card_name)
    # card_name = json.dumps(card_name)
    return render(request,'Cardgame/playing.html',{'topic':topic,'cards':card_name},
    )


def home(request):
    deck = Deck.objects.all()
    context = {
        'deck_list' : deck
    }
    return render(request, 'Cardgame/home.html',context)
def setting(request):
    return render(request,'Cardgame/setting.html')
    
