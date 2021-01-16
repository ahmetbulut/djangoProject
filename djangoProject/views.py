from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def home(request):
    return render(request, "base.html")

def display_image(request):
    return render(request, "image.html")

def plot(request):
    # Typical Data Pre-processing
    # 1. Load dataset.
    # 2. Pre-process the dataset.
    # 2.1 Handle missing data
    # 2.2 Formatting (type conversions)
    # 3. Split dataset into training & test sets (80:20).
    X = [[0.1, 0.9], [0.2, 0.8], [1.0, 0.0], [0.5, 0.5],
         [0.3, 0.7], [0.7, 0.3], [0.8, 0.2], [0.9, 0.1],
         [0.0, 1.0], [0.6, 0.4]]
    y = [0, 0, 1, 0, 0, 1, 1, 1, 0, 1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50)

    # Typical ML Flow.
    # 1. Fit a model on training set.
    # 2. Make predictions on test set.
    clf = KNeighborsClassifier(2)
    clf.fit(X_train, y_train)
    y_score = clf.predict_proba(X_test)[:, 1]

    fig = px.scatter(
        X_test, x=0, y=1,
        color=y_score, color_continuous_scale='ylorrd',
        symbol=y_test, symbol_map={0: 'square-dot', 1: 'circle-dot'},
        #labels={'symbol': 'label', 'color': 'score of <br>first class'}
    )
    fig.update_traces(marker_size=12, marker_line_width=1.5)
    fig.update_layout(legend_orientation='h')
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def __plot(request):
    #df = pd.DataFrame()
    df = pd.read_csv("static/data.csv", header=0)
    df.info(verbose=True)
    #df['year'] = [1990, 2000, 2010, 2020]
    #df['lifeExp'] = [65, 70, 75, 50]
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Turkey')
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
