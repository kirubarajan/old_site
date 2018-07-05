import markdown2
from django.shortcuts import render
from blog.models import Post

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts })

def post(request, id):
    post = Post.objects.get(id=id)
    post.body = markdown2.markdown(post.body)
    return render(request, 'post.html', {'post': post })