from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import *
from .forms import *
# Create your views here.

def hello(request):
    text= """<h1>Welcome to Kyrgyzstan!</h1>"""

    return HttpResponse(text)

def index(request):
    allNews = News.objects.order_by('-created_at')
    content = {'newsAll': allNews,
               'titleInHtml':'Список всех новостей'
               }

    return render(request,template_name="firstapp/index.html",context=content)

def get_category(request,category_id):
    news = News.objects.filter(category=category_id)
    category = Category.objects.get(pk = category_id)
    content = {'news': news,
               'category': category
               }
    return render(request, "firstapp/category.html", content)

def about(request):
    title = 'Страница о Нас! Рад вас приветствовать!'
    content = {
        'title': title,
    }
    return render(request, template_name="firstapp/about.html", context=content)

def contactus(request):
    return HttpResponse("<h2>Страница для связи с нами</h2>")

def view_news(request, news_id):
    # try:
    #     news_item = News.objects.get(pk = news_id)
    # except News.DoesNotExist:
    #     raise Http404(" Такой новости не существует!")

    news_item = get_object_or_404(News, pk=news_id)
    return render(request, "firstapp/view_news.html", {'news_item': news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)

        if form.is_valid():
            #print(form.cleaned_data)
            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            News.objects.create(**form.cleaned_data)
            return redirect('home')


    else:
        form = NewsForm()

    return render(request, 'firstapp/add_news.html', {"form": form})