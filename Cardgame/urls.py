from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.index, name='index'),
    path('playing/<str:name>', views.playing, name='playing'),
    path('logout/',views.views_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('setting/<str:name>', views.setting, name='setting'),
    path('playing/<str:name>/summary', views.summary, name="summary"),
    path('scoreboard/<str:name>/<int:time>', views.scoreboard, name='scoreboard'),
    path('save/<str:name>',views.save_score,name='save')
]
