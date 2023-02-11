import random
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    myRandomNumber = a + b
    html = "<html><body style='background:black'><h1 style='color:lightgreen'>Random numbers addition: " + str(myRandomNumber) + "</h1><img src='https://e1.pxfuel.com/desktop-wallpaper/502/274/desktop-wallpaper-retro-gamer-gamer-kid.jpg' alt='Hacker wallpaper'></body></html>"
    return HttpResponse(html)