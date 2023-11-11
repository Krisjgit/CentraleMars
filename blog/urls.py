#  Copyright Joubi Kris (c) 2023.
#

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('person/<int:pk>/', views.person_detail, name='person_detail'),
    path('person-list/', views.person_list, name = 'person_list'),
    path('room-list/', views.room_list, name = 'room_list'),
    #path('/admin/auth/user/<int:pk>/',  auth_views.LoginView.as_view(), name='admin_user')
]