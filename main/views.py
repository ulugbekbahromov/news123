from django.shortcuts import render
import requests
from datetime import datetime

API = "a939ce1460a341a5b430205130cbead3"
# API = "cd0c6fe9d0034f87ae07b3f0f618bf65"


def home(request):
    # url = f"https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/03/19"
    # response = requests.get(url)
    # data = response.json()
    # selected = data["events"][2]
    #
    # context = {
    #     "selected": selected
    # }
    return render(request, "home.html")


def politico(request):
    url = f"https://newsapi.org/v2/top-headlines?sources=politico&apiKey={API}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    context = {
        "articles": articles
    }
    return render(request, "politico.html", context)


def bbc_news(request):
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    context = {
        "articles": articles
    }
    return render(request, "bbc_news.html", context)


def reuters(request):
    url = f"https://newsapi.org/v2/top-headlines?sources=reuters&apiKey={API}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    context = {
        "articles": articles
    }
    return render(request, "reuters.html", context)


def nbc_news(request):
    url = f"https://newsapi.org/v2/top-headlines?sources=nbc-news&apiKey={API}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    context = {
        "articles": articles
    }
    return render(request, "nbc_news.html", context)


def abc_news(request):
    url = f"https://newsapi.org/v2/top-headlines?sources=abc-news&apiKey={API}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    context = {
        "articles": articles
    }
    return render(request, "abc_news.html", context)


def cnn_news(request):
    url = f"https://newsapi.org/v2/top-headlines?sources=cnn&apiKey={API}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    context = {
        "articles": articles
    }
    return render(request, "cnn_news.html", context)


def tech_crunch(request):
    url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={API}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    context = {
        "articles": articles
    }
    return render(request, "tech_crunch.html", context)


def zen_today_history(request):
    now = datetime.now()
    day = now.day
    month = now.month
    url = f"https://today.zenquotes.io/api/{month}/{day}"
    response = requests.get(url)
    page = response.json()
    data = page["data"]["Events"]

    context = {
        "data": data,
        "now": now,
    }

    return render(request, "zen_history.html", context)


def zen_quotes(request):
    url = "https://zenquotes.io/api/quotes"
    page = requests.get(url)
    data = page.json()

    quote_topic = request.GET.get("keyword")
    if quote_topic:
        url = f"https://zenquotes.io/keywords/{quote_topic}"
        response = requests.get(url)
        data = response.json()

    context = {
        "data": data,
    }
    return render(request, "quotes.html", context)