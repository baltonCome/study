from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = { 'rooms' : rooms }
    return render(request, 'base/home.html', context)

def room(request, key):
    room = Room.objects.get(id=key)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, key):
    room = Room.objects.get(id = key)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, key):
    room = Room.objects.get(id = key)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', { 'obj':room })