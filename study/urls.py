from django.http import HttpResponse
from django.contrib import admin
from django.urls import path


def home(request):
    return HttpResponse('Home Page')

def room(request):
    return HttpResponse('Rooms')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/', room)
]
