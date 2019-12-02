from django.http import HttpResponse, Http404
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
    try:
        from random import shuffle
        topic = Deck.objects.get(deck_name=name)
        total_card = list(topic.card_set.all())
        card_name = [i.card_name for i in total_card]
        shuffle(card_name)

        return render(request,'Cardgame/playing.html',{'topic':topic,'cards':card_name},)

    except :
        return render(request,'Cardgame/404.html')


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
    player_score_45 = Playerscore.objects.filter( deck = topic).filter(time = 45).order_by('-score')
    name_45 = []
    score_45 = []
    player_score_60 = Playerscore.objects.filter(deck = topic).filter(time = 60).order_by('-score')
    name_60 = []
    score_60 = []
    player_score_90 = Playerscore.objects.filter(deck = topic).filter(time = 90).order_by('-score')
    name_90 = []
    score_90 = []
    for player in player_score_45:
        name_45.append(player.user.username)
        score_45.append(str(player.score))
    for player in player_score_60:
        name_60.append(player.user.username)
        score_60.append(str(player.score))    
    for player in player_score_90:
        name_90.append(player.user.username)
        score_90.append(str(player.score))    
    context = { 'score45' : score_45 ,'name45':name_45,'score60':score_60,
    'name60':name_60,'score90':score_90,'name90':name_90,'topic':topic}
    print(name_45)
    print(score_45)
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
