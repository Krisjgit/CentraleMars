

from django.shortcuts import render, get_object_or_404
from .models import Room
from django.utils import timezone


def home(request):
    rooms = Room.objects.all()
    return render(request, 'blog/home.html', {'rooms':rooms})


def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'blog/room_detail.html', {'room':room})