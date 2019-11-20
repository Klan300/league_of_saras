from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playing/', views.playing, name='playing'),
    path('home/', views.home, name='home'),
    path('logout/',views.views_logout, name='logout'),
]
