from django.shortcuts import render
from .models import News

# Create your views here.

#render позволяет отобразить определённый hhtp файл на странице
#request в ретёрне обязательный параметр
#второй параметр - путь к файлу который хотим отобразить
#путь начинается от папки templates
def home(request):
    news = [
        {
            'title': 'Наша первая статья',
            'text': 'Полный текст статьи',
            'date': '25 Сентября 2000 года',
            'autor': 'Роман'
        },
        {
            'title': 'Наша вторая статья',
            'text': 'Полный текст статьи',
            'date': '25 Сентября 2100 года'
        }
    ]

    data = {
        'news': News.objects.all(),
        'title': 'Главная страница'
    }
    return render (request, 'blog/home.html', data) 

#словарь можно создать внутри
def about(request):
    return render (request, 'blog/about.html', {'title': 'Страница контакты!!'}) 
