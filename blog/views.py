import markdown2
from django.shortcuts import render
from blog.models import Post

def blog(request):
    colors = dict({'Programming': 'primary', 'Coffee': 'info', 'Personal': 'success'})
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'colors': colors})

def post(request, id):
    post = Post.objects.get(id=id)
    post.body = markdown2.markdown(post.body)
    return render(request, 'post.html', {'post': post, 'id': id})