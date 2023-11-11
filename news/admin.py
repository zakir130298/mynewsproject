from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')  # поля, которые будут отображаться в списке
    list_filter = ('publish_date', 'author')  # фильтры по полям
    search_fields = ('title', 'content')  # поля, по которым можно искать

# или альтернативный способ без использования декоратора
# admin.site.register(Article, ArticleAdmin)
