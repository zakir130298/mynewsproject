from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)  # Заголовок статьи
    content = models.TextField()  # Содержание статьи
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Ссылка на автора статьи
    publish_date = models.DateTimeField(auto_now_add=True)  # Дата и время публикации статьи

    def __str__(self):
        return self.title