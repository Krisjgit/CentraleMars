#  Copyright Joubi Kris (c) 2023.
#

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
]