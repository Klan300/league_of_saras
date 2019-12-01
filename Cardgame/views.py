from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render ,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Deck, Playerscore
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages,add_message





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
def setting(request,name):
    topic = Deck.objects.get(deck_name=name)
    return render(request,'Cardgame/setting.html',{'topic':topic})


@login_required(login_url='/')
def playing(request,name):
    topic = Deck.objects.get(deck_name=name)
    total_card = list(topic.card_set.all())
    card_name = [i.card_name for i in total_card]
    print(card_name)
    return render(request,'Cardgame/playing.html',{'topic':topic,'cards':card_name})


@login_required(login_url='/')
def summary(request,name):
    topic = Deck.objects.get(deck_name=name)
    total_card = list(topic.card_set.all())
    card_name = [i.card_name for i in total_card]
    name = topic.deck_name
    storage = get_messages(request)
    for message in storage:
        time = message
        break
    return render(request, 'Cardgame/summary.html',{'topic':topic,'cards':card_name , 'name':name, 'time' : time })


@login_required(login_url='/')
def scoreboard(request,name,time):
    topic = Deck.objects.get(deck_name=name)
    player_score = Playerscore.objects.filter( deck = topic).filter(time = time).order_by('-score')
    for player in player_score:
        print(f'{player.deck.deck_name}    {player.time} {player.score} {player.user.username}')
    
    context = { 'player_score' : player_score }

    return render(request, 'Cardgame/scoreboard.html' , context) 


@login_required(login_url='/')
def save_score(request,name):
    print(request)
    score = int(request.POST['score'])
    time = int(request.POST['time'][:2])
    user = User.objects.get(username = request.POST['user'])
    deck = Deck.objects.get(deck_name = name)
    player = Playerscore(score = score ,time= time , user= user , deck = deck)
    player.save()
    messages.add_message(request,  messages.INFO, time )
    return HttpResponseRedirect(f'/playing/{name}/summary')
