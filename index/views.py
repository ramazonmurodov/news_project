from django.shortcuts import render, get_object_or_404
from .models import NewsCategory, News
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Favorite


# Главная страница
def home_page(request):
    categories = NewsCategory.objects.all()
    news = News.objects.all().order_by('-added_date')
    context = {
        'categories': categories,
        'news': news,
        'current_category': None,  #
    }
    return render(request, 'home.html', context)


# Страница категории
def category_page(request, pk):
    categories = NewsCategory.objects.all()
    category = get_object_or_404(NewsCategory, id=pk)
    news = News.objects.filter(category=category).order_by('-added_date')
    context = {
        'categories': categories,
        'news': news,
        'current_category': category,
    }
    return render(request, 'home.html', context)


# Страница отдельной новости
def news_page(request, pk):
    news_item = get_object_or_404(News, id=pk)
    context = {'news_item': news_item}
    return render(request, 'news.html', context)


# Функция для регистрации пользователя
def register(request):
    from django.contrib.auth.forms import UserCreationForm
    from django.shortcuts import render, redirect

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def add_to_favorites(request, pk):
    news_item = get_object_or_404(News, id=pk)
    Favorite.objects.get_or_create(
        user=request.user,
        news=news_item
    )
    return redirect('news_page', pk=pk)


@login_required
def remove_from_favorites(request, pk):
    news_item = get_object_or_404(News, id=pk)
    Favorite.objects.filter(
        user=request.user,
        news=news_item
    ).delete()
    return redirect('news_page', pk=pk)


@login_required
def favorites_page(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})
