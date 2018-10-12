import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
from django.shortcuts import render
from blog.models import Post, Category

def category(request, category):
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'categories': categories, 'select': True})

def blog(request):
    sections = list()
    categories = Category.objects.all()
    for category in categories:
        posts = Post.objects.filter(category=category)
        sections.append({"posts": posts, "category": category})
    sections.reverse()
    return render(request, 'blog.html', {'sections': sections, 'categories': categories, 'select': False})

def post(request, id):
    post = Post.objects.get(id=id)
    post.body = markdown.markdown(post.body, extensions=[GithubFlavoredMarkdownExtension()])
    return render(request, 'post.html', {'post': post})