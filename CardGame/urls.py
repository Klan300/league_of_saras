from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playing/', views.playing, name='playing'),
    path('setting/', views.setting, name='setting'),
    path('setting2/', views.setting2, name='setting2'),
    # path('/scoreboard/', views.scoreboard, name='scoreboard')
]