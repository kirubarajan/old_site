import markdown2
from django.shortcuts import render
from blog.models import Post, Category

def category(request, category):
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'categories': categories, 'select': True})

def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'categories': categories, 'select': False})

def post(request, id):
    post = Post.objects.get(id=id)
    post.body = markdown2.markdown(post.body)
    return render(request, 'post.html', {'post': post})