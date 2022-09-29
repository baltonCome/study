from multiprocessing import context
from django.shortcuts import render
from .models import Room


'''rooms = [
    { 'id': 1, 'name': 'Pythoners' },
    { 'id': 2, 'name': 'Javanators' },
    { 'id': 3, 'name': 'PHPillers' },
    { 'id': 4, 'name': 'Basers' },
    { 'id': 5, 'name': 'Laracaster' },
]'''

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = { 'rooms' : rooms }
    return render(request, 'base/home.html', context)


def room(request, key):
    room = Room.objects.get(id=key)
    context = {'room': room}
    return render(request, 'base/room.html', context)