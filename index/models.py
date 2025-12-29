from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=16, verbose_name='название категории')
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.category_name


class News(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Основной текст')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name='категория')
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
    def __str__(self):
        return self.title