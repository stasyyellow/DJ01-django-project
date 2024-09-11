from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Это мой первый проект на Django (DJ01)<br> "
                        "Вы можете перейти на страничку с данными {/data} или с тестированием {/test}.</h2>")

def data(request):
    return HttpResponse("<h3>Данные (data)</h3>")

def test(request):
    return HttpResponse("<h3>Тестирование (test)</h3>")