from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playing/<str:name>', views.playing, name='playing'),
    path('logout/',views.views_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('setting/', views.setting, name='setting'),
    path('playing/<str:name>/summary', views.summary, name="summary")
    # path('scoreboard/', views.scoreboard, name='scoreboard')
]
