from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('category/<int:pk>/', views.category_page, name='category_page'),
    path('news/<int:pk>/', views.news_page, name='news_page'),
    path('register/', views.register, name='register'),

    path('favorites/', views.favorites_page, name='favorites'),
    path('favorites/add/<int:pk>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:pk>/', views.remove_from_favorites, name='remove_from_favorites'),
]
