from django.http import HttpResponse, Http404
from django.shortcuts import render ,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Deck





def index(request):
    return render(request, 'Cardgame/index.html')


def views_logout(request):
    logout(request)
    return redirect("index")


@login_required(login_url='/')
def home(request):
    deck = Deck.objects.all()
    context = {
        'deck_list' : deck
    }
    return render(request, 'Cardgame/home.html',context)


@login_required(login_url='/')
def setting(request):
    return render(request,'Cardgame/setting.html')


@login_required(login_url='/')
def playing(request,name):
    try:
        topic = Deck.objects.get(deck_name=name)
        total_card = list(topic.card_set.all())
        card_name = [i.card_name for i in total_card]

        return render(request,'Cardgame/playing.html',{'topic':topic,'cards':card_name},)

    except :
        return render(request,'Cardgame/404.html')


@login_required(login_url='/')
def summary(request,name):
    topic = Deck.objects.get(deck_name=name)
    total_card = list(topic.card_set.all())
    card_name = [i.card_name for i in total_card]

    return render(request, 'Cardgame/summary.html',{'topic':topic,'cards':card_name})




