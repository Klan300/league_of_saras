from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playing/', views.playing, name='playing'),
    path('logout/',views.views_logout, name='logout'),
    path('setting/', views.setting, name='setting'),
    # path('/scoreboard/', views.scoreboard, name='scoreboard')
]
