from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import plotly.express as px
import plotly.io as pio
import pandas as pd

def home(request):
    return render(request, "base.html")

def plot(request):
    df = pd.DataFrame()
    df['year'] = [1990, 2000, 2010, 2020]
    df['lifeExp'] = [65, 70, 75, 50]
    fig = px.bar(df, x="year", y="lifeExp", title='Life expectancy in Turkey')
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

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
