from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playing/', views.playing, name='playing')
    # path('scoreboard/', views.scoreboard, name='scoreboard')
]