# news/views.py
from django.shortcuts import render
from .models import Article


# views.py в вашем приложении

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход пользователя в систему сразу после регистрации
            return redirect('article_list')  # Перенаправление на страницу со списком статей
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def article_list(request):
    articles = Article.objects.all().order_by('-publish_date')
    return render(request, 'news/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})
