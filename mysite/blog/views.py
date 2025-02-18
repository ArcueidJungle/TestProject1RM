from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Получить все посты из базы
    return render(request, 'blog/post_list.html', {'posts': posts})