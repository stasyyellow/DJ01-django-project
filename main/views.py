from django.http import HttpResponse

def data(request):
    return HttpResponse("<h1>Это страница data</h1>")

def test(request):
    return HttpResponse("<h1>Это страница test</h1>")
