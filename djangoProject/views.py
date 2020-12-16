from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world")

def today(request):
    now = datetime.now()
    html = "<html><body>" + str(now) + "</body></html>"
    return HttpResponse(html)

def today_proper(request):
    now = datetime.now()
    return render(request, "today.html", {"now": now})

#the first parameter is request, i.e., HttpRequest
def display(request):
    books_list = [
        {"title": "Tesla Inventor of the Modern", "publisher": "Norton", "year": "2018"},
        {"title": "Kubeflow for Machine Learning", "publisher": "OReilly", "year": "2020"},
        {"title": "Africa Diaries", "publisher": "Adventure Press", "year": "2006"},
        {"title": "How to Be Rich", "publisher": "Penguin Books", "year": "2011"}
    ]

    flag = True
    return render(request, "display.html", {"books_list": books_list,
                                            "flag": flag
                                            })
