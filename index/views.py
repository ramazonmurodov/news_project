from django.shortcuts import render
from .models import NewsCategory, News


# Create your views here.
# Главная страница
def home_page(request):
    # Достаем данные из БД












    categories = NewsCategory.objects.all()
    news = News.objects.all()
    # Передаем данные из фронт
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'home.html', context)


# Страница с категорией
def category_page(request, pk):
    # Достаем данные из БД
    category = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(category=category)
    # Предаем данные из фронт
    context = {
        'category': category,
        'news': news,
    }
    return render(request, 'category.html', context)


# страница с вестями
def news_page(request, pk):
    # Достаем данные из БД
    news_item = News.objects.get(id=pk)
    # Передаем данные из фронт
    context = {'news_item': news_item}
    return render(request, 'news.html', context)
