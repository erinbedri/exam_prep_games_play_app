from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'Room.html')
